#!/usr/bin/env python3
"""Generation context and citation-map formatting."""

from __future__ import annotations

from typing import Any, Iterable

from ..retrieval.pipeline import Evidence


def _extract_parent_leads(
    parent_context: str | None, body_text: str = ""
) -> tuple[str | None, str | None]:
    """Extract (article_intro, clause_lead) from parent_context when not redundant."""
    if not parent_context:
        return None, None
    article_intro: str | None = None
    clause_lead: str | None = None
    norm_body = body_text.strip()
    for raw_line in parent_context.splitlines():
        line = raw_line.strip()
        if line.startswith("Mở đầu điều:"):
            val = line[len("Mở đầu điều:") :].strip()
            if val and val != norm_body:
                article_intro = val
        elif line.startswith("Nội dung dẫn của khoản:"):
            val = line[len("Nội dung dẫn của khoản:") :].strip()
            if val and val != norm_body:
                clause_lead = val
    return article_intro, clause_lead


def format_evidence(evidences: Iterable[Evidence]) -> tuple[str, dict[str, dict[str, Any]]]:
    blocks: list[str] = []
    citation_map: dict[str, dict[str, Any]] = {}
    for evidence in evidences:
        article_intro, clause_lead = _extract_parent_leads(
            getattr(evidence, "parent_context", None), evidence.text
        )
        fields = [
            ("Văn bản", evidence.document_title),
            ("Số văn bản", evidence.document_number),
            ("Điều", evidence.article_label),
            ("Mở đầu điều", article_intro),
            ("Khoản", evidence.clause_label),
            ("Nội dung dẫn của khoản", clause_lead),
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
