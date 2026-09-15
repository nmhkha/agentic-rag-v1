"""Offline validation of missing-data gates, raw ratios, bootstrap and saved judgments."""
import copy
import json
from pathlib import Path
from analyze_frozen import summarize, partition, paired_statistics, bootstrap, rows
from evaluate_frozen import OUT, ROOT, VARIANTS, require, exclusive_json, file_hash
from evaluate_standard_rag import parse_judge

def run():
    checked=[]
    sample=dict(query_id='q',required_point_ids=['P1','P2'],supported_point_ids=['P1'],
        citation_supported_point_ids=['P1'],answer_completeness=.5,citation_completeness=.5,
        citation_correctness=1.,groundedness=.75,unsupported_claim_rate=.5,citation_valid=True,
        generation_error=None,evaluation_error=None,
        judge=dict(claim_count=4,grounded_claim_count=3,unsupported_claim_count=2,
                   cited_claim_count=2,correctly_cited_claim_count=2))
    m=summarize([sample],{'q':2})
    require(m['groundedness']['pooled_micro']==.75 and m['unsupported_claim_rate']['pooled_micro']==.5,
            'claim metrics inferred rather than independently counted')
    require(len(m['anomalies'])==1,'unreconciled claim counts not flagged')
    checked.append('Independent raw groundedness/UCR ratios and retained count anomaly')
    zero=copy.deepcopy(sample)
    zero['query_id']='z'
    zero['judge'].update(claim_count=0,grounded_claim_count=0,unsupported_claim_count=0,cited_claim_count=0,correctly_cited_claim_count=0)
    zero.update(citation_correctness=None,groundedness=None,unsupported_claim_rate=None)
    m=summarize([sample,zero],{'q':2,'z':2})
    require(m['groundedness']['macro_query_denominator']==1 and m['groundedness']['denominator']==4,
            'zero denominator imputed')
    checked.append('Zero claim denominator stays null and is excluded only from defined-ratio macro')
    missing=copy.deepcopy(sample)
    missing.update(query_id='missing',evaluation_error={'type':'test'},answer_completeness=None,citation_completeness=None)
    m=summarize([sample,missing],{'q':2,'missing':3})
    require(not m['complete'] and m['answer_completeness']['macro'] is None and m['answer_completeness']['micro'] is None,
            'incomplete primary score leaked')
    require(m['required_point_count']==5 and m['judged_point_denominator']==2 and m['failed_query_ids']==['missing'],
            'missing denominator silently reduced')
    require(partition([sample],[missing],{('q','P1')}) is None and paired_statistics([sample],[missing],True) is None,
            'incomplete point table/bootstrap executed')
    checked.append('Missing-data primary gate with explicit query/point denominators and no bootstrap')
    other=copy.deepcopy(sample); other['supported_point_ids']=['P2']
    p=partition([sample],[other],{('q','P1'),('q','P2')})
    require(p['gross_churn']==2 and p['net_reference_contribution']==0,'net-zero churn lost')
    checked.append('Point partition retains nonzero gross churn at zero net change')
    a,b=bootstrap([1.]*31),bootstrap([0.]*31)
    require(a['ci95']==[1.,1.] and b['ci95']==[0.,0.],'constant paired bootstrap mismatch')
    try:
        bootstrap([1.]*30)
    except ValueError:
        pass
    else:
        raise AssertionError('smaller bootstrap denominator accepted')
    checked.append('Frozen seeded paired bootstrap constant controls and 31-query guard (synthetic only)')
    actual={}
    for alias,variant in VARIANTS.items():
        directory=OUT/variant
        results=rows(directory/'evaluation.jsonl'); attempts=rows(directory/'evaluation_attempts.jsonl')
        require(len(results)==len({r['query_id'] for r in results})==31,'result count')
        counts={}
        for r in results:
            q=r['query_id']
            logs=[x for x in attempts if x['query_id']==q]
            require(1<=len(logs)<=3 and [x['attempt'] for x in logs]==list(range(1,len(logs)+1)), 'attempt order/ceiling')
            require(all(not x['replay'] for x in logs),'unexpected replay')
            slots=list((directory/'attempts'/q).glob('*/request.json'))
            require(len(slots)==len(logs)==r['evaluation_attempts'],'durable attempt/log mismatch')
            accepted=[x for x in logs if x['status']=='valid_parsed_judgment']
            if r['evaluation_error'] is None:
                require(len(accepted)==1 and logs[-1]==accepted[0],'first valid judgment not terminal')
                response=json.loads((directory/'attempts'/q/str(logs[-1]['attempt'])/'response.json').read_text())
                parsed=parse_judge(response['raw'],r['required_point_ids'])
                require(parsed['raw']==r['judge'],'saved judgment differs from first valid raw response')
                support=[pid for pid in r['required_point_ids'] if parsed['by_id'][pid]['supported']]
                cited=[pid for pid in support if parsed['by_id'][pid]['citation_supported']]
                require(support==r['supported_point_ids'] and cited==r['citation_supported_point_ids'], 'saved point labels changed')
                require(r['answer_completeness']==len(support)/len(r['required_point_ids']),'AC ratio mismatch')
            else:
                require(not accepted and len(logs)==3,'failed query did not exhaust frozen attempts')
                require(all(x['status']=='transport_error' and 'LLM HTTP 429:' in x['error'] for x in logs),'unexpected failure class')
            production=json.loads((ROOT/'data/rag/traces/phase5'/variant/'outputs'/(q+'.json')).read_text())
            require(r['trace']==production['trace'] and r['query']==production['query'],'immutable production input changed')
            counts[q]=len(logs)
        actual[alias]=dict(judged=sum(r['evaluation_error'] is None for r in results),attempts=len(attempts),
                          failed_attempts=sum(x['status']!='valid_parsed_judgment' for x in attempts),per_query_attempts=counts)
    checked.append('All 93 real records: original trace equality, exact attempt slots, first valid raw judgment, no fourth calls')
    exclusive_json(OUT/'analysis_validation.json',dict(status='PASS',checks=checked,actual=actual,
        validation_source_sha256=file_hash(__file__),analysis_source_sha256=file_hash(OUT/'analyze_frozen.py'),
        test_bootstraps='Synthetic constant controls only; no incomplete experiment bootstrap',network_calls=0))
    print(json.dumps(dict(status='PASS',checks=len(checked),actual={a:{k:v for k,v in d.items() if k!='per_query_attempts'} for a,d in actual.items()})))

if __name__=='__main__':
    run()
