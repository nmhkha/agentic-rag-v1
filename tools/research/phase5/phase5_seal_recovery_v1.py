#!/usr/bin/env python3
"""Phase 5B.2-R only: offline provenance recovery, never production or judging."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys

from phase5_common import canonical, digest, exclusive_bytes, exclusive_json, file_hash
from phase5_durable_seal_v1 import (SUPPLEMENT, EPHEMERAL_SHA256, audit_original,
    build_supplement, exclusion, read_json, require, safe_path, verify_pair)

ROOT = Path(__file__).resolve().parents[1]
BASE = 'data/evaluation/generation/phase5'
TRACE = 'data/rag/traces/phase5'
VARIANTS = {'R2': 'full-agentic-replication', 'A1': 'agentic-v1-no-answer-revision',
            'A2': 'agentic-v1-no-evidence-expansion'}
PROTOCOL = BASE + '/phase5b2r_recovery_protocol_v1.json'
MANIFEST = BASE + '/phase5b2r_recovery_manifest_v0.json'
REPORT = BASE + '/phase5b2r_recovery_report_v0.md'
TESTS = BASE + '/phase5b2r_negative_tests_v1.json'
SOURCE_FILES = ['scripts/phase5_durable_seal_v1.py', 'scripts/phase5_seal_recovery_v1.py',
                'tests/test_phase5_seal_recovery_v1.py']


def deny_network(event, args):
    if event in ('socket.connect', 'socket.connect_ex', 'socket.getaddrinfo',
                 'socket.sendto', 'socket.bind', 'urllib.Request'):
        raise RuntimeError('network forbidden during infrastructure recovery')


def verify_hashes(root, hashes):
    for name, expected in hashes.items():
        # Absolute paths are pinned local model snapshot paths from historical
        # records; HF snapshot symlinks are legitimate. Seal-relative paths use
        # safe_path and never inherit this exception.
        path = Path(name) if Path(name).is_absolute() else safe_path(root, name)
        require(file_hash(path) == expected, 'frozen artifact hash mismatch: ' + name)
    return len(hashes)


def historical_hashes(root):
    integrity = read_json(root / BASE / 'integrity_before_after_v0.json')
    hashes = {}
    def add(name, expected):
        require(name not in hashes or hashes[name] == expected, 'conflicting historical hash: ' + name)
        hashes[name] = expected
    for group in ('files', 'asset_files'):
        for name, entry in integrity[group].items():
            require(entry['before_sha256'] == entry['after_sha256'], 'historical integrity failure')
            add(name, entry['before_sha256'])
    for name, expected in read_json(root / BASE / 'report_artifact_hashes_v0.json')['files'].items():
        add(BASE + '/' + name, expected)
    env = read_json(root / BASE / 'execution_environment_v0.json')
    for group in ('asset_files', 'runtime_files'):
        for name, expected in env['runtime_lock'][group].items():
            add(name, expected)
    design = read_json(root / BASE / 'phase5a_ablation_manifest_v0.json')
    for entry in design['frozen_artifacts']:
        add(entry['path'], entry['sha256'])
    return hashes


def diagnosis(root):
    torch = '.venv/lib/python3.12/site-packages/torch/distributed/nn/'
    paths = [torch + 'jit/instantiator.py', torch + 'api/remote_module.py',
             torch + 'jit/templates/remote_module_template.py',
             '/usr/lib/python3.12/tempfile.py', '/usr/lib/python3.12/weakref.py',
             'scripts/phase5_ablation_runner.py', 'scripts/phase5_analyze.py',
             'scripts/evaluate_agentic_rag.py', 'scripts/evaluate_standard_rag.py']
    sources = {p: (root / p).read_text() for p in paths}
    inst = sources[paths[0]]
    require('_TEMP_DIR = tempfile.TemporaryDirectory()' in inst
            and 'INSTANTIATED_TEMPLATE_DIR_PATH = _TEMP_DIR.name' in inst
            and 'generated_module_name = f"{_FILE_PREFIX}non_scriptable"' in inst
            and '_write(out_path, generated_code_text)' in inst
            and 'importlib.import_module' in inst, 'PyTorch lifecycle evidence drift')
    require('instantiator.instantiate_non_scriptable_remote_module_template()' in sources[paths[1]],
            'PyTorch import entry evidence drift')
    require('_weakref.finalize(' in sources[paths[3]] and 'cls._rmtree(name' in sources[paths[3]]
            and 'atexit.register(self._exitfunc)' in sources[paths[4]], 'stdlib cleanup evidence drift')
    require('tempfile.tempdir = str(scratch)' in sources[paths[5]], 'worker temp root evidence drift')
    for name in paths[6:]:
        require('_remote_module_non_scriptable' not in sources[name]
                and 'runtime_cache' not in sources[name], 'unexpected evaluator cache dependency')
    # Use a benign sentinel, never import torch or recreate its missing module.
    code = ('import pathlib,tempfile; t=tempfile.TemporaryDirectory(prefix="phase5b2r-lifecycle-",dir="/tmp"); '
            'p=pathlib.Path(t.name)/"lifecycle_sentinel.txt"; p.write_text("benign cleanup probe"); '
            'print(t.name,flush=True)')
    probe = subprocess.run([sys.executable, '-B', '-c', code], check=True, capture_output=True, text=True)
    vanished = probe.stdout.strip()
    require(vanished.startswith('/tmp/phase5b2r-lifecycle-') and not Path(vanished).exists(),
            'normal process exit did not remove TemporaryDirectory')
    return dict(status='PASS', method='local source inspection plus stdlib-only normal-exit sentinel probe',
        source_sha256={p: file_hash(root / p) for p in paths},
        entry='torch/distributed/nn/api/remote_module.py:41-43 (module import)',
        creation='torch/distributed/nn/jit/instantiator.py:20-21, 92-107, 141-155',
        cleanup='/usr/lib/python3.12/tempfile.py:1024-1027,1072-1076; weakref.py:569-580,643-672',
        output_independence='Worker serializes/fsyncs JSON records and journals before exit; no temporary module path is an evaluator input. The legacy seal existence loop is the only dependency.',
        normal_exit_probe=dict(returncode=probe.returncode, directory=vanished, removed=True,
                               sentinel='lifecycle_sentinel.txt', torch_imported=False),
        missing_module_recreated=False, network_calls=0, model_inference_calls=0)


def anchor_for(root, alias, baseline):
    variant = VARIANTS[alias]
    directory = root / TRACE / variant
    run = read_json(root / BASE / variant / 'run_manifest.json')
    seal = read_json(directory / 'production_seal.json')
    missing = [p for p in seal['files'] if not safe_path(directory, p).is_file()]
    require(len(missing) == 1, 'unexpected missing file count')
    require(run['production_seal_sha256'] == file_hash(directory / 'production_seal.json'), 'run/original seal mismatch')
    provenance = [BASE + '/' + variant + '/' + name for name in ('run_manifest.json', 'variant_manifest.json')]
    provenance += [BASE + '/' + name for name in ('query_inputs_v0.json', 'execution_environment_v0.json',
                    'phase5a_ablation_manifest_v0.json', 'phase5a_ablation_spec_v0.md',
                    'phase5b1_preflight_manifest_v0.json', 'production_seal_validation_v0.json')]
    return dict(variant=alias, directory=TRACE + '/' + variant, query_count=31,
        original_seal_sha256=run['production_seal_sha256'], config_sha256=run['config_sha256'],
        ephemeral_exclusions=[exclusion(directory, missing[0], seal['files'][missing[0]])],
        provenance_artifacts=[dict(path=p, sha256=baseline[p]) for p in provenance])


def verify_run_records(root, alias, anchor, queries):
    variant = VARIANTS[alias]
    run = read_json(root / BASE / variant / 'run_manifest.json')
    seal, _, result = audit_original(root / anchor['directory'], queries, anchor)
    require(run['production_files'] == seal['files'], 'run/original inventory mismatch')
    require(run['variant'] == alias and run['variant_id'] == variant, 'run variant mismatch')
    require(run['production_attempt_count'] == 31 and run['production_errors'] == [], 'run incomplete/error')
    require(run['query_order'] == seal['query_ids'] and run['query_hash'] == seal['query_hash'], 'run query mismatch')
    serialized = (root / anchor['directory'] / 'production_outputs.jsonl').read_bytes()
    require(b'_remote_module_non_scriptable.py' not in serialized
            and anchor['ephemeral_exclusions'][0]['original_path'].encode() not in serialized,
            'temporary module referenced by serialized output')
    require(run['query_run_ids'] == result['query_run_ids'], 'run manifest ID mismatch')
    require(file_hash(root / BASE / variant / 'variant_manifest.json') == seal['config_hash']
            == run['variant_manifest_sha256'], 'variant config mismatch')
    verify_hashes(root, run['frozen_source_sha256'])
    env = read_json(root / BASE / 'execution_environment_v0.json')
    require(file_hash(root / BASE / 'execution_environment_v0.json') == run['environment_sha256'], 'environment provenance mismatch')
    require(read_json(root / anchor['directory'] / 'loaded_environment.json')
            == env['runtime_lock']['loaded_pipeline'], 'model snapshot provenance mismatch')
    for name, field in [('phase5a_ablation_manifest_v0.json', 'manifest'), ('phase5a_ablation_spec_v0.md', 'specification')]:
        require(file_hash(root / BASE / name) == run['design_sha256'][field], 'design provenance mismatch')
    require(run['evaluator_attempt_count'] == 0 and run['evaluation_start_utc'] is None, 'evaluation already started')
    require((root / BASE / variant / 'evaluation_attempts.jsonl').read_bytes() == b'', 'evaluation attempts exist')
    require(not (root / BASE / variant / 'records').exists(), 'semantic records exist')
    blocked = [json.loads(line) for line in (root / BASE / variant / 'evaluation.jsonl').read_text().splitlines()]
    require([r['query_id'] for r in blocked] == seal['query_ids']
            and all(r['evaluation_status'] == 'BLOCKED_NOT_ATTEMPTED'
                    and r['evaluation_attempted'] is False and r['evaluation_attempts'] == 0 for r in blocked),
            'unexpected evaluation state')
    return result


def verify_protocol(root, protocol):
    require(protocol['schema'] == 'phase5b2r-recovery-protocol-v1', 'unsupported recovery protocol')
    verify_hashes(root, protocol['preserved_project_files'])
    verify_hashes(root, protocol['historical_frozen_hashes'])
    require(historical_hashes(root) == protocol['historical_frozen_hashes'], 'historical inventory changed')
    verify_hashes(root, protocol['diagnosis']['source_sha256'])
    verify_hashes(root, protocol['infrastructure_source_sha256'])
    queries = read_json(root / BASE / 'query_inputs_v0.json')
    results = {}
    require(set(protocol['variants']) == set(VARIANTS), 'primary variant set mismatch')
    for alias in VARIANTS:
        anchor = protocol['variants'][alias]
        require(anchor == anchor_for(root, alias, protocol['preserved_project_files']), 'variant trust anchor mismatch')
        results[alias] = verify_run_records(root, alias, anchor, queries)
    return queries, results


def create(root, baseline_path, test_path):
    targets = [PROTOCOL, MANIFEST, REPORT, TESTS] + [TRACE + '/' + v + '/' + SUPPLEMENT for v in VARIANTS.values()]
    require(all(not (root / p).exists() for p in targets), 'recovery output already exists; never overwrite')
    baseline = read_json(baseline_path)
    verify_hashes(root, baseline)
    tests = read_json(test_path)
    require(tests['status'] == 'PASS' and tests['failures'] == 0 and tests['errors'] == 0
            and tests['tests_run'] >= 9, 'negative tests not passing')
    require(tests['test_source_sha256'] == file_hash(root / SOURCE_FILES[2]), 'test evidence source mismatch')
    require(tests['infrastructure_source_sha256'] == {p: file_hash(root / p) for p in SOURCE_FILES[:2]},
            'infrastructure changed since negative tests')
    protocol = dict(schema='phase5b2r-recovery-protocol-v1', phase='5B.2-R',
        amendment='post-production infrastructure correction discovered before semantic evaluation',
        created_utc=datetime.now(timezone.utc).isoformat(),
        exclusion_rule='Exactly one anchored runtime_cache/tmp[a-z0-9_]{8}/_remote_module_non_scriptable.py per original run, with the approved SHA-256 and exact classification/reason; reject all symlink components and traversal.',
        expected_ephemeral_sha256=EPHEMERAL_SHA256, diagnosis=diagnosis(root),
        preserved_project_files=baseline, historical_frozen_hashes=historical_hashes(root),
        infrastructure_source_sha256={p: file_hash(root / p) for p in SOURCE_FILES},
        variants={a: anchor_for(root, a, baseline) for a in VARIANTS},
        semantic_evaluation_authorized=False, production_reruns=0)
    queries, results = verify_protocol(root, protocol)
    # All variants must pass before any supplemental PASS seal is published.
    protocol_hash = digest(protocol)
    supplements = {a: build_supplement(root / anchor['directory'], queries, anchor, protocol_hash,
                                     project_root=root) for a, anchor in protocol['variants'].items()}
    exclusive_json(root / PROTOCOL, protocol)
    exclusive_json(root / TESTS, tests)
    for alias, seal in supplements.items():
        directory = root / protocol['variants'][alias]['directory']
        exclusive_json(directory / SUPPLEMENT, seal)
        verify_pair(directory, queries, protocol['variants'][alias], protocol_hash, project_root=root)
    verify_protocol(root, protocol)
    lines = ['# Phase 5B.2-R recovery report v0', '', 'Phase 5B.2-R status: PASS', '',
        'Infrastructure recovery and provenance / seal validation amendment.', '',
        'Original production: R2 31/31; A1 31/31; A2 31/31. Production errors: 0.',
        'Production reruns: 0. Semantic evaluations: 0/93.',
        'Original seals modified: NO. Their historical failure remains FAILED_EPHEMERAL_LIFECYCLE.', '',
        'Failure root cause: the v0 sealer inventories process-owned PyTorch generated code before worker exit. '
        'PyTorch instantiator creates the module in a TemporaryDirectory; Python weakref.finalize removes it at normal exit. '
        'The local source hashes and a successful benign sentinel cleanup probe are recorded in the protocol. '
        'The missing PyTorch files were never reconstructed and PyTorch was not imported.', '',
        'Evaluator source inspection confirms the generated module is not an evaluation input. '
        'Production records were serialized and fsynced before exit; the old existence check alone requires the vanished file.', '',
        '| Variant | Missing ephemeral path | Durable files from original seal | Recovery |',
        '|---|---|---:|---|']
    for alias, seal in supplements.items():
        lines.append(f"| {alias} | `{seal['ephemeral_exclusions'][0]['original_path']}` | {len(seal['durable_artifacts'])} | PASS |")
    lines += ['', f'All three original seals independently recorded SHA-256 `{EPHEMERAL_SHA256}` for the missing module.',
        'No other missing files exist. All surviving cache files remain durable; runtime_cache/** is not excluded.', '',
        'Durable artifacts verified: ordered output and attempt journals, 93 per-query outputs, 93 traces, '
        '93 observer sidecars, 186 per-query attempt records, run bindings, loaded model provenance and all other surviving seal entries. '
        'Query order/hash, config hashes and run manifest identities reconcile. Run/variant manifests and source, model, prompt, gold, '
        'corpus, retrieval, R0/R1 and earlier phase artifacts are covered by frozen hash inventories.', '',
        f"Negative corruption tests: {tests['tests_run']}/{tests['tests_run']} PASS (including T1–T9). See `{Path(TESTS).name}`.",
        f'Frozen artifact integrity: PASS. All {len(baseline)} preexisting project files remain byte-identical; '
        f"{len(protocol['historical_frozen_hashes'])} historical hash references also match (overlapping inventories).", '',
        'Future-only correction: `scripts/phase5_durable_seal_v1.py` supplies `seal_production_v1` and '
        '`verify_future_seal`. Future workers must opt in to these versioned functions. Known ephemeral entries are recorded '
        'in a separately hashed execution/cache provenance sidecar. Unknown cache files remain durable. The future sealer refuses '
        'existing v0 seals and recovery namespaces. The frozen v0 worker and evaluator remain unchanged and still reject the old seals.', '',
        'This is a post-production infrastructure correction discovered before semantic evaluation, not an experimental-system change.', '',
        'Network calls during recovery: 0. Gemini/API calls during recovery: 0. Model inference calls: 0. '
        'Recovery uses standard-library filesystem checks with a network-denying audit hook; tests use copied artifacts. '
        'No answers were displayed or manually inspected for quality. No semantic evaluator, point comparison or bootstrap was invoked.', '',
        'Existing Phase 5B.2 production outputs are eligible for semantic evaluation.',
        'This eligibility is not authorization to evaluate. Evaluation remains unstarted and requires separate review/authorization.', '',
        'Independent verification command (use the manifest SHA-256 printed at creation as the external trust anchor):', '',
        '```sh', 'python3 -B scripts/phase5_seal_recovery_v1.py verify --manifest-sha256 <reviewed-manifest-sha256>', '```', '',
        'STOP. Await review.']
    exclusive_bytes(root / REPORT, ('\n'.join(lines) + '\n').encode())
    artifacts = [p for p in targets if p != MANIFEST]
    manifest = dict(schema='phase5b2r-recovery-manifest-v0', status='PASS', protocol_sha256=protocol_hash,
        artifacts={p: file_hash(root / p) for p in artifacts},
        variants={a: dict(durable_recovery='PASS', durable_artifact_count=len(supplements[a]['durable_artifacts']),
                         reconciliation=results[a]) for a in VARIANTS},
        frozen_artifact_integrity='PASS', preserved_file_count=len(baseline), original_seals_modified=False,
        negative_tests=tests['tests_run'], production_reruns=0, semantic_evaluations=0,
        network_calls=0, gemini_api_calls=0, eligible_for_semantic_evaluation=True,
        semantic_evaluation_authorized=False, stop='Await review')
    exclusive_json(root / MANIFEST, manifest)
    verify(root, file_hash(root / MANIFEST))


def verify(root, manifest_hash):
    require(file_hash(root / MANIFEST) == manifest_hash, 'recovery manifest trust anchor mismatch')
    manifest = read_json(root / MANIFEST)
    verify_hashes(root, manifest['artifacts'])
    protocol = read_json(root / PROTOCOL)
    require(file_hash(root / PROTOCOL) == manifest['protocol_sha256'], 'recovery protocol changed')
    queries, results = verify_protocol(root, protocol)
    for alias, anchor in protocol['variants'].items():
        result = verify_pair(root / anchor['directory'], queries, anchor,
                             manifest['protocol_sha256'], project_root=root)
        require(result == results[alias] == manifest['variants'][alias]['reconciliation'], 'recovery result mismatch')
    print(json.dumps(dict(status='PASS', variants=list(results), production_reruns=0,
                          semantic_evaluations=0, manifest_sha256=manifest_hash)))


def main():
    sys.addaudithook(deny_network)
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    make = commands.add_parser('create')
    make.add_argument('--before-snapshot', type=Path, required=True)
    make.add_argument('--test-results', type=Path, required=True)
    check = commands.add_parser('verify')
    check.add_argument('--manifest-sha256', required=True, help='Frozen external trust anchor printed at creation')
    args = parser.parse_args()
    if args.command == 'create':
        create(ROOT, args.before_snapshot, args.test_results)
    else:
        verify(ROOT, args.manifest_sha256)


if __name__ == '__main__':
    main()
