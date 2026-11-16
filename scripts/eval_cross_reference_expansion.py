#!/usr/bin/env python3
"""Evaluate Cross-Reference and Clause Expansion on 40-query benchmark.

Measures Recall, Hit Rate, and Chunk Count across:
1. Raw baseline
2. Clause expansion only
3. Cross-reference following only
4. Combined: Clause expansion + Cross-reference following

Specifically tracks and reports impact on the 30 new queries vs 10 legacy queries.
"""

from __future__ import annotations

import json
import os
import sys
import time
from collections import defaultdict
from pathlib import Path
from statistics import mean

ROOT = Path("/home/minhkha/kk/TTTN/legal-agentic-rag-next")
sys.path.insert(0, str(ROOT / "src"))

os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

from legal_rag.cross_reference import CrossReferenceResolver
from legal_rag.retrieval.dense import DenseRetriever
from legal_rag.retrieval.reranker import BGEReranker, union_candidates
from legal_rag.retrieval.sparse import PersistentBM25Retriever

CORPUS = ROOT / "data/versions/corpus-v0.2/chunks/chunks.jsonl"
IX = ROOT / "experiments/indexes/corpus-v0.2"
CFP = "7525978bfbf645d2ace8955d52a06906985799350c82c7b9fd797d246f80b827"
RR = "953dc6f6f85a1b2dbfca4c34a2796e7dde08d41e"
EVAL_FILE = ROOT / "eval-sets/retrieval/baseline_eval_40.jsonl"
OUTPUT_FILE = ROOT / "experiments/retrieval/corpus-v0.2/cross_reference_eval_results.json"


def compute_recall_and_hits(retrieved_chunks: list[str], gold_chunks: set[str]):
    """Calculate recall and hit rates for an arbitrary retrieved set."""
    if not gold_chunks:
        return 0.0, 0
    ret_set = set(retrieved_chunks)
    hits = len(ret_set.intersection(gold_chunks))
    recall = hits / len(gold_chunks)
    has_hit = int(hits > 0)
    return recall, has_hit


def main():
    print("Initializing CrossReferenceResolver...")
    t0 = time.time()
    resolver = CrossReferenceResolver(CORPUS)
    print(f"Corpus loaded: {len(resolver.chunks_by_id)} chunks in {time.time() - t0:.2f}s")

    print("\nLoading retrieval models...")
    t1 = time.time()
    bm = PersistentBM25Retriever(
        CORPUS,
        IX / "sparse/sparse_index.json",
        IX / "manifests/sparse_manifest.json",
        corpus_fingerprint=CFP,
    )
    den = DenseRetriever(CORPUS, IX / "dense", corpus_fingerprint=CFP, load_encoder=True)
    scorer = BGEReranker(revision=RR, batch_size=8)
    print(f"Models loaded in {time.time() - t1:.2f}s")

    queries = []
    with open(EVAL_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                queries.append(json.loads(line))
    print(f"Loaded {len(queries)} queries ({sum(1 for q in queries if q.get('source') == 'new_design')} new).")

    eval_records = []
    print("\nRunning evaluation across all 40 queries...")

    for idx, q_item in enumerate(queries, 1):
        qid = q_item["query_id"]
        q_text = q_item["query"]
        gold_chunks = set(q_item["gold_chunk_ids"])
        source = q_item.get("source", "unknown")

        # 1. Base retrieval
        bm_res = bm.search(q_text, 20)
        bm_cids = [x["chunk"]["chunk_id"] for x in bm_res]

        den_res = den.search(q_text, 20)
        den_cids = [x["chunk"]["chunk_id"] for x in den_res]

        u_res = union_candidates(bm_res, den_res)
        rr_res = scorer.rerank(q_text, u_res, len(u_res))
        rr_cids = [x["chunk"]["chunk_id"] for x in rr_res]

        # Candidate sets
        cand_sets = {}

        for prefix, base_cids in [("bm25", bm_cids), ("dense", den_cids), ("rerank", rr_cids)]:
            for k in [5, 10, 20]:
                k_cids = base_cids[:k]
                # 1. Base
                cand_sets[f"{prefix}_top{k}_base"] = k_cids
                # 2. Clause only
                cand_sets[f"{prefix}_top{k}_clause"] = resolver.expand(
                    k_cids, enable_clause_expansion=True, enable_cross_references=False
                )
                # 3. Cross-ref only
                cand_sets[f"{prefix}_top{k}_crossref"] = resolver.expand(
                    k_cids, enable_clause_expansion=False, enable_cross_references=True
                )
                # 4. Combined (Clause + Cross-ref)
                cand_sets[f"{prefix}_top{k}_combined"] = resolver.expand(
                    k_cids, enable_clause_expansion=True, enable_cross_references=True
                )

        row = {
            "query_id": qid,
            "query": q_text,
            "source": source,
            "gold_count": len(gold_chunks),
            "gold_chunk_ids": list(gold_chunks),
            "metrics": {},
        }

        for cfg_name, cids in cand_sets.items():
            rec, hit = compute_recall_and_hits(cids, gold_chunks)
            row["metrics"][cfg_name] = {
                "count": len(cids),
                "recall": rec,
                "hit": hit,
            }

        eval_records.append(row)
        if idx % 10 == 0 or idx == len(queries):
            print(f"  Processed {idx}/{len(queries)} queries...")

    # Aggregates
    configs = list(eval_records[0]["metrics"].keys())

    def get_summary(subset):
        res = {}
        for cfg in configs:
            recs = [r["metrics"][cfg]["recall"] for r in subset]
            hits = [r["metrics"][cfg]["hit"] for r in subset]
            counts = [r["metrics"][cfg]["count"] for r in subset]
            res[cfg] = {
                "mean_recall": mean(recs),
                "hit_rate": mean(hits),
                "mean_chunk_count": mean(counts),
            }
        return res

    all_summary = get_summary(eval_records)
    legacy_summary = get_summary([r for r in eval_records if r["source"] == "legacy_retrieval_eval"])
    new_summary = get_summary([r for r in eval_records if r["source"] == "new_design"])

    output_payload = {
        "all_40": all_summary,
        "legacy_10": legacy_summary,
        "new_30": new_summary,
        "per_query": eval_records,
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output_payload, f, ensure_ascii=False, indent=2)
    print(f"\nSaved detailed evaluation to {OUTPUT_FILE}")

    # Display comparison table
    display_rows = [
        ("BM25 Top 5", "bm25_top5"),
        ("BM25 Top 10", "bm25_top10"),
        ("Dense Top 5", "dense_top5"),
        ("Dense Top 10", "dense_top10"),
        ("Reranker Top 5", "rerank_top5"),
        ("Reranker Top 10", "rerank_top10"),
        ("Reranker Top 20", "rerank_top20"),
    ]

    for group_title, summary, n in [
        ("30 NEW QUERIES (17 Documents Cross-Corpus)", new_summary, 30),
        ("10 LEGACY QUERIES (AI Domain Focus)", legacy_summary, 10),
        ("TOÀN BỘ 40 QUERIES BENCHMARK", all_summary, 40),
    ]:
        title_str = f"{group_title} (N={n}): SO SÁNH HIỆU QUẢ CÁC CƠ CHẾ EXPANSION"
        print("\n" + "=" * 110)
        print(f"{title_str:^110}")
        print("=" * 110)
        print(
            f"{'Phương pháp':<16} | {'Base Rec':<9} | {'Clause Rec':<11} | {'Cross-Ref Rec':<14} | {'Combined Rec':<13} | {'Δ Comb vs Base':<15} | {'Avg Chunks':<10}"
        )
        print("-" * 110)
        for label, base_key in display_rows:
            r_base = summary[f"{base_key}_base"]["mean_recall"] * 100
            r_clause = summary[f"{base_key}_clause"]["mean_recall"] * 100
            r_xref = summary[f"{base_key}_crossref"]["mean_recall"] * 100
            r_comb = summary[f"{base_key}_combined"]["mean_recall"] * 100
            diff = r_comb - r_base
            rel = (diff / r_base * 100) if r_base > 0 else 0.0
            avg_c = summary[f"{base_key}_combined"]["mean_chunk_count"]
            print(
                f"{label:<16} | {r_base:>8.1f}% | {r_clause:>10.1f}% | {r_xref:>13.1f}% | {r_comb:>12.1f}% | {diff:>+6.1f}% ({rel:>+5.1f}%) | {avg_c:>10.1f}"
            )
        print("-" * 110)


if __name__ == "__main__":
    main()
