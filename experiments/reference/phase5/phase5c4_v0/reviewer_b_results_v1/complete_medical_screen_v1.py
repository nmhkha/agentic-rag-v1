"""Complete the deferred, query-text-only medical contamination review.

Does not load Annotation A, the quarantined packet, system outcomes, or any
retrieval module. The sealed B annotation files are hashed only and never written.
The per-item semantic judgments below were authored independently by Reviewer B
after reading only the newly authorized medical reference.
"""
import collections
import datetime
import hashlib
import json
import os
import re
import unicodedata
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[5]
PACKET = OUT.parent / 'reviewer_b_packet_v1/reviewer_b_queries_v1.jsonl'
REFERENCE = OUT.parent / 'reviewer_b_packet_v1/contamination_reference_medical_v1.json'

# Private text-only distinction for each query, in the supplied packet order.
# No medical gold, inferred risk classification, or hidden proposition bundle is used.
RATIONALES = [
 'Phân biệt nhà cung cấp theo thương hiệu với nhóm kỹ thuật thuê ngoài; không phải kế hoạch xây chatbot y tế.',
 'Chia sẻ năng lực hạ tầng tư nhân và giữ quyền quản lý/lựa chọn công nghệ; khác mục đích xây chatbot y tế.',
 'Ngoại lệ phân loại công cụ văn phòng đã nhận biết rõ là AI; không cùng tình huống hay câu hỏi triển khai chatbot y tế.',
 'Tra tên và mã tổ chức chứng nhận; nhu cầu danh bạ cụ thể, không phải các lưu ý xây chatbot y tế.',
 'Xác định cơ quan tổng hợp và trình danh mục rủi ro; khác hoàn toàn câu hỏi xây sản phẩm chatbot y tế.',
 'Thủ tục chuyển dữ liệu cá nhân ra nước ngoài với hồ sơ/cơ quan/thời hạn; reference không nêu chuyển dữ liệu hay thủ tục này.',
 'Dùng dữ liệu quốc gia cho nghiên cứu và công bố khoa học; không nêu chatbot, bệnh nhân hoặc dịch vụ y tế.',
 'Hồ sơ rút gọn, thời hạn và hỗ trợ sandbox cấp độ 1 tại một tỉnh; reference không chứa tình tiết thử nghiệm này.',
 'Tư cách bên triển khai khi sắp xếp ảnh gia đình phi thương mại; không cùng tác vụ hoặc bối cảnh chatbot y tế.',
 'Thông báo và quản lý sau phân loại lại tăng mức do tích hợp; khác xây chatbot mới, reference không nêu sự kiện phân loại lại.',
 'Đưa phiên bản AI cao đã đánh giá vào vận hành sau thay mô hình/dữ liệu; chỉ giao nhau ở ý định chuẩn bị AI chung, không cùng tình huống.',
 'Bàn giao hệ thống của nhà cung cấp nước ngoài cho đối tác trong nước với điều kiện chứng nhận đã nêu; không có các tình tiết này trong reference.',
 'Phạm vi Luật đối với hoạt động chỉ phục vụ quốc phòng; không tương đương câu hỏi xây chatbot y tế.',
 'Điều kiện khai thác dữ liệu quốc gia và phí mỗi lượt; không phải tổng thể lưu ý xây chatbot y tế, reference không nêu nguồn dữ liệu này.',
 'Phân loại mô hình độc lập chưa thành hệ thống; khác yêu cầu xây một chatbot y tế.',
 'Chi phí, chứng từ và thanh toán Phiếu hỗ trợ kiểm thử sandbox; reference không đề cập tài trợ hoặc thanh toán.',
 'Triển lãm bảo tàng mô phỏng nhân vật lịch sử và Khung tự nguyện; có dạng câu hỏi chuẩn bị nhưng khác mục đích, nội dung và nghĩa vụ được hỏi.',
 'Gia hạn vận hành chuyển tiếp sau hoàn thành sandbox; không cùng giai đoạn hoặc thủ tục với xây chatbot y tế.',
 'Báo cáo sự cố thiệt hại tài sản, lưu tài liệu và ý nghĩa không thừa nhận lỗi; reference không nêu sự cố đã xảy ra.',
 'Bảo hiểm của hệ thống cao ngoài sandbox; reference không xác định mức rủi ro hoặc đặt câu hỏi bảo hiểm.',
 'Tự đánh giá sự phù hợp và ngưỡng chất lượng dữ liệu của AI cao; reference không chứa hai yêu cầu cụ thể này.',
 'Sửa lỗi thường lệ và có phải phân loại/đánh giá lại không; không cùng sự kiện hoặc mục tiêu xây chatbot y tế.',
 'Phát hành hệ thống tạo video miễn phí và phân công đánh dấu với cửa hàng; khác loại sản phẩm và chuỗi cung cấp nội dung.',
 'Endpoint và schema JSON thông báo phân loại; yêu cầu đặc tả tích hợp cụ thể, không có trong reference.',
 'Phân biệt cấp độ thử nghiệm khi có người tham gia nhưng không dùng đầu ra thực tế; reference không nêu tiêu chí thử nghiệm.',
 'Nghiên cứu và viết ý tưởng trong lab khép kín, không người thực/đầu ra ngoài; dạng chuẩn bị chung giống nhau nhưng tình huống và nhu cầu khác chatbot y tế.',
 'Ưu tiên mua sắm công và tỷ lệ ưu đãi giá cho công nghệ huấn luyện; khác xây chatbot và không cùng proposition được hỏi.',
 'Giao diện dịch vụ công cho người cao tuổi/vùng kết nối kém và cơ chế phản ánh; không nêu hội thoại hay y tế, nên tương đồng lập kế hoạch AI chung chưa đủ near-duplicate mạnh.',
 'Mốc chuyển tiếp khi đổi chức năng thành cao mà không sửa danh mục; không cùng câu hỏi hoặc sự kiện pháp lý.',
 'Chuyển tiếp của trường công đã vận hành AI và kênh thông báo khi cổng chưa mở; khác xây chatbot y tế mới.',
 'Gửi phân loại trung bình tự động, cấp mã/xác nhận và bổ sung tài liệu; không cùng nhu cầu với các lưu ý xây chatbot y tế.',
 'Ngoại lệ công khai hệ thống dân sự thuộc bí mật nhà nước; reference không nêu điều kiện bí mật hay câu hỏi công khai.',
 'Đánh giá tác động bổ sung sau đổi dữ liệu và đào tạo cán bộ khi ra quyết định hành chính; khác sản phẩm và giai đoạn sử dụng.',
 'Việc không dùng mẫu có là lý do từ chối xem xét hỗ trợ phi tài chính; không phải hướng dẫn xây chatbot y tế.',
 'Đủ điều kiện đầu mối/hiện diện của nhà cung cấp nước ngoài khi chưa biết diện chứng nhận; reference không có tình tiết chủ thể này.',
 'Lập kế hoạch môi trường/lợi ích xã hội cho dịch vụ công trên mạng lưới hạ tầng; khác ý định y tế và không thể suy reference chứa bundle này.',
 'Nghĩa vụ nhà phát triển khi sự cố nghiêm trọng; câu hỏi vai trò hẹp, không phải kế hoạch xây chatbot.',
 'Cơ chế bồi thường dù vận hành đúng và phối hợp trước tổn thất khi thuê AI cao; reference không nêu thuê hệ thống, mức cao hoặc bồi thường.',
 'Định hướng hỗ trợ đào tạo và ngân sách năm 2026 của Quỹ; khác đối tượng và thông tin yêu cầu.',
 'Công bố khi cung cấp dữ liệu Nhà nước qua API và quyền sở hữu; reference không nêu cung cấp cơ sở dữ liệu.',
 'Phối hợp xưởng phim và đơn vị phát hành về nhãn giọng mô phỏng; khác chatbot y tế và tình huống sản xuất.',
 'Số năm lưu hồ sơ sau ngừng AI cao và tài liệu thanh tra; reference không có giai đoạn hậu vận hành hoặc yêu cầu định lượng này.',
 'Công nhận cụm liên kết nghiên cứu với hồ sơ, điều phối và quyền lợi; không phải xây một chatbot y tế.',
 'Trách nhiệm nhóm phát triển dịch vụ công đối với đầu độc dữ liệu/mô hình; reference không chứa tranh luận vai trò hay nguy cơ tấn công này.',
 'Phần đánh giá nước ngoài chưa được thừa nhận cùng công khai/lưu hồ sơ; reference không nêu chứng nhận hoặc kết quả nước ngoài.',
 'Quản trị xếp hạng trợ cấp làm căn cứ trực tiếp quyết định hành chính; cùng dạng chuẩn bị triển khai nhưng khác tình huống và các yêu cầu công bằng được nêu.',
 'Công nghệ phần cứng ưu tiên và thuế suất doanh nghiệp; không cùng sản phẩm hoặc câu hỏi y tế.',
 'Đưa AI đánh giá học sinh vào dùng lần đầu với mức cao và diện chứng nhận đã xác định. Gần ở mẫu chuẩn bị AI theo ngành, nhưng khác tác vụ, nhóm bị ảnh hưởng và dữ kiện pháp lý; không phải đổi tên chatbot y tế đơn thuần.',
 'Phối hợp trường–doanh nghiệp đào tạo thực hành và chia sẻ tri thức; khác xây chatbot y tế.',
 'Phân công kiểm soát truy cập dữ liệu và ngăn tái nhận dạng khi huấn luyện tại chỗ; reference không nêu cơ sở dữ liệu hay phương thức khai thác này.',
 'Phạm vi Luật đối với hoạt động hỗn hợp quốc phòng/dân sự; không cùng bối cảnh hoặc câu hỏi với chatbot y tế.',
 'Điều khoản hình sự và khung tù cho giả mạo AI gây hại; reference không nêu hành vi vi phạm hoặc yêu cầu chế tài.',
 'Danh mục và mã dữ liệu cốt lõi/quan trọng để đối chiếu thử nghiệm; không có yêu cầu danh mục này trong reference.',
 'Liêm chính công bố bản thảo nghiên cứu và sở hữu quyền tác giả phần AI tạo; khác tác vụ chatbot y tế và proposition được hỏi.',
 'Công thức/trần bồi thường thiệt hại tài sản; không phải yêu cầu chuẩn bị xây chatbot y tế.',
 'Mức tiền phạt xóa nhãn AI bắt buộc trên video; khác tình huống và không có yêu cầu chế tài tương ứng trong reference.',
 'Phạm vi bắt buộc của Khung đối với cửa hàng tư nhân thông thường; khác câu hỏi xây chatbot y tế.',
 'Hồ sơ phân loại dựa mô hình bên thứ ba, quyền truy cập dữ liệu thô và tài liệu quốc tế; reference không xác định cấu trúc tích hợp hoặc các yêu cầu hồ sơ này.',
 'Nội dung thông tin hỗ trợ phi tài chính, tính tự nguyện của mẫu và báo cáo; khác mục đích xây chatbot y tế.',
 'Chia sẻ mô hình tiếng dân tộc thiểu số và tìm hỗ trợ hạ tầng theo Khung tự nguyện; khác hệ thống y tế và chuỗi tác vụ.'
]
TEMPLATE_OVERLAP = {11,12,17,26,28,36,38,46,48,60}

def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha_bytes(raw): return hashlib.sha256(raw).hexdigest()
def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024),b''):h.update(block)
    return {'sha256':h.hexdigest(),'size_bytes':path.stat().st_size}
def dump(name,value):
    p=OUT/name;p.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n');p.chmod(0o600)
def norm(s):return ' '.join(re.findall(r'\w+',unicodedata.normalize('NFKC',s).casefold()))

def inventory():
    files={};links={}
    for current,dirs,names in os.walk(ROOT,followlinks=False):
        dirs[:]=[d for d in dirs if Path(current)/d!=OUT]
        for name in dirs+names:
            p=Path(current)/name
            if p.is_symlink():links[str(p.relative_to(ROOT))]=os.readlink(p)
        for name in names:
            p=Path(current)/name
            if p.is_file() and not p.is_symlink():files[str(p.relative_to(ROOT))]=digest(p)
    return {'files':files,'symlinks':links}

def main():
    assert len(RATIONALES)==60
    assert not (OUT/'medical_screening_completed_v1.json').exists(),'Medical completion already exists; do not overwrite audit.'
    pre=json.loads((OUT/'medical_screen_pre_read_seal_audit_v1.json').read_text())
    assert pre['substantive_annotations_sealed_before_reference']
    for name,expected in pre['protected_files'].items():assert digest(ROOT/name)['sha256']==expected,name
    # New Custodian additions are preexisting inputs for this continuation,
    # not changes made by Reviewer B. Contents outside the allowlist are hash-only.
    before=inventory()
    dump('medical_screen_integrity_baseline_v1.json',{'captured_at_utc':now(),**before,
        'scope':'All repository files outside reviewer_b_results_v1; new Custodian reference preparation is preexisting for this continuation.',
        'read_mode':'Opaque streaming hash only; no prohibited contents parsed or emitted.'})
    packet_raw=PACKET.read_bytes();rows=[json.loads(l) for l in packet_raw.splitlines()]
    assert len(rows)==60 and all(set(r)=={'review_id_b','query'} for r in rows)
    assert len({r['review_id_b'] for r in rows})==60
    ref_raw=REFERENCE.read_bytes();ref=json.loads(ref_raw)
    assert set(ref)=={'reference_id','query'} and all(isinstance(v,str) for v in ref.values())
    assert sha_bytes(ref_raw)=='3d1b8b0368fc0eebc1f8c08dd66daf123f0ceb94deaf40e6ed27f1c2fa4b9006'
    assert sha_bytes(packet_raw)=='dace0b18b2bc5975e2c63e223536e9d4316735241f3d4b3a5461e7347e132342'
    flags_path=OUT/'reviewer_b_contamination_flags_v1.jsonl'
    old_flags=[json.loads(l) for l in flags_path.read_text().splitlines()]
    assert [r['review_id_b'] for r in old_flags]==[r['review_id_b'] for r in rows]
    assert all(r['historical_31_text_screen']=='COMPLETE' and r['new_candidate_text_screen']=='COMPLETE' for r in old_flags)
    started=now();medical=[]
    for i,(row,rationale) in enumerate(zip(rows,RATIONALES),1):
        exact=row['query']==ref['query'];normalized=norm(row['query'])==norm(ref['query'])
        # Semantic false judgments are individually justified above, not inferred
        # from a failed keyword match or similarity threshold.
        assert not exact and not normalized
        medical.append({'review_id_b':row['review_id_b'],'reference_id':ref['reference_id'],
            'candidate_query_sha256':sha_bytes(row['query'].encode()),
            'reference_query_sha256':sha_bytes(ref['query'].encode()),
            'review_status':'COMPLETE','exact_duplicate':False,'normalized_identity':False,
            'trivial_paraphrase':False,'strong_scenario_or_proposition_near_duplicate':False,
            'generic_planning_template_overlap':i in TEMPLATE_OVERLAP,
            'judgment':'NO_DUPLICATE_IDENTIFIED','rationale':rationale,
            'basis':'Independent comparison of the two query texts only; actor, activity, purpose, stated facts and explicit asks considered.',
            'proposition_boundary':'Only propositions explicit in query text; no medical gold, legal answer, inferred risk level or hidden scope reconstructed.',
            'reference_gold_or_system_output_seen':False,
            'substantive_annotation_used_to_infer_reference_scope':False,
            'annotation_revision':False,'adjudication':False})
    mutable=['reviewer_b_contamination_flags_v1.jsonl','phase5c4b_review_summary_v1.md',
        'phase5c4b_agreement_ready_summary_v1.json','phase5c4b_validation_v1.json',
        'phase5c4b_access_manifest_v1.json','phase5c4b_console_v1.txt',
        'reviewer_b_manifest_v1.json','generated_artifact_hashes_v1.json']
    snapshots={}
    for name in mutable:
        p=OUT/name;raw=p.read_bytes();backup=OUT/('pre_medical_'+name)
        assert not backup.exists(),backup.name
        backup.write_bytes(raw);backup.chmod(0o600)
        snapshots[name]={'backup':backup.name,**digest(p)}
    # Only screening status is changed; preserve every earlier text-screen flag.
    for result,med in zip(old_flags,medical):
        result['pre_medical_status']=result['status']
        result['status']='COMPLETE';result['medical_chatbot_text_screen']='COMPLETE'
        result['medical_reference_id']=ref['reference_id']
        result['medical_texts_compared']=1
        result['medical_comparison']=med
        result['missing_source_action']=None
        result['medical_screen_detail_file']='reviewer_b_medical_contamination_screen_v1.jsonl'
        result['screening_completed_at_utc']=now()
    flags_path.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in old_flags))
    (OUT/'reviewer_b_medical_contamination_screen_v1.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in medical))
    after=inventory()
    changed=sorted(name for name,v in before['files'].items() if after['files'].get(name)!=v)
    added=sorted(set(after['files'])-set(before['files']))
    intact=not changed and not added and before['symlinks']==after['symlinks']
    protected={name:{'before':expected,'after':digest(ROOT/name)['sha256']} for name,expected in pre['protected_files'].items()}
    sealed_intact=all(v['before']==v['after'] for v in protected.values())
    assert intact and sealed_intact,'Integrity failed; cannot report PASS'
    integrity={'status':'PASS','checked_at_utc':now(),'baseline_file':'medical_screen_integrity_baseline_v1.json',
        'baseline_sha256':digest(OUT/'medical_screen_integrity_baseline_v1.json')['sha256'],
        'outside_namespace_file_count':len(before['files']),'changed_outside_namespace':changed,
        'added_outside_namespace':added,'symlink_targets_unchanged':True,
        'protected_substantive_files':protected,'substantive_bytes_unchanged':True,
        'input_reference_sha256':sha_bytes(ref_raw),'input_packet_sha256':sha_bytes(packet_raw),
        'custodian_artifacts_opened_for_semantic_read':False}
    dump('medical_screen_integrity_before_after_v1.json',integrity)
    audit={'schema':'medical-contamination-screen-completion-v1','started_at_utc':started,'completed_at_utc':now(),
        'status':'PASS','reviewer_role':'INDEPENDENT_ANNOTATOR_B',
        'reviewer_type':'MODEL_BASED_INDEPENDENT_ANNOTATOR','independent_context':True,
        'reference_file':str(REFERENCE.relative_to(ROOT)),'reference_sha256':sha_bytes(ref_raw),
        'reference_visible_fields':['reference_id','query'],'reference_count':1,
        'reference_schema_validation':'PASS','custodian_audit_PASS_basis':'Explicit user confirmation; no quarantined source or Custodian preparation/audit content opened.',
        'substantive_annotations_sealed_before_medical_reference':True,
        'pre_read_seal_audit':'medical_screen_pre_read_seal_audit_v1.json',
        'annotation_B_sha256_before':pre['final_annotation_sha256'],
        'annotation_B_sha256_after':digest(OUT/'annotation_B_v1.jsonl')['sha256'],
        'original_substantive_lock_time':pre['sealed_at_utc'],
        'substantive_annotations_modified':False,'admission_recommendations_modified':False,
        'historical_31_screening':{'completed':60,'total':60,'previous_results_preserved':True},
        'candidate_internal_screening':{'completed':60,'total':60,'previous_results_preserved':True},
        'medical_screening':{'completed':60,'total':60,'exact_duplicates':0,'trivial_paraphrases':0,
            'strong_scenario_or_proposition_near_duplicates':0,'generic_template_overlap_count':len(TEMPLATE_OVERLAP)},
        'full_contamination_screening':{'completed':60,'total':60,'status':'COMPLETE'},
        'semantic_limit':'General AI planning wording alone is not a strong near-duplicate. No unstated medical risk class, duties or gold proposition bundle inferred.',
        'semantic_results_file':'reviewer_b_medical_contamination_screen_v1.jsonl',
        'annotation_A_read':False,'A_substantive_metadata_seen':False,'old_packet_read':False,
        'system_outputs_read':False,'network_api_calls':0,'production_evaluator_calls':0,
        'retrieval_reranking_inference':0,'D6':'EMPIRICAL_UNVERIFIED','A_B_comparison':False,
        'adjudication':False,'dataset_frozen':False,'independent_human_legal_review_complete':False,
        'holdout_storage_isolation':'NOT_YET_ENFORCED','prior_output_snapshots':snapshots,
        'integrity':'PASS','ready_for_phase5c4c_comparison':True,'ready_for_final_dataset_freeze':False,
        'read_audit':{'new_substantive_input_only':str(REFERENCE.relative_to(ROOT)),
            'candidate_text_source':str(PACKET.relative_to(ROOT)),
            'private_B_result_reads':[n for n in mutable if n!='generated_artifact_hashes_v1.json']+['medical_screen_pre_read_seal_audit_v1.json'],
            'protected_B_annotations':'hash-only; no write',
            'outside_namespace_hash_reads':'medical_screen_integrity_baseline_v1.json / files',
            'new_input_path_discovery':'File paths/sizes only; no Custodian file content exposed.'}}
    dump('medical_screening_completed_v1.json',audit)

    ready=json.loads((OUT/'phase5c4b_agreement_ready_summary_v1.json').read_text())
    ready['phase5c4b_retry_status']='PASS'
    ready['status_scope']='Independent B annotations sealed; historical, candidate-internal and newly sanitized medical query-only contamination screening complete. No A/B comparison or adjudication.'
    ready['full_contamination_screen_complete']=True;ready['contamination_status']='COMPLETE'
    ready['completed_screen_sources']=['new candidate query text','31 historical query-only inputs','newly sanitized exploratory medical query-only reference']
    ready['pending_screen_source']=None
    ready['all_admission_recommendations_provisional_pending_full_uniqueness_review']=False
    ready['admission_recommendations_remain_unadjudicated']=True
    ready['existing_candidate_similarity_flags_remain_for_trusted_review']=True
    ready['substantive_annotation_file_unchanged']=True
    ready['embedded_pending_metadata_in_sealed_annotation']='Historical pre-medical snapshot only. Current status is in reviewer_b_contamination_flags_v1.jsonl and this summary; sealed annotation bytes preserved.'
    ready['medical_completion_audit']='medical_screening_completed_v1.json'
    ready['counts']['medical_chatbot_contamination_screen']=60;ready['counts']['full_contamination_screen']=60
    ready['counts']['medical_duplicate_flags']={'exact_duplicate':0,'trivial_paraphrase':0,'strong_scenario_or_proposition_near_duplicate':0}
    ready['required_next_trusted_actions']=['Perform Phase 5C.4-C A/B comparison in an authorized trusted context',
        'Review the existing candidate-to-candidate similarity flags without assuming a split or adjudicated disposition',
        'Resolve human legal review and legal adjudication requirements before any final freeze']
    dump('phase5c4b_agreement_ready_summary_v1.json',ready)

    validation=json.loads((OUT/'phase5c4b_validation_v1.json').read_text())
    validation['status_scope']=ready['status_scope']
    validation['contamination_screening']='COMPLETE'
    validation['missing_reference_user_authorized_to_defer']=False
    validation['prior_missing_reference_deferral_resolved']=True
    validation['medical_contamination_screening']='PASS_60_OF_60'
    validation['substantive_annotations_sealed_before_medical_reference']=True
    validation['substantive_annotations_unchanged_during_medical_screen']=True
    validation['medical_screen_integrity']='PASS'
    validation['counts']=ready['counts']
    validation['PASS_does_not_mean']=[x for x in validation['PASS_does_not_mean'] if x!='full contamination screening complete']
    validation['medical_completion_audit']='medical_screening_completed_v1.json'
    dump('phase5c4b_validation_v1.json',validation)

    access=json.loads((OUT/'phase5c4b_access_manifest_v1.json').read_text())
    access['explicit_substantive_or_projected_input_reads'].append({'path':str(REFERENCE.relative_to(ROOT)),
        'purpose':'User-authorized newly sanitized medical query-only reference, read after verification of B annotation seals.',**digest(REFERENCE)})
    access['authorizations'].append({'event':'sanitized_medical_reference_completion','source':'User continuation request',
        'effect':'Compare all 60 candidate texts against newly audited reference only; update contamination results/public-safe summaries; preserve substantive B annotations.'})
    access['medical_contamination_completion']={'status':'COMPLETE','candidate_count':60,
        'pre_read_seal_audit':'medical_screen_pre_read_seal_audit_v1.json','completion_audit':'medical_screening_completed_v1.json',
        'integrity_audit':'medical_screen_integrity_before_after_v1.json',
        'all_continuation_hash_reads':'medical_screen_integrity_baseline_v1.json / files',
        'quarantined_packet_or_custodian_audit_content_read':False,
        'annotation_A_read':False,'substantive_annotation_write_count':0}
    dump('phase5c4b_access_manifest_v1.json',access)

    manifest=json.loads((OUT/'reviewer_b_manifest_v1.json').read_text())
    manifest['contamination_status']='COMPLETE';manifest['counts']=ready['counts']
    manifest['pending_reference_requirements']=[]
    manifest['medical_completion_audit']='medical_screening_completed_v1.json'
    manifest['medical_reference']=str(REFERENCE.relative_to(ROOT))
    manifest['medical_reference_sha256']=sha_bytes(ref_raw)
    manifest['substantive_annotations_sealed_before_medical_reference']=True
    manifest['substantive_annotations_modified_during_medical_screen']=False
    manifest['sealed_annotation_embedded_screening_metadata_is_historical']=True
    assert manifest['final_annotation_sha256']==pre['final_annotation_sha256']
    dump('reviewer_b_manifest_v1.json',manifest)

    summary='''# Phase 5C.4-B — final independent B review

PASS. Substantive annotations: 60/60. Historical 31-query screening: 60/60. Medical diagnostic screening: 60/60. Full contamination screening: 60/60 COMPLETE.

Substantive annotations sealed before medical reference: YES. The final annotation file matched its preexisting manifest/hash seal before the new reference was read, and its bytes are unchanged after screening. No scope, aspect, support, applicability, answerability, dimension or admission judgment was changed.

The newly authorized medical reference contains only `reference_id` and `query`. Custodian audit PASS was confirmed by the user; Reviewer B did not open the quarantined source or Custodian preparation/audit contents. Only the new reference was used for this continuation.

Independent comparison of all 60 query texts found 0 exact duplicates, 0 trivial paraphrases and 0 strong scenario-or-proposition near-duplicates of the medical reference. General AI planning phrasing alone was not treated as a strong duplicate; no unstated medical facts, risk class, legal duties or gold bundle was inferred. Private per-candidate rationales and hashes are in `reviewer_b_medical_contamination_screen_v1.jsonl`.

Earlier historical and candidate-internal screening results are preserved, including 7 candidate-to-candidate similarity pairs for trusted later review. Screening completion does not adjudicate those flags or finalize admission. The sealed annotation file retains its historical pending-screen metadata; current screening status is recorded in the separate contamination results and manifests to preserve the annotation seal.

The independent annotation still contains 155 aspects: 139 substantive-supported, 3 qualified-partial, 13 unresolved-disclosure. Answerability counts remain 44 fully_answerable, 9 partially_answerable, 7 insufficient_evidence. Admission recommendations remain 58 RETAIN, 1 RESERVE, 1 NEEDS_ADJUDICATION, without legal adjudication or final admission approval.

Independent context review complete: YES
Independent human legal review complete: NO
Annotation A read: NO
System outputs inspected: NO
D6: EMPIRICAL_UNVERIFIED
Network/API, production/evaluator and retrieval/reranking inference: 0

Integrity: PASS. All protected substantive B files and all files outside the retry results namespace are unchanged during this continuation. Earlier output versions were preserved as private snapshots. No exact query text appears in current public-safe reports or the result console; reading text through session tool output remains expressly authorized by the user.

HOLDOUT storage isolation: NOT_YET_ENFORCED
Dataset frozen: NO
Agentic v2 implementation: NOT STARTED; future implementation in this context: FORBIDDEN

B annotations complete and ready for trusted A/B comparison.
Ready for Phase 5C.4-C A/B comparison: YES
Ready for final dataset freeze: NO

No A/B comparison, adjudication or dataset freeze was performed. Human legal review and adjudication requirements remain unresolved.
'''
    (OUT/'phase5c4b_review_summary_v1.md').write_text(summary)
    console='''Phase 5C.4-B final status:
PASS

Substantive annotations sealed before medical reference:
YES

Historical 31-query contamination screening:
60/60

Medical diagnostic contamination screening:
60/60

Full contamination screening:
60/60 COMPLETE

Annotation A read:
NO

D6:
EMPIRICAL_UNVERIFIED

Independent human legal review complete:
NO

HOLDOUT storage isolation:
NOT_YET_ENFORCED

Ready for Phase 5C.4-C A/B comparison:
YES

Ready for final dataset freeze:
NO

STOP
'''
    (OUT/'phase5c4b_console_v1.txt').write_text(console)
    public=['phase5c4b_review_summary_v1.md','phase5c4b_agreement_ready_summary_v1.json',
        'phase5c4b_access_manifest_v1.json','phase5c4b_validation_v1.json','phase5c4b_console_v1.txt',
        'medical_screen_integrity_before_after_v1.json']
    queries=[r['query'] for r in rows]+[ref['query']]
    for name in public:assert not any(q in (OUT/name).read_text() for q in queries),name
    final_flags=[json.loads(l) for l in flags_path.read_text().splitlines()]
    backup_flags=[json.loads(l) for l in (OUT/'pre_medical_reviewer_b_contamination_flags_v1.jsonl').read_text().splitlines()]
    assert len(final_flags)==60
    for new,old in zip(final_flags,backup_flags):
        assert new['flags']==old['flags'] and new['historical_overlap_review']==old['historical_overlap_review']
        assert new['historical_31_text_screen']==new['medical_chatbot_text_screen']==new['new_candidate_text_screen']=='COMPLETE'
    for name,expected in pre['protected_files'].items():assert digest(ROOT/name)['sha256']==expected
    dump('medical_screen_completion_validation_v1.json',{'status':'PASS','candidate_comparisons':60,
        'reference_records':1,'exact_duplicate_count':0,'trivial_paraphrase_count':0,'strong_near_duplicate_count':0,
        'previous_flags_and_historical_results_unchanged':True,'substantive_protected_hashes_unchanged':True,
        'reference_and_packet_hashes_verified':True,'public_safe_files_query_free':public,
        'full_contamination_screening':'60/60 COMPLETE','independent_human_legal_review_complete':False,
        'validation_scope':'Artifact consistency and reference-text screening only, no production/evaluator or legal adjudication.'})
    generated={str(p.relative_to(ROOT)):digest(p) for p in OUT.iterdir() if p.is_file() and p.name!='generated_artifact_hashes_v1.json'}
    dump('generated_artifact_hashes_v1.json',{'created_at_utc':now(),'files':generated,
        'self_excluded':True,'read_purpose':'Final hash coverage including pre-medical snapshots and completion/access audits'})
    for p in OUT.iterdir():
        if p.is_file():p.chmod(0o600)
    print(console,end='')

if __name__=='__main__':main()
