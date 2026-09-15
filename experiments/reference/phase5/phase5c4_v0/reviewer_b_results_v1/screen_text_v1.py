"""Private B-authored query-text screening; no old packet is opened."""
import json,hashlib,datetime,unicodedata,re
from pathlib import Path
OUT=Path(__file__).resolve().parent
def sha(b):return hashlib.sha256(b).hexdigest()
def norm(s):return ' '.join(re.findall(r'\w+',unicodedata.normalize('NFKC',s).casefold()))

# Independently compared text only, after substantive annotation lock.
# These are similarity flags for trusted later review, not split/cluster assignments.
PAIRS=[
 (7,14,'strong_near_duplicate','moderate','Cùng nhóm khai thác cơ sở dữ liệu quốc gia để huấn luyện/thử mô hình. Phần điều kiện sử dụng chung đáng kể; một câu thêm công bố khoa học, câu kia thêm mức phí chưa có. Không phải paraphrase toàn bộ.'),
 (11,22,'same_scenario_proposition_bundle','moderate','Cùng cập nhật hệ thống cao đã đánh giá; thay đổi đáng kể và sửa lỗi thường lệ là hai nhánh điều kiện đối lập của yêu cầu rà soát/đánh giá lại. Phải giữ khác biệt điều kiện, cần xem xét chung nguy cơ lặp mẫu.'),
 (12,35,'strong_near_duplicate','moderate','Cùng nhà cung cấp nước ngoài có AI cao và điều kiện hiện diện/đầu mối. Một câu có điều kiện không chứng nhận và thêm bàn giao; câu kia thiếu điều kiện chứng nhận, nên không đồng nhất đáp án.'),
 (13,51,'same_scenario_proposition_bundle','high','Cùng ranh giới hoạt động quốc phòng theo điều kiện chỉ phục vụ; biến thể mục đích duy nhất và mục đích hỗn hợp đảo trạng thái áp dụng. Không phải exact duplicate, nhưng chia sẻ mẫu pháp lý đối lập.'),
 (17,41,'strong_near_duplicate','moderate','Cùng tác phẩm mô phỏng giọng/hình người thật và bảo toàn thông tin/nhãn khi công khai. Bảo tàng áp dụng Khung tự nguyện khác chuỗi xưởng–phát hành; không coi các nghĩa vụ bổ sung giống nhau.'),
 (34,59,'strong_near_duplicate','high','Tính không bắt buộc của mẫu/thông tin xin hỗ trợ phi tài chính là câu hỏi cốt lõi trùng nhau; câu 59 thêm nội dung thông tin và chế độ báo cáo. Câu 34 là kiểm tra hẹp nằm phần lớn trong nhu cầu câu 59.'),
 (40,50,'strong_near_duplicate','moderate','Đều là đơn vị quản lý dữ liệu cung cấp môi trường khai thác AI; có phần kiểm soát truy cập/quyền dữ liệu chung. API và công bố của dữ liệu Nhà nước khác môi trường tại chỗ và rủi ro tái nhận dạng; cần rà lại mức gần trùng, chưa kết luận đồng nhất.')
]

# Explicitly reviewed plausible historical overlaps, preserving material differences.
HISTORY={
 3:([1],'Phân loại theo trường hợp loại trừ văn phòng, khác việc chỉ liệt kê ba mức.'),
 5:([2],'Câu lịch sử hỏi chủ thể ban hành danh mục; câu mới phân biệt nhiệm vụ tổng hợp/trình với doanh nghiệp.'),
 8:([12,13,14,15],'Câu mới có cấp độ 1, doanh nghiệp nhỏ, một tỉnh và hồ sơ rút gọn/thời hạn/hỗ trợ; lịch sử hỏi chung cơ chế, thẩm quyền hoặc hồ sơ thông thường.'),
 10:([3,4,5,6],'Trọng tâm mới là tăng mức đã hoàn tất rà soát, thời hạn thông báo lại và áp dụng biện pháp ngay.'),
 11:([4,5],'Nghĩa vụ quản lý chung có giao nhau, nhưng câu mới hỏi chuyển phiên bản và điều kiện đánh giá lại mô hình/dữ liệu đối tác.'),
 12:([4,5,6],'Câu mới phối hợp vai trò nước ngoài, không chứng nhận bắt buộc và bàn giao nội địa, khác câu liệt kê quản lý chung.'),
 17:([8,9,28],'Có phần nhãn/nguyên tắc chung; câu mới đưa tác phẩm bảo tàng có người thật ra công chúng và chủ động Khung, không cùng toàn bộ nhu cầu bằng chứng.'),
 18:([18,19],'Lịch sử hỏi gia hạn thử nghiệm và xử lý kết quả; câu mới gia hạn vận hành chuyển tiếp sau hoàn thành, mốc và điều kiện khác.'),
 19:([11],'Câu mới lịch báo cáo thiệt hại tài sản không khẩn cấp và ý nghĩa không nhận lỗi; lịch sử hỏi hành động nhà cung cấp khi phát hiện sự cố nói chung.'),
 23:([7,8,9],'Câu mới phân công đánh dấu máy đọc trong hệ thống miễn phí; khác câu minh bạch/nhãn chung.'),
 25:([14],'Trường hợp đủ người tham gia nhưng không dùng kết quả thực tế cần phân biệt điều kiện cấp độ, khác liệt kê tiêu chí chung.'),
 26:([12,28],'Câu mới lab khép kín bị loại khỏi sandbox và nghĩa vụ liêm chính; không cùng phạm vi cơ chế hỗ trợ hoặc đạo đức chung.'),
 28:([28,29,30,31],'Giao diện dịch vụ công cho nhóm dễ tổn thương, kết nối kém và đầu mối phản ánh khác các câu nguyên tắc/giám sát tổng quát.'),
 31:([3],'Thủ tục gửi tự động, xác nhận/mã và giới hạn tài liệu khác thời điểm lập hồ sơ.'),
 33:([26,27,30,31],'Đánh giá bổ sung khi thay nguồn dữ liệu trước tiếp tục dùng và đào tạo cán bộ khác câu hỏi phạm vi/nội dung báo cáo chung.'),
 36:([28],'Kế hoạch môi trường vòng đời và hạ tầng mạng lưới có yêu cầu cụ thể, không chỉ liệt kê nguyên tắc đạo đức.'),
 37:([11],'Nhà phát triển kỹ thuật là điều kiện chủ thể trung tâm; không thay bằng nhà cung cấp của câu lịch sử.'),
 38:([6],'Câu mới trọng tâm cơ chế bồi thường dù vận hành đúng và phối hợp trước tổn thất; quản lý vận hành chỉ là một phần giao nhau.'),
 40:([20,22,23,24],'Câu mới công bố của đơn vị vận hành dữ liệu Nhà nước qua API và quyền sở hữu, khác nguyên tắc/loại dữ liệu/xây dựng cập nhật chung.'),
 41:([8,9],'Câu mới chuỗi tạo phim/phát hành và phân công cung cấp thông tin; không chỉ nguyên tắc gắn nhãn chung.'),
 42:([4,5],'Câu mới thời hạn lưu sau dừng và tài liệu thanh tra, gồm khoảng trống định lượng; khác quản lý hệ thống đang hoạt động.'),
 44:([28,30,31],'Câu mới phạm vi nghĩa vụ an ninh của nhà phát triển dịch vụ công, tập trung đầu độc dữ liệu/mô hình.'),
 45:([4,5],'Câu mới kết quả đánh giá nước ngoài chỉ được thừa nhận một phần, khác quản lý cao nói chung.'),
 46:([26,27,28,29,30,31],'Câu mới quản trị xếp hạng trợ cấp trước quyết định hành chính, phối hợp báo cáo, công bằng và phản ánh. Chia sẻ điều luật nhưng không exact/trivial hay cùng toàn bộ câu hỏi.'),
 48:([3,4,5,7,10],'Câu mới triển khai đầu tiên AI cao đánh giá học sinh, điều kiện chứng nhận và người học; không chỉ lặp thời điểm hồ sơ hay thông báo tương tác.'),
 50:([20,24],'Câu mới phân công hai bên và nguy cơ tái nhận dạng trong môi trường huấn luyện tại chỗ, khác nguyên tắc kết nối/khai thác chung.'),
 57:([28],'Câu mới giới hạn phạm vi bắt buộc với cửa hàng tư nhân; lịch sử hỏi nội dung nguyên tắc.'),
 58:([3,7,29],'Câu mới quyền tiếp cận tài liệu bên thứ ba, tài liệu quốc tế và thỏa thuận kỹ thuật; khác câu thời điểm hồ sơ/minh bạch/giải trình chung.'),
 60:([28],'Phương án chia sẻ mô hình ngôn ngữ thiểu số và hỗ trợ phi tài chính có căn cứ riêng ngoài câu đạo đức tổng quát.')
}

def main():
    rows=[json.loads(l) for l in (OUT/'annotation_B_v1.jsonl').read_text().splitlines()]
    history=json.loads((OUT/'historical_31_query_text_v1.json').read_text())
    assert len(rows)==60 and len(history)==31
    initial=(OUT/'annotation_B_v1.jsonl').read_bytes()
    lock=json.loads((OUT/'substantive_lock_v1.json').read_text())
    assert sha(initial)==lock['annotation_sha256'],'Do not rewrite an already post-screened record'
    (OUT/'annotation_B_substantive_locked_v1.jsonl').write_bytes(initial)
    events=[]; exact_count=0
    for i,r in enumerate(rows,1):
        flags=[]
        for a,b,t,c,note in PAIRS:
            if i in [a,b]:
                other=b if i==a else a
                flags.append({'source':'new_candidate_query_text','other_review_id_b':rows[other-1]['review_id_b'],
                    'flag':t,'confidence':c,'rationale':note,
                    'disposition':'TRUSTED_SIMILARITY_REVIEW_REQUIRED_NO_SPLIT_INFERRED'})
        for j,s in enumerate(rows,1):
            if i!=j and (r['query']==s['query'] or norm(r['query'])==norm(s['query'])):
                flags.append({'source':'new_candidate_query_text','other_review_id_b':s['review_id_b'],
                    'flag':'exact_duplicate' if r['query']==s['query'] else 'trivial_paraphrase','confidence':'high',
                    'rationale':'Deterministic exact or case/punctuation/whitespace normalized identity.'})
                exact_count+=1
        for h in history:
            if r['query']==h['query'] or norm(r['query'])==norm(h['query']):
                flags.append({'source':'historical_31_query_text','historical_ref_b':h['historical_ref_b'],
                    'flag':'exact_duplicate' if r['query']==h['query'] else 'trivial_paraphrase','confidence':'high',
                    'rationale':'Deterministic exact or normalized identity.'})
                exact_count+=1
        historical=[]
        if i in HISTORY:
            nums,note=HISTORY[i]
            historical=[{'historical_refs_b':[f'historical_{n:02d}' for n in nums],
                'disposition':'TOPICAL_OR_PARTIAL_PROPOSITION_OVERLAP_NOT_STRONG_DUPLICATE',
                'rationale':note}]
        events.append({'review_id_b':r['review_id_b'],'status':'PENDING_SANITIZED_REFERENCE',
            'new_candidate_text_screen':'COMPLETE','historical_31_text_screen':'COMPLETE',
            'medical_chatbot_text_screen':'PENDING_SANITIZED_REFERENCE',
            'new_texts_compared':59,'historical_texts_compared':31,
            'methods':['exact identity','Unicode/case/punctuation normalized identity','B semantic full-query comparison after substantive lock'],
            'flags':flags,'historical_overlap_review':historical,
            'historical_semantic_result':'No exact duplicate, trivial paraphrase or strong full-scope equivalent identified among the authorized 31 texts; source-sharing alone not treated as duplication.',
            'missing_source_action':'Wait for separately audited sanitized medical chatbot reference from Dataset Custodian. Old packet never opened.',
            'A_metadata_or_system_outcomes_used':False})
        old=r['admission_recommendation'].copy()
        r['admission_recommendation']['pre_text_screen_recommendation']=old
        r['admission_recommendation']['uniqueness_status']='PROVISIONAL_PENDING_SANITIZED_REFERENCE'
        r['admission_recommendation']['candidate_similarity_flag_count']=len(flags)
        r['admission_recommendation']['basis']=[x.replace('uniqueness_pending_text_screen','uniqueness_partial_text_screen') for x in old['basis']]
        if i==34:
            r['admission_recommendation']['label']='RESERVE'
            r['admission_recommendation']['rationale']=old['rationale']+' Sau so sánh text: phạm vi hẹp trùng trọng tâm tự nguyện dùng mẫu của '+rows[58]['review_id_b']+'; đề nghị dự phòng vì tính riêng biệt hạn chế, không vì kết quả hệ thống.'
        elif flags:
            r['admission_recommendation']['rationale']=old['rationale']+' Có cờ tương đồng cần trusted review; giữ khuyến nghị hiện tại vì các điều kiện hoặc nghĩa vụ bổ sung vẫn khác biệt trọng yếu. Không gán split hoặc cluster.'
        r['contamination_screening']={'status':'PENDING_SANITIZED_REFERENCE',
            'detail_file':'reviewer_b_contamination_flags_v1.jsonl','medical_reference_seen':False}
    (OUT/'reviewer_b_contamination_flags_v1.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in events))
    (OUT/'annotation_B_v1.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))
    (OUT/'text_screen_provenance_v1.json').write_text(json.dumps({
        'screened_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'substantive_lock_sha256':lock['annotation_sha256'],
        'original_substantive_copy':'annotation_B_substantive_locked_v1.jsonl',
        'substantive_scope_aspects_evidence_answerability_dimensions_changed':False,
        'only_post_screen_admission_and_contamination_metadata_added':True,
        'status':'PENDING_SANITIZED_REFERENCE','historical_source':'data/evaluation/generation/phase5/query_inputs_v0.json',
        'historical_source_fields':['query_id','query'],'historical_count':31,
        'candidate_pairs_compared':1770,'candidate_historical_pairs_compared':1860,
        'new_candidate_semantic_flag_pairs':len(PAIRS),'exact_or_normalized_duplicate_events':exact_count,
        'medical_reference_read':False,'old_packet_read':False,
        'authorization':'User explicitly requires newly sanitized and audited medical reference; missing source does not compromise independent substantive review.'},ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'candidate_texts_screened':60,'historical_reference_texts':31,'candidate_semantic_flag_pairs':len(PAIRS),'full_contamination_screen':'PENDING_SANITIZED_REFERENCE'}))

if __name__=='__main__':main()
