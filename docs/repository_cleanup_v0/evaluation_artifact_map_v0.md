# Historical evaluation artifact map v0

Static data inspection only: 31 retrieval queries; 31 verified generation queries; 102 required-point records. These counts were read from JSON, without importing a validator or evaluator.

R0 is Standard RAG; R1 is historical Agentic v1. Phase 5 R2 full-agentic-replication is a separate replication and must not replace R1. A1/no-answer-revision and A2/no-evidence-expansion are separate ablations. Canonical Phase 5 judging is indexed by `data/evaluation/generation/phase5/phase5b2f_v0/canonical_judgments_manifest.json`; preserve earlier failed/recovery records as provenance.

| Role | Exact authority/path |
| --- | --- |
| INPUT / GOLD | data/evaluation/retrieval_eval.jsonl |
| INPUT / GOLD | data/evaluation/generation/generation_eval_v1_verified.json + generation_eval_v1_verified_manifest.json |
| INPUT / CORPUS | data/versions/corpus-v0.1/chunks.jsonl |
| GENERATED RESULT / R0 | data/evaluation/generation/standard_rag_eval_v0.jsonl; standard_rag_metrics_v0.json; standard_rag_manifest_v0.json |
| GENERATED RESULT / R1 | data/evaluation/generation/agentic_rag_eval_v1_agentic-v1.jsonl; agentic_rag_metrics_v1_agentic-v1.json (embedded manifest) |
| TRACE / R1 | data/rag/traces/agentic-rag-v1/agentic-v1/ |
| ANALYSIS / Phase 4A | data/evaluation/generation/failure_analysis_*; reports/standard_rag_failure_analysis_v0.md |
| ANALYSIS / Phase 4E | data/evaluation/generation/agentic_trace_analysis_*; reports/agentic_trace_analysis_v0.md |
| Phase 5 trace outputs | data/rag/traces/phase5/{full-agentic-replication,agentic-v1-no-answer-revision,agentic-v1-no-evidence-expansion}/ |
| Phase 5 analysis/recovery | data/evaluation/generation/phase5/phase5b* |
| Phase 5C design/review | data/evaluation/generation/phase5/phase5c1_v0 through phase5c4_v0 |

## Complete evaluation/trace path index

Generated results can become inputs to later analysis; this table describes their primary provenance role. Phase 5 review inputs are not the historical 31-query gold. Generic phase records require manifest-specific role review; names alone do not authorize use as gold.

| Path | Role |
| --- | --- |
| data/evaluation/backups/retrieval_eval.20260814-145701.jsonl | GENERATED RESULT |
| data/evaluation/backups/retrieval_eval.20260814-151851.jsonl | GENERATED RESULT |
| data/evaluation/backups/retrieval_eval.20260814-153333.jsonl | GENERATED RESULT |
| data/evaluation/dev_queries.jsonl | GENERATED RESULT |
| data/evaluation/generation/ANNOTATION_WORKFLOW.md | ANALYSIS |
| data/evaluation/generation/agentic_rag_eval_v1_agentic-v1.jsonl | GENERATED RESULT |
| data/evaluation/generation/agentic_rag_metrics_v1_agentic-v1.json | GENERATED RESULT |
| data/evaluation/generation/agentic_trace_analysis_metrics_v0.json | ANALYSIS |
| data/evaluation/generation/agentic_trace_analysis_v0.jsonl | ANALYSIS |
| data/evaluation/generation/backups/generation_eval_v1.20260902-145534.json | INPUT / GOLD (draft or template; non-authoritative) |
| data/evaluation/generation/failure_analysis_metrics_v0.json | ANALYSIS |
| data/evaluation/generation/failure_analysis_points_v0.jsonl | ANALYSIS |
| data/evaluation/generation/failure_analysis_queries_v0.json | ANALYSIS |
| data/evaluation/generation/generation_annotation_audit_v1.md | ANALYSIS |
| data/evaluation/generation/generation_annotation_v1_report.md | ANALYSIS |
| data/evaluation/generation/generation_annotation_v1_review.md | ANALYSIS |
| data/evaluation/generation/generation_eval_v0.json | INPUT / GOLD (draft or template; non-authoritative) |
| data/evaluation/generation/generation_eval_v0.schema.json | ANALYSIS / PROVENANCE |
| data/evaluation/generation/generation_eval_v0_manifest.json | ANALYSIS / PROVENANCE |
| data/evaluation/generation/generation_eval_v1.json | INPUT / GOLD (draft or template; non-authoritative) |
| data/evaluation/generation/generation_eval_v1.schema.json | ANALYSIS / PROVENANCE |
| data/evaluation/generation/generation_eval_v1_manifest.json | ANALYSIS / PROVENANCE |
| data/evaluation/generation/generation_eval_v1_verified.json | INPUT / GOLD (authoritative) |
| data/evaluation/generation/generation_eval_v1_verified_manifest.json | ANALYSIS / PROVENANCE |
| data/evaluation/generation/partials/standard_rag_eval_v0_partial.20260902-151753.jsonl | GENERATED RESULT |
| data/evaluation/generation/partials/standard_rag_eval_v0_partial.20260902-155801.jsonl | GENERATED RESULT |
| data/evaluation/generation/phase5/agentic-v1-no-answer-revision/evaluation.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/agentic-v1-no-answer-revision/evaluation_attempts.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/agentic-v1-no-answer-revision/metrics.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/agentic-v1-no-answer-revision/run_manifest.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/agentic-v1-no-answer-revision/variant_manifest.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion/evaluation.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion/evaluation_attempts.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion/metrics.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion/run_manifest.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion/variant_manifest.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/contrast_R2_A1.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/contrast_R2_A2.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/execution_environment_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/execution_tools/launch_frozen_v0.py | ANALYSIS |
| data/evaluation/generation/phase5/execution_tools/report_incomplete_v0.py | ANALYSIS |
| data/evaluation/generation/phase5/full-agentic-replication/evaluation.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/full-agentic-replication/evaluation_attempts.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/full-agentic-replication/metrics.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/full-agentic-replication/run_manifest.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/full-agentic-replication/variant_manifest.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/integrity_before_after_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5a_ablation_manifest_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5a_ablation_spec_v0.md | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b1_preflight_manifest_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b1_preflight_report_v0.md | ANALYSIS |
| data/evaluation/generation/phase5/phase5b2_preflight_rerun_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2_preflight_tests_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval001/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval001/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval002/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval002/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval003/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval003/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval004/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval004/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval005a/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval005a/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval005b/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval005b/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval006/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval006/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval007/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval007/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval008/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval008/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval009/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval009/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval010/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval010/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval011/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval011/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval012/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval012/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval012/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval012/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval013/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval013/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval013/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval013/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval015/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval015/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval017/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval017/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval017/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval017/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval018/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval018/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval018/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval018/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval027/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval027/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval027/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval027/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval028/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval028/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval029/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval029/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval030/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval030/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/evaluation.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/evaluation_attempts.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/metrics.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval001.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval002.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval003.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval004.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval005a.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval005b.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval006.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval007.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval008.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval009.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval010.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval011.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval012.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval013.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval014.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval015.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval016.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval017.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval018.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval019.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval020.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval021.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval022.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval023.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval024.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval025.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval026.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval027.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval028.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval029.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/records/eval030.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval001/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval001/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval002/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval002/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval003/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval003/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval004/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval004/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval005a/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval005a/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval005b/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval005b/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval006/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval006/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval007/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval007/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval008/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval008/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval009/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval009/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval010/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval010/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval011/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval011/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval012/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval012/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval013/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval013/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval014/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval014/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval014/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval014/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval021/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval021/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval028/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval028/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval029/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval029/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval030/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval030/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/evaluation.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/evaluation_attempts.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/metrics.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval001.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval002.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval003.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval004.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval005a.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval005b.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval006.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval007.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval008.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval009.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval010.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval011.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval012.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval013.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval014.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval015.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval016.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval017.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval018.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval019.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval020.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval021.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval022.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval023.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval024.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval025.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval026.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval027.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval028.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval029.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/records/eval030.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/analysis_validation.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b2e_v0/analyze_frozen.py | ANALYSIS |
| data/evaluation/generation/phase5/phase5b2e_v0/console_output.txt | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/contrast_R2_A1.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/contrast_R2_A2.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/evaluate_frozen.py | ANALYSIS |
| data/evaluation/generation/phase5/phase5b2e_v0/evaluation_protocol.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b2e_v0/evaluation_protocol_initial.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b2e_v0/evaluator.lock | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval001/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval001/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval002/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval002/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval003/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval003/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval004/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval004/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval005a/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval005a/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval005b/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval005b/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval006/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval006/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval007/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval007/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval008/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval008/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval009/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval009/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval010/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval010/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval011/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval011/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval012/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval012/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval013/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval013/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval014/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval014/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval015/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval015/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval015/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval015/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval016/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval016/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval017/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval017/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval017/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval017/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval020/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval020/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/2/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/2/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/3/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/3/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval029/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval029/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval030/1/request.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval030/1/response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/evaluation.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/evaluation_attempts.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/metrics.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval001.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval002.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval003.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval004.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval005a.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval005b.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval006.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval007.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval008.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval009.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval010.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval011.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval012.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval013.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval014.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval015.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval016.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval017.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval018.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval019.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval020.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval021.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval022.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval023.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval024.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval025.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval026.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval027.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval028.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval029.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/records/eval030.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/integrity_after.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b2e_v0/integrity_before.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b2e_v0/provenance.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/recovery_gate.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/render_report.py | ANALYSIS |
| data/evaluation/generation/phase5/phase5b2e_v0/replication_R1_R2.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2e_v0/reporting_correction_validation.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b2e_v0/validate_analysis.py | ANALYSIS |
| data/evaluation/generation/phase5/phase5b2er1_console_v0.txt | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er1_integrity_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b2er1_quota_recovery_manifest_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b2er1_quota_recovery_spec_v0.md | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b2er1_quota_recovery_tests_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval014/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval014/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval014/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval014/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval016/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval016/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval016/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval016/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval019/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval019/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval019/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval019/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval020/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval020/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval020/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval020/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval022/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval022/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval022/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval022/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval023/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval023/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval023/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval023/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/2/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/2/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/2/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval024/2/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval025/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval025/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval025/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval025/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval026/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval026/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval026/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A1/eval026/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval015/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval015/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval015/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval015/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval016/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval016/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval016/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval016/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval017/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval017/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval017/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval017/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval018/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval018/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval018/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval018/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval019/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval019/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval019/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval019/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval020/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval020/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval020/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval020/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval022/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval022/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval022/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval022/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval023/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval023/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval023/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval023/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval024/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval024/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval024/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval024/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval025/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval025/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval025/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval025/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval026/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval026/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval026/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval026/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval027/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval027/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval027/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/A2/eval027/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval021/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval021/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval021/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval021/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval022/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval022/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval022/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval022/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval023/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval023/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval023/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval023/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval024/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval024/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval024/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval024/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval025/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval025/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval025/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval025/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval026/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval026/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval026/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval026/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval027/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval027/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval027/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval027/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval028/1/evaluation_record.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval028/1/receipt.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval028/1/started.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/R2/eval028/1/wire_response.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/execution_driver_session_0001.py | ANALYSIS |
| data/evaluation/generation/phase5/phase5b2er2_v1/execution_driver_session_0002.py | ANALYSIS |
| data/evaluation/generation/phase5/phase5b2er2_v1/phase5b2er2_session_0001_report.json | ANALYSIS |
| data/evaluation/generation/phase5/phase5b2er2_v1/phase5b2er2_session_0002_report.json | ANALYSIS |
| data/evaluation/generation/phase5/phase5b2er2_v1/protocol_binding.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b2er2_v1/quota_stop_0001.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/quota_stop_0001_resume_authorization.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2er2_v1/session.lock | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b2er2_v1/session_0001_binding.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b2er2_v1/session_0001_integrity.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b2er2_v1/session_0002_binding.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b2er2_v1/session_0002_integrity.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b2f_v0/agentic-v1-no-answer-revision/evaluation_complete.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2f_v0/agentic-v1-no-answer-revision/metrics.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2f_v0/agentic-v1-no-evidence-expansion/evaluation_complete.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2f_v0/agentic-v1-no-evidence-expansion/metrics.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2f_v0/analysis_tools/offline_analysis_v0.py | ANALYSIS |
| data/evaluation/generation/phase5/phase5b2f_v0/analysis_tools/phase5b2f_gate.py | ANALYSIS |
| data/evaluation/generation/phase5/phase5b2f_v0/analysis_tools/verify_final_analysis_v0.py | ANALYSIS |
| data/evaluation/generation/phase5/phase5b2f_v0/bootstrap_R2_A1.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2f_v0/bootstrap_R2_A2.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2f_v0/canonical_judgments_manifest.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b2f_v0/contrast_R2_A1.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2f_v0/contrast_R2_A2.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2f_v0/efficiency_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2f_v0/final_artifact_hashes_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2f_v0/full-agentic-replication/evaluation_complete.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2f_v0/full-agentic-replication/metrics.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2f_v0/integrity_before_after_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b2f_v0/integrity_before_inventory_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b2f_v0/phase5b2f_console_v0.txt | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2f_v0/phase5b2f_final_report_v0.md | ANALYSIS |
| data/evaluation/generation/phase5/phase5b2f_v0/phase5b2f_metrics_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2f_v0/point_transitions_R1_R2.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2f_v0/point_transitions_R2_A1.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2f_v0/point_transitions_R2_A2.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2f_v0/provenance_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2f_v0/recovery_completion_gate_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2f_v0/replication_R1_R2.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2f_v0/validation_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b2r_negative_tests_v1.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b2r_recovery_manifest_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b2r_recovery_protocol_v1.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5b2r_recovery_report_v0.md | ANALYSIS |
| data/evaluation/generation/phase5/phase5b_evaluation_metrics_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5b_evaluation_report_v0.md | ANALYSIS |
| data/evaluation/generation/phase5/phase5b_report_v0.md | ANALYSIS |
| data/evaluation/generation/phase5/phase5c1_v0/consolidate_research_v0.py | ANALYSIS |
| data/evaluation/generation/phase5/phase5c1_v0/final_artifact_hashes_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c1_v0/integrity_before_after_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c1_v0/integrity_before_inventory_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c1_v0/phase5c1_console_v0.txt | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c1_v0/phase5c1_decision_log_v0.md | ANALYSIS |
| data/evaluation/generation/phase5/phase5c1_v0/phase5c1_evidence_matrix_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c1_v0/phase5c1_exploratory_diagnostic_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c1_v0/phase5c1_manifest_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c1_v0/phase5c1_problem_requirement_map_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c1_v0/phase5c1_research_synthesis_v0.md | ANALYSIS |
| data/evaluation/generation/phase5/phase5c1_v0/phase5c1_validation_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c2_v0/final_artifact_hashes_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c2_v0/integrity_baseline_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c2_v0/integrity_before_after_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c2_v0/phase5c2_challenge_set_design_v0.md | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c2_v0/phase5c2_console_v0.txt | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c2_v0/phase5c2_decision_log_v0.md | ANALYSIS |
| data/evaluation/generation/phase5/phase5c2_v0/phase5c2_evaluation_protocol_draft_v0.md | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c2_v0/phase5c2_manifest_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c2_v0/phase5c2_requirement_validation_matrix_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c2_v0/phase5c2_trace_schema_design_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c2_v0/phase5c2_v2_requirements_design_v0.md | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c2_v0/phase5c2_validation_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c3_v0/final_artifact_hashes_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c3_v0/integrity_baseline_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c3_v0/integrity_before_after_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_console_v0.txt | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_controller_status_decision_table_v0.json | ANALYSIS |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_decision_table_validation_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_design_amendments_v0.md | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_external_review_v0.md | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_freeze_manifest_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_frozen_design_spec_v0.md | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_margin_governance_v0.md | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_quota_scheduler_requirements_v0.md | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_spec_bindings_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_trace_matrix_amendment_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c3_v0/phase5c3_validation_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/adjudication_corpus_audit_v0.json | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/adjudication_issue_resolutions_v0.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/candidate_admission_decisions_v0.jsonl | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/final_adjudicated_annotations_v0.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/final_retained_36_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/final_split_assignment_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/input_contamination_incident_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/integrity_before_after_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/phase5c4d_adjudication_report_v0.md | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/phase5c4d_console_v0.txt | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/phase5c4d_dimension_summary_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/phase5c4d_selection_summary_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/phase5c4d_validation_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_applicability_sufficiency_comparison_v0.jsonl | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_aspect_mapping_v0.jsonl | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_candidate_alignment_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_contamination_comparison_v0.jsonl | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_corpus_audit_comparison_v0.jsonl | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_disagreement_registry_v0.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_scope_comparison_v0.jsonl | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/ab_support_comparison_v0.jsonl | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/artifact_hashes_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/build_comparison_v0.py | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/comparison_access_manifest_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/comparison_check_results_v0.json | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/final_artifact_hashes_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/integrity_baseline_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/integrity_before_after_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/phase5c4c1_agreement_metrics_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/phase5c4c1_comparison_report_v0.md | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/phase5c4c1_console_v0.txt | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/phase5c4c1_disagreement_summary_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/phase5c4c1_validation_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/semantic_mapping_decisions_v0.py | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/source_integrity_validation_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/comparison_c1/validate_comparison_v0.py | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/annotation_A_v0.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/authored_tasks_v0.py | INPUT / GOLD (phase-specific; inspect access rules) |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/build_construction_v0.py | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/challenge_candidates_v0.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/cluster_rationales_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/construction_notes_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/contaminated_packet_quarantine_v0.json | INPUT / GOLD (phase-specific; inspect access rules) |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/contamination_screening_details_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/corpus_absence_audits_v0.jsonl | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/corpus_mapping_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/custodian_manifest_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/exclusion_log_v0.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/explicit_asks_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/exposure_events_v0.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/artifact_hashes_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/execution_and_access_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/fresh_reviewer_b_handoff_v1.md | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/integrity_baseline_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/integrity_before_after_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/phase5c4b0_console_v0.txt | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/phase5c4b0_review_summary_v0.md | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/phase5c4b0_validation_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b0_remediation_v0/sanitize_reviewer_b_v1.py | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b1_reference_preparation_v0/medical_reference_projection_audit_v1.json | INPUT / GOLD (phase-specific; inspect access rules) |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b1_reference_preparation_v0/phase5c4b1_console_v0.txt | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/phase5c4b1_reference_preparation_v0/prepare_medical_reference_v1.py | INPUT / GOLD (phase-specific; inspect access rules) |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/reviewer_b_comparison_after_independent_v0.jsonl | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/reviewer_b_id_mapping_v1.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/reviewer_b_packet_projection_audit_v1.json | INPUT / GOLD (phase-specific; inspect access rules) |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/reviewer_b_shuffle_provenance_v1.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/custodian/split_assignment_provisional_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/artifact_hashes_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/finalize_amendment_v0.py | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/integrity_baseline_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/integrity_before_after_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_adjudicator_c_protocol_v0.md | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_amendment_console_v0.txt | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_amendment_manifest_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_amendment_validation_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_research_claim_boundaries_v0.md | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_resource_constrained_amendment_v0.md | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/pragmatic_amendment_v0/phase5c4_selection_rules_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/artifact_hashes_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/frozen_source_checks_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/integrity_baseline_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/integrity_before_after_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_access_manifest_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_aggregate_composition_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_candidate_summary_v0.csv | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_cluster_summary_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_console_v0.txt | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_construction_report_v0.md | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_contamination_report_v0.md | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_dimension_matrix_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/public_review/phase5c4a_validation_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b/01_independent_review_units_v0.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b/README_independent_review_v0.md | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b/complete_corpus_evidence_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b/contamination_query_only_sources_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_packet_v1/contamination_reference_medical_v1.json | INPUT / GOLD (phase-specific; inspect access rules) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_packet_v1/reviewer_b_annotation_instructions_v1.md | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_packet_v1/reviewer_b_packet_manifest_v1.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_packet_v1/reviewer_b_queries_v1.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/annotation_B_v0.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/integrity_baseline_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/integrity_before_after_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/phase5c4b_access_manifest_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/phase5c4b_agreement_ready_summary_v0.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/phase5c4b_console_v0.txt | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/phase5c4b_review_summary_v0.md | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/phase5c4b_validation_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/reviewer_b_contamination_flags_v0.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/reviewer_b_corpus_audit_v0.json | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/reviewer_b_manifest_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/annotation_B_pre_anchor_correction_v1.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/annotation_B_substantive_locked_v1.jsonl | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/annotation_B_v1.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/annotation_structural_validation_v1.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/authored_specs_v1.py | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/build_b_annotations_v1.py | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/complete_medical_screen_v1.py | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/evidence_anchor_corrections_v1.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/finalize_b_v1.py | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/frozen_design_binding_checks_v1.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/generated_artifact_hashes_v1.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/historical_31_query_text_v1.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/integrity_baseline_v1.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/integrity_before_after_v1.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/medical_screen_completion_validation_v1.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/medical_screen_integrity_baseline_v1.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/medical_screen_integrity_before_after_v1.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/medical_screen_pre_read_seal_audit_v1.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/medical_screening_completed_v1.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/packet_schema_validation_v1.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/phase5c4b_access_manifest_v1.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/phase5c4b_agreement_ready_summary_v1.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/phase5c4b_console_v1.txt | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/phase5c4b_review_summary_v1.md | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/phase5c4b_validation_v1.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_generated_artifact_hashes_v1.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_phase5c4b_access_manifest_v1.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_phase5c4b_agreement_ready_summary_v1.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_phase5c4b_console_v1.txt | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_phase5c4b_review_summary_v1.md | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_phase5c4b_validation_v1.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_reviewer_b_contamination_flags_v1.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/pre_medical_reviewer_b_manifest_v1.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/preexisting_inventory_paths_v1.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/refine_bundle_anchors_v1.py | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/resume_audit_v1.json | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/reviewer_b_contamination_flags_v1.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/reviewer_b_corpus_audit_v1.json | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/reviewer_b_manifest_v1.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/reviewer_b_medical_contamination_screen_v1.jsonl | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/scoped_corpus_reviews_v1.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/screen_text_v1.py | ANALYSIS |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/substantive_lock_v1.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/text_screen_provenance_v1.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results_v1/validate_b_v1.py | ANALYSIS |
| data/evaluation/generation/phase5/production_seal_validation_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/phase5/query_inputs_v0.json | INPUT / GOLD (phase-specific; inspect access rules) |
| data/evaluation/generation/phase5/replication_R1_R2.json | GENERATED RESULT (phase record; verify manifest role) |
| data/evaluation/generation/phase5/report_artifact_hashes_v0.json | ANALYSIS |
| data/evaluation/generation/phase5/report_validation_v0.json | ANALYSIS / PROVENANCE / DESIGN |
| data/evaluation/generation/reports/agentic_rag_eval_v1_agentic-v1.md | ANALYSIS |
| data/evaluation/generation/reports/agentic_trace_analysis_v0.md | ANALYSIS |
| data/evaluation/generation/reports/standard_rag_eval_v0.md | ANALYSIS |
| data/evaluation/generation/reports/standard_rag_failure_analysis_v0.md | ANALYSIS |
| data/evaluation/generation/standard_rag_eval_v0.jsonl | GENERATED RESULT |
| data/evaluation/generation/standard_rag_manifest_v0.json | ANALYSIS / PROVENANCE |
| data/evaluation/generation/standard_rag_metrics_v0.json | GENERATED RESULT |
| data/evaluation/human_review_report.md | ANALYSIS |
| data/evaluation/human_review_summary.csv | ANALYSIS |
| data/evaluation/results/bge-reranker-v2-m3-v0_by_difficulty.csv | GENERATED RESULT |
| data/evaluation/results/bge-reranker-v2-m3-v0_by_query_type.csv | GENERATED RESULT |
| data/evaluation/results/bge-reranker-v2-m3-v0_failures.md | ANALYSIS |
| data/evaluation/results/bge-reranker-v2-m3-v0_metrics.json | GENERATED RESULT |
| data/evaluation/results/bge-reranker-v2-m3-v0_per_query.csv | GENERATED RESULT |
| data/evaluation/results/bm25-simple-v0_by_difficulty.csv | GENERATED RESULT |
| data/evaluation/results/bm25-simple-v0_by_query_type.csv | GENERATED RESULT |
| data/evaluation/results/bm25-simple-v0_failures.md | ANALYSIS |
| data/evaluation/results/bm25-simple-v0_metrics.json | GENERATED RESULT |
| data/evaluation/results/bm25-simple-v0_per_query.csv | GENERATED RESULT |
| data/evaluation/results/bm25-vs-dense-comparison.md | ANALYSIS |
| data/evaluation/results/candidate-union-v0_metrics.json | GENERATED RESULT |
| data/evaluation/results/candidate-union-v0_missing_gold.csv | GENERATED RESULT |
| data/evaluation/results/candidate-union-v0_per_query.csv | GENERATED RESULT |
| data/evaluation/results/candidate-union-v0_report.md | ANALYSIS |
| data/evaluation/results/dense-jina-v3-v0_by_difficulty.csv | GENERATED RESULT |
| data/evaluation/results/dense-jina-v3-v0_by_query_type.csv | GENERATED RESULT |
| data/evaluation/results/dense-jina-v3-v0_failures.md | ANALYSIS |
| data/evaluation/results/dense-jina-v3-v0_metrics.json | GENERATED RESULT |
| data/evaluation/results/dense-jina-v3-v0_per_query.csv | GENERATED RESULT |
| data/evaluation/results/hybrid-rrf-v0_by_difficulty.csv | GENERATED RESULT |
| data/evaluation/results/hybrid-rrf-v0_by_query_type.csv | GENERATED RESULT |
| data/evaluation/results/hybrid-rrf-v0_failures.md | ANALYSIS |
| data/evaluation/results/hybrid-rrf-v0_metrics.json | GENERATED RESULT |
| data/evaluation/results/hybrid-rrf-v0_per_query.csv | GENERATED RESULT |
| data/evaluation/results/retriever-comparison-v0.md | ANALYSIS |
| data/evaluation/retrieval_eval.jsonl | INPUT / GOLD (authoritative) |
| data/evaluation/retrieval_eval_annotation_report.md | ANALYSIS |
| data/evaluation/retrieval_eval_annotation_summary.csv | ANALYSIS |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval001.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval002.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval003.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval004.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval005a.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval005b.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval006.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval007.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval008.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval009.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval010.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval011.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval012.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval013.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval014.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval015.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval016.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval017.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval018.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval019.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval020.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval021.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval022.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval023.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval024.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval025.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval026.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval027.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval028.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval029.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval030.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1_20260909T132334.960415Z.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1_20260909T132915.670264Z.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1_20260913T071538.629769Z.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1_20260913T072604.572183Z.json | GENERATED RESULT / TRACE |
| data/rag/traces/agentic-rag-v1_smoke.json | GENERATED RESULT / TRACE |
| data/rag/traces/legal-rag-v0_20260824T082500.431067Z.json | GENERATED RESULT / TRACE |
| data/rag/traces/legal-rag-v0_20260824T083023.964302Z.json | GENERATED RESULT / TRACE |
| data/rag/traces/legal-rag-v0_20260824T083324.619096Z.json | GENERATED RESULT / TRACE |
| data/rag/traces/legal-rag-v0_20260824T083822.282992Z.json | GENERATED RESULT / TRACE |
| data/rag/traces/legal-rag-v0_20260824T084241.384282Z.json | GENERATED RESULT / TRACE |
| data/rag/traces/legal-rag-v0_20260824T084747.340310Z.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval001/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval001/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval002/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval002/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval003/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval003/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval004/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval004/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval005a/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval005a/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval005b/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval005b/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval006/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval006/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval007/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval007/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval008/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval008/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval009/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval009/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval010/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval010/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval011/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval011/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval012/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval012/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval013/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval013/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval014/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval014/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval015/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval015/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval016/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval016/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval017/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval017/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval018/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval018/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval019/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval019/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval020/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval020/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval021/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval021/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval022/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval022/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval023/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval023/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval024/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval024/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval025/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval025/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval026/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval026/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval027/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval027/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval028/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval028/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval029/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval029/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval030/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/attempts/eval030/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/durable_seal_recovery_v1.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval001.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval002.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval003.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval004.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval005a.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval005b.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval006.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval007.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval008.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval009.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval010.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval011.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval012.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval013.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval014.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval015.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval016.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval017.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval018.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval019.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval020.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval021.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval022.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval023.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval024.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval025.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval026.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval027.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval028.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval029.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/eval030.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/loaded_environment.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval001.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval002.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval003.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval004.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval005a.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval005b.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval006.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval007.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval008.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval009.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval010.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval011.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval012.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval013.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval014.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval015.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval016.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval017.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval018.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval019.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval020.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval021.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval022.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval023.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval024.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval025.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval026.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval027.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval028.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval029.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/observations/eval030.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval001.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval002.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval003.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval004.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval005a.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval005b.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval006.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval007.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval008.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval009.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval010.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval011.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval012.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval013.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval014.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval015.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval016.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval017.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval018.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval019.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval020.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval021.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval022.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval023.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval024.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval025.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval026.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval027.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval028.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval029.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/outputs/eval030.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/production_attempts.jsonl | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/production_outputs.jsonl | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/production_seal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/run_binding.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/__init__.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/__init__.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/__init__.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/__init__.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/__init__.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/block.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/configuration_xlm_roberta.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/embedding.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mha.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mlp.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_lora.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_xlm_roberta.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/rotary.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/stochastic_depth.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/xlm_padding.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-answer-revision/worker.lock | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval001/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval001/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval002/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval002/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval003/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval003/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval004/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval004/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval005a/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval005a/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval005b/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval005b/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval006/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval006/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval007/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval007/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval008/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval008/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval009/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval009/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval010/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval010/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval011/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval011/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval012/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval012/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval013/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval013/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval014/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval014/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval015/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval015/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval016/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval016/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval017/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval017/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval018/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval018/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval019/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval019/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval020/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval020/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval021/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval021/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval022/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval022/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval023/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval023/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval024/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval024/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval025/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval025/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval026/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval026/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval027/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval027/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval028/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval028/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval029/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval029/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval030/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/attempts/eval030/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/durable_seal_recovery_v1.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval001.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval002.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval003.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval004.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval005a.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval005b.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval006.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval007.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval008.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval009.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval010.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval011.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval012.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval013.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval014.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval015.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval016.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval017.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval018.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval019.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval020.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval021.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval022.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval023.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval024.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval025.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval026.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval027.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval028.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval029.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/eval030.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/loaded_environment.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval001.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval002.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval003.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval004.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval005a.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval005b.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval006.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval007.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval008.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval009.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval010.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval011.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval012.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval013.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval014.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval015.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval016.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval017.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval018.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval019.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval020.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval021.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval022.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval023.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval024.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval025.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval026.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval027.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval028.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval029.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/observations/eval030.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval001.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval002.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval003.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval004.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval005a.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval005b.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval006.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval007.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval008.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval009.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval010.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval011.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval012.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval013.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval014.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval015.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval016.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval017.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval018.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval019.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval020.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval021.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval022.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval023.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval024.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval025.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval026.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval027.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval028.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval029.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/outputs/eval030.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/production_attempts.jsonl | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/production_outputs.jsonl | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/production_seal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/run_binding.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/__init__.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/__init__.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/__init__.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/__init__.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/__init__.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/block.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/configuration_xlm_roberta.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/embedding.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mha.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mlp.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_lora.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_xlm_roberta.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/rotary.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/stochastic_depth.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/xlm_padding.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/agentic-v1-no-evidence-expansion/worker.lock | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval001/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval001/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval002/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval002/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval003/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval003/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval004/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval004/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval005a/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval005a/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval005b/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval005b/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval006/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval006/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval007/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval007/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval008/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval008/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval009/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval009/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval010/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval010/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval011/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval011/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval012/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval012/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval013/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval013/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval014/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval014/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval015/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval015/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval016/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval016/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval017/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval017/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval018/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval018/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval019/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval019/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval020/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval020/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval021/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval021/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval022/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval022/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval023/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval023/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval024/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval024/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval025/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval025/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval026/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval026/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval027/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval027/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval028/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval028/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval029/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval029/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval030/started.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/attempts/eval030/terminal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/durable_seal_recovery_v1.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval001.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval002.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval003.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval004.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval005a.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval005b.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval006.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval007.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval008.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval009.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval010.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval011.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval012.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval013.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval014.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval015.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval016.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval017.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval018.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval019.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval020.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval021.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval022.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval023.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval024.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval025.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval026.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval027.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval028.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval029.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/eval030.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/loaded_environment.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval001.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval002.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval003.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval004.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval005a.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval005b.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval006.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval007.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval008.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval009.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval010.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval011.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval012.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval013.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval014.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval015.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval016.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval017.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval018.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval019.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval020.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval021.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval022.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval023.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval024.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval025.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval026.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval027.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval028.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval029.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/observations/eval030.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval001.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval002.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval003.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval004.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval005a.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval005b.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval006.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval007.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval008.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval009.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval010.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval011.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval012.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval013.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval014.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval015.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval016.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval017.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval018.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval019.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval020.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval021.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval022.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval023.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval024.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval025.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval026.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval027.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval028.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval029.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/outputs/eval030.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/production_attempts.jsonl | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/production_outputs.jsonl | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/production_seal.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/run_binding.json | GENERATED RESULT / TRACE |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/__init__.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/__init__.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/__init__.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/__init__.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/__init__.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/block.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/configuration_xlm_roberta.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/embedding.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mha.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mlp.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_lora.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_xlm_roberta.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/rotary.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/stochastic_depth.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/xlm_padding.py | GENERATED CACHE / not benchmark score |
| data/rag/traces/phase5/full-agentic-replication/worker.lock | GENERATED RESULT / TRACE |
