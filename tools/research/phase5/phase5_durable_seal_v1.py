"""Offline durable sealing primitives; post-production infrastructure correction.

The frozen v0 worker/evaluator remain byte-identical. Future workers must opt in
to seal_production_v1 instead of the v0 seal_production function. No inference or
evaluation code is imported here. Recovery never invokes the future sealer.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import re

from phase5_common import canonical, digest, exclusive_bytes, exclusive_json, file_hash

EPHEMERAL_SHA256 = '8205b16956fb264841ecd8644784a0d157f87df79b17c16825dc1163433ce5d8'
CLASSIFICATION = 'ephemeral_runtime_temporary_file'
REASON = ('PyTorch instantiator creates this generated module inside its process-owned '
          'TemporaryDirectory; Python weakref.finalize removes the directory at normal '
          'exit. Serialized production results do not require the module afterward.')
TEMP_PATTERN = re.compile(r'runtime_cache/tmp[a-z0-9_]{8}/_remote_module_non_scriptable\.py\Z')
SUPPLEMENT = 'durable_seal_recovery_v1.json'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, 'duplicate JSON key')
            result[key] = value
        return result
    return json.loads(Path(path).read_text(), object_pairs_hook=unique)


def safe_path(directory, relative):
    """Reject aliases, traversal and symlinks, including dangling parent links."""
    directory = Path(directory).absolute()
    require(directory.resolve() == directory, 'symlink in artifact root')
    require(isinstance(relative, str) and bool(relative), 'invalid artifact path')
    parts = relative.split('/')
    require(all(re.fullmatch(r'[A-Za-z0-9_.-]+', p) and p not in ('.', '..')
                for p in parts), 'noncanonical or wildcard artifact path')
    path = directory
    for part in parts:
        path = path / part
        require(not path.is_symlink(), 'symlink in artifact path: ' + relative)
    require(path.resolve().is_relative_to(directory), 'escaped artifact path')
    return path


def exclusion(directory, relative, expected):
    safe_path(directory, relative)
    require(TEMP_PATTERN.fullmatch(relative) is not None and expected == EPHEMERAL_SHA256,
            'unapproved ephemeral exclusion: ' + relative)
    return dict(original_path=relative, original_expected_sha256=expected,
                classification=CLASSIFICATION, reason=REASON)


def inventory(directory):
    result = set()
    for path in sorted(Path(directory).rglob('*')):
        relative = path.relative_to(directory).as_posix()
        safe_path(directory, relative)
        require(path.is_dir() or path.is_file(), 'nonregular artifact: ' + relative)
        if path.is_file():
            result.add(relative)
    return result


def reconcile(directory, seal, queries):
    """Structural equality and identities only; answer text is never displayed."""
    directory = Path(directory)
    ids = [q['query_id'] for q in queries]
    require(len(ids) == len(set(ids)) and seal['query_ids'] == ids, 'query order/count mismatch')
    require(digest(queries) == seal['query_hash'], 'query hash mismatch')
    for qid in ids:
        require(re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*', qid) is not None,
                'unsafe query ID')
    expected = {'production_outputs.jsonl', 'production_attempts.jsonl', 'run_binding.json'}
    for qid in ids:
        expected.update((f'{qid}.json', f'outputs/{qid}.json', f'observations/{qid}.json',
                         f'attempts/{qid}/started.json', f'attempts/{qid}/terminal.json'))
    require(expected <= set(seal['files']), 'incomplete durable record inventory')
    for folder in ('outputs', 'observations', 'attempts'):
        names = {p.name for p in (directory / folder).iterdir()}
        require(names == {q if folder == 'attempts' else q + '.json' for q in ids},
                'unexpected/missing ' + folder + ' record')
    binding = read_json(safe_path(directory, 'run_binding.json'))
    require(binding == {k: seal[k] for k in ('variant', 'config_hash', 'query_hash')},
            'run binding mismatch')
    outputs, attempts, run_ids = [], [], {}
    for query in queries:
        qid = query['query_id']
        start = read_json(safe_path(directory, f'attempts/{qid}/started.json'))
        terminal = read_json(safe_path(directory, f'attempts/{qid}/terminal.json'))
        output_path = safe_path(directory, f'outputs/{qid}.json')
        output = read_json(output_path)
        trace = read_json(safe_path(directory, f'{qid}.json'))
        observer = read_json(safe_path(directory, f'observations/{qid}.json'))
        require(start['query_id'] == terminal['query_id'] == output['query_id'] == qid,
                'record query ID mismatch')
        require(start['status'] == 'started' and terminal['status'] == 'completed'
                and output['generation_error'] is None, 'production incomplete/error')
        require(terminal['output_sha256'] == file_hash(output_path), 'terminal hash mismatch')
        require(output['query'] == trace['query'] == query['query'], 'record query text mismatch')
        require(trace == output['trace'] and start['run_id'] == trace['run_id'],
                'trace/output/run ID mismatch')
        events = observer['events']
        require(all(e['status'] == 'success' for e in events), 'observer execution error')
        require(sum(e['logical_call_type'] == 'llm' for e in events) == len(trace['llm_calls']),
                'observer/trace LLM count mismatch')
        require(sum(e['logical_call_type'] == 'retrieval' for e in events)
                == len(trace['retrieval_calls']), 'observer/trace retrieval count mismatch')
        require(observer['metadata']['error_type'] is None, 'observer error metadata')
        for kind in {e['logical_call_type'] for e in events}:
            selected = [e for e in events if e['logical_call_type'] == kind]
            require([e['logical_call_index'] for e in selected] == list(range(1, len(selected) + 1)),
                    'observer logical order mismatch')
        outputs.append(output)
        attempts.extend((start, terminal))
        run_ids[qid] = start['run_id']
    require(len(set(run_ids.values())) == len(ids), 'duplicate production run ID')
    for name, rows in [('production_outputs.jsonl', outputs), ('production_attempts.jsonl', attempts)]:
        require(safe_path(directory, name).read_bytes() == b''.join(canonical(r) + b'\n' for r in rows),
                'ordered journal mismatch: ' + name)
    return dict(completed=len(ids), production_errors=0, attempts=len(ids),
                traces=len(ids), observer_sidecars=len(ids), query_run_ids=run_ids,
                query_order_hash_reconciliation='PASS', ledger_trace_observer_reconciliation='PASS')


def audit_original(directory, queries, anchor):
    original = safe_path(directory, 'production_seal.json')
    require(file_hash(original) == anchor['original_seal_sha256'], 'original seal changed')
    seal = read_json(original)
    require(seal['schema'] == 'phase5-production-seal-v0', 'unsupported original seal')
    require(seal['variant'] == anchor['variant'] and seal['config_hash'] == anchor['config_sha256'],
            'original variant/config mismatch')
    require(len(queries) == anchor['query_count'] == 31, 'production must complete 31 queries')
    declared = anchor['ephemeral_exclusions']
    require(len(declared) == 1, 'incident requires exactly one declared exclusion')
    entry = declared[0]
    require(entry == exclusion(directory, entry['original_path'], entry['original_expected_sha256']),
            'incorrect ephemeral classification/reason')
    approved = {entry['original_path']: entry}
    durable, missing = [], []
    for relative, expected in sorted(seal['files'].items()):
        path = safe_path(directory, relative)
        if relative in approved:
            require(approved[relative]['original_expected_sha256'] == expected,
                    'exclusion hash differs from original seal')
            require(not path.exists(), 'incident exclusion must be missing after process exit')
            missing.append(relative)
        else:
            require(path.is_file(), 'missing durable artifact: ' + relative)
            require(file_hash(path) == expected, 'changed durable artifact: ' + relative)
            durable.append(dict(path=relative, sha256=expected))
    require(set(missing) == set(approved), 'unlisted/mismatched missing file')
    actual = inventory(directory)
    require(actual - {'production_seal.json', SUPPLEMENT, 'worker.lock'}
            == {item['path'] for item in durable}, 'unsealed additional artifact')
    result = reconcile(directory, seal, queries)
    return seal, durable, result


def build_supplement(directory, queries, anchor, protocol_hash, *, project_root):
    for entry in anchor['provenance_artifacts']:
        require(file_hash(safe_path(project_root, entry['path'])) == entry['sha256'],
                'changed provenance artifact: ' + entry['path'])
    _, durable, result = audit_original(directory, queries, anchor)
    return dict(schema='phase5b2r-durable-recovery-v1', seal_type='supplemental_durable_recovery',
                original_seal_status='FAILED_EPHEMERAL_LIFECYCLE',
                original_seal_hash=anchor['original_seal_sha256'], variant=anchor['variant'],
                protocol_sha256=protocol_hash, durable_artifacts=durable,
                provenance_artifacts=anchor['provenance_artifacts'],
                ephemeral_exclusions=anchor['ephemeral_exclusions'], reconciliation=result,
                durable_verification='PASS', production_rerun=False,
                semantic_evaluation_started=False)


def verify_pair(directory, queries, anchor, protocol_hash, *, project_root):
    """Recompute from original records; never trust supplemental PASS labels."""
    supplied = read_json(safe_path(directory, SUPPLEMENT))
    expected = build_supplement(directory, queries, anchor, protocol_hash, project_root=project_root)
    require(supplied == expected, 'supplemental seal content mismatch')
    return expected['reconciliation']


def seal_production_v1(output, rows, config):
    """Future-only replacement for seal_production; cannot reseal a v0 run.

    Takes already completed durable records. Ephemeral provenance is written as
    a separate, itself durably hashed sidecar. Unknown cache files stay durable.
    """
    output = Path(output)
    for name in ('production_seal.json', SUPPLEMENT, 'production_seal_v1.json',
                 'execution_cache_provenance_v1.json'):
        require(not (output / name).exists(), 'refusing existing/historical seal namespace')
    binding = read_json(safe_path(output, 'run_binding.json'))
    require(config.alias == binding['variant'], 'future variant mismatch')
    for name, paths in (
        ('production_outputs.jsonl', [f"outputs/{r['query_id']}.json" for r in rows]),
        ('production_attempts.jsonl', [f"attempts/{r['query_id']}/{n}.json" for r in rows for n in ('started', 'terminal')]),
    ):
        content = b''.join(canonical(read_json(safe_path(output, p))) + b'\n' for p in paths)
        target = safe_path(output, name)
        if target.exists():
            require(target.read_bytes() == content, 'future journal mismatch')
        else:
            exclusive_bytes(target, content)
    files, ephemeral = {}, []
    for relative in sorted(inventory(output) - {'worker.lock'}):
        expected = file_hash(safe_path(output, relative))
        if TEMP_PATTERN.fullmatch(relative) and expected == EPHEMERAL_SHA256:
            ephemeral.append(exclusion(output, relative, expected))
        else:
            files[relative] = expected
    seal = dict(schema='phase5-production-durable-seal-v1', **binding,
                query_ids=[r['query_id'] for r in rows], producer_pid=os.getpid(), files=files)
    reconcile(output, seal, rows)
    provenance = dict(schema='phase5-execution-cache-provenance-v1', ephemeral_artifacts=ephemeral)
    exclusive_json(output / 'execution_cache_provenance_v1.json', provenance)
    files['execution_cache_provenance_v1.json'] = file_hash(output / 'execution_cache_provenance_v1.json')
    exclusive_json(output / 'production_seal_v1.json', seal)


def verify_future_seal(directory, queries, *, separate_process=True):
    seal = read_json(safe_path(directory, 'production_seal_v1.json'))
    require(seal['schema'] == 'phase5-production-durable-seal-v1', 'unsupported future seal')
    require(not separate_process or seal['producer_pid'] != os.getpid(), 'requires separate verifier process')
    require('execution_cache_provenance_v1.json' in seal['files'], 'missing cache provenance binding')
    for relative, expected in seal['files'].items():
        require(file_hash(safe_path(directory, relative)) == expected, 'future durable hash mismatch')
    provenance = read_json(safe_path(directory, 'execution_cache_provenance_v1.json'))
    require(provenance['schema'] == 'phase5-execution-cache-provenance-v1', 'unknown cache provenance')
    ephemeral = set()
    for entry in provenance['ephemeral_artifacts']:
        relative, expected = entry['original_path'], entry['original_expected_sha256']
        require(entry == exclusion(directory, relative, expected), 'unknown future classification')
        require(relative not in ephemeral and relative not in seal['files'], 'duplicate future exclusion')
        ephemeral.add(relative)
        path = safe_path(directory, relative)
        if path.exists():
            require(file_hash(path) == expected, 'changed ephemeral artifact')
    require(inventory(directory) - ephemeral - {'production_seal_v1.json', 'worker.lock'}
            == set(seal['files']), 'unexpected future artifact')
    return reconcile(directory, seal, queries)
