# Repository Map

This map answers where each new file belongs. Paths are relative to the repository
root.

| File or artifact type | Canonical location | Rule |
|---|---|---|
| Reusable application/library code | `src/legal_rag/` | Organize by ingestion, retrieval, generation, agentic version, or evaluation. |
| Supported user CLI | `scripts/` | Keep argument parsing and orchestration thin; algorithms belong in `src/`. |
| Dataset maintenance command | `tools/dataset/` | May orchestrate corpus/benchmark maintenance, not runtime retrieval. |
| Annotation command | `tools/annotation/` | Read/write annotation working data only through explicit paths. |
| Validation/diagnostic command | `tools/validation/` | Cross-artifact checks belong here; generic validation primitives belong in `src/`. |
| Experiment-specific analysis | `tools/research/<topic>/` | Preserve scientific provenance and keep it outside production entrypoints. |
| Obsolete historical utility | `tools/legacy/` | Retain only with an explanation; never import from active code. |
| Raw legal source | `data/raw/docx/` or `data/raw/pdf/` | Preserve the original source and registry metadata. |
| Extracted/cleaned text | `data/extracted/` | Deterministic intermediate text artifacts. |
| Current processed corpus | `data/processed/` | Canonical `articles.jsonl` and `chunks.jsonl`. |
| Frozen corpus release | `data/versions/<version>/` | Immutable versioned data and its validation manifest. |
| Evaluation input/gold | `eval-sets/<benchmark>/` | Isolated from runtime; never write generated results here. |
| Retrieval index | `experiments/indexes/<version>/` | Store embeddings and index manifests together. |
| Authoritative historical experiment | `experiments/reference/<domain>/` | Immutable research evidence; do not clean as cache. |
| New experiment output | `experiments/runs/<domain>/` | Disposable/reproducible output; ignored by Git except directory anchors. |
| Runtime/evaluation trace | `experiments/traces/<system>/` | Preserve trace schema/version and avoid benchmark gold. |
| Annotation working data/report | `annotation/<benchmark>/` | Drafts, backups, samples, and human-review reports. |
| Versioned model prompt | `prompts/` | Treat historical prompts as frozen inputs. |
| Active regression test | `tests/<package-area>/` | Mirror package boundaries: ingestion, retrieval, generation, agentic/v1, evaluation. |
| Design or migration documentation | `docs/architecture/` or `docs/refactor/` | Historical reports remain factual and need not be rewritten. |

Phase 5C challenge HOLDOUT material is outside the ordinary migration workflow.
Do not create, expose, or reorganize plaintext HOLDOUT data without a separately
reviewed isolation plan.
