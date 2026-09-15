# bge-reranker-v2-m3-v0 Failure Analysis

Diagnostic only; the frozen gold set and retrieval/reranking configuration were not changed.

## eval004

Query: Nhà cung cấp hệ thống AI rủi ro cao phải duy trì những biện pháp quản lý nào?

Taxonomy: **PARTIAL_CANDIDATE_COVERAGE**  
Interpretation: mixed failure: candidate coverage is incomplete and ranking may also limit recall  
Union gold: 2/6  
Reranker first gold rank: 1  
Hit@5: 1  
Recall@5: 0.166667

| rank | chunk_id | reranker_score | bm25_rank | dense_rank |
|---:|---|---:|---:|---:|
| 1 | `142-2026-ND-CP_dieu-15_khoan-1` | 6.188964 | 1 | 1 |
| 2 | `134-2025-QH15_dieu-14_khoan-1_diem-a` | 4.751915 | 2 | 7 |
| 3 | `142-2026-ND-CP_dieu-11_khoan-5` | 4.164655 | 7 | 5 |
| 4 | `134-2025-QH15_dieu-14_khoan-3` | 4.140761 |  | 3 |
| 5 | `134-2025-QH15_dieu-14_khoan-6` | 3.710024 | 4 | 8 |

---

## eval005a

Query: Nhà cung cấp hệ thống trí tuệ nhân tạo có rủi ro cao phải thực hiện những nghĩa vụ quản lý nào?

Taxonomy: **PARTIAL_CANDIDATE_COVERAGE**  
Interpretation: mixed failure: candidate coverage is incomplete and ranking may also limit recall  
Union gold: 2/7  
Reranker first gold rank: 7  
Hit@5: 0  
Recall@5: 0.000000

| rank | chunk_id | reranker_score | bm25_rank | dense_rank |
|---:|---|---:|---:|---:|
| 1 | `142-2026-ND-CP_dieu-15_khoan-1` | 6.862057 | 3 | 2 |
| 2 | `134-2025-QH15_dieu-14_khoan-3` | 6.351699 |  | 3 |
| 3 | `134-2025-QH15_dieu-14_khoan-5` | 6.253772 | 2 | 10 |
| 4 | `142-2026-ND-CP_dieu-15_khoan-3` | 6.123996 |  | 1 |
| 5 | `134-2025-QH15_dieu-14_khoan-6` | 5.764684 | 1 | 12 |

---

## eval005b

Query: Bên triển khai hệ thống trí tuệ nhân tạo có rủi ro cao phải thực hiện những nghĩa vụ quản lý nào?

Taxonomy: **PARTIAL_CANDIDATE_COVERAGE**  
Interpretation: mixed failure: candidate coverage is incomplete and ranking may also limit recall  
Union gold: 2/6  
Reranker first gold rank: 5  
Hit@5: 1  
Recall@5: 0.166667

| rank | chunk_id | reranker_score | bm25_rank | dense_rank |
|---:|---|---:|---:|---:|
| 1 | `142-2026-ND-CP_dieu-15_khoan-4` | 6.774661 | 2 | 2 |
| 2 | `134-2025-QH15_dieu-14_khoan-3` | 6.585158 | 13 | 5 |
| 3 | `134-2025-QH15_dieu-14_khoan-5` | 6.421985 | 1 | 14 |
| 4 | `134-2025-QH15_dieu-14_khoan-1_diem-đ` | 5.972978 | 3 |  |
| 5 | `134-2025-QH15_dieu-14_khoan-2_diem-d` | 5.639184 | 4 |  |

---

## eval007

Query: Nội dung do AI tạo ra phải được thông báo hoặc gắn nhãn như thế nào?

Taxonomy: **MULTI_CHUNK_COVERAGE**  
Interpretation: multi-chunk coverage failure within a five-result cutoff  
Union gold: 9/9  
Reranker first gold rank: 4  
Hit@5: 1  
Recall@5: 0.222222

| rank | chunk_id | reranker_score | bm25_rank | dense_rank |
|---:|---|---:|---:|---:|
| 1 | `142-2026-ND-CP_dieu-18_khoan-6` | 7.345581 | 1 | 1 |
| 2 | `142-2026-ND-CP_dieu-18_khoan-1` | 5.875829 | 2 | 2 |
| 3 | `142-2026-ND-CP_dieu-18_khoan-4_diem-d` | 4.389977 | 3 | 3 |
| 4 | `142-2026-ND-CP_dieu-18_khoan-5_diem-d` | 4.381055 | 11 | 18 |
| 5 | `142-2026-ND-CP_dieu-18_khoan-5_diem-b` | 4.269179 | 10 |  |

---

## eval011

Query: Cơ chế thử nghiệm có kiểm soát cho phép tổ chức, cá nhân được hưởng những cơ chế gì trong phạm vi thử nghiệm?

Taxonomy: **CANDIDATE_MISS**  
Interpretation: candidate-generation failure; not a reranker reasoning failure  
Union gold: 0/2  
Reranker first gold rank: not in Top-10  
Hit@5: 0  
Recall@5: 0.000000

| rank | chunk_id | reranker_score | bm25_rank | dense_rank |
|---:|---|---:|---:|---:|
| 1 | `142-2026-ND-CP_dieu-23_khoan-1` | 6.306210 | 2 | 2 |
| 2 | `142-2026-ND-CP_dieu-21_khoan-6` | 3.656868 | 13 |  |
| 3 | `142-2026-ND-CP_dieu-27_khoan-3` | 3.224338 | 3 | 20 |
| 4 | `142-2026-ND-CP_dieu-25_khoan-1_diem-b` | 3.029016 | 6 | 19 |
| 5 | `142-2026-ND-CP_dieu-26_khoan-2_diem-a` | 2.882030 | 5 | 16 |

---

## eval016

Query: Tổ chức hoặc cá nhân phải báo cáo gì trong quá trình thử nghiệm có kiểm soát?

Taxonomy: **MULTI_CHUNK_COVERAGE**  
Interpretation: multi-chunk coverage failure within a five-result cutoff  
Union gold: 5/5  
Reranker first gold rank: 1  
Hit@5: 1  
Recall@5: 0.400000

| rank | chunk_id | reranker_score | bm25_rank | dense_rank |
|---:|---|---:|---:|---:|
| 1 | `142-2026-ND-CP_dieu-25_khoan-4` | 6.139714 | 1 | 1 |
| 2 | `142-2026-ND-CP_dieu-25_khoan-1_diem-b` | 4.782024 | 3 | 4 |
| 3 | `142-2026-ND-CP_dieu-25_khoan-3_diem-b` | 4.731558 | 2 | 2 |
| 4 | `142-2026-ND-CP_dieu-25_khoan-1_diem-a` | 4.425781 | 5 | 3 |
| 5 | `142-2026-ND-CP_dieu-25_khoan-1_diem-c` | 4.062366 | 4 | 5 |

---

## eval021

Query: Những loại dữ liệu nào có thể được đưa vào cơ sở dữ liệu phục vụ trí tuệ nhân tạo?

Taxonomy: **MULTI_CHUNK_COVERAGE**  
Interpretation: multi-chunk coverage failure within a five-result cutoff  
Union gold: 3/3  
Reranker first gold rank: 2  
Hit@5: 1  
Recall@5: 0.333333

| rank | chunk_id | reranker_score | bm25_rank | dense_rank |
|---:|---|---:|---:|---:|
| 1 | `134-2025-QH15_dieu-17_khoan-5` | 5.416946 |  | 11 |
| 2 | `142-2026-ND-CP_dieu-32_khoan-1_diem-c` | 4.348154 |  | 4 |
| 3 | `134-2025-QH15_dieu-17_khoan-2` | 3.868177 | 5 | 3 |
| 4 | `142-2026-ND-CP_dieu-35_khoan-1` | 3.076549 | 19 | 2 |
| 5 | `142-2026-ND-CP_dieu-32_khoan-5_diem-a` | 3.061347 | 12 | 7 |

---

## eval022

Query: Cơ quan quản lý có trách nhiệm gì đối với việc xây dựng và cập nhật dữ liệu mở phục vụ AI?

Taxonomy: **PARTIAL_CANDIDATE_COVERAGE**  
Interpretation: mixed failure: candidate coverage is incomplete and ranking may also limit recall  
Union gold: 2/3  
Reranker first gold rank: 5  
Hit@5: 1  
Recall@5: 0.333333

| rank | chunk_id | reranker_score | bm25_rank | dense_rank |
|---:|---|---:|---:|---:|
| 1 | `142-2026-ND-CP_dieu-43_khoan-4` | 3.310117 | 6 | 7 |
| 2 | `142-2026-ND-CP_dieu-36_khoan-1` | 2.499109 | 20 | 16 |
| 3 | `142-2026-ND-CP_dieu-42_khoan-3` | 2.413505 | 5 | 1 |
| 4 | `134-2025-QH15_dieu-17_khoan-3` | 2.245725 | 2 | 8 |
| 5 | `142-2026-ND-CP_dieu-32_khoan-5_diem-a` | 2.191192 | 1 |  |

---

## eval025

Query: Khi ứng dụng AI trong quản lý nhà nước, cơ quan vận hành phải đánh giá tác động trong trường hợp nào?

Taxonomy: **MULTI_CHUNK_COVERAGE**  
Interpretation: multi-chunk coverage failure within a five-result cutoff  
Union gold: 7/7  
Reranker first gold rank: 2  
Hit@5: 1  
Recall@5: 0.285714

| rank | chunk_id | reranker_score | bm25_rank | dense_rank |
|---:|---|---:|---:|---:|
| 1 | `134-2025-QH15_dieu-27_khoan-3` | 4.462298 | 1 | 11 |
| 2 | `142-2026-ND-CP_dieu-20_khoan-2` | 3.958962 | 8 | 1 |
| 3 | `142-2026-ND-CP_dieu-20_khoan-5` | 2.050312 | 5 | 6 |
| 4 | `142-2026-ND-CP_dieu-20_khoan-7_diem-d` | 2.029358 | 11 | 5 |
| 5 | `134-2025-QH15_dieu-27_khoan-4` | 1.814560 | 6 | 19 |

---

## eval026

Query: Báo cáo đánh giá tác động khi sử dụng AI trong khu vực công cần đề cập những nội dung gì?

Taxonomy: **PARTIAL_CANDIDATE_COVERAGE**  
Interpretation: mixed failure: candidate coverage is incomplete and ranking may also limit recall  
Union gold: 3/4  
Reranker first gold rank: 5  
Hit@5: 1  
Recall@5: 0.250000

| rank | chunk_id | reranker_score | bm25_rank | dense_rank |
|---:|---|---:|---:|---:|
| 1 | `134-2025-QH15_dieu-27_khoan-3` | 2.318991 | 5 | 5 |
| 2 | `134-2025-QH15_dieu-27_khoan-4` | 1.639735 | 1 | 2 |
| 3 | `142-2026-ND-CP_dieu-20_khoan-5` | 1.361600 | 4 | 1 |
| 4 | `142-2026-ND-CP_dieu-20_khoan-4` | 1.071260 | 2 | 4 |
| 5 | `142-2026-ND-CP_dieu-20_khoan-3_diem-a` | -0.054695 |  | 12 |

---

## eval027

Query: Nguyên tắc đạo đức khi phát triển và sử dụng trí tuệ nhân tạo được đặt ra như thế nào?

Taxonomy: **PARTIAL_CANDIDATE_COVERAGE**  
Interpretation: mixed failure: candidate coverage is incomplete and ranking may also limit recall  
Union gold: 2/4  
Reranker first gold rank: 3  
Hit@5: 1  
Recall@5: 0.250000

| rank | chunk_id | reranker_score | bm25_rank | dense_rank |
|---:|---|---:|---:|---:|
| 1 | `05-2026-TT-BKHCN_dieu-2_khoan-1` | 6.116686 | 2 | 2 |
| 2 | `134-2025-QH15_dieu-26_khoan-4` | 4.319105 | 6 | 4 |
| 3 | `134-2025-QH15_dieu-26_khoan-1_diem-b` | 4.046256 | 10 | 14 |
| 4 | `134-2025-QH15_dieu-4_khoan-3` | 4.025735 |  | 16 |
| 5 | `05-2026-TT-BKHCN_dieu-3_khoan-3_diem-c` | 3.515550 | 19 | 1 |

---

## Candidate rescue analysis

| query_id | union_gold_count | best baseline first_gold_rank | reranker first_gold_rank | reranker Hit@5 | reranker Recall@5 |
|---|---:|---:|---:|---:|---:|
| eval002 | 1 | 4 | 2 | 1 | 1.000000 |
| eval005a | 2 | 4 | 7 | 0 | 0.000000 |
| eval010 | 1 | 1 | 2 | 1 | 1.000000 |
| eval011 | 0 | not in Top-10 | not in Top-10 | 0 | 0.000000 |
| eval012 | 3 | 3 | 3 | 1 | 1.000000 |
| eval026 | 3 | not in Top-10 | 5 | 1 | 0.250000 |
