from __future__ import annotations

import json
from dataclasses import replace

from legal_rag.retrieval.pipeline import Evidence, RetrievalPipeline


def make_evidence(number: int, score: float | None = None) -> Evidence:
    return Evidence(
        rank=number, evidence_id=f"E{number}", chunk_id=f"chunk-{number}",
        document_id="doc", document_number="1/2026", document_title="Luật",
        article_id="doc_dieu-1", article="1", article_label="Điều 1",
        clause=None, clause_label=None, point=None, point_label=None,
        text=f"Nội dung {number}", retrieval_text=f"Nội dung {number}",
        official_source_url=None, reranker_score=score if score is not None else 10-number,
        bm25_rank=number, dense_rank=number,
    )


class FakePipeline(RetrievalPipeline):
    def __init__(self, evidences=None, audit=None):
        self.values = evidences or [make_evidence(i) for i in range(1, 7)]
        self.audit = audit
        self.calls = []

    def retrieve_with_audit(self, query, top_k=5, *, all_candidates=False):
        self.calls.append((query, all_candidates))
        values = list(self.values if all_candidates else self.values[:top_k])
        audit = self.audit or {
            "query": query, "bm25_depth": 20, "dense_depth": 20,
            "candidate_chunk_ids": [item.chunk_id for item in values],
            "candidate_count": len(values), "reranker_ranks": [],
            "top5_chunk_ids": [item.chunk_id for item in values[:5]],
            "candidate_ranks": [],
        }
        return values, dict(audit)


class ScriptedClient:
    model = "gemini-3.5-flash-lite"

    def __init__(self, responses):
        self.responses = iter(responses)
        self.records = []

    def generate(self, prompt):
        response = next(self.responses)
        self.records.append({
            "call_index": len(self.records) + 1,
            "prompt": prompt,
            "response": response,
        })
        return response


def model_answer(answer="Nội dung 1 [E1]", used=None, insufficient=False):
    return json.dumps({
        "answer": answer,
        "used_evidence_ids": used if used is not None else ["E1"],
        "insufficient_evidence": insufficient,
        "missing_information": [],
    }, ensure_ascii=False)


STRAIGHT = [
    '{"sufficient":true,"missing_aspects":[],"reason":"đủ"}',
    model_answer(),
    '{"complete":true,"missing_points":[],"reason":"đủ"}',
]
