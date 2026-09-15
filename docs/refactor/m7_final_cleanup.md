# M7 Final Cleanup Report

Status: **PASS**  
Working repository: `legal-agentic-rag-next`  
Scope: repository cleanup only; no Agentic v2 behavior, network access, model
inference, or challenge HOLDOUT migration.

## Script inventory and disposition

The pre-change inventory was recorded before relocation or deletion in
`docs/refactor/m7_script_disposition.csv`, including SHA-256 for all 51 Python
files under `scripts/`. Every file received exactly one requested classification;
there were no `UNKNOWN` entries.

| Measure | Before | After |
|---|---:|---:|
| Python files in `scripts/` | 51 | 5 |
| Primary thin CLIs | 5 | 5 |
| Core logic left only in legacy scripts | 1 | 0 |

The retained CLIs are `ingest.py`, `build_index.py`, `run_eval.py`,
`run_standard_rag.py`, and `run_agentic_rag.py`. They parse arguments and delegate
to `legal_rag`; help parsing occurs before optional heavy runtime imports.

## Deleted legacy implementation

Twenty-three fully replaced files were deleted after regression/equivalence
coverage was confirmed:

```text
agentic_rag.py                 bm25_baseline.py
build_chunks.py                build_dense_index.py
citation_validator.py          clean_docx_text.py
dense_baseline.py              evaluate_agentic_rag.py
evaluate_bm25.py               evaluate_dense.py
evaluate_hybrid.py             evaluate_reranker.py
evaluate_standard_rag.py       evidence_formatter.py
extract_docx.py                hybrid_rrf.py
llm_client.py                  parse_legal_structure.py
rag_baseline.py                reranker_baseline.py
response_formatter.py          retrieval_pipeline.py
validate_corpus.py
```

Their active replacements are under `src/legal_rag/ingestion`, `retrieval`,
`generation`, `agentic/v1`, `evaluation`, and `legal_rag.llm_client`.

## Tool relocation

Twenty-three useful utilities moved out of `scripts/`:

- 3 dataset tools to `tools/dataset/`;
- 4 annotation tools to `tools/annotation/`;
- 3 validation tools to `tools/validation/`;
- 12 research tools to topic directories under `tools/research/`;
- 1 obsolete registry utility to `tools/legacy/`.

The ten Phase 5 source tools were verified byte-identical after relocation
(10 checked, 0 SHA-256 mismatches). They remain frozen and inactive; their legacy
embedded paths/imports are documented in `tools/research/phase5/README.md` rather
than rewritten. The generation-evaluation validation tool now delegates reusable
record/point invariants to `legal_rag.evaluation.validation` and retains only its
cross-artifact and benchmark-specific checks.

## Remaining core migration

Canonical chunk construction moved from `scripts/build_chunks.py` to
`src/legal_rag/ingestion/chunking.py`. The public API exposes deterministic build
and serialization functions. Against the current corpus:

- chunk count: 737;
- duplicate chunk IDs: 0;
- deterministic order: PASS;
- chunk-ID equivalence: PASS;
- semantic equivalence: PASS;
- byte-for-byte JSONL equivalence: PASS.

Coverage is in `tests/ingestion/test_chunking.py`; only after it passed was the
legacy script deleted.

## Test cleanup

Active tests now follow package boundaries under ingestion, retrieval, generation,
agentic/v1, and evaluation. Three fully duplicated root legacy-runtime test files
were removed. Two useful root suites moved into generation/evaluation. Legacy
equivalence tests were converted to durable behavior contracts, including all 31
stored Agentic v1 initial Top-5 traces. Eight provenance-sensitive Phase 5 test
files moved byte-for-byte beside frozen research tooling and are not active tests.

Unique dataset validation, prompt/format/citation behavior, branch/budget behavior,
trace compatibility, retrieval ordering, historical metric reproduction, and gold
isolation coverage remain. Final active result: **98 passed, 0 failed** (63
`unittest` tests and 35 pytest-style M5 tests). Because pytest was unavailable in
the offline copied environment, the 35 tests were executed with the same minimal
compatibility harness used during M5; no test was skipped.

## Cache, environment, and credentials cleanup

- generic `__pycache__/`: removed (0 remain outside frozen reference artifacts);
- generic `*.pyc`/`*.pyo`: removed (0 remain outside frozen reference artifacts);
- `.pytest_cache/`: removed;
- copied `.venv/`: removed and not recreated;
- `.env`: removed; `.env.example` retained;
- high-confidence credential scan: 0 real credential candidates.

The supported recreation command is:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Packaging and configuration

`pyproject.toml` is authoritative and defines Python >=3.10, runtime dependencies,
the `dev` extra, src-layout discovery, and pytest discovery. `requirements.txt` is
the matching convenience runtime list. `.gitignore` covers credentials,
environments, Python/tool caches, coverage, builds, distributions, and egg-info;
only `experiments/runs/**` is ignored, not frozen references or evaluation gold.

A fresh temporary venv installed the package editable with
`--no-deps --no-build-isolation`; build dependencies and runtime dependencies were
reused from the existing offline environment before its removal. Imports of
`legal_rag`, ingestion, retrieval, generation, agentic.v1, and evaluation passed.
No dependency resolution or network access occurred.

## Scans and offline verification

- active `from scripts` / `import scripts` matches: 0;
- active dependencies on deleted legacy files: 0;
- one deleted-basename text match is the legitimate current path
  `src/legal_rag/llm_client.py`;
- stale M5/M6 runtime paths (`data/indexes`, `data/evaluation`,
  `data/rag/traces`) in active code: 0;
- CLI `--help`: 5/5 PASS after `.venv` removal;
- historical reranker retrieval score-only: PASS;
- historical Standard RAG score-only: PASS;
- historical Agentic v1 score-only: PASS;
- runtime evaluation/gold import isolation: PASS.

Stored Agentic v1 traces remain readable and reproduce:

```text
expansion = 6/31
answer_revision = 7/31
citation_revision = 1/31
success = 28
insufficient_evidence = 2
incomplete_answer = 1
```

## Final repository tree

```text
src/legal_rag/             importable core package
scripts/                   5 supported thin CLIs
tools/                     dataset, annotation, validation, research, legacy tools
data/                      source and corpus data
eval-sets/                 benchmark input/gold
experiments/indexes/       retrieval indexes
experiments/reference/     frozen historical evidence
experiments/runs/          new disposable outputs
experiments/traces/        runtime/evaluation traces
annotation/                annotation workspace and reports
prompts/                   versioned prompts
docs/                      maps, architecture/research history, migration reports
tests/                     active package-oriented tests
```

## Known remaining technical debt

- Frozen Phase 5 tools contain pre-M7 path strings and imports. Updating them would
  change provenance-sensitive source, so they are explicitly inactive historical
  tooling; frozen outputs are verified through the new evaluation package.
- Phase 5C challenge HOLDOUT migration remains intentionally deferred. No plaintext
  HOLDOUT was exposed or reorganized, and no human legal validation is claimed.
- A normal development environment must install `.[dev]` to run pytest directly.
- No automated deletion was performed for modules under `src/legal_rag/`: all have
  an import path, test coverage, or intended public role. No obvious duplicate
  legacy implementation remains there.

The repository is ready for a separately scoped Agentic v2 development phase.
