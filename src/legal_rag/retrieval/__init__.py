"""Stable retrieval APIs for the frozen legal RAG configuration."""

from .dense import DenseRetriever, build_dense_index, encode
from .fusion import HybridRRFRetriever, fuse_rankings
from .pipeline import Evidence, RetrievalPipeline, retrieval_config, retrieve
from .reranker import (
    BGEReranker,
    RerankerRetriever,
    rank_candidates,
    union_candidates,
)
from .sparse import BM25Retriever, read_chunks, tokenize

__all__ = [
    "BGEReranker",
    "BM25Retriever",
    "DenseRetriever",
    "Evidence",
    "HybridRRFRetriever",
    "RerankerRetriever",
    "RetrievalPipeline",
    "build_dense_index",
    "encode",
    "fuse_rankings",
    "read_chunks",
    "rank_candidates",
    "retrieval_config",
    "retrieve",
    "tokenize",
    "union_candidates",
]
