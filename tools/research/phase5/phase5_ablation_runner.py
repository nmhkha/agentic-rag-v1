#!/usr/bin/env python3
"""Thin production worker. Trusted preparation and analysis run in other processes."""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import sys
import sysconfig
import uuid
from phase5_common import canonical, digest, exclusive_bytes, exclusive_json, file_hash, sync_dir, validate_queries
from phase5_isolation import ReadGuard
from phase5_observer import Observer, ObservedClient, ObservedPipeline

ROOT = Path(__file__).resolve().parents[1]
QUERY_HASH = '1d29c4304f61d7c2235d7cab37e2bbf63a35e0c0caf6873d7e458e23904ebc78'
DENSE_REVISION = 'ab036b023d30b4d1138c4c3bfa9f0c445ab455d6'
RERANKER_REVISION = '953dc6f6f85a1b2dbfca4c34a2796e7dde08d41e'
# Sealed minimal mapping from the byte-verified design. No design object enters a controller.
CONFIG_HASHES = {
    'R2': 'cc4f30732d3f5ecf46b69f804aab905b5e82fc8fe82f9f89098e4bd17dc2a956',
    'A1': '9f7beb58b43658af823410d99aad247cc9022b6bdfd0c6ff9e1ee6f4b201076e',
    'A2': '7d151d91a522f8ba0236664deade43aa19c35d07d926856e11fb93f6f87d66f5',
}
VARIANT_IDS = {'R2': 'full-agentic-replication', 'A1': 'agentic-v1-no-answer-revision', 'A2': 'agentic-v1-no-evidence-expansion'}


@dataclass(frozen=True)
class RuntimeConfig:
    alias: str

    def __post_init__(self):
        if type(self.alias) is not str or self.alias not in CONFIG_HASHES:
            raise ValueError('unsupported primary variant')

    @property
    def flags(self):
        return dict(enable_expansion=self.alias != 'A2', enable_answer_revision=self.alias != 'A1', enable_citation_revision=True)


def run_query(query, config, pipeline, client, *, run_id=None):
    """Dependency injection for synthetic tests; controller behavior is never copied."""
    if type(config) is not RuntimeConfig or type(query) is not str:
        raise TypeError('only a query string and minimal RuntimeConfig are accepted')
    from agentic_rag import AgentState, AgenticRAGController, record_execution_error, trace_for_state
    state = AgentState(query=query.strip(), run_id=run_id or uuid.uuid4().hex)
    observer = Observer(state, secrets=(getattr(client, 'api_key', ''),))
    wrapped_client = ObservedClient(client, observer)
    controller = AgenticRAGController(ObservedPipeline(pipeline, observer), wrapped_client, **config.flags)
    try:
        controller.run(query, run_id=state.run_id, state=state)
    except Exception as exc:
        record_execution_error(state, exc)
    return state, trace_for_state(state, wrapped_client), {'events': observer.events, 'metadata': observer.metadata(config.flags)}


class AttemptLedger:
    """One exclusive directory per query; started and terminal files are fsynced.

    The per-query files are authoritative. An interrupted/partial record is an
    ambiguous attempt and is never replayed. Terminal status is execution status,
    independent of answer quality/status.
    """
    def __init__(self, directory):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)

    def path(self, query_id):
        if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*', query_id) or query_id in ('.', '..'):
            raise ValueError('unsafe query ID')
        return self.directory / query_id

    def status(self, query_id):
        path = self.path(query_id)
        if not path.exists():
            return 'never_started'
        try:
            started = json.loads((path / 'started.json').read_text())
            assert started['status'] == 'started'
            assert started['query_id'] == query_id
            terminal = json.loads((path / 'terminal.json').read_text())
            assert terminal['status'] in ('completed', 'error')
            assert terminal['query_id'] == query_id
            return terminal['status']
        except (OSError, ValueError, KeyError, AssertionError):
            return 'ambiguous'

    def start(self, query_id):
        path = self.path(query_id)
        path.mkdir(exist_ok=False)
        sync_dir(self.directory)
        run_id = uuid.uuid4().hex
        exclusive_json(path / 'started.json', {'query_id': query_id, 'status': 'started',
            'run_id': run_id, 'timestamp': datetime.now(timezone.utc).isoformat()})
        return run_id

    def finish(self, query_id, status, output_hash):
        path = self.path(query_id)
        if status not in ('completed', 'error') or not (path / 'started.json').is_file():
            raise ValueError('invalid terminal transition')
        exclusive_json(path / 'terminal.json', {'query_id': query_id, 'status': status,
            'output_sha256': output_hash, 'timestamp': datetime.now(timezone.utc).isoformat()})


def produce(rows, config, pipeline, client, output, *, expected_hash=QUERY_HASH, expected_count=31):
    validate_queries(rows, expected_hash, expected_count)
    output = Path(output)
    if (output / 'production_seal.json').exists():
        raise FileExistsError('production is sealed')
    output.mkdir(parents=True, exist_ok=True)
    # Prevent concurrent workers from advancing different queries out of order.
    lock = output / 'worker.lock'
    with lock.open('a') as handle:
        import fcntl
        fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        binding = dict(variant=config.alias, config_hash=CONFIG_HASHES[config.alias], query_hash=digest(rows))
        binding_path = output / 'run_binding.json'
        if binding_path.exists():
            if json.loads(binding_path.read_text()) != binding:
                raise ValueError('resume configuration/query identity drift')
        else:
            exclusive_json(binding_path, binding)
        ledger = AttemptLedger(output / 'attempts')
        for row in rows:
            qid = row['query_id']
            status = ledger.status(qid)
            if status == 'ambiguous':
                raise RuntimeError('ambiguous in-flight attempt: ' + qid)
            if status != 'never_started':
                continue
            if any((output / relative).exists() for relative in (qid + '.json', 'outputs/' + qid + '.json', 'observations/' + qid + '.json')):
                raise RuntimeError('orphan output without attempt: ' + qid)
            run_id = ledger.start(qid)
            state, trace, sidecar = run_query(row['query'], config, pipeline, client, run_id=run_id)
            # Persist original trace without extra observer metadata.
            exclusive_json(output / (qid + '.json'), trace)
            exclusive_json(output / 'observations' / (qid + '.json'), sidecar)
            envelope = dict(query_id=qid, query=row['query'], status=state.final_status,
                            trace=trace, generation_error=state.execution_error)
            target = output / 'outputs' / (qid + '.json')
            exclusive_json(target, envelope)
            ledger.finish(qid, 'error' if state.execution_error else 'completed', file_hash(target))
        seal_production(output, rows, config)


def seal_production(output, rows, config):
    output = Path(output)
    ledger = AttemptLedger(output / 'attempts')
    for row in rows:
        if ledger.status(row['query_id']) not in ('completed', 'error'):
            raise RuntimeError('cannot seal unfinished production')
        terminal = json.loads((ledger.path(row['query_id']) / 'terminal.json').read_text())
        if terminal['output_sha256'] != file_hash(output / 'outputs' / (row['query_id'] + '.json')):
            raise ValueError('terminal output hash mismatch')
        for relative in (row['query_id'] + '.json', 'observations/' + row['query_id'] + '.json'):
            if not (output / relative).is_file():
                raise ValueError('missing trace/observer artifact')
    # Ordered convenience journals are assembled only from already durable records.
    # Per-query attempt files remain authoritative during an interrupted run.
    journals = {'production_outputs.jsonl': [output / 'outputs' / (r['query_id'] + '.json') for r in rows],
                'production_attempts.jsonl': [ledger.path(r['query_id']) / name for r in rows for name in ('started.json', 'terminal.json')]}
    for name, records in journals.items():
        content = b''.join(canonical(json.loads(p.read_text())) + b'\n' for p in records)
        path = output / name
        if path.exists():
            if path.read_bytes() != content:
                raise ValueError('partial or mismatched sealing journal')
        else:
            exclusive_bytes(path, content)
    paths = [p for p in sorted(output.rglob('*')) if p.is_file() and p.name != 'worker.lock']
    exclusive_json(output / 'production_seal.json', dict(schema='phase5-production-seal-v0',
        variant=config.alias, config_hash=CONFIG_HASHES[config.alias], query_hash=digest(rows),
        query_ids=[r['query_id'] for r in rows], producer_pid=os.getpid(),
        files={str(p.relative_to(output)): file_hash(p) for p in paths}))


def runtime_allowlist(output, query_input, cache):
    modules = ['agentic_rag', 'bm25_baseline', 'citation_validator', 'dense_baseline',
               'evidence_formatter', 'llm_client', 'rag_baseline', 'reranker_baseline',
               'response_formatter', 'retrieval_pipeline', 'phase5_ablation_runner',
               'phase5_common', 'phase5_isolation', 'phase5_observer', 'phase5_assets']
    files = [ROOT / 'scripts' / (n + '.py') for n in modules]
    files += [query_input, ROOT / 'prompts/legal_rag_v0.txt', ROOT / 'data/versions/corpus-v0.1/chunks.jsonl']
    roots = {Path(sysconfig.get_path(k)).resolve() for k in ('stdlib', 'platstdlib', 'purelib', 'platlib')}
    roots.update([Path(cache).resolve(), ROOT / 'data/indexes/dense-jina-v3-v0'])
    return ReadGuard(files=files, directories=roots, writable=[output], source_directory=ROOT / 'scripts')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--variant', choices=list(CONFIG_HASHES), required=True)
    parser.add_argument('--query-input', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--runtime-lock', type=Path, required=True)
    parser.add_argument('--lock-sha256', required=True)
    parser.add_argument('--execute-phase5b2', action='store_true', help='Future production only, after external review')
    args = parser.parse_args()
    if not args.execute_phase5b2:
        parser.error('production requires separately authorized --execute-phase5b2')
    worker(args.variant, args.query_input, args.output, args.runtime_lock, args.lock_sha256)


def worker(alias, query_input, output, lock_path, lock_hash):
    """Fresh-process production entry point; never called during Phase 5B.1."""
    config = RuntimeConfig(alias)
    output, query_input, lock_path = Path(output).absolute(), Path(query_input).absolute(), Path(lock_path).absolute()
    if any(p.resolve() != p for p in (output, query_input, lock_path)):
        raise ValueError('worker paths must not use symlink aliases')
    if lock_path.parent.parent != Path('/tmp') or not lock_path.parent.name.startswith('phase5-runtime-lock-') or lock_path.name != 'runtime_lock.json':
        raise ValueError('only a trusted temporary runtime lock may enter the worker')
    if output != ROOT / 'data/rag/traces/phase5' / VARIANT_IDS[alias]:
        raise ValueError('production output namespace mismatch')
    if query_input != ROOT / 'data/evaluation/generation/phase5/query_inputs_v0.json':
        raise ValueError('production input path mismatch')
    if file_hash(lock_path) != lock_hash:
        raise ValueError('runtime lock hash mismatch')
    lock = json.loads(lock_path.read_text())
    if set(lock) != {'schema', 'config_hashes', 'query_hash', 'runtime_files', 'asset_files', 'cache', 'packages', 'python_version', 'loaded_pipeline', 'endpoint'}:
        raise ValueError('runtime lock schema mismatch')
    if lock['schema'] != 'phase5-runtime-lock-v0' or lock['config_hashes'] != CONFIG_HASHES or lock['query_hash'] != QUERY_HASH:
        raise ValueError('runtime lock identity mismatch')
    if (os.environ.get('RAG_LLM_MODEL', '').strip() != lock['endpoint']['model']
            or digest(os.environ.get('RAG_LLM_BASE_URL', '').strip()) != lock['endpoint']['base_url_canonical_sha256']):
        raise ValueError('endpoint differs from preflight')
    # The trusted parent supplies only a minimal lock, never a full design object.
    from phase5_assets import environment, inspect_loaded_pipeline
    current = environment()
    if current['packages'] != lock['packages'] or current['python_version'] != lock['python_version']:
        raise ValueError('execution environment differs from preflight')
    output.mkdir(parents=True, exist_ok=True)
    scratch = output / 'runtime_cache'
    scratch.mkdir(exist_ok=True)
    os.environ.update(HF_HUB_OFFLINE='1', TRANSFORMERS_OFFLINE='1', HF_HUB_DISABLE_TELEMETRY='1',
                      HF_MODULES_CACHE=str(scratch / 'modules'), TMPDIR=str(scratch),
                      HF_TOKEN_PATH=str(scratch / 'unused_hub_token'), HF_HUB_DISABLE_IMPLICIT_TOKEN='1',
                      HF_HUB_CACHE=lock['cache'], PYTHONDONTWRITEBYTECODE='1')
    sys.dont_write_bytecode = True
    import tempfile
    tempfile.tempdir = str(scratch)
    guard = runtime_allowlist(output, query_input, lock['cache'])
    with guard:
        for path, expected in {**lock['runtime_files'], **lock['asset_files']}.items():
            if file_hash(path) != expected:
                raise ValueError('runtime/asset drift: ' + path)
        rows = validate_queries(json.loads(query_input.read_text()), QUERY_HASH)
        from retrieval_pipeline import RetrievalPipeline
        from llm_client import client_from_env
        from agentic_rag import require_expected_model
        pipeline = RetrievalPipeline()
        actual = inspect_loaded_pipeline(pipeline)
        if actual != lock['loaded_pipeline']:
            raise ValueError('loaded pipeline differs from preflight certificate')
        client = client_from_env()
        require_expected_model(client)
        if client.timeout != 120.0:
            raise ValueError('client timeout drift')
        ready_path = output / 'loaded_environment.json'
        if ready_path.exists():
            if json.loads(ready_path.read_text()) != actual:
                raise ValueError('loaded environment changed on resume')
        else:
            exclusive_json(ready_path, actual)
        produce(rows, config, pipeline, client, output)


if __name__ == '__main__':
    main()
