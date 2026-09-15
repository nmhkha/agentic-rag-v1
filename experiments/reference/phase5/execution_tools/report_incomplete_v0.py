"""Fail-closed Phase 5B.2 audit. Does not judge, repair seals, or load gold."""
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean, median

ROOT = Path('/home/minhkha/kk/TTTN/legal-agentic-rag')
sys.path.insert(0, str(ROOT/'scripts'))
from phase5_common import canonical, exclusive_json, exclusive_bytes, file_hash, digest
from phase5_ablation_runner import VARIANT_IDS, CONFIG_HASHES, QUERY_HASH
from phase5_analyze import verify_seal
from phase5_preflight import load_design, integrity

BASE=ROOT/'data/evaluation/generation/phase5'
TRACE=ROOT/'data/rag/traces/phase5'
METRICS=('answer_completeness_macro','answer_completeness_micro','supported_required_points',
    'citation_completeness_macro','citation_completeness_micro','citation_correctness_macro',
    'citation_correctness_micro','groundedness_macro','groundedness_micro',
    'unsupported_claim_rate_macro','unsupported_claim_rate_micro','citation_syntax_validity')

def stats(values):
    return dict(total=sum(values),mean=mean(values),median=median(values),max=max(values),query_count=len(values))

def main():
    design=load_design()
    integrity(design)
    env=json.loads((BASE/'execution_environment_v0.json').read_text())
    queries=json.loads((BASE/'query_inputs_v0.json').read_text())
    qids=[q['query_id'] for q in queries]
    assert len(qids)==31 and qids==design['query_order'] and digest(queries)==QUERY_HASH
    assert not any((BASE/v/'records').exists() for v in VARIANT_IDS.values()), 'Unexpected semantic evaluation records'
    audits={}
    metrics={}
    manifests={}
    for alias,variant in VARIANT_IDS.items():
        directory=TRACE/variant
        seal=json.loads((directory/'production_seal.json').read_text())
        assert seal['variant']==alias and seal['config_hash']==CONFIG_HASHES[alias]
        assert seal['query_hash']==QUERY_HASH and seal['query_ids']==qids
        assert file_hash(BASE/variant/'variant_manifest.json')==CONFIG_HASHES[alias]
        audit=[]
        for rel,expected in seal['files'].items():
            path=directory/rel
            actual=file_hash(path) if path.is_file() else None
            audit.append(dict(path=rel,expected_sha256=expected,actual_sha256=actual,
                status='PASS' if expected==actual else 'MISSING' if actual is None else 'CHANGED'))
        try:
            verify_seal(directory)
            verification=dict(status='PASS',error=None)
        except Exception as exc:
            verification=dict(status='FAIL',error=dict(type=type(exc).__name__,message=str(exc)))
        audits[alias]=dict(frozen_verifier=verification,production_seal_sha256=file_hash(directory/'production_seal.json'),
            files=audit,failed_files=[a for a in audit if a['status']!='PASS'],
            non_runtime_cache_files_pass=all(a['status']=='PASS' for a in audit if not a['path'].startswith('runtime_cache/')))
        rows=[]
        attempts=[]
        observations={}
        errors=[]
        assert {p.stem for p in (directory/'outputs').glob('*.json')}==set(qids)
        assert {p.name for p in (directory/'attempts').iterdir()}==set(qids)
        for query in queries:
            qid=query['query_id']
            start=json.loads((directory/'attempts'/qid/'started.json').read_text())
            terminal=json.loads((directory/'attempts'/qid/'terminal.json').read_text())
            output=json.loads((directory/'outputs'/(qid+'.json')).read_text())
            trace=json.loads((directory/(qid+'.json')).read_text())
            observer=json.loads((directory/'observations'/(qid+'.json')).read_text())
            assert start['query_id']==terminal['query_id']==output['query_id']==qid
            assert start['run_id']==trace['run_id'] and trace==output['trace']
            assert output['query']==query['query']
            assert terminal['output_sha256']==file_hash(directory/'outputs'/(qid+'.json'))
            assert terminal['status']==('error' if output['generation_error'] else 'completed')
            events=observer['events']
            counts={kind:sum(e['logical_call_type']==kind for e in events) for kind in ('retrieval','llm','merge_rerank')}
            assert counts['llm']==len(trace['llm_calls'])
            assert sum(e['logical_call_type']=='retrieval' and e['status']=='success' for e in events)==len(trace['retrieval_calls'])
            counts.update(failed_calls=dict(Counter(e['logical_call_type'] for e in events if e['status']=='error')),
                stages=dict(Counter(e['stage'] for e in events)),
                successful_trace_retrieval_calls=len(trace['retrieval_calls']),
                observable_http_attempts=sum(e['observable_http_attempts'] for e in events if e['logical_call_type']=='llm' and isinstance(e['observable_http_attempts'],int)),
                unknown_transport_logical_calls=sum(e['logical_call_type']=='llm' and e['observable_http_attempts']=='unknown' for e in events))
            observations[qid]=counts
            attempts.extend([start,terminal])
            rows.append(output)
            if output['generation_error']:
                errors.append(dict(query_id=qid,error=output['generation_error']))
        assert (directory/'production_outputs.jsonl').read_bytes()==b''.join(canonical(r)+b'\n' for r in rows)
        assert (directory/'production_attempts.jsonl').read_bytes()==b''.join(canonical(r)+b'\n' for r in attempts)
        audits[alias]['ledger_trace_observer_reconciliation']='PASS'
        metrics[alias]=dict(schema='phase5b2-blocked-metrics-v0',status='INCOMPLETE / INSUFFICIENT EVIDENCE',
            benchmark_query_count=31,benchmark_required_point_count=102,production_attempt_count=31,
            successful_production_count=31-len(errors),judged_count=0,evaluator_attempt_count=0,
            blocked_judgment_count=31,blocked_query_ids=qids,production_errors=errors,judge_failure_count=0,
            semantic_evaluation_executed=False,primary_metrics={k:None for k in METRICS},
            available_case_metrics=None,available_case_denominator=0,
            interpretation='Insufficient evidence',
            reason='Frozen production seal verification fails; semantic evaluation was never entered.',
            efficiency=dict(per_query=observations,totals={k:stats([o[k] for o in observations.values()]) for k in ('retrieval','llm','merge_rerank')},
                observable_http_attempts=sum(o['observable_http_attempts'] for o in observations.values()),
                unknown_transport_logical_calls=sum(o['unknown_transport_logical_calls'] for o in observations.values()),
                provider_internal_retries='unknown',evaluator_calls_excluded=True,token_records='unavailable',monetary_cost='unavailable'),
            savings_vs_R2=None,comparative_analysis_executed=False)
        manifests[alias]=dict(schema='phase5b2-incomplete-run-manifest-v0',variant=alias,variant_id=variant,
            config_sha256=CONFIG_HASHES[alias],variant_manifest_sha256=file_hash(BASE/variant/'variant_manifest.json'),
            query_order=qids,query_hash=QUERY_HASH,environment_sha256=file_hash(BASE/'execution_environment_v0.json'),
            design_sha256=dict(manifest=file_hash(BASE/'phase5a_ablation_manifest_v0.json'),specification=file_hash(BASE/'phase5a_ablation_spec_v0.md')),
            frozen_source_sha256=env['preflight_rerun']['implementation_hashes'],
            start_utc=attempts[0]['timestamp'],end_production_utc=attempts[-1]['timestamp'],
            query_run_ids={a['query_id']:a['run_id'] for a in attempts if a['status']=='started'},
            production_attempt_count=31,evaluator_attempt_count=0,production_seal_created=True,
            production_seal_verified=verification['status']=='PASS',production_seal_sha256=file_hash(directory/'production_seal.json'),
            production_files=seal['files'],completion='INCOMPLETE / INSUFFICIENT EVIDENCE',
            production_errors=errors,seal_verification=verification,
            analysis_source_sha256=file_hash(__file__),evaluation_start_utc=None,evaluation_end_utc=None)
    assert any(a['frozen_verifier']['status']=='FAIL' for a in audits.values()), 'No seal blocker; use trusted evaluator instead'
    # Verify the frozen scheduler respected complete sequential passes.
    assert manifests['R2']['end_production_utc']<=manifests['A1']['start_utc']
    assert manifests['A1']['end_production_utc']<=manifests['A2']['start_utc']
    exclusive_json(BASE/'production_seal_validation_v0.json',dict(status='FAIL',variants=audits,
        root_cause='seal_production recursively includes runtime_cache temporary files. PyTorch TemporaryDirectory cleanup removes generated code at normal worker exit.',
        source_evidence=dict(sealer='scripts/phase5_ablation_runner.py:172',temporary_directory='.venv/lib/python3.12/site-packages/torch/distributed/nn/jit/instantiator.py:20'),
        repair_performed=False,semantic_evaluation_executed=False,production_order_verified=True))
    blocker=dict(type='EvaluationBlockedByProductionSeal',stage='pre_evaluation_seal_verification',
        message='At least one mandatory production seal fails the unchanged frozen verifier; no judge request was made.',
        details_path='production_seal_validation_v0.json')
    for alias,variant in VARIANT_IDS.items():
        directory=BASE/variant
        blocked=[dict(query_id=q['query_id'],query=q['query'],evaluation_status='BLOCKED_NOT_ATTEMPTED',
            evaluation_attempted=False,evaluation_attempts=0,evaluation_error=blocker,
            answer_completeness=None,citation_completeness=None,citation_correctness=None,groundedness=None,unsupported_claim_rate=None,
            production_output_path=str((TRACE/variant/'outputs'/(q['query_id']+'.json')).relative_to(ROOT))) for q in queries]
        exclusive_bytes(directory/'evaluation.jsonl',b''.join(canonical(r)+b'\n' for r in blocked))
        exclusive_bytes(directory/'evaluation_attempts.jsonl',b'')
        exclusive_json(directory/'metrics.json',metrics[alias])
        manifests[alias].update(efficiency=metrics[alias]['efficiency'],evaluation_error=blocker,
            report_artifact_hashes={p.name:file_hash(p) for p in directory.iterdir() if p.is_file()},
            recorded_utc=datetime.now(timezone.utc).isoformat())
        exclusive_json(directory/'run_manifest.json',manifests[alias])
    for name,reference,comparator in [('replication_R1_R2.json','R1','R2'),('contrast_R2_A1.json','R2','A1'),('contrast_R2_A2.json','R2','A2')]:
        exclusive_json(BASE/name,dict(status='INCOMPLETE / INSUFFICIENT EVIDENCE',reference=reference,comparator=comparator,
            analysis_executed=False,interpretation='Insufficient evidence',reason=blocker,query_count=31,required_point_count=102,
            per_query=[dict(query_id=q,reference_metrics=None,comparator_metrics=None,delta=None,error=blocker) for q in qids],
            transition_partition=None,paired_statistics=None,replication_flags=None,trigger_strata=None,
            bootstrap=dict(executed=False,resamples=10000,seed=20260906,sample_size=31,ci95=None),
            historical_R1_unchanged=True))
    after={p:dict(before_sha256=v['before_sha256'],after_sha256=file_hash(ROOT/p)) for p,v in env['before_integrity'].items()}
    assets={p:dict(before_sha256=h,after_sha256=file_hash(p)) for p,h in env['runtime_lock']['asset_files'].items()}
    unchanged=all(v['before_sha256']==v['after_sha256'] for v in [*after.values(),*assets.values()])
    exclusive_json(BASE/'integrity_before_after_v0.json',dict(status='PASS' if unchanged else 'FAIL',files=after,asset_files=assets))
    report=render(metrics,audits,unchanged,qids)
    exclusive_bytes(BASE/'phase5b_report_v0.md',report.encode())
    exclusive_json(BASE/'report_artifact_hashes_v0.json',dict(
        files={str(p.relative_to(BASE)):file_hash(p) for p in sorted(BASE.rglob('*')) if p.is_file()},
        purpose='Audit artifact inventory only; does not replace or amend any production seal.'))
    print(report)

def render(metrics,audits,unchanged,qids):
    lines=['Phase 5B.2 status: '+('INCOMPLETE' if unchanged else 'FAIL'),'','PRODUCTION']
    lines += [f"{a}: {m['successful_production_count']}/31 completed" for a,m in metrics.items()]
    lines += ['','All three planned production passes finished in order R2 → A1 → A2. No production query was rerun.',
        'Production seal verification: FAIL. The unchanged verifier rejects missing temporary runtime files.',
        'The original seals and every surviving production artifact are preserved. No seal entry was removed or repaired.','', 'EVALUATION']
    lines += [f'{a}: 0/31 judged' for a in metrics]
    lines += ['No trusted evaluator process or semantic judge request was launched. evaluation.jsonl contains explicitly marked BLOCKED_NOT_ATTEMPTED envelopes, not judgments. evaluation_attempts.jsonl is empty.',
        '', 'R1 → R2 REPLICATION', 'AC macro: N/A', 'AC micro: N/A', 'Net required-point change: N/A', 'Gross point churn: N/A',
        'Replication variability assessment: unavailable; R2 has no valid judgments. Historical R1 was not reevaluated or replaced.']
    for a,title in [('A1','NO ANSWER REVISION'),('A2','NO EVIDENCE EXPANSION')]:
        lines += ['',f'R2 vs {a} — {title}','Status: INCOMPLETE / INSUFFICIENT EVIDENCE',
            'R2 AC macro: N/A',f'{a} AC macro: N/A','Delta: N/A',
            'R2 AC micro: N/A',f'{a} AC micro: N/A','Delta: N/A',
            'Points lost by ablation: N/A','Points gained by ablation: N/A','Net R2 contribution: N/A',
            f'R2 better / tied / {a} better: N/A / N/A / N/A','95% paired bootstrap CI: N/A (not executed)',
            'R2-triggered query count: N/A (comparative analysis not entered)',
            'Production LLM calls saved: N/A','Retrieval calls saved: N/A','Merge-reranks saved: N/A',
            'Interpretation: Insufficient evidence']
    lines += ['','SAFETY / CITATION','Citation Completeness: N/A','Citation Correctness: N/A',
        'Groundedness macro/micro: N/A / N/A','Unsupported Claim Rate macro/micro: N/A / N/A','Citation syntax validity: N/A',
        'All quality metrics, point transitions, bootstrap results, trigger strata and replication-attribution flags are withheld. The declared denominator remains 31 queries / 102 required points; nothing is imputed.',
        '', 'EFFICIENCY','Per-run production diagnostics only; comparative analysis remains blocked.','',
        '| Run | Retrieval total / mean / median / max | LLM total / mean / median / max | Merge-reranks | Observed HTTP submissions |',
        '|---|---|---|---|---|']
    for a,m in metrics.items():
        cost=m['efficiency']['totals']
        values=[' / '.join(str(cost[k][x]) for x in ('total','mean','median','max')) for k in ('retrieval','llm')]
        lines.append(f"| {a} | {' | '.join(values)} | {cost['merge_rerank']['total']} | {m['efficiency']['observable_http_attempts']} |")
    lines += ['','Evaluator calls: 0. Provider-internal retries and token/cost records: unavailable.',
        'Historical R0 contextual baseline only: configured logical 31 retrieval + 31 generation calls, mean/median/max 1. No measured Standard HTTP cost is claimed.',
        '', 'ERRORS']
    for a,m in metrics.items():
        lines.append(f"{a} production errors: "+json.dumps(m['production_errors'],ensure_ascii=False))
        lines.append(f'{a} evaluation errors: 0 judge failures; 31 judgments blocked before evaluator entry.')
        lines.append(f'{a} exact blocked query IDs: '+', '.join(qids))
        lines.append(f'{a} seal failures:')
        lines.extend('- `'+f['path']+'`: '+f['status']+'; expected SHA-256 `'+f['expected_sha256']+'`.' for f in audits[a]['failed_files'])
        lines.append(f"{a} ledger/trace/observer reconciliation: {audits[a]['ledger_trace_observer_reconciliation']}; non-runtime-cache artifact hashes: "+('PASS' if audits[a]['non_runtime_cache_files_pass'] else 'FAIL'))
    lines += ['','The sealer inventories every file below the production output directory, including runtime_cache. PyTorch creates its remote-module Python file in a TemporaryDirectory, which disappears on normal worker exit. The seal therefore references a file that no longer exists when a separate evaluator checks it. This lifecycle failure was not detected by the passing preflight tests.',
        'Evidence: scripts/phase5_ablation_runner.py:172; scripts/phase5_analyze.py:23; .venv/lib/python3.12/site-packages/torch/distributed/nn/jit/instantiator.py:20.',
        '', 'INTEGRITY','Frozen artifact hashes unchanged: '+('PASS' if unchanged else 'FAIL'),
        'Before/after hashes are recorded in integrity_before_after_v0.json, including pre-Phase-5B.2 artifacts and pinned runtime/model assets.',
        'Pre-execution gates: 36/36 tests PASS; all 262 initially certified file hashes matched; offline model/tokenizer/configuration/package/endpoint certificates matched Phase 5B.1.',
        'The runtime seal failure is separate from frozen source/design/model drift. No frozen source, design, Phase 5B.1 artifact, model asset, prompt, gold, R0 or R1 was repaired or overwritten.',
        '', 'EXPERIMENTAL CLAIM','Controlled single-run ablation evidence only; no quality or contribution claim is available because semantic evaluation is blocked.',
        'Causal/general claims remain limited by benchmark size and observed replication variability. Replication variability was not measured in this incomplete execution.',
        '', 'Ready for Phase 5C:','NO','','STOP. No Agentic v1 changes, A3/A4 runs, or Phase 5C work were performed.','']
    return '\n'.join(lines)

if __name__=='__main__':
    main()
