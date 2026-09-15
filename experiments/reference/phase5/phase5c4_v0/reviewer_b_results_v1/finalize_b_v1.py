"""Produce public-safe and private manifests for the independent B retry."""
import json,hashlib,datetime,os,collections
from pathlib import Path
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[5]
BASE='data/evaluation/generation/phase5/'
REQUEST=Path('/home/minhkha/.codex/attachments/e68f2852-04b5-44fb-944d-0db448812cbf/pasted-text.txt')
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(name,value):
    (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
    return {'sha256':h.hexdigest(),'size_bytes':path.stat().st_size}

def main():
    stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
    rows=[json.loads(l) for l in (OUT/'annotation_B_v1.jsonl').read_text().splitlines()]
    initial=[json.loads(l) for l in (OUT/'annotation_B_substantive_locked_v1.jsonl').read_text().splitlines()]
    validation=json.loads((OUT/'annotation_structural_validation_v1.json').read_text())
    assert validation['status']=='PASS' and validation['annotation_sha256']==sha((OUT/'annotation_B_v1.jsonl').read_bytes())
    assert len(rows)==len(initial)==60
    for a,b in zip(rows,initial):
        assert a['scope']==b['scope'] and a['answerability']==b['answerability']
        assert [(x['aspect_id_b'],x['proposition'],x['answer_role']) for x in a['required_legal_aspects']]==[(x['aspect_id_b'],x['proposition'],x['answer_role']) for x in b['required_legal_aspects']]
        assert a['response_obligations']==b['response_obligations']
        assert {d:v['value'] for d,v in a['dimensions'].items()}=={d:v['value'] for d,v in b['dimensions'].items()}
    schema=json.loads((OUT/'packet_schema_validation_v1.json').read_text())
    assert schema['status']=='PASS'
    schema.update({'query_text_read_in_authorized_session_tool_output':True,
        'authorization':'User expressly allowed reading queries through tool output in this session; exact queries remain forbidden in result console/public reports.',
        'public_report_or_result_console_query_text_emitted':False,
        'candidate_content_semantically_seen':True})
    # Preserve chronology of the initial schema-only read rather than relabel its event.
    schema['initial_schema_check_query_text_emitted']=schema.pop('query_text_emitted')
    dump('packet_schema_validation_v1.json',schema)
    counts={'candidates':60,'scopes':60,'required_aspects':60,'support_bundles':60,
        'applicability':60,'answerability':60,'dimensions':60,'admission_recommendations':60,
        'new_candidate_contamination_screen':60,'historical_31_contamination_screen':60,
        'medical_chatbot_contamination_screen':0,'full_contamination_screen':0,
        'material_aspects':sum(len(r['required_legal_aspects']) for r in rows),
        'answerability_counts':dict(collections.Counter(r['answerability']['label'] for r in rows)),
        'answer_role_counts':dict(collections.Counter(a['answer_role'] for r in rows for a in r['required_legal_aspects'])),
        'admission_counts':dict(collections.Counter(r['admission_recommendation']['label'] for r in rows)),
        'dimension_counts':{d:sum(r['dimensions'][d]['value'] is True for r in rows) for d in ['D1','D2','D3','D4','D5','D7','D8','D9','D10']},
        'candidate_semantic_similarity_flag_pairs':7}
    independence={'annotation_A_read':False,'A_substantive_metadata_seen':False,
        'system_output_read':False,'retrieval_inference':0,'reranking_inference':0,
        'network_api':0,'production_calls':0,'evaluator_calls':0,
        'comparison_with_A_performed':False,'adjudication_performed':False,
        'independent_context':True,'independent_human_legal_review':False,
        'old_reviewer_packet_semantically_read':False,
        'old_contamination_reference_opened':False,
        'annotation_A_or_system_content_emitted_by_hash_worker':False,
        'audit_interpretation':'annotation_A_read/system_output_read denote substantive inspection by the reviewer. A local hash worker read opaque file bytes solely to compute integrity digests; no parsing or content output for prohibited files.',
        'hash_worker_reads_are_separately_enumerated':True,
        'basis':'Observed tool actions and explicit artifact reads; not an OS-wide process/network attestation.'}
    explicit_reads=[
        (str(REQUEST),'user request'),
        (BASE+'phase5c4_v0/custodian/phase5c4b0_remediation_v0/fresh_reviewer_b_handoff_v1.md','B0 candidate-independent handoff; expressly requested path discovery'),
        (BASE+'phase5c4_v0/reviewer_b_packet_v1/reviewer_b_annotation_instructions_v1.md','sanitized packet instructions'),
        (BASE+'phase5c4_v0/reviewer_b_packet_v1/reviewer_b_packet_manifest_v1.json','packet authority and hashes'),
        (BASE+'phase5c4_v0/reviewer_b_packet_v1/reviewer_b_queries_v1.jsonl','initial structural-only parser; subsequently complete text read after user allowed session tool output'),
        (BASE+'phase5c3_v0/phase5c3_frozen_design_spec_v0.md','candidate-independent frozen design'),
        (BASE+'phase5c3_v0/phase5c3_spec_bindings_v0.json','candidate-independent source bindings'),
        (BASE+'phase5c3_v0/phase5c3_freeze_manifest_v0.json','frozen design status/hash authority; no historical outcomes artifact opened'),
        (BASE+'phase5c2_v0/phase5c2_challenge_set_design_v0.md','hash-bound inherited generic annotation rubric, taxonomy and P/Q/U semantics'),
        ('data/versions/corpus-v0.1/documents.csv','complete corpus document inventory'),
        ('data/versions/corpus-v0.1/articles.jsonl','complete hierarchy inspection of 86 articles, selected re-reads to recover truncated tool output'),
        ('data/versions/corpus-v0.1/chunks.jsonl','structure/count/identity inspection, exact B-selected evidence serialization and validation; selected parent_context re-read'),
        ('data/evaluation/generation/phase5/query_inputs_v0.json','after substantive lock only; verified 31 records containing exactly query_id/query; no gold/scores/outcomes fields')]
    read_records=[]
    for name,purpose in explicit_reads:
        p=Path(name) if Path(name).is_absolute() else ROOT/name
        read_records.append({'path':name,'purpose':purpose,**digest(p)})
    # Hash every preexisting regular file and compare symlink targets; never emit contents.
    baseline=json.loads((OUT/'integrity_baseline_v1.json').read_text())
    after={};changed=[];missing=[]
    for name,old in baseline['files'].items():
        p=ROOT/name
        if not p.is_file() or p.is_symlink():missing.append(name);continue
        after[name]=digest(p)
        if after[name]!=old:changed.append(name)
    nowpaths=set();symlinks={};new=[]
    for root,dirs,files in os.walk(ROOT,followlinks=False):
        dirs[:]=[d for d in dirs if Path(root)/d!=OUT]
        for name in dirs+files:
            p=Path(root)/name
            if p.is_symlink():symlinks[str(p.relative_to(ROOT))]=os.readlink(p)
        for name in files:
            p=Path(root)/name
            if p.is_file() and not p.is_symlink():nowpaths.add(str(p.relative_to(ROOT)))
    new=sorted(nowpaths-set(baseline['files']))
    integrity_pass=not changed and not missing and not new and symlinks==baseline['symlinks']
    integrity={'status':'PASS' if integrity_pass else 'FAIL','before_manifest':'integrity_baseline_v1.json',
        'before_manifest_sha256':sha((OUT/'integrity_baseline_v1.json').read_bytes()),
        'preexisting_regular_file_count':len(baseline['files']),'preexisting_symlink_count':len(baseline['symlinks']),
        'changed':changed,'missing':missing,'additions_outside_allowed_namespace':new,
        'symlink_targets_unchanged':symlinks==baseline['symlinks'],
        'after':after,'checked_at_utc':stamp,
        'hash_mode':'Opaque streaming SHA-256 only for files outside the substantive-read allowlist; no A/output contents parsed or exposed.'}
    dump('integrity_before_after_v1.json',integrity)
    assert integrity_pass,'Preexisting artifact integrity failed; do not issue PASS'
    corpus=json.loads((OUT/'reviewer_b_corpus_audit_v1.json').read_text())
    scoped=json.loads((OUT/'scoped_corpus_reviews_v1.json').read_text())
    corpus.update({'status':'B_CORPUS_REVIEW_COMPLETE','candidate_review_count':60,
        'semantic_read_coverage':{'documents.csv':'complete','articles.jsonl':'all 86 article hierarchies; truncated outputs re-read for L12–22 and N8–9',
            'chunks.jsonl':'complete deterministic structural inspection and selected normative/context spans; not a claim of reading every redundant chunk separately'},
        'scoped_absence_reviews':scoped,'scoped_review_count':len(scoped),
        'corpus_files_sha256':{str(p.relative_to(ROOT)):digest(p)['sha256'] for p in (ROOT/'data/versions/corpus-v0.1').iterdir() if p.is_file()},
        'per_candidate_research_trail':'annotation_B_v1.jsonl / research_audit',
        'lookup_operations':['filter articles by document_id and numeric article range','enumerate every article title','resolve exact document/article/clause/point to chunk IDs',
            'compare exact evidence spans and parent_context to corpus','hierarchical scoped absence/alternative review'],
        'retrieval_rank_used':False,'evidence_anchor_corrections':'evidence_anchor_corrections_v1.json',
        'conflicts':'Private aspect-level conflict flags preserved for trusted legal adjudication; corpus not corrected.'})
    dump('reviewer_b_corpus_audit_v1.json',corpus)
    access={'schema':'phase5c4b-access-v1','role':'INDEPENDENT_ANNOTATOR_B',
        'created_at_utc':stamp,'independence_audit':independence,
        'explicit_substantive_or_projected_input_reads':read_records,
        'all_preexisting_hash_only_reads':'integrity_baseline_v1.json / files; integrity_before_after_v1.json / after',
        'hash_worker_A_bytes_read':True,'hash_worker_system_artifact_bytes_read':True,
        'hash_read_note':'Intentional opaque integrity computation required by user; these bytes never entered reviewer semantic context.',
        'filename_only_discovery':['ancestor AGENTS.md existence checks (none found)','rg --files for AGENTS.md under repository parent (no matches)',
            'directory inventories for Phase 5C.3/5C.4/corpus; candidate-independent inherited rubric filename discovery',
            'preexisting path inventory filtered for historical query-only resources; no output/gold/trace content searches'],
        'generated_files_read_scope':'Files in the private retry namespace read by generation, screening, correction, validation, manifesting and integrity scripts; exact paths in generated_artifact_hashes_v1.json.',
        'runtime_note':'Python standard-library loader/OS incidental reads are not syscall-traced; explicit artifact reads and all hash-worker file reads are recorded.',
        'tool_metadata_discovery':'Local list of available tool names/descriptions inspected while checking for a private file reader; no connector/network tools invoked.',
        'authorizations':[{'event':'session_query_tool_output_allowed','source':'user asynchronous reply','effect':'Exact query text may be read in this session tool output; it remains prohibited in public reports/result console.'},
            {'event':'old_contamination_reference_forbidden','source':'user asynchronous reply','effect':'Do not open old packet reference; wait for newly sanitized/audited reference from Dataset Custodian; pending screen does not compromise substantive independence.'}],
        'future_v2_implementation_in_this_context':'FORBIDDEN',
        'holdout_storage_isolation':'HOLDOUT_STORAGE_ISOLATION_NOT_YET_ENFORCED',
        'independent_human_legal_review_complete':False,'network_api_calls':0}
    dump('phase5c4b_access_manifest_v1.json',access)
    ready={'schema':'phase5c4b-agreement-ready-v1','phase5c4b_retry_status':'PASS',
        'status_scope':'Clean independent substantive B pass; user-authorized deferred medical contamination reference remains pending.',
        'B_annotations_complete':True,'candidate_count':60,'trusted_phase5c4c_comparison_input_ready':True,
        'comparison_has_started':False,'agreement_metrics_computed':False,
        'full_contamination_screen_complete':False,'contamination_status':'PENDING_SANITIZED_REFERENCE',
        'completed_screen_sources':['new candidate query text','31 historical query-only inputs'],
        'pending_screen_source':'Newly sanitized and audited exploratory medical chatbot query-only reference from Dataset Custodian',
        'all_admission_recommendations_provisional_pending_full_uniqueness_review':True,
        'independent_context_review_complete':True,'independent_human_legal_review_complete':False,
        'ready_for_final_dataset_freeze':False,'dataset_frozen':False,'holdout_storage_isolation_enforced':False,
        'D6':'EMPIRICAL_UNVERIFIED','Agentic_v2_implementation':'NOT STARTED',
        'annotation_file':'annotation_B_v1.jsonl','annotation_sha256':sha((OUT/'annotation_B_v1.jsonl').read_bytes()),
        'counts':counts,
        'required_next_trusted_actions':['Obtain audited sanitized medical reference and finish deferred text screen',
            'Perform Phase 5C.4-C A/B comparison in an authorized trusted context','Resolve human legal review and legal adjudication requirements before freeze'],
        'declaration':'B annotations complete and ready for trusted A/B comparison.'}
    dump('phase5c4b_agreement_ready_summary_v1.json',ready)
    final_validation={'schema':'phase5c4b-validation-v1','status':'PASS','status_scope':ready['status_scope'],
        'independent_annotation_gates_pass':True,'all_end_to_end_dataset_gates_complete':False,
        'sanitized_packet_verified':'PASS','visible_candidate_fields':['review_id_b','query'],
        'independence_audit':'PASS','annotation_structural_validation':'PASS',
        'annotation_structural_check_count':sum(validation['checks'].values()),
        'support_anchor_correction_audit':'PASS_PRESERVED_PRIOR_BYTES',
        'no_scope_proposition_answerability_or_dimension_value_changes_after_text_screen':True,
        'contamination_screening':'PENDING_SANITIZED_REFERENCE','missing_reference_user_authorized_to_defer':True,
        'corpus_only_annotation':True,'D6':'EMPIRICAL_UNVERIFIED',
        'no_exact_query_in_public_reports_or_result_console':None,
        'session_tool_output_query_read_explicitly_authorized':True,
        'preexisting_integrity':'PASS','additions_only_allowed_namespace':True,
        'counts':counts,'independence':independence,
        'ready_for_trusted_comparison':True,'ready_for_final_dataset_freeze':False,
        'PASS_does_not_mean':['full contamination screening complete','A/B agreement','adjudication','human legal review','dataset freeze','storage isolation enforcement','v2 authorization']}
    summary='''# Phase 5C.4-B retry — independent B review

PASS cho lượt annotation nội dung độc lập, 60/60 ứng viên. Sàng lọc contamination tổng thể còn `PENDING_SANITIZED_REFERENCE`, theo chỉ dẫn bổ sung của người dùng; không tuyên bố hoàn tất phần này.

Role: `INDEPENDENT_ANNOTATOR_B`.
Reviewer type: `MODEL_BASED_INDEPENDENT_ANNOTATOR`.
Independent context review complete: YES
Independent human legal review complete: NO

Packet B0 đã được kiểm tra: 60 bản ghi, đúng hai trường `review_id_b`, `query`, ID duy nhất và hash khớp manifest. Annotation A, metadata nội dung A và kết quả hệ thống không được xem. Không có API/network, production/evaluator hoặc retrieval/reranking inference. D6 vẫn `EMPIRICAL_UNVERIFIED`.

Đã hoàn thành scope, aspects, bundle OR/AND, applicability, sufficiency, answerability, dimensions và khuyến nghị admission cho cả 60 ứng viên. Có 155 aspect: 139 substantive-supported, 3 qualified-partial và 13 unresolved-disclosure. Các aspect partial có nghĩa vụ Q và U riêng. Có 16 audit theo phạm vi với toàn bộ 86 điều trong ba văn bản corpus; không suy thiếu bằng chứng từ thất bại tìm từ khóa.

Answerability: 44 fully_answerable, 9 partially_answerable, 7 insufficient_evidence. Khuyến nghị admission: 58 RETAIN, 1 RESERVE, 1 NEEDS_ADJUDICATION; đều tạm thời cho đến khi hoàn tất kiểm tra uniqueness. Không áp quota hoặc suy split/family của A.

Đã so sánh query text của 60 ứng viên với nhau và với nguồn lịch sử 31 câu chỉ chứa query/ID. Ghi nhận 7 cặp gần nhau cần trusted review, không gán cluster hoặc split. Nguồn chatbot y tế cũ chưa được mở. Chờ Dataset Custodian tạo bản tham chiếu sanitized mới và audit rằng chỉ có query text/opaque IDs; phần kiểm tra này chưa hoàn thành và không làm mất independence của annotation nội dung.

Hash bản annotation nội dung trước screening được giữ trong `substantive_lock_v1.json`, cùng bản sao nguyên trạng. Audit tối giản bundle sau đó thay sáu nhóm neo bằng chứng/tham chiếu dư, dựa duy nhất vào hierarchy corpus; giữ bản trước sửa và nhật ký, không đổi scope, proposition, answerability hay giá trị dimension. Không có A/B comparison hoặc adjudication.

Preexisting artifact integrity: PASS. Chỉ thêm tệp trong namespace retry được phép; corpus, benchmark, thiết kế, A, B thất bại, B0 và runtime được giữ nguyên. Hash worker đọc byte mù để kiểm tra toàn vẹn, không đưa nội dung tệp cấm vào context. Access manifest phân biệt rõ việc này với đọc nội dung pháp lý.

Người dùng đã cho phép đọc query qua đầu ra công cụ của phiên; không có query nguyên văn trong báo cáo public-safe hoặc console kết quả. Tệp riêng có quyền owner-only, nhưng trạng thái vẫn `HOLDOUT_STORAGE_ISOLATION_NOT_YET_ENFORCED`; chưa có bằng chứng cô lập vai trò ở mức kỹ thuật.

B annotations complete and ready for trusted A/B comparison.
Ready for A/B comparison: YES — readiness của đầu vào annotation, không phải full contamination clearance.
Ready for final dataset freeze: NO.
Dataset frozen: NO. Human legal review/adjudication requirements remain unresolved.
Agentic v2 implementation: NOT STARTED; future implementation in this context: FORBIDDEN.
'''
    (OUT/'phase5c4b_review_summary_v1.md').write_text(summary)
    console='''Phase 5C.4-B retry status:
PASS

Role:
INDEPENDENT_ANNOTATOR_B

Reviewer type:
MODEL_BASED_INDEPENDENT_ANNOTATOR

Independent context:
YES

Sanitized B packet verified:
PASS

Reviewer-B visible candidate fields:
review_id_b, query

Annotation A substantive labels read:
NO

A candidate metadata exposed:
NO

System outputs inspected:
NO

Candidates independently reviewed:
60/60

Scope annotations completed:
60/60

Required-aspect annotations completed:
60/60

Support-bundle annotations completed:
60/60

Applicability annotations completed:
60/60

Answerability annotations completed:
60/60

Dimension annotations completed:
60/60
D6:
EMPIRICAL_UNVERIFIED

Admission recommendations completed:
60/60

Contamination screening completed:
0/60 — PENDING_SANITIZED_REFERENCE

Network/API calls:
0

Production/evaluator calls:
0

Retrieval/reranking inference:
0

Exact query text printed publicly:
NO

Independent context review complete:
YES

Independent human legal review complete:
NO

HOLDOUT storage isolation:
NOT_YET_ENFORCED

Dataset frozen:
NO

Agentic v2 implementation:
NOT STARTED

Preexisting artifact integrity:
PASS

Ready for trusted Phase 5C.4-C A/B comparison:
YES

Ready for final dataset freeze:
NO

STOP
'''
    (OUT/'phase5c4b_console_v1.txt').write_text(console)
    manifest={'schema':'reviewer-b-manifest-v1','created_at_utc':stamp,
        'role':'INDEPENDENT_ANNOTATOR_B','reviewer_type':'MODEL_BASED_INDEPENDENT_ANNOTATOR',
        'independent_context':True,'independent_human_legal_review':False,
        'annotation_status':'COMPLETE','contamination_status':'PENDING_SANITIZED_REFERENCE',
        'counts':counts,'independence_audit':independence,
        'packet_path':BASE+'phase5c4_v0/reviewer_b_packet_v1/reviewer_b_queries_v1.jsonl',
        'corpus_version':'corpus-v0.1','generic_rubric':BASE+'phase5c2_v0/phase5c2_challenge_set_design_v0.md',
        'rubric_authority':BASE+'phase5c3_v0/phase5c3_spec_bindings_v0.json',
        'candidate_ids_in_packet_order':[r['review_id_b'] for r in rows],
        'exposure_declaration':{'challenge_query_plaintext_seen':True,'all_candidates_treated_as_potential_HOLDOUT':True,
            'session_tool_output_read_authorized_by_user':True,'public_reports_and_result_console_query_free':True,
            'future_v2_implementation_in_this_context':'FORBIDDEN'},
        'storage_isolation':'HOLDOUT_STORAGE_ISOLATION_NOT_YET_ENFORCED',
        'no_reference_answers_generated':True,'gold_finalized':False,'dataset_frozen':False,
        'human_review_adjudication_unresolved':True,'trusted_comparison_ready':True,
        'preexisting_integrity':'PASS','final_annotation_sha256':sha((OUT/'annotation_B_v1.jsonl').read_bytes()),
        'historical_reference_provenance':'text_screen_provenance_v1.json',
        'corpus_audit':'reviewer_b_corpus_audit_v1.json','access_audit':'phase5c4b_access_manifest_v1.json',
        'pending_reference_requirements':['New sanitized reference outside quarantined packet',
            'Audit confirms only historical/exploratory query text and opaque IDs',
            'No A metadata, splits, dimensions, scores, gold, traces or system outcomes'],
        'artifact_hash_index':'generated_artifact_hashes_v1.json'}
    dump('reviewer_b_manifest_v1.json',manifest)
    dump('phase5c4b_validation_v1.json',final_validation)
    public_names=['phase5c4b_review_summary_v1.md','phase5c4b_agreement_ready_summary_v1.json',
        'phase5c4b_access_manifest_v1.json','phase5c4b_validation_v1.json',
        'integrity_before_after_v1.json','phase5c4b_console_v1.txt']
    leaked=[]
    for name in public_names:
        text=(OUT/name).read_text()
        if any(r['query'] in text for r in rows):leaked.append(name)
    assert not leaked,'Public-safe file contains exact query text'
    final_validation['no_exact_query_in_public_reports_or_result_console']=True
    final_validation['public_safe_files_checked']=public_names
    dump('phase5c4b_validation_v1.json',final_validation)
    # Enumerate every generated file read during final hashing (self-excluded index).
    generated={str(p.relative_to(ROOT)):digest(p) for p in OUT.iterdir() if p.is_file() and p.name!='generated_artifact_hashes_v1.json'}
    dump('generated_artifact_hashes_v1.json',{'created_at_utc':stamp,'files':generated,
        'self_excluded':True,'read_purpose':'Final byte integrity and exact generated-file access inventory'})
    for p in OUT.iterdir():
        if p.is_file():p.chmod(0o600)
    print(console,end='')

if __name__=='__main__':main()
