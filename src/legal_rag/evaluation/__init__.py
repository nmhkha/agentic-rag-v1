"""Unified, importable evaluation framework."""

from .metrics import (
    aggregate_generation,
    aggregate_retrieval,
    generation_query_metrics,
    retrieval_query_metrics,
)
from .pipelines import PIPELINES, get_pipeline
from .runner import run_evaluation

__all__ = [
    "PIPELINES",
    "aggregate_generation",
    "aggregate_retrieval",
    "generation_query_metrics",
    "get_pipeline",
    "retrieval_query_metrics",
    "run_evaluation",
]
