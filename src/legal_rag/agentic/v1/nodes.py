"""Pure prompts, parsing, and deterministic node helpers for Agentic v1."""

from __future__ import annotations

import json
import re
from typing import Any, Callable

from ...generation.evidence import format_evidence
from ...generation.formatter import parse_model_output
from ...generation.prompts import build_prompt
from ...generation.verifier import CitationValidation, validate_citations
from ...retrieval.pipeline import DEFAULT_TOP_K, RetrievalPipeline
from ...retrieval.pipeline import Evidence
from ...llm_client import LLMClient
from .policies import MAX_SUB_QUERIES
from .state import CompletenessCheck, CoverageCheck

VALID_CITATION_TOKEN = re.compile(r"\[E([1-9][0-9]*)\]")
WORD_TOKEN = re.compile(r"[0-9]+|[a-zà-ỹđ]+", re.IGNORECASE)
ALIGNMENT_STOP_WORDS = {
    "và", "hoặc", "của", "là", "có", "được", "phải", "theo", "với", "cho",
    "trong", "khi", "này", "đó", "các", "những", "một", "về", "tại", "đối",
    "hệ", "thống", "trí", "tuệ", "nhân", "tạo", "ai",
}


def _json_object(raw: str) -> dict[str, Any]:
    """Parse a JSON object while tolerating an accidental markdown fence."""
    text = raw.strip()
    fenced = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", text, re.I | re.S)
    if fenced:
        text = fenced.group(1).strip()
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start < 0 or end <= start:
            raise ValueError("LLM response does not contain a JSON object")
        value = json.loads(text[start:end + 1])
    if not isinstance(value, dict):
        raise ValueError("LLM response must be a JSON object")
    return value


def _string_list(value: Any, field_name: str, limit: int | None = None) -> list[str]:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"{field_name} must be a string array")
    result = [item.strip() for item in value if item.strip()]
    return result[:limit] if limit is not None else result


def parse_coverage_response(raw: str) -> CoverageCheck:
    value = _json_object(raw)
    missing = _string_list(value.get("missing_aspects", []), "missing_aspects", MAX_SUB_QUERIES)
    if not isinstance(value.get("sufficient"), bool):
        raise ValueError("coverage.sufficient must be boolean")
    if not isinstance(value.get("reason", ""), str):
        raise ValueError("coverage.reason must be a string")
    if value["sufficient"] and missing:
        raise ValueError("coverage.missing_aspects must be empty when sufficient is true")
    return CoverageCheck(value["sufficient"], missing, str(value.get("reason", "")))


def parse_completeness_response(raw: str) -> CompletenessCheck:
    value = _json_object(raw)
    if not isinstance(value.get("complete"), bool):
        raise ValueError("completeness.complete must be boolean")
    if not isinstance(value.get("reason", ""), str):
        raise ValueError("completeness.reason must be a string")
    missing = _string_list(value.get("missing_points", []), "missing_points")
    if value["complete"] and missing:
        raise ValueError("completeness.missing_points must be empty when complete is true")
    return CompletenessCheck(value["complete"], missing, str(value.get("reason", "")))


LLMCall = Callable[[Any, str, str], str]
Transition = Callable[[Any, str], None]


def retrieve_evidence(
    state: Any, pipeline: RetrievalPipeline, query: str, round_number: int, *,
    sub_query: bool, all_candidates: bool, transition: Transition,
) -> list[Evidence]:
    transition(
        state,
        f"expansion_retrieval_{len(state.retrieval_calls)}"
        if sub_query else "initial_retrieval",
    )
    evidences, audit = pipeline.retrieve_with_audit(
        query, DEFAULT_TOP_K, all_candidates=all_candidates
    )
    state.retrieval_calls.append({
        "call_number": len(state.retrieval_calls) + 1,
        "round": round_number,
        "query": query,
        "sub_query": sub_query,
        **audit,
    })
    return evidences


def check_evidence_sufficiency(state: Any, llm_call: LLMCall) -> CoverageCheck:
    return parse_coverage_response(llm_call(
        state, "coverage_check", coverage_prompt(state.query, state.current_evidence)
    ))


def generate_answer_node(state: Any, llm_call: LLMCall) -> tuple[dict[str, Any], dict[str, Any]]:
    context, citation_map = format_evidence(state.current_evidence)
    parsed = parse_model_output(llm_call(
        state, "answer_generation", build_prompt(state.query, context)
    ))
    return parsed, citation_map


def check_answer_completeness(
    state: Any, answer: str | None, llm_call: LLMCall
) -> CompletenessCheck:
    return parse_completeness_response(llm_call(
        state, "completeness_check",
        completeness_prompt(state.query, answer or "", state.current_evidence),
    ))


def revise_answer_node(
    state: Any, answer: str, missing_points: list[str], llm_call: LLMCall
) -> dict[str, Any]:
    return parse_model_output(llm_call(
        state, "answer_revision",
        answer_revision_prompt(state.query, answer, missing_points, state.current_evidence),
    ))


def validate_answer_citations(
    answer: str, citation_map: dict[str, Any], used_evidence_ids: list[str]
) -> CitationValidation:
    return validate_citations(answer, citation_map, used_evidence_ids)


def revise_citations_node(
    state: Any, answer: str, errors: list[str], llm_call: LLMCall
) -> dict[str, Any]:
    return parse_model_output(llm_call(
        state, "citation_revision",
        citation_revision_prompt(answer, errors, state.current_evidence),
    ))


def coverage_prompt(query: str, evidences: list[Evidence]) -> str:
    context, _ = format_evidence(evidences)
    return f"""You are an evidence coverage evaluator for a legal RAG system.
Use only the original query and the supplied evidence. Do not use outside legal knowledge and do not write an answer.
Return only one JSON object with this exact shape:
{{"sufficient":true,"missing_aspects":[],"reason":"short reason"}}
Set sufficient=false when an aspect needed to answer the query is not present or cannot be established from the evidence. Each missing_aspect must describe information to retrieve, not a legal conclusion. Return at most {MAX_SUB_QUERIES} missing aspects.

ORIGINAL QUERY:
{query}

CURRENT EVIDENCE:
{context}
"""


def completeness_prompt(query: str, answer: str, evidences: list[Evidence]) -> str:
    context, _ = format_evidence(evidences)
    return f"""You are a strict legal answer completeness evaluator.
Use only the query, answer, and supplied evidence. Do not use gold labels or outside legal knowledge. Do not rewrite the answer.
Return only one JSON object with this exact shape:
{{"complete":true,"missing_points":[],"reason":"short reason"}}
Set complete=false when the answer omits a material aspect that the supplied evidence supports. missing_points must describe omitted answer content, not invent new law.

QUERY:
{query}

ANSWER:
{answer}

EVIDENCE:
{context}
"""


def answer_revision_prompt(query: str, answer: str, missing_points: list[str], evidences: list[Evidence]) -> str:
    context, _ = format_evidence(evidences)
    return f"""Revise a legal RAG answer using only the supplied evidence.
Return the same JSON schema as the baseline prompt: {{"answer":"...","used_evidence_ids":[],"insufficient_evidence":false,"missing_information":[]}}.
Address the missing points where the evidence supports them, preserve citations for existing claims, and do not invent unsupported legal claims. Cite important legal claims with the supplied [E#] identifiers.

ORIGINAL QUERY:
{query}

CURRENT ANSWER:
{answer}

MISSING POINTS:
{json.dumps(missing_points, ensure_ascii=False)}

EVIDENCE:
{context}
"""


def citation_revision_prompt(answer: str, errors: list[str], evidences: list[Evidence]) -> str:
    context, _ = format_evidence(evidences)
    return f"""Repair citations in this legal RAG answer.
Return only the baseline JSON schema: {{"answer":"...","used_evidence_ids":[],"insufficient_evidence":false,"missing_information":[]}}.
Keep substantive claims within the evidence. Fix only citation syntax, unknown IDs, or citation-to-evidence mismatches. Use only the supplied evidence IDs.

ANSWER:
{answer}

CITATION ERRORS:
{json.dumps(errors, ensure_ascii=False)}

EVIDENCE:
{context}
"""


def semantic_citation_prompt(
    answer: str,
    suspicious_claims: list[str],
    evidences: list[Evidence],
    *,
    allow_revision: bool,
) -> str:
    context, _ = format_evidence(evidences)
    revision_rule = (
        "If invalid, also return a corrected baseline answer JSON in revised_answer."
        if allow_revision else "Set revised_answer to null; revision is disabled."
    )
    return f"""You are a strict semantic citation alignment checker for a legal RAG answer.
Use only the answer and supplied evidence. Check whether each cited evidence actually supports the legal claim carrying that citation. Do not use outside legal knowledge. {revision_rule}
Return only one JSON object:
{{"valid":true,"errors":[],"reason":"short reason","revised_answer":null}}
If revising, revised_answer must use this schema:
{{"answer":"...","used_evidence_ids":[],"insufficient_evidence":false,"missing_information":[]}}
Preserve supported substantive claims. Remove or narrow unsupported claims and use only supplied evidence IDs.

ANSWER:
{answer}

CLAIMS REQUIRING SEMANTIC REVIEW:
{json.dumps(suspicious_claims, ensure_ascii=False)}

EVIDENCE:
{context}
"""


def claims_needing_semantic_alignment(
    answer: str, evidences: list[Evidence]
) -> list[str]:
    """Conservatively route low-overlap cited claims to semantic review.

    This is only a deterministic gate; it never decides legal support itself.
    The gate prevents an extra LLM call for citations whose claim/evidence
    relationship is lexically clear while escalating ambiguous paraphrases.
    """
    evidence_by_id = {item.evidence_id: item for item in evidences}
    units = [part.strip() for part in re.split(r"\n+|(?<=[.!?])\s+", answer) if part.strip()]
    suspicious: list[str] = []
    for unit in units:
        cited_ids = [f"E{number}" for number in VALID_CITATION_TOKEN.findall(unit)]
        if not cited_ids:
            continue
        claim_text = VALID_CITATION_TOKEN.sub("", unit)
        claim_tokens = {
            token.lower() for token in WORD_TOKEN.findall(claim_text)
            if token.lower() not in ALIGNMENT_STOP_WORDS
        }
        evidence_tokens: set[str] = set()
        for evidence_id in cited_ids:
            item = evidence_by_id.get(evidence_id)
            if item is not None:
                evidence_tokens.update(
                    token.lower() for token in WORD_TOKEN.findall(item.text)
                    if token.lower() not in ALIGNMENT_STOP_WORDS
                )
        overlap = len(claim_tokens.intersection(evidence_tokens))
        required_overlap = 1 if len(claim_tokens) <= 5 else 2
        if not claim_tokens or overlap < required_overlap:
            suspicious.append(unit)
    return suspicious
