# Phase 5A — Controlled Ablation Experimental Specification v0

Status: **FROZEN**. Scope: **DESIGN ONLY**. Execution started: **false**.
The companion `phase5a_ablation_manifest_v0.json` supplies exact SHA-256 values,
fully resolved variant configurations, query order, and static validation evidence.
No production, retrieval, generation, evaluation, API request, benchmark, prompt
tuning, or optimization is authorized or performed by this specification.

## 1. Question, references, and limits

Which frozen Agentic RAG v1 intervention contributes observable quality improvement
over an otherwise matched Agentic execution, and what production work does it cost?
This is controlled benchmark evidence and post-hoc explanatory analysis on the
already frozen final evaluation set, not universal proof of superiority.

Historical observations, copied from existing artifacts rather than reevaluated:

| Reference | Macro Answer Completeness | Supported points | Micro AC |
|---|---:|---:|---:|
| R0 — frozen Standard RAG | 0.6752688172043011 | 60/102 | 0.5882352941176471 |
| R1 — frozen Agentic RAG v1 | 0.7236559139784946 | 65/102 | 0.6372549019607843 |

Phase 4E reported six gained points, one lost point, net +5; expansion in six
queries (five unchanged final Top-5, one changed, zero annotated supporting chunks
added to final Top-5); answer revision in seven queries (eval002 strongest
trace-consistent helpful case); citation revision in one; semantic citation check
in zero; and 17 potential internal complete=true / benchmark-incomplete disagreements.
These observations motivate H1–H3 only. They must not enter production decisions,
query selection, prompts, thresholds, budgets, or model selection.

Never rerun R0. Never replace, overwrite, or relabel R1 as the new control. There
is no best-of-N selection, selective regression rerun, changed query, changed gold,
larger Top-K, corpus edit, retrieval/model change, fallback LLM, or tuning on these
31 final-benchmark queries. Preserve hypotheses even if results contradict them.

## 2. Authoritative repository mapping and provenance

All paths below are relative to the repository root. The JSON manifest's
`frozen_artifacts` identifies roles and hashes; `source_integrity.before_sha256`
also inventories all 246 preexisting project files in the inspection scope.

| Role | Authoritative current path |
|---|---|
| Corpus used at runtime | `data/versions/corpus-v0.1/chunks.jsonl` |
| Verified final generation dataset | `data/evaluation/generation/generation_eval_v1_verified.json` |
| Verification manifest | `data/evaluation/generation/generation_eval_v1_verified_manifest.json` |
| Frozen retrieval gold | `data/evaluation/retrieval_eval.jsonl` |
| Generation prompt | `prompts/legal_rag_v0.txt` |
| Dense index | `data/indexes/dense-jina-v3-v0/{index_manifest.json,chunk_ids.json,embeddings.npy}` |
| Historical reranker manifest | `data/indexes/bge-reranker-v2-m3-v0/reranker_manifest.json` |
| R0 results / metrics / manifest | `data/evaluation/generation/standard_rag_{eval,metrics,manifest}_v0.{jsonl,json,json}` (respectively) |
| R0 report | `data/evaluation/generation/reports/standard_rag_eval_v0.md` |
| R1 results | `data/evaluation/generation/agentic_rag_eval_v1_agentic-v1.jsonl` |
| R1 metrics and embedded manifest | `data/evaluation/generation/agentic_rag_metrics_v1_agentic-v1.json`, JSON pointer `/manifest` |
| R1 report | `data/evaluation/generation/reports/agentic_rag_eval_v1_agentic-v1.md` |
| R1 31 individual traces | `data/rag/traces/agentic-rag-v1/agentic-v1/<query_id>.json` |
| Phase 4E context | `data/evaluation/generation/agentic_trace_analysis_v0.jsonl`, `agentic_trace_analysis_metrics_v0.json`, and `reports/agentic_trace_analysis_v0.md` in that generation directory |
| Phase 4A labels (analysis only) | `data/evaluation/generation/failure_analysis_{points,queries,metrics}_v0.{jsonl,json,json}` (respectively) |
| Frozen controller | `scripts/agentic_rag.py` |
| Shared evaluator methodology | `scripts/evaluate_standard_rag.py`: `judge_prompt`, `parse_judge`, `point_audit` |
| Current Agentic evaluator adapter | `scripts/evaluate_agentic_rag.py`: `evaluate_record` |

`generation_eval_v1.json` is the draft, not the verified execution dataset.
`data/processed/chunks.jsonl` is not the authoritative runtime corpus. R1 has no
separate manifest file; use its embedded manifest. `FINAL_DEPTH=10` in the old
reranker benchmark is not the RAG context size: `DEFAULT_TOP_K=5` in
`retrieval_pipeline.py` is authoritative. Hybrid RRF artifacts are historical;
production uses union/deduplication with no fusion.

Current bytes match historical R0/R1 corpus, dataset, retrieval-gold, prompt, and
result hashes. All 113 files recorded by Phase 4E still match its after-hashes.
There is no usable Git working tree or historical complete source commit. Current
runtime/evaluator bytes are pinned now; this is not proof of the exact historical
execution environment. Model weights outside the project and provider backend
identity are not historically byte-pinned here. Record those limits for R1–R2.

## 3. Frozen matrix, configuration, and order

| ID | Variant ID | Expansion | Answer revision | Citation revision | Role |
|---|---|---:|---:|---:|---|
| R2 | `full-agentic-replication` | true | true | true | Mandatory matched full control |
| A1 | `agentic-v1-no-answer-revision` | true | false | true | Mandatory single capability contrast |
| A2 | `agentic-v1-no-evidence-expansion` | false | true | true | Mandatory single capability contrast |
| A3 | `agentic-v1-no-citation-revision` | true | true | false | OPTIONAL EXPLORATORY ABLATION |
| A4 | `agentic-v1-no-substantive-interventions` | false | false | false | Optional combined ablation |

One complete 31-query production pass each, sequentially R2, A1, A2. Within each
variant use the verified dataset item order, recorded as `query_order` in JSON.
No parallel production variants or per-query variant interleaving. Complete the
mandatory variants and their evaluation before considering optional A3 then A4;
optional runs require a later budget decision and never displace primary work.
Freeze all three primary configurations and execution environment before R2.
Generate and seal all three primary output sets before semantic evaluation or
quality inspection. Do not redesign A2 from R2/A1 outputs or intermediate metrics.

Common configuration:

- Base version `agentic-rag-v1`; corpus `corpus-v0.1` (737 chunks).
- `BM25-simple-v0@20` plus `dense-jina-v3-v0@20`; union/deduplicate by `chunk_id`, fusion null.
- Dense `jinaai/jina-embeddings-v3`, revision `ab036b023d30b4d1138c4c3bfa9f0c445ab455d6`;
  `retrieval.query`, existing normalized float32 1024-dimensional index.
- Reranker `BAAI/bge-reranker-v2-m3`, revision `953dc6f6f85a1b2dbfca4c34a2796e7dde08d41e`;
  max length 8192; score descending, then chunk_id lexical ascending.
- Final Top-K 5, original prompt `legal-rag-prompt-v0` plus unchanged controller
  prompt functions pinned by the controller source hash.
- Production and existing semantic evaluator model `gemini-3.5-flash-lite`;
  existing OpenAI-compatible client, temperature 0, JSON-object response format,
  one user message, timeout 120 seconds. No new seed, decoding parameter, system
  prompt, semantic judge, or max-token override.
- Code budgets remain `MAX_RETRIEVAL_EXPANSIONS=1`, `MAX_SUB_QUERIES=3`,
  `MAX_ANSWER_REVISIONS=1`, `MAX_CITATION_REVISIONS=1`, `MAX_LLM_CALLS=6` in every
  variant. Disable capabilities with existing booleans, not edited constants.
  Thus nominal manifest budgets remain equal even when effective allowed use is zero.
- Use CPU/float32, dense batch size 4 and reranker batch size 1, no batch-size
  override, matching recorded historical CPU settings and current CPU defaults.
  Pin one Python/dependency environment for all new variants before R2; record
  actual versions, executable, device, endpoint identifier, and resolved revisions
  in an execution-environment manifest. Never serialize credentials. If the
  historical endpoint is unavailable, stop preflight rather than silently substitute.

The reranker constructor currently leaves `revision=None`; a manifest claim alone
does not enforce its revision. Phase 5B must load the existing pipeline from a
verified local cache with hub offline mode and check actual dense and reranker
resolved commits (including tokenizer snapshot) before any query or LLM call.
Mismatch, unavailable snapshot, unexpected device/configuration, or hash drift
fails preflight. Restore the specified snapshot before execution; do not change
the expected revision. This is an environment/provenance guard, not a new retriever.

Each `variant_manifests[ID]` in JSON is a complete immutable design configuration
with the required corpus/dataset/prompt hashes, retrieval settings, budgets, flags,
and a common creation timestamp. In Phase 5B materialize those exact objects as
separate variant manifests with exclusive creation. Their canonical hashes are
already declared; keep run-time metadata in separate run manifests.

For comparison, recursively compare every variant field after excluding ONLY
`variant_id`. Common `created_at` must also match. Require the exact difference set:

- R2–A1: `ablation_flags.enable_answer_revision`, true → false.
- R2–A2: `ablation_flags.enable_expansion`, true → false.
- R2–A3: `ablation_flags.enable_citation_revision`, true → false (optional).
- R2–A4: all three capability flags, true → false (optional).

Reject missing or extra keys, type changes (including true versus 1), unexpected
values, extra differences, and no-op ablations. Do not wildcard-ignore hashes,
budgets, or metadata. Validate runtime-resolved configuration against its manifest
as well. Canonical configuration hash: SHA-256 of UTF-8 JSON with sorted keys,
`ensure_ascii=False`, separators `(',', ':')`, no trailing newline.

## 4. State-machine mapping and minimal Phase 5B mechanism

Use a new thin experiment wrapper around the unchanged
`AgenticRAGController(pipeline, client, enable_expansion=..., enable_answer_revision=...,
enable_citation_revision=...)`. Keep all default booleans true for R2. Do not edit,
copy/rewrite, subclass to replace decisions, or monkeypatch frozen controller logic.
The existing evaluation CLI exposes `--no-expansion`, `--no-answer-revision`, and
`--no-citation-revision`; these confirm the mapping but that CLI is not the Phase
5B execution entry point. It reads gold in the same process, mixes generation and
judging, writes outside Phase 5, and `--resume` can regenerate production errors.

Actual unchanged sequence:

1. Initial audited BM25@20 ∪ dense@20 candidate retrieval/reranking; retain all
   candidate ranks in trace but only initial Top-5 as evidence.
2. Coverage LLM check always runs. Expansion eligibility is `not sufficient AND
   nonempty missing_aspects AND MAX_RETRIEVAL_EXPANSIONS > 0`.
3. If enabled and eligible, form up to three subqueries as `aspect + ' ' + original
   query`, retrieve each complete candidate pool, deduplicate, and rerank initial
   Top-5 plus expanded candidates to Top-5. This is the existing expansion pool;
   do not silently include the rest of the initial candidate pool in the merge.
4. Generate using the frozen baseline prompt, then always run completeness check.
5. If incomplete, answer revision enabled, and revision count below one, revise
   once and run the existing post-revision completeness check. Both calls are part
   of the revision branch; A1 removes that branch including its dependent recheck.
   Retaining the initial completeness check is mandatory; adding a dummy recheck
   to match call counts would change the experiment.
6. Deterministic citation check; optionally repair invalid citations and recheck.
   Preserve the original low-overlap semantic citation gate and six-call budget.
   Semantic checking can repair within the same call only if citation revision is
   enabled. It remains available when revision is disabled with `revised_answer=null`.
7. Preserve current status precedence: citation_check_failed, insufficient_evidence,
   incomplete_answer, or success, as implemented; do not normalize status to success.
   Preserve exception handling with `record_execution_error` and partial trace.

A1 keeps the draft as the substantive answer on failed completeness, then follows
normal citation validation/optional repair. Citation repair may still alter answer
text under the existing prompt. Do not force final byte equality to the draft or
silently disable citation repair. A2 records missing aspects, creates no subqueries,
performs no expansion retrieval or merge-rerank, retains initial Top-5 exactly, and
keeps downstream revision/citation behavior unchanged. Freed call capacity may
affect downstream semantic eligibility; log this as a consequence of the removed
branch, without changing `MAX_LLM_CALLS` or adding compensatory work.

A3 retains deterministic and gated semantic Citation Check; it disables both
syntactic citation repair and semantic in-call repair, retains the current answer,
and records validator failure/status. The existing semantic prompt's
`allow_revision=False` wording is the prescribed capability switch, not prompt
tuning. A4 disables all three interventions while keeping all checks and ordinary
generation. It estimates controller/check overhead versus substantive interventions;
it does not isolate any one mechanism or establish additive effects.

### Observability contract (wrapper-only, future implementation)

Existing traces lack explicit would-have-triggered/blocked flags, overwrite the
first completeness result after revision, and omit raw LLM responses. Use a
pass-through client/pipeline observer for every variant to retain stage-ordered
request/response/error events and input/output hashes without extra calls, altered
responses, extra parsing in the control path, or decisions based on logs. Save the
unmodified `trace_for_state` payload plus a separate observer sidecar. Preserve
the first completeness check even in R2; derive metadata after the call sequence.

At the original decision boundary, define:

- `answer_revision_would_have_triggered`: first successfully parsed completeness
  check is incomplete and the pre-revision count is below nominal budget one.
- `answer_revision_blocked_by_ablation`: the preceding condition AND
  `enable_answer_revision == false`.
- `expansion_would_have_triggered`: successfully parsed coverage is insufficient,
  its cleaned/truncated missing-aspects list is nonempty, and nominal expansion
  budget is positive.
- `expansion_blocked_by_ablation`: the preceding condition AND `enable_expansion == false`.

These mean branch eligibility for that run, not a stochastic counterfactual about
what a different run would answer. Insufficient coverage with an empty missing
list is not expansion-eligible in v1: record `missing_aspects_empty` and false,
not true. An unreached decision or parse/transport error yields null plus reason,
not false. Record eligibility, attempted intervention (existing *_used flags),
completed revision counts, budget exhaustion, and observed errors separately.
An attempted revision that fails is not a successful intervention. Logs must never
read gold. In A1/A2 successful runs these predicates can be derived from retained
checks, but the observer ensures common logging and preserves decision history.

## 5. Leakage boundary and tests to implement before Phase 5B

The design/audit process may read gold. Production may not. A trusted offline
preparation step on the evaluator side validates the frozen dataset and projects
only `{query_id, query}` in the declared order into a new Phase 5 input file.
Its canonical expected hash is recorded in JSON. Preserve query text exactly;
existing controller `.strip()` remains unchanged (verified queries have no edge
whitespace). The production parent passes only the string query to `run`, plus
an opaque run ID and fresh state. Do not pass entire dataset records or manifests
containing reference results/outcome labels to the controller.

Run production in a separate process with a filesystem allowlist: frozen runtime
source, corpus, dense index, approved model caches/dependencies, query-only input,
and that variant's Phase 5 output directory. Deny the evaluation tree (except the
query-only input if placed there), all historical R0/R1 outputs/traces, Phase 4A/4E
artifacts, verified/draft gold, reference answers, required-point labels, and
retrieval-eval gold. Do not inherit these through memory, environment, handles,
stdin, or imports. The full design manifest belongs to orchestration/analysis;
production receives its minimal resolved configuration only. Hash preflight reads
of gold occur in the trusted parent, never in the production process.

Before real execution Phase 5B must implement and pass these synthetic/offline
tests, with transport blocked and no final-benchmark prompts:

| Test | Required assertion |
|---|---|
| L1 source/import boundary | Controller plus local production import closure contains no evaluator imports or prohibited artifact paths/label identifiers; scan future wrapper too. Ordinary legal corpus `point_id` is not benchmark `required_point_ids`. |
| L2 projection schema | Exactly query_id/query, 31 unique IDs, exact ordered query-byte hashes; reject extra/nested gold fields. Test schema rejection with synthetic records. |
| L3 denied reads | Filesystem guards reject verified dataset, retrieval gold, Phase 4A/4E and historical result paths, including resolved symlink aliases; instrument all production reads/imports. |
| L4 sentinel flow | Synthetic gold with unique sentinel content cannot reach runtime inputs, prompts, state, or production logs; fake client/pipeline receive query/evidence only. |
| L5 reference separation | Production can finish fake runs with gold unavailable; evaluator joins saved output with gold only after production is sealed. |
| B1 A1 | Fake incomplete first check still occurs, answer_revision and dependent recheck absent, draft preserved until citation stage, citation repair still available, blocked predicate correct. |
| B2 A2 | Fake insufficient coverage with nonempty aspects still checked/logged; exactly one retrieval, no subqueries/merge rerank, final Top-5 equals initial, answer revision still available. Include empty-aspects boundary. |
| B3 control parity | Wrapper R2 vs direct frozen controller on identical synthetic stage responses/evidence: same prompts, calls, evidence, answer, transitions, and statuses after excluding observer metadata/run IDs/time. |
| B4 no compensation/errors | Unreached decisions are null; six-call ceiling preserved; failed calls retained; no new fallback, retries, retrieval, or formatting decisions. |
| B5 optional capability | If A3/A4 later enabled, checks remain active and both citation-repair paths are disabled; gate/budget behavior unchanged. |

Phase 5A runs only static source/import and specification checks. L2–L5 and B1–B5
are acceptance requirements, **not claims of executed tests or enforced process
isolation today**. Existing `test_production_module_has_no_evaluation_leakage_markers`
checks only the controller source; it is insufficient as a runtime security boundary.
No runtime tests, fake controller runs, or evaluation functions are executed in 5A.

## 6. One-run, failures, retries, and preservation

Exactly one production attempt per query per new variant; one planned pass of 31
queries, including explicit records for failures. Never repeat a completed answer
or a failed-looking/regressing query to improve quality. Durable attempt ledger
must mark started before the controller call and seal completion or error afterward.
After interruption, resume only never-started queries. An ambiguous in-flight
attempt becomes a reported technical error; do not regenerate it. Existing
`--resume` does not enforce this policy and must not be used directly.

Repository reality: `OpenAICompatibleClient.generate` performs one HTTP request
with 120-second timeout and **zero automatic production retries**. Preserve this
policy across R2/A1/A2. Do not invent exponential backoff, semantic retries, or a
production three-attempt policy. Log any observable transport attempts and errors;
provider-internal retries, if unobservable, are unknown rather than asserted zero.
Logical failed LLM calls are included in the existing state ledger. Retrieval
calls are logged by the controller only after success; the pass-through observer
must separately record attempted/failed retrieval calls, including setup errors.

Evaluation reuses `evaluate_record` and its existing maximum three attempts on
judge exceptions, including malformed responses. Use the same prompt unchanged,
accept the first valid parsed response, retain every attempt/error in the evaluator
ledger, and never regenerate production. Three attempts is a total across restart,
not three more on every resume. Exhaustion is an evaluation error. No rejudging
valid outputs to pick favorable scores. This reliability distinction is preserved
even though historical Standard RAG had a single judge attempt.

In Phase 5B use exclusive-create output paths and append/seal ledgers; refuse
collisions. Never write via the existing default Phase 4 output paths. Proposed
per-variant layout (create none of these run/result files in Phase 5A):

```text
data/rag/traces/phase5/<variant_id>/
  production_outputs.jsonl             # 31 query output/error envelopes, no gold
  <query_id>.json                      # 31 original controller traces, partial on error
  observations/<query_id>.json         # decision/attempt observer sidecars, no gold
  production_attempts.jsonl
data/evaluation/generation/phase5/<variant_id>/
  variant_manifest.json                # exact predeclared object, created before R2
  run_manifest.json                    # sealed run metadata, environment/code/input/output hashes
  evaluation.jsonl                     # 31 joined records after production sealing
  evaluation_attempts.jsonl
  metrics.json
data/evaluation/generation/phase5/
  query_inputs_v0.json                 # trusted projection, created only in 5B
  execution_environment_v0.json        # common preflight lock, created only in 5B
  replication_R1_R2.json
  contrast_R2_A1.json
  contrast_R2_A2.json
  phase5b_report_v0.md
```

Run manifests must include design/config/environment/source hashes, query order
and input hash, start/end UTC, variant/run IDs, production/evaluation attempt
counts, retrieval and LLM counts, errors with query/stage identity, artifact paths
and hashes, completion/seal status, and transport observability. Retain raw
production responses through the observer, with API keys/auth headers excluded.
31 trace envelopes is required even on error; only an error-free trace may be
called a complete successful production trace. Preserve partial traces explicitly.

## 7. Frozen evaluation and missing-data policy

Use the existing frozen shared `judge_prompt`, `parse_judge`, `point_audit`,
`citation_validator.validate_citations`, and Agentic `evaluate_record` methodology.
Hash these source files, controller prompts, and formatter dependencies; do not
rewrite judge wording/parser/point semantics or introduce an extra semantic audit.
Production completeness checks are not the external Answer Completeness metric.

For query q with n_q required points, s_q supported points, and c_q supported
points with supporting answer citations:

- Answer Completeness (primary): AC_q = s_q/n_q; macro = sum(AC_q)/31;
  micro = sum(s_q)/102; always display supported points /102.
- Citation Completeness: CC_q = c_q/n_q; macro mean, pooled micro sum(c_q)/102.
- Citation Correctness: correctly_cited_claim_count / cited_claim_count.
- Groundedness: grounded_claim_count / claim_count.
- Unsupported Claim Rate (UCR): unsupported_claim_count / claim_count (lower better).
- Citation syntax validity: deterministic `citation_valid`; valid count, eligible
  count, and rate, separate from semantic citation alignment/final status.

For claim metrics, macro is mean of defined per-query ratios; zero denominator
is null, not zero. Pooled micro uses sums of matching numerator and denominator
over the same eligible judged records; publish every raw count and denominator.
Do not infer groundedness as 1-UCR if raw counts do not reconcile; flag anomalies
without repairing judge labels or adding calls. R0 claim counts are stored as
`judge_<name>` fields; R1/new Agentic counts are under `judge.<name>`.
Use saved supported_point_ids/required_point_ids to recover R0 AC per query;
the original Agentic comparison report omits AC and micro AC, so extend only
Phase 5 analysis outputs. Never edit historical summaries to fill omissions.

Preserve evaluator error semantics: production errors have AC/CC=0 in per-query
records; judge exhaustion has null quality metrics. The existing Agentic aggregate
filters to successful judged records, so retain it as a labeled diagnostic with
its actual denominator, **not** as an unlabeled 31-query primary score. A complete
primary comparison, 102-point transition table, and 31-pair CI require 31 successful
production outputs and valid judgments in each compared run. If this gate fails,
mark the primary contrast insufficient evidence/incomplete; do not impute judge
failures, reduce 31/102 silently, or claim the complete primary experiment passed.
Report available-case metrics with explicit IDs/counts and known supported /102
as an incomplete observed-coverage count (not a definitive micro estimate), plus
separate generation and evaluator error counts. Keep all 31 paired rows with nulls
as needed. Cost summaries include every attempted query and partial trace.

## 8. Paired contrasts, trigger strata, and replication

Report R1 versus R2 **before** interpreting R2 versus A1 and R2 versus A2. R2 is
one same-configuration replication, not a replacement frozen benchmark. Report
R2−R1 macro/micro AC, gained/lost required-point identities, all secondary metrics
including pooled claims, and every per-query change. Call this observed replication
variation, not formal variance estimation, and do not subtract it to manufacture
a corrected causal estimate.

For each primary contrast define the reported quality delta as **R2 − ablation**
for every raw metric. Positive AC favors R2; positive raw UCR favors the ablation.
Also report oriented safety deltas with the UCR sign reversed when interpreting
tradeoffs, explicitly labeled. Query pairs use exact query_id and query text;
reject duplicates, missing/extra IDs, changed text, or changed point universes.

For universe U = all 102 `(query_id, point_id)` tuples, R2 support S_R and ablation
support S_A, output sorted identities and counts:

- both supported = S_R ∩ S_A;
- only R2 = S_R − S_A = points lost by ablation;
- only ablation = S_A − S_R = points gained by ablation;
- neither = U − (S_R ∪ S_A).

All four sets partition U. Net ablation change = gained − lost; R2 contribution
in points = lost − gained. Name both directions; never use local P1/P2 as global
IDs. Use analogous gained/lost tables for R2 relative to R1.

Each paired row retains both variants' AC, CC, citation correctness, groundedness,
UCR, syntax validity, all raw deltas, R2 intervention-used flag, ablation eligibility
and blocked flag, both final statuses/errors, retrieval/production-LLM counts,
and trace links. Summarize A1 separately for `R2.revision_used=true/false`; A2 for
`R2.expansion_used=true/false`. Preserve failed/unreached trigger status separately.
Report full 31-query aggregate and both strata, including sizes, required-point
denominators, quality deltas, point transitions, and costs. The R2-triggered stratum
is the primary behavior-specific view; membership is never chosen from A1/A2
outcomes. Include a cross-tab of R2-used versus ablation-blocked, since stochastic
check decisions can differ across runs. Differences in R2 non-triggered queries
are background run variation/downstream differences, not direct evidence that
removing an unused intervention caused them. Trigger strata are post-treatment
descriptive subsets, not randomized causal subgroups.

## 9. Deterministic statistics (Phase 5B local analysis only)

For each complete 31-query primary contrast compute mean and median per-query AC
delta, counts of queries better under R2 / tied / better under ablation, and net
required-point difference. For the ablation's improved/equal/worsened counts,
reverse the first and last labels explicitly. Determine AC signs/ties from exact
supported-count ratios (integer cross-products or rational arithmetic); do not
introduce a tunable practical-significance threshold.

Predeclare paired query-level percentile bootstrap: 10,000 resamples, seed
20260906, sample size 31 with replacement. Use local Python `random.Random(seed)`;
reinitialize independently to this seed for R2–A1 and R2–A2. In each iteration draw
31 indices with `rng.randrange(31)` in the manifest query order, carry each whole
pair together, and compute mean AC difference. Sort the 10,000 means; report
2.5th and 97.5th percentiles using linear interpolation at `(N-1)*p` (floor index
plus fractional interpolation). Record Python version. Do not resample points,
claims, variants independently, or individual API attempts. No bootstrap is run
in 5A. Subset summaries are descriptive; this protocol's primary CI is full-set
macro AC, not an undeclared subset significance search. Report a simple paired
sign summary, no new p-value test or significance claim.

One replication cannot quantify all stochastic generation/judge variation. To
make the caution reproducible, predeclare an attribution-limited flag when both
absolute ablation macro AC difference and absolute net point difference are no
larger than their R1–R2 counterparts (and at least one replication difference is
nonzero). Also disclose gross replication churn (gained + lost), even with net
zero; flag churn at least as large as a nonzero contrast churn as additional
attribution weakness. These are conservative reporting rules, not tuned system
thresholds, formal noise bounds, or a variance-adjusted test.

## 10. Interpretation and frozen hypotheses

Assign a label with explicit numerical evidence and limitations, using this
predeclared precedence so conflicting metrics cannot be hidden:

1. **Insufficient evidence**: incomplete primary data, at most one R2-triggered
   query, or nonzero effects dominated by the replication flags above. Explain
   whether too few triggers, errors, or run variation limits attribution.
2. **Mixed evidence**: AC and safety/groundedness move in conflicting directions,
   macro and pooled safety directions conflict, macro AC and net points conflict,
   or full-set and triggered-stratum conclusions disagree. Any nonzero directional
   conflict must be disclosed; this is descriptive, not a significance test.
3. **Supported contribution on this benchmark**: R2 macro AC is higher, lost
   points exceed gained points, triggered stratum is consistent, and the preceding
   caveats do not dominate. Always display CI, costs, and one-run limitations.
4. **Ablation performs better**: removing the capability improves completeness
   and/or safety without a conflicting deterioration, and costs no more in either
   production call type and strictly less in at least one. Report uncertainty.
5. **No observed contribution**: removal does not reduce completeness/coverage
   beyond observed replication variation, with no conflicting quality direction;
   exact quality ties with enough triggers also fall here. Remaining ambiguous
   cases are **Mixed evidence** or **Insufficient evidence**, with the reason.

H1 — Answer Revision: Removing Answer Revision is expected to reduce Answer
Completeness on at least some revision-triggered queries, particularly
generation-omission cases. This is a hypothesis, not a guaranteed result.

H2 — Evidence Expansion: Removing Evidence Expansion may have limited impact
because most observed expansions did not change final Top-5 evidence; however a
controlled run is required before concluding the mechanism is unnecessary.

H3 — Citation Revision: Current benchmark evidence is insufficient for a strong
hypothesis because Citation Revision triggered only once. Citation-only profile
has zero queries and semantic citation checks were 0/31; A3 is exploratory.

If A1 ≈ R2: “No clear aggregate contribution was demonstrated in this 31-query
ablation,” never “Answer Revision never helps.” If A2 ≈ or > R2: “Evidence
Expansion v1 does not show clear value on this benchmark relative to its retrieval
cost,” not a general claim about all evidence expansion methods. If R1 and R2
differ materially: “Single-run generation/evaluation variation limits attribution
strength.” Do not rewrite hypotheses or repeat runs after seeing these outcomes.

## 11. Production efficiency

For R2 and each new variant report total, mean/query, median/query, and maximum/query
retrieval calls and production LLM calls. Include all 31 attempted query envelopes,
errors, stage counts, and both successful and failed attempts. Separate the original
trace's successful retrieval count from the observer's attempt count on failure.
Count one hybrid pipeline request as one logical retrieval call (BM25 and dense
are components); count expansion merge-rerank operations separately. Do not hide
that additional reranking work inside or omit it from the accompanying cost report.

LLM logical calls include coverage, generation, all completeness checks, answer
repair, citation repair, and gated semantic alignment; exclude every evaluator
attempt. Transport requests/retries are separate observations, not independent
samples. Report unobserved transport/token/cost data as unavailable.

For each cost type C and reference B in R0 and R2, report C_variant − C_B,
C_variant/C_B, and 100*(C_variant/C_B − 1)% overhead; report savings versus R2
as C_R2 − C_variant and 100*(1 − C_variant/C_R2)%. A zero reference denominator
yields null. Pair savings with AC macro/micro changes and net points.

R0 has no complete production-call ledger in its evaluation JSONL. Use the
explicitly labeled **configured logical** baseline: one retrieval and one answer
LLM call/query, totals 31/31, mean/median/max 1, supported by `run_rag` and the
31 successful frozen output records. Do not claim measured HTTP totals. Existing
Phase 4E R1 trace counts are 38 retrieval and 108 production LLM calls; retain
them as historical context. No monetary estimate without real token/cost data.

## 12. Freeze validation and stop condition

Phase 5A PASS means the two design artifacts exist and agree, historical hashes
match, proposed recursive config diffs pass including negative controls, static
production import/leakage checks pass, all original inventoried bytes are unchanged,
and the only new repository files are this spec and its JSON manifest. Validation
uses Python standard-library parsing, AST inspection, and hashing only. It neither
imports production/evaluator modules nor executes retrieval, generation, evaluation,
bootstrap, network tools, package installation, or test suites.

The JSON `validation` distinguishes completed static checks from future Phase 5B
acceptance tests. The spec's exact byte hash is stored in the companion manifest;
the manifest's per-variant canonical hashes detect configuration drift. Before
Phase 5B, seal the exact design-file byte hashes into the run lock with exclusive
creation. Immutability here is an append-only experiment rule plus hash guards,
not a claim of filesystem write protection or cryptographic signed provenance.
Any design amendment must use a new version before execution and must not be
motivated by new benchmark outcomes.

Ready for Phase 5B means **ready to implement the specified wrapper and preflight**,
not an already implemented/validated production runner or verified provider access.
All future isolation, instrumentation, parity, revision, and environment gates must
pass before the first real query. Source artifacts modified: NONE. Network/API
calls: 0. New retrieval/generation/evaluation: NO. After these two design artifacts
are created and statically validated, **STOP**. Do not implement variants or start
Phase 5B automatically.
