#!/usr/bin/env python3
"""Diagnostic coverage analysis for BM25@20 union Dense@20 (no fusion/reranking)."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean
from typing import Any

from legal_rag.retrieval import BM25Retriever, DenseRetriever, read_chunks
from legal_rag.retrieval.dense import DEFAULT_INDEX_DIR

ROOT = Path(__file__).resolve().parents[3]
CORPUS = ROOT / "data/versions/corpus-v0.1/chunks.jsonl"
EVALUATION = ROOT / "eval-sets/retrieval/retrieval_eval.jsonl"
RESULTS = ROOT / "experiments/runs/retrieval/candidate-union-v0"
STEM = "candidate-union-v0"
DEPTH = 20
EXPECTED_QUERIES = 31
SPECIAL_IDS = ["eval002", "eval005a", "eval010", "eval011", "eval012", "eval022", "eval023", "eval026"]

PER_QUERY_FIELDS = [
    "query_id", "query", "query_type", "difficulty", "gold_chunk_count",
    "bm25_gold_found", "dense_gold_found", "union_gold_found",
    "bm25_candidate_recall", "dense_candidate_recall", "union_candidate_recall",
    "bm25_any_gold", "dense_any_gold", "union_any_gold",
    "bm25_full_gold", "dense_full_gold", "union_full_gold",
    "bm25_candidate_count", "dense_candidate_count", "union_candidate_count",
    "overlap_count", "overlap_ratio",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_queries(path: Path) -> list[dict[str, Any]]:
    queries = []
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            query = json.loads(line)
            if query.get("annotation_status") != "verified":
                continue
            if not query.get("gold_chunk_ids") or not query.get("gold_article_ids"):
                raise ValueError(f"Verified query has empty gold at line {line_number}")
            queries.append(query)
    if len(queries) != EXPECTED_QUERIES:
        raise ValueError(f"Expected {EXPECTED_QUERIES} verified queries, found {len(queries)}")
    ids = [str(q["query_id"]) for q in queries]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate query_id in evaluation")
    return queries


def article_id(chunk: dict[str, Any]) -> str:
    return f"{chunk['document_id']}_dieu-{chunk['article']}"


def ids(results: list[dict[str, Any]]) -> list[str]:
    return [str(result["chunk"]["chunk_id"]) for result in results]


def article_ids(results: list[dict[str, Any]]) -> set[str]:
    return {article_id(result["chunk"]) for result in results}


def ratio(numerator: int, denominator: int) -> float:
    return numerator / denominator if denominator else 0.0


def coverage(found: set[str], gold: set[str]) -> tuple[int, int, int, float]:
    count = len(found & gold)
    return count, int(count > 0), int(count == len(gold)), ratio(count, len(gold))


def rank_map(ranking: list[str]) -> dict[str, int]:
    return {item: rank for rank, item in enumerate(ranking, 1)}


def write_csv(path: Path, fields: list[str], rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: f"{value:.10f}" if isinstance(value, float) else value
                             for key, value in row.items() if key in fields})


def group_breakdown(rows: list[dict[str, Any]], field: str) -> dict[str, dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[str(row[field])].append(row)
    output = {}
    for name in sorted(groups):
        current = groups[name]
        output[name] = {
            "query_count": len(current),
            "union_any_gold_coverage": mean(r["union_any_gold"] for r in current),
            "union_full_gold_coverage": mean(r["union_full_gold"] for r in current),
            "macro_candidate_recall": mean(r["union_candidate_recall"] for r in current),
            "average_candidate_pool_size": mean(r["union_candidate_count"] for r in current),
        }
        if field == "query_type":
            output[name].pop("union_full_gold_coverage")
            output[name].pop("average_candidate_pool_size")
    return output


def fmt(value: float) -> str:
    return f"{value:.6f}"


def render_report(metrics: dict[str, Any], rows: list[dict[str, Any]], missing: list[dict[str, Any]]) -> str:
    c, p, a = metrics["chunk_level"], metrics["candidate_pool"], metrics["article_level"]
    ga, qa = metrics["gold_source_attribution"], metrics["query_source_attribution"]
    by_id = {r["query_id"]: r for r in rows}
    lines = [
        "# Candidate Union v0 Diagnostic Report", "",
        "BM25@20 ∪ Dense@20 is an unranked, chunk-id-deduplicated candidate pool. "
        "No RRF, fusion ranking, reranking, or retriever tuning was performed.", "",
        "## Configuration", "", f"- BM25 depth: {DEPTH}", f"- Dense depth: {DEPTH}",
        f"- Verified queries: {len(rows)}", "",
        "## Chunk candidate coverage", "",
        "| Metric | BM25 | Dense | Union |", "|---|---:|---:|---:|",
        f"| Any-Gold Coverage | {fmt(c['bm25_any_gold_coverage'])} | {fmt(c['dense_any_gold_coverage'])} | {fmt(c['union_any_gold_coverage'])} |",
        f"| Full-Gold Coverage | {fmt(c['bm25_full_gold_coverage'])} | {fmt(c['dense_full_gold_coverage'])} | {fmt(c['union_full_gold_coverage'])} |",
        f"| Macro Candidate Recall | {fmt(c['bm25_macro_candidate_recall'])} | {fmt(c['dense_macro_candidate_recall'])} | {fmt(c['union_macro_candidate_recall'])} |",
        f"| Micro Candidate Recall | {fmt(c['bm25_micro_candidate_recall'])} | {fmt(c['dense_micro_candidate_recall'])} | {fmt(c['union_micro_candidate_recall'])} |",
        "", "## Perfect-reranker theoretical upper bounds", "",
        f"- Hit@1 upper bound: {fmt(c['perfect_reranker_hit_at_1_upper_bound'])}",
        f"- Full-answer candidate coverage: {fmt(c['perfect_reranker_full_answer_candidate_coverage'])}",
        "", "These are candidate-coverage upper bounds, not measured reranker performance.", "",
        "## Gold source attribution", "",
        "| Source | Count | Ratio |", "|---|---:|---:|",
    ]
    for key, label in (("both", "BOTH"), ("bm25_only", "BM25_ONLY"),
                       ("dense_only", "DENSE_ONLY"), ("neither", "NEITHER")):
        lines.append(f"| {label} | {ga[key + '_count']} | {fmt(ga[key + '_ratio'])} |")
    lines += ["", "## Query-level source attribution", "",
              "| Class | Count |", "|---|---:|",
              f"| BOTH_FIND_GOLD | {qa['both_find_gold']} |",
              f"| BM25_ONLY_FINDS_GOLD | {qa['bm25_only_finds_gold']} |",
              f"| DENSE_ONLY_FINDS_GOLD | {qa['dense_only_finds_gold']} |",
              f"| NEITHER_FINDS_GOLD | {qa['neither_finds_gold']} |", "",
              "## Candidate pool", "",
              f"- Average size: {p['average_size']:.6f}", f"- Min / max: {p['min_size']} / {p['max_size']}",
              f"- Average overlap count: {p['average_overlap_count']:.6f}",
              f"- Average overlap ratio: {p['average_overlap_ratio']:.6f}",
              f"- Size distribution: {json.dumps(p['size_distribution'], sort_keys=True)}", "",
              "## Article candidate coverage", "",
              "| Metric | BM25 | Dense | Union |", "|---|---:|---:|---:|",
              f"| Any-Gold Coverage | {fmt(a['bm25_any_gold_coverage'])} | {fmt(a['dense_any_gold_coverage'])} | {fmt(a['union_any_gold_coverage'])} |",
              f"| Full-Gold Coverage | {fmt(a['bm25_full_gold_coverage'])} | {fmt(a['dense_full_gold_coverage'])} | {fmt(a['union_full_gold_coverage'])} |", "",
              "## Difficulty breakdown", "", "| Difficulty | Queries | Union any | Union full | Macro recall | Avg pool |",
              "|---|---:|---:|---:|---:|---:|"]
    for name, value in metrics["difficulty_breakdown"].items():
        lines.append(f"| {name} | {value['query_count']} | {fmt(value['union_any_gold_coverage'])} | "
                     f"{fmt(value['union_full_gold_coverage'])} | {fmt(value['macro_candidate_recall'])} | "
                     f"{value['average_candidate_pool_size']:.6f} |")
    lines += ["", "## Query type breakdown", "",
              "Groups with one sample are descriptive only; no strong inference is made.", "",
              "| Query type | Queries | Union any | Macro recall |", "|---|---:|---:|---:|"]
    for name, value in metrics["query_type_breakdown"].items():
        lines.append(f"| {name} | {value['query_count']} | {fmt(value['union_any_gold_coverage'])} | {fmt(value['macro_candidate_recall'])} |")
    lines += ["", "## Special failures", "",
              "| Query | Gold | BM25 found@20 | Dense found@20 | Union found | Union recall |",
              "|---|---:|---:|---:|---:|---:|"]
    for query_id in SPECIAL_IDS:
        row = by_id[query_id]
        lines.append(f"| {query_id} | {row['gold_chunk_count']} | {row['bm25_gold_found']} | "
                     f"{row['dense_gold_found']} | {row['union_gold_found']} | {fmt(row['union_candidate_recall'])} |")
    lines += ["", f"Missing gold chunks: {len(missing)}. Queries with no gold in union: "
              f"{sum(r['union_any_gold'] == 0 for r in rows)}.", "",
              "For missing gold, full-corpus BM25/Dense ranks in the CSV are diagnostic only; candidate depth remains 20.", "",
              "## Diagnostic interpretation", "", metrics["diagnostic_interpretation"], "",
              "This statement is diagnostic and does not select a final architecture.", ""]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=CORPUS)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    parser.add_argument("--index-dir", type=Path, default=DEFAULT_INDEX_DIR)
    parser.add_argument("--results-dir", type=Path, default=RESULTS)
    args = parser.parse_args()

    input_hashes = {"corpus_sha256": sha256(args.corpus), "evaluation_sha256": sha256(args.evaluation)}
    queries, chunks = load_queries(args.evaluation), read_chunks(args.corpus)
    chunk_by_id = {str(c["chunk_id"]): c for c in chunks}
    if len(chunk_by_id) != len(chunks):
        raise ValueError("Corpus contains duplicate chunk_id")
    for query in queries:
        missing_labels = set(query["gold_chunk_ids"]) - chunk_by_id.keys()
        if missing_labels:
            raise ValueError(f"Gold chunks absent from corpus for {query['query_id']}: {sorted(missing_labels)}")
        derived = {article_id(chunk_by_id[x]) for x in query["gold_chunk_ids"]}
        if not derived.issubset(set(query["gold_article_ids"])):
            raise ValueError(f"Gold chunk/article mismatch for {query['query_id']}")

    bm25, dense = BM25Retriever(chunks), DenseRetriever(args.corpus, args.index_dir)
    rows, missing_rows = [], []
    gold_attribution, query_attribution = Counter(), Counter()
    total_gold = total_bm25 = total_dense = total_union = 0

    for number, query in enumerate(queries, 1):
        print(f"[{number:02d}/{len(queries)}] {query['query_id']}", flush=True)
        bm25_all = bm25.search(query["query"], top_k=len(chunks))
        dense_all = dense.search(query["query"], top_k=len(chunks))
        bm25_rank, dense_rank = rank_map(ids(bm25_all)), rank_map(ids(dense_all))
        bm25_top, dense_top = bm25_all[:DEPTH], dense_all[:DEPTH]
        bset, dset = set(ids(bm25_top)), set(ids(dense_top))
        union = bset | dset
        gold = set(query["gold_chunk_ids"])
        bcount, bany, bfull, brecall = coverage(bset, gold)
        dcount, dany, dfull, drecall = coverage(dset, gold)
        ucount, uany, ufull, urecall = coverage(union, gold)
        overlap = len(bset & dset)
        row = {
            "query_id": query["query_id"], "query": query["query"],
            "query_type": query["query_type"], "difficulty": query["difficulty"],
            "gold_chunk_count": len(gold), "bm25_gold_found": bcount,
            "dense_gold_found": dcount, "union_gold_found": ucount,
            "bm25_candidate_recall": brecall, "dense_candidate_recall": drecall,
            "union_candidate_recall": urecall, "bm25_any_gold": bany,
            "dense_any_gold": dany, "union_any_gold": uany,
            "bm25_full_gold": bfull, "dense_full_gold": dfull, "union_full_gold": ufull,
            "bm25_candidate_count": len(bset), "dense_candidate_count": len(dset),
            "union_candidate_count": len(union), "overlap_count": overlap,
            "overlap_ratio": ratio(overlap, len(union)),
        }
        bgold_articles, dgold_articles = article_ids(bm25_top), article_ids(dense_top)
        gold_articles = set(query["gold_article_ids"])
        for prefix, aset in (("bm25", bgold_articles), ("dense", dgold_articles), ("union", bgold_articles | dgold_articles)):
            _, any_found, full_found, _ = coverage(aset, gold_articles)
            row[f"{prefix}_article_any_gold"] = any_found
            row[f"{prefix}_article_full_gold"] = full_found
        for gold_id in query["gold_chunk_ids"]:
            if gold_id in bset and gold_id in dset: gold_attribution["both"] += 1
            elif gold_id in bset: gold_attribution["bm25_only"] += 1
            elif gold_id in dset: gold_attribution["dense_only"] += 1
            else:
                gold_attribution["neither"] += 1
                missing_rows.append({
                    "query_id": query["query_id"], "query": query["query"],
                    "difficulty": query["difficulty"], "query_type": query["query_type"],
                    "gold_chunk_id": gold_id, "gold_article_id": article_id(chunk_by_id[gold_id]),
                    "bm25_full_corpus_rank": bm25_rank.get(gold_id, ""),
                    "dense_full_corpus_rank": dense_rank.get(gold_id, ""),
                })
        query_attribution["both_find_gold" if bany and dany else
                          "bm25_only_finds_gold" if bany else
                          "dense_only_finds_gold" if dany else "neither_finds_gold"] += 1
        total_gold += len(gold); total_bm25 += bcount; total_dense += dcount; total_union += ucount
        rows.append(row)

    avg = lambda field: mean(float(r[field]) for r in rows)
    chunk_level = {
        f"{prefix}_{metric}": avg(f"{prefix}_{field}")
        for prefix in ("bm25", "dense", "union")
        for metric, field in (("any_gold_coverage", "any_gold"),
                              ("full_gold_coverage", "full_gold"),
                              ("macro_candidate_recall", "candidate_recall"))
    }
    chunk_level.update({
        "bm25_micro_candidate_recall": ratio(total_bm25, total_gold),
        "dense_micro_candidate_recall": ratio(total_dense, total_gold),
        "union_micro_candidate_recall": ratio(total_union, total_gold),
        "perfect_reranker_hit_at_1_upper_bound": chunk_level["union_any_gold_coverage"],
        "perfect_reranker_full_answer_candidate_coverage": chunk_level["union_full_gold_coverage"],
    })
    total_attributed = sum(gold_attribution.values())
    gold_source = {}
    for key in ("both", "bm25_only", "dense_only", "neither"):
        gold_source[key + "_count"] = gold_attribution[key]
        gold_source[key + "_ratio"] = ratio(gold_attribution[key], total_attributed)
    union_any = chunk_level["union_any_gold_coverage"]
    interpretation = ("Candidate generation appears strong enough to justify testing a reranker. "
                      "Candidate generation has very high any-gold coverage; ranking is likely the dominant "
                      "bottleneck for most queries." if union_any >= .95 else
                      "Candidate generation appears strong enough to justify testing a reranker." if union_any >= .90 else
                      "Candidate generation still misses a meaningful number of queries; reranking alone cannot solve all failures.")
    pool_sizes = Counter(r["union_candidate_count"] for r in rows)
    metrics = {
        "experiment": STEM, "query_count": len(rows), "bm25_depth": DEPTH, "dense_depth": DEPTH,
        "chunk_level": chunk_level,
        "candidate_pool": {"average_size": avg("union_candidate_count"),
                           "min_size": min(r["union_candidate_count"] for r in rows),
                           "max_size": max(r["union_candidate_count"] for r in rows),
                           "average_overlap_count": avg("overlap_count"),
                           "average_overlap_ratio": avg("overlap_ratio"),
                           "size_distribution": {str(k): pool_sizes[k] for k in sorted(pool_sizes)}},
        "gold_source_attribution": gold_source,
        "query_source_attribution": {key: query_attribution[key] for key in
                                     ("both_find_gold", "bm25_only_finds_gold", "dense_only_finds_gold", "neither_finds_gold")},
        "article_level": {f"{prefix}_{metric}_coverage": avg(f"{prefix}_article_{field}")
                          for prefix in ("bm25", "dense", "union")
                          for metric, field in (("any_gold", "any_gold"), ("full_gold", "full_gold"))},
        "difficulty_breakdown": group_breakdown(rows, "difficulty"),
        "query_type_breakdown": group_breakdown(rows, "query_type"),
        "missing_gold_chunk_count": len(missing_rows),
        "queries_with_no_gold_in_union": sum(r["union_any_gold"] == 0 for r in rows),
        "diagnostic_interpretation": interpretation,
        "integrity": {**input_hashes, "gold_integrity": "PASS", "corpus_integrity": "PASS"},
    }
    args.results_dir.mkdir(parents=True, exist_ok=True)
    metrics_path = args.results_dir / f"{STEM}_metrics.json"
    per_query_path = args.results_dir / f"{STEM}_per_query.csv"
    missing_path = args.results_dir / f"{STEM}_missing_gold.csv"
    report_path = args.results_dir / f"{STEM}_report.md"
    metrics_path.write_text(json.dumps(metrics, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_csv(per_query_path, PER_QUERY_FIELDS, rows)
    write_csv(missing_path, ["query_id", "query", "difficulty", "query_type", "gold_chunk_id",
                             "gold_article_id", "bm25_full_corpus_rank", "dense_full_corpus_rank"], missing_rows)
    report_path.write_text(render_report(metrics, rows, missing_rows), encoding="utf-8")
    if input_hashes != {"corpus_sha256": sha256(args.corpus), "evaluation_sha256": sha256(args.evaluation)}:
        raise RuntimeError("Frozen input changed while analysis was running")
    print(f"Wrote {metrics_path}")
    print(f"Wrote {per_query_path}")
    print(f"Wrote {missing_path}")
    print(f"Wrote {report_path}")


if __name__ == "__main__":
    main()
