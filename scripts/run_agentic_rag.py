#!/usr/bin/env python3
"""Run packaged Agentic RAG v1 with the existing retrieval and LLM clients."""

from __future__ import annotations

import argparse
import json
import sys
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="agentic-rag-v1")
    parser.add_argument("--query", required=True)
    parser.add_argument("--batch-size", type=int)
    parser.add_argument("--trace", nargs="?", const="", metavar="PATH")
    parser.add_argument("--debug", action="store_true")
    parser.add_argument(
        "--no-practical",
        dest="practical",
        action="store_false",
        default=True,
        help="Bypass practical router and run direct agentic v1",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    from legal_rag.agentic.v1 import AgentState, run_agentic_rag, trace_for_state, write_trace
    from legal_rag.agentic.v1.trace import record_execution_error, require_expected_model
    from legal_rag.generation import format_evidence, format_final_response
    from legal_rag.llm_client import LLMClient, client_from_env
    from legal_rag.retrieval import RetrievalPipeline

    client: LLMClient | None = None
    state = AgentState(query=args.query.strip(), run_id=uuid.uuid4().hex)
    error: Exception | None = None
    trace_payload: dict | None = None
    try:
        if args.practical:
            from legal_rag.document_scoped_search import DocumentScopedSearchResult
            from legal_rag.exact_lookup import ExactLookupResult
            from legal_rag.navigation import NavigationResult
            from legal_rag.practical import run_practical_rag

            # Fast path: deterministic navigation and exact lookup require neither pipeline nor LLM
            route_result = run_practical_rag(args.query)
            if not getattr(route_result, "handled", False):
                client = client_from_env()
                require_expected_model(client)
                pipeline = RetrievalPipeline(batch_size=args.batch_size)
                route_result = run_practical_rag(
                    args.query,
                    pipeline,
                    client,
                    run_id=state.run_id,
                    state=state,
                )

            if isinstance(route_result, (NavigationResult, ExactLookupResult, DocumentScopedSearchResult)):
                final_status = "success" if route_result.status == "SUCCESS" else "insufficient_evidence"
                state.final_answer = getattr(route_result, "message", None) or getattr(route_result, "content", "")
                state.final_status = final_status
                if isinstance(route_result, DocumentScopedSearchResult) and route_result.results:
                    state.current_evidence = [item.evidence for item in route_result.results]
                    state.final_top5 = [item.chunk_id for item in route_result.results]
                trace_payload = trace_for_state(state, client)
                trace_payload.update({
                    "route": getattr(route_result, "route", type(route_result).__name__),
                    "status": route_result.status,
                    "intent": getattr(route_result, "intent", None),
                })
            else:
                state = route_result
        else:
            client = client_from_env()
            require_expected_model(client)
            pipeline = RetrievalPipeline(batch_size=args.batch_size)
            state = run_agentic_rag(
                args.query,
                pipeline,
                client,
                run_id=state.run_id,
                state=state,
            )
    except Exception as exc:
        error = exc
        record_execution_error(state, exc)
    target = Path(args.trace) if args.trace else None
    trace_to_write = trace_payload if trace_payload is not None else trace_for_state(state, client)
    trace_path = write_trace(trace_to_write, target)
    if error is not None:
        print(f"ERROR: {error}", file=sys.stderr)
        print(f"Trace: {trace_path}", file=sys.stderr)
        return 2
    if args.debug:
        print(json.dumps(trace_to_write, ensure_ascii=False, indent=2))
    else:
        if state.citation_check.cited_evidence_ids and state.current_evidence:
            citation_map = format_evidence(state.current_evidence)[1]
            print(format_final_response(
                state.final_answer or "",
                state.citation_check.cited_evidence_ids,
                citation_map,
            ))
        else:
            print(state.final_answer or "")
    print(f"\nStatus: {state.final_status}")
    print(f"Trace: {trace_path}")
    return 3 if state.final_status == "citation_check_failed" else 0


if __name__ == "__main__":
    raise SystemExit(main())
