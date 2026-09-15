"""Agentic RAG v1 runtime state and result structures."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any

from ...generation.verifier import CitationValidation
from ...retrieval.pipeline import Evidence


@dataclass
class CoverageCheck:
    sufficient: bool = False
    missing_aspects: list[str] = field(default_factory=list)
    reason: str = ""


@dataclass
class CompletenessCheck:
    complete: bool = False
    missing_points: list[str] = field(default_factory=list)
    reason: str = ""


@dataclass
class CitationCheck:
    valid: bool = False
    cited_evidence_ids: list[str] = field(default_factory=list)
    unknown_citations: list[str] = field(default_factory=list)
    malformed_citations: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    alignment_checked: bool = False
    alignment_method: str = "not_required"
    alignment_reason: str = ""
    reviewed_claims: list[str] = field(default_factory=list)

    @classmethod
    def from_validation(cls, value: CitationValidation) -> "CitationCheck":
        return cls(
            valid=value.valid,
            cited_evidence_ids=value.cited_evidence_ids,
            unknown_citations=value.unknown_citations,
            malformed_citations=value.malformed_citations,
            errors=value.errors,
        )


@dataclass
class AgentState:
    query: str
    initial_evidence: list[Evidence] = field(default_factory=list)
    current_evidence: list[Evidence] = field(default_factory=list)
    retrieval_round: int = 0
    coverage_check: CoverageCheck = field(default_factory=CoverageCheck)
    missing_aspects: list[str] = field(default_factory=list)
    sub_queries: list[str] = field(default_factory=list)
    expansion_evidence: list[Evidence] = field(default_factory=list)
    draft_answer: str | None = None
    completeness_check: CompletenessCheck = field(default_factory=CompletenessCheck)
    citation_check: CitationCheck = field(default_factory=CitationCheck)
    revision_count: int = 0
    citation_revision_count: int = 0
    final_answer: str | None = None
    final_status: str = "not_started"
    run_id: str = ""
    initial_top5: list[str] = field(default_factory=list)
    expanded_candidates: list[str] = field(default_factory=list)
    final_top5: list[str] = field(default_factory=list)
    retrieval_calls: list[dict[str, Any]] = field(default_factory=list)
    llm_calls: list[dict[str, Any]] = field(default_factory=list)
    expansion_used: bool = False
    revision_used: bool = False
    citation_revision_used: bool = False
    execution_error: dict[str, str] | None = None
    transitions: list[str] = field(default_factory=lambda: ["initialized"])

    def to_dict(self) -> dict[str, Any]:
        value = asdict(self)
        for key in ("initial_evidence", "current_evidence", "expansion_evidence"):
            value[key] = [item.to_dict() for item in getattr(self, key)]
        return value
