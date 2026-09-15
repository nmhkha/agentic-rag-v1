#!/usr/bin/env python3
"""Unified evaluation CLI with a zero-inference score-only mode."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from legal_rag.evaluation import PIPELINES, run_evaluation


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pipeline", required=True, choices=PIPELINES)
    parser.add_argument("--score-only", action="store_true")
    parser.add_argument("--results", type=Path)
    parser.add_argument("--eval-set", type=Path)
    parser.add_argument(
        "--output-dir", type=Path, default=Path("/tmp/legal-rag-m5")
    )
    args = parser.parse_args()
    if not args.score_only:
        parser.error(
            "this structural-migration CLI currently requires --score-only; "
            "runtime execution is available through run_evaluation(executor=...)"
        )
    run = run_evaluation(
        pipeline=args.pipeline,
        eval_set=args.eval_set,
        results=args.results,
        output_dir=args.output_dir / args.pipeline,
        score_only=True,
    )
    print(json.dumps(run["metrics"], ensure_ascii=False, indent=2))
    for name, path in run["outputs"].items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
