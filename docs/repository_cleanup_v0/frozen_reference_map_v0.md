# Frozen reference map v0

Phase 5A is the explicit runtime/evaluation freeze anchor: `data/evaluation/generation/phase5/phase5a_ablation_manifest_v0.json#/frozen_artifacts`. All 67 listed file hashes match the current snapshot. Preserve both bytes and paths. Four CLI entrypoints are FROZEN_BUT_WRAPPABLE: this permits proposing a separate launcher, never changing the original.

| Path | Role | Recorded SHA-256 | Current match |
| --- | --- | --- | --- |
| data/evaluation/generation/agentic_rag_eval_v1_agentic-v1.jsonl | R1_results | a8d6a4bb5f18ddd79d6fcf98d8330b009e44764759e5f135e894528ad715b06e | YES |
| data/evaluation/generation/agentic_rag_metrics_v1_agentic-v1.json | R1_metrics_and_embedded_manifest | ca0459b683bcec40833b69f288497b5d6e6bd2640daa1910ab0f18b7ff4bf1d5 | YES |
| data/evaluation/generation/agentic_trace_analysis_metrics_v0.json | phase4e_context_and_provenance_analysis_only | ab10b4cd185cc41acc553cc991df74040cc980fd284c8217fdbdccc8c0bacab7 | YES |
| data/evaluation/generation/agentic_trace_analysis_v0.jsonl | phase4e_context_analysis_only | 750d33655f9038f7e3a4dc52160933f9cd742ca2d7a0b2142796c23f407e664a | YES |
| data/evaluation/generation/failure_analysis_metrics_v0.json | phase4a_labels_analysis_only | d2ea8278285d78fcbe9c4adf613bc90b5762b8fa62ea45deb03393194a4b7fb7 | YES |
| data/evaluation/generation/failure_analysis_points_v0.jsonl | phase4a_labels_analysis_only | bbc6993d0ff7108e5f39f6b34bd8549bff15493c3c435adefc3514b0cf1f1f53 | YES |
| data/evaluation/generation/failure_analysis_queries_v0.json | phase4a_labels_analysis_only | 842871677c4345562d92384e2abeb9f3f69da1d8f0158891dd02aea9200bd10e | YES |
| data/evaluation/generation/generation_eval_v1_verified.json | verified_final_gold_evaluator_only | 1795dbef913e63492c5cd6b8963c2f1a85642ddee0b1a42087f97203bc1895a4 | YES |
| data/evaluation/generation/generation_eval_v1_verified_manifest.json | verified_dataset_manifest | 693b2b3f0839bdefc380254de2640e47d9b5a81ff4c14f9acccbd5ee4c242fbe | YES |
| data/evaluation/generation/reports/agentic_rag_eval_v1_agentic-v1.md | R1_report | f87b5999a8a1b6d43a46f98caea912f4acbfa9ebfd4f3cfaf6419cf1b9e82ea2 | YES |
| data/evaluation/generation/reports/agentic_trace_analysis_v0.md | phase4e_context_analysis_only | 6aa6dffb0a33bd79ae6e6c2e874ec888a358cd2a8bc42c19369f5a1f7f654768 | YES |
| data/evaluation/generation/reports/standard_rag_eval_v0.md | R0_report | 8dc7a635fa4c9663a9fdbe1d36956bd1e327403d2b18d4c430dd48567235add2 | YES |
| data/evaluation/generation/standard_rag_eval_v0.jsonl | R0_results | 691f98cdffe29d6f4f2bfff8ad93c540447ee9cb4c78c3e48c003e2c2c4f487e | YES |
| data/evaluation/generation/standard_rag_manifest_v0.json | R0_manifest | bb0a4c56873f118b47f29b0aead8d2c30fa2b0a14702707762fe4c63f6c3a3ae | YES |
| data/evaluation/generation/standard_rag_metrics_v0.json | R0_metrics | 720cc8acd5c05d819c3b5f74bd46db8a4217eb93eee8abf2ea50ba229748ffe9 | YES |
| data/evaluation/retrieval_eval.jsonl | frozen_retrieval_gold_evaluator_only | 659c5cd0ff378747b9b135df00be57e5c1f5681b7eede761d3ce5808afbf3c62 | YES |
| data/indexes/bge-reranker-v2-m3-v0/reranker_manifest.json | frozen_retrieval_asset | 5a8f0845284bd2687addfe57de736606cfd01027118c2e7aa2c67dd0013d48e2 | YES |
| data/indexes/dense-jina-v3-v0/chunk_ids.json | frozen_retrieval_asset | b74ecd99fb6a79140cc3ac3e65c447b808a1294516788d7652c8e17b82b8a489 | YES |
| data/indexes/dense-jina-v3-v0/embeddings.npy | frozen_retrieval_asset | 9e0db949191bc830f8f16858a2e7de6c04b7a23e957362153d1798b4d855be04 | YES |
| data/indexes/dense-jina-v3-v0/index_manifest.json | frozen_retrieval_asset | 54685dd8a5543a6c0eba678eef93bfa595e67c0bed10e15f2632b4e384558a5f | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval001.json | R1_individual_trace | 25141dceea56ca96a7377588a7c64d4e2585ca867c4416da22ca174f90bf564d | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval002.json | R1_individual_trace | 8c54c15847d99f63c225de41e4f770ff74efc0b1d29b5fb0350c68d52ee768ff | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval003.json | R1_individual_trace | b53cc17ec50ffd631c1ceda0047e87a2049804bb86e59cab2eee20f7b6cedd59 | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval004.json | R1_individual_trace | 479db80a3c421d17c52034c6abc66c5a865332a7071ad2a95cbd65d1b64e3135 | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval005a.json | R1_individual_trace | b709ab073fa60ca9bc20421018149e3e1b5f12997ada77cea4edab2a2f11d2ba | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval005b.json | R1_individual_trace | bf159d710d5873700d13369b101b430480d5602c595ce1e6dafcdf3a9bab726d | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval006.json | R1_individual_trace | 954756d2b452499323051b507cea38d541fe03c24cfc92db1117e228ce739641 | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval007.json | R1_individual_trace | 997faabee29b9a26f80ecf7fb01931b7de9ac269c5f007b512fb7cbfe94b4a0b | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval008.json | R1_individual_trace | 87c78f08d17ae969d605a30323459719a5763bc112e9386eae741db643826315 | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval009.json | R1_individual_trace | 4dcfd8b5fc2c7aa32c886ea68e83edded394a471a991bb30bb4cf248526bbbc4 | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval010.json | R1_individual_trace | 7b653d8ba8bfd6248ea06d696a0cac58ce464b0860caf34b3175d2d0a42b30a0 | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval011.json | R1_individual_trace | b734c28db4268e7056fb83ae2de4ab699c86494198c965b58adc575cb4386c56 | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval012.json | R1_individual_trace | c8dbeff63de34d6d71f4a99a9bb621c49804d02abc739481328d8f4da2320c3e | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval013.json | R1_individual_trace | f9405c6865ca4fc5823bc8904e4f295cc9611d06f25062eb4035385d375eed97 | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval014.json | R1_individual_trace | c46fe23270427a64557a903f4083f0642c06f9a9013b120b7a9e33d593db2cdf | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval015.json | R1_individual_trace | 2798812d76030967c09dc0aaf2254cefb64e0d3296b244f7362e0015fa405228 | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval016.json | R1_individual_trace | 7a683265ef29edea00c5fdc1e3e99471cb227e711b9020aadd80188125200478 | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval017.json | R1_individual_trace | 82ce503a45908cdc4f2f18a32474763fef791d03909e3e2efab9ded1b85fe098 | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval018.json | R1_individual_trace | aca28a01ca545c70d552f819329b499d16d8eba8fee730b316c057345ab2a936 | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval019.json | R1_individual_trace | e8fdba42ac5e999e5c5951ffa771e193f4424824e4d0cd2ffeb40e860578dba5 | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval020.json | R1_individual_trace | c4f9c93f8d7928a2f6a03c6d4bf0e0ae53f9e6eb18de775df006fba6f253ca16 | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval021.json | R1_individual_trace | 0deb2e716908d3ad68aeea1cf8660224c9515669550a2358811b235b81c71f27 | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval022.json | R1_individual_trace | e1988000bb9fe1ad5d13d7904e28af149f07c94e96b41de2c26d651b34ff26f3 | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval023.json | R1_individual_trace | 61c963adbdc89a4d0618bffa8facef3cbdc4118d91f30861b62485733fc153fc | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval024.json | R1_individual_trace | 97148165e4286826e003ad0be172663491430a8466cd96417bd4e300b3f2a029 | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval025.json | R1_individual_trace | c9c08a8e76cb74d05b1bab1019a16c3387a2bea3fcef0f7ad38d49caf65a6938 | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval026.json | R1_individual_trace | faf9191e612b4049d84fa6738d155c1a2172495ee06c5a5e57f31e5d230a338c | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval027.json | R1_individual_trace | c342f074ddd4cdfb27f712f4e9bbc8ea273f206fb897407e7edd092c968dfc24 | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval028.json | R1_individual_trace | b8a71c5999f7a12c63a8eb2996177f9ae6cf412320ba999413ccd1ed4f902343 | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval029.json | R1_individual_trace | adf9f47115dbba09df89e4bba2cb8b4051b5bfa2b346e21a4d0ab9fd225cc8d0 | YES |
| data/rag/traces/agentic-rag-v1/agentic-v1/eval030.json | R1_individual_trace | e4f4a77a477ad41fa01105ad0907bf5e6a6bb5348cae986bc313249e84434b55 | YES |
| data/versions/corpus-v0.1/chunks.jsonl | authoritative_runtime_corpus | 0a6eff1601d14d6409552d566411cc8aebb5f51938402e3f998c312d72d63c67 | YES |
| prompts/legal_rag_v0.txt | baseline_generation_prompt | 0141aad79a262960eeeb88d9b138bc092ea15caeb0407a5ebadad27b8268d39e | YES |
| requirements.txt | declared_dependencies | 81fb0e06a2b80a7ee839a231ea1141e77e146d7589c6ab4986a72a52b9c94621 | YES |
| scripts/agentic_rag.py | frozen_production_source | e415429b39786e9cb7dc46488718fcda0fc164ca4a84e49d95630835188745b6 | YES |
| scripts/bm25_baseline.py | frozen_production_source | 704f6ba51889411f4891ddad615e54eb68672583e37aea6b5a9afca90c378ac8 | YES |
| scripts/citation_validator.py | frozen_production_source | 7e5eeb43e2c9316909e7c297f05dbaa9171eb51c3a5db76bd26944c6a36232fc | YES |
| scripts/dense_baseline.py | frozen_production_source | 030602670a13bc17aac4ab97dd65209a5825c4ef790fd25c0c3b6c2224fe99a8 | YES |
| scripts/evaluate_agentic_rag.py | frozen_evaluator_source | b78ad3224be4bd996d494f870dab3caaf0cc2680ad54d832936624db9dcc04c9 | YES |
| scripts/evaluate_standard_rag.py | frozen_evaluator_source | 0c8a8def9966b94c946d80ddbfbf31a4ddd446e3e6eb49f02c89254a2f032bf7 | YES |
| scripts/evidence_formatter.py | frozen_production_source | f9ad9f39944f6ec72bea920822f17c53e7ac95bf9ac416a1d53382ab8e04d259 | YES |
| scripts/llm_client.py | frozen_production_source | b60c064aad63ef92d320af697791ec65c5c30c35caee8a7e174c3ef37724bf84 | YES |
| scripts/rag_baseline.py | frozen_production_source | ae5a2dd7b0f89d7969c16c5d711e229bd1673df43e188f9a7296086e57d9b95a | YES |
| scripts/reranker_baseline.py | frozen_production_source | 609c2eb42f52265fa0a630697cedd2e000b9b5a52a4b0a848259d597e2bb6f85 | YES |
| scripts/response_formatter.py | frozen_production_source | ccc506802981ca3e200b043c4c279e94b2dc3dbdaa8f60317a6d69369154f7e0 | YES |
| scripts/retrieval_pipeline.py | frozen_production_source | 5080df6e2bbfb33cf945f3fa797107ac7d510cab1f6e2bc4f3bf25741766fd42 | YES |
| scripts/validate_generation_eval.py | frozen_evaluator_source | b8b5cc4eff89bc41eae0ff3f4bf3379c7ba6c11d508b8ec4d1082d5e7a18c824 | YES |

## Phase 5 and Phase 5C protection

Protect all original Phase 5/5C artifacts, including analysis Python under data/, access manifests, reviewer packets, amendments, locks, seals and integrity inventories. A file hash in an ordinary before-inventory proves a historical byte binding, not an explicit research freeze declaration. Phase 5 infrastructure is conservatively marked FROZEN_REFERENCE because later validation/manifest records bind it; resolve intended authoritative version before loosening that protection. Functional roles are not lost: observer/common/isolation/assets are shared support, runners and recovery tools are phase-specific tooling.

| Script | Evidence source | JSON pointer | Status |
| --- | --- | --- | --- |
| scripts/phase5_ablation_runner.py | data/evaluation/generation/phase5/agentic-v1-no-answer-revision/run_manifest.json | /frozen_source_sha256/scripts/phase5_ablation_runner.py | MATCH |
| scripts/phase5_analyze.py | data/evaluation/generation/phase5/agentic-v1-no-answer-revision/run_manifest.json | /frozen_source_sha256/scripts/phase5_analyze.py | MATCH |
| scripts/phase5_assets.py | data/evaluation/generation/phase5/agentic-v1-no-answer-revision/run_manifest.json | /frozen_source_sha256/scripts/phase5_assets.py | MATCH |
| scripts/phase5_common.py | data/evaluation/generation/phase5/agentic-v1-no-answer-revision/run_manifest.json | /frozen_source_sha256/scripts/phase5_common.py | MATCH |
| scripts/phase5_durable_seal_v1.py | data/evaluation/generation/phase5/phase5b2er1_quota_recovery_manifest_v0.json | /historical_file_hashes/scripts/phase5_durable_seal_v1.py | MATCH |
| scripts/phase5_evaluation_quota_recovery_v1.py | data/evaluation/generation/phase5/phase5b2er1_quota_recovery_manifest_v0.json | /infrastructure_hashes/scripts/phase5_evaluation_quota_recovery_v1.py | MATCH |
| scripts/phase5_isolation.py | data/evaluation/generation/phase5/agentic-v1-no-answer-revision/run_manifest.json | /frozen_source_sha256/scripts/phase5_isolation.py | MATCH |
| scripts/phase5_observer.py | data/evaluation/generation/phase5/agentic-v1-no-answer-revision/run_manifest.json | /frozen_source_sha256/scripts/phase5_observer.py | MATCH |
| scripts/phase5_preflight.py | data/evaluation/generation/phase5/agentic-v1-no-answer-revision/run_manifest.json | /frozen_source_sha256/scripts/phase5_preflight.py | MATCH |
| scripts/phase5_seal_recovery_v1.py | data/evaluation/generation/phase5/phase5b2er1_quota_recovery_manifest_v0.json | /historical_file_hashes/scripts/phase5_seal_recovery_v1.py | MATCH |

## Historical discrepancies and limitations

A historical bytecode hash differs for `scripts/__pycache__/retrieval_pipeline.cpython-310.pyc`. This discrepancy existed at the initial snapshot; it is not a modification by this inventory. Keep the bytecode until provenance review. Explicit Phase 5A frozen source/data bindings still match.

| Status | Occurrences |
| --- | --- |
| MATCH | 9830 |
| UNRESOLVED | 26457 |
| MISMATCH | 8 |

Full path/hash evidence is in dependency_map_v0.json. Unresolved records include model-cache assets outside this repository and paths relative to other historical roots; they are not automatically missing project files or drift. JSON pointer/object hashes and semantically named hash fields without explicit path pairs are not claimed as verified file hashes.

| Mismatched path | Evidence | Pointer |
| --- | --- | --- |
| scripts/__pycache__/retrieval_pipeline.cpython-310.pyc | data/evaluation/generation/phase5/phase5a_ablation_manifest_v0.json | /source_integrity/before_sha256/scripts/__pycache__/retrieval_pipeline.cpython-310.pyc |
| scripts/__pycache__/retrieval_pipeline.cpython-310.pyc | data/evaluation/generation/phase5/phase5b2e_v0/integrity_before.json | /scripts/__pycache__/retrieval_pipeline.cpython-310.pyc |
| scripts/__pycache__/retrieval_pipeline.cpython-310.pyc | data/evaluation/generation/phase5/phase5b2e_v0/provenance.json | /historical_frozen_hashes/scripts/__pycache__/retrieval_pipeline.cpython-310.pyc |
| scripts/__pycache__/retrieval_pipeline.cpython-310.pyc | data/evaluation/generation/phase5/phase5b2er1_quota_recovery_manifest_v0.json | /historical_file_hashes/scripts/__pycache__/retrieval_pipeline.cpython-310.pyc |
| scripts/__pycache__/retrieval_pipeline.cpython-310.pyc | data/evaluation/generation/phase5/phase5b2er2_v1/session_0002_binding.json | /before_inventory/scripts/__pycache__/retrieval_pipeline.cpython-310.pyc |
| scripts/__pycache__/retrieval_pipeline.cpython-310.pyc | data/evaluation/generation/phase5/phase5b2f_v0/integrity_before_inventory_v0.json | /project/scripts/__pycache__/retrieval_pipeline.cpython-310.pyc |
| scripts/__pycache__/retrieval_pipeline.cpython-310.pyc | data/evaluation/generation/phase5/phase5b2r_recovery_protocol_v1.json | /historical_frozen_hashes/scripts/__pycache__/retrieval_pipeline.cpython-310.pyc |
| scripts/__pycache__/retrieval_pipeline.cpython-310.pyc | data/evaluation/generation/phase5/phase5b2r_recovery_protocol_v1.json | /preserved_project_files/scripts/__pycache__/retrieval_pipeline.cpython-310.pyc |
