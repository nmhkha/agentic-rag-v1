# Phase 4A — Standard RAG Failure Analysis

## Executive Summary

Phase 3 reported macro Answer Completeness of **0.6753** across queries. At required-point level, **60/102** points were supported, giving micro completeness of **0.5882**. The difference exists because queries contain different numbers of required points. The result is analyzed as a read-only artifact; no corpus, benchmark, gold label, prompt, retriever, reranker, model, or Phase 3 result was modified.

The dominant primary causes are evidence coverage (**17 points**), answer generation (**9**), retrieval miss (**16**), and citation (**4**). The Top-5 bottleneck is measured separately from answer completeness.

## Dataset / System

- Ground truth: `generation-eval-v1`, status `verified`, 31 queries, 102 required points.
- Ground-truth SHA-256: `1795dbef913e63492c5cd6b8963c2f1a85642ddee0b1a42087f97203bc1895a4`
- Standard RAG result model: `gemini-3.5-flash-lite`
- Retrieval: `BM25-simple-v0@20 + dense-jina-v3-v0@20 union -> BAAI/bge-reranker-v2-m3`
- Prompt: `legal-rag-prompt-v0`
- Evidence: Top-5

## Aggregate Results

- Phase 3 macro Answer Completeness (query average): **0.6753**
- Point-level micro completeness: **60/102 = 0.5882**
- Fully supported points: **60/102**
- Partial points: **not separately identifiable**; the Phase 3 result stores only binary supported/unsupported labels. Unsupported points are conservatively counted as missing (**42**).
- Missing points: **42/102**
- Retrieval gold coverage is reported separately and is not Answer Completeness.

## Required-point Failure Taxonomy

| primary failure | points | percentage |
|---|---:|---:|
| Retrieval Miss | 16 | 0.1569 |
| Evidence Coverage | 17 | 0.1667 |
| Answer Generation | 9 | 0.0882 |
| Citation | 4 | 0.0392 |
| No Failure | 56 | 0.5490 |

Secondary causes are retained in the point matrix; retrieval/evidence failures with an uncovered answer point also record `answer_generation` as a secondary observed failure.

## Retrieval vs Evidence Coverage

- Candidate union had sufficient annotated evidence: **81/102**
- Top-5 retained sufficient annotated evidence: **53/102**
- Lost during reranking/Top-5 selection: **28/102**

A point is considered sufficient only when all of its annotated supporting chunk IDs are present. This uses the frozen point annotation; no unannotated alternative evidence was inferred.

## Generation Failures

Top-5 sufficient + answer incomplete: **9/102** points.
These are direct generation-limited points under the binary Phase 3 audit: the complete annotated support set was retained in Top-5, but the answer did not cover the proposition.

## Citation Failures

- Citation syntax valid: **30/31** queries.
- Syntax-invalid query IDs: `eval012`.
- Point-level citation statuses: `{"correct": 56, "incorrect": 4, "not_applicable": 42}`.
- Citation completeness and citation correctness are kept separate in the Phase 3 result; this analysis does not treat retrieved evidence as automatically correct citation.

## Worst Queries

### eval001

Query: Các mức phân loại rủi ro của hệ thống trí tuệ nhân tạo gồm những mức nào?

Answer Completeness: **0.0000**
Query taxonomy: **F. Mixed failure**
Root cause: **answer_generation**

Answer:

Bằng chứng hiện tại chưa đủ để kết luận toàn bộ các mức phân loại rủi ro của hệ thống trí tuệ nhân tạo, vì các văn bản cung cấp chỉ đề cập đến mức rủi ro cao [E3] và rủi ro trung bình [E1][E4].

| point | gold support | candidate status | Top-5 status | answer | citation | primary |
|---|---|---|---|---|---|---|
| P1 | 134-2025-QH15_dieu-9_khoan-1_diem-a | sufficient | sufficient | missing | not_applicable | answer_generation |
| P2 | 134-2025-QH15_dieu-9_khoan-1_diem-b | sufficient | sufficient | missing | not_applicable | answer_generation |
| P3 | 134-2025-QH15_dieu-9_khoan-1_diem-c | sufficient | insufficient | missing | not_applicable | evidence_coverage |

Conclusion: answer_generation is the main root cause under the primary point taxonomy.

### eval005a

Query: Nhà cung cấp hệ thống trí tuệ nhân tạo có rủi ro cao phải thực hiện những nghĩa vụ quản lý nào?

Answer Completeness: **0.0000**
Query taxonomy: **F. Mixed failure**
Root cause: **retrieval_miss**

Answer:

Nhà cung cấp hệ thống trí tuệ nhân tạo có rủi ro cao phải thực hiện các nghĩa vụ quản lý sau:
1. Phải thiết lập và duy trì hệ thống quản lý rủi ro đối với hệ thống do mình cung cấp sao cho phù hợp với mục đích sử dụng, phạm vi triển khai và mức độ rủi ro của hệ thống [E1].
2. Cung cấp cho bên triển khai các thông tin cần thiết về mục đích sử dụng, điều kiện vận hành an toàn, các rủi ro đã được xác định và biện pháp quản lý rủi ro tương ứng [E4].
3. Đối với nhà cung cấp nước ngoài có hệ thống trí tuệ nhân tạo có rủi ro cao cung cấp tại Việt Nam, phải có đầu mối liên hệ hợp pháp tại Việt Nam; và phải có hiện diện thương mại hoặc đại diện được ủy quyền tại Việt Nam nếu hệ thống thuộc diện bắt buộc chứng nhận sự phù hợp trước khi đưa vào sử dụng [E5].

| point | gold support | candidate status | Top-5 status | answer | citation | primary |
|---|---|---|---|---|---|---|
| P1 | 134-2025-QH15_dieu-14_khoan-1_diem-a | insufficient | insufficient | missing | not_applicable | retrieval_miss |
| P2 | 134-2025-QH15_dieu-14_khoan-1_diem-b | insufficient | insufficient | missing | not_applicable | retrieval_miss |
| P3 | 134-2025-QH15_dieu-14_khoan-1_diem-c | insufficient | insufficient | missing | not_applicable | retrieval_miss |
| P4 | 134-2025-QH15_dieu-14_khoan-1_diem-d | insufficient | insufficient | missing | not_applicable | retrieval_miss |
| P5 | 134-2025-QH15_dieu-14_khoan-1_diem-đ | sufficient | insufficient | missing | not_applicable | evidence_coverage |
| P6 | 134-2025-QH15_dieu-14_khoan-1_diem-e | sufficient | insufficient | missing | not_applicable | evidence_coverage |
| P7 | 134-2025-QH15_dieu-14_khoan-1_diem-g | insufficient | insufficient | missing | not_applicable | retrieval_miss |

Conclusion: retrieval_miss is the main root cause under the primary point taxonomy.

### eval005b

Query: Bên triển khai hệ thống trí tuệ nhân tạo có rủi ro cao phải thực hiện những nghĩa vụ quản lý nào?

Answer Completeness: **0.0000**
Query taxonomy: **F. Mixed failure**
Root cause: **retrieval_miss**

Answer:

Bên triển khai hệ thống trí tuệ nhân tạo có rủi ro cao phải tổ chức quản lý rủi ro trong quá trình triển khai và vận hành hệ thống, với các điều kiện phù hợp với mục đích sử dụng, phạm vi triển khai, mức độ rủi ro và hướng dẫn kỹ thuật của nhà cung cấp [E1].

| point | gold support | candidate status | Top-5 status | answer | citation | primary |
|---|---|---|---|---|---|---|
| P1 | 134-2025-QH15_dieu-14_khoan-2_diem-a | insufficient | insufficient | missing | not_applicable | retrieval_miss |
| P2 | 134-2025-QH15_dieu-14_khoan-2_diem-b | insufficient | insufficient | missing | not_applicable | retrieval_miss |
| P3 | 134-2025-QH15_dieu-14_khoan-2_diem-c | insufficient | insufficient | missing | not_applicable | retrieval_miss |
| P4 | 134-2025-QH15_dieu-14_khoan-2_diem-d | sufficient | sufficient | missing | not_applicable | answer_generation |
| P5 | 134-2025-QH15_dieu-14_khoan-2_diem-đ | sufficient | insufficient | missing | not_applicable | evidence_coverage |
| P6 | 134-2025-QH15_dieu-14_khoan-2_diem-e | insufficient | insufficient | missing | not_applicable | retrieval_miss |

Conclusion: retrieval_miss is the main root cause under the primary point taxonomy.

### eval014

Query: Hồ sơ thông thường để tham gia cơ chế thử nghiệm có kiểm soát gồm những thành phần nào?

Answer Completeness: **0.0000**
Query taxonomy: **F. Mixed failure**
Root cause: **mixed**

Answer:

Bằng chứng hiện tại chưa đủ để liệt kê toàn bộ các thành phần của hồ sơ thông thường để tham gia cơ chế thử nghiệm có kiểm soát do các bằng chứng chỉ cung cấp một số thành phần rời rạc như đơn đề nghị theo Mẫu AI03a hoặc AI03b [E1][E2], đề án thử nghiệm [E3], và tài liệu mô tả năng lực kỹ thuật, nhân sự hoặc hạ tầng [E4].

| point | gold support | candidate status | Top-5 status | answer | citation | primary |
|---|---|---|---|---|---|---|
| P1 | 142-2026-ND-CP_dieu-24_khoan-2_diem-a | sufficient | sufficient | missing | not_applicable | answer_generation |
| P2 | 142-2026-ND-CP_dieu-24_khoan-2_diem-b | sufficient | insufficient | missing | not_applicable | evidence_coverage |
| P3 | 142-2026-ND-CP_dieu-24_khoan-2_diem-c | sufficient | insufficient | missing | not_applicable | evidence_coverage |
| P4 | 142-2026-ND-CP_dieu-24_khoan-2_diem-d | sufficient | sufficient | missing | not_applicable | answer_generation |

Conclusion: mixed is the main root cause under the primary point taxonomy.

### eval022

Query: Cơ quan quản lý có trách nhiệm gì đối với việc xây dựng và cập nhật dữ liệu mở phục vụ AI?

Answer Completeness: **0.0000**
Query taxonomy: **F. Mixed failure**
Root cause: **mixed**

Answer:

Bằng chứng hiện tại chưa đủ để kết luận cụ thể về trách nhiệm xây dựng và cập nhật "dữ liệu mở phục vụ AI" do các quy định trong bằng chứng đề cập đến việc xây dựng, cập nhật dữ liệu mở nói chung [E5] hoặc việc thu thập, tạo lập, bảo đảm chất lượng, gán nhãn, chuẩn hóa, quản lý, khai thác cơ sở dữ liệu phục vụ trí tuệ nhân tạo thuộc phạm vi quản lý [E1], chứ chưa làm rõ nghĩa vụ riêng biệt cho "dữ liệu mở phục vụ AI".

| point | gold support | candidate status | Top-5 status | answer | citation | primary |
|---|---|---|---|---|---|---|
| P1 | 142-2026-ND-CP_dieu-32_khoan-5_diem-a | sufficient | sufficient | missing | not_applicable | answer_generation |
| P2 | 142-2026-ND-CP_dieu-32_khoan-5_diem-b | sufficient | insufficient | missing | not_applicable | evidence_coverage |
| P3 | 142-2026-ND-CP_dieu-32_khoan-5_diem-c | insufficient | insufficient | missing | not_applicable | retrieval_miss |

Conclusion: mixed is the main root cause under the primary point taxonomy.

## Best Queries

### eval003

Query: Nhà cung cấp phải lập hồ sơ phân loại rủi ro vào thời điểm nào?

Answer Completeness: **1.0000**
Query taxonomy: **A. Mostly successful**
Root cause: **none**

Answer:

Nhà cung cấp phải lập hồ sơ phân loại rủi ro đối với hệ thống trí tuệ nhân tạo có rủi ro cao và hệ thống trí tuệ nhân tạo có rủi ro trung bình trước khi đưa hệ thống vào sử dụng [E1].

The point rows in the machine-readable matrix show whether success depended on candidate/Top-5 sufficiency and citation correctness.

### eval006

Query: Trách nhiệm minh bạch của nhà cung cấp hệ thống trí tuệ nhân tạo bao gồm những gì?

Answer Completeness: **1.0000**
Query taxonomy: **A. Mostly successful**
Root cause: **none**

Answer:

Trách nhiệm minh bạch của nhà cung cấp hệ thống trí tuệ nhân tạo bao gồm: thực hiện trách nhiệm minh bạch, thông báo, đánh dấu kỹ thuật và gắn nhãn hiển thị đối với hệ thống trí tuệ nhân tạo và nội dung do hệ thống tạo ra cho phù hợp với mục đích sử dụng, bối cảnh triển khai và mức độ rủi ro của hệ thống [E1]; bảo đảm hệ thống tương tác trực tiếp với con người được thiết kế và vận hành để người sử dụng nhận biết khi đang tương tác với hệ thống, trừ trường hợp pháp luật có quy định khác [E2]; bảo đảm các nội dung âm thanh, hình ảnh, video do hệ thống tạo ra được đánh dấu ở định dạng máy đọc theo quy định của Chính phủ [E3]; và duy trì thông tin minh bạch trong suốt quá trình cung cấp hệ thống, sản phẩm hoặc nội dung cho người sử dụng [E5].

The point rows in the machine-readable matrix show whether success depended on candidate/Top-5 sufficiency and citation correctness.

### eval009

Query: Hệ thống AI tương tác trực tiếp với con người phải được thiết kế theo yêu cầu gì?

Answer Completeness: **1.0000**
Query taxonomy: **A. Mostly successful**
Root cause: **none**

Answer:

Hệ thống trí tuệ nhân tạo tương tác trực tiếp với con người phải được thiết kế và vận hành để người sử dụng nhận biết khi đang tương tác với hệ thống, trừ trường hợp pháp luật có quy định khác [E1].

The point rows in the machine-readable matrix show whether success depended on candidate/Top-5 sufficiency and citation correctness.

### eval010

Query: Nhà cung cấp cần làm gì khi phát hiện sự cố liên quan đến hệ thống trí tuệ nhân tạo?

Answer Completeness: **1.0000**
Query taxonomy: **A. Mostly successful**
Root cause: **none**

Answer:

Khi phát hiện sự cố liên quan đến hệ thống trí tuệ nhân tạo, nhà cung cấp có trách nhiệm kịp thời phát hiện, khắc phục sự cố có khả năng gây tổn hại đến con người, tài sản, dữ liệu hoặc trật tự xã hội [E1]. Nhà cung cấp phải khẩn trương áp dụng biện pháp kỹ thuật để khắc phục, tạm dừng hoặc thu hồi hệ thống, đồng thời thông báo cho cơ quan có thẩm quyền [E2]; áp dụng các biện pháp kỹ thuật cần thiết để ngăn chặn, hạn chế và khắc phục hậu quả của sự cố [E4]; duy trì, lưu giữ nhật ký hệ thống, dữ liệu và thông tin liên quan đến sự cố để phục vụ việc xác minh, đánh giá và khắc phục sự cố; đồng thời gửi báo cáo chính thức về kết quả khắc phục sự cố cho cơ quan nhà nước có thẩm quyền trong thời hạn 15 ngày kể từ ngày nộp báo cáo sơ bộ [E3]. Ngoài ra, nhà cung cấp có trách nhiệm giải trình về mục đích sử dụng, nguyên lý hoạt động ở mức mô tả chức năng, dữ liệu đầu vào chủ yếu và biện pháp quản lý rủi ro, an toàn của hệ thống khi có yêu cầu của cơ quan nhà nước trong thanh tra, kiểm tra hoặc khi có dấu hiệu rủi ro hoặc sự cố [E5].

The point rows in the machine-readable matrix show whether success depended on candidate/Top-5 sufficiency and citation correctness.

### eval012

Query: Cơ quan nào quyết định chấp thuận tham gia cơ chế thử nghiệm có kiểm soát?

Answer Completeness: **1.0000**
Query taxonomy: **E. Citation-limited**
Root cause: **citation**

Answer:

Cơ quan nhà nước có thẩm quyền chấp thuận việc tham gia cơ chế thử nghiệm có kiểm soát bao gồm: Ủy ban nhân dân cấp tỉnh (đối với hệ thống trí tuệ nhân tạo cấp độ 1 hoặc cấp độ 2 triển khai trong phạm vi một tỉnh, thành phố trực thuộc trung ương) [E3]; Bộ, cơ quan ngang bộ (đối với hệ thống cấp độ 1 hoặc cấp độ 2 thuộc phạm vi quản lý và triển khai trên từ hai tỉnh trở lên, hoặc do cơ quan, tổ chức thuộc phạm vi quản lý trực tiếp triển khai) [E4]; và Bộ Công an (đối với hệ thống trí tuệ nhân tạo cấp độ 3, hoặc bộ quản lý ngành, lĩnh vực có phạm vi quản lý trực tiếp đối với hoạt động sử dụng chính trong trường hợp hệ thống thuộc phạm vi quản lý của nhiều bộ, cơ quan ngang bộ) [E5].

The point rows in the machine-readable matrix show whether success depended on candidate/Top-5 sufficiency and citation correctness.

## Best vs Worst Comparison

| dimension | best queries | worst queries |
|---|---:|---:|
| Number of required points | 2.20 | 4.60 |
| Evidence concentration (gold chunks/query) | 1.80 | 4.60 |
| Candidate gold coverage | 1.0000 | 0.6571 |
| Top-5 gold coverage | 1.0000 | 0.3333 |
| Generation completeness | 1.0000 | 0.0000 |
| Citation-issue queries | 1 | 0 |

These are descriptive aggregates of the selected best/worst sets, not causal proof. The exact per-query values are in `failure_analysis_queries_v0.json`.

## Root Causes

1. The largest point-level group is evidence coverage: annotated support exists in the candidate union but is not retained in Top-5.
2. A second large group is answer generation: Top-5 contains the complete annotated support set but the answer omits the proposition.
3. Pure retrieval miss is smaller and occurs only when the complete annotated support set is absent from the BM25@20 ∪ Dense@20 candidate union.
4. Citation failures are distinct from both retrieval and completeness; `eval012` has full point coverage but invalid declared/cited evidence alignment.

## Agentic RAG Requirements Derived from Evidence

These are behavior requirements only; no Agentic RAG was designed or implemented in Phase 4A.

### Requirement R1 — Evidence coverage check / targeted expansion

Evidence: **28/102** points had sufficient annotated evidence in the candidate union but not in Top-5. A coverage check could detect missing required propositions before generation and request targeted evidence expansion.

### Requirement R2 — Answer completeness self-check

Evidence: **9/102** points had sufficient Top-5 evidence but were absent from the answer. A post-generation point checklist/revision behavior is justified for this observed failure class.

### Requirement R3 — Query decomposition or reformulation only for retrieval misses

Evidence: **16/102** points had no complete annotated support set in the candidate union. This supports targeted reformulation/decomposition as a conditional behavior, not a default for every query.

### Requirement R4 — Citation alignment check

Evidence: **4/102** points were answer-supported but citation-problematic, and 1 query had syntax/declaration invalidity. A citation validation/revision behavior is justified separately from evidence retrieval.

## Limitations

- Candidate sufficiency is defined from the frozen annotated supporting chunk IDs; unannotated but legally adequate alternatives were not inferred.
- Phase 3 persisted binary point support only. Partial answer coverage cannot be recovered exactly, so unsupported points are labeled `missing` conservatively and partial count is reported as not separately identifiable.
- Semantic point and citation decisions are inherited from the Phase 3 structured audit; this phase does not re-judge answers or use outside legal knowledge.
- The result dataset has no Git commit because the project directory is not a Git working tree.

## Sanity Checks

- Queries analyzed: **31/31**
- Required points analyzed: **102/102**
- Candidate reconstruction mismatches: **0**
- Benchmark source files modified: **no**
- Generation ground truth modified: **no**
