#!/usr/bin/env python3
"""Deterministic, corpus-only support tool for retrieval evaluation annotation.

Candidate search is deliberately lexical (token overlap), not BM25.  Gold labels
are an explicit reviewed mapping below and are never inferred from search scores.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVAL = ROOT / "eval-sets/retrieval/retrieval_eval.jsonl"
ARTICLES = ROOT / "data/versions/corpus-v0.1/articles.jsonl"
CHUNKS = ROOT / "data/versions/corpus-v0.1/chunks.jsonl"
REPORT = ROOT / "annotation/retrieval/retrieval_eval_annotation_report.md"
SUMMARY = ROOT / "annotation/retrieval/retrieval_eval_annotation_summary.csv"


def ann(difficulty, chunks, why, ambiguity=""):
    return {"difficulty": difficulty, "chunks": chunks, "why": why,
            "ambiguity": ambiguity}


# This mapping records corpus-content judgments made after reading each complete
# candidate Article. Candidate scores are not persisted and do not determine gold.
ANNOTATIONS = {
 "eval001": ann("easy", ["134-2025-QH15_dieu-9_khoan-1_diem-a", "134-2025-QH15_dieu-9_khoan-1_diem-b", "134-2025-QH15_dieu-9_khoan-1_diem-c"], "Khoản 1 Điều 9 liệt kê trực tiếp ba mức rủi ro và nội hàm từng mức."),
 "eval002": ann("easy", ["142-2026-ND-CP_dieu-7_khoan-2_diem-d"], "Điểm d khoản 2 Điều 7 xác định Bộ Khoa học và Công nghệ trình Thủ tướng Chính phủ ban hành Danh mục."),
 "eval003": ann("easy", ["142-2026-ND-CP_dieu-12_khoan-1"], "Khoản 1 Điều 12 quy định trực tiếp đối tượng phải lập và thời điểm trước khi đưa hệ thống vào sử dụng."),
 "eval004": ann("medium", ["142-2026-ND-CP_dieu-15_khoan-1", "142-2026-ND-CP_dieu-15_khoan-2_diem-a", "142-2026-ND-CP_dieu-15_khoan-2_diem-b", "142-2026-ND-CP_dieu-15_khoan-2_diem-c", "142-2026-ND-CP_dieu-15_khoan-2_diem-d", "142-2026-ND-CP_dieu-15_khoan-2_diem-đ"], "Điều 15 quy định nghĩa vụ thiết lập, duy trì hệ thống quản lý rủi ro và đầy đủ năm nhóm biện pháp của nhà cung cấp."),
 "eval005a": ann("hard", ["134-2025-QH15_dieu-14_khoan-1_diem-a", "134-2025-QH15_dieu-14_khoan-1_diem-b", "134-2025-QH15_dieu-14_khoan-1_diem-c", "134-2025-QH15_dieu-14_khoan-1_diem-d", "134-2025-QH15_dieu-14_khoan-1_diem-đ", "134-2025-QH15_dieu-14_khoan-1_diem-e", "134-2025-QH15_dieu-14_khoan-1_diem-g"], "Khoản 1 Điều 14 liệt kê trực tiếp và đầy đủ bảy nghĩa vụ quản lý của nhà cung cấp hệ thống AI rủi ro cao."),
 "eval005b": ann("hard", ["134-2025-QH15_dieu-14_khoan-2_diem-a", "134-2025-QH15_dieu-14_khoan-2_diem-b", "134-2025-QH15_dieu-14_khoan-2_diem-c", "134-2025-QH15_dieu-14_khoan-2_diem-d", "134-2025-QH15_dieu-14_khoan-2_diem-đ", "134-2025-QH15_dieu-14_khoan-2_diem-e"], "Khoản 2 Điều 14 liệt kê trực tiếp và đầy đủ sáu nghĩa vụ quản lý của bên triển khai hệ thống AI rủi ro cao."),
 "eval006": ann("medium", ["134-2025-QH15_dieu-11_khoan-1", "134-2025-QH15_dieu-11_khoan-2", "134-2025-QH15_dieu-11_khoan-5"], "Các khoản 1, 2 và 5 Điều 11 trực tiếp quy định trách nhiệm của nhà cung cấp về nhận biết tương tác, đánh dấu máy đọc và duy trì minh bạch."),
 "eval007": ann("hard", ["142-2026-ND-CP_dieu-18_khoan-3_diem-a", "142-2026-ND-CP_dieu-18_khoan-3_diem-b", "142-2026-ND-CP_dieu-18_khoan-3_diem-c", "142-2026-ND-CP_dieu-18_khoan-3_diem-d", "142-2026-ND-CP_dieu-18_khoan-3_diem-đ", "142-2026-ND-CP_dieu-18_khoan-5_diem-a", "142-2026-ND-CP_dieu-18_khoan-5_diem-b", "142-2026-ND-CP_dieu-18_khoan-5_diem-c", "142-2026-ND-CP_dieu-18_khoan-5_diem-d"], "Khoản 3 quy định chất lượng, thời điểm của nhãn/thông báo; khoản 5 liệt kê các hình thức hiển thị phù hợp."),
 "eval008": ann("medium", ["142-2026-ND-CP_dieu-18_khoan-1", "142-2026-ND-CP_dieu-18_khoan-2_diem-a", "142-2026-ND-CP_dieu-18_khoan-2_diem-b", "142-2026-ND-CP_dieu-18_khoan-6"], "Điều 18 xác định nội dung công khai dễ gây nhầm lẫn, nội dung mô phỏng người thật/tái hiện sự kiện và trường hợp tác phẩm sáng tạo phải giúp nhận biết nguồn gốc."),
 "eval009": ann("easy", ["134-2025-QH15_dieu-11_khoan-1"], "Khoản 1 Điều 11 quy định trực tiếp yêu cầu thiết kế và vận hành để người dùng nhận biết đang tương tác với AI."),
 "eval010": ann("easy", ["134-2025-QH15_dieu-12_khoan-2_diem-a"], "Điểm a khoản 2 Điều 12 nêu trọn nghĩa vụ của nhà cung cấp: khắc phục, tạm dừng hoặc thu hồi và thông báo cơ quan có thẩm quyền."),
 "eval011": ann("medium", ["134-2025-QH15_dieu-21_khoan-2_diem-a", "134-2025-QH15_dieu-21_khoan-2_diem-b"], "Khoản 2 Điều 21 liệt kê hai cơ chế được áp dụng trong phạm vi thử nghiệm."),
 "eval012": ann("medium", ["142-2026-ND-CP_dieu-23_khoan-3_diem-a", "142-2026-ND-CP_dieu-23_khoan-3_diem-b", "142-2026-ND-CP_dieu-23_khoan-3_diem-c"], "Khoản 3 Điều 23 phân thẩm quyền theo cấp độ, phạm vi địa bàn và lĩnh vực quản lý."),
 "eval013": ann("medium", ["142-2026-ND-CP_dieu-22_khoan-1_diem-a", "142-2026-ND-CP_dieu-22_khoan-1_diem-b", "142-2026-ND-CP_dieu-22_khoan-1_diem-c", "142-2026-ND-CP_dieu-22_khoan-1_diem-d", "142-2026-ND-CP_dieu-22_khoan-2"], "Khoản 1 Điều 22 liệt kê bốn tiêu chí; khoản 2 quy định cách xử lý khi đồng thời thuộc nhiều cấp độ."),
 "eval014": ann("medium", ["142-2026-ND-CP_dieu-24_khoan-2_diem-a", "142-2026-ND-CP_dieu-24_khoan-2_diem-b", "142-2026-ND-CP_dieu-24_khoan-2_diem-c", "142-2026-ND-CP_dieu-24_khoan-2_diem-d"], "Khoản 2 Điều 24 liệt kê trực tiếp bốn thành phần của hồ sơ thông thường; không lấy khoản 3 về hồ sơ rút gọn."),
 "eval015": ann("hard", ["134-2025-QH15_dieu-21_khoan-3", "142-2026-ND-CP_dieu-25_khoan-1_diem-c"], "Luật nêu căn cứ rủi ro ảnh hưởng an toàn, an ninh hoặc quyền lợi; Nghị định cụ thể hóa vi phạm giới hạn hoặc không khắc phục sự cố."),
 "eval016": ann("medium", ["142-2026-ND-CP_dieu-25_khoan-2_diem-a", "142-2026-ND-CP_dieu-25_khoan-2_diem-b", "142-2026-ND-CP_dieu-25_khoan-3_diem-a", "142-2026-ND-CP_dieu-25_khoan-3_diem-b", "142-2026-ND-CP_dieu-25_khoan-4"], "Điều 25 quy định báo cáo định kỳ theo cấp độ, báo cáo sự cố/vượt giới hạn và báo cáo tổng kết."),
 "eval017": ann("medium", ["142-2026-ND-CP_dieu-27_khoan-1"], "Khoản 1 Điều 27 trả lời đầy đủ khả năng gia hạn, thời điểm nộp, thành phần, thời hạn giải quyết và nghĩa vụ nêu lý do khi từ chối."),
 "eval018": ann("medium", ["142-2026-ND-CP_dieu-27_khoan-1", "142-2026-ND-CP_dieu-27_khoan-2_diem-a", "142-2026-ND-CP_dieu-27_khoan-2_diem-b"], "Điều 27 quy định đánh giá, cấp xác nhận hoàn thành và việc công nhận kết quả hoặc điều chỉnh nghĩa vụ sau thử nghiệm."),
 "eval019": ann("easy", ["134-2025-QH15_dieu-17_khoan-2"], "Khoản 2 Điều 17 nêu trực tiếp các nguyên tắc mở, an toàn, có kiểm soát, chất lượng, kết nối và khai thác."),
 "eval020": ann("easy", ["142-2026-ND-CP_dieu-3_khoan-7"], "Khoản 7 Điều 3 là định nghĩa trực tiếp của dữ liệu mở có điều kiện."),
 "eval021": ann("easy", ["142-2026-ND-CP_dieu-32_khoan-1_diem-a", "142-2026-ND-CP_dieu-32_khoan-1_diem-b", "142-2026-ND-CP_dieu-32_khoan-1_diem-c"], "Khoản 1 Điều 32 liệt kê trực tiếp ba loại dữ liệu trong cơ sở dữ liệu phục vụ AI."),
 "eval022": ann("medium", ["142-2026-ND-CP_dieu-32_khoan-5_diem-a", "142-2026-ND-CP_dieu-32_khoan-5_diem-b", "142-2026-ND-CP_dieu-32_khoan-5_diem-c"], "Khoản 5 Điều 32 quy định trách nhiệm xây dựng/cập nhật, bảo đảm chất lượng và kết nối/chia sẻ/khai thác của cơ quan quản lý."),
 "eval023": ann("easy", ["134-2025-QH15_dieu-17_khoan-2", "134-2025-QH15_dieu-17_khoan-3"], "Khoản 2 đặt yêu cầu về kết nối, khai thác; khoản 3 yêu cầu các cơ sở dữ liệu của cơ quan nhà nước kết nối thống nhất và bảo đảm tiêu chuẩn, chất lượng, an toàn."),
 "eval024": ann("easy", ["134-2025-QH15_dieu-7_khoan-2_diem-c"], "Điểm c khoản 2 Điều 7 trực tiếp cấm lợi dụng điểm yếu của các nhóm dễ bị tổn thương để gây tổn hại."),
 "eval025": ann("hard", ["142-2026-ND-CP_dieu-20_khoan-1_diem-a", "142-2026-ND-CP_dieu-20_khoan-1_diem-b", "142-2026-ND-CP_dieu-20_khoan-2", "142-2026-ND-CP_dieu-20_khoan-7_diem-a", "142-2026-ND-CP_dieu-20_khoan-7_diem-b", "142-2026-ND-CP_dieu-20_khoan-7_diem-c", "142-2026-ND-CP_dieu-20_khoan-7_diem-d"], "Điều 20 bao quát trường hợp rủi ro cao, quyết định hành chính, đánh giá bổ sung khi thay đổi và bốn dạng liên quan quyền con người/công bằng/lợi ích công cộng."),
 "eval026": ann("medium", ["142-2026-ND-CP_dieu-20_khoan-3_diem-a", "142-2026-ND-CP_dieu-20_khoan-3_diem-b", "142-2026-ND-CP_dieu-20_khoan-3_diem-c", "142-2026-ND-CP_dieu-20_khoan-3_diem-d"], "Khoản 3 Điều 20 liệt kê trực tiếp bốn nhóm nội dung bắt buộc của báo cáo."),
 "eval027": ann("medium", ["134-2025-QH15_dieu-26_khoan-1_diem-a", "134-2025-QH15_dieu-26_khoan-1_diem-b", "134-2025-QH15_dieu-26_khoan-1_diem-c", "134-2025-QH15_dieu-26_khoan-1_diem-d"], "Khoản 1 Điều 26 đặt ra bốn nhóm nguyên tắc làm cơ sở ban hành Khung đạo đức quốc gia."),
 "eval028": ann("hard", ["05-2026-TT-BKHCN_dieu-3_khoan-2_diem-d", "05-2026-TT-BKHCN_dieu-3_khoan-4_diem-b"], "Khung đạo đức yêu cầu tài liệu giải thích, bằng chứng, phân định chủ thể giải trình, trách nhiệm trong vòng đời và đầu mối khiếu nại/khắc phục."),
 "eval029": ann("hard", ["05-2026-TT-BKHCN_dieu-3_khoan-1_diem-c", "05-2026-TT-BKHCN_dieu-3_khoan-2_diem-a"], "Trong phạm vi Khung đạo đức quốc gia, hai điểm trực tiếp yêu cầu giám sát/can thiệp tương xứng và rà soát để không xâm phạm quyền con người; không lấy quy định riêng cho khu vực công."),
 "eval030": ann("hard", ["134-2025-QH15_dieu-4_khoan-2"], "Khoản 2 Điều 4 của Luật trực tiếp và đầy đủ yêu cầu duy trì kiểm soát, khả năng can thiệp, kiểm tra và giám sát của con người."),
}


def load_jsonl(path):
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def article_id(chunk):
    return f"{chunk['document_id']}_dieu-{chunk['article']}"


def normalized_tokens(text):
    text = unicodedata.normalize("NFD", text.lower())
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return set(re.findall(r"[a-z0-9đ]+", text))


def search(query, limit):
    q = normalized_tokens(query)
    rows = []
    for chunk in load_jsonl(CHUNKS):
        tokens = normalized_tokens(chunk["retrieval_text"])
        score = len(q & tokens) / max(1, len(q))
        if score:
            rows.append((score, chunk))
    for score, chunk in sorted(rows, key=lambda x: (-x[0], x[1]["chunk_id"]))[:limit]:
        print(f"{score:.3f}\t{chunk['chunk_id']}\t{chunk['text']}")


def show_article(aid):
    found = False
    for chunk in load_jsonl(CHUNKS):
        if article_id(chunk) == aid:
            found = True
            print(f"{chunk['chunk_id']}\n{chunk['text']}\n")
    if not found:
        raise SystemExit(f"Unknown article: {aid}")


def materialize():
    queries = load_jsonl(EVAL)
    migrated = []
    for q in queries:
        if q["query_id"] == "eval005":
            for qid, text in (
                ("eval005a", "Nhà cung cấp hệ thống trí tuệ nhân tạo có rủi ro cao phải thực hiện những nghĩa vụ quản lý nào?"),
                ("eval005b", "Bên triển khai hệ thống trí tuệ nhân tạo có rủi ro cao phải thực hiện những nghĩa vụ quản lý nào?"),
            ):
                replacement = dict(q)
                replacement.update(query_id=qid, query=text, query_type="actor_obligation")
                migrated.append(replacement)
        else:
            if q["query_id"] == "eval014":
                q["query"] = "Hồ sơ thông thường để tham gia cơ chế thử nghiệm có kiểm soát gồm những thành phần nào?"
            elif q["query_id"] == "eval029":
                q["query"] = "Theo Khung đạo đức trí tuệ nhân tạo quốc gia, khi hệ thống AI có thể ảnh hưởng đáng kể đến quyền con người thì cần áp dụng những biện pháp kiểm soát nào?"
            migrated.append(q)
    queries = migrated
    chunks = {c["chunk_id"]: c for c in load_jsonl(CHUNKS)}
    articles = {a["article_id"]: a for a in load_jsonl(ARTICLES)}
    if {q["query_id"] for q in queries} != set(ANNOTATIONS):
        raise SystemExit("Annotation mapping and evaluation query IDs differ")
    report = ["# Retrieval Evaluation Annotation Report", ""]
    summary_rows = []
    for q in queries:
        a = ANNOTATIONS[q["query_id"]]
        selected = [chunks[cid] for cid in a["chunks"]]
        article_ids = list(dict.fromkeys(article_id(c) for c in selected))
        document_ids = list(dict.fromkeys(c["document_id"] for c in selected))
        q.update(difficulty=a["difficulty"], gold_document_ids=document_ids,
                 gold_article_ids=article_ids, gold_chunk_ids=a["chunks"],
                 annotation_status="verified",
                 annotated_by="Codex-assisted; human-reviewed by Nguyễn Minh Kha",
                 notes=a["why"] + ((" Potential ambiguity: " + a["ambiguity"]) if a["ambiguity"] else ""))
        attention = bool(a["ambiguity"] or len(article_ids) > 1 or len(a["chunks"]) > 5)
        report += [f"## {q['query_id']}", "", "Query:", q["query"], "", "Intent:", q["query_type"], "", "Difficulty:", q["difficulty"], "", "Gold documents:"]
        report += [f"- {d}" for d in document_ids] or ["- (none)"]
        report += ["", "Gold articles:"] + ([f"- {x}" for x in article_ids] or ["- (none)"])
        report += ["", "Gold chunks:"] + ([f"- {x}" for x in a["chunks"]] or ["- (none)"])
        report += ["", "Why:", a["why"], "", "Potential ambiguity:", a["ambiguity"] or "None identified.", "", "---", ""]
        summary_rows.append({"query_id": q["query_id"], "query": q["query"], "query_type": q["query_type"], "difficulty": q["difficulty"], "gold_document_count": len(document_ids), "gold_article_count": len(article_ids), "gold_chunk_count": len(a["chunks"]), "annotation_status": q["annotation_status"], "needs_manual_attention": str(attention).lower()})
        for aid in article_ids:
            assert aid in articles
    with EVAL.open("w", encoding="utf-8") as f:
        for q in queries:
            f.write(json.dumps(q, ensure_ascii=False) + "\n")
    REPORT.write_text("\n".join(report), encoding="utf-8")
    fields = list(summary_rows[0])
    with SUMMARY.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(summary_rows)


def stats():
    qs = load_jsonl(EVAL)
    difficulty = Counter(q["difficulty"] for q in qs)
    types = Counter(q["query_type"] for q in qs)
    counts = [len(q["gold_chunk_ids"]) for q in qs]
    print(f"Total queries: {len(qs)}")
    for key in ("easy", "medium", "hard"):
        print(f"{key.title()}: {difficulty[key]}")
    print(f"Single-document queries: {sum(len(q['gold_document_ids']) == 1 for q in qs)}")
    print(f"Multi-document queries: {sum(len(q['gold_document_ids']) > 1 for q in qs)}")
    print(f"Single-article queries: {sum(len(q['gold_article_ids']) == 1 for q in qs)}")
    print(f"Multi-article queries: {sum(len(q['gold_article_ids']) > 1 for q in qs)}")
    print(f"Average gold chunks/query: {sum(counts)/len(counts):.2f}")
    print(f"Max gold chunks/query: {max(counts)}")
    print(f"in_review: {sum(q['annotation_status'] == 'in_review' for q in qs)}")
    print(f"needs_review: {sum(q['annotation_status'] == 'needs_review' for q in qs)}")
    print("By query_type:")
    for key in sorted(types): print(f"  {key}: {types[key]}")


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="command", required=True)
    s = sub.add_parser("search", help="lexical candidate search only")
    s.add_argument("query"); s.add_argument("--limit", type=int, default=10)
    a = sub.add_parser("show-article", help="show every chunk in an Article")
    a.add_argument("article_id")
    sub.add_parser("apply", help="write deterministic annotations and reports")
    sub.add_parser("stats", help="print annotation statistics")
    args = p.parse_args()
    if args.command == "search": search(args.query, args.limit)
    elif args.command == "show-article": show_article(args.article_id)
    elif args.command == "apply": materialize()
    else: stats()


if __name__ == "__main__":
    main()
