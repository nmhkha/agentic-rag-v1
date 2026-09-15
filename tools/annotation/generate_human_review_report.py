#!/usr/bin/env python3
"""Generate read-only human-review artifacts for flagged retrieval annotations."""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVAL = ROOT / "eval-sets/retrieval/retrieval_eval.jsonl"
CORPUS = ROOT / "data/versions/corpus-v0.1"
REPORT = ROOT / "annotation/retrieval/human_review_report.md"
SUMMARY = ROOT / "annotation/retrieval/human_review_summary.csv"
IDS = ["eval004", "eval005", "eval007", "eval014", "eval015", "eval025", "eval029", "eval030"]

COVERAGE_MAP = {
 "eval004": [["142-2026-ND-CP_dieu-15_khoan-1"], ["142-2026-ND-CP_dieu-15_khoan-2_diem-a"], ["142-2026-ND-CP_dieu-15_khoan-2_diem-b"], ["142-2026-ND-CP_dieu-15_khoan-2_diem-c"], ["142-2026-ND-CP_dieu-15_khoan-2_diem-d"], ["142-2026-ND-CP_dieu-15_khoan-2_diem-đ"]],
 "eval005": [
  ["134-2025-QH15_dieu-14_khoan-1_diem-a", "134-2025-QH15_dieu-14_khoan-1_diem-b", "134-2025-QH15_dieu-14_khoan-1_diem-c", "134-2025-QH15_dieu-14_khoan-1_diem-d", "134-2025-QH15_dieu-14_khoan-1_diem-đ", "134-2025-QH15_dieu-14_khoan-1_diem-e", "134-2025-QH15_dieu-14_khoan-1_diem-g"],
  ["134-2025-QH15_dieu-14_khoan-2_diem-a", "134-2025-QH15_dieu-14_khoan-2_diem-b", "134-2025-QH15_dieu-14_khoan-2_diem-c", "134-2025-QH15_dieu-14_khoan-2_diem-d", "134-2025-QH15_dieu-14_khoan-2_diem-đ", "134-2025-QH15_dieu-14_khoan-2_diem-e"],
  ["134-2025-QH15_dieu-14_khoan-3"], ["134-2025-QH15_dieu-14_khoan-4"], ["134-2025-QH15_dieu-14_khoan-5"], ["134-2025-QH15_dieu-14_khoan-6"]],
 "eval007": [["142-2026-ND-CP_dieu-18_khoan-3_diem-a", "142-2026-ND-CP_dieu-18_khoan-3_diem-b", "142-2026-ND-CP_dieu-18_khoan-3_diem-c"], ["142-2026-ND-CP_dieu-18_khoan-3_diem-d", "142-2026-ND-CP_dieu-18_khoan-3_diem-đ"], ["142-2026-ND-CP_dieu-18_khoan-5_diem-a", "142-2026-ND-CP_dieu-18_khoan-5_diem-b", "142-2026-ND-CP_dieu-18_khoan-5_diem-c", "142-2026-ND-CP_dieu-18_khoan-5_diem-d"]],
 "eval014": [["142-2026-ND-CP_dieu-24_khoan-2_diem-a", "142-2026-ND-CP_dieu-24_khoan-2_diem-b", "142-2026-ND-CP_dieu-24_khoan-2_diem-c", "142-2026-ND-CP_dieu-24_khoan-2_diem-d"], ["142-2026-ND-CP_dieu-24_khoan-3_diem-a", "142-2026-ND-CP_dieu-24_khoan-3_diem-b"], ["142-2026-ND-CP_dieu-24_khoan-2_diem-a", "142-2026-ND-CP_dieu-24_khoan-3_diem-a"]],
 "eval015": [["134-2025-QH15_dieu-21_khoan-3"], ["142-2026-ND-CP_dieu-25_khoan-1_diem-c"]],
 "eval025": [["142-2026-ND-CP_dieu-20_khoan-1_diem-a"], ["142-2026-ND-CP_dieu-20_khoan-1_diem-b"], ["142-2026-ND-CP_dieu-20_khoan-7_diem-a", "142-2026-ND-CP_dieu-20_khoan-7_diem-b", "142-2026-ND-CP_dieu-20_khoan-7_diem-c", "142-2026-ND-CP_dieu-20_khoan-7_diem-d"], ["142-2026-ND-CP_dieu-20_khoan-2"]],
 "eval029": [["05-2026-TT-BKHCN_dieu-3_khoan-1_diem-c"], ["05-2026-TT-BKHCN_dieu-3_khoan-2_diem-a"]],
 "eval030": [["134-2025-QH15_dieu-4_khoan-2"], ["134-2025-QH15_dieu-4_khoan-2", "05-2026-TT-BKHCN_dieu-3_khoan-1_diem-c"], ["134-2025-QH15_dieu-4_khoan-2"]],
}

REVIEW = {
 "eval004": {
  "flag": "Có 6 gold chunks; cần xác nhận khoản mở đầu và năm điểm có cùng cần thiết hay không.",
  "action": "KEEP", "confidence": "high", "ambiguity": "Thấp. Cụm “duy trì những biện pháp quản lý” khớp hệ thống quản lý rủi ro và danh sách năm biện pháp của nhà cung cấp.",
  "coverage": ["Nghĩa vụ thiết lập và duy trì hệ thống quản lý rủi ro.", "Nhận diện, đánh giá rủi ro.", "Quản trị chất lượng dữ liệu.", "Giám sát và can thiệp của con người.", "Biện pháp kỹ thuật/quản lý để kiểm soát rủi ro.", "Rà soát, cập nhật khi hệ thống thay đổi."],
  "missing": "Không.", "unnecessary": "Không. Khoản 1 là mệnh đề nghĩa vụ chính; năm điểm khoản 2 là toàn bộ nội dung cấu thành hệ thống quản lý rủi ro.",
  "reason": "Cả 6 chunks tạo thành một quy định hoàn chỉnh: khoản 1 xác lập nghĩa vụ, năm điểm của khoản 2 liệt kê các biện pháp.",
  "assess": {"142-2026-ND-CP_dieu-15_khoan-1": "SUPPORTING"}},
 "eval005": {
  "flag": "Gold hiện có 17 chunks và query không xác định chủ thể hay phạm vi của “việc quản lý”.",
  "action": "SPLIT_QUERY", "confidence": "high",
  "ambiguity": "Cao. Có thể hỏi toàn bộ chế độ quản lý, riêng nhà cung cấp, riêng bên triển khai, hoặc cả người sử dụng và quy định bổ trợ.",
  "coverage": ["Bảy nghĩa vụ của nhà cung cấp.", "Sáu nghĩa vụ của bên triển khai.", "Nghĩa vụ của người sử dụng.", "Giới hạn của giải trình.", "Khuyến khích bảo hiểm/bảo đảm nghĩa vụ.", "Yêu cầu riêng với nhà cung cấp nước ngoài."],
  "missing": "Không nếu hiểu query là toàn bộ Điều 14; chính độ rộng làm gold phình lớn.",
  "unnecessary": "Khoản 5 và khoản 6 là QUESTIONABLE đối với cách hiểu “quản lý nói chung”; khoản 4 là quy định hỗ trợ. Nếu tách theo chủ thể, chỉ giữ các chunks thuộc chủ thể tương ứng.",
  "reason": "Nên tách tối thiểu thành: “Nhà cung cấp hệ thống AI rủi ro cao có những nghĩa vụ gì?” và “Bên triển khai hệ thống AI rủi ro cao có những nghĩa vụ gì?”. Có thể tạo query riêng về người sử dụng nếu cần đánh giá vai trò đó.",
  "assess": {"134-2025-QH15_dieu-14_khoan-4": "SUPPORTING", "134-2025-QH15_dieu-14_khoan-5": "QUESTIONABLE", "134-2025-QH15_dieu-14_khoan-6": "QUESTIONABLE"}},
 "eval007": {
  "flag": "Có 9 chunks, cần phân biệt yêu cầu chung và cách thức triển khai nhãn/thông báo.",
  "action": "KEEP", "confidence": "high",
  "ambiguity": "Thấp. Từ “như thế nào” hợp lý bao gồm cả tiêu chuẩn thể hiện và các hình thức thể hiện được lựa chọn.",
  "coverage": ["Nhãn/thông báo phải rõ ràng, đúng thời điểm và không che giấu.", "Phải phù hợp loại nội dung và không cản trở đáng kể việc sử dụng.", "Bốn hình thức thể hiện có thể lựa chọn."],
  "missing": "Không đối với câu hỏi về cách thức. Gold không cố đưa điều kiện phát sinh nghĩa vụ, ngoại lệ hay trường hợp tác phẩm sáng tạo vào.",
  "unnecessary": "Không. Năm chunks khoản 3 là general rule; bốn chunks khoản 5 là implementation forms, đều trực tiếp trả lời “như thế nào”.",
  "reason": "Giữ nguyên; 9 chunks là hai danh sách bổ sung nhau, không phải các trường hợp ngoại lệ bị gom quá rộng.", "assess": {}},
 "eval014": {
  "flag": "Gold trộn hồ sơ thông thường bốn tài liệu và hồ sơ rút gọn hai tài liệu.",
  "action": "REWRITE_QUERY", "confidence": "high",
  "ambiguity": "Cao nhưng không nằm ở tổ chức so với cá nhân: hai chủ thể dùng cùng thành phần, chỉ khác mẫu đơn AI03a/AI03b. Khác biệt thực sự là hồ sơ thông thường và hồ sơ rút gọn dành cho một số chủ thể thử nghiệm cấp độ 1.",
  "coverage": ["Bốn thành phần của hồ sơ thông thường.", "Hai thành phần của hồ sơ rút gọn.", "Mẫu đơn tương ứng tổ chức/cá nhân trong mỗi chế độ."],
  "missing": "Không, nhưng query không cho biết cần áp dụng chế độ nào.",
  "unnecessary": "Không thể loại an toàn khi wording hiện tại vẫn hỏi chung. Sau khi rewrite, một trong hai nhóm chunks sẽ trở thành không cần thiết.",
  "reason": "Nên đổi thành một trong hai câu rõ phạm vi: “Hồ sơ thông thường đăng ký tham gia thử nghiệm có kiểm soát gồm những tài liệu nào?” hoặc “Hồ sơ rút gọn cho chủ thể đủ điều kiện thử nghiệm cấp độ 1 gồm những tài liệu nào?”.", "assess": {}},
 "eval015": {
  "flag": "Gold lấy hai Article thuộc Luật và Nghị định; cần xác định quan hệ nguyên tắc–chi tiết.",
  "action": "KEEP", "confidence": "high",
  "ambiguity": "Thấp. Hai căn cứ quy định các nhóm điều kiện khác nhau nhưng bổ sung trực tiếp cho cùng hành vi tạm dừng/chấm dứt.",
  "coverage": ["Căn cứ chung: rủi ro ảnh hưởng an toàn, an ninh hoặc quyền/lợi ích hợp pháp.", "Căn cứ chi tiết: vi phạm giới hạn thử nghiệm hoặc không khắc phục sự cố theo yêu cầu."],
  "missing": "Không.", "unnecessary": "Không. Điều 21 Luật là PRIMARY; Điều 25 Nghị định là SUPPORTING nhưng vẫn trực tiếp bổ sung điều kiện cụ thể, không chỉ liên quan chung.",
  "reason": "Giữ cả hai Article để không mất căn cứ rủi ro ở Luật hoặc các trường hợp vi phạm cụ thể ở Nghị định.", "assess": {},
  "article_roles": {"134-2025-QH15_dieu-21": "PRIMARY", "142-2026-ND-CP_dieu-25": "SUPPORTING"}},
 "eval025": {
  "flag": "Có 7 chunks cho câu hỏi chỉ hỏi điều kiện kích hoạt đánh giá tác động.",
  "action": "KEEP", "confidence": "medium",
  "ambiguity": "Trung bình. Cần phân biệt đánh giá ban đầu với đánh giá bổ sung; wording “trong trường hợp nào” đủ rộng để bao gồm cả hai.",
  "coverage": ["Hệ thống rủi ro cao.", "Hệ thống thuộc khoản 7 có đầu ra dùng trực tiếp cho quyết định hành chính.", "Bốn nhóm hệ thống tại khoản 7 để giải nghĩa dẫn chiếu.", "Đánh giá bổ sung khi thay đổi làm phát sinh hoặc đổi mức rủi ro."],
  "missing": "Không.",
  "unnecessary": "Không có chunk về nội dung báo cáo hay trách nhiệm ngoài điều kiện. Bốn điểm khoản 7 là SUPPORTING vì khoản 1 điểm b dẫn chiếu trực tiếp đến khoản này; chúng không phải điều kiện độc lập nếu thiếu yêu cầu đầu ra được dùng trực tiếp cho quyết định hành chính.",
  "reason": "Giữ nguyên nhưng khi human review cần đọc khoản 1 điểm b cùng khoản 7 theo quan hệ liên kết, tránh diễn giải bốn điểm khoản 7 thành bốn trigger độc lập.",
  "assess": {"142-2026-ND-CP_dieu-20_khoan-7_diem-a": "SUPPORTING", "142-2026-ND-CP_dieu-20_khoan-7_diem-b": "SUPPORTING", "142-2026-ND-CP_dieu-20_khoan-7_diem-c": "SUPPORTING", "142-2026-ND-CP_dieu-20_khoan-7_diem-d": "SUPPORTING"}},
 "eval029": {
  "flag": "Query không nêu khu vực áp dụng trong khi corpus có quy định chung và quy định riêng cho khu vực công.",
  "action": "REWRITE_QUERY", "confidence": "medium",
  "ambiguity": "Có hai cách hiểu. (1) Áp dụng chung: Khung đạo đức yêu cầu rà soát quyền và cơ chế giám sát/can thiệp tương xứng mức ảnh hưởng. (2) Khu vực công: Điều 27 Luật và Điều 20 Nghị định yêu cầu báo cáo đánh giá tác động, nhận diện rủi ro, biện pháp kiểm soát và giám sát con người. Gold hiện tại chỉ theo cách hiểu (1).",
  "coverage": ["Cơ chế giám sát và can thiệp của con người tương xứng mức ảnh hưởng.", "Rà soát để không xâm phạm các quyền hợp pháp."],
  "missing": "Thiếu căn cứ đánh giá tác động nếu người hỏi muốn nói riêng cơ quan nhà nước; không thiếu theo cách hiểu Khung đạo đức áp dụng chung.",
  "unnecessary": "Không theo cách hiểu hiện tại.",
  "reason": "Nên viết rõ “Theo Khung đạo đức AI quốc gia, tổ chức, cá nhân phải áp dụng biện pháp nào...” để giữ gold hiện tại; hoặc viết riêng câu về cơ quan nhà nước và đánh giá tác động.", "assess": {}},
 "eval030": {
  "flag": "Gold gồm Luật và Khung đạo đức dù chunk của Luật có thể tự trả lời đầy đủ.",
  "action": "REMOVE_CHUNK", "confidence": "high",
  "ambiguity": "Thấp về nội dung, nhưng wording không yêu cầu hướng dẫn đạo đức nên ưu tiên căn cứ pháp lý trực tiếp và tối thiểu.",
  "coverage": ["Không thay thế thẩm quyền và trách nhiệm con người.", "Duy trì kiểm soát và khả năng can thiệp.", "Cho phép kiểm tra, giám sát quá trình phát triển và vận hành."],
  "missing": "Không sau khi chỉ giữ khoản 2 Điều 4 Luật.",
  "unnecessary": "05-2026-TT-BKHCN_dieu-3_khoan-1_diem-c lặp lại nguyên tắc cốt lõi và chỉ bổ sung tính tương xứng mức ảnh hưởng; đây là SUPPORTING GUIDANCE, không cần để trả lời đầy đủ query retrieval hiện tại.",
  "reason": "Đề xuất bỏ chunk của Thông tư khỏi gold và giữ 134-2025-QH15_dieu-4_khoan-2 làm PRIMARY LEGAL BASIS.",
  "assess": {"05-2026-TT-BKHCN_dieu-3_khoan-1_diem-c": "QUESTIONABLE"},
  "article_roles": {"134-2025-QH15_dieu-4": "PRIMARY LEGAL BASIS", "05-2026-TT-BKHCN_dieu-3": "SUPPORTING GUIDANCE"}},
}


def load(path):
    return [json.loads(x) for x in path.open(encoding="utf-8") if x.strip()]


def aid(c): return f"{c['document_id']}_dieu-{c['article']}"


def render():
    queries = {q["query_id"]: q for q in load(EVAL)}
    chunks = {c["chunk_id"]: c for c in load(CORPUS / "chunks.jsonl")}
    articles = {a["article_id"]: a for a in load(CORPUS / "articles.jsonl")}
    lines = ["# Human Review Report", "", "## Review summary", "", "| query_id | gold_articles | gold_chunks | flag_reason | recommended_action | confidence |", "|---|---:|---:|---|---|---|"]
    rows = []
    for qid in IDS:
        q, r = queries[qid], REVIEW[qid]
        lines.append(f"| {qid} | {len(q['gold_article_ids'])} | {len(q['gold_chunk_ids'])} | {r['flag']} | {r['action']} | {r['confidence']} |")
        questionable = sum(r["assess"].get(cid, "DIRECT") == "QUESTIONABLE" for cid in q["gold_chunk_ids"])
        rows.append({"query_id": qid, "query": q["query"], "current_gold_article_count": len(q["gold_article_ids"]), "current_gold_chunk_count": len(q["gold_chunk_ids"]), "recommended_action": r["action"], "questionable_chunk_count": questionable, "ambiguity": r["ambiguity"], "confidence": r["confidence"], "human_decision": "", "human_notes": ""})
    for qid in IDS:
        q, r = queries[qid], REVIEW[qid]
        lines += ["", "---", "", f"# {qid}", "", "## Query", "", q["query"], "", "## Current annotation", "", f"Query type: {q['query_type']}  ", f"Difficulty: {q['difficulty']}  ", f"Annotation status: {q['annotation_status']}", "", "Gold documents:"]
        lines += [f"- {x}" for x in q["gold_document_ids"]]
        lines += ["", "Gold articles:"] + [f"- {x}" for x in q["gold_article_ids"]]
        lines += ["", "Gold chunks:"] + [f"- {x}" for x in q["gold_chunk_ids"]]
        lines += ["", "## Why this query was flagged", "", r["flag"], "", "## Article context"]
        for article_id in q["gold_article_ids"]:
            a = articles[article_id]
            role = r.get("article_roles", {}).get(article_id, "PRIMARY")
            lines += ["", f"### Article {article_id}", "", f"Title: {a['article_title']}  ", f"Document: {a['document_title']} ({a['document_number']})  ", f"Structure: {('Chương ' + str(a['chapter']) + ' — ' + str(a['chapter_title'])) if a.get('chapter') else 'Không chia chương'}  ", f"Review role: {role}", "", "Article context:"]
            article_chunks = [c for c in chunks.values() if aid(c) == article_id]
            for c in article_chunks:
                lines.append(f"- `{c['chunk_id']}` — {c['text']}")
        lines += ["", "## Gold chunk review"]
        for i, cid in enumerate(q["gold_chunk_ids"], 1):
            c = chunks[cid]
            assessment = r["assess"].get(cid, "DIRECT")
            if assessment == "DIRECT": reason = "Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời."
            elif assessment == "SUPPORTING": reason = "Cần để xác lập phạm vi/nghĩa vụ hoặc giải nghĩa dẫn chiếu, nhưng không tự nó là toàn bộ đáp án."
            else: reason = "Chỉ cần nếu giữ cách hiểu rộng hiện tại; có thể loại sau khi thu hẹp hoặc làm rõ query."
            location = f"{c['document_number']}, Điều {c['article']}"
            if c.get("clause"): location += f", khoản {c['clause']}"
            if c.get("point"): location += f", điểm {c['point']}"
            lines += ["", f"### Chunk {i}", "", f"chunk_id: `{cid}`", "", f"Legal location: {location}", "", "Text:", "", c["text"], "", "Reason selected:", "", reason, "", "Assessment:", f"- {assessment}"]
        lines += ["", "## Coverage analysis", "", "Câu hỏi cần trả lời những ý nào?"]
        lines += [f"{i}. {x}" for i, x in enumerate(r["coverage"], 1)]
        lines += ["", "Gold hiện tại có bao phủ từng ý không?"]
        for i, mapped in enumerate(COVERAGE_MAP[qid], 1):
            lines.append(f"- Ý {i} → " + ", ".join(f"`{cid}`" for cid in mapped) + ".")
        lines += ["", "Missing coverage:", "", r["missing"], "", "Potential unnecessary chunks:", "", r["unnecessary"], "", "## Ambiguity", "", r["ambiguity"], "", "## Recommended human decision", "", f"Suggested action: **{r['action']}**", "", "Reason:", "", r["reason"], "", "## Human decision", "", "- [ ] KEEP", "- [ ] REMOVE_CHUNK", "- [ ] ADD_CHUNK", "- [ ] REWRITE_QUERY", "- [ ] SPLIT_QUERY", "- [ ] NEEDS_REVIEW", "", "Human notes:", ""]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    fields = ["query_id", "query", "current_gold_article_count", "current_gold_chunk_count", "recommended_action", "questionable_chunk_count", "ambiguity", "confidence", "human_decision", "human_notes"]
    with SUMMARY.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)


if __name__ == "__main__": render()
