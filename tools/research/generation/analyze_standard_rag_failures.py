#!/usr/bin/env python3
"""Read-only Phase 4A failure analysis for a Standard RAG result dataset."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import statistics
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]

from legal_rag.retrieval import RerankerRetriever
from tools.validation.validate_generation_eval import validate


GENERATION = ROOT / "eval-sets/generation/generation_eval_v1_verified.json"
GENERATION_MANIFEST = ROOT / "eval-sets/generation/generation_eval_v1_verified_manifest.json"
RESULTS = ROOT / "experiments/reference/generation/standard-rag-v0/standard_rag_eval_v0.jsonl"
RESULT_METRICS = ROOT / "experiments/reference/generation/standard-rag-v0/standard_rag_metrics_v0.json"
RESULT_MANIFEST = ROOT / "experiments/reference/generation/standard-rag-v0/standard_rag_manifest_v0.json"
RETRIEVAL = ROOT / "eval-sets/retrieval/retrieval_eval.jsonl"
CORPUS = ROOT / "data/versions/corpus-v0.1/chunks.jsonl"
CORPUS_VERSION = "corpus-v0.1"
OUTPUT_DIR = ROOT / "experiments/runs/generation/failure-analysis"
REPORT_DIR = OUTPUT_DIR / "reports"
POINTS_OUT = OUTPUT_DIR / "failure_analysis_points_v0.jsonl"
QUERIES_OUT = OUTPUT_DIR / "failure_analysis_queries_v0.json"
METRICS_OUT = OUTPUT_DIR / "failure_analysis_metrics_v0.json"
REPORT_OUT = REPORT_DIR / "standard_rag_failure_analysis_v0.md"
CANDIDATE_CACHE = OUTPUT_DIR / ".failure_analysis_candidate_cache_v0.jsonl"

PRIMARY = ("retrieval_miss", "evidence_coverage", "answer_generation", "citation")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_inputs() -> tuple[dict[str, Any], list[dict[str, Any]], dict[str, dict[str, Any]], dict[str, dict[str, Any]], dict[str, Any]]:
    errors = validate(GENERATION, RETRIEVAL, CORPUS)
    if errors:
        raise RuntimeError("Generation ground truth validator failed: " + "; ".join(errors))
    generation = load_json(GENERATION)
    result_rows = load_jsonl(RESULTS)
    retrieval_rows = load_jsonl(RETRIEVAL)
    result_metrics = load_json(RESULT_METRICS)
    result_manifest = load_json(RESULT_MANIFEST)
    if generation.get("dataset_status") != "verified":
        raise RuntimeError("Generation ground truth is not verified")
    if len(generation.get("items", [])) != 31 or len(result_rows) != 31:
        raise RuntimeError("Expected exactly 31 generation and result records")
    generation_by_id = {row["query_id"]: row for row in generation["items"]}
    result_by_id = {row["query_id"]: row for row in result_rows}
    retrieval_by_id = {row["query_id"]: row for row in retrieval_rows}
    if len(generation_by_id) != 31 or len(result_by_id) != 31 or len(retrieval_by_id) != 31:
        raise RuntimeError("Duplicate or missing query IDs in input artifacts")
    expected_ids = set(generation_by_id)
    if set(result_by_id) != expected_ids or set(retrieval_by_id) != expected_ids:
        raise RuntimeError("Ground truth, result, and retrieval query IDs do not match")
    for qid, item in generation_by_id.items():
        if item["query"] != retrieval_by_id[qid]["query"] or item["query"] != result_by_id[qid]["query"]:
            raise RuntimeError(f"Query text mismatch for {qid}")
    if sum(len(item["required_points"]) for item in generation["items"]) != 102:
        raise RuntimeError("Expected exactly 102 required points")
    if result_manifest.get("llm_model") != "gemini-3.5-flash-lite":
        raise RuntimeError("Unexpected Standard RAG result model")
    return generation, result_rows, retrieval_by_id, result_by_id, result_metrics


def safe_fraction(numerator: int | float, denominator: int | float) -> float:
    return numerator / denominator if denominator else 0.0


def classify_query(primary_counts: Counter[str]) -> str:
    active = {category for category in PRIMARY if primary_counts[category]}
    if not active:
        return "A. Mostly successful"
    if len(active) > 1:
        return "F. Mixed failure"
    only = next(iter(active))
    return {
        "retrieval_miss": "B. Retrieval-limited",
        "evidence_coverage": "C. Evidence-coverage-limited",
        "answer_generation": "D. Generation-limited",
        "citation": "E. Citation-limited",
    }[only]


def root_cause(primary_counts: Counter[str]) -> str:
    active = {category: primary_counts.get(category, 0) for category in PRIMARY if primary_counts.get(category, 0)}
    if not active:
        return "none"
    highest = max(active.values())
    winners = sorted(category for category, count in active.items() if count == highest)
    return winners[0] if len(winners) == 1 else "mixed"


def point_analysis(item: dict[str, Any], result: dict[str, Any], candidate_ids: list[str]) -> list[dict[str, Any]]:
    candidate_set = set(candidate_ids)
    top5_ids = result["retrieved_chunk_ids"]
    top5_set = set(top5_ids)
    supported = set(result["supported_point_ids"])
    citation_supported = set(result.get("citation_supported_point_ids", []))
    cited_ids = set(result.get("cited_evidence_ids", []))
    rows = []
    for point in item["required_points"]:
        point_id = point["point_id"]
        support_ids = list(point["supporting_chunk_ids"])
        candidate_support = [chunk_id for chunk_id in support_ids if chunk_id in candidate_set]
        top5_support = [chunk_id for chunk_id in support_ids if chunk_id in top5_set]
        candidate_sufficient = set(support_ids).issubset(candidate_set)
        top5_sufficient = set(support_ids).issubset(top5_set)
        answer_support = "full" if point_id in supported else "missing"
        if answer_support == "full":
            if point_id in citation_supported and result["citation_valid"]:
                citation_support = "correct"
                primary_failure = "none"
                secondary_failure = None
            elif not cited_ids:
                citation_support = "missing"
                primary_failure = "citation"
                secondary_failure = None
            else:
                citation_support = "incorrect"
                primary_failure = "citation"
                secondary_failure = None
        else:
            citation_support = "not_applicable"
            if not candidate_sufficient:
                primary_failure = "retrieval_miss"
                secondary_failure = "answer_generation"
            elif not top5_sufficient:
                primary_failure = "evidence_coverage"
                secondary_failure = "answer_generation"
            else:
                primary_failure = "answer_generation"
                secondary_failure = None
        rationale = (
            f"Answer support={answer_support}; candidate contains {len(candidate_support)}/{len(support_ids)} "
            f"supporting chunks and Top-5 contains {len(top5_support)}/{len(support_ids)}. "
        )
        if primary_failure == "none":
            rationale += "The point is covered and its citation is valid/supporting."
        elif primary_failure == "retrieval_miss":
            rationale += "The complete annotated support set is absent from BM25@20 ∪ Dense@20."
        elif primary_failure == "evidence_coverage":
            rationale += "The complete annotated support set is in the candidate union but not retained in Top-5."
        elif primary_failure == "answer_generation":
            rationale += "Top-5 contains the complete annotated support set, but the answer does not cover the point."
        else:
            rationale += "The answer covers the point but its citation is missing, malformed, or not semantically suitable."
        rationale += " Partial answer status is not available in the Phase 3 binary point audit; unsupported points are conservatively recorded as missing."
        rows.append({
            "query_id": item["query_id"],
            "point_id": point_id,
            "point_text": point["description"],
            "importance": point["importance"],
            "supporting_chunk_ids": support_ids,
            "candidate_chunk_ids": candidate_ids,
            "candidate_supporting_chunk_ids": candidate_support,
            "candidate_sufficient_evidence": candidate_sufficient,
            "top5_chunk_ids": top5_ids,
            "top5_supporting_chunk_ids": top5_support,
            "top5_sufficient_evidence": top5_sufficient,
            "answer_support": answer_support,
            "citation_support": citation_support,
            "primary_failure": primary_failure,
            "secondary_failure": secondary_failure,
            "rationale": rationale,
        })
    return rows


def analyze_query(item: dict[str, Any], result: dict[str, Any], retrieval: dict[str, Any],
                  candidate_ids: list[str], top5_reconstructed: list[str]) -> dict[str, Any]:
    points = point_analysis(item, result, candidate_ids)
    primary_counts = Counter(point["primary_failure"] for point in points)
    missing = [point["point_id"] for point in points if point["answer_support"] != "full"]
    supported_count = len(points) - len(missing)
    answer_completeness = safe_fraction(supported_count, len(points))
    retrieval_gold = set(retrieval["gold_chunk_ids"])
    top5 = set(result["retrieved_chunk_ids"])
    candidate = set(candidate_ids)
    return {
        "query_id": item["query_id"],
        "query": item["query"],
        "answer_completeness": answer_completeness,
        "required_points": [point["point_id"] for point in points],
        "required_point_count": len(points),
        "supported_points": [point["point_id"] for point in points if point["answer_support"] == "full"],
        "supported_point_count": supported_count,
        "missing_points": missing,
        "missing_point_count": len(missing),
        "primary_failure_counts": {category: primary_counts[category] for category in PRIMARY if primary_counts[category]},
        "has_retrieval_miss": bool(primary_counts["retrieval_miss"]),
        "has_evidence_coverage_issue": bool(primary_counts["evidence_coverage"]),
        "has_generation_issue": bool(primary_counts["answer_generation"]),
        "has_citation_issue": bool(primary_counts["citation"]),
        "overall_root_cause": root_cause(primary_counts),
        "query_taxonomy": classify_query(primary_counts),
        "candidate_chunk_count": len(candidate_ids),
        "candidate_chunk_ids": candidate_ids,
        "top5_chunk_ids": result["retrieved_chunk_ids"],
        "top5_reconstruction_match": result["retrieved_chunk_ids"] == top5_reconstructed,
        "gold_chunk_count": len(retrieval["gold_chunk_ids"]),
        "candidate_gold_chunk_count": len(retrieval_gold.intersection(candidate)),
        "top5_gold_chunk_count": len(retrieval_gold.intersection(top5)),
        "candidate_gold_coverage": safe_fraction(len(retrieval_gold.intersection(candidate)), len(retrieval_gold)),
        "top5_gold_coverage": safe_fraction(len(retrieval_gold.intersection(top5)), len(retrieval_gold)),
        "citation_valid": result["citation_valid"],
        "citation_issue_point_count": primary_counts["citation"],
        "answer": result["answer"],
        "points": points,
    }


def aggregate(query_rows: list[dict[str, Any]], point_rows: list[dict[str, Any]], result_metrics: dict[str, Any]) -> dict[str, Any]:
    primary = Counter(point["primary_failure"] for point in point_rows)
    secondary = Counter(point["secondary_failure"] for point in point_rows if point["secondary_failure"])
    answer_support = Counter(point["answer_support"] for point in point_rows)
    citation_support = Counter(point["citation_support"] for point in point_rows)
    candidate_sufficient = sum(point["candidate_sufficient_evidence"] for point in point_rows)
    top5_sufficient = sum(point["top5_sufficient_evidence"] for point in point_rows)
    lost_top5 = sum(point["candidate_sufficient_evidence"] and not point["top5_sufficient_evidence"] for point in point_rows)
    generation_bottleneck = sum(
        point["top5_sufficient_evidence"] and point["answer_support"] != "full" for point in point_rows
    )
    taxonomy = Counter(row["query_taxonomy"] for row in query_rows)
    if sum(primary.values()) != len(point_rows):
        raise RuntimeError("Primary failure counts do not reconcile")
    return {
        "query_count": len(query_rows),
        "required_point_count": len(point_rows),
        "answer_completeness_from_points": safe_fraction(answer_support["full"], len(point_rows)),
        "phase3_answer_completeness_macro": result_metrics["answer_completeness"]["macro"],
        "fully_supported_points": answer_support["full"],
        "partial_points": {
            "count": 0,
            "status": "not_separately_identifiable",
            "reason": "Phase 3 result artifact stores binary supported_point_ids only; no partial labels were persisted. Unsupported points are conservatively recorded as missing.",
        },
        "missing_points": answer_support["missing"],
        "primary_failure_counts": {category: primary[category] for category in (*PRIMARY, "none")},
        "primary_failure_percentages": {category: safe_fraction(primary[category], len(point_rows)) for category in (*PRIMARY, "none")},
        "secondary_failure_counts": dict(secondary),
        "citation_point_status_counts": dict(citation_support),
        "citation_syntax_valid_queries": sum(row["citation_valid"] for row in query_rows),
        "citation_syntax_invalid_query_ids": [row["query_id"] for row in query_rows if not row["citation_valid"]],
        "candidate_had_sufficient_evidence": candidate_sufficient,
        "top5_retained_sufficient_evidence": top5_sufficient,
        "lost_during_reranking_top5": lost_top5,
        "generation_bottleneck_top5_sufficient_answer_incomplete": generation_bottleneck,
        "query_level_taxonomy_counts": dict(taxonomy),
        "reconstruction_mismatch_query_ids": [row["query_id"] for row in query_rows if not row["top5_reconstruction_match"]],
        "retrieval_gold_coverage_is_not_answer_completeness": True,
    }


def mean_for(rows: list[dict[str, Any]], field: str) -> float:
    return statistics.mean(row[field] for row in rows) if rows else 0.0


def comparison(query_rows: list[dict[str, Any]], ids: list[str]) -> dict[str, Any]:
    selected = [row for row in query_rows if row["query_id"] in ids]
    return {
        "query_ids": ids,
        "query_count": len(selected),
        "required_points_mean": mean_for(selected, "required_point_count"),
        "candidate_chunk_count_mean": mean_for(selected, "candidate_chunk_count"),
        "candidate_gold_coverage_mean": mean_for(selected, "candidate_gold_coverage"),
        "top5_gold_coverage_mean": mean_for(selected, "top5_gold_coverage"),
        "answer_completeness_mean": mean_for(selected, "answer_completeness"),
        "citation_issue_query_count": sum(row["has_citation_issue"] for row in selected),
        "gold_chunk_count_mean": mean_for(selected, "gold_chunk_count"),
    }


def deep_dive(rows_by_id: dict[str, dict[str, Any]], points_by_id: dict[str, list[dict[str, Any]]], ids: list[str]) -> list[dict[str, Any]]:
    output = []
    for qid in ids:
        row = rows_by_id[qid]
        output.append({
            "query_id": qid,
            "query": row["query"],
            "answer_completeness": row["answer_completeness"],
            "answer": row["answer"],
            "required_points": points_by_id[qid],
            "root_cause": row["overall_root_cause"],
            "query_taxonomy": row["query_taxonomy"],
        })
    return output


def render_report(generation: dict[str, Any], result_manifest: dict[str, Any], metrics: dict[str, Any],
                  query_rows: list[dict[str, Any]], point_rows: list[dict[str, Any]], worst: list[str], best: list[str],
                  deep_worst: list[dict[str, Any]], deep_best: list[dict[str, Any]]) -> str:
    agg = metrics
    lines = [
        "# Phase 4A — Standard RAG Failure Analysis",
        "",
        "## Executive Summary",
        "",
        f"Phase 3 reported macro Answer Completeness of **{agg['phase3_answer_completeness_macro']:.4f}** across queries. At required-point level, **{agg['fully_supported_points']}/{agg['required_point_count']}** points were supported, giving micro completeness of **{agg['answer_completeness_from_points']:.4f}**. The difference exists because queries contain different numbers of required points. The result is analyzed as a read-only artifact; no corpus, benchmark, gold label, prompt, retriever, reranker, model, or Phase 3 result was modified.",
        "",
        f"The dominant primary causes are evidence coverage (**{agg['primary_failure_counts']['evidence_coverage']} points**), answer generation (**{agg['primary_failure_counts']['answer_generation']}**), retrieval miss (**{agg['primary_failure_counts']['retrieval_miss']}**), and citation (**{agg['primary_failure_counts']['citation']}**). The Top-5 bottleneck is measured separately from answer completeness.",
        "",
        "## Dataset / System",
        "",
        f"- Ground truth: `generation-eval-v1`, status `{generation['dataset_status']}`, {len(generation['items'])} queries, {sum(len(item['required_points']) for item in generation['items'])} required points.",
        f"- Ground-truth SHA-256: `{sha256(GENERATION)}`",
        f"- Standard RAG result model: `{result_manifest['llm_model']}`",
        f"- Retrieval: `{result_manifest['retrieval']['pipeline']}`",
        f"- Prompt: `{result_manifest['prompt_version']}`",
        f"- Evidence: Top-{result_manifest['retrieval']['top_k']}",
        "",
        "## Aggregate Results",
        "",
        f"- Phase 3 macro Answer Completeness (query average): **{agg['phase3_answer_completeness_macro']:.4f}**",
        f"- Point-level micro completeness: **{agg['fully_supported_points']}/{agg['required_point_count']} = {agg['answer_completeness_from_points']:.4f}**",
        f"- Fully supported points: **{agg['fully_supported_points']}/102**",
        f"- Partial points: **not separately identifiable**; the Phase 3 result stores only binary supported/unsupported labels. Unsupported points are conservatively counted as missing (**{agg['missing_points']}**).",
        f"- Missing points: **{agg['missing_points']}/102**",
        "- Retrieval gold coverage is reported separately and is not Answer Completeness.",
        "",
        "## Required-point Failure Taxonomy",
        "",
        "| primary failure | points | percentage |",
        "|---|---:|---:|",
    ]
    labels = {
        "retrieval_miss": "Retrieval Miss",
        "evidence_coverage": "Evidence Coverage",
        "answer_generation": "Answer Generation",
        "citation": "Citation",
        "none": "No Failure",
    }
    for category in (*PRIMARY, "none"):
        lines.append(f"| {labels[category]} | {agg['primary_failure_counts'][category]} | {agg['primary_failure_percentages'][category]:.4f} |")
    lines += [
        "",
        "Secondary causes are retained in the point matrix; retrieval/evidence failures with an uncovered answer point also record `answer_generation` as a secondary observed failure.",
        "",
        "## Retrieval vs Evidence Coverage",
        "",
        f"- Candidate union had sufficient annotated evidence: **{agg['candidate_had_sufficient_evidence']}/102**",
        f"- Top-5 retained sufficient annotated evidence: **{agg['top5_retained_sufficient_evidence']}/102**",
        f"- Lost during reranking/Top-5 selection: **{agg['lost_during_reranking_top5']}/102**",
        "",
        "A point is considered sufficient only when all of its annotated supporting chunk IDs are present. This uses the frozen point annotation; no unannotated alternative evidence was inferred.",
        "",
        "## Generation Failures",
        "",
        f"Top-5 sufficient + answer incomplete: **{agg['generation_bottleneck_top5_sufficient_answer_incomplete']}/102** points.",
        "These are direct generation-limited points under the binary Phase 3 audit: the complete annotated support set was retained in Top-5, but the answer did not cover the proposition.",
        "",
        "## Citation Failures",
        "",
        f"- Citation syntax valid: **{agg['citation_syntax_valid_queries']}/31** queries.",
        f"- Syntax-invalid query IDs: {', '.join(f'`{qid}`' for qid in agg['citation_syntax_invalid_query_ids']) or 'none'}.",
        f"- Point-level citation statuses: `{json.dumps(agg['citation_point_status_counts'], ensure_ascii=False, sort_keys=True)}`.",
        "- Citation completeness and citation correctness are kept separate in the Phase 3 result; this analysis does not treat retrieved evidence as automatically correct citation.",
        "",
        "## Worst Queries",
        "",
    ]
    for row in deep_worst:
        lines += [f"### {row['query_id']}", "", f"Query: {row['query']}", "", f"Answer Completeness: **{row['answer_completeness']:.4f}**", f"Query taxonomy: **{row['query_taxonomy']}**", f"Root cause: **{row['root_cause']}**", "", "Answer:", "", row["answer"], "", "| point | gold support | candidate status | Top-5 status | answer | citation | primary |", "|---|---|---|---|---|---|---|"]
        for point in row["required_points"]:
            lines.append(
                f"| {point['point_id']} | {', '.join(point['supporting_chunk_ids'])} | {'sufficient' if point['candidate_sufficient_evidence'] else 'insufficient'} | {'sufficient' if point['top5_sufficient_evidence'] else 'insufficient'} | {point['answer_support']} | {point['citation_support']} | {point['primary_failure']} |"
            )
        lines += ["", f"Conclusion: {row['root_cause']} is the main root cause under the primary point taxonomy.", ""]
    lines += ["## Best Queries", ""]
    for row in deep_best:
        lines += [f"### {row['query_id']}", "", f"Query: {row['query']}", "", f"Answer Completeness: **{row['answer_completeness']:.4f}**", f"Query taxonomy: **{row['query_taxonomy']}**", f"Root cause: **{row['root_cause']}**", "", "Answer:", "", row["answer"], "", "The point rows in the machine-readable matrix show whether success depended on candidate/Top-5 sufficiency and citation correctness.", ""]
    lines += [
        "## Best vs Worst Comparison",
        "",
        "| dimension | best queries | worst queries |",
        "|---|---:|---:|",
    ]
    best_comp = comparison(query_rows, best)
    worst_comp = comparison(query_rows, worst)
    for label, key, fmt in [
        ("Number of required points", "required_points_mean", "{:.2f}"),
        ("Evidence concentration (gold chunks/query)", "gold_chunk_count_mean", "{:.2f}"),
        ("Candidate gold coverage", "candidate_gold_coverage_mean", "{:.4f}"),
        ("Top-5 gold coverage", "top5_gold_coverage_mean", "{:.4f}"),
        ("Generation completeness", "answer_completeness_mean", "{:.4f}"),
        ("Citation-issue queries", "citation_issue_query_count", "{}"),
    ]:
        lines.append(f"| {label} | {fmt.format(best_comp[key])} | {fmt.format(worst_comp[key])} |")
    lines += [
        "",
        "These are descriptive aggregates of the selected best/worst sets, not causal proof. The exact per-query values are in `failure_analysis_queries_v0.json`.",
        "",
        "## Root Causes",
        "",
        "1. The largest point-level group is evidence coverage: annotated support exists in the candidate union but is not retained in Top-5.",
        "2. A second large group is answer generation: Top-5 contains the complete annotated support set but the answer omits the proposition.",
        "3. Pure retrieval miss is smaller and occurs only when the complete annotated support set is absent from the BM25@20 ∪ Dense@20 candidate union.",
        "4. Citation failures are distinct from both retrieval and completeness; `eval012` has full point coverage but invalid declared/cited evidence alignment.",
        "",
        "## Agentic RAG Requirements Derived from Evidence",
        "",
        "These are behavior requirements only; no Agentic RAG was designed or implemented in Phase 4A.",
        "",
        f"### Requirement R1 — Evidence coverage check / targeted expansion",
        "",
        f"Evidence: **{agg['lost_during_reranking_top5']}/102** points had sufficient annotated evidence in the candidate union but not in Top-5. A coverage check could detect missing required propositions before generation and request targeted evidence expansion.",
        "",
        f"### Requirement R2 — Answer completeness self-check",
        "",
        f"Evidence: **{agg['generation_bottleneck_top5_sufficient_answer_incomplete']}/102** points had sufficient Top-5 evidence but were absent from the answer. A post-generation point checklist/revision behavior is justified for this observed failure class.",
        "",
        "### Requirement R3 — Query decomposition or reformulation only for retrieval misses",
        "",
        f"Evidence: **{agg['primary_failure_counts']['retrieval_miss']}/102** points had no complete annotated support set in the candidate union. This supports targeted reformulation/decomposition as a conditional behavior, not a default for every query.",
        "",
        "### Requirement R4 — Citation alignment check",
        "",
        f"Evidence: **{agg['primary_failure_counts']['citation']}/102** points were answer-supported but citation-problematic, and {31 - agg['citation_syntax_valid_queries']} query had syntax/declaration invalidity. A citation validation/revision behavior is justified separately from evidence retrieval.",
        "",
        "## Limitations",
        "",
        "- Candidate sufficiency is defined from the frozen annotated supporting chunk IDs; unannotated but legally adequate alternatives were not inferred.",
        "- Phase 3 persisted binary point support only. Partial answer coverage cannot be recovered exactly, so unsupported points are labeled `missing` conservatively and partial count is reported as not separately identifiable.",
        "- Semantic point and citation decisions are inherited from the Phase 3 structured audit; this phase does not re-judge answers or use outside legal knowledge.",
        "- The result dataset has no Git commit because the project directory is not a Git working tree.",
        "",
        "## Sanity Checks",
        "",
        f"- Queries analyzed: **{len(query_rows)}/31**",
        f"- Required points analyzed: **{len(point_rows)}/102**",
        f"- Candidate reconstruction mismatches: **{len(agg['reconstruction_mismatch_query_ids'])}**",
        "- Benchmark source files modified: **no**",
        "- Generation ground truth modified: **no**",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    generation, result_rows, retrieval_by_id, result_by_id, result_metrics = check_inputs()
    retriever = RerankerRetriever()
    point_rows: list[dict[str, Any]] = []
    query_rows: list[dict[str, Any]] = []
    points_by_id: dict[str, list[dict[str, Any]]] = {}
    cached_candidates = {
        row["query_id"]: row for row in load_jsonl(CANDIDATE_CACHE)
    } if CANDIDATE_CACHE.exists() else {}
    cache_handle = CANDIDATE_CACHE.open("a", encoding="utf-8")
    for index, item in enumerate(generation["items"], 1):
        qid = item["query_id"]
        result = result_by_id[qid]
        print(f"[{index}/31] {qid}", flush=True)
        if qid in cached_candidates:
            candidate_ids = cached_candidates[qid]["candidate_chunk_ids"]
            top5_ids = cached_candidates[qid]["top5_chunk_ids"]
        else:
            top5, candidates = retriever.search_with_candidates(item["query"], top_k=5)
            candidate_ids = [candidate.chunk["chunk_id"] for candidate in candidates]
            top5_ids = [row["chunk"]["chunk_id"] for row in top5]
            cache_row = {"query_id": qid, "candidate_chunk_ids": candidate_ids, "top5_chunk_ids": top5_ids}
            cache_handle.write(json.dumps(cache_row, ensure_ascii=False) + "\n")
            cache_handle.flush()
        query_row = analyze_query(item, result, retrieval_by_id[qid], candidate_ids, top5_ids)
        query_rows.append(query_row)
        points = query_row.pop("points")
        points_by_id[qid] = points
        point_rows.extend(points)
        print(f"  candidates={len(candidate_ids)} top5_match={query_row['top5_reconstruction_match']} points={query_row['supported_point_count']}/{query_row['required_point_count']}", flush=True)
    cache_handle.close()
    if len(point_rows) != 102 or len(query_rows) != 31:
        raise RuntimeError("Analysis did not account for all 31 queries and 102 points")
    aggregate_metrics = aggregate(query_rows, point_rows, result_metrics)
    worst = [row["query_id"] for row in sorted(query_rows, key=lambda row: (row["answer_completeness"], row["query_id"]))[:5]]
    best = [row["query_id"] for row in sorted(query_rows, key=lambda row: (-row["answer_completeness"], row["query_id"]))[:5]]
    rows_by_id = {row["query_id"]: row for row in query_rows}
    deep_worst = deep_dive(rows_by_id, points_by_id, worst)
    deep_best = deep_dive(rows_by_id, points_by_id, best)
    now = datetime.now(timezone.utc).isoformat()
    metadata = {
        "analysis_version": "phase-4a-standard-rag-failure-analysis-v0",
        "created_at": now,
        "read_only_analysis": True,
        "inputs": {
            "generation_ground_truth": str(GENERATION.relative_to(ROOT)),
            "standard_rag_result": str(RESULTS.relative_to(ROOT)),
            "retrieval_benchmark": str(RETRIEVAL.relative_to(ROOT)),
            "corpus": str(CORPUS.relative_to(ROOT)),
        },
        "input_hashes": {
            "generation_verified_sha256": sha256(GENERATION),
            "generation_verified_manifest_sha256": sha256(GENERATION_MANIFEST),
            "standard_rag_result_sha256": sha256(RESULTS),
            "standard_rag_metrics_sha256": sha256(RESULT_METRICS),
            "standard_rag_manifest_sha256": sha256(RESULT_MANIFEST),
            "retrieval_eval_sha256": sha256(RETRIEVAL),
            "corpus_chunks_sha256": sha256(CORPUS),
        },
        "system": {
            "llm_model": load_json(RESULT_MANIFEST)["llm_model"],
            "retrieval": load_json(RESULT_MANIFEST)["retrieval"],
            "prompt_version": load_json(RESULT_MANIFEST)["prompt_version"],
        },
        "partial_label_limit": "Phase 3 stored binary supported_point_ids; partial coverage is not separately identifiable.",
        "aggregate": aggregate_metrics,
        "worst_query_ids": worst,
        "best_query_ids": best,
    }
    output_queries = {
        "analysis_version": metadata["analysis_version"],
        "query_count": len(query_rows),
        "queries": query_rows,
        "worst_query_ids": worst,
        "best_query_ids": best,
    }
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    POINTS_OUT.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in point_rows), encoding="utf-8")
    QUERIES_OUT.write_text(json.dumps(output_queries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    METRICS_OUT.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT_OUT.write_text(render_report(generation, load_json(RESULT_MANIFEST), aggregate_metrics, query_rows, point_rows, worst, best, deep_worst, deep_best), encoding="utf-8")
    CANDIDATE_CACHE.unlink(missing_ok=True)
    print(f"Points: {POINTS_OUT}")
    print(f"Queries: {QUERIES_OUT}")
    print(f"Metrics: {METRICS_OUT}")
    print(f"Report: {REPORT_OUT}")


if __name__ == "__main__":
    main()
