#!/usr/bin/env python3
"""Run the practical router; scoped searches use frozen local retrieval assets."""

from __future__ import annotations

import argparse
import os
import sys
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the practical legal router and v1 fallback.")
    parser.add_argument("--query", required=True)
    args = parser.parse_args()

    from legal_rag.document_scoped_search import (
        DOCUMENT_SCOPED_SEARCH,
        detect_document_scoped_search,
        try_document_scoped_search,
    )
    from legal_rag.exact_lookup import try_exact_lookup
    from legal_rag.navigation import try_document_navigation

    result = try_document_navigation(args.query)
    route = "DOCUMENT_NAVIGATION"
    if not result.handled:
        result = try_exact_lookup(args.query)
        route = "EXACT_LEGAL_LOOKUP"
    if not result.handled:
        scoped = detect_document_scoped_search(args.query)
        if scoped.intent == DOCUMENT_SCOPED_SEARCH:
            # Use the default corpus-v2.1 RetrievalPipeline. Models are loaded
            # locally; this makes no API call.
            os.environ["HF_HUB_OFFLINE"] = "1"
            os.environ["TRANSFORMERS_OFFLINE"] = "1"
            from legal_rag.retrieval.pipeline import RetrievalPipeline

            result = try_document_scoped_search(args.query, RetrievalPipeline())
            route = DOCUMENT_SCOPED_SEARCH
        else:
            route = "V1_RAG"
            return _run_practical_v1(args.query)
    print("ROUTE")
    print(route)
    print("\nINTENT")
    print(result.intent)
    print("\nSTATUS")
    print(result.status)
    print("\nDOCUMENT")
    print(result.document_title or "NOT_AVAILABLE")
    print(result.document_number or "NOT_AVAILABLE")
    if route == DOCUMENT_SCOPED_SEARCH:
        print("\nSCOPED QUERY")
        print(result.scoped_query or "NOT_AVAILABLE")
    print("\nARTICLE")
    print(getattr(result, "article", None) or "NOT_AVAILABLE")
    if getattr(result, "clause", None):
        print("\nCLAUSE")
        print(result.clause)
    if getattr(result, "point", None):
        print("\nPOINT")
        print(result.point)
    print("\nRETRIEVAL CALLS")
    print(getattr(result, "retrieval_call_count", 0))
    print("\nLLM CALLS")
    print(getattr(result, "llm_call_count", 0))
    if route == DOCUMENT_SCOPED_SEARCH:
        print("\nRESULTS")
        if not result.results:
            print("NO_RESULTS")
        for item in result.results:
            print(
                f"- rank={item.rank} chunk_id={item.chunk_id} "
                f"document_id={item.document_id} article_id={item.article_id} "
                f"clause={item.clause or '-'} point={item.point or '-'} "
                f"bm25_rank={item.bm25_rank} dense_rank={item.dense_rank} "
                f"reranker_score={item.reranker_score:.6f}"
            )
    print("\nANSWER")
    print(result.message or "Forward to the existing v1 RAG workflow.")
    return 0


def _run_practical_v1(query: str) -> int:
    """Run the practical v1 fallback and print its evidence-selection trace."""
    os.environ["HF_HUB_OFFLINE"] = "1"
    os.environ["TRANSFORMERS_OFFLINE"] = "1"
    from legal_rag.agentic.v1 import (
        GAP_PRESERVING_V1_PRACTICAL_V1,
        run_agentic_rag,
        trace_for_state,
    )
    from legal_rag.agentic.v1.trace import require_expected_model
    from legal_rag.llm_client import client_from_env
    from legal_rag.retrieval.pipeline import RetrievalPipeline

    pipeline = RetrievalPipeline()
    client = client_from_env()
    require_expected_model(client)
    state = run_agentic_rag(
        query,
        pipeline,
        client,
        final_evidence_policy=GAP_PRESERVING_V1_PRACTICAL_V1,
    )
    trace = trace_for_state(state, client)

    print("ROUTE\nV1_RAG")
    print("\nV1 PRACTICAL EVIDENCE POLICY\nGAP_PRESERVING")
    print("\ncoverage gaps:")
    print(json.dumps(state.missing_aspects, ensure_ascii=False, indent=2))
    print("\nexpansion reservations:")
    print(json.dumps(state.expansion_reservations, ensure_ascii=False, indent=2))
    print("\nfinal Top5:")
    print(json.dumps([
        {
            "rank": item.rank,
            "chunk_id": item.chunk_id,
            "evidence_id": item.evidence_id,
            "selection": selection,
        }
        for item, selection in zip(state.current_evidence, state.final_evidence_selection)
    ], ensure_ascii=False, indent=2))
    print("\nanswer:")
    print(state.final_answer or "NOT_AVAILABLE")
    print(f"\nretrieval calls: {trace['retrieval_call_count']}")
    print(f"LLM calls: {trace['llm_call_count']}")
    return 3 if state.final_status == "citation_check_failed" else 0


if __name__ == "__main__":
    raise SystemExit(main())
