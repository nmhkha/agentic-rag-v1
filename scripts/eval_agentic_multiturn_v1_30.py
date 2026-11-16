#!/usr/bin/env python3
"""Evaluate Agentic Multi-turn Retrieval (v1) on 30 New Benchmark Queries over frozen corpus-v0.2.

Measures Recall, Hit Rate, and Chunk Count across:
1. Turn 1 (Initial Single-Pass Retrieval Top-5 / Top-10)
2. Turn 2 (Agentic V1 First-Hop Expansion based on Coverage Check)
3. Turn 3 (Agentic V1 Second-Hop Expansion for remaining gaps)
4. Turn 3 + Deterministic Expansion (Clause Expansion + Cross-Reference Following)
"""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path
from statistics import mean

ROOT = Path("/home/minhkha/kk/TTTN/legal-agentic-rag-next")
sys.path.insert(0, str(ROOT / "src"))

os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

# Load environment variables from .env
env_file = ROOT / ".env"
if env_file.exists():
    with open(env_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                os.environ[k.strip()] = v.strip()

from legal_rag.agentic.v1.nodes import check_evidence_sufficiency
from legal_rag.agentic.v1.state import AgentState
from legal_rag.cross_reference import CrossReferenceResolver
from legal_rag.llm_client import OpenAICompatibleClient
from legal_rag.retrieval.pipeline import DEFAULT_TOP_K, Evidence, RetrievalPipeline
from legal_rag.retrieval.reranker import RerankerRetriever

CORPUS = ROOT / "data/versions/corpus-v0.2/chunks/chunks.jsonl"
DENSE_IX = ROOT / "experiments/indexes/corpus-v0.2/dense"
EVAL_FILE = ROOT / "eval-sets/retrieval/baseline_eval_40.jsonl"
OUTPUT_FILE = ROOT / "experiments/retrieval/corpus-v0.2/agentic_v1_multiturn_30_results.json"


def compute_metrics(retrieved_cids: list[str], gold_cids: set[str], chunks_dict: dict):
    if not gold_cids:
        return 0.0, 0, 0
    ret_set = set(retrieved_cids)
    hits = len(ret_set.intersection(gold_cids))
    recall = hits / len(gold_cids)
    chunk_hit = int(hits > 0)

    # Article-level hit
    gold_articles = {chunks_dict.get(c, {}).get("article_id") for c in gold_cids if chunks_dict.get(c)}
    ret_articles = {chunks_dict.get(c, {}).get("article_id") for c in ret_set if chunks_dict.get(c)}
    art_hit = int(bool(gold_articles & ret_articles))

    return recall, chunk_hit, art_hit


def main():
    print("Loading Corpus Chunks...", flush=True)
    t0 = time.time()
    chunks_dict = {}
    with open(CORPUS, "r", encoding="utf-8") as f:
        for line in f:
            c = json.loads(line)
            chunks_dict[c["chunk_id"]] = c
    print(f"Loaded {len(chunks_dict)} chunks in {time.time() - t0:.2f}s", flush=True)

    print("\nInitializing Pipeline on corpus-v0.2, Resolver, and LLM Client...", flush=True)
    t1 = time.time()
    retriever = RerankerRetriever(corpus_path=CORPUS, index_dir=DENSE_IX, batch_size=8)
    pipeline = RetrievalPipeline(retriever=retriever)
    resolver = CrossReferenceResolver(CORPUS)

    model = os.getenv("RAG_LLM_MODEL", "gemini-3.5-flash-lite")
    base_url = os.getenv("RAG_LLM_BASE_URL", "https://generativelanguage.googleapis.com/v1beta/openai/")
    api_key = os.getenv("RAG_LLM_API_KEY", "")
    client = OpenAICompatibleClient(model=model, base_url=base_url, api_key=api_key)
    print(f"Components loaded in {time.time() - t1:.2f}s", flush=True)

    # Load 30 new queries
    queries = []
    with open(EVAL_FILE, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            if item.get("source") == "new_design":
                queries.append(item)
    print(f"Loaded {len(queries)} new benchmark queries across 17 legal instruments.", flush=True)

    def _call_llm(s: AgentState, stage: str, prompt: str) -> str:
        for attempt in range(4):
            try:
                return client.generate(prompt)
            except Exception as e:
                if attempt == 3:
                    raise
                print(f"    [Warning] LLM retry {attempt+1}/3 due to: {e}", flush=True)
                time.sleep(2 * (attempt + 1))

    results = []
    print(f"\nRunning 3-Turn Agentic Multi-turn Evaluation on {len(queries)} queries...", flush=True)

    for idx, q_item in enumerate(queries, 1):
        qid = q_item["query_id"]
        q_text = q_item["query"]
        gold_cids = set(q_item["gold_chunk_ids"])
        start_q = time.time()

        # ==========================================
        # TURN 1: Initial Retrieval (Single-Pass)
        # ==========================================
        t1_evidences = pipeline.retrieve(q_text, top_k=DEFAULT_TOP_K)
        t1_cids = [e.chunk_id for e in t1_evidences]

        rec1, hit1, art_hit1 = compute_metrics(t1_cids, gold_cids, chunks_dict)

        # Agent Coverage Assessment
        state = AgentState(query=q_text, run_id=f"run_{qid}")
        state.current_evidence = list(t1_evidences)
        cov1 = check_evidence_sufficiency(state, _call_llm)

        # ==========================================
        # TURN 2: Agentic Hop 1 (Targeted Search)
        # ==========================================
        t2_accumulated_evidences = list(t1_evidences)
        t2_cids = list(t1_cids)
        seen_cids = set(t1_cids)
        turn2_subqueries = []

        if not cov1.sufficient and cov1.missing_aspects:
            for aspect in cov1.missing_aspects[:2]:
                sub_q = f"{aspect} {q_text}"
                turn2_subqueries.append(sub_q)
                sub_res = pipeline.retrieve(sub_q, top_k=DEFAULT_TOP_K)
                for e in sub_res:
                    if e.chunk_id not in seen_cids:
                        seen_cids.add(e.chunk_id)
                        t2_accumulated_evidences.append(e)
                        t2_cids.append(e.chunk_id)

        rec2, hit2, art_hit2 = compute_metrics(t2_cids, gold_cids, chunks_dict)

        # Agent Coverage Re-assessment for Turn 3
        state.current_evidence = t2_accumulated_evidences[:DEFAULT_TOP_K * 2]
        cov2 = check_evidence_sufficiency(state, _call_llm)

        # ==========================================
        # TURN 3: Agentic Hop 2 (Iterative Search)
        # ==========================================
        t3_cids = list(t2_cids)
        turn3_subqueries = []

        if not cov2.sufficient and cov2.missing_aspects:
            for aspect in cov2.missing_aspects[:2]:
                sub_q = f"{aspect} {q_text}"
                turn3_subqueries.append(sub_q)
                sub_res = pipeline.retrieve(sub_q, top_k=DEFAULT_TOP_K)
                for e in sub_res:
                    if e.chunk_id not in seen_cids:
                        seen_cids.add(e.chunk_id)
                        t3_cids.append(e.chunk_id)

        rec3, hit3, art_hit3 = compute_metrics(t3_cids, gold_cids, chunks_dict)

        # ==========================================
        # COMBINED: Agentic + Deterministic Resolver
        # ==========================================
        comb_cids = resolver.expand(
            t3_cids,
            enable_clause_expansion=True,
            enable_cross_references=True,
            max_source_chunks_for_refs=5,
            max_total_chunks=40,
        )
        rec_comb, hit_comb, art_hit_comb = compute_metrics(comb_cids, gold_cids, chunks_dict)

        q_elapsed = time.time() - start_q
        row = {
            "query_id": qid,
            "query": q_text,
            "gold_count": len(gold_cids),
            "turn1": {"recall": rec1, "hit": hit1, "art_hit": art_hit1, "chunks": len(t1_cids)},
            "turn2": {
                "recall": rec2,
                "hit": hit2,
                "art_hit": art_hit2,
                "chunks": len(t2_cids),
                "subqueries": turn2_subqueries,
            },
            "turn3": {
                "recall": rec3,
                "hit": hit3,
                "art_hit": art_hit3,
                "chunks": len(t3_cids),
                "subqueries": turn3_subqueries,
            },
            "combined": {
                "recall": rec_comb,
                "hit": hit_comb,
                "art_hit": art_hit_comb,
                "chunks": len(comb_cids),
            },
            "elapsed": q_elapsed,
        }
        results.append(row)

        print(
            f"  [{idx:02d}/{len(queries)}] {qid} ({q_elapsed:.1f}s) | "
            f"T1 Rec: {rec1*100:.1f}% -> T2 Rec: {rec2*100:.1f}% -> T3 Rec: {rec3*100:.1f}% -> Comb: {rec_comb*100:.1f}% (ArtHit: {art_hit_comb*100:.0f}%)",
            flush=True,
        )

    # Summary Statistics
    summary = {
        "turn1": {
            "mean_recall": mean(r["turn1"]["recall"] for r in results),
            "hit_rate": mean(r["turn1"]["hit"] for r in results),
            "art_hit_rate": mean(r["turn1"]["art_hit"] for r in results),
            "mean_chunks": mean(r["turn1"]["chunks"] for r in results),
        },
        "turn2": {
            "mean_recall": mean(r["turn2"]["recall"] for r in results),
            "hit_rate": mean(r["turn2"]["hit"] for r in results),
            "art_hit_rate": mean(r["turn2"]["art_hit"] for r in results),
            "mean_chunks": mean(r["turn2"]["chunks"] for r in results),
        },
        "turn3": {
            "mean_recall": mean(r["turn3"]["recall"] for r in results),
            "hit_rate": mean(r["turn3"]["hit"] for r in results),
            "art_hit_rate": mean(r["turn3"]["art_hit"] for r in results),
            "mean_chunks": mean(r["turn3"]["chunks"] for r in results),
        },
        "combined": {
            "mean_recall": mean(r["combined"]["recall"] for r in results),
            "hit_rate": mean(r["combined"]["hit"] for r in results),
            "art_hit_rate": mean(r["combined"]["art_hit"] for r in results),
            "mean_chunks": mean(r["combined"]["chunks"] for r in results),
        },
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump({"summary": summary, "per_query": results}, f, ensure_ascii=False, indent=2)
    print(f"\nSaved results to {OUTPUT_FILE}", flush=True)

    # Display Report
    print("\n" + "=" * 105, flush=True)
    print(f"{'KẾT QUẢ ĐÁNH GIÁ AGENTIC V1 MULTI-TURN TRÊN 30 NEW QUERIES (17 DOCUMENTS)':^105}", flush=True)
    print("=" * 105, flush=True)
    print(
        f"{'Giai đoạn (Turn)':<25} | {'Chunk Recall':<14} | {'Chunk Hit Rate':<16} | {'Article Hit Rate':<18} | {'Avg Chunks':<12}",
        flush=True,
    )
    print("-" * 105, flush=True)

    stages = [
        ("Turn 1 (Single-Pass Top-5)", "turn1"),
        ("Turn 2 (Agentic Hop 1)", "turn2"),
        ("Turn 3 (Agentic Hop 2)", "turn3"),
        ("Turn 3 + Deterministic Exp", "combined"),
    ]

    for label, k in stages:
        rec = summary[k]["mean_recall"] * 100
        chit = summary[k]["hit_rate"] * 100
        ahit = summary[k]["art_hit_rate"] * 100
        c_cnt = summary[k]["mean_chunks"]
        print(f"{label:<25} | {rec:>12.1f}% | {chit:>14.1f}% | {ahit:>16.1f}% | {c_cnt:>10.1f}", flush=True)
    print("-" * 105, flush=True)


if __name__ == "__main__":
    main()
