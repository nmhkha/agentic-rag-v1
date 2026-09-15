# Phase 5B.2-E — Frozen production semantic evaluation

**Status: INCOMPLETE.** Production reruns: 0; production LLM calls during this phase: 0.

Recovery gate R2/A1/A2: PASS against external manifest SHA-256 `60f2c25b82082e41d466439afa0d93106484ca8fb4cdd41bbdb35cd1f83282bc`.
Original v0 seals remain historically `FAILED_EPHEMERAL_LIFECYCLE`. Authorization uses the unchanged original seals, supplemental durable recovery seals, recovery manifest, and the explicit Phase 5B.2-E user request.

The evaluator used the unchanged `evaluate_record`, `judge_prompt`, `parse_judge`, `point_audit`, and `citation_validator.validate_citations`; `gemini-3.5-flash-lite`, temperature 0, frozen endpoint and 120-second timeout. Variants ran sequentially R2 → A1 → A2; first valid judgment accepted, maximum three requests per query. Production entry points were guarded against execution.

Exact joins passed before calls: 31 R2, 31 A1, 31 A2, 31 gold queries, exact query text and 102 unique `(query_id, point_id)` tuples.

## R1 → R2 replication (reported first)

R1 is historical and unchanged. R2 has incomplete judging, so full 31-query replication deltas, gained/lost totals, net change and gross churn are unavailable. This is not a formal variance estimate; no effect correction or subtraction is made.

| Metric | R1 | R2 |
|---|---|---|
| AC primary macro | 0.723655914 | N/A |
| AC primary micro | 0.637254902 | N/A |
| AC available-case macro (queries) | 0.723655914 (n=31) | 0.692753623 (n=23) |
| AC available-case micro (points) | 0.637254902 (65/102) | 0.589743590 (46/78) |
| Citation Completeness primary macro | 0.723655914 | N/A |
| Citation Completeness primary micro | 0.637254902 | N/A |
| Citation Completeness available-case macro (queries) | 0.723655914 (n=31) | 0.692753623 (n=23) |
| Citation Completeness available-case micro (points) | 0.637254902 (65/102) | 0.589743590 (46/78) |
| Citation Correctness macro (defined queries) | 0.982795699 (n=31) | 0.956521739 (n=23) |
| Citation Correctness pooled micro (raw counts) | 0.978723404 (92/94) | 0.983870968 (61/62) |
| Groundedness macro (defined queries) | 0.966666667 (n=31) | 0.956521739 (n=23) |
| Groundedness pooled micro (raw counts) | 0.958762887 (93/97) | 0.984126984 (62/63) |
| UCR macro (defined queries) | 0.033333333 (n=31) | 0.043478261 (n=23) |
| UCR pooled micro (raw counts) | 0.041237113 (4/97) | 0.015873016 (1/63) |
| Citation syntax validity | 1.000000000 (31/31) | 1.000000000 (31/31) |

The R1 and available-case R2 secondary values above cover different query sets. Their arithmetic deltas in the JSON are explicitly diagnostic and must not be interpreted as a paired replication effect. Point observations retain all 102 tuple identities with unknown R2 labels represented as null.

## Completeness gate and evaluator failures

| Variant | Judged / 31 | Failed queries | Attempts | Failed attempts | Observed supported / 102 |
|---|---:|---:|---:|---:|---:|
| R2 | 23/31 | 8 | 53 | 30 | 46/102 (incomplete) |
| A1 | 22/31 | 9 | 56 | 34 | 43/102 (incomplete) |
| A2 | 19/31 | 12 | 56 | 37 | 34/102 (incomplete) |

HTTP 429 `RESOURCE_EXHAUSTED` responses reported a free-tier request quota limit of 15. The unchanged evaluator retries immediately and exhausted three attempts on the failed queries. The harness added no pacing or retry backoff. All request slots, transport responses/errors and parsed-attempt logs are retained; no fourth attempts, label repairs or rejudging were performed.

- R2 failed query IDs: `eval021`, `eval022`, `eval023`, `eval024`, `eval025`, `eval026`, `eval027`, `eval028`.
- A1 failed query IDs: `eval014`, `eval016`, `eval019`, `eval020`, `eval022`, `eval023`, `eval024`, `eval025`, `eval026`.
- A2 failed query IDs: `eval015`, `eval016`, `eval017`, `eval018`, `eval019`, `eval020`, `eval022`, `eval023`, `eval024`, `eval025`, `eval026`, `eval027`.

All 93 evaluation envelopes are present, including failures. The mandatory 31/31-per-variant gate failed. Full primary AC, complete 102-point partitions, full paired sign/median summaries and 31-pair bootstrap CIs are withheld. Missing judgments remain null; no denominator reduction or imputation is used.

## Per-variant available-case diagnostics

The following semantic metrics are descriptive diagnostics over successfully judged records. They are not the complete primary benchmark result. AC/CC primary macro and micro remain null. Pooled claim metrics use raw matching sums over eligible judged records; zero-denominator query ratios are excluded from macro means and remain null. Groundedness and UCR are calculated independently. Deterministic citation syntax validity covers all completed outputs, including semantic judge failures.

| Metric | R2 | A1 | A2 |
|---|---|---|---|
| AC primary macro | N/A | N/A | N/A |
| AC primary micro | N/A | N/A | N/A |
| AC available-case macro (queries) | 0.692753623 (n=23) | 0.653030303 (n=22) | 0.606140351 (n=19) |
| AC available-case micro (points) | 0.589743590 (46/78) | 0.558441558 (43/77) | 0.500000000 (34/68) |
| Citation Completeness primary macro | N/A | N/A | N/A |
| Citation Completeness primary micro | N/A | N/A | N/A |
| Citation Completeness available-case macro (queries) | 0.692753623 (n=23) | 0.653030303 (n=22) | 0.606140351 (n=19) |
| Citation Completeness available-case micro (points) | 0.589743590 (46/78) | 0.558441558 (43/77) | 0.500000000 (34/68) |
| Citation Correctness macro (defined queries) | 0.956521739 (n=23) | 0.954545455 (n=22) | 0.947368421 (n=19) |
| Citation Correctness pooled micro (raw counts) | 0.983870968 (61/62) | 0.966101695 (57/59) | 0.982758621 (57/58) |
| Groundedness macro (defined queries) | 0.956521739 (n=23) | 0.954545455 (n=22) | 0.934210526 (n=19) |
| Groundedness pooled micro (raw counts) | 0.984126984 (62/63) | 0.950000000 (57/60) | 0.966101695 (57/59) |
| UCR macro (defined queries) | 0.043478261 (n=23) | 0.045454545 (n=22) | 0.065789474 (n=19) |
| UCR pooled micro (raw counts) | 0.015873016 (1/63) | 0.050000000 (3/60) | 0.033898305 (2/59) |
| Citation syntax validity | 1.000000000 (31/31) | 1.000000000 (31/31) | 1.000000000 (31/31) |

Raw-count anomalies (retained without repairs or extra judgments):
- R2: none.
- A1: none.
- A2: none.

## R2 vs A1 — Answer Revision

**Interpretation: Insufficient evidence.** Incomplete primary data.
Full macro/micro AC differences, median differences, R2-better/tied/ablation-better counts, both/only-R2/only-ablation/neither totals, and net contribution: N/A because the complete paired-data gate failed.
Bootstrap: not executed. Frozen configuration remains 10,000 paired query-level resamples, seed 20260906, sample size 31, independently reset Python `random.Random`, percentile interpolation at `(N-1)*p`; no p-values and no point-level resampling.
Replication attribution safeguards cannot be evaluated because full R1→R2 variation and the primary ablation effect are unavailable. No alternative threshold or corrected effect is used.

The JSON retains all 31 query rows, both variants’ available scores and raw deltas, statuses/errors, production costs, trace links, and all 102 point observations with nulls for missing judgments.

### Answer Revision trigger-aware diagnostics

Strata use sealed R2 intervention-used flags. These are descriptive post-treatment subsets, not randomized causal subgroups. Differences where R2 did not use the intervention are background run variation/downstream differences.

| R2 used | Queries | Required points | R2 judged | A1 judged | R2 AC macro | A1 AC macro | Macro delta |
|---|---:|---:|---:|---:|---:|---:|---:|
| true | 4 | 19 | 4 | 4 | 0.566666667 | 0.300000000 | 0.266666667 |
| false | 27 | 83 | 19 | 18 | N/A | N/A | N/A |
| unreached_or_error | 0 | 0 | 0 | 0 | N/A | N/A | N/A |

Cross-tab against the ablation’s own decision metadata:

| R2 used | Ablation would have triggered | Ablation blocked | Queries |
|---|---|---|---:|
| False | False | False | 27 |
| True | True | True | 3 |
| True | False | False | 1 |

R2-used=true: query IDs eval005b, eval007, eval013, eval029.
Required-point denominator: 19. Complete point partition: {"both_supported": 5, "only_reference": 4, "only_comparator": 0, "neither_supported": 10}.
Subset production costs (R2 / A1): retrieval 6 / 6; llm 20 / 12; merge_rerank 2 / 2.
Subset AC/CC and claim-metric diagnostics, with explicit denominators:

| Metric | R2 | A1 |
|---|---|---|
| AC primary macro | 0.566666667 | 0.300000000 |
| AC primary micro | 0.473684211 | 0.263157895 |
| AC available-case macro (queries) | 0.566666667 (n=4) | 0.300000000 (n=4) |
| AC available-case micro (points) | 0.473684211 (9/19) | 0.263157895 (5/19) |
| Citation Completeness primary macro | 0.566666667 | 0.300000000 |
| Citation Completeness primary micro | 0.473684211 | 0.263157895 |
| Citation Completeness available-case macro (queries) | 0.566666667 (n=4) | 0.300000000 (n=4) |
| Citation Completeness available-case micro (points) | 0.473684211 (9/19) | 0.263157895 (5/19) |
| Citation Correctness macro (defined queries) | 1.000000000 (n=4) | 1.000000000 (n=4) |
| Citation Correctness pooled micro (raw counts) | 1.000000000 (12/12) | 1.000000000 (7/7) |
| Groundedness macro (defined queries) | 1.000000000 (n=4) | 1.000000000 (n=4) |
| Groundedness pooled micro (raw counts) | 1.000000000 (12/12) | 1.000000000 (7/7) |
| UCR macro (defined queries) | 0.000000000 (n=4) | 0.000000000 (n=4) |
| UCR pooled micro (raw counts) | 0.000000000 (0/12) | 0.000000000 (0/7) |
| Citation syntax validity | 1.000000000 (4/4) | 1.000000000 (4/4) |

R2-used=false: query IDs eval001, eval002, eval003, eval004, eval005a, eval006, eval008, eval009, eval010, eval011, eval012, eval014, eval015, eval016, eval017, eval018, eval019, eval020, eval021, eval022, eval023, eval024, eval025, eval026, eval027, eval028, eval030.
Required-point denominator: 83. Complete point partition: N/A; at least one missing judgment.
Subset production costs (R2 / A1): retrieval 36 / 36; llm 81 / 82; merge_rerank 7 / 9.
Subset AC/CC and claim-metric diagnostics, with explicit denominators:

| Metric | R2 | A1 |
|---|---|---|
| AC primary macro | N/A | N/A |
| AC primary micro | N/A | N/A |
| AC available-case macro (queries) | 0.719298246 (n=19) | 0.731481481 (n=18) |
| AC available-case micro (points) | 0.627118644 (37/59) | 0.655172414 (38/58) |
| Citation Completeness primary macro | N/A | N/A |
| Citation Completeness primary micro | N/A | N/A |
| Citation Completeness available-case macro (queries) | 0.719298246 (n=19) | 0.731481481 (n=18) |
| Citation Completeness available-case micro (points) | 0.627118644 (37/59) | 0.655172414 (38/58) |
| Citation Correctness macro (defined queries) | 0.947368421 (n=19) | 0.944444444 (n=18) |
| Citation Correctness pooled micro (raw counts) | 0.980000000 (49/50) | 0.961538462 (50/52) |
| Groundedness macro (defined queries) | 0.947368421 (n=19) | 0.944444444 (n=18) |
| Groundedness pooled micro (raw counts) | 0.980392157 (50/51) | 0.943396226 (50/53) |
| UCR macro (defined queries) | 0.052631579 (n=19) | 0.055555556 (n=18) |
| UCR pooled micro (raw counts) | 0.019607843 (1/51) | 0.056603774 (3/53) |
| Citation syntax validity | 1.000000000 (27/27) | 1.000000000 (27/27) |

## R2 vs A2 — Evidence Expansion

**Interpretation: Insufficient evidence.** Incomplete primary data.
Full macro/micro AC differences, median differences, R2-better/tied/ablation-better counts, both/only-R2/only-ablation/neither totals, and net contribution: N/A because the complete paired-data gate failed.
Bootstrap: not executed. Frozen configuration remains 10,000 paired query-level resamples, seed 20260906, sample size 31, independently reset Python `random.Random`, percentile interpolation at `(N-1)*p`; no p-values and no point-level resampling.
Replication attribution safeguards cannot be evaluated because full R1→R2 variation and the primary ablation effect are unavailable. No alternative threshold or corrected effect is used.

The JSON retains all 31 query rows, both variants’ available scores and raw deltas, statuses/errors, production costs, trace links, and all 102 point observations with nulls for missing judgments.

### Evidence Expansion trigger-aware diagnostics

Strata use sealed R2 intervention-used flags. These are descriptive post-treatment subsets, not randomized causal subgroups. Differences where R2 did not use the intervention are background run variation/downstream differences.

| R2 used | Queries | Required points | R2 judged | A2 judged | R2 AC macro | A2 AC macro | Macro delta |
|---|---:|---:|---:|---:|---:|---:|---:|
| true | 9 | 36 | 8 | 7 | N/A | N/A | N/A |
| false | 22 | 66 | 15 | 12 | N/A | N/A | N/A |
| unreached_or_error | 0 | 0 | 0 | 0 | N/A | N/A | N/A |

Cross-tab against the ablation’s own decision metadata:

| R2 used | Ablation would have triggered | Ablation blocked | Queries |
|---|---|---|---:|
| True | True | True | 7 |
| False | False | False | 21 |
| True | False | False | 2 |
| False | True | True | 1 |

R2-used=true: query IDs eval001, eval005a, eval005b, eval006, eval011, eval013, eval014, eval016, eval023.
Required-point denominator: 36. Complete point partition: N/A; at least one missing judgment.
Subset production costs (R2 / A2): retrieval 20 / 9; llm 31 / 30; merge_rerank 9 / 0.
Subset AC/CC and claim-metric diagnostics, with explicit denominators:

| Metric | R2 | A2 |
|---|---|---|
| AC primary macro | N/A | N/A |
| AC primary micro | N/A | N/A |
| AC available-case macro (queries) | 0.439583333 (n=8) | 0.323809524 (n=7) |
| AC available-case micro (points) | 0.382352941 (13/34) | 0.266666667 (8/30) |
| Citation Completeness primary macro | N/A | N/A |
| Citation Completeness primary micro | N/A | N/A |
| Citation Completeness available-case macro (queries) | 0.439583333 (n=8) | 0.323809524 (n=7) |
| Citation Completeness available-case micro (points) | 0.382352941 (13/34) | 0.266666667 (8/30) |
| Citation Correctness macro (defined queries) | 0.875000000 (n=8) | 0.857142857 (n=7) |
| Citation Correctness pooled micro (raw counts) | 0.950000000 (19/20) | 0.947368421 (18/19) |
| Groundedness macro (defined queries) | 0.875000000 (n=8) | 0.857142857 (n=7) |
| Groundedness pooled micro (raw counts) | 0.950000000 (19/20) | 0.947368421 (18/19) |
| UCR macro (defined queries) | 0.125000000 (n=8) | 0.142857143 (n=7) |
| UCR pooled micro (raw counts) | 0.050000000 (1/20) | 0.052631579 (1/19) |
| Citation syntax validity | 1.000000000 (9/9) | 1.000000000 (9/9) |

R2-used=false: query IDs eval002, eval003, eval004, eval007, eval008, eval009, eval010, eval012, eval015, eval017, eval018, eval019, eval020, eval021, eval022, eval024, eval025, eval026, eval027, eval028, eval029, eval030.
Required-point denominator: 66. Complete point partition: N/A; at least one missing judgment.
Subset production costs (R2 / A2): retrieval 22 / 22; llm 70 / 71; merge_rerank 0 / 0.
Subset AC/CC and claim-metric diagnostics, with explicit denominators:

| Metric | R2 | A2 |
|---|---|---|
| AC primary macro | N/A | N/A |
| AC primary micro | N/A | N/A |
| AC available-case macro (queries) | 0.827777778 (n=15) | 0.770833333 (n=12) |
| AC available-case micro (points) | 0.750000000 (33/44) | 0.684210526 (26/38) |
| Citation Completeness primary macro | N/A | N/A |
| Citation Completeness primary micro | N/A | N/A |
| Citation Completeness available-case macro (queries) | 0.827777778 (n=15) | 0.770833333 (n=12) |
| Citation Completeness available-case micro (points) | 0.750000000 (33/44) | 0.684210526 (26/38) |
| Citation Correctness macro (defined queries) | 1.000000000 (n=15) | 1.000000000 (n=12) |
| Citation Correctness pooled micro (raw counts) | 1.000000000 (42/42) | 1.000000000 (39/39) |
| Groundedness macro (defined queries) | 1.000000000 (n=15) | 0.979166667 (n=12) |
| Groundedness pooled micro (raw counts) | 1.000000000 (43/43) | 0.975000000 (39/40) |
| UCR macro (defined queries) | 0.000000000 (n=15) | 0.020833333 (n=12) |
| UCR pooled micro (raw counts) | 0.000000000 (0/43) | 0.025000000 (1/40) |
| Citation syntax validity | 1.000000000 (22/22) | 1.000000000 (22/22) |

## Production efficiency from sealed ledgers

All 31 attempted queries per variant are included. Observer call counts reconcile with original traces, per-query journals, production attempts and durable seals. Evaluator requests are excluded.

| Variant | Retrieval total / mean / median / max | Production LLM total / mean / median / max | Merge-reranks | Observable HTTP submissions |
|---|---|---|---:|---:|
| R2 | 42 / 1.354838710 / 1 / 3 | 101 / 3.258064516 / 3 / 5 | 9 | 101 |
| A1 | 42 / 1.354838710 / 1 / 2 | 94 / 3.032258065 / 3 / 4 | 11 | 94 |
| A2 | 31 / 1 / 1 / 1 | 101 / 3.258064516 / 3 / 6 | 0 | 101 |

A1 savings, R2 − A1: production LLM 7; retrieval 0; merge-reranks -2. Negative savings mean the ablation used more calls.

A2 savings, R2 − A2: production LLM 0; retrieval 11; merge-reranks 9. Negative savings mean the ablation used more calls.

Provider-internal retries, token records and monetary costs are unavailable. Observed HTTP submissions are kept distinct from these unknown quantities.

## Frozen hypotheses and limits

- H1: Removing Answer Revision is expected to reduce Answer Completeness on at least some revision-triggered queries, particularly generation-omission cases. Hypothesis, not guaranteed result.
- H2: Removing Evidence Expansion may have limited impact because most observed expansions did not change final Top-5 evidence; however a controlled run is required before concluding the mechanism is unnecessary.
- H3 remains exploratory and was not tested.

H1/H2 receive insufficient evidence because the primary evaluation is incomplete. They are not rewritten from the observed diagnostics. Historical R1 source/environment and provider backend identity limits remain as declared in Phase 5A.

## Artifact paths and provenance

Historical root contrast files and per-variant evaluation/metrics placeholders are pinned by the recovery protocol. They remain byte-identical at their original paths. Completed Phase 5B.2-E records and incomplete analysis results use the additive `phase5b2e_v0/` directory:

- `phase5b2e_v0/replication_R1_R2.json`
- `phase5b2e_v0/contrast_R2_A1.json`
- `phase5b2e_v0/contrast_R2_A2.json`
- `phase5b2e_v0/<variant_id>/{evaluation.jsonl,evaluation_attempts.jsonl,metrics.json}`
- `phase5b_evaluation_metrics_v0.json` and this new report
- `phase5b2e_v0/provenance.json`, `integrity_before.json`, `integrity_after.json`, request/response slots, and per-query records

Provenance records Phase 5A/5B.1 hashes, original and supplemental seals, production output hashes, external recovery anchor, evaluator/gold hashes, historical source/asset hashes and evaluation artifact hashes. The manifest excludes its own hash; that SHA-256 is printed separately.

A pre-call harness endpoint check initially stripped the trailing slash, unlike the frozen preflight. It stopped before any evaluator request. The hash check was aligned with the frozen whitespace-only canonicalization and both protocol versions and the amendment were retained; the endpoint, client and evaluator were unchanged.

## Final integrity and stop

**Production artifact integrity: PASS. Frozen source integrity: PASS.** All preexisting files in the integrity snapshot retain identical SHA-256 values. The unchanged independent recovery verifier passed again after evaluation. Production outputs/traces/sidecars, all original/supplemental seals, corpus, gold, R0/R1, Phase 4, Phase 5A, Phase 5B.1, Phase 5B.2-R, Agentic runtime, retrieval, prompts, and historical incomplete reports/placeholders remain unchanged.

**Ready for Phase 5C: NO.** No A3/A4, production reruns, optimization or Phase 5C execution. The exhausted attempt budgets are preserved.

## Required console output

```text
Phase 5B.2-E status: INCOMPLETE

RECOVERY GATE
R2: PASS
A1: PASS
A2: PASS

PRODUCTION RERUNS:
0

EVALUATION
R2: 23/31
A1: 22/31
A2: 19/31

R1 → R2
AC macro: 0.723655914 → N/A; delta N/A
AC micro: 0.637254902 → N/A; delta N/A
Supported points: 65/102 → N/A (46/102 known observed support; incomplete)
Net point change: N/A
Gross churn: N/A
Replication variability: Unavailable: incomplete R2 judging; no full-cohort variation estimate

R2 vs A1
AC macro: N/A vs N/A
Delta: N/A
AC micro: N/A vs N/A
Delta: N/A
Only R2 points: N/A
Only A1 points: N/A
Net R2 contribution: N/A
R2 better / tied / A1 better: N/A / N/A / N/A
95% bootstrap CI: [N/A, N/A] — not executed; 31-pair gate failed
R2 revision-triggered queries: 4 (eval005b, eval007, eval013, eval029)
Production LLM calls:
R2 101
A1 94
Saved 7
Interpretation: Insufficient evidence; Incomplete primary data

R2 vs A2
AC macro: N/A vs N/A
Delta: N/A
AC micro: N/A vs N/A
Delta: N/A
Only R2 points: N/A
Only A2 points: N/A
Net R2 contribution: N/A
R2 better / tied / A2 better: N/A / N/A / N/A
95% bootstrap CI: [N/A, N/A] — not executed; 31-pair gate failed
R2 expansion-triggered queries: 9 (eval001, eval005a, eval005b, eval006, eval011, eval013, eval014, eval016, eval023)
Retrieval calls:
R2 42
A2 31
Saved 11
Merge-reranks:
R2 9
A2 0
Saved 9
Interpretation: Insufficient evidence; Incomplete primary data

CITATION / SAFETY
Semantic metrics are available-case diagnostics; syntax validity covers all completed outputs independently. Explicit denominators and raw counts follow.
| Metric | R2 | A1 | A2 |
|---|---|---|---|
| AC primary macro | N/A | N/A | N/A |
| AC primary micro | N/A | N/A | N/A |
| AC available-case macro (queries) | 0.692753623 (n=23) | 0.653030303 (n=22) | 0.606140351 (n=19) |
| AC available-case micro (points) | 0.589743590 (46/78) | 0.558441558 (43/77) | 0.500000000 (34/68) |
| Citation Completeness primary macro | N/A | N/A | N/A |
| Citation Completeness primary micro | N/A | N/A | N/A |
| Citation Completeness available-case macro (queries) | 0.692753623 (n=23) | 0.653030303 (n=22) | 0.606140351 (n=19) |
| Citation Completeness available-case micro (points) | 0.589743590 (46/78) | 0.558441558 (43/77) | 0.500000000 (34/68) |
| Citation Correctness macro (defined queries) | 0.956521739 (n=23) | 0.954545455 (n=22) | 0.947368421 (n=19) |
| Citation Correctness pooled micro (raw counts) | 0.983870968 (61/62) | 0.966101695 (57/59) | 0.982758621 (57/58) |
| Groundedness macro (defined queries) | 0.956521739 (n=23) | 0.954545455 (n=22) | 0.934210526 (n=19) |
| Groundedness pooled micro (raw counts) | 0.984126984 (62/63) | 0.950000000 (57/60) | 0.966101695 (57/59) |
| UCR macro (defined queries) | 0.043478261 (n=23) | 0.045454545 (n=22) | 0.065789474 (n=19) |
| UCR pooled micro (raw counts) | 0.015873016 (1/63) | 0.050000000 (3/60) | 0.033898305 (2/59) |
| Citation syntax validity | 1.000000000 (31/31) | 1.000000000 (31/31) | 1.000000000 (31/31) |

EVALUATOR ERRORS
R2: 8 exhausted queries; 53 evaluator attempts; 30 failed attempts.
Failed query IDs: eval021, eval022, eval023, eval024, eval025, eval026, eval027, eval028
A1: 9 exhausted queries; 56 evaluator attempts; 34 failed attempts.
Failed query IDs: eval014, eval016, eval019, eval020, eval022, eval023, eval024, eval025, eval026
A2: 12 exhausted queries; 56 evaluator attempts; 37 failed attempts.
Failed query IDs: eval015, eval016, eval017, eval018, eval019, eval020, eval022, eval023, eval024, eval025, eval026, eval027
Provider errors: HTTP 429 RESOURCE_EXHAUSTED (reported free-tier request quota limit 15).
The frozen evaluate_record retries immediately; no backoff was introduced. Every exhausted query used all three allowed attempts. No fourth attempt or valid-output rejudging occurred.

PRODUCTION ARTIFACT INTEGRITY:
PASS

FROZEN SOURCE INTEGRITY:
PASS

Ready for Phase 5C:
NO
```
