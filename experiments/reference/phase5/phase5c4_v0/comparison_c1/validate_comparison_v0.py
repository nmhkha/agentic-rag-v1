"""Independent consistency checks for C1 outputs; no source mutations."""
from pathlib import Path
import collections
import hashlib
import json
import os
import sys
import traceback

HERE=Path(__file__).resolve().parent
N={'__name__':'comparison_validation_import','__file__':str(HERE/'build_comparison_v0.py')}
exec(compile((HERE/'build_comparison_v0.py').read_bytes(),'build_comparison_v0.py','exec'),N)
checks=[]

def check(condition,name):
    if not condition:raise RuntimeError(name)
    checks.append({'check':name,'status':'PASS'})

def main():
    os.umask(0o077);Path(__file__).chmod(0o600)
    read=N['read'];rows=N['rows'];ROOT=N['ROOT'];BASE=N['BASE'];rel=N['rel'];sha=N['sha'];compact=N['compact']
    before=read(HERE/'integrity_baseline_v0.json')['entries']
    registry=read(HERE/'artifact_hashes_v0.json')['artifacts']
    check(all(N['fhash'](ROOT/p)==v['sha256'] for p,v in registry.items()),'C1_GENERATED_HASHES_MATCH')
    A=rows(N['AP']);B=rows(N['BP']);C=rows(N['CP']);M=read(N['MP'])['mapping']
    alignment=N['align'](A,B,C,M)
    check(alignment==read(HERE/'ab_candidate_alignment_v0.json')['alignment'],'ALIGNMENT_RECOMPUTED_EXACTLY')
    maps=rows(HERE/'ab_aspect_mapping_v0.jsonl');support=rows(HERE/'ab_support_comparison_v0.jsonl')
    axes=rows(HERE/'ab_applicability_sufficiency_comparison_v0.jsonl');scopes=rows(HERE/'ab_scope_comparison_v0.jsonl')
    issues=rows(HERE/'ab_disagreement_registry_v0.jsonl');contam=rows(HERE/'ab_contamination_comparison_v0.jsonl')
    metrics=read(HERE/'phase5c4c1_agreement_metrics_v0.json');summary=read(HERE/'phase5c4c1_disagreement_summary_v0.json')
    mids={x['mapping_id']:x for x in maps};qs={x['canonical_candidate_id'] for x in alignment}
    check(len(mids)==len(maps),'UNIQUE_ASPECT_MAPPING_IDS')
    check({x['mapping_id'] for x in support}==set(mids) and len(support)==len(mids),'SUPPORT_COVERS_EVERY_MAPPING')
    matched={m['mapping_id'] for m in maps if m['A_aspect_refs'] and m['B_aspect_refs']}
    check({x['mapping_id'] for x in axes}==matched and len(axes)==len(matched),'AXES_COVER_EVERY_MATCHED_GROUP')
    check(len(scopes)==len(contam)==60 and {x['canonical_candidate_id'] for x in scopes}==qs and {x['canonical_candidate_id'] for x in contam}==qs,'SCOPE_AND_CONTAMINATION_COVER_ALL_CANDIDATES')
    for al in alignment:
        q=al['canonical_candidate_id'];aa=A[al['A_record']];bb=B[al['B_record']]
        mm=[x for x in maps if x['canonical_candidate_id']==q]
        for side,source,key in [('A',aa,'aspect_id'),('B',bb,'aspect_id_b')]:
            actual=[v for x in mm for v in x[side+'_aspect_ids']]
            expected=[v[key] for v in source['required_legal_aspects']]
            check(sorted(actual)==sorted(expected) and len(actual)==len(set(actual)),side+'_ASPECT_PARTITION_'+str(al['A_record']))
        ss=next(x for x in scopes if x['canonical_candidate_id']==q)
        check({x['field'] for x in ss['components']}==set(N['SCOPE_FIELDS']),'FIVE_SCOPE_COMPONENTS_'+str(al['A_record']))
        for v in ss['components']:
            field=v['field']
            check(v['A_value_sha256']==sha(compact(aa['scope'][field])) and v['B_value_sha256']==sha(compact(bb['scope'][field])),'SCOPE_SOURCE_HASH_'+str(al['A_record'])+'_'+field)
    check(all(x['status']=='UNRESOLVED' for x in issues),'NO_SILENT_ISSUE_RESOLUTION')
    required={'issue_id','canonical_candidate_id','field_family','A_value_ref','B_value_ref','aspect_mapping_ref','severity','reason_for_review','requires_legal_adjudication','status'}
    check(all(required<=set(x) and x['canonical_candidate_id'] in qs for x in issues),'ISSUE_SCHEMA_AND_CANDIDATES')
    check(len({x['issue_id'] for x in issues})==len(issues),'UNIQUE_ISSUE_IDS')
    check(all(x['aspect_mapping_ref'] is None or x['aspect_mapping_ref']['mapping_id'] in mids for x in issues),'ISSUE_MAPPING_REFS_RESOLVE')
    cache={}
    def resolve(value):
        if isinstance(value,list):
            for v in value:resolve(v)
        elif isinstance(value,dict):
            if 'path' in value:
                path=ROOT/value['path'];check(path.exists(),'SOURCE_REFERENCE_EXISTS')
                if 'json_pointer' in value or 'record_index_zero_based' in value:
                    if path not in cache:cache[path]=rows(path) if path.suffix=='.jsonl' else read(path)
                    obj=cache[path]
                    if 'record_index_zero_based' in value:obj=obj[value['record_index_zero_based']]
                    for key in value.get('json_pointer','').split('/')[1:]:
                        key=key.replace('~1','/').replace('~0','~')
                        obj=obj[int(key)] if isinstance(obj,list) else obj[key]
            for k,v in value.items():
                if isinstance(v,(dict,list)):resolve(v)
    for x in issues:
        resolve(x['A_value_ref']);resolve(x['B_value_ref'])
    counts=collections.Counter(x['canonical_candidate_id'] for x in issues)
    check(summary['unresolved_issue_count']==len(issues),'REGISTRY_TOTAL_MATCHES_SUMMARY')
    for row in summary['candidates']:
        ii=[x for x in issues if x['canonical_candidate_id']==row['canonical_candidate_id']]
        check(row['unresolved_issue_count']==len(ii) and row['comparison_priority']==max((x['severity'] for x in ii),key=N['RANK'].__getitem__,default='LOW'),'CANDIDATE_SEVERITY_RECOMPUTED')
    expected_priority=collections.Counter(x['comparison_priority'] for x in summary['candidates'])
    check(all(summary['candidate_priority_distribution'][k]==expected_priority[k] for k in N['RANK']),'CANDIDATE_PRIORITY_TOTALS')
    check(sum(summary['candidate_priority_distribution'].values())==60,'SEVERITY_DENOMINATOR_IS_CANDIDATES')
    check(sum(summary['issue_severity_distribution'].values())==len(issues),'ISSUE_SEVERITY_DENOMINATOR')
    check(metrics['candidates_with_full_substantive_agreement']==sum(counts[q]==0 for q in qs),'FULL_AGREEMENT_COUNT_IS_CONSERVATIVE')
    answer=[];admission=[]
    for al in alignment:
        a=A[al['A_record']];b=B[al['B_record']];c=C[al['canonical_record']]
        answer.append((a['answerability']['label'],b['answerability']['label']))
        admission.append(('retain' if c['admission'].startswith('RETAIN') else c['admission'].lower(),b['admission_recommendation']['label'].lower()))
        check(c['dimensions']['D6']['member'] is None and b['dimensions']['D6']['value'] is None,'D6_NOT_CHARACTERIZED')
    for key,pairs,labels_a,labels_b in [('answerability',answer,N['ANS'],N['ANS']),('admission',admission,N['ADM_A'],N['ADM_B'])]:
        m=N['matrix'](labels_a,labels_b,pairs,metrics[key]['eligibility'])
        check(m==metrics[key],key.upper()+'_FULL_MATRIX_RECOMPUTED')
    for d in N['DIMS']:
        c=collections.Counter((C[x['canonical_record']]['dimensions'][d]['member'],B[x['B_record']]['dimensions'][d]['value']) for x in alignment)
        e=metrics['dimensions'][d]
        check([e['both_present'],e['A_only'],e['B_only'],e['both_absent']]==[c[True,True],c[True,False],c[False,True],c[False,False]],d+'_COUNTS_RECOMPUTED')
    for axis,labels in [('applicability',N['APP']),('sufficiency',N['SUFF'])]:
        all_pairs=[];strict=[]
        for x in axes:
            m=mids[x['mapping_id']]
            if len(m['A_aspect_refs'])==len(m['B_aspect_refs'])==1:
                pair=(x['A_'+axis+'_labels'][0],x['B_'+axis+'_labels'][0]);all_pairs.append(pair)
                if m['relationship']=='equivalent':strict.append(pair)
        for suffix,pairs in [('equivalent_one_to_one',strict),('all_one_to_one_diagnostic',all_pairs)]:
            key=axis+'_'+suffix
            check(N['matrix'](labels,labels,pairs,metrics[key]['eligibility'])==metrics[key],key.upper()+'_RECOMPUTED')
    # Synthetic controls: mixed labels are not pooled, parent/text coordinates
    # cannot match, adjacent spans merge, AND and OR structure is retained.
    s=('doc','1','2','','chunk','text',0,10)
    parent=('doc','1','2','','chunk','parent_context',0,10)
    small=('doc','1','2','','chunk','text',2,8)
    adjacent=('doc','1','2','','chunk','text',10,15)
    check(not N['span_contains']([s],[parent]),'CONTROL_DISTINCT_PARENT_TEXT_COORDINATES')
    check(N['span_contains']([s],[small]) and not N['span_contains']([small],[s]),'CONTROL_SPAN_CONTAINMENT_DIRECTION')
    check(N['normalize_branch']([s,adjacent])==(s[:-2]+(0,15),),'CONTROL_ADJACENT_SPAN_NORMALIZATION')
    check(N['support_class']([(s,)],[(small,)],'equivalent')=='A superset','CONTROL_A_SUPERSET')
    check(N['support_class']([(small,)],[(s,)],'equivalent')=='B superset','CONTROL_B_SUPERSET')
    check(N['support_class']([],[(s,)],'equivalent')=='unresolved support disagreement','CONTROL_ABSENT_SUPPORT_NOT_EQUIVALENT')
    check(N['support_class']([(s,),(parent,)],[(s,parent)],'equivalent')!='equivalent support','CONTROL_OR_NOT_COLLAPSED_INTO_AND')
    check(N['matrix'](N['ANS'],N['ANS'],[],'none')['raw_agreement'] is None,'CONTROL_ZERO_ELIGIBILITY_NOT_PERFECT_AGREEMENT')
    for x in axes:
        delta=set(x['A_sufficiency_labels'])^set(x['B_sufficiency_labels'])
        if 'no_support_in_corpus' in delta:
            check(any(i['field_family']=='sufficiency' and i['aspect_mapping_ref'] and i['aspect_mapping_ref']['mapping_id']==x['mapping_id'] and 'LEGAL_REVIEW_HIGH_PRIORITY' in i['review_flags'] for i in issues),'ABSENCE_DISAGREEMENT_HIGH_PRIORITY')
    # Re-resolve source spans, respecting explicitly recorded parent anchors.
    chunks={r['chunk_id']:r for r in rows(ROOT/'data/versions/corpus-v0.1/chunks.jsonl')}
    for a in A:N['bundle_formula'](a['required_legal_aspects'],'A',chunks)
    for b in B:N['bundle_formula'](b['required_legal_aspects'],'B',chunks)
    check(True,'ALL_A_B_SUPPORT_ANCHORS_REVALIDATED')
    check(all('reviewer_b_results_v1/' in x['B_value_ref']['path'] for x in alignment),'ONLY_SUCCESSFUL_B_ANNOTATION_COMPARED')
    public=read(HERE/'phase5c4c1_validation_v0.json')['public_safe_files']
    secrets=[x['query'].encode() for x in C]+[t['proposition'].encode() for x in A+B for t in x['required_legal_aspects']]
    check(all(not any(s in (HERE/f).read_bytes() for s in secrets) for f in public),'PUBLIC_ARTIFACTS_QUERY_AND_PROPOSITION_FREE')
    current=N['snapshot']()
    check(all(current.get(k)==v for k,v in before.items()),'ALL_PREEXISTING_BYTES_MODES_SYMLINKS_UNCHANGED')
    check(all((ROOT/k).parent==HERE for k in current.keys()-before.keys()),'ALL_ADDITIONS_ONLY_C1')
    evidence={'status':'PASS','check_count':len(checks),'checks':checks,'scope':'Source alignment, exhaustive mapping, reference resolution, denominators, severity, absence flags, byte integrity and public confidentiality; not legal adjudication.',
              'source_hashes':{rel(p):N['fhash'](p) for p in [N['AP'],N['BP'],N['CP'],N['MP']]},
              'private_artifact':True,'annotation_or_adjudication_performed':False}
    N['dump']('comparison_check_results_v0.json',evidence)
    N['dump']('final_artifact_hashes_v0.json',{'purpose':'C1 completed comparison and validation inventory; not dataset freeze','algorithm':'sha256','self_excluded':True,
                                           'private_addendum_files':['validate_comparison_v0.py','comparison_check_results_v0.json','final_artifact_hashes_v0.json'],
                                           'artifacts':{rel(p):{'sha256':N['fhash'](p),'size_bytes':p.stat().st_size} for p in sorted(HERE.iterdir()) if p.is_file()}})
    print('C1 verification PASS:',len(checks),'checks; all preexisting bytes unchanged; no public query/proposition leakage.')

if __name__=='__main__':
    try:main()
    except Exception as e:
        print('C1 independent verification FAILED; legal-review handoff is not cleared by this verifier.',file=sys.stderr)
        print('Error type:',type(e).__name__,file=sys.stderr)
        if isinstance(e,RuntimeError):print('Check code:',str(e),file=sys.stderr)
        print('Code locations:',[(t.name,t.lineno) for t in traceback.extract_tb(e.__traceback__)],file=sys.stderr)
        raise SystemExit(1) from None
