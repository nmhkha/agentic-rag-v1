# M2 retrieval migration

## Scope and legacy mapping

M2 migrates only reusable retrieval and dense-index construction behavior into
`src/legal_rag/retrieval`. All source scripts remain byte-identical and are
`LEGACY_PENDING_REMOVAL`.

| Legacy source | Package target | Status |
| --- | --- | --- |
| `scripts/bm25_baseline.py` | `retrieval/sparse.py` | `LEGACY_PENDING_REMOVAL` |
| `scripts/dense_baseline.py` | `retrieval/dense.py` | `LEGACY_PENDING_REMOVAL` |
| `scripts/build_dense_index.py` | `retrieval/dense.py`, `scripts/build_index.py` | `LEGACY_PENDING_REMOVAL` |
| `scripts/hybrid_rrf.py` | `retrieval/fusion.py` | `LEGACY_PENDING_REMOVAL` |
| `scripts/reranker_baseline.py` | `retrieval/reranker.py` | `LEGACY_PENDING_REMOVAL` |
| `scripts/retrieval_pipeline.py` | `retrieval/pipeline.py` | `LEGACY_PENDING_REMOVAL` |

The four `evaluate_{bm25,dense,hybrid,reranker}.py` scripts were inspected but
not migrated. Their query loading, metric aggregation, failure reports, and
benchmark artifact writes belong to M5.

## Frozen selected architecture

The canonical `RetrievalPipeline` retains:

```text
BM25-simple-v0 Top-20 + dense-jina-v3-v0 Top-20
    -> insertion-ordered union/deduplication by chunk_id
    -> BAAI/bge-reranker-v2-m3
    -> reranker score descending, chunk_id lexical tie-break
    -> Top-5 Evidence objects
```

Component ranks and scores are retained as metadata but never used as fusion
signals in the selected path. RRF exists as historical experimental retrieval,
but is NOT the final selected production retrieval path.

## Public API

Stable exports from `legal_rag.retrieval` are:

- `BM25Retriever`, `tokenize`, and `read_chunks`;
- `DenseRetriever`, `encode`, and `build_dense_index`;
- `fuse_rankings` and `HybridRRFRetriever` for the historical experiment;
- `union_candidates`, `rank_candidates`, `BGEReranker`, and
  `RerankerRetriever`;
- `Evidence`, `RetrievalPipeline`, `retrieve`, and `retrieval_config`.

Imports do not parse arguments, load models, create indexes, execute retrieval,
write files, or exit. Model loading occurs only when a concrete dense or
reranker instance is constructed. `Evidence.to_dict()` preserves the legacy
fields plus the existing `source_url`, `clause_id`, and `point_id`
compatibility aliases required by runtime consumers and traces.

## Model and index provenance

The copied, read-only index assets moved in M6 to `experiments/indexes`.

| Component | Model/revision | Frozen asset |
| --- | --- | --- |
| Dense | `jinaai/jina-embeddings-v3@ab036b023d30b4d1138c4c3bfa9f0c445ab455d6` | `dense-jina-v3-v0` |
| Reranker | `BAAI/bge-reranker-v2-m3@953dc6f6f85a1b2dbfca4c34a2796e7dde08d41e` | `bge-reranker-v2-m3-v0/reranker_manifest.json` |

The revisions were read from the frozen manifests, not inferred from the M2
prompt. Dense embeddings remain 737 x 1024 finite float32, L2-normalized,
aligned exactly to `chunk_ids.json`, and queried using `retrieval.query`.
Passages retain `retrieval.passage`. Similarity remains normalized dot product
with stable descending NumPy sorting.

The reranker retains deterministic torch settings, CPU float32 behavior,
batch size 1 on CPU, paired query/passage tokenization, max length 8192, raw
logit extraction, descending score order, and lexical chunk-ID tie behavior.

## Dense build CLI

`scripts/build_index.py --method dense` is the only persistent-index path.
It delegates to `build_dense_index`; BM25 and the reranker do not receive fake
index-building modes. The CLI requires an explicit output directory so a caller
can use `/tmp` without touching the authoritative index. M2 did not rebuild the
frozen index.

## Tests

Ten offline retrieval tests cover:

- exact legacy BM25 normalization, tokenization, scores, ranks, Top-K, and ties;
- frozen dense manifest loading, chunk alignment, normalized-index validation,
  similarity order, stable ties, and Top-K;
- RRF constant/math, duplicates, source-rank ordering, and final lexical ties;
- candidate union metadata and pure reranker score/tie/Top-K ordering;
- BM25 + dense union -> reranker -> Top-K orchestration and all Evidence
  compatibility fields;
- explicit confirmation that `retrieval_config()["fusion"]` is `None`.

The 9 M1 ingestion tests also continue to pass.

## Frozen 31-query equivalence

All 31 verified queries (now under `eval-sets/retrieval/retrieval_eval.jsonl`) were run in
offline mode. Temporary details are under `/tmp/legal-rag-m2/`; no official
evaluation result was regenerated or changed.

| Layer | Result |
| --- | --- |
| BM25 Top-20 IDs/ranks/scores | 31/31 exact |
| Dense Top-20 IDs/ranks/scores | 31/31 exact |
| Union candidate IDs/order | 31/31 exact |
| Reranker Top-5 IDs/order/scores | 31/31 exact |

Holding both large models in one process exceeded the available memory and the
OS killed the initial smoke query after both models loaded. Equivalence was
therefore executed in separate offline processes per layer. Dense old and new
were each run over all 31 queries. Candidate unions were independently produced
by old and new implementations. The reranker was then loaded alone with the
frozen revision and scored every union using the frozen batch size; the legacy
and migrated ranking paths received the same model logits. The old/new
`score()` instruction bytecode and referenced operations were also verified
identical. This avoids simultaneous model residency without changing any
retrieval calculation or weakening the output comparison.

No network/API call, external model download, index overwrite, benchmark
metric regeneration, or write beneath `data/evaluation/results` occurred.

## Protected scope

M1 ingestion behavior, Standard RAG, generation, Agentic RAG v1, evaluation,
benchmark gold, challenge benchmark, historical metrics/traces, and Phase 5
artifacts were not changed. Frozen original and working-copy legacy retrieval
hashes were verified after implementation.
