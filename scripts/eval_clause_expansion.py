#!/usr/bin/env python3
"""Evaluate Clause-Level Expansion (Mở rộng theo khoản) on 40-query benchmark.

Rule: Khi một điểm (point) thuộc khoản (clause) được retrieve, toàn bộ các điểm khác
trong cùng khoản đó sẽ được tự động gom vào tập kết quả.
"""

import os
import sys
import json
import time
from pathlib import Path
from collections import defaultdict
from statistics import mean

ROOT = Path("/home/minhkha/kk/TTTN/legal-agentic-rag-next")
sys.path.insert(0, str(ROOT / "src"))

os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

from legal_rag.retrieval.sparse import PersistentBM25Retriever
from legal_rag.retrieval.dense import DenseRetriever
from legal_rag.retrieval.reranker import union_candidates, BGEReranker

CORPUS = ROOT / "data/versions/corpus-v0.2/chunks/chunks.jsonl"
IX = ROOT / "experiments/indexes/corpus-v0.2"
CFP = "7525978bfbf645d2ace8955d52a06906985799350c82c7b9fd797d246f80b827"
RR = "953dc6f6f85a1b2dbfca4c34a2796e7dde08d41e"
EVAL_FILE = ROOT / "eval-sets/retrieval/baseline_eval_40.jsonl"
OUTPUT_FILE = ROOT / "experiments/retrieval/corpus-v0.2/clause_expansion_eval_results.json"

def build_clause_mapping(corpus_path: Path):
    """Build bidirectional mapping between chunk_id and clause_id."""
    chunks_by_clause = defaultdict(list)
    chunk_to_clause = {}
    
    with open(corpus_path, "r", encoding="utf-8") as f:
        for line in f:
            c = json.loads(line)
            cid = c["chunk_id"]
            aid = c.get("article_id")
            clause = c.get("clause")
            if aid and clause is not None:
                ckey = f"{aid}_khoan-{clause}"
            elif aid:
                ckey = aid
            else:
                ckey = cid
            chunks_by_clause[ckey].append(cid)
            chunk_to_clause[cid] = ckey
            
    return chunk_to_clause, chunks_by_clause

def expand_chunks_by_clause(chunk_ids: list[str], chunk_to_clause, chunks_by_clause) -> list[str]:
    """Given a list of chunk IDs, expand to include all siblings in the same clause."""
    seen = set()
    expanded = []
    for cid in chunk_ids:
        ckey = chunk_to_clause.get(cid, cid)
        siblings = chunks_by_clause.get(ckey, [cid])
        for sib in siblings:
            if sib not in seen:
                seen.add(sib)
                expanded.append(sib)
    return expanded

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
    print("Building clause index mapping...")
    chunk_to_clause, chunks_by_clause = build_clause_mapping(CORPUS)
    print(f"Total chunks indexed: {len(chunk_to_clause)}, Total clauses: {len(chunks_by_clause)}")

    print("\nLoading retrieval models...")
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
    print(f"Loaded {len(queries)} queries.")

    # Configurations to test
    # Each entry: (name, base_getter, do_expand)
    eval_records = []

    print("\nRunning evaluation on 40 queries...")
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

        # Slices
        cand_sets = {
            # BM25
            "bm25_top5": bm_cids[:5],
            "bm25_top5_expanded": expand_chunks_by_clause(bm_cids[:5], chunk_to_clause, chunks_by_clause),
            "bm25_top10": bm_cids[:10],
            "bm25_top10_expanded": expand_chunks_by_clause(bm_cids[:10], chunk_to_clause, chunks_by_clause),
            "bm25_top20": bm_cids[:20],
            "bm25_top20_expanded": expand_chunks_by_clause(bm_cids[:20], chunk_to_clause, chunks_by_clause),
            
            # Dense
            "dense_top5": den_cids[:5],
            "dense_top5_expanded": expand_chunks_by_clause(den_cids[:5], chunk_to_clause, chunks_by_clause),
            "dense_top10": den_cids[:10],
            "dense_top10_expanded": expand_chunks_by_clause(den_cids[:10], chunk_to_clause, chunks_by_clause),
            "dense_top20": den_cids[:20],
            "dense_top20_expanded": expand_chunks_by_clause(den_cids[:20], chunk_to_clause, chunks_by_clause),

            # Reranker
            "rerank_top5": rr_cids[:5],
            "rerank_top5_expanded": expand_chunks_by_clause(rr_cids[:5], chunk_to_clause, chunks_by_clause),
            "rerank_top10": rr_cids[:10],
            "rerank_top10_expanded": expand_chunks_by_clause(rr_cids[:10], chunk_to_clause, chunks_by_clause),
            "rerank_top20": rr_cids[:20],
            "rerank_top20_expanded": expand_chunks_by_clause(rr_cids[:20], chunk_to_clause, chunks_by_clause),
        }

        row = {
            "query_id": qid,
            "source": source,
            "gold_count": len(gold_chunks),
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

    # Output JSON
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

    # Print formatted comparative report
    print("\n" + "=" * 95)
    print(f"{'KẾT QUẢ SO SÁNH: TRƯỚC VÀ SAU KHI MỞ RỘNG THEO KHOẢN (CLAUSE EXPANSION)':^95}")
    print("=" * 95)

    pairs = [
        ("BM25 Top 5", "bm25_top5", "bm25_top5_expanded"),
        ("BM25 Top 10", "bm25_top10", "bm25_top10_expanded"),
        ("BM25 Top 20", "bm25_top20", "bm25_top20_expanded"),
        ("Dense Top 5", "dense_top5", "dense_top5_expanded"),
        ("Dense Top 10", "dense_top10", "dense_top10_expanded"),
        ("Dense Top 20", "dense_top20", "dense_top20_expanded"),
        ("Reranker Top 5", "rerank_top5", "rerank_top5_expanded"),
        ("Reranker Top 10", "rerank_top10", "rerank_top10_expanded"),
        ("Reranker Top 20", "rerank_top20", "rerank_top20_expanded"),
    ]

    for group_title, summary, n in [
        ("TOÀN BỘ 40 QUERIES", all_summary, 40),
        ("10 LEGACY QUERIES (AI Focus)", legacy_summary, 10),
        ("30 NEW QUERIES (17 Documents Cross-Corpus)", new_summary, 30),
    ]:
        print(f"\n>>> {group_title} (N={n})")
        print("-" * 95)
        print(f"{'Phương pháp':<18} | {'Recall Gốc':<11} | {'Recall Mở Rộng':<14} | {'Tăng tuyệt đối':<14} | {'Tăng tương đối':<15} | {'Avg Chunks':<10}")
        print("-" * 95)
        for label, base_k, exp_k in pairs:
            base_r = summary[base_k]["mean_recall"] * 100
            exp_r = summary[exp_k]["mean_recall"] * 100
            diff = exp_r - base_r
            rel_diff = (diff / base_r * 100) if base_r > 0 else 0.0
            avg_c = summary[exp_k]["mean_chunk_count"]
            print(f"{label:<18} | {base_r:>9.1f}% | {exp_r:>12.1f}% | {diff:>+12.1f}% | {rel_diff:>+13.1f}% | {avg_c:>10.1f}")
        print("-" * 95)

if __name__ == "__main__":
    main()
