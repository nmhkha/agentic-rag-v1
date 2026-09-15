# Repository inventory v0

Read-only inventory and classification proposal, 2026-09-14. No migration or application execution.

1647 existing project files hashed (211,035,249 bytes). `.git` internals and `.venv` are excluded from logical inventory and project-byte integrity checks; `.venv` occupies approximately 1.1 GiB. Hidden project files and bytecode are included. No AGENTS.md was found in the repository/parent search. The ten new planning files are excluded from before/after comparison. Counts below overlap. Python count includes cached downloaded model source.

| Category | Count |
| --- | --- |
| Python files | 130 |
| Shell scripts | 0 |
| JSON/JSONL | 1337 |
| Markdown | 54 |
| Prompts/templates | 1 |
| Tests (all files under tests/) | 16 |
| Data directories | 506 |
| Generated artifacts (may also be frozen) | 1523 |
| Temporary files (name heuristic) | 0 |
| Caches | 94 |
| Notebooks | 0 |
| Archives | 0 |

## Script classification counts

Counts here and in the final console refer to all 91 files under scripts/, including 45 bytecode files; they do not count frozen data as source files. Frozen protection takes precedence over functional role, which remains in the CSV. Zero ACTIVE_V2 means no v2 implementation identified, not that Phase 5C designs are obsolete.

| Classification | Count |
| --- | --- |
| FROZEN_REFERENCE | 19 |
| FROZEN_BUT_WRAPPABLE | 4 |
| ACTIVE_SHARED | 0 |
| ACTIVE_V2 | 0 |
| RESEARCH_TOOLING | 13 |
| ONE_OFF_PHASE_SCRIPT | 2 |
| UTILITY | 8 |
| OBSOLETE_CANDIDATE | 0 |
| GENERATED_ARTIFACT | 45 |
| UNKNOWN | 0 |

## Python files

- `data/evaluation/generation/phase5/execution_tools/launch_frozen_v0.py`
- `data/evaluation/generation/phase5/execution_tools/report_incomplete_v0.py`
- `data/evaluation/generation/phase5/phase5b2e_v0/analyze_frozen.py`
- `data/evaluation/generation/phase5/phase5b2e_v0/evaluate_frozen.py`
- `data/evaluation/generation/phase5/phase5b2e_v0/render_report.py`
- `data/evaluation/generation/phase5/phase5b2e_v0/validate_analysis.py`
- `data/evaluation/generation/phase5/phase5b2er2_v1/execution_driver_session_0001.py`
- `data/evaluation/generation/phase5/phase5b2er2_v1/execution_driver_session_0002.py`
- `data/evaluation/generation/phase5/phase5b2f_v0/analysis_tools/offline_analysis_v0.py`
- `data/evaluation/generation/phase5/phase5b2f_v0/analysis_tools/phase5b2f_gate.py`
- `data/evaluation/generation/phase5/phase5b2f_v0/analysis_tools/verify_final_analysis_v0.py`
- `data/evaluation/generation/phase5/phase5c1_v0/consolidate_research_v0.py`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/build_comparison_v0.py`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/semantic_mapping_decisions_v0.py`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/validate_comparison_v0.py`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/authored_tasks_v0.py`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/build_construction_v0.py`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/sanitize_reviewer_b_v1.py`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b1_reference_preparation_v0/prepare_medical_reference_v1.py`
- `data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/finalize_amendment_v0.py`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/authored_specs_v1.py`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/build_b_annotations_v1.py`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/complete_medical_screen_v1.py`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/finalize_b_v1.py`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/refine_bundle_anchors_v1.py`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/screen_text_v1.py`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/validate_b_v1.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/block.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/configuration_xlm_roberta.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/embedding.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mha.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mlp.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_lora.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_xlm_roberta.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/rotary.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/stochastic_depth.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/xlm_padding.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/block.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/configuration_xlm_roberta.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/embedding.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mha.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mlp.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_lora.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_xlm_roberta.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/rotary.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/stochastic_depth.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/xlm_padding.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/__init__.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/__init__.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/__init__.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/__init__.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/__init__.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/block.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/configuration_xlm_roberta.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/embedding.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mha.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mlp.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_lora.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_xlm_roberta.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/rotary.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/stochastic_depth.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/xlm_padding.py`
- `scripts/agentic_rag.py`
- `scripts/analyze_candidate_coverage.py`
- `scripts/analyze_standard_rag_failures.py`
- `scripts/annotate_retrieval_eval.py`
- `scripts/bm25_baseline.py`
- `scripts/build_chunks.py`
- `scripts/build_dense_index.py`
- `scripts/build_generation_eval_v1.py`
- `scripts/check_register.py`
- `scripts/citation_validator.py`
- `scripts/clean_docx_text.py`
- `scripts/create_verification_samples.py`
- `scripts/dense_baseline.py`
- `scripts/evaluate_agentic_rag.py`
- `scripts/evaluate_bm25.py`
- `scripts/evaluate_dense.py`
- `scripts/evaluate_hybrid.py`
- `scripts/evaluate_reranker.py`
- `scripts/evaluate_standard_rag.py`
- `scripts/evidence_formatter.py`
- `scripts/extract_docx.py`
- `scripts/generate_human_review_report.py`
- `scripts/hash_raw_files.py`
- `scripts/hybrid_rrf.py`
- `scripts/inspect_chunk_issues.py`
- `scripts/llm_client.py`
- `scripts/parse_legal_structure.py`
- `scripts/phase5_ablation_runner.py`
- `scripts/phase5_analyze.py`
- `scripts/phase5_assets.py`
- `scripts/phase5_common.py`
- `scripts/phase5_durable_seal_v1.py`
- `scripts/phase5_evaluation_quota_recovery_v1.py`
- `scripts/phase5_isolation.py`
- `scripts/phase5_observer.py`
- `scripts/phase5_preflight.py`
- `scripts/phase5_seal_recovery_v1.py`
- `scripts/rag_baseline.py`
- `scripts/reranker_baseline.py`
- `scripts/response_formatter.py`
- `scripts/retrieval_pipeline.py`
- `scripts/update_source_hashes.py`
- `scripts/update_verification_status.py`
- `scripts/validate_corpus.py`
- `scripts/validate_generation_eval.py`
- `scripts/validate_retrieval_eval.py`
- `tests/phase5_run_suite.py`
- `tests/phase5_synthetic_worker.py`
- `tests/phase5_test_support.py`
- `tests/test_agentic_evaluation.py`
- `tests/test_agentic_rag.py`
- `tests/test_generation_eval.py`
- `tests/test_phase5_ablation_runner.py`
- `tests/test_phase5_evaluation_quota_recovery.py`
- `tests/test_phase5_leakage.py`
- `tests/test_phase5_preflight.py`
- `tests/test_phase5_seal_recovery_v1.py`
- `tests/test_rag_runtime.py`

## Shell scripts

None found.

## JSON/JSONL

- `.vscode/settings.json`
- `data/evaluation/backups/retrieval_eval.20260814-145701.jsonl`
- `data/evaluation/backups/retrieval_eval.20260814-151851.jsonl`
- `data/evaluation/backups/retrieval_eval.20260814-153333.jsonl`
- `data/evaluation/dev_queries.jsonl`
- `data/evaluation/generation/agentic_rag_eval_v1_agentic-v1.jsonl`
- `data/evaluation/generation/agentic_rag_metrics_v1_agentic-v1.json`
- `data/evaluation/generation/agentic_trace_analysis_metrics_v0.json`
- `data/evaluation/generation/agentic_trace_analysis_v0.jsonl`
- `data/evaluation/generation/backups/generation_eval_v1.20260902-145534.json`
- `data/evaluation/generation/failure_analysis_metrics_v0.json`
- `data/evaluation/generation/failure_analysis_points_v0.jsonl`
- `data/evaluation/generation/failure_analysis_queries_v0.json`
- `data/evaluation/generation/generation_eval_v0.json`
- `data/evaluation/generation/generation_eval_v0.schema.json`
- `data/evaluation/generation/generation_eval_v0_manifest.json`
- `data/evaluation/generation/generation_eval_v1.json`
- `data/evaluation/generation/generation_eval_v1.schema.json`
- `data/evaluation/generation/generation_eval_v1_manifest.json`
- `data/evaluation/generation/generation_eval_v1_verified.json`
- `data/evaluation/generation/generation_eval_v1_verified_manifest.json`
- `data/evaluation/generation/partials/standard_rag_eval_v0_partial.20260902-151753.jsonl`
- `data/evaluation/generation/partials/standard_rag_eval_v0_partial.20260902-155801.jsonl`
- `data/evaluation/generation/phase5/agentic-v1-no-answer-revision/evaluation.jsonl`
- `data/evaluation/generation/phase5/agentic-v1-no-answer-revision/evaluation_attempts.jsonl`
- `data/evaluation/generation/phase5/agentic-v1-no-answer-revision/metrics.json`
- `data/evaluation/generation/phase5/agentic-v1-no-answer-revision/run_manifest.json`
- `data/evaluation/generation/phase5/agentic-v1-no-answer-revision/variant_manifest.json`
- `data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion/evaluation.jsonl`
- `data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion/evaluation_attempts.jsonl`
- `data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion/metrics.json`
- `data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion/run_manifest.json`
- `data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion/variant_manifest.json`
- `data/evaluation/generation/phase5/contrast_R2_A1.json`
- `data/evaluation/generation/phase5/contrast_R2_A2.json`
- `data/evaluation/generation/phase5/execution_environment_v0.json`
- `data/evaluation/generation/phase5/full-agentic-replication/evaluation.jsonl`
- `data/evaluation/generation/phase5/full-agentic-replication/evaluation_attempts.jsonl`
- `data/evaluation/generation/phase5/full-agentic-replication/metrics.json`
- `data/evaluation/generation/phase5/full-agentic-replication/run_manifest.json`
- `data/evaluation/generation/phase5/full-agentic-replication/variant_manifest.json`
- `data/evaluation/generation/phase5/integrity_before_after_v0.json`
- `data/evaluation/generation/phase5/phase5a_ablation_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5b1_preflight_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5b2_preflight_rerun_v0.json`
- `data/evaluation/generation/phase5/phase5b2_preflight_tests_v0.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval001/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval001/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval002/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval002/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval003/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval003/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval004/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval004/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval005a/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval005a/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval005b/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval005b/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval006/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval006/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval007/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval007/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval008/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval008/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval009/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval009/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval010/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval010/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval011/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval011/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval012/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval012/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval012/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval012/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval013/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval013/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval013/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval013/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval015/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval015/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval017/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval017/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval017/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval017/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval018/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval018/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval018/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval018/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval027/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval027/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval027/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval027/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval028/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval028/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval029/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval029/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval030/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval030/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/evaluation.jsonl`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/evaluation_attempts.jsonl`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/metrics.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval001.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval002.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval003.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval004.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval005a.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval005b.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval006.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval007.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval008.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval009.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval010.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval011.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval012.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval013.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval014.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval015.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval016.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval017.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval018.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval019.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval020.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval021.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval022.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval023.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval024.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval025.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval026.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval027.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval028.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval029.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval030.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval001/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval001/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval002/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval002/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval003/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval003/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval004/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval004/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval005a/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval005a/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval005b/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval005b/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval006/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval006/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval007/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval007/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval008/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval008/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval009/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval009/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval010/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval010/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval011/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval011/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval012/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval012/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval013/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval013/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval014/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval014/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval014/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval014/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval021/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval021/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval028/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval028/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval029/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval029/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval030/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval030/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/evaluation.jsonl`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/evaluation_attempts.jsonl`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/metrics.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval001.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval002.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval003.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval004.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval005a.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval005b.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval006.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval007.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval008.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval009.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval010.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval011.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval012.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval013.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval014.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval015.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval016.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval017.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval018.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval019.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval020.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval021.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval022.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval023.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval024.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval025.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval026.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval027.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval028.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval029.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval030.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/analysis_validation.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/contrast_R2_A1.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/contrast_R2_A2.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/evaluation_protocol.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/evaluation_protocol_initial.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval001/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval001/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval002/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval002/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval003/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval003/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval004/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval004/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval005a/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval005a/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval005b/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval005b/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval006/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval006/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval007/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval007/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval008/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval008/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval009/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval009/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval010/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval010/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval011/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval011/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval012/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval012/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval013/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval013/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval014/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval014/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval015/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval015/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval015/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval015/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval016/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval016/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval017/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval017/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval017/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval017/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval020/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval020/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval029/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval029/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval030/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval030/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/evaluation.jsonl`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/evaluation_attempts.jsonl`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/metrics.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval001.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval002.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval003.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval004.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval005a.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval005b.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval006.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval007.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval008.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval009.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval010.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval011.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval012.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval013.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval014.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval015.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval016.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval017.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval018.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval019.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval020.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval021.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval022.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval023.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval024.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval025.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval026.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval027.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval028.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval029.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval030.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/integrity_after.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/integrity_before.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/provenance.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/recovery_gate.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/replication_R1_R2.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/reporting_correction_validation.json`
- `data/evaluation/generation/phase5/phase5b2er1_integrity_v0.json`
- `data/evaluation/generation/phase5/phase5b2er1_quota_recovery_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5b2er1_quota_recovery_tests_v0.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval014/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval014/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval014/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval014/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval016/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval016/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval016/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval016/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval019/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval019/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval019/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval019/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval020/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval020/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval020/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval020/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval022/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval022/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval022/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval022/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval023/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval023/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval023/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval023/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/2/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/2/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/2/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/2/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval025/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval025/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval025/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval025/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval026/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval026/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval026/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval026/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval015/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval015/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval015/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval015/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval016/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval016/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval016/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval016/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval017/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval017/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval017/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval017/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval018/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval018/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval018/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval018/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval019/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval019/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval019/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval019/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval020/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval020/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval020/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval020/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval022/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval022/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval022/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval022/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval023/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval023/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval023/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval023/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval024/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval024/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval024/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval024/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval025/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval025/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval025/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval025/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval026/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval026/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval026/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval026/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval027/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval027/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval027/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval027/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval021/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval021/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval021/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval021/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval022/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval022/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval022/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval022/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval023/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval023/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval023/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval023/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval024/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval024/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval024/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval024/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval025/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval025/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval025/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval025/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval026/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval026/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval026/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval026/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval027/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval027/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval027/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval027/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval028/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval028/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval028/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval028/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/phase5b2er2_session_0001_report.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/phase5b2er2_session_0002_report.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/protocol_binding.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/quota_stop_0001.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/quota_stop_0001_resume_authorization.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/session_0001_binding.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/session_0001_integrity.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/session_0002_binding.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/session_0002_integrity.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/agentic-v1-no-answer-revision/evaluation_complete.jsonl`
- `data/evaluation/generation/phase5/phase5b2f_v0/agentic-v1-no-answer-revision/metrics.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/agentic-v1-no-evidence-expansion/evaluation_complete.jsonl`
- `data/evaluation/generation/phase5/phase5b2f_v0/agentic-v1-no-evidence-expansion/metrics.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/bootstrap_R2_A1.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/bootstrap_R2_A2.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/canonical_judgments_manifest.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/contrast_R2_A1.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/contrast_R2_A2.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/efficiency_v0.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/final_artifact_hashes_v0.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/full-agentic-replication/evaluation_complete.jsonl`
- `data/evaluation/generation/phase5/phase5b2f_v0/full-agentic-replication/metrics.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/integrity_before_after_v0.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/integrity_before_inventory_v0.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/phase5b2f_metrics_v0.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/point_transitions_R1_R2.jsonl`
- `data/evaluation/generation/phase5/phase5b2f_v0/point_transitions_R2_A1.jsonl`
- `data/evaluation/generation/phase5/phase5b2f_v0/point_transitions_R2_A2.jsonl`
- `data/evaluation/generation/phase5/phase5b2f_v0/provenance_v0.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/recovery_completion_gate_v0.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/replication_R1_R2.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/validation_v0.json`
- `data/evaluation/generation/phase5/phase5b2r_negative_tests_v1.json`
- `data/evaluation/generation/phase5/phase5b2r_recovery_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5b2r_recovery_protocol_v1.json`
- `data/evaluation/generation/phase5/phase5b_evaluation_metrics_v0.json`
- `data/evaluation/generation/phase5/phase5c1_v0/final_artifact_hashes_v0.json`
- `data/evaluation/generation/phase5/phase5c1_v0/integrity_before_after_v0.json`
- `data/evaluation/generation/phase5/phase5c1_v0/integrity_before_inventory_v0.json`
- `data/evaluation/generation/phase5/phase5c1_v0/phase5c1_evidence_matrix_v0.json`
- `data/evaluation/generation/phase5/phase5c1_v0/phase5c1_exploratory_diagnostic_v0.json`
- `data/evaluation/generation/phase5/phase5c1_v0/phase5c1_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5c1_v0/phase5c1_problem_requirement_map_v0.json`
- `data/evaluation/generation/phase5/phase5c1_v0/phase5c1_validation_v0.json`
- `data/evaluation/generation/phase5/phase5c2_v0/final_artifact_hashes_v0.json`
- `data/evaluation/generation/phase5/phase5c2_v0/integrity_baseline_v0.json`
- `data/evaluation/generation/phase5/phase5c2_v0/integrity_before_after_v0.json`
- `data/evaluation/generation/phase5/phase5c2_v0/phase5c2_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5c2_v0/phase5c2_requirement_validation_matrix_v0.json`
- `data/evaluation/generation/phase5/phase5c2_v0/phase5c2_trace_schema_design_v0.json`
- `data/evaluation/generation/phase5/phase5c2_v0/phase5c2_validation_v0.json`
- `data/evaluation/generation/phase5/phase5c3_v0/final_artifact_hashes_v0.json`
- `data/evaluation/generation/phase5/phase5c3_v0/integrity_baseline_v0.json`
- `data/evaluation/generation/phase5/phase5c3_v0/integrity_before_after_v0.json`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_controller_status_decision_table_v0.json`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_decision_table_validation_v0.json`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_freeze_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_spec_bindings_v0.json`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_trace_matrix_amendment_v0.json`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_validation_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/adjudication_corpus_audit_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/adjudication_issue_resolutions_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/candidate_admission_decisions_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/final_adjudicated_annotations_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/final_retained_36_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/final_split_assignment_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/input_contamination_incident_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/integrity_before_after_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/phase5c4d_dimension_summary_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/phase5c4d_selection_summary_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/phase5c4d_validation_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_applicability_sufficiency_comparison_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_aspect_mapping_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_candidate_alignment_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_contamination_comparison_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_corpus_audit_comparison_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_disagreement_registry_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_scope_comparison_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_support_comparison_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/artifact_hashes_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/comparison_access_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/comparison_check_results_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/final_artifact_hashes_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/integrity_baseline_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/integrity_before_after_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/phase5c4c1_agreement_metrics_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/phase5c4c1_disagreement_summary_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/phase5c4c1_validation_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/source_integrity_validation_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/annotation_A_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/challenge_candidates_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/cluster_rationales_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/construction_notes_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/contaminated_packet_quarantine_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/contamination_screening_details_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/corpus_absence_audits_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/corpus_mapping_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/custodian_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/exclusion_log_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/explicit_asks_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/exposure_events_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/artifact_hashes_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/execution_and_access_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/integrity_baseline_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/integrity_before_after_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/phase5c4b0_validation_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b1_reference_preparation_v0/medical_reference_projection_audit_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/reviewer_b_comparison_after_independent_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/reviewer_b_id_mapping_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/reviewer_b_packet_projection_audit_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/reviewer_b_shuffle_provenance_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/split_assignment_provisional_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/artifact_hashes_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/integrity_baseline_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/integrity_before_after_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_amendment_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_amendment_validation_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_selection_rules_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/artifact_hashes_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/frozen_source_checks_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/integrity_baseline_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/integrity_before_after_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_access_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_aggregate_composition_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_cluster_summary_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_dimension_matrix_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_validation_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b/01_independent_review_units_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b/complete_corpus_evidence_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b/contamination_query_only_sources_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_packet_v1/contamination_reference_medical_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_packet_v1/reviewer_b_packet_manifest_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_packet_v1/reviewer_b_queries_v1.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/annotation_B_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/integrity_baseline_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/integrity_before_after_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/phase5c4b_access_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/phase5c4b_agreement_ready_summary_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/phase5c4b_validation_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/reviewer_b_contamination_flags_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/reviewer_b_corpus_audit_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/reviewer_b_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/annotation_B_pre_anchor_correction_v1.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/annotation_B_substantive_locked_v1.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/annotation_B_v1.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/annotation_structural_validation_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/evidence_anchor_corrections_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/frozen_design_binding_checks_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/generated_artifact_hashes_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/historical_31_query_text_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/integrity_baseline_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/integrity_before_after_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/medical_screen_completion_validation_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/medical_screen_integrity_baseline_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/medical_screen_integrity_before_after_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/medical_screen_pre_read_seal_audit_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/medical_screening_completed_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/packet_schema_validation_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/phase5c4b_access_manifest_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/phase5c4b_agreement_ready_summary_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/phase5c4b_validation_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_generated_artifact_hashes_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_phase5c4b_access_manifest_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_phase5c4b_agreement_ready_summary_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_phase5c4b_validation_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_reviewer_b_contamination_flags_v1.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_reviewer_b_manifest_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/preexisting_inventory_paths_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/resume_audit_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/reviewer_b_contamination_flags_v1.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/reviewer_b_corpus_audit_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/reviewer_b_manifest_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/reviewer_b_medical_contamination_screen_v1.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/scoped_corpus_reviews_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/substantive_lock_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/text_screen_provenance_v1.json`
- `data/evaluation/generation/phase5/production_seal_validation_v0.json`
- `data/evaluation/generation/phase5/query_inputs_v0.json`
- `data/evaluation/generation/phase5/replication_R1_R2.json`
- `data/evaluation/generation/phase5/report_artifact_hashes_v0.json`
- `data/evaluation/generation/phase5/report_validation_v0.json`
- `data/evaluation/generation/standard_rag_eval_v0.jsonl`
- `data/evaluation/generation/standard_rag_manifest_v0.json`
- `data/evaluation/generation/standard_rag_metrics_v0.json`
- `data/evaluation/results/bge-reranker-v2-m3-v0_metrics.json`
- `data/evaluation/results/bm25-simple-v0_metrics.json`
- `data/evaluation/results/candidate-union-v0_metrics.json`
- `data/evaluation/results/dense-jina-v3-v0_metrics.json`
- `data/evaluation/results/hybrid-rrf-v0_metrics.json`
- `data/evaluation/retrieval_eval.jsonl`
- `data/indexes/bge-reranker-v2-m3-v0/reranker_manifest.json`
- `data/indexes/dense-jina-v3-v0/chunk_ids.json`
- `data/indexes/dense-jina-v3-v0/index_manifest.json`
- `data/indexes/hybrid-rrf-v0/hybrid_manifest.json`
- `data/processed/articles.jsonl`
- `data/processed/chunks.jsonl`
- `data/rag/legal-rag-v0_manifest.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval001.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval002.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval003.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval004.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval005a.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval005b.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval006.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval007.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval008.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval009.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval010.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval011.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval012.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval013.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval014.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval015.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval016.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval017.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval018.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval019.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval020.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval021.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval022.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval023.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval024.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval025.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval026.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval027.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval028.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval029.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval030.json`
- `data/rag/traces/agentic-rag-v1_20260909T132334.960415Z.json`
- `data/rag/traces/agentic-rag-v1_20260909T132915.670264Z.json`
- `data/rag/traces/agentic-rag-v1_20260913T071538.629769Z.json`
- `data/rag/traces/agentic-rag-v1_20260913T072604.572183Z.json`
- `data/rag/traces/agentic-rag-v1_smoke.json`
- `data/rag/traces/legal-rag-v0_20260824T082500.431067Z.json`
- `data/rag/traces/legal-rag-v0_20260824T083023.964302Z.json`
- `data/rag/traces/legal-rag-v0_20260824T083324.619096Z.json`
- `data/rag/traces/legal-rag-v0_20260824T083822.282992Z.json`
- `data/rag/traces/legal-rag-v0_20260824T084241.384282Z.json`
- `data/rag/traces/legal-rag-v0_20260824T084747.340310Z.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval001/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval001/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval002/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval002/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval003/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval003/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval004/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval004/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval005a/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval005a/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval005b/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval005b/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval006/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval006/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval007/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval007/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval008/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval008/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval009/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval009/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval010/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval010/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval011/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval011/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval012/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval012/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval013/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval013/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval014/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval014/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval015/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval015/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval016/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval016/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval017/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval017/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval018/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval018/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval019/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval019/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval020/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval020/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval021/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval021/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval022/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval022/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval023/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval023/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval024/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval024/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval025/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval025/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval026/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval026/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval027/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval027/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval028/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval028/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval029/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval029/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval030/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval030/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/durable_seal_recovery_v1.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval001.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval002.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval003.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval004.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval005a.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval005b.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval006.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval007.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval008.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval009.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval010.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval011.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval012.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval013.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval014.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval015.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval016.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval017.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval018.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval019.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval020.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval021.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval022.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval023.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval024.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval025.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval026.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval027.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval028.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval029.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval030.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/loaded_environment.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval001.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval002.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval003.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval004.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval005a.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval005b.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval006.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval007.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval008.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval009.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval010.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval011.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval012.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval013.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval014.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval015.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval016.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval017.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval018.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval019.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval020.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval021.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval022.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval023.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval024.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval025.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval026.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval027.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval028.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval029.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval030.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval001.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval002.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval003.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval004.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval005a.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval005b.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval006.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval007.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval008.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval009.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval010.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval011.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval012.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval013.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval014.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval015.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval016.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval017.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval018.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval019.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval020.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval021.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval022.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval023.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval024.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval025.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval026.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval027.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval028.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval029.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval030.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/production_attempts.jsonl`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/production_outputs.jsonl`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/production_seal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/run_binding.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval001/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval001/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval002/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval002/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval003/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval003/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval004/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval004/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval005a/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval005a/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval005b/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval005b/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval006/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval006/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval007/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval007/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval008/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval008/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval009/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval009/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval010/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval010/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval011/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval011/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval012/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval012/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval013/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval013/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval014/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval014/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval015/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval015/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval016/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval016/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval017/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval017/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval018/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval018/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval019/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval019/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval020/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval020/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval021/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval021/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval022/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval022/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval023/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval023/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval024/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval024/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval025/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval025/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval026/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval026/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval027/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval027/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval028/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval028/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval029/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval029/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval030/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval030/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/durable_seal_recovery_v1.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval001.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval002.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval003.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval004.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval005a.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval005b.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval006.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval007.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval008.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval009.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval010.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval011.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval012.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval013.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval014.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval015.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval016.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval017.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval018.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval019.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval020.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval021.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval022.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval023.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval024.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval025.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval026.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval027.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval028.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval029.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval030.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/loaded_environment.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval001.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval002.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval003.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval004.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval005a.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval005b.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval006.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval007.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval008.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval009.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval010.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval011.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval012.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval013.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval014.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval015.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval016.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval017.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval018.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval019.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval020.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval021.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval022.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval023.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval024.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval025.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval026.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval027.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval028.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval029.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval030.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval001.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval002.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval003.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval004.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval005a.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval005b.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval006.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval007.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval008.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval009.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval010.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval011.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval012.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval013.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval014.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval015.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval016.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval017.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval018.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval019.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval020.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval021.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval022.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval023.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval024.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval025.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval026.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval027.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval028.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval029.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval030.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/production_attempts.jsonl`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/production_outputs.jsonl`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/production_seal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/run_binding.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval001/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval001/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval002/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval002/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval003/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval003/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval004/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval004/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval005a/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval005a/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval005b/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval005b/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval006/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval006/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval007/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval007/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval008/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval008/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval009/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval009/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval010/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval010/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval011/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval011/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval012/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval012/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval013/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval013/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval014/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval014/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval015/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval015/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval016/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval016/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval017/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval017/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval018/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval018/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval019/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval019/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval020/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval020/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval021/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval021/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval022/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval022/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval023/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval023/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval024/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval024/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval025/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval025/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval026/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval026/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval027/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval027/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval028/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval028/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval029/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval029/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval030/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval030/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/durable_seal_recovery_v1.json`
- `data/rag/traces/phase5/full-agentic-replication/eval001.json`
- `data/rag/traces/phase5/full-agentic-replication/eval002.json`
- `data/rag/traces/phase5/full-agentic-replication/eval003.json`
- `data/rag/traces/phase5/full-agentic-replication/eval004.json`
- `data/rag/traces/phase5/full-agentic-replication/eval005a.json`
- `data/rag/traces/phase5/full-agentic-replication/eval005b.json`
- `data/rag/traces/phase5/full-agentic-replication/eval006.json`
- `data/rag/traces/phase5/full-agentic-replication/eval007.json`
- `data/rag/traces/phase5/full-agentic-replication/eval008.json`
- `data/rag/traces/phase5/full-agentic-replication/eval009.json`
- `data/rag/traces/phase5/full-agentic-replication/eval010.json`
- `data/rag/traces/phase5/full-agentic-replication/eval011.json`
- `data/rag/traces/phase5/full-agentic-replication/eval012.json`
- `data/rag/traces/phase5/full-agentic-replication/eval013.json`
- `data/rag/traces/phase5/full-agentic-replication/eval014.json`
- `data/rag/traces/phase5/full-agentic-replication/eval015.json`
- `data/rag/traces/phase5/full-agentic-replication/eval016.json`
- `data/rag/traces/phase5/full-agentic-replication/eval017.json`
- `data/rag/traces/phase5/full-agentic-replication/eval018.json`
- `data/rag/traces/phase5/full-agentic-replication/eval019.json`
- `data/rag/traces/phase5/full-agentic-replication/eval020.json`
- `data/rag/traces/phase5/full-agentic-replication/eval021.json`
- `data/rag/traces/phase5/full-agentic-replication/eval022.json`
- `data/rag/traces/phase5/full-agentic-replication/eval023.json`
- `data/rag/traces/phase5/full-agentic-replication/eval024.json`
- `data/rag/traces/phase5/full-agentic-replication/eval025.json`
- `data/rag/traces/phase5/full-agentic-replication/eval026.json`
- `data/rag/traces/phase5/full-agentic-replication/eval027.json`
- `data/rag/traces/phase5/full-agentic-replication/eval028.json`
- `data/rag/traces/phase5/full-agentic-replication/eval029.json`
- `data/rag/traces/phase5/full-agentic-replication/eval030.json`
- `data/rag/traces/phase5/full-agentic-replication/loaded_environment.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval001.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval002.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval003.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval004.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval005a.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval005b.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval006.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval007.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval008.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval009.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval010.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval011.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval012.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval013.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval014.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval015.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval016.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval017.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval018.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval019.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval020.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval021.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval022.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval023.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval024.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval025.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval026.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval027.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval028.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval029.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval030.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval001.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval002.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval003.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval004.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval005a.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval005b.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval006.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval007.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval008.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval009.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval010.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval011.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval012.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval013.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval014.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval015.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval016.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval017.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval018.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval019.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval020.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval021.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval022.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval023.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval024.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval025.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval026.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval027.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval028.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval029.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval030.json`
- `data/rag/traces/phase5/full-agentic-replication/production_attempts.jsonl`
- `data/rag/traces/phase5/full-agentic-replication/production_outputs.jsonl`
- `data/rag/traces/phase5/full-agentic-replication/production_seal.json`
- `data/rag/traces/phase5/full-agentic-replication/run_binding.json`
- `data/versions/corpus-v0.1/articles.jsonl`
- `data/versions/corpus-v0.1/chunks.jsonl`
- `data/versions/corpus-v0.1/corpus_validation_manifest.json`
- `data/versions/corpus_validation_manifest.json`

## Markdown

- `README.md`
- `data/evaluation/generation/ANNOTATION_WORKFLOW.md`
- `data/evaluation/generation/generation_annotation_audit_v1.md`
- `data/evaluation/generation/generation_annotation_v1_report.md`
- `data/evaluation/generation/generation_annotation_v1_review.md`
- `data/evaluation/generation/phase5/phase5a_ablation_spec_v0.md`
- `data/evaluation/generation/phase5/phase5b1_preflight_report_v0.md`
- `data/evaluation/generation/phase5/phase5b2er1_quota_recovery_spec_v0.md`
- `data/evaluation/generation/phase5/phase5b2f_v0/phase5b2f_final_report_v0.md`
- `data/evaluation/generation/phase5/phase5b2r_recovery_report_v0.md`
- `data/evaluation/generation/phase5/phase5b_evaluation_report_v0.md`
- `data/evaluation/generation/phase5/phase5b_report_v0.md`
- `data/evaluation/generation/phase5/phase5c1_v0/phase5c1_decision_log_v0.md`
- `data/evaluation/generation/phase5/phase5c1_v0/phase5c1_research_synthesis_v0.md`
- `data/evaluation/generation/phase5/phase5c2_v0/phase5c2_challenge_set_design_v0.md`
- `data/evaluation/generation/phase5/phase5c2_v0/phase5c2_decision_log_v0.md`
- `data/evaluation/generation/phase5/phase5c2_v0/phase5c2_evaluation_protocol_draft_v0.md`
- `data/evaluation/generation/phase5/phase5c2_v0/phase5c2_v2_requirements_design_v0.md`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_design_amendments_v0.md`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_external_review_v0.md`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_frozen_design_spec_v0.md`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_margin_governance_v0.md`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_quota_scheduler_requirements_v0.md`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/phase5c4d_adjudication_report_v0.md`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/phase5c4c1_comparison_report_v0.md`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/fresh_reviewer_b_handoff_v1.md`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/phase5c4b0_review_summary_v0.md`
- `data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_adjudicator_c_protocol_v0.md`
- `data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_research_claim_boundaries_v0.md`
- `data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_resource_constrained_amendment_v0.md`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_construction_report_v0.md`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_contamination_report_v0.md`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b/README_independent_review_v0.md`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_packet_v1/reviewer_b_annotation_instructions_v1.md`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/phase5c4b_review_summary_v0.md`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/phase5c4b_review_summary_v1.md`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_phase5c4b_review_summary_v1.md`
- `data/evaluation/generation/reports/agentic_rag_eval_v1_agentic-v1.md`
- `data/evaluation/generation/reports/agentic_trace_analysis_v0.md`
- `data/evaluation/generation/reports/standard_rag_eval_v0.md`
- `data/evaluation/generation/reports/standard_rag_failure_analysis_v0.md`
- `data/evaluation/human_review_report.md`
- `data/evaluation/results/bge-reranker-v2-m3-v0_failures.md`
- `data/evaluation/results/bm25-simple-v0_failures.md`
- `data/evaluation/results/bm25-vs-dense-comparison.md`
- `data/evaluation/results/candidate-union-v0_report.md`
- `data/evaluation/results/dense-jina-v3-v0_failures.md`
- `data/evaluation/results/hybrid-rrf-v0_failures.md`
- `data/evaluation/results/retriever-comparison-v0.md`
- `data/evaluation/retrieval_eval_annotation_report.md`
- `data/validation/manual_verification/05-2026-TT-BKHCN.verification.md`
- `data/validation/manual_verification/134-2025-QH15.verification.md`
- `data/validation/manual_verification/142-2026-ND-CP.verification.md`
- `retriever-reranker-comparison-v0.md`

## Prompts/templates

- `prompts/legal_rag_v0.txt`

## Tests (all files under tests/)

- `tests/__pycache__/test_agentic_evaluation.cpython-312.pyc`
- `tests/__pycache__/test_agentic_rag.cpython-312.pyc`
- `tests/__pycache__/test_generation_eval.cpython-312.pyc`
- `tests/__pycache__/test_rag_runtime.cpython-312.pyc`
- `tests/phase5_run_suite.py`
- `tests/phase5_synthetic_worker.py`
- `tests/phase5_test_support.py`
- `tests/test_agentic_evaluation.py`
- `tests/test_agentic_rag.py`
- `tests/test_generation_eval.py`
- `tests/test_phase5_ablation_runner.py`
- `tests/test_phase5_evaluation_quota_recovery.py`
- `tests/test_phase5_leakage.py`
- `tests/test_phase5_preflight.py`
- `tests/test_phase5_seal_recovery_v1.py`
- `tests/test_rag_runtime.py`

## Data directories

- `data/evaluation`
- `data/evaluation/backups`
- `data/evaluation/generation`
- `data/evaluation/generation/backups`
- `data/evaluation/generation/partials`
- `data/evaluation/generation/phase5`
- `data/evaluation/generation/phase5/agentic-v1-no-answer-revision`
- `data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion`
- `data/evaluation/generation/phase5/execution_tools`
- `data/evaluation/generation/phase5/full-agentic-replication`
- `data/evaluation/generation/phase5/phase5b2e_v0`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval001`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval001/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval002`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval002/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval003`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval003/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval004`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval004/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval005a`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval005a/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval005b`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval005b/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval006`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval006/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval007`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval007/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval008`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval008/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval009`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval009/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval010`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval010/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval011`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval011/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval012`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval012/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval012/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval013`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval013/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval013/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval015`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval015/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval017`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval017/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval017/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval018`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval018/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval018/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval027`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval027/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval027/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval028`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval028/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval029`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval029/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval030`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval030/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval001`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval001/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval002`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval002/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval003`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval003/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval004`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval004/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval005a`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval005a/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval005b`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval005b/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval006`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval006/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval007`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval007/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval008`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval008/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval009`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval009/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval010`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval010/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval011`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval011/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval012`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval012/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval013`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval013/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval014`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval014/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval014/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval021`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval021/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval028`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval028/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval029`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval029/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval030`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval030/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval001`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval001/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval002`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval002/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval003`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval003/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval004`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval004/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval005a`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval005a/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval005b`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval005b/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval006`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval006/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval007`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval007/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval008`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval008/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval009`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval009/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval010`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval010/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval011`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval011/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval012`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval012/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval013`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval013/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval014`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval014/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval015`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval015/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval015/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval016`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval016/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval017`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval017/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval017/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval020`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval020/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/2`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/3`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval029`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval029/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval030`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval030/1`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records`
- `data/evaluation/generation/phase5/phase5b2er2_v1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval014`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval014/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval016`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval016/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval019`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval019/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval020`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval020/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval022`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval022/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval023`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval023/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/2`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval025`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval025/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval026`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval026/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval015`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval015/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval016`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval016/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval017`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval017/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval018`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval018/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval019`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval019/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval020`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval020/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval022`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval022/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval023`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval023/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval024`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval024/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval025`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval025/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval026`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval026/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval027`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval027/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval021`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval021/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval022`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval022/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval023`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval023/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval024`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval024/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval025`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval025/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval026`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval026/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval027`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval027/1`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval028`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval028/1`
- `data/evaluation/generation/phase5/phase5b2f_v0`
- `data/evaluation/generation/phase5/phase5b2f_v0/agentic-v1-no-answer-revision`
- `data/evaluation/generation/phase5/phase5b2f_v0/agentic-v1-no-evidence-expansion`
- `data/evaluation/generation/phase5/phase5b2f_v0/analysis_tools`
- `data/evaluation/generation/phase5/phase5b2f_v0/full-agentic-replication`
- `data/evaluation/generation/phase5/phase5c1_v0`
- `data/evaluation/generation/phase5/phase5c2_v0`
- `data/evaluation/generation/phase5/phase5c3_v0`
- `data/evaluation/generation/phase5/phase5c4_v0`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b1_reference_preparation_v0`
- `data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_packet_v1`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1`
- `data/evaluation/generation/reports`
- `data/evaluation/results`
- `data/extracted`
- `data/indexes`
- `data/indexes/bge-reranker-v2-m3-v0`
- `data/indexes/dense-jina-v3-v0`
- `data/indexes/hybrid-rrf-v0`
- `data/processed`
- `data/rag`
- `data/rag/traces`
- `data/rag/traces/agentic-rag-v1`
- `data/rag/traces/agentic-rag-v1/agentic-v1`
- `data/rag/traces/phase5`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval001`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval002`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval003`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval004`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval005a`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval005b`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval006`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval007`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval008`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval009`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval010`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval011`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval012`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval013`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval014`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval015`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval016`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval017`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval018`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval019`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval020`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval021`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval022`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval023`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval024`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval025`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval026`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval027`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval028`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval029`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval030`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval001`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval002`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval003`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval004`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval005a`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval005b`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval006`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval007`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval008`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval009`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval010`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval011`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval012`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval013`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval014`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval015`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval016`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval017`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval018`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval019`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval020`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval021`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval022`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval023`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval024`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval025`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval026`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval027`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval028`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval029`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval030`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3`
- `data/rag/traces/phase5/full-agentic-replication`
- `data/rag/traces/phase5/full-agentic-replication/attempts`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval001`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval002`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval003`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval004`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval005a`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval005b`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval006`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval007`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval008`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval009`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval010`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval011`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval012`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval013`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval014`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval015`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval016`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval017`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval018`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval019`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval020`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval021`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval022`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval023`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval024`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval025`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval026`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval027`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval028`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval029`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval030`
- `data/rag/traces/phase5/full-agentic-replication/observations`
- `data/rag/traces/phase5/full-agentic-replication/outputs`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3`
- `data/raw`
- `data/raw/docx`
- `data/raw/pdf`
- `data/source_registry`
- `data/source_registry/backups`
- `data/validation`
- `data/validation/manual_verification`
- `data/versions`
- `data/versions/corpus-v0.1`

## Generated artifacts (may also be frozen)

- `data/evaluation/generation/agentic_rag_eval_v1_agentic-v1.jsonl`
- `data/evaluation/generation/agentic_rag_metrics_v1_agentic-v1.json`
- `data/evaluation/generation/agentic_trace_analysis_metrics_v0.json`
- `data/evaluation/generation/agentic_trace_analysis_v0.jsonl`
- `data/evaluation/generation/failure_analysis_metrics_v0.json`
- `data/evaluation/generation/failure_analysis_points_v0.jsonl`
- `data/evaluation/generation/failure_analysis_queries_v0.json`
- `data/evaluation/generation/generation_annotation_v1_report.md`
- `data/evaluation/generation/partials/standard_rag_eval_v0_partial.20260902-151753.jsonl`
- `data/evaluation/generation/partials/standard_rag_eval_v0_partial.20260902-155801.jsonl`
- `data/evaluation/generation/phase5/agentic-v1-no-answer-revision/evaluation.jsonl`
- `data/evaluation/generation/phase5/agentic-v1-no-answer-revision/evaluation_attempts.jsonl`
- `data/evaluation/generation/phase5/agentic-v1-no-answer-revision/metrics.json`
- `data/evaluation/generation/phase5/agentic-v1-no-answer-revision/run_manifest.json`
- `data/evaluation/generation/phase5/agentic-v1-no-answer-revision/variant_manifest.json`
- `data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion/evaluation.jsonl`
- `data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion/evaluation_attempts.jsonl`
- `data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion/metrics.json`
- `data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion/run_manifest.json`
- `data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion/variant_manifest.json`
- `data/evaluation/generation/phase5/contrast_R2_A1.json`
- `data/evaluation/generation/phase5/contrast_R2_A2.json`
- `data/evaluation/generation/phase5/execution_environment_v0.json`
- `data/evaluation/generation/phase5/execution_tools/launch_frozen_v0.py`
- `data/evaluation/generation/phase5/execution_tools/report_incomplete_v0.py`
- `data/evaluation/generation/phase5/full-agentic-replication/evaluation.jsonl`
- `data/evaluation/generation/phase5/full-agentic-replication/evaluation_attempts.jsonl`
- `data/evaluation/generation/phase5/full-agentic-replication/metrics.json`
- `data/evaluation/generation/phase5/full-agentic-replication/run_manifest.json`
- `data/evaluation/generation/phase5/full-agentic-replication/variant_manifest.json`
- `data/evaluation/generation/phase5/integrity_before_after_v0.json`
- `data/evaluation/generation/phase5/phase5a_ablation_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5a_ablation_spec_v0.md`
- `data/evaluation/generation/phase5/phase5b1_preflight_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5b1_preflight_report_v0.md`
- `data/evaluation/generation/phase5/phase5b2_preflight_rerun_v0.json`
- `data/evaluation/generation/phase5/phase5b2_preflight_tests_v0.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval001/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval001/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval002/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval002/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval003/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval003/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval004/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval004/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval005a/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval005a/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval005b/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval005b/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval006/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval006/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval007/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval007/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval008/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval008/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval009/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval009/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval010/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval010/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval011/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval011/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval012/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval012/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval012/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval012/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval013/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval013/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval013/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval013/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval015/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval015/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval017/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval017/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval017/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval017/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval018/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval018/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval018/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval018/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval027/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval027/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval027/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval027/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval028/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval028/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval029/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval029/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval030/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval030/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/evaluation.jsonl`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/evaluation_attempts.jsonl`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/metrics.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval001.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval002.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval003.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval004.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval005a.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval005b.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval006.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval007.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval008.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval009.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval010.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval011.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval012.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval013.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval014.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval015.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval016.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval017.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval018.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval019.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval020.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval021.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval022.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval023.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval024.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval025.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval026.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval027.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval028.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval029.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval030.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval001/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval001/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval002/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval002/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval003/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval003/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval004/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval004/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval005a/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval005a/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval005b/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval005b/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval006/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval006/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval007/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval007/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval008/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval008/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval009/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval009/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval010/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval010/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval011/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval011/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval012/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval012/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval013/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval013/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval014/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval014/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval014/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval014/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval021/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval021/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval028/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval028/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval029/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval029/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval030/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval030/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/evaluation.jsonl`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/evaluation_attempts.jsonl`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/metrics.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval001.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval002.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval003.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval004.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval005a.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval005b.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval006.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval007.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval008.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval009.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval010.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval011.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval012.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval013.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval014.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval015.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval016.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval017.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval018.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval019.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval020.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval021.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval022.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval023.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval024.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval025.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval026.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval027.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval028.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval029.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval030.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/analysis_validation.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/analyze_frozen.py`
- `data/evaluation/generation/phase5/phase5b2e_v0/console_output.txt`
- `data/evaluation/generation/phase5/phase5b2e_v0/contrast_R2_A1.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/contrast_R2_A2.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/evaluate_frozen.py`
- `data/evaluation/generation/phase5/phase5b2e_v0/evaluation_protocol.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/evaluation_protocol_initial.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/evaluator.lock`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval001/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval001/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval002/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval002/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval003/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval003/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval004/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval004/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval005a/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval005a/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval005b/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval005b/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval006/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval006/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval007/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval007/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval008/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval008/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval009/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval009/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval010/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval010/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval011/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval011/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval012/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval012/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval013/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval013/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval014/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval014/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval015/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval015/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval015/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval015/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval016/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval016/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval017/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval017/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval017/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval017/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval020/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval020/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval029/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval029/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval030/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval030/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/evaluation.jsonl`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/evaluation_attempts.jsonl`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/metrics.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval001.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval002.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval003.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval004.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval005a.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval005b.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval006.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval007.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval008.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval009.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval010.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval011.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval012.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval013.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval014.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval015.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval016.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval017.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval018.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval019.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval020.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval021.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval022.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval023.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval024.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval025.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval026.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval027.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval028.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval029.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval030.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/integrity_after.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/integrity_before.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/provenance.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/recovery_gate.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/render_report.py`
- `data/evaluation/generation/phase5/phase5b2e_v0/replication_R1_R2.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/reporting_correction_validation.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/validate_analysis.py`
- `data/evaluation/generation/phase5/phase5b2er1_console_v0.txt`
- `data/evaluation/generation/phase5/phase5b2er1_integrity_v0.json`
- `data/evaluation/generation/phase5/phase5b2er1_quota_recovery_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5b2er1_quota_recovery_spec_v0.md`
- `data/evaluation/generation/phase5/phase5b2er1_quota_recovery_tests_v0.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval014/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval014/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval014/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval014/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval016/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval016/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval016/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval016/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval019/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval019/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval019/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval019/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval020/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval020/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval020/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval020/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval022/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval022/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval022/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval022/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval023/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval023/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval023/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval023/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/2/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/2/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/2/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/2/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval025/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval025/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval025/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval025/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval026/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval026/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval026/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval026/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval015/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval015/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval015/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval015/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval016/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval016/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval016/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval016/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval017/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval017/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval017/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval017/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval018/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval018/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval018/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval018/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval019/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval019/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval019/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval019/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval020/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval020/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval020/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval020/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval022/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval022/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval022/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval022/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval023/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval023/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval023/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval023/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval024/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval024/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval024/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval024/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval025/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval025/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval025/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval025/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval026/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval026/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval026/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval026/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval027/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval027/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval027/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval027/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval021/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval021/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval021/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval021/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval022/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval022/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval022/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval022/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval023/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval023/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval023/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval023/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval024/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval024/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval024/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval024/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval025/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval025/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval025/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval025/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval026/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval026/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval026/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval026/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval027/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval027/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval027/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval027/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval028/1/evaluation_record.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval028/1/receipt.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval028/1/started.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval028/1/wire_response.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/execution_driver_session_0001.py`
- `data/evaluation/generation/phase5/phase5b2er2_v1/execution_driver_session_0002.py`
- `data/evaluation/generation/phase5/phase5b2er2_v1/phase5b2er2_session_0001_report.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/phase5b2er2_session_0002_report.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/protocol_binding.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/quota_stop_0001.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/quota_stop_0001_resume_authorization.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/session.lock`
- `data/evaluation/generation/phase5/phase5b2er2_v1/session_0001_binding.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/session_0001_integrity.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/session_0002_binding.json`
- `data/evaluation/generation/phase5/phase5b2er2_v1/session_0002_integrity.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/agentic-v1-no-answer-revision/evaluation_complete.jsonl`
- `data/evaluation/generation/phase5/phase5b2f_v0/agentic-v1-no-answer-revision/metrics.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/agentic-v1-no-evidence-expansion/evaluation_complete.jsonl`
- `data/evaluation/generation/phase5/phase5b2f_v0/agentic-v1-no-evidence-expansion/metrics.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/analysis_tools/offline_analysis_v0.py`
- `data/evaluation/generation/phase5/phase5b2f_v0/analysis_tools/phase5b2f_gate.py`
- `data/evaluation/generation/phase5/phase5b2f_v0/analysis_tools/verify_final_analysis_v0.py`
- `data/evaluation/generation/phase5/phase5b2f_v0/bootstrap_R2_A1.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/bootstrap_R2_A2.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/canonical_judgments_manifest.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/contrast_R2_A1.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/contrast_R2_A2.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/efficiency_v0.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/final_artifact_hashes_v0.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/full-agentic-replication/evaluation_complete.jsonl`
- `data/evaluation/generation/phase5/phase5b2f_v0/full-agentic-replication/metrics.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/integrity_before_after_v0.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/integrity_before_inventory_v0.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/phase5b2f_console_v0.txt`
- `data/evaluation/generation/phase5/phase5b2f_v0/phase5b2f_final_report_v0.md`
- `data/evaluation/generation/phase5/phase5b2f_v0/phase5b2f_metrics_v0.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/point_transitions_R1_R2.jsonl`
- `data/evaluation/generation/phase5/phase5b2f_v0/point_transitions_R2_A1.jsonl`
- `data/evaluation/generation/phase5/phase5b2f_v0/point_transitions_R2_A2.jsonl`
- `data/evaluation/generation/phase5/phase5b2f_v0/provenance_v0.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/recovery_completion_gate_v0.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/replication_R1_R2.json`
- `data/evaluation/generation/phase5/phase5b2f_v0/validation_v0.json`
- `data/evaluation/generation/phase5/phase5b2r_negative_tests_v1.json`
- `data/evaluation/generation/phase5/phase5b2r_recovery_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5b2r_recovery_protocol_v1.json`
- `data/evaluation/generation/phase5/phase5b2r_recovery_report_v0.md`
- `data/evaluation/generation/phase5/phase5b_evaluation_metrics_v0.json`
- `data/evaluation/generation/phase5/phase5b_evaluation_report_v0.md`
- `data/evaluation/generation/phase5/phase5b_report_v0.md`
- `data/evaluation/generation/phase5/phase5c1_v0/consolidate_research_v0.py`
- `data/evaluation/generation/phase5/phase5c1_v0/final_artifact_hashes_v0.json`
- `data/evaluation/generation/phase5/phase5c1_v0/integrity_before_after_v0.json`
- `data/evaluation/generation/phase5/phase5c1_v0/integrity_before_inventory_v0.json`
- `data/evaluation/generation/phase5/phase5c1_v0/phase5c1_console_v0.txt`
- `data/evaluation/generation/phase5/phase5c1_v0/phase5c1_decision_log_v0.md`
- `data/evaluation/generation/phase5/phase5c1_v0/phase5c1_evidence_matrix_v0.json`
- `data/evaluation/generation/phase5/phase5c1_v0/phase5c1_exploratory_diagnostic_v0.json`
- `data/evaluation/generation/phase5/phase5c1_v0/phase5c1_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5c1_v0/phase5c1_problem_requirement_map_v0.json`
- `data/evaluation/generation/phase5/phase5c1_v0/phase5c1_research_synthesis_v0.md`
- `data/evaluation/generation/phase5/phase5c1_v0/phase5c1_validation_v0.json`
- `data/evaluation/generation/phase5/phase5c2_v0/final_artifact_hashes_v0.json`
- `data/evaluation/generation/phase5/phase5c2_v0/integrity_baseline_v0.json`
- `data/evaluation/generation/phase5/phase5c2_v0/integrity_before_after_v0.json`
- `data/evaluation/generation/phase5/phase5c2_v0/phase5c2_challenge_set_design_v0.md`
- `data/evaluation/generation/phase5/phase5c2_v0/phase5c2_console_v0.txt`
- `data/evaluation/generation/phase5/phase5c2_v0/phase5c2_decision_log_v0.md`
- `data/evaluation/generation/phase5/phase5c2_v0/phase5c2_evaluation_protocol_draft_v0.md`
- `data/evaluation/generation/phase5/phase5c2_v0/phase5c2_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5c2_v0/phase5c2_requirement_validation_matrix_v0.json`
- `data/evaluation/generation/phase5/phase5c2_v0/phase5c2_trace_schema_design_v0.json`
- `data/evaluation/generation/phase5/phase5c2_v0/phase5c2_v2_requirements_design_v0.md`
- `data/evaluation/generation/phase5/phase5c2_v0/phase5c2_validation_v0.json`
- `data/evaluation/generation/phase5/phase5c3_v0/final_artifact_hashes_v0.json`
- `data/evaluation/generation/phase5/phase5c3_v0/integrity_baseline_v0.json`
- `data/evaluation/generation/phase5/phase5c3_v0/integrity_before_after_v0.json`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_console_v0.txt`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_controller_status_decision_table_v0.json`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_decision_table_validation_v0.json`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_design_amendments_v0.md`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_external_review_v0.md`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_freeze_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_frozen_design_spec_v0.md`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_margin_governance_v0.md`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_quota_scheduler_requirements_v0.md`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_spec_bindings_v0.json`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_trace_matrix_amendment_v0.json`
- `data/evaluation/generation/phase5/phase5c3_v0/phase5c3_validation_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/adjudication_corpus_audit_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/adjudication_issue_resolutions_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/candidate_admission_decisions_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/final_adjudicated_annotations_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/final_retained_36_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/final_split_assignment_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/input_contamination_incident_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/integrity_before_after_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/phase5c4d_adjudication_report_v0.md`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/phase5c4d_console_v0.txt`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/phase5c4d_dimension_summary_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/phase5c4d_selection_summary_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/phase5c4d_validation_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_applicability_sufficiency_comparison_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_aspect_mapping_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_candidate_alignment_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_contamination_comparison_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_corpus_audit_comparison_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_disagreement_registry_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_scope_comparison_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_support_comparison_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/artifact_hashes_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/build_comparison_v0.py`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/comparison_access_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/comparison_check_results_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/final_artifact_hashes_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/integrity_baseline_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/integrity_before_after_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/phase5c4c1_agreement_metrics_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/phase5c4c1_comparison_report_v0.md`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/phase5c4c1_console_v0.txt`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/phase5c4c1_disagreement_summary_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/phase5c4c1_validation_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/semantic_mapping_decisions_v0.py`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/source_integrity_validation_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/validate_comparison_v0.py`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/annotation_A_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/authored_tasks_v0.py`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/build_construction_v0.py`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/challenge_candidates_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/cluster_rationales_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/construction_notes_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/contaminated_packet_quarantine_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/contamination_screening_details_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/corpus_absence_audits_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/corpus_mapping_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/custodian_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/exclusion_log_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/explicit_asks_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/exposure_events_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/artifact_hashes_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/execution_and_access_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/fresh_reviewer_b_handoff_v1.md`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/integrity_baseline_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/integrity_before_after_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/phase5c4b0_console_v0.txt`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/phase5c4b0_review_summary_v0.md`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/phase5c4b0_validation_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/sanitize_reviewer_b_v1.py`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b1_reference_preparation_v0/medical_reference_projection_audit_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b1_reference_preparation_v0/phase5c4b1_console_v0.txt`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b1_reference_preparation_v0/prepare_medical_reference_v1.py`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/reviewer_b_comparison_after_independent_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/reviewer_b_id_mapping_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/reviewer_b_packet_projection_audit_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/reviewer_b_shuffle_provenance_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/custodian/split_assignment_provisional_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/artifact_hashes_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/finalize_amendment_v0.py`
- `data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/integrity_baseline_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/integrity_before_after_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_adjudicator_c_protocol_v0.md`
- `data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_amendment_console_v0.txt`
- `data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_amendment_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_amendment_validation_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_research_claim_boundaries_v0.md`
- `data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_resource_constrained_amendment_v0.md`
- `data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_selection_rules_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/artifact_hashes_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/frozen_source_checks_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/integrity_baseline_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/integrity_before_after_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_access_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_aggregate_composition_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_candidate_summary_v0.csv`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_cluster_summary_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_console_v0.txt`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_construction_report_v0.md`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_contamination_report_v0.md`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_dimension_matrix_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_validation_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b/01_independent_review_units_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b/README_independent_review_v0.md`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b/complete_corpus_evidence_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b/contamination_query_only_sources_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_packet_v1/contamination_reference_medical_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_packet_v1/reviewer_b_annotation_instructions_v1.md`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_packet_v1/reviewer_b_packet_manifest_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_packet_v1/reviewer_b_queries_v1.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/annotation_B_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/integrity_baseline_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/integrity_before_after_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/phase5c4b_access_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/phase5c4b_agreement_ready_summary_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/phase5c4b_console_v0.txt`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/phase5c4b_review_summary_v0.md`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/phase5c4b_validation_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/reviewer_b_contamination_flags_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/reviewer_b_corpus_audit_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/reviewer_b_manifest_v0.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/annotation_B_pre_anchor_correction_v1.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/annotation_B_substantive_locked_v1.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/annotation_B_v1.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/annotation_structural_validation_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/authored_specs_v1.py`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/build_b_annotations_v1.py`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/complete_medical_screen_v1.py`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/evidence_anchor_corrections_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/finalize_b_v1.py`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/frozen_design_binding_checks_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/generated_artifact_hashes_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/historical_31_query_text_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/integrity_baseline_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/integrity_before_after_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/medical_screen_completion_validation_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/medical_screen_integrity_baseline_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/medical_screen_integrity_before_after_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/medical_screen_pre_read_seal_audit_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/medical_screening_completed_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/packet_schema_validation_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/phase5c4b_access_manifest_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/phase5c4b_agreement_ready_summary_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/phase5c4b_console_v1.txt`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/phase5c4b_review_summary_v1.md`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/phase5c4b_validation_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_generated_artifact_hashes_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_phase5c4b_access_manifest_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_phase5c4b_agreement_ready_summary_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_phase5c4b_console_v1.txt`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_phase5c4b_review_summary_v1.md`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_phase5c4b_validation_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_reviewer_b_contamination_flags_v1.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_reviewer_b_manifest_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/preexisting_inventory_paths_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/refine_bundle_anchors_v1.py`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/resume_audit_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/reviewer_b_contamination_flags_v1.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/reviewer_b_corpus_audit_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/reviewer_b_manifest_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/reviewer_b_medical_contamination_screen_v1.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/scoped_corpus_reviews_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/screen_text_v1.py`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/substantive_lock_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/text_screen_provenance_v1.json`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/validate_b_v1.py`
- `data/evaluation/generation/phase5/production_seal_validation_v0.json`
- `data/evaluation/generation/phase5/query_inputs_v0.json`
- `data/evaluation/generation/phase5/replication_R1_R2.json`
- `data/evaluation/generation/phase5/report_artifact_hashes_v0.json`
- `data/evaluation/generation/phase5/report_validation_v0.json`
- `data/evaluation/generation/reports/agentic_rag_eval_v1_agentic-v1.md`
- `data/evaluation/generation/reports/agentic_trace_analysis_v0.md`
- `data/evaluation/generation/reports/standard_rag_eval_v0.md`
- `data/evaluation/generation/reports/standard_rag_failure_analysis_v0.md`
- `data/evaluation/generation/standard_rag_eval_v0.jsonl`
- `data/evaluation/generation/standard_rag_metrics_v0.json`
- `data/evaluation/results/bge-reranker-v2-m3-v0_by_difficulty.csv`
- `data/evaluation/results/bge-reranker-v2-m3-v0_by_query_type.csv`
- `data/evaluation/results/bge-reranker-v2-m3-v0_failures.md`
- `data/evaluation/results/bge-reranker-v2-m3-v0_metrics.json`
- `data/evaluation/results/bge-reranker-v2-m3-v0_per_query.csv`
- `data/evaluation/results/bm25-simple-v0_by_difficulty.csv`
- `data/evaluation/results/bm25-simple-v0_by_query_type.csv`
- `data/evaluation/results/bm25-simple-v0_failures.md`
- `data/evaluation/results/bm25-simple-v0_metrics.json`
- `data/evaluation/results/bm25-simple-v0_per_query.csv`
- `data/evaluation/results/bm25-vs-dense-comparison.md`
- `data/evaluation/results/candidate-union-v0_metrics.json`
- `data/evaluation/results/candidate-union-v0_missing_gold.csv`
- `data/evaluation/results/candidate-union-v0_per_query.csv`
- `data/evaluation/results/candidate-union-v0_report.md`
- `data/evaluation/results/dense-jina-v3-v0_by_difficulty.csv`
- `data/evaluation/results/dense-jina-v3-v0_by_query_type.csv`
- `data/evaluation/results/dense-jina-v3-v0_failures.md`
- `data/evaluation/results/dense-jina-v3-v0_metrics.json`
- `data/evaluation/results/dense-jina-v3-v0_per_query.csv`
- `data/evaluation/results/hybrid-rrf-v0_by_difficulty.csv`
- `data/evaluation/results/hybrid-rrf-v0_by_query_type.csv`
- `data/evaluation/results/hybrid-rrf-v0_failures.md`
- `data/evaluation/results/hybrid-rrf-v0_metrics.json`
- `data/evaluation/results/hybrid-rrf-v0_per_query.csv`
- `data/evaluation/results/retriever-comparison-v0.md`
- `data/extracted/05-2026-TT-BKHCN.cleaned.txt`
- `data/extracted/05-2026-TT-BKHCN.raw.txt`
- `data/extracted/134-2025-QH15.cleaned.txt`
- `data/extracted/134-2025-QH15.raw.txt`
- `data/extracted/142-2026-ND-CP.cleaned.txt`
- `data/extracted/142-2026-ND-CP.raw.txt`
- `data/indexes/bge-reranker-v2-m3-v0/reranker_manifest.json`
- `data/indexes/dense-jina-v3-v0/chunk_ids.json`
- `data/indexes/dense-jina-v3-v0/embeddings.npy`
- `data/indexes/dense-jina-v3-v0/index_manifest.json`
- `data/indexes/hybrid-rrf-v0/hybrid_manifest.json`
- `data/processed/articles.jsonl`
- `data/processed/chunks.jsonl`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval001.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval002.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval003.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval004.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval005a.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval005b.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval006.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval007.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval008.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval009.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval010.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval011.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval012.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval013.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval014.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval015.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval016.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval017.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval018.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval019.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval020.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval021.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval022.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval023.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval024.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval025.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval026.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval027.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval028.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval029.json`
- `data/rag/traces/agentic-rag-v1/agentic-v1/eval030.json`
- `data/rag/traces/agentic-rag-v1_20260909T132334.960415Z.json`
- `data/rag/traces/agentic-rag-v1_20260909T132915.670264Z.json`
- `data/rag/traces/agentic-rag-v1_20260913T071538.629769Z.json`
- `data/rag/traces/agentic-rag-v1_20260913T072604.572183Z.json`
- `data/rag/traces/agentic-rag-v1_smoke.json`
- `data/rag/traces/legal-rag-v0_20260824T082500.431067Z.json`
- `data/rag/traces/legal-rag-v0_20260824T083023.964302Z.json`
- `data/rag/traces/legal-rag-v0_20260824T083324.619096Z.json`
- `data/rag/traces/legal-rag-v0_20260824T083822.282992Z.json`
- `data/rag/traces/legal-rag-v0_20260824T084241.384282Z.json`
- `data/rag/traces/legal-rag-v0_20260824T084747.340310Z.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval001/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval001/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval002/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval002/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval003/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval003/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval004/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval004/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval005a/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval005a/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval005b/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval005b/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval006/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval006/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval007/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval007/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval008/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval008/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval009/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval009/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval010/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval010/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval011/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval011/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval012/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval012/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval013/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval013/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval014/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval014/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval015/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval015/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval016/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval016/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval017/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval017/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval018/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval018/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval019/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval019/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval020/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval020/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval021/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval021/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval022/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval022/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval023/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval023/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval024/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval024/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval025/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval025/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval026/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval026/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval027/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval027/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval028/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval028/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval029/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval029/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval030/started.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval030/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/durable_seal_recovery_v1.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval001.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval002.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval003.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval004.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval005a.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval005b.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval006.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval007.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval008.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval009.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval010.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval011.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval012.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval013.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval014.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval015.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval016.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval017.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval018.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval019.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval020.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval021.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval022.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval023.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval024.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval025.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval026.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval027.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval028.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval029.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/eval030.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/loaded_environment.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval001.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval002.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval003.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval004.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval005a.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval005b.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval006.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval007.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval008.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval009.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval010.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval011.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval012.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval013.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval014.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval015.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval016.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval017.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval018.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval019.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval020.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval021.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval022.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval023.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval024.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval025.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval026.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval027.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval028.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval029.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval030.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval001.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval002.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval003.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval004.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval005a.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval005b.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval006.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval007.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval008.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval009.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval010.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval011.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval012.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval013.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval014.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval015.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval016.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval017.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval018.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval019.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval020.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval021.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval022.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval023.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval024.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval025.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval026.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval027.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval028.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval029.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval030.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/production_attempts.jsonl`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/production_outputs.jsonl`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/production_seal.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/run_binding.json`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/block.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/configuration_xlm_roberta.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/embedding.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mha.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mlp.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_lora.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_xlm_roberta.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/rotary.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/stochastic_depth.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/xlm_padding.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/worker.lock`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval001/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval001/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval002/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval002/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval003/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval003/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval004/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval004/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval005a/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval005a/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval005b/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval005b/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval006/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval006/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval007/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval007/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval008/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval008/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval009/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval009/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval010/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval010/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval011/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval011/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval012/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval012/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval013/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval013/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval014/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval014/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval015/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval015/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval016/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval016/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval017/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval017/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval018/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval018/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval019/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval019/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval020/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval020/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval021/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval021/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval022/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval022/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval023/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval023/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval024/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval024/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval025/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval025/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval026/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval026/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval027/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval027/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval028/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval028/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval029/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval029/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval030/started.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval030/terminal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/durable_seal_recovery_v1.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval001.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval002.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval003.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval004.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval005a.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval005b.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval006.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval007.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval008.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval009.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval010.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval011.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval012.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval013.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval014.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval015.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval016.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval017.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval018.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval019.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval020.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval021.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval022.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval023.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval024.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval025.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval026.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval027.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval028.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval029.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval030.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/loaded_environment.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval001.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval002.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval003.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval004.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval005a.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval005b.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval006.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval007.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval008.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval009.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval010.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval011.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval012.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval013.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval014.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval015.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval016.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval017.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval018.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval019.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval020.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval021.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval022.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval023.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval024.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval025.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval026.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval027.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval028.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval029.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval030.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval001.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval002.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval003.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval004.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval005a.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval005b.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval006.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval007.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval008.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval009.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval010.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval011.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval012.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval013.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval014.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval015.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval016.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval017.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval018.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval019.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval020.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval021.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval022.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval023.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval024.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval025.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval026.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval027.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval028.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval029.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval030.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/production_attempts.jsonl`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/production_outputs.jsonl`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/production_seal.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/run_binding.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/block.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/configuration_xlm_roberta.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/embedding.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mha.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mlp.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_lora.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_xlm_roberta.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/rotary.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/stochastic_depth.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/xlm_padding.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/worker.lock`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval001/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval001/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval002/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval002/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval003/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval003/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval004/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval004/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval005a/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval005a/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval005b/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval005b/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval006/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval006/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval007/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval007/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval008/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval008/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval009/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval009/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval010/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval010/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval011/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval011/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval012/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval012/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval013/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval013/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval014/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval014/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval015/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval015/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval016/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval016/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval017/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval017/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval018/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval018/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval019/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval019/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval020/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval020/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval021/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval021/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval022/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval022/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval023/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval023/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval024/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval024/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval025/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval025/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval026/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval026/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval027/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval027/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval028/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval028/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval029/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval029/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval030/started.json`
- `data/rag/traces/phase5/full-agentic-replication/attempts/eval030/terminal.json`
- `data/rag/traces/phase5/full-agentic-replication/durable_seal_recovery_v1.json`
- `data/rag/traces/phase5/full-agentic-replication/eval001.json`
- `data/rag/traces/phase5/full-agentic-replication/eval002.json`
- `data/rag/traces/phase5/full-agentic-replication/eval003.json`
- `data/rag/traces/phase5/full-agentic-replication/eval004.json`
- `data/rag/traces/phase5/full-agentic-replication/eval005a.json`
- `data/rag/traces/phase5/full-agentic-replication/eval005b.json`
- `data/rag/traces/phase5/full-agentic-replication/eval006.json`
- `data/rag/traces/phase5/full-agentic-replication/eval007.json`
- `data/rag/traces/phase5/full-agentic-replication/eval008.json`
- `data/rag/traces/phase5/full-agentic-replication/eval009.json`
- `data/rag/traces/phase5/full-agentic-replication/eval010.json`
- `data/rag/traces/phase5/full-agentic-replication/eval011.json`
- `data/rag/traces/phase5/full-agentic-replication/eval012.json`
- `data/rag/traces/phase5/full-agentic-replication/eval013.json`
- `data/rag/traces/phase5/full-agentic-replication/eval014.json`
- `data/rag/traces/phase5/full-agentic-replication/eval015.json`
- `data/rag/traces/phase5/full-agentic-replication/eval016.json`
- `data/rag/traces/phase5/full-agentic-replication/eval017.json`
- `data/rag/traces/phase5/full-agentic-replication/eval018.json`
- `data/rag/traces/phase5/full-agentic-replication/eval019.json`
- `data/rag/traces/phase5/full-agentic-replication/eval020.json`
- `data/rag/traces/phase5/full-agentic-replication/eval021.json`
- `data/rag/traces/phase5/full-agentic-replication/eval022.json`
- `data/rag/traces/phase5/full-agentic-replication/eval023.json`
- `data/rag/traces/phase5/full-agentic-replication/eval024.json`
- `data/rag/traces/phase5/full-agentic-replication/eval025.json`
- `data/rag/traces/phase5/full-agentic-replication/eval026.json`
- `data/rag/traces/phase5/full-agentic-replication/eval027.json`
- `data/rag/traces/phase5/full-agentic-replication/eval028.json`
- `data/rag/traces/phase5/full-agentic-replication/eval029.json`
- `data/rag/traces/phase5/full-agentic-replication/eval030.json`
- `data/rag/traces/phase5/full-agentic-replication/loaded_environment.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval001.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval002.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval003.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval004.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval005a.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval005b.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval006.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval007.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval008.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval009.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval010.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval011.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval012.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval013.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval014.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval015.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval016.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval017.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval018.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval019.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval020.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval021.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval022.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval023.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval024.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval025.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval026.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval027.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval028.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval029.json`
- `data/rag/traces/phase5/full-agentic-replication/observations/eval030.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval001.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval002.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval003.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval004.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval005a.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval005b.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval006.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval007.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval008.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval009.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval010.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval011.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval012.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval013.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval014.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval015.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval016.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval017.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval018.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval019.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval020.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval021.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval022.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval023.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval024.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval025.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval026.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval027.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval028.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval029.json`
- `data/rag/traces/phase5/full-agentic-replication/outputs/eval030.json`
- `data/rag/traces/phase5/full-agentic-replication/production_attempts.jsonl`
- `data/rag/traces/phase5/full-agentic-replication/production_outputs.jsonl`
- `data/rag/traces/phase5/full-agentic-replication/production_seal.json`
- `data/rag/traces/phase5/full-agentic-replication/run_binding.json`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/__init__.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/__init__.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/__init__.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/__init__.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/__init__.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/block.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/configuration_xlm_roberta.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/embedding.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mha.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mlp.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_lora.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_xlm_roberta.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/rotary.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/stochastic_depth.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/xlm_padding.py`
- `data/rag/traces/phase5/full-agentic-replication/worker.lock`
- `scripts/__pycache__/agentic_rag.cpython-312.pyc`
- `scripts/__pycache__/analyze_candidate_coverage.cpython-312.pyc`
- `scripts/__pycache__/analyze_standard_rag_failures.cpython-312.pyc`
- `scripts/__pycache__/annotate_retrieval_eval.cpython-312.pyc`
- `scripts/__pycache__/bm25_baseline.cpython-310.pyc`
- `scripts/__pycache__/bm25_baseline.cpython-312.pyc`
- `scripts/__pycache__/build_chunks.cpython-312.pyc`
- `scripts/__pycache__/build_dense_index.cpython-312.pyc`
- `scripts/__pycache__/build_generation_eval_v1.cpython-312.pyc`
- `scripts/__pycache__/check_register.cpython-312.pyc`
- `scripts/__pycache__/citation_validator.cpython-310.pyc`
- `scripts/__pycache__/citation_validator.cpython-312.pyc`
- `scripts/__pycache__/clean_docx_text.cpython-312.pyc`
- `scripts/__pycache__/create_verification_samples.cpython-312.pyc`
- `scripts/__pycache__/dense_baseline.cpython-310.pyc`
- `scripts/__pycache__/dense_baseline.cpython-312.pyc`
- `scripts/__pycache__/evaluate_agentic_rag.cpython-312.pyc`
- `scripts/__pycache__/evaluate_bm25.cpython-312.pyc`
- `scripts/__pycache__/evaluate_dense.cpython-312.pyc`
- `scripts/__pycache__/evaluate_hybrid.cpython-312.pyc`
- `scripts/__pycache__/evaluate_reranker.cpython-312.pyc`
- `scripts/__pycache__/evaluate_standard_rag.cpython-312.pyc`
- `scripts/__pycache__/evidence_formatter.cpython-310.pyc`
- `scripts/__pycache__/evidence_formatter.cpython-312.pyc`
- `scripts/__pycache__/extract_docx.cpython-312.pyc`
- `scripts/__pycache__/generate_human_review_report.cpython-312.pyc`
- `scripts/__pycache__/hash_raw_files.cpython-312.pyc`
- `scripts/__pycache__/hybrid_rrf.cpython-312.pyc`
- `scripts/__pycache__/inspect_chunk_issues.cpython-312.pyc`
- `scripts/__pycache__/llm_client.cpython-310.pyc`
- `scripts/__pycache__/llm_client.cpython-312.pyc`
- `scripts/__pycache__/parse_legal_structure.cpython-312.pyc`
- `scripts/__pycache__/rag_baseline.cpython-310.pyc`
- `scripts/__pycache__/rag_baseline.cpython-312.pyc`
- `scripts/__pycache__/reranker_baseline.cpython-310.pyc`
- `scripts/__pycache__/reranker_baseline.cpython-312.pyc`
- `scripts/__pycache__/response_formatter.cpython-310.pyc`
- `scripts/__pycache__/response_formatter.cpython-312.pyc`
- `scripts/__pycache__/retrieval_pipeline.cpython-310.pyc`
- `scripts/__pycache__/retrieval_pipeline.cpython-312.pyc`
- `scripts/__pycache__/update_source_hashes.cpython-312.pyc`
- `scripts/__pycache__/update_verification_status.cpython-312.pyc`
- `scripts/__pycache__/validate_corpus.cpython-312.pyc`
- `scripts/__pycache__/validate_generation_eval.cpython-312.pyc`
- `scripts/__pycache__/validate_retrieval_eval.cpython-312.pyc`
- `tests/__pycache__/test_agentic_evaluation.cpython-312.pyc`
- `tests/__pycache__/test_agentic_rag.cpython-312.pyc`
- `tests/__pycache__/test_generation_eval.cpython-312.pyc`
- `tests/__pycache__/test_rag_runtime.cpython-312.pyc`

## Temporary files (name heuristic)

None found.

## Caches

- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/block.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/configuration_xlm_roberta.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/embedding.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mha.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mlp.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_lora.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_xlm_roberta.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/rotary.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/stochastic_depth.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/xlm_padding.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/block.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/configuration_xlm_roberta.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/embedding.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mha.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mlp.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_lora.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_xlm_roberta.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/rotary.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/stochastic_depth.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/xlm_padding.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/__init__.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/__init__.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/__init__.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/__init__.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/__init__.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/block.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/configuration_xlm_roberta.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/embedding.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mha.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mlp.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_lora.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_xlm_roberta.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/rotary.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/stochastic_depth.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/xlm_padding.py`
- `scripts/__pycache__/agentic_rag.cpython-312.pyc`
- `scripts/__pycache__/analyze_candidate_coverage.cpython-312.pyc`
- `scripts/__pycache__/analyze_standard_rag_failures.cpython-312.pyc`
- `scripts/__pycache__/annotate_retrieval_eval.cpython-312.pyc`
- `scripts/__pycache__/bm25_baseline.cpython-310.pyc`
- `scripts/__pycache__/bm25_baseline.cpython-312.pyc`
- `scripts/__pycache__/build_chunks.cpython-312.pyc`
- `scripts/__pycache__/build_dense_index.cpython-312.pyc`
- `scripts/__pycache__/build_generation_eval_v1.cpython-312.pyc`
- `scripts/__pycache__/check_register.cpython-312.pyc`
- `scripts/__pycache__/citation_validator.cpython-310.pyc`
- `scripts/__pycache__/citation_validator.cpython-312.pyc`
- `scripts/__pycache__/clean_docx_text.cpython-312.pyc`
- `scripts/__pycache__/create_verification_samples.cpython-312.pyc`
- `scripts/__pycache__/dense_baseline.cpython-310.pyc`
- `scripts/__pycache__/dense_baseline.cpython-312.pyc`
- `scripts/__pycache__/evaluate_agentic_rag.cpython-312.pyc`
- `scripts/__pycache__/evaluate_bm25.cpython-312.pyc`
- `scripts/__pycache__/evaluate_dense.cpython-312.pyc`
- `scripts/__pycache__/evaluate_hybrid.cpython-312.pyc`
- `scripts/__pycache__/evaluate_reranker.cpython-312.pyc`
- `scripts/__pycache__/evaluate_standard_rag.cpython-312.pyc`
- `scripts/__pycache__/evidence_formatter.cpython-310.pyc`
- `scripts/__pycache__/evidence_formatter.cpython-312.pyc`
- `scripts/__pycache__/extract_docx.cpython-312.pyc`
- `scripts/__pycache__/generate_human_review_report.cpython-312.pyc`
- `scripts/__pycache__/hash_raw_files.cpython-312.pyc`
- `scripts/__pycache__/hybrid_rrf.cpython-312.pyc`
- `scripts/__pycache__/inspect_chunk_issues.cpython-312.pyc`
- `scripts/__pycache__/llm_client.cpython-310.pyc`
- `scripts/__pycache__/llm_client.cpython-312.pyc`
- `scripts/__pycache__/parse_legal_structure.cpython-312.pyc`
- `scripts/__pycache__/rag_baseline.cpython-310.pyc`
- `scripts/__pycache__/rag_baseline.cpython-312.pyc`
- `scripts/__pycache__/reranker_baseline.cpython-310.pyc`
- `scripts/__pycache__/reranker_baseline.cpython-312.pyc`
- `scripts/__pycache__/response_formatter.cpython-310.pyc`
- `scripts/__pycache__/response_formatter.cpython-312.pyc`
- `scripts/__pycache__/retrieval_pipeline.cpython-310.pyc`
- `scripts/__pycache__/retrieval_pipeline.cpython-312.pyc`
- `scripts/__pycache__/update_source_hashes.cpython-312.pyc`
- `scripts/__pycache__/update_verification_status.cpython-312.pyc`
- `scripts/__pycache__/validate_corpus.cpython-312.pyc`
- `scripts/__pycache__/validate_generation_eval.cpython-312.pyc`
- `scripts/__pycache__/validate_retrieval_eval.cpython-312.pyc`
- `tests/__pycache__/test_agentic_evaluation.cpython-312.pyc`
- `tests/__pycache__/test_agentic_rag.cpython-312.pyc`
- `tests/__pycache__/test_generation_eval.cpython-312.pyc`
- `tests/__pycache__/test_rag_runtime.cpython-312.pyc`

## Notebooks

None found.

## Archives

None found.

## Complete existing-file inventory

Every path, size and SHA-256 is also available as a node in dependency_map_v0.json.

| Path | Bytes |
| --- | --- |
| .env | 215 |
| .env.example | 282 |
| .vscode/settings.json | 132 |
| README.md | 2893 |
| data/evaluation/backups/retrieval_eval.20260814-145701.jsonl | 10575 |
| data/evaluation/backups/retrieval_eval.20260814-151851.jsonl | 21377 |
| data/evaluation/backups/retrieval_eval.20260814-153333.jsonl | 21231 |
| data/evaluation/dev_queries.jsonl | 1505 |
| data/evaluation/generation/ANNOTATION_WORKFLOW.md | 1382 |
| data/evaluation/generation/agentic_rag_eval_v1_agentic-v1.jsonl | 2090257 |
| data/evaluation/generation/agentic_rag_metrics_v1_agentic-v1.json | 3021 |
| data/evaluation/generation/agentic_trace_analysis_metrics_v0.json | 151338 |
| data/evaluation/generation/agentic_trace_analysis_v0.jsonl | 393703 |
| data/evaluation/generation/backups/generation_eval_v1.20260902-145534.json | 60852 |
| data/evaluation/generation/failure_analysis_metrics_v0.json | 4045 |
| data/evaluation/generation/failure_analysis_points_v0.jsonl | 231690 |
| data/evaluation/generation/failure_analysis_queries_v0.json | 109386 |
| data/evaluation/generation/generation_annotation_audit_v1.md | 8516 |
| data/evaluation/generation/generation_annotation_v1_report.md | 4721 |
| data/evaluation/generation/generation_annotation_v1_review.md | 81507 |
| data/evaluation/generation/generation_eval_v0.json | 31909 |
| data/evaluation/generation/generation_eval_v0.schema.json | 1826 |
| data/evaluation/generation/generation_eval_v0_manifest.json | 738 |
| data/evaluation/generation/generation_eval_v1.json | 60852 |
| data/evaluation/generation/generation_eval_v1.schema.json | 1811 |
| data/evaluation/generation/generation_eval_v1_manifest.json | 996 |
| data/evaluation/generation/generation_eval_v1_verified.json | 60948 |
| data/evaluation/generation/generation_eval_v1_verified_manifest.json | 821 |
| data/evaluation/generation/partials/standard_rag_eval_v0_partial.20260902-151753.jsonl | 135785 |
| data/evaluation/generation/partials/standard_rag_eval_v0_partial.20260902-155801.jsonl | 146994 |
| data/evaluation/generation/phase5/agentic-v1-no-answer-revision/evaluation.jsonl | 23335 |
| data/evaluation/generation/phase5/agentic-v1-no-answer-revision/evaluation_attempts.jsonl | 0 |
| data/evaluation/generation/phase5/agentic-v1-no-answer-revision/metrics.json | 10768 |
| data/evaluation/generation/phase5/agentic-v1-no-answer-revision/run_manifest.json | 32371 |
| data/evaluation/generation/phase5/agentic-v1-no-answer-revision/variant_manifest.json | 4412 |
| data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion/evaluation.jsonl | 23428 |
| data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion/evaluation_attempts.jsonl | 0 |
| data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion/metrics.json | 10246 |
| data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion/run_manifest.json | 31855 |
| data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion/variant_manifest.json | 4415 |
| data/evaluation/generation/phase5/contrast_R2_A1.json | 11548 |
| data/evaluation/generation/phase5/contrast_R2_A2.json | 11548 |
| data/evaluation/generation/phase5/execution_environment_v0.json | 494277 |
| data/evaluation/generation/phase5/execution_tools/launch_frozen_v0.py | 3111 |
| data/evaluation/generation/phase5/execution_tools/report_incomplete_v0.py | 17756 |
| data/evaluation/generation/phase5/full-agentic-replication/evaluation.jsonl | 23180 |
| data/evaluation/generation/phase5/full-agentic-replication/evaluation_attempts.jsonl | 0 |
| data/evaluation/generation/phase5/full-agentic-replication/metrics.json | 10776 |
| data/evaluation/generation/phase5/full-agentic-replication/run_manifest.json | 32369 |
| data/evaluation/generation/phase5/full-agentic-replication/variant_manifest.json | 4406 |
| data/evaluation/generation/phase5/integrity_before_after_v0.json | 64789 |
| data/evaluation/generation/phase5/phase5a_ablation_manifest_v0.json | 102610 |
| data/evaluation/generation/phase5/phase5a_ablation_spec_v0.md | 36472 |
| data/evaluation/generation/phase5/phase5b1_preflight_manifest_v0.json | 423743 |
| data/evaluation/generation/phase5/phase5b1_preflight_report_v0.md | 12846 |
| data/evaluation/generation/phase5/phase5b2_preflight_rerun_v0.json | 415740 |
| data/evaluation/generation/phase5/phase5b2_preflight_tests_v0.json | 4565 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval001/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval001/1/response.json | 962 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval002/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval002/1/response.json | 938 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval003/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval003/1/response.json | 667 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval004/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval004/1/response.json | 2105 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval005a/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval005a/1/response.json | 1290 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval005b/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval005b/1/response.json | 1558 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval006/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval006/1/response.json | 1620 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval007/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval007/1/response.json | 2150 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval008/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval008/1/response.json | 1503 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval009/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval009/1/response.json | 704 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval010/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval010/1/response.json | 928 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval011/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval011/1/response.json | 912 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval012/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval012/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval012/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval012/2/response.json | 1377 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval013/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval013/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval013/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval013/2/response.json | 1740 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval015/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval015/1/response.json | 969 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval017/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval017/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval017/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval017/2/response.json | 1262 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval018/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval018/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval018/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval018/2/response.json | 1580 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/3/response.json | 1227 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval027/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval027/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval027/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval027/2/response.json | 1736 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval028/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval028/1/response.json | 1674 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval029/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval029/1/response.json | 925 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval030/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval030/1/response.json | 1553 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/evaluation.jsonl | 2322829 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/evaluation_attempts.jsonl | 36974 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/metrics.json | 45293 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval001.json | 117703 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval002.json | 47627 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval003.json | 44333 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval004.json | 53660 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval005a.json | 128192 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval005b.json | 126226 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval006.json | 122839 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval007.json | 51284 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval008.json | 54881 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval009.json | 47818 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval010.json | 49474 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval011.json | 118779 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval012.json | 55440 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval013.json | 107755 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval014.json | 117700 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval015.json | 55566 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval016.json | 117760 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval017.json | 56665 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval018.json | 52856 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval019.json | 47916 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval020.json | 41844 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval021.json | 50090 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval022.json | 119374 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval023.json | 122559 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval024.json | 45049 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval025.json | 47229 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval026.json | 121315 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval027.json | 48586 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval028.json | 53430 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval029.json | 50477 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval030.json | 48371 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval001/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval001/1/response.json | 959 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval002/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval002/1/response.json | 938 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval003/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval003/1/response.json | 647 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval004/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval004/1/response.json | 2126 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval005a/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval005a/1/response.json | 2299 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval005b/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval005b/1/response.json | 2094 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval006/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval006/1/response.json | 1343 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval007/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval007/1/response.json | 2167 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval008/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval008/1/response.json | 1395 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval009/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval009/1/response.json | 691 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval010/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval010/1/response.json | 1013 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval011/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval011/1/response.json | 976 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval012/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval012/1/response.json | 1588 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval013/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval013/1/response.json | 1798 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval014/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval014/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval014/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval014/2/response.json | 1262 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval021/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval021/1/response.json | 1242 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval028/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval028/1/response.json | 1643 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval029/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval029/1/response.json | 1134 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval030/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval030/1/response.json | 1531 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/evaluation.jsonl | 1553306 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/evaluation_attempts.jsonl | 38360 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/metrics.json | 49225 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval001.json | 48152 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval002.json | 47625 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval003.json | 44187 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval004.json | 56317 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval005a.json | 54367 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval005b.json | 46566 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval006.json | 49991 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval007.json | 51441 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval008.json | 54431 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval009.json | 48053 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval010.json | 51202 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval011.json | 48395 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval012.json | 55335 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval013.json | 47567 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval014.json | 47919 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval015.json | 55273 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval016.json | 50056 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval017.json | 56261 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval018.json | 51998 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval019.json | 47874 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval020.json | 41862 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval021.json | 50531 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval022.json | 48438 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval023.json | 55623 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval024.json | 45156 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval025.json | 47243 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval026.json | 46426 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval027.json | 49224 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval028.json | 53353 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval029.json | 54034 |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval030.json | 48375 |
| data/evaluation/generation/phase5/phase5b2e_v0/analysis_validation.json | 2183 |
| data/evaluation/generation/phase5/phase5b2e_v0/analyze_frozen.py | 28074 |
| data/evaluation/generation/phase5/phase5b2e_v0/console_output.txt | 3862 |
| data/evaluation/generation/phase5/phase5b2e_v0/contrast_R2_A1.json | 111104 |
| data/evaluation/generation/phase5/phase5b2e_v0/contrast_R2_A2.json | 116043 |
| data/evaluation/generation/phase5/phase5b2e_v0/evaluate_frozen.py | 11241 |
| data/evaluation/generation/phase5/phase5b2e_v0/evaluation_protocol.json | 2464 |
| data/evaluation/generation/phase5/phase5b2e_v0/evaluation_protocol_initial.json | 2119 |
| data/evaluation/generation/phase5/phase5b2e_v0/evaluator.lock | 0 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval001/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval001/1/response.json | 1007 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval002/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval002/1/response.json | 907 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval003/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval003/1/response.json | 650 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval004/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval004/1/response.json | 1701 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval005a/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval005a/1/response.json | 2100 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval005b/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval005b/1/response.json | 2113 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval006/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval006/1/response.json | 1434 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval007/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval007/1/response.json | 2158 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval008/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval008/1/response.json | 1350 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval009/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval009/1/response.json | 710 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval010/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval010/1/response.json | 932 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval011/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval011/1/response.json | 1015 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval012/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval012/1/response.json | 1557 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval013/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval013/1/response.json | 1754 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval014/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval014/1/response.json | 1620 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval015/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval015/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval015/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval015/2/response.json | 922 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval016/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval016/1/response.json | 1093 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval017/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval017/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval017/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval017/2/response.json | 1363 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/3/response.json | 1556 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/3/response.json | 1246 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval020/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval020/1/response.json | 745 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/1/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/2/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/2/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/3/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/3/response.json | 40 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval029/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval029/1/response.json | 1153 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval030/1/request.json | 101 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval030/1/response.json | 1531 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/evaluation.jsonl | 2273796 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/evaluation_attempts.jsonl | 33981 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/metrics.json | 41321 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval001.json | 129308 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval002.json | 47582 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval003.json | 44424 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval004.json | 56306 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval005a.json | 175773 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval005b.json | 127045 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval006.json | 125559 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval007.json | 51665 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval008.json | 55152 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval009.json | 47830 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval010.json | 50902 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval011.json | 114212 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval012.json | 56197 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval013.json | 101128 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval014.json | 119604 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval015.json | 55339 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval016.json | 116540 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval017.json | 57150 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval018.json | 52712 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval019.json | 48282 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval020.json | 41825 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval021.json | 49841 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval022.json | 49075 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval023.json | 159163 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval024.json | 44889 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval025.json | 47305 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval026.json | 45640 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval027.json | 49272 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval028.json | 52784 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval029.json | 52728 |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval030.json | 48533 |
| data/evaluation/generation/phase5/phase5b2e_v0/integrity_after.json | 205118 |
| data/evaluation/generation/phase5/phase5b2e_v0/integrity_before.json | 116871 |
| data/evaluation/generation/phase5/phase5b2e_v0/provenance.json | 130002 |
| data/evaluation/generation/phase5/phase5b2e_v0/recovery_gate.json | 5190 |
| data/evaluation/generation/phase5/phase5b2e_v0/render_report.py | 16973 |
| data/evaluation/generation/phase5/phase5b2e_v0/replication_R1_R2.json | 64830 |
| data/evaluation/generation/phase5/phase5b2e_v0/reporting_correction_validation.json | 988 |
| data/evaluation/generation/phase5/phase5b2e_v0/validate_analysis.py | 6505 |
| data/evaluation/generation/phase5/phase5b2er1_console_v0.txt | 977 |
| data/evaluation/generation/phase5/phase5b2er1_integrity_v0.json | 322900 |
| data/evaluation/generation/phase5/phase5b2er1_quota_recovery_manifest_v0.json | 537478 |
| data/evaluation/generation/phase5/phase5b2er1_quota_recovery_spec_v0.md | 17323 |
| data/evaluation/generation/phase5/phase5b2er1_quota_recovery_tests_v0.json | 508 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval014/1/evaluation_record.json | 118223 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval014/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval014/1/started.json | 537 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval014/1/wire_response.json | 1902 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval016/1/evaluation_record.json | 118188 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval016/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval016/1/started.json | 537 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval016/1/wire_response.json | 1787 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval019/1/evaluation_record.json | 48094 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval019/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval019/1/started.json | 537 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval019/1/wire_response.json | 1481 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval020/1/evaluation_record.json | 41534 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval020/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval020/1/started.json | 537 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval020/1/wire_response.json | 855 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval022/1/evaluation_record.json | 119388 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval022/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval022/1/started.json | 537 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval022/1/wire_response.json | 1285 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval023/1/evaluation_record.json | 122706 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval023/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval023/1/started.json | 537 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval023/1/wire_response.json | 1186 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/1/receipt.json | 1931 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/1/started.json | 537 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/1/wire_response.json | 1740 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/2/evaluation_record.json | 44825 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/2/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/2/started.json | 537 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/2/wire_response.json | 927 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval025/1/evaluation_record.json | 47697 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval025/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval025/1/started.json | 537 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval025/1/wire_response.json | 1478 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval026/1/evaluation_record.json | 121647 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval026/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval026/1/started.json | 537 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval026/1/wire_response.json | 1699 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval015/1/evaluation_record.json | 55456 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval015/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval015/1/started.json | 540 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval015/1/wire_response.json | 1410 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval016/1/evaluation_record.json | 50436 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval016/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval016/1/started.json | 540 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval016/1/wire_response.json | 1739 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval017/1/evaluation_record.json | 56611 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval017/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval017/1/started.json | 540 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval017/1/wire_response.json | 1653 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval018/1/evaluation_record.json | 52408 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval018/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval018/1/started.json | 540 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval018/1/wire_response.json | 1777 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval019/1/evaluation_record.json | 47971 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval019/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval019/1/started.json | 540 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval019/1/wire_response.json | 1400 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval020/1/evaluation_record.json | 41720 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval020/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval020/1/started.json | 540 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval020/1/wire_response.json | 1023 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval022/1/evaluation_record.json | 48671 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval022/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval022/1/started.json | 540 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval022/1/wire_response.json | 1496 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval023/1/evaluation_record.json | 55751 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval023/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval023/1/started.json | 540 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval023/1/wire_response.json | 1345 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval024/1/evaluation_record.json | 44935 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval024/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval024/1/started.json | 540 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval024/1/wire_response.json | 931 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval025/1/evaluation_record.json | 47604 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval025/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval025/1/started.json | 540 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval025/1/wire_response.json | 1624 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval026/1/evaluation_record.json | 46831 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval026/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval026/1/started.json | 540 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval026/1/wire_response.json | 1784 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval027/1/evaluation_record.json | 49782 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval027/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval027/1/started.json | 540 |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval027/1/wire_response.json | 1961 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval021/1/evaluation_record.json | 50024 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval021/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval021/1/started.json | 532 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval021/1/wire_response.json | 1486 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval022/1/evaluation_record.json | 49163 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval022/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval022/1/started.json | 532 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval022/1/wire_response.json | 1359 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval023/1/evaluation_record.json | 159225 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval023/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval023/1/started.json | 532 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval023/1/wire_response.json | 1279 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval024/1/evaluation_record.json | 44644 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval024/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval024/1/started.json | 532 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval024/1/wire_response.json | 785 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval025/1/evaluation_record.json | 47766 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval025/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval025/1/started.json | 532 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval025/1/wire_response.json | 1724 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval026/1/evaluation_record.json | 45966 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval026/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval026/1/started.json | 532 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval026/1/wire_response.json | 1693 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval027/1/evaluation_record.json | 49716 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval027/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval027/1/started.json | 532 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval027/1/wire_response.json | 1871 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval028/1/evaluation_record.json | 53359 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval028/1/receipt.json | 593 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval028/1/started.json | 532 |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval028/1/wire_response.json | 1942 |
| data/evaluation/generation/phase5/phase5b2er2_v1/execution_driver_session_0001.py | 10131 |
| data/evaluation/generation/phase5/phase5b2er2_v1/execution_driver_session_0002.py | 14061 |
| data/evaluation/generation/phase5/phase5b2er2_v1/phase5b2er2_session_0001_report.json | 10544 |
| data/evaluation/generation/phase5/phase5b2er2_v1/phase5b2er2_session_0002_report.json | 7429 |
| data/evaluation/generation/phase5/phase5b2er2_v1/protocol_binding.json | 226 |
| data/evaluation/generation/phase5/phase5b2er2_v1/quota_stop_0001.json | 292 |
| data/evaluation/generation/phase5/phase5b2er2_v1/quota_stop_0001_resume_authorization.json | 308 |
| data/evaluation/generation/phase5/phase5b2er2_v1/session.lock | 0 |
| data/evaluation/generation/phase5/phase5b2er2_v1/session_0001_binding.json | 4462510 |
| data/evaluation/generation/phase5/phase5b2er2_v1/session_0001_integrity.json | 589 |
| data/evaluation/generation/phase5/phase5b2er2_v1/session_0002_binding.json | 4164790 |
| data/evaluation/generation/phase5/phase5b2er2_v1/session_0002_integrity.json | 9724 |
| data/evaluation/generation/phase5/phase5b2f_v0/agentic-v1-no-answer-revision/evaluation_complete.jsonl | 2408101 |
| data/evaluation/generation/phase5/phase5b2f_v0/agentic-v1-no-answer-revision/metrics.json | 1542 |
| data/evaluation/generation/phase5/phase5b2f_v0/agentic-v1-no-evidence-expansion/evaluation_complete.jsonl | 1614201 |
| data/evaluation/generation/phase5/phase5b2f_v0/agentic-v1-no-evidence-expansion/metrics.json | 1544 |
| data/evaluation/generation/phase5/phase5b2f_v0/analysis_tools/offline_analysis_v0.py | 54165 |
| data/evaluation/generation/phase5/phase5b2f_v0/analysis_tools/phase5b2f_gate.py | 4990 |
| data/evaluation/generation/phase5/phase5b2f_v0/analysis_tools/verify_final_analysis_v0.py | 15681 |
| data/evaluation/generation/phase5/phase5b2f_v0/bootstrap_R2_A1.json | 1167 |
| data/evaluation/generation/phase5/phase5b2f_v0/bootstrap_R2_A2.json | 1167 |
| data/evaluation/generation/phase5/phase5b2f_v0/canonical_judgments_manifest.json | 119636 |
| data/evaluation/generation/phase5/phase5b2f_v0/contrast_R2_A1.json | 124363 |
| data/evaluation/generation/phase5/phase5b2f_v0/contrast_R2_A2.json | 125557 |
| data/evaluation/generation/phase5/phase5b2f_v0/efficiency_v0.json | 5428 |
| data/evaluation/generation/phase5/phase5b2f_v0/final_artifact_hashes_v0.json | 3083 |
| data/evaluation/generation/phase5/phase5b2f_v0/full-agentic-replication/evaluation_complete.jsonl | 2358173 |
| data/evaluation/generation/phase5/phase5b2f_v0/full-agentic-replication/metrics.json | 1545 |
| data/evaluation/generation/phase5/phase5b2f_v0/integrity_before_after_v0.json | 11601 |
| data/evaluation/generation/phase5/phase5b2f_v0/integrity_before_inventory_v0.json | 229666 |
| data/evaluation/generation/phase5/phase5b2f_v0/phase5b2f_console_v0.txt | 4521 |
| data/evaluation/generation/phase5/phase5b2f_v0/phase5b2f_final_report_v0.md | 40137 |
| data/evaluation/generation/phase5/phase5b2f_v0/phase5b2f_metrics_v0.json | 352761 |
| data/evaluation/generation/phase5/phase5b2f_v0/point_transitions_R1_R2.jsonl | 12205 |
| data/evaluation/generation/phase5/phase5b2f_v0/point_transitions_R2_A1.jsonl | 12220 |
| data/evaluation/generation/phase5/phase5b2f_v0/point_transitions_R2_A2.jsonl | 12187 |
| data/evaluation/generation/phase5/phase5b2f_v0/provenance_v0.json | 5090 |
| data/evaluation/generation/phase5/phase5b2f_v0/recovery_completion_gate_v0.json | 36268 |
| data/evaluation/generation/phase5/phase5b2f_v0/replication_R1_R2.json | 50724 |
| data/evaluation/generation/phase5/phase5b2f_v0/validation_v0.json | 2028 |
| data/evaluation/generation/phase5/phase5b2r_negative_tests_v1.json | 2206 |
| data/evaluation/generation/phase5/phase5b2r_recovery_manifest_v0.json | 6343 |
| data/evaluation/generation/phase5/phase5b2r_recovery_protocol_v1.json | 167567 |
| data/evaluation/generation/phase5/phase5b2r_recovery_report_v0.md | 3629 |
| data/evaluation/generation/phase5/phase5b_evaluation_metrics_v0.json | 615292 |
| data/evaluation/generation/phase5/phase5b_evaluation_report_v0.md | 23746 |
| data/evaluation/generation/phase5/phase5b_report_v0.md | 6625 |
| data/evaluation/generation/phase5/phase5c1_v0/consolidate_research_v0.py | 64524 |
| data/evaluation/generation/phase5/phase5c1_v0/final_artifact_hashes_v0.json | 1393 |
| data/evaluation/generation/phase5/phase5c1_v0/integrity_before_after_v0.json | 5678128 |
| data/evaluation/generation/phase5/phase5c1_v0/integrity_before_inventory_v0.json | 5676401 |
| data/evaluation/generation/phase5/phase5c1_v0/phase5c1_console_v0.txt | 2763 |
| data/evaluation/generation/phase5/phase5c1_v0/phase5c1_decision_log_v0.md | 2473 |
| data/evaluation/generation/phase5/phase5c1_v0/phase5c1_evidence_matrix_v0.json | 115575 |
| data/evaluation/generation/phase5/phase5c1_v0/phase5c1_exploratory_diagnostic_v0.json | 8364 |
| data/evaluation/generation/phase5/phase5c1_v0/phase5c1_manifest_v0.json | 100732 |
| data/evaluation/generation/phase5/phase5c1_v0/phase5c1_problem_requirement_map_v0.json | 9465 |
| data/evaluation/generation/phase5/phase5c1_v0/phase5c1_research_synthesis_v0.md | 37972 |
| data/evaluation/generation/phase5/phase5c1_v0/phase5c1_validation_v0.json | 34343 |
| data/evaluation/generation/phase5/phase5c2_v0/final_artifact_hashes_v0.json | 1993 |
| data/evaluation/generation/phase5/phase5c2_v0/integrity_baseline_v0.json | 5679004 |
| data/evaluation/generation/phase5/phase5c2_v0/integrity_before_after_v0.json | 5680820 |
| data/evaluation/generation/phase5/phase5c2_v0/phase5c2_challenge_set_design_v0.md | 22031 |
| data/evaluation/generation/phase5/phase5c2_v0/phase5c2_console_v0.txt | 1145 |
| data/evaluation/generation/phase5/phase5c2_v0/phase5c2_decision_log_v0.md | 7567 |
| data/evaluation/generation/phase5/phase5c2_v0/phase5c2_evaluation_protocol_draft_v0.md | 31374 |
| data/evaluation/generation/phase5/phase5c2_v0/phase5c2_manifest_v0.json | 11390 |
| data/evaluation/generation/phase5/phase5c2_v0/phase5c2_requirement_validation_matrix_v0.json | 18680 |
| data/evaluation/generation/phase5/phase5c2_v0/phase5c2_trace_schema_design_v0.json | 23233 |
| data/evaluation/generation/phase5/phase5c2_v0/phase5c2_v2_requirements_design_v0.md | 25618 |
| data/evaluation/generation/phase5/phase5c2_v0/phase5c2_validation_v0.json | 10625 |
| data/evaluation/generation/phase5/phase5c3_v0/final_artifact_hashes_v0.json | 2439 |
| data/evaluation/generation/phase5/phase5c3_v0/integrity_baseline_v0.json | 7001012 |
| data/evaluation/generation/phase5/phase5c3_v0/integrity_before_after_v0.json | 7003460 |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_console_v0.txt | 1207 |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_controller_status_decision_table_v0.json | 40118 |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_decision_table_validation_v0.json | 2029 |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_design_amendments_v0.md | 7772 |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_external_review_v0.md | 7433 |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_freeze_manifest_v0.json | 14937 |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_frozen_design_spec_v0.md | 14277 |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_margin_governance_v0.md | 4559 |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_quota_scheduler_requirements_v0.md | 6529 |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_spec_bindings_v0.json | 5362 |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_trace_matrix_amendment_v0.json | 8110 |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_validation_v0.json | 17218 |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/adjudication_corpus_audit_v0.json | 859 |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/adjudication_issue_resolutions_v0.jsonl | 0 |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/candidate_admission_decisions_v0.jsonl | 0 |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/final_adjudicated_annotations_v0.jsonl | 0 |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/final_retained_36_v0.json | 605 |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/final_split_assignment_v0.json | 660 |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/input_contamination_incident_v0.json | 1868 |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/integrity_before_after_v0.json | 56438 |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/phase5c4d_adjudication_report_v0.md | 1683 |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/phase5c4d_console_v0.txt | 1086 |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/phase5c4d_dimension_summary_v0.json | 1709 |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/phase5c4d_selection_summary_v0.json | 1155 |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/phase5c4d_validation_v0.json | 1365 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_applicability_sufficiency_comparison_v0.jsonl | 1098437 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_aspect_mapping_v0.jsonl | 156564 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_candidate_alignment_v0.json | 53824 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_contamination_comparison_v0.jsonl | 78564 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_corpus_audit_comparison_v0.jsonl | 14991 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_disagreement_registry_v0.jsonl | 435691 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_scope_comparison_v0.jsonl | 208444 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_support_comparison_v0.jsonl | 254283 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/artifact_hashes_v0.json | 4298 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/build_comparison_v0.py | 54392 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/comparison_access_manifest_v0.json | 1666 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/comparison_check_results_v0.json | 136863 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/final_artifact_hashes_v0.json | 5107 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/integrity_baseline_v0.json | 6812359 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/integrity_before_after_v0.json | 2260 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/phase5c4c1_agreement_metrics_v0.json | 15405 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/phase5c4c1_comparison_report_v0.md | 3878 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/phase5c4c1_console_v0.txt | 1032 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/phase5c4c1_disagreement_summary_v0.json | 14049 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/phase5c4c1_validation_v0.json | 3045 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/semantic_mapping_decisions_v0.py | 9123 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/source_integrity_validation_v0.json | 45598 |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/validate_comparison_v0.py | 12019 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/annotation_A_v0.jsonl | 1674286 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/authored_tasks_v0.py | 92589 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/build_construction_v0.py | 76100 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/challenge_candidates_v0.jsonl | 324819 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/cluster_rationales_v0.json | 22664 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/construction_notes_v0.json | 15682 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/contaminated_packet_quarantine_v0.json | 4840 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/contamination_screening_details_v0.json | 1429829 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/corpus_absence_audits_v0.jsonl | 830798 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/corpus_mapping_v0.json | 818557 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/custodian_manifest_v0.json | 5229 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/exclusion_log_v0.jsonl | 1315 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/explicit_asks_v0.json | 7447 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/exposure_events_v0.jsonl | 4206 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/artifact_hashes_v0.json | 3591 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/execution_and_access_v0.json | 3171 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/fresh_reviewer_b_handoff_v1.md | 1962 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/integrity_baseline_v0.json | 6794954 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/integrity_before_after_v0.json | 6797295 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/phase5c4b0_console_v0.txt | 875 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/phase5c4b0_review_summary_v0.md | 1904 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/phase5c4b0_validation_v0.json | 2799 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/sanitize_reviewer_b_v1.py | 41023 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b1_reference_preparation_v0/medical_reference_projection_audit_v1.json | 5402 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b1_reference_preparation_v0/phase5c4b1_console_v0.txt | 560 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b1_reference_preparation_v0/prepare_medical_reference_v1.py | 11662 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/reviewer_b_comparison_after_independent_v0.jsonl | 1627134 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/reviewer_b_id_mapping_v1.json | 32032 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/reviewer_b_packet_projection_audit_v1.json | 34338 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/reviewer_b_shuffle_provenance_v1.json | 1518 |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/split_assignment_provisional_v0.json | 23623 |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/artifact_hashes_v0.json | 2443 |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/finalize_amendment_v0.py | 19203 |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/integrity_baseline_v0.json | 6818373 |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/integrity_before_after_v0.json | 2048 |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_adjudicator_c_protocol_v0.md | 8267 |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_amendment_console_v0.txt | 586 |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_amendment_manifest_v0.json | 18028 |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_amendment_validation_v0.json | 4399 |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_research_claim_boundaries_v0.md | 4562 |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_resource_constrained_amendment_v0.md | 7202 |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_selection_rules_v0.json | 7449 |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/artifact_hashes_v0.json | 6847 |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/frozen_source_checks_v0.json | 12240 |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/integrity_baseline_v0.json | 5684392 |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/integrity_before_after_v0.json | 11368926 |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_access_manifest_v0.json | 11216 |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_aggregate_composition_v0.json | 3215 |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_candidate_summary_v0.csv | 11918 |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_cluster_summary_v0.json | 23782 |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_console_v0.txt | 1309 |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_construction_report_v0.md | 4769 |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_contamination_report_v0.md | 1377 |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_dimension_matrix_v0.json | 4841 |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_validation_v0.json | 7737 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b/01_independent_review_units_v0.jsonl | 140624 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b/README_independent_review_v0.md | 2172 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b/complete_corpus_evidence_v0.json | 2941002 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b/contamination_query_only_sources_v0.json | 7294 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_packet_v1/contamination_reference_medical_v1.json | 132 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_packet_v1/reviewer_b_annotation_instructions_v1.md | 3243 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_packet_v1/reviewer_b_packet_manifest_v1.json | 762 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_packet_v1/reviewer_b_queries_v1.jsonl | 21319 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/annotation_B_v0.jsonl | 0 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/integrity_baseline_v0.json | 5691596 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/integrity_before_after_v0.json | 5692496 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/phase5c4b_access_manifest_v0.json | 2781 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/phase5c4b_agreement_ready_summary_v0.json | 573 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/phase5c4b_console_v0.txt | 953 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/phase5c4b_review_summary_v0.md | 2579 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/phase5c4b_validation_v0.json | 15675 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/reviewer_b_contamination_flags_v0.jsonl | 1057 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/reviewer_b_corpus_audit_v0.json | 406 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/reviewer_b_manifest_v0.json | 4754 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/annotation_B_pre_anchor_correction_v1.jsonl | 1605846 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/annotation_B_substantive_locked_v1.jsonl | 1561924 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/annotation_B_v1.jsonl | 1565704 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/annotation_structural_validation_v1.json | 1385 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/authored_specs_v1.py | 81113 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/build_b_annotations_v1.py | 15313 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/complete_medical_screen_v1.py | 31138 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/evidence_anchor_corrections_v1.json | 4050 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/finalize_b_v1.py | 23118 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/frozen_design_binding_checks_v1.json | 1644 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/generated_artifact_hashes_v1.json | 10250 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/historical_31_query_text_v1.json | 5540 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/integrity_baseline_v1.json | 5697440 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/integrity_before_after_v1.json | 5697560 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/medical_screen_completion_validation_v1.json | 857 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/medical_screen_integrity_baseline_v1.json | 5698439 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/medical_screen_integrity_before_after_v1.json | 3520 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/medical_screen_pre_read_seal_audit_v1.json | 2567 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/medical_screening_completed_v1.json | 5388 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/packet_schema_validation_v1.json | 538 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/phase5c4b_access_manifest_v1.json | 8360 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/phase5c4b_agreement_ready_summary_v1.json | 3316 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/phase5c4b_console_v1.txt | 468 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/phase5c4b_review_summary_v1.md | 3040 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/phase5c4b_validation_v1.json | 4177 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_generated_artifact_hashes_v1.json | 6749 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_phase5c4b_access_manifest_v1.json | 7161 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_phase5c4b_agreement_ready_summary_v1.json | 2646 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_phase5c4b_console_v1.txt | 1226 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_phase5c4b_review_summary_v1.md | 3542 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_phase5c4b_validation_v1.json | 3673 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_reviewer_b_contamination_flags_v1.jsonl | 68171 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_reviewer_b_manifest_v1.json | 6560 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/preexisting_inventory_paths_v1.json | 2471921 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/refine_bundle_anchors_v1.py | 6179 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/resume_audit_v1.json | 3708 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/reviewer_b_contamination_flags_v1.jsonl | 146134 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/reviewer_b_corpus_audit_v1.json | 150941 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/reviewer_b_manifest_v1.json | 6986 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/reviewer_b_medical_contamination_screen_v1.jsonl | 69023 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/scoped_corpus_reviews_v1.json | 141257 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/screen_text_v1.py | 13844 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/substantive_lock_v1.json | 252 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/text_screen_provenance_v1.json | 992 |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/validate_b_v1.py | 7555 |
| data/evaluation/generation/phase5/production_seal_validation_v0.json | 121749 |
| data/evaluation/generation/phase5/query_inputs_v0.json | 4548 |
| data/evaluation/generation/phase5/replication_R1_R2.json | 11548 |
| data/evaluation/generation/phase5/report_artifact_hashes_v0.json | 3536 |
| data/evaluation/generation/phase5/report_validation_v0.json | 406 |
| data/evaluation/generation/reports/agentic_rag_eval_v1_agentic-v1.md | 1205 |
| data/evaluation/generation/reports/agentic_trace_analysis_v0.md | 98803 |
| data/evaluation/generation/reports/standard_rag_eval_v0.md | 5864 |
| data/evaluation/generation/reports/standard_rag_failure_analysis_v0.md | 19556 |
| data/evaluation/generation/standard_rag_eval_v0.jsonl | 359858 |
| data/evaluation/generation/standard_rag_manifest_v0.json | 3354 |
| data/evaluation/generation/standard_rag_metrics_v0.json | 21866 |
| data/evaluation/human_review_report.md | 87988 |
| data/evaluation/human_review_summary.csv | 2933 |
| data/evaluation/results/bge-reranker-v2-m3-v0_by_difficulty.csv | 568 |
| data/evaluation/results/bge-reranker-v2-m3-v0_by_query_type.csv | 2473 |
| data/evaluation/results/bge-reranker-v2-m3-v0_failures.md | 8887 |
| data/evaluation/results/bge-reranker-v2-m3-v0_metrics.json | 1083 |
| data/evaluation/results/bge-reranker-v2-m3-v0_per_query.csv | 9835 |
| data/evaluation/results/bm25-simple-v0_by_difficulty.csv | 568 |
| data/evaluation/results/bm25-simple-v0_by_query_type.csv | 2473 |
| data/evaluation/results/bm25-simple-v0_failures.md | 37714 |
| data/evaluation/results/bm25-simple-v0_metrics.json | 509 |
| data/evaluation/results/bm25-simple-v0_per_query.csv | 9136 |
| data/evaluation/results/bm25-vs-dense-comparison.md | 1183 |
| data/evaluation/results/candidate-union-v0_metrics.json | 5414 |
| data/evaluation/results/candidate-union-v0_missing_gold.csv | 4674 |
| data/evaluation/results/candidate-union-v0_per_query.csv | 7293 |
| data/evaluation/results/candidate-union-v0_report.md | 3655 |
| data/evaluation/results/dense-jina-v3-v0_by_difficulty.csv | 568 |
| data/evaluation/results/dense-jina-v3-v0_by_query_type.csv | 2473 |
| data/evaluation/results/dense-jina-v3-v0_failures.md | 10972 |
| data/evaluation/results/dense-jina-v3-v0_metrics.json | 512 |
| data/evaluation/results/dense-jina-v3-v0_per_query.csv | 9116 |
| data/evaluation/results/hybrid-rrf-v0_by_difficulty.csv | 568 |
| data/evaluation/results/hybrid-rrf-v0_by_query_type.csv | 2473 |
| data/evaluation/results/hybrid-rrf-v0_failures.md | 25236 |
| data/evaluation/results/hybrid-rrf-v0_metrics.json | 508 |
| data/evaluation/results/hybrid-rrf-v0_per_query.csv | 9246 |
| data/evaluation/results/retriever-comparison-v0.md | 3670 |
| data/evaluation/retrieval_eval.jsonl | 22347 |
| data/evaluation/retrieval_eval_annotation_report.md | 18227 |
| data/evaluation/retrieval_eval_annotation_summary.csv | 5159 |
| data/extracted/05-2026-TT-BKHCN.cleaned.txt | 17912 |
| data/extracted/05-2026-TT-BKHCN.raw.txt | 17991 |
| data/extracted/134-2025-QH15.cleaned.txt | 65287 |
| data/extracted/134-2025-QH15.raw.txt | 65293 |
| data/extracted/142-2026-ND-CP.cleaned.txt | 269419 |
| data/extracted/142-2026-ND-CP.raw.txt | 269573 |
| data/indexes/bge-reranker-v2-m3-v0/reranker_manifest.json | 750 |
| data/indexes/dense-jina-v3-v0/chunk_ids.json | 29095 |
| data/indexes/dense-jina-v3-v0/embeddings.npy | 3018880 |
| data/indexes/dense-jina-v3-v0/index_manifest.json | 733 |
| data/indexes/hybrid-rrf-v0/hybrid_manifest.json | 977 |
| data/processed/articles.jsonl | 317310 |
| data/processed/chunks.jsonl | 2326073 |
| data/rag/legal-rag-v0_manifest.json | 524 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval001.json | 206978 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval002.json | 58961 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval003.json | 55378 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval004.json | 65944 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval005a.json | 151325 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval005b.json | 58314 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval006.json | 151369 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval007.json | 60817 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval008.json | 67112 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval009.json | 61368 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval010.json | 62180 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval011.json | 59554 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval012.json | 66291 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval013.json | 141328 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval014.json | 144237 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval015.json | 67369 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval016.json | 142925 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval017.json | 68549 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval018.json | 62413 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval019.json | 59536 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval020.json | 53818 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval021.json | 60958 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval022.json | 60725 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval023.json | 68127 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval024.json | 56314 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval025.json | 57340 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval026.json | 58079 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval027.json | 59772 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval028.json | 64431 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval029.json | 65364 |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval030.json | 59035 |
| data/rag/traces/agentic-rag-v1_20260909T132334.960415Z.json | 3085 |
| data/rag/traces/agentic-rag-v1_20260909T132915.670264Z.json | 272394 |
| data/rag/traces/agentic-rag-v1_20260913T071538.629769Z.json | 4005 |
| data/rag/traces/agentic-rag-v1_20260913T072604.572183Z.json | 234296 |
| data/rag/traces/agentic-rag-v1_smoke.json | 55148 |
| data/rag/traces/legal-rag-v0_20260824T082500.431067Z.json | 4442 |
| data/rag/traces/legal-rag-v0_20260824T083023.964302Z.json | 4472 |
| data/rag/traces/legal-rag-v0_20260824T083324.619096Z.json | 4324 |
| data/rag/traces/legal-rag-v0_20260824T083822.282992Z.json | 4678 |
| data/rag/traces/legal-rag-v0_20260824T084241.384282Z.json | 5786 |
| data/rag/traces/legal-rag-v0_20260824T084747.340310Z.json | 5786 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval001/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval001/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval002/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval002/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval003/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval003/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval004/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval004/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval005a/started.json | 133 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval005a/terminal.json | 174 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval005b/started.json | 133 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval005b/terminal.json | 174 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval006/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval006/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval007/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval007/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval008/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval008/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval009/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval009/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval010/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval010/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval011/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval011/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval012/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval012/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval013/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval013/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval014/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval014/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval015/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval015/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval016/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval016/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval017/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval017/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval018/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval018/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval019/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval019/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval020/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval020/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval021/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval021/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval022/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval022/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval023/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval023/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval024/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval024/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval025/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval025/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval026/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval026/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval027/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval027/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval028/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval028/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval029/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval029/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval030/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval030/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/durable_seal_recovery_v1.json | 24573 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval001.json | 116369 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval002.json | 46305 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval003.json | 43203 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval004.json | 51429 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval005a.json | 126336 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval005b.json | 124465 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval006.json | 120886 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval007.json | 49053 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval008.json | 52998 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval009.json | 46625 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval010.json | 48132 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval011.json | 117409 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval012.json | 53817 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval013.json | 105787 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval014.json | 116498 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval015.json | 54004 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval016.json | 116588 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval017.json | 55075 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval018.json | 51013 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval019.json | 46724 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval020.json | 40712 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval021.json | 48519 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval022.json | 118164 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval023.json | 121363 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval024.json | 43858 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval025.json | 46026 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval026.json | 120126 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval027.json | 46628 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval028.json | 51490 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval029.json | 49024 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval030.json | 46522 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/loaded_environment.json | 1221 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval001.json | 5088 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval002.json | 3219 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval003.json | 3280 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval004.json | 3884 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval005a.json | 5295 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval005b.json | 4846 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval006.json | 5246 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval007.json | 4185 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval008.json | 3770 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval009.json | 3286 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval010.json | 4087 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval011.json | 4331 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval012.json | 5627 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval013.json | 5772 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval014.json | 5008 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval015.json | 3561 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval016.json | 5247 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval017.json | 3918 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval018.json | 3876 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval019.json | 3299 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval020.json | 3052 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval021.json | 3988 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval022.json | 5404 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval023.json | 5364 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval024.json | 3623 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval025.json | 3893 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval026.json | 4500 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval027.json | 4091 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval028.json | 4582 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval029.json | 3836 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval030.json | 4233 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval001.json | 116568 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval002.json | 46486 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval003.json | 43373 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval004.json | 51612 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval005a.json | 126548 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval005b.json | 124693 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval006.json | 121078 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval007.json | 49227 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval008.json | 53197 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval009.json | 46821 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval010.json | 48329 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval011.json | 117640 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval012.json | 53998 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval013.json | 105986 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval014.json | 116713 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval015.json | 54184 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval016.json | 116773 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval017.json | 55262 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval018.json | 51199 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval019.json | 46929 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval020.json | 40857 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval021.json | 48722 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval022.json | 118387 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval023.json | 121572 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval024.json | 44062 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval025.json | 46242 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval026.json | 120328 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval027.json | 46833 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval028.json | 51679 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval029.json | 49325 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval030.json | 46733 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/production_attempts.jsonl | 9521 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/production_outputs.jsonl | 2281387 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/production_seal.json | 18332 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/run_binding.json | 177 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/__init__.py | 0 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/__init__.py | 0 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/__init__.py | 0 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/__init__.py | 0 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/__init__.py | 0 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/block.py | 17796 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/configuration_xlm_roberta.py | 6542 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/embedding.py | 4442 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mha.py | 34368 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mlp.py | 7619 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_lora.py | 15447 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_xlm_roberta.py | 51134 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/rotary.py | 24758 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/stochastic_depth.py | 3761 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/xlm_padding.py | 10032 |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/worker.lock | 0 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval001/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval001/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval002/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval002/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval003/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval003/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval004/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval004/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval005a/started.json | 133 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval005a/terminal.json | 174 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval005b/started.json | 133 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval005b/terminal.json | 174 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval006/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval006/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval007/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval007/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval008/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval008/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval009/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval009/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval010/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval010/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval011/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval011/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval012/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval012/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval013/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval013/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval014/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval014/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval015/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval015/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval016/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval016/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval017/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval017/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval018/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval018/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval019/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval019/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval020/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval020/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval021/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval021/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval022/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval022/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval023/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval023/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval024/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval024/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval025/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval025/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval026/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval026/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval027/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval027/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval028/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval028/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval029/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval029/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval030/started.json | 132 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval030/terminal.json | 173 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/durable_seal_recovery_v1.json | 24579 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval001.json | 46821 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval002.json | 46303 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval003.json | 43077 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval004.json | 54065 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval005a.json | 51933 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval005b.json | 44275 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval006.json | 48301 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval007.json | 49153 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval008.json | 52656 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval009.json | 46873 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval010.json | 49775 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval011.json | 46961 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval012.json | 53501 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval013.json | 45561 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval014.json | 46335 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval015.json | 54106 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval016.json | 48870 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval017.json | 55087 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval018.json | 50825 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval019.json | 46682 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval020.json | 40730 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval021.json | 48957 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval022.json | 47242 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval023.json | 54413 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval024.json | 43964 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval025.json | 46040 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval026.json | 45237 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval027.json | 48032 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval028.json | 51444 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval029.json | 52376 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval030.json | 46560 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/loaded_environment.json | 1221 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval001.json | 3803 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval002.json | 3136 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval003.json | 3091 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval004.json | 4615 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval005a.json | 5042 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval005b.json | 6767 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval006.json | 4500 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval007.json | 4229 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval008.json | 3506 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval009.json | 3458 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval010.json | 7734 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval011.json | 3399 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval012.json | 5477 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval013.json | 4427 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval014.json | 4091 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval015.json | 3605 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval016.json | 4423 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval017.json | 3921 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval018.json | 3667 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval019.json | 3257 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval020.json | 3087 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval021.json | 4107 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval022.json | 5999 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval023.json | 4650 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval024.json | 3605 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval025.json | 3929 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval026.json | 3754 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval027.json | 4970 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval028.json | 4552 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval029.json | 4593 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval030.json | 4212 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval001.json | 47020 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval002.json | 46484 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval003.json | 43247 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval004.json | 54248 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval005a.json | 52159 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval005b.json | 44489 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval006.json | 48507 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval007.json | 49327 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval008.json | 52855 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval009.json | 47069 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval010.json | 49972 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval011.json | 47192 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval012.json | 53682 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval013.json | 45760 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval014.json | 46550 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval015.json | 54286 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval016.json | 49069 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval017.json | 55274 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval018.json | 51011 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval019.json | 46887 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval020.json | 40875 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval021.json | 49160 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval022.json | 47451 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval023.json | 54636 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval024.json | 44168 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval025.json | 46256 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval026.json | 45439 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval027.json | 48237 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval028.json | 51633 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval029.json | 52681 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval030.json | 46771 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/production_attempts.jsonl | 9521 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/production_outputs.jsonl | 1512426 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/production_seal.json | 18332 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/run_binding.json | 177 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/__init__.py | 0 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/__init__.py | 0 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/__init__.py | 0 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/__init__.py | 0 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/__init__.py | 0 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/block.py | 17796 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/configuration_xlm_roberta.py | 6542 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/embedding.py | 4442 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mha.py | 34368 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mlp.py | 7619 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_lora.py | 15447 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_xlm_roberta.py | 51134 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/rotary.py | 24758 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/stochastic_depth.py | 3761 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/xlm_padding.py | 10032 |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/worker.lock | 0 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval001/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval001/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval002/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval002/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval003/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval003/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval004/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval004/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval005a/started.json | 133 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval005a/terminal.json | 174 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval005b/started.json | 133 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval005b/terminal.json | 174 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval006/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval006/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval007/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval007/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval008/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval008/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval009/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval009/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval010/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval010/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval011/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval011/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval012/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval012/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval013/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval013/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval014/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval014/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval015/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval015/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval016/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval016/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval017/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval017/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval018/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval018/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval019/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval019/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval020/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval020/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval021/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval021/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval022/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval022/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval023/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval023/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval024/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval024/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval025/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval025/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval026/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval026/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval027/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval027/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval028/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval028/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval029/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval029/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval030/started.json | 132 |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval030/terminal.json | 173 |
| data/rag/traces/phase5/full-agentic-replication/durable_seal_recovery_v1.json | 24563 |
| data/rag/traces/phase5/full-agentic-replication/eval001.json | 127929 |
| data/rag/traces/phase5/full-agentic-replication/eval002.json | 46291 |
| data/rag/traces/phase5/full-agentic-replication/eval003.json | 43311 |
| data/rag/traces/phase5/full-agentic-replication/eval004.json | 54037 |
| data/rag/traces/phase5/full-agentic-replication/eval005a.json | 173552 |
| data/rag/traces/phase5/full-agentic-replication/eval005b.json | 124735 |
| data/rag/traces/phase5/full-agentic-replication/eval006.json | 123792 |
| data/rag/traces/phase5/full-agentic-replication/eval007.json | 49414 |
| data/rag/traces/phase5/full-agentic-replication/eval008.json | 53422 |
| data/rag/traces/phase5/full-agentic-replication/eval009.json | 46631 |
| data/rag/traces/phase5/full-agentic-replication/eval010.json | 49556 |
| data/rag/traces/phase5/full-agentic-replication/eval011.json | 112739 |
| data/rag/traces/phase5/full-agentic-replication/eval012.json | 54394 |
| data/rag/traces/phase5/full-agentic-replication/eval013.json | 99180 |
| data/rag/traces/phase5/full-agentic-replication/eval014.json | 117704 |
| data/rag/traces/phase5/full-agentic-replication/eval015.json | 53824 |
| data/rag/traces/phase5/full-agentic-replication/eval016.json | 114871 |
| data/rag/traces/phase5/full-agentic-replication/eval017.json | 55459 |
| data/rag/traces/phase5/full-agentic-replication/eval018.json | 50893 |
| data/rag/traces/phase5/full-agentic-replication/eval019.json | 46690 |
| data/rag/traces/phase5/full-agentic-replication/eval020.json | 40656 |
| data/rag/traces/phase5/full-agentic-replication/eval021.json | 48651 |
| data/rag/traces/phase5/full-agentic-replication/eval022.json | 47879 |
| data/rag/traces/phase5/full-agentic-replication/eval023.json | 157967 |
| data/rag/traces/phase5/full-agentic-replication/eval024.json | 43698 |
| data/rag/traces/phase5/full-agentic-replication/eval025.json | 46102 |
| data/rag/traces/phase5/full-agentic-replication/eval026.json | 44451 |
| data/rag/traces/phase5/full-agentic-replication/eval027.json | 48080 |
| data/rag/traces/phase5/full-agentic-replication/eval028.json | 51608 |
| data/rag/traces/phase5/full-agentic-replication/eval029.json | 51057 |
| data/rag/traces/phase5/full-agentic-replication/eval030.json | 46718 |
| data/rag/traces/phase5/full-agentic-replication/loaded_environment.json | 1221 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval001.json | 4907 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval002.json | 3195 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval003.json | 3357 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval004.json | 4918 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval005a.json | 5926 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval005b.json | 6630 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval006.json | 5128 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval007.json | 7801 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval008.json | 4043 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval009.json | 3419 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval010.json | 4413 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval011.json | 4505 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval012.json | 4429 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval013.json | 7916 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval014.json | 5203 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval015.json | 3490 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval016.json | 4827 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval017.json | 4024 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval018.json | 3761 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval019.json | 3299 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval020.json | 3010 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval021.json | 4160 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval022.json | 3969 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval023.json | 5808 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval024.json | 3511 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval025.json | 3963 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval026.json | 3413 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval027.json | 5247 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval028.json | 4634 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval029.json | 7122 |
| data/rag/traces/phase5/full-agentic-replication/observations/eval030.json | 4315 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval001.json | 128128 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval002.json | 46472 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval003.json | 43481 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval004.json | 54220 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval005a.json | 173764 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval005b.json | 124949 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval006.json | 123984 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval007.json | 49588 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval008.json | 53621 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval009.json | 46827 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval010.json | 49753 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval011.json | 112970 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval012.json | 54575 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval013.json | 99365 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval014.json | 117919 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval015.json | 54004 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval016.json | 115056 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval017.json | 55646 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval018.json | 51079 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval019.json | 46895 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval020.json | 40801 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval021.json | 48854 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval022.json | 48088 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval023.json | 158176 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval024.json | 43902 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval025.json | 46318 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval026.json | 44653 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval027.json | 48285 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval028.json | 51797 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval029.json | 51358 |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval030.json | 46929 |
| data/rag/traces/phase5/full-agentic-replication/production_attempts.jsonl | 9521 |
| data/rag/traces/phase5/full-agentic-replication/production_outputs.jsonl | 2231488 |
| data/rag/traces/phase5/full-agentic-replication/production_seal.json | 18332 |
| data/rag/traces/phase5/full-agentic-replication/run_binding.json | 177 |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/__init__.py | 0 |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/__init__.py | 0 |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/__init__.py | 0 |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/__init__.py | 0 |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/__init__.py | 0 |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/block.py | 17796 |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/configuration_xlm_roberta.py | 6542 |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/embedding.py | 4442 |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mha.py | 34368 |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mlp.py | 7619 |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_lora.py | 15447 |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_xlm_roberta.py | 51134 |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/rotary.py | 24758 |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/stochastic_depth.py | 3761 |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/xlm_padding.py | 10032 |
| data/rag/traces/phase5/full-agentic-replication/worker.lock | 0 |
| data/raw/docx/05-2026-TT-BKHCN.docx | 44429 |
| data/raw/docx/134-2025-QH15.docx | 47835 |
| data/raw/docx/142-2026-ND-CP.docx | 134312 |
| data/raw/pdf/05-2026-TT-BKHCN.pdf | 2265822 |
| data/raw/pdf/134-2025-QH15.pdf | 1060110 |
| data/raw/pdf/142-2026-ND-CP.pdf | 3661910 |
| data/source_registry/backups/documents.20260728-170238-881364.csv | 1459 |
| data/source_registry/backups/documents.20260809-194217-484925.csv | 1889 |
| data/source_registry/backups/documents.20260809-194330-642068.csv | 1917 |
| data/source_registry/backups/documents.20260809-194424-558417.csv | 1945 |
| data/source_registry/backups/documents.20260809-194439-245595.csv | 1973 |
| data/source_registry/backups/documents.20260809-194529-982940.csv | 1963 |
| data/source_registry/backups/documents.20260809-194557-704060.csv | 1953 |
| data/source_registry/boilerplate_lines.txt | 256 |
| data/source_registry/documents.csv | 1943 |
| data/validation/05-2026-TT-BKHCN.outline.txt | 494 |
| data/validation/134-2025-QH15.outline.txt | 4059 |
| data/validation/142-2026-ND-CP.outline.txt | 5827 |
| data/validation/chunking_report.csv | 532 |
| data/validation/cleaning_report.csv | 555 |
| data/validation/corpus_validation_details.txt | 1505 |
| data/validation/corpus_validation_summary.csv | 514 |
| data/validation/duplicate_chunks_report.txt | 43 |
| data/validation/extraction_report.csv | 428 |
| data/validation/manual_verification/05-2026-TT-BKHCN.verification.md | 6860 |
| data/validation/manual_verification/134-2025-QH15.verification.md | 13172 |
| data/validation/manual_verification/142-2026-ND-CP.verification.md | 14767 |
| data/validation/parser_report.csv | 550 |
| data/validation/short_chunks_report.txt | 176 |
| data/versions/corpus-v0.1/articles.jsonl | 317310 |
| data/versions/corpus-v0.1/chunks.jsonl | 2326073 |
| data/versions/corpus-v0.1/corpus_validation_details.txt | 1505 |
| data/versions/corpus-v0.1/corpus_validation_manifest.json | 1233 |
| data/versions/corpus-v0.1/corpus_validation_summary.csv | 514 |
| data/versions/corpus-v0.1/documents.csv | 1943 |
| data/versions/corpus_validation_manifest.json | 1233 |
| prompts/legal_rag_v0.txt | 1248 |
| requirements.txt | 78 |
| retriever-reranker-comparison-v0.md | 724 |
| scripts/__pycache__/agentic_rag.cpython-312.pyc | 37877 |
| scripts/__pycache__/analyze_candidate_coverage.cpython-312.pyc | 25577 |
| scripts/__pycache__/analyze_standard_rag_failures.cpython-312.pyc | 39595 |
| scripts/__pycache__/annotate_retrieval_eval.cpython-312.pyc | 24556 |
| scripts/__pycache__/bm25_baseline.cpython-310.pyc | 5602 |
| scripts/__pycache__/bm25_baseline.cpython-312.pyc | 9008 |
| scripts/__pycache__/build_chunks.cpython-312.pyc | 22085 |
| scripts/__pycache__/build_dense_index.cpython-312.pyc | 6215 |
| scripts/__pycache__/build_generation_eval_v1.cpython-312.pyc | 40017 |
| scripts/__pycache__/check_register.cpython-312.pyc | 5282 |
| scripts/__pycache__/citation_validator.cpython-310.pyc | 2174 |
| scripts/__pycache__/citation_validator.cpython-312.pyc | 2880 |
| scripts/__pycache__/clean_docx_text.cpython-312.pyc | 10239 |
| scripts/__pycache__/create_verification_samples.cpython-312.pyc | 16067 |
| scripts/__pycache__/dense_baseline.cpython-310.pyc | 6849 |
| scripts/__pycache__/dense_baseline.cpython-312.pyc | 11319 |
| scripts/__pycache__/evaluate_agentic_rag.cpython-312.pyc | 23632 |
| scripts/__pycache__/evaluate_bm25.cpython-312.pyc | 15811 |
| scripts/__pycache__/evaluate_dense.cpython-312.pyc | 10009 |
| scripts/__pycache__/evaluate_hybrid.cpython-312.pyc | 19759 |
| scripts/__pycache__/evaluate_reranker.cpython-312.pyc | 16523 |
| scripts/__pycache__/evaluate_standard_rag.cpython-312.pyc | 36852 |
| scripts/__pycache__/evidence_formatter.cpython-310.pyc | 1356 |
| scripts/__pycache__/evidence_formatter.cpython-312.pyc | 1905 |
| scripts/__pycache__/extract_docx.cpython-312.pyc | 9097 |
| scripts/__pycache__/generate_human_review_report.cpython-312.pyc | 21166 |
| scripts/__pycache__/hash_raw_files.cpython-312.pyc | 1647 |
| scripts/__pycache__/hybrid_rrf.cpython-312.pyc | 10361 |
| scripts/__pycache__/inspect_chunk_issues.cpython-312.pyc | 5195 |
| scripts/__pycache__/llm_client.cpython-310.pyc | 2591 |
| scripts/__pycache__/llm_client.cpython-312.pyc | 3808 |
| scripts/__pycache__/parse_legal_structure.cpython-312.pyc | 31565 |
| scripts/__pycache__/rag_baseline.cpython-310.pyc | 5255 |
| scripts/__pycache__/rag_baseline.cpython-312.pyc | 8114 |
| scripts/__pycache__/reranker_baseline.cpython-310.pyc | 7948 |
| scripts/__pycache__/reranker_baseline.cpython-312.pyc | 12073 |
| scripts/__pycache__/response_formatter.cpython-310.pyc | 2694 |
| scripts/__pycache__/response_formatter.cpython-312.pyc | 4542 |
| scripts/__pycache__/retrieval_pipeline.cpython-310.pyc | 9306 |
| scripts/__pycache__/retrieval_pipeline.cpython-312.pyc | 13351 |
| scripts/__pycache__/update_source_hashes.cpython-312.pyc | 7850 |
| scripts/__pycache__/update_verification_status.cpython-312.pyc | 6391 |
| scripts/__pycache__/validate_corpus.cpython-312.pyc | 34107 |
| scripts/__pycache__/validate_generation_eval.cpython-312.pyc | 11383 |
| scripts/__pycache__/validate_retrieval_eval.cpython-312.pyc | 6662 |
| scripts/agentic_rag.py | 30562 |
| scripts/analyze_candidate_coverage.py | 19038 |
| scripts/analyze_standard_rag_failures.py | 32091 |
| scripts/annotate_retrieval_eval.py | 17300 |
| scripts/bm25_baseline.py | 5610 |
| scripts/build_chunks.py | 18271 |
| scripts/build_dense_index.py | 3652 |
| scripts/build_generation_eval_v1.py | 33969 |
| scripts/check_register.py | 4719 |
| scripts/citation_validator.py | 1705 |
| scripts/clean_docx_text.py | 9704 |
| scripts/create_verification_samples.py | 10620 |
| scripts/dense_baseline.py | 6513 |
| scripts/evaluate_agentic_rag.py | 18554 |
| scripts/evaluate_bm25.py | 11408 |
| scripts/evaluate_dense.py | 6921 |
| scripts/evaluate_hybrid.py | 13611 |
| scripts/evaluate_reranker.py | 10919 |
| scripts/evaluate_standard_rag.py | 29924 |
| scripts/evidence_formatter.py | 1332 |
| scripts/extract_docx.py | 7788 |
| scripts/generate_human_review_report.py | 17951 |
| scripts/hash_raw_files.py | 713 |
| scripts/hybrid_rrf.py | 6490 |
| scripts/inspect_chunk_issues.py | 3197 |
| scripts/llm_client.py | 2042 |
| scripts/parse_legal_structure.py | 29036 |
| scripts/phase5_ablation_runner.py | 14648 |
| scripts/phase5_analyze.py | 5692 |
| scripts/phase5_assets.py | 8396 |
| scripts/phase5_common.py | 1982 |
| scripts/phase5_durable_seal_v1.py | 13987 |
| scripts/phase5_evaluation_quota_recovery_v1.py | 42776 |
| scripts/phase5_isolation.py | 4126 |
| scripts/phase5_observer.py | 6104 |
| scripts/phase5_preflight.py | 27120 |
| scripts/phase5_seal_recovery_v1.py | 19963 |
| scripts/rag_baseline.py | 5364 |
| scripts/reranker_baseline.py | 7022 |
| scripts/response_formatter.py | 2471 |
| scripts/retrieval_pipeline.py | 11031 |
| scripts/update_source_hashes.py | 4820 |
| scripts/update_verification_status.py | 3854 |
| scripts/validate_corpus.py | 37207 |
| scripts/validate_generation_eval.py | 7491 |
| scripts/validate_retrieval_eval.py | 4183 |
| tests/__pycache__/test_agentic_evaluation.cpython-312.pyc | 5241 |
| tests/__pycache__/test_agentic_rag.cpython-312.pyc | 15576 |
| tests/__pycache__/test_generation_eval.cpython-312.pyc | 13250 |
| tests/__pycache__/test_rag_runtime.cpython-312.pyc | 11122 |
| tests/phase5_run_suite.py | 1810 |
| tests/phase5_synthetic_worker.py | 1280 |
| tests/phase5_test_support.py | 3563 |
| tests/test_agentic_evaluation.py | 2929 |
| tests/test_agentic_rag.py | 9396 |
| tests/test_generation_eval.py | 5130 |
| tests/test_phase5_ablation_runner.py | 13869 |
| tests/test_phase5_evaluation_quota_recovery.py | 24058 |
| tests/test_phase5_leakage.py | 11104 |
| tests/test_phase5_preflight.py | 6548 |
| tests/test_phase5_seal_recovery_v1.py | 12809 |
| tests/test_rag_runtime.py | 6031 |

## Final integrity verification

PASS: SHA-256 compared before/after for all 1647 existing project files. Modified: 0. Deleted: 0. New files outside docs/repository_cleanup_v0/: 0. Exactly ten requested reports created. No project code or tests executed; network/API calls: 0. Per-file before/after hashes are in dependency_map_v0.json. Canonical hash-map SHA-256: `65ea71ec64c296ed8dfda883e49a0cf9e0399f5a9540b86992e731ead3dd721d`.

Manual move review count is 68 (23 source files plus 45 generated bytecode files with safe_to_move=needs_review); the migration_action MANUAL_REVIEW subset contains 23 source files. The other 23 scripts are protected in place or original-preserving wrapper candidates.
