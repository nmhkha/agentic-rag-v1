# M5 unified evaluation framework migration

## Scope and result

M5 moves reusable evaluation behavior into `legal_rag.evaluation` without
changing retrieval, generation, Agentic v1, benchmark gold, stored results, or
historical traces. The legacy evaluators remain byte-identical and are
`LEGACY_PENDING_REMOVAL` until M7. No generation or retrieval model was run.

## Old to new mapping

| Legacy source | Classification | M5 destination/status |
|---|---|---|
| `evaluate_bm25.py` | core evaluation + legacy reports | retrieval formulas in `metrics.py`; generic output in `reporting.py` |
| `evaluate_dense.py` | core evaluation | shared retrieval adapter/metrics |
| `evaluate_hybrid.py` | core evaluation + experiment comparison | shared retrieval adapter/metrics; experiment comparison deferred |
| `evaluate_reranker.py` | core evaluation + experiment diagnostics | shared retrieval adapter/metrics; experiment diagnostics deferred |
| `evaluate_standard_rag.py` | core evaluation + generic report | shared generation metrics and reporting |
| `evaluate_agentic_rag.py` | core evaluation + mechanism summary | shared generation metrics; generic Agentic usage summary |
| `validate_generation_eval.py` | dataset validation | reusable pure invariants in `validation.py`; repository cross-artifact validation remains legacy |
| `analyze_candidate_coverage.py` | research-specific analysis | `RESEARCH_SPECIFIC_DEFERRED` |
| `analyze_standard_rag_failures.py` | research-specific analysis | `RESEARCH_SPECIFIC_DEFERRED` |
| `generate_human_review_report.py` | annotation tooling | left intact |

Phase 5 ablation, experiment-specific bootstrap confidence intervals,
replication safeguards, challenge-set adjudication, Phase 5C, and sealed
experiment recovery are all `RESEARCH_SPECIFIC_DEFERRED`.

## Architecture

The package enforces this flow:

```text
external pipeline executor
        -> adapter-normalized per-query records
        -> pure metrics
        -> aggregation
        -> metrics.json / per_query.csv / report.md
```

`pipelines.py` registers `bm25`, `dense`, `hybrid-rrf`, `reranker`,
`standard-rag`, and `agentic-v1`. It only normalizes stored or externally
produced records. Runtime implementations remain in `legal_rag.retrieval`,
`legal_rag.generation`, and `legal_rag.agentic.v1`. The runner accepts an
external executor for future online runs and passes it query text only.

## Historical metric definitions

Retrieval ranks are one-based and limited to the first ten results. Hit@K is
one when the first matching gold item has rank at most K. Recall@K is the set
intersection of gold chunk IDs and the first K ranked chunk IDs divided by the
number of gold chunks. Duplicate chunk IDs therefore do not increase recall,
but retain their rank positions. Article rankings are deduplicated in first-seen
order before article Hit/MRR is calculated. All retrieval aggregates are macro
averages over queries; a miss contributes zero.

Answer Completeness and Citation Completeness divide per-query supported point
counts by required point counts; a zero-point query contributes 0.0, matching
the legacy behavior. Their macro values average queries and micro values pool
point counts. Citation Correctness, Groundedness, and Unsupported Claim Rate
use the structured judge claim counts. A zero-denominator query yields `None`
and is excluded from macro. Their pooled values sum claim numerators and
denominators before division.

Macro and pooled claim metrics are deliberately distinct. For historical
Agentic v1, Groundedness macro is `0.9666666666666667`, while pooled
Groundedness is `93/97 = 0.9587628865979382`; UCR macro is
`0.03333333333333333`, while pooled UCR is `4/97 = 0.041237113402061855`.

## Score-only workflow

Stored outputs can be scored without constructing any runtime pipeline:

```bash
python scripts/run_eval.py \
  --pipeline agentic-v1 \
  --score-only \
  --results experiments/reference/generation/agentic-rag-v1/agentic_rag_eval_v1_agentic-v1.jsonl \
  --output-dir /tmp/legal-rag-m5
```

Retrieval score-only mode consumes the stored `*_per_query.csv` artifacts, or
raw ranking JSON/JSONL together with `--eval-set`. All output defaults to
`/tmp/legal-rag-m5`; protected repository artifacts are read-only inputs.
Score-only rejects an executor, guaranteeing zero LLM calls and zero retrieval
model inference by construction.

## Historical equivalence

All four stored retrieval runs reproduce their source metric JSON. The final
reranker reproduces chunk H@1/H@3/H@5 `0.516129/0.741935/0.935484`, Recall@5/10
`0.623912/0.765950`, and MRR@10 `0.666436`; article H@1/H@3/H@5 and MRR are
`0.645161/0.935484/0.967742/0.796774`. Differences below `2e-10` are caused by
the historical per-query CSV serialization at ten decimal places.

The stored Standard RAG output reproduces Answer Completeness macro
`0.6752688172043011`, micro `60/102`, Citation Completeness
`0.6752688172043011`, Citation Correctness/Groundedness
`0.9612903225806452`, UCR `0.03870967741935484`, and citation syntax `30/31`.

The stored Agentic v1 output reproduces Answer/Citation Completeness macro
`0.7236559139784946`, Answer Completeness micro `65/102`, Citation Correctness
`0.9827956989247312`, the separate macro/pooled Groundedness and UCR values
above, and citation syntax `31/31`. The verified generation gold remains 31
queries and 102 independently scorable required points.

## Tests and protection

M5 adds metric edge cases, registry/adapter tests, runner isolation tests,
generic reporting tests, validation tests, all historical equivalence checks,
gold integrity, and an AST regression check proving runtime packages do not
import evaluation/gold loaders. The 51 M1-M4 tests remain passing. Source hash
audits cover protected runtime modules, legacy evaluators, and historical data.

## Limitations

M5 does not reorganize data, delete legacy scripts, rerun a model, perform a
new semantic judge pass, migrate research-specific experiments, or introduce
Agentic v2. Online execution remains an explicit library integration point;
the M5 CLI intentionally exposes only safe score-only operation.
