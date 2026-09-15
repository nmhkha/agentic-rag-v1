from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[3]

REGISTRY_PATH = (
    PROJECT_ROOT
    / "data"
    / "source_registry"
    / "documents.csv"
)

ARTICLES_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "articles.jsonl"
)

CHUNKS_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "chunks.jsonl"
)

VALIDATION_DIRECTORY = (
    PROJECT_ROOT
    / "data"
    / "validation"
)

SUMMARY_REPORT_PATH = (
    VALIDATION_DIRECTORY
    / "corpus_validation_summary.csv"
)

DETAIL_REPORT_PATH = (
    VALIDATION_DIRECTORY
    / "corpus_validation_details.txt"
)

VALIDATED_MANIFEST_PATH = (
    PROJECT_ROOT
    / "data"
    / "versions"
    / "corpus_validation_manifest.json"
)


EXPECTED_ARTICLE_COUNTS = {
    "134-2025-QH15": 35,
    "142-2026-ND-CP": 46,
    "05-2026-TT-BKHCN": 5,
}

VALID_DOCUMENT_TYPES = {
    "luat",
    "nghi_dinh",
    "thong_tu",
    "quyet_dinh",
    "nghi_quyet",
}

VALID_DOCUMENT_STATUSES = {
    "con_hieu_luc",
    "het_hieu_luc",
    "het_hieu_luc_mot_phan",
    "chua_co_hieu_luc",
    "khong_xac_dinh",
}

VALID_CORPUS_LAYERS = {
    "core",
    "related",
    "sectoral",
    "historical",
    "guidance",
}

VALID_VERIFICATION_STATUSES = {
    "pending",
    "structure_verified",
    "content_verified",
    "verified",
    "needs_review",
    "rejected",
}

VALID_CHUNK_LEVELS = {
    "article",
    "article_intro",
    "clause",
    "point",
}

SHORT_CHUNK_THRESHOLD = 20
MAX_CHUNK_CHARACTERS = 3500


class ValidationCollector:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.info: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warning(self, message: str) -> None:
        self.warnings.append(message)

    def add_info(self, message: str) -> None:
        self.info.append(message)


def normalize_text(value: Any) -> str:
    return re.sub(
        r"\s+",
        " ",
        str(value or ""),
    ).strip()


def parse_iso_date(
    value: str,
    *,
    field_name: str,
    context: str,
    collector: ValidationCollector,
    required: bool = False,
) -> date | None:
    value = value.strip()

    if not value:
        if required:
            collector.error(
                f"{context}: thiếu {field_name}"
            )
        return None

    try:
        return date.fromisoformat(value)
    except ValueError:
        collector.error(
            f"{context}: {field_name} không đúng YYYY-MM-DD: {value}"
        )
        return None


def read_registry(
    collector: ValidationCollector,
    path: Path | None = None,
) -> dict[str, dict[str, str]]:
    path = path or REGISTRY_PATH
    if not path.exists():
        collector.error(
            f"Không tìm thấy registry: {path}"
        )
        return {}

    required_columns = {
        "document_id",
        "document_number",
        "document_title",
        "document_type",
        "issuing_authority",
        "issued_date",
        "effective_from",
        "effective_to",
        "status",
        "corpus_layer",
        "official_source_url",
        "extraction_source_url",
        "official_pdf_path",
        "working_docx_path",
        "extraction_method",
        "official_pdf_hash",
        "working_docx_hash",
        "verification_status",
        "verified_by",
        "notes",
    }

    registry: dict[str, dict[str, str]] = {}

    with path.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as file:
        reader = csv.DictReader(file)

        fieldnames = set(reader.fieldnames or [])
        missing_columns = required_columns - fieldnames

        if missing_columns:
            collector.error(
                "documents.csv thiếu cột: "
                f"{sorted(missing_columns)}"
            )
            return {}

        for row_number, row in enumerate(
            reader,
            start=2,
        ):
            clean_row = {
                key: (value or "").strip()
                for key, value in row.items()
            }

            document_id = clean_row["document_id"]
            context = f"documents.csv dòng {row_number}"

            if not document_id:
                collector.error(
                    f"{context}: document_id trống"
                )
                continue

            if document_id in registry:
                collector.error(
                    f"{context}: document_id trùng: {document_id}"
                )
                continue

            registry[document_id] = clean_row

            required_text_fields = [
                "document_number",
                "document_title",
                "document_type",
                "issuing_authority",
                "status",
                "corpus_layer",
                "official_source_url",
                "official_pdf_path",
                "working_docx_path",
                "extraction_method",
                "verification_status",
            ]

            for field in required_text_fields:
                if not clean_row[field]:
                    collector.error(
                        f"{context} ({document_id}): thiếu {field}"
                    )

            if (
                clean_row["document_type"]
                and clean_row["document_type"]
                not in VALID_DOCUMENT_TYPES
            ):
                collector.error(
                    f"{context} ({document_id}): "
                    "document_type không hợp lệ: "
                    f"{clean_row['document_type']}"
                )

            if (
                clean_row["status"]
                and clean_row["status"]
                not in VALID_DOCUMENT_STATUSES
            ):
                collector.error(
                    f"{context} ({document_id}): "
                    f"status không hợp lệ: {clean_row['status']}"
                )

            if (
                clean_row["corpus_layer"]
                and clean_row["corpus_layer"]
                not in VALID_CORPUS_LAYERS
            ):
                collector.error(
                    f"{context} ({document_id}): "
                    "corpus_layer không hợp lệ: "
                    f"{clean_row['corpus_layer']}"
                )

            if (
                clean_row["verification_status"]
                and clean_row["verification_status"]
                not in VALID_VERIFICATION_STATUSES
            ):
                collector.error(
                    f"{context} ({document_id}): "
                    "verification_status không hợp lệ: "
                    f"{clean_row['verification_status']}"
                )

            issued_date = parse_iso_date(
                clean_row["issued_date"],
                field_name="issued_date",
                context=f"{context} ({document_id})",
                collector=collector,
                required=True,
            )

            effective_from = parse_iso_date(
                clean_row["effective_from"],
                field_name="effective_from",
                context=f"{context} ({document_id})",
                collector=collector,
                required=True,
            )

            effective_to = parse_iso_date(
                clean_row["effective_to"],
                field_name="effective_to",
                context=f"{context} ({document_id})",
                collector=collector,
            )

            if (
                issued_date
                and effective_from
                and effective_from < issued_date
            ):
                collector.warning(
                    f"{context} ({document_id}): "
                    "effective_from sớm hơn issued_date"
                )

            if (
                effective_from
                and effective_to
                and effective_to < effective_from
            ):
                collector.error(
                    f"{context} ({document_id}): "
                    "effective_to sớm hơn effective_from"
                )

            if not clean_row["official_pdf_hash"]:
                collector.warning(
                    f"{context} ({document_id}): "
                    "official_pdf_hash đang trống"
                )

            if not clean_row["working_docx_hash"]:
                collector.warning(
                    f"{context} ({document_id}): "
                    "working_docx_hash đang trống"
                )

            if (
                clean_row["verification_status"]
                in {"structure_verified", "content_verified", "verified"}
                and not clean_row["verified_by"]
            ):
                collector.warning(
                    f"{context} ({document_id}): "
                    "đã xác minh nhưng verified_by đang trống"
                )

    return registry


def read_jsonl(
    path: Path,
    *,
    label: str,
    collector: ValidationCollector,
) -> list[dict[str, Any]]:
    if not path.exists():
        collector.error(
            f"Không tìm thấy {label}: {path}"
        )
        return []

    rows: list[dict[str, Any]] = []

    with path.open("r", encoding="utf-8") as file:
        for line_number, raw_line in enumerate(
            file,
            start=1,
        ):
            line = raw_line.strip()

            if not line:
                collector.warning(
                    f"{label} dòng {line_number}: dòng trống"
                )
                continue

            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                collector.error(
                    f"{label} dòng {line_number}: JSON lỗi: {exc}"
                )
                continue

            if not isinstance(row, dict):
                collector.error(
                    f"{label} dòng {line_number}: "
                    "mỗi dòng phải là JSON object"
                )
                continue

            row["_jsonl_line"] = line_number
            rows.append(row)

    return rows


def validate_articles(
    articles: list[dict[str, Any]],
    registry: dict[str, dict[str, str]],
    collector: ValidationCollector,
) -> dict[str, dict[str, Any]]:
    article_by_id: dict[str, dict[str, Any]] = {}
    article_counts: Counter[str] = Counter()

    for article in articles:
        line_number = article.get("_jsonl_line")
        context = f"articles.jsonl dòng {line_number}"

        article_id = normalize_text(
            article.get("article_id")
        )
        document_id = normalize_text(
            article.get("document_id")
        )
        article_number = normalize_text(
            article.get("article")
        )

        if not article_id:
            collector.error(
                f"{context}: thiếu article_id"
            )
            continue

        if article_id in article_by_id:
            collector.error(
                f"{context}: article_id trùng: {article_id}"
            )
        else:
            article_by_id[article_id] = article

        if not document_id:
            collector.error(
                f"{context} ({article_id}): thiếu document_id"
            )
        elif document_id not in registry:
            collector.error(
                f"{context} ({article_id}): "
                f"document_id không có trong registry: {document_id}"
            )
        else:
            article_counts[document_id] += 1

        if not article_number:
            collector.error(
                f"{context} ({article_id}): thiếu article"
            )

        expected_article_id = (
            f"{document_id}_dieu-{article_number.lower()}"
            if document_id and article_number
            else ""
        )

        if (
            expected_article_id
            and article_id != expected_article_id
        ):
            collector.error(
                f"{context} ({article_id}): "
                "article_id không khớp document_id/article; "
                f"kỳ vọng {expected_article_id}"
            )

        if not normalize_text(
            article.get("document_number")
        ):
            collector.error(
                f"{context} ({article_id}): "
                "thiếu document_number"
            )

        if not normalize_text(
            article.get("document_title")
        ):
            collector.error(
                f"{context} ({article_id}): "
                "thiếu document_title"
            )

        if not normalize_text(
            article.get("article_title")
        ):
            collector.warning(
                f"{context} ({article_id}): "
                "article_title đang trống"
            )

        start_line = article.get("start_line")
        end_line = article.get("end_line")

        if not isinstance(start_line, int):
            collector.error(
                f"{context} ({article_id}): "
                "start_line không phải số nguyên"
            )

        if not isinstance(end_line, int):
            collector.error(
                f"{context} ({article_id}): "
                "end_line không phải số nguyên"
            )

        if (
            isinstance(start_line, int)
            and isinstance(end_line, int)
            and end_line < start_line
        ):
            collector.error(
                f"{context} ({article_id}): "
                "end_line nhỏ hơn start_line"
            )

        clauses = article.get("clauses")

        if clauses is None:
            clauses = []

        if not isinstance(clauses, list):
            collector.error(
                f"{context} ({article_id}): clauses không phải list"
            )
            clauses = []

        direct_points = article.get("direct_points")

        if direct_points is None:
            direct_points = []

        if not isinstance(direct_points, list):
            collector.error(
                f"{context} ({article_id}): "
                "direct_points không phải list"
            )
            direct_points = []

        clause_numbers: list[str] = []

        for clause in clauses:
            if not isinstance(clause, dict):
                collector.error(
                    f"{context} ({article_id}): "
                    "một clause không phải object"
                )
                continue

            clause_number = normalize_text(
                clause.get("clause")
            )

            if not clause_number:
                collector.error(
                    f"{context} ({article_id}): "
                    "clause thiếu số"
                )
                continue

            clause_numbers.append(clause_number)

            points = clause.get("points") or []

            if not isinstance(points, list):
                collector.error(
                    f"{context} ({article_id}, khoản "
                    f"{clause_number}): points không phải list"
                )
                continue

            point_numbers: list[str] = []

            for point in points:
                if not isinstance(point, dict):
                    collector.error(
                        f"{context} ({article_id}, khoản "
                        f"{clause_number}): point không phải object"
                    )
                    continue

                point_number = normalize_text(
                    point.get("point")
                ).lower()

                if not point_number:
                    collector.error(
                        f"{context} ({article_id}, khoản "
                        f"{clause_number}): point thiếu ký hiệu"
                    )
                    continue

                point_numbers.append(point_number)

            duplicate_points = sorted(
                point
                for point, count in Counter(
                    point_numbers
                ).items()
                if count > 1
            )

            if duplicate_points:
                collector.error(
                    f"{context} ({article_id}, khoản "
                    f"{clause_number}): point trùng: "
                    f"{duplicate_points}"
                )

        duplicate_clauses = sorted(
            clause
            for clause, count in Counter(
                clause_numbers
            ).items()
            if count > 1
        )

        if duplicate_clauses:
            collector.error(
                f"{context} ({article_id}): "
                f"khoản trùng: {duplicate_clauses}"
            )

        direct_point_numbers = [
            normalize_text(point.get("point")).lower()
            for point in direct_points
            if isinstance(point, dict)
        ]

        duplicate_direct_points = sorted(
            point
            for point, count in Counter(
                direct_point_numbers
            ).items()
            if point and count > 1
        )

        if duplicate_direct_points:
            collector.error(
                f"{context} ({article_id}): "
                "direct point trùng: "
                f"{duplicate_direct_points}"
            )

    for document_id, expected_count in (
        EXPECTED_ARTICLE_COUNTS.items()
    ):
        actual_count = article_counts.get(
            document_id,
            0,
        )

        if actual_count != expected_count:
            collector.error(
                f"{document_id}: số Điều {actual_count}, "
                f"kỳ vọng {expected_count}"
            )
        else:
            collector.add_info(
                f"{document_id}: đủ {actual_count} Điều"
            )

    for document_id in registry:
        if article_counts.get(document_id, 0) == 0:
            collector.error(
                f"{document_id}: không có Article nào"
            )

    return article_by_id


def validate_chunks(
    chunks: list[dict[str, Any]],
    registry: dict[str, dict[str, str]],
    article_by_id: dict[str, dict[str, Any]],
    collector: ValidationCollector,
) -> dict[str, Any]:
    chunk_by_id: dict[str, dict[str, Any]] = {}
    document_chunk_counts: Counter[str] = Counter()
    corpus_versions: set[str] = set()
    exact_text_groups: dict[
        tuple[str, str],
        list[str],
    ] = defaultdict(list)

    short_chunk_ids: list[str] = []
    long_chunk_ids: list[str] = []

    for chunk in chunks:
        line_number = chunk.get("_jsonl_line")
        context = f"chunks.jsonl dòng {line_number}"

        chunk_id = normalize_text(
            chunk.get("chunk_id")
        )
        document_id = normalize_text(
            chunk.get("document_id")
        )
        article_number = normalize_text(
            chunk.get("article")
        )
        clause_number = normalize_text(
            chunk.get("clause")
        )
        point_number = normalize_text(
            chunk.get("point")
        ).lower()
        chunk_level = normalize_text(
            chunk.get("chunk_level")
        )
        text = normalize_text(chunk.get("text"))
        retrieval_text = normalize_text(
            chunk.get("retrieval_text")
        )
        structure_path_text = normalize_text(
            chunk.get("structure_path_text")
        )
        corpus_version = normalize_text(
            chunk.get("corpus_version")
        )

        if not chunk_id:
            collector.error(
                f"{context}: thiếu chunk_id"
            )
            continue

        if chunk_id in chunk_by_id:
            collector.error(
                f"{context}: chunk_id trùng: {chunk_id}"
            )
        else:
            chunk_by_id[chunk_id] = chunk

        required_fields = [
            "document_number",
            "document_title",
            "document_type",
            "issuing_authority",
            "issued_date",
            "effective_from",
            "status",
            "corpus_layer",
            "article",
            "chunk_level",
            "text",
            "retrieval_text",
            "parent_context",
            "structure_path_text",
            "official_source_url",
            "official_pdf_path",
            "working_docx_path",
            "extraction_method",
            "verification_status",
            "corpus_version",
        ]

        for field in required_fields:
            if not normalize_text(chunk.get(field)):
                collector.error(
                    f"{context} ({chunk_id}): thiếu {field}"
                )

        if document_id not in registry:
            collector.error(
                f"{context} ({chunk_id}): "
                f"document_id không có trong registry: {document_id}"
            )
        else:
            document_chunk_counts[document_id] += 1
            registry_row = registry[document_id]

            matching_fields = [
                "document_number",
                "document_title",
                "document_type",
                "issuing_authority",
                "issued_date",
                "effective_from",
                "effective_to",
                "status",
                "corpus_layer",
                "official_source_url",
                "official_pdf_path",
                "working_docx_path",
                "extraction_method",
                "verification_status",
            ]

            for field in matching_fields:
                chunk_value = normalize_text(
                    chunk.get(field)
                )
                registry_value = normalize_text(
                    registry_row.get(field)
                )

                if chunk_value != registry_value:
                    collector.error(
                        f"{context} ({chunk_id}): "
                        f"{field} không khớp documents.csv"
                    )

        article_id = (
            f"{document_id}_dieu-{article_number.lower()}"
            if document_id and article_number
            else ""
        )

        if not article_id:
            collector.error(
                f"{context} ({chunk_id}): "
                "không tạo được article_id tham chiếu"
            )
        elif article_id not in article_by_id:
            collector.error(
                f"{context} ({chunk_id}): "
                f"không tìm thấy Article cha {article_id}"
            )

        if chunk_level not in VALID_CHUNK_LEVELS:
            collector.error(
                f"{context} ({chunk_id}): "
                f"chunk_level không hợp lệ: {chunk_level}"
            )

        if chunk_level in {"article", "article_intro"}:
            if clause_number or point_number:
                collector.error(
                    f"{context} ({chunk_id}): "
                    "chunk cấp Điều không được có clause/point"
                )

        if chunk_level == "clause":
            if not clause_number:
                collector.error(
                    f"{context} ({chunk_id}): "
                    "chunk cấp clause thiếu clause"
                )

            if point_number:
                collector.error(
                    f"{context} ({chunk_id}): "
                    "chunk cấp clause không được có point"
                )

        if chunk_level == "point":
            if not point_number:
                collector.error(
                    f"{context} ({chunk_id}): "
                    "chunk cấp point thiếu point"
                )

        if not text:
            collector.error(
                f"{context} ({chunk_id}): text rỗng"
            )

        if not retrieval_text:
            collector.error(
                f"{context} ({chunk_id}): retrieval_text rỗng"
            )
        elif text and text not in retrieval_text:
            collector.error(
                f"{context} ({chunk_id}): "
                "retrieval_text không chứa nguyên text"
            )

        if (
            structure_path_text
            and f"Điều {article_number}"
            not in structure_path_text
        ):
            collector.error(
                f"{context} ({chunk_id}): "
                "structure_path_text không chứa Điều tương ứng"
            )

        if (
            chunk_level == "clause"
            and f"Khoản {clause_number}"
            not in structure_path_text
        ):
            collector.error(
                f"{context} ({chunk_id}): "
                "structure_path_text thiếu Khoản"
            )

        if (
            chunk_level == "point"
            and f"Điểm {point_number}"
            not in structure_path_text
        ):
            collector.error(
                f"{context} ({chunk_id}): "
                "structure_path_text thiếu Điểm"
            )

        if corpus_version:
            corpus_versions.add(corpus_version)

        text_length = len(text)

        if text_length < SHORT_CHUNK_THRESHOLD:
            short_chunk_ids.append(chunk_id)

        if text_length > MAX_CHUNK_CHARACTERS:
            long_chunk_ids.append(chunk_id)

        if text:
            exact_text_groups[
                (document_id, text)
            ].append(chunk_id)

        segment_index = chunk.get("segment_index")
        segment_count = chunk.get("segment_count")

        if not isinstance(segment_index, int):
            collector.error(
                f"{context} ({chunk_id}): "
                "segment_index không phải số nguyên"
            )

        if not isinstance(segment_count, int):
            collector.error(
                f"{context} ({chunk_id}): "
                "segment_count không phải số nguyên"
            )

        if (
            isinstance(segment_index, int)
            and isinstance(segment_count, int)
        ):
            if segment_index < 1:
                collector.error(
                    f"{context} ({chunk_id}): "
                    "segment_index phải >= 1"
                )

            if segment_count < 1:
                collector.error(
                    f"{context} ({chunk_id}): "
                    "segment_count phải >= 1"
                )

            if segment_index > segment_count:
                collector.error(
                    f"{context} ({chunk_id}): "
                    "segment_index lớn hơn segment_count"
                )

        parse_iso_date(
            normalize_text(chunk.get("issued_date")),
            field_name="issued_date",
            context=f"{context} ({chunk_id})",
            collector=collector,
            required=True,
        )

        effective_from = parse_iso_date(
            normalize_text(chunk.get("effective_from")),
            field_name="effective_from",
            context=f"{context} ({chunk_id})",
            collector=collector,
            required=True,
        )

        effective_to = parse_iso_date(
            normalize_text(chunk.get("effective_to")),
            field_name="effective_to",
            context=f"{context} ({chunk_id})",
            collector=collector,
        )

        if (
            effective_from
            and effective_to
            and effective_to < effective_from
        ):
            collector.error(
                f"{context} ({chunk_id}): "
                "effective_to sớm hơn effective_from"
            )

    if len(corpus_versions) == 0:
        collector.error(
            "Không tìm thấy corpus_version trong chunks"
        )
    elif len(corpus_versions) > 1:
        collector.error(
            "Corpus chứa nhiều version: "
            f"{sorted(corpus_versions)}"
        )
    else:
        collector.add_info(
            f"Corpus version: {next(iter(corpus_versions))}"
        )

    for document_id in registry:
        if document_chunk_counts.get(document_id, 0) == 0:
            collector.error(
                f"{document_id}: không có Chunk nào"
            )
        else:
            collector.add_info(
                f"{document_id}: "
                f"{document_chunk_counts[document_id]} Chunk"
            )

    if short_chunk_ids:
        collector.warning(
            f"{len(short_chunk_ids)} chunk ngắn hơn "
            f"{SHORT_CHUNK_THRESHOLD} ký tự: "
            f"{short_chunk_ids}"
        )

    if long_chunk_ids:
        collector.error(
            f"{len(long_chunk_ids)} chunk dài hơn "
            f"{MAX_CHUNK_CHARACTERS} ký tự: "
            f"{long_chunk_ids}"
        )

    exact_duplicate_text_groups = {
        key: ids
        for key, ids in exact_text_groups.items()
        if len(ids) > 1
    }

    for (document_id, text), chunk_ids in sorted(
        exact_duplicate_text_groups.items(),
        key=lambda item: item[0][0],
    ):
        collector.warning(
            f"{document_id}: text trùng nguyên văn ở "
            f"{chunk_ids}; text='{text[:100]}'"
        )

    return {
        "chunk_count": len(chunks),
        "chunk_id_count": len(chunk_by_id),
        "document_chunk_counts": dict(
            document_chunk_counts
        ),
        "corpus_versions": sorted(corpus_versions),
        "short_chunk_ids": short_chunk_ids,
        "long_chunk_ids": long_chunk_ids,
        "exact_duplicate_text_group_count": len(
            exact_duplicate_text_groups
        ),
    }


def validate_corpus(
    *,
    registry_path: str | Path = REGISTRY_PATH,
    articles_path: str | Path = ARTICLES_PATH,
    chunks_path: str | Path = CHUNKS_PATH,
) -> tuple[ValidationCollector, dict[str, Any]]:
    """Run legacy corpus checks without writing reports or exiting the process."""
    collector = ValidationCollector()
    registry = read_registry(collector, Path(registry_path))
    articles = read_jsonl(
        Path(articles_path), label="articles.jsonl", collector=collector
    )
    chunks = read_jsonl(
        Path(chunks_path), label="chunks.jsonl", collector=collector
    )
    article_by_id = validate_articles(articles, registry, collector)
    chunk_stats = validate_chunks(
        chunks, registry, article_by_id, collector
    )
    return collector, chunk_stats
