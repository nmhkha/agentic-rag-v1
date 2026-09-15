#!/usr/bin/env python3
"""Strict validation of model-generated evidence citations."""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass
from typing import Any

VALID_CITATION = re.compile(r"\[E([1-9][0-9]*)\]")
BRACKETED_E_LIKE = re.compile(r"\[[eE][^\]]*\]")


@dataclass(frozen=True)
class CitationValidation:
    valid: bool
    cited_evidence_ids: list[str]
    unknown_citations: list[str]
    malformed_citations: list[str]
    duplicate_citations: list[str]
    errors: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def validate_citations(
    answer: str,
    citation_map: dict[str, Any],
    used_evidence_ids: list[str] | None = None,
) -> CitationValidation:
    tokens = [f"E{number}" for number in VALID_CITATION.findall(answer)]
    malformed = [item for item in BRACKETED_E_LIKE.findall(answer)
                 if not VALID_CITATION.fullmatch(item)]
    unknown = list(dict.fromkeys(token for token in tokens if token not in citation_map))
    cited = list(dict.fromkeys(tokens))
    # Reusing evidence for separate claims is valid. Keep this field for API
    # compatibility; only genuinely invalid duplicate forms should populate it.
    duplicate: list[str] = []
    errors: list[str] = []
    if unknown:
        errors.append("Unknown citation(s): " + ", ".join(unknown))
    if malformed:
        errors.append("Malformed citation(s): " + ", ".join(malformed))
    if used_evidence_ids is not None and set(used_evidence_ids) != set(cited):
        errors.append("used_evidence_ids does not match citations in answer")
    return CitationValidation(not errors, cited, unknown, malformed, duplicate, errors)
