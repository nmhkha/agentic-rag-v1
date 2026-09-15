"""Private versioned B evidence-link correction from corpus hierarchy only.

Preserves the pre-screen substantive lock and pre-correction annotation bytes.
No scope/proposition/answerability/admission judgment is rewritten here.
"""
import json,hashlib,datetime,itertools
from pathlib import Path
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[5]
def sha(b):return hashlib.sha256(b).hexdigest()
def main():
    path=OUT/'annotation_B_v1.jsonl';before=path.read_bytes()
    prior=OUT/'annotation_B_pre_anchor_correction_v1.jsonl'
    assert not prior.exists(),'Correction already executed'
    prior.write_bytes(before)
    rows=[json.loads(l) for l in before.splitlines()]
    chunks={x['chunk_id']:x for x in [json.loads(l) for l in (ROOT/'data/versions/corpus-v0.1/chunks.jsonl').read_text().splitlines()]}
    changes=[]
    # Parent-intro duties are present in each point chunk's parent_context.
    # One exact parent_context span supplies that duty; all sibling point bodies
    # are not jointly necessary when the aspect does not enumerate their fields.
    for number,aspect_no,reference in [(11,3,'N13.6'),(12,3,'N13.6'),(18,1,'N27.6'),(48,2,'N13.6')]:
        row=rows[number-1];a=row['required_legal_aspects'][aspect_no-1]
        for b in a['support_bundles']:
            selected=[e for e in b['evidence'] if e['reference']==reference]
            assert selected
            e=selected[0].copy();chunk=chunks[e['chunk_id']]
            intro=e['hierarchy_context']['clause_intro'];assert intro in chunk['parent_context']
            e['relevant_span']=intro;e['source_field']='parent_context'
            e['span_start']=chunk['parent_context'].index(intro);e['span_end']=e['span_start']+len(intro)
            e['span_sha256']=sha(intro.encode());e['source_field_sha256']=sha(chunk['parent_context'].encode())
            e['reference']=reference+'^parent_intro'
            e['anchor_rationale']='Exact normative clause introduction in this chunk parent_context; sibling point bodies are not required for this proposition.'
            b['evidence']=[x for x in b['evidence'] if x not in selected]+[e]
            oldids={x['chunk_id'] for x in selected}
            rels=[x for x in row['evidence_relationships'] if x['aspect_id_b']==a['aspect_id_b'] and x['bundle_id_b']==b['bundle_id_b'] and x['chunk_id'] in oldids]
            first=next(x for x in rels if x['chunk_id']==e['chunk_id']).copy()
            first['evidence_source_field']='parent_context'
            row['evidence_relationships']=[x for x in row['evidence_relationships'] if x not in rels]+[first]
            changes.append({'review_id_b':row['review_id_b'],'aspect_id_b':a['aspect_id_b'],
                'change':'Replace jointly unnecessary sibling-point bodies with one exact normative parent_context span.',
                'old_chunk_ids':sorted(oldids),'retained_anchor_chunk_id':e['chunk_id'],'source_field':'parent_context'})
    # Remove redundant restatements, keeping each necessary independent proposition.
    for number,aspect_no,refs in [(43,4,{'N39.5.a','N39.5.b'}),(46,3,{'L27.2'})]:
        row=rows[number-1];a=row['required_legal_aspects'][aspect_no-1]
        for b in a['support_bundles']:
            removed=[e for e in b['evidence'] if e['reference'] in refs]
            assert removed
            b['evidence']=[e for e in b['evidence'] if e not in removed]
            removedids={e['chunk_id'] for e in removed}
            # Retain redundant restatements as context, never required AND members.
            a['context_evidence']+=removed
            for rel in row['evidence_relationships']:
                if rel['aspect_id_b']==a['aspect_id_b'] and rel['bundle_id_b']==b['bundle_id_b'] and rel['chunk_id'] in removedids:
                    rel['bundle_id_b']=None;rel['relevance']='contextual';rel['evidence_role']='supporting_context'
            changes.append({'review_id_b':row['review_id_b'],'aspect_id_b':a['aspect_id_b'],
                'change':'Move redundant statutory restatement from required AND bundle to contextual evidence.',
                'context_chunk_ids':sorted(removedids)})
    for row in rows:
        supported=[a for a in row['required_legal_aspects'] if a['support_bundles']]
        options=[[{(e['document_id'],e['article']) for e in b['evidence']} for b in a['support_bundles']] for a in supported]
        joint=[set().union(*v) for v in itertools.product(*options)] if options else []
        minimum=min(map(len,joint)) if joint else 0
        docs=min(len({d for d,n in v}) for v in joint) if joint else 0
        assert row['dimensions']['D3']['value']==(minimum>=2)
        assert row['dimensions']['D4']['value']==(docs>=2)
        row['dimensions']['D3']['rationale']=f'Minimum {minimum} distinct articles across independently accepted support alternatives for the supported scope.'
        if row['dimensions']['D4']['rationale'].startswith('Minimum '):
            row['dimensions']['D4']['rationale']=f'Minimum {docs} documents across accepted alternatives. All three documents were inspected for a single-document alternative.'
        row['research_audit']['reviewed_article_refs']=sorted({e['reference'] for a in row['required_legal_aspects'] for e in a['context_evidence']+a['counterevidence']+[e for b in a['support_bundles'] for e in b['evidence']]})
    path.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))
    record={'created_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'reason':'Corpus hierarchy and AND-bundle necessity audit; not historical similarity or system outcomes.',
        'original_pre_screen_lock_preserved':True,'before_sha256':sha(before),'after_sha256':sha(path.read_bytes()),
        'pre_correction_copy':prior.name,'scope_propositions_answerability_dimension_values_changed':False,
        'changes':changes,'A_or_system_inputs_used':False}
    (OUT/'evidence_anchor_corrections_v1.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'evidence_anchor_corrections':len(changes),'scope_or_answerability_changes':0,'pre_screen_lock_preserved':True}))
if __name__=='__main__':main()
