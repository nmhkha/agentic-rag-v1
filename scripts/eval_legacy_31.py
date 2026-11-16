#!/usr/bin/env python3
"""Comprehensive evaluation of the 31 Legacy Queries on frozen corpus-v0.2.

Evaluates:
1. Baseline Retrieval (BM25, Dense Jina-v3, BGE-Reranker-v2-m3)
2. Clause Expansion (Mở rộng theo khoản)
3. Cross-Reference Following (Nhảy dẫn chiếu pháp lý)
4. Combined Expansion (Clause + Cross-Reference)

Metrics:
- Chunk-level Recall@5, @10, @20
- Chunk-level Hit@1, @3, @5, @10, @20
- Article-level Hit@1, @3, @5, @10, @20
- MRR@10 (Mean Reciprocal Rank)
- Average Chunks (Context size)
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
EVAL_FILE = ROOT / "eval-sets/retrieval/retrieval_eval.jsonl"
OUTPUT_FILE = ROOT / "experiments/retrieval/corpus-v0.2/legacy_31_eval_results.json"


def compute_metrics(retrieved_cids: list[str], gold_cids: set[str], chunks_dict: dict):
    if not gold_cids:
        return 0.0, 0, 0, 0.0

    ret_set = set(retrieved_cids)
    hits = len(ret_set.intersection(gold_cids))
    recall = hits / len(gold_cids)
    chunk_hit = int(hits > 0)

    # Article-level hit
    gold_articles = {chunks_dict.get(c, {}).get("article_id") for c in gold_cids if chunks_dict.get(c)}
    ret_articles = {chunks_dict.get(c, {}).get("article_id") for c in ret_set if chunks_dict.get(c)}
    art_hit = int(bool(gold_articles & ret_articles))

    # Reciprocal Rank (RR)
    rr = 0.0
    for rank, cid in enumerate(retrieved_cids, 1):
        if cid in gold_cids:
            rr = 1.0 / rank
            break

    return recall, chunk_hit, art_hit, rr


def main():
    print("Loading Corpus Chunks and Index Mapping...", flush=True)
    t0 = time.time()
    chunks_dict = {}
    with open(CORPUS, "r", encoding="utf-8") as f:
        for line in f:
            c = json.loads(line)
            chunks_dict[c["chunk_id"]] = c
    print(f"Corpus loaded: {len(chunks_dict)} chunks in {time.time() - t0:.2f}s", flush=True)

    print("\nInitializing CrossReferenceResolver & Retrievers...", flush=True)
    t1 = time.time()
    resolver = CrossReferenceResolver(CORPUS)
    bm = PersistentBM25Retriever(
        CORPUS,
        IX / "sparse/sparse_index.json",
        IX / "manifests/sparse_manifest.json",
        corpus_fingerprint=CFP,
    )
    den = DenseRetriever(CORPUS, IX / "dense", corpus_fingerprint=CFP, load_encoder=True)
    scorer = BGEReranker(revision=RR, batch_size=8)
    print(f"Models initialized in {time.time() - t1:.2f}s", flush=True)

    queries = []
    with open(EVAL_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                queries.append(json.loads(line))
    print(f"Loaded {len(queries)} legacy queries from {EVAL_FILE.name}.", flush=True)

    eval_records = []
    print(f"\nRunning full evaluation on {len(queries)} legacy queries...", flush=True)

    for idx, q_item in enumerate(queries, 1):
        qid = q_item["query_id"]
        q_text = q_item["query"]
        gold_cids = set(q_item["gold_chunk_ids"])

        # 1. Base Retrieval
        bm_res = bm.search(q_text, 20)
        bm_cids = [x["chunk"]["chunk_id"] for x in bm_res]

        den_res = den.search(q_text, 20)
        den_cids = [x["chunk"]["chunk_id"] for x in den_res]

        u_res = union_candidates(bm_res, den_res)
        rr_res = scorer.rerank(q_text, u_res, len(u_res))
        rr_cids = [x["chunk"]["chunk_id"] for x in rr_res]

        cand_sets = {}
        for prefix, base_cids in [("bm25", bm_cids), ("dense", den_cids), ("rerank", rr_cids)]:
            for k in [5, 10, 20]:
                k_cids = base_cids[:k]
                cand_sets[f"{prefix}_top{k}_base"] = k_cids
                cand_sets[f"{prefix}_top{k}_clause"] = resolver.expand(
                    k_cids, enable_clause_expansion=True, enable_cross_references=False
                )
                cand_sets[f"{prefix}_top{k}_crossref"] = resolver.expand(
                    k_cids, enable_clause_expansion=False, enable_cross_references=True
                )
                cand_sets[f"{prefix}_top{k}_combined"] = resolver.expand(
                    k_cids, enable_clause_expansion=True, enable_cross_references=True
                )

        row = {
            "query_id": qid,
            "query": q_text,
            "difficulty": q_item.get("difficulty", "medium"),
            "gold_count": len(gold_cids),
            "gold_chunk_ids": list(gold_cids),
            "metrics": {},
        }

        for cfg_name, cids in cand_sets.items():
            rec, hit, art_hit, rr = compute_metrics(cids, gold_cids, chunks_dict)
            row["metrics"][cfg_name] = {
                "count": len(cids),
                "recall": rec,
                "hit": hit,
                "art_hit": art_hit,
                "mrr": rr,
            }

        eval_records.append(row)
        if idx % 10 == 0 or idx == len(queries):
            print(f"  Processed {idx}/{len(queries)} queries...", flush=True)

    # Summary
    configs = list(eval_records[0]["metrics"].keys())
    summary = {}
    for cfg in configs:
        summary[cfg] = {
            "mean_recall": mean(r["metrics"][cfg]["recall"] for r in eval_records),
            "hit_rate": mean(r["metrics"][cfg]["hit"] for r in eval_records),
            "art_hit_rate": mean(r["metrics"][cfg]["art_hit"] for r in eval_records),
            "mrr": mean(r["metrics"][cfg]["mrr"] for r in eval_records),
            "mean_chunk_count": mean(r["metrics"][cfg]["count"] for r in eval_records),
        }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump({"summary": summary, "per_query": eval_records}, f, ensure_ascii=False, indent=2)
    print(f"\nSaved detailed evaluation to {OUTPUT_FILE}", flush=True)

    # Format output tables
    display_rows = [
        ("BM25 Top 5", "bm25_top5"),
        ("BM25 Top 10", "bm25_top10"),
        ("BM25 Top 20", "bm25_top20"),
        ("Dense Top 5", "dense_top5"),
        ("Dense Top 10", "dense_top10"),
        ("Dense Top 20", "dense_top20"),
        ("Reranker Top 5", "rerank_top5"),
        ("Reranker Top 10", "rerank_top10"),
        ("Reranker Top 20", "rerank_top20"),
    ]

    title = "KẾT QUẢ ĐÁNH GIÁ 31 QUERY LEGACY (CORPUS-V0.2): HIỆU QUẢ CÁC CƠ CHẾ EXPANSION"
    print("\n" + "=" * 115, flush=True)
    print(f"{title:^115}", flush=True)
    print("=" * 115, flush=True)
    print(
        f"{'Phương pháp':<16} | {'Base Rec':<9} | {'Clause Rec':<11} | {'Cross-Ref Rec':<14} | {'Combined Rec':<13} | {'Δ Comb vs Base':<15} | {'Art Hit':<9} | {'Avg Chunks':<10}",
        flush=True,
    )
    print("-" * 115, flush=True)

    for label, base_key in display_rows:
        r_base = summary[f"{base_key}_base"]["mean_recall"] * 100
        r_clause = summary[f"{base_key}_clause"]["mean_recall"] * 100
        r_xref = summary[f"{base_key}_crossref"]["mean_recall"] * 100
        r_comb = summary[f"{base_key}_combined"]["mean_recall"] * 100
        diff = r_comb - r_base
        rel = (diff / r_base * 100) if r_base > 0 else 0.0
        art_hit = summary[f"{base_key}_combined"]["art_hit_rate"] * 100
        avg_c = summary[f"{base_key}_combined"]["mean_chunk_count"]
        print(
            f"{label:<16} | {r_base:>8.1f}% | {r_clause:>10.1f}% | {r_xref:>13.1f}% | {r_comb:>12.1f}% | {diff:>+6.1f}% ({rel:>+5.1f}%) | {art_hit:>8.1f}% | {avg_c:>10.1f}",
            flush=True,
        )
    print("-" * 115, flush=True)


if __name__ == "__main__":
    main()
