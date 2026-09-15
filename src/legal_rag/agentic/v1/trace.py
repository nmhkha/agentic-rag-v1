"""Agentic v1 trace construction, guards, and persistence."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ...generation.standard import PROMPT_VERSION
from ...llm_client import LLMClient
from ...paths import GENERATION_TRACE_DIR, REPOSITORY_ROOT
from ...retrieval.pipeline import retrieval_config
from .policies import (
    EXPECTED_LLM_MODEL, MAX_ANSWER_REVISIONS, MAX_CITATION_REVISIONS,
    MAX_LLM_CALLS, MAX_RETRIEVAL_EXPANSIONS, MAX_SUB_QUERIES,
)
from .state import AgentState

ROOT = REPOSITORY_ROOT
TRACE_DIR = GENERATION_TRACE_DIR
RAG_VERSION = "agentic-rag-v1"


def trace_for_state(state: AgentState, client: LLMClient | None) -> dict[str, Any]:
    value = state.to_dict()
    return {
        "run_id": state.run_id,
        "query": state.query,
        "retrieval_config": retrieval_config(),
        "prompt_version": PROMPT_VERSION,
        "model": getattr(client, "model", os.getenv("RAG_LLM_MODEL", "")),
        "provider": os.getenv("RAG_LLM_PROVIDER", "openai-compatible"),
        "initial_candidate_count": (
            state.retrieval_calls[0].get("candidate_count", 0)
            if state.retrieval_calls else 0
        ),
        "initial_top5": state.initial_top5,
        "coverage_check": value["coverage_check"],
        "missing_aspects": state.missing_aspects,
        "sub_queries": state.sub_queries,
        "expansion_used": state.expansion_used,
        "expansion_candidates": state.expanded_candidates,
        "final_evidence": value["current_evidence"],
        "final_top5": state.final_top5,
        "draft_answer": state.draft_answer,
        "completeness_check": value["completeness_check"],
        "revision_used": state.revision_used,
        "citation_check": value["citation_check"],
        "citation_revision_used": state.citation_revision_used,
        "final_answer": state.final_answer,
        "final_status": state.final_status,
        "retrieval_calls": state.retrieval_calls,
        "retrieval_call_count": len(state.retrieval_calls),
        "llm_calls": state.llm_calls,
        "llm_call_count": len(state.llm_calls),
        "budgets": {
            "max_retrieval_expansions": MAX_RETRIEVAL_EXPANSIONS,
            "max_sub_queries": MAX_SUB_QUERIES,
            "max_answer_revisions": MAX_ANSWER_REVISIONS,
            "max_citation_revisions": MAX_CITATION_REVISIONS,
            "max_llm_calls": MAX_LLM_CALLS,
        },
        "state": value,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def require_expected_model(client: LLMClient) -> None:
    model = str(getattr(client, "model", "")).strip()
    if model != EXPECTED_LLM_MODEL:
        raise RuntimeError(
            f"Agentic RAG v1 requires RAG_LLM_MODEL={EXPECTED_LLM_MODEL}; got {model or '<empty>'}"
        )


def record_execution_error(state: AgentState, exc: Exception) -> None:
    state.final_status = "execution_error"
    state.execution_error = {"type": type(exc).__name__, "message": str(exc)}
    final_transition = "final:execution_error"
    if not state.transitions or state.transitions[-1] != final_transition:
        state.transitions.append(final_transition)


def write_trace(trace: dict[str, Any], target: Path | None = None) -> Path:
    TRACE_DIR.mkdir(parents=True, exist_ok=True)
    if target is None:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
        target = TRACE_DIR / f"{RAG_VERSION}_{stamp}.json"
    elif not target.is_absolute():
        target = ROOT / target
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(trace, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return target
