# Agentic RAG v1 dependency closure v0

Identified by recursive static imports, including imports inside functions and TYPE_CHECKING branches. No runtime/evaluator was imported or executed. This source closure is an overapproximation of runtime imports, not a successful execution certificate.

## Runtime: exact repository Python closure (10 files)

- `scripts/agentic_rag.py`
- `scripts/bm25_baseline.py`
- `scripts/citation_validator.py`
- `scripts/dense_baseline.py`
- `scripts/evidence_formatter.py`
- `scripts/llm_client.py`
- `scripts/rag_baseline.py`
- `scripts/reranker_baseline.py`
- `scripts/response_formatter.py`
- `scripts/retrieval_pipeline.py`

## Benchmark/evaluator closure

The evaluator requires the full runtime closure plus:

- `scripts/evaluate_agentic_rag.py`
- `scripts/evaluate_standard_rag.py`
- `scripts/validate_generation_eval.py`

`evaluate_agentic_rag.py` imports Standard judge_prompt, load_verified_dataset, parse_judge, point_audit and sha256. The Standard evaluator imports validate_generation_eval. Do not move the Standard evaluator merely because the desired release is Agentic v1. Production does not import the gold/evaluation closure.

## Required prompt/configuration

- `prompts/legal_rag_v0.txt`: shared frozen generation prompt.
- `scripts/agentic_rag.py`: inline coverage, completeness, answer revision, citation revision and semantic alignment prompts; budget/ablation constants are source-bound.
- `scripts/evaluate_standard_rag.py`: inline evaluation judge prompt, evaluator-only.
- `requirements.txt`, `data/indexes/dense-jina-v3-v0/index_manifest.json`, `data/indexes/bge-reranker-v2-m3-v0/reranker_manifest.json`, `data/rag/legal-rag-v0_manifest.json`: environment/asset provenance.
- Environment variables RAG_LLM_MODEL, RAG_LLM_BASE_URL, RAG_LLM_API_KEY. Model guard requires `gemini-3.5-flash-lite`. Distribute configuration documentation or a reviewed example, never `.env` credentials.

## Runtime data/assets

- `data/versions/corpus-v0.1/chunks.jsonl` (737 chunks per index manifest).
- `data/indexes/dense-jina-v3-v0/embeddings.npy`, `chunk_ids.json`, `index_manifest.json`: preserve ordering and bytes together.
- Dense model `jinaai/jina-embeddings-v3`, revision `ab036b023d30b4d1138c4c3bfa9f0c445ab455d6`; remote implementation code is required by trust_remote_code.
- Reranker `BAAI/bge-reranker-v2-m3`; Phase 5 assets pin `953dc6f6f85a1b2dbfca4c34a2796e7dde08d41e`. Direct BGEReranker default accepts revision=None, so the vanilla historical runtime is not fully pinned by source alone.
- External torch/transformers/numpy/rank_bm25 and transitive model dependencies. requirements.txt is not a full environment lock; historical manifests themselves note incomplete source/environment provenance. Cached Python source in this repository is not a complete weight bundle. No external model cache was read or downloaded.

## Evaluation-only assets and outputs

- Inputs: `data/evaluation/generation/generation_eval_v1_verified.json`, its `_manifest.json`, `data/evaluation/retrieval_eval.jsonl`, frozen corpus and prompt.
- Comparison input: `data/evaluation/generation/standard_rag_metrics_v0.json`.
- R1 results: `data/evaluation/generation/agentic_rag_eval_v1_agentic-v1.jsonl`, `agentic_rag_metrics_v1_agentic-v1.json`, `reports/agentic_rag_eval_v1_agentic-v1.md`.
- R1 traces: `data/rag/traces/agentic-rag-v1/agentic-v1/*.json`.
- General runtime trace root: `data/rag/traces/`. Results and trace trees are output requirements; preserved historical outputs are release evidence, not production input.

## Paths and Phase 5 extension

`Path(__file__).resolve().parents[1]`, bare sibling imports, sys.path insertion, README commands, absolute trace paths and frozen file inventories bind the original layout. Retain scripts/, prompts/, corpus/index paths, evaluator input/result paths, and Phase 5 run paths. `phase5_ablation_runner.py` asserts exact variant/query/output paths and builds an allowlist of source and asset paths; preflight launches it by script path. Phase 5 reproduction additionally needs phase5_*.py tools, query_inputs_v0.json, per-variant manifests, run locks, sealed traces, observer/attempt records, recovery protocols and canonical judgments. This is distinct from the minimal v1 release.

## Third-party packaging proposal

Package the ten original runtime files, frozen prompt, versioned corpus, dense index files and provenance/configuration in a layout-preserving runtime bundle. Provide model revision acquisition instructions or a separately reviewed complete offline model bundle. Add the three evaluator files, verified/gold inputs and preserved R0/R1 evidence only in a benchmark bundle. Preserve original source bytes and include licenses/dependency notices after a separate redistribution review. Exclude secrets, machine environment, incidental bytecode and unrelated reviewer material from the proposed release; do not delete them from this repository. Packaging is feasible in principle, but portability, model availability and exact historical generation reproducibility have not been tested.

## Direct local-import graph

| Consumer | Imported repository modules |
| --- | --- |
| `scripts/agentic_rag.py` | `scripts/citation_validator.py`, `scripts/evidence_formatter.py`, `scripts/llm_client.py`, `scripts/rag_baseline.py`, `scripts/response_formatter.py`, `scripts/retrieval_pipeline.py` |
| `scripts/bm25_baseline.py` |  |
| `scripts/citation_validator.py` |  |
| `scripts/dense_baseline.py` |  |
| `scripts/evaluate_agentic_rag.py` | `scripts/agentic_rag.py`, `scripts/citation_validator.py`, `scripts/evaluate_standard_rag.py`, `scripts/llm_client.py`, `scripts/retrieval_pipeline.py` |
| `scripts/evaluate_standard_rag.py` | `scripts/citation_validator.py`, `scripts/llm_client.py`, `scripts/rag_baseline.py`, `scripts/retrieval_pipeline.py`, `scripts/validate_generation_eval.py` |
| `scripts/evidence_formatter.py` | `scripts/retrieval_pipeline.py` |
| `scripts/llm_client.py` |  |
| `scripts/rag_baseline.py` | `scripts/citation_validator.py`, `scripts/evidence_formatter.py`, `scripts/llm_client.py`, `scripts/response_formatter.py`, `scripts/retrieval_pipeline.py` |
| `scripts/reranker_baseline.py` | `scripts/bm25_baseline.py`, `scripts/dense_baseline.py` |
| `scripts/response_formatter.py` |  |
| `scripts/retrieval_pipeline.py` | `scripts/reranker_baseline.py` |
| `scripts/validate_generation_eval.py` |  |
