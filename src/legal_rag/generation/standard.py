#!/usr/bin/env python3
"""Single-shot legal-rag-v0 runtime (no agentic behavior)."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ..llm_client import LLMClient
from ..paths import GENERATION_TRACE_DIR, PROMPT_DIR, REPOSITORY_ROOT
from ..retrieval.pipeline import DEFAULT_TOP_K, RetrievalPipeline, retrieval_config
from .answerer import generate_answer
from .evidence import format_evidence
from .formatter import parse_model_output
from .verifier import validate_citations

ROOT = REPOSITORY_ROOT
PROMPT_PATH = PROMPT_DIR / "legal_rag_v0.txt"
TRACE_DIR = GENERATION_TRACE_DIR
RAG_VERSION = "legal-rag-v0"
PROMPT_VERSION = "legal-rag-prompt-v0"


def run_rag(query: str, pipeline: RetrievalPipeline, client: LLMClient) -> dict[str, Any]:
    evidences = pipeline.retrieve(query, DEFAULT_TOP_K)
    context, citation_map = format_evidence(evidences)
    prompt, raw = generate_answer(query, context, client, prompt_path=PROMPT_PATH)
    parsed = parse_model_output(raw)
    validation = validate_citations(
        parsed["answer"], citation_map, parsed["used_evidence_ids"]
    )
    validation_dict = validation.to_dict()
    return {
        "query": query, "evidences": evidences, "evidence_context": context,
        "citation_map": citation_map, "prompt": prompt, "raw_model_response": raw,
        "parsed_result": parsed, "citation_validation": validation_dict,
    }


def make_trace(run: dict[str, Any]) -> dict[str, Any]:
    evidences = run["evidences"]
    return {
        "query": run["query"],
        "retrieval_config": retrieval_config(),
        "retrieved_chunk_ids": [item.chunk_id for item in evidences],
        "reranker_scores": [item.reranker_score for item in evidences],
        "formatted_evidence_ids": [item.evidence_id for item in evidences],
        "model": os.getenv("RAG_LLM_MODEL", ""),
        "provider": os.getenv("RAG_LLM_PROVIDER", "openai-compatible"),
        "prompt_version": PROMPT_VERSION,
        "raw_model_response": run["raw_model_response"],
        "parsed_result": run["parsed_result"],
        "citation_validation": run["citation_validation"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


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
