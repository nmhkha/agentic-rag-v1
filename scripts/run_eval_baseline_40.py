#!/usr/bin/env python3
"""Run baseline evaluation (BM25, Dense, Union, Reranker) on baseline_eval_40.jsonl."""

import os
import sys
import json
import time
from pathlib import Path

ROOT = Path("/home/minhkha/kk/TTTN/legal-agentic-rag-next")
sys.path.insert(0, str(ROOT / "src"))

os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

from legal_rag.retrieval.sparse import PersistentBM25Retriever
from legal_rag.retrieval.dense import DenseRetriever
from legal_rag.retrieval.reranker import union_candidates, BGEReranker
from legal_rag.evaluation.metrics import retrieval_query_metrics, aggregate_retrieval

CORPUS = ROOT / "data/versions/corpus-v0.2/chunks/chunks.jsonl"
IX = ROOT / "experiments/indexes/corpus-v0.2"
CFP = "7525978bfbf645d2ace8955d52a06906985799350c82c7b9fd797d246f80b827"
RR = "953dc6f6f85a1b2dbfca4c34a2796e7dde08d41e"
EVAL_FILE = ROOT / "eval-sets/retrieval/baseline_eval_40.jsonl"
OUTPUT_FILE = ROOT / "experiments/retrieval/corpus-v0.2/baseline_40_eval_results.json"

def main():
    print("Loading models and indexes...")
    t0 = time.time()
    bm = PersistentBM25Retriever(
        CORPUS,
        IX / "sparse/sparse_index.json",
        IX / "manifests/sparse_manifest.json",
        corpus_fingerprint=CFP,
    )
    den = DenseRetriever(CORPUS, IX / "dense", corpus_fingerprint=CFP, load_encoder=True)
    scorer = BGEReranker(revision=RR, batch_size=8)
    print(f"Models loaded in {time.time() - t0:.2f}s")

    queries = []
    with open(EVAL_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                queries.append(json.loads(line))
    print(f"Loaded {len(queries)} evaluation queries.")

    stages = ["bm25", "dense", "union", "rerank_top5", "rerank_top10"]
    query_results = {s: [] for s in stages}
    detailed_per_query = []

    print("\nRunning retrieval and reranking for 40 queries...")
    for idx, q_item in enumerate(queries, 1):
        qid = q_item["query_id"]
        query_text = q_item["query"]
        gold_chunks = q_item["gold_chunk_ids"]
        gold_articles = q_item["gold_article_ids"]

        # 1. BM25 search
        bm_res = bm.search(query_text, 20)
        bm_chunks = [x["chunk"]["chunk_id"] for x in bm_res]
        bm_articles = [x["chunk"].get("article_id") for x in bm_res if x["chunk"].get("article_id")]

        # 2. Dense search
        den_res = den.search(query_text, 20)
        den_chunks = [x["chunk"]["chunk_id"] for x in den_res]
        den_articles = [x["chunk"].get("article_id") for x in den_res if x["chunk"].get("article_id")]

        # 3. Union
        u_res = union_candidates(bm_res, den_res)
        u_chunks = [x.chunk["chunk_id"] for x in u_res]
        u_articles = [x.chunk.get("article_id") for x in u_res if x.chunk.get("article_id")]

        # 4. Rerank
        rr_res = scorer.rerank(query_text, u_res, len(u_res))
        rr_top5 = rr_res[:5]
        rr_top10 = rr_res[:10]

        rr5_chunks = [x["chunk"]["chunk_id"] for x in rr_top5]
        rr5_articles = [x["chunk"].get("article_id") for x in rr_top5 if x["chunk"].get("article_id")]

        rr10_chunks = [x["chunk"]["chunk_id"] for x in rr_top10]
        rr10_articles = [x["chunk"].get("article_id") for x in rr_top10 if x["chunk"].get("article_id")]

        stage_candidates = {
            "bm25": (bm_chunks, bm_articles),
            "dense": (den_chunks, den_articles),
            "union": (u_chunks, u_articles),
            "rerank_top5": (rr5_chunks, rr5_articles),
            "rerank_top10": (rr10_chunks, rr10_articles),
        }

        row_eval = {
            "query_id": qid,
            "query": query_text,
            "source": q_item.get("source", "unknown"),
            "difficulty": q_item.get("difficulty", "unknown"),
            "metrics": {},
        }

        for s in stages:
            c_ids, a_ids = stage_candidates[s]
            m = retrieval_query_metrics(
                gold_chunk_ids=gold_chunks,
                gold_article_ids=gold_articles,
                retrieved_chunk_ids=c_ids,
                retrieved_article_ids=a_ids,
            )
            m["query_id"] = qid
            m["source"] = q_item.get("source", "unknown")
            query_results[s].append(m)
            row_eval["metrics"][s] = m

        detailed_per_query.append(row_eval)
        if idx % 10 == 0 or idx == len(queries):
            print(f"  Processed {idx}/{len(queries)} queries...")

    # Aggregate metrics
    print("\nAggregating metrics...")

    def compute_aggregates(subset_filter=None):
        out = {}
        for s in stages:
            rows = query_results[s]
            if subset_filter:
                rows = [r for r in rows if subset_filter(r)]
            out[s] = aggregate_retrieval(rows)
        return out

    all_agg = compute_aggregates()
    legacy_agg = compute_aggregates(lambda r: r.get("source") == "legacy_retrieval_eval")
    new_agg = compute_aggregates(lambda r: r.get("source") == "new_design")

    final_payload = {
        "benchmark_file": str(EVAL_FILE),
        "total_queries": len(queries),
        "aggregates": {
            "all_40": all_agg,
            "legacy_10": legacy_agg,
            "new_30": new_agg,
        },
        "per_query": detailed_per_query,
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(final_payload, f, ensure_ascii=False, indent=2)
    print(f"\nSaved results to {OUTPUT_FILE}")

    # Print summary table
    print("\n" + "=" * 90)
    print(f"{'RETRIEVAL BASELINE BENCHMARK RESULTS (40 QUERIES)':^90}")
    print("=" * 90)

    for group_name, agg in [
        ("TOÀN BỘ 40 QUERIES", all_agg),
        ("10 LEGACY QUERIES (AI Focus)", legacy_agg),
        ("30 NEW DESIGN QUERIES (17 Documents Cross-Corpus)", new_agg),
    ]:
        print(f"\n>>> PHÂN TÍCH: {group_name} (N={agg['bm25']['query_count']})")
        print("-" * 90)
        print(f"{'Stage':<15} | {'Chunk H@1':<10} | {'Chunk H@3':<10} | {'Chunk H@5':<10} | {'Chunk R@5':<10} | {'Chunk R@10':<10} | {'Chunk MRR':<10}")
        print("-" * 90)
        for s in stages:
            cl = agg[s]["chunk_level"]
            print(
                f"{s:<15} | "
                f"{cl['hit_at_1']*100:>8.1f}% | "
                f"{cl['hit_at_3']*100:>8.1f}% | "
                f"{cl['hit_at_5']*100:>8.1f}% | "
                f"{cl['recall_at_5']*100:>8.1f}% | "
                f"{cl['recall_at_10']*100:>8.1f}% | "
                f"{cl['mrr_at_10']:>9.3f}"
            )
        print("-" * 90)
        print(f"{'Stage':<15} | {'Art H@1':<10} | {'Art H@3':<10} | {'Art H@5':<10} | {'Art MRR':<10}")
        print("-" * 90)
        for s in stages:
            al = agg[s]["article_level"]
            print(
                f"{s:<15} | "
                f"{al['hit_at_1']*100:>8.1f}% | "
                f"{al['hit_at_3']*100:>8.1f}% | "
                f"{al['hit_at_5']*100:>8.1f}% | "
                f"{al['mrr_at_10']:>9.3f}"
            )
        print("-" * 90)

if __name__ == "__main__":
    main()
