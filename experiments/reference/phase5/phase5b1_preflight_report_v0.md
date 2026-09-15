# Phase 5B.1 — implementation, isolation and offline preflight

**Status: PASS**. Phase 5B.2 has not started and is not authorized.

## 1. Implementation

Added a thin wrapper around the unchanged AgenticRAGController. No frozen file was modified.

- `data/evaluation/generation/phase5/phase5b1_preflight_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5b1_preflight_report_v0.md`
- `data/evaluation/generation/phase5/query_inputs_v0.json`
- `scripts/phase5_ablation_runner.py`
- `scripts/phase5_analyze.py`
- `scripts/phase5_assets.py`
- `scripts/phase5_common.py`
- `scripts/phase5_isolation.py`
- `scripts/phase5_observer.py`
- `scripts/phase5_preflight.py`
- `tests/phase5_run_suite.py`
- `tests/phase5_synthetic_worker.py`
- `tests/phase5_test_support.py`
- `tests/test_phase5_ablation_runner.py`
- `tests/test_phase5_leakage.py`
- `tests/test_phase5_preflight.py`

## 2. Frozen design and configurations

- Specification SHA-256: `51f1bf9e4db72ac3c3edeaf36ef5385dc9aff295c63068d4ffb07926ecb15b64`
- Manifest SHA-256: `20893844b3bb7161b23d258476349e234675e404cd0b8a60fba17a376d8647cd`
- The original embedded Phase 5A validator passed before implementation: 246 original files, 67 named artifacts and 113 Phase 4E provenance entries matched.
- The manifest has no self-hash. Its observed byte hash above was sealed at the start of Phase 5B.1; the specification hash matches its frozen manifest declaration.

| ID | Exact variant ID | Canonical config SHA-256 |
|---|---|---|
| R2 | full-agentic-replication | `cc4f30732d3f5ecf46b69f804aab905b5e82fc8fe82f9f89098e4bd17dc2a956` |
| A1 | agentic-v1-no-answer-revision | `9f7beb58b43658af823410d99aad247cc9022b6bdfd0c6ff9e1ee6f4b201076e` |
| A2 | agentic-v1-no-evidence-expansion | `7d151d91a522f8ba0236664deade43aa19c35d07d926856e11fb93f6f87d66f5` |

Full objects are validated with SHA-256 of UTF-8 JSON, sorted keys, ensure_ascii=False, separators=(comma, colon), no newline. Only variant_id is excluded from the recursive difference check. A1 differs only in enable_answer_revision; A2 only in enable_expansion. Tests reject missing/extra/type/configuration drift and no-op ablations. Exact variant objects were materialized only in temporary test directories.

## 3. Runtime architecture

Trusted preparation validates the frozen verified dataset and projects exactly 31 ordered query_id/query records. The projection canonical hash is `1d29c4304f61d7c2235d7cab37e2bbf63a35e0c0caf6873d7e458e23904ebc78`.

The future scheduler materializes all primary manifests first and runs R2, A1, A2 in separate fresh sequential processes. It passes a minimal hash-locked runtime certificate, an allowlisted environment, no inherited data descriptors, and stdin=/dev/null. Production rejects full-design paths/schema, unapproved preloaded source modules, resolved symlink aliases and reads outside explicit source/corpus/index/cache/input/output permissions. The controller receives only a query string and a fresh state.

The observer delegates each call once and returns the original response object or exception. It records stage/order, logical type, attempt index, UTC timestamp, canonical request/response hashes, success/error, redacted raw response, and observed urllib submissions. Provider-internal retries remain unknown. Successful controller-assigned check snapshots determine eligibility; no observer parse drives a controller decision. Unreached/failed decisions are null with reasons.

Each query gets an exclusive attempt directory and fsynced started record before invocation; terminal completion/error follows durable trace, sidecar and output writes. Worker flock prevents concurrent advancement. Resume is bound to the same variant/query hash and executes only never-started queries; completed/errors are skipped, ambiguous and orphan outputs fail closed. Ordered JSONL journals and hashes seal production artifacts. No retries or budget compensation were added.

The separate trusted evaluator requires all primary seals before joining references. It imports the unchanged evaluate_record, judge_prompt, parse_judge, point_audit and citation validator. Durable request/response slots replay the same responses into the frozen parser after a crash, preserving at most three actual evaluator requests in total. Existing evaluator outputs are never rejudged. The analysis CLI only verifies seals in this phase.

## 4. Leakage gates L1–L5

- L1: recursive production AST/import closure and runtime rejection of evaluator reads/imports, including already imported unapproved modules.
- L2: exact projection schema/count/order/hash; duplicate IDs/text, missing values, additional/nested labels and changed text are rejected.
- L3: built-in open, pathlib and os.open reject direct and symlink paths for gold, historical outputs, traces and analysis files.
- L4: PHASE5_GOLD_SENTINEL_DO_NOT_LEAK stays absent from synthetic controller state/output, prompts, retrieval calls, original trace and sidecars.
- L5: fresh-process fake production succeeds with references unavailable; a different process joins only after all seals verify. Tampering and missing seals fail.

## 5. Behavior and evaluator tests

R2 direct-controller parity compares complete states/traces, prompt bytes, retrieval/merge arguments and transitions on ordinary, expansion, revision, citation, semantic and error paths, excluding only run IDs and timestamps. A1 retains its initial completeness check and citation repair but removes answer revision and its dependent recheck. A2 retains coverage/missing aspects and answer/citation repair while preserving initial Top-5 exactly and removing expansion retrieval/merge. Empty aspects are ineligible. All nominal budgets, including six LLM calls, remain unchanged. Synthetic evaluator wiring exercises the actual frozen evaluator, identical retry prompts and no rejudging.

**Tests: 36/36 PASS.**

- `test_phase5_ablation_runner.BehaviorTests.test_a1_no_answer_revision_no_compensation_citation_preserved`
- `test_phase5_ablation_runner.BehaviorTests.test_a2_no_expansion_no_compensation_revision_preserved`
- `test_phase5_ablation_runner.BehaviorTests.test_citation_semantic_gate_and_budget_all_variants`
- `test_phase5_ablation_runner.BehaviorTests.test_controller_input_rejects_design_and_records`
- `test_phase5_ablation_runner.BehaviorTests.test_empty_missing_aspects`
- `test_phase5_ablation_runner.BehaviorTests.test_null_on_unreached_or_failed_check`
- `test_phase5_ablation_runner.BehaviorTests.test_observer_identity_error_no_retries_redaction`
- `test_phase5_ablation_runner.BehaviorTests.test_r2_direct_parity_all_paths`
- `test_phase5_ablation_runner.BehaviorTests.test_r2_error_parity`
- `test_phase5_ablation_runner.EdgeGateTests.test_actual_http_attempt_event_is_separate_from_logical_call`
- `test_phase5_ablation_runner.EdgeGateTests.test_failed_revision_retains_eligibility_but_zero_completed_count`
- `test_phase5_ablation_runner.EdgeGateTests.test_observer_redacts_structured_auth`
- `test_phase5_ablation_runner.EdgeGateTests.test_r2_six_call_budget_no_extra_semantic_call`
- `test_phase5_ablation_runner.EdgeGateTests.test_resume_rejects_variant_or_query_drift_and_orphan_outputs`
- `test_phase5_ablation_runner.LedgerTests.test_ambiguous_resume_rejected_before_calls`
- `test_phase5_ablation_runner.LedgerTests.test_lifecycle_exclusive_and_ambiguous`
- `test_phase5_ablation_runner.LedgerTests.test_resume_never_started_only`
- `test_phase5_leakage.LeakageTests.test_durable_evaluator_attempt_ceiling_and_replay`
- `test_phase5_leakage.LeakageTests.test_evaluator_reuses_frozen_functions`
- `test_phase5_leakage.LeakageTests.test_hub_download_blocked_offline`
- `test_phase5_leakage.LeakageTests.test_l1_recursive_production_source_import_closure`
- `test_phase5_leakage.LeakageTests.test_l3_direct_symlink_pathlib_builtin_os_open`
- `test_phase5_leakage.LeakageTests.test_l4_sentinel_and_l5_without_gold_separate_evaluator`
- `test_phase5_leakage.LeakageTests.test_network_socket_http_gemini_fail_immediately`
- `test_phase5_leakage.LeakageTests.test_preloaded_unapproved_module_rejected`
- `test_phase5_leakage.LeakageTests.test_real_frozen_evaluator_wiring_with_synthetic_judge`
- `test_phase5_leakage.LeakageTests.test_unsealed_and_same_process_rejected`
- `test_phase5_leakage.LeakageTests.test_worker_rejects_full_design_path_before_read`
- `test_phase5_preflight.ConfigTests.test_config_drift_rejected`
- `test_phase5_preflight.ConfigTests.test_design_hashes_and_integrity`
- `test_phase5_preflight.ConfigTests.test_environment_config_types`
- `test_phase5_preflight.ConfigTests.test_exact_variants_flags_hashes_and_materialization`
- `test_phase5_preflight.ConfigTests.test_l2_schema_duplicate_nested_modified_order`
- `test_phase5_preflight.ConfigTests.test_real_projection_deterministic_only`
- `test_phase5_preflight.SnapshotTests.test_missing_tokenizer_or_weights_or_symlink_escape`
- `test_phase5_preflight.SnapshotTests.test_model_and_tokenizer_snapshot_revision`

## 6. Environment

- Python executable: `/home/minhkha/kk/TTTN/legal-agentic-rag/.venv/bin/python`
- Python version: `3.12.3`
- Actual pipeline: CPU, Dense float32/batch 4, reranker float32/batch 1, max length 8192.
- Endpoint configuration: `gemini-3.5-flash-lite` at `generativelanguage.googleapis.com`; configuration-only, no availability request.
- All installed package versions are recorded in the companion JSON manifest. No credentials or authorization headers are recorded.

## 7. Model and tokenizer snapshots

- dense: `jinaai/jina-embeddings-v3` revision `ab036b023d30b4d1138c4c3bfa9f0c445ab455d6`; snapshot `/home/minhkha/.cache/huggingface/hub/models--jinaai--jina-embeddings-v3/snapshots/ab036b023d30b4d1138c4c3bfa9f0c445ab455d6`.
- dense actual tokenizer fingerprint: `c29e2a24f78f21bb899d74f306224962dadae21c60c4a0dc16a798b48f9562c8`; exact-snapshot fingerprint: `c29e2a24f78f21bb899d74f306224962dadae21c60c4a0dc16a798b48f9562c8`.
- reranker: `BAAI/bge-reranker-v2-m3` revision `953dc6f6f85a1b2dbfca4c34a2796e7dde08d41e`; snapshot `/home/minhkha/.cache/huggingface/hub/models--BAAI--bge-reranker-v2-m3/snapshots/953dc6f6f85a1b2dbfca4c34a2796e7dde08d41e`.
- reranker actual tokenizer fingerprint: `bab87e87fc7f90826b1b6fa8b6cb38be83ea5c8de7ebd1e5a28198fb5c4748b9`; exact-snapshot fingerprint: `bab87e87fc7f90826b1b6fa8b6cb38be83ea5c8de7ebd1e5a28198fb5c4748b9`.
- Model weight/config/tokenizer file hashes and resolved blob paths are recorded. Cache blob identities are checked. The loaded model config revisions and actual tokenizer backend/special-token fingerprints are validated against explicit offline snapshot loads.
- Dense external implementation snapshot: `bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3`; current source hashes pinned separately.

## 8. Frozen source integrity

All 248 original/design paths match their before-hashes after implementation. The manifest contains every before/after SHA-256, covering corpus, gold, R0/R1, R1 traces, Phase 4A/4E, prompt, production/retrieval/evaluator sources, dependencies, original tests and original bytecode. New implementation/test source hashes are also recorded and must match before future launch.

## 9. Network and execution scope

Network calls = 0; Gemini/API calls = 0; real benchmark production queries = 0; real semantic evaluations = 0. The suite blocks transport before application imports, including HTTP/Gemini probes and offline Hub downloads. Deliberately blocked guard probes are counted separately: 2. The guarded model-load subprocess recorded zero connection attempts. No final production manifests/results were materialized.

## 10. Blockers and limits

- No implementation/preflight blocker remains.
- Read guard covers Python audited I/O/imports in reviewed code; it is not a hostile native-code sandbox.
- Endpoint validated by local configuration only; provider availability/backend identity was not tested.
- Hub warnings about downloaded remote-code files refer to offline cache-to-scratch copies; audited network attempts during pipeline loading were zero.
- Historical R1 full environment and Dense remote-code revision were not independently frozen; current cache source hashes are recorded for new variants.
- Production/evaluation launch requires separate Phase 5B.2 authorization; no benchmark is launched by preflight.

Reproduce without network or benchmark execution:

```bash
.venv/bin/python -B tests/phase5_run_suite.py --output /tmp/phase5-tests-NEW.json
.venv/bin/python -B scripts/phase5_preflight.py --load-pipeline --output /tmp/phase5-preflight-NEW.json
```

Use new output filenames; writes are exclusive. To produce a new complete report, add --tests-json and --report-markdown with new paths. Do not overwrite this report or the frozen Phase 5A design.

STOP: wait for external review before any Phase 5B.2 production or evaluation.
