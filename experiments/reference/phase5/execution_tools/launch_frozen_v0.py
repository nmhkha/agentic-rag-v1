"""Authorized orchestration only; frozen workers are unchanged."""
import json
import os
from pathlib import Path
import shlex
import sys
from datetime import datetime, timezone

ROOT = Path('/home/minhkha/kk/TTTN/legal-agentic-rag')
sys.path.insert(0, str(ROOT / 'scripts'))
from phase5_common import exclusive_json, file_hash
from phase5_preflight import load_design, integrity, runtime_lock, launch_primary, endpoint_configuration

BASE = ROOT / 'data/evaluation/generation/phase5'
old = json.loads((BASE / 'phase5b1_preflight_manifest_v0.json').read_text())
fresh = json.loads(Path('/tmp/phase5b2-preflight-20260907.json').read_text())
tests = json.loads(Path('/tmp/phase5b2-tests-20260907.json').read_text())
assert fresh['status'] == 'PASS' and tests['passed'] and tests['tests_run'] == 36
for key in ('integrity', 'environment', 'dense', 'reranker', 'query_input', 'endpoint', 'dense_remote_code', 'pipeline_load'):
    assert fresh[key] == old[key], 'STOP: frozen drift: ' + key
assert tests['implementation_hashes'] == old['implementation_hashes']
fresh.update(tests=tests, implementation_hashes=old['implementation_hashes'])
before = json.loads(Path('/tmp/phase5b2-initial-integrity-20260907.json').read_text())
for relative, entry in before.items():
    assert file_hash(ROOT / relative) == entry['expected_sha256'], 'STOP: frozen drift: ' + relative
manifest_relative = str((BASE / 'phase5b1_preflight_manifest_v0.json').relative_to(ROOT))
before[manifest_relative] = dict(before_sha256=file_hash(ROOT / manifest_relative))
query_relative = str((BASE / 'query_inputs_v0.json').relative_to(ROOT))
before[query_relative] = dict(before_sha256=file_hash(ROOT / query_relative))
design = load_design()
integrity(design)
lock = runtime_lock(fresh, design)

# Parse only three endpoint variables as data. Never serialize credentials.
names = ('RAG_LLM_MODEL', 'RAG_LLM_BASE_URL', 'RAG_LLM_API_KEY')
for line in (ROOT / '.env').read_text().splitlines():
    name, separator, value = line.removeprefix('export ').partition('=')
    name = name.strip()
    if separator and name in names and not os.environ.get(name):
        parts = shlex.split(value, comments=True)
        if len(parts) == 1:
            os.environ[name] = parts[0]
assert all(os.environ.get(name) for name in names), 'Missing endpoint configuration'
assert endpoint_configuration() == old['endpoint'], 'STOP: endpoint drift'
environment_path = BASE / 'execution_environment_v0.json'
environment = dict(schema='phase5b2-execution-environment-v0',
    created_at=datetime.now(timezone.utc).isoformat(), execution_authorized=True,
    production_order=['R2', 'A1', 'A2'], runtime_lock=lock,
    preflight_certificate_sha256=file_hash(BASE / 'phase5b1_preflight_manifest_v0.json'),
    preflight_rerun=fresh, before_integrity=before,
    orchestration_sha256=file_hash(__file__))
exclusive_json(environment_path, environment)
print('Preflight PASS. Launching frozen R2, A1, A2 sequentially.', flush=True)
launch_primary(fresh, execute_phase5b2=True)
print('All mandatory production runs sealed. No semantic evaluation launched.', flush=True)
