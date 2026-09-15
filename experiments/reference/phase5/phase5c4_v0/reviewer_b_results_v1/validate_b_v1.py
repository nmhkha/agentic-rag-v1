"""Offline annotation artifact validation; not a production/evaluator run."""
import json, hashlib, collections
from pathlib import Path
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[5]
def sha(b):return hashlib.sha256(b).hexdigest()
def validate():
    rows=[json.loads(l) for l in (OUT/'annotation_B_v1.jsonl').read_text().splitlines()]
    packet=[json.loads(l) for l in (OUT.parent/'reviewer_b_packet_v1/reviewer_b_queries_v1.jsonl').read_text().splitlines()]
    corpus={c['chunk_id']:c for c in [json.loads(l) for l in (ROOT/'data/versions/corpus-v0.1/chunks.jsonl').read_text().splitlines()]}
    audits={a['audit_id']:a for a in json.loads((OUT/'scoped_corpus_reviews_v1.json').read_text())}
    errors=[]; counts=collections.Counter()
    def check(condition,code,rid=None):
        counts[code]+=1
        if not condition:errors.append({'check':code,'review_id_b':rid})
    check(len(rows)==len(packet)==60,'all_60_records')
    check([r['review_id_b'] for r in rows]==[r['review_id_b'] for r in packet],'packet_order_and_ids')
    all_ids=set()
    for row,p in zip(rows,packet):
        rid=row['review_id_b']; aspects=row['required_legal_aspects']
        check(row['query']==p['query'] and row['query_sha256']==sha(p['query'].encode()),'exact_query_identity',rid)
        check(set(row['scope'])=={'explicit_asks','bounded_interpretation','relevant_user_facts','unspecified_facts','excluded_scope'},'scope_fields',rid)
        check(bool(row['scope']['explicit_asks']) and bool(row['scope']['bounded_interpretation']),'finite_explicit_scope',rid)
        check(row['reviewer_type']=='MODEL_BASED_INDEPENDENT_ANNOTATOR' and row['independent_context'] and not row['independent_human_legal_review'],'honest_identity',rid)
        check(set(row['dimensions'])=={'D'+str(n) for n in range(1,11)},'all_dimensions',rid)
        check(row['dimensions']['D6']['verification_status']=='EMPIRICAL_UNVERIFIED' and row['dimensions']['D6']['value'] is None,'D6_unmeasured',rid)
        for d,v in row['dimensions'].items():
            if d!='D6':check(isinstance(v['value'],bool) and bool(v['rationale']),'dimension_rationale',rid)
        check(row['admission_recommendation']['label'] in ['RETAIN','RESERVE','EXCLUDE','NEEDS_ADJUDICATION'],'admission_enum',rid)
        aidset={a['aspect_id_b'] for a in aspects}
        check(len(aidset)==len(aspects) and not (aidset & all_ids),'unique_B_aspect_ids',rid)
        all_ids.update(aidset)
        sufficient=0; supported=0
        for a in aspects:
            aid=a['aspect_id_b'];label=a['evidence_sufficiency']['label'];bundles=a['support_bundles']
            expected={'sufficient_support':'substantive_supported','partial_support':'qualified_partial','no_support_in_corpus':'unresolved_disclosure'}
            check(label in expected and expected.get(label)==a['answer_role'],'support_role_consistency',rid)
            check(a['origin'] in ['query_explicit','scope_necessary'] and a['parent_aspect_id'] in [None,*aidset],'aspect_origin_parent',rid)
            check(bool(a['proposition']) and bool(a['materiality']),'aspect_materiality',rid)
            sufficient+=label=='sufficient_support';supported+=bool(bundles)
            check(bool(bundles)==(label!='no_support_in_corpus'),'supported_bundle_presence',rid)
            check(a['support_bundle_operator']=='OR' and all(b['operator']=='AND' and b['evidence'] for b in bundles),'OR_AND_semantics',rid)
            if label!='sufficient_support':
                audit=audits.get(a['evidence_sufficiency']['corpus_audit_id'],{})
                check(bool(audit) and sum(len(x) for x in audit.get('corpus_coverage',{}).values())==86 and bool(audit.get('finding')),'documented_scoped_corpus_review',rid)
                check(bool(a['evidence_sufficiency']['unsupported_scope']),'explicit_unresolved_scope',rid)
            expected_modes={'substantive_supported':{'P+'},'qualified_partial':{'Q','U'},'unresolved_disclosure':{'U'}}[a['answer_role']]
            obs=[o for o in row['response_obligations'] if o['aspect_id_b']==aid]
            check({o['set'] for o in obs}==expected_modes and len(obs)==len(expected_modes),'P_Q_U_obligations',rid)
            for b in bundles:
                check(len({e['chunk_id'] for e in b['evidence']})==len(b['evidence']),'no_duplicate_bundle_members',rid)
            ev=a['context_evidence']+a['counterevidence']+[e for b in bundles for e in b['evidence']]
            for e in ev:
                c=corpus.get(e['chunk_id'])
                check(c is not None,'chunk_exists',rid)
                if c:
                    check(all(e[k]==c[k] for k in ['document_id','article','clause','point']),'exact_evidence_location',rid)
                    field=e.get('source_field','text')
                    check(field in ['text','parent_context'],'evidence_source_field',rid)
                    check(e['relevant_span']==c[field][e['span_start']:e['span_end']] and e['span_sha256']==sha(e['relevant_span'].encode()) and e['chunk_text_sha256']==sha(c['text'].encode()),'evidence_span_hash',rid)
                    if field=='parent_context':check(e['source_field_sha256']==sha(c[field].encode()),'parent_context_source_hash',rid)
                    check(bool(e['hierarchy_context']['clause_intro']) if c['point'] else True,'point_parent_context',rid)
            for b in bundles:
                for e in b['evidence']:
                    matches=[rel for rel in row['evidence_relationships'] if rel['aspect_id_b']==aid and rel['chunk_id']==e['chunk_id'] and rel['bundle_id_b']==b['bundle_id_b']]
                    check(len(matches)==1 and matches[0]['relevance']=='direct' and matches[0]['evidence_role']=='normative_support' and matches[0]['applicability']!='not_applicable','bundle_relationship_support',rid)
        for rel in row['evidence_relationships']:
            check(rel['aspect_id_b'] in aidset and rel['chunk_id'] in corpus,'relationship_links',rid)
            check(rel['relevance'] in ['direct','contextual','irrelevant','uncertain'] and rel['evidence_role'] in ['normative_support','supporting_context','counterevidence'] and rel['applicability'] in ['direct','conditional','not_applicable','uncertain'],'relationship_enums',rid)
            check(all(rel.get(k) for k in ['actor','legal_scope','system_class','conditions','predicate_assessment']),'applicability_predicates_present',rid)
            if rel['applicability'] in ['uncertain','conditional']:
                check(bool(rel['uncertainty_rationale']),'applicability_uncertainty_explained',rid)
        expected='fully_answerable' if sufficient==len(aspects) else 'partially_answerable' if supported else 'insufficient_evidence'
        check(row['answerability']['label']==expected,'answerability_derivation',rid)
        obs=row['response_obligations']
        check(len({o['obligation_id_b'] for o in obs})==len(obs) and all(o['aspect_id_b'] in aidset for o in obs),'disjoint_obligation_ids',rid)
    result={'status':'PASS' if not errors else 'FAIL','candidate_count':len(rows),'checks':dict(counts),'errors':errors,
            'validation_kind':'schema/evidence/provenance consistency only; no system or answer scoring; not legal adjudication',
            'annotation_sha256':sha((OUT/'annotation_B_v1.jsonl').read_bytes())}
    (OUT/'annotation_structural_validation_v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'annotation_validation':result['status'],'check_count':sum(counts.values()),'errors':errors}))
    return result
if __name__=='__main__':validate()
