Phase 5B.2 status: INCOMPLETE

PRODUCTION
R2: 31/31 completed
A1: 31/31 completed
A2: 31/31 completed

All three planned production passes finished in order R2 → A1 → A2. No production query was rerun.
Production seal verification: FAIL. The unchanged verifier rejects missing temporary runtime files.
The original seals and every surviving production artifact are preserved. No seal entry was removed or repaired.

EVALUATION
R2: 0/31 judged
A1: 0/31 judged
A2: 0/31 judged
No trusted evaluator process or semantic judge request was launched. evaluation.jsonl contains explicitly marked BLOCKED_NOT_ATTEMPTED envelopes, not judgments. evaluation_attempts.jsonl is empty.

R1 → R2 REPLICATION
AC macro: N/A
AC micro: N/A
Net required-point change: N/A
Gross point churn: N/A
Replication variability assessment: unavailable; R2 has no valid judgments. Historical R1 was not reevaluated or replaced.

R2 vs A1 — NO ANSWER REVISION
Status: INCOMPLETE / INSUFFICIENT EVIDENCE
R2 AC macro: N/A
A1 AC macro: N/A
Delta: N/A
R2 AC micro: N/A
A1 AC micro: N/A
Delta: N/A
Points lost by ablation: N/A
Points gained by ablation: N/A
Net R2 contribution: N/A
R2 better / tied / A1 better: N/A / N/A / N/A
95% paired bootstrap CI: N/A (not executed)
R2-triggered query count: N/A (comparative analysis not entered)
Production LLM calls saved: N/A
Retrieval calls saved: N/A
Merge-reranks saved: N/A
Interpretation: Insufficient evidence

R2 vs A2 — NO EVIDENCE EXPANSION
Status: INCOMPLETE / INSUFFICIENT EVIDENCE
R2 AC macro: N/A
A2 AC macro: N/A
Delta: N/A
R2 AC micro: N/A
A2 AC micro: N/A
Delta: N/A
Points lost by ablation: N/A
Points gained by ablation: N/A
Net R2 contribution: N/A
R2 better / tied / A2 better: N/A / N/A / N/A
95% paired bootstrap CI: N/A (not executed)
R2-triggered query count: N/A (comparative analysis not entered)
Production LLM calls saved: N/A
Retrieval calls saved: N/A
Merge-reranks saved: N/A
Interpretation: Insufficient evidence

SAFETY / CITATION
Citation Completeness: N/A
Citation Correctness: N/A
Groundedness macro/micro: N/A / N/A
Unsupported Claim Rate macro/micro: N/A / N/A
Citation syntax validity: N/A
All quality metrics, point transitions, bootstrap results, trigger strata and replication-attribution flags are withheld. The declared denominator remains 31 queries / 102 required points; nothing is imputed.

EFFICIENCY
Per-run production diagnostics only; comparative analysis remains blocked.

| Run | Retrieval total / mean / median / max | LLM total / mean / median / max | Merge-reranks | Observed HTTP submissions |
|---|---|---|---|---|
| R2 | 42 / 1.3548387096774193 / 1 / 3 | 101 / 3.2580645161290325 / 3 / 5 | 9 | 101 |
| A1 | 42 / 1.3548387096774193 / 1 / 2 | 94 / 3.032258064516129 / 3 / 4 | 11 | 94 |
| A2 | 31 / 1 / 1 / 1 | 101 / 3.2580645161290325 / 3 / 6 | 0 | 101 |

Evaluator calls: 0. Provider-internal retries and token/cost records: unavailable.
Historical R0 contextual baseline only: configured logical 31 retrieval + 31 generation calls, mean/median/max 1. No measured Standard HTTP cost is claimed.

ERRORS
R2 production errors: []
R2 evaluation errors: 0 judge failures; 31 judgments blocked before evaluator entry.
R2 exact blocked query IDs: eval001, eval002, eval003, eval004, eval005a, eval005b, eval006, eval007, eval008, eval009, eval010, eval011, eval012, eval013, eval014, eval015, eval016, eval017, eval018, eval019, eval020, eval021, eval022, eval023, eval024, eval025, eval026, eval027, eval028, eval029, eval030
R2 seal failures:
- `runtime_cache/tmpw675ical/_remote_module_non_scriptable.py`: MISSING; expected SHA-256 `8205b16956fb264841ecd8644784a0d157f87df79b17c16825dc1163433ce5d8`.
R2 ledger/trace/observer reconciliation: PASS; non-runtime-cache artifact hashes: PASS
A1 production errors: []
A1 evaluation errors: 0 judge failures; 31 judgments blocked before evaluator entry.
A1 exact blocked query IDs: eval001, eval002, eval003, eval004, eval005a, eval005b, eval006, eval007, eval008, eval009, eval010, eval011, eval012, eval013, eval014, eval015, eval016, eval017, eval018, eval019, eval020, eval021, eval022, eval023, eval024, eval025, eval026, eval027, eval028, eval029, eval030
A1 seal failures:
- `runtime_cache/tmpgpcxup8f/_remote_module_non_scriptable.py`: MISSING; expected SHA-256 `8205b16956fb264841ecd8644784a0d157f87df79b17c16825dc1163433ce5d8`.
A1 ledger/trace/observer reconciliation: PASS; non-runtime-cache artifact hashes: PASS
A2 production errors: []
A2 evaluation errors: 0 judge failures; 31 judgments blocked before evaluator entry.
A2 exact blocked query IDs: eval001, eval002, eval003, eval004, eval005a, eval005b, eval006, eval007, eval008, eval009, eval010, eval011, eval012, eval013, eval014, eval015, eval016, eval017, eval018, eval019, eval020, eval021, eval022, eval023, eval024, eval025, eval026, eval027, eval028, eval029, eval030
A2 seal failures:
- `runtime_cache/tmpo8gyry6w/_remote_module_non_scriptable.py`: MISSING; expected SHA-256 `8205b16956fb264841ecd8644784a0d157f87df79b17c16825dc1163433ce5d8`.
A2 ledger/trace/observer reconciliation: PASS; non-runtime-cache artifact hashes: PASS

The sealer inventories every file below the production output directory, including runtime_cache. PyTorch creates its remote-module Python file in a TemporaryDirectory, which disappears on normal worker exit. The seal therefore references a file that no longer exists when a separate evaluator checks it. This lifecycle failure was not detected by the passing preflight tests.
Evidence: scripts/phase5_ablation_runner.py:172; scripts/phase5_analyze.py:23; .venv/lib/python3.12/site-packages/torch/distributed/nn/jit/instantiator.py:20.

INTEGRITY
Frozen artifact hashes unchanged: PASS
Before/after hashes are recorded in integrity_before_after_v0.json, including pre-Phase-5B.2 artifacts and pinned runtime/model assets.
Pre-execution gates: 36/36 tests PASS; all 262 initially certified file hashes matched; offline model/tokenizer/configuration/package/endpoint certificates matched Phase 5B.1.
The runtime seal failure is separate from frozen source/design/model drift. No frozen source, design, Phase 5B.1 artifact, model asset, prompt, gold, R0 or R1 was repaired or overwritten.

EXPERIMENTAL CLAIM
Controlled single-run ablation evidence only; no quality or contribution claim is available because semantic evaluation is blocked.
Causal/general claims remain limited by benchmark size and observed replication variability. Replication variability was not measured in this incomplete execution.

Ready for Phase 5C:
NO

STOP. No Agentic v1 changes, A3/A4 runs, or Phase 5C work were performed.
