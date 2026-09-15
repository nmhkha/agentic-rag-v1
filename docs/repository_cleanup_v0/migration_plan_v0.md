# Migration plan v0

Proposal only. MOVE_SAFE count is zero: absence of import consumers does not establish safe relocation where root paths, outputs, historical inventories or external commands may bind the file. No existing source is classified as obsolete solely because outputs exist.

1. Preserve the SHA-256 baseline and original paths; resolve the historical bytecode discrepancy.
2. Review per-script import edges, path literals, dynamic callsites and manifest bindings in dependency_map_v0.json. Confirm external consumers, which static inspection cannot discover.
3. Develop v2 under src/legal_rag/agentic_v2 with independent prompts/config/results and new tests.
4. If desired, add separately reviewed launchers for frozen v1/Standard entrypoints. Preserve all originals byte-for-byte.
5. Only after approval, migrate selected nonfrozen tools with updates to callers, root discovery, documentation and tests. Retain an evidence-backed old/new path map outside immutable manifests.
6. Review bytecode/cache cleanup separately against seals and before-inventories. Do not regenerate frozen artifacts as a cleanup action.
7. At migration time use offline static checks first, then separately authorized tests; compare frozen hashes again. No such tests or migration ran in this phase.

| Path | Action | Move safety | Candidate destination |
| --- | --- | --- | --- |
| scripts/__pycache__/agentic_rag.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/analyze_candidate_coverage.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/analyze_standard_rag_failures.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/annotate_retrieval_eval.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/bm25_baseline.cpython-310.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/bm25_baseline.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/build_chunks.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/build_dense_index.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/build_generation_eval_v1.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/check_register.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/citation_validator.cpython-310.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/citation_validator.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/clean_docx_text.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/create_verification_samples.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/dense_baseline.cpython-310.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/dense_baseline.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/evaluate_agentic_rag.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/evaluate_bm25.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/evaluate_dense.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/evaluate_hybrid.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/evaluate_reranker.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/evaluate_standard_rag.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/evidence_formatter.cpython-310.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/evidence_formatter.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/extract_docx.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/generate_human_review_report.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/hash_raw_files.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/hybrid_rrf.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/inspect_chunk_issues.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/llm_client.cpython-310.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/llm_client.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/parse_legal_structure.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/rag_baseline.cpython-310.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/rag_baseline.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/reranker_baseline.cpython-310.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/reranker_baseline.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/response_formatter.cpython-310.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/response_formatter.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/retrieval_pipeline.cpython-310.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/retrieval_pipeline.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/update_source_hashes.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/update_verification_status.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/validate_corpus.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/validate_generation_eval.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/__pycache__/validate_retrieval_eval.cpython-312.pyc | DELETE_CANDIDATE_LATER | needs_review | outside source tree; regenerate cache after approval |
| scripts/agentic_rag.py | COPY_WRAPPER_ONLY | no | scripts/agentic_rag.py |
| scripts/analyze_candidate_coverage.py | MANUAL_REVIEW | needs_review | scripts/analysis/analyze_candidate_coverage.py |
| scripts/analyze_standard_rag_failures.py | MANUAL_REVIEW | needs_review | scripts/analysis/analyze_standard_rag_failures.py |
| scripts/annotate_retrieval_eval.py | MANUAL_REVIEW | needs_review | scripts/dataset/annotate_retrieval_eval.py |
| scripts/bm25_baseline.py | KEEP_IN_PLACE | no | scripts/bm25_baseline.py |
| scripts/build_chunks.py | MANUAL_REVIEW | needs_review | scripts/dataset/build_chunks.py |
| scripts/build_dense_index.py | MANUAL_REVIEW | needs_review | scripts/dataset/build_dense_index.py |
| scripts/build_generation_eval_v1.py | MANUAL_REVIEW | needs_review | scripts/dataset/build_generation_eval_v1.py |
| scripts/check_register.py | MANUAL_REVIEW | needs_review | scripts/validate/check_register.py |
| scripts/citation_validator.py | KEEP_IN_PLACE | no | scripts/citation_validator.py |
| scripts/clean_docx_text.py | MANUAL_REVIEW | needs_review | scripts/dataset/clean_docx_text.py |
| scripts/create_verification_samples.py | MANUAL_REVIEW | needs_review | scripts/dataset/create_verification_samples.py |
| scripts/dense_baseline.py | KEEP_IN_PLACE | no | scripts/dense_baseline.py |
| scripts/evaluate_agentic_rag.py | COPY_WRAPPER_ONLY | no | scripts/evaluate_agentic_rag.py |
| scripts/evaluate_bm25.py | MANUAL_REVIEW | needs_review | scripts/evaluate/evaluate_bm25.py |
| scripts/evaluate_dense.py | MANUAL_REVIEW | needs_review | scripts/evaluate/evaluate_dense.py |
| scripts/evaluate_hybrid.py | MANUAL_REVIEW | needs_review | scripts/evaluate/evaluate_hybrid.py |
| scripts/evaluate_reranker.py | MANUAL_REVIEW | needs_review | scripts/evaluate/evaluate_reranker.py |
| scripts/evaluate_standard_rag.py | COPY_WRAPPER_ONLY | no | scripts/evaluate_standard_rag.py |
| scripts/evidence_formatter.py | KEEP_IN_PLACE | no | scripts/evidence_formatter.py |
| scripts/extract_docx.py | MANUAL_REVIEW | needs_review | scripts/dataset/extract_docx.py |
| scripts/generate_human_review_report.py | MANUAL_REVIEW | needs_review | scripts/dataset/generate_human_review_report.py |
| scripts/hash_raw_files.py | MANUAL_REVIEW | needs_review | scripts/utilities/hash_raw_files.py |
| scripts/hybrid_rrf.py | MANUAL_REVIEW | needs_review | scripts/utilities/hybrid_rrf.py |
| scripts/inspect_chunk_issues.py | MANUAL_REVIEW | needs_review | scripts/analysis/inspect_chunk_issues.py |
| scripts/llm_client.py | KEEP_IN_PLACE | no | scripts/llm_client.py |
| scripts/parse_legal_structure.py | MANUAL_REVIEW | needs_review | scripts/dataset/parse_legal_structure.py |
| scripts/phase5_ablation_runner.py | KEEP_IN_PLACE | no | scripts/phase5_ablation_runner.py |
| scripts/phase5_analyze.py | KEEP_IN_PLACE | no | scripts/phase5_analyze.py |
| scripts/phase5_assets.py | KEEP_IN_PLACE | no | scripts/phase5_assets.py |
| scripts/phase5_common.py | KEEP_IN_PLACE | no | scripts/phase5_common.py |
| scripts/phase5_durable_seal_v1.py | KEEP_IN_PLACE | no | scripts/phase5_durable_seal_v1.py |
| scripts/phase5_evaluation_quota_recovery_v1.py | KEEP_IN_PLACE | no | scripts/phase5_evaluation_quota_recovery_v1.py |
| scripts/phase5_isolation.py | KEEP_IN_PLACE | no | scripts/phase5_isolation.py |
| scripts/phase5_observer.py | KEEP_IN_PLACE | no | scripts/phase5_observer.py |
| scripts/phase5_preflight.py | KEEP_IN_PLACE | no | scripts/phase5_preflight.py |
| scripts/phase5_seal_recovery_v1.py | KEEP_IN_PLACE | no | scripts/phase5_seal_recovery_v1.py |
| scripts/rag_baseline.py | COPY_WRAPPER_ONLY | no | scripts/rag_baseline.py |
| scripts/reranker_baseline.py | KEEP_IN_PLACE | no | scripts/reranker_baseline.py |
| scripts/response_formatter.py | KEEP_IN_PLACE | no | scripts/response_formatter.py |
| scripts/retrieval_pipeline.py | KEEP_IN_PLACE | no | scripts/retrieval_pipeline.py |
| scripts/update_source_hashes.py | MANUAL_REVIEW | needs_review | scripts/utilities/update_source_hashes.py |
| scripts/update_verification_status.py | MANUAL_REVIEW | needs_review | scripts/utilities/update_verification_status.py |
| scripts/validate_corpus.py | MANUAL_REVIEW | needs_review | scripts/validate/validate_corpus.py |
| scripts/validate_generation_eval.py | KEEP_IN_PLACE | no | scripts/validate_generation_eval.py |
| scripts/validate_retrieval_eval.py | MANUAL_REVIEW | needs_review | scripts/validate/validate_retrieval_eval.py |

KEEP_IN_PLACE protects original paths. COPY_WRAPPER_ONLY protects originals while allowing future new launchers. MANUAL_REVIEW is not relocation permission. DELETE_CANDIDATE_LATER applies only to generated bytecode here. ARCHIVE_LATER and MOVE_SAFE have no approved members.
