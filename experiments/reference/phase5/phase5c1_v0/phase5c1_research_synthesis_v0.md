| Phase | Question | Main result | Evidence tier | Status |
| --- | --- | --- | --- | --- |
| Corpus | Có nền dữ liệu cố định để nghiên cứu?  | corpus-v0.1: 3 documents, 86 articles, 737 chunks; 0 errors, 4 warnings | A — frozen validation artifact | Historical validation passed; unchanged |
| Retrieval | Localization có đủ cho full answer? | Article Hit@5 0.967741935484; chunk Recall@5 0.623911930364 | A | Historical frozen |
| Standard RAG | Top-5 → answer đủ ý? | AC macro 0.675268817204; 60/102 | A | R0 frozen |
| Failure Analysis | Failure nằm ở đâu? | Primary causes: {'retrieval_miss': 16, 'evidence_coverage': 17, 'answer_generation': 9, 'citation': 4, 'none': 56} | A — frozen point audit, descriptive | Phase 4A complete |
| Agentic v1 | Conditional intervention giúp ở đâu? | R1 AC macro 0.723655913978; 65/102; higher call cost | A — historical comparison | R1 frozen; attribution limited |
| Trace Analysis | Hành vi và self-check có khớp outcomes? | 17 internal-complete/benchmark-incomplete; 15 false-success pattern | B | Phase 4E observational |
| Controlled Ablation | Revision/expansion contribution vượt replication? | 93/93 judgments; A1 và A2: Insufficient evidence | A; trigger descriptions B | Phase 5B.2-F PASS |
| Exploratory hard-query diagnostic | Missing aspects còn được theo dõi tới answer? | Expansion/revision used; E58 added to answer; E6/E26 unused; completeness=true | C | EXPLORATORY / NON-BENCHMARK / NON-CONFIRMATORY |

# Phase 5C.1 — Research Findings Consolidation

## 1. Scope and methodology

READ-ONLY RESEARCH SYNTHESIS. Chỉ tạo additive artifacts trong `data/evaluation/generation/phase5/phase5c1_v0/`. Phân tích các records, traces, frozen metrics và reports đã có; không thực hiện semantic judging, không chạy lại bootstrap, retrieval hay production. Network/API = 0; production = 0; evaluator = 0. Không thay corpus, gold, prompt, runtime, evaluator, benchmark hoặc interpretation Phase 5. Không chạy A3/A4.

Authority: Phase 5A quy định interpretation; `phase5b2f_v0/` chứa final complete 93/93 benchmark. Các available-case outputs và run manifests ghi INCOMPLETE thuộc thời điểm trước recovery, không phải primary final analysis. Final canonical records dùng accepted v0 trước, nếu thiếu mới dùng accepted recovery v1; 64 + 29 judgments. Phase 5B ghi Phase 5C chưa bắt đầu là trạng thái lịch sử; 5C.1 này là synthesis mới, không sửa trạng thái trong nguồn.

Tier A = controlled/frozen artifacts (không đồng nghĩa mọi historical comparison là causal); Tier B = observational traces; Tier C = diagnostic hypothesis. F7 dùng sealed traces nhưng phát biểu về hành vi nên xếp B. F2 dựa trên frozen point audit nên xếp A cho mô tả đếm, không nâng taxonomy thành thử nghiệm nhân quả. Confidence áp dụng cho allowed claim, không cho mọi suy diễn của finding.

Kiểm kê trước bao phủ mọi preexisting regular file dưới project root, kể cả môi trường và hidden files; symlink ghi đích, không theo ra ngoài. Không có usable Git working tree. Đối chiếu local SHA-256, canonical production/source bindings, stored point transitions và sealed R2 traces; không import project modules. Chi tiết nguồn/hash ở [phase5c1_manifest_v0.json](phase5c1_manifest_v0.json).

## 2. Research timeline

Bảng mở đầu thể hiện đường đi: corpus cố định → localization tốt nhưng thiếu full evidence → Standard bỏ ý → conditional agent → trace mismatch → controlled ablation giới hạn attribution → hypothesis ngoài benchmark. Không gộp các tầng bằng chứng.

## 3. Standard RAG findings

### F1 — Localization tương đối mạnh; retrieval chưa được giải quyết hoàn toàn

| Measurement / denominator | Frozen value |
| --- | --- |
| Union any-gold chunk coverage / 31 queries | 0.967741935484 |
| Union full-gold chunk coverage / 31 queries | 0.709677419355 |
| Union macro / micro candidate chunk recall | 0.842549923195 / 0.785714285714 |
| Union article any / full coverage | 0.967741935484 / 0.967741935484 |
| Reranker article Hit@5 | 0.967741935484 |
| Reranker exact chunk Hit@5 / Recall@5 | 0.935483870968 / 0.623911930364 |
| Generation point annotated support: candidate / Top-5 | 81/102 / 53/102 |

Candidate union là BM25@20 ∪ Dense@20 unranked; final RAG dùng reranked Top-5, không dùng RRF và không biến upper bound thành measured reranker quality. Retrieval denominator có 98 query-scoped gold chunk occurrences; generation có 102 required points. Article localization không bảo đảm đủ khoản/điểm hoặc synthesis. Nguồn: [candidate-union-v0_metrics.json](../../../results/candidate-union-v0_metrics.json), [bge-reranker-v2-m3-v0_metrics.json](../../../results/bge-reranker-v2-m3-v0_metrics.json).

### F2 — Failures không chỉ nằm ở retrieval

| Primary point failure | Count / 102 |
| --- | --- |
| retrieval_miss | 16 |
| evidence_coverage | 17 |
| answer_generation | 9 |
| citation | 4 |
| none | 56 |

Standard hỗ trợ 60/102 điểm, thiếu 42/102. Có 9/102 điểm mà Top-5 chứa toàn bộ annotated support nhưng answer vẫn bỏ ý. Đây là căn cứ trực tiếp cho Completeness-aware Answer Revision. Query/point identities: eval001/P1, eval001/P2, eval002/P2, eval005b/P4, eval014/P1, eval014/P4, eval022/P1, eval030/P1, eval030/P3.

28/102 points mất sufficient annotated support từ candidate → Top-5 là overlap diagnostic trên mọi điểm; 17/102 primary evidence-coverage failures là taxonomy của outcome. Không đồng nhất hai số. Citation 4 + no failure 56 = 60 supported points; 42 missing points thuộc 16 retrieval + 17 evidence + 9 generation. Primary causes là mutually exclusive, secondary causes thì không. Số partial points không xác định riêng từ binary labels.

Đối chiếu phát hiện một cách diễn đạt không nhất quán trong report 4A: câu “pure retrieval miss is smaller” không được dùng để nói 16 nhỏ hơn 9. Bảng/JSON/point rows là authority cho các con số; nguồn cũ giữ nguyên byte. Nguồn: [failure_analysis_metrics_v0.json](../../failure_analysis_metrics_v0.json) và [failure_analysis_points_v0.jsonl](../../failure_analysis_points_v0.jsonl).

## 4. Agentic v1 findings

### F3 — Historical improvement, đặt ngay cạnh replication

| Run | AC macro | AC micro | Interpretation |
| --- | --- | --- | --- |
| R0 | 0.675268817204 | 60/102 = 0.588235294118 | Historical Standard |
| R1 | 0.723655913978 | 65/102 = 0.637254901961 | Historical Agentic |
| R2 | 0.696774193548 | 63/102 = 0.617647058824 | Same-configuration replication |

R0→R1 Δ macro 0.048387096774; +5 net points (gained 6, lost 1). Ngay cạnh đó, R1→R2 Δ macro -0.026881720430, net -2. Không quy historical gain cho một mechanism hay coi R1 là guaranteed performance.

| Metric | R0 macro | R1 macro | R0 pooled raw | R1 pooled raw |
| --- | --- | --- | --- | --- |
| Citation completeness | 0.675268817204 | 0.723655913978 | 60/102 | 65/102 |
| Citation correctness | 0.961290322581 | 0.982795698925 | 83/86 | 92/94 |
| Groundedness | 0.961290322581 | 0.966666666667 | 83/86 | 93/97 |
| Unsupported claim rate ↓ | 0.038709677419 | 0.033333333333 | 3/86 | 4/97 |
| Citation syntax validity | 0.967741935484 | 1.000000000000 | 30/31 | 31/31 |

R1 macro safety nhìn thuận hơn nhưng pooled Groundedness 83/86→93/97 giảm, pooled UCR 3/86→4/97 tăng. Claim denominators khác nhau, không phải paired claim effects. Syntax validity tách khỏi semantic correctness; eval012 sửa được syntax trong R1 dù không dùng Citation Revision, nên không quy cải thiện này cho citation repair.

R0 configured logical cost = 31 retrieval + 31 generation calls, không có measured HTTP ledger. R1 recorded trace cost = 38 retrieval + 108 production LLM calls, thêm 6 merge-reranks; overhead +22.58% retrieval và +248.39% LLM. Evaluator attempts không tính vào production. Không có token/currency/latency ledger đầy đủ để kết luận monetary cost. Nguồn: [agentic_trace_analysis_metrics_v0.json](../../agentic_trace_analysis_metrics_v0.json), [standard_rag_metrics_v0.json](../../standard_rag_metrics_v0.json), [efficiency_v0.json](../phase5b2f_v0/efficiency_v0.json).

## 5. Replication findings

### F4 — Same-configuration stochastic variation là material

| Transition R1→R2 | Count |
| --- | --- |
| Gained | 1 |
| Lost | 3 |
| Net | -2 |
| Gross churn | 4 |

Gained: eval027/P4. Lost: eval002/P2, eval022/P2, eval026/P1. Gross churn giữ lại chuyển động bị che bởi net. Một single production run không đủ để coi mọi chênh lệch nhỏ là mechanism effect. Đây là một observed replication, không phải variance estimate, noise distribution, stochasticity CI hay số để trừ khỏi ablation delta.

| Metric | R1 macro | R2 macro | Δ R2−R1 macro | R1 pooled raw | R2 pooled raw |
| --- | --- | --- | --- | --- | --- |
| citation_correctness | 0.982795698925 | 0.935483870968 | -0.047311827957 | 92/94 | 82/85 |
| groundedness | 0.966666666667 | 0.935483870968 | -0.031182795699 | 93/97 | 84/87 |
| unsupported_claim_rate | 0.033333333333 | 0.064516129032 | 0.031182795699 | 4/97 | 3/87 |
| citation_syntax_validity | 1.000000000000 | 1.000000000000 | 0.000000000000 | 31/31 | 31/31 |

Groundedness macro giảm nhưng pooled tăng; UCR macro tăng nhưng pooled giảm. Citation correctness giảm ở cả hai. Provider/backend, generation variation và semantic judge variation chưa tách được. Nguồn: [replication_R1_R2.json](../phase5b2f_v0/replication_R1_R2.json); [point_transitions_R1_R2.jsonl](../phase5b2f_v0/point_transitions_R1_R2.jsonl).

## 6. Answer Revision evidence

### F5 — Descriptive positive signal

| Scope | Queries / points | R2 macro AC | A1 macro AC | R2 supported | A1 supported |
| --- | --- | --- | --- | --- | --- |
| Full set | 31 / 102 | 0.696774193548 | 0.662365591398 | 63/102 | 59/102 |
| R2_used_false | 27 / 83 | 0.716049382716 | 0.716049382716 | 54/83 | 54/83 |
| R2_used_true | 4 / 19 | 0.566666666667 | 0.300000000000 | 9/19 | 5/19 |

Full-set micro: R2 0.617647058824; A1 0.578431372549. Δ R2−A1: macro 0.034408602151; micro 0.039215686275. All quality deltas use R2−ablation; positive raw UCR favors ablation.

| Point transition | Count |
| --- | --- |
| both_supported | 59 |
| neither_supported | 39 |
| only_A1 | 0 |
| only_R2 | 4 |
| gross churn | 4 |
| net R2 contribution | 4 |

Changed point identities: {"only_A1": [], "only_R2": [{"point_id": "P4", "query_id": "eval005b"}, {"point_id": "P3", "query_id": "eval013"}, {"point_id": "P4", "query_id": "eval013"}, {"point_id": "P2", "query_id": "eval029"}]}.

R2-triggered query IDs: eval005b, eval007, eval013, eval029. Triggered strata are descriptive post-treatment subsets, not randomized causal subgroups. Stochastic trigger disagreements: eval007.

Frozen paired bootstrap 95% CI [0.000000000000, 0.079569892473], observed mean 0.034408602151; 10000 paired-query resamples, seed 20260906, n=31. Chỉ đọc artifact bootstrap có sẵn. CI mô tả query-sampling uncertainty, không generation/judge stochasticity; không p-value hoặc significance claim.

Replication-attribution macro/net flag = false; separate gross-churn flag = true. Frozen interpretation: **Insufficient evidence**. Giữ precedence Phase 5A §10; research planning status không thay frozen label.

| Safety metric | R2 macro | A1 macro | R2 pooled raw | A1 pooled raw |
| --- | --- | --- | --- | --- |
| citation_correctness | 0.935483870968 | 0.967741935484 | 82/85 | 75/77 |
| groundedness | 0.935483870968 | 0.967741935484 | 84/87 | 75/78 |
| unsupported_claim_rate | 0.064516129032 | 0.032258064516 | 3/87 | 3/78 |

Nguồn: [contrast_R2_A1.json](../phase5b2f_v0/contrast_R2_A1.json), [bootstrap_R2_A1.json](../phase5b2f_v0/bootstrap_R2_A1.json), [point_transitions_R2_A1.jsonl](../phase5b2f_v0/point_transitions_R2_A1.jsonl), [efficiency_v0.json](../phase5b2f_v0/efficiency_v0.json).

**Evidence ủng hộ giữ revision làm candidate:** only-R2=4, only-A1=0; 3 queries tốt hơn, 28 bằng, không query AC giảm; cả 4 gained points nằm trong 4 R2-used queries. Triggered 9/19 vs 5/19, trong khi 27 non-used queries 54/83 vs 54/83. Phase 4A xác nhận generation omission là failure class có thật. Điều này ủng hộ tiếp tục nghiên cứu chức năng revision, chưa chứng minh nên giữ nguyên policy.

**Evidence chống khẳng định chắc contribution:** replication churn 4 bằng contrast churn 4 kích hoạt safeguard dù macro/net flag false; CI chạm zero; 4 triggered queries; safety conflicts. Citation correctness và macro groundedness/UCR thuận A1, pooled groundedness/UCR thuận R2. eval007 dùng revision ở R2 nhưng A1 checker không muốn trigger; không phải cùng một draft được randomize.

**Cost:** R2 101 vs A1 94 production LLM calls; A1 tiết kiệm 7 (6.930693%). Bốn R2 revision branches gồm 4 repair + 4 dependent rechecks = 8 calls; A1 có một citation repair ở eval012 ngoài nhóm used, khiến net full-set saving là 7. Retrieval 42 vs 42; merge-rerank 9 vs 11 (A1 nhiều hơn 2 do run-path variation). Không biến 7 thành fixed cost mỗi revision.

**Recommendation: INVESTIGATE_BEFORE_IMPLEMENTATION (V2-R1).** Giữ Completeness-aware Answer Revision trong requirements research; chưa đủ cơ sở KEEP_AS_IS như một contribution đã xác nhận. Cần thiết kế đo recovery, safety và cost độc lập trước implementation.

## 7. Evidence Expansion evidence

### F6 — Weak aggregate contribution

| Scope | Queries / points | R2 macro AC | A2 macro AC | R2 supported | A2 supported |
| --- | --- | --- | --- | --- | --- |
| Full set | 31 / 102 | 0.696774193548 | 0.696774193548 | 63/102 | 62/102 |
| R2_used_false | 22 / 66 | 0.799242424242 | 0.833333333333 | 49/66 | 51/66 |
| R2_used_true | 9 / 36 | 0.446296296296 | 0.362962962963 | 14/36 | 11/36 |

Full-set micro: R2 0.617647058824; A2 0.607843137255. Δ R2−A2: macro 0.000000000000; micro 0.009803921569. All quality deltas use R2−ablation; positive raw UCR favors ablation.

| Point transition | Count |
| --- | --- |
| both_supported | 59 |
| neither_supported | 36 |
| only_A2 | 3 |
| only_R2 | 4 |
| gross churn | 7 |
| net R2 contribution | 1 |

Changed point identities: {"only_A2": [{"point_id": "P1", "query_id": "eval022"}, {"point_id": "P2", "query_id": "eval022"}, {"point_id": "P1", "query_id": "eval026"}], "only_R2": [{"point_id": "P4", "query_id": "eval007"}, {"point_id": "P1", "query_id": "eval014"}, {"point_id": "P2", "query_id": "eval014"}, {"point_id": "P4", "query_id": "eval014"}]}.

R2-triggered query IDs: eval001, eval005a, eval005b, eval006, eval011, eval013, eval014, eval016, eval023. Triggered strata are descriptive post-treatment subsets, not randomized causal subgroups. Stochastic trigger disagreements: eval005b, eval011, eval029.

Frozen paired bootstrap 95% CI [-0.064516129032, 0.072580645161], observed mean 0.000000000000; 10000 paired-query resamples, seed 20260906, n=31. Chỉ đọc artifact bootstrap có sẵn. CI mô tả query-sampling uncertainty, không generation/judge stochasticity; không p-value hoặc significance claim.

Replication-attribution macro/net flag = true; separate gross-churn flag = false. Frozen interpretation: **Insufficient evidence**. Giữ precedence Phase 5A §10; research planning status không thay frozen label.

| Safety metric | R2 macro | A2 macro | R2 pooled raw | A2 pooled raw |
| --- | --- | --- | --- | --- |
| citation_correctness | 0.935483870968 | 0.967741935484 | 82/85 | 86/87 |
| groundedness | 0.935483870968 | 0.959677419355 | 84/87 | 86/88 |
| unsupported_claim_rate | 0.064516129032 | 0.040322580645 | 3/87 | 2/88 |

Nguồn: [contrast_R2_A2.json](../phase5b2f_v0/contrast_R2_A2.json), [bootstrap_R2_A2.json](../phase5b2f_v0/bootstrap_R2_A2.json), [point_transitions_R2_A2.jsonl](../phase5b2f_v0/point_transitions_R2_A2.jsonl), [efficiency_v0.json](../phase5b2f_v0/efficiency_v0.json).

**Có giúp ở triggered queries?** Có descriptive positive signal: 14/36 vs 11/36 ở 9 R2-used queries; 3 gained points đều ở eval014. Không chứng minh causal effect: stratum post-treatment và checks/generation vẫn stochastic. Ở 22 non-used queries, R2 49/66 vs A2 51/66; only-R2 eval007/P4, only-A2 eval022/P1,P2 và eval026/P1. Không quy các thay đổi non-used cho removal của expansion.

**Aggregate cải thiện?** Macro AC bằng nhau; R2 63/102 vs 62/102 chỉ net +1, only-R2 4 và only-A2 3, gross churn 7. A2 có safety summaries tốt hơn. Source conflict list trống vì classifier dùng các tiêu chí frozen; báo cáo này vẫn phơi bày macro tie, micro +1 và safety tradeoff mà không relabel.

**Overhead:** R2 retrieval 42 vs A2 31: saving 11 (26.190476%); merge-rerank 9 vs 0: saving 9; production LLM 101 vs 101: no LLM saving. Triggered LLM 31 vs 30 được bù bởi non-used 70 vs 71, nên không suy ra mọi per-query LLM cost bằng nhau.

**Stochastic confounding:** macro/net replication flag true (|0| ≤ |−0.026881720430| và |1| ≤ |−2|); gross-churn flag false (4 < 7). Bootstrap spans both signs; checker disagreement tại eval005b, eval011, eval029. Phase 4E bổ sung observation: 5/6 R1 expansions không đổi Top-5, không thêm annotated supporting chunks; đó là Tier B, không phủ định mọi expansion.

**Recommendation: INVESTIGATE_BEFORE_IMPLEMENTATION (V2-R4).** Đưa selectivity/value criteria vào design research; chưa chọn policy cụ thể, không tăng retrieval rounds và không kết luận Expansion unnecessary.

## 8. Controller/self-check findings

### F7 — Usage trên sealed R2 traces

| Intervention | Used / 31 | Rate | Query IDs |
| --- | --- | --- | --- |
| revision_used | 4/31 | 0.129032258065 | eval005b, eval007, eval013, eval029 |
| expansion_used | 9/31 | 0.290322580645 | eval001, eval005a, eval005b, eval006, eval011, eval013, eval014, eval016, eval023 |
| citation_revision_used | 0/31 | 0.000000000000 | None |

Đã đối chiếu từng R2 trace trên disk với embedded canonical record và production binding. Citation revision R2 = 0/31; historical R1 = 1/31. Answer revision R1 = 7/31 và expansion R1 = 6/31, khác R2. Many queries were resolved without invoking the corresponding intervention; ở đây “resolved” chỉ nghĩa controller đã trả output, không nghĩa benchmark-complete. Usage thấp không chứng minh ineffective; không gắn nhãn cả benchmark “easy”.

### F8 — Tier B completeness calibration mismatch

| Internal completeness (last retained check) | Benchmark complete | Benchmark incomplete |
| --- | --- | --- |
| complete=true | 13 | 17 |
| complete=false | 1 | 0 |

Tổng 31. Internal complete=true có 17/30 benchmark-incomplete; controller success có 15/28 benchmark-incomplete. Hai tập không đồng nhất: eval001/014 có internal complete nhưng status insufficient_evidence. eval010 internal incomplete nhưng benchmark-complete. Controller `success` không đồng nghĩa benchmark-complete.

False-success status query IDs: eval004, eval005a, eval005b, eval007, eval008, eval011, eval013, eval016, eval018, eval022, eval023, eval025, eval027, eval028, eval030.

Đây là calibration mismatch đã quan sát, không tự động là software bug. Internal checks dựa vào query/evidence còn benchmark dùng frozen required points. Initial checks bị overwritten trong bảy R1 revision cases; eval005b check cuối diễn ra trước citation edit. Không invent intermediate missing-point labels hoặc benchmark draft scores. Nguồn: [agentic_trace_analysis_metrics_v0.json](../../agentic_trace_analysis_metrics_v0.json) và [agentic_trace_analysis_v0.jsonl](../../agentic_trace_analysis_v0.jsonl).

## 9. Exploratory chatbot diagnostic

**EXPLORATORY / NON-BENCHMARK / NON-CONFIRMATORY — Tier C.** Query: Tôi muốn xây dựng một chatbot y tế, tôi cần lưu ý điều gì. Không thuộc 31-query benchmark, không có benchmark score và không được dùng để sửa kết luận Phase 5. Nguồn duy nhất: [agentic-rag-v1_20260909T132915.670264Z.json](../../../../rag/traces/agentic-rag-v1_20260909T132915.670264Z.json). Đây là phân tích trace, không phải tư vấn pháp lý/y tế hay xác minh hiệu lực văn bản.

### F9 — Chuỗi observation được xác minh

| Stage | Observed trace content |
| --- | --- |
| Missing aspects | Quy định chi tiết về trách nhiệm pháp lý và nghĩa vụ cụ thể của đơn vị phát triển chatbot y tế<br>Yêu cầu kỹ thuật và tiêu chuẩn kiểm thử đối với hệ thống trí tuệ nhân tạo trong lĩnh vực y tế |
| Subqueries | Quy định chi tiết về trách nhiệm pháp lý và nghĩa vụ cụ thể của đơn vị phát triển chatbot y tế Tôi muốn xây dựng một chatbot y tế, tôi cần lưu ý điều gì<br>Yêu cầu kỹ thuật và tiêu chuẩn kiểm thử đối với hệ thống trí tuệ nhân tạo trong lĩnh vực y tế Tôi muốn xây dựng một chatbot y tế, tôi cần lưu ý điều gì |
| Expansion | expansion_used=true; 2 subqueries; final Top-5 thêm E58, E6, E26 so với initial Top-5 |
| Draft | Chỉ nêu an toàn bệnh nhân, độ tin cậy và bảo vệ dữ liệu sức khỏe [E1] |
| Revision | revision_used=true; answer thêm cơ chế giám sát thực chất của con người [E58] |
| Final answer | Cites E1, E58; E6, E2, E26 không được trích dẫn và các nội dung đặc thù của chúng không được nêu |
| Final completeness | complete=true; missing_points=[]; reason chỉ nhắc E1 và E58; final_status=success |

| New final evidence | Relation to detected gap | Answer usage / caveat |
| --- | --- | --- |
| E58 — 142-2026-ND-CP_dieu-8_khoan-2_diem-b | Human oversight technical/operational mechanism; relevance to technical aspect | Added by revision. Context is criteria for high-risk list; do not infer unconditional application to all chatbots. |
| E6 — 142-2026-ND-CP_dieu-43_khoan-1 | Sector authorities establish detailed safety/risk/deployment standards; partial relation to missing technical standards | Not used; regulator duty, not concrete medical testing standard or direct developer duty. |
| E26 — 142-2026-ND-CP_dieu-16_khoan-4 | Limits on mandatory disclosure by providers/deployers when explaining/providing information; partial relation to legal duties | Not used; not a complete catalogue of developer obligations. |

E6/E26 cung cấp nội dung có liên quan một phần đến missing aspects nhưng answer không mang nội dung đó sang hoặc nói rõ phần còn chưa giải quyết. Không có căn cứ nói chúng đã đáp ứng đầy đủ missing aspects. Việc không cite mọi chunk tự nó không là lỗi; E2 cũng có thể không cần cho câu hỏi xây dựng chatbot. Revision thực sự mang E58 vào answer là counterevidence đối với giả thuyết “agent bỏ toàn bộ mục tiêu”.

**Exploratory observation suggests a possible goal-persistence / evidence-to-answer coverage gap.** Mạnh hơn mức này là không được hỗ trợ. Final complete=true không có independent gold để chấm lại. Initial completeness payload không được lưu riêng; transition ghi hai checks nhưng không phục hồi được nguyên văn lý do trigger revision. Chỉ hypotheses/candidate V2-R3; **requires confirmation on a separately designed challenge set**. Không có medical rule, prompt sửa riêng hoặc subquery template riêng cho query này.

## 10. Retrieval vs generation vs controller limitations

| Limitation | Definition | Evidence / boundary |
| --- | --- | --- |
| Retrieval / final-evidence coverage | Evidence cần thiết không vào candidate hoặc final evidence | F1/F2: 81/102 candidate sufficient → 53/102 Top-5; distinguish candidate miss from selection loss. No evidence that all legal detail exists in corpus. |
| Generation | Relevant supporting evidence present but answer omits its proposition | F2: 9 frozen points; F5 positive but insufficient attribution. F9 only partial related evidence, not confirmed omission gold. |
| Controller/self-check | Sufficient/complete/stop decision does not track intended completeness | F8: Tier B mismatch. F9: Tier C possible missing-aspect carry-through gap, separately unconfirmed. |

Một query có thể có nhiều limitation; không sửa taxonomy frozen hoặc coi mọi unsupported claim là retrieval miss. Relevance, applicability, sufficient support, citation usage và answer coverage là các quan hệ khác nhau.

## 11. Candidate Agentic v2 requirements

Chỉ behavior/evaluation requirements, không thiết kế implementation. Mỗi requirement có đúng một decision class; research design readiness không có nghĩa implementation readiness.

### V2-R1

Problem: Generation omission; Completeness-aware Answer Revision

Evidence: F2, F5

Evidence tier: A

Current behavior: Có evidence nhưng bỏ ý; current revision có descriptive positive signal, frozen label Insufficient evidence.

Desired behavior: Revision có mục tiêu phục hồi các ý liên quan được evidence hỗ trợ, bảo toàn grounding/citation và báo phần chưa giải quyết.

Why justified: 9 omission points ở R0; R2-used stratum 9/19 so với 5/19.

Known risk: Checker sai hoặc revision thêm claim unsupported; chi phí tăng.

How to evaluate later: Predeclare separate development/challenge evaluation, frozen historical reporting, draft/final completeness and safety, repeated paired runs and call budgets; no tuning on the 31 queries.

Status: INVESTIGATE_BEFORE_IMPLEMENTATION

### V2-R2

Problem: Weak completeness/self-check calibration; Evidence-aware completeness verification

Evidence: F8

Evidence tier: B

Current behavior: Internal complete=true có thể đi cùng benchmark-incomplete; 15 controller success chưa complete.

Desired behavior: Quyết định complete/success phản ánh phạm vi evidence và các ý được trả lời, phân biệt insufficient evidence với omitted supported content.

Why justified: Frozen Phase 4E mismatch có 17 trường hợp, nên đủ lý do refine requirement.

Known risk: Checker quá bảo thủ, lặp sửa không cần thiết hoặc học lén gold; internal check không thể giả định biết benchmark labels.

How to evaluate later: On separately designed cases, predeclare calibration matrix and stop-status definitions, preserve each check/answer stage; benchmark labels stay evaluator-side.

Status: REFINE

### V2-R3

Problem: Possible goal persistence from missing aspect → evidence → answer

Evidence: F9

Evidence tier: C

Current behavior: Missing aspects dẫn tới subqueries, final evidence mở rộng nhưng final check chỉ mô tả những ý đã có trong answer.

Desired behavior: Mỗi aspect đã nêu cần có kết cục rõ: được trả lời có hỗ trợ, chưa đủ evidence, hoặc ngoài phạm vi với lý do.

Why justified: Một diagnostic gợi ý khoảng trống; chưa xác nhận thành problem tổng quát.

Known risk: Ép trả lời mọi aspect tự sinh, đưa evidence không áp dụng vào answer hoặc overfit domain y tế.

How to evaluate later: requires confirmation on a separately designed challenge set; cross-domain aspect-to-evidence-to-answer review with explicit relevance/applicability, without hardcoded medical rules.

Status: INVESTIGATE_BEFORE_IMPLEMENTATION

### V2-R4

Problem: Evidence Expansion efficiency; More selective / higher-value expansion policy

Evidence: F1, F6, F7

Evidence tier: A, B

Current behavior: 9/31 R2 expansions; 11 additional retrievals and 9 merge-reranks; macro AC tie with A2.

Desired behavior: Expansion chỉ nên tiêu thêm công khi có cơ sở kỳ vọng bổ sung evidence liên quan và cải thiện answer, với budget và lợi ích quan sát được.

Why justified: Weak aggregate contribution relative to measured retrieval work justifies examining selectivity, not deleting expansion.

Known risk: Trigger quá chặt bỏ lỡ evidence phân tán; trigger quá rộng tốn công; one-run differences confound effects.

How to evaluate later: Future predeclared comparison of evidence gains/losses, final point support, calibration, safety and retrieval/merge cost on independent cases and repeated runs. No automatic increase in retrieval rounds.

Status: INVESTIGATE_BEFORE_IMPLEMENTATION

### V2-R5

Problem: Hard-query evaluation gap; Separate challenge/hard-query benchmark

Evidence: F1, F2, F4, F7, F8, F9

Evidence tier: A, B, C

Current behavior: Current frozen 31 queries give historical evidence but limited observed mechanism exposures; one broad exploratory query has no gold.

Desired behavior: Thiết kế dataset riêng cho broad/open-ended, multi-aspect, multi-article, dispersed evidence, initial Top-5 partial, synthesis, omission risk và decomposition/reformulation opportunity.

Why justified: Đủ lý do mở rộng phạm vi đánh giá nghiên cứu; không chứng minh benchmark hiện tại easy.

Known risk: Selection theo lỗi v1, contamination từ chatbot diagnostic, tối ưu riêng challenge hoặc thay benchmark lịch sử.

How to evaluate later: Predeclare dataset, annotation/applicability criteria, splits, metrics and repeated-run protocol before running v2; retain frozen 31 as primary historical benchmark. No dataset created in 5C.1.

Status: INVESTIGATE_BEFORE_IMPLEMENTATION

### V2-R6

Problem: Historical comparability and stochastic attribution

Evidence: F3, F4, F5, F6

Evidence tier: A

Current behavior: R1→R2 shows material variation; frozen precedence safeguards block stronger labels.

Desired behavior: Giữ frozen historical benchmark, provenance, paired point transitions, macro/micro safety, separate call ledgers và predeclared attribution rules; future design must account for repeated runs.

Why justified: Traceability and replication prevent interpreting small single-run differences as proven contribution.

Known risk: Cost of future repeated runs; retrospective selection or changing labels from new outcomes.

How to evaluate later: Audit protocol/design before future execution; show all runs and query-sampling vs generation/judge uncertainty separately.

Status: KEEP_AS_IS

## 12. Hard-query evaluation need

**Research justification: YES — sufficient to DESIGN a separate challenge set.** F1/F2 chứng minh có evidence/coverage/omission limitations; F4 cho thấy cần nghiên cứu uncertainty; F7 cho thấy số lần quan sát mỗi mechanism hữu hạn. F8 hỗ trợ kiểm tra completeness calibration. F9 chỉ tạo hypothesis, không chứng minh prevalence hoặc benchmark thiếu độ khó. Retrieval artifact hiện đã có 8 queries được gắn “hard”; không relabel chúng hoặc phủ nhận độ khó sẵn có.

Mục tiêu dataset tương lai: broad/open-ended queries; multi-aspect; multi-article; evidence dispersed; initial Top-5 partial; synthesis required; generation omission risk; query decomposition/reformulation opportunity. Đây là dimensions cần predeclare và annotate khi thiết kế, chưa chọn queries hay tạo gold/dataset trong 5C.1. Không chỉ tuyển câu hỏi v1 thất bại hoặc sao chép medical diagnostic thành bài thi v2.

**Current 31-query frozen benchmark remains the primary historical benchmark.** Challenge set sau này là dataset mới, tách development/test và khai báo trước khi chạy system v2; goals, scope/applicability, metrics, repeated-run analysis và cost accounting phải có trước kết quả. Không thay/loại bỏ/retune frozen 31 queries. Đây là evaluation requirement V2-R5, không là production mechanism hay lý do tự động thêm retrieval rounds.

## 13. Decision table

| Problem | Evidence | Strength | Candidate requirement | Ready for v2 design? |
| --- | --- | --- | --- | --- |
| Generation omission | F2, F5 | Tier A frozen omission evidence; revision contribution insufficient | V2-R1 — INVESTIGATE_BEFORE_IMPLEMENTATION | YES — hypothesis/validation design only |
| Weak completeness/self-check calibration | F8 | Tier B observational mismatch | V2-R2 — REFINE | YES — refine requirement, no implementation |
| Explicit missing-aspect carry-through gap | F9 | Tier C exploratory only | V2-R3 — INVESTIGATE_BEFORE_IMPLEMENTATION | YES — confirmation-study design only; problem unconfirmed |
| Evidence Expansion efficiency | F1, F6, F7 | Tier A weak aggregate result plus Tier B usage; no established causal utility | V2-R4 — INVESTIGATE_BEFORE_IMPLEMENTATION | YES — candidate criteria and validation design only |
| Hard-query evaluation gap | F1, F2, F4, F7, F8, F9 | A/B motivate evaluation coverage; C generates hypotheses only | V2-R5 — INVESTIGATE_BEFORE_IMPLEMENTATION | YES — evaluation requirement, not production mechanism |
| Attribution and historical comparability | F3, F4, F5, F6 | Tier A single replication plus frozen safeguards | V2-R6 — KEEP_AS_IS | YES — preserve research constraints |

Decision classes chỉ phục vụ research planning. V2-R1/V2-R3/V2-R4/V2-R5 cần INVESTIGATE_BEFORE_IMPLEMENTATION; V2-R2 REFINE phát biểu về calibration; V2-R6 KEEP_AS_IS đối với historical safeguards. A3/A4 và citation-only mechanism work: DEFER trong decision log vì không thuộc phạm vi và exposure quá ít; không tạo thêm v2 capability bằng suy đoán.

## 14. What is known

**Confirmed / relatively well-supported within frozen scope:** F1 localization mạnh hơn full evidence coverage; F2 generation omission cùng tồn tại với retrieval/evidence failures; F3 historical AC improvement và cost overhead là các số quan sát đã reconcile; F4 same-configuration point churn/safety drift có thật trong cặp R1/R2. F7 usage counts verified, F8 calibration mismatch consistently observed, nhưng hai findings này vẫn Tier B và không causal.

**Suggestive findings:** F5 descriptive positive revision signal ở used stratum; F6 expansion có triggered signal nhưng weak aggregate contribution và overhead. Cả hai frozen conclusions vẫn **Insufficient evidence**. Tier A của dữ liệu không xóa attribution safeguards.

**Exploratory findings:** F9 possible missing-aspect carry-through gap; evidence chỉ từ một ad-hoc trace, partly related evidence không đủ tạo confirmed omission. Revision cũng cho thấy một aspect được đưa vào answer.

## 15. What remains unknown

Contribution nào tồn tại ổn định qua production/judge repetitions? Revision recover supported omissions bao nhiêu so với added unsupported claims? Checker bỏ sót do missing evidence, incomplete goals hay đánh giá wording? Expansion tăng final evidence value khi nào và có đáng cost không? Goal persistence có tái diễn trên nhiều domains với applicable evidence không? Broad questions cần phạm vi/gold thế nào để “complete” không vô hạn? Những câu hỏi này cần thiết kế đánh giá mới; current data không cung cấp causal estimates, calibrated uncertainty, token cost hoặc benchmark-equivalent draft/final effects.

## 16. Limitations

31 queries/102 points là một frozen historical set, không đại diện mọi legal task. Query-sampling bootstrap không là generation/judge variance. Chỉ một R1→R2 replication; historical environment/provider provenance không đầy đủ. Triggered strata post-treatment, không randomized; không trừ replication delta. Macro và pooled safety có thể đi ngược chiều do denominator/claim composition. AC và citation completeness trùng nhau ở dữ liệu này không làm hai metrics độc lập. Annotated support overlap có thể bỏ sót alternatives; binary point labels không đo partial support. Corpus validation PASS là structural validation của 3 documents/737 chunks, không chứng minh toàn bộ pháp luật/medical requirements đã có. Unretained intermediate checks không thể tái tạo; unquoted evidence không tự động là omission. Tier C không có independent gold và chỉ được dùng tạo hypothesis. Không có usable Git provenance; local hash integrity chứng minh bytes unchanged từ snapshot trước, không là cryptographic signed execution attestation.

## 17. Recommendation for Phase 5C.2

**Is there sufficient research justification to proceed to Phase 5C.2 — Agentic v2 Requirements & Challenge-Set Design? YES.** Justification là các failure classes và calibration mismatches đã quan sát, coupled với attribution uncertainty cần được xử lý bằng design; không phải tuyên bố v2 chắc chắn tốt hơn. Phase 5C.2 chỉ DESIGN: cụ thể hóa requirements có traceability, tiêu chí challenge-set, predeclared evaluation và confirmation criteria. Không code, không tạo dataset trong 5C.1, không chạy benchmark/API/production/evaluator và không đổi controller. STOP.

Source registry và validation: [phase5c1_manifest_v0.json](phase5c1_manifest_v0.json), [phase5c1_validation_v0.json](phase5c1_validation_v0.json), [integrity_before_after_v0.json](integrity_before_after_v0.json). Full evidence/requirements: [phase5c1_evidence_matrix_v0.json](phase5c1_evidence_matrix_v0.json), [phase5c1_problem_requirement_map_v0.json](phase5c1_problem_requirement_map_v0.json).
