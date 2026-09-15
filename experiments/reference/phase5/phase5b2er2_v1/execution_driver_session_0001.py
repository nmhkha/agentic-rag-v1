"""Execute one user-authorized frozen recovery session; never resume automatically."""
import json
import os
from pathlib import Path
import shlex
import sys

ROOT = Path('/home/minhkha/kk/TTTN/legal-agentic-rag')
sys.path.insert(0, str(ROOT / 'scripts'))
import phase5_evaluation_quota_recovery_v1 as q
from phase5_common import exclusive_json, exclusive_bytes, file_hash, digest
from llm_client import client_from_env

ANCHOR = '8e74013cab6df4564dd33f17cd6901e968152b631d82bbc0c523e680c4a999ee'
SESSION = 'phase5b2er2_session_0001'
DEST = ROOT / q.RECOVERY_ROOT
AUTH = Path('/home/minhkha/.codex/attachments/e9100a3e-b760-4dee-9f96-90b79ffa7c5f/pasted-text.txt')

def inventory():
    values = {}
    for directory, dirs, files in os.walk(ROOT, followlinks=False):
        dirs[:] = sorted(d for d in dirs if Path(directory) / d != DEST)
        for name in sorted(files):
            path = Path(directory) / name
            relative = str(path.relative_to(ROOT))
            values[relative] = {'sha256': file_hash(path)}
            if path.is_symlink():
                values[relative]['symlink'] = os.readlink(path)
        for name in dirs:
            path = Path(directory) / name
            if path.is_symlink():
                values[str(path.relative_to(ROOT))] = {'symlink': os.readlink(path)}
    return values

q.require(not DEST.exists(), 'Session 0001 requires absent recovery root; no automatic resume')
q.require(file_hash(ROOT / q.MANIFEST) == ANCHOR, 'manifest trust anchor mismatch')
m = q.read_json(ROOT / q.MANIFEST)
expected = dict(status='PASS', completed_v0_judgment_count=64, eligible_slot_count=29,
                tests_run=31, max_recovery_attempts_per_slot=3, recovery_attempts_created=0)
q.require(all(m.get(k) == v for k, v in expected.items()), 'recovery manifest gate failed')
test_result = q.read_json(Path('/tmp/phase5b2er1-tests.json'))
q.require(test_result['status'] == 'PASS' and test_result['tests_run'] == 31
          and test_result['failures'] == test_result['errors'] == 0
          and test_result['source_hashes'] == m['infrastructure_hashes'], 'fresh frozen tests gate failed')
eligible = [s for s in m['slots'] if s['completion'] == 'ELIGIBLE_EXHAUSTED_429']
plan = [dict(variant_id=s['variant_id'], query_id=s['query_id']) for s in eligible]
q.require(plan == m['recovery_order'] == m['eligible_slots'] == [
    dict(variant_id=q.VARIANTS[a], query_id=i) for a in q.VARIANTS for i in q.EXPECTED[a]],
    'exact eligible ordered universe mismatch')
for line in (ROOT / '.env').read_text().splitlines():
    name, separator, value = line.removeprefix('export ').partition('=')
    name = name.strip()
    if separator and name in ('RAG_LLM_MODEL', 'RAG_LLM_BASE_URL', 'RAG_LLM_API_KEY') and not os.getenv(name):
        parts = shlex.split(value, comments=True)
        if len(parts) == 1:
            os.environ[name] = parts[0]
transport = q.QuotaTransport(client_from_env(), m['frozen_endpoint']['base_url_canonical_sha256'],
                             real_requests_authorized=True)
# Hash-only inventory; quality fields never enter session scheduling/reporting.
before = inventory()
started = q.utc()
print(json.dumps({'event': 'frozen_verification_started', 'session_id': SESSION}), flush=True)
scheduler = q.make_reviewed_session(ROOT, ANCHOR, transport=transport,
    external_review_reference='User Phase 5B.2-E-R2 authorization; attachment SHA-256 ' + file_hash(AUTH))
exclusive_bytes(DEST / 'execution_driver_session_0001.py', Path(__file__).read_bytes())
exclusive_json(DEST / 'session_0001_binding.json', dict(
    session_id=SESSION, start_utc=started, manifest_trust_anchor=ANCHOR,
    authorization_sha256=file_hash(AUTH), protocol=q.VERSION,
    production_hashes=m['production_hashes'], gold_hash=m['gold_hash'],
    evaluator_hashes=m['frozen_evaluator_hashes'], endpoint=m['frozen_endpoint'],
    model=m['frozen_model'], temperature=0, timeout_seconds=120,
    ordered_recovery_plan=plan, starting_completed_count=64,
    existing_v0_judgments_locked=64, tests=test_result,
    before_inventory=before, execution_driver_sha256=file_hash(Path(__file__))))

submissions = []
active = {}
def audit(event, args):
    if event == 'urllib.Request':
        submissions.append(dict(active))
sys.addaudithook(audit)
original_worker = scheduler.worker
def observed_worker(slot, path, *, resume=False):
    active.clear()
    active.update(variant_id=slot['variant_id'], query_id=slot['query_id'],
                  recovery_attempt_index=int(path.name))
    print(json.dumps(dict(event='attempt_started', **active)), flush=True)
    outcome = original_worker(slot, path, resume=resume)
    print(json.dumps(dict(event='attempt_returned', **active,
        status=outcome['final_recovery_status'], parse_status=outcome['parse_status'],
        http_status=outcome['http_status'])), flush=True)
    return outcome
scheduler.worker = observed_worker

# The user's execution stop condition is stricter than the library's terminal
# aggregate: stop immediately after persisting any third invalid parser receipt.
# No parser, transport, attempt budget, ledger format, or scheduling order changes.
class ExhaustedSession(BaseException):
    pass
original_finish = scheduler.ledger.finish
def stop_on_exhaustion(path, index, outcome, now):
    receipt = original_finish(path, index, outcome, now)
    if receipt['slot_status_after_attempt'] == 'RECOVERY_EXHAUSTED' and receipt['final_recovery_status'] != 'QUOTA_BLOCKED':
        raise ExhaustedSession()
    return receipt
scheduler.ledger.finish = stop_on_exhaustion

error_type = None
try:
    result = scheduler.run()  # Exactly one invocation; no sleeps or resume loop.
except ExhaustedSession:
    result = dict(status='RECOVERY_EXHAUSTED', slot=[active['variant_id'], active['query_id']],
                  attempt=active['recovery_attempt_index'])
except BaseException as exc:
    error_type = type(exc).__name__
    result = dict(status='FAIL', error_type=error_type)
provider_end = q.utc()
print(json.dumps({'event': 'session_requests_stopped', 'result': result,
                  'provider_http_submissions': len(submissions)}), flush=True)

successes, failed, remaining, attempts = [], [], [], []
for slot in eligible:
    history, last = scheduler.ledger.state(slot)
    for path, start, receipt in history:
        entry = dict(variant_id=slot['variant_id'], query_id=slot['query_id'],
                     recovery_attempt_index=start['recovery_attempt_index'],
                     v0_attempt_count=start['v0_attempt_count'],
                     receipt_path=str((path / 'receipt.json').relative_to(ROOT)) if receipt else None,
                     status=receipt['final_recovery_status'] if receipt else 'AMBIGUOUS',
                     http_status=receipt.get('http_status') if receipt else None)
        attempts.append(entry)
        if entry['status'] != 'VALID_JUDGMENT':
            failed.append(entry)
    identity = dict(variant_id=slot['variant_id'], query_id=slot['query_id'])
    (successes if last and last['parse_status'] == 'valid' else remaining).append(identity)
stops = [dict(path=str(p.relative_to(ROOT)), sha256=file_hash(p), **q.read_json(p))
         for p in scheduler.ledger.blocks()]
status = {'VALID_JUDGMENT': 'COMPLETE', 'TRANSPORT_ERROR': 'TRANSPORT_BLOCKED'}.get(result['status'], result['status'])
q.require(status != 'COMPLETE' or len(successes) == 29, 'incomplete recovery cannot be COMPLETE')

print(json.dumps({'event': 'post_session_integrity_started'}), flush=True)
integrity_error = None
try:
    q.verify_manifest(ROOT, ANCHOR)
except Exception as exc:
    integrity_error = type(exc).__name__
after = inventory()
changed = [p for p in before if after.get(p) != before[p]]
added = sorted(set(after) - set(before))
integrity = 'PASS' if not integrity_error and not changed and not added else 'FAIL'
ended = q.utc()
integrity_path = DEST / 'session_0001_integrity.json'
exclusive_json(integrity_path, dict(status=integrity, checked_at_utc=ended,
    manifest_trust_anchor=ANCHOR, frozen_verifier='PASS' if not integrity_error else 'FAIL',
    verifier_error_type=integrity_error, before_inventory_sha256=digest(before),
    after_inventory_sha256=digest(after), checked_preexisting_entries=len(before),
    changed_or_missing_preexisting_paths=changed, added_paths_outside_recovery_root=added,
    allowed_additive_root=q.RECOVERY_ROOT))
quota_info = None
if stops:
    blocking = failed[-1]
    receipt = q.read_json(ROOT / blocking['receipt_path'])
    quota_info = dict(blocking_variant=blocking['variant_id'], blocking_query=blocking['query_id'],
        recovery_attempt_index=blocking['recovery_attempt_index'], http_status=receipt['http_status'],
        provider_metadata=receipt['quota_metadata'], quota_stop=stops[-1],
        global_not_before_utc=q.utc(stops[-1]['not_before_epoch']) if stops[-1]['not_before_epoch'] else None)
report = dict(session_id=SESSION, status=status, start_utc=started, provider_session_end_utc=provider_end,
    end_utc=ended, manifest_trust_anchor=ANCHOR, manifest_verification='PASS',
    starting_completed_count=64, successful_recovered_slots=successes,
    recovered_v1_judgment_count=len(successes), failed_attempts=failed, attempts=attempts,
    recovery_attempts_used=len(attempts), ending_completed_count=64+len(successes),
    remaining_ordered_slots=remaining, remaining_count=len(remaining),
    provider_http_submissions=len(submissions), http_submission_slots=submissions,
    http_429_events=sum(a['http_status'] == 429 for a in attempts), quota_stop_information=quota_info,
    production_calls=0, existing_valid_judgments_rejudged=0, protected_v0_judgments=64,
    integrity_result=integrity, integrity_artifact=str(integrity_path.relative_to(ROOT)),
    frozen_scheduler_result=result, final_analysis_executed=False,
    ready_for_final_analysis=status == 'COMPLETE' and integrity == 'PASS',
    automatic_resume=False, stop='STOP; await review')
exclusive_json(DEST / (SESSION + '_report.json'), report)
print(json.dumps(report), flush=True)
sys.exit(0 if integrity == 'PASS' and status != 'FAIL' else 1)
