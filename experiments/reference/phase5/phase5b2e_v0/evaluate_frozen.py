"""Trusted, additive Phase 5B.2-E execution; no production entry points."""
from __future__ import annotations
import argparse
import copy
import fcntl
import json
import os
from pathlib import Path
import shlex
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / 'scripts'))
from phase5_common import canonical, digest, exclusive_json, exclusive_bytes, file_hash
from phase5_seal_recovery_v1 import verify, VARIANTS, MANIFEST, PROTOCOL
from phase5_durable_seal_v1 import read_json, require, verify_pair

BASE = ROOT / 'data/evaluation/generation/phase5'
OUT = Path(__file__).resolve().parent
ANCHOR = '60f2c25b82082e41d466439afa0d93106484ca8fb4cdd41bbdb35cd1f83282bc'
SOURCES = ['scripts/evaluate_agentic_rag.py', 'scripts/evaluate_standard_rag.py',
           'scripts/citation_validator.py', 'scripts/evidence_formatter.py',
           'scripts/llm_client.py', 'scripts/phase5_analyze.py']

def now():
    return datetime.now(timezone.utc).isoformat()

def append(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('ab') as stream:
        stream.write(canonical(value) + b'\n')
        stream.flush()
        os.fsync(stream.fileno())

def snapshot():
    return {str(p.relative_to(ROOT)): file_hash(p)
            for top in ('scripts', 'tests', 'prompts', 'data')
            for p in sorted((ROOT / top).rglob('*'))
            if p.is_file() and not p.is_relative_to(OUT)}

def gate():
    # The unchanged independent recovery verifier also checks historical sources,
    # observer/trace/ledger equality, query-only inputs and all pinned model assets.
    verify(ROOT, ANCHOR)
    manifest, protocol = read_json(ROOT / MANIFEST), read_json(ROOT / PROTOCOL)
    require(manifest['status'] == 'PASS' and manifest['eligible_for_semantic_evaluation'],
            'recovery not eligible')
    projection = read_json(BASE / 'query_inputs_v0.json')
    results = {a: verify_pair(ROOT / p['directory'], projection, p,
               manifest['protocol_sha256'], project_root=ROOT)
               for a, p in protocol['variants'].items()}
    return dict(status='PASS', external_manifest_sha256=ANCHOR,
                variants={a: dict(status='PASS', reconciliation=results[a]) for a in VARIANTS},
                original_seals_historical_status='FAILED_EPHEMERAL_LIFECYCLE',
                authorization='Explicit user Phase 5B.2-E request; recovery eligibility plus original and supplemental seals')

def joined():
    # Only this trusted evaluator process loads reference annotations.
    from evaluate_standard_rag import load_verified_dataset
    _, items, _ = load_verified_dataset()
    projection = [{'query_id': i['query_id'], 'query': i['query']} for i in items]
    require(projection == read_json(BASE / 'query_inputs_v0.json'), 'gold query identity mismatch')
    universe = {(i['query_id'], p['point_id']) for i in items for p in i['required_points']}
    require(len(items) == 31 and len(universe) == sum(len(i['required_points']) for i in items) == 102,
            'gold count/point uniqueness mismatch')
    records = {}
    for alias, variant in VARIANTS.items():
        directory = ROOT / 'data/rag/traces/phase5' / variant
        rows = [read_json(directory / 'outputs' / (i['query_id'] + '.json')) for i in items]
        require(len(rows) == len({r['query_id'] for r in rows}) == 31, 'production record count')
        require([{'query_id': r['query_id'], 'query': r['query']} for r in rows] == projection,
                'production query mismatch')
        require(all(r['generation_error'] is None for r in rows), 'production error')
        records[alias] = rows
    return items, records

def prepare():
    result = gate()
    items, records = joined()
    before = snapshot()
    for filename, value in {
        'integrity_before.json': before,
        'recovery_gate.json': result,
        'evaluation_protocol.json': dict(schema='phase5b2e-protocol-v0', created_utc=now(),
            order=list(VARIANTS), query_order=[i['query_id'] for i in items], gold_queries=31,
            unique_required_point_tuples=102, production_record_counts={a: len(r) for a,r in records.items()},
            model='gemini-3.5-flash-lite', temperature=0, max_evaluator_attempts=3,
            frozen_functions=['evaluate_record', 'judge_prompt', 'parse_judge', 'point_audit', 'validate_citations'],
            evaluator_source_sha256={p: file_hash(ROOT / p) for p in SOURCES},
            gold_sha256=file_hash(ROOT / 'data/evaluation/generation/generation_eval_v1_verified.json'),
            harness_sha256=file_hash(__file__), python=sys.version, production_reruns=0,
            path_policy='Additive phase5b2e_v0 namespace preserves every recovery-pinned historical placeholder at its original path.',
            user_request_sha256='beyond protocol: attached request retained by session',
            bootstrap=read_json(BASE / 'phase5a_ablation_manifest_v0.json')['analysis_plan']['bootstrap'])
    }.items():
        exclusive_json(OUT / filename, value)
    print('PREPARED: recovery R2/A1/A2 PASS; exact 31/31/31/31 query joins; 102 unique points; production calls 0.', flush=True)

def production_guard(frame, event, arg):
    if event != 'call':
        return
    filename = Path(frame.f_code.co_filename)
    if filename.parent != ROOT / 'scripts':
        return
    module, function = filename.stem, frame.f_code.co_name
    forbidden = (module in {'phase5_ablation_runner', 'phase5_assets'}
        or module == 'agentic_rag' and function not in {'<module>', 'AgentState', 'CoverageCheck',
            'CompletenessCheck', 'AgenticRAGController'}
        or module in {'reranker_baseline', 'dense_retrieval_baseline', 'bm25_baseline'}
        or module == 'retrieval_pipeline' and function in {'__init__', 'retrieve', 'retrieve_candidates', 'rerank'}
        or module == 'rag_baseline' and function == 'run_rag'
        or module == 'evaluate_agentic_rag' and function in {'main', 'evaluate_item'}
        or module == 'evaluate_standard_rag' and function in {'main', 'result_for_item'})
    if forbidden:
        raise RuntimeError('Production entry prohibited: ' + module + '.' + function)

def execute():
    gate()
    protocol = read_json(OUT / 'evaluation_protocol.json')
    require(file_hash(__file__) == protocol['harness_sha256'], 'harness changed since preparation')
    require(sys.version == protocol['python'], 'Python changed')
    for p,h in protocol['evaluator_source_sha256'].items():
        require(file_hash(ROOT / p) == h, 'evaluator source changed')
    items, records = joined()
    from evaluate_agentic_rag import evaluate_record
    from evaluate_standard_rag import parse_judge
    from phase5_analyze import DurableJudgeClient
    from llm_client import client_from_env
    for line in (ROOT / '.env').read_text().splitlines():
        name, sep, value = line.removeprefix('export ').partition('=')
        name = name.strip()
        if sep and name in ('RAG_LLM_MODEL','RAG_LLM_BASE_URL','RAG_LLM_API_KEY') and not os.environ.get(name):
            parts = shlex.split(value, comments=True)
            require(len(parts) == 1, 'invalid endpoint configuration')
            os.environ[name] = parts[0]
    client = client_from_env()
    endpoint = read_json(BASE / 'phase5b1_preflight_manifest_v0.json')['endpoint']
    require(client.model == endpoint['model'] == 'gemini-3.5-flash-lite', 'model drift')
    require(digest(client.base_url.strip()) == endpoint['base_url_canonical_sha256'], 'endpoint drift')
    require(client.timeout == 120.0, 'timeout drift')
    sys.setprofile(production_guard)
    with (OUT / 'evaluator.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        for alias, variant in VARIANTS.items():
            directory = OUT / variant
            results = []
            for item, production in zip(items, records[alias]):
                qid = item['query_id']
                target = directory / 'records' / (qid + '.json')
                if target.exists():
                    record = read_json(target)
                    require(record['query_id'] == qid and record['query'] == item['query']
                            and record['trace'] == production['trace'], 'cached evaluation mismatch')
                else:
                    durable = DurableJudgeClient(client, directory / 'attempts' / qid)
                    class LoggedJudge:
                        def generate(self, prompt):
                            slot = durable.index + 1
                            cached = (durable.directory / str(slot) / 'request.json').exists()
                            entry = dict(variant=alias, query_id=qid, attempt=slot,
                                         started_utc=now(), prompt_sha256=digest(prompt), replay=cached)
                            try:
                                raw = durable.generate(prompt)
                                try:
                                    parse_judge(raw, [p['point_id'] for p in item['required_points']])
                                except Exception as exc:
                                    entry.update(status='parse_error', error_type=type(exc).__name__, error=str(exc))
                                else:
                                    entry.update(status='valid_parsed_judgment', error=None)
                                entry['raw_response_sha256'] = digest(raw)
                                return raw
                            except Exception as exc:
                                message = str(exc).replace(client.api_key, '[REDACTED]')
                                entry.update(status='transport_error', error_type=type(exc).__name__, error=message)
                                raise
                            finally:
                                entry['ended_utc'] = now()
                                append(directory / 'evaluation_attempts.jsonl', entry)
                    record = evaluate_record(item, copy.deepcopy(production), LoggedJudge())
                    record.update(evaluation_status='JUDGED' if record['evaluation_error'] is None else 'FAILED',
                                  evaluated_utc=now(), production_output_sha256=digest(production))
                    exclusive_json(target, record)
                results.append(record)
                print(f"{alias}: {len(results)}/31 processed; {qid}: {record['evaluation_status']}", flush=True)
            journal = b''.join(canonical(r)+b'\n' for r in results)
            if (directory / 'evaluation.jsonl').exists():
                require((directory / 'evaluation.jsonl').read_bytes() == journal, 'evaluation journal changed')
            else:
                exclusive_bytes(directory / 'evaluation.jsonl', journal)
        sys.setprofile(None)
    print('Evaluation pass finished. Production calls/reruns: 0. No quality-dependent changes.', flush=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['prepare', 'evaluate'])
    args = parser.parse_args()
    prepare() if args.command == 'prepare' else execute()
