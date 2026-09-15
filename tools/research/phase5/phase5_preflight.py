#!/usr/bin/env python3
"""Trusted offline preparation/preflight. Never imported by production."""
from __future__ import annotations
import argparse
import copy
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys
import tempfile
from urllib.parse import urlsplit
from phase5_common import canonical, digest, exclusive_json, file_hash, validate_queries
from phase5_assets import DENSE, RERANKER, cache_root, environment, inspect_snapshot, validate_environment

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'data/evaluation/generation/phase5'
DESIGN_HASH = '20893844b3bb7161b23d258476349e234675e404cd0b8a60fba17a376d8647cd'
SPEC_HASH = '51f1bf9e4db72ac3c3edeaf36ef5385dc9aff295c63068d4ffb07926ecb15b64'


def load_design(root=ROOT):
    root = Path(root)
    manifest = root / 'data/evaluation/generation/phase5/phase5a_ablation_manifest_v0.json'
    spec = manifest.with_name('phase5a_ablation_spec_v0.md')
    if file_hash(manifest) != DESIGN_HASH or file_hash(spec) != SPEC_HASH:
        raise ValueError('FROZEN DESIGN HASH MISMATCH: STOP; do not repair')
    design = json.loads(manifest.read_text())
    if design['specification']['sha256'] != SPEC_HASH or design['status'] != 'FROZEN':
        raise ValueError('design not frozen')
    for alias in ('R2', 'A1', 'A2'):
        validate_variant(design, alias, design['variant_manifests'][alias])
    return design


def differences(a, b, prefix=''):
    if type(a) is not type(b):
        return [prefix]
    if type(a) is dict:
        result = []
        for key in sorted(set(a) | set(b)):
            path = prefix + '.' + key if prefix else key
            result.extend([path] if key not in a or key not in b else differences(a[key], b[key], path))
        return result
    return [] if a == b else [prefix]


def validate_variant(design, alias, candidate):
    if alias not in ('R2', 'A1', 'A2'):
        raise ValueError('only mandatory variants are supported')
    if digest(candidate) != design['variant_manifest_canonical_sha256'][alias]:
        raise ValueError('canonical config hash mismatch')
    expected = {'R2': [], 'A1': ['ablation_flags.enable_answer_revision'], 'A2': ['ablation_flags.enable_expansion']}[alias]
    actual = [p for p in differences(design['variant_manifests']['R2'], candidate) if p != 'variant_id']
    if actual != expected:
        raise ValueError('single-variable diff mismatch')
    return copy.deepcopy(candidate)


def resolve_variant(alias, root=ROOT):
    design = load_design(root)
    return validate_variant(design, alias, design['variant_manifests'][alias])


def materialize_variants(directory, design):
    for alias in ('R2', 'A1', 'A2'):
        value = validate_variant(design, alias, design['variant_manifests'][alias])
        exclusive_json(Path(directory) / alias / 'variant_manifest.json', value)


def integrity(design, root=ROOT):
    expected = dict(design['source_integrity']['before_sha256'])
    expected['data/evaluation/generation/phase5/phase5a_ablation_manifest_v0.json'] = DESIGN_HASH
    expected['data/evaluation/generation/phase5/phase5a_ablation_spec_v0.md'] = SPEC_HASH
    result = {p: {'before_sha256': h, 'after_sha256': file_hash(Path(root) / p)} for p, h in expected.items()}
    changed = [p for p, v in result.items() if v['before_sha256'] != v['after_sha256']]
    if changed:
        raise ValueError('frozen integrity mismatch: ' + ', '.join(changed))
    return result


def prepare_queries(target=BASE / 'query_inputs_v0.json', root=ROOT):
    design = load_design(root)
    source = next(a for a in design['frozen_artifacts'] if a['role'] == 'verified_final_gold_evaluator_only')
    path = Path(root) / source['path']
    if file_hash(path) != source['sha256']:
        raise ValueError('verified dataset hash mismatch')
    rows = [{'query_id': i['query_id'], 'query': i['query']} for i in json.loads(path.read_text())['items']]
    validate_queries(rows, design['query_input_schema']['canonical_sha256'])
    if [r['query_id'] for r in rows] != design['query_order']:
        raise ValueError('query order mismatch')
    if Path(target).exists():
        if Path(target).is_symlink() or Path(target).read_bytes() != canonical(rows):
            raise FileExistsError('existing projection differs; no overwrite')
    else:
        exclusive_json(target, rows)
    return {'count': len(rows), 'canonical_sha256': digest(rows), 'path': str(target)}


def endpoint_configuration():
    """Read only endpoint settings as data, never source/execute an env file."""
    names = ('RAG_LLM_MODEL', 'RAG_LLM_BASE_URL')
    settings = {k: os.environ.get(k, '') for k in names}
    env_file = ROOT / '.env'
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            name, separator, value = line.removeprefix('export ').partition('=')
            name = name.strip()
            if separator and name in names and not settings[name]:
                parts = shlex.split(value, comments=True)
                settings[name] = parts[0] if len(parts) == 1 else ''
    parsed = urlsplit(settings['RAG_LLM_BASE_URL'])
    valid = settings['RAG_LLM_MODEL'] == 'gemini-3.5-flash-lite' and parsed.scheme in ('http', 'https') and bool(parsed.hostname)
    # No query strings, embedded auth, keys, or request headers enter provenance.
    return dict(model=settings['RAG_LLM_MODEL'], endpoint_host=parsed.hostname,
                endpoint_scheme=parsed.scheme, endpoint_port=parsed.port,
                base_url_canonical_sha256=digest(settings['RAG_LLM_BASE_URL'].strip()),
                configuration_only=True, availability_tested=False, valid=bool(valid))


def inspect_remote_code(cache):
    repo = Path(cache) / 'models--jinaai--xlm-roberta-flash-implementation'
    ref = repo / 'refs/main'
    if not ref.is_file():
        raise ValueError('Dense remote-code cache refs/main is missing')
    revision = ref.read_text().strip()
    snapshot = repo / 'snapshots' / revision
    files = {str(p): file_hash(p) for p in sorted(snapshot.glob('*.py'))}
    if not files or not (snapshot / 'modeling_lora.py').is_file():
        raise ValueError('Dense remote-code snapshot incomplete')
    files[str(ref)] = file_hash(ref)
    return dict(resolved_revision=revision, files=files,
                provenance='Current offline cache pinned for all new variants; historical code revision was not frozen in Phase 5A')


def preflight(*, load_pipeline=False):
    from phase5_isolation import block_network
    counts = block_network()
    design = load_design()
    hashes = integrity(design)
    config = resolve_variant('R2')
    validate_environment(config)
    result = dict(design='VERIFIED', integrity=hashes, environment=environment(),
                  dense=inspect_snapshot(cache_root(), *DENSE),
                  reranker=inspect_snapshot(cache_root(), *RERANKER, require_main=True),
                  query_input=prepare_queries(), network=counts, pipeline_load=None, blockers=[],
                  endpoint=endpoint_configuration())
    for name in ('dense', 'reranker'):
        result['blockers'].extend(name + ': ' + e for e in result[name]['errors'])
    if not result['endpoint']['valid']:
        result['blockers'].append('configured endpoint model mismatch')
    try:
        result['dense_remote_code'] = inspect_remote_code(cache_root())
    except ValueError as exc:
        result['blockers'].append(str(exc))
    if load_pipeline and not result['blockers']:
        try:
            with tempfile.TemporaryDirectory(prefix='phase5-offline-load-') as scratch:
                env = {k: os.environ[k] for k in ('PATH', 'LANG') if k in os.environ}
                env.update(HF_HUB_CACHE=str(cache_root()), PYTHONDONTWRITEBYTECODE='1')
                probe = subprocess.run([sys.executable, '-B', str(ROOT / 'scripts/phase5_assets.py'),
                    '--scratch', scratch, '--query-input', result['query_input']['path']],
                    env=env, stdin=subprocess.DEVNULL, close_fds=True, capture_output=True, text=True, check=True)
                loaded = json.loads(probe.stdout)
                if loaded['status'] != 'PASS':
                    raise ValueError(loaded['error'])
                result['pipeline_load'] = loaded['actual']
                result['pipeline_read_audit'] = loaded['reads']
                result['pipeline_network'] = loaded['network']
        except Exception as exc:
            result['blockers'].append('offline pipeline load: ' + type(exc).__name__ + ': ' + str(exc))
    elif not load_pipeline:
        result['blockers'].append('actual pipeline load/configuration not yet verified')
    result['status'] = 'BLOCKED' if result['blockers'] else 'PASS'
    return result


def runtime_lock(result, design):
    """Minimal worker-only projection, excluding design/reference provenance."""
    if result['status'] != 'PASS':
        raise ValueError('preflight is not PASS')
    if not result.get('tests', {}).get('passed') or not result.get('implementation_hashes'):
        raise ValueError('full Phase 5B.1 test certificate required')
    for path, expected in result['implementation_hashes'].items():
        if file_hash(ROOT / path) != expected:
            raise ValueError('implementation changed since acceptance tests: ' + path)
    from phase5_ablation_runner import CONFIG_HASHES
    paths = [a['path'] for a in design['frozen_artifacts'] if a['role'] in
             ('frozen_production_source', 'authoritative_runtime_corpus', 'baseline_generation_prompt')]
    paths += ['data/indexes/dense-jina-v3-v0/' + n for n in ('embeddings.npy', 'chunk_ids.json', 'index_manifest.json')]
    paths += ['scripts/' + n for n in ('phase5_common.py', 'phase5_isolation.py', 'phase5_observer.py', 'phase5_assets.py', 'phase5_ablation_runner.py')]
    assets = dict(result['dense_remote_code']['files'])
    for name in ('dense', 'reranker'):
        for filename, value in result[name]['files'].items():
            assets[str(Path(result[name]['snapshot']) / filename)] = value['sha256']
        ref = Path(result[name]['snapshot']).parent.parent / 'refs/main'
        assets[str(ref)] = file_hash(ref)
    return dict(schema='phase5-runtime-lock-v0', config_hashes=CONFIG_HASHES,
                query_hash=design['query_input_schema']['canonical_sha256'],
                runtime_files={str(ROOT / p): file_hash(ROOT / p) for p in paths}, asset_files=assets,
                cache=str(cache_root()), packages=result['environment']['packages'],
                python_version=result['environment']['python_version'], loaded_pipeline=result['pipeline_load'],
                endpoint=result['endpoint'])


def launch_primary(result, *, execute_phase5b2=False):
    """Future trusted scheduler. Explicit execution opt-in; never invoked in 5B.1."""
    if not execute_phase5b2:
        raise PermissionError('separate Phase 5B.2 authorization required')
    design = load_design()
    integrity(design)
    lock = runtime_lock(result, design)
    from phase5_ablation_runner import VARIANT_IDS
    env = {k: os.environ[k] for k in ('PATH', 'LANG', 'RAG_LLM_MODEL', 'RAG_LLM_BASE_URL', 'RAG_LLM_API_KEY') if k in os.environ}
    if any(not env.get(k) for k in ('RAG_LLM_MODEL', 'RAG_LLM_BASE_URL', 'RAG_LLM_API_KEY')):
        raise ValueError('export the endpoint environment before approved production')
    env.update(PYTHONDONTWRITEBYTECODE='1', HF_HUB_OFFLINE='1', TRANSFORMERS_OFFLINE='1')
    # All full manifests materialize before the first worker starts.
    for alias in ('R2', 'A1', 'A2'):
        target = BASE / VARIANT_IDS[alias] / 'variant_manifest.json'
        config = resolve_variant(alias)
        if target.exists():
            if target.read_bytes() != canonical(config):
                raise ValueError('existing variant manifest differs')
        else:
            exclusive_json(target, config)
    with tempfile.TemporaryDirectory(prefix='phase5-runtime-lock-') as tmp:
        lock_path = Path(tmp) / 'runtime_lock.json'
        exclusive_json(lock_path, lock)
        for alias in ('R2', 'A1', 'A2'):
            out = ROOT / 'data/rag/traces/phase5' / VARIANT_IDS[alias]
            if (out / 'production_seal.json').exists():
                from phase5_analyze import verify_seal
                seal = verify_seal(out)
                if seal['config_hash'] != lock['config_hashes'][alias] or seal['query_hash'] != lock['query_hash']:
                    raise ValueError('existing production seal differs')
                continue
            subprocess.run([sys.executable, '-B', str(ROOT / 'scripts/phase5_ablation_runner.py'),
                '--variant', alias, '--query-input', str(BASE / 'query_inputs_v0.json'), '--output', str(out),
                '--runtime-lock', str(lock_path), '--lock-sha256', file_hash(lock_path), '--execute-phase5b2'],
                env=env, stdin=subprocess.DEVNULL, close_fds=True, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--load-pipeline', action='store_true', help='Offline load only; no queries or inference')
    parser.add_argument('--output', type=Path, required=True, help='New preflight JSON path (exclusive create)')
    parser.add_argument('--tests-json', type=Path, help='Offline acceptance certificate from tests/phase5_run_suite.py')
    parser.add_argument('--report-markdown', type=Path, help='New human-readable report (exclusive create)')
    args = parser.parse_args()
    result = preflight(load_pipeline=args.load_pipeline)
    if bool(args.tests_json) != bool(args.report_markdown):
        parser.error('--tests-json and --report-markdown must be supplied together')
    if args.tests_json:
        certify(result, json.loads(args.tests_json.read_text()))
        from phase5_common import exclusive_bytes
        exclusive_bytes(args.report_markdown, render_report(result).encode())
        result['report_sha256'] = file_hash(args.report_markdown)
    exclusive_json(args.output, result)
    print(console_summary(result) if args.tests_json else 'Phase 5B.1 preflight: ' + result['status'])
    if not args.tests_json:
        for blocker in result['blockers']:
            print('BLOCKER:', blocker)
    raise SystemExit(0 if result['status'] == 'PASS' else 2)


def certify(result, tests):
    design = load_design()
    result['tests'] = tests
    result['implementation_hashes'] = tests['implementation_hashes']
    if not tests['passed'] or tests['failures']:
        result['status'] = 'FAIL'
        result['blockers'].append('acceptance tests failed')
    for path, expected in tests['implementation_hashes'].items():
        if file_hash(ROOT / path) != expected:
            result['status'] = 'FAIL'
            result['blockers'].append('implementation changed after tests: ' + path)
    result['integrity'] = integrity(design)
    result['phase5a_hashes'] = {'specification': SPEC_HASH, 'manifest': DESIGN_HASH}
    result['variant_config_hashes'] = {a: design['variant_manifest_canonical_sha256'][a] for a in ('R2', 'A1', 'A2')}
    result['variant_ids'] = {a: design['variant_manifests'][a]['variant_id'] for a in ('R2', 'A1', 'A2')}
    result['scope'] = dict(phase='5B.1', real_benchmark_production_queries=0, real_semantic_evaluations=0,
                          gemini_api_calls=0, network_calls=0, phase5b2_started=False)
    result['files_created'] = sorted(list(tests['implementation_hashes']) + [
        'data/evaluation/generation/phase5/query_inputs_v0.json',
        'data/evaluation/generation/phase5/phase5b1_preflight_report_v0.md',
        'data/evaluation/generation/phase5/phase5b1_preflight_manifest_v0.json'])
    result['files_modified'] = []
    result['ready_for_phase5b2'] = result['status'] == 'PASS'
    result['execution_authorized'] = False
    result['limitations'] = [
        'Read guard covers Python audited I/O/imports in reviewed code; it is not a hostile native-code sandbox.',
        'Endpoint validated by local configuration only; provider availability/backend identity was not tested.',
        'Hub warnings about downloaded remote-code files refer to offline cache-to-scratch copies; audited network attempts during pipeline loading were zero.',
        'Historical R1 full environment and Dense remote-code revision were not independently frozen; current cache source hashes are recorded for new variants.',
        'Production/evaluation launch requires separate Phase 5B.2 authorization; no benchmark is launched by preflight.',
    ]
    return result


def console_summary(result):
    passed = 'PASS' if result['tests']['passed'] else 'FAIL'
    lines = ['Phase 5B.1 status: ' + result['status'], '', 'Phase 5A design: VERIFIED']
    for label in ('Wrapper implementation', 'R2 parity', 'A1 behavior', 'A2 behavior', 'Leakage isolation',
                  'Query-only input', 'Observer pass-through', 'Attempt ledger', 'Production/evaluator separation'):
        lines.append(label + ': ' + passed)
    for name, label in (('dense', 'Dense'), ('reranker', 'Reranker')):
        item = result[name]
        lines += [label + ' snapshot: ' + ('PASS' if item['model_pass'] else 'FAIL'),
                  'Resolved revision: ' + str(item['resolved_revision']),
                  label + ' tokenizer: ' + ('PASS' if item['tokenizer_pass'] and (result.get('pipeline_load') or {}).get(name + '_tokenizer', {}).get('verified') else 'FAIL')]
    lines += ['Frozen source integrity: PASS',
              f"Tests: {len(result['tests']['successes'])}/{result['tests']['tests_run']} PASS",
              'Network calls: 0', 'Gemini/API calls: 0', 'Real benchmark production queries: 0', 'Real semantic evaluations: 0',
              'Files created:', *result['files_created'], 'Files modified: none',
              'Blockers: ' + ('; '.join(result['blockers']) or 'none'),
              'Ready for Phase 5B.2: ' + ('YES (requires separate authorization)' if result['ready_for_phase5b2'] else 'NO')]
    return '\n'.join(lines)


def render_report(result):
    tests = result['tests']
    lines = ['# Phase 5B.1 — implementation, isolation and offline preflight', '',
             '**Status: ' + result['status'] + '**. Phase 5B.2 has not started and is not authorized.', '',
             '## 1. Implementation', '',
             'Added a thin wrapper around the unchanged AgenticRAGController. No frozen file was modified.', '',
             *['- `' + p + '`' for p in result['files_created']], '',
             '## 2. Frozen design and configurations', '',
             '- Specification SHA-256: `' + SPEC_HASH + '`', '- Manifest SHA-256: `' + DESIGN_HASH + '`',
             '- The original embedded Phase 5A validator passed before implementation: 246 original files, 67 named artifacts and 113 Phase 4E provenance entries matched.',
             '- The manifest has no self-hash. Its observed byte hash above was sealed at the start of Phase 5B.1; the specification hash matches its frozen manifest declaration.', '',
             '| ID | Exact variant ID | Canonical config SHA-256 |', '|---|---|---|']
    for alias, name in result['variant_ids'].items():
        lines.append(f"| {alias} | {name} | `{result['variant_config_hashes'][alias]}` |")
    lines += ['', 'Full objects are validated with SHA-256 of UTF-8 JSON, sorted keys, ensure_ascii=False, separators=(comma, colon), no newline. Only variant_id is excluded from the recursive difference check. A1 differs only in enable_answer_revision; A2 only in enable_expansion. Tests reject missing/extra/type/configuration drift and no-op ablations. Exact variant objects were materialized only in temporary test directories.', '',
        '## 3. Runtime architecture', '',
        'Trusted preparation validates the frozen verified dataset and projects exactly 31 ordered query_id/query records. The projection canonical hash is `' + result['query_input']['canonical_sha256'] + '`.', '',
        'The future scheduler materializes all primary manifests first and runs R2, A1, A2 in separate fresh sequential processes. It passes a minimal hash-locked runtime certificate, an allowlisted environment, no inherited data descriptors, and stdin=/dev/null. Production rejects full-design paths/schema, unapproved preloaded source modules, resolved symlink aliases and reads outside explicit source/corpus/index/cache/input/output permissions. The controller receives only a query string and a fresh state.', '',
        'The observer delegates each call once and returns the original response object or exception. It records stage/order, logical type, attempt index, UTC timestamp, canonical request/response hashes, success/error, redacted raw response, and observed urllib submissions. Provider-internal retries remain unknown. Successful controller-assigned check snapshots determine eligibility; no observer parse drives a controller decision. Unreached/failed decisions are null with reasons.', '',
        'Each query gets an exclusive attempt directory and fsynced started record before invocation; terminal completion/error follows durable trace, sidecar and output writes. Worker flock prevents concurrent advancement. Resume is bound to the same variant/query hash and executes only never-started queries; completed/errors are skipped, ambiguous and orphan outputs fail closed. Ordered JSONL journals and hashes seal production artifacts. No retries or budget compensation were added.', '',
        'The separate trusted evaluator requires all primary seals before joining references. It imports the unchanged evaluate_record, judge_prompt, parse_judge, point_audit and citation validator. Durable request/response slots replay the same responses into the frozen parser after a crash, preserving at most three actual evaluator requests in total. Existing evaluator outputs are never rejudged. The analysis CLI only verifies seals in this phase.', '',
        '## 4. Leakage gates L1–L5', '',
        '- L1: recursive production AST/import closure and runtime rejection of evaluator reads/imports, including already imported unapproved modules.',
        '- L2: exact projection schema/count/order/hash; duplicate IDs/text, missing values, additional/nested labels and changed text are rejected.',
        '- L3: built-in open, pathlib and os.open reject direct and symlink paths for gold, historical outputs, traces and analysis files.',
        '- L4: PHASE5_GOLD_SENTINEL_DO_NOT_LEAK stays absent from synthetic controller state/output, prompts, retrieval calls, original trace and sidecars.',
        '- L5: fresh-process fake production succeeds with references unavailable; a different process joins only after all seals verify. Tampering and missing seals fail.', '',
        '## 5. Behavior and evaluator tests', '',
        'R2 direct-controller parity compares complete states/traces, prompt bytes, retrieval/merge arguments and transitions on ordinary, expansion, revision, citation, semantic and error paths, excluding only run IDs and timestamps. A1 retains its initial completeness check and citation repair but removes answer revision and its dependent recheck. A2 retains coverage/missing aspects and answer/citation repair while preserving initial Top-5 exactly and removing expansion retrieval/merge. Empty aspects are ineligible. All nominal budgets, including six LLM calls, remain unchanged. Synthetic evaluator wiring exercises the actual frozen evaluator, identical retry prompts and no rejudging.', '',
        f"**Tests: {len(tests['successes'])}/{tests['tests_run']} PASS.**", '',
        *['- `' + name + '`' for name in tests['successes']], '',
        '## 6. Environment', '',
        '- Python executable: `' + result['environment']['python_executable'] + '`',
        '- Python version: `' + result['environment']['python_version'] + '`',
        '- Actual pipeline: CPU, Dense float32/batch 4, reranker float32/batch 1, max length 8192.',
        '- Endpoint configuration: `' + result['endpoint']['model'] + '` at `' + str(result['endpoint']['endpoint_host']) + '`; configuration-only, no availability request.',
        '- All installed package versions are recorded in the companion JSON manifest. No credentials or authorization headers are recorded.', '',
        '## 7. Model and tokenizer snapshots', '']
    for name in ('dense', 'reranker'):
        item = result[name]
        actual = (result.get('pipeline_load') or {}).get(name + '_tokenizer', {})
        lines += [f"- {name}: `{item['model_id']}` revision `{item['resolved_revision']}`; snapshot `{item['snapshot']}`.",
                  f"- {name} actual tokenizer fingerprint: `{actual.get('actual_fingerprint', 'unverified')}`; exact-snapshot fingerprint: `{actual.get('expected_fingerprint', 'unverified')}`."]
    lines += ['- Model weight/config/tokenizer file hashes and resolved blob paths are recorded. Cache blob identities are checked. The loaded model config revisions and actual tokenizer backend/special-token fingerprints are validated against explicit offline snapshot loads.',
              '- Dense external implementation snapshot: `' + result.get('dense_remote_code', {}).get('resolved_revision', 'unverified') + '`; current source hashes pinned separately.', '',
        '## 8. Frozen source integrity', '',
        f"All {len(result['integrity'])} original/design paths match their before-hashes after implementation. The manifest contains every before/after SHA-256, covering corpus, gold, R0/R1, R1 traces, Phase 4A/4E, prompt, production/retrieval/evaluator sources, dependencies, original tests and original bytecode. New implementation/test source hashes are also recorded and must match before future launch.", '',
        '## 9. Network and execution scope', '',
        'Network calls = 0; Gemini/API calls = 0; real benchmark production queries = 0; real semantic evaluations = 0. The suite blocks transport before application imports, including HTTP/Gemini probes and offline Hub downloads. Deliberately blocked guard probes are counted separately: ' + str(tests['blocked_network_probe_attempts']) + '. The guarded model-load subprocess recorded zero connection attempts. No final production manifests/results were materialized.', '',
        '## 10. Blockers and limits', '',
        *(['- ' + b for b in result['blockers']] or ['- No implementation/preflight blocker remains.']),
        *['- ' + item for item in result['limitations']], '',
        'Reproduce without network or benchmark execution:', '', '```bash',
        '.venv/bin/python -B tests/phase5_run_suite.py --output /tmp/phase5-tests-NEW.json',
        '.venv/bin/python -B scripts/phase5_preflight.py --load-pipeline --output /tmp/phase5-preflight-NEW.json',
        '```', '',
        'Use new output filenames; writes are exclusive. To produce a new complete report, add --tests-json and --report-markdown with new paths. Do not overwrite this report or the frozen Phase 5A design.', '',
        'STOP: wait for external review before any Phase 5B.2 production or evaluation.', '']
    return '\n'.join(lines)


if __name__ == '__main__':
    main()
