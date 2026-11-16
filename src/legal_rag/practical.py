"""Practical task router with deterministic legal routes and v1 fallback."""

from __future__ import annotations

from typing import Any

from .agentic.v1.controller import AgenticRAGController, run_agentic_rag
from .agentic.v1.evidence_selection import GAP_PRESERVING_V1_PRACTICAL_V1
from .document_scoped_search import (
    DocumentScopedSearchResult,
    try_document_scoped_search,
)
from .exact_lookup import ExactLookupResult, ExactProvisionLookup, try_exact_lookup
from .navigation import DocumentNavigator, NavigationResult, try_document_navigation


def run_practical_rag(
    query: str,
    pipeline: Any = None,
    client: Any = None,
    *,
    controller: AgenticRAGController | None = None,
    navigator: DocumentNavigator | None = None,
    lookup: ExactProvisionLookup | None = None,
    **v1_kwargs: Any,
) -> NavigationResult | ExactLookupResult | DocumentScopedSearchResult | Any:
    """Run deterministic routes first, then v1 with its practical policy."""
    if pipeline is None and controller is not None:
        pipeline = getattr(controller, "pipeline", None)
    if client is None and controller is not None:
        client = getattr(controller, "client", None)

    navigation = try_document_navigation(query, navigator)
    if navigation.handled:
        return navigation
    exact = try_exact_lookup(query, navigator, lookup=lookup)
    if exact.handled:
        return exact
    if pipeline is not None:
        scoped = try_document_scoped_search(query, pipeline, navigator)
        if scoped.handled:
            return scoped

    if pipeline is None and controller is None:
        return NavigationResult(
            handled=False,
            intent="UNHANDLED",
            status="NOT_NAVIGATION",
            message="Query not handled by deterministic routes and no pipeline provided.",
        )

    v1_kwargs.setdefault(
        "final_evidence_policy", GAP_PRESERVING_V1_PRACTICAL_V1
    )
    if controller is not None:
        state = v1_kwargs.pop("state", None)
        run_id = v1_kwargs.pop("run_id", None)
        policy = v1_kwargs.pop("final_evidence_policy", GAP_PRESERVING_V1_PRACTICAL_V1)
        if hasattr(controller, "final_evidence_policy"):
            controller.final_evidence_policy = policy
        return controller.run(query, run_id=run_id, state=state, **v1_kwargs)

    return run_agentic_rag(query, pipeline, client, **v1_kwargs)


__all__ = ["run_practical_rag"]

