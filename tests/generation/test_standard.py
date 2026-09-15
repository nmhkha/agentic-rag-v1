from __future__ import annotations

import unittest

from legal_rag.generation.standard import make_trace, run_rag
from legal_rag.retrieval.pipeline import Evidence


def item(rank: int) -> Evidence:
    return Evidence(
        rank=rank, evidence_id=f"E{rank}", chunk_id=f"c{rank}",
        document_id="doc", document_number="1/2026", document_title="Luật",
        article_id="doc_dieu-1", article="1", article_label="Điều 1",
        clause=None, clause_label=None, point=None, point_label=None,
        text=f"Text {rank}", retrieval_text=f"Text {rank}",
        official_source_url=None, reranker_score=float(3-rank),
        bm25_rank=rank, dense_rank=rank,
    )


class FakePipeline:
    def retrieve(self, query, top_k):
        return [item(1), item(2)][:top_k]


class FakeClient:
    def __init__(self):
        self.prompts = []

    def generate(self, prompt):
        self.prompts.append(prompt)
        return '{"answer":"Kết luận [E1]","used_evidence_ids":["E1"],"insufficient_evidence":false,"missing_information":[]}'


class StandardTests(unittest.TestCase):
    def test_offline_run_contract(self) -> None:
        client = FakeClient()
        run = run_rag("Câu hỏi?", FakePipeline(), client)
        self.assertEqual(run["query"], "Câu hỏi?")
        self.assertEqual(run["parsed_result"]["answer"], "Kết luận [E1]")
        self.assertTrue(run["citation_validation"]["valid"])
        self.assertEqual(len(client.prompts), 1)

    def test_trace_deterministic_fields(self) -> None:
        run = run_rag("Câu hỏi?", FakePipeline(), FakeClient())
        trace = make_trace(run)
        self.assertEqual(trace["retrieved_chunk_ids"], ["c1", "c2"])
        self.assertEqual(trace["formatted_evidence_ids"], ["E1", "E2"])
        self.assertEqual(trace["prompt_version"], "legal-rag-prompt-v0")


if __name__ == "__main__":
    unittest.main()
