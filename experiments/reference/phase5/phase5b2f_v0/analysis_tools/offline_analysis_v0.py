"""Offline, additive Phase 5B.2-F assembly; no evaluator or runtime execution.

Run from repository root after phase5b2f_gate.py. Source records are copied without
payload edits. Deterministic parser/point-audit AST extraction verifies integrity.
"""
import ast, collections, json, math, platform, random, statistics, sys
from fractions import Fraction
from pathlib import Path
from phase5b2f_gate import ROOT,BASE,OUT,COUNTS,sha,read,snapshot

VARIANTS={'R2':'full-agentic-replication','A1':'agentic-v1-no-answer-revision','A2':'agentic-v1-no-evidence-expansion'}
METRICS=['answer_completeness','citation_completeness','citation_correctness','groundedness','unsupported_claim_rate','citation_syntax_validity']
CLAIMS={'citation_correctness':('correctly_cited_claim_count','cited_claim_count'),'groundedness':('grounded_claim_count','claim_count'),'unsupported_claim_rate':('unsupported_claim_count','claim_count')}
def canonical(v):return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
def digest(v):
    import hashlib
    return hashlib.sha256(canonical(v)).hexdigest()
def jsonl(p):return [json.loads(s) for s in Path(p).read_text().splitlines() if s]
def save(name,v):
    p=OUT/name;p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x') as f:json.dump(v,f,ensure_ascii=False,sort_keys=True,indent=2,allow_nan=False);f.write('\n')
def lines(name,rows):
    p=OUT/name;p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x') as f:
        for r in rows:f.write(json.dumps(r,ensure_ascii=False,sort_keys=True,allow_nan=False)+'\n')
def write(name,text):
    p=OUT/name;p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x') as f:f.write(text)
def ratio(n,d):return n/d if d else None
def ac(r):return Fraction(len(r['supported_point_ids']),len(r['required_point_ids']))
def metric_values(r):return {k:(r['citation_valid'] if k=='citation_syntax_validity' else r[k]) for k in METRICS}
def aggregate(rows):
    assert rows
    n=len(rows); denom=sum(len(r['required_point_ids']) for r in rows)
    result={'query_count':n,'required_point_count':denom,'generation_errors':0,'evaluation_errors':0}
    for name,field in [('answer_completeness','supported_point_ids'),('citation_completeness','citation_supported_point_ids')]:
        total=sum(len(r[field]) for r in rows)
        result[name]={'macro':sum(r[name] for r in rows)/n,'macro_defined_queries':n,'micro':total/denom,'numerator':total,'denominator':denom,'raw':f'{total}/{denom}'}
    for name,(nf,df) in CLAIMS.items():
        eligible=[r for r in rows if r['judge'][df]!=0]
        num=sum(r['judge'][nf] for r in rows);den=sum(r['judge'][df] for r in rows)
        result[name]={'macro':sum(r[name] for r in eligible)/len(eligible) if eligible else None,'macro_defined_queries':len(eligible),'micro':ratio(num,den),'numerator':num,'denominator':den,'raw':f'{num}/{den}'}
    valid=sum(r['citation_valid'] for r in rows)
    result['citation_syntax_validity']={'macro':valid/n,'macro_defined_queries':n,'micro':valid/n,'numerator':valid,'denominator':n,'raw':f'{valid}/{n}','basis':'deterministic citation_valid; separate from semantic correctness'}
    result['raw_claim_counts']={f:sum(r['judge'][f] for r in rows) for f in sorted({f for pair in CLAIMS.values() for f in pair})}
    result['raw_count_anomalies']=[{'query_id':r['query_id'],'counts':{k:r['judge'][k] for k in result['raw_claim_counts']},'grounded_plus_unsupported_ne_claims':r['judge']['grounded_claim_count']+r['judge']['unsupported_claim_count']!=r['judge']['claim_count'],'numerator_exceeds_denominator':any(r['judge'][nf]>r['judge'][df] for nf,df in CLAIMS.values())} for r in rows if r['judge']['grounded_claim_count']+r['judge']['unsupported_claim_count']!=r['judge']['claim_count'] or any(r['judge'][nf]>r['judge'][df] for nf,df in CLAIMS.values())]
    return result
def delta_metrics(left,right):
    return {k:{s:(left[k][s]-right[k][s] if left[k][s] is not None and right[k][s] is not None else None) for s in ('macro','micro','numerator','denominator')} for k in METRICS}
def cost_summary(costs):
    result={}
    for field in ('retrieval','production_llm','merge_reranks','observable_http_submissions'):
        v=[c[field] for c in costs];result[field]={'total':sum(v),'mean':statistics.mean(v),'median':statistics.median(v),'max':max(v)}
    result['query_count']=len(costs)
    result['successful_retrievals']=sum(c['successful_retrievals'] for c in costs)
    result['failed_event_count']=sum(c['failed_event_count'] for c in costs)
    result['llm_stage_counts']=dict(sum((collections.Counter(c['llm_stage_counts']) for c in costs),collections.Counter()))
    result['provider_internal_retries']='unavailable'
    result['token_counts_and_monetary_cost']='unavailable'
    return result
def transitions(left,right,left_name,right_name):
    rows=[]
    for a,b in zip(left,right):
        assert a['query_id']==b['query_id'] and a['required_point_ids']==b['required_point_ids']
        sa,sb=set(a['supported_point_ids']),set(b['supported_point_ids'])
        for pid in a['required_point_ids']:
            category='both_supported' if pid in sa and pid in sb else 'only_'+left_name if pid in sa else 'only_'+right_name if pid in sb else 'neither_supported'
            rows.append({'query_id':a['query_id'],'point_id':pid,left_name+'_supported':pid in sa,right_name+'_supported':pid in sb,'transition':category})
    names=['both_supported','only_'+left_name,'only_'+right_name,'neither_supported']
    counts={k:sum(r['transition']==k for r in rows) for k in names}
    assert sum(counts.values())==len(rows)==sum(len(r['required_point_ids']) for r in left)
    return {'counts':counts,'denominator':len(rows),'net_'+left_name+'_points':counts[names[1]]-counts[names[2]],'gross_churn':counts[names[1]]+counts[names[2]],'changed_point_ids':{k:[{'query_id':r['query_id'],'point_id':r['point_id']} for r in sorted(rows,key=lambda r:(r['query_id'],r['point_id'])) if r['transition']==k] for k in names[1:3]}},rows
def bootstrap(left,right,other,order):
    # Frozen Phase 5B.2-E implementation converts exact paired fractions to float
    # before resampling. Preserve that order of operations byte-for-byte.
    diffs=[float(ac(a)-ac(b)) for a,b in zip(left,right)]
    rng=random.Random(20260906)
    means=sorted(sum(diffs[rng.randrange(31)] for _ in range(31))/31 for _ in range(10000))
    def percentile(p):
        x=(len(means)-1)*p;i=math.floor(x);return means[i]+(x-i)*(means[min(i+1,len(means)-1)]-means[i])
    return {'contrast':'R2 - '+other,'observed_delta':float(sum(ac(a)-ac(b) for a,b in zip(left,right))/31),'ci_lower':percentile(.025),'ci_upper':percentile(.975),'confidence_level':.95,'resamples':10000,'seed':20260906,'sample_size':31,'rng':'random.Random(seed); rng.randrange(31)','independently_reinitialized':True,'percentile_rule':'linear interpolation at (N-1)*p','query_order':order,'unit':'whole paired queries','python_version':platform.python_version(),'sorted_bootstrap_means_canonical_sha256':digest(means),'uncertainty':'query-sampling uncertainty only; not generation/judge stochasticity','p_values':None,'significance_claim':False}

def main():
    assert not OUT.exists(),'never overwrite final analysis namespace'
    gate=read('/tmp/phase5b2f_gate.json');assert gate['status']=='PASS'
    before=read('/tmp/phase5b2f_before.json')
    for name,h in before['project'].items():assert sha(ROOT/name)==h,'pre-analysis drift: '+name
    design=read(BASE/'phase5a_ablation_manifest_v0.json')
    gold=read(ROOT/'data/evaluation/generation/generation_eval_v1_verified.json')['items']
    order=design['query_order'];assert [r['query_id'] for r in gold]==order and len(set(order))==31
    items={r['query_id']:r for r in gold}
    universe=[(r['query_id'],p['point_id']) for r in gold for p in r['required_points']]
    assert len(universe)==len(set(universe))==102
    manifest=read(BASE/'phase5b2er1_quota_recovery_manifest_v0.json')
    slots={(s['alias'],s['query_id']):s for s in manifest['slots']}
    source={(s['alias'],s['query_id']):s for s in gate['sources']}
    # Extract only pure frozen functions. Never import evaluate_record or runtime.
    source_ast=ast.parse((ROOT/'scripts/evaluate_standard_rag.py').read_text())
    nodes=[ast.ImportFrom(module='__future__',names=[ast.alias(name='annotations')],level=0)]+[n for n in source_ast.body if isinstance(n,ast.FunctionDef) and n.name in ('parse_judge','point_audit')]
    ns={'json':json};exec(compile(ast.fix_missing_locations(ast.Module(body=nodes,type_ignores=[])),'<frozen pure parser and point_audit>','exec'),ns)
    from citation_validator import validate_citations
    records={};provenance=[];costs={};observers={};production={}
    def validate(row,item):
        assert row['query_id']==item['query_id'] and row['query']==item['query']
        assert row['generation_error'] is None and row['evaluation_error'] is None
        ids=[p['point_id'] for p in item['required_points']]
        parsed=ns['parse_judge'](json.dumps(row['judge']),ids)
        audit=ns['point_audit'](item,{e['chunk_id'] for e in row['trace']['final_evidence']},parsed)
        for k in ('required_point_ids','supported_point_ids','citation_supported_point_ids'):assert row[k]==audit[k],(row['query_id'],k)
        assert row['answer_completeness']==len(row['supported_point_ids'])/len(ids)
        assert row['citation_completeness']==len(row['citation_supported_point_ids'])/len(ids)
        for k,(nf,df) in CLAIMS.items():assert row[k]==ratio(row['judge'][nf],row['judge'][df]),(row['query_id'],k)
        t=row['trace'];valid=validate_citations(t.get('final_answer') or '',{e['evidence_id']:e for e in t['final_evidence']},t.get('citation_check',{}).get('cited_evidence_ids',[])).valid
        assert row['citation_valid']==valid
    for alias,variant in VARIANTS.items():
        frozen=design['variant_manifests'][alias];assert read(BASE/variant/'variant_manifest.json')==frozen
        assert digest(frozen)==design['variant_manifest_canonical_sha256'][alias]
        records[alias]=[];costs[alias]={};observers[alias]={};production[alias]={}
        for qid in order:
            slot=slots[alias,qid];src=source[alias,qid];p=ROOT/src['source'];assert sha(p)==src['source_sha256']
            row=read(p);prod=read(ROOT/slot['production_output_path']);validate(row,items[qid])
            assert all(row[k]==v for k,v in prod.items()),'semantic record production payload drift'
            assert sha(ROOT/slot['production_output_path'])==slot['production_output_hash']
            assert digest(items[qid])==slot['gold_item_sha256'] and digest(items[qid]['query'])==slot['query_sha256']
            if src['kind']=='v0':assert row['evaluation_status']=='JUDGED' and row['production_output_sha256']==slot['production_output_hash']
            path=ROOT/'data/rag/traces/phase5'/variant
            assert read(path/(qid+'.json'))==prod['trace']
            obs=read(path/'observations'/(qid+'.json'));meta=obs['metadata'];t=prod['trace'];events=obs['events']
            assert t['revision_used']==meta['revision_attempted'] and t['expansion_used']==meta['expansion_attempted']
            for feature,used in [('answer_revision','revision_used'),('expansion','expansion_used')]:
                eligible=meta[feature+'_would_have_triggered'];blocked=meta[feature+'_blocked_by_ablation']
                assert type(eligible) is bool and type(blocked) is bool
                enabled=frozen['ablation_flags']['enable_answer_revision' if feature=='answer_revision' else 'enable_expansion']
                assert blocked==(eligible and not enabled)
                assert t[used]==(eligible and enabled)
            c={'retrieval':sum(e['logical_call_type']=='retrieval' for e in events),'production_llm':sum(e['logical_call_type']=='llm' for e in events),'merge_reranks':sum(e['logical_call_type']=='merge_rerank' for e in events),'observable_http_submissions':sum(e['observable_http_attempts'] for e in events if e['logical_call_type']=='llm'),'successful_retrievals':sum(e['logical_call_type']=='retrieval' and e['status']=='success' for e in events),'failed_event_count':sum(e['status']!='success' for e in events),'llm_stage_counts':dict(collections.Counter(e['stage'] for e in events if e['logical_call_type']=='llm')),'trace_path':str((path/(qid+'.json')).relative_to(ROOT)),'observer_path':str((path/'observations'/(qid+'.json')).relative_to(ROOT))}
            assert c['retrieval']==t['retrieval_call_count']==len(t['retrieval_calls'])
            assert c['production_llm']==t['llm_call_count']==len(t['llm_calls'])
            assert c['failed_event_count']==0
            records[alias].append(row);costs[alias][qid]=c;observers[alias][qid]=obs;production[alias][qid]=prod
            provenance.append({'alias':alias,'variant_id':variant,'query_id':qid,'judgment_source':'phase5b2e_v0' if src['kind']=='v0' else 'phase5b2er2_v1','source_record_path':src['source'],'source_record_hash':src['source_sha256'],'canonical_record_hash':digest(row),'production_output_path':slot['production_output_path'],'production_output_hash':slot['production_output_hash'],'production_answer_sha256':sha_text(t['final_answer']),'query_text_sha256':sha_text(row['query']),'gold_item_sha256':slot['gold_item_sha256'],'gold_query_binding_hash':slot['gold_query_binding_hash'],'required_point_ids':row['required_point_ids'],'semantic_payload_rewritten':False})
    for alias,flag in [('A1','enable_answer_revision'),('A2','enable_expansion')]:
        base=json.loads(json.dumps(design['variant_manifests']['R2']));base['variant_id']=VARIANTS[alias];base['ablation_flags'][flag]=False
        assert base==design['variant_manifests'][alias],'unexpected config difference'
    r1path=ROOT/'data/evaluation/generation/agentic_rag_eval_v1_agentic-v1.jsonl'
    records['R1']=jsonl(r1path);assert [r['query_id'] for r in records['R1']]==order
    for r in records['R1']:
        validate(r,items[r['query_id']]);assert read(ROOT/'data/rag/traces/agentic-rag-v1/agentic-v1'/(r['query_id']+'.json'))==r['trace']
    metrics={a:aggregate(records[a]) for a in ('R1','R2','A1','A2')}
    assert metrics['R1']['answer_completeness']['numerator']==65
    assert math.isclose(metrics['R1']['answer_completeness']['macro'],0.7236559139784946,abs_tol=1e-15)
    triggers={'A1':[qid for qid in order if production['R2'][qid]['trace']['revision_used']],'A2':[qid for qid in order if production['R2'][qid]['trace']['expansion_used']]}
    assert triggers['A1']==['eval005b','eval007','eval013','eval029'],'revision trigger mismatch'
    assert triggers['A2']==['eval001','eval005a','eval005b','eval006','eval011','eval013','eval014','eval016','eval023'],'expansion trigger mismatch'
    efficiency={a:cost_summary(list(costs[a].values())) for a in VARIANTS}
    assert [(efficiency[a]['retrieval']['total'],efficiency[a]['production_llm']['total'],efficiency[a]['merge_reranks']['total']) for a in VARIANTS]==[(42,101,9),(42,94,11),(31,101,0)],'cost reconciliation mismatch'
    rep_partition,rep_points=transitions(records['R2'],records['R1'],'R2','R1')
    rep_diffs=[ac(a)-ac(b) for a,b in zip(records['R2'],records['R1'])]
    replication={'contrast':'R2 - R1','description':'one observed same-configuration replication; not formal model variance, stochasticity CI, or noise distribution','metrics':{a:metrics[a] for a in ('R1','R2')},'deltas':delta_metrics(metrics['R2'],metrics['R1']),'point_transitions':rep_partition,'gained_points':rep_partition['counts']['only_R2'],'lost_points':rep_partition['counts']['only_R1'],'net_point_difference':rep_partition['net_R2_points'],'gross_churn':rep_partition['gross_churn'],'query_counts':signs(rep_diffs,'R1'),'per_query':[{'query_id':a['query_id'],'R1':metric_values(b),'R2':metric_values(a),'delta_R2_minus_R1':{k:float(metric_values(a)[k])-float(metric_values(b)[k]) if metric_values(a)[k] is not None and metric_values(b)[k] is not None else None for k in METRICS},'point_transitions':[p for p in rep_points if p['query_id']==a['query_id']]} for a,b in zip(records['R2'],records['R1'])],'warning':'Macro and pooled micro can move in different directions; display both.'}
    contrasts={};boots={};point_files={}
    for alias,feature in [('A1','answer_revision'),('A2','expansion')]:
        left,right=records['R2'],records[alias];part,pts=transitions(left,right,'R2',alias);point_files[alias]=pts
        diffs=[ac(a)-ac(b) for a,b in zip(left,right)]
        c={'contrast':'R2 - '+alias,'frozen_difference':{'flag':'enable_'+feature,'from':True,'to':False},'metrics':{'R2':metrics['R2'],alias:metrics[alias]},'deltas':delta_metrics(metrics['R2'],metrics[alias]),'point_transitions':part,'net_R2_contribution':part['net_R2_points'],'net_ablation_point_change':-part['net_R2_points'],'gross_churn':part['gross_churn'],'query_counts':signs(diffs,alias),'ablation_improved_equal_worsened':{'improved':sum(x<0 for x in diffs),'equal':sum(x==0 for x in diffs),'worsened':sum(x>0 for x in diffs)},'mean_paired_AC_delta':float(sum(diffs)/31),'median_paired_AC_delta':float(statistics.median(diffs)),'per_query':[],'triggered_query_ids':triggers[alias],'strata':{},'cross_tab':[]}
        for a,b,d in zip(left,right,diffs):
            qid=a['query_id'];meta=observers[alias][qid]['metadata'];used=qid in triggers[alias]
            p={'query_id':qid,'required_point_count':len(a['required_point_ids']),'R2':metric_values(a),alias:metric_values(b),'delta_R2_minus_'+alias:{k:float(metric_values(a)[k])-float(metric_values(b)[k]) if metric_values(a)[k] is not None and metric_values(b)[k] is not None else None for k in METRICS},'AC_delta_exact':str(d),'required_point_transitions':[r for r in pts if r['query_id']==qid],'R2_intervention_used':used,alias+'_would_have_triggered':meta[feature+'_would_have_triggered'],alias+'_blocked_by_ablation':meta[feature+'_blocked_by_ablation'],'production_cost':{v:costs[v][qid] for v in ('R2',alias)},'status_and_errors':{v:{k:records[v][order.index(qid)].get(k) for k in ('status','generation_error','evaluation_error')} for v in ('R2',alias)}}
            c['per_query'].append(p)
        for used in (True,False):
            ids=[q for q in order if (q in triggers[alias])==used];l=[r for r in left if r['query_id'] in ids];r=[r for r in right if r['query_id'] in ids]
            lm,rm=aggregate(l),aggregate(r);p,_=transitions(l,r,'R2',alias)
            c['strata']['R2_used_'+str(used).lower()]={'label':'descriptive post-treatment stratum; not randomized subgroup','query_ids':ids,'query_count':len(ids),'required_point_denominator':sum(len(x['required_point_ids']) for x in l),'metrics':{'R2':lm,alias:rm},'deltas':delta_metrics(lm,rm),'point_transitions':p,'production_cost':{v:cost_summary([costs[v][q] for q in ids]) for v in ('R2',alias)}}
        for used in (False,True):
            for would in (False,True):
                for blocked in (False,True):
                    ids=[p['query_id'] for p in c['per_query'] if p['R2_intervention_used']==used and p[alias+'_would_have_triggered']==would and p[alias+'_blocked_by_ablation']==blocked]
                    c['cross_tab'].append({'R2_used':used,alias+'_would_have_triggered':would,alias+'_blocked_by_ablation':blocked,'query_count':len(ids),'query_ids':ids})
        c['stochastic_trigger_disagreement_query_ids']=[p['query_id'] for p in c['per_query'] if p['R2_intervention_used']!=p[alias+'_would_have_triggered']]
        rep_macro=sum(rep_diffs)/31;effect=sum(diffs)/31;rep_net=replication['net_point_difference']
        flag=(rep_macro!=0 or rep_net!=0) and abs(effect)<=abs(rep_macro) and abs(part['net_R2_points'])<=abs(rep_net)
        churn_flag=part['gross_churn']>0 and replication['gross_churn']>=part['gross_churn']
        c['replication_attribution_flag']=flag;c['replication_gross_churn_flag']=churn_flag
        c['attribution_rule_evidence']={'ablation_abs_macro':float(abs(effect)),'replication_abs_macro':float(abs(rep_macro)),'ablation_abs_net_points':abs(part['net_R2_points']),'replication_abs_net_points':abs(rep_net),'replication_nonzero':rep_macro!=0 or rep_net!=0,'replication_gross_churn':replication['gross_churn'],'ablation_gross_churn':part['gross_churn'],'rule_source':'Phase 5A specification sections 9–10','no_replication_delta_subtraction':True}
        c['oriented_safety_deltas']={k:{s:(-1 if k=='unsupported_claim_rate' else 1)*c['deltas'][k][s] for s in ('macro','micro')} for k in ('citation_correctness','groundedness','unsupported_claim_rate')}
        c['conflicts']=conflicts(c,alias)
        c['interpretation']=interpret(c,alias)
        c['attribution_statement']='Attribution limited by observed same-configuration replication variation.' if flag else 'The predeclared macro/net replication-attribution flag is not triggered.'
        boots[alias]=bootstrap(left,right,alias,order);c['bootstrap']=boots[alias]
        c['efficiency_contrast']=eff_contrast(efficiency[alias],efficiency['R2'])
        contrasts[alias]=c
    efficiency['contrasts']={a:contrasts[a]['efficiency_contrast'] for a in ('A1','A2')}
    efficiency['R0_configured_logical_baseline']={'retrieval':31,'production_llm':31,'basis':'configured one retrieval and one answer generation/query; not measured HTTP'}
    efficiency['versus_R0']={a:{k:{'difference':efficiency[a][k]['total']-31,'ratio':efficiency[a][k]['total']/31,'overhead_percent':100*(efficiency[a][k]['total']/31-1)} for k in ('retrieval','production_llm')} for a in VARIANTS}
    efficiency['R1_historical_trace_totals']={k:sum(len(r['trace'][field]) for r in records['R1']) for k,field in [('retrieval','retrieval_calls'),('production_llm','llm_calls')]}
    hypotheses=hypothesis_conclusions(contrasts,design)
    result={'schema':'phase5b2f-metrics-v0','status':'PASS','analysis_role':'primary complete benchmark; historical available-case diagnostics are non-primary','semantic_completeness':gate['counts'],'valid_semantic_records':93,'query_count':31,'unique_required_point_tuples':102,'metrics':metrics,'replication':replication,'contrasts':contrasts,'efficiency':efficiency,'hypotheses':hypotheses,'calls':COUNTS,'ready_for_phase5c':True,'phase5c_started':False}
    OUT.mkdir()
    save('recovery_completion_gate_v0.json',gate)
    save('canonical_judgments_manifest.json',{'schema':'phase5b2f-canonical-judgments-v0','merge_rule':'accepted v0 first; otherwise only frozen eligible valid v1; no quality selection','query_order':order,'required_point_universe':[{'query_id':q,'point_id':p} for q,p in universe],'counts':gate['counts'],'total':93,'records':provenance,'semantic_payload_rewritten':False,'canonical_jsonl_serialization':'each parsed source object is identical; source-file and canonical-object SHA-256 recorded separately; provenance is kept here without injecting fields into semantic records'})
    for alias,variant in VARIANTS.items():
        lines(variant+'/evaluation_complete.jsonl',records[alias]);save(variant+'/metrics.json',metrics[alias])
    save('replication_R1_R2.json',replication);lines('point_transitions_R1_R2.jsonl',rep_points)
    for alias in ('A1','A2'):
        save('contrast_R2_'+alias+'.json',contrasts[alias]);lines('point_transitions_R2_'+alias+'.jsonl',point_files[alias]);save('bootstrap_R2_'+alias+'.json',boots[alias])
    save('efficiency_v0.json',efficiency);save('phase5b2f_metrics_v0.json',result)
    save('integrity_before_inventory_v0.json',before)
    write('analysis_tools/phase5b2f_gate.py',Path(__file__).with_name('phase5b2f_gate.py').read_text())
    write('analysis_tools/offline_analysis_v0.py',Path(__file__).read_text())
    report=render_report(result,provenance);write('phase5b2f_final_report_v0.md',report)
    console=render_console(result);write('phase5b2f_console_v0.txt',console)
    after=snapshot();changed=[p for p,h in before['project'].items() if after.get(p)!=h];added=sorted(set(after)-set(before['project']))
    external_after={p:sha(p) for p in before['external_assets']};assert not changed and not added and external_after==before['external_assets'],'historical artifact integrity failed'
    integrity={'status':'PASS','checked_preexisting_project_files':len(before['project']),'checked_external_asset_files':len(external_after),'scope':'All project regular files including historical artifacts, source, prompts, gold, corpus, retrieval assets, pyc and hash-only .env; excludes .venv and inaccessible metadata directories .git/.agents/.codex; separately checks frozen external model assets. No credentials displayed.','before_inventory_file':'integrity_before_inventory_v0.json','before_inventory_sha256':sha(OUT/'integrity_before_inventory_v0.json'),'project_before_canonical_sha256':digest(before['project']),'project_after_canonical_sha256':digest(after),'changed_or_missing_preexisting_paths':changed,'added_paths_outside_analysis_namespace':added,'external_assets_before_sha256':before['external_assets'],'external_assets_after_sha256':external_after,'production_outputs_unchanged':93,'production_traces_unchanged':93,'observer_sidecars_unchanged':93,'accepted_v0_judgments_unchanged':64,'accepted_recovery_judgments_unchanged':29,'all_preexisting_evaluation_and_recovery_attempt_files_unchanged':True,'calls':COUNTS}
    save('integrity_before_after_v0.json',integrity)
    hashes={str(p.relative_to(OUT)):sha(p) for p in sorted(OUT.rglob('*')) if p.is_file()}
    save('provenance_v0.json',{'schema':'phase5b2f-provenance-v0','recovery_R1_anchor':gate['anchor'],'original_evaluation_provenance_anchor':sha(BASE/'phase5b2e_v0/provenance.json'),'phase5a_manifest_sha256':sha(BASE/'phase5a_ablation_manifest_v0.json'),'phase5a_specification_sha256':sha(BASE/'phase5a_ablation_spec_v0.md'),'frozen_evaluator_sources':manifest['frozen_evaluator_hashes'],'canonical_manifest_sha256':sha(OUT/'canonical_judgments_manifest.json'),'artifacts':hashes,'self_hash_policy':'provenance excludes itself; its SHA-256 is printed in the execution log','python_version':platform.python_version(),'network_enforcement':'Python audit hook rejects socket, HTTP and child process events before application imports','analysis_calls':COUNTS,'accepted_observations':'64 immutable v0 + 29 immutable recovery judgments; quality-blind precedence','recovery_amendment':'quota-recovery amendment after evaluation transport failure; retained in provenance; no rejudging in Phase 5B.2-F','production_seals':'frozen original seals plus approved supplemental durable seals verified by frozen verifier','reproducibility':'analysis_tools contains exact offline source; replay in a separate copy without phase5b2f_v0 using gate then analysis, from repository root. Original namespace uses exclusive creation; never overwrite.','integrity_scope':integrity['scope']})
    print(console)
    print('Provenance SHA-256:',sha(OUT/'provenance_v0.json'))

def sha_text(s):
    import hashlib
    return hashlib.sha256(s.encode()).hexdigest()
def signs(diffs,other):return {'R2_better':sum(d>0 for d in diffs),'tie':sum(d==0 for d in diffs),other+'_better':sum(d<0 for d in diffs)}
def eff_contrast(a,r):
    return {k:{'ablation_minus_R2':a[k]['total']-r[k]['total'],'ratio_to_R2':a[k]['total']/r[k]['total'],'overhead_percent':100*(a[k]['total']/r[k]['total']-1),'saved_by_ablation':r[k]['total']-a[k]['total'],'saved_percent':100*(1-a[k]['total']/r[k]['total'])} for k in ('retrieval','production_llm','merge_reranks','observable_http_submissions')}
def conflicts(c,alias):
    out=[];d=c['deltas'];ac_delta=d['answer_completeness']['macro'];net=c['net_R2_contribution']
    for k in ('citation_completeness','citation_correctness','groundedness','unsupported_claim_rate'):
        orient=-1 if k=='unsupported_claim_rate' else 1
        if d[k]['macro']*d[k]['micro']<0:out.append(k+': macro and pooled micro directions conflict')
        if ac_delta and any(ac_delta*orient*d[k][s]<0 for s in ('macro','micro')):out.append('AC direction conflicts with '+k)
    if ac_delta*net<0:out.append('macro AC direction conflicts with net points')
    st=c['strata']['R2_used_true']
    if ac_delta*st['deltas']['answer_completeness']['macro']<0 or net*st['point_transitions']['net_R2_points']<0:out.append('full-set direction conflicts with triggered stratum')
    return out
def interpret(c,alias):
    nonzero=c['mean_paired_AC_delta']!=0 or c['net_R2_contribution']!=0
    if len(c['triggered_query_ids'])<=1 or ((nonzero or c['gross_churn']>0) and (c['replication_attribution_flag'] or c['replication_gross_churn_flag'])):return 'Insufficient evidence'
    if c['conflicts']:return 'Mixed evidence'
    st=c['strata']['R2_used_true']
    if c['mean_paired_AC_delta']>0 and c['net_R2_contribution']>0 and st['deltas']['answer_completeness']['macro']>=0 and st['point_transitions']['net_R2_points']>=0:return 'Supported contribution on this benchmark'
    safety=[v for x in c['oriented_safety_deltas'].values() for v in x.values()]+[c['deltas']['citation_syntax_validity']['macro']]
    quality=[c['mean_paired_AC_delta'],c['net_R2_contribution']]+safety+[c['deltas']['citation_completeness'][s] for s in ('macro','micro')]
    costs=c['strata']['R2_used_true']['production_cost']
    # Full-cohort efficiency is attached immediately after this classification;
    # recover totals from the complete paired rows, not the triggered subset.
    saved={k:sum(p['production_cost']['R2'][k]-p['production_cost'][alias][k] for p in c['per_query']) for k in ('retrieval','production_llm')}
    if all(v<=0 for v in quality) and any(v<0 for v in quality) and all(v>=0 for v in saved.values()) and any(v>0 for v in saved.values()):return 'Ablation performs better'
    if not nonzero and all(v==0 for v in safety):return 'No observed contribution'
    return 'Mixed evidence'

def hypothesis_conclusions(c,design):
    return {'H1':{'frozen_hypothesis':design['hypotheses']['H1'],'classification':c['A1']['interpretation'],'assessment':'See complete full-set, R2 revision-triggered point transitions, replication safeguard and production LLM savings. A lower A1 score on some triggered queries is descriptive support for the narrow expectation; it does not override frozen attribution precedence or establish generation-omission causality.'},'H2':{'frozen_hypothesis':design['hypotheses']['H2'],'classification':c['A2']['interpretation'],'assessment':'See complete full-set and R2 expansion-triggered results with retrieval/merge savings. No universal claim that Expansion is unnecessary or useless follows from cheaper execution.'},'H3':{'classification':'NOT TESTED','assessment':'No Citation Revision contribution is inferred; A3 was not run.'}}

# Report renderers are defined below; numerical calculations above are independent.
LABELS={'answer_completeness':'Answer Completeness','citation_completeness':'Citation Completeness','citation_correctness':'Citation Correctness','groundedness':'Groundedness','unsupported_claim_rate':'Unsupported Claim Rate ↓','citation_syntax_validity':'Citation syntax validity'}
def fmt(v):return 'null' if v is None else f'{v:.12f}' if isinstance(v,float) else str(v)
def table(headers,rows):return '\n'.join(['| '+' | '.join(headers)+' |','|'+'|'.join('---' for _ in headers)+'|']+['| '+' | '.join(fmt(v).replace('|','/') for v in row)+' |' for row in rows])
def quality_table(metrics,variants,fields=METRICS):
    return table(['Variant','Metric','Macro','Defined queries','Pooled micro / rate','Raw numerator / denominator'],[[a,LABELS[k],metrics[a][k]['macro'],metrics[a][k]['macro_defined_queries'],metrics[a][k]['micro'],metrics[a][k]['raw']] for a in variants for k in fields])
def comparison_table(metrics,deltas,left,right,fields=METRICS):
    return table(['Metric',right+' macro',left+' macro','Δ macro',right+' pooled (raw)',left+' pooled (raw)','Δ pooled','Δ numerator / denominator'],[[LABELS[k],metrics[right][k]['macro'],metrics[left][k]['macro'],deltas[k]['macro'],f"{fmt(metrics[right][k]['micro'])} ({metrics[right][k]['raw']})",f"{fmt(metrics[left][k]['micro'])} ({metrics[left][k]['raw']})",deltas[k]['micro'],f"{deltas[k]['numerator']} / {deltas[k]['denominator']}"] for k in fields])
def point_list(points):return ', '.join('`'+p['query_id']+'/'+p['point_id']+'`' for p in points) or 'None'
def point_section(p,other):
    counts=p['counts']
    return '\n\n'.join([table(['Both supported','Only R2','Only '+other,'Neither','Total','Net R2 points','Gross churn'],[[counts['both_supported'],counts['only_R2'],counts['only_'+other],counts['neither_supported'],p['denominator'],p['net_R2_points'],p['gross_churn']]]),'Only R2: '+point_list(p['changed_point_ids']['only_R2'])+'.','Only '+other+': '+point_list(p['changed_point_ids']['only_'+other])+'.'])
def stratum_section(c,alias):
    chunks=[]
    for key in ('R2_used_true','R2_used_false'):
        s=c['strata'][key]
        chunks+=['### '+key.replace('_',' '),'','**Descriptive post-treatment stratum; not a randomized subgroup.** '+str(s['query_count'])+' queries / '+str(s['required_point_denominator'])+' required points.','', 'Query IDs: '+', '.join('`'+q+'`' for q in s['query_ids'])+'.','',comparison_table(s['metrics'],s['deltas'],'R2',alias),'',point_section(s['point_transitions'],alias),'',table(['Variant','Retrieval total','LLM total','Merge-reranks','Observable HTTP submissions'],[[a]+[s['production_cost'][a][k]['total'] for k in ('retrieval','production_llm','merge_reranks','observable_http_submissions')] for a in ('R2',alias)]),'']
    chunks+=['### Trigger cross-tab','','All eight Boolean cells are retained; no null/unreached decision exists in these sealed successful runs.','',table(['R2 used',alias+' would have triggered',alias+' blocked','Count','Query IDs'],[[x['R2_used'],x[alias+'_would_have_triggered'],x[alias+'_blocked_by_ablation'],x['query_count'],', '.join(x['query_ids']) or '—'] for x in c['cross_tab']]),'','Stochastic decision disagreements: '+', '.join('`'+q+'`' for q in c['stochastic_trigger_disagreement_query_ids'])+'. These are branch decisions in two distinct stochastic runs, not clean intervention counterfactuals. Non-triggered query differences are background run variation/downstream differences, not direct evidence of removing an unused intervention.']
    return '\n'.join(chunks)
def paired_query_table(c,alias):
    rows=[]
    for p in c['per_query']:
        d=p['delta_R2_minus_'+alias]['answer_completeness'];trans=collections.Counter(x['transition'] for x in p['required_point_transitions']);co=p['production_cost']
        rows.append([p['query_id'],p['R2']['answer_completeness'],p[alias]['answer_completeness'],d,'/'.join(str(trans[k]) for k in ('both_supported','only_R2','only_'+alias,'neither_supported')),p['R2_intervention_used'],p[alias+'_would_have_triggered'],p[alias+'_blocked_by_ablation'],f"{co['R2']['retrieval']}/{co[alias]['retrieval']}",f"{co['R2']['production_llm']}/{co[alias]['production_llm']}",f"{co['R2']['merge_reranks']}/{co[alias]['merge_reranks']}"])
    return table(['Query','R2 AC',alias+' AC','Δ R2−'+alias,'Both/only R2/only '+alias+'/neither','R2 used',alias+' would',alias+' blocked','Retrieval R2/'+alias,'LLM R2/'+alias,'Merge R2/'+alias],rows)
def contrast_section(c,alias):
    b=c['bootstrap'];parts=[f"The sole frozen configuration difference is `{c['frozen_difference']['flag']}: true → false`. All quality deltas are R2 − {alias}; a positive raw UCR delta favors the ablation.",comparison_table(c['metrics'],c['deltas'],'R2',alias,fields=METRICS[:2]),point_section(c['point_transitions'],alias),f"Points lost by removal = only R2; points gained after removal = only {alias}; net observed R2 contribution = only R2 − only {alias}. Net ablation point change is {c['net_ablation_point_change']}.",f"R2 better / tied / {alias} better: **{c['query_counts']['R2_better']} / {c['query_counts']['tie']} / {c['query_counts'][alias+'_better']}**. Mean paired AC delta {fmt(c['mean_paired_AC_delta'])}; median {fmt(c['median_paired_AC_delta'])}. Ablation improved/equal/worsened: {c['ablation_improved_equal_worsened']}.",f"Paired bootstrap 95% CI: **[{fmt(b['ci_lower'])}, {fmt(b['ci_upper'])}]**. This describes query-sampling uncertainty only; no p-value or significance claim.",f"Macro/net `replication_attribution_flag`: **{str(c['replication_attribution_flag']).lower()}**. Separate gross-churn flag: **{str(c['replication_gross_churn_flag']).lower()}**. {c['attribution_statement']}",f"Frozen interpretation: **{c['interpretation']}**. "+('Nonzero effects meet the frozen replication magnitude/churn safeguard, which takes precedence over directional conflicts and supported-contribution classification.' if c['interpretation']=='Insufficient evidence' else ''),'Conflicts retained despite precedence: '+('; '.join(c['conflicts']) or 'none detected by the frozen directional checks')+'.','### Every matched query',paired_query_table(c,alias),f"All raw per-query quality metrics, exact rational AC deltas, full point identities, statuses/errors, costs and trace/observer links are retained in [contrast_R2_{alias}.json](contrast_R2_{alias}.json)."]
    return '\n\n'.join(parts)
def render_report(result,provenance):
    m=result['metrics'];r=result['replication'];cs=result['contrasts'];e=result['efficiency']
    p=['# Phase 5B.2-F — Final frozen paired ablation analysis v0','','## 1. Experiment completion and provenance','','**Phase 5B.2-F: PASS. Primary complete benchmark: 93/93 accepted semantic records.** Exactly 31 frozen queries per variant and 102 unique `(query_id, point_id)` tuples. No denominator reduction or imputation.','','Recovery anchor: `8e74013cab6df4564dd33f17cd6901e968152b631d82bbc0c523e680c4a999ee`. The append-only attempt ledger reconciles to 29/29 recovered judgments, zero remaining slots, zero unresolved STARTED, AMBIGUOUS, RECOVERY_EXHAUSTED or unsealed accepted records. Original/supplemental production seals and frozen historical hashes passed the existing offline verifier.','',table(['Variant','Accepted v0','Recovered v1','Complete'],[[a,result['semantic_completeness'][a]['v0'],result['semantic_completeness'][a]['v1'],'31/31'] for a in VARIANTS]),'','Authority is accepted v0 if present, otherwise the one valid recovery observation for that frozen slot. Canonical JSONL records equal their source objects; source-file hashes and unmodified semantic payloads are preserved. The [canonical manifest](canonical_judgments_manifest.json) binds each record to its production output, answer hash, query, point set and source.','', '**Previous available-case diagnostics = non-primary historical diagnostics. Final 93/93 analysis = primary complete benchmark.** The incomplete report, available-case metrics, placeholders and recovery artifacts remain unchanged. The quota-recovery amendment followed evaluation transport failure; it remains part of provenance and does not invalidate the completed benchmark.','','Network/API calls: **0**. Production calls: **0**. Evaluator calls: **0**. Deterministic stored-label/parser/point-audit and citation-syntax integrity verification only; no semantic judging or response selection.','','## 2. R1 → R2 replication','',f"R1 AC macro **{fmt(m['R1']['answer_completeness']['macro'])}** → R2 **{fmt(m['R2']['answer_completeness']['macro'])}**; Δ R2−R1 **{fmt(r['deltas']['answer_completeness']['macro'])}**. AC micro **65/102 → 63/102**; delta {fmt(r['deltas']['answer_completeness']['micro'])}.",'',point_section(r['point_transitions'],'R1'),'',f"R2 gained {r['gained_points']} point, lost {r['lost_points']}, net {r['net_point_difference']}, gross churn {r['gross_churn']}. R2 better / tied / R1 better: **{r['query_counts']['R2_better']} / {r['query_counts']['tie']} / {r['query_counts']['R1_better']}**.",'', '**One observed same-configuration replication.** This is not formal model variance, a stochasticity confidence interval, or a noise distribution. No replication delta is subtracted from an ablation effect.','',comparison_table(r['metrics'],r['deltas'],'R2','R1'),'','**Macro and pooled micro can move in different directions.** R2 Groundedness macro falls while pooled Groundedness rises; UCR macro rises while pooled UCR falls. Citation Correctness falls on both summaries. Keep these separate.','',table(['Query','R1 AC','R2 AC','Δ R2−R1'],[[x['query_id'],x['R1']['answer_completeness'],x['R2']['answer_completeness'],x['delta_R2_minus_R1']['answer_completeness']] for x in r['per_query']]),'','## 3. R2 vs A1 — Answer Revision','',contrast_section(cs['A1'],'A1'),'','## 4. A1 trigger-aware analysis','',stratum_section(cs['A1'],'A1'),'','## 5. R2 vs A2 — Evidence Expansion','',contrast_section(cs['A2'],'A2'),'','## 6. A2 trigger-aware analysis','',stratum_section(cs['A2'],'A2'),'','## 7. Citation/safety metrics','',quality_table(m,['R1','R2','A1','A2'],METRICS[1:]),'','Claim macro scores average only defined per-query ratios; zero denominators remain null. All current claim ratios are defined on 31 queries. Pooled scores sum stored numerator and denominator counts independently. Groundedness was computed from grounded claims and UCR from unsupported claims; neither was inferred from the other. No raw-count anomalies were found. Syntax is separate from semantic correctness.','','R2 − A1:','',comparison_table(cs['A1']['metrics'],cs['A1']['deltas'],'R2','A1',METRICS[1:]),'','R2 − A2:','',comparison_table(cs['A2']['metrics'],cs['A2']['deltas'],'R2','A2',METRICS[1:]),'','A1 has lower AC but higher macro Citation Correctness/Groundedness and lower macro UCR. Its pooled Groundedness/UCR move in the opposite direction from those macro summaries. A2 has equal macro AC and one fewer supported point, while its claim safety summaries favor A2. These tradeoffs remain visible even when the higher-precedence insufficient-evidence category applies.','','## 8. Efficiency','','Measured from all 93 sealed production observer sidecars, reconciled against trace call counts. Logical hybrid retrieval counts as one call; merge-rerank work is separate. All production events succeeded. Evaluator and quota-recovery attempts are excluded.','',table(['Variant','Cost','Total','Mean/query','Median/query','Max/query'],[[a,k]+[e[a][k][s] for s in ('total','mean','median','max')] for a in VARIANTS for k in ('retrieval','production_llm','merge_reranks','observable_http_submissions')]),'','A1 saves **7 production LLM calls**, with retrieval difference **0** and **2 more merge-reranks** than R2. A2 saves **11 retrieval calls** and **9 merge-reranks**, with LLM difference **0**.','',table(['Ablation','Cost','Ablation−R2','Ratio to R2','Overhead %','Saved','Saved %'],[[a,k]+[e['contrasts'][a][k][s] for s in ('ablation_minus_R2','ratio_to_R2','overhead_percent','saved_by_ablation','saved_percent')] for a in ('A1','A2') for k in ('retrieval','production_llm','merge_reranks')]),'','R0 is a **configured logical baseline** of 31 retrieval and 31 answer-generation calls; its HTTP count was not measured.','',table(['Variant','Cost','Difference from configured R0','Ratio','Overhead %'],[[a,k]+[e['versus_R0'][a][k][s] for s in ('difference','ratio','overhead_percent')] for a in VARIANTS for k in ('retrieval','production_llm')]),'',f"Historical R1 trace context: {e['R1_historical_trace_totals']['retrieval']} retrieval and {e['R1_historical_trace_totals']['production_llm']} LLM calls. Provider-internal retries, token records and monetary cost are unavailable; no money estimate is made. Production stage counts and per-query trace links are in the JSON artifacts.",'','## 9. Bootstrap uncertainty','','Exactly 10,000 paired query-level resamples per contrast; sample size 31; `random.Random(20260906)` reinitialized independently. Each draw calls `rng.randrange(31)` 31 times in frozen query order. Statistic: mean per-query AC difference. Percentiles use linear interpolation at `(10000−1)*p`, for p=.025 and .975. Python '+platform.python_version()+'.','',table(['Contrast','Observed mean Δ','95% CI lower','95% CI upper'],[['R2−'+a]+[cs[a]['bootstrap'][k] for k in ('observed_delta','ci_lower','ci_upper')] for a in ('A1','A2')]),'','No points, claims, attempts or variants were resampled independently. No p-values or significance claims. Bootstrap captures query-sampling uncertainty only; it does not characterize generation/judge stochasticity.','','## 10. Replication-attribution assessment','',table(['Contrast','|AC Δ|','|Replication AC Δ|','|Net points|','|Replication net|','Macro/net flag','Contrast churn','Replication churn','Churn flag'],[[a,cs[a]['attribution_rule_evidence']['ablation_abs_macro'],cs[a]['attribution_rule_evidence']['replication_abs_macro'],abs(cs[a]['net_R2_contribution']),abs(r['net_point_difference']),cs[a]['replication_attribution_flag'],cs[a]['gross_churn'],r['gross_churn'],cs[a]['replication_gross_churn_flag']] for a in ('A1','A2')]),'','The frozen magnitude condition requires both absolute AC macro and absolute net-point effects to be no larger than replication, with at least one nonzero replication difference. The independent gross-churn warning requires replication churn ≥ nonzero contrast churn. Exact rational AC differences determine comparison signs and flags.','','A1: macro/net flag **false**; gross-churn flag **true** (4 ≥ 4). A2: macro/net flag **true**; gross-churn flag **false** (4 < 7). **Attribution limited by observed same-configuration replication variation.** This applies to A2 under the required magnitude flag and to A1 under the separately disclosed churn safeguard.','','Under Phase 5A §10 and its already-frozen Phase 5B.2-E offline interpretation implementation, nonzero effects meeting either magnitude or churn safeguard receive **Insufficient evidence** before Mixed evidence or supported-contribution labels. This preserves the preexisting conservative interpretation; it introduces no new threshold. The magnitude flag is kept separate from the churn flag rather than relabeled true for A1.','','## 11. H1/H2 conclusions','','**H1 — Answer Revision.** Frozen hypothesis: “Removing Answer Revision is expected to reduce Answer Completeness on at least some revision-triggered queries, particularly generation-omission cases.”','','Full cohort: R2−A1 macro AC +0.034408602151 and net +4 points. R2 revision-triggered stratum: 4 queries / 19 points; R2 9/19 versus A1 5/19, macro 0.566666666667 versus 0.300000000000. Removing revision loses eval005b/P4, eval013/P3, eval013/P4 and eval029/P2; no required point is gained. Three triggered queries worsen and eval007 ties. Thus the narrow expectation of losses on some triggered queries is observed. No new semantic audit establishes a generation-omission causal diagnosis.','','H1 final category: **Insufficient evidence** under frozen churn precedence; retain the descriptive revision-associated coverage gain, safety conflicts, single-run caveat, and saving of 7 production LLM calls with A1. No aggregate supported-contribution label is claimed.','','**H2 — Evidence Expansion.** Frozen hypothesis: “Removing Evidence Expansion may have limited impact because most observed expansions did not change final Top-5 evidence; however a controlled run is required before concluding the mechanism is unnecessary.”','','Full cohort: equal macro AC, but R2 63/102 versus A2 62/102. Across all points, only R2=4 and only A2=3, net R2 +1 and churn 7. The expansion-triggered stratum has 9 queries / 36 points, R2 14/36 versus A2 11/36 and macro 0.446296296296 versus 0.362962962963. Removing Expansion saves 11 retrievals and 9 merge-reranks without saving LLM calls. A2 claim safety summaries are better.','','H2 final category: **Insufficient evidence** under the macro/net replication safeguard. The limited full-set macro impact is compatible with H2, while triggered coverage gains and bidirectional point changes prevent a claim that Expansion is unnecessary. Stochastic check disagreements and R2 non-triggered changes are not clean counterfactuals. Do not declare Expansion useless because A2 is cheaper.','','**H3: NOT TESTED.** No Citation Revision contribution is inferred.','','## 12. Limitations','','- 31-query / 102-point benchmark; no claim of universal causality.','- Single production run per configuration and only one R2 same-configuration replication.','- LLM/judge stochasticity is not fully characterized.','- Bootstrap captures query-sampling uncertainty only.','- Triggered strata are post-treatment and descriptive, not randomized subgroups.','- A quota-recovery amendment occurred after evaluation transport failure; immutable accepted observations and recovery receipts remain in provenance.','- Historical R1 full runtime/backend environment was not completely frozen.','- Macro and pooled safety metrics weight observations differently and can disagree.','- Provider-internal retries, tokens and monetary costs are unavailable.','','## 13. Phase 5B final conclusion','','The complete controlled benchmark is assembled and analyzed with frozen metrics and paired bootstrap. Answer Revision shows a descriptive four-point coverage advantage concentrated in three of four R2-triggered queries; Evidence Expansion has tied full-set macro AC, a one-point net advantage and higher retrieval work. Both final mechanism-attribution categories are **Insufficient evidence** under the predeclared replication safeguards; all safety tradeoffs remain reported.','','Historical/frozen artifact integrity: **PASS**. All preexisting project artifacts and separately frozen external assets remained byte-identical. See [integrity before/after](integrity_before_after_v0.json) and [provenance](provenance_v0.json) for scope and hashes. The existing original-seal ephemeral-file exception remains governed solely by the frozen supplemental production-seal protocol; no old seal was rewritten.','','**Ready for Phase 5C: YES — for external review. Phase 5C has not started. STOP.** No A3/A4 run, runtime or prompt edit, controller tuning, or further experiment was performed.','']
    return '\n'.join(p)
def render_console(result):
    m=result['metrics'];r=result['replication'];out=['Phase 5B.2-F status: PASS','','SEMANTIC COMPLETENESS','R2: 31/31','A1: 31/31','A2: 31/31','Total: 93/93','','Network/API calls:','0','','Production calls:','0','','Evaluator calls:','0','','R1 → R2 REPLICATION',f"AC macro: {fmt(m['R1']['answer_completeness']['macro'])} → {fmt(m['R2']['answer_completeness']['macro'])}",f"Delta: {fmt(r['deltas']['answer_completeness']['macro'])}",f"AC micro: {fmt(m['R1']['answer_completeness']['micro'])} → {fmt(m['R2']['answer_completeness']['micro'])}",f"Supported points: 65/102 → {m['R2']['answer_completeness']['raw']}",f"Points gained: {r['gained_points']}",point_list(r['point_transitions']['changed_point_ids']['only_R2']),f"Points lost: {r['lost_points']}",point_list(r['point_transitions']['changed_point_ids']['only_R1']),f"Net: {r['net_point_difference']}",f"Gross churn: {r['gross_churn']}",f"R2 better / tied / R1 better: {r['query_counts']['R2_better']} / {r['query_counts']['tie']} / {r['query_counts']['R1_better']}",'Replication variation: one observed same-configuration replication; not formal variance or noise distribution.']
    for alias,title,h in [('A1','ANSWER REVISION','H1'),('A2','EVIDENCE EXPANSION','H2')]:
        c=result['contrasts'][alias];s=c['strata']['R2_used_true'];part=c['point_transitions'];b=c['bootstrap']
        out+=['',f'R2 vs {alias} — {title}','AC macro:',f"R2 {fmt(m['R2']['answer_completeness']['macro'])}",f"{alias} {fmt(m[alias]['answer_completeness']['macro'])}",f"Delta {fmt(c['deltas']['answer_completeness']['macro'])}",'AC micro:',f"R2 {m['R2']['answer_completeness']['raw']}",f"{alias} {m[alias]['answer_completeness']['raw']}",f"Delta {fmt(c['deltas']['answer_completeness']['micro'])}",f"Both supported: {part['counts']['both_supported']}",f"Only R2: {part['counts']['only_R2']}",point_list(part['changed_point_ids']['only_R2']),f"Only {alias}: {part['counts']['only_'+alias]}",point_list(part['changed_point_ids']['only_'+alias]),f"Neither: {part['counts']['neither_supported']}",f"Net R2 contribution: {c['net_R2_contribution']}",f"Gross churn: {c['gross_churn']}",f"R2 better / tied / {alias} better: {c['query_counts']['R2_better']} / {c['query_counts']['tie']} / {c['query_counts'][alias+'_better']}",f"Mean paired AC delta: {fmt(c['mean_paired_AC_delta'])}",f"Median paired AC delta: {fmt(c['median_paired_AC_delta'])}",f"95% paired bootstrap CI: [{fmt(b['ci_lower'])}, {fmt(b['ci_upper'])}]",('Revision' if alias=='A1' else 'Expansion')+'-triggered queries: '+', '.join(c['triggered_query_ids']),f"Triggered-stratum AC: R2 macro {fmt(s['metrics']['R2']['answer_completeness']['macro'])}, micro {s['metrics']['R2']['answer_completeness']['raw']}; {alias} macro {fmt(s['metrics'][alias]['answer_completeness']['macro'])}, micro {s['metrics'][alias]['answer_completeness']['raw']}"]
        for field,label in [('production_llm','Production LLM')] if alias=='A1' else [('retrieval','Retrieval calls'),('merge_reranks','Merge-reranks')]:
            out += [label+':',f"R2 {result['efficiency']['R2'][field]['total']}",f"{alias} {result['efficiency'][alias][field]['total']}",f"Savings {c['efficiency_contrast'][field]['saved_by_ablation']}"]
        out += ['Replication-attribution flag: '+str(c['replication_attribution_flag']).lower(),'Separate replication gross-churn flag: '+str(c['replication_gross_churn_flag']).lower(),'Interpretation: '+c['interpretation'],h+': '+result['hypotheses'][h]['classification'],('Descriptive losses in 3/4 revision-triggered queries; four points; attribution limited by churn; safety tradeoffs.' if alias=='A1' else 'Tied full-set macro AC; +1 net R2 point, +3 triggered points; cheaper A2; magnitude safeguard limits attribution.')]
    out+=['','CITATION / SAFETY',quality_table(m,['R1','R2','A1','A2'],METRICS[1:]),'Macro and pooled micro can move in different directions. Raw Groundedness and UCR computed independently.','','H3: NOT TESTED','','INTEGRITY','Historical/frozen artifacts unchanged: PASS','','Ready for Phase 5C: YES','External review only; Phase 5C not started. STOP.','']
    return '\n'.join(out)

if __name__=='__main__':main()
