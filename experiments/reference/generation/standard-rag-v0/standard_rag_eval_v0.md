# Standard RAG Generation Evaluation v0

This is the Standard RAG baseline, not Agentic RAG. Generation used the frozen retrieval pipeline, `legal-rag-prompt-v0`, and `gemini-3.5-flash-lite`. No benchmark, gold label, prompt, retriever, or reranker was changed.

## Dataset

- Generation evaluation: `generation-eval-v1`
- Queries: **31**
- Required points: **102**
- Dataset status: **verified**
- SHA-256: `1795dbef913e63492c5cd6b8963c2f1a85642ddee0b1a42087f97203bc1895a4`

## System

- Retrieval: `BM25-simple-v0@20 + dense-jina-v3-v0@20 union -> BAAI/bge-reranker-v2-m3`
- Dense model/revision: `jinaai/jina-embeddings-v3` / `ab036b023d30b4d1138c4c3bfa9f0c445ab455d6`
- Reranker: `BAAI/bge-reranker-v2-m3` / `953dc6f6f85a1b2dbfca4c34a2796e7dde08d41e`
- Evidence top-k: **5**
- Prompt: `legal-rag-prompt-v0`
- LLM: `gemini-3.5-flash-lite`

## Results

- Answer Completeness (macro): **0.6753**
- Answer Completeness (micro): **0.5882**
- Weighted Completeness: **N/A** — no numeric ground-truth weights; categorical importance labels were not converted into weights.
- Citation Completeness: **0.6753**
- Citation syntax validity: **30/31** (0.9677)
- Citation Correctness: **0.9613**
- Groundedness: **0.9613**
- Unsupported Claim Rate: **0.0387**
- Abstention Accuracy: **N/A** — All 31 frozen queries are answerable.

Semantic metrics use a structured evaluator call over each answer, its citations, required points, and Top-5 evidence. Syntax-level `citation_valid` remains separately recorded in each JSONL record.
`retrieval_gold_coverage` is reported separately and was not used as Answer Completeness.

## Per-query analysis

| query | completeness | citation completeness | citation correctness | groundedness | unsupported claim rate | retrieval gold coverage | failure taxonomy |
|---|---:|---:|---:|---:|---:|---:|---|
| eval001 | 0.000 | 0.000 | 1.000 | 1.000 | 0.000 | 0.667 | evidence_coverage_issue, answer_generation_issue |
| eval002 | 0.500 | 0.500 | 1.000 | 1.000 | 0.000 | 1.000 | answer_generation_issue |
| eval003 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | — |
| eval004 | 0.500 | 0.500 | 1.000 | 1.000 | 0.000 | 0.167 | evidence_coverage_issue, answer_generation_issue |
| eval005a | 0.000 | 0.000 | 1.000 | 1.000 | 0.000 | 0.000 | retrieval_miss, evidence_coverage_issue, answer_generation_issue |
| eval005b | 0.000 | 0.000 | 1.000 | 1.000 | 0.000 | 0.167 | evidence_coverage_issue, answer_generation_issue |
| eval006 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | — |
| eval007 | 0.500 | 0.500 | 1.000 | 1.000 | 0.000 | 0.222 | evidence_coverage_issue, answer_generation_issue |
| eval008 | 0.667 | 0.667 | 1.000 | 1.000 | 0.000 | 0.500 | evidence_coverage_issue, answer_generation_issue |
| eval009 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | — |
| eval010 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | — |
| eval011 | 0.500 | 0.500 | 1.000 | 1.000 | 0.000 | 0.000 | retrieval_miss, evidence_coverage_issue, answer_generation_issue |
| eval012 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | citation_issue |
| eval013 | 0.600 | 0.600 | 1.000 | 1.000 | 0.000 | 0.600 | evidence_coverage_issue, answer_generation_issue |
| eval014 | 0.000 | 0.000 | 1.000 | 1.000 | 0.000 | 0.500 | evidence_coverage_issue, answer_generation_issue |
| eval015 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | — |
| eval016 | 0.500 | 0.500 | 0.800 | 0.800 | 0.200 | 0.400 | evidence_coverage_issue, answer_generation_issue, citation_issue |
| eval017 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | — |
| eval018 | 0.750 | 0.750 | 1.000 | 1.000 | 0.000 | 0.667 | evidence_coverage_issue, answer_generation_issue |
| eval019 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | — |
| eval020 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | — |
| eval021 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 0.333 | evidence_coverage_issue |
| eval022 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.333 | evidence_coverage_issue, answer_generation_issue, citation_issue |
| eval023 | 0.500 | 0.500 | 1.000 | 1.000 | 0.000 | 0.500 | evidence_coverage_issue, answer_generation_issue |
| eval024 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | — |
| eval025 | 0.667 | 0.667 | 1.000 | 1.000 | 0.000 | 0.286 | evidence_coverage_issue, answer_generation_issue |
| eval026 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 0.250 | evidence_coverage_issue |
| eval027 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 0.250 | evidence_coverage_issue |
| eval028 | 0.750 | 0.750 | 1.000 | 1.000 | 0.000 | 0.500 | evidence_coverage_issue, answer_generation_issue |
| eval029 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | — |
| eval030 | 0.500 | 0.500 | 1.000 | 1.000 | 0.000 | 1.000 | answer_generation_issue |

### Best queries

`eval003` (1.000), `eval006` (1.000), `eval009` (1.000), `eval010` (1.000), `eval012` (1.000)

### Worst queries

`eval001` (0.000), `eval005a` (0.000), `eval005b` (0.000), `eval014` (0.000), `eval022` (0.000)

### Failure taxonomy

- `answer_generation_issue`: 17
- `citation_issue`: 3
- `evidence_coverage_issue`: 18
- `retrieval_miss`: 2

### Sample audit

Deterministic random sample (seed `20260902`): `eval026`, `eval008`, `eval019`, `eval030`, `eval023`.
The corresponding actual answers, citations, Top-5 evidence metadata, point decisions, and judge decisions are stored in `standard_rag_eval_v0.jsonl` for inspection.

## Integrity and reproducibility

- Retrieval benchmark SHA-256: `659c5cd0ff378747b9b135df00be57e5c1f5681b7eede761d3ce5808afbf3c62`
- Corpus SHA-256: `0a6eff1601d14d6409552d566411cc8aebb5f51938402e3f998c312d72d63c67`
- Prompt SHA-256: `0141aad79a262960eeeb88d9b138bc092ea15caeb0407a5ebadad27b8268d39e`
- Generation errors: **0**
- Evaluation errors: **0**
- Silent skips: **0**; result records: **31/31**

No retrieval or generation benchmark artifact was modified after the run.
