#!/usr/bin/env python3
"""Create deterministic manual-verification checklists for the corpus."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ARTICLES_PATH = PROJECT_ROOT / "data/processed/articles.jsonl"
CHUNKS_PATH = PROJECT_ROOT / "data/processed/chunks.jsonl"
REGISTRY_PATH = PROJECT_ROOT / "data/source_registry/documents.csv"
PARSER_REPORT_PATH = PROJECT_ROOT / "data/validation/parser_report.csv"
OUTPUT_DIR = PROJECT_ROOT / "data/validation/manual_verification"
SHORT_THRESHOLD = 20


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as source:
        for line_number, line in enumerate(source, 1):
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: JSON không hợp lệ") from exc
    return rows


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as source:
        return [
            {key: value or "" for key, value in row.items() if key is not None}
            for row in csv.DictReader(source)
        ]


def natural_article_key(article: dict[str, Any]) -> tuple[int, str]:
    value = str(article["article"])
    match = re.match(r"(\d+)", value)
    return (int(match.group(1)) if match else 10**9, value)


def article_counts(article: dict[str, Any]) -> tuple[int, int]:
    clauses = article.get("clauses") or []
    point_count = len(article.get("direct_points") or [])
    point_count += sum(len(clause.get("points") or []) for clause in clauses)
    return len(clauses), point_count


def article_excerpt(article: dict[str, Any], limit: int = 360) -> str:
    pieces = [article.get("intro_text") or ""]
    pieces.extend(point.get("text") or "" for point in article.get("direct_points") or [])
    for clause in article.get("clauses") or []:
        pieces.append(clause.get("text") or "")
        pieces.extend(point.get("text") or "" for point in clause.get("points") or [])
    text = re.sub(r"\s+", " ", " ".join(filter(None, pieces))).strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def select_samples(
    articles: list[dict[str, Any]], warning_article_ids: set[str]
) -> list[dict[str, Any]]:
    ordered = sorted(articles, key=natural_article_key)
    chosen: dict[str, dict[str, Any]] = {}

    def add(article: dict[str, Any]) -> None:
        chosen[article["article_id"]] = article

    add(ordered[0])
    add(ordered[-1])
    for index in sorted({len(ordered) // 4, len(ordered) // 2, 3 * len(ordered) // 4}):
        add(ordered[min(index, len(ordered) - 1)])
    add(max(ordered, key=lambda item: (article_counts(item)[0], natural_article_key(item))))
    add(max(ordered, key=lambda item: (article_counts(item)[1], natural_article_key(item))))
    for article in ordered:
        if article["article_id"] in warning_article_ids:
            add(article)
    return sorted(chosen.values(), key=natural_article_key)[:10]


def main() -> int:
    articles = read_jsonl(ARTICLES_PATH)
    chunks = read_jsonl(CHUNKS_PATH)
    registry = {row["document_id"]: row for row in read_csv(REGISTRY_PATH)}
    parser_reports = {row["document_id"]: row for row in read_csv(PARSER_REPORT_PATH)}
    articles_by_doc: dict[str, list[dict[str, Any]]] = defaultdict(list)
    chunks_by_article: dict[str, list[dict[str, Any]]] = defaultdict(list)
    chunks_by_doc: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for article in articles:
        articles_by_doc[article["document_id"]].append(article)
    for chunk in chunks:
        article_id = f"{chunk['document_id']}_dieu-{str(chunk['article']).lower()}"
        chunks_by_article[article_id].append(chunk)
        chunks_by_doc[chunk["document_id"]].append(chunk)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for document_id, metadata in registry.items():
        document_articles = articles_by_doc[document_id]
        document_chunks = chunks_by_doc[document_id]
        text_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for chunk in document_chunks:
            text_groups[chunk["text"]].append(chunk)
        duplicate_groups = [group for group in text_groups.values() if len(group) > 1]
        short_chunks = [
            chunk for chunk in document_chunks if len(chunk["text"]) < SHORT_THRESHOLD
        ]
        warning_ids = {
            f"{chunk['document_id']}_dieu-{str(chunk['article']).lower()}"
            for group in duplicate_groups for chunk in group
        } | {
            f"{chunk['document_id']}_dieu-{str(chunk['article']).lower()}"
            for chunk in short_chunks
        }
        samples = select_samples(document_articles, warning_ids)
        ordered = sorted(document_articles, key=natural_article_key)
        chapters = {
            (item.get("chapter"), item.get("chapter_title"))
            for item in document_articles if item.get("chapter")
        }
        sections = {
            (item.get("section"), item.get("section_title"))
            for item in document_articles if item.get("section")
        }
        parser_report = parser_reports.get(document_id, {})
        appendix_line = parser_report.get("appendix_start_line") or "Không có"
        appendix_excluded = (
            "Có — `end_line` lớn nhất của Điều là "
            f"{max(int(item['end_line']) for item in document_articles)}, "
            f"trước dòng phụ lục {appendix_line}"
            if appendix_line != "Không có"
            else "Không áp dụng — parser report không ghi nhận phụ lục"
        )

        lines = [
            f"# Checklist xác minh: {document_id}",
            "",
            "## A. Thông tin nguồn",
            "",
            f"- `document_id`: `{document_id}`",
            f"- Số hiệu văn bản: {metadata['document_number']}",
            f"- Tên văn bản: {metadata['document_title']}",
            f"- PDF chính thức: `{metadata['official_pdf_path']}`",
            f"- DOCX làm việc: `{metadata['working_docx_path']}`",
            f"- SHA-256 PDF: `{metadata['official_pdf_hash']}`",
            f"- SHA-256 DOCX: `{metadata['working_docx_hash']}`",
            f"- URL chính thức: {metadata['official_source_url']}",
            f"- Trạng thái xác minh: `{metadata['verification_status']}`",
            "",
            "## B. Kiểm tra cấu trúc tổng thể",
            "",
            f"- Số Điều thực tế: {len(document_articles)}",
            f"- Điều đầu tiên: Điều {ordered[0]['article']}",
            f"- Điều cuối cùng: Điều {ordered[-1]['article']}",
            f"- Số Chương: {len(chapters)}",
            f"- Số Mục: {len(sections)}",
            f"- Dòng bắt đầu phụ lục theo parser report: {appendix_line}",
            f"- Xác nhận parser đã loại phụ lục khỏi `articles.jsonl`: {appendix_excluded}",
            "",
            "- [ ] Số Điều khớp PDF chính thức",
            "- [ ] Điều đầu tiên đúng",
            "- [ ] Điều cuối cùng đúng",
            "- [ ] Tiêu đề Chương đúng",
            "- [ ] Không có Điều thuộc phụ lục lọt vào corpus chính",
            "",
            "## C. Mẫu Điều cần kiểm tra",
            "",
            "Mẫu được chọn tái tạo từ Điều đầu/cuối, các tứ phân vị, Điều nhiều Khoản/Điểm nhất và Điều có warning.",
            "",
        ]
        for article in samples:
            clause_count, point_count = article_counts(article)
            chunk_ids = [chunk["chunk_id"] for chunk in chunks_by_article[article["article_id"]]]
            chapter = (
                f"Chương {article.get('chapter')}: {article.get('chapter_title')}"
                if article.get("chapter") else "Không có"
            )
            section = (
                f"Mục {article.get('section')}: {article.get('section_title')}"
                if article.get("section") else "Không có"
            )
            lines.extend([
                f"### Điều {article['article']}. {article.get('article_title') or ''}".rstrip(),
                "",
                f"- `article_id`: `{article['article_id']}`",
                f"- Chương/Mục: {chapter} / {section}",
                f"- Dòng nguồn: {article.get('start_line')}–{article.get('end_line')}",
                f"- Số Khoản: {clause_count}",
                f"- Số Điểm: {point_count}",
                "- `chunk_id`: " + ", ".join(f"`{value}`" for value in chunk_ids),
                f"- Nội dung đối chiếu: {article_excerpt(article)}",
                "",
                "- [ ] Tiêu đề Điều đúng",
                "- [ ] Nội dung mở đầu đúng",
                "- [ ] Số Khoản đúng",
                "- [ ] Số Điểm đúng",
                "- [ ] Chunk không mất nội dung",
                "- [ ] Nội dung khớp PDF chính thức",
                "",
            ])

        lines.extend(["## D. Các warning cần xác nhận", ""])
        if not short_chunks and not duplicate_groups:
            lines.extend(["Không có warning riêng cho văn bản này.", ""])
        for chunk in short_chunks:
            lines.extend([
                f"### Chunk ngắn `{chunk['chunk_id']}`",
                "",
                f"Text: {chunk['text']}",
                "",
                "- [ ] Xác nhận đây là nội dung pháp lý ngắn nhưng hợp lệ",
                "",
            ])
        for number, group in enumerate(duplicate_groups, 1):
            lines.extend([
                f"### Nhóm text giống nhau {number}",
                "",
                "- Vị trí pháp lý: " + ", ".join(f"`{item['chunk_id']}`" for item in group),
                f"- Text: {group[0]['text']}",
                "",
                "- [ ] Xác nhận text trùng là hợp lệ tại các vị trí pháp lý khác nhau",
                "",
            ])
        output = OUTPUT_DIR / f"{document_id}.verification.md"
        output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        print(f"Created: {output.relative_to(PROJECT_ROOT)} ({len(samples)} Điều mẫu)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
