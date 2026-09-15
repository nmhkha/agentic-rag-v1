from __future__ import annotations

import json
import unittest

from legal_rag.agentic.v1.controller import AgenticRAGController
from legal_rag.agentic.v1.state import AgentState
from tests.agentic.v1.support import FakePipeline, STRAIGHT, ScriptedClient, model_answer


class ControllerTests(unittest.TestCase):
    def run_case(self, responses, **flags):
        client = ScriptedClient(responses)
        state = AgenticRAGController(FakePipeline(), client, **flags).run("q", run_id="run")
        return state, client

    def test_a_straight_through_success(self) -> None:
        state, _ = self.run_case(list(STRAIGHT))
        self.assertEqual(state.final_status, "success")
        self.assertFalse(state.expansion_used or state.revision_used or state.citation_revision_used)

    def test_b_expansion_is_bounded_and_merges(self) -> None:
        responses = ['{"sufficient":false,"missing_aspects":["a","b","c","d"],"reason":"thiếu"}', model_answer(), '{"complete":true,"missing_points":[],"reason":"đủ"}']
        state, _ = self.run_case(responses)
        self.assertTrue(state.expansion_used)
        self.assertEqual(len(state.sub_queries), 3)
        self.assertEqual(state.retrieval_round, 1)
        self.assertEqual(len(state.retrieval_calls), 4)

    def test_c_answer_revision_once(self) -> None:
        responses = [STRAIGHT[0], model_answer(), '{"complete":false,"missing_points":["x"],"reason":"thiếu"}', model_answer("Nội dung 1 bổ sung [E1]"), STRAIGHT[2]]
        state, _ = self.run_case(responses)
        self.assertEqual(state.revision_count, 1)
        self.assertTrue(state.revision_used)

    def test_d_citation_revision_once(self) -> None:
        responses = [STRAIGHT[0], model_answer("Sai [E99]", ["E99"]), STRAIGHT[2], model_answer()]
        state, _ = self.run_case(responses)
        self.assertEqual(state.citation_revision_count, 1)
        self.assertTrue(state.citation_revision_used)

    def test_e_combined_path_uses_six_calls(self) -> None:
        responses = ['{"sufficient":false,"missing_aspects":["x"],"reason":"thiếu"}', model_answer("Sai [E99]", ["E99"]), '{"complete":false,"missing_points":["x"],"reason":"thiếu"}', model_answer("Vẫn sai [E99]", ["E99"]), STRAIGHT[2], model_answer()]
        state, client = self.run_case(responses)
        self.assertTrue(state.expansion_used and state.revision_used and state.citation_revision_used)
        self.assertEqual(len(client.records), 6)

    def test_f_insufficient_and_g_incomplete_statuses(self) -> None:
        insufficient = ['{"sufficient":false,"missing_aspects":[],"reason":"thiếu"}', model_answer(insufficient=True), STRAIGHT[2]]
        state, _ = self.run_case(insufficient)
        self.assertEqual(state.final_status, "insufficient_evidence")
        incomplete = [STRAIGHT[0], model_answer(), '{"complete":false,"missing_points":["x"],"reason":"thiếu"}']
        state, _ = self.run_case(incomplete, enable_answer_revision=False)
        self.assertEqual(state.final_status, "incomplete_answer")

    def test_h_llm_budget_exhaustion(self) -> None:
        controller = AgenticRAGController(FakePipeline(), ScriptedClient([]))
        state = AgentState("q", llm_calls=[{} for _ in range(6)])
        with self.assertRaisesRegex(RuntimeError, "budget exceeded"):
            controller._llm(state, "stage", "prompt")

    def test_i_malformed_controller_and_j_empty_revision_output(self) -> None:
        with self.assertRaises((ValueError, json.JSONDecodeError)):
            self.run_case(["not-json"])
        responses = [STRAIGHT[0], model_answer(), '{"complete":false,"missing_points":["x"]}', ""]
        with self.assertRaises((ValueError, json.JSONDecodeError)):
            self.run_case(responses)


if __name__ == "__main__":
    unittest.main()
