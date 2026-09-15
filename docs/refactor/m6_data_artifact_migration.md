# M6 data, eval-set, experiment, and annotation migration

## Result

M6 reorganized 1,489 files (196,419,922 bytes) without changing any moved
file's content. The pre-migration inventory, complete per-file path map, and
post-migration verification are respectively:

- `m6_pre_migration_manifest.json`
- `m6_path_map.json`
- `m6_post_migration_manifest.json`

All destination SHA-256 values equal their recorded pre-migration values.
Missing files, hash mismatches, and duplicate destination paths are all zero.

## Classification and directory map

| Old area | New canonical area | Role |
|---|---|---|
| `data/indexes/` | `experiments/indexes/` | generated retrieval indexes |
| `data/evaluation/retrieval_eval.jsonl` | `eval-sets/retrieval/` | verified retrieval gold/input |
| verified generation dataset/schema/manifest | `eval-sets/generation/` | authoritative generation gold/input |
| retrieval evaluator results | `experiments/reference/retrieval/<system>/` | frozen historical outputs |
| Standard RAG results | `experiments/reference/generation/standard-rag-v0/` | frozen historical outputs |
| Agentic v1 results | `experiments/reference/generation/agentic-rag-v1/` | frozen historical outputs |
| generic generation analyses | `experiments/reference/generation/analysis/` | historical research analyses |
| Agentic/runtime/Phase 5 traces | `experiments/traces/` | historical run evidence |
| Phase 5 result tree | `experiments/reference/phase5/` | sealed historical research evidence |
| generic retrieval comparisons | `experiments/comparisons/` | cross-system reports |
| annotation reports/drafts/history | `annotation/retrieval/`, `annotation/generation/` | review workflow material |

`data/` now contains only source/corpus material: raw, extracted, processed,
source registry, corpus validation, and versioned corpus assets. `eval-sets/`
contains inputs only. `experiments/reference/` is frozen evidence and is not
disposable; future outputs belong under `experiments/runs/`.

## Counts

The path-map classifications are:

| Classification | Files |
|---|---:|
| sealed Phase 5 reference | 846 |
| historical traces | 573 |
| historical retrieval outputs | 24 |
| annotation/review material | 19 |
| historical generation outputs/reports | 10 |
| research analysis | 5 |
| experiment indexes | 5 |
| evaluation gold | 3 |
| evaluation inputs | 2 |
| generic comparisons | 2 |
| annotation working outputs | 2 |

The five index files retain their directories and bytes. Historical retrieval
outputs comprise 24 files grouped across BM25, Dense, Hybrid RRF, reranker, and
candidate-union references. Historical generation references comprise 15
files. All 573 historical trace files retain run identity and relative layout.

## Gold integrity

Retrieval gold moved byte-for-byte to
`eval-sets/retrieval/retrieval_eval.jsonl`. The authoritative generation
dataset, manifest, and v1 schema moved byte-for-byte to
`eval-sets/generation/`. The verified dataset remains exactly 31 queries and
102 independently scorable required legal points.

Draft generation datasets, annotation audits/reviews, backups, and partial
work files are under `annotation/generation/`; they are not presented as
authoritative gold. Retrieval review reports and benchmark snapshots are under
`annotation/retrieval/`.

## Challenge and HOLDOUT handling

The Phase 5 tree contains 194 Phase 5C files and explicit HOLDOUT isolation,
custodian, reviewer, adjudication, and seal records. The coherent Phase 5 tree
was moved unchanged to `experiments/reference/phase5/`, preserving its internal
layout and bytes. No challenge plaintext or candidate gold was extracted into
the general `eval-sets/challenge/` area. That semantic split is recorded as
`DEFERRED_FOR_HOLDOUT_ISOLATION` and must be performed only with the appropriate
custodian/access context. The empty canonical directories do not weaken or
claim completion of holdout publication.

## Runtime path changes

The minimal `legal_rag.paths` module now owns repository root, corpus version,
index, prompt, and new-run directories. It deliberately contains no evaluation
gold path. Dense/Hybrid/Reranker runtime loads indexes from
`experiments/indexes/`; Standard and Agentic runtimes write new default traces
to `experiments/runs/generation/traces/`. Existing corpus paths remain under
`data/versions/corpus-v0.1/`.

The path integration changes only locations. Retrieval, generation, Agentic
controller, LLM, and metric algorithms were not redesigned.

## Historical offline checks

The unified evaluator successfully read the moved reranker, Standard RAG, and
Agentic v1 artifacts in score-only mode. Historical metrics remain identical.
The moved 31-query Agentic trace set reports:

- evidence expansion: 6/31;
- answer revision: 7/31;
- citation revision: 1/31;
- success: 28;
- insufficient evidence: 2;
- incomplete answer: 1.

No LLM, retrieval model, network, or API operation was invoked.

## Stale-path scan

Active refactored runtime matches for the four obsolete canonical prefixes are
zero. Thin M3-M5 entry points, README, and migrated M1-M5 tests also use the new
layout. Remaining matches are classified as follows:

- 19 legacy/frozen/annotation/research scripts: intentional, pending M7;
- 2 Phase 5 research-specific tests: tied to frozen historical tooling;
- 8 `docs/repository_cleanup_v0/` inventories: intentional historical records;
- M6 pre/path/post manifests: required old-to-new provenance.

None is an active refactored runtime path. Legacy scripts were not edited or
deleted.

## Regression and deferred cleanup

M1 9/9, M2 10/10, M3 12/12, M4 20/20, and M5 35/35 pass after migration (86
total). The additional legacy generation-dataset suite passes 12/12.

Source-registry backup snapshots remain under
`data/source_registry/backups/`: their authority is uncertain, so the M6 rule
to keep and report uncertain files was applied. M7 may classify or relocate
them after provenance review. Empty obsolete directories and generic Python
caches are also cleanup candidates for M7; no aggressive cache or sealed-tree
cleanup occurred in M6.
