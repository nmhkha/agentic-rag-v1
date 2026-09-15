#!/usr/bin/env python3
"""Build persistent indexes supported by the retrieval package."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--method", choices=["dense"], required=True)
    parser.add_argument("--corpus", type=Path, default=ROOT / "data/processed/chunks.jsonl")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--revision", help="Model revision (defaults to the package-pinned revision)")
    parser.add_argument("--batch-size", type=int)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    from legal_rag.retrieval.dense import DENSE_MODEL_REVISION, build_dense_index

    manifest = build_dense_index(
        args.corpus,
        args.output_dir,
        revision=args.revision or DENSE_MODEL_REVISION,
        batch_size=args.batch_size,
    )
    print(
        f"Built {manifest['retriever_name']}: "
        f"{manifest['corpus_chunk_count']} x {manifest['embedding_dimension']}"
    )
    print(f"Output: {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
