from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from legal_rag.agentic.v1.controller import AgenticRAGController
from legal_rag.agentic.v1.trace import record_execution_error, trace_for_state, write_trace
from tests.agentic.v1.support import FakePipeline, STRAIGHT, ScriptedClient


class TraceTests(unittest.TestCase):
    def test_trace_schema_and_values(self) -> None:
        client = ScriptedClient(list(STRAIGHT))
        state = AgenticRAGController(FakePipeline(), client).run("q", run_id="run")
        trace = trace_for_state(state, client)
        expected = {"run_id", "query", "retrieval_config", "prompt_version", "model",
                    "provider", "initial_top5", "final_top5", "retrieval_calls",
                    "llm_calls", "budgets", "state", "timestamp"}
        self.assertTrue(expected.issubset(trace))
        self.assertEqual(trace["run_id"], "run")
        self.assertEqual(trace["retrieval_call_count"], len(trace["retrieval_calls"]))
        self.assertEqual(trace["llm_call_count"], len(trace["llm_calls"]))

    def test_error_record_and_explicit_trace_write(self) -> None:
        state = AgenticRAGController(FakePipeline(), ScriptedClient(list(STRAIGHT))).run("q")
        record_execution_error(state, ValueError("bad"))
        self.assertEqual(state.final_status, "execution_error")
        self.assertEqual(state.execution_error, {"type": "ValueError", "message": "bad"})
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "trace.json"
            self.assertEqual(write_trace(trace_for_state(state, None), path), path)
            self.assertTrue(path.read_text(encoding="utf-8").endswith("\n"))


if __name__ == "__main__":
    unittest.main()
