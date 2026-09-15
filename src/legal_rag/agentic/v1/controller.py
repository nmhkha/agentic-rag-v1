"""Canonical finite-state controller for frozen Agentic RAG v1."""

from __future__ import annotations

import json
import uuid
from dataclasses import replace

from ...generation.evidence import format_evidence
from ...generation.formatter import parse_model_output
from ...generation.prompts import build_prompt
from ...generation.verifier import validate_citations
from ...llm_client import LLMClient
from ...retrieval.pipeline import DEFAULT_TOP_K, Evidence, RetrievalPipeline
from .nodes import (
    _json_object, _string_list, answer_revision_prompt, citation_revision_prompt,
    check_answer_completeness, check_evidence_sufficiency,
    claims_needing_semantic_alignment, generate_answer_node,
    retrieve_evidence, revise_answer_node, revise_citations_node,
    semantic_citation_prompt, validate_answer_citations,
)
from .policies import (
    MAX_ANSWER_REVISIONS, MAX_CITATION_REVISIONS, MAX_LLM_CALLS,
    MAX_SUB_QUERIES, AgenticConfig, answer_revision_allowed,
    citation_revision_allowed, determine_final_status, expansion_allowed,
    llm_call_allowed,
)
from .state import AgentState, CitationCheck, CompletenessCheck


class AgenticRAGController:
    """Finite-state controller for Agentic RAG v1."""

    def __init__(
        self,
        pipeline: RetrievalPipeline,
        client: LLMClient,
        *,
        enable_expansion: bool = True,
        enable_answer_revision: bool = True,
        enable_citation_revision: bool = True,
    ) -> None:
        self.pipeline = pipeline
        self.client = client
        self.enable_expansion = enable_expansion
        self.enable_answer_revision = enable_answer_revision
        self.enable_citation_revision = enable_citation_revision

    @staticmethod
    def _transition(state: AgentState, stage: str) -> None:
        if not state.transitions or state.transitions[-1] != stage:
            state.transitions.append(stage)

    def _llm(self, state: AgentState, stage: str, prompt: str) -> str:
        if len(state.llm_calls) >= MAX_LLM_CALLS:
            raise RuntimeError(f"LLM call budget exceeded ({MAX_LLM_CALLS})")
        self._transition(state, stage)
        call_number = len(state.llm_calls) + 1
        state.llm_calls.append({"call_number": call_number, "stage": stage})
        return self.client.generate(prompt)

    def _retrieve(self, state: AgentState, query: str, round_number: int,
                  *, sub_query: bool, all_candidates: bool = False) -> list[Evidence]:
        return retrieve_evidence(
            state, self.pipeline, query, round_number, sub_query=sub_query,
            all_candidates=all_candidates, transition=self._transition,
        )

    def run(
        self,
        query: str,
        *,
        run_id: str | None = None,
        state: AgentState | None = None,
    ) -> AgentState:
        if not query or not query.strip():
            raise ValueError("query must not be empty")
        normalized_query = query.strip()
        if state is None:
            state = AgentState(query=normalized_query, run_id=run_id or uuid.uuid4().hex)
        elif state.query != normalized_query:
            raise ValueError("provided state query does not match query")
        elif run_id is not None and state.run_id != run_id:
            raise ValueError("provided state run_id does not match run_id")
        elif (state.retrieval_calls or state.llm_calls
              or state.final_status != "not_started"):
            raise ValueError("provided state must be fresh")

        state.retrieval_round = 0
        # Ask the frozen reranker for the complete BM25@20 ∪ Dense@20 pool so
        # the trace contains all candidate and reranker ranks; only the final
        # Top-5 enters the LLM context.
        initial = self._retrieve(state, state.query, 0, sub_query=False,
                                 all_candidates=True)
        state.initial_evidence = initial[:DEFAULT_TOP_K]
        state.current_evidence = list(state.initial_evidence)
        state.initial_top5 = [item.chunk_id for item in state.initial_evidence]

        coverage = check_evidence_sufficiency(state, self._llm)
        state.coverage_check = coverage
        state.missing_aspects = list(coverage.missing_aspects)

        if expansion_allowed(self.enable_expansion, state.coverage_check.sufficient,
                             state.missing_aspects):
            state.retrieval_round = 1
            state.expansion_used = True
            # Missing aspects are already targeted retrieval intents from the
            # structured controller decision. Adding the original query gives
            # the frozen retrievers useful legal context without another LLM call.
            state.sub_queries = [f"{aspect} {state.query}" for aspect in state.missing_aspects]
            raw_expanded: list[Evidence] = []
            for sub_query in state.sub_queries[:MAX_SUB_QUERIES]:
                raw_expanded.extend(self._retrieve(
                    state, sub_query, 1, sub_query=True, all_candidates=True
                ))
            unique_expanded: dict[str, Evidence] = {}
            for item in raw_expanded:
                unique_expanded.setdefault(item.chunk_id, item)
            # Retrieval calls use local ranks, but state-level IDs are assigned
            # once after cross-query deduplication and remain deterministic.
            expanded = [
                replace(item, evidence_id=f"E{len(state.initial_evidence) + index}")
                for index, item in enumerate(unique_expanded.values(), 1)
            ]
            state.expansion_evidence = expanded
            state.expanded_candidates = list(dict.fromkeys(item.chunk_id for item in expanded))
            pool = state.initial_evidence + expanded
            self._transition(state, "evidence_merge_rerank")
            state.current_evidence = self.pipeline.rerank_evidence_pool(
                state.query, pool, DEFAULT_TOP_K
            )
        else:
            state.sub_queries = []
            state.expanded_candidates = []
            state.current_evidence = list(state.initial_evidence)
        state.final_top5 = [item.chunk_id for item in state.current_evidence]

        draft, citation_map = generate_answer_node(state, self._llm)
        state.draft_answer = draft["answer"]
        state.final_answer = draft["answer"]
        answer_declares_insufficient = draft["insufficient_evidence"]
        used_evidence_ids = draft["used_evidence_ids"]

        complete = self._check_completeness(state, state.final_answer)
        state.completeness_check = complete
        if answer_revision_allowed(self.enable_answer_revision, complete.complete,
                                   state.revision_count):
            state.revision_used = True
            revised = revise_answer_node(
                state, state.final_answer or "", complete.missing_points, self._llm
            )
            state.revision_count += 1
            state.final_answer = revised["answer"]
            answer_declares_insufficient = revised["insufficient_evidence"]
            used_evidence_ids = revised["used_evidence_ids"]
            state.completeness_check = self._check_completeness(state, state.final_answer)

        validation = validate_answer_citations(
            state.final_answer or "", citation_map, used_evidence_ids,
        )
        self._transition(state, "citation_check")
        state.citation_check = CitationCheck.from_validation(validation)
        if citation_revision_allowed(self.enable_citation_revision, validation.valid,
                                     state.citation_revision_count):
            state.citation_revision_used = True
            revised = revise_citations_node(
                state, state.final_answer or "", validation.errors, self._llm
            )
            state.citation_revision_count += 1
            state.final_answer = revised["answer"]
            answer_declares_insufficient = revised["insufficient_evidence"]
            self._transition(state, "citation_recheck")
            validation = validate_answer_citations(
                state.final_answer, citation_map, revised["used_evidence_ids"]
            )
            state.citation_check = CitationCheck.from_validation(validation)

        suspicious_claims = (
            claims_needing_semantic_alignment(
                state.final_answer or "", state.current_evidence
            ) if (state.citation_check.valid
                  and state.citation_revision_count == 0) else []
        )
        if suspicious_claims and llm_call_allowed(len(state.llm_calls)):
            allow_semantic_revision = citation_revision_allowed(
                self.enable_citation_revision, False, state.citation_revision_count
            )
            semantic = _json_object(self._llm(
                state, "semantic_citation_alignment", semantic_citation_prompt(
                    state.final_answer or "", suspicious_claims,
                    state.current_evidence, allow_revision=allow_semantic_revision,
                )
            ))
            if not isinstance(semantic.get("valid"), bool):
                raise ValueError("semantic citation valid must be boolean")
            if not isinstance(semantic.get("reason", ""), str):
                raise ValueError("semantic citation reason must be a string")
            semantic_errors = _string_list(
                semantic.get("errors", []), "semantic citation errors"
            )
            if semantic["valid"] and semantic_errors:
                raise ValueError("semantic citation errors must be empty when valid is true")
            state.citation_check.alignment_checked = True
            state.citation_check.alignment_method = "structured_llm"
            state.citation_check.alignment_reason = str(semantic.get("reason", ""))
            state.citation_check.reviewed_claims = suspicious_claims
            if not semantic["valid"]:
                state.citation_check.valid = False
                state.citation_check.errors.extend(
                    semantic_errors or [str(semantic.get("reason", "semantic citation mismatch"))]
                )
                revised_payload = semantic.get("revised_answer")
                if allow_semantic_revision and isinstance(revised_payload, dict):
                    revised = parse_model_output(json.dumps(
                        revised_payload, ensure_ascii=False
                    ))
                    state.citation_revision_used = True
                    state.citation_revision_count += 1
                    state.final_answer = revised["answer"]
                    answer_declares_insufficient = revised["insufficient_evidence"]
                    self._transition(state, "citation_recheck")
                    validation = validate_answer_citations(
                        state.final_answer, citation_map, revised["used_evidence_ids"]
                    )
                    state.citation_check = CitationCheck.from_validation(validation)
                    state.citation_check.alignment_checked = True
                    state.citation_check.alignment_method = "structured_llm_with_revision"
                    state.citation_check.alignment_reason = str(semantic.get("reason", ""))
                    state.citation_check.reviewed_claims = suspicious_claims
        elif suspicious_claims:
            state.citation_check.valid = False
            state.citation_check.errors.append(
                "Semantic citation alignment required but LLM call budget is exhausted"
            )
            state.citation_check.alignment_checked = False
            state.citation_check.alignment_method = "required_but_budget_exhausted"
            state.citation_check.alignment_reason = state.citation_check.errors[-1]
            state.citation_check.reviewed_claims = suspicious_claims
        elif state.citation_check.valid and state.citation_revision_count > 0:
            state.citation_check.alignment_checked = False
            state.citation_check.alignment_method = "not_required_after_targeted_revision"
            state.citation_check.alignment_reason = (
                "Deterministic citation recheck passed after the single targeted revision."
            )
        elif state.citation_check.valid:
            state.citation_check.alignment_checked = False
            state.citation_check.alignment_method = "not_required_by_deterministic_gate"
            state.citation_check.alignment_reason = (
                "No low-overlap cited claim was found by the deterministic gate."
            )
        else:
            state.citation_check.alignment_checked = False
            state.citation_check.alignment_method = "deterministic_validation_failed"
            state.citation_check.alignment_reason = "; ".join(state.citation_check.errors)

        state.final_status = determine_final_status(
            citation_valid=state.citation_check.valid,
            coverage_sufficient=state.coverage_check.sufficient,
            completeness_complete=state.completeness_check.complete,
            expansion_used=state.expansion_used,
            answer_declares_insufficient=answer_declares_insufficient,
        )
        self._transition(state, f"final:{state.final_status}")
        return state

    def _check_completeness(self, state: AgentState, answer: str | None) -> CompletenessCheck:
        return check_answer_completeness(state, answer, self._llm)


def run_agentic_rag(
    query: str, pipeline: RetrievalPipeline, client: LLMClient, *,
    run_id: str | None = None, state: AgentState | None = None,
    config: AgenticConfig | None = None,
) -> AgentState:
    """Run v1 with explicit dependencies and the frozen feature switches."""
    config = config or AgenticConfig()
    return AgenticRAGController(
        pipeline, client,
        enable_expansion=config.enable_expansion,
        enable_answer_revision=config.enable_answer_revision,
        enable_citation_revision=config.enable_citation_revision,
    ).run(query, run_id=run_id, state=state)
