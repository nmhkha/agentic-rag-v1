"""Offline Phase 5A paired analysis of frozen judgments; never calls a model."""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
import math
import random
from statistics import mean, median
import sys
from pathlib import Path
from evaluate_frozen import (ROOT, BASE, OUT, ANCHOR, VARIANTS, SOURCES, now, gate,
                             read_json, require, file_hash, exclusive_json, exclusive_bytes, canonical)

first_bytes = exclusive_bytes
REFRESH_HASHES = None

def exclusive_bytes(path, data):
    """Only explicitly enumerated derived analysis outputs may be refreshed."""
    path = Path(path)
    if not path.exists():
        return first_bytes(path,data)
    allowed = {OUT/n for n in ('replication_R1_R2.json','contrast_R2_A1.json','contrast_R2_A2.json',
                               'integrity_after.json','console_output.txt','provenance.json')}
    allowed |= {OUT/v/'metrics.json' for v in VARIANTS.values()}
    allowed |= {BASE/n for n in ('phase5b_evaluation_metrics_v0.json','phase5b_evaluation_report_v0.md')}
    require(REFRESH_HASHES is not None and path in allowed, 'refusing to overwrite non-derived or historical artifact')
    require(file_hash(path)==REFRESH_HASHES[str(path.relative_to(ROOT))], 'derived output changed before refresh')
    path.write_bytes(data)

def exclusive_json(path,value):
    exclusive_bytes(path,canonical(value))

FIELDS = ('answer_completeness', 'citation_completeness', 'citation_correctness',
          'groundedness', 'unsupported_claim_rate')
CLAIMS = {'citation_correctness': ('correctly_cited_claim_count', 'cited_claim_count'),
          'groundedness': ('grounded_claim_count', 'claim_count'),
          'unsupported_claim_rate': ('unsupported_claim_count', 'claim_count')}

def rows(path):
    return [__import__('json').loads(s) for s in path.read_text().splitlines() if s]

def ratio(n, d):
    return n / d if d else None

def subtract(a, b):
    return a - b if a is not None and b is not None else None

def stats(values):
    return dict(total=sum(values), mean=mean(values) if values else None,
                median=median(values) if values else None, max=max(values) if values else None,
                query_count=len(values))

def valid(r):
    return r.get('generation_error') is None and r.get('evaluation_error') is None and 'judge' in r

def summarize(records, sizes):
    eligible = [r for r in records if valid(r)]
    denominator = sum(sizes[r['query_id']] for r in records)
    judged_denominator = sum(sizes[r['query_id']] for r in eligible)
    complete = len(eligible) == len(records) and bool(records)
    result = dict(query_count=len(records), judged_count=len(eligible), required_point_count=denominator,
                  judged_point_denominator=judged_denominator, complete=complete,
                  metric_scope='complete' if complete else 'available-case diagnostics only; full-denominator AC/CC withheld',
                  failed_query_ids=[r['query_id'] for r in records if not valid(r)],
                  generation_errors=[dict(query_id=r['query_id'], error=r['generation_error'])
                                     for r in records if r.get('generation_error')],
                  evaluation_errors=[dict(query_id=r['query_id'], error=r.get('evaluation_error'))
                                     for r in records if not valid(r)], anomalies=[])
    for metric, field in [('answer_completeness','supported_point_ids'),
                          ('citation_completeness','citation_supported_point_ids')]:
        n = sum(len(r[field]) for r in eligible)
        value = dict(macro=mean(r[metric] for r in eligible) if eligible else None,
                     macro_query_denominator=len(eligible), micro=ratio(n, judged_denominator),
                     numerator=n, denominator=judged_denominator)
        result[metric] = value if complete else dict(macro=None, micro=None, numerator=None,
            denominator=denominator, available_case_diagnostic=value,
            known_observed_supported_count=n, known_count_benchmark_denominator=denominator)
    for metric, (num, den) in CLAIMS.items():
        defined = [r for r in eligible if r['judge'][den] != 0]
        value = dict(macro=mean(r[metric] for r in defined) if defined else None,
                     macro_query_denominator=len(defined), eligible_judged_queries=len(eligible),
                     pooled_micro=ratio(sum(r['judge'][num] for r in eligible), sum(r['judge'][den] for r in eligible)),
                     numerator=sum(r['judge'][num] for r in eligible), denominator=sum(r['judge'][den] for r in eligible))
        result[metric] = value
    syntax_eligible = [r for r in records if r.get('generation_error') is None and isinstance(r.get('citation_valid'),bool)]
    result['citation_syntax_validity'] = dict(valid=sum(r['citation_valid'] for r in syntax_eligible),
        eligible=len(syntax_eligible), rate=ratio(sum(r['citation_valid'] for r in syntax_eligible),len(syntax_eligible)),
        scope='All completed outputs with deterministic validation, independent of semantic judge success')
    for r in eligible:
        j = r['judge']
        anomalies = []
        if j['grounded_claim_count'] + j['unsupported_claim_count'] != j['claim_count']:
            anomalies.append('grounded + unsupported != claim_count')
        for n,d in CLAIMS.values():
            if j[n] > j[d]:
                anomalies.append(n + ' > ' + d)
        if j['cited_claim_count'] > j['claim_count']:
            anomalies.append('cited_claim_count > claim_count')
        if anomalies:
            result['anomalies'].append(dict(query_id=r['query_id'], anomalies=anomalies, raw_counts={
                k:j[k] for k in ('claim_count','grounded_claim_count','unsupported_claim_count',
                                'cited_claim_count','correctly_cited_claim_count')}))
    return result

def metric_deltas(left, right):
    output = {}
    for m in FIELDS:
        pool = 'micro' if m in FIELDS[:2] else 'pooled_micro'
        output[m] = {k: subtract(left[m][k],right[m][k]) for k in ('macro',pool)}
    output['citation_syntax_validity'] = subtract(left['citation_syntax_validity']['rate'],
                                               right['citation_syntax_validity']['rate'])
    output['oriented_safety_deltas'] = {m: {k: (-v if m=='unsupported_claim_rate' and v is not None else v)
        for k,v in output[m].items()} for m in CLAIMS}
    return output

def ac_fraction(r):
    return Fraction(len(r['supported_point_ids']), len(r['required_point_ids'])) if valid(r) else None

def partition(left, right, universe):
    if not all(valid(r) for r in left + right):
        return None
    ls = {(r['query_id'], p) for r in left for p in r['supported_point_ids']}
    rs = {(r['query_id'], p) for r in right for p in r['supported_point_ids']}
    require(ls <= universe and rs <= universe, 'point support outside universe')
    groups = dict(both_supported=ls&rs, only_reference=ls-rs, only_comparator=rs-ls,
                  neither_supported=universe-(ls|rs))
    require(sum(map(len,groups.values())) == len(universe), 'point partition incomplete')
    return dict(denominator=len(universe), counts={k:len(v) for k,v in groups.items()},
        identities={k:[dict(query_id=q,point_id=p) for q,p in sorted(v)] for k,v in groups.items()},
        net_reference_contribution=len(ls-rs)-len(rs-ls), net_comparator_change=len(rs-ls)-len(ls-rs),
        gross_churn=len(ls-rs)+len(rs-ls))

def point_observations(left,right,universe):
    lmap={r['query_id']:r for r in left}
    rmap={r['query_id']:r for r in right}
    return [dict(query_id=q,point_id=p,
                 reference_supported=(p in lmap[q]['supported_point_ids']) if valid(lmap[q]) else None,
                 comparator_supported=(p in rmap[q]['supported_point_ids']) if valid(rmap[q]) else None)
            for q,p in sorted(universe)]

def bootstrap(deltas):
    require(len(deltas)==31, 'bootstrap requires 31 pairs')
    rng = random.Random(20260906)
    means = sorted(sum(deltas[rng.randrange(31)] for _ in range(31))/31 for _ in range(10000))
    def percentile(p):
        position=(len(means)-1)*p
        lower=math.floor(position)
        return means[lower]+(position-lower)*(means[min(lower+1,len(means)-1)]-means[lower])
    return dict(executed=True,seed=20260906,resamples=10000,sample_size=31,
                unit='paired query',rng='Python random.Random; rng.randrange(31)',python=sys.version,
                seed_reinitialized_for_contrast=True,percentile_method='linear interpolation at (N-1)*p',
                ci95=[percentile(.025),percentile(.975)])

def paired_statistics(left, right, with_ci=False):
    if not left or not all(valid(r) for r in left+right):
        return None
    exact=[ac_fraction(l)-ac_fraction(r) for l,r in zip(left,right)]
    differences=[float(x) for x in exact]
    return dict(mean_ac_difference=float(mean(exact)), median_ac_difference=float(median(exact)),
        reference_better=sum(x>0 for x in exact), tied=sum(x==0 for x in exact),
        comparator_better=sum(x<0 for x in exact), comparator_improved=sum(x<0 for x in exact),
        comparator_equal=sum(x==0 for x in exact), comparator_worsened=sum(x>0 for x in exact),
        exact_mean_ac_difference=str(mean(exact)),
        bootstrap=bootstrap(differences) if with_ci else dict(executed=False,reason='Descriptive summary'))

def cost_record(trace, observer=None):
    if observer is None:
        return dict(retrieval=len(trace['retrieval_calls']), llm=len(trace['llm_calls']),
                    merge_rerank=None, observable_http_submissions=None)
    events=observer['events']
    counts={kind:sum(e['logical_call_type']==kind for e in events) for kind in ('retrieval','llm','merge_rerank')}
    require(counts['retrieval']==len(trace['retrieval_calls'])==trace['retrieval_call_count'], 'retrieval count mismatch')
    require(counts['llm']==len(trace['llm_calls'])==trace['llm_call_count'], 'production LLM count mismatch')
    counts.update(observable_http_submissions=sum(e['observable_http_attempts'] for e in events
        if e['logical_call_type']=='llm' and isinstance(e['observable_http_attempts'],int)),
        unknown_transport_calls=sum(e['logical_call_type']=='llm' and not isinstance(e['observable_http_attempts'],int) for e in events),
        completed_retrieval=sum(e['logical_call_type']=='retrieval' and e['status']=='success' for e in events),
        failed_calls=sum(e['status']!='success' for e in events),
        stages=dict(Counter(e['stage'] for e in events)))
    return counts

def costs_summary(costs, qids):
    selected=[costs[q] for q in qids]
    return dict(query_count=len(qids), totals={k:stats([c[k] for c in selected]) for k in ('retrieval','llm','merge_rerank')},
        observable_http_submissions=sum(c['observable_http_submissions'] for c in selected),
        unknown_transport_calls=sum(c['unknown_transport_calls'] for c in selected),
        completed_retrieval=sum(c['completed_retrieval'] for c in selected),
        failed_calls=sum(c['failed_calls'] for c in selected),
        production_stages=dict(sum((Counter(c['stages']) for c in selected),Counter())),
        evaluator_calls_excluded=True, provider_internal_retries='unknown',tokens='unavailable',monetary_cost='unavailable')

def differences_saved(left,right):
    return {k:left['totals'][k]['total']-right['totals'][k]['total'] for k in ('retrieval','llm','merge_rerank')}

def paired_rows(left,right,left_name,right_name,costs,metadata=None,flag=None):
    result=[]
    for l,r in zip(left,right):
        q=l['query_id']
        require(q==r['query_id'] and l['query']==r['query'], 'paired query mismatch')
        values={name:{k:record.get(k) for k in FIELDS+('citation_valid','status','generation_error','evaluation_error')}
                for name,record in ((left_name,l),(right_name,r))}
        delta={m:subtract(l.get(m),r.get(m)) for m in FIELDS}
        delta['citation_valid']=subtract(int(l['citation_valid']),int(r['citation_valid']))
        if valid(l) and valid(r):
            delta['answer_completeness_exact']=str(ac_fraction(l)-ac_fraction(r))
        row=dict(query_id=q,query=l['query'],metrics=values,raw_delta_direction=left_name+' - '+right_name,
            deltas=delta,costs={left_name:costs[left_name][q],right_name:costs[right_name][q]},
            traces={left_name:l.get('trace_path'),right_name:r.get('trace_path')})
        if metadata is not None:
            key='answer_revision' if flag=='revision_used' else 'expansion'
            md=metadata[right_name][q]
            row.update(R2_intervention_used=l['trace'].get(flag),
                ablation_would_have_triggered=md[key+'_would_have_triggered'],
                ablation_blocked_by_ablation=md[key+'_blocked_by_ablation'],
                ablation_trigger_reason=md[key+'_reason'])
        result.append(row)
    return result

def interpretation(contrast, replication):
    if not contrast['complete']:
        return 'Insufficient evidence',['Incomplete primary data']
    effect=Fraction(contrast['paired_statistics']['exact_mean_ac_difference'])
    rep_effect=Fraction(replication['paired_statistics']['exact_mean_ac_difference'])
    p,rp=contrast['point_partition'],replication['point_partition']
    net,rep_net=p['net_reference_contribution'],rp['net_reference_contribution']
    magnitude=(rep_effect!=0 or rep_net!=0) and abs(effect)<=abs(rep_effect) and abs(net)<=abs(rep_net)
    churn=rp['gross_churn']>=p['gross_churn']>0
    contrast['replication_safeguards']=dict(absolute_macro_ac_effect=float(abs(effect)),
        absolute_replication_macro_ac_change=float(abs(rep_effect)),absolute_net_point_effect=abs(net),
        absolute_replication_net_point_change=abs(rep_net),contrast_gross_churn=p['gross_churn'],
        replication_gross_churn=rp['gross_churn'],magnitude_attribution_limited=bool(magnitude),
        gross_churn_attribution_weakness=churn,
        label='ATTRIBUTION LIMITED BY OBSERVED REPLICATION VARIATION' if magnitude or churn else None,
        no_subtraction_or_corrected_effect=True)
    reasons=[]
    if contrast['strata']['true']['query_count']<=1:
        reasons.append('At most one R2-triggered query')
    if (effect!=0 or net!=0 or p['gross_churn']>0) and (magnitude or churn):
        reasons.append('Nonzero effects dominated by frozen observed-replication magnitude/churn flags')
    # Enumerate conflicts even when the higher-precedence insufficient label wins.
    conflicts=[]
    d=contrast['metric_deltas']
    if effect*net<0:
        conflicts.append('Macro AC and net supported points have opposite directions')
    safety=[]
    for metric in CLAIMS:
        vals=d['oriented_safety_deltas'][metric]
        ma,mi=vals['macro'],vals['pooled_micro']
        if ma is not None and mi is not None and ma*mi<0:
            conflicts.append(metric+' macro and pooled safety directions conflict')
        for kind,value in vals.items():
            if value is not None:
                safety.append(value)
                if value*effect<0:
                    conflicts.append('AC and '+metric+' '+kind+' safety direction conflict')
    syntax=d['citation_syntax_validity']
    if syntax is not None:
        safety.append(syntax)
        if syntax*effect<0:
            conflicts.append('AC and citation syntax validity conflict')
    triggered=contrast['strata']['true']
    ts=triggered['paired_statistics']
    if ts:
        te=Fraction(ts['exact_mean_ac_difference'])
        tn=triggered['point_partition']['net_reference_contribution']
        if te*effect<0 or tn*net<0:
            conflicts.append('Full-set and R2-triggered stratum directions conflict')
        if te*tn<0:
            conflicts.append('Triggered macro AC and net points conflict')
    else:
        te=tn=0
    contrast['directional_conflicts']=conflicts
    if reasons:
        return 'Insufficient evidence',reasons
    if conflicts:
        return 'Mixed evidence',conflicts
    if effect>0 and net>0 and te>=0 and tn>=0:
        return 'Supported contribution on this benchmark',['Positive macro AC/net points; consistent triggered subset; no dominating frozen caveat']
    quality=[float(effect),net]+safety+[d['citation_completeness']['macro'],d['citation_completeness']['micro']]
    saved=contrast['savings_relative_to_R2']
    if all(v is None or v<=0 for v in quality) and any(v is not None and v<0 for v in quality) and saved['retrieval']>=0 and saved['llm']>=0 and (saved['retrieval']>0 or saved['llm']>0):
        return 'Ablation performs better',['Ablation improves quality without conflicting deterioration and costs no more in either production call type, strictly less in at least one']
    if effect==0 and net==0 and all(v==0 for v in safety):
        return 'No observed contribution',['Exact completeness/safety ties with enough triggers']
    return 'Mixed evidence',['Remaining directional or attribution ambiguity under frozen precedence']

def build_contrast(alias,records,sizes,universe,metrics,costs,metadata,replication):
    left,right=records['R2'],records[alias]
    flag='revision_used' if alias=='A1' else 'expansion_used'
    per_query=paired_rows(left,right,'R2',alias,costs,metadata,flag)
    complete=all(valid(r) for r in left+right)
    result=dict(schema='phase5b2e-contrast-v0',reference='R2',comparator=alias,complete=complete,
        analysis_status='COMPLETE' if complete else 'INCOMPLETE',
        primary_analysis_valid=complete,
        secondary_deltas_scope='Complete judged cohorts' if complete else 'Unpaired available-case diagnostics with different query denominators; not a primary effect',
        raw_delta_direction='R2 - '+alias,metrics={'R2':metrics['R2'],alias:metrics[alias]},
        metric_deltas=metric_deltas(metrics['R2'],metrics[alias]),point_partition=partition(left,right,universe),
        paired_statistics=paired_statistics(left,right,True),per_query=per_query,strata={},
        required_point_observations=point_observations(left,right,universe),
        bootstrap_policy=dict(executed=complete,seed=20260906,resamples=10000,sample_size=31,
                              reason=None if complete else 'Mandatory 31-pair completeness gate failed; no smaller-denominator CI'),
        strata_interpretation='Descriptive post-treatment subsets; not randomized causal evidence. Non-triggered differences are background run variation/downstream differences.',
        savings_relative_to_R2=differences_saved(costs_summary(costs['R2'],list(sizes)),costs_summary(costs[alias],list(sizes))))
    cross=Counter()
    for r in per_query:
        cross[(r['R2_intervention_used'],r['ablation_would_have_triggered'],r['ablation_blocked_by_ablation'])]+=1
    result['trigger_cross_tab']=[dict(R2_used=u,ablation_would_have_triggered=w,ablation_blocked_by_ablation=b,count=n)
                                for (u,w,b),n in cross.items()]
    for value,key in [(True,'true'),(False,'false'),(None,'unreached_or_error')]:
        ids=[r['query_id'] for r in per_query if r['R2_intervention_used'] is value]
        l=[r for r in left if r['query_id'] in ids]
        r=[r for r in right if r['query_id'] in ids]
        lm,rm=summarize(l,sizes),summarize(r,sizes)
        result['strata'][key]=dict(query_count=len(ids),query_ids=ids,required_point_denominator=sum(sizes[q] for q in ids),
            metrics={'R2':lm,alias:rm},metric_deltas=metric_deltas(lm,rm),
            point_partition=partition(l,r,{p for p in universe if p[0] in ids}),paired_statistics=paired_statistics(l,r),
            costs={'R2':costs_summary(costs['R2'],ids),alias:costs_summary(costs[alias],ids)})
    result['interpretation'],result['interpretation_reasons']=interpretation(result,replication)
    return result

def main():
    # Only the trusted evaluator's cached records/point IDs are read here; no gold file is opened.
    sys.addaudithook(lambda event,args: (_ for _ in ()).throw(RuntimeError('Offline analysis forbids network'))
                     if event in ('socket.connect','socket.getaddrinfo','urllib.Request') else None)
    require(all((OUT/v/'evaluation.jsonl').exists() for v in VARIANTS.values()), 'evaluation journals incomplete')
    gate_result=gate()
    records={a:rows(OUT/v/'evaluation.jsonl') for a,v in VARIANTS.items()}
    records['R1']=rows(ROOT/'data/evaluation/generation/agentic_rag_eval_v1_agentic-v1.jsonl')
    qids=read_json(BASE/'phase5a_ablation_manifest_v0.json')['query_order']
    sizes={r['query_id']:len(r['required_point_ids']) for r in records['R1']}
    universe={(r['query_id'],p) for r in records['R1'] for p in r['required_point_ids']}
    require(len(sizes)==31 and len(universe)==sum(sizes.values())==102,'historical point universe mismatch')
    historical={r['query_id']:r for r in records['R1']}
    costs,metadata={},{}
    for a,rs in records.items():
        require(len(rs)==31 and [r['query_id'] for r in rs]==qids,'analysis order/ID mismatch')
        costs[a],metadata[a]={},{}
        for r in rs:
            q=r['query_id']
            require(r['query']==historical[q]['query'],'historical query text mismatch')
            if valid(r):
                require(r['required_point_ids']==historical[q]['required_point_ids'],'changed point universe')
                require(set(r['supported_point_ids'])<=set(r['required_point_ids']),'unknown supported point')
            observer=None if a=='R1' else read_json(ROOT/'data/rag/traces/phase5'/VARIANTS[a]/'observations'/(q+'.json'))
            costs[a][q]=cost_record(r['trace'],observer)
            if observer:
                metadata[a][q]=observer['metadata']
    metrics={a:summarize(rs,sizes) for a,rs in records.items()}
    # R1 -> R2 must be computed and written before primary contrasts.
    replication=dict(schema='phase5b2e-replication-v0',historical_reference='R1',replication='R2',
        delta_direction='R2 - R1',description='Observed same-configuration replication variation; not formal stochastic variance estimation.',
        metrics={a:metrics[a] for a in ('R1','R2')},metric_deltas=metric_deltas(metrics['R2'],metrics['R1']),
        point_partition=partition(records['R2'],records['R1'],universe),
        required_point_observations=point_observations(records['R2'],records['R1'],universe),
        complete=metrics['R2']['complete'] and metrics['R1']['complete'],
        secondary_deltas_scope='Unpaired available-case diagnostics if R2 incomplete; not a replication effect estimate',
        paired_statistics=paired_statistics(records['R2'],records['R1']),
        per_query=paired_rows(records['R2'],records['R1'],'R2','R1',costs),
        limitations=['R1 is retained, not replaced or rejudged.','Historical complete source commit and provider backend identity are not byte-pinned.','One replication mixes production and evaluator variation; no corrected effect is estimated.'])
    exclusive_json(OUT/'replication_R1_R2.json',replication)
    contrasts={a:build_contrast(a,records,sizes,universe,metrics,costs,metadata,replication) for a in ('A1','A2')}
    for a,c in contrasts.items():
        exclusive_json(OUT/('contrast_R2_'+a+'.json'),c)
    attempts={a:rows(OUT/v/'evaluation_attempts.jsonl') for a,v in VARIANTS.items()}
    for a in VARIANTS:
        for q in qids:
            actual=list((OUT/VARIANTS[a]/'attempts'/q).glob('*/request.json'))
            require(len(actual)<=3,'evaluator attempt ceiling exceeded')
            accepted=[x for x in attempts[a] if x['query_id']==q and x['status']=='valid_parsed_judgment' and not x['replay']]
            require(len(accepted)<=1,'valid output rejudged')
        metrics[a]['efficiency']=costs_summary(costs[a],qids)
        metrics[a]['efficiency']['per_query']=costs[a]
        metrics[a]['evaluator_attempt_count']=sum(not x['replay'] for x in attempts[a])
        metrics[a]['evaluator_errors']=[x for x in attempts[a] if x['status']!='valid_parsed_judgment']
        metrics[a]['evaluation_artifact_path']=str((OUT/VARIANTS[a]/'evaluation.jsonl').relative_to(ROOT))
        exclusive_json(OUT/VARIANTS[a]/'metrics.json',metrics[a])
    before=read_json(OUT/'integrity_before.json')
    verification={p:dict(before_sha256=h,after_sha256=file_hash(ROOT/p)) for p,h in before.items()}
    unchanged=all(v['before_sha256']==v['after_sha256'] for v in verification.values())
    require(unchanged,'frozen artifact changed; evaluation FAIL')
    integrity=dict(status='PASS',files=verification,preserved_file_count=len(before),
        categories={k:'PASS' for k in ('production_outputs','production_traces','observer_sidecars','original_seals',
            'supplemental_seals','corpus','gold','R0_R1','Phase4','Phase5A','Phase5B1','Phase5B2R',
            'Agentic_runtime','retrieval','prompts','historical_Phase5B2_report_and_placeholders')},
        recovery_verification_after_evaluation=gate_result,
        production_reruns=0,production_llm_calls_during_phase=0,new_retrieval_calls=0)
    exclusive_json(OUT/'integrity_after.json',integrity)
    summary=dict(schema='phase5b2e-evaluation-metrics-v0',status='PASS' if all(metrics[a]['complete'] for a in VARIANTS) else 'INCOMPLETE',
        completed_utc=now(),recovery_gate=gate_result,production_reruns=0,production_llm_calls_during_phase=0,
        evaluation_order=list(VARIANTS),variants={a:metrics[a] for a in VARIANTS},
        replication=replication,contrasts=contrasts,integrity='PASS',
        hypotheses=read_json(BASE/'phase5a_ablation_manifest_v0.json')['hypotheses'],H3_tested=False,
        artifact_namespace=str(OUT.relative_to(ROOT)),historical_placeholders_preserved=True,
        ready_for_phase5c=all(metrics[a]['complete'] for a in VARIANTS),phase5c_started=False)
    exclusive_json(BASE/'phase5b_evaluation_metrics_v0.json',summary)
    from render_report import render
    report,console=render(summary)
    exclusive_bytes(BASE/'phase5b_evaluation_report_v0.md',report.encode())
    exclusive_bytes(OUT/'console_output.txt',console.encode())
    protocol=read_json(ROOT/'data/evaluation/generation/phase5/phase5b2r_recovery_protocol_v1.json')
    artifacts={str(p.relative_to(ROOT)):file_hash(p) for p in sorted(OUT.rglob('*')) if p.is_file() and p != OUT/'provenance.json'}
    artifacts.update({str((BASE/n).relative_to(ROOT)):file_hash(BASE/n)
                     for n in ('phase5b_evaluation_metrics_v0.json','phase5b_evaluation_report_v0.md')})
    provenance=dict(schema='phase5b2e-provenance-v0',external_recovery_manifest_sha256=ANCHOR,
        phase5a={str(p.relative_to(ROOT)):file_hash(p) for p in BASE.glob('phase5a*')},
        phase5b1={str(p.relative_to(ROOT)):file_hash(p) for p in BASE.glob('phase5b1*')},
        original_production_seals={a:file_hash(ROOT/'data/rag/traces/phase5'/v/'production_seal.json') for a,v in VARIANTS.items()},
        supplemental_seals={a:file_hash(ROOT/'data/rag/traces/phase5'/v/'durable_seal_recovery_v1.json') for a,v in VARIANTS.items()},
        production_outputs={a:{q:file_hash(ROOT/'data/rag/traces/phase5'/v/'outputs'/(q+'.json')) for q in qids} for a,v in VARIANTS.items()},
        evaluator_sources={p:file_hash(ROOT/p) for p in SOURCES},
        gold_sha256=read_json(OUT/'evaluation_protocol.json')['gold_sha256'],
        historical_frozen_hashes=protocol['historical_frozen_hashes'],evaluation_artifacts=artifacts,
        self_hash_policy='This manifest is excluded from its own hash inventory; SHA-256 printed in console.')
    exclusive_json(OUT/'provenance.json',provenance)
    print(console,flush=True)
    print('Provenance SHA-256: '+file_hash(OUT/'provenance.json'),flush=True)

if __name__=='__main__':
    if sys.argv[1:] == ['--refresh-reporting']:
        prior=read_json(OUT/'provenance.json')
        REFRESH_HASHES=dict(prior['evaluation_artifacts'])
        REFRESH_HASHES[str((OUT/'provenance.json').relative_to(ROOT))]=file_hash(OUT/'provenance.json')
    else:
        require(not sys.argv[1:],'unsupported analysis arguments')
    main()
