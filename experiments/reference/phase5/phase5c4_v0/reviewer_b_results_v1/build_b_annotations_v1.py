"""Private, B-authored annotation serialization. No retrieval or model calls.

Legal judgments in authored_specs_v1.py are manually authored in this independent
context from the query-only packet and corpus. This program only resolves exact
hierarchical references and serializes/validates those judgments.
"""
import json, hashlib, datetime, itertools
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[5]
CORPUS = ROOT / 'data/versions/corpus-v0.1'
PACKET = OUT.parent / 'reviewer_b_packet_v1/reviewer_b_queries_v1.jsonl'
DOCS = {'L': '134-2025-QH15', 'N': '142-2026-ND-CP', 'T': '05-2026-TT-BKHCN'}
SPECS = []

def aspect(proposition, refs='', *, alternatives=None, origin='query_explicit',
           status='sufficient_support', app='direct', condition=None, unknown=None,
           context='', counter='', note=None):
    return dict(proposition=proposition, refs=refs.split(), alternatives=alternatives,
                origin=origin, status=status, app=app, condition=condition,
                unknown=unknown, context=context.split(), counter=counter.split(), note=note)

def item(number, asks, facts, missing, excluded, actor, system, aspects, *, broad=False,
         applicability=False, admission='RETAIN', quality, bounds=None, d4=None):
    assert number == len(SPECS) + 1
    SPECS.append(dict(number=number, asks=asks, facts=facts, missing=missing,
                      excluded=excluded, actor=actor, system=system, aspects=aspects,
                      broad=broad, applicability=applicability, admission=admission,
                      quality=quality, bounds=bounds or ' ; '.join(asks), d4=d4))

def sha(b): return hashlib.sha256(b).hexdigest()

def main():
    exec(compile((OUT/'authored_specs_v1.py').read_text(), 'authored_specs_v1.py', 'exec'), globals())
    records = [json.loads(l) for l in PACKET.read_text().splitlines()]
    chunks = [json.loads(l) for l in (CORPUS/'chunks.jsonl').read_text().splitlines()]
    articles = [json.loads(l) for l in (CORPUS/'articles.jsonl').read_text().splitlines()]
    by_article = {(a['document_id'],a['article']):a for a in articles}
    assert len(records)==len(SPECS)==60
    assert all(set(r)=={'review_id_b','query'} for r in records)
    stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()

    def resolve(ref):
        doc=DOCS[ref[0]]; parts=ref[1:].split('.')
        art=parts[0]; clause=parts[1] if len(parts)>1 else None
        point=parts[2] if len(parts)>2 else None
        candidates=[c for c in chunks if c['document_id']==doc and c['article']==art
                    and (clause is None or c['clause']==clause)
                    and (point is None or c['point']==point)]
        assert candidates, ref
        if clause is None:
            direct=[c for c in candidates if c['chunk_level']=='article']
            if direct: candidates=direct
        a=by_article[(doc,art)]
        ret=[]
        for c in candidates:
            cl=next((x for x in a['clauses'] if x['clause']==c['clause']),None)
            ret.append(dict(document_id=doc, document_number=c['document_number'],
                document_title=c['document_title'], article=art, article_title=a['article_title'],
                clause=c['clause'], point=c['point'], chunk_id=c['chunk_id'],
                relevant_span=c['text'], span_start=0, span_end=len(c['text']),
                span_sha256=sha(c['text'].encode()), chunk_text_sha256=sha(c['text'].encode()),
                hierarchy_context={'article_intro':a['intro_text'],
                    'clause_intro':cl['text'] if cl and c['point'] else None,
                    'source_lines':[c['source_start_line'],c['source_end_line']]},
                reference=ref))
        return ret

    def evidence(refs):
        result={}
        for ref in refs:
            for e in resolve(ref):result[e['chunk_id']]=e
        return list(result.values())

    output=[];absence=[]
    for r,s in zip(records,SPECS):
        rid=r['review_id_b']; aspects=[]; obligations=[]; relationships=[]
        for k,a in enumerate(s['aspects'],1):
            aid=f'{rid}:b_aspect_{k:02d}'
            role={'sufficient_support':'substantive_supported','partial_support':'qualified_partial',
                  'no_support_in_corpus':'unresolved_disclosure'}[a['status']]
            alternatives = a['alternatives'] or ([a['refs']] if a['refs'] else [])
            bundles=[]
            for bi,refs in enumerate(alternatives,1):
                if isinstance(refs,str):refs=refs.split()
                ev=evidence(refs)
                bundles.append({'bundle_id_b':f'{aid}:bundle_{bi}', 'operator':'AND',
                                'supported_proposition':a['proposition'],
                                'coverage':'whole_aspect' if a['status']=='sufficient_support' else 'qualified_supported_portion',
                                'evidence':ev})
            assert (role=='unresolved_disclosure') == (not bundles),aid
            predicates=[{'predicate':'actor and activity match bounded query',
                         'assessment':'met','basis':s['actor']+'; '+s['system']},
                        {'predicate':a['condition'] or 'Additional material condition',
                         'assessment':'unknown' if a['app'] in ['uncertain','conditional'] else 'met' if a['condition'] else 'not_required',
                         'basis':(a['unknown'] or a['condition']) if a['app'] in ['uncertain','conditional'] else (a['condition'] or 'No extra factual assumption required for this bounded proposition.')}]
            def relationship(e, relevance, erole, application, bundle_id=None):
                return {'aspect_id_b':aid,'chunk_id':e['chunk_id'],'bundle_id_b':bundle_id,
                    'relevance':relevance,'evidence_role':erole,'applicability':application,
                    'actor':s['actor'],'legal_scope':s['bounds'],'system_class':s['system'],
                    'conditions':a['condition'] or 'Within the expressly bounded question and corpus.',
                    'predicate_assessment':predicates if application!='not_applicable' else [
                        {'predicate':'Duty asserted for the query actor/system','assessment':'unmet',
                         'basis':a['note'] or 'The special duty has a different actor, activity, or condition.'}],
                    'uncertainty_rationale':(a['unknown'] or a['condition']) if application in ['uncertain','conditional'] else None,
                    'qualification':a['note']}
            for b in bundles:
                for e in b['evidence']:relationships.append(relationship(e,'direct','normative_support',a['app'],b['bundle_id_b']))
            ctx=evidence(a['context']); neg=evidence(a['counter'])
            for e in ctx:relationships.append(relationship(e,'contextual','supporting_context','uncertain' if a['unknown'] else 'direct'))
            for e in neg:relationships.append(relationship(e,'direct','counterevidence','not_applicable'))
            audit_id=None
            if a['status']!='sufficient_support':
                audit_id=f'{aid}:scoped_audit'
                absence.append({'audit_id':audit_id,'review_id_b':rid,'aspect_id_b':aid,
                    'bounded_unsupported_ask':a['unknown'],
                    'review_method':'Full hierarchical reading of all 86 corpus articles, followed by scoped review of cited neighboring rules and delegation clauses; no retrieval pipeline.',
                    'corpus_coverage':{d:[v['article'] for v in articles if v['document_id']==d] for d in DOCS.values()},
                    'closest_corpus_evidence':ctx+[e for b in bundles for e in b['evidence']],
                    'finding':a['note'] or a['unknown'],
                    'alternatives_reviewed':'Reviewed the Act, Decree and ethical framework; topical/delegating provisions do not establish the requested missing conclusion.',
                    'failed_keyword_search_is_not_basis':True,
                    'external_law_consulted':False})
            aspects.append({'aspect_id_b':aid,'proposition':a['proposition'],
                'origin':a['origin'],'materiality':'material: '+a['proposition'],
                'parent_aspect_id':None,'answer_role':role,'support_bundle_operator':'OR',
                'support_bundles':bundles,'context_evidence':ctx,'counterevidence':neg,
                'evidence_sufficiency':{'label':a['status'],
                    'supported_scope':a['proposition'] if bundles else None,
                    'unsupported_scope':a['unknown'],'conflict_flag':bool(a['note'] and 'CONFLICT' in a['note']),
                    'rationale':a['note'] or ('Exact corpus support for the bounded proposition.' if bundles else a['unknown']),
                    'corpus_audit_id':audit_id},
                'applicability':a['app'],'annotation_confidence':'moderate' if a['unknown'] or s['admission']=='NEEDS_ADJUDICATION' else 'high'})
            modes=['P+'] if role=='substantive_supported' else ['Q','U'] if role=='qualified_partial' else ['U']
            for mode in modes:
                obligations.append({'obligation_id_b':aid+':'+mode,'aspect_id_b':aid,'set':mode,
                    'expected_response_mode':{'P+':'substantive_supported','Q':'qualified_partial','U':'unresolved_disclosure'}[mode],
                    'content':a['unknown'] if mode=='U' else a['proposition'],
                    'necessary_qualification':a['condition'] or a['unknown'],
                    'equivalence_rule':'Semantic equivalence preserving actor, conditions, exceptions, amounts and time units; disclosure alone does not earn substantive credit.'})
        supported=[a for a in aspects if a['support_bundles']]
        fully=all(a['evidence_sufficiency']['label']=='sufficient_support' for a in aspects)
        answerability='fully_answerable' if fully else 'partially_answerable' if supported else 'insufficient_evidence'
        options=[]
        for a in supported:
            options.append([set((e['document_id'],e['article']) for e in b['evidence']) for b in a['support_bundles']])
        joint=[set().union(*v) for v in itertools.product(*options)] if options else []
        min_articles=min(map(len,joint)) if joint else 0
        min_docs=min(len({d for d,art in v}) for v in joint) if joint else 0
        pcount=sum(a['answer_role']=='substantive_supported' for a in aspects)
        values={'D1':s['broad'],'D2':pcount>=3,'D3':min_articles>=2,
            'D4':min_docs>=2,'D5':min_articles>=2,'D7':fully and pcount>=2,
            'D8':len(aspects)>=2 or s['applicability'],'D9':s['applicability'],'D10':not fully}
        rationale={
            'D1':'Finite planning scope without a supplied checklist.' if values['D1'] else 'Concrete enumerated or narrow interpretive ask.',
            'D2':f'{pcount} independent sufficiently supported substantive propositions; Q/U do not inflate this count.',
            'D3':f'Minimum {min_articles} distinct articles across independently accepted support alternatives for the supported scope.',
            'D4':s['d4'] or f'Minimum {min_docs} documents across accepted alternatives. All three documents were inspected for a single-document alternative.',
            'D5':'Support necessarily spans distinct articles.' if values['D5'] else 'No necessary inter-article dispersion established for supported scope.',
            'D7':'Coordinating the listed independent propositions/conditions creates structural omission opportunity; no generated answer inspected.' if values['D7'] else 'Not tagged: whole scoped sufficient support with multiple independent propositions was not established.',
            'D8':'Distinct evidence needs or actor/condition concept distinction follows the listed aspects.' if values['D8'] else 'Single narrow evidence need.',
            'D9':s['quality'] if values['D9'] else 'No material competing applicability predicate selected for this bounded ask.',
            'D10':'At least one material conclusion remains unsupported or partial; see aspect audits.' if values['D10'] else 'All bounded material conclusions have sufficient corpus support.'}
        dims={d:{'value':v,'rationale':rationale[d],'basis':'corpus_structure','verification_status':'B_INDEPENDENT_REVIEW_NOT_ADJUDICATED'} for d,v in values.items()}
        dims['D6']={'value':None,'verification_status':'EMPIRICAL_UNVERIFIED','basis':None,'rationale':'No retrieval or reranking inference; not used for admission.'}
        output.append({'schema':'independent-annotation-B-v1','review_id_b':rid,'query':r['query'],
            'query_sha256':sha(r['query'].encode()),'reviewer_role':'INDEPENDENT_ANNOTATOR_B',
            'reviewer_type':'MODEL_BASED_INDEPENDENT_ANNOTATOR','independent_context':True,
            'independent_human_legal_review':False,
            'scope':{'explicit_asks':s['asks'],'bounded_interpretation':s['bounds'],
                'relevant_user_facts':s['facts'],'unspecified_facts':s['missing'],
                'excluded_scope':[{'scope':e,'reason':'Outside the express bounded task; no additional legal conclusion assumed.'} for e in s['excluded']]},
            'required_legal_aspects':aspects,'evidence_relationships':relationships,
            'response_obligations':obligations,'answerability':{'label':answerability,
                'derivation':'All material aspects sufficient' if fully else 'Some substantive support plus material unresolved portion' if supported else 'No material requested legal portion supported; nearby context is not substantive support'},
            'dimensions':dims,'admission_recommendation':{'label':s['admission'],
                'rationale':s['quality'],'basis':['legal_clarity','naturalness','bounded_scope','corpus_support','annotation_quality','uniqueness_pending_text_screen','challenge_relevance'],
                'expected_system_performance_used':False},
            'research_audit':{'method':'direct corpus file and hierarchy reading','corpus_files':['documents.csv','articles.jsonl','chunks.jsonl'],
                'reviewed_article_refs':sorted({e['reference'] for a in aspects for e in a['context_evidence']+a['counterevidence']+[e for b in a['support_bundles'] for e in b['evidence']]}),
                'full_corpus_scoped_audit_ids':[a['evidence_sufficiency']['corpus_audit_id'] for a in aspects if a['evidence_sufficiency']['corpus_audit_id']]},
            'review_status':'INDEPENDENT_B_SUBSTANTIVE_COMPLETE_NOT_ADJUDICATED',
            'completed_at_utc':stamp})
    (OUT/'annotation_B_v1.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in output))
    (OUT/'scoped_corpus_reviews_v1.json').write_text(json.dumps(absence,ensure_ascii=False,indent=2)+'\n')
    (OUT/'substantive_lock_v1.json').write_text(json.dumps({'locked_at_utc':stamp,
        'candidate_count':60,'annotation_sha256':sha((OUT/'annotation_B_v1.jsonl').read_bytes()),
        'historical_text_screen_started':False,'A_comparison_performed':False},indent=2)+'\n')
    for p in OUT.iterdir():
        if p.is_file():p.chmod(0o600)
    print(json.dumps({'substantive_annotations':len(output),'material_aspects':sum(len(r['required_legal_aspects']) for r in output),'scoped_partial_or_absence_audits':len(absence)}))

if __name__=='__main__': main()
