"""Independent read-only verification against frozen Phase 5B.2-E functions.

Run: python3 -B data/evaluation/generation/phase5/phase5b2f_v0/analysis_tools/verify_final_analysis_v0.py
The --record option exclusively creates validation artifacts on its first run.
"""
import ast, collections, hashlib, json, math, os, random, statistics, sys
from fractions import Fraction
from pathlib import Path
ROOT=Path.cwd();BASE=ROOT/'data/evaluation/generation/phase5';OUT=BASE/'phase5b2f_v0'
sys.dont_write_bytecode=True
blocked=[]
def guard(event,args):
    if event.startswith('socket.') or event in ('urllib.Request','http.client.connect','http.client.send','subprocess.Popen','os.system','os.posix_spawn'):
        blocked.append(event);raise RuntimeError('offline validation transport/child-process prohibition')
sys.addaudithook(guard)
def sha(p):
    with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def read(p):return json.loads(Path(p).read_text())
def rows(p):return [json.loads(x) for x in Path(p).read_text().splitlines() if x]
def require(c,m):
    if not c:raise AssertionError(m)
def digest(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def same_number(a,b):return a==b or a is not None and b is not None and math.isclose(a,b,rel_tol=0,abs_tol=5e-16)
V={'R2':'full-agentic-replication','A1':'agentic-v1-no-answer-revision','A2':'agentic-v1-no-evidence-expansion'}
checks=[]
def passed(name):checks.append(name)
def main():
    provenance=read(OUT/'provenance_v0.json')
    for name,h in provenance['artifacts'].items():require(sha(OUT/name)==h,'analysis artifact hash drift: '+name)
    passed('All declared analysis artifact byte hashes')
    design=read(BASE/'phase5a_ablation_manifest_v0.json');order=design['query_order']
    gold=read(ROOT/'data/evaluation/generation/generation_eval_v1_verified.json')['items'];items={r['query_id']:r for r in gold}
    universe={(r['query_id'],p['point_id']) for r in gold for p in r['required_points']};require(len(universe)==102,'frozen universe')
    manifest=read(OUT/'canonical_judgments_manifest.json');require(manifest['query_order']==order,'query order')
    records={a:rows(OUT/v/'evaluation_complete.jsonl') for a,v in V.items()}
    records['R1']=rows(ROOT/'data/evaluation/generation/agentic_rag_eval_v1_agentic-v1.jsonl')
    for a,r in records.items():require(len(r)==31 and [x['query_id'] for x in r]==order,a+' cohort completeness')
    sources={(r['alias'],r['query_id']):r for r in manifest['records']};require(len(sources)==93,'unique source slots')
    counts=collections.Counter()
    for a in V:
        for row in records[a]:
            q=row['query_id'];s=sources[a,q];item=items[q];counts[s['judgment_source']]+=1
            require(s['variant_id']==V[a] and s['query_id']==q,'variant identity')
            require(sha(ROOT/s['source_record_path'])==s['source_record_hash'],'source record byte hash')
            require(row==read(ROOT/s['source_record_path']) and digest(row)==s['canonical_record_hash'],'semantic payload equality')
            prod=read(ROOT/s['production_output_path']);require(sha(ROOT/s['production_output_path'])==s['production_output_hash'],'production hash')
            require(all(row[k]==v for k,v in prod.items()),'production payload equality')
            require(hashlib.sha256(prod['trace']['final_answer'].encode()).hexdigest()==s['production_answer_sha256'],'answer hash')
            require(row['query']==item['query'] and s['required_point_ids']==row['required_point_ids']==[p['point_id'] for p in item['required_points']],'gold binding')
            require(row['generation_error'] is None and row['evaluation_error'] is None and 'judge' in row,'valid semantic observation')
    require(counts=={'phase5b2e_v0':64,'phase5b2er2_v1':29},'64+29 authority')
    passed('93 unchanged semantic payloads, unique authorities, frozen gold/query/production/answer/variant bindings')
    # Execute only selected pure arithmetic functions from the existing frozen
    # offline analysis; exclude imports, main, gate and all evaluator wiring.
    frozen=BASE/'phase5b2e_v0/analyze_frozen.py';tree=ast.parse(frozen.read_text())
    names={'ratio','subtract','valid','summarize','metric_deltas','ac_fraction','partition','bootstrap','paired_statistics','interpretation'}
    constants=[n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id in ('FIELDS','CLAIMS') for t in n.targets)]
    code=ast.Module(body=constants+[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names],type_ignores=[])
    ns={'Fraction':Fraction,'math':math,'random':random,'mean':statistics.mean,'median':statistics.median,'sys':sys,'require':require}
    exec(compile(code,str(frozen),'exec'),ns)
    sizes={q:len(items[q]['required_points']) for q in order}
    frozen_metrics={a:ns['summarize'](r,sizes) for a,r in records.items()}
    result=read(OUT/'phase5b2f_metrics_v0.json')
    for a,f in frozen_metrics.items():
        actual=result['metrics'][a]
        for k in ns['FIELDS']:
            fk='micro' if k in ns['FIELDS'][:2] else 'pooled_micro'
            require(same_number(f[k]['macro'],actual[k]['macro']) and f[k][fk]==actual[k]['micro'],a+' frozen metric '+k)
            require(f[k]['numerator']==actual[k]['numerator'] and f[k]['denominator']==actual[k]['denominator'],a+' raw counts '+k)
        require(f['citation_syntax_validity']['rate']==actual['citation_syntax_validity']['micro'],'syntax ratio')
        require(f['anomalies']==actual['raw_count_anomalies']==[],'raw count anomaly parity')
    passed('All R1/R2/A1/A2 primary, citation and safety metrics reproduce frozen summarize semantics and raw counts')
    rep={'paired_statistics':ns['paired_statistics'](records['R2'],records['R1']),'point_partition':ns['partition'](records['R2'],records['R1'],universe)}
    expected_costs={}
    for a,v in V.items():
        co=[]
        for q,row in zip(order,records[a]):
            t=row['trace'];obs=read(ROOT/'data/rag/traces/phase5'/v/'observations'/(q+'.json'));ev=obs['events']
            c={'retrieval':sum(x['logical_call_type']=='retrieval' for x in ev),'production_llm':sum(x['logical_call_type']=='llm' for x in ev),'merge_reranks':sum(x['logical_call_type']=='merge_rerank' for x in ev),'observable_http_submissions':sum(x['observable_http_attempts'] for x in ev if x['logical_call_type']=='llm')};co.append(c)
            require(c['retrieval']==t['retrieval_call_count']==len(t['retrieval_calls']) and c['production_llm']==t['llm_call_count']==len(t['llm_calls']),'cost ledgers/trace parity')
        expected_costs[a]=co
        for k in co[0]:
            vals=[r[k] for r in co];e=result['efficiency'][a][k]
            require(e=={'total':sum(vals),'mean':statistics.mean(vals),'median':statistics.median(vals),'max':max(vals)},'efficiency statistics '+a+'/'+k)
    passed('Sealed production event counts, HTTP submissions and trace totals; all efficiency summary statistics')
    for alias in ('R1','A1','A2'):
        left,right=records['R2'],records[alias];fpart=ns['partition'](left,right,universe)
        filename='point_transitions_R1_R2.jsonl' if alias=='R1' else 'point_transitions_R2_'+alias+'.jsonl'
        p=rows(OUT/filename);require(len(p)==102 and {(x['query_id'],x['point_id']) for x in p}==universe,'point file universe')
        remap={'both_supported':'both_supported','only_reference':'only_R2','only_comparator':'only_'+alias,'neither_supported':'neither_supported'}
        for k,identities in fpart['identities'].items():require({(x['query_id'],x['point_id']) for x in p if x['transition']==remap[k]}=={(x['query_id'],x['point_id']) for x in identities},'point identities '+alias+'/'+k)
        if alias=='R1':continue
        c=read(OUT/('contrast_R2_'+alias+'.json'));require(c==result['contrasts'][alias],'contrast aggregation parity')
        fstats=ns['paired_statistics'](left,right,True);b=read(OUT/('bootstrap_R2_'+alias+'.json'))
        require([b['ci_lower'],b['ci_upper']]==fstats['bootstrap']['ci95'],'exact frozen bootstrap endpoints')
        require(b['observed_delta']==fstats['mean_ac_difference']==c['mean_paired_AC_delta'],'exact frozen observed delta')
        require(c['median_paired_AC_delta']==fstats['median_ac_difference'],'paired median')
        require(c['query_counts']=={'R2_better':fstats['reference_better'],'tie':fstats['tied'],alias+'_better':fstats['comparator_better']},'exact paired sign counts')
        # Independent reconstruction checks every bootstrap draw, not just bounds.
        rng=random.Random(20260906);d=[float(ns['ac_fraction'](a)-ns['ac_fraction'](z)) for a,z in zip(left,right)]
        means=sorted(sum(d[rng.randrange(31)] for _ in range(31))/31 for _ in range(10000))
        require(digest(means)==b['sorted_bootstrap_means_canonical_sha256'],'exact frozen bootstrap draw digest')
        flag='revision_used' if alias=='A1' else 'expansion_used';ids=[r['query_id'] for r in left if r['trace'][flag]]
        require(c['triggered_query_ids']==ids,'sealed R2 trigger derivation')
        strata={}
        for used in (True,False):
            qs=[r['query_id'] for r in left if r['trace'][flag]==used];lr=[r for r in left if r['query_id'] in qs];rr=[r for r in right if r['query_id'] in qs]
            ms=[ns['summarize'](r,sizes) for r in (lr,rr)]
            strata[str(used).lower()]={'query_count':len(qs),'paired_statistics':ns['paired_statistics'](lr,rr),'point_partition':ns['partition'](lr,rr,{x for x in universe if x[0] in qs})}
            st=c['strata']['R2_used_'+str(used).lower()];require(st['query_ids']==qs and st['required_point_denominator']==sum(sizes[q] for q in qs),'stratum membership/denominator')
            for a,m in zip(('R2',alias),ms):
                for k in ns['FIELDS']:
                    pool='micro' if k in ns['FIELDS'][:2] else 'pooled_micro'
                    require(same_number(m[k]['macro'],st['metrics'][a][k]['macro']) and m[k][pool]==st['metrics'][a][k]['micro'],'stratum metric parity')
        adapter={'complete':True,'paired_statistics':fstats,'point_partition':fpart,'strata':strata,'metric_deltas':ns['metric_deltas'](frozen_metrics['R2'],frozen_metrics[alias]),'savings_relative_to_R2':{'retrieval':sum(x['retrieval'] for x in expected_costs['R2'])-sum(x['retrieval'] for x in expected_costs[alias]),'llm':sum(x['production_llm'] for x in expected_costs['R2'])-sum(x['production_llm'] for x in expected_costs[alias])}}
        label,reasons=ns['interpretation'](adapter,rep)
        require(label==c['interpretation'],'frozen interpretation precedence')
        sg=adapter['replication_safeguards'];require(sg['magnitude_attribution_limited']==c['replication_attribution_flag'] and sg['gross_churn_attribution_weakness']==c['replication_gross_churn_flag'],'frozen safeguard flags')
        feature='answer_revision' if alias=='A1' else 'expansion'
        observed=[]
        for q in order:
            meta=read(ROOT/'data/rag/traces/phase5'/V[alias]/'observations'/(q+'.json'))['metadata']
            observed.append((q,q in ids,meta[feature+'_would_have_triggered'],meta[feature+'_blocked_by_ablation']))
        require(sum(x['query_count'] for x in c['cross_tab'])==31,'cross-tab total')
        for cell in c['cross_tab']:
            qs=[q for q,u,w,blo in observed if (u,w,blo)==(cell['R2_used'],cell[alias+'_would_have_triggered'],cell[alias+'_blocked_by_ablation'])]
            require(qs==cell['query_ids'] and len(qs)==cell['query_count'],'three-way trigger cross-tab')
        for x,y,pair in zip(left,right,c['per_query']):
            q=x['query_id'];require(pair['query_id']==q,'paired row order')
            require(Fraction(pair['AC_delta_exact'])==ns['ac_fraction'](x)-ns['ac_fraction'](y),'per-query exact delta')
            for a,row in [('R2',x),(alias,y)]:
                for k in ns['FIELDS']:require(pair[a][k]==row[k],'per-query metric source parity')
        passed(alias+': exact frozen bootstrap endpoints, all 10,000 means, paired signs, 102-point transitions, both strata, cross-tab and interpretation precedence ('+label+')')
    report=(OUT/'phase5b2f_final_report_v0.md').read_text();headings=[s for s in report.splitlines() if s.startswith('## ')]
    require(len(headings)==13 and [int(s.split('.')[0][3:]) for s in headings]==list(range(1,14)),'report structure/order')
    require(result['hypotheses']['H3']['classification']=='NOT TESTED' and result['phase5c_started'] is False,'stop scope')
    passed('Required 13-section report structure, replication-first order and H3/Phase 5C stop scope')
    before=read(OUT/'integrity_before_inventory_v0.json');current={}
    for parent,dirs,files in os.walk(ROOT):
        dirs[:]=[d for d in dirs if d not in ('.venv','.git','.agents','.codex') and Path(parent)/d!=OUT]
        for name in files:
            p=Path(parent)/name;current[str(p.relative_to(ROOT))]=sha(p)
    require(current==before['project'],'historical changed/missing/added path')
    for path,h in before['external_assets'].items():require(sha(path)==h,'external frozen asset')
    require(not blocked,'transport event attempted')
    require(not any(n in sys.modules for n in ('evaluate_agentic_rag','evaluate_standard_rag','agentic_rag','llm_client')),'forbidden runtime/evaluator imports')
    passed('Final before/after byte integrity: 1,420 project files and 24 external assets; zero outside-namespace additions')
    passed('Zero network/API, production and evaluator calls; no frozen runtime or evaluator module imports')
    validation={'status':'PASS','checks':checks,'check_count':len(checks),'independent_reference':{'path':str(frozen.relative_to(ROOT)),'sha256':sha(frozen),'method':'AST extraction of pure frozen arithmetic/interpretation functions; no module import or evaluator execution'},'bootstrap_exact_endpoint_and_all_draw_parity':True,'frozen_interpretation_parity':{'A1':'Insufficient evidence','A2':'Insufficient evidence'},'project_files_unchanged':len(current),'external_assets_unchanged':len(before['external_assets']),'network_calls':0,'blocked_network_attempts':len(blocked),'production_calls':0,'evaluator_calls':0,'artifact_provenance_sha256':sha(OUT/'provenance_v0.json'),'validator_sha256':sha(__file__),'ready_for_phase5c_review':True,'phase5c_started':False}
    if '--record' in sys.argv:
        target=OUT/'analysis_tools/verify_final_analysis_v0.py'
        require(not target.exists(),'exclusive validator artifact')
        with target.open('x') as f:f.write(Path(__file__).read_text())
        with (OUT/'validation_v0.json').open('x') as f:json.dump(validation,f,indent=2,sort_keys=True);f.write('\n')
        final={str(p.relative_to(OUT)):sha(p) for p in sorted(OUT.rglob('*')) if p.is_file()}
        with (OUT/'final_artifact_hashes_v0.json').open('x') as f:json.dump({'schema':'phase5b2f-final-artifact-hashes-v0','status':'PASS','files':final,'self_hash_policy':'This manifest excludes itself; SHA-256 printed in verification console'},f,indent=2,sort_keys=True);f.write('\n')
    elif (OUT/'final_artifact_hashes_v0.json').exists():
        seal=read(OUT/'final_artifact_hashes_v0.json')
        for p,h in seal['files'].items():require(sha(OUT/p)==h,'final artifact seal '+p)
        require({str(p.relative_to(OUT)) for p in OUT.rglob('*') if p.is_file()}==set(seal['files'])|{'final_artifact_hashes_v0.json'},'undeclared final artifact')
    print(json.dumps(validation,indent=2))
    if (OUT/'final_artifact_hashes_v0.json').exists():print('Final artifact manifest SHA-256:',sha(OUT/'final_artifact_hashes_v0.json'))

if __name__=='__main__':main()
