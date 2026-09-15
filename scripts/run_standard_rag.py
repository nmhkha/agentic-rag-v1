#!/usr/bin/env python3
"""Run the packaged single-shot Standard RAG runtime."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="legal-rag-v0")
    parser.add_argument("--query", required=True)
    parser.add_argument("--batch-size", type=int)
    parser.add_argument("--show-evidence", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    from legal_rag.generation import format_final_response, run_rag
    from legal_rag.llm_client import client_from_env
    from legal_rag.retrieval import RetrievalPipeline

    try:
        run = run_rag(
            args.query,
            RetrievalPipeline(batch_size=args.batch_size),
            client_from_env(),
        )
    except (RuntimeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if args.show_evidence:
        print("RETRIEVED EVIDENCE:\n" + run["evidence_context"] + "\n")
    validation = run["citation_validation"]
    if not validation["valid"]:
        print("CITATION VALIDATION: FAIL", file=sys.stderr)
        for error in validation["errors"]:
            print(error, file=sys.stderr)
        return 3
    print(
        format_final_response(
            run["parsed_result"]["answer"],
            validation["cited_evidence_ids"],
            run["citation_map"],
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
