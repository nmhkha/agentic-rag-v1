# Phase 4E — Agentic RAG v1 Trace Analysis

## 1. Executive Summary

**Phase 4E status: PASS.** Read-only post-hoc analysis covers **31/31 production traces and 102/102 query-scoped required points**. No inference, retrieval, external API, new semantic judge, benchmark rerun, threshold tuning or ablation was performed.

Agentic RAG v1 intervened conditionally: 19 queries had **No Substantive Intervention**; 6 used Targeted Evidence Expansion, 7 used Answer Revision and 1 used Citation Revision. Two queries combined interventions. All 31 executed Evidence Coverage Check and Answer Completeness Check; none executed Semantic Citation Check. Checks alone are not Substantive Interventions.

The five oriented benchmark metrics classify **5 Improved, 0 Improved with Trade-off, 23 No Change, 3 Regressed and 0 Inconclusive**. Answer Completeness macro rises from **0.675269 to 0.723656** (+0.048387); micro rises from **60/102 to 65/102** (+5/102). Six required points were gained and one lost. One query is fully rescued and three partially rescued. Regressions are eval001, eval013 and eval027; only eval027 loses a required point.

The production traces record **38 retrieval calls and 108 logical production LLM calls**, averaging 1.225806 and 3.483871 per query. Relative to the frozen Standard runner’s one retrieval and one generation call per query, this is +7 retrieval calls and +77 production LLM calls. Six additional Evidence Merge reranks are outside the retrieval-call total. All configured budgets were respected.

The strongest helpful association is Answer Revision on eval002: the draft exactly matches the frozen Standard answer, evidence content/citation mapping is identical, and the final answer adds the previously unsupported P2. Expansion has mixed associations: only one of six expansions changes final Top-5, and no annotated supporting chunk is added. The largest completeness gain, eval014, occurs with unchanged final evidence and cannot be uniquely attributed to expansion.

**Most important remaining weakness:** internal completeness and success are poor substitutes for benchmark required-point coverage. There are **17 potential completeness false-success / evaluator disagreements**, including **15 success statuses with incomplete benchmark answers**. In addition, macro Groundedness improves while pooled micro Groundedness declines; average improvements should not conceal this change in claim composition.

## 2. Inputs and Integrity

| Input | Identification | Repository path |
|---|---|---|
| Agentic production traces | 31 JSON files; each benchmark trace_path resolved | data/rag/traces/agentic-rag-v1/agentic-v1/ |
| Agentic benchmark results | agentic-rag-eval-v1 / agentic-v1 | data/evaluation/generation/agentic_rag_eval_v1_agentic-v1.jsonl |
| Agentic metrics + manifest | 31 completed, 31 judged | data/evaluation/generation/agentic_rag_metrics_v1_agentic-v1.json |
| Agentic source report | comparison omits Answer Completeness | data/evaluation/generation/reports/agentic_rag_eval_v1_agentic-v1.md |
| Standard benchmark results | standard-rag-eval-v0; Phase 4A control | data/evaluation/generation/standard_rag_eval_v0.jsonl |
| Standard metrics | 31 completed, 102 required points | data/evaluation/generation/standard_rag_metrics_v0.json |
| Standard manifest | frozen retrieval/model/prompt and hashes | data/evaluation/generation/standard_rag_manifest_v0.json |
| Gold + verification manifest | generation-eval-v1; verified; 31/102 | data/evaluation/generation/generation_eval_v1_verified.json; generation_eval_v1_verified_manifest.json |
| Phase 4A points/queries/metrics | phase-4a-standard-rag-failure-analysis-v0 | data/evaluation/generation/failure_analysis_points_v0.jsonl; failure_analysis_queries_v0.json; failure_analysis_metrics_v0.json |
| Corpus | corpus-v0.1 | data/versions/corpus-v0.1/chunks.jsonl |
| Retrieval evaluation | frozen | data/evaluation/retrieval_eval.jsonl |

Authoritative paths were established from the Phase 4A `inputs`, the Standard manifest, the Agentic metrics manifest, the evaluator’s artifact constants and each benchmark row’s `trace_path`. All 31 disk traces equal their embedded benchmark traces, including full state. Query IDs and exact query text align across Standard, Agentic, gold, Phase 4A query records and frozen retrieval evaluation. No duplicate query, missing trace, malformed trace, duplicate trace reference or missing benchmark result was found. All 102 `(query_id, point_id)` pairs reconcile across both benchmarks, verified gold and Phase 4A point records; local IDs such as P1 recur across queries and are not globally unique.

Both systems use `gemini-3.5-flash-lite`, `legal-rag-prompt-v0`, `corpus-v0.1`, and the identical verified generation dataset hash. Frozen Standard retrieval is **BM25-simple-v0 @20 + dense-jina-v3-v0 @20 → union/dedup → BAAI/bge-reranker-v2-m3 → Top-5** (no fusion). Standard dense revision: `ab036b023d30b4d1138c4c3bfa9f0c445ab455d6`; reranker revision: `953dc6f6f85a1b2dbfca4c34a2796e7dde08d41e`. All 31 Agentic Initial Retrieval Top-5 lists equal the frozen Standard lists. Agentic enabled all three intervention mechanisms.

Evaluation compatibility is supported by shared `judge_prompt`, `parse_judge` and `point_audit` functions used by both existing evaluator implementations, the identical required-point set, and reconciliation of every saved score to saved point/claim counts. The Standard manifest records a structured semantic audit using `gemini-3.5-flash-lite` at temperature 0; the Agentic evaluator constructs a separate judge client and enforces the same expected model. Production LLM call lists are separate from evaluator results. This analysis reads source code for schema/method interpretation only and imports no production/evaluation runtime module. Historical source commits and complete judge prompt/response provenance are not fully recorded, so identical historical execution cannot be independently reconstructed beyond the frozen artifacts.

**Source integrity before/after: PASS.** SHA-256 was recorded before analysis and verified again after writing outputs for all 113 snapshotted source files, including corpus, benchmark/gold files, all traces, runtime/evaluator source, prompts, and existing tests. The metrics JSON contains every before/after hash. Available manifest hashes also match current inputs. No source was repaired or modified.

| Source | Before SHA-256 | After SHA-256 | Result |
|---|---|---|---|
| data/versions/corpus-v0.1/chunks.jsonl | 0a6eff1601d14d6409552d566411cc8aebb5f51938402e3f998c312d72d63c67 | 0a6eff1601d14d6409552d566411cc8aebb5f51938402e3f998c312d72d63c67 | PASS |
| data/evaluation/retrieval_eval.jsonl | 659c5cd0ff378747b9b135df00be57e5c1f5681b7eede761d3ce5808afbf3c62 | 659c5cd0ff378747b9b135df00be57e5c1f5681b7eede761d3ce5808afbf3c62 | PASS |
| data/evaluation/generation/generation_eval_v1_verified.json | 1795dbef913e63492c5cd6b8963c2f1a85642ddee0b1a42087f97203bc1895a4 | 1795dbef913e63492c5cd6b8963c2f1a85642ddee0b1a42087f97203bc1895a4 | PASS |
| data/evaluation/generation/standard_rag_eval_v0.jsonl | 691f98cdffe29d6f4f2bfff8ad93c540447ee9cb4c78c3e48c003e2c2c4f487e | 691f98cdffe29d6f4f2bfff8ad93c540447ee9cb4c78c3e48c003e2c2c4f487e | PASS |
| data/evaluation/generation/agentic_rag_eval_v1_agentic-v1.jsonl | a8d6a4bb5f18ddd79d6fcf98d8330b009e44764759e5f135e894528ad715b06e | a8d6a4bb5f18ddd79d6fcf98d8330b009e44764759e5f135e894528ad715b06e | PASS |

Non-blocking source limitations are retained and reported: the original Agentic comparison Markdown/JSON omit Answer Completeness comparison; its summary omits micro Answer Completeness; some gold annotation notes still refer to draft creation even though dataset/item status and the verification manifest are verified. These omissions/stale notes do not change the frozen labels or numerical comparability. The repository is not a Git working tree, as already documented by the Standard manifest.

Exactly three repository files are added: `agentic_trace_analysis_v0.jsonl`, `agentic_trace_analysis_metrics_v0.json`, and this report. To satisfy the three-file restriction while adding deterministic analysis tests, executable analysis, renderer and test code live in `/tmp/phase4e_analysis.py`, `/tmp/phase4e_report.py`, and `/tmp/test_phase4e_analysis.py`. Their exact source text and hashes are archived inside the metrics JSON under `reproducibility`, so reproduction does not depend on temporary-file retention. The complete original source hash inventory is also embedded. **20 deterministic tests pass**, covering duplicate/missing/mismatched inputs, all profiles/outcomes, UCR orientation, point sets, production accounting, aggregate reconciliation, calibration, missing intermediate states, budgets and source integrity. Tests block socket connections. No network/API call occurred.

## 3. Benchmark Reconciliation

| Metric | Standard RAG | Agentic RAG v1 | Raw Agentic − Standard | Oriented improvement |
|---|---|---|---|---|
| Answer Completeness (macro) | 0.675269 | 0.723656 | 0.048387 | 0.048387 |
| Answer Completeness (micro) | 0.588235 | 0.637255 | 0.049020 | 0.049020 |
| Citation Completeness (macro) | 0.675269 | 0.723656 | 0.048387 | 0.048387 |
| Citation Correctness (macro) | 0.961290 | 0.982796 | 0.021505 | 0.021505 |
| Groundedness (macro) | 0.961290 | 0.966667 | 0.005376 | 0.005376 |
| Unsupported Claim Rate (macro) | 0.038710 | 0.033333 | -0.005376 | 0.005376 |

Macro = unweighted mean of 31 per-query values. Answer Completeness micro = total supported required points / 102. Both benchmarks have all five quality metrics available for all 31 queries. Standard per-row Answer Completeness is reconstructed from its persisted supported/required point IDs because its result rows do not have an explicit score field. All recorded macro summaries and comparison deltas reconcile within epsilon = 1e-9. Standard micro and Phase 4A’s 60 supported points also reconcile; Agentic’s 65 supported points reconcile with its summary.

Citation Completeness equals Answer Completeness in this particular frozen run because every supported point is also citation-supported. This equality is observed data, not a general metric definition. Groundedness and Unsupported Claim Rate are complementary here and are not independent evidence of two separate effects. The query outcome classifier uses the requested five metrics regardless of that dependence.

| Additional pooled micro metric | Standard RAG | Agentic RAG v1 | Raw Agentic − Standard |
|---|---|---|---|
| Citation Completeness | 0.588235 | 0.637255 | 0.049020 |
| Citation Correctness | 0.965116 | 0.978723 | 0.013607 |
| Groundedness | 0.965116 | 0.958763 | -0.006353 |
| Unsupported Claim Rate | 0.034884 | 0.041237 | 0.006353 |

Micro Citation Completeness uses 60/102 versus 65/102. Micro Citation Correctness uses 83/86 versus 92/94 cited claims. Micro Groundedness uses **83/86 versus 93/97 total claims**; micro Unsupported Claim Rate uses **3/86 versus 4/97**. Thus pooled Groundedness regresses by 0.006353 and pooled UCR increases by 0.006353, despite favorable macro changes. Claim counts differ between answers and these are additional descriptive aggregates, not matched-claim causal comparisons. They do not replace the frozen macro benchmark or change the specified per-query outcome definitions.

The original Standard citation syntax validity is 30/31 (eval012 invalid); Agentic is 31/31. eval012 performed no Citation Revision and its five specified quality metrics do not change, illustrating why deterministic validator status is reported separately from benchmark semantic citation quality.

## 4. Agent Execution Statistics

| Primary profile | Queries | Rate |
|---|---|---|
| P0 — No Substantive Intervention | 19 | 0.612903 |
| P1 — Evidence Expansion Only | 5 | 0.161290 |
| P2 — Answer Revision Only | 5 | 0.161290 |
| P3 — Citation Revision Only | 0 | 0.000000 |
| P4 — Multiple Interventions | 2 | 0.064516 |

P0–P4 are mutually exclusive and sum to 31. Expansion/Answer Revision/Citation Revision usage counts overlap: the two multiple-intervention cases are eval013 (expansion + Answer Revision) and eval005b (Answer Revision + Citation Revision). No Citation Revision Only query was observed.

| Production calls | Total | Mean | Median | Max | Distribution (calls: queries) |
|---|---|---|---|---|---|
| Retrieval | 38 | 1.225806 | 1 | 3 | {"1": 25, "2": 5, "3": 1} |
| LLM | 108 | 3.483871 | 3 | 6 | {"3": 24, "5": 6, "6": 1} |

| Budget | Configured limit | Maximum observed |
|---|---|---|
| Retrieval expansion rounds | 1 | 1 |
| Subqueries | 3 | 2 |
| Answer Revisions | 1 | 1 |
| Citation Revisions | 1 | 1 |
| Production LLM calls | 6 | 6 |

**Budget compliance: PASS; violations: none.** One expansion round may contain multiple retrieval calls (eval001 has two subqueries and three total retrieval calls). A second completeness call is a Final Completeness Re-check, not a second Answer Revision. The raw transition paths, explicit normalized execution paths, individual retrieval calls, stage lists, coverage/missing aspects, initial/final evidence and retained answers are included for every query in JSONL.

| Query / trace | Actual execution path | Retrieval / production LLM |
|---|---|---|
| [eval001](../../../rag/traces/agentic-rag-v1/agentic-v1/eval001.json) | START → Initial Retrieval → Evidence Coverage Check → Targeted Evidence Expansion (subquery 1) → Targeted Evidence Expansion (subquery 2) → Evidence Merge / Final Evidence Selection → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (insufficient_evidence) | 3 / 3 |
| [eval002](../../../rag/traces/agentic-rag-v1/agentic-v1/eval002.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Answer Revision → Final Completeness Re-check → Deterministic Citation Check → END (success) | 1 / 5 |
| [eval003](../../../rag/traces/agentic-rag-v1/agentic-v1/eval003.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (success) | 1 / 3 |
| [eval004](../../../rag/traces/agentic-rag-v1/agentic-v1/eval004.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (success) | 1 / 3 |
| [eval005a](../../../rag/traces/agentic-rag-v1/agentic-v1/eval005a.json) | START → Initial Retrieval → Evidence Coverage Check → Targeted Evidence Expansion (subquery 1) → Evidence Merge / Final Evidence Selection → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (success) | 2 / 3 |
| [eval005b](../../../rag/traces/agentic-rag-v1/agentic-v1/eval005b.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Answer Revision → Final Completeness Re-check → Deterministic Citation Check → Citation Revision → Deterministic Citation Re-check → END (success) | 1 / 6 |
| [eval006](../../../rag/traces/agentic-rag-v1/agentic-v1/eval006.json) | START → Initial Retrieval → Evidence Coverage Check → Targeted Evidence Expansion (subquery 1) → Evidence Merge / Final Evidence Selection → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (success) | 2 / 3 |
| [eval007](../../../rag/traces/agentic-rag-v1/agentic-v1/eval007.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (success) | 1 / 3 |
| [eval008](../../../rag/traces/agentic-rag-v1/agentic-v1/eval008.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (success) | 1 / 3 |
| [eval009](../../../rag/traces/agentic-rag-v1/agentic-v1/eval009.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (success) | 1 / 3 |
| [eval010](../../../rag/traces/agentic-rag-v1/agentic-v1/eval010.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Answer Revision → Final Completeness Re-check → Deterministic Citation Check → END (incomplete_answer) | 1 / 5 |
| [eval011](../../../rag/traces/agentic-rag-v1/agentic-v1/eval011.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (success) | 1 / 3 |
| [eval012](../../../rag/traces/agentic-rag-v1/agentic-v1/eval012.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (success) | 1 / 3 |
| [eval013](../../../rag/traces/agentic-rag-v1/agentic-v1/eval013.json) | START → Initial Retrieval → Evidence Coverage Check → Targeted Evidence Expansion (subquery 1) → Evidence Merge / Final Evidence Selection → Answer Generation → Answer Completeness Check → Answer Revision → Final Completeness Re-check → Deterministic Citation Check → END (success) | 2 / 5 |
| [eval014](../../../rag/traces/agentic-rag-v1/agentic-v1/eval014.json) | START → Initial Retrieval → Evidence Coverage Check → Targeted Evidence Expansion (subquery 1) → Evidence Merge / Final Evidence Selection → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (insufficient_evidence) | 2 / 3 |
| [eval015](../../../rag/traces/agentic-rag-v1/agentic-v1/eval015.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (success) | 1 / 3 |
| [eval016](../../../rag/traces/agentic-rag-v1/agentic-v1/eval016.json) | START → Initial Retrieval → Evidence Coverage Check → Targeted Evidence Expansion (subquery 1) → Evidence Merge / Final Evidence Selection → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (success) | 2 / 3 |
| [eval017](../../../rag/traces/agentic-rag-v1/agentic-v1/eval017.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (success) | 1 / 3 |
| [eval018](../../../rag/traces/agentic-rag-v1/agentic-v1/eval018.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (success) | 1 / 3 |
| [eval019](../../../rag/traces/agentic-rag-v1/agentic-v1/eval019.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (success) | 1 / 3 |
| [eval020](../../../rag/traces/agentic-rag-v1/agentic-v1/eval020.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (success) | 1 / 3 |
| [eval021](../../../rag/traces/agentic-rag-v1/agentic-v1/eval021.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (success) | 1 / 3 |
| [eval022](../../../rag/traces/agentic-rag-v1/agentic-v1/eval022.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Answer Revision → Final Completeness Re-check → Deterministic Citation Check → END (success) | 1 / 5 |
| [eval023](../../../rag/traces/agentic-rag-v1/agentic-v1/eval023.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (success) | 1 / 3 |
| [eval024](../../../rag/traces/agentic-rag-v1/agentic-v1/eval024.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (success) | 1 / 3 |
| [eval025](../../../rag/traces/agentic-rag-v1/agentic-v1/eval025.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (success) | 1 / 3 |
| [eval026](../../../rag/traces/agentic-rag-v1/agentic-v1/eval026.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Answer Revision → Final Completeness Re-check → Deterministic Citation Check → END (success) | 1 / 5 |
| [eval027](../../../rag/traces/agentic-rag-v1/agentic-v1/eval027.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (success) | 1 / 3 |
| [eval028](../../../rag/traces/agentic-rag-v1/agentic-v1/eval028.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (success) | 1 / 3 |
| [eval029](../../../rag/traces/agentic-rag-v1/agentic-v1/eval029.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Answer Revision → Final Completeness Re-check → Deterministic Citation Check → END (success) | 1 / 5 |
| [eval030](../../../rag/traces/agentic-rag-v1/agentic-v1/eval030.json) | START → Initial Retrieval → Evidence Coverage Check → Answer Generation → Answer Completeness Check → Deterministic Citation Check → END (success) | 1 / 3 |

## 5. Evidence Expansion Analysis

Targeted Evidence Expansion ran for **6 queries**, with **25 without expansion**. Seven subqueries were issued (mean **1.166667** among expanded queries). Final Top-5 order and membership changed in **1/6** and were unchanged in **5/6**. The mean newly introduced final evidence count is **0.166667** among expanded queries (0.032258 across all queries). No rank-only changes were observed.

| Query | Subqueries | Expanded unique candidates | Final Top-5 changed | Added / removed | Gold support added | Observation |
|---|---|---|---|---|---|---|
| [eval001](../../../rag/traces/agentic-rag-v1/agentic-v1/eval001.json) | 2 | 47 | True | 1 / 1 | 0 | observed_regression |
| [eval005a](../../../rag/traces/agentic-rag-v1/agentic-v1/eval005a.json) | 1 | 30 | False | 0 / 0 | 0 | no_observed_gain |
| [eval006](../../../rag/traces/agentic-rag-v1/agentic-v1/eval006.json) | 1 | 32 | False | 0 / 0 | 0 | no_observed_gain |
| [eval013](../../../rag/traces/agentic-rag-v1/agentic-v1/eval013.json) | 1 | 30 | False | 0 / 0 | 0 | observed_regression |
| [eval014](../../../rag/traces/agentic-rag-v1/agentic-v1/eval014.json) | 1 | 29 | False | 0 / 0 | 0 | observed_gain |
| [eval016](../../../rag/traces/agentic-rag-v1/agentic-v1/eval016.json) | 1 | 29 | False | 0 / 0 | 0 | observed_gain |

**Post-hoc gold-support overlap only:** none of the expanded queries adds or removes a chunk in the union of the query’s annotated required-point supporting sets. This is not semantic sufficiency: non-gold chunks may support a proposition. Only eval001 changes final evidence, adding `134-2025-QH15_dieu-10_khoan-3` and removing `142-2026-ND-CP_dieu-8_khoan-1_diem-a`. The missing low-risk definition (`134-2025-QH15_dieu-9_khoan-1_diem-c`) appears in expanded candidates but remains outside final Top-5. There is no observed removal of an annotated required-point supporting chunk; usefulness beyond gold overlap is not established.

Expansion has 2 observed gains, 2 no-observed-gain outcomes and 2 regressions. The two gains (eval014 and eval016) both retain the same final Top-5 content and citation mapping. eval013 combines expansion and Answer Revision: **multiple interventions — attribution not isolated**. Existing artifacts do not isolate expansion as the explanation for final metric changes.

### [eval001](../../../rag/traces/agentic-rag-v1/agentic-v1/eval001.json)

Các mức phân loại rủi ro của hệ thống trí tuệ nhân tạo gồm những mức nào?

Coverage missing aspects: ["Danh mục đầy đủ các mức phân loại rủi ro của hệ thống trí tuệ nhân tạo (hiện tại các văn bản chỉ đề cập đến rủi ro trung bình và rủi ro cao)", "Quy định chi tiết về hệ thống trí tuệ nhân tạo có rủi ro thấp hoặc rủi ro không đáng kể nếu có"].

Targeted subqueries: ["Danh mục đầy đủ các mức phân loại rủi ro của hệ thống trí tuệ nhân tạo (hiện tại các văn bản chỉ đề cập đến rủi ro trung bình và rủi ro cao) Các mức phân loại rủi ro của hệ thống trí tuệ nhân tạo gồm những mức nào?", "Quy định chi tiết về hệ thống trí tuệ nhân tạo có rủi ro thấp hoặc rủi ro không đáng kể nếu có Các mức phân loại rủi ro của hệ thống trí tuệ nhân tạo gồm những mức nào?"].

Initial Top-5: `134-2025-QH15_dieu-9_khoan-1_diem-b`, `134-2025-QH15_dieu-9_khoan-2`, `134-2025-QH15_dieu-9_khoan-1_diem-a`, `134-2025-QH15_dieu-10_khoan-1`, `142-2026-ND-CP_dieu-8_khoan-1_diem-a`.

Final Top-5: `134-2025-QH15_dieu-9_khoan-1_diem-b`, `134-2025-QH15_dieu-9_khoan-2`, `134-2025-QH15_dieu-9_khoan-1_diem-a`, `134-2025-QH15_dieu-10_khoan-3`, `134-2025-QH15_dieu-10_khoan-1`.

Added: `134-2025-QH15_dieu-10_khoan-3`; removed: `142-2026-ND-CP_dieu-8_khoan-1_diem-a`.

Expansion adds article 10 clause 3 and removes a non-gold initial chunk, but the missing low-risk definition remains outside final Top-5. The draft/final answer adds a low-risk mention and still abstains. Frozen groundedness falls from 1 to 0.5; the judge retains aggregate claim counts, not claim-specific reasons. No Answer Revision or Citation Revision occurred. Evidence removal of a required-point supporting chunk is not observed. single intervention; observational association only.

### [eval005a](../../../rag/traces/agentic-rag-v1/agentic-v1/eval005a.json)

Nhà cung cấp hệ thống trí tuệ nhân tạo có rủi ro cao phải thực hiện những nghĩa vụ quản lý nào?

Coverage missing aspects: ["Quy định chi tiết về các nghĩa vụ quản lý cụ thể khác ngoài việc thiết lập hệ thống quản lý rủi ro và cung cấp thông tin cho bên triển khai của nhà cung cấp hệ thống trí tuệ nhân tạo có rủi ro cao."].

Targeted subqueries: ["Quy định chi tiết về các nghĩa vụ quản lý cụ thể khác ngoài việc thiết lập hệ thống quản lý rủi ro và cung cấp thông tin cho bên triển khai của nhà cung cấp hệ thống trí tuệ nhân tạo có rủi ro cao. Nhà cung cấp hệ thống trí tuệ nhân tạo có rủi ro cao phải thực hiện những nghĩa vụ quản lý nào?"].

Initial Top-5: `142-2026-ND-CP_dieu-15_khoan-1`, `134-2025-QH15_dieu-14_khoan-3`, `134-2025-QH15_dieu-14_khoan-5`, `142-2026-ND-CP_dieu-15_khoan-3`, `134-2025-QH15_dieu-14_khoan-6`.

Final Top-5: `142-2026-ND-CP_dieu-15_khoan-1`, `134-2025-QH15_dieu-14_khoan-3`, `134-2025-QH15_dieu-14_khoan-5`, `142-2026-ND-CP_dieu-15_khoan-3`, `134-2025-QH15_dieu-14_khoan-6`.

Added: —; removed: —.

Expansion leaves ordered Top-5 unchanged. Neither answer covers any of the seven complete required propositions according to the frozen evaluator; the internal complete decision and success status disagree with benchmark completeness 0. single intervention; observational association only.

### [eval006](../../../rag/traces/agentic-rag-v1/agentic-v1/eval006.json)

Trách nhiệm minh bạch của nhà cung cấp hệ thống trí tuệ nhân tạo bao gồm những gì?

Coverage missing aspects: ["Nội dung chi tiết của Khoản 4 Điều 11 Luật Trí tuệ nhân tạo quy định về trách nhiệm minh bạch của nhà cung cấp hệ thống trí tuệ nhân tạo"].

Targeted subqueries: ["Nội dung chi tiết của Khoản 4 Điều 11 Luật Trí tuệ nhân tạo quy định về trách nhiệm minh bạch của nhà cung cấp hệ thống trí tuệ nhân tạo Trách nhiệm minh bạch của nhà cung cấp hệ thống trí tuệ nhân tạo bao gồm những gì?"].

Initial Top-5: `142-2026-ND-CP_dieu-16_khoan-1`, `134-2025-QH15_dieu-11_khoan-1`, `134-2025-QH15_dieu-11_khoan-2`, `134-2025-QH15_dieu-11_khoan-3`, `134-2025-QH15_dieu-11_khoan-5`.

Final Top-5: `142-2026-ND-CP_dieu-16_khoan-1`, `134-2025-QH15_dieu-11_khoan-1`, `134-2025-QH15_dieu-11_khoan-2`, `134-2025-QH15_dieu-11_khoan-3`, `134-2025-QH15_dieu-11_khoan-5`.

Added: —; removed: —.

Expansion leaves ordered Top-5 unchanged; all five quality metrics remain unchanged and Answer Completeness stays 1. The trigger sought another clause beyond the already satisfied frozen required points; this does not prove the trigger incorrect. single intervention; observational association only.

### [eval013](../../../rag/traces/agentic-rag-v1/agentic-v1/eval013.json)

Việc phân loại cấp độ thử nghiệm có kiểm soát dựa trên những tiêu chí nào?

Coverage missing aspects: ["Chi tiết toàn bộ danh mục các tiêu chí cụ thể quy định tại Khoản 1 Điều 22 Nghị định 142/2026/NĐ-CP (hiện tại thiếu các điểm a và b của khoản này)"].

Targeted subqueries: ["Chi tiết toàn bộ danh mục các tiêu chí cụ thể quy định tại Khoản 1 Điều 22 Nghị định 142/2026/NĐ-CP (hiện tại thiếu các điểm a và b của khoản này) Việc phân loại cấp độ thử nghiệm có kiểm soát dựa trên những tiêu chí nào?"].

Initial Top-5: `142-2026-ND-CP_dieu-22_khoan-2`, `142-2026-ND-CP_dieu-22_khoan-6`, `142-2026-ND-CP_dieu-22_khoan-1_diem-c`, `142-2026-ND-CP_dieu-22_khoan-1_diem-d`, `142-2026-ND-CP_dieu-22_khoan-5_diem-a`.

Final Top-5: `142-2026-ND-CP_dieu-22_khoan-2`, `142-2026-ND-CP_dieu-22_khoan-6`, `142-2026-ND-CP_dieu-22_khoan-1_diem-c`, `142-2026-ND-CP_dieu-22_khoan-1_diem-d`, `142-2026-ND-CP_dieu-22_khoan-5_diem-a`.

Added: —; removed: —.

Expansion leaves ordered Top-5 unchanged. Answer Revision appends the highest-applicable-testing-level sentence, which was already in the frozen Standard answer. Citation Correctness and Groundedness fall to 0.8, while completeness stays 0.6. The final judge gives aggregate claim counts without locating its unsupported claim; no evidence establishes that revision introduced unsupported content. multiple interventions — attribution not isolated.

### [eval014](../../../rag/traces/agentic-rag-v1/agentic-v1/eval014.json)

Hồ sơ thông thường để tham gia cơ chế thử nghiệm có kiểm soát gồm những thành phần nào?

Coverage missing aspects: ["Các thành phần tài liệu pháp lý hoặc giấy tờ tùy thân khác trong hồ sơ ngoài đơn đề nghị, đề án thử nghiệm và tài liệu mô tả năng lực kỹ thuật"].

Targeted subqueries: ["Các thành phần tài liệu pháp lý hoặc giấy tờ tùy thân khác trong hồ sơ ngoài đơn đề nghị, đề án thử nghiệm và tài liệu mô tả năng lực kỹ thuật Hồ sơ thông thường để tham gia cơ chế thử nghiệm có kiểm soát gồm những thành phần nào?"].

Initial Top-5: `142-2026-ND-CP_dieu-24_khoan-2_diem-a`, `142-2026-ND-CP_dieu-24_khoan-3_diem-a`, `142-2026-ND-CP_dieu-24_khoan-1_diem-b`, `142-2026-ND-CP_dieu-24_khoan-2_diem-d`, `142-2026-ND-CP_dieu-23_khoan-2`.

Final Top-5: `142-2026-ND-CP_dieu-24_khoan-2_diem-a`, `142-2026-ND-CP_dieu-24_khoan-3_diem-a`, `142-2026-ND-CP_dieu-24_khoan-1_diem-b`, `142-2026-ND-CP_dieu-24_khoan-2_diem-d`, `142-2026-ND-CP_dieu-23_khoan-2`.

Added: —; removed: —.

Expansion leaves ordered Top-5 unchanged. The generated draft/final answer gives more detail for application forms and testing-project contents; the frozen evaluator gains P1, P2 and P4 despite continued abstention. Expansion did not introduce final evidence, so its contribution is not isolated from generation/evaluator variation. single intervention; observational association only.

### [eval016](../../../rag/traces/agentic-rag-v1/agentic-v1/eval016.json)

Tổ chức hoặc cá nhân phải báo cáo gì trong quá trình thử nghiệm có kiểm soát?

Coverage missing aspects: ["Nội dung chi tiết và tần suất của báo cáo định kỳ trong quá trình thử nghiệm"].

Targeted subqueries: ["Nội dung chi tiết và tần suất của báo cáo định kỳ trong quá trình thử nghiệm Tổ chức hoặc cá nhân phải báo cáo gì trong quá trình thử nghiệm có kiểm soát?"].

Initial Top-5: `142-2026-ND-CP_dieu-25_khoan-4`, `142-2026-ND-CP_dieu-25_khoan-1_diem-b`, `142-2026-ND-CP_dieu-25_khoan-3_diem-b`, `142-2026-ND-CP_dieu-25_khoan-1_diem-a`, `142-2026-ND-CP_dieu-25_khoan-1_diem-c`.

Final Top-5: `142-2026-ND-CP_dieu-25_khoan-4`, `142-2026-ND-CP_dieu-25_khoan-1_diem-b`, `142-2026-ND-CP_dieu-25_khoan-3_diem-b`, `142-2026-ND-CP_dieu-25_khoan-1_diem-a`, `142-2026-ND-CP_dieu-25_khoan-1_diem-c`.

Added: —; removed: —.

Expansion leaves ordered Top-5 unchanged. The new answer omits several specific form identifiers present in Standard; the frozen evaluator reports higher citation correctness and groundedness, with unchanged required-point coverage. This is consistent with a narrower answer but does not isolate an expansion effect. single intervention; observational association only.

## 6. Answer Revision Analysis

**7 queries used Answer Revision**, and all seven have text changes between stored draft and final answer. Three final outcomes improve relative to Standard, three are unchanged, and one regresses. Five are Answer Revision Only; eval013 also expands and eval005b also revises citations.

| Query | Profile | Draft → final text changed | Initial internal complete | Last internal complete | Standard AC → Agentic AC | Final outcome |
|---|---|---|---|---|---|---|
| [eval002](../../../rag/traces/agentic-rag-v1/agentic-v1/eval002.json) | P2 — Answer Revision Only | True | not retained (false inferred from branch) | True | 0.500000 → 1.000000 | O1 — Improved |
| [eval005b](../../../rag/traces/agentic-rag-v1/agentic-v1/eval005b.json) | P4 — Multiple Interventions | True | not retained (false inferred from branch) | True | 0.000000 → 0.166667 | O1 — Improved |
| [eval010](../../../rag/traces/agentic-rag-v1/agentic-v1/eval010.json) | P2 — Answer Revision Only | True | not retained (false inferred from branch) | False | 1.000000 → 1.000000 | O3 — No Change |
| [eval013](../../../rag/traces/agentic-rag-v1/agentic-v1/eval013.json) | P4 — Multiple Interventions | True | not retained (false inferred from branch) | True | 0.600000 → 0.600000 | O4 — Regressed |
| [eval022](../../../rag/traces/agentic-rag-v1/agentic-v1/eval022.json) | P2 — Answer Revision Only | True | not retained (false inferred from branch) | True | 0.000000 → 0.333333 | O1 — Improved |
| [eval026](../../../rag/traces/agentic-rag-v1/agentic-v1/eval026.json) | P2 — Answer Revision Only | True | not retained (false inferred from branch) | True | 1.000000 → 1.000000 | O3 — No Change |
| [eval029](../../../rag/traces/agentic-rag-v1/agentic-v1/eval029.json) | P2 — Answer Revision Only | True | not retained (false inferred from branch) | True | 1.000000 → 1.000000 | O3 — No Change |

The trace stores only the final completeness payload, overwriting the initial result. The initial false decision can be inferred from the recorded Answer Revision transition and controller branch, but its missing-points list/reason cannot be recovered. Those fields are null in JSONL with an explicit availability note. No new judge was introduced. No query is marked as having a directly confirmed separately benchmarked draft-to-final effect. eval002 provides unusually strong evidence through an exact draft match to the frozen Standard answer with identical evidence content and citation mapping; this is labelled a frozen-Standard draft proxy, and historical evaluator variation still cannot be excluded.

For eval005b, draft-to-final differences span both Answer Revision and Citation Revision. The intermediate answer immediately before Citation Revision is absent. In all cases distinguish “revision changed the answer” and “final Agentic result improved relative to Standard” from an isolated contribution of revision.

### [eval002](../../../rag/traces/agentic-rag-v1/agentic-v1/eval002.json)

Ai có thẩm quyền ban hành danh mục hệ thống trí tuệ nhân tạo có rủi ro cao?

Answer Revision adds the ministry coordination/submission responsibility (P2) with citation E2. Draft text exactly matches the frozen Standard answer and the evidence content/citation map is identical. This is the strongest trace-consistent revision association; the frozen Standard audit is an exact-draft proxy, not a separately run draft audit.

**Pre-revision draft:**

Thủ tướng Chính phủ có thẩm quyền xem xét và ban hành Danh mục hệ thống trí tuệ nhân tạo có rủi ro cao [E1][E2][E5].

**Final answer:**

Thủ tướng Chính phủ có thẩm quyền xem xét và ban hành Danh mục hệ thống trí tuệ nhân tạo có rủi ro cao [E1][E2][E5]. Bên cạnh đó, Bộ Khoa học và Công nghệ có trách nhiệm chủ trì, phối hợp với các bộ, cơ quan ngang bộ và các tổ chức liên quan tổng hợp, xây dựng và trình Thủ tướng Chính phủ ban hành, sửa đổi, bổ sung danh mục này [E2].

Final internal check: {"complete": true, "missing_points": [], "reason": "Câu trả lời đã nêu đầy đủ thẩm quyền ban hành của Thủ tướng Chính phủ và trách nhiệm xây dựng, trình của Bộ Khoa học và Công nghệ theo đúng các tài liệu được cung cấp.", "scope": "final answer", "recheck_used": true}.

### [eval005b](../../../rag/traces/agentic-rag-v1/agentic-v1/eval005b.json)

Bên triển khai hệ thống trí tuệ nhân tạo có rủi ro cao phải thực hiện những nghĩa vụ quản lý nào?

Answer Revision and Citation Revision occur on unchanged evidence. The final answer adds transparency and incident-handling obligations (P4). Citation recheck passes, but the answer between the two revisions and the original validator errors were not retained. Their separate contributions cannot be isolated; the final completeness decision precedes Citation Revision.

**Pre-revision draft:**

Bên triển khai hệ thống trí tuệ nhân tạo có rủi ro cao phải tổ chức quản lý rủi ro trong quá trình triển khai và vận hành hệ thống phù hợp với mục đích sử dụng, phạm vi triển khai, mức độ rủi ro của hệ thống và hướng dẫn kỹ thuật của nhà cung cấp [E1].

**Final answer:**

Bên triển khai hệ thống trí tuệ nhân tạo có rủi ro cao phải tổ chức quản lý rủi ro trong quá trình triển khai và vận hành hệ thống phù hợp với mục đích sử dụng, phạm vi triển khai, mức độ rủi ro của hệ thống và hướng dẫn kỹ thuật của nhà cung cấp [E1]. Bên cạnh đó, bên triển khai còn phải thực hiện nghĩa vụ minh bạch và xử lý sự cố theo quy định tại Điều 11 và Điều 12 của Luật Trí tuệ nhân tạo [E4] [E5].

Final internal check: {"complete": true, "missing_points": [], "reason": "Câu trả lời đã bao quát đầy đủ các nghĩa vụ quản lý của bên triển khai hệ thống trí tuệ nhân tạo có rủi ro cao được nêu trong các tài liệu chứng cứ (quản lý rủi ro, nghĩa vụ minh bạch và xử lý sự cố).", "scope": "last internal completeness decision; before Citation Revision", "recheck_used": true}.

### [eval010](../../../rag/traces/agentic-rag-v1/agentic-v1/eval010.json)

Nhà cung cấp cần làm gì khi phát hiện sự cố liên quan đến hệ thống trí tuệ nhân tạo?

Answer Revision changes the reporting sentence, yet benchmark completeness stays 1. The final internal checker requests an explanation obligation associated with E5 beyond the two frozen required points and returns incomplete_answer. This illustrates a difference in target definitions, not a formal checker false positive/negative.

**Pre-revision draft:**

Khi phát hiện sự cố liên quan đến hệ thống trí tuệ nhân tạo, nhà cung cấp có trách nhiệm kịp thời phát hiện và khắc phục sự cố có khả năng gây tổn hại đến con người, tài sản, dữ liệu hoặc trật tự xã hội [E1]. Nhà cung cấp phải khẩn trương áp dụng biện pháp kỹ thuật để khắc phục, tạm dừng hoặc thu hồi hệ thống, đồng thời thông báo cho cơ quan có thẩm quyền [E2]; áp dụng các biện pháp kỹ thuật cần thiết để ngăn chặn, hạn chế và khắc phục hậu quả của sự cố [E4]; duy trì, lưu giữ nhật ký hệ thống, dữ liệu và thông tin liên quan đến sự cố để phục vụ việc xác minh, đánh giá và khắc phục sự cố [E3]; đồng thời gửi báo cáo chính thức về kết quả khắc phục sự cố cho cơ quan nhà nước có thẩm quyền trong thời hạn 15 ngày kể từ ngày nộp báo cáo sơ bộ [E3].

**Final answer:**

Khi phát hiện sự cố liên quan đến hệ thống trí tuệ nhân tạo, nhà cung cấp có trách nhiệm kịp thời phát hiện và khắc phục sự cố có khả năng gây tổn hại đến con người, tài sản, dữ liệu hoặc trật tự xã hội [E1]. Nhà cung cấp phải khẩn trương áp dụng biện pháp kỹ thuật để khắc phục, tạm dừng hoặc thu hồi hệ thống, đồng thời thông báo cho cơ quan có thẩm quyền [E2]; áp dụng các biện pháp kỹ thuật cần thiết để ngăn chặn, hạn chế và khắc phục hậu quả của sự cố [E4]; duy trì, lưu giữ nhật ký hệ thống, dữ liệu và thông tin liên quan đến sự cố để phục vụ việc xác minh, đánh giá và khắc phục sự cố [E3]. Ngoài ra, nhà cung cấp phải gửi báo cáo sơ bộ về sự cố cho cơ quan nhà nước có thẩm quyền và gửi báo cáo chính thức về kết quả khắc phục sự cố trong thời hạn 15 ngày kể từ ngày nộp báo cáo sơ bộ [E3].

Final internal check: {"complete": false, "missing_points": ["Nhà cung cấp chưa được đề cập trách nhiệm giải trình về mục đích sử dụng, nguyên lý hoạt động, dữ liệu đầu vào và biện pháp quản lý rủi ro, an toàn khi có yêu cầu của cơ quan nhà nước hoặc khi có dấu hiệu rủi ro, sự cố theo E5."], "reason": "Câu trả lời bỏ sót nghĩa vụ giải trình của nhà cung cấp khi xảy ra sự cố theo quy định tại E5.", "scope": "final answer", "recheck_used": true}.

### [eval013](../../../rag/traces/agentic-rag-v1/agentic-v1/eval013.json)

Việc phân loại cấp độ thử nghiệm có kiểm soát dựa trên những tiêu chí nào?

Expansion leaves ordered Top-5 unchanged. Answer Revision appends the highest-applicable-testing-level sentence, which was already in the frozen Standard answer. Citation Correctness and Groundedness fall to 0.8, while completeness stays 0.6. The final judge gives aggregate claim counts without locating its unsupported claim; no evidence establishes that revision introduced unsupported content.

**Pre-revision draft:**

Việc phân loại cấp độ thử nghiệm có kiểm soát được xác định trên cơ sở chức năng, mục đích sử dụng và tác động tổng thể của hệ thống trí tuệ nhân tạo (bao gồm cả trường hợp hệ thống triển khai qua nhiều thành phần, mô-đun hoặc dịch vụ kết hợp) [E1]. Bên cạnh đó, việc phân loại còn dựa trên các tiêu chí cụ thể như phạm vi và quy mô triển khai thử nghiệm (gồm địa bàn triển khai, số lượng điểm thử nghiệm, đối tượng tham gia thử nghiệm và mức độ kết nối với hệ thống dữ liệu hoặc hệ thống thông tin) [E3], mức độ tác động đối với an ninh quốc gia, trật tự, an toàn xã hội và quyền, lợi ích hợp pháp của tổ chức, cá nhân [E4], cũng như tiêu chí cụ thể để xác định đối tượng tham gia thử nghiệm [E5].

**Final answer:**

Việc phân loại cấp độ thử nghiệm có kiểm soát được xác định trên cơ sở chức năng, mục đích sử dụng và tác động tổng thể của hệ thống trí tuệ nhân tạo (bao gồm cả trường hợp hệ thống triển khai qua nhiều thành phần, mô-đun hoặc dịch vụ kết hợp) [E1]. Bên cạnh đó, việc phân loại còn dựa trên các tiêu chí cụ thể như phạm vi và quy mô triển khai thử nghiệm (gồm địa bàn triển khai, số lượng điểm thử nghiệm, đối tượng tham gia thử nghiệm và mức độ kết nối với hệ thống dữ liệu hoặc hệ thống thông tin) [E3], mức độ tác động đối với an ninh quốc gia, trật tự, an toàn xã hội và quyền, lợi ích hợp pháp của tổ chức, cá nhân [E4], cũng như tiêu chí cụ thể để xác định đối tượng tham gia thử nghiệm [E5]. Ngoài ra, trường hợp hệ thống trí tuệ nhân tạo đồng thời đáp ứng tiêu chí của nhiều cấp độ thử nghiệm khác nhau thì hệ thống được phân loại theo cấp độ thử nghiệm cao nhất [E1].

Final internal check: {"complete": true, "missing_points": [], "reason": "Câu trả lời đã bao gồm đầy đủ các tiêu chí phân loại cấp độ thử nghiệm có kiểm soát theo các tài liệu chứng cứ được cung cấp.", "scope": "final answer", "recheck_used": true}.

### [eval022](../../../rag/traces/agentic-rag-v1/agentic-v1/eval022.json)

Cơ quan quản lý có trách nhiệm gì đối với việc xây dựng và cập nhật dữ liệu mở phục vụ AI?

Answer Revision appends the agency database collection/quality/annotation responsibility with E1. The frozen evaluator gains P2 and improves all five oriented metrics, while P1 and P3 remain unsupported. Evidence stays unchanged; draft benchmark scores were not retained.

**Pre-revision draft:**

Bằng chứng hiện tại chưa đủ để kết luận về trách nhiệm cụ thể của cơ quan quản lý đối với riêng việc xây dựng và cập nhật "dữ liệu mở" phục vụ AI. Bằng chứng [E5] chỉ quy định chung về trách nhiệm "Xây dựng, cập nhật dữ liệu mở, dữ liệu mở có điều kiện, dữ liệu thương mại thuộc phạm vi quản lý" mà chưa làm rõ mối liên hệ trực tiếp với dữ liệu mở phục vụ AI.

**Final answer:**

Bằng chứng hiện tại chưa đủ để kết luận về trách nhiệm cụ thể của cơ quan quản lý đối với riêng việc xây dựng và cập nhật "dữ liệu mở" phục vụ AI. Bằng chứng [E5] chỉ quy định chung về trách nhiệm "Xây dựng, cập nhật dữ liệu mở, dữ liệu mở có điều kiện, dữ liệu thương mại thuộc phạm vi quản lý" mà chưa làm rõ mối liên hệ trực tiếp với dữ liệu mở phục vụ AI. Tuy nhiên, theo Khoản 4 Điều 43 Nghị định 142/2026/NĐ-CP, cơ quan quản lý có trách nhiệm tổ chức thu thập, tạo lập, bảo đảm chất lượng, gán nhãn, chú thích, chuẩn hóa, quản lý, khai thác cơ sở dữ liệu phục vụ trí tuệ nhân tạo thuộc phạm vi quản lý [E1].

Final internal check: {"complete": true, "missing_points": [], "reason": "The answer accurately addresses the query using the provided evidence, citing both the general provision on open data [E5] and the specific responsibilities regarding databases for artificial intelligence [E1].", "scope": "final answer", "recheck_used": true}.

### [eval026](../../../rag/traces/agentic-rag-v1/agentic-v1/eval026.json)

Báo cáo đánh giá tác động khi sử dụng AI trong khu vực công cần đề cập những nội dung gì?

Answer Revision adds system description and intended use (E5), which the Standard answer already included. Final metrics remain at 1 for completeness/citations/groundedness and 0 unsupported rate. No gain over Standard does not exclude recovery from an incomplete Agentic draft.

**Pre-revision draft:**

Báo cáo đánh giá tác động khi sử dụng hệ thống trí tuệ nhân tạo (có rủi ro cao hoặc có tác động đáng kể đến quyền con người, công bằng xã hội hoặc lợi ích công cộng) bao gồm các nội dung về việc xác định rủi ro, các biện pháp kiểm soát và bảo đảm khả năng giám sát, can thiệp của con người [E1].

**Final answer:**

Báo cáo đánh giá tác động khi sử dụng hệ thống trí tuệ nhân tạo (có rủi ro cao hoặc có tác động đáng kể đến quyền con người, công bằng xã hội hoặc lợi ích công cộng) bao gồm thông tin mô tả hệ thống trí tuệ nhân tạo và mục đích sử dụng [E5], việc xác định rủi ro, các biện pháp kiểm soát và bảo đảm khả năng giám sát, can thiệp của con người [E1].

Final internal check: {"complete": true, "missing_points": [], "reason": "Câu trả lời đã bao gồm đầy đủ các nội dung theo yêu cầu của văn bản pháp luật được cung cấp trong các chứng cứ.", "scope": "final answer", "recheck_used": true}.

### [eval029](../../../rag/traces/agentic-rag-v1/agentic-v1/eval029.json)

Theo Khung đạo đức trí tuệ nhân tạo quốc gia, khi hệ thống AI có thể ảnh hưởng đáng kể đến quyền con người thì cần áp dụng những biện pháp kiểm soát nào?

Answer Revision appends an impact-assessment report obligation (E4), while the two frozen required points and all five quality metrics remain unchanged. The added material extends beyond the frozen point set; it is not evidence of a wrong trigger.

**Pre-revision draft:**

Theo Khung đạo đức trí tuệ nhân tạo quốc gia, tổ chức và cá nhân phải áp dụng các biện pháp rà soát phù hợp nhằm bảo đảm hệ thống trí tuệ nhân tạo không xâm phạm quyền riêng tư, dữ liệu cá nhân, tự do ý chí, quyền tiếp cận thông tin, quyền được đối xử bình đẳng và các quyền hợp pháp khác [E1]. Đồng thời, cần xây dựng cơ chế giám sát và can thiệp của con người phù hợp với mức độ ảnh hưởng, bảo đảm duy trì sự kiểm soát và khả năng can thiệp của con người đối với mọi quyết định và hành vi của hệ thống [E2]. Ngoài ra, tổ chức và cá nhân phải áp dụng biện pháp bảo vệ phù hợp để phòng ngừa, phát hiện, ngăn chặn và ứng phó với các hành vi xâm nhập, chiếm quyền điều khiển, tấn công, rò rỉ dữ liệu và lạm dụng hệ thống [E3].

**Final answer:**

Theo Khung đạo đức trí tuệ nhân tạo quốc gia, tổ chức và cá nhân phải áp dụng các biện pháp rà soát phù hợp nhằm bảo đảm hệ thống trí tuệ nhân tạo không xâm phạm quyền riêng tư, dữ liệu cá nhân, tự do ý chí, quyền tiếp cận thông tin, quyền được đối xử bình đẳng và các quyền hợp pháp khác [E1]. Đồng thời, cần xây dựng cơ chế giám sát và can thiệp của con người phù hợp với mức độ ảnh hưởng, bảo đảm duy trì sự kiểm soát và khả năng can thiệp của con người đối với mọi quyết định và hành vi của hệ thống [E2]. Ngoài ra, tổ chức và cá nhân phải áp dụng biện pháp bảo vệ phù hợp để phòng ngừa, phát hiện, ngăn chặn và ứng phó với các hành vi xâm nhập, chiếm quyền điều khiển, tấn công, rò rỉ dữ liệu và lạm dụng hệ thống [E3]. Bên cạnh đó, theo quy định về hệ thống trí tuệ nhân tạo có tác động đáng kể đến quyền con người, cơ quan vận hành hệ thống phải lập báo cáo đánh giá tác động việc sử dụng hệ thống, bao gồm việc xác định rủi ro, biện pháp kiểm soát và bảo đảm khả năng giám sát, can thiệp của con người [E4].

Final internal check: {"complete": true, "missing_points": [], "reason": "Câu trả lời đã bao gồm đầy đủ các biện pháp kiểm soát theo Khung đạo đức trí tuệ nhân tạo quốc gia và quy định liên quan đến hệ thống trí tuệ nhân tạo có tác động đáng kể đến quyền con người được cung cấp trong các đoạn bằng chứng.", "scope": "final answer", "recheck_used": true}.

## 7. Citation Revision Analysis

**1 query used Citation Revision: eval005b**, also using Answer Revision. Its trace records `citation_check → citation_revision → citation_recheck`, and the final deterministic validator is valid with cited IDs E1, E4, E5 and no errors. Alignment method is `not_required_after_targeted_revision`. Semantic Citation Check was not used.

The original deterministic error payload and the answer immediately before Citation Revision are not retained. A validator failure followed by a pass is trace-consistent and inferred from the transition and guarded runtime branch; the precise error (for example formatting, unknown ID or mismatch) is **unknown**. The original draft cites E1 and the final answer additionally cites E4 and E5, but these changes cannot be allocated between the two revisions. Whether Citation Revision altered substantive content is **not identifiable** from the retained intermediate artifacts.

| Query | Pre-validator issue | Final validator | Citation Completeness Standard → Agentic | Citation Correctness Standard → Agentic | Observation |
|---|---|---|---|---|---|
| [eval005b](../../../rag/traces/agentic-rag-v1/agentic-v1/eval005b.json) | not retained; failure inferred | PASS | 0.000000 → 0.166667 | 1.000000 → 1.000000 | observed gain with multiple interventions; attribution not isolated |

A validator fix and benchmark-quality improvement are different observations. Citation Correctness stays 1; Citation Completeness rises from 0 to 1/6 together with Answer Completeness. Existing evidence is insufficient to identify a separate citation-revision quality gain. The last completeness check occurred before Citation Revision and was not repeated afterward.

## 8. Internal Self-check Calibration

| Final internal completeness decision | Benchmark AC = 1 | Benchmark AC < 1 |
|---|---|---|
| complete = true | 13 | 17 |
| complete = false | 1 | 0 |

**17/30 internal complete decisions accompany incomplete benchmark answers.** There are 13 true/complete agreements, 17 potential false-success / evaluator disagreements, 1 internal-incomplete/benchmark-complete disagreement (eval010), and 0 false/incomplete agreements. All 31 last internal decisions are available; eval005b’s decision precedes Citation Revision. These are not formal false positives or false negatives: the checker assesses completeness using query and retrieved evidence, while the frozen evaluator requires all annotated propositions including material conditions and scope.

| Potential false-success query | Benchmark Answer Completeness | Final status | Internal reason |
|---|---|---|---|
| [eval001](../../../rag/traces/agentic-rag-v1/agentic-v1/eval001.json) | 0.000000 | insufficient_evidence | Câu trả lời đã phản ánh chính xác các mức phân loại rủi ro được đề cập trong các văn bản cung cấp (rủi ro cao, rủi ro trung bình, rủi ro thấp) và đúng với giới hạn của bằng chứng hiện có. |
| [eval004](../../../rag/traces/agentic-rag-v1/agentic-v1/eval004.json) | 0.500000 | success | Câu trả lời đã bao quát đầy đủ các biện pháp quản lý mà nhà cung cấp hệ thống AI rủi ro cao phải duy trì theo các bằng chứng được cung cấp. |
| [eval005a](../../../rag/traces/agentic-rag-v1/agentic-v1/eval005a.json) | 0.000000 | success | Câu trả lời đã bao quát đầy đủ các nghĩa vụ quản lý của nhà cung cấp hệ thống trí tuệ nhân tạo có rủi ro cao theo đúng các tài liệu chứng cứ được cung cấp. |
| [eval005b](../../../rag/traces/agentic-rag-v1/agentic-v1/eval005b.json) | 0.166667 | success | Câu trả lời đã bao quát đầy đủ các nghĩa vụ quản lý của bên triển khai hệ thống trí tuệ nhân tạo có rủi ro cao được nêu trong các tài liệu chứng cứ (quản lý rủi ro, nghĩa vụ minh bạch và xử lý sự cố). |
| [eval007](../../../rag/traces/agentic-rag-v1/agentic-v1/eval007.json) | 0.500000 | success | Câu trả lời đã bao quát đầy đủ các quy định về việc thông báo và gắn nhãn nội dung do AI tạo ra hoặc chỉnh sửa theo các bằng chứng được cung cấp. |
| [eval008](../../../rag/traces/agentic-rag-v1/agentic-v1/eval008.json) | 0.666667 | success | Câu trả lời đã bao quát đầy đủ các trường hợp theo yêu cầu dựa trên chứng cứ: nội dung gây nhầm lẫn về sự kiện, nhân vật, nguồn gốc, và các tác phẩm điện ảnh, chương trình nghệ thuật hoặc nội dung sáng tạo. |
| [eval011](../../../rag/traces/agentic-rag-v1/agentic-v1/eval011.json) | 0.500000 | success | Câu trả lời đã phản ánh chính xác nội dung tại [E1] về các cơ chế mà tổ chức, cá nhân được hưởng trong phạm vi thử nghiệm. |
| [eval013](../../../rag/traces/agentic-rag-v1/agentic-v1/eval013.json) | 0.600000 | success | Câu trả lời đã bao gồm đầy đủ các tiêu chí phân loại cấp độ thử nghiệm có kiểm soát theo các tài liệu chứng cứ được cung cấp. |
| [eval014](../../../rag/traces/agentic-rag-v1/agentic-v1/eval014.json) | 0.750000 | insufficient_evidence | Câu trả lời đã phản ánh chính xác rằng các bằng chứng hiện tại chỉ đề cập đến một số thành phần của hồ sơ chứ chưa đủ để kết luận toàn bộ, đồng thời liệt kê đúng các thành phần có trong các đoạn trích dẫn. |
| [eval016](../../../rag/traces/agentic-rag-v1/agentic-v1/eval016.json) | 0.500000 | success | Câu trả lời đã nêu đầy đủ các loại báo cáo mà tổ chức hoặc cá nhân phải thực hiện trong quá trình thử nghiệm có kiểm soát dựa trên các đoạn bằng chứng. |
| [eval018](../../../rag/traces/agentic-rag-v1/agentic-v1/eval018.json) | 0.750000 | success | Câu trả lời đã bao quát đầy đủ các nội dung xử lý kết quả thử nghiệm theo các tài liệu được cung cấp. |
| [eval022](../../../rag/traces/agentic-rag-v1/agentic-v1/eval022.json) | 0.333333 | success | The answer accurately addresses the query using the provided evidence, citing both the general provision on open data [E5] and the specific responsibilities regarding databases for artificial intelligence [E1]. |
| [eval023](../../../rag/traces/agentic-rag-v1/agentic-v1/eval023.json) | 0.500000 | success | The answer fully covers the regulations on ensuring connectivity and data exploitation to serve artificial intelligence based on the provided evidence. |
| [eval025](../../../rag/traces/agentic-rag-v1/agentic-v1/eval025.json) | 0.666667 | success | Câu trả lời đã bao quát đầy đủ các trường hợp phải đánh giá tác động theo đúng các căn cứ được cung cấp tại E1 và E2. |
| [eval027](../../../rag/traces/agentic-rag-v1/agentic-v1/eval027.json) | 0.750000 | success | Câu trả lời đã bao quát đầy đủ các nguyên tắc đạo đức khi phát triển và sử dụng trí tuệ nhân tạo được đề cập trong các văn bản cung cấp. |
| [eval028](../../../rag/traces/agentic-rag-v1/agentic-v1/eval028.json) | 0.750000 | success | Câu trả lời đã bao quát đầy đủ các nội dung về trách nhiệm giải trình của nhà cung cấp, bên triển khai và các tổ chức theo quy định tại các nguồn E1, E2, E3 và E4. |
| [eval030](../../../rag/traces/agentic-rag-v1/agentic-v1/eval030.json) | 0.500000 | success | Câu trả lời đã bao quát đầy đủ các yêu cầu được quy định trong các văn bản chứng cứ liên quan đến việc bảo đảm con người có khả năng giám sát và can thiệp vào hệ thống AI. |

eval010 illustrates the reverse disagreement: the benchmark’s two required points are supported, but the internal checker still asks for an explanation obligation in E5 and returns incomplete_answer. eval005a illustrates false-success risk: internal complete=true and success accompany 0/7 supported required points. eval027 loses P4 without triggering an intervention, yet receives complete=true and success.

| Final status | Queries | Benchmark AC < 1 | Citation Correctness < 1 | Groundedness < 1 |
|---|---|---|---|---|
| incomplete_answer | 1 | 0 | 0 | 0 |
| insufficient_evidence | 2 | 2 | 0 | 1 |
| success | 28 | 15 | 2 | 2 |

**15/28 success statuses accompany incomplete benchmark answers.** Success queries with Citation Correctness below 1 are eval013 (0.8) and eval022 (2/3); these same two have Groundedness below 1. Success is a controller termination label, not benchmark certification. eval001 and eval014 have internal complete=true but insufficient_evidence status because the generated answer declares insufficient evidence; the two fields should not be conflated. Every final deterministic citation check passes, yet these semantic deficiencies remain, and Semantic Citation Check is unused in all 31 traces.

## 9. Standard Failure → Agent Response

This mapping uses frozen Phase 4A evaluator-side labels after production. The runtime did not receive Standard failure categories or gold labels. Query primary failure counts below exclude `none` when Phase 4A stores an empty issue map; the 102-point table in Section 10 includes `none` explicitly. Query taxonomies are retained exactly, and a query may contain multiple point failure categories.

| Query | Standard Phase 4A failure profile | Agent intervention profile | Observed final outcome |
|---|---|---|---|
| [eval001](../../../rag/traces/agentic-rag-v1/agentic-v1/eval001.json) | F. Mixed failure; {"evidence_coverage": 1, "answer_generation": 2} | P1 — Evidence Expansion Only | O4 — Regressed |
| [eval002](../../../rag/traces/agentic-rag-v1/agentic-v1/eval002.json) | D. Generation-limited; {"answer_generation": 1} | P2 — Answer Revision Only | O1 — Improved |
| [eval003](../../../rag/traces/agentic-rag-v1/agentic-v1/eval003.json) | A. Mostly successful; none | P0 — No Substantive Intervention | O3 — No Change |
| [eval004](../../../rag/traces/agentic-rag-v1/agentic-v1/eval004.json) | B. Retrieval-limited; {"retrieval_miss": 3} | P0 — No Substantive Intervention | O3 — No Change |
| [eval005a](../../../rag/traces/agentic-rag-v1/agentic-v1/eval005a.json) | F. Mixed failure; {"retrieval_miss": 5, "evidence_coverage": 2} | P1 — Evidence Expansion Only | O3 — No Change |
| [eval005b](../../../rag/traces/agentic-rag-v1/agentic-v1/eval005b.json) | F. Mixed failure; {"retrieval_miss": 4, "evidence_coverage": 1, "answer_generation": 1} | P4 — Multiple Interventions | O1 — Improved |
| [eval006](../../../rag/traces/agentic-rag-v1/agentic-v1/eval006.json) | A. Mostly successful; none | P1 — Evidence Expansion Only | O3 — No Change |
| [eval007](../../../rag/traces/agentic-rag-v1/agentic-v1/eval007.json) | C. Evidence-coverage-limited; {"evidence_coverage": 3} | P0 — No Substantive Intervention | O3 — No Change |
| [eval008](../../../rag/traces/agentic-rag-v1/agentic-v1/eval008.json) | B. Retrieval-limited; {"retrieval_miss": 1} | P0 — No Substantive Intervention | O3 — No Change |
| [eval009](../../../rag/traces/agentic-rag-v1/agentic-v1/eval009.json) | A. Mostly successful; none | P0 — No Substantive Intervention | O3 — No Change |
| [eval010](../../../rag/traces/agentic-rag-v1/agentic-v1/eval010.json) | A. Mostly successful; none | P2 — Answer Revision Only | O3 — No Change |
| [eval011](../../../rag/traces/agentic-rag-v1/agentic-v1/eval011.json) | B. Retrieval-limited; {"retrieval_miss": 1} | P0 — No Substantive Intervention | O3 — No Change |
| [eval012](../../../rag/traces/agentic-rag-v1/agentic-v1/eval012.json) | E. Citation-limited; {"citation": 4} | P0 — No Substantive Intervention | O3 — No Change |
| [eval013](../../../rag/traces/agentic-rag-v1/agentic-v1/eval013.json) | C. Evidence-coverage-limited; {"evidence_coverage": 2} | P4 — Multiple Interventions | O4 — Regressed |
| [eval014](../../../rag/traces/agentic-rag-v1/agentic-v1/eval014.json) | F. Mixed failure; {"evidence_coverage": 2, "answer_generation": 2} | P1 — Evidence Expansion Only | O1 — Improved |
| [eval015](../../../rag/traces/agentic-rag-v1/agentic-v1/eval015.json) | A. Mostly successful; none | P0 — No Substantive Intervention | O3 — No Change |
| [eval016](../../../rag/traces/agentic-rag-v1/agentic-v1/eval016.json) | C. Evidence-coverage-limited; {"evidence_coverage": 2} | P1 — Evidence Expansion Only | O1 — Improved |
| [eval017](../../../rag/traces/agentic-rag-v1/agentic-v1/eval017.json) | A. Mostly successful; none | P0 — No Substantive Intervention | O3 — No Change |
| [eval018](../../../rag/traces/agentic-rag-v1/agentic-v1/eval018.json) | C. Evidence-coverage-limited; {"evidence_coverage": 1} | P0 — No Substantive Intervention | O3 — No Change |
| [eval019](../../../rag/traces/agentic-rag-v1/agentic-v1/eval019.json) | A. Mostly successful; none | P0 — No Substantive Intervention | O3 — No Change |
| [eval020](../../../rag/traces/agentic-rag-v1/agentic-v1/eval020.json) | A. Mostly successful; none | P0 — No Substantive Intervention | O3 — No Change |
| [eval021](../../../rag/traces/agentic-rag-v1/agentic-v1/eval021.json) | A. Mostly successful; none | P0 — No Substantive Intervention | O3 — No Change |
| [eval022](../../../rag/traces/agentic-rag-v1/agentic-v1/eval022.json) | F. Mixed failure; {"retrieval_miss": 1, "evidence_coverage": 1, "answer_generation": 1} | P2 — Answer Revision Only | O1 — Improved |
| [eval023](../../../rag/traces/agentic-rag-v1/agentic-v1/eval023.json) | B. Retrieval-limited; {"retrieval_miss": 1} | P0 — No Substantive Intervention | O3 — No Change |
| [eval024](../../../rag/traces/agentic-rag-v1/agentic-v1/eval024.json) | A. Mostly successful; none | P0 — No Substantive Intervention | O3 — No Change |
| [eval025](../../../rag/traces/agentic-rag-v1/agentic-v1/eval025.json) | C. Evidence-coverage-limited; {"evidence_coverage": 1} | P0 — No Substantive Intervention | O3 — No Change |
| [eval026](../../../rag/traces/agentic-rag-v1/agentic-v1/eval026.json) | A. Mostly successful; none | P2 — Answer Revision Only | O3 — No Change |
| [eval027](../../../rag/traces/agentic-rag-v1/agentic-v1/eval027.json) | A. Mostly successful; none | P0 — No Substantive Intervention | O4 — Regressed |
| [eval028](../../../rag/traces/agentic-rag-v1/agentic-v1/eval028.json) | C. Evidence-coverage-limited; {"evidence_coverage": 1} | P0 — No Substantive Intervention | O3 — No Change |
| [eval029](../../../rag/traces/agentic-rag-v1/agentic-v1/eval029.json) | A. Mostly successful; none | P2 — Answer Revision Only | O3 — No Change |
| [eval030](../../../rag/traces/agentic-rag-v1/agentic-v1/eval030.json) | D. Generation-limited; {"answer_generation": 2} | P0 — No Substantive Intervention | O3 — No Change |

| Behavior | Used where intended Standard target is present | Used where target is absent | Usage |
|---|---|---|---|
| evidence_expansion | 5 | 1 | 6 |
| answer_revision | 3 | 4 | 7 |
| citation_revision | 0 | 1 | 1 |

Five of six expansions coincide with a Standard retrieval/evidence issue; eval006 was already benchmark-complete. Three of seven Answer Revisions coincide with a Phase 4A generation issue (eval002, eval005b, eval022); the other four target Agentic draft content or checker requirements even though the corresponding Standard failure category is absent. Citation Revision occurs on eval005b, which had no Standard citation issue; it responds to an issue in the Agentic execution. This is not a proven wrong trigger. Standard’s syntax failure on eval012 disappears without Citation Revision, while its five quality metrics stay unchanged.

The six gained points comprise four Standard answer_generation failures and two evidence_coverage failures; no retrieval_miss point is recovered. eval016’s citation/grounding improvement occurs without a required-point gain. This supports prioritizing generation omissions and checker/evidence selection behavior for controlled evaluation, without implying runtime awareness of the taxonomy.

## 10. Required-point Gain/Loss

**Standard supported: 60/102. Agentic supported: 65/102. Gained: 6. Lost: 1. Net gain: 5.** Sets are computed independently for each query: Agentic supported − Standard supported, and the reverse. No point is re-judged. Standard has 42 unsupported points; Agentic has 37.

| Standard primary point category | All required points | Gained | Lost |
|---|---|---|---|
| retrieval_miss | 16 | 0 | 0 |
| evidence_coverage | 17 | 2 | 0 |
| answer_generation | 9 | 4 | 0 |
| citation | 4 | 0 | 0 |
| none | 56 | 0 | 1 |

| Query | Point | Change | Frozen Standard primary failure | Required point |
|---|---|---|---|---|
| eval002 | P2 | gained | answer_generation | Bộ Khoa học và Công nghệ chủ trì phối hợp xây dựng và trình Danh mục trên cơ sở tiêu chí, nguyên tắc của Nghị định. |
| eval005b | P4 | gained | answer_generation | Bên triển khai phải thực hiện nghĩa vụ minh bạch và xử lý sự cố. |
| eval014 | P1 | gained | answer_generation | Đơn đề nghị tham gia cơ chế thử nghiệm theo mẫu tương ứng với tổ chức hoặc cá nhân. |
| eval014 | P2 | gained | evidence_coverage | Đề án thử nghiệm mô tả hệ thống, mục tiêu, phạm vi, thời gian và phương án quản lý rủi ro. |
| eval014 | P4 | gained | answer_generation | Tài liệu mô tả năng lực kỹ thuật, nhân sự hoặc hạ tầng liên quan trực tiếp đến phạm vi thử nghiệm. |
| eval022 | P2 | gained | evidence_coverage | Cơ quan phải tổ chức thu thập, tạo lập, cập nhật, bảo đảm chất lượng, gán nhãn, chú thích và chuẩn hóa các bộ dữ liệu thiết yếu phục vụ phát triển AI. |
| eval027 | P4 | lost | none | Khuyến khích đổi mới sáng tạo và trách nhiệm xã hội trong nghiên cứu, phát triển và ứng dụng AI. |

All 102 required points are accounted for through the query-scoped required ID arrays and the validated Phase 4A point partition. No global union of local P1/P2 identifiers was used. **Fully rescued:** eval002. **Partially rescued:** eval014, eval022, eval005b. “Rescued” refers only to the specified Answer Completeness definition; eval014 remains insufficient_evidence and eval005b/eval022 remain benchmark-incomplete.

## 11. Intervention × Outcome Matrix

| Intervention profile | Queries | Improved | Trade-off | No change | Regressed | Inconclusive |
|---|---|---|---|---|---|---|
| P0 — No Substantive Intervention | 19 | 0 | 0 | 18 | 1 | 0 |
| P1 — Evidence Expansion Only | 5 | 2 | 0 | 2 | 1 | 0 |
| P2 — Answer Revision Only | 5 | 2 | 0 | 3 | 0 | 0 |
| P3 — Citation Revision Only | 0 | 0 | 0 | 0 | 0 | 0 |
| P4 — Multiple Interventions | 2 | 1 | 0 | 0 | 1 | 0 |
| Total | 31 | 5 | 0 | 23 | 3 | 0 |

Improvement orientation is Agentic − Standard for Answer Completeness, Citation Completeness, Citation Correctness and Groundedness, and Standard − Agentic for Unsupported Claim Rate. With epsilon = 1e-9 only for numerical equality: positive/no negative = Improved; both signs = Improved with Trade-off; all zero = No Change; negative/no positive = Regressed; a required metric missing = Inconclusive. All rows and columns reconcile to 31. “No meaningful change” is not an intervention profile.

## 12. Rescued Queries

All four rescued cases are ranked primarily by Δ Answer Completeness, with citation and groundedness context below. This is the full rescue group, without forcing a fixed example count.

| Rank | Query | Standard AC | Agentic AC | Delta | Gained points | Profile |
|---|---|---|---|---|---|---|
| 1 | [eval014](../../../rag/traces/agentic-rag-v1/agentic-v1/eval014.json) | 0.000000 | 0.750000 | 0.750000 | `P1`, `P2`, `P4` | P1 — Evidence Expansion Only |
| 2 | [eval002](../../../rag/traces/agentic-rag-v1/agentic-v1/eval002.json) | 0.500000 | 1.000000 | 0.500000 | `P2` | P2 — Answer Revision Only |
| 3 | [eval022](../../../rag/traces/agentic-rag-v1/agentic-v1/eval022.json) | 0.000000 | 0.333333 | 0.333333 | `P2` | P2 — Answer Revision Only |
| 4 | [eval005b](../../../rag/traces/agentic-rag-v1/agentic-v1/eval005b.json) | 0.000000 | 0.166667 | 0.166667 | `P4` | P4 — Multiple Interventions |

### [eval014](../../../rag/traces/agentic-rag-v1/agentic-v1/eval014.json) — partially rescued

Hồ sơ thông thường để tham gia cơ chế thử nghiệm có kiểm soát gồm những thành phần nào?

Answer Completeness: **0.000000 → 0.750000** (Δ 0.750000). Gained points: `P1`, `P2`, `P4`. Profile: P1 — Evidence Expansion Only.

Evidence added: —; removed: —. Draft-to-final answer text changed: False; draft-to-final citation ID set changed: False; Standard-to-Agentic cited chunk set changed: False.

Expansion leaves ordered Top-5 unchanged. The generated draft/final answer gives more detail for application forms and testing-project contents; the frozen evaluator gains P1, P2 and P4 despite continued abstention. Expansion did not introduce final evidence, so its contribution is not isolated from generation/evaluator variation.

Final Citation Completeness=0.750000, Citation Correctness=1.000000, Groundedness=1.000000, Unsupported Claim Rate=0.000000. single intervention; observational association only.

### [eval002](../../../rag/traces/agentic-rag-v1/agentic-v1/eval002.json) — fully rescued

Ai có thẩm quyền ban hành danh mục hệ thống trí tuệ nhân tạo có rủi ro cao?

Answer Completeness: **0.500000 → 1.000000** (Δ 0.500000). Gained points: `P2`. Profile: P2 — Answer Revision Only.

Evidence added: —; removed: —. Draft-to-final answer text changed: True; draft-to-final citation ID set changed: False; Standard-to-Agentic cited chunk set changed: False.

Answer Revision adds the ministry coordination/submission responsibility (P2) with citation E2. Draft text exactly matches the frozen Standard answer and the evidence content/citation map is identical. This is the strongest trace-consistent revision association; the frozen Standard audit is an exact-draft proxy, not a separately run draft audit.

Final Citation Completeness=1.000000, Citation Correctness=1.000000, Groundedness=1.000000, Unsupported Claim Rate=0.000000. single intervention; observational association only.

### [eval022](../../../rag/traces/agentic-rag-v1/agentic-v1/eval022.json) — partially rescued

Cơ quan quản lý có trách nhiệm gì đối với việc xây dựng và cập nhật dữ liệu mở phục vụ AI?

Answer Completeness: **0.000000 → 0.333333** (Δ 0.333333). Gained points: `P2`. Profile: P2 — Answer Revision Only.

Evidence added: —; removed: —. Draft-to-final answer text changed: True; draft-to-final citation ID set changed: True; Standard-to-Agentic cited chunk set changed: False.

Answer Revision appends the agency database collection/quality/annotation responsibility with E1. The frozen evaluator gains P2 and improves all five oriented metrics, while P1 and P3 remain unsupported. Evidence stays unchanged; draft benchmark scores were not retained.

Final Citation Completeness=0.333333, Citation Correctness=0.666667, Groundedness=0.666667, Unsupported Claim Rate=0.333333. single intervention; observational association only.

### [eval005b](../../../rag/traces/agentic-rag-v1/agentic-v1/eval005b.json) — partially rescued

Bên triển khai hệ thống trí tuệ nhân tạo có rủi ro cao phải thực hiện những nghĩa vụ quản lý nào?

Answer Completeness: **0.000000 → 0.166667** (Δ 0.166667). Gained points: `P4`. Profile: P4 — Multiple Interventions.

Evidence added: —; removed: —. Draft-to-final answer text changed: True; draft-to-final citation ID set changed: True; Standard-to-Agentic cited chunk set changed: True.

Answer Revision and Citation Revision occur on unchanged evidence. The final answer adds transparency and incident-handling obligations (P4). Citation recheck passes, but the answer between the two revisions and the original validator errors were not retained. Their separate contributions cannot be isolated; the final completeness decision precedes Citation Revision.

Final Citation Completeness=0.166667, Citation Correctness=1.000000, Groundedness=1.000000, Unsupported Claim Rate=0.000000. multiple interventions — attribution not isolated.

## 13. No-observed-gain Interventions

**7 intervention queries have no positive oriented benchmark change:** five No Change (eval005a, eval006, eval010, eval026, eval029) and two Regressed (eval001, eval013). Regressions are also analyzed separately. This definition excludes cases that improve one metric while worsening another; no trade-off cases occur in this dataset.

| Query | Profile | Final outcome | Evidence added / removed | Draft → final changed | Production retrieval / LLM |
|---|---|---|---|---|---|
| [eval001](../../../rag/traces/agentic-rag-v1/agentic-v1/eval001.json) | P1 — Evidence Expansion Only | O4 — Regressed | 1 / 1 | False | 3 / 3 |
| [eval005a](../../../rag/traces/agentic-rag-v1/agentic-v1/eval005a.json) | P1 — Evidence Expansion Only | O3 — No Change | 0 / 0 | False | 2 / 3 |
| [eval006](../../../rag/traces/agentic-rag-v1/agentic-v1/eval006.json) | P1 — Evidence Expansion Only | O3 — No Change | 0 / 0 | False | 2 / 3 |
| [eval010](../../../rag/traces/agentic-rag-v1/agentic-v1/eval010.json) | P2 — Answer Revision Only | O3 — No Change | 0 / 0 | True | 1 / 5 |
| [eval013](../../../rag/traces/agentic-rag-v1/agentic-v1/eval013.json) | P4 — Multiple Interventions | O4 — Regressed | 0 / 0 | True | 2 / 5 |
| [eval026](../../../rag/traces/agentic-rag-v1/agentic-v1/eval026.json) | P2 — Answer Revision Only | O3 — No Change | 0 / 0 | True | 1 / 5 |
| [eval029](../../../rag/traces/agentic-rag-v1/agentic-v1/eval029.json) | P2 — Answer Revision Only | O3 — No Change | 0 / 0 | True | 1 / 5 |

The most important no-observed-gain pattern is expansion that leaves final evidence unchanged: eval005a and eval006 show no metric gain, and eval013 regresses alongside Answer Revision. Answer Revision on eval010, eval026 and eval029 changes text but adds no supported point relative to the frozen Standard answer. eval026 is a necessary caution: revision visibly restores a detail missing from its own draft but present in Standard, so “no gain over Standard” does not establish that revision was unnecessary.

Citation Revision has no isolated no-gain case: its only use overlaps Answer Revision and the final combined outcome improves. Do not label these triggers “false interventions”; the observations concern final benchmark gain, and the benchmark does not cover every reasonable internal-check requirement.

## 14. Regression Cases

All three queries with any negative oriented metric are listed. None also has a positive oriented metric, so all three are O4 Regressed. No significance threshold or statistical significance claim is introduced.

| Query | Metric | Standard | Agentic | Oriented delta | Intervention profile |
|---|---|---|---|---|---|
| [eval001](../../../rag/traces/agentic-rag-v1/agentic-v1/eval001.json) | groundedness | 1.000000 | 0.500000 | -0.500000 | P1 — Evidence Expansion Only |
| [eval001](../../../rag/traces/agentic-rag-v1/agentic-v1/eval001.json) | unsupported_claim_rate | 0.000000 | 0.500000 | -0.500000 | P1 — Evidence Expansion Only |
| [eval013](../../../rag/traces/agentic-rag-v1/agentic-v1/eval013.json) | citation_correctness | 1.000000 | 0.800000 | -0.200000 | P4 — Multiple Interventions |
| [eval013](../../../rag/traces/agentic-rag-v1/agentic-v1/eval013.json) | groundedness | 1.000000 | 0.800000 | -0.200000 | P4 — Multiple Interventions |
| [eval013](../../../rag/traces/agentic-rag-v1/agentic-v1/eval013.json) | unsupported_claim_rate | 0.000000 | 0.200000 | -0.200000 | P4 — Multiple Interventions |
| [eval027](../../../rag/traces/agentic-rag-v1/agentic-v1/eval027.json) | answer_completeness | 1.000000 | 0.750000 | -0.250000 | P0 — No Substantive Intervention |
| [eval027](../../../rag/traces/agentic-rag-v1/agentic-v1/eval027.json) | citation_completeness | 1.000000 | 0.750000 | -0.250000 | P0 — No Substantive Intervention |

Evidence-removal inspection: eval001 removes one initial chunk, but it is not in any annotated required-point supporting set. The lost required point eval027/P4 occurs with unchanged evidence and no intervention. Added evidence in eval001 accompanies lower Groundedness and higher UCR, **not lower Answer Completeness** (0 → 0). No expanded query loses a supported required point. There is no isolated evidence that Answer Revision introduces unsupported content: eval013’s appended highest-level sentence already appears in Standard, while its final judge stores only aggregate unsupported-claim counts. Citation Revision is absent from all three regression traces; its possible substantive effect in eval005b remains unidentifiable.

### [eval001](../../../rag/traces/agentic-rag-v1/agentic-v1/eval001.json)

Các mức phân loại rủi ro của hệ thống trí tuệ nhân tạo gồm những mức nào?

Expansion adds article 10 clause 3 and removes a non-gold initial chunk, but the missing low-risk definition remains outside final Top-5. The draft/final answer adds a low-risk mention and still abstains. Frozen groundedness falls from 1 to 0.5; the judge retains aggregate claim counts, not claim-specific reasons. No Answer Revision or Citation Revision occurred. Evidence removal of a required-point supporting chunk is not observed.

Profile: P1 — Evidence Expansion Only. Evidence added: `134-2025-QH15_dieu-10_khoan-3`; removed: `142-2026-ND-CP_dieu-8_khoan-1_diem-a`. Answer Revision: False; Citation Revision: False.

Standard answer:

Bằng chứng hiện tại chưa đủ để kết luận toàn bộ các mức phân loại rủi ro của hệ thống trí tuệ nhân tạo, vì các văn bản cung cấp chỉ đề cập đến mức rủi ro cao [E3] và rủi ro trung bình [E1][E4].

Final Agentic answer:

Bằng chứng hiện tại chưa đủ để kết luận toàn bộ các mức phân loại rủi ro của hệ thống trí tuệ nhân tạo, vì các văn bản cung cấp chỉ đề cập trực tiếp đến mức rủi ro cao [E3], rủi ro trung bình [E1], và nhắc đến rủi ro thấp [E6], chứ không liệt kê đầy đủ tất cả các mức phân loại rủi ro.

### [eval013](../../../rag/traces/agentic-rag-v1/agentic-v1/eval013.json)

Việc phân loại cấp độ thử nghiệm có kiểm soát dựa trên những tiêu chí nào?

Expansion leaves ordered Top-5 unchanged. Answer Revision appends the highest-applicable-testing-level sentence, which was already in the frozen Standard answer. Citation Correctness and Groundedness fall to 0.8, while completeness stays 0.6. The final judge gives aggregate claim counts without locating its unsupported claim; no evidence establishes that revision introduced unsupported content.

Profile: P4 — Multiple Interventions. Evidence added: —; removed: —. Answer Revision: True; Citation Revision: False.

Standard answer:

Việc phân loại cấp độ thử nghiệm được xác định trên cơ sở chức năng, mục đích sử dụng và tác động tổng thể của hệ thống trí tuệ nhân tạo, bao gồm cả trường hợp hệ thống được triển khai thông qua nhiều thành phần, mô-đun hoặc dịch vụ kết hợp với nhau [E1]. Đồng thời, các tiêu chí cụ thể bao gồm phạm vi và quy mô triển khai thử nghiệm (địa bàn triển khai, số lượng điểm thử nghiệm, đối tượng tham gia thử nghiệm và mức độ kết nối với hệ thống dữ liệu hoặc hệ thống thông tin) [E3], mức độ tác động đối với an ninh quốc gia, trật tự, an toàn xã hội và quyền, lợi ích hợp pháp của tổ chức, cá nhân [E4], và đối tượng tham gia thử nghiệm được xác định theo tiêu chí cụ thể [E5]. Trường hợp hệ thống trí tuệ nhân tạo đồng thời đáp ứng tiêu chí của nhiều cấp độ thử nghiệm khác nhau thì hệ thống được phân loại theo cấp độ thử nghiệm cao nhất [E1].

Final Agentic answer:

Việc phân loại cấp độ thử nghiệm có kiểm soát được xác định trên cơ sở chức năng, mục đích sử dụng và tác động tổng thể của hệ thống trí tuệ nhân tạo (bao gồm cả trường hợp hệ thống triển khai qua nhiều thành phần, mô-đun hoặc dịch vụ kết hợp) [E1]. Bên cạnh đó, việc phân loại còn dựa trên các tiêu chí cụ thể như phạm vi và quy mô triển khai thử nghiệm (gồm địa bàn triển khai, số lượng điểm thử nghiệm, đối tượng tham gia thử nghiệm và mức độ kết nối với hệ thống dữ liệu hoặc hệ thống thông tin) [E3], mức độ tác động đối với an ninh quốc gia, trật tự, an toàn xã hội và quyền, lợi ích hợp pháp của tổ chức, cá nhân [E4], cũng như tiêu chí cụ thể để xác định đối tượng tham gia thử nghiệm [E5]. Ngoài ra, trường hợp hệ thống trí tuệ nhân tạo đồng thời đáp ứng tiêu chí của nhiều cấp độ thử nghiệm khác nhau thì hệ thống được phân loại theo cấp độ thử nghiệm cao nhất [E1].

### [eval027](../../../rag/traces/agentic-rag-v1/agentic-v1/eval027.json)

Nguyên tắc đạo đức khi phát triển và sử dụng trí tuệ nhân tạo được đặt ra như thế nào?

No Substantive Intervention and unchanged initial/final evidence. Frozen evaluator loses P4 (innovation/social responsibility); the final internal checker still declares complete and success. Standard point labels are retained without per-point judge rationales, so generation wording and evaluator variability cannot be separated.

Profile: P0 — No Substantive Intervention. Evidence added: —; removed: —. Answer Revision: False; Citation Revision: False.

Standard answer:

Nguyên tắc đạo đức khi phát triển và sử dụng trí tuệ nhân tạo được đặt ra nhằm bảo đảm tôn trọng con người, quyền con người, lợi ích công cộng và phát triển bền vững [E1]. Quá trình này phải bảo đảm tính minh bạch, công bằng, an toàn [E2], không phân biệt đối xử [E2][E3], không thiên lệch, không gây hại cho con người hoặc xã hội [E4]. Đồng thời, cần tuân thủ chuẩn mực đạo đức và giá trị văn hóa Việt Nam, thực hiện trách nhiệm giải trình về các quyết định và hệ quả của hệ thống trí tuệ nhân tạo [E4], cũng như xem xét tác động môi trường và ưu tiên giải pháp tiết kiệm năng lượng, hạn chế phát thải trong suốt vòng đời hệ thống [E5]. Nhà nước khuyến khích các tổ chức, cá nhân áp dụng Khung đạo đức trí tuệ nhân tạo quốc gia trong các hoạt động liên quan [E2].

Final Agentic answer:

Nguyên tắc đạo đức khi phát triển và sử dụng trí tuệ nhân tạo được định hướng nhằm bảo đảm tôn trọng con người, quyền con người, lợi ích công cộng và phát triển bền vững [E1]. Quá trình này nhằm bảo đảm tính minh bạch, công bằng, an toàn và tôn trọng quyền con người [E2], cụ thể bao gồm tôn trọng quyền con người, quyền công dân, bảo đảm công bằng, minh bạch và không phân biệt đối xử [E3][E4], không thiên lệch, không gây hại cho con người hoặc xã hội, tuân thủ chuẩn mực đạo đức và giá trị văn hóa Việt Nam, đồng thời thực hiện trách nhiệm giải trình về các quyết định và hệ quả của hệ thống trí tuệ nhân tạo [E4]. Bên cạnh đó, nguyên tắc phát triển bền vững yêu cầu tổ chức, cá nhân xem xét mức tiêu thụ năng lượng, tài nguyên tính toán và tác động môi trường, ưu tiên giải pháp kỹ thuật, hạ tầng và quy trình vận hành tiết kiệm năng lượng, hạn chế phát thải [E5].

## 15. Efficiency Analysis

| Profile | Queries | Retrieval mean / median / max | Retrieval distribution | LLM mean / median / max | LLM distribution |
|---|---|---|---|---|---|
| P0 — No Substantive Intervention | 19 | 1 / 1 / 1 | {"1": 19} | 3 / 3 / 3 | {"3": 19} |
| P1 — Evidence Expansion Only | 5 | 2.200000 / 2 / 3 | {"2": 4, "3": 1} | 3 / 3 / 3 | {"3": 5} |
| P2 — Answer Revision Only | 5 | 1 / 1 / 1 | {"1": 5} | 5 / 5 / 5 | {"5": 5} |
| P3 — Citation Revision Only | 0 | — / — / — | {} | — / — / — | {} |
| P4 — Multiple Interventions | 2 | 1.500000 / 1.500000 / 2 | {"1": 1, "2": 1} | 5.500000 / 5.500000 / 6 | {"5": 1, "6": 1} |

| Behavior | Queries | Rate |
|---|---|---|
| Targeted Evidence Expansion | 6 | 0.193548 |
| Answer Revision | 7 | 0.225806 |
| Citation Revision | 1 | 0.032258 |
| Semantic Citation Check | 0 | 0.000000 |

| Production LLM stage | Calls |
|---|---|
| Evidence Coverage Check | 31 |
| Answer Generation | 31 |
| Answer Completeness Check (31 initial + 7 rechecks) | 38 |
| Answer Revision | 7 |
| Citation Revision | 1 |
| Semantic Citation Check | 0 |

**108 = 31 coverage checks + 31 answer generations + 38 completeness checks + 7 answer revisions + 1 citation revision.** Deterministic Citation Check and Evidence Merge use no LLM call. The 38 retrieval calls comprise 31 Initial Retrieval calls plus 7 expansion subqueries; six Evidence Merge reranks are additionally recorded by transitions. Therefore call counts alone omit extra reranker work.

The frozen Standard runner’s logical production baseline is 31 retrieval + 31 answer-generation calls. Agentic therefore records **1.225806× retrieval calls and 3.483871× production LLM calls** (+22.58% and +248.39%). All 19 No Substantive Intervention queries still execute three production LLM calls (57 total). The two checks that every query executes account for 62 of the 77 additional LLM calls; seven Answer Revisions plus rechecks account for 14, and Citation Revision for 1. Expansion uses targeted intents from the coverage response rather than a separate subquery-generation LLM call.

The observed aggregate quality gain is +5 net required points with this overhead, including five improved and three regressed queries. These totals are descriptive and do not assign points to particular calls. Production accounting excludes all evaluator/judge calls and evaluation attempts. Traces record logical controller invocations, not exact HTTP requests or possible transport retries. No exact token, monetary cost or latency data is available for this comparison, so none is estimated.

## 16. Behavior Evidence Summary

| Behavior | Intended target | Usage | Observed association | Attribution confidence | Evidence |
|---|---|---|---|---|---|
| Evidence expansion | Retrieval / evidence coverage | 6 | Observed mixed: 2 Improved, 2 No Change, 2 Regressed | Lower for a helpful evidence effect: five unchanged Top-5; mixed interventions on eval013 | eval001, eval005a, eval006, eval013, eval014, eval016 |
| Answer revision | Generation omission | 7 | Observed mixed: 3 Improved, 3 No Change, 1 Regressed | Higher association for eval002: single intervention + exact draft proxy + state change; lower for combined/missing intermediate audits | eval002, eval005b, eval010, eval013, eval022, eval026, eval029 |
| Citation revision | Citation issues | 1 | Insufficient evidence for isolated quality effect; final validator passes and combined result improves | Lower: multiple interventions and missing pre-citation answer/errors | eval005b |

Higher attribution confidence here means stronger observational support from a single substantive intervention and trace-consistent state change, not established causality. Answer Revision on eval002 is an **Observed helpful association** within an overall mixed Answer Revision pattern. Expansion’s only final evidence change coincides with regression on eval001; no beneficial evidence-addition effect is confirmed.

## 17. Implications for Ablation

1. **Answer Completeness Check → Answer Revision → Final Completeness Re-check.** Isolate this chain against the same generation/evidence setup. eval002 is the strongest helpful association; eval022 gains P2; eval010/026/029 show no final gain over Standard, and eval013 regresses. Evaluate checker disagreement and whether revision recovers omissions in the Agentic draft. Preserve draft/final states and equivalent frozen evaluations in a future controlled design.

2. **Evidence Coverage Check → Targeted Evidence Expansion → Evidence Merge / Final Evidence Selection.** Isolate expansion and final evidence selection. Five of six expansions leave Top-5 unchanged, no annotated supporting chunks enter final context, and the only evidence change coincides with regression. Compare controlled behavior with the same initial evidence and generation settings before attributing gains or removing this mechanism.

3. **Citation Revision and Semantic Citation Check routing.** Isolate the deterministic repair path from Answer Revision and examine semantic routing with a separately designed evaluation. The sole repair case lacks intermediate payloads, Semantic Citation Check fires 0/31, and final semantic citation errors survive on eval013 and eval022. A final completeness check after citation edits is also a behavior worth evaluating in a controlled follow-up.

These are Phase 5 priorities, not executed changes. Pre-specify contrasts and success metrics using a separate development set; do not tune prompts, thresholds, models or budgets on these 31 final-evaluation queries. Report macro and micro quality, regressions and logical call overhead for future controlled experiments. No ablation or Phase 5 work was started.

## 18. Limitations

Trace analysis is observational. Trace analysis does not establish causal contribution of individual interventions. Multiple interventions make attribution ambiguous. Internal Agent checks are not equivalent to the frozen benchmark evaluator. Gold labels were used only post-hoc by the analysis/evaluator and were not exposed to runtime. Causal claims require ablation or another controlled experiment.

The 31 queries are one frozen final-evaluation set, not replicated runs or a random sample supporting broad performance claims. Differences in answer generation and semantic evaluator judgments remain possible even at temperature 0. No Substantive Intervention is a control-path category, not a guarantee of text-identical outputs. eval027 demonstrates a regression without intervention; eval014 demonstrates improvement despite unchanged final evidence.

Initial completeness payloads are overwritten for all seven Answer Revision cases; exact pre-Citation-Revision answer/error state is absent; final internal completeness on eval005b precedes the final citation edit. There are no separately stored benchmark-equivalent Agentic draft evaluations. Standard point-level judge rationales and claim-specific error explanations are unavailable; saved binary required-point IDs and aggregate claim counts are authoritative. No semantic labels were invented from these gaps.

Gold-support chunk overlap is only a post-hoc proxy and can miss support from non-gold evidence. Phase 4A binary labels do not represent partial proposition coverage. Historical source commit provenance is absent. Logical call accounting does not include HTTP retries, elapsed latency, context/token differences or monetary cost. Micro claim metrics have different answer-level denominators across systems. Completeness/Citation Completeness equality and Groundedness/UCR complementarity mean the five metrics are partly redundant in these artifacts.

**Final validation:** 31/31 queries, 102/102 required points, no duplicates, profiles/outcomes/matrix totals reconcile, metric orientations and gained/lost sets verified, production/evaluation calls separated, budget compliance PASS, 20 deterministic tests PASS, source integrity before/after PASS. Exactly the three authorized output artifacts were created; runtime, source results, gold, prompts and retrieval were untouched. **Network/API calls: NONE. Causal claims: NOT ESTABLISHED — observational trace analysis only. Phase 4E complete; STOP.**
