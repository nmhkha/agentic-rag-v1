#!/usr/bin/env python3
"""Evaluate corpus-v2.1 across BM25, Dense (Jina-v3), BGE-Reranker-v2-m3, and Expansions.

Compares directly against frozen corpus-v0.2 results on:
1. 31 Legacy Queries (eval-sets/retrieval/retrieval_eval.jsonl)
2. 40 Cross-Corpus Benchmark Queries (eval-sets/retrieval/baseline_eval_40.jsonl)
"""

from __future__ import annotations

import glob
import json
import os
import sys
import time
from pathlib import Path
from statistics import mean

try:
    import torch  # noqa: F401
except ImportError:
    if not os.environ.get("_LEGAL_RAG_REEXEC"):
        candidates = sorted(
            glob.glob(str(Path.home() / "*conda*/envs/*/bin/python"))
            + glob.glob(str(Path.home() / ".conda/envs/*/bin/python"))
            + glob.glob(str(Path.home() / "*conda*/bin/python"))
            + glob.glob(str(Path.home() / ".venv*/bin/python"))
            + glob.glob("/opt/*conda*/envs/*/bin/python")
        )
        for cand in candidates:
            env_root = Path(cand).parent.parent
            if os.access(cand, os.X_OK) and list((env_root / "lib").glob("python*/site-packages/torch")):
                os.environ["_LEGAL_RAG_REEXEC"] = "1"
                os.execv(cand, [cand, *sys.argv])

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

from legal_rag.cross_reference import CrossReferenceResolver
from legal_rag.evaluation.metrics import aggregate_retrieval, retrieval_query_metrics
from legal_rag.retrieval.dense import DenseRetriever
from legal_rag.retrieval.reranker import BGEReranker, union_candidates
from legal_rag.retrieval.sparse import PersistentBM25Retriever

CORPUS_V21 = ROOT / "data/versions/corpus-v2.1/chunks/chunks.jsonl"
MANIFEST_V21 = ROOT / "data/versions/corpus-v2.1/corpus_manifest.json"
IX_V21 = ROOT / "experiments/indexes/corpus-v2.1"
RR_REV = "953dc6f6f85a1b2dbfca4c34a2796e7dde08d41e"

EVAL_31 = ROOT / "eval-sets/retrieval/retrieval_eval.jsonl"
EVAL_40 = ROOT / "eval-sets/retrieval/baseline_eval_40.jsonl"

OUT_DIR = ROOT / "experiments/retrieval/corpus-v2.1"
OUT_31 = OUT_DIR / "legacy_31_eval_results.json"
OUT_40 = OUT_DIR / "baseline_40_eval_results.json"

V02_31 = ROOT / "experiments/retrieval/corpus-v0.2/legacy_31_eval_results.json"
V02_40 = ROOT / "experiments/retrieval/corpus-v0.2/baseline_40_eval_results.json"


def compute_legacy_metrics(retrieved_cids: list[str], gold_cids: set[str], chunks_dict: dict):
    if not gold_cids:
        return 0.0, 0, 0, 0.0
    ret_set = set(retrieved_cids)
    hits = len(ret_set.intersection(gold_cids))
    recall = hits / len(gold_cids)
    chunk_hit = int(hits > 0)
    gold_articles = {chunks_dict.get(c, {}).get("article_id") for c in gold_cids if chunks_dict.get(c)}
    ret_articles = {chunks_dict.get(c, {}).get("article_id") for c in ret_set if chunks_dict.get(c)}
    art_hit = int(bool(gold_articles & ret_articles))
    rr = 0.0
    for rank, cid in enumerate(retrieved_cids, 1):
        if cid in gold_cids:
            rr = 1.0 / rank
            break
    return recall, chunk_hit, art_hit, rr


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest = json.loads(MANIFEST_V21.read_text(encoding="utf-8"))
    cfp = manifest["corpus_fingerprint_sha256"]

    print("Loading corpus-v2.1 chunks, indexes, and models...", flush=True)
    t0 = time.time()
    chunks_dict = {
        json.loads(line)["chunk_id"]: json.loads(line)
        for line in CORPUS_V21.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }
    resolver = CrossReferenceResolver(CORPUS_V21)
    bm = PersistentBM25Retriever(
        CORPUS_V21,
        IX_V21 / "sparse/sparse_index.json",
        IX_V21 / "manifests/sparse_manifest.json",
        corpus_fingerprint=cfp,
    )
    den = DenseRetriever(CORPUS_V21, IX_V21 / "dense", corpus_fingerprint=cfp, load_encoder=True)
    scorer = BGEReranker(revision=RR_REV, batch_size=8)
    print(f"Loaded in {time.time() - t0:.2f}s", flush=True)

    # =========================================================================
    # 1. Evaluate 31 Legacy Queries
    # =========================================================================
    if OUT_31.exists() and "--force-31" not in sys.argv:
        print(f"\n[Info] {OUT_31.name} already exists. Loading saved summary to save time...", flush=True)
        summary_31 = json.loads(OUT_31.read_text(encoding="utf-8"))["summary"]
    else:
        q31_list = [json.loads(l) for l in EVAL_31.read_text(encoding="utf-8").splitlines() if l.strip()]
        print(f"\nEvaluating {len(q31_list)} Legacy Queries on corpus-v2.1...", flush=True)
        eval_31_records = []
        for idx, q_item in enumerate(q31_list, 1):
            t_q = time.time()
            qid = q_item["query_id"]
            q_text = q_item["query"]
            gold_cids = set(q_item["gold_chunk_ids"])

            bm_res = bm.search(q_text, 20)
            bm_cids = [x["chunk"]["chunk_id"] for x in bm_res]

            den_res = den.search(q_text, 20)
            den_cids = [x["chunk"]["chunk_id"] for x in den_res]

            u_res = union_candidates(bm_res, den_res)
            rr_res = scorer.rerank(q_text, u_res, len(u_res))
            rr_cids = [x["chunk"]["chunk_id"] for x in rr_res]

            base_lists = {
                "bm25_top5": bm_cids[:5],
                "bm25_top10": bm_cids[:10],
                "bm25_top20": bm_cids[:20],
                "dense_top5": den_cids[:5],
                "dense_top10": den_cids[:10],
                "dense_top20": den_cids[:20],
                "rerank_top5": rr_cids[:5],
                "rerank_top10": rr_cids[:10],
                "rerank_top20": rr_cids[:20],
            }
            q_metrics = {}
            for name, cids in base_lists.items():
                r_b, h_b, ah_b, rr_b = compute_legacy_metrics(cids, gold_cids, chunks_dict)
                q_metrics[f"{name}_base"] = {"count": len(cids), "recall": r_b, "hit": h_b, "art_hit": ah_b, "mrr": rr_b}

                c_cids = resolver.expand(cids, enable_clause_expansion=True, enable_cross_references=False)
                r_c, h_c, ah_c, rr_c = compute_legacy_metrics(c_cids, gold_cids, chunks_dict)
                q_metrics[f"{name}_clause"] = {"count": len(c_cids), "recall": r_c, "hit": h_c, "art_hit": ah_c, "mrr": rr_c}

                x_cids = resolver.expand(cids, enable_clause_expansion=False, enable_cross_references=True)
                r_x, h_x, ah_x, rr_x = compute_legacy_metrics(x_cids, gold_cids, chunks_dict)
                q_metrics[f"{name}_crossref"] = {"count": len(x_cids), "recall": r_x, "hit": h_x, "art_hit": ah_x, "mrr": rr_x}

                cb_cids = resolver.expand(cids, enable_clause_expansion=True, enable_cross_references=True)
                r_cb, h_cb, ah_cb, rr_cb = compute_legacy_metrics(cb_cids, gold_cids, chunks_dict)
                q_metrics[f"{name}_combined"] = {"count": len(cb_cids), "recall": r_cb, "hit": h_cb, "art_hit": ah_cb, "mrr": rr_cb}

            eval_31_records.append({
                "query_id": qid,
                "query": q_text,
                "difficulty": q_item.get("difficulty", "unknown"),
                "gold_count": len(gold_cids),
                "gold_chunk_ids": list(gold_cids),
                "metrics": q_metrics,
            })
            print(f"  [31 Legacy: {idx}/{len(q31_list)}] {qid} ({time.time() - t_q:.1f}s)", flush=True)

        summary_31 = {}
        for k in eval_31_records[0]["metrics"].keys():
            summary_31[k] = {
                "mean_recall": mean(r["metrics"][k]["recall"] for r in eval_31_records),
                "hit_rate": mean(r["metrics"][k]["hit"] for r in eval_31_records),
                "art_hit_rate": mean(r["metrics"][k]["art_hit"] for r in eval_31_records),
                "mrr": mean(r["metrics"][k]["mrr"] for r in eval_31_records),
                "mean_chunk_count": mean(r["metrics"][k]["count"] for r in eval_31_records),
            }
        OUT_31.write_text(
            json.dumps({"summary": summary_31, "per_query": eval_31_records}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    # =========================================================================
    # 2. Evaluate 40 Benchmark Queries
    # =========================================================================
    q40_list = [json.loads(l) for l in EVAL_40.read_text(encoding="utf-8").splitlines() if l.strip()]
    print(f"\nEvaluating {len(q40_list)} Cross-Corpus Benchmark Queries on corpus-v2.1...", flush=True)
    stages = ["bm25", "dense", "union", "rerank_top5", "rerank_top10"]
    query_results = {s: [] for s in stages}
    detailed_40 = []

    for idx, q_item in enumerate(q40_list, 1):
        t_q = time.time()
        qid = q_item["query_id"]
        query_text = q_item["query"]
        gold_chunks = q_item["gold_chunk_ids"]
        gold_articles = q_item["gold_article_ids"]

        bm_res = bm.search(query_text, 20)
        bm_chunks = [x["chunk"]["chunk_id"] for x in bm_res]
        bm_articles = [x["chunk"].get("article_id") for x in bm_res if x["chunk"].get("article_id")]

        den_res = den.search(query_text, 20)
        den_chunks = [x["chunk"]["chunk_id"] for x in den_res]
        den_articles = [x["chunk"].get("article_id") for x in den_res if x["chunk"].get("article_id")]

        u_res = union_candidates(bm_res, den_res)
        u_chunks = [x.chunk["chunk_id"] for x in u_res]
        u_articles = [x.chunk.get("article_id") for x in u_res if x.chunk.get("article_id")]

        rr_res = scorer.rerank(query_text, u_res, len(u_res))
        rr5_chunks = [x["chunk"]["chunk_id"] for x in rr_res[:5]]
        rr5_articles = [x["chunk"].get("article_id") for x in rr_res[:5] if x["chunk"].get("article_id")]
        rr10_chunks = [x["chunk"]["chunk_id"] for x in rr_res[:10]]
        rr10_articles = [x["chunk"].get("article_id") for x in rr_res[:10] if x["chunk"].get("article_id")]

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
        detailed_40.append(row_eval)
        print(
            f"  [40 Benchmark: {idx}/{len(q40_list)}] {qid} ({q_item.get('source', '')}) evaluated in {time.time() - t_q:.1f}s",
            flush=True,
        )

    aggregates_40 = {"all_40": {}, "legacy_10": {}, "new_30": {}}
    for s in stages:
        all_m = query_results[s]
        leg_m = [m for m in all_m if m["source"] == "legacy_retrieval_eval"]
        new_m = [m for m in all_m if m["source"] == "new_design"]
        aggregates_40["all_40"][s] = aggregate_retrieval(all_m)
        aggregates_40["legacy_10"][s] = aggregate_retrieval(leg_m)
        aggregates_40["new_30"][s] = aggregate_retrieval(new_m)

    OUT_40.write_text(
        json.dumps(
            {
                "benchmark_file": str(EVAL_40),
                "corpus_version": "corpus-v2.1",
                "total_queries": len(q40_list),
                "aggregates": aggregates_40,
                "per_query": detailed_40,
            },
            ensure_ascii=False,
            indent=2,
        ) + "\n",
        encoding="utf-8",
    )

    # Print comparison summary
    v02_31_sum = json.loads(V02_31.read_text(encoding="utf-8"))["summary"]
    print("\n================ 31 LEGACY QUERIES: v0.2 vs v2.1 ================")
    for key in [
        "bm25_top5_base",
        "dense_top5_base",
        "rerank_top5_base",
        "rerank_top10_base",
        "rerank_top20_base",
        "rerank_top5_clause",
        "rerank_top5_combined",
        "rerank_top10_combined",
    ]:
        r02 = v02_31_sum[key]["mean_recall"] * 100
        r21 = summary_31[key]["mean_recall"] * 100
        m02 = v02_31_sum[key]["mrr"] * 100
        m21 = summary_31[key]["mrr"] * 100
        print(f"{key:24s} | Recall: {r02:6.2f}% -> {r21:6.2f}% ({r21-r02:+6.2f}%) | MRR: {m02:6.2f}% -> {m21:6.2f}% ({m21-m02:+6.2f}%)")

    v02_40_agg = json.loads(V02_40.read_text(encoding="utf-8"))["aggregates"]
    for subset in ["all_40", "new_30"]:
        print(f"\n================ {subset.upper()}: v0.2 vs v2.1 ================")
        for s in stages:
            c02 = v02_40_agg[subset][s]["chunk_level"]
            c21 = aggregates_40[subset][s]["chunk_level"]
            r5_02, r5_21 = c02["recall_at_5"] * 100, c21["recall_at_5"] * 100
            r10_02, r10_21 = c02["recall_at_10"] * 100, c21["recall_at_10"] * 100
            mrr_02, mrr_21 = c02["mrr_at_10"] * 100, c21["mrr_at_10"] * 100
            print(
                f"{s:14s} | R@5: {r5_02:5.2f}%->{r5_21:5.2f}% ({r5_21-r5_02:+5.2f}%) "
                f"| R@10: {r10_02:5.2f}%->{r10_21:5.2f}% ({r10_21-r10_02:+5.2f}%) "
                f"| MRR@10: {mrr_02:5.2f}%->{mrr_21:5.2f}% ({mrr_21-mrr_02:+5.2f}%)"
            )


if __name__ == "__main__":
    main()
