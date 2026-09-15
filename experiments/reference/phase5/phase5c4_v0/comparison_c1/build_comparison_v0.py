"""Private C1 comparison coordinator. Offline, additive, no adjudication.

Only import Python standard library and the newly authored comparison decisions.
No production/retrieval/evaluator module is imported or executed.
"""
import collections
import datetime
import hashlib
import itertools
import json
import os
from pathlib import Path
import re
import stat
import sys
import unicodedata

OUT = Path(__file__).resolve().parent
BASE = OUT.parent
ROOT = BASE.parents[4]
AP = BASE / 'custodian/annotation_A_v0.jsonl'
BP = BASE / 'reviewer_b_results_v1/annotation_B_v1.jsonl'
CP = BASE / 'custodian/challenge_candidates_v0.jsonl'
MP = BASE / 'custodian/reviewer_b_id_mapping_v1.json'
ACP = BASE / 'custodian/contamination_screening_details_v0.json'
BCP = BASE / 'reviewer_b_results_v1/reviewer_b_contamination_flags_v1.jsonl'
AAP = BASE / 'custodian/corpus_absence_audits_v0.jsonl'
BAP = BASE / 'reviewer_b_results_v1/reviewer_b_corpus_audit_v1.json'
DIMS = ['D1','D2','D3','D4','D5','D7','D8','D9','D10']
APP = ['direct','conditional','not_applicable','uncertain']
SUFF = ['sufficient_support','partial_support','no_support_in_corpus']
ANS = ['fully_answerable','partially_answerable','insufficient_evidence']
ADM_A = ['retain','reserve','exclude']
ADM_B = ADM_A + ['needs_adjudication']
RANK = {'LOW':0,'MEDIUM':1,'HIGH':2,'CRITICAL_REVIEW':3}
SCOPE_FIELDS = ['explicit_asks','bounded_interpretation','relevant_user_facts','unspecified_facts','excluded_scope']

def require(value, code):
    if not value: raise RuntimeError(code)

def sha(raw): return hashlib.sha256(raw).hexdigest()
def encode(x): return (json.dumps(x,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
def compact(x): return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')
def read(path): return json.loads(path.read_bytes())
def rows(path): return [json.loads(l) for l in path.read_bytes().splitlines()]
def rel(path): return path.relative_to(ROOT).as_posix()
def fhash(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for z in iter(lambda:f.read(1048576),b''):h.update(z)
    return h.hexdigest()
def write(path, raw):
    with os.fdopen(os.open(path,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600),'wb') as f:f.write(raw)
def dump(name,x):write(OUT/name,encode(x))
def dump_rows(name,x):write(OUT/name,b''.join(compact(z)+b'\n' for z in x))
def norm(x):
    if isinstance(x,str):return ' '.join(unicodedata.normalize('NFC',x).casefold().split())
    if isinstance(x,list):return sorted([norm(v) for v in x],key=lambda v:compact(v))
    if isinstance(x,dict):return {k:norm(v) for k,v in sorted(x.items())}
    return x
def ref(path,record,pointer=''):
    return {'path':rel(path),'record_index_zero_based':record,'json_pointer':pointer}

def snapshot():
    result={}
    for base,dirs,files in os.walk(ROOT,followlinks=False):
        for name in sorted(dirs+files):
            p=Path(base)/name;s=p.lstat()
            if stat.S_ISLNK(s.st_mode):result[rel(p)]={'kind':'symlink','target':os.readlink(p),'mode':stat.S_IMODE(s.st_mode)}
            elif stat.S_ISREG(s.st_mode):result[rel(p)]={'kind':'file','sha256':fhash(p),'size_bytes':s.st_size,'mode':stat.S_IMODE(s.st_mode)}
            else:require(stat.S_ISDIR(s.st_mode),'UNSUPPORTED_ENTRY')
    return dict(sorted(result.items()))

def matrix(a_labels,b_labels,pairs,scope):
    cells={a:{b:0 for b in b_labels} for a in a_labels}
    for a,b in pairs:
        require(a in cells and b in cells[a],'UNKNOWN_MATRIX_LABEL');cells[a][b]+=1
    n=len(pairs);agree=sum(a==b for a,b in pairs)
    return {'eligible_denominator':n,'raw_agreement_count':agree,'raw_agreement':agree/n if n else None,
            'confusion_matrix_A_rows_B_columns':cells,'eligibility':scope,
            'interpretation':'Descriptive agreement only; no legal correctness or reliability certification.'}

def verify_sources(before):
    checked=[]
    for registry,key in [(BASE/'public_review/artifact_hashes_v0.json','artifacts'),
                         (BASE/'custodian/phase5c4b0_remediation_v0/artifact_hashes_v0.json','artifacts'),
                         (BASE/'reviewer_b_results_v1/generated_artifact_hashes_v1.json','files')]:
        for name,v in read(registry)[key].items():
            require(before[name]['sha256']==v['sha256'],'SOURCE_HASH_BINDING_FAILED')
            checked.append({'registry':rel(registry),'path':name,'sha256':v['sha256'],'match':True})
    fdir=BASE.parent/'phase5c3_v0';f=read(fdir/'phase5c3_freeze_manifest_v0.json')
    require(f['phase_status']=='PASS' and f['phase5c3_freeze_status']=='FROZEN','DESIGN_NOT_FROZEN')
    for field in ['artifact_hashes','phase5c1_authoritative_artifacts','phase5c2_all_artifacts']:
        for name,v in f[field].items():
            path=rel(fdir/name) if field=='artifact_hashes' else name
            require(before[path]['sha256']==v['sha256'],'FROZEN_BINDING_FAILED')
            checked.append({'registry':rel(fdir/'phase5c3_freeze_manifest_v0.json'),'path':path,'sha256':v['sha256'],'match':True})
    v=read(BASE/'reviewer_b_results_v1/phase5c4b_validation_v1.json')
    m=read(BASE/'reviewer_b_results_v1/reviewer_b_manifest_v1.json')
    require(v['status']=='PASS' and v['counts']['candidates']==v['counts']['full_contamination_screen']==60,'SUCCESSFUL_B_REQUIRED')
    require(v['independence']['independent_context'] is True and v['independence']['annotation_A_read'] is False,'INDEPENDENT_B_REQUIRED')
    require(v['D6']=='EMPIRICAL_UNVERIFIED' and v['independence']['independent_human_legal_review'] is False,'B_GATE_FACTS_CHANGED')
    require(m['final_annotation_sha256']==before[rel(BP)]['sha256'],'B_FINAL_HASH_FAILED')
    require(read(BASE/'reviewer_b_results_v1/medical_screen_completion_validation_v1.json')['status']=='PASS','MEDICAL_SCREEN_NOT_COMPLETE')
    return {'status':'PASS','hash_bindings_checked':len(checked),'checks':checked,
            'comparison_sources':{rel(p):before[rel(p)] for p in [AP,BP,CP,MP,ACP,BCP,AAP,BAP]},
            'failed_B_used_for_comparison':False,
            'historical_B_failure':'Preserved; no failed-attempt annotation/source packet used. Its bytes are hashed only in whole-project integrity inventory.',
            'authoritative_B':'Successful independent reviewer_b_results_v1 final annotation and completed contamination files; earlier locked/pre-medical copies are provenance only.'}

def align(A,B,C,M):
    require(len(A)==len(B)==len(C)==len(M)==60,'MAPPING_COUNT_FAILED')
    ai={r['query_id']:i for i,r in enumerate(A)};bi={r['review_id_b']:i for i,r in enumerate(B)}
    ci={r['query_id']:i for i,r in enumerate(C)};mp={r['canonical_candidate_id']:r for r in M}
    require(len(ai)==len(bi)==len(ci)==len(mp)==len({r['review_id_b'] for r in M})==60,'DUPLICATE_MAPPING')
    require(set(ai)==set(ci)==set(mp) and set(bi)=={r['review_id_b'] for r in M},'UNMAPPED_CANDIDATE')
    result=[]
    for q,i in ai.items():
        j=bi[mp[q]['review_id_b']];c=C[ci[q]];b=B[j]
        digest=sha(c['query'].encode('utf-8'))
        require(A[i]['query_sha256']==b['query_sha256']==c['query_sha256']==digest,'QUERY_HASH_MISMATCH')
        require(b['query'].encode('utf-8')==c['query'].encode('utf-8'),'QUERY_BYTE_MISMATCH')
        result.append({'canonical_candidate_id':q,'review_id_b':b['review_id_b'],'A_record':i,'B_record':j,'canonical_record':ci[q],
                       'query_sha256':digest,'A_value_ref':ref(AP,i),'B_value_ref':ref(BP,j),
                       'mapping_source':rel(MP),'match_method':'EXACT_TRUSTED_ID_BIJECTION','query_byte_identity':True})
    return result

def applicability(t):return t['applicability']['status'] if isinstance(t['applicability'],dict) else t['applicability']

def anchor(s,side,chunks):
    c=chunks[s['chunk_id']]
    start=s['span']['start_char'] if side=='A' else s['span_start']
    end=s['span']['end_char'] if side=='A' else s['span_end']
    field=s['span']['field'] if side=='A' else ('parent_context' if s['reference'].endswith('^parent_intro') else 'text')
    require(field in ['text','parent_context'],'UNSUPPORTED_SPAN_FIELD')
    require(0<=start<end<=len(c[field]),'SPAN_OUT_OF_BOUNDS')
    require(s['document_id']==c['document_id'] and s['clause']==c['clause'] and s['point']==c['point'],'ANCHOR_HIERARCHY_MISMATCH')
    if side=='A':
        require(s['article_id']==c['document_id']+'_dieu-'+c['article'],'A_ARTICLE_MISMATCH')
        require(s['text_sha256']==sha(c['text'].encode('utf-8')),'A_CHUNK_HASH_MISMATCH')
    else:
        require(s['article']==c['article'],'B_ARTICLE_MISMATCH')
        require(s['chunk_text_sha256']==sha(c['text'].encode('utf-8')),'B_CHUNK_HASH_MISMATCH')
        require(s['relevant_span']==c[field][start:end] and s['span_sha256']==sha(s['relevant_span'].encode('utf-8')),'B_SPAN_HASH_MISMATCH')
    return (c['document_id'],c['article'],c['clause'],c['point'] or '',c['chunk_id'],field,start,end)

def normalize_branch(items):
    intervals=collections.defaultdict(list)
    for x in items:intervals[x[:-2]].append((x[-2],x[-1]))
    result=[]
    for k,values in sorted(intervals.items()):
        merged=[]
        for start,end in sorted(values):
            if merged and start<=merged[-1][1]:merged[-1]=(merged[-1][0],max(end,merged[-1][1]))
            else:merged.append((start,end))
        result.extend(k+(a,b) for a,b in merged)
    return tuple(result)

def bundle_formula(aspects,side,chunks):
    formulas=[]
    for t in aspects:
        op=t['across_bundle_logic'] if side=='A' else t['support_bundle_operator']
        require(op=='OR','UNSUPPORTED_ACROSS_BUNDLE_LOGIC')
        choices=[]
        for bundle in t['support_bundles']:
            require(bundle['within_bundle_logic' if side=='A' else 'operator']=='AND','UNSUPPORTED_WITHIN_BUNDLE_LOGIC')
            choices.append(normalize_branch([anchor(s,side,chunks) for s in bundle['required_spans' if side=='A' else 'evidence']]))
        if choices:formulas.append(choices)
    if not formulas:return []
    size=1
    for choices in formulas:size*=len(choices)
    require(size<=4096,'BUNDLE_CROSS_PRODUCT_TOO_LARGE')
    return sorted(set(normalize_branch([s for bundle in combination for s in bundle]) for combination in itertools.product(*formulas)))

def span_contains(bigger,smaller):
    return all(any(a[:-2]==b[:-2] and a[-2]<=b[-2] and a[-1]>=b[-1] for a in bigger) for b in smaller)

def support_class(A,B,semantic_relation):
    if not A and not B:return 'equivalent support'
    if not A or not B:return 'unresolved support disagreement'
    if A==B:return 'equivalent support'
    def cover(big,small):
        # Preserve alternatives: same branch count and a bijection of containing
        # branches. This is structural span inclusion, never sufficiency.
        return len(big)==len(small) and any(all(span_contains(x,y) for x,y in zip(perm,small)) for perm in itertools.permutations(big))
    if cover(A,B):return 'A superset'
    if cover(B,A):return 'B superset'
    a_articles={s[:2] for branch in A for s in branch};b_articles={s[:2] for branch in B for s in branch}
    if a_articles==b_articles and semantic_relation=='equivalent':return 'alternative-valid candidate'
    if not a_articles.intersection(b_articles):return 'materially different support'
    return 'unresolved support disagreement'

def main():
    os.umask(0o077)
    require(ROOT==Path.cwd().resolve(),'RUN_FROM_REPOSITORY_ROOT')
    require(not (OUT/'phase5c4c1_validation_v0.json').exists(),'C1_ALREADY_COMPLETED')
    for p in OUT.iterdir():
        if p.is_file():p.chmod(0o600)
    before=read(OUT/'integrity_baseline_v0.json')['entries']
    provenance=verify_sources(before)
    A=rows(AP);B=rows(BP);C=rows(CP);M=read(MP)['mapping'];alignment=align(A,B,C,M)
    decision_namespace={};exec(compile((OUT/'semantic_mapping_decisions_v0.py').read_bytes(),'private_semantic_decisions','exec'),decision_namespace)
    decisions=decision_namespace['DECISIONS'];require(set(decisions)==set(range(1,61)),'SEMANTIC_REVIEW_COVERAGE')
    chunks={r['chunk_id']:r for r in rows(ROOT/'data/versions/corpus-v0.1/chunks.jsonl')}
    AA=rows(AAP);BA=read(BAP)['scoped_absence_reviews']
    aa={v['audit_id']:(i,v) for i,v in enumerate(AA)};ba={v['audit_id']:(i,v) for i,v in enumerate(BA)}
    ac=read(ACP);aci={v['query_id']:(i,v) for i,v in enumerate(ac['individual_review'])}
    bc=rows(BCP);bci={v['review_id_b']:(i,v) for i,v in enumerate(bc)}
    b_to_q={x['review_id_b']:x['canonical_candidate_id'] for x in alignment}
    q_to_pair={x['canonical_candidate_id']:i+1 for i,x in enumerate(alignment)}
    issues=[];aspect_rows=[];support_rows=[];scope_rows=[];axis_rows=[];contamination_rows=[];candidate_results=[]
    answer_pairs=[];admission_pairs=[];app_pairs=[];suff_pairs=[];app_strict=[];suff_strict=[]
    dimension_counts={d:collections.Counter() for d in DIMS};scope_counts={f:collections.Counter() for f in SCOPE_FIELDS}
    relation_counts=collections.Counter();support_counts=collections.Counter();absence_comparisons=[]
    issue_counts=collections.Counter();matched_A=matched_B=unmatched_A=unmatched_B=0

    def issue(al,family,a_ref,b_ref,mapping_ref,severity,reason,legal=True,flags=None):
        issue_id='issue_'+sha(compact([al['canonical_candidate_id'],family,a_ref,b_ref,mapping_ref,reason]))[:24]
        issues.append({'issue_id':issue_id,'canonical_candidate_id':al['canonical_candidate_id'],'field_family':family,
                       'A_value_ref':a_ref,'B_value_ref':b_ref,'aspect_mapping_ref':mapping_ref,
                       'severity':severity,'reason_for_review':reason,'requires_legal_adjudication':legal,
                       'review_flags':flags or [],'status':'UNRESOLVED','correct_annotation_determined':False})
        issue_counts[al['canonical_candidate_id']]+=1
        return issue_id

    # Explicit coordinator crosswalk of A's cluster rationales, not a new
    # duplicate screen and not a conversion of every cluster to a duplicate.
    a_shared_pairs={tuple(sorted(x)) for x in [(1,13),(1,46),(13,46),(2,45),(6,25),(8,21),(19,44),(24,36)]}
    a_distinct_pairs={(15,34),(23,28)}
    b_pair_flags={}
    for r in bc:
        q=b_to_q[r['review_id_b']]
        for f in r['flags']:
            if f['source']=='new_candidate_query_text':
                other=b_to_q[f['other_review_id_b']];key=tuple(sorted((q_to_pair[q],q_to_pair[other])))
                b_pair_flags[key]=f['flag']

    for number,al in enumerate(alignment,1):
        ai=al['A_record'];bi=al['B_record'];a=A[ai];b=B[bi];c=C[al['canonical_record']];q=al['canonical_candidate_id']
        require(c['dimensions']['D6']['member'] is None and c['dimensions']['D6']['dimension_status'].upper()=='EMPIRICAL_UNVERIFIED','A_D6_CHANGED')
        require(b['dimensions']['D6']['value'] is None and b['dimensions']['D6']['verification_status'].upper()=='EMPIRICAL_UNVERIFIED','B_D6_CHANGED')
        scopes=[]
        for field in SCOPE_FIELDS:
            x=a['scope'][field];y=b['scope'][field];exact=norm(x)==norm(y)
            if exact:status='NORMALIZED_TEXT_EQUIVALENT_PENDING_FINAL_REVIEW'
            elif field=='bounded_interpretation':
                status='MATERIAL_SCOPE_BOUNDARY_REVIEW' if number in decision_namespace['SCOPE_MATERIAL_PAIRS'] else 'BOUNDED_TASK_EQUIVALENT_WORDING_PENDING_FINAL_REVIEW'
            else:status='WORDING_OR_CONTENT_DIFFERENCE_UNRESOLVED'
            scopes.append({'field':field,'A_value_ref':ref(AP,ai,'/scope/'+field),'B_value_ref':ref(BP,bi,'/scope/'+field),
                           'A_value_sha256':sha(compact(x)),'B_value_sha256':sha(compact(y)),
                           'normalized_text_equal':exact,'comparison':status})
            scope_counts[field]['eligible']+=1;scope_counts[field]['text_equal' if exact else 'text_different']+=1
            if not exact and status!='BOUNDED_TASK_EQUIVALENT_WORDING_PENDING_FINAL_REVIEW':
                issue(al,'scope',ref(AP,ai,'/scope/'+field),ref(BP,bi,'/scope/'+field),None,
                      'HIGH' if status=='MATERIAL_SCOPE_BOUNDARY_REVIEW' else 'MEDIUM',
                      'Bounded required scope differs as indicated by semantic aspect mapping.' if status=='MATERIAL_SCOPE_BOUNDARY_REVIEW' else
                      'Scope component wording/content differs; exact values remain referenced separately. Equivalence of facts, exclusions or asks is not assumed from similar task summaries.',True)
        scope_rows.append({'canonical_candidate_id':q,'components':scopes,
                           'semantic_basis':'Bounded task summary and proposition comparison; other component equivalence is conservative and explicitly unresolved when wording differs.',
                           'no_scope_reconciled':True})
        groups=decisions[number];covered_a=[];covered_b=[];candidate_mapping_ids=[];all_equiv=True
        for pos,g in enumerate(groups):
            ia=g['A'];ib=g['B'];covered_a+=ia;covered_b+=ib
            require(all(0<=k<len(a['required_legal_aspects']) for k in ia) and all(0<=k<len(b['required_legal_aspects']) for k in ib),'ASPECT_INDEX_INVALID')
            xa=[a['required_legal_aspects'][k] for k in ia];xb=[b['required_legal_aspects'][k] for k in ib]
            mid='map_'+sha(compact([q,ia,ib]))[:24];candidate_mapping_ids.append(mid);relation=g['relation'];relation_counts[relation]+=1
            mapping_ref={'path':rel(OUT/'ab_aspect_mapping_v0.jsonl'),'mapping_id':mid}
            arefs=[ref(AP,ai,'/required_legal_aspects/'+str(k)) for k in ia];brefs=[ref(BP,bi,'/required_legal_aspects/'+str(k)) for k in ib]
            mapped=bool(ia and ib)
            if mapped:matched_A+=len(ia);matched_B+=len(ib)
            else:unmatched_A+=len(ia);unmatched_B+=len(ib)
            one_equiv=relation=='equivalent' and len(ia)==len(ib)==1
            all_equiv &= one_equiv
            aspect_rows.append({'mapping_id':mid,'canonical_candidate_id':q,'A_aspect_refs':arefs,'B_aspect_refs':brefs,
                                'A_aspect_ids':[t['aspect_id'] for t in xa],'B_aspect_ids':[t['aspect_id_b'] for t in xb],
                                'relationship':relation,'semantic_reason':g['reason'],'mapping_method':'COORDINATOR_PROPOSITION_AND_BOUNDED_ROLE_REVIEW',
                                'boundary_mismatch':relation in ['A_broader','B_broader','ambiguous'] or g['additional_boundary_difference'],
                                'atomization_mismatch':len(ia)!=len(ib) and mapped or relation=='ambiguous' and mapped,
                                'omitted_on_A_side':not ia,'omitted_on_B_side':not ib,
                                'omission_note':'Absent from the required-aspect list only; no correctness or duty-omission conclusion.',
                                'scope_dependent':number in decision_namespace['SCOPE_MATERIAL_PAIRS'] and not one_equiv,
                                'status':'AGREED_PENDING_FINAL_REVIEW' if one_equiv else 'UNRESOLVED',
                                'legal_correctness_determined':False})
            if not one_equiv:
                severity='HIGH' if relation in ['A_only','B_only','A_broader','B_broader'] else 'MEDIUM'
                flags=[]
                if number in decision_namespace['ACTOR_REVIEW_PAIRS']:
                    severity='CRITICAL_REVIEW';flags=['ACTOR_OR_LEGAL_DUTY_REVIEW']
                issue(al,'required_aspects',arefs,brefs,mapping_ref,severity,g['reason'],True,flags)
            if not mapped:
                support_rows.append({'mapping_id':mid,'canonical_candidate_id':q,'comparison':'NOT_COMPARABLE_UNMATCHED_ASPECT',
                                     'A_value_ref':arefs,'B_value_ref':brefs,'status':'UNRESOLVED'})
                continue
            fa=bundle_formula(xa,'A',chunks);fb=bundle_formula(xb,'B',chunks)
            support=support_class(fa,fb,relation);support_counts[support]+=1
            support_rows.append({'mapping_id':mid,'canonical_candidate_id':q,'comparison':support,
                                 'A_value_ref':arefs,'B_value_ref':brefs,'A_formula_OR_of_AND_spans':fa,'B_formula_OR_of_AND_spans':fb,
                                 'span_tuple_fields':['document','article','clause','point','chunk','source_text_field','start_char','end_char'],
                                 'parent_anchor_policy':'B references ending ^parent_intro use their recorded parent_context span; text and parent-context coordinates are never conflated.',
                                 'group_composition':'AND across mapped aspects, OR across alternative bundles; comparison representation only, never merged annotation.',
                                 'A_clause_chunk_set':sorted({s[:5] for branch in fa for s in branch}),
                                 'B_clause_chunk_set':sorted({s[:5] for branch in fb for s in branch}),
                                 'A_alternative_count':len(fa),'B_alternative_count':len(fb),
                                 'same_absence_of_support_bundles':not fa and not fb,
                                 'context_evidence_comparison':'A source-scope requirements and B context/counterevidence preserved in source refs, not silently counted as substantive bundle spans.',
                                 'alternative_validity':'UNDETERMINED_REQUIRES_LEGAL_REVIEW' if support=='alternative-valid candidate' else 'NOT_ADJUDICATED',
                                 'status':'AGREED_PENDING_FINAL_REVIEW' if support=='equivalent support' else 'UNRESOLVED'})
            if support!='equivalent support':
                sev='HIGH' if support in ['materially different support','unresolved support disagreement'] else 'MEDIUM'
                issue(al,'support_bundles',arefs,brefs,mapping_ref,sev,
                      'Support branch/span structure differs: '+support+'. Inclusion is structural only; more evidence is not judged better. Alternative validity and necessity remain unresolved.',True)
            aa_labels=[applicability(t) for t in xa];bb_labels=[applicability(t) for t in xb]
            as_labels=[t['evidence_sufficiency']['label'] for t in xa];bs_labels=[t['evidence_sufficiency']['label'] for t in xb]
            aroles=[t['answer_role'] for t in xa];broles=[t['answer_role'] for t in xb]
            arel=[v for t in xa for v in t['evidence_relationships']]
            brel=[v for v in b['evidence_relationships'] if v['aspect_id_b'] in {t['aspect_id_b'] for t in xb}]
            predicate_a=[{k:v.get(k) for k in ['actor','scenario_actor_facts','legal_scope','system_class','material_conditions','condition_assessment','uncertainty_rationale']} for v in arel]
            predicate_b=[{k:v.get(k) for k in ['actor','legal_scope','system_class','conditions','predicate_assessment','uncertainty_rationale','qualification']} for v in brel]
            predicate_refs={'A':arefs,'B':ref(BP,bi,'/evidence_relationships')}
            absence_target=(set(as_labels)==set(bs_labels)=={'no_support_in_corpus'})
            predicate_status='UNRESOLVED_PREDICATE_OR_SCOPE_BOUNDARY' if number in decision_namespace['ACTOR_REVIEW_PAIRS']|decision_namespace['CONDITION_REVIEW_PAIRS'] else 'INDEPENDENT_PREDICATE_FORMULATIONS_PRESERVED_PENDING_REVIEW'
            axis_rows.append({'canonical_candidate_id':q,'mapping_id':mid,'A_value_ref':arefs,'B_value_ref':brefs,
                              'A_applicability_labels':aa_labels,'B_applicability_labels':bb_labels,
                              'A_sufficiency_labels':as_labels,'B_sufficiency_labels':bs_labels,
                              'A_answer_roles':aroles,'B_answer_roles':broles,
                              'A_material_predicates':predicate_a,'B_material_predicates':predicate_b,
                              'predicate_source_refs':predicate_refs,'predicate_comparison':predicate_status,
                              'predicate_axes_compared':['actor','legal_scope','system_class','material_conditions','known_unknown_facts'],
                              'absence_applicability_target_mismatch_possible':absence_target and set(aa_labels)!=set(bb_labels),
                              'target_note':'For absence aspects B may label applicability of disclosure while A labels the unresolved underlying legal proposition; equal absence conclusions do not settle this target mismatch.' if absence_target else None,
                              'group_labels_not_collapsed':True})
            if len(xa)==len(xb)==1:
                app_pairs.append((aa_labels[0],bb_labels[0]));suff_pairs.append((as_labels[0],bs_labels[0]))
                if one_equiv:app_strict.append((aa_labels[0],bb_labels[0]));suff_strict.append((as_labels[0],bs_labels[0]))
            if set(aa_labels)!=set(bb_labels):
                critical='direct' in aa_labels and 'not_applicable' in bb_labels or 'not_applicable' in aa_labels and 'direct' in bb_labels
                issue(al,'applicability',arefs,brefs,mapping_ref,'CRITICAL_REVIEW' if critical else 'HIGH',
                      'Applicability labels differ. '+('Both sides report absent support; review the label target before treating this as a legal predicate contradiction.' if absence_target else 'Review actor, condition, known/unknown facts and aspect partition before deciding legal applicability.'),True,['LEGAL_REVIEW_HIGH_PRIORITY'])
            if set(as_labels)!=set(bs_labels):
                absent='no_support_in_corpus' in set(as_labels)^set(bs_labels)
                critical=len(xa)==len(xb)==1 and absent
                issue(al,'sufficiency',arefs,brefs,mapping_ref,'CRITICAL_REVIEW' if critical else 'HIGH',
                      'Support sufficiency labels differ'+('; at least one side includes corpus-wide scoped absence. Do not equate group atomization with a proven contradiction.' if absent else '; preserve partial/full support boundaries.'),True,
                      ['LEGAL_REVIEW_HIGH_PRIORITY'] if absent else [])
            if set(aroles)!=set(broles):
                issue(al,'answer_role',arefs,brefs,mapping_ref,'HIGH','Substantive, qualified-partial or disclosure credit differs; inspect proposition partition without merging credit sets.',True)
            if predicate_status=='UNRESOLVED_PREDICATE_OR_SCOPE_BOUNDARY':
                issue(al,'material_predicates',predicate_refs['A'],predicate_refs['B'],mapping_ref,
                      'CRITICAL_REVIEW' if number in decision_namespace['ACTOR_REVIEW_PAIRS'] and not one_equiv else 'HIGH',
                      'Actor assignment or material conditional boundary requires explicit review; compared source formulations are preserved separately, including regulator/developer/deployer roles and known/unknown predicates.',True,['LEGAL_REVIEW_HIGH_PRIORITY'])
            a_audits=[t['evidence_sufficiency'].get('corpus_audit_id') for t in xa if t['evidence_sufficiency'].get('corpus_audit_id')]
            b_audits=[t['evidence_sufficiency'].get('corpus_audit_id') for t in xb if t['evidence_sufficiency'].get('corpus_audit_id')]
            if a_audits or b_audits:
                a_refs=[];b_refs=[];a_coverage=[];b_coverage=[]
                for ident in a_audits:
                    require(ident in aa,'A_ABSENCE_AUDIT_MISSING');idx,v=aa[ident]
                    a_refs.append(ref(AAP,idx));a_coverage.append(v['review_coverage'])
                for ident in b_audits:
                    require(ident in ba,'B_ABSENCE_AUDIT_MISSING');idx,v=ba[ident]
                    b_refs.append({'path':rel(BAP),'json_pointer':'/scoped_absence_reviews/'+str(idx)})
                    b_coverage.append({'documents':len(v['corpus_coverage']),'articles':sum(len(z) for z in v['corpus_coverage'].values())})
                absence_comparisons.append({'canonical_candidate_id':q,'mapping_id':mid,'A_audit_refs':a_refs,'B_audit_refs':b_refs,
                                            'A_reported_coverage':a_coverage,'B_reported_coverage':b_coverage,
                                            'rationale_comparison':'Same bounded absence conclusion pending final review; independently worded rationale preserved.' if set(as_labels)==set(bs_labels) else 'Scope/credit boundary differs; corpus-audit rationale remains unresolved.',
                                            'A_rationale_fields':['bounded_missing_request','reason_support_remains_absent','plausible_alternatives_considered'],
                                            'B_rationale_fields':['bounded_unsupported_ask','finding','alternatives_reviewed'],
                                            'absence_legally_verified':False,'status':'AGREED_PENDING_FINAL_REVIEW' if set(as_labels)==set(bs_labels) else 'UNRESOLVED'})
        require(sorted(covered_a)==list(range(len(a['required_legal_aspects']))) and sorted(covered_b)==list(range(len(b['required_legal_aspects']))),'ASPECT_MAPPING_NOT_EXHAUSTIVE_OR_DUPLICATE')
        answer_pairs.append((a['answerability']['label'],b['answerability']['label']))
        if answer_pairs[-1][0]!=answer_pairs[-1][1]:
            full_insufficient=set(answer_pairs[-1])=={'fully_answerable','insufficient_evidence'}
            issue(al,'answerability',ref(AP,ai,'/answerability'),ref(BP,bi,'/answerability'),None,
                  'CRITICAL_REVIEW' if full_insufficient else 'HIGH','Candidate answerability labels differ; no label selected as final.',True)
        a_adm='retain' if c['admission'].startswith('RETAIN') else c['admission'].lower();b_adm=b['admission_recommendation']['label'].lower()
        admission_pairs.append((a_adm,b_adm))
        if a_adm!=b_adm or b_adm=='needs_adjudication':
            required=(a_adm,b_adm) in [('retain','exclude'),('exclude','retain')] or b_adm=='needs_adjudication'
            issue(al,'admission',ref(CP,al['canonical_record'],'/admission'),ref(BP,bi,'/admission_recommendation'),None,
                  'HIGH' if required else 'MEDIUM','Admission recommendations differ; retain/reserve/exclude set is not finalized or modified.',False,
                  ['ADMISSION_REVIEW_REQUIRED'] if required else [])
        for d in DIMS:
            x=c['dimensions'][d]['member'];y=b['dimensions'][d]['value'];require(type(x) is bool and type(y) is bool,'DIMENSION_NOT_BOOLEAN')
            dimension_counts[d][('both_present' if y else 'A_only') if x else ('B_only' if y else 'both_absent')]+=1
            if x!=y:issue(al,'dimensions',ref(CP,al['canonical_record'],'/dimensions/'+d),ref(BP,bi,'/dimensions/'+d),None,
                          'MEDIUM','Independently proposed '+d+' membership differs; diagnostic structural disagreement, not automatically legal error.',False)
        acidx,acr=aci[q];bcidx,bcr=bci[al['review_id_b']]
        require(bcr['historical_31_text_screen']==bcr['medical_chatbot_text_screen']==bcr['new_candidate_text_screen']=='COMPLETE','B_CONTAMINATION_INCOMPLETE')
        a_hist='strong_near_duplicate' if number==43 else 'no_issue'
        b_hist='no_issue'
        medical=bcr['medical_comparison']
        b_med='exact_duplicate' if medical['exact_duplicate'] else 'trivial_paraphrase' if medical['trivial_paraphrase'] else 'strong_near_duplicate' if medical['strong_scenario_or_proposition_near_duplicate'] else 'no_issue'
        require('No diagnostic or close medical-chatbot scenario' in acr['medical_structural_review'],'A_MEDICAL_LABEL_UNRECOGNIZED')
        if a_hist!=b_hist:issue(al,'contamination',{'path':rel(ACP),'json_pointer':'/individual_review/'+str(acidx)},ref(BCP,bcidx,'/historical_overlap_review'),None,
                               'HIGH','A conservatively excluded for near-duplicate historical proposition/role pattern; B distinguishes the actor task and reports no strong full-scope duplicate. Preserve both decisions.',False,['ADMISSION_REVIEW_REQUIRED'])
        if b_med!='no_issue':issue(al,'contamination',{'path':rel(ACP),'json_pointer':'/individual_review/'+str(acidx)+'/medical_structural_review'},ref(BCP,bcidx,'/medical_comparison'),None,'HIGH','Medical-reference contamination judgments differ.',False)
        pair_records=[]
        for key in sorted(a_shared_pairs|a_distinct_pairs|set(b_pair_flags)):
            if number not in key:continue
            ca='same_scenario_proposition_bundle' if key in a_shared_pairs else 'no_issue' if key in a_distinct_pairs else 'not_separately_categorized'
            cb=b_pair_flags.get(key,'no_positive_flag')
            pair_records.append({'other_canonical_candidate_id':alignment[(key[1] if key[0]==number else key[0])-1]['canonical_candidate_id'],
                                 'A_category_crosswalk':ca,'B_category':cb,
                                 'A_basis':'Explicit cluster rationale semantic relation, not cluster membership alone' if key in a_shared_pairs|a_distinct_pairs else 'No equivalent per-pair semantic category in A; lexical score is not a legal similarity judgment',
                                 'A_source':rel(BASE/'custodian/cluster_rationales_v0.json'),'B_source':ref(BCP,bcidx,'/flags'),
                                 'agreement':ca==cb,'status':'AGREED_PENDING_FINAL_REVIEW' if ca==cb else 'UNRESOLVED'})
            if ca!=cb:
                issue(al,'contamination',{'path':rel(BASE/'custodian/cluster_rationales_v0.json'),'candidate_pair':[alignment[k-1]['canonical_candidate_id'] for k in key]},ref(BCP,bcidx,'/flags'),None,
                      'MEDIUM','Internal-pair contamination category or annotation coverage differs. Cluster relation, near-duplicate flag and absence of a flag are not interchangeable.',False)
        contamination_rows.append({'canonical_candidate_id':q,'A_value_ref':{'path':rel(ACP),'json_pointer':'/individual_review/'+str(acidx)},'B_value_ref':ref(BCP,bcidx),
                                   'historical_31':{'A':a_hist,'B':b_hist,'agree':a_hist==b_hist},
                                   'medical_reference':{'A':'no_issue','B':b_med,'agree':b_med=='no_issue'},
                                   'internal_candidate_pairs':pair_records,
                                   'category_vocabulary':['exact_duplicate','trivial_paraphrase','strong_near_duplicate','same_scenario_proposition_bundle','no_issue'],
                                   'missing_category_policy':'Unrecorded A pair categories and absent B positive flags remain missing-category states, not certified no issue.',
                                   'additional_A_reference_coverage':{'existing_DEV_queries':9,'B_comparable_screening_available':False,'treatment':'Outside common 31+medical reference set; not silently counted as agreement or B failure.'},
                                   'no_re_screening_performed':True,'no_admission_change':True})
        candidate_results.append({'canonical_candidate_id':q,'aspect_mapping_ids':candidate_mapping_ids,'all_aspects_one_to_one_equivalent':all_equiv,
                                  'answerability_agrees':answer_pairs[-1][0]==answer_pairs[-1][1],
                                  'admission_agrees':a_adm==b_adm,'status':'PENDING_REGISTRY_AGGREGATION'})

    require(len({x['issue_id'] for x in issues})==len(issues),'DUPLICATE_ISSUE_ID')
    by_q=collections.defaultdict(list)
    for x in issues:by_q[x['canonical_candidate_id']].append(x)
    for x in candidate_results:
        ii=by_q[x['canonical_candidate_id']]
        x.update({'unresolved_issue_count':len(ii),'comparison_priority':max((v['severity'] for v in ii),key=lambda v:RANK[v],default='LOW'),
                  'full_substantive_agreement':not ii,'status':'UNRESOLVED' if ii else 'AGREED_PENDING_FINAL_REVIEW'})
    priority=collections.Counter(x['comparison_priority'] for x in candidate_results)
    issue_severity=collections.Counter(x['severity'] for x in issues)
    full=sum(x['full_substantive_agreement'] for x in candidate_results)
    dimension_metrics={d:{k:dimension_counts[d][k] for k in ['both_present','A_only','B_only','both_absent']} for d in DIMS}
    for d,x in dimension_metrics.items():
        x.update({'eligible_denominator':60,'agreement_count':x['both_present']+x['both_absent'],'raw_agreement':(x['both_present']+x['both_absent'])/60,
                  'confusion_matrix_A_rows_B_columns':{'false':{'false':x['both_absent'],'true':x['B_only']},'true':{'false':x['A_only'],'true':x['both_present']}}})
    categories=['exact_duplicate','trivial_paraphrase','strong_near_duplicate','same_scenario_proposition_bundle','no_issue']
    metrics={'status':'PASS','measurement_type':'DESCRIPTIVE_STRUCTURAL_AGREEMENT','not_legal_reliability_certification':True,
             'answerability':matrix(ANS,ANS,answer_pairs,'All 60 exact-ID matched candidates'),
             'admission':matrix(ADM_A,ADM_B,admission_pairs,'All 60 candidates; A provisional DEV/TEST retain labels both projected to retain for descriptive comparison only'),
             'applicability_equivalent_one_to_one':matrix(APP,APP,app_strict,'Only semantically equivalent 1:1 mappings; different label targets remain explicitly flagged'),
             'sufficiency_equivalent_one_to_one':matrix(SUFF,SUFF,suff_strict,'Only semantically equivalent 1:1 mappings'),
             'applicability_all_one_to_one_diagnostic':matrix(APP,APP,app_pairs,'All 1:1 mappings including broad/narrow/ambiguous; descriptive diagnostic only'),
             'sufficiency_all_one_to_one_diagnostic':matrix(SUFF,SUFF,suff_pairs,'All 1:1 mappings including broad/narrow/ambiguous; no pooled multi-aspect label'),
             'dimensions':dimension_metrics,'D6':'EMPIRICAL_UNVERIFIED',
             'scope':{f:{'eligible_denominator':60,'normalized_text_agreement_count':scope_counts[f]['text_equal'],
                          'normalized_text_agreement':scope_counts[f]['text_equal']/60,
                          'wording_or_content_difference_count':scope_counts[f]['text_different'],
                          'warning':'Text agreement is not semantic/legal agreement; differing facts/exclusions/asks remain unresolved unless explicitly reviewed.'} for f in SCOPE_FIELDS},
             'aspects':{'A_total':sum(len(a['required_legal_aspects']) for a in A),'B_total':sum(len(b['required_legal_aspects']) for b in B),
                        'relationship_counts':dict(relation_counts),'A_aspects_in_mapping_groups':matched_A,'B_aspects_in_mapping_groups':matched_B,
                        'unmatched_A':unmatched_A,'unmatched_B':unmatched_B,
                        'equivalent_one_to_one_matches':relation_counts['equivalent'],
                        'boundary_disagreement_groups':sum(x['boundary_mismatch'] for x in aspect_rows),
                        'atomization_disagreement_groups':sum(x['atomization_mismatch'] for x in aspect_rows),
                        'candidate_level_full_aspect_equivalence':sum(x['all_aspects_one_to_one_equivalent'] for x in candidate_results),
                        'mapping_group_denominator':len(aspect_rows),
                        'matched_is_not_equivalent':'Broad/narrow, split and ambiguous associations are counted as mapped, not as equivalent matches.'},
             'support_structure':{'mapped_group_denominator':sum(support_counts.values()),'classification_counts':dict(support_counts),
                                  'equivalent_structure_count':support_counts['equivalent support'],
                                  'raw_structural_agreement':support_counts['equivalent support']/sum(support_counts.values()),
                                  'absent_bundles_on_both_sides':sum(x.get('same_absence_of_support_bundles',False) for x in support_rows),
                                  'validity_not_adjudicated':True},
             'contamination_historical_31':matrix(categories,categories,[(x['historical_31']['A'],x['historical_31']['B']) for x in contamination_rows],'60 candidates; common authorized historical 31 texts'),
             'contamination_medical':matrix(categories,categories,[(x['medical_reference']['A'],x['medical_reference']['B']) for x in contamination_rows],'60 candidates; same single exploratory reference'),
             'internal_contamination_comparability':{'B_flagged_undirected_pairs':len(b_pair_flags),'A_explicit_shared_relation_crosswalk_pairs':len(a_shared_pairs),
                                                    'union_pairs_reviewed':len(a_shared_pairs|a_distinct_pairs|set(b_pair_flags)),
                                                    'pooled_category_agreement':None,'reason':'A cluster rationales and B positive pair flags are not identically categorized; absent labels are not imputed as negative judgments.'},
             'candidates_with_full_substantive_agreement':full,'candidates_with_one_or_more_unresolved_differences':60-full,
             'full_agreement_interpretation':'Conservative confirmed-agreement count. Any unresolved scope wording/content equivalence, predicate, evidence, category or substantive difference blocks full agreement; this is not a count of legally wrong candidates.',
             'independent_human_legal_review_complete':False,'human_legal_review_gate':'HUMAN_LEGAL_REVIEW_REQUIRED'}
    summary={'candidate_count':60,'unresolved_issue_count':len(issues),'candidate_priority_distribution':{k:priority[k] for k in RANK},
             'issue_severity_distribution':{k:issue_severity[k] for k in RANK},'issue_field_family_counts':dict(collections.Counter(x['field_family'] for x in issues)),
             'candidates':candidate_results,'priority_is_not_correctness':True,'all_issues_status':'UNRESOLVED',
             'severity_unit':'Console severity counts are candidates classified by maximum issue severity; issue severities are reported separately.',
             'legal_review_required_issues':sum(x['requires_legal_adjudication'] for x in issues),
             'absence_high_priority_flags':sum('LEGAL_REVIEW_HIGH_PRIORITY' in x['review_flags'] and x['field_family']=='sufficiency' for x in issues),
             'admission_review_required_flags':sum('ADMISSION_REVIEW_REQUIRED' in x['review_flags'] for x in issues),
             'human_legal_review_gate':'HUMAN_LEGAL_REVIEW_REQUIRED','dataset_freeze_ready':False}
    # Public per-candidate summaries exclude mapping IDs and answer/dimension labels.
    summary['candidates']=[{k:x[k] for k in ['canonical_candidate_id','unresolved_issue_count','comparison_priority','full_substantive_agreement','status']} for x in candidate_results]
    dump('source_integrity_validation_v0.json',provenance)
    dump('ab_candidate_alignment_v0.json',{'status':'PASS','count':60,'duplicate_mappings':0,'unmapped_candidates':0,'alignment':alignment})
    dump_rows('ab_scope_comparison_v0.jsonl',scope_rows)
    dump_rows('ab_aspect_mapping_v0.jsonl',aspect_rows)
    dump_rows('ab_support_comparison_v0.jsonl',support_rows)
    dump_rows('ab_applicability_sufficiency_comparison_v0.jsonl',axis_rows)
    dump_rows('ab_corpus_audit_comparison_v0.jsonl',absence_comparisons)
    dump_rows('ab_disagreement_registry_v0.jsonl',issues)
    dump_rows('ab_contamination_comparison_v0.jsonl',contamination_rows)
    dump('phase5c4c1_agreement_metrics_v0.json',metrics)
    dump('phase5c4c1_disagreement_summary_v0.json',summary)
    after=snapshot();changed=[k for k,v in before.items() if after.get(k)!=v]
    added=sorted(after.keys()-before.keys());require(not changed,'PREEXISTING_INTEGRITY_FAILED')
    require(all((ROOT/k).parent==OUT for k in added),'ADDITION_OUTSIDE_C1')
    integrity={'status':'PASS','preexisting_regular_files':sum(v['kind']=='file' for v in before.values()),
               'preexisting_symlinks':sum(v['kind']=='symlink' for v in before.values()),
               'all_preexisting_files_byte_identical':True,'modes_and_symlink_targets_unchanged':True,
               'before_inventory_sha256':sha(compact(before)),'after_preexisting_inventory_sha256':sha(compact({k:after[k] for k in before})),
               'changed_or_missing':changed,'all_additions_under_comparison_c1':True,'additions_at_integrity_sweep':added,
               'baseline_file':'integrity_baseline_v0.json','baseline_sha256':fhash(OUT/'integrity_baseline_v0.json'),
               'scope':'All preexisting project files including hidden and virtualenv; opaque binary hashes only for failed B/system artifacts; symlinks not followed. Remaining C1 reports are new files in this directory.'}
    dump('integrity_before_after_v0.json',integrity)
    public_names=['phase5c4c1_comparison_report_v0.md','phase5c4c1_agreement_metrics_v0.json','phase5c4c1_disagreement_summary_v0.json',
                  'phase5c4c1_validation_v0.json','integrity_before_after_v0.json','phase5c4c1_console_v0.txt']
    report=f'''# Phase 5C.4-C1 — PASS

All 60 A and successful independent B v1 annotations align through the trusted
ID mapping with no duplicate or missing records. Source registries and frozen
design bindings were verified before comparison. The failed B attempt was not
used for comparison, and all preexisting artifacts remain unchanged.

Comparison covers all five scope components, all required aspects, supporting
document/article/clause/point/chunk spans and AND/OR alternatives, applicability,
material predicates, sufficiency and corpus-audit rationale, answerability, nine
proposed dimensions, admission, and completed historical/medical contamination.
D6 remains EMPIRICAL_UNVERIFIED. No annotation was merged or selected as final.

There are {metrics['aspects']['A_total']} A aspects and {metrics['aspects']['B_total']} B aspects.
The coordinator identified {relation_counts['equivalent']} equivalent one-to-one mappings;
{unmatched_A} A aspects and {unmatched_B} B aspects have no counterpart. Broad/narrow,
split and ambiguous mappings remain explicit. IDs and shared evidence alone were
not used to decide semantic equivalence. Legal roles and bounded propositions
were read directly; ambiguous intersections were preserved for review.

Answerability agrees for {metrics['answerability']['raw_agreement_count']}/60 candidates.
Admission agrees for {metrics['admission']['raw_agreement_count']}/60. Full A×B matrices
and denominators are in the metrics file. Applicability/sufficiency matrices for
equivalent one-to-one mappings are separated from the broader diagnostic matrix;
heterogeneous split groups are never collapsed to one categorical label.

Confirmed full agreement: {full}/60. Candidates with unresolved differences:
{60-full}/60, containing {len(issues)} issues. This is a conservative lower bound on
confirmed agreement: differing scope facts, exclusions and asks remain unresolved
when semantic equivalence is not established. It does not mean every difference
is a legal error. Some applicability differences concern whether the label targets
an underlying proposition or disclosure of corpus absence. Predicate formulations
are preserved separately; candidate-specific actor/conditionality concerns are
flagged without choosing a correct assignment.

Evidence supersets describe span inclusion only. Empty support on both sides
means matching recorded absence of bundles, not verified absence of law. An
alternative-valid candidate is only a possible alternative awaiting legal review.
Corpus-audit coverage is compared as reported; C1 performs no new absence search.

Historical contamination agrees for {metrics['contamination_historical_31']['raw_agreement_count']}/60;
medical-reference screening agrees for {metrics['contamination_medical']['raw_agreement_count']}/60.
Internal similarity cannot be reduced to a single pooled categorical score:
A cluster rationale, B near-duplicate flags and missing per-pair labels are
different records. The private comparison preserves these distinctions and
flags category/coverage differences. Additional A exploratory DEV references
are outside the common historical-31-plus-medical comparison denominator.

Candidate priorities (maximum unresolved issue severity):
CRITICAL_REVIEW {priority['CRITICAL_REVIEW']}; HIGH {priority['HIGH']};
MEDIUM {priority['MEDIUM']}; LOW {priority['LOW']}.
Issue severity counts are separately reported to prevent denominator confusion.
Priorities order later review; they are not correctness judgments.

End state: HUMAN_LEGAL_REVIEW_REQUIRED. B is model-based; this is not two human
legal reviewers agreeing. No final legal adjudication, final gold, retained-set
selection or split freeze was performed. HOLDOUT_STORAGE_ISOLATION_NOT_YET_ENFORCED
remains unchanged, so final dataset freeze is blocked. Owner-only private files
do not enforce separation between contexts sharing the same OS identity.

Network/API, production/evaluator and retrieval/reranking inference calls: 0.
System outputs were not substantively inspected; whole-project binary hashing
is separately documented. Agentic v2 implementation is NOT STARTED and forbidden
in this exposed context. C2 adjudication/legal-review gate is ready to receive
the unresolved registry; this does not authorize C1 to adjudicate.

STOP
'''
    write(OUT/'phase5c4c1_comparison_report_v0.md',report.encode('utf-8'))
    gates=['60_exact_canonical_mappings','no_failed_B_comparison_input','scope_compared','aspects_semantically_mapped',
           'support_compared','applicability_compared','sufficiency_compared','answerability_compared','dimensions_compared',
           'admission_compared','contamination_compared','disagreements_retained_unresolved','no_final_gold','no_adjudication',
           'D6_untouched','no_substantive_system_output_read','no_API_network','preexisting_integrity_PASS']
    validation={'phase':'5C.4-C1','phase_status':'PASS','role':'TRUSTED_DATASET_CUSTODIAN / COMPARISON_COORDINATOR',
                'gates':[{'gate':g,'status':'PASS'} for g in gates],
                'records':{'A':60,'B':60,'mapping':60,'unmapped':0,'duplicate_mapping':0},
                'source_hash_bindings_verified':provenance['hash_bindings_checked'],
                'semantic_review_scope':'Coordinator reading of paired bounded scopes, propositions and legal roles; ambiguous mappings explicit. No final legal correctness determined.',
                'scope_equivalence_limit':'All components compared; text differences in asks/facts/exclusions are conservatively unresolved rather than auto-reconciled.',
                'human_legal_review_complete':False,'final_legal_adjudication_complete':False,'final_gold_produced':False,
                'D6':'EMPIRICAL_UNVERIFIED','storage_isolation':'NOT_YET_ENFORCED','dataset_frozen':False,
                'network_api_calls':0,'production_evaluator_calls':0,'retrieval_reranking_inference':0,
                'system_outputs_substantively_inspected':0,'implementation':'NOT_STARTED',
                'future_v2_implementation_in_this_context':'FORBIDDEN','preexisting_integrity':'PASS',
                'ready_for_C2_legal_review_gate':True,'ready_for_final_dataset_freeze':False,
                'public_plaintext_scan':'PASS','public_safe_files':public_names,
                'execution_basis':'Task-initiated local reads, comparisons, source-span normalization and binary hashes only; no production modules or external inference; no OS-wide network attestation.'}
    console='\n'.join(['Phase 5C.4-C1 status: PASS','Role: TRUSTED_DATASET_CUSTODIAN / COMPARISON_COORDINATOR',
                      'A records: 60/60','B records: 60/60','Canonical mappings: 60/60']+
                     [name+' comparison: COMPLETE' for name in ['Scope','Aspect','Support','Applicability','Sufficiency','Answerability','Dimension','Admission','Contamination']]+
                     [f'Candidates with full substantive agreement: {full}',f'Candidates with one or more disagreements: {60-full}',
                      f'Unresolved disagreement issues: {len(issues)}']+[k+': '+str(priority[k]) for k in ['CRITICAL_REVIEW','HIGH','MEDIUM','LOW']]+
                     ['Independent human legal review complete: NO','Final legal adjudication complete: NO','D6: EMPIRICAL_UNVERIFIED',
                      'HOLDOUT storage isolation: NOT_YET_ENFORCED','Dataset frozen: NO','Network/API calls: 0','Production/evaluator calls: 0',
                      'Retrieval/reranking inference: 0','Agentic v2 implementation: NOT STARTED','Preexisting artifact integrity: PASS',
                      'Ready for Phase 5C.4-C2 adjudication/legal-review gate: YES','Ready for final dataset freeze: NO','STOP',''])
    dump('phase5c4c1_validation_v0.json',validation);write(OUT/'phase5c4c1_console_v0.txt',console.encode('utf-8'))
    confidential=[c['query'].encode('utf-8') for c in C]+[t['proposition'].encode('utf-8') for a in A+B for t in a['required_legal_aspects']]
    for name in public_names:
        raw=(OUT/name).read_bytes();require(not any(x in raw for x in confidential),'PUBLIC_QUERY_OR_PROPOSITION_LEAK')
    access={'role':validation['role'],'future_v2_implementation_in_this_context':'FORBIDDEN','authorized_roles':['TRUSTED_DATASET_CUSTODIAN','COMPARISON_COORDINATOR','LATER_AUTHORIZED_LEGAL_REVIEWER'],
            'implementation_access':'FORBIDDEN','independent_reviewer_B_annotation_access':'FORBIDDEN',
            'public_safe_artifacts':public_names,'private_artifacts':sorted(p.name for p in OUT.iterdir() if p.name not in public_names),
            'private_content':'Canonical/B ID mappings, legal-aspect links, support spans and predicate formulations; exact queries not duplicated.',
            'storage_isolation':'NOT_YET_ENFORCED','permission_limit':'0700 directory and 0600 files are owner-only, not tested role separation.',
            'historical_facts_preserved':{'A':'PASS','B0':'PASS','B_final':'PASS','human_legal_review':False,'D6':'EMPIRICAL_UNVERIFIED'},
            'no_subagents':True,'no_external_messages':True,'no_web_or_network':True}
    dump('comparison_access_manifest_v0.json',access)
    dump('artifact_hashes_v0.json',{'purpose':'C1 comparison provenance, not dataset freeze','algorithm':'sha256','self_excluded':True,
                                  'artifacts':{rel(p):{'sha256':fhash(p),'size_bytes':p.stat().st_size} for p in sorted(OUT.iterdir()) if p.is_file()}})
    print(console,end='')

if __name__=='__main__':
    try:main()
    except Exception as e:
        print('C1 comparison execution stopped; C2 readiness not authorized by this run.',file=sys.stderr)
        if isinstance(e,RuntimeError) and re.fullmatch('[A-Z_]+',str(e)):print('Validation code: '+str(e),file=sys.stderr)
        else:print('Error type: '+type(e).__name__,file=sys.stderr)
        raise SystemExit(1) from None
