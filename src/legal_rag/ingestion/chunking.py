"""Deterministic legal-article to retrieval-chunk construction."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Iterable, Mapping

CORPUS_VERSION = "corpus-v0.1"
MAX_CHARS = 3500
MIN_CHARS = 20

def normalize_text(text: str | None) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def split_long_text(text: str, max_chars: int = MAX_CHARS) -> list[str]:
    text = normalize_text(text)
    if len(text) <= max_chars:
        return [text]

    sentences = re.split(r"(?<=[.;!?])\s+(?=[A-ZÀ-Ỹ0-9])", text)
    segments: list[str] = []
    current: list[str] = []

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        candidate = " ".join(current + [sentence])
        if current and len(candidate) > max_chars:
            segments.append(" ".join(current))
            current = [sentence]
        else:
            current.append(sentence)

    if current:
        segments.append(" ".join(current))

    final_segments: list[str] = []
    for segment in segments:
        while len(segment) > max_chars:
            cut = segment.rfind(" ", 0, max_chars)
            if cut <= 0:
                cut = max_chars
            final_segments.append(segment[:cut].strip())
            segment = segment[cut:].strip()
        if segment:
            final_segments.append(segment)

    return final_segments


def structure_path(
    article: dict[str, Any],
    clause: str | None = None,
    point: str | None = None,
) -> list[str]:
    values = [article["document_title"]]

    mappings = [
        ("part", "part_title", "Phần"),
        ("chapter", "chapter_title", "Chương"),
        ("section", "section_title", "Mục"),
        ("subsection", "subsection_title", "Tiểu mục"),
    ]

    for number_key, title_key, label in mappings:
        number = article.get(number_key)
        if number:
            value = f"{label} {number}"
            if article.get(title_key):
                value += f": {article[title_key]}"
            values.append(value)

    article_value = f"Điều {article['article']}"
    if article.get("article_title"):
        article_value += f": {article['article_title']}"
    values.append(article_value)

    if clause:
        values.append(f"Khoản {clause}")
    if point:
        values.append(f"Điểm {point})")

    return values


def parent_context(
    article: dict[str, Any],
    clause: str | None = None,
    clause_text: str | None = None,
) -> str:
    parts = [
        f"Văn bản: {article['document_title']} ({article['document_number']})"
    ]

    if article.get("chapter"):
        value = f"Chương {article['chapter']}"
        if article.get("chapter_title"):
            value += f": {article['chapter_title']}"
        parts.append(value)

    value = f"Điều {article['article']}"
    if article.get("article_title"):
        value += f": {article['article_title']}"
    parts.append(value)

    intro = normalize_text(article.get("intro_text"))
    if intro:
        parts.append(f"Mở đầu điều: {intro}")

    if clause:
        parts.append(f"Khoản {clause}")
    if clause_text:
        parts.append(f"Nội dung dẫn của khoản: {normalize_text(clause_text)}")

    return "\n".join(parts)


def retrieval_text(
    article: dict[str, Any],
    body: str,
    clause: str | None = None,
    point: str | None = None,
) -> str:
    lines = [
        article["document_title"],
        article["document_number"],
    ]

    if article.get("chapter_title"):
        lines.append(article["chapter_title"])

    article_heading = f"Điều {article['article']}"
    if article.get("article_title"):
        article_heading += f". {article['article_title']}"
    lines.append(article_heading)

    if clause:
        lines.append(f"Khoản {clause}")
    if point:
        lines.append(f"Điểm {point})")

    lines.append(body)
    return "\n".join(lines)


def make_chunk_id(
    document_id: str,
    article: str,
    level: str,
    clause: str | None,
    point: str | None,
    segment_index: int,
    segment_count: int,
) -> str:
    parts = [document_id, f"dieu-{article.lower()}"]
    if clause:
        parts.append(f"khoan-{clause.lower()}")
    if point:
        parts.append(f"diem-{point.lower()}")
    if level == "article_intro":
        parts.append("mo-dau")
    if segment_count > 1:
        parts.append(f"phan-{segment_index}")
    return "_".join(parts)


def create_records(
    article: dict[str, Any],
    metadata: dict[str, str],
    body: str,
    level: str,
    clause: str | None = None,
    point: str | None = None,
    clause_text: str | None = None,
    start_line: int | None = None,
) -> list[dict[str, Any]]:
    body = normalize_text(body)
    if not body:
        return []

    segments = split_long_text(body)
    records: list[dict[str, Any]] = []

    for index, segment in enumerate(segments, start=1):
        path = structure_path(article, clause, point)
        records.append(
            {
                "chunk_id": make_chunk_id(
                    article["document_id"],
                    str(article["article"]),
                    level,
                    clause,
                    point,
                    index,
                    len(segments),
                ),
                "corpus_version": CORPUS_VERSION,
                "document_id": article["document_id"],
                "document_number": article["document_number"],
                "document_title": article["document_title"],
                "document_type": metadata.get("document_type"),
                "issuing_authority": metadata.get("issuing_authority"),
                "issued_date": metadata.get("issued_date"),
                "effective_from": metadata.get("effective_from"),
                "effective_to": metadata.get("effective_to") or None,
                "status": metadata.get("status"),
                "corpus_layer": metadata.get("corpus_layer"),
                "part": article.get("part"),
                "part_title": article.get("part_title"),
                "chapter": article.get("chapter"),
                "chapter_title": article.get("chapter_title"),
                "section": article.get("section"),
                "section_title": article.get("section_title"),
                "subsection": article.get("subsection"),
                "subsection_title": article.get("subsection_title"),
                "article": str(article["article"]),
                "article_title": article.get("article_title"),
                "clause": clause,
                "point": point.lower() if point else None,
                "chunk_level": level,
                "segment_index": index,
                "segment_count": len(segments),
                "text": segment,
                "retrieval_text": retrieval_text(
                    article, segment, clause, point
                ),
                "parent_context": parent_context(
                    article, clause, clause_text
                ),
                "structure_path": path,
                "structure_path_text": " > ".join(path),
                "source_start_line": start_line,
                "source_end_line": article.get("end_line"),
                "official_source_url": metadata.get("official_source_url"),
                "extraction_source_url": metadata.get("extraction_source_url"),
                "official_pdf_path": metadata.get("official_pdf_path"),
                "working_docx_path": metadata.get("working_docx_path"),
                "extraction_method": metadata.get("extraction_method"),
                "official_pdf_hash": metadata.get("official_pdf_hash"),
                "working_docx_hash": metadata.get("working_docx_hash"),
                "verification_status": metadata.get("verification_status"),
                "verified_by": metadata.get("verified_by") or None,
            }
        )

    return records


def build_article_chunks(
    article: dict[str, Any],
    metadata: dict[str, str],
) -> list[dict[str, Any]]:
    chunks: list[dict[str, Any]] = []
    intro = normalize_text(article.get("intro_text"))
    clauses = article.get("clauses") or []
    direct_points = article.get("direct_points") or []

    if not clauses and not direct_points:
        return create_records(
            article,
            metadata,
            intro,
            "article",
            start_line=article.get("start_line"),
        )

    if intro:
        chunks.extend(
            create_records(
                article,
                metadata,
                intro,
                "article_intro",
                start_line=article.get("start_line"),
            )
        )

    for point_data in direct_points:
        chunks.extend(
            create_records(
                article,
                metadata,
                point_data.get("text", ""),
                "point",
                point=str(point_data.get("point") or "") or None,
                start_line=point_data.get("start_line"),
            )
        )

    for clause_data in clauses:
        clause = str(clause_data.get("clause") or "") or None
        clause_text = normalize_text(clause_data.get("text"))
        points = clause_data.get("points") or []

        if not points:
            chunks.extend(
                create_records(
                    article,
                    metadata,
                    clause_text,
                    "clause",
                    clause=clause,
                    start_line=clause_data.get("start_line"),
                )
            )
            continue

        for point_data in points:
            chunks.extend(
                create_records(
                    article,
                    metadata,
                    point_data.get("text", ""),
                    "point",
                    clause=clause,
                    point=str(point_data.get("point") or "") or None,
                    clause_text=clause_text,
                    start_line=point_data.get("start_line"),
                )
            )

    return chunks


def validate_chunk(chunk: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = [
        "chunk_id",
        "document_id",
        "article",
        "chunk_level",
        "text",
        "retrieval_text",
        "structure_path_text",
        "official_source_url",
        "verification_status",
    ]

    for field in required:
        value = chunk.get(field)
        if value is None or (isinstance(value, str) and not value.strip()):
            errors.append(f"Thiếu {field}")

    length = len(normalize_text(chunk.get("text")))
    if length > MAX_CHARS:
        errors.append(f"Text quá dài ({length} ký tự)")

    return errors


def review_chunk(chunk: dict[str, Any]) -> list[str]:
    warnings: list[str] = []
    length = len(normalize_text(chunk.get("text")))
    if length < MIN_CHARS:
        warnings.append(
            f"Cảnh báo: nội dung pháp lý ngắn ({length} ký tự)"
        )
    return warnings




def build_chunks(
    articles: Iterable[Mapping[str, Any]],
    registry: Mapping[str, Mapping[str, str]],
) -> list[dict[str, Any]]:
    """Build chunks in input article order using authoritative registry metadata."""
    chunks: list[dict[str, Any]] = []
    for article in articles:
        document_id = str(article.get("document_id") or "").strip()
        if document_id not in registry:
            raise ValueError(f"Không tìm thấy {document_id} trong documents.csv")
        chunks.extend(build_article_chunks(dict(article), dict(registry[document_id])))
    return chunks


def serialize_chunks(rows: Iterable[Mapping[str, Any]]) -> bytes:
    """Serialize with the historical JSONL encoding and field order."""
    return "".join(
        json.dumps(dict(row), ensure_ascii=False) + "\n" for row in rows
    ).encode("utf-8")


def write_chunks(path: Path, rows: Iterable[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(serialize_chunks(rows))
