from __future__ import annotations

import json
import unittest

from legal_rag.agentic.v1.state import AgentState, CitationCheck
from tests.agentic.v1.support import make_evidence


class StateTests(unittest.TestCase):
    def test_defaults_and_serialization_preserve_all_runtime_fields(self) -> None:
        state = AgentState(query="q", initial_evidence=[make_evidence(1)])
        value = json.loads(json.dumps(state.to_dict(), ensure_ascii=False))
        for key in (
            "query", "current_evidence", "missing_aspects", "sub_queries",
            "draft_answer", "completeness_check", "citation_check",
            "revision_count", "citation_revision_count", "final_status",
            "retrieval_calls", "llm_calls", "execution_error", "transitions",
        ):
            self.assertIn(key, value)
        self.assertEqual(value["transitions"], ["initialized"])

    def test_citation_adapter_preserves_legacy_fields(self) -> None:
        from legal_rag.generation.verifier import CitationValidation
        source = CitationValidation(False, ["E1"], ["E9"], ["[e1]"], [], ["bad"])
        value = CitationCheck.from_validation(source)
        self.assertEqual(value.cited_evidence_ids, ["E1"])
        self.assertEqual(value.errors, ["bad"])


if __name__ == "__main__":
    unittest.main()
