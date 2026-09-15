#!/usr/bin/env python3
"""Run the M1-supported DOCX extraction, cleaning, and parsing stages."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Source DOCX file")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--document-id", required=True)
    parser.add_argument("--document-number", required=True)
    parser.add_argument("--document-title", required=True)
    parser.add_argument(
        "--boilerplate-file",
        type=Path,
        help="Exact boilerplate lines to remove (comments start with #)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    from legal_rag.ingestion import (
        clean_text, extract_document, load_boilerplate_lines, parse_legal_structure,
    )
    from legal_rag.ingestion.parsers import natural_article_key

    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    raw_text, paragraph_count, table_count = extract_document(args.input)
    if not raw_text:
        raise ValueError("DOCX không tạo ra nội dung text")

    boilerplate = (
        load_boilerplate_lines(args.boilerplate_file)
        if args.boilerplate_file
        else set()
    )
    cleaned_text, removed_lines = clean_text(raw_text, boilerplate)
    if not cleaned_text:
        raise ValueError("Kết quả cleaning bị rỗng")

    articles = parse_legal_structure(
        cleaned_text,
        document_id=args.document_id,
        document_number=args.document_number,
        document_title=args.document_title,
    )
    if not articles:
        raise ValueError("Không nhận diện được Điều nào")
    articles.sort(key=lambda item: natural_article_key(item.number))

    raw_path = output_dir / f"{args.document_id}.raw.txt"
    cleaned_path = output_dir / f"{args.document_id}.cleaned.txt"
    articles_path = output_dir / f"{args.document_id}.articles.jsonl"
    raw_path.write_text(raw_text, encoding="utf-8")
    cleaned_path.write_text(cleaned_text + "\n", encoding="utf-8")
    with articles_path.open("w", encoding="utf-8") as target:
        for article in articles:
            target.write(json.dumps(article.to_dict(), ensure_ascii=False) + "\n")

    print(f"Raw: {raw_path}")
    print(f"Cleaned: {cleaned_path}")
    print(f"Articles: {articles_path}")
    print(
        f"Paragraphs: {paragraph_count}; tables: {table_count}; "
        f"removed boilerplate lines: {len(removed_lines)}; articles: {len(articles)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
