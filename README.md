# Vietnamese Legal Agentic RAG

## Overview

This repository is a reproducible research implementation for retrieval and
answer generation over a versioned Vietnamese legal corpus. The importable
package is `legal_rag`; command-line entrypoints are intentionally thin and all
benchmark gold is isolated from runtime code.

## Architecture

```text
Query
  |
  v
BM25@20 + Dense@20
  |
  v
Union / deduplication
  |
  v
BGE reranker
  |
  v
Top-5 evidence
  |-- Standard RAG (single answer pass)
  `-- Agentic RAG v1
       |-- evidence check and bounded conditional expansion
       |-- answer generation
       |-- completeness check and bounded revision
       `-- citation validation and bounded revision
```

Standard RAG and Agentic RAG v1 share ingestion, retrieval, evidence formatting,
LLM-client, and evaluation modules. Agentic RAG v2 is future work and is not
implemented here.

## Repository Structure

- `src/legal_rag/`: importable ingestion, retrieval, generation, Agentic v1, and evaluation logic.
- `scripts/`: supported user-facing CLIs only.
- `tools/`: dataset, annotation, validation, and research maintenance commands.
- `data/`: raw sources, processed corpus, validation evidence, and frozen corpus versions.
- `eval-sets/`: benchmark inputs and gold labels; never loaded by runtime paths.
- `experiments/`: indexes, frozen reference evidence, traces, and disposable new runs.
- `annotation/`: working annotation data and reviewer reports.
- `prompts/`: versioned prompt templates.
- `docs/`: architecture, migration, and research documentation.
- `tests/`: active package-oriented regression suites.

See [docs/REPOSITORY_MAP.md](docs/REPOSITORY_MAP.md) for placement rules.

## Installation

Python 3.12 or newer is required (tested: 3.12.14). `pyproject.toml` is
authoritative; `requirements.txt` is a convenience runtime dependency list.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

Model weights are not downloaded during installation by this project. Runtime
retrieval requires compatible locally available Hugging Face model assets or
normal library cache behavior.

## Quick Start

Inspect the offline-safe interfaces first:

```bash
python scripts/ingest.py --help
python scripts/build_index.py --help
python scripts/run_eval.py --help
```

Runtime generation reads the OpenAI-compatible settings documented in
`.env.example`. Keep real credentials outside the repository.

## Run Standard RAG

```bash
python scripts/run_standard_rag.py --query "Nội dung câu hỏi pháp lý"
```

## Run Agentic RAG v1

```bash
python scripts/run_agentic_rag.py --query "Nội dung câu hỏi pháp lý" --trace
```

Agentic v1 uses frozen bounds and prompts. It is a historical research baseline,
not a substitute for professional legal advice.

## Run the API

Set the `RAG_LLM_MODEL`, `RAG_LLM_BASE_URL`, and `RAG_LLM_API_KEY`
environment variables, then run one Uvicorn worker:

```bash
python -m uvicorn legal_rag.api.app:app --host 127.0.0.1 --port 8000 --workers 1
```

Open `http://127.0.0.1:8000/` for the minimal web client. The API endpoints are
`GET /api/v1/health` and `POST /api/v1/answers` with a JSON body such as
`{"query":"Nội dung câu hỏi pháp lý"}`. `rag_latency_ms` measures only the
Agentic RAG controller execution. Browser and benchmark end-to-end latency also
includes request queuing, trace persistence, HTTP transfer, and JSON parsing.

After the API is ready, run an end-to-end benchmark with:

```bash
python tools/research/api/benchmark_e2e.py \
  --query "Nội dung câu hỏi pháp lý" \
  --warmup 1 \
  --runs 5
```

The benchmark stores individual samples, RAG and HTTP end-to-end summaries, and
the test machine CPU metadata under `experiments/runs/api-benchmark/`.

See [Web API handoff](docs/WEB_API_HANDOFF.md) for the tested Windows setup,
exact Hugging Face cache revisions, temporary credential configuration, API
contract, verification results, and known limitations. `.env.example` is a
template only: the application does not automatically load `.env` files.

The web layer is isolated in `src/legal_rag/api/` (including vanilla HTML/CSS/JS
in `static/`), with offline tests in `tests/api/` and the HTTP benchmark in
`tools/research/api/`. The application reuses one loaded retrieval pipeline and
LLM client per worker; it does not replace the frozen RAG implementation.

## Evaluation

Re-score stored output without inference or API access:

```bash
python scripts/run_eval.py \
  --pipeline agentic-v1 \
  --score-only \
  --results experiments/reference/generation/agentic-rag-v1/agentic_rag_eval_v1_agentic-v1.jsonl
```

The authoritative Agentic v1 historical benchmark reports Answer Completeness
macro approximately `0.7237`, while micro is `65/102` (approximately `0.6373`).
Groundedness macro and pooled values are different summaries, so this repository
does not claim universal groundedness improvement. Detailed metrics and reports
live in `experiments/reference/generation/` and `docs/`.

New reruns may vary because generation and model execution can be stochastic;
store them under `experiments/runs/` and do not overwrite historical references.

## Corpus

The canonical working corpus is `data/processed/chunks.jsonl`; the frozen version
is `data/versions/corpus-v0.1/`. It contains 737 deterministic chunks with unique
IDs. Source provenance is recorded in `data/source_registry/`.

## Experiment Artifacts

`experiments/reference/` contains immutable historical research evidence.
`experiments/indexes/` contains retrieval indexes, `experiments/traces/` contains
execution traces, and `experiments/runs/` is reserved for disposable new output.
The repository intentionally does not blanket-ignore `experiments/`.

## Reproducibility

Use frozen corpus/evaluation versions, pinned runtime dependencies, stored model
revisions, and score-only evaluation where possible. Do not feed `eval-sets/`
gold fields to a runtime executor. Phase 5 provenance-sensitive tools are retained
byte-for-byte under `tools/research/phase5/`.

## Research Status

- Agentic RAG v1: implemented and frozen historical baseline.
- Agentic RAG v2: not implemented yet.
- Phase 5 controlled ablation: completed.
- Phase 5C challenge benchmark: in progress; HOLDOUT handling remains deferred.

The resource-constrained challenge benchmark has not received human legal
validation, and M7 does not expose or migrate HOLDOUT plaintext.

## Development

```bash
pytest
```

Keep reusable logic in `src/legal_rag/`, thin user commands in `scripts/`, and
maintenance or experiment-specific commands in `tools/`. Generic caches, local
environments, credentials, and new experiment runs are ignored.
