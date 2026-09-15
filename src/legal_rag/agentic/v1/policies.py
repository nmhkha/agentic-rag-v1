"""Frozen budgets and deterministic Agentic RAG v1 transition policies."""

from __future__ import annotations

from dataclasses import dataclass

EXPECTED_LLM_MODEL = "gemini-3.5-flash-lite"
MAX_SUB_QUERIES = 3
MAX_RETRIEVAL_EXPANSIONS = 1
MAX_ANSWER_REVISIONS = 1
MAX_CITATION_REVISIONS = 1
MAX_LLM_CALLS = 6


@dataclass(frozen=True)
class AgenticConfig:
    enable_expansion: bool = True
    enable_answer_revision: bool = True
    enable_citation_revision: bool = True


def expansion_allowed(enabled: bool, sufficient: bool, missing_aspects: list[str]) -> bool:
    return bool(enabled and not sufficient and missing_aspects and MAX_RETRIEVAL_EXPANSIONS > 0)


def answer_revision_allowed(enabled: bool, complete: bool, revision_count: int) -> bool:
    return not complete and enabled and revision_count < MAX_ANSWER_REVISIONS


def citation_revision_allowed(enabled: bool, valid: bool, revision_count: int) -> bool:
    return not valid and enabled and revision_count < MAX_CITATION_REVISIONS


def llm_call_allowed(call_count: int) -> bool:
    return call_count < MAX_LLM_CALLS


def determine_final_status(
    *, citation_valid: bool, coverage_sufficient: bool,
    completeness_complete: bool, expansion_used: bool,
    answer_declares_insufficient: bool,
) -> str:
    if not citation_valid:
        return "citation_check_failed"
    if not coverage_sufficient and not completeness_complete:
        return "insufficient_evidence"
    if not completeness_complete:
        return "incomplete_answer"
    if not coverage_sufficient and not expansion_used:
        return "insufficient_evidence"
    if answer_declares_insufficient and not coverage_sufficient:
        return "insufficient_evidence"
    return "success"
