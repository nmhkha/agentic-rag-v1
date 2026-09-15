# Cleanup risks v0

## Integrity and research risks

- Frozen original source and artifact paths must stay intact. Phase 5A explicit frozen hashes match; an older retrieval_pipeline CPython 3.10 bytecode hash differs from eight historical inventory records. This predates this work.
- Historical whole-repository inventories can fail merely because new planning files exist. Treat that as inventory scope, not permission to rewrite frozen manifests.
- Bare imports and __file__ parent arithmetic will break under naive nesting. Root discovery changes would alter frozen source hashes.
- Phase 5 allowlists, exact path checks and seals bind source, assets and output locations, sometimes using absolute machine paths.
- Static inspection cannot prove absence of external callers or resolve every dynamic path/import. Source closures include lazy/conditional imports; unresolved external assets are not certified present.
- Frozen generated results are research evidence. Do not delete because they are reproducible in theory. Draft/verified and historical/replication roles must remain distinct.

## Credentials (values withheld)

`.env` exists (215 bytes) and must not enter a release bundle. `.env.example` is separately present. Signature scanning is heuristic, not a guarantee that all secrets were found; no actual credential values or source snippets are copied.

| Path | Line | Finding |
| --- | --- | --- |
| .env | 4 | credential-like content; value withheld |

## Caches, downloads, archives and temporary files

`.venv` is approximately 1.1 GiB and excluded. External model-cache roots referenced by manifests were not inspected. Repository runtime_cache includes downloaded transformer implementation Python; it is not proof of complete model weights. No cache was loaded.

| Category | Files | Bytes |
| --- | --- | --- |
| Caches | 94 | 1179181 |
| Temporary files (name heuristic) | 0 | 0 |
| Archives | 0 | 0 |

Cache directory paths:

- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3`
- `scripts/__pycache__`
- `tests/__pycache__`

## Largest existing files

| Path | Bytes |
| --- | --- |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/integrity_before_after_v0.json | 11368926 |
| data/evaluation/generation/phase5/phase5c3_v0/integrity_before_after_v0.json | 7003460 |
| data/evaluation/generation/phase5/phase5c3_v0/integrity_baseline_v0.json | 7001012 |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/integrity_baseline_v0.json | 6818373 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/integrity_baseline_v0.json | 6812359 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/integrity_before_after_v0.json | 6797295 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/integrity_baseline_v0.json | 6794954 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/medical_screen_integrity_baseline_v1.json | 5698439 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/integrity_before_after_v1.json | 5697560 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/integrity_baseline_v1.json | 5697440 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/integrity_before_after_v0.json | 5692496 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/integrity_baseline_v0.json | 5691596 |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/integrity_baseline_v0.json | 5684392 |
| data/evaluation/generation/phase5/phase5c2_v0/integrity_before_after_v0.json | 5680820 |
| data/evaluation/generation/phase5/phase5c2_v0/integrity_baseline_v0.json | 5679004 |
| data/evaluation/generation/phase5/phase5c1_v0/integrity_before_after_v0.json | 5678128 |
| data/evaluation/generation/phase5/phase5c1_v0/integrity_before_inventory_v0.json | 5676401 |
| data/evaluation/generation/phase5/phase5b2er2_v1/session_0001_binding.json | 4462510 |
| data/evaluation/generation/phase5/phase5b2er2_v1/session_0002_binding.json | 4164790 |
| data/raw/pdf/142-2026-ND-CP.pdf | 3661910 |
| data/indexes/dense-jina-v3-v0/embeddings.npy | 3018880 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b/complete_corpus_evidence_v0.json | 2941002 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/preexisting_inventory_paths_v1.json | 2471921 |
| data/evaluation/generation/phase5/phase5b2f_v0/agentic-v1-no-answer-revision/evaluation_complete.jsonl | 2408101 |
| data/evaluation/generation/phase5/phase5b2f_v0/full-agentic-replication/evaluation_complete.jsonl | 2358173 |

## Log/output files

| Path | Bytes |
| --- | --- |

## Machine-specific references

Includes /home, /Users and /tmp literals. Record locations only; exact secret-bearing lines are not reproduced. Not every temporary path denotes an existing temporary file.

| File | Matching lines |
| --- | --- |
| data/evaluation/generation/agentic_rag_eval_v1_agentic-v1.jsonl | 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31 |
| data/evaluation/generation/agentic_trace_analysis_metrics_v0.json | 599,1216,1220,1228 |
| data/evaluation/generation/phase5/agentic-v1-no-answer-revision/run_manifest.json | 1 |
| data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion/run_manifest.json | 1 |
| data/evaluation/generation/phase5/execution_environment_v0.json | 1 |
| data/evaluation/generation/phase5/execution_tools/launch_frozen_v0.py | 9,16,17,23 |
| data/evaluation/generation/phase5/execution_tools/report_incomplete_v0.py | 9 |
| data/evaluation/generation/phase5/full-agentic-replication/run_manifest.json | 1 |
| data/evaluation/generation/phase5/integrity_before_after_v0.json | 1 |
| data/evaluation/generation/phase5/phase5a_ablation_manifest_v0.json | 1589 |
| data/evaluation/generation/phase5/phase5b1_preflight_manifest_v0.json | 1 |
| data/evaluation/generation/phase5/phase5b1_preflight_report_v0.md | 106,114,116,141,142 |
| data/evaluation/generation/phase5/phase5b2_preflight_rerun_v0.json | 1 |
| data/evaluation/generation/phase5/phase5b2e_v0/provenance.json | 1 |
| data/evaluation/generation/phase5/phase5b2e_v0/replication_R1_R2.json | 1 |
| data/evaluation/generation/phase5/phase5b2er1_quota_recovery_spec_v0.md | 298,299 |
| data/evaluation/generation/phase5/phase5b2er2_v1/execution_driver_session_0001.py | 8,17,41 |
| data/evaluation/generation/phase5/phase5b2er2_v1/execution_driver_session_0002.py | 9,17 |
| data/evaluation/generation/phase5/phase5b2f_v0/analysis_tools/offline_analysis_v0.py | 85,86 |
| data/evaluation/generation/phase5/phase5b2f_v0/analysis_tools/phase5b2f_gate.py | 3,33,73 |
| data/evaluation/generation/phase5/phase5b2f_v0/integrity_before_after_v0.json | 18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67 |
| data/evaluation/generation/phase5/phase5b2f_v0/integrity_before_inventory_v0.json | 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26 |
| data/evaluation/generation/phase5/phase5b2r_recovery_protocol_v1.json | 1 |
| data/evaluation/generation/phase5/phase5b_evaluation_metrics_v0.json | 1 |
| data/evaluation/generation/phase5/phase5c3_v0/integrity_baseline_v0.json | 2 |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_freeze_manifest_v0.json | 13 |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/finalize_amendment_v0.py | 122 |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_amendment_manifest_v0.json | 10 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/phase5c4b_access_manifest_v0.json | 19 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/phase5c4b_validation_v0.json | 31 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/reviewer_b_manifest_v0.json | 29 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/finalize_b_v1.py | 7 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/phase5c4b_access_manifest_v1.json | 27 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_phase5c4b_access_manifest_v1.json | 27 |
| data/evaluation/generation/phase5/production_seal_validation_v0.json | 1 |
| data/evaluation/generation/reports/agentic_trace_analysis_v0.md | 51 |
| data/evaluation/generation/standard_rag_manifest_v0.json | 68 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/loaded_environment.json | 1 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/loaded_environment.json | 1 |
| data/rag/traces/phase5/full-agentic-replication/loaded_environment.json | 1 |
| scripts/phase5_preflight.py | 375,376 |
| scripts/phase5_seal_recovery_v1.py | 95 |
| tests/test_phase5_evaluation_quota_recovery.py | 394 |

## Review readiness

Ready to review this proposal, not authorized to migrate. No network/API, project imports, production, inference, evaluator, benchmark or tests ran. Integrity verification outcome is recorded in repository_inventory_v0.md and dependency_map_v0.json.
