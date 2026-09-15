# Duplicate and superseded candidates v0

No file is approved for deletion or relocation. Similar responsibilities do not establish equivalent behavior.

| Group | Authority / reason | Proposal |
| --- | --- | --- |
| rag_baseline / agentic_rag | Separate R0 single-shot and R1 finite-budget controllers; both explicitly frozen. | Keep both. |
| evaluate_standard_rag / evaluate_agentic_rag | Agentic imports Standard judge/point-audit utilities. Different benchmark roles, not replacements. | Keep both with validator closure. |
| evaluate_bm25 / evaluate_dense / evaluate_hybrid / evaluate_reranker | Distinct historical experiments; shared BM25 metric implementation is imported by later evaluators. | Preserve metric semantics and all experiment outputs. |
| hybrid_rrf / reranker_baseline / retrieval_pipeline | Current frozen runtime uses candidate union then reranking, not RRF. hybrid_rrf remains authoritative for hybrid-rrf-v0. | Possible legacy location after provenance migration review, not obsolete deletion. |
| phase5_analyze / data/.../evaluate_frozen.py / offline_analysis_v0.py | Post-seal judging, frozen evaluation recovery, and offline analysis serve different stages. Canonical judgments are bound by phase5b2f_v0/canonical_judgments_manifest.json. | Preserve recovery lineage; do not replace by newest filename. |
| phase5_seal_recovery_v1 / phase5_durable_seal_v1 / phase5_evaluation_quota_recovery_v1 | Provenance recovery, durable sealing correction and quota recovery are separate mechanisms with recorded artifacts. | Keep path-stable. |
| generation_eval_v0 / generation_eval_v1 / generation_eval_v1_verified | Verified v1 is evaluator authority: verified manifest binds 31 queries and 102 points. Earlier draft/schema/audit files are provenance. | Archive only via later evidence-preserving plan. |
| hash_raw_files / update_source_hashes / sha256 helpers | Read/registry-update responsibilities overlap; phase5_common canonical hashing is used in seals. | Do not centralize frozen helper implementations. |
| data/processed versus data/versions/corpus-v0.1 | Versioned corpus is frozen runtime authority; processed files are construction provenance. | Retain both pending exact data lineage review. |
| scripts/__pycache__ and cached transformer source | Generated caches, including copied downloaded model code. Some inventories/seals bind their bytes. | Future cleanup candidate only after provenance review. |

## Exactly repeated top-level function ASTs

AST equality ignores source positions but retains function names, constants and bodies; it does not prove identical global context. Frozen callsites remain authoritative for their own runs.

- `scripts/agentic_rag.py::write_trace`; `scripts/rag_baseline.py::write_trace`
- `scripts/analyze_candidate_coverage.py::sha256`; `scripts/build_dense_index.py::sha256`; `scripts/evaluate_hybrid.py::sha256`; `scripts/evaluate_reranker.py::sha256`
- `scripts/analyze_candidate_coverage.py::article_id`; `scripts/evaluate_bm25.py::article_id`
- `scripts/analyze_standard_rag_failures.py::load_json`; `scripts/evaluate_standard_rag.py::load_json`
- `scripts/analyze_standard_rag_failures.py::load_jsonl`; `scripts/validate_generation_eval.py::load_jsonl`
- `scripts/analyze_standard_rag_failures.py::sha256`; `scripts/build_generation_eval_v1.py::sha256`; `scripts/validate_generation_eval.py::sha256`
- `scripts/evaluate_agentic_rag.py::utc_now`; `scripts/evaluate_standard_rag.py::utc_now`
- `scripts/evaluate_hybrid.py::load_csv`; `scripts/evaluate_reranker.py::load_csv`

## Byte-identical files

Each group shares SHA-256. Copies inside reviewer packets, caches and historical snapshots may be intentional and independently path-bound. Authority is the role/manifest binding, not date or shortest path. Empty files are included.

### Group 1

- `data/evaluation/generation/backups/generation_eval_v1.20260902-145534.json`
- `data/evaluation/generation/generation_eval_v1.json`
### Group 2

- `data/evaluation/generation/phase5/agentic-v1-no-answer-revision/evaluation_attempts.jsonl`
- `data/evaluation/generation/phase5/agentic-v1-no-evidence-expansion/evaluation_attempts.jsonl`
- `data/evaluation/generation/phase5/full-agentic-replication/evaluation_attempts.jsonl`
- `data/evaluation/generation/phase5/phase5b2e_v0/evaluator.lock`
- `data/evaluation/generation/phase5/phase5b2er2_v1/session.lock`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/adjudication_issue_resolutions_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/candidate_admission_decisions_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/adjudication_d_v0/final_adjudicated_annotations_v0.jsonl`
- `data/evaluation/generation/phase5/phase5c4_v0/reviewer_b_results/annotation_B_v0.jsonl`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-answer-revision/worker.lock`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/__init__.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/worker.lock`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/__init__.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/__init__.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/__init__.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/__init__.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/__init__.py`
- `data/rag/traces/phase5/full-agentic-replication/worker.lock`
### Group 3

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval002/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval002/1/request.json`
### Group 4

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval003/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval003/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval003/1/request.json`
### Group 5

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval009/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval009/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval009/1/request.json`
### Group 6

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval012/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval012/2/request.json`
### Group 7

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval012/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval013/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval017/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval018/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval027/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval014/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval015/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval017/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/3/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/2/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/3/response.json`
### Group 8

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval013/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval013/2/request.json`
### Group 9

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval014/3/request.json`
### Group 10

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval015/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval015/3/request.json`
### Group 11

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval016/3/request.json`
### Group 12

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval017/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval017/2/request.json`
### Group 13

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval018/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval018/2/request.json`
### Group 14

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval019/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval019/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval019/3/request.json`
### Group 15

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval020/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval020/3/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval020/1/request.json`
### Group 16

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval021/3/request.json`
### Group 17

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval022/3/request.json`
### Group 18

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval023/3/request.json`
### Group 19

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval024/3/request.json`
### Group 20

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval025/3/request.json`
### Group 21

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval026/3/request.json`
### Group 22

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval027/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-answer-revision/attempts/eval027/2/request.json`
### Group 23

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval011/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval011/1/request.json`
### Group 24

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval014/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval014/2/request.json`
### Group 25

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval016/3/request.json`
### Group 26

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval017/3/request.json`
### Group 27

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval018/3/request.json`
### Group 28

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval022/3/request.json`
### Group 29

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval023/3/request.json`
### Group 30

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval024/3/request.json`
### Group 31

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval025/3/request.json`
### Group 32

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval026/3/request.json`
### Group 33

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval027/3/request.json`
### Group 34

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval030/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval030/1/request.json`
### Group 35

- `data/evaluation/generation/phase5/phase5b2e_v0/agentic-v1-no-evidence-expansion/attempts/eval030/1/response.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval030/1/response.json`
### Group 36

- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval015/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval015/2/request.json`
### Group 37

- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval017/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval017/2/request.json`
### Group 38

- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval018/3/request.json`
### Group 39

- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval021/3/request.json`
### Group 40

- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval022/3/request.json`
### Group 41

- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval023/3/request.json`
### Group 42

- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval024/3/request.json`
### Group 43

- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval025/3/request.json`
### Group 44

- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval026/3/request.json`
### Group 45

- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval027/3/request.json`
### Group 46

- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/1/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/2/request.json`
- `data/evaluation/generation/phase5/phase5b2e_v0/full-agentic-replication/attempts/eval028/3/request.json`
### Group 47

- `data/processed/articles.jsonl`
- `data/versions/corpus-v0.1/articles.jsonl`
### Group 48

- `data/processed/chunks.jsonl`
- `data/versions/corpus-v0.1/chunks.jsonl`
### Group 49

- `data/rag/traces/phase5/agentic-v1-no-answer-revision/loaded_environment.json`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/loaded_environment.json`
- `data/rag/traces/phase5/full-agentic-replication/loaded_environment.json`
### Group 50

- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/block.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/block.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/block.py`
### Group 51

- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/configuration_xlm_roberta.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/configuration_xlm_roberta.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/configuration_xlm_roberta.py`
### Group 52

- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/embedding.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/embedding.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/embedding.py`
### Group 53

- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mha.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mha.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mha.py`
### Group 54

- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mlp.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mlp.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/mlp.py`
### Group 55

- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_lora.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_lora.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_lora.py`
### Group 56

- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_xlm_roberta.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_xlm_roberta.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/modeling_xlm_roberta.py`
### Group 57

- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/rotary.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/rotary.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/rotary.py`
### Group 58

- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/stochastic_depth.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/stochastic_depth.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/stochastic_depth.py`
### Group 59

- `data/rag/traces/phase5/agentic-v1-no-answer-revision/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/xlm_padding.py`
- `data/rag/traces/phase5/agentic-v1-no-evidence-expansion/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/xlm_padding.py`
- `data/rag/traces/phase5/full-agentic-replication/runtime_cache/modules/transformers_modules/jinaai/xlm-roberta-flash-implementation/bd55a5ec8e6c0fb1d6c26efb4b6a4a74ce8a88d3/xlm_padding.py`
### Group 60

- `data/source_registry/documents.csv`
- `data/versions/corpus-v0.1/documents.csv`
### Group 61

- `data/validation/corpus_validation_details.txt`
- `data/versions/corpus-v0.1/corpus_validation_details.txt`
### Group 62

- `data/validation/corpus_validation_summary.csv`
- `data/versions/corpus-v0.1/corpus_validation_summary.csv`
### Group 63

- `data/versions/corpus-v0.1/corpus_validation_manifest.json`
- `data/versions/corpus_validation_manifest.json`
