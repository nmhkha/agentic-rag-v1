#!/usr/bin/env python3
"""Generation context and citation-map formatting."""

from __future__ import annotations

from typing import Any, Iterable

from ..retrieval.pipeline import Evidence


def format_evidence(evidences: Iterable[Evidence]) -> tuple[str, dict[str, dict[str, Any]]]:
    blocks: list[str] = []
    citation_map: dict[str, dict[str, Any]] = {}
    for evidence in evidences:
        fields = [
            ("Văn bản", evidence.document_title),
            ("Số văn bản", evidence.document_number),
            ("Điều", evidence.article_label),
            ("Khoản", evidence.clause_label),
            ("Điểm", evidence.point_label),
            ("Nguồn chính thức", evidence.official_source_url),
        ]
        metadata = [f"{label}: {value}" for label, value in fields if value not in (None, "")]
        blocks.append("\n".join([f"[{evidence.evidence_id}]", *metadata, "", "Nội dung:", evidence.text]))
        citation_map[evidence.evidence_id] = {
            "chunk_id": evidence.chunk_id,
            "document_number": evidence.document_number,
            "article": evidence.article,
            "clause": evidence.clause,
            "point": evidence.point,
            "official_source_url": evidence.official_source_url,
        }
    return "\n\n".join(blocks), citation_map
