# Phase 5B.2-R recovery report v0

Phase 5B.2-R status: PASS

Infrastructure recovery and provenance / seal validation amendment.

Original production: R2 31/31; A1 31/31; A2 31/31. Production errors: 0.
Production reruns: 0. Semantic evaluations: 0/93.
Original seals modified: NO. Their historical failure remains FAILED_EPHEMERAL_LIFECYCLE.

Failure root cause: the v0 sealer inventories process-owned PyTorch generated code before worker exit. PyTorch instantiator creates the module in a TemporaryDirectory; Python weakref.finalize removes it at normal exit. The local source hashes and a successful benign sentinel cleanup probe are recorded in the protocol. The missing PyTorch files were never reconstructed and PyTorch was not imported.

Evaluator source inspection confirms the generated module is not an evaluation input. Production records were serialized and fsynced before exit; the old existence check alone requires the vanished file.

| Variant | Missing ephemeral path | Durable files from original seal | Recovery |
|---|---|---:|---|
| R2 | `runtime_cache/tmpw675ical/_remote_module_non_scriptable.py` | 174 | PASS |
| A1 | `runtime_cache/tmpgpcxup8f/_remote_module_non_scriptable.py` | 174 | PASS |
| A2 | `runtime_cache/tmpo8gyry6w/_remote_module_non_scriptable.py` | 174 | PASS |

All three original seals independently recorded SHA-256 `8205b16956fb264841ecd8644784a0d157f87df79b17c16825dc1163433ce5d8` for the missing module.
No other missing files exist. All surviving cache files remain durable; runtime_cache/** is not excluded.

Durable artifacts verified: ordered output and attempt journals, 93 per-query outputs, 93 traces, 93 observer sidecars, 186 per-query attempt records, run bindings, loaded model provenance and all other surviving seal entries. Query order/hash, config hashes and run manifest identities reconcile. Run/variant manifests and source, model, prompt, gold, corpus, retrieval, R0/R1 and earlier phase artifacts are covered by frozen hash inventories.

Negative corruption tests: 21/21 PASS (including T1–T9). See `phase5b2r_negative_tests_v1.json`.
Frozen artifact integrity: PASS. All 820 preexisting project files remain byte-identical; 335 historical hash references also match (overlapping inventories).

Future-only correction: `scripts/phase5_durable_seal_v1.py` supplies `seal_production_v1` and `verify_future_seal`. Future workers must opt in to these versioned functions. Known ephemeral entries are recorded in a separately hashed execution/cache provenance sidecar. Unknown cache files remain durable. The future sealer refuses existing v0 seals and recovery namespaces. The frozen v0 worker and evaluator remain unchanged and still reject the old seals.

This is a post-production infrastructure correction discovered before semantic evaluation, not an experimental-system change.

Network calls during recovery: 0. Gemini/API calls during recovery: 0. Model inference calls: 0. Recovery uses standard-library filesystem checks with a network-denying audit hook; tests use copied artifacts. No answers were displayed or manually inspected for quality. No semantic evaluator, point comparison or bootstrap was invoked.

Existing Phase 5B.2 production outputs are eligible for semantic evaluation.
This eligibility is not authorization to evaluate. Evaluation remains unstarted and requires separate review/authorization.

Independent verification command (use the manifest SHA-256 printed at creation as the external trust anchor):

```sh
python3 -B scripts/phase5_seal_recovery_v1.py verify --manifest-sha256 <reviewed-manifest-sha256>
```

STOP. Await review.
