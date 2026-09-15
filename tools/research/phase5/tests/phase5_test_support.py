"""Synthetic fixtures only; never use final dataset text as controller inputs."""
import json
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from phase5_isolation import block_network
NETWORK = block_network()
from retrieval_pipeline import Evidence, RetrievalPipeline


def evidence(n):
    return Evidence(rank=n, evidence_id=f'E{n}', chunk_id=f'synthetic-{n}', document_id='synthetic-law',
        document_number='TEST', document_title='Synthetic rule', article_id='art-1', article='1',
        article_label='Article 1', clause=None, clause_label=None, point=None, point_label=None,
        text=f'Synthetic registration rule {n}', retrieval_text=f'Synthetic registration rule {n}',
        official_source_url=None, reranker_score=float(20-n), bm25_rank=n, dense_rank=n)


class Pipeline(RetrievalPipeline):
    def __init__(self, fail=False):
        self.calls, self.merges = [], []
        self.fail = fail

    def retrieve_with_audit(self, query, top_k=5, *, all_candidates=False):
        self.calls.append([query, top_k, all_candidates])
        if self.fail:
            raise RuntimeError('synthetic retrieval failure')
        values = [evidence(i) for i in range(1, 8)]
        return values, dict(query=query, candidate_count=7, candidate_chunk_ids=[e.chunk_id for e in values],
                            top5_chunk_ids=[e.chunk_id for e in values[:5]])

    def rerank_evidence_pool(self, query, pool, top_k=5):
        self.merges.append([query, [e.to_dict() for e in pool], top_k])
        return super().rerank_evidence_pool(query, pool, top_k)


class Client:
    model = 'gemini-3.5-flash-lite'
    def __init__(self, responses):
        self.responses = iter(responses)
        self.prompts = []

    def generate(self, prompt):
        self.prompts.append(prompt)
        result = next(self.responses)
        if isinstance(result, Exception):
            raise result
        return result


def answer(text='Synthetic registration rule 1 [E1]', used=None):
    return json.dumps(dict(answer=text, used_evidence_ids=['E1'] if used is None else used, insufficient_evidence=False, missing_information=[]))


def coverage(sufficient=True, missing=None):
    return json.dumps(dict(sufficient=sufficient, missing_aspects=missing or [], reason='synthetic'))


def completeness(complete=True):
    return json.dumps(dict(complete=complete, missing_points=[] if complete else ['synthetic detail'], reason='synthetic'))


def responses(alias='R2', expansion=False, incomplete=False, invalid=False, semantic=False):
    result = [coverage(not expansion, ['synthetic exception'] if expansion else []),
              answer('Unrelated astronomy assertion [E1]' if semantic else 'Synthetic registration rule 1 [E99]' if invalid else 'Synthetic registration rule 1 [E1]', ['E99'] if invalid else ['E1']),
              completeness(not incomplete)]
    if incomplete and alias != 'A1':
        result += [answer('Synthetic registration rule 1 [E99]', ['E99']) if invalid else answer(), completeness()]
    if invalid:
        result.append(answer())
    elif semantic:
        result.append(json.dumps(dict(valid=False, errors=['synthetic mismatch'], reason='synthetic', revised_answer=json.loads(answer()))))
    return result


def normalize(value):
    if isinstance(value, dict):
        return {k: normalize(v) for k, v in value.items() if k not in ('run_id', 'timestamp')}
    if isinstance(value, list):
        return [normalize(v) for v in value]
    return value
