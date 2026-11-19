"""Public API for the frozen Agentic RAG v1 runtime."""

from .controller import AgenticRAGController, run_agentic_rag
from .evidence_selection import (
    GAP_PRESERVING_V1_PRACTICAL_V1,
    HISTORICAL_V1,
    MAX_RESERVED_EXPANSION_SLOTS,
)
from .policies import AgenticConfig
from .state import AgentState
from .trace import trace_for_state, write_trace

__all__ = ["AgentState", "AgenticConfig", "AgenticRAGController",
           "run_agentic_rag", "trace_for_state", "write_trace",
           "HISTORICAL_V1", "GAP_PRESERVING_V1_PRACTICAL_V1",
           "MAX_RESERVED_EXPANSION_SLOTS"]
