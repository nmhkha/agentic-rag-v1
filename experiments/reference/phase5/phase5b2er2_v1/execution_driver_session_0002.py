"""One externally reviewed Session 2, using the unchanged frozen implementation."""
import json
import os
from pathlib import Path
import shlex
import sys
import time

ROOT = Path('/home/minhkha/kk/TTTN/legal-agentic-rag')
sys.path.insert(0, str(ROOT / 'scripts'))
import phase5_evaluation_quota_recovery_v1 as q
from phase5_common import exclusive_json, exclusive_bytes, file_hash, digest
from llm_client import client_from_env

ANCHOR = '8e74013cab6df4564dd33f17cd6901e968152b631d82bbc0c523e680c4a999ee'
DEST = ROOT / q.RECOVERY_ROOT
AUTH = Path('/home/minhkha/.codex/attachments/d546f76e-4524-45a6-8488-b68bbb9887cd/pasted-text.txt')
SESSION = 'phase5b2er2_session_0002'
REVIEW = 'External user review authorizing Phase 5B.2-E-R2 Session 2; attachment SHA-256 ' + file_hash(AUTH)

def inventory():
    values = {}
    for directory, dirs, files in os.walk(ROOT, followlinks=False):
        dirs.sort()
        for name in sorted(files):
            path = Path(directory) / name
            if path == DEST / 'session.lock':
                continue
            values[str(path.relative_to(ROOT))] = file_hash(path)
    return values

def state(ledger, slots):
    valid, remaining, attempts = [], [], []
    for slot in slots:
        history, last = ledger.state(slot)
        if slot['completion'] == 'LOCKED_VALID_V0':
            q.require(not history, 'protected v0 slot has recovery attempts')
            continue
        for path, start, receipt in history:
            q.require(receipt is not None, 'unfinished prior request: AMBIGUOUS; STOP')
            wire = q.read_json(path / 'wire_response.json')
            q.require(wire['started_record_hash'] == file_hash(path / 'started.json')
                      and wire['prompt_sha256'] == slot['prompt_sha256'], 'wire request binding mismatch')
            if wire['transport_status'] == 'completed':
                q.require(digest(wire['raw']) == wire['response_hash'], 'wire response hash mismatch')
            q.require(start['protocol'] == q.VERSION
                      and start['variant_id'] == slot['variant_id']
                      and start['query_id'] == slot['query_id']
                      and start['production_output_hash'] == slot['production_output_hash']
                      and start['gold_query_binding_hash'] == slot['gold_query_binding_hash']
                      and start['v0_attempt_count'] == 3, 'attempt provenance mismatch')
            q.require((receipt['parse_status'] == 'valid') ==
                      (receipt['final_recovery_status'] == 'VALID_JUDGMENT' and bool(receipt.get('result_hash'))),
                      'inconsistent completion receipt')
            attempts.append(dict(alias=slot['alias'], variant_id=slot['variant_id'], query_id=slot['query_id'],
                recovery_attempt_index=int(path.name), status=receipt['final_recovery_status'],
                http_status=receipt['http_status'], started_at=start['started_at'], ended_at=receipt['ended_at'],
                receipt_path=str((path / 'receipt.json').relative_to(ROOT))))
        identity = dict(variant_id=slot['variant_id'], query_id=slot['query_id'])
        (valid if last and last['parse_status'] == 'valid' else remaining).append(identity)
    actual = {str(p.relative_to(ROOT)) for p in DEST.glob('*/*/*/started.json')}
    expected = {a['receipt_path'].removesuffix('receipt.json') + 'started.json' for a in attempts}
    q.require(actual == expected, 'unplanned recovery attempt')
    return valid, remaining, attempts

print(json.dumps(dict(event='preflight_started', session_id=SESSION)), flush=True)
m = q.verify_manifest(ROOT, ANCHOR)
q.require(m['recovery_protocol_version'] == q.VERSION, 'protocol mismatch')
q.require(not (DEST / 'session_0002_binding.json').exists(), 'Session 2 already started; no automatic resume')
ledger = q.RecoveryLedger(DEST, m['slots'], ANCHOR)
prior_valid, remaining, prior_attempts = state(ledger, m['slots'])
plan = m['recovery_order']
expected_remaining = [dict(variant_id=q.VARIANTS[a], query_id=i) for a, ids in
    [('A1', ['eval024', 'eval025', 'eval026']), ('A2', q.EXPECTED['A2'])] for i in ids]
q.require(sum(s['completion'] == 'LOCKED_VALID_V0' for s in m['slots']) == 64
          and len(prior_valid) == 14 and len(prior_attempts) == 15
          and prior_valid == plan[:14] and remaining == plan[14:] == expected_remaining,
          'MISMATCH: prior ledger is not the authorized 78/93 state')
q.require(all(a['recovery_attempt_index'] == 1 for a in prior_attempts)
          and all(a['status'] == 'VALID_JUDGMENT' for a in prior_attempts[:14]), 'prior attempt mismatch')
blocking = prior_attempts[-1]
q.require(blocking['alias'] == 'A1' and blocking['query_id'] == 'eval024'
          and blocking['status'] == 'QUOTA_BLOCKED' and blocking['http_status'] == 429,
          'previous quota-stop slot mismatch')
blocks = ledger.blocks()
q.require(blocks == [DEST / 'quota_stop_0001.json'], 'previous quota-stop count mismatch')
stop_path = blocks[0]
stop = q.read_json(stop_path)
stop_hash = file_hash(stop_path)
q.require(stop_hash == '457ccaf7d7591a7b57a3de3dfa54eeb360181f4b2537c280e1c11295e02eef45', 'previous quota-stop hash mismatch')
receipt = q.read_json(ROOT / blocking['receipt_path'])
q.require(digest(receipt) == stop['receipt_sha256']
          and receipt['quota_metadata']['provider_status'] == 'RESOURCE_EXHAUSTED'
          and stop['retry_delay_seconds'] == 9.656832983
          and q.utc(stop['not_before_epoch']) == '2026-09-09T08:17:00.234707+00:00',
          'previous quota barrier binding mismatch')
q.require(all(a['started_at'] <= blocking['started_at'] for a in prior_attempts)
          and all(a['ended_at'] <= blocking['started_at'] for a in prior_attempts[:-1]),
          'request order mismatch or request after prior 429')
q.require(time.time() >= stop['not_before_epoch'], 'NOT_BEFORE_BLOCKED')
old_binding = q.read_json(DEST / 'session_0001_binding.json')
q.require(file_hash(DEST / 'execution_driver_session_0001.py') == old_binding['execution_driver_sha256']
          and old_binding['manifest_trust_anchor'] == ANCHOR
          and q.read_json(DEST / 'session_0001_integrity.json')['status'] == 'PASS', 'prior session binding mismatch')
for line in (ROOT / '.env').read_text().splitlines():
    name, sep, value = line.removeprefix('export ').partition('=')
    name = name.strip()
    if sep and name in ('RAG_LLM_MODEL', 'RAG_LLM_BASE_URL', 'RAG_LLM_API_KEY') and not os.getenv(name):
        parts = shlex.split(value, comments=True)
        if len(parts) == 1:
            os.environ[name] = parts[0]
transport = q.QuotaTransport(client_from_env(), m['frozen_endpoint']['base_url_canonical_sha256'], real_requests_authorized=True)
print(json.dumps(dict(event='preflight_pass', protected_v0=64, protected_v1=14,
    starting_total=78, remaining=remaining, first_recovery_attempt_index=2,
    previous_quota_stop_sha256=stop_hash, global_not_before=q.utc(stop['not_before_epoch']), current_time=q.utc())), flush=True)
if '--verify-only' in sys.argv:
    sys.exit(0)
q.require(sys.argv[1:] == ['--execute-reviewed-session-2'], 'explicit execution flag required')
before = inventory()
scheduler = q.make_reviewed_session(ROOT, ANCHOR, transport=transport, external_review_reference=REVIEW)
q.require(state(ledger, m['slots']) == (prior_valid, remaining, prior_attempts), 'ledger changed during preflight')
q.require(time.time() >= stop['not_before_epoch'], 'NOT_BEFORE_BLOCKED')
started = q.utc()
exclusive_bytes(DEST / 'execution_driver_session_0002.py', Path(__file__).read_bytes())
exclusive_json(DEST / 'session_0002_binding.json', dict(session_id=SESSION, protocol=q.VERSION,
    manifest_trust_anchor=ANCHOR, authorization_sha256=file_hash(AUTH), review_reference=REVIEW,
    previous_quota_stop_sha256=stop_hash, start_utc=started, starting_completed_count=78,
    protected_v0_judgments=64, protected_prior_v1_judgments=14, prior_valid_slots=prior_valid,
    remaining_ordered_slots=remaining, next_recovery_attempt_index=2, before_inventory=before,
    driver_sha256=file_hash(Path(__file__))))
resume = dict(blocked_record_sha256=stop_hash, review_reference=REVIEW)
exclusive_json(stop_path.with_name(stop_path.stem + '_resume_authorization.json'), dict(resume, authorized_at=q.utc()))
submissions, active = [], {}
protected = {(s['variant_id'], s['query_id']) for s in m['slots'] if s['completion'] == 'LOCKED_VALID_V0'}
protected.update((s['variant_id'], s['query_id']) for s in prior_valid)
def audit(event, args):
    if event == 'urllib.Request':
        q.require((active.get('variant_id'), active.get('query_id')) not in protected, 'protected judgment provider call prohibited')
        q.require(time.time() >= stop['not_before_epoch'], 'NOT_BEFORE_BLOCKED')
        submissions.append(dict(active))
sys.addaudithook(audit)
original_worker = scheduler.worker
def observed_worker(slot, path, *, resume=False):
    q.require((slot['variant_id'], slot['query_id']) not in protected, 'protected judgment must not reach worker')
    active.clear()
    active.update(variant_id=slot['variant_id'], query_id=slot['query_id'], recovery_attempt_index=int(path.name))
    print(json.dumps(dict(event='attempt_started', **active)), flush=True)
    outcome = original_worker(slot, path, resume=resume)
    print(json.dumps(dict(event='attempt_returned', **active, status=outcome['final_recovery_status'],
                         http_status=outcome['http_status'])), flush=True)
    return outcome
scheduler.worker = observed_worker
class ExhaustedSession(BaseException):
    pass
original_finish = scheduler.ledger.finish
def stop_on_exhaustion(path, index, outcome, now):
    receipt = original_finish(path, index, outcome, now)
    if receipt['slot_status_after_attempt'] == 'RECOVERY_EXHAUSTED' and receipt['final_recovery_status'] != 'QUOTA_BLOCKED':
        raise ExhaustedSession()
    return receipt
scheduler.ledger.finish = stop_on_exhaustion
try:
    result = scheduler.run(explicit_resume=resume)
except ExhaustedSession:
    result = dict(status='RECOVERY_EXHAUSTED', **active)
except BaseException as exc:
    result = dict(status='FAIL', error_type=type(exc).__name__)
print(json.dumps(dict(event='session_requests_stopped', result=result, provider_http_submissions=len(submissions))), flush=True)
successes, remaining, attempts = state(ledger, m['slots'])
new_attempts = [a for a in attempts if a['receipt_path'] not in {p['receipt_path'] for p in prior_attempts}]
status = {'VALID_JUDGMENT': 'COMPLETE', 'TRANSPORT_ERROR': 'TRANSPORT_BLOCKED'}.get(result['status'], result['status'])
print(json.dumps(dict(event='post_session_integrity_started')), flush=True)
verification_error = None
try:
    q.verify_manifest(ROOT, ANCHOR)
except Exception as exc:
    verification_error = type(exc).__name__
after = inventory()
changed = [p for p, h in before.items() if after.get(p) != h]
added = sorted(set(after) - set(before))
outside = [p for p in added if not p.startswith(q.RECOVERY_ROOT + '/')]
integrity = 'PASS' if not verification_error and not changed and not outside else 'FAIL'
accounting = (len(submissions) == len(new_attempts)
    and all((s['variant_id'], s['query_id']) not in protected for s in submissions)
    and (not new_attempts or (new_attempts[0]['alias'] == 'A1'
         and new_attempts[0]['query_id'] == 'eval024' and new_attempts[0]['recovery_attempt_index'] == 2))
    and all(1 <= a['recovery_attempt_index'] <= 3 for a in attempts))
quota_info = None
if status == 'QUOTA_BLOCKED':
    last = new_attempts[-1]
    r = q.read_json(ROOT / last['receipt_path'])
    p = ledger.blocks()[-1]
    b = q.read_json(p)
    quota_info = dict(blocking_variant=last['variant_id'], blocking_query=last['query_id'],
        recovery_attempt_index=last['recovery_attempt_index'], http_status=r['http_status'],
        provider_code=r['quota_metadata']['provider_status'], reliable_retry_delay=r['quota_metadata']['reliable_retry_delay_seconds'],
        global_not_before=q.utc(b['not_before_epoch']) if b['not_before_epoch'] is not None else None,
        quota_stop_sha256=file_hash(p))
    accounting = accounting and new_attempts[-1]['http_status'] == 429 and sum(a['http_status'] == 429 for a in new_attempts) == 1
if status == 'COMPLETE' and len(successes) != 29 or integrity != 'PASS' or not accounting:
    status = 'FAIL'
exclusive_json(DEST / 'session_0002_integrity.json', dict(status=integrity, checked_at=q.utc(),
    frozen_verifier='PASS' if verification_error is None else 'FAIL', verifier_error_type=verification_error,
    checked_preexisting_files=len(before), before_inventory_sha256=digest(before),
    changed_or_missing_preexisting_paths=changed, added_paths_outside_recovery_root=outside,
    session_2_added_hashes={p:after[p] for p in added}, recovery_attempt_accounting='PASS' if accounting else 'FAIL'))
report = dict(session_id=SESSION, status=status, protocol_verification='PASS',
    protected_v0_judgments=64, protected_prior_v1_judgments=14, starting_total_valid=78,
    recovered_during_session_2=len(successes)-14, cumulative_v1_recovered=len(successes),
    current_total_valid=64+len(successes), remaining_count=len(remaining), remaining_ordered_slots=remaining,
    completed_by_variant={a:sum(s['completion']=='LOCKED_VALID_V0' and s['alias']==a for s in m['slots'])
        +sum(s['variant_id']==v for s in successes) for a,v in q.VARIANTS.items()},
    quota_stop_information=quota_info, provider_http_submissions=len(submissions), http_submission_slots=submissions,
    new_attempts=new_attempts, production_calls=0, previously_valid_judgments_rejudged=0,
    recovery_attempt_accounting='PASS' if accounting else 'FAIL', frozen_integrity=integrity,
    ready_for_final_analysis=status=='COMPLETE' and integrity=='PASS', final_analysis_executed=False,
    automatic_resume=False, start_utc=started, end_utc=q.utc(), frozen_scheduler_result=result, stop='STOP')
exclusive_json(DEST / (SESSION + '_report.json'), report)
print(json.dumps(report), flush=True)
sys.exit(1 if status == 'FAIL' else 0)
