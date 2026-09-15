#!/usr/bin/env python3
"""Validate retrieval gold annotations against the immutable corpus snapshot."""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVAL = ROOT / "eval-sets/retrieval/retrieval_eval.jsonl"
CORPUS = ROOT / "data/versions/corpus-v0.1"
ALLOWED_DIFFICULTY = {"easy", "medium", "hard"}
ALLOWED_STATUS = {"pending", "in_review", "needs_review", "verified"}


def jsonl(path):
    with path.open(encoding="utf-8") as f:
        for number, line in enumerate(f, 1):
            if line.strip():
                yield number, json.loads(line)


def main():
    errors, warnings = [], []
    with (CORPUS / "documents.csv").open(encoding="utf-8-sig", newline="") as f:
        documents = {r["document_id"] for r in csv.DictReader(f)}
    articles = {a["article_id"]: a for _, a in jsonl(CORPUS / "articles.jsonl")}
    chunks = {c["chunk_id"]: c for _, c in jsonl(CORPUS / "chunks.jsonl")}
    queries, seen = [], set()
    try:
        queries = list(jsonl(EVAL))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        errors.append(f"Cannot parse evaluation JSONL: {exc}")
    for line, q in queries:
        prefix = f"line {line} ({q.get('query_id', '<missing>')})"
        qid = q.get("query_id")
        if not qid: errors.append(f"{prefix}: query_id is empty")
        elif qid in seen: errors.append(f"{prefix}: duplicate query_id")
        seen.add(qid)
        if not str(q.get("query", "")).strip(): errors.append(f"{prefix}: query is empty")
        if q.get("difficulty") not in ALLOWED_DIFFICULTY: errors.append(f"{prefix}: invalid difficulty {q.get('difficulty')!r}")
        status = q.get("annotation_status")
        if status not in ALLOWED_STATUS: errors.append(f"{prefix}: invalid annotation_status {status!r}")
        annotated_by = str(q.get("annotated_by", "")).strip()
        if status == "verified" and "human-reviewed" not in annotated_by.lower():
            warnings.append(f"{prefix}: verified requires documented human review")
        if not annotated_by: errors.append(f"{prefix}: annotated_by is empty")
        gold_docs = q.get("gold_document_ids", [])
        gold_articles = q.get("gold_article_ids", [])
        gold_chunks = q.get("gold_chunk_ids", [])
        for label, values in (("document", gold_docs), ("article", gold_articles), ("chunk", gold_chunks)):
            if not isinstance(values, list):
                errors.append(f"{prefix}: gold_{label}_ids is not a list"); continue
            if len(values) != len(set(values)): errors.append(f"{prefix}: duplicate gold {label} ID")
        if status == "in_review" and not (gold_docs and gold_articles and gold_chunks):
            errors.append(f"{prefix}: in_review requires non-empty gold at all three levels")
        if status == "needs_review" and (gold_docs or gold_articles or gold_chunks):
            warnings.append(f"{prefix}: needs_review normally has empty gold labels")
        for did in gold_docs:
            if did not in documents: errors.append(f"{prefix}: unknown document {did}")
        for aid in gold_articles:
            if aid not in articles: errors.append(f"{prefix}: unknown article {aid}")
            elif articles[aid]["document_id"] not in gold_docs:
                errors.append(f"{prefix}: article {aid} parent document is not gold")
        for cid in gold_chunks:
            if cid not in chunks:
                errors.append(f"{prefix}: unknown chunk {cid}"); continue
            c = chunks[cid]
            aid = f"{c['document_id']}_dieu-{c['article']}"
            if c["document_id"] not in gold_docs:
                errors.append(f"{prefix}: chunk {cid} document is not gold")
            if aid not in gold_articles:
                errors.append(f"{prefix}: chunk {cid} parent article {aid} is not gold")
    print(f"Queries: {len(queries)}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    for e in errors: print(f"ERROR: {e}")
    for w in warnings: print(f"WARNING: {w}")
    print("Validation: PASSED" if not errors else "Validation: FAILED")
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
