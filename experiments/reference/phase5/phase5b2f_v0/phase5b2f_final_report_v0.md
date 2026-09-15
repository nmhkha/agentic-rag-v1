# Phase 5B.2-F — Final frozen paired ablation analysis v0

## 1. Experiment completion and provenance

**Phase 5B.2-F: PASS. Primary complete benchmark: 93/93 accepted semantic records.** Exactly 31 frozen queries per variant and 102 unique `(query_id, point_id)` tuples. No denominator reduction or imputation.

Recovery anchor: `8e74013cab6df4564dd33f17cd6901e968152b631d82bbc0c523e680c4a999ee`. The append-only attempt ledger reconciles to 29/29 recovered judgments, zero remaining slots, zero unresolved STARTED, AMBIGUOUS, RECOVERY_EXHAUSTED or unsealed accepted records. Original/supplemental production seals and frozen historical hashes passed the existing offline verifier.

| Variant | Accepted v0 | Recovered v1 | Complete |
|---|---|---|---|
| R2 | 23 | 8 | 31/31 |
| A1 | 22 | 9 | 31/31 |
| A2 | 19 | 12 | 31/31 |

Authority is accepted v0 if present, otherwise the one valid recovery observation for that frozen slot. Canonical JSONL records equal their source objects; source-file hashes and unmodified semantic payloads are preserved. The [canonical manifest](canonical_judgments_manifest.json) binds each record to its production output, answer hash, query, point set and source.

**Previous available-case diagnostics = non-primary historical diagnostics. Final 93/93 analysis = primary complete benchmark.** The incomplete report, available-case metrics, placeholders and recovery artifacts remain unchanged. The quota-recovery amendment followed evaluation transport failure; it remains part of provenance and does not invalidate the completed benchmark.

Network/API calls: **0**. Production calls: **0**. Evaluator calls: **0**. Deterministic stored-label/parser/point-audit and citation-syntax integrity verification only; no semantic judging or response selection.

## 2. R1 → R2 replication

R1 AC macro **0.723655913978** → R2 **0.696774193548**; Δ R2−R1 **-0.026881720430**. AC micro **65/102 → 63/102**; delta -0.019607843137.

| Both supported | Only R2 | Only R1 | Neither | Total | Net R2 points | Gross churn |
|---|---|---|---|---|---|---|
| 62 | 1 | 3 | 36 | 102 | -2 | 4 |

Only R2: `eval027/P4`.

Only R1: `eval002/P2`, `eval022/P2`, `eval026/P1`.

R2 gained 1 point, lost 3, net -2, gross churn 4. R2 better / tied / R1 better: **1 / 27 / 3**.

**One observed same-configuration replication.** This is not formal model variance, a stochasticity confidence interval, or a noise distribution. No replication delta is subtracted from an ablation effect.

| Metric | R1 macro | R2 macro | Δ macro | R1 pooled (raw) | R2 pooled (raw) | Δ pooled | Δ numerator / denominator |
|---|---|---|---|---|---|---|---|
| Answer Completeness | 0.723655913978 | 0.696774193548 | -0.026881720430 | 0.637254901961 (65/102) | 0.617647058824 (63/102) | -0.019607843137 | -2 / 0 |
| Citation Completeness | 0.723655913978 | 0.696774193548 | -0.026881720430 | 0.637254901961 (65/102) | 0.617647058824 (63/102) | -0.019607843137 | -2 / 0 |
| Citation Correctness | 0.982795698925 | 0.935483870968 | -0.047311827957 | 0.978723404255 (92/94) | 0.964705882353 (82/85) | -0.014017521902 | -10 / -9 |
| Groundedness | 0.966666666667 | 0.935483870968 | -0.031182795699 | 0.958762886598 (93/97) | 0.965517241379 (84/87) | 0.006754354781 | -9 / -10 |
| Unsupported Claim Rate ↓ | 0.033333333333 | 0.064516129032 | 0.031182795699 | 0.041237113402 (4/97) | 0.034482758621 (3/87) | -0.006754354781 | -1 / -10 |
| Citation syntax validity | 1.000000000000 | 1.000000000000 | 0.000000000000 | 1.000000000000 (31/31) | 1.000000000000 (31/31) | 0.000000000000 | 0 / 0 |

**Macro and pooled micro can move in different directions.** R2 Groundedness macro falls while pooled Groundedness rises; UCR macro rises while pooled UCR falls. Citation Correctness falls on both summaries. Keep these separate.

| Query | R1 AC | R2 AC | Δ R2−R1 |
|---|---|---|---|
| eval001 | 0.000000000000 | 0.000000000000 | 0.000000000000 |
| eval002 | 1.000000000000 | 0.500000000000 | -0.500000000000 |
| eval003 | 1.000000000000 | 1.000000000000 | 0.000000000000 |
| eval004 | 0.500000000000 | 0.500000000000 | 0.000000000000 |
| eval005a | 0.000000000000 | 0.000000000000 | 0.000000000000 |
| eval005b | 0.166666666667 | 0.166666666667 | 0.000000000000 |
| eval006 | 1.000000000000 | 1.000000000000 | 0.000000000000 |
| eval007 | 0.500000000000 | 0.500000000000 | 0.000000000000 |
| eval008 | 0.666666666667 | 0.666666666667 | 0.000000000000 |
| eval009 | 1.000000000000 | 1.000000000000 | 0.000000000000 |
| eval010 | 1.000000000000 | 1.000000000000 | 0.000000000000 |
| eval011 | 0.500000000000 | 0.500000000000 | 0.000000000000 |
| eval012 | 1.000000000000 | 1.000000000000 | 0.000000000000 |
| eval013 | 0.600000000000 | 0.600000000000 | 0.000000000000 |
| eval014 | 0.750000000000 | 0.750000000000 | 0.000000000000 |
| eval015 | 1.000000000000 | 1.000000000000 | 0.000000000000 |
| eval016 | 0.500000000000 | 0.500000000000 | 0.000000000000 |
| eval017 | 1.000000000000 | 1.000000000000 | 0.000000000000 |
| eval018 | 0.750000000000 | 0.750000000000 | 0.000000000000 |
| eval019 | 1.000000000000 | 1.000000000000 | 0.000000000000 |
| eval020 | 1.000000000000 | 1.000000000000 | 0.000000000000 |
| eval021 | 1.000000000000 | 1.000000000000 | 0.000000000000 |
| eval022 | 0.333333333333 | 0.000000000000 | -0.333333333333 |
| eval023 | 0.500000000000 | 0.500000000000 | 0.000000000000 |
| eval024 | 1.000000000000 | 1.000000000000 | 0.000000000000 |
| eval025 | 0.666666666667 | 0.666666666667 | 0.000000000000 |
| eval026 | 1.000000000000 | 0.750000000000 | -0.250000000000 |
| eval027 | 0.750000000000 | 1.000000000000 | 0.250000000000 |
| eval028 | 0.750000000000 | 0.750000000000 | 0.000000000000 |
| eval029 | 1.000000000000 | 1.000000000000 | 0.000000000000 |
| eval030 | 0.500000000000 | 0.500000000000 | 0.000000000000 |

## 3. R2 vs A1 — Answer Revision

The sole frozen configuration difference is `enable_answer_revision: true → false`. All quality deltas are R2 − A1; a positive raw UCR delta favors the ablation.

| Metric | A1 macro | R2 macro | Δ macro | A1 pooled (raw) | R2 pooled (raw) | Δ pooled | Δ numerator / denominator |
|---|---|---|---|---|---|---|---|
| Answer Completeness | 0.662365591398 | 0.696774193548 | 0.034408602151 | 0.578431372549 (59/102) | 0.617647058824 (63/102) | 0.039215686275 | 4 / 0 |
| Citation Completeness | 0.662365591398 | 0.696774193548 | 0.034408602151 | 0.578431372549 (59/102) | 0.617647058824 (63/102) | 0.039215686275 | 4 / 0 |

| Both supported | Only R2 | Only A1 | Neither | Total | Net R2 points | Gross churn |
|---|---|---|---|---|---|---|
| 59 | 4 | 0 | 39 | 102 | 4 | 4 |

Only R2: `eval005b/P4`, `eval013/P3`, `eval013/P4`, `eval029/P2`.

Only A1: None.

Points lost by removal = only R2; points gained after removal = only A1; net observed R2 contribution = only R2 − only A1. Net ablation point change is -4.

R2 better / tied / A1 better: **3 / 28 / 0**. Mean paired AC delta 0.034408602151; median 0.000000000000. Ablation improved/equal/worsened: {'improved': 0, 'equal': 28, 'worsened': 3}.

Paired bootstrap 95% CI: **[0.000000000000, 0.079569892473]**. This describes query-sampling uncertainty only; no p-value or significance claim.

Macro/net `replication_attribution_flag`: **false**. Separate gross-churn flag: **true**. The predeclared macro/net replication-attribution flag is not triggered.

Frozen interpretation: **Insufficient evidence**. Nonzero effects meet the frozen replication magnitude/churn safeguard, which takes precedence over directional conflicts and supported-contribution classification.

Conflicts retained despite precedence: AC direction conflicts with citation_correctness; groundedness: macro and pooled micro directions conflict; AC direction conflicts with groundedness; unsupported_claim_rate: macro and pooled micro directions conflict; AC direction conflicts with unsupported_claim_rate.

### Every matched query

| Query | R2 AC | A1 AC | Δ R2−A1 | Both/only R2/only A1/neither | R2 used | A1 would | A1 blocked | Retrieval R2/A1 | LLM R2/A1 | Merge R2/A1 |
|---|---|---|---|---|---|---|---|---|---|---|
| eval001 | 0.000000000000 | 0.000000000000 | 0.000000000000 | 0/0/0/3 | False | False | False | 2/2 | 3/3 | 1/1 |
| eval002 | 0.500000000000 | 0.500000000000 | 0.000000000000 | 1/0/0/1 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval003 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 1/0/0/0 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval004 | 0.500000000000 | 0.500000000000 | 0.000000000000 | 3/0/0/3 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval005a | 0.000000000000 | 0.000000000000 | 0.000000000000 | 0/0/0/7 | False | False | False | 3/2 | 3/3 | 1/1 |
| eval005b | 0.166666666667 | 0.000000000000 | 0.166666666667 | 0/1/0/5 | True | True | True | 2/2 | 5/3 | 1/1 |
| eval006 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 3/0/0/0 | False | False | False | 2/2 | 3/3 | 1/1 |
| eval007 | 0.500000000000 | 0.500000000000 | 0.000000000000 | 3/0/0/3 | True | False | False | 1/1 | 5/3 | 0/0 |
| eval008 | 0.666666666667 | 0.666666666667 | 0.000000000000 | 2/0/0/1 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval009 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 1/0/0/0 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval010 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 2/0/0/0 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval011 | 0.500000000000 | 0.500000000000 | 0.000000000000 | 1/0/0/1 | False | False | False | 2/2 | 3/3 | 1/1 |
| eval012 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 4/0/0/0 | False | False | False | 1/1 | 3/4 | 0/0 |
| eval013 | 0.600000000000 | 0.200000000000 | 0.400000000000 | 1/2/0/2 | True | True | True | 2/2 | 5/3 | 1/1 |
| eval014 | 0.750000000000 | 0.750000000000 | 0.000000000000 | 3/0/0/1 | False | False | False | 2/2 | 3/3 | 1/1 |
| eval015 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 2/0/0/0 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval016 | 0.500000000000 | 0.500000000000 | 0.000000000000 | 2/0/0/2 | False | False | False | 2/2 | 3/3 | 1/1 |
| eval017 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 3/0/0/0 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval018 | 0.750000000000 | 0.750000000000 | 0.000000000000 | 3/0/0/1 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval019 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 3/0/0/0 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval020 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 1/0/0/0 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval021 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 3/0/0/0 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval022 | 0.000000000000 | 0.000000000000 | 0.000000000000 | 0/0/0/3 | False | False | False | 1/2 | 3/3 | 0/1 |
| eval023 | 0.500000000000 | 0.500000000000 | 0.000000000000 | 1/0/0/1 | False | False | False | 3/2 | 3/3 | 1/1 |
| eval024 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 1/0/0/0 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval025 | 0.666666666667 | 0.666666666667 | 0.000000000000 | 2/0/0/1 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval026 | 0.750000000000 | 0.750000000000 | 0.000000000000 | 3/0/0/1 | False | False | False | 1/2 | 3/3 | 0/1 |
| eval027 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 4/0/0/0 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval028 | 0.750000000000 | 0.750000000000 | 0.000000000000 | 3/0/0/1 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval029 | 1.000000000000 | 0.500000000000 | 0.500000000000 | 1/1/0/0 | True | True | True | 1/1 | 5/3 | 0/0 |
| eval030 | 0.500000000000 | 0.500000000000 | 0.000000000000 | 2/0/0/2 | False | False | False | 1/1 | 3/3 | 0/0 |

All raw per-query quality metrics, exact rational AC deltas, full point identities, statuses/errors, costs and trace/observer links are retained in [contrast_R2_A1.json](contrast_R2_A1.json).

## 4. A1 trigger-aware analysis

### R2 used true

**Descriptive post-treatment stratum; not a randomized subgroup.** 4 queries / 19 required points.

Query IDs: `eval005b`, `eval007`, `eval013`, `eval029`.

| Metric | A1 macro | R2 macro | Δ macro | A1 pooled (raw) | R2 pooled (raw) | Δ pooled | Δ numerator / denominator |
|---|---|---|---|---|---|---|---|
| Answer Completeness | 0.300000000000 | 0.566666666667 | 0.266666666667 | 0.263157894737 (5/19) | 0.473684210526 (9/19) | 0.210526315789 | 4 / 0 |
| Citation Completeness | 0.300000000000 | 0.566666666667 | 0.266666666667 | 0.263157894737 (5/19) | 0.473684210526 (9/19) | 0.210526315789 | 4 / 0 |
| Citation Correctness | 1.000000000000 | 1.000000000000 | 0.000000000000 | 1.000000000000 (7/7) | 1.000000000000 (12/12) | 0.000000000000 | 5 / 5 |
| Groundedness | 1.000000000000 | 1.000000000000 | 0.000000000000 | 1.000000000000 (7/7) | 1.000000000000 (12/12) | 0.000000000000 | 5 / 5 |
| Unsupported Claim Rate ↓ | 0.000000000000 | 0.000000000000 | 0.000000000000 | 0.000000000000 (0/7) | 0.000000000000 (0/12) | 0.000000000000 | 0 / 5 |
| Citation syntax validity | 1.000000000000 | 1.000000000000 | 0.000000000000 | 1.000000000000 (4/4) | 1.000000000000 (4/4) | 0.000000000000 | 0 / 0 |

| Both supported | Only R2 | Only A1 | Neither | Total | Net R2 points | Gross churn |
|---|---|---|---|---|---|---|
| 5 | 4 | 0 | 10 | 19 | 4 | 4 |

Only R2: `eval005b/P4`, `eval013/P3`, `eval013/P4`, `eval029/P2`.

Only A1: None.

| Variant | Retrieval total | LLM total | Merge-reranks | Observable HTTP submissions |
|---|---|---|---|---|
| R2 | 6 | 20 | 2 | 20 |
| A1 | 6 | 12 | 2 | 12 |

### R2 used false

**Descriptive post-treatment stratum; not a randomized subgroup.** 27 queries / 83 required points.

Query IDs: `eval001`, `eval002`, `eval003`, `eval004`, `eval005a`, `eval006`, `eval008`, `eval009`, `eval010`, `eval011`, `eval012`, `eval014`, `eval015`, `eval016`, `eval017`, `eval018`, `eval019`, `eval020`, `eval021`, `eval022`, `eval023`, `eval024`, `eval025`, `eval026`, `eval027`, `eval028`, `eval030`.

| Metric | A1 macro | R2 macro | Δ macro | A1 pooled (raw) | R2 pooled (raw) | Δ pooled | Δ numerator / denominator |
|---|---|---|---|---|---|---|---|
| Answer Completeness | 0.716049382716 | 0.716049382716 | 0.000000000000 | 0.650602409639 (54/83) | 0.650602409639 (54/83) | 0.000000000000 | 0 / 0 |
| Citation Completeness | 0.716049382716 | 0.716049382716 | 0.000000000000 | 0.650602409639 (54/83) | 0.650602409639 (54/83) | 0.000000000000 | 0 / 0 |
| Citation Correctness | 0.962962962963 | 0.925925925926 | -0.037037037037 | 0.971428571429 (68/70) | 0.958904109589 (70/73) | -0.012524461840 | 2 / 3 |
| Groundedness | 0.962962962963 | 0.925925925926 | -0.037037037037 | 0.957746478873 (68/71) | 0.960000000000 (72/75) | 0.002253521127 | 4 / 4 |
| Unsupported Claim Rate ↓ | 0.037037037037 | 0.074074074074 | 0.037037037037 | 0.042253521127 (3/71) | 0.040000000000 (3/75) | -0.002253521127 | 0 / 4 |
| Citation syntax validity | 1.000000000000 | 1.000000000000 | 0.000000000000 | 1.000000000000 (27/27) | 1.000000000000 (27/27) | 0.000000000000 | 0 / 0 |

| Both supported | Only R2 | Only A1 | Neither | Total | Net R2 points | Gross churn |
|---|---|---|---|---|---|---|
| 54 | 0 | 0 | 29 | 83 | 0 | 0 |

Only R2: None.

Only A1: None.

| Variant | Retrieval total | LLM total | Merge-reranks | Observable HTTP submissions |
|---|---|---|---|---|
| R2 | 36 | 81 | 7 | 81 |
| A1 | 36 | 82 | 9 | 82 |

### Trigger cross-tab

All eight Boolean cells are retained; no null/unreached decision exists in these sealed successful runs.

| R2 used | A1 would have triggered | A1 blocked | Count | Query IDs |
|---|---|---|---|---|
| False | False | False | 27 | eval001, eval002, eval003, eval004, eval005a, eval006, eval008, eval009, eval010, eval011, eval012, eval014, eval015, eval016, eval017, eval018, eval019, eval020, eval021, eval022, eval023, eval024, eval025, eval026, eval027, eval028, eval030 |
| False | False | True | 0 | — |
| False | True | False | 0 | — |
| False | True | True | 0 | — |
| True | False | False | 1 | eval007 |
| True | False | True | 0 | — |
| True | True | False | 0 | — |
| True | True | True | 3 | eval005b, eval013, eval029 |

Stochastic decision disagreements: `eval007`. These are branch decisions in two distinct stochastic runs, not clean intervention counterfactuals. Non-triggered query differences are background run variation/downstream differences, not direct evidence of removing an unused intervention.

## 5. R2 vs A2 — Evidence Expansion

The sole frozen configuration difference is `enable_expansion: true → false`. All quality deltas are R2 − A2; a positive raw UCR delta favors the ablation.

| Metric | A2 macro | R2 macro | Δ macro | A2 pooled (raw) | R2 pooled (raw) | Δ pooled | Δ numerator / denominator |
|---|---|---|---|---|---|---|---|
| Answer Completeness | 0.696774193548 | 0.696774193548 | 0.000000000000 | 0.607843137255 (62/102) | 0.617647058824 (63/102) | 0.009803921569 | 1 / 0 |
| Citation Completeness | 0.696774193548 | 0.696774193548 | 0.000000000000 | 0.607843137255 (62/102) | 0.617647058824 (63/102) | 0.009803921569 | 1 / 0 |

| Both supported | Only R2 | Only A2 | Neither | Total | Net R2 points | Gross churn |
|---|---|---|---|---|---|---|
| 59 | 4 | 3 | 36 | 102 | 1 | 7 |

Only R2: `eval007/P4`, `eval014/P1`, `eval014/P2`, `eval014/P4`.

Only A2: `eval022/P1`, `eval022/P2`, `eval026/P1`.

Points lost by removal = only R2; points gained after removal = only A2; net observed R2 contribution = only R2 − only A2. Net ablation point change is -1.

R2 better / tied / A2 better: **2 / 27 / 2**. Mean paired AC delta 0.000000000000; median 0.000000000000. Ablation improved/equal/worsened: {'improved': 2, 'equal': 27, 'worsened': 2}.

Paired bootstrap 95% CI: **[-0.064516129032, 0.072580645161]**. This describes query-sampling uncertainty only; no p-value or significance claim.

Macro/net `replication_attribution_flag`: **true**. Separate gross-churn flag: **false**. Attribution limited by observed same-configuration replication variation.

Frozen interpretation: **Insufficient evidence**. Nonzero effects meet the frozen replication magnitude/churn safeguard, which takes precedence over directional conflicts and supported-contribution classification.

Conflicts retained despite precedence: none detected by the frozen directional checks.

### Every matched query

| Query | R2 AC | A2 AC | Δ R2−A2 | Both/only R2/only A2/neither | R2 used | A2 would | A2 blocked | Retrieval R2/A2 | LLM R2/A2 | Merge R2/A2 |
|---|---|---|---|---|---|---|---|---|---|---|
| eval001 | 0.000000000000 | 0.000000000000 | 0.000000000000 | 0/0/0/3 | True | True | True | 2/1 | 3/3 | 1/0 |
| eval002 | 0.500000000000 | 0.500000000000 | 0.000000000000 | 1/0/0/1 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval003 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 1/0/0/0 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval004 | 0.500000000000 | 0.500000000000 | 0.000000000000 | 3/0/0/3 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval005a | 0.000000000000 | 0.000000000000 | 0.000000000000 | 0/0/0/7 | True | True | True | 3/1 | 3/3 | 1/0 |
| eval005b | 0.166666666667 | 0.166666666667 | 0.000000000000 | 1/0/0/5 | True | False | False | 2/1 | 5/6 | 1/0 |
| eval006 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 3/0/0/0 | True | True | True | 2/1 | 3/3 | 1/0 |
| eval007 | 0.500000000000 | 0.333333333333 | 0.166666666667 | 2/1/0/3 | False | False | False | 1/1 | 5/3 | 0/0 |
| eval008 | 0.666666666667 | 0.666666666667 | 0.000000000000 | 2/0/0/1 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval009 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 1/0/0/0 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval010 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 2/0/0/0 | False | False | False | 1/1 | 3/5 | 0/0 |
| eval011 | 0.500000000000 | 0.500000000000 | 0.000000000000 | 1/0/0/1 | True | False | False | 2/1 | 3/3 | 1/0 |
| eval012 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 4/0/0/0 | False | False | False | 1/1 | 3/4 | 0/0 |
| eval013 | 0.600000000000 | 0.600000000000 | 0.000000000000 | 3/0/0/2 | True | True | True | 2/1 | 5/3 | 1/0 |
| eval014 | 0.750000000000 | 0.000000000000 | 0.750000000000 | 0/3/0/1 | True | True | True | 2/1 | 3/3 | 1/0 |
| eval015 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 2/0/0/0 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval016 | 0.500000000000 | 0.500000000000 | 0.000000000000 | 2/0/0/2 | True | True | True | 2/1 | 3/3 | 1/0 |
| eval017 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 3/0/0/0 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval018 | 0.750000000000 | 0.750000000000 | 0.000000000000 | 3/0/0/1 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval019 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 3/0/0/0 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval020 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 1/0/0/0 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval021 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 3/0/0/0 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval022 | 0.000000000000 | 0.666666666667 | -0.666666666667 | 0/0/2/1 | False | False | False | 1/1 | 3/5 | 0/0 |
| eval023 | 0.500000000000 | 0.500000000000 | 0.000000000000 | 1/0/0/1 | True | True | True | 3/1 | 3/3 | 1/0 |
| eval024 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 1/0/0/0 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval025 | 0.666666666667 | 0.666666666667 | 0.000000000000 | 2/0/0/1 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval026 | 0.750000000000 | 1.000000000000 | -0.250000000000 | 3/0/1/0 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval027 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 4/0/0/0 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval028 | 0.750000000000 | 0.750000000000 | 0.000000000000 | 3/0/0/1 | False | False | False | 1/1 | 3/3 | 0/0 |
| eval029 | 1.000000000000 | 1.000000000000 | 0.000000000000 | 2/0/0/0 | False | True | True | 1/1 | 5/3 | 0/0 |
| eval030 | 0.500000000000 | 0.500000000000 | 0.000000000000 | 2/0/0/2 | False | False | False | 1/1 | 3/3 | 0/0 |

All raw per-query quality metrics, exact rational AC deltas, full point identities, statuses/errors, costs and trace/observer links are retained in [contrast_R2_A2.json](contrast_R2_A2.json).

## 6. A2 trigger-aware analysis

### R2 used true

**Descriptive post-treatment stratum; not a randomized subgroup.** 9 queries / 36 required points.

Query IDs: `eval001`, `eval005a`, `eval005b`, `eval006`, `eval011`, `eval013`, `eval014`, `eval016`, `eval023`.

| Metric | A2 macro | R2 macro | Δ macro | A2 pooled (raw) | R2 pooled (raw) | Δ pooled | Δ numerator / denominator |
|---|---|---|---|---|---|---|---|
| Answer Completeness | 0.362962962963 | 0.446296296296 | 0.083333333333 | 0.305555555556 (11/36) | 0.388888888889 (14/36) | 0.083333333333 | 3 / 0 |
| Citation Completeness | 0.362962962963 | 0.446296296296 | 0.083333333333 | 0.305555555556 (11/36) | 0.388888888889 (14/36) | 0.083333333333 | 3 / 0 |
| Citation Correctness | 0.888888888889 | 0.888888888889 | 0.000000000000 | 0.962962962963 (26/27) | 0.958333333333 (23/24) | -0.004629629630 | -3 / -3 |
| Groundedness | 0.888888888889 | 0.888888888889 | 0.000000000000 | 0.962962962963 (26/27) | 0.958333333333 (23/24) | -0.004629629630 | -3 / -3 |
| Unsupported Claim Rate ↓ | 0.111111111111 | 0.111111111111 | 0.000000000000 | 0.037037037037 (1/27) | 0.041666666667 (1/24) | 0.004629629630 | 0 / -3 |
| Citation syntax validity | 1.000000000000 | 1.000000000000 | 0.000000000000 | 1.000000000000 (9/9) | 1.000000000000 (9/9) | 0.000000000000 | 0 / 0 |

| Both supported | Only R2 | Only A2 | Neither | Total | Net R2 points | Gross churn |
|---|---|---|---|---|---|---|
| 11 | 3 | 0 | 22 | 36 | 3 | 3 |

Only R2: `eval014/P1`, `eval014/P2`, `eval014/P4`.

Only A2: None.

| Variant | Retrieval total | LLM total | Merge-reranks | Observable HTTP submissions |
|---|---|---|---|---|
| R2 | 20 | 31 | 9 | 31 |
| A2 | 9 | 30 | 0 | 30 |

### R2 used false

**Descriptive post-treatment stratum; not a randomized subgroup.** 22 queries / 66 required points.

Query IDs: `eval002`, `eval003`, `eval004`, `eval007`, `eval008`, `eval009`, `eval010`, `eval012`, `eval015`, `eval017`, `eval018`, `eval019`, `eval020`, `eval021`, `eval022`, `eval024`, `eval025`, `eval026`, `eval027`, `eval028`, `eval029`, `eval030`.

| Metric | A2 macro | R2 macro | Δ macro | A2 pooled (raw) | R2 pooled (raw) | Δ pooled | Δ numerator / denominator |
|---|---|---|---|---|---|---|---|
| Answer Completeness | 0.833333333333 | 0.799242424242 | -0.034090909091 | 0.772727272727 (51/66) | 0.742424242424 (49/66) | -0.030303030303 | -2 / 0 |
| Citation Completeness | 0.833333333333 | 0.799242424242 | -0.034090909091 | 0.772727272727 (51/66) | 0.742424242424 (49/66) | -0.030303030303 | -2 / 0 |
| Citation Correctness | 1.000000000000 | 0.954545454545 | -0.045454545455 | 1.000000000000 (60/60) | 0.967213114754 (59/61) | -0.032786885246 | -1 / 1 |
| Groundedness | 0.988636363636 | 0.954545454545 | -0.034090909091 | 0.983606557377 (60/61) | 0.968253968254 (61/63) | -0.015352589123 | 1 / 2 |
| Unsupported Claim Rate ↓ | 0.011363636364 | 0.045454545455 | 0.034090909091 | 0.016393442623 (1/61) | 0.031746031746 (2/63) | 0.015352589123 | 1 / 2 |
| Citation syntax validity | 1.000000000000 | 1.000000000000 | 0.000000000000 | 1.000000000000 (22/22) | 1.000000000000 (22/22) | 0.000000000000 | 0 / 0 |

| Both supported | Only R2 | Only A2 | Neither | Total | Net R2 points | Gross churn |
|---|---|---|---|---|---|---|
| 48 | 1 | 3 | 14 | 66 | -2 | 4 |

Only R2: `eval007/P4`.

Only A2: `eval022/P1`, `eval022/P2`, `eval026/P1`.

| Variant | Retrieval total | LLM total | Merge-reranks | Observable HTTP submissions |
|---|---|---|---|---|
| R2 | 22 | 70 | 0 | 70 |
| A2 | 22 | 71 | 0 | 71 |

### Trigger cross-tab

All eight Boolean cells are retained; no null/unreached decision exists in these sealed successful runs.

| R2 used | A2 would have triggered | A2 blocked | Count | Query IDs |
|---|---|---|---|---|
| False | False | False | 21 | eval002, eval003, eval004, eval007, eval008, eval009, eval010, eval012, eval015, eval017, eval018, eval019, eval020, eval021, eval022, eval024, eval025, eval026, eval027, eval028, eval030 |
| False | False | True | 0 | — |
| False | True | False | 0 | — |
| False | True | True | 1 | eval029 |
| True | False | False | 2 | eval005b, eval011 |
| True | False | True | 0 | — |
| True | True | False | 0 | — |
| True | True | True | 7 | eval001, eval005a, eval006, eval013, eval014, eval016, eval023 |

Stochastic decision disagreements: `eval005b`, `eval011`, `eval029`. These are branch decisions in two distinct stochastic runs, not clean intervention counterfactuals. Non-triggered query differences are background run variation/downstream differences, not direct evidence of removing an unused intervention.

## 7. Citation/safety metrics

| Variant | Metric | Macro | Defined queries | Pooled micro / rate | Raw numerator / denominator |
|---|---|---|---|---|---|
| R1 | Citation Completeness | 0.723655913978 | 31 | 0.637254901961 | 65/102 |
| R1 | Citation Correctness | 0.982795698925 | 31 | 0.978723404255 | 92/94 |
| R1 | Groundedness | 0.966666666667 | 31 | 0.958762886598 | 93/97 |
| R1 | Unsupported Claim Rate ↓ | 0.033333333333 | 31 | 0.041237113402 | 4/97 |
| R1 | Citation syntax validity | 1.000000000000 | 31 | 1.000000000000 | 31/31 |
| R2 | Citation Completeness | 0.696774193548 | 31 | 0.617647058824 | 63/102 |
| R2 | Citation Correctness | 0.935483870968 | 31 | 0.964705882353 | 82/85 |
| R2 | Groundedness | 0.935483870968 | 31 | 0.965517241379 | 84/87 |
| R2 | Unsupported Claim Rate ↓ | 0.064516129032 | 31 | 0.034482758621 | 3/87 |
| R2 | Citation syntax validity | 1.000000000000 | 31 | 1.000000000000 | 31/31 |
| A1 | Citation Completeness | 0.662365591398 | 31 | 0.578431372549 | 59/102 |
| A1 | Citation Correctness | 0.967741935484 | 31 | 0.974025974026 | 75/77 |
| A1 | Groundedness | 0.967741935484 | 31 | 0.961538461538 | 75/78 |
| A1 | Unsupported Claim Rate ↓ | 0.032258064516 | 31 | 0.038461538462 | 3/78 |
| A1 | Citation syntax validity | 1.000000000000 | 31 | 1.000000000000 | 31/31 |
| A2 | Citation Completeness | 0.696774193548 | 31 | 0.607843137255 | 62/102 |
| A2 | Citation Correctness | 0.967741935484 | 31 | 0.988505747126 | 86/87 |
| A2 | Groundedness | 0.959677419355 | 31 | 0.977272727273 | 86/88 |
| A2 | Unsupported Claim Rate ↓ | 0.040322580645 | 31 | 0.022727272727 | 2/88 |
| A2 | Citation syntax validity | 1.000000000000 | 31 | 1.000000000000 | 31/31 |

Claim macro scores average only defined per-query ratios; zero denominators remain null. All current claim ratios are defined on 31 queries. Pooled scores sum stored numerator and denominator counts independently. Groundedness was computed from grounded claims and UCR from unsupported claims; neither was inferred from the other. No raw-count anomalies were found. Syntax is separate from semantic correctness.

R2 − A1:

| Metric | A1 macro | R2 macro | Δ macro | A1 pooled (raw) | R2 pooled (raw) | Δ pooled | Δ numerator / denominator |
|---|---|---|---|---|---|---|---|
| Citation Completeness | 0.662365591398 | 0.696774193548 | 0.034408602151 | 0.578431372549 (59/102) | 0.617647058824 (63/102) | 0.039215686275 | 4 / 0 |
| Citation Correctness | 0.967741935484 | 0.935483870968 | -0.032258064516 | 0.974025974026 (75/77) | 0.964705882353 (82/85) | -0.009320091673 | 7 / 8 |
| Groundedness | 0.967741935484 | 0.935483870968 | -0.032258064516 | 0.961538461538 (75/78) | 0.965517241379 (84/87) | 0.003978779841 | 9 / 9 |
| Unsupported Claim Rate ↓ | 0.032258064516 | 0.064516129032 | 0.032258064516 | 0.038461538462 (3/78) | 0.034482758621 (3/87) | -0.003978779841 | 0 / 9 |
| Citation syntax validity | 1.000000000000 | 1.000000000000 | 0.000000000000 | 1.000000000000 (31/31) | 1.000000000000 (31/31) | 0.000000000000 | 0 / 0 |

R2 − A2:

| Metric | A2 macro | R2 macro | Δ macro | A2 pooled (raw) | R2 pooled (raw) | Δ pooled | Δ numerator / denominator |
|---|---|---|---|---|---|---|---|
| Citation Completeness | 0.696774193548 | 0.696774193548 | 0.000000000000 | 0.607843137255 (62/102) | 0.617647058824 (63/102) | 0.009803921569 | 1 / 0 |
| Citation Correctness | 0.967741935484 | 0.935483870968 | -0.032258064516 | 0.988505747126 (86/87) | 0.964705882353 (82/85) | -0.023799864773 | -4 / -2 |
| Groundedness | 0.959677419355 | 0.935483870968 | -0.024193548387 | 0.977272727273 (86/88) | 0.965517241379 (84/87) | -0.011755485893 | -2 / -1 |
| Unsupported Claim Rate ↓ | 0.040322580645 | 0.064516129032 | 0.024193548387 | 0.022727272727 (2/88) | 0.034482758621 (3/87) | 0.011755485893 | 1 / -1 |
| Citation syntax validity | 1.000000000000 | 1.000000000000 | 0.000000000000 | 1.000000000000 (31/31) | 1.000000000000 (31/31) | 0.000000000000 | 0 / 0 |

A1 has lower AC but higher macro Citation Correctness/Groundedness and lower macro UCR. Its pooled Groundedness/UCR move in the opposite direction from those macro summaries. A2 has equal macro AC and one fewer supported point, while its claim safety summaries favor A2. These tradeoffs remain visible even when the higher-precedence insufficient-evidence category applies.

## 8. Efficiency

Measured from all 93 sealed production observer sidecars, reconciled against trace call counts. Logical hybrid retrieval counts as one call; merge-rerank work is separate. All production events succeeded. Evaluator and quota-recovery attempts are excluded.

| Variant | Cost | Total | Mean/query | Median/query | Max/query |
|---|---|---|---|---|---|
| R2 | retrieval | 42 | 1.354838709677 | 1 | 3 |
| R2 | production_llm | 101 | 3.258064516129 | 3 | 5 |
| R2 | merge_reranks | 9 | 0.290322580645 | 0 | 1 |
| R2 | observable_http_submissions | 101 | 3.258064516129 | 3 | 5 |
| A1 | retrieval | 42 | 1.354838709677 | 1 | 2 |
| A1 | production_llm | 94 | 3.032258064516 | 3 | 4 |
| A1 | merge_reranks | 11 | 0.354838709677 | 0 | 1 |
| A1 | observable_http_submissions | 94 | 3.032258064516 | 3 | 4 |
| A2 | retrieval | 31 | 1 | 1 | 1 |
| A2 | production_llm | 101 | 3.258064516129 | 3 | 6 |
| A2 | merge_reranks | 0 | 0 | 0 | 0 |
| A2 | observable_http_submissions | 101 | 3.258064516129 | 3 | 6 |

A1 saves **7 production LLM calls**, with retrieval difference **0** and **2 more merge-reranks** than R2. A2 saves **11 retrieval calls** and **9 merge-reranks**, with LLM difference **0**.

| Ablation | Cost | Ablation−R2 | Ratio to R2 | Overhead % | Saved | Saved % |
|---|---|---|---|---|---|---|
| A1 | retrieval | 0 | 1.000000000000 | 0.000000000000 | 0 | 0.000000000000 |
| A1 | production_llm | -7 | 0.930693069307 | -6.930693069307 | 7 | 6.930693069307 |
| A1 | merge_reranks | 2 | 1.222222222222 | 22.222222222222 | -2 | -22.222222222222 |
| A2 | retrieval | -11 | 0.738095238095 | -26.190476190476 | 11 | 26.190476190476 |
| A2 | production_llm | 0 | 1.000000000000 | 0.000000000000 | 0 | 0.000000000000 |
| A2 | merge_reranks | -9 | 0.000000000000 | -100.000000000000 | 9 | 100.000000000000 |

R0 is a **configured logical baseline** of 31 retrieval and 31 answer-generation calls; its HTTP count was not measured.

| Variant | Cost | Difference from configured R0 | Ratio | Overhead % |
|---|---|---|---|---|
| R2 | retrieval | 11 | 1.354838709677 | 35.483870967742 |
| R2 | production_llm | 70 | 3.258064516129 | 225.806451612903 |
| A1 | retrieval | 11 | 1.354838709677 | 35.483870967742 |
| A1 | production_llm | 63 | 3.032258064516 | 203.225806451613 |
| A2 | retrieval | 0 | 1.000000000000 | 0.000000000000 |
| A2 | production_llm | 70 | 3.258064516129 | 225.806451612903 |

Historical R1 trace context: 38 retrieval and 108 LLM calls. Provider-internal retries, token records and monetary cost are unavailable; no money estimate is made. Production stage counts and per-query trace links are in the JSON artifacts.

## 9. Bootstrap uncertainty

Exactly 10,000 paired query-level resamples per contrast; sample size 31; `random.Random(20260906)` reinitialized independently. Each draw calls `rng.randrange(31)` 31 times in frozen query order. Statistic: mean per-query AC difference. Percentiles use linear interpolation at `(10000−1)*p`, for p=.025 and .975. Python 3.12.3.

| Contrast | Observed mean Δ | 95% CI lower | 95% CI upper |
|---|---|---|---|
| R2−A1 | 0.034408602151 | 0.000000000000 | 0.079569892473 |
| R2−A2 | 0.000000000000 | -0.064516129032 | 0.072580645161 |

No points, claims, attempts or variants were resampled independently. No p-values or significance claims. Bootstrap captures query-sampling uncertainty only; it does not characterize generation/judge stochasticity.

## 10. Replication-attribution assessment

| Contrast | |AC Δ| | |Replication AC Δ| | |Net points| | |Replication net| | Macro/net flag | Contrast churn | Replication churn | Churn flag |
|---|---|---|---|---|---|---|---|---|
| A1 | 0.034408602151 | 0.026881720430 | 4 | 2 | False | 4 | 4 | True |
| A2 | 0.000000000000 | 0.026881720430 | 1 | 2 | True | 7 | 4 | False |

The frozen magnitude condition requires both absolute AC macro and absolute net-point effects to be no larger than replication, with at least one nonzero replication difference. The independent gross-churn warning requires replication churn ≥ nonzero contrast churn. Exact rational AC differences determine comparison signs and flags.

A1: macro/net flag **false**; gross-churn flag **true** (4 ≥ 4). A2: macro/net flag **true**; gross-churn flag **false** (4 < 7). **Attribution limited by observed same-configuration replication variation.** This applies to A2 under the required magnitude flag and to A1 under the separately disclosed churn safeguard.

Under Phase 5A §10 and its already-frozen Phase 5B.2-E offline interpretation implementation, nonzero effects meeting either magnitude or churn safeguard receive **Insufficient evidence** before Mixed evidence or supported-contribution labels. This preserves the preexisting conservative interpretation; it introduces no new threshold. The magnitude flag is kept separate from the churn flag rather than relabeled true for A1.

## 11. H1/H2 conclusions

**H1 — Answer Revision.** Frozen hypothesis: “Removing Answer Revision is expected to reduce Answer Completeness on at least some revision-triggered queries, particularly generation-omission cases.”

Full cohort: R2−A1 macro AC +0.034408602151 and net +4 points. R2 revision-triggered stratum: 4 queries / 19 points; R2 9/19 versus A1 5/19, macro 0.566666666667 versus 0.300000000000. Removing revision loses eval005b/P4, eval013/P3, eval013/P4 and eval029/P2; no required point is gained. Three triggered queries worsen and eval007 ties. Thus the narrow expectation of losses on some triggered queries is observed. No new semantic audit establishes a generation-omission causal diagnosis.

H1 final category: **Insufficient evidence** under frozen churn precedence; retain the descriptive revision-associated coverage gain, safety conflicts, single-run caveat, and saving of 7 production LLM calls with A1. No aggregate supported-contribution label is claimed.

**H2 — Evidence Expansion.** Frozen hypothesis: “Removing Evidence Expansion may have limited impact because most observed expansions did not change final Top-5 evidence; however a controlled run is required before concluding the mechanism is unnecessary.”

Full cohort: equal macro AC, but R2 63/102 versus A2 62/102. Across all points, only R2=4 and only A2=3, net R2 +1 and churn 7. The expansion-triggered stratum has 9 queries / 36 points, R2 14/36 versus A2 11/36 and macro 0.446296296296 versus 0.362962962963. Removing Expansion saves 11 retrievals and 9 merge-reranks without saving LLM calls. A2 claim safety summaries are better.

H2 final category: **Insufficient evidence** under the macro/net replication safeguard. The limited full-set macro impact is compatible with H2, while triggered coverage gains and bidirectional point changes prevent a claim that Expansion is unnecessary. Stochastic check disagreements and R2 non-triggered changes are not clean counterfactuals. Do not declare Expansion useless because A2 is cheaper.

**H3: NOT TESTED.** No Citation Revision contribution is inferred.

## 12. Limitations

- 31-query / 102-point benchmark; no claim of universal causality.
- Single production run per configuration and only one R2 same-configuration replication.
- LLM/judge stochasticity is not fully characterized.
- Bootstrap captures query-sampling uncertainty only.
- Triggered strata are post-treatment and descriptive, not randomized subgroups.
- A quota-recovery amendment occurred after evaluation transport failure; immutable accepted observations and recovery receipts remain in provenance.
- Historical R1 full runtime/backend environment was not completely frozen.
- Macro and pooled safety metrics weight observations differently and can disagree.
- Provider-internal retries, tokens and monetary costs are unavailable.

## 13. Phase 5B final conclusion

The complete controlled benchmark is assembled and analyzed with frozen metrics and paired bootstrap. Answer Revision shows a descriptive four-point coverage advantage concentrated in three of four R2-triggered queries; Evidence Expansion has tied full-set macro AC, a one-point net advantage and higher retrieval work. Both final mechanism-attribution categories are **Insufficient evidence** under the predeclared replication safeguards; all safety tradeoffs remain reported.

Historical/frozen artifact integrity: **PASS**. All preexisting project artifacts and separately frozen external assets remained byte-identical. See [integrity before/after](integrity_before_after_v0.json) and [provenance](provenance_v0.json) for scope and hashes. The existing original-seal ephemeral-file exception remains governed solely by the frozen supplemental production-seal protocol; no old seal was rewritten.

**Ready for Phase 5C: YES — for external review. Phase 5C has not started. STOP.** No A3/A4 run, runtime or prompt edit, controller tuning, or further experiment was performed.
