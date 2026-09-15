# hybrid-rrf-v0 Failure Analysis

Diagnostic analysis only; no retrieval configuration or frozen labels were changed.

## eval002

Query: Ai có thẩm quyền ban hành danh mục hệ thống trí tuệ nhân tạo có rủi ro cao?

Gold chunks:

- `142-2026-ND-CP_dieu-7_khoan-2_diem-d`

**BM25 top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-7_khoan-1_diem-a` | 28.500710 |
| 2 | `142-2026-ND-CP_dieu-7_khoan-1_diem-b` | 27.672165 |
| 3 | `142-2026-ND-CP_dieu-7_khoan-2_diem-c` | 25.903154 |
| 4 | `142-2026-ND-CP_dieu-7_khoan-2_diem-a` | 25.668343 |
| 5 | `142-2026-ND-CP_dieu-7_khoan-2_diem-b` | 25.528553 |

**Dense top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-8_khoan-5` | 0.748274 |
| 2 | `142-2026-ND-CP_dieu-8_khoan-4` | 0.706855 |
| 3 | `142-2026-ND-CP_dieu-8_khoan-3` | 0.694881 |
| 4 | `142-2026-ND-CP_dieu-7_khoan-2_diem-d` | 0.692294 |
| 5 | `142-2026-ND-CP_dieu-7_khoan-2_diem-b` | 0.684793 |

**Hybrid top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-8_khoan-5` | 0.031545 |
| 2 | `142-2026-ND-CP_dieu-7_khoan-2_diem-c` | 0.030798 |
| 3 | `142-2026-ND-CP_dieu-7_khoan-2_diem-b` | 0.030769 |
| 4 | `142-2026-ND-CP_dieu-8_khoan-4` | 0.030622 |
| 5 | `142-2026-ND-CP_dieu-7_khoan-2_diem-a` | 0.030331 |

Possible reason: **rank dilution**

---

## eval004

Query: Nhà cung cấp hệ thống AI rủi ro cao phải duy trì những biện pháp quản lý nào?

Gold chunks:

- `142-2026-ND-CP_dieu-15_khoan-1`
- `142-2026-ND-CP_dieu-15_khoan-2_diem-a`
- `142-2026-ND-CP_dieu-15_khoan-2_diem-b`
- `142-2026-ND-CP_dieu-15_khoan-2_diem-c`
- `142-2026-ND-CP_dieu-15_khoan-2_diem-d`
- `142-2026-ND-CP_dieu-15_khoan-2_diem-đ`

**BM25 top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-15_khoan-1` | 21.865478 |
| 2 | `134-2025-QH15_dieu-14_khoan-1_diem-a` | 20.568262 |
| 3 | `134-2025-QH15_dieu-14_khoan-2_diem-c` | 16.222403 |
| 4 | `134-2025-QH15_dieu-14_khoan-6` | 15.946447 |
| 5 | `142-2026-ND-CP_dieu-10_khoan-2` | 15.931823 |

**Dense top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-15_khoan-1` | 0.628401 |
| 2 | `142-2026-ND-CP_dieu-15_khoan-3` | 0.576546 |
| 3 | `134-2025-QH15_dieu-14_khoan-3` | 0.576406 |
| 4 | `142-2026-ND-CP_dieu-15_khoan-4` | 0.569794 |
| 5 | `142-2026-ND-CP_dieu-11_khoan-5` | 0.554248 |

**Hybrid top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-15_khoan-1` | 0.032787 |
| 2 | `134-2025-QH15_dieu-14_khoan-1_diem-a` | 0.031054 |
| 3 | `134-2025-QH15_dieu-14_khoan-6` | 0.030331 |
| 4 | `142-2026-ND-CP_dieu-11_khoan-5` | 0.030310 |
| 5 | `142-2026-ND-CP_dieu-15_khoan-3` | 0.030018 |

Possible reason: **multi-chunk coverage**

---

## eval005a

Query: Nhà cung cấp hệ thống trí tuệ nhân tạo có rủi ro cao phải thực hiện những nghĩa vụ quản lý nào?

Gold chunks:

- `134-2025-QH15_dieu-14_khoan-1_diem-a`
- `134-2025-QH15_dieu-14_khoan-1_diem-b`
- `134-2025-QH15_dieu-14_khoan-1_diem-c`
- `134-2025-QH15_dieu-14_khoan-1_diem-d`
- `134-2025-QH15_dieu-14_khoan-1_diem-đ`
- `134-2025-QH15_dieu-14_khoan-1_diem-e`
- `134-2025-QH15_dieu-14_khoan-1_diem-g`

**BM25 top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `134-2025-QH15_dieu-14_khoan-6` | 24.711711 |
| 2 | `134-2025-QH15_dieu-14_khoan-5` | 24.596076 |
| 3 | `142-2026-ND-CP_dieu-15_khoan-1` | 23.844765 |
| 4 | `134-2025-QH15_dieu-14_khoan-1_diem-đ` | 23.248946 |
| 5 | `134-2025-QH15_dieu-14_khoan-2_diem-d` | 23.248946 |

**Dense top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-15_khoan-3` | 0.707783 |
| 2 | `142-2026-ND-CP_dieu-15_khoan-1` | 0.703611 |
| 3 | `134-2025-QH15_dieu-14_khoan-3` | 0.674401 |
| 4 | `134-2025-QH15_dieu-15_khoan-1_diem-b` | 0.667376 |
| 5 | `142-2026-ND-CP_dieu-15_khoan-4` | 0.660683 |

**Hybrid top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-15_khoan-1` | 0.032002 |
| 2 | `134-2025-QH15_dieu-14_khoan-5` | 0.030415 |
| 3 | `142-2026-ND-CP_dieu-15_khoan-4` | 0.030310 |
| 4 | `134-2025-QH15_dieu-14_khoan-6` | 0.030282 |
| 5 | `142-2026-ND-CP_dieu-13_khoan-2_diem-b` | 0.030077 |

Possible reason: **multi-chunk coverage**

---

## eval005b

Query: Bên triển khai hệ thống trí tuệ nhân tạo có rủi ro cao phải thực hiện những nghĩa vụ quản lý nào?

Gold chunks:

- `134-2025-QH15_dieu-14_khoan-2_diem-a`
- `134-2025-QH15_dieu-14_khoan-2_diem-b`
- `134-2025-QH15_dieu-14_khoan-2_diem-c`
- `134-2025-QH15_dieu-14_khoan-2_diem-d`
- `134-2025-QH15_dieu-14_khoan-2_diem-đ`
- `134-2025-QH15_dieu-14_khoan-2_diem-e`

**BM25 top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `134-2025-QH15_dieu-14_khoan-5` | 25.603723 |
| 2 | `142-2026-ND-CP_dieu-15_khoan-4` | 24.303689 |
| 3 | `134-2025-QH15_dieu-14_khoan-1_diem-đ` | 23.248946 |
| 4 | `134-2025-QH15_dieu-14_khoan-2_diem-d` | 23.248946 |
| 5 | `142-2026-ND-CP_dieu-11_khoan-2` | 22.807566 |

**Dense top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-15_khoan-3` | 0.720054 |
| 2 | `142-2026-ND-CP_dieu-15_khoan-4` | 0.718635 |
| 3 | `142-2026-ND-CP_dieu-15_khoan-1` | 0.699636 |
| 4 | `134-2025-QH15_dieu-15_khoan-1_diem-c` | 0.697789 |
| 5 | `134-2025-QH15_dieu-14_khoan-3` | 0.695665 |

**Hybrid top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-15_khoan-4` | 0.032258 |
| 2 | `142-2026-ND-CP_dieu-15_khoan-1` | 0.030579 |
| 3 | `134-2025-QH15_dieu-14_khoan-5` | 0.029907 |
| 4 | `134-2025-QH15_dieu-14_khoan-3` | 0.029083 |
| 5 | `142-2026-ND-CP_dieu-15_khoan-3` | 0.029052 |

Possible reason: **multi-chunk coverage**

---

## eval007

Query: Nội dung do AI tạo ra phải được thông báo hoặc gắn nhãn như thế nào?

Gold chunks:

- `142-2026-ND-CP_dieu-18_khoan-3_diem-a`
- `142-2026-ND-CP_dieu-18_khoan-3_diem-b`
- `142-2026-ND-CP_dieu-18_khoan-3_diem-c`
- `142-2026-ND-CP_dieu-18_khoan-3_diem-d`
- `142-2026-ND-CP_dieu-18_khoan-3_diem-đ`
- `142-2026-ND-CP_dieu-18_khoan-5_diem-a`
- `142-2026-ND-CP_dieu-18_khoan-5_diem-b`
- `142-2026-ND-CP_dieu-18_khoan-5_diem-c`
- `142-2026-ND-CP_dieu-18_khoan-5_diem-d`

**BM25 top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-18_khoan-6` | 29.270588 |
| 2 | `142-2026-ND-CP_dieu-18_khoan-1` | 26.513518 |
| 3 | `142-2026-ND-CP_dieu-18_khoan-4_diem-d` | 25.642398 |
| 4 | `142-2026-ND-CP_dieu-18_khoan-3_diem-b` | 25.106758 |
| 5 | `142-2026-ND-CP_dieu-18_khoan-4_diem-c` | 24.852874 |

**Dense top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-18_khoan-6` | 0.739672 |
| 2 | `142-2026-ND-CP_dieu-18_khoan-1` | 0.680208 |
| 3 | `142-2026-ND-CP_dieu-18_khoan-4_diem-d` | 0.644078 |
| 4 | `134-2025-QH15_dieu-11_khoan-4` | 0.639843 |
| 5 | `142-2026-ND-CP_dieu-18_khoan-7` | 0.616425 |

**Hybrid top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-18_khoan-6` | 0.032787 |
| 2 | `142-2026-ND-CP_dieu-18_khoan-1` | 0.032258 |
| 3 | `142-2026-ND-CP_dieu-18_khoan-4_diem-d` | 0.031746 |
| 4 | `142-2026-ND-CP_dieu-18_khoan-3_diem-b` | 0.029911 |
| 5 | `142-2026-ND-CP_dieu-18_khoan-3_diem-c` | 0.029236 |

Possible reason: **multi-chunk coverage**

---

## eval010

Query: Nhà cung cấp cần làm gì khi phát hiện sự cố liên quan đến hệ thống trí tuệ nhân tạo?

Gold chunks:

- `134-2025-QH15_dieu-12_khoan-2_diem-a`

**BM25 top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `134-2025-QH15_dieu-10_khoan-5_diem-c` | 22.223315 |
| 2 | `142-2026-ND-CP_dieu-20_khoan-8` | 20.072054 |
| 3 | `134-2025-QH15_dieu-12_khoan-3` | 19.536711 |
| 4 | `134-2025-QH15_dieu-12_khoan-1` | 19.289118 |
| 5 | `134-2025-QH15_dieu-14_khoan-1_diem-c` | 19.199525 |

**Dense top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `134-2025-QH15_dieu-12_khoan-2_diem-a` | 0.670297 |
| 2 | `142-2026-ND-CP_dieu-19_khoan-3_diem-c` | 0.650058 |
| 3 | `134-2025-QH15_dieu-12_khoan-1` | 0.636616 |
| 4 | `142-2026-ND-CP_dieu-19_khoan-2_diem-c` | 0.597408 |
| 5 | `142-2026-ND-CP_dieu-19_khoan-4` | 0.584467 |

**Hybrid top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `134-2025-QH15_dieu-12_khoan-1` | 0.031498 |
| 2 | `142-2026-ND-CP_dieu-19_khoan-3_diem-c` | 0.030214 |
| 3 | `142-2026-ND-CP_dieu-19_khoan-2_diem-c` | 0.029514 |
| 4 | `142-2026-ND-CP_dieu-19_khoan-4` | 0.028718 |
| 5 | `134-2025-QH15_dieu-12_khoan-3` | 0.028694 |

Possible reason: **rank dilution**

---

## eval011

Query: Cơ chế thử nghiệm có kiểm soát cho phép tổ chức, cá nhân được hưởng những cơ chế gì trong phạm vi thử nghiệm?

Gold chunks:

- `134-2025-QH15_dieu-21_khoan-2_diem-a`
- `134-2025-QH15_dieu-21_khoan-2_diem-b`

**BM25 top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-26_khoan-2_diem-c` | 31.868007 |
| 2 | `142-2026-ND-CP_dieu-23_khoan-1` | 31.467476 |
| 3 | `142-2026-ND-CP_dieu-27_khoan-3` | 30.983013 |
| 4 | `142-2026-ND-CP_dieu-25_khoan-1_diem-c` | 30.555941 |
| 5 | `142-2026-ND-CP_dieu-26_khoan-2_diem-a` | 30.007277 |

**Dense top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-26_khoan-1` | 0.584427 |
| 2 | `142-2026-ND-CP_dieu-23_khoan-1` | 0.551450 |
| 3 | `142-2026-ND-CP_dieu-21_khoan-3` | 0.525513 |
| 4 | `142-2026-ND-CP_dieu-26_khoan-3_diem-c` | 0.525375 |
| 5 | `142-2026-ND-CP_dieu-25_khoan-1_diem-c` | 0.516325 |

**Hybrid top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-23_khoan-1` | 0.032258 |
| 2 | `142-2026-ND-CP_dieu-25_khoan-1_diem-c` | 0.031010 |
| 3 | `142-2026-ND-CP_dieu-26_khoan-2_diem-c` | 0.030886 |
| 4 | `142-2026-ND-CP_dieu-21_khoan-3` | 0.030798 |
| 5 | `142-2026-ND-CP_dieu-26_khoan-1` | 0.029727 |

Possible reason: **both retrievers miss**

---

## eval012

Query: Cơ quan nào quyết định chấp thuận tham gia cơ chế thử nghiệm có kiểm soát?

Gold chunks:

- `142-2026-ND-CP_dieu-23_khoan-3_diem-a`
- `142-2026-ND-CP_dieu-23_khoan-3_diem-b`
- `142-2026-ND-CP_dieu-23_khoan-3_diem-c`

**BM25 top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-23_khoan-6` | 29.705148 |
| 2 | `142-2026-ND-CP_dieu-23_khoan-1` | 28.986056 |
| 3 | `142-2026-ND-CP_dieu-23_khoan-7_diem-b` | 27.748716 |
| 4 | `142-2026-ND-CP_dieu-23_khoan-7_diem-a` | 27.468970 |
| 5 | `142-2026-ND-CP_dieu-23_khoan-7_diem-đ` | 27.468970 |

**Dense top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-23_khoan-5_diem-c` | 0.678973 |
| 2 | `142-2026-ND-CP_dieu-23_khoan-1` | 0.674544 |
| 3 | `142-2026-ND-CP_dieu-23_khoan-3_diem-c` | 0.655407 |
| 4 | `142-2026-ND-CP_dieu-23_khoan-3_diem-b` | 0.653478 |
| 5 | `142-2026-ND-CP_dieu-23_khoan-4` | 0.636322 |

**Hybrid top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-23_khoan-1` | 0.032258 |
| 2 | `142-2026-ND-CP_dieu-23_khoan-6` | 0.031545 |
| 3 | `142-2026-ND-CP_dieu-23_khoan-5_diem-c` | 0.030092 |
| 4 | `142-2026-ND-CP_dieu-23_khoan-4` | 0.029274 |
| 5 | `142-2026-ND-CP_dieu-23_khoan-5_diem-a` | 0.028992 |

Possible reason: **rank dilution**

---

## eval013

Query: Việc phân loại cấp độ thử nghiệm có kiểm soát dựa trên những tiêu chí nào?

Gold chunks:

- `142-2026-ND-CP_dieu-22_khoan-1_diem-a`
- `142-2026-ND-CP_dieu-22_khoan-1_diem-b`
- `142-2026-ND-CP_dieu-22_khoan-1_diem-c`
- `142-2026-ND-CP_dieu-22_khoan-1_diem-d`
- `142-2026-ND-CP_dieu-22_khoan-2`

**BM25 top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-22_khoan-6` | 25.540442 |
| 2 | `142-2026-ND-CP_dieu-22_khoan-2` | 25.083276 |
| 3 | `142-2026-ND-CP_dieu-22_khoan-5_diem-a` | 23.348067 |
| 4 | `142-2026-ND-CP_dieu-44_khoan-5` | 17.146403 |
| 5 | `142-2026-ND-CP_dieu-22_khoan-1_diem-a` | 16.790073 |

**Dense top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-22_khoan-2` | 0.664429 |
| 2 | `142-2026-ND-CP_dieu-22_khoan-6` | 0.596321 |
| 3 | `142-2026-ND-CP_dieu-22_khoan-4_diem-a` | 0.580422 |
| 4 | `142-2026-ND-CP_dieu-22_khoan-1_diem-c` | 0.579512 |
| 5 | `142-2026-ND-CP_dieu-22_khoan-3_diem-a` | 0.573605 |

**Hybrid top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-22_khoan-6` | 0.032522 |
| 2 | `142-2026-ND-CP_dieu-22_khoan-2` | 0.032522 |
| 3 | `142-2026-ND-CP_dieu-22_khoan-5_diem-a` | 0.031025 |
| 4 | `142-2026-ND-CP_dieu-22_khoan-1_diem-c` | 0.030777 |
| 5 | `142-2026-ND-CP_dieu-22_khoan-4_diem-a` | 0.030159 |

Possible reason: **other**

---

## eval014

Query: Hồ sơ thông thường để tham gia cơ chế thử nghiệm có kiểm soát gồm những thành phần nào?

Gold chunks:

- `142-2026-ND-CP_dieu-24_khoan-2_diem-a`
- `142-2026-ND-CP_dieu-24_khoan-2_diem-b`
- `142-2026-ND-CP_dieu-24_khoan-2_diem-c`
- `142-2026-ND-CP_dieu-24_khoan-2_diem-d`

**BM25 top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-24_khoan-5` | 30.195379 |
| 2 | `142-2026-ND-CP_dieu-23_khoan-4` | 24.543169 |
| 3 | `142-2026-ND-CP_dieu-23_khoan-2` | 24.206620 |
| 4 | `142-2026-ND-CP_dieu-22_khoan-6` | 22.401349 |
| 5 | `142-2026-ND-CP_dieu-24_khoan-2_diem-a` | 22.267946 |

**Dense top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-24_khoan-2_diem-a` | 0.468657 |
| 2 | `142-2026-ND-CP_dieu-24_khoan-3_diem-a` | 0.468221 |
| 3 | `142-2026-ND-CP_dieu-23_khoan-4` | 0.460737 |
| 4 | `142-2026-ND-CP_dieu-23_khoan-2` | 0.439827 |
| 5 | `142-2026-ND-CP_dieu-23_khoan-1` | 0.414808 |

**Hybrid top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-23_khoan-4` | 0.032002 |
| 2 | `142-2026-ND-CP_dieu-24_khoan-2_diem-a` | 0.031778 |
| 3 | `142-2026-ND-CP_dieu-24_khoan-5` | 0.031545 |
| 4 | `142-2026-ND-CP_dieu-23_khoan-2` | 0.031498 |
| 5 | `142-2026-ND-CP_dieu-24_khoan-3_diem-a` | 0.031281 |

Possible reason: **other**

---

## eval016

Query: Tổ chức hoặc cá nhân phải báo cáo gì trong quá trình thử nghiệm có kiểm soát?

Gold chunks:

- `142-2026-ND-CP_dieu-25_khoan-2_diem-a`
- `142-2026-ND-CP_dieu-25_khoan-2_diem-b`
- `142-2026-ND-CP_dieu-25_khoan-3_diem-a`
- `142-2026-ND-CP_dieu-25_khoan-3_diem-b`
- `142-2026-ND-CP_dieu-25_khoan-4`

**BM25 top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-25_khoan-4` | 27.560938 |
| 2 | `142-2026-ND-CP_dieu-25_khoan-3_diem-b` | 26.318932 |
| 3 | `142-2026-ND-CP_dieu-25_khoan-1_diem-b` | 25.329286 |
| 4 | `142-2026-ND-CP_dieu-25_khoan-1_diem-c` | 25.237062 |
| 5 | `142-2026-ND-CP_dieu-25_khoan-1_diem-a` | 24.585332 |

**Dense top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-25_khoan-4` | 0.596240 |
| 2 | `142-2026-ND-CP_dieu-25_khoan-3_diem-b` | 0.524695 |
| 3 | `142-2026-ND-CP_dieu-25_khoan-1_diem-a` | 0.522950 |
| 4 | `142-2026-ND-CP_dieu-25_khoan-1_diem-b` | 0.509293 |
| 5 | `142-2026-ND-CP_dieu-25_khoan-1_diem-c` | 0.508108 |

**Hybrid top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-25_khoan-4` | 0.032787 |
| 2 | `142-2026-ND-CP_dieu-25_khoan-3_diem-b` | 0.032258 |
| 3 | `142-2026-ND-CP_dieu-25_khoan-1_diem-b` | 0.031498 |
| 4 | `142-2026-ND-CP_dieu-25_khoan-1_diem-a` | 0.031258 |
| 5 | `142-2026-ND-CP_dieu-25_khoan-1_diem-c` | 0.031010 |

Possible reason: **other**

---

## eval018

Query: Sau khi kết thúc thử nghiệm, cơ quan có thẩm quyền xử lý kết quả như thế nào?

Gold chunks:

- `142-2026-ND-CP_dieu-27_khoan-1`
- `142-2026-ND-CP_dieu-27_khoan-2_diem-a`
- `142-2026-ND-CP_dieu-27_khoan-2_diem-b`

**BM25 top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-27_khoan-6_diem-a` | 23.824665 |
| 2 | `142-2026-ND-CP_dieu-27_khoan-1` | 23.670844 |
| 3 | `142-2026-ND-CP_dieu-27_khoan-8` | 22.326192 |
| 4 | `142-2026-ND-CP_dieu-27_khoan-2_diem-a` | 21.732372 |
| 5 | `142-2026-ND-CP_dieu-23_khoan-5_diem-c` | 21.036696 |

**Dense top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-27_khoan-1` | 0.554123 |
| 2 | `142-2026-ND-CP_dieu-27_khoan-6_diem-a` | 0.546954 |
| 3 | `142-2026-ND-CP_dieu-27_khoan-9` | 0.518373 |
| 4 | `142-2026-ND-CP_dieu-25_khoan-4` | 0.504803 |
| 5 | `142-2026-ND-CP_dieu-27_khoan-5` | 0.504078 |

**Hybrid top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-27_khoan-6_diem-a` | 0.032522 |
| 2 | `142-2026-ND-CP_dieu-27_khoan-1` | 0.032522 |
| 3 | `142-2026-ND-CP_dieu-27_khoan-9` | 0.031025 |
| 4 | `142-2026-ND-CP_dieu-27_khoan-8` | 0.030579 |
| 5 | `142-2026-ND-CP_dieu-27_khoan-5` | 0.030310 |

Possible reason: **other**

---

## eval021

Query: Những loại dữ liệu nào có thể được đưa vào cơ sở dữ liệu phục vụ trí tuệ nhân tạo?

Gold chunks:

- `142-2026-ND-CP_dieu-32_khoan-1_diem-a`
- `142-2026-ND-CP_dieu-32_khoan-1_diem-b`
- `142-2026-ND-CP_dieu-32_khoan-1_diem-c`

**BM25 top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `134-2025-QH15_dieu-17_khoan-1` | 23.365684 |
| 2 | `134-2025-QH15_dieu-17_khoan-3` | 22.122502 |
| 3 | `134-2025-QH15_dieu-17_khoan-4` | 21.704470 |
| 4 | `134-2025-QH15_dieu-17_khoan-6` | 21.303696 |
| 5 | `134-2025-QH15_dieu-17_khoan-2` | 20.770506 |

**Dense top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `134-2025-QH15_dieu-17_khoan-1` | 0.604472 |
| 2 | `142-2026-ND-CP_dieu-35_khoan-1` | 0.564434 |
| 3 | `134-2025-QH15_dieu-17_khoan-2` | 0.548825 |
| 4 | `142-2026-ND-CP_dieu-32_khoan-1_diem-c` | 0.540386 |
| 5 | `142-2026-ND-CP_dieu-3_khoan-8` | 0.517458 |

**Hybrid top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `134-2025-QH15_dieu-17_khoan-1` | 0.032787 |
| 2 | `134-2025-QH15_dieu-17_khoan-2` | 0.031258 |
| 3 | `134-2025-QH15_dieu-17_khoan-4` | 0.031025 |
| 4 | `134-2025-QH15_dieu-17_khoan-3` | 0.029828 |
| 5 | `142-2026-ND-CP_dieu-3_khoan-8` | 0.029469 |

Possible reason: **rank dilution**

---

## eval022

Query: Cơ quan quản lý có trách nhiệm gì đối với việc xây dựng và cập nhật dữ liệu mở phục vụ AI?

Gold chunks:

- `142-2026-ND-CP_dieu-32_khoan-5_diem-a`
- `142-2026-ND-CP_dieu-32_khoan-5_diem-b`
- `142-2026-ND-CP_dieu-32_khoan-5_diem-c`

**BM25 top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-32_khoan-5_diem-a` | 29.655199 |
| 2 | `134-2025-QH15_dieu-17_khoan-3` | 22.063331 |
| 3 | `134-2025-QH15_dieu-17_khoan-2` | 20.284659 |
| 4 | `142-2026-ND-CP_dieu-42_khoan-2` | 19.890638 |
| 5 | `142-2026-ND-CP_dieu-42_khoan-3` | 18.599098 |

**Dense top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-42_khoan-3` | 0.595165 |
| 2 | `134-2025-QH15_dieu-31_khoan-1` | 0.573920 |
| 3 | `142-2026-ND-CP_dieu-42_khoan-2` | 0.555000 |
| 4 | `142-2026-ND-CP_dieu-44_khoan-2` | 0.554927 |
| 5 | `142-2026-ND-CP_dieu-28_khoan-6` | 0.549850 |

**Hybrid top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-42_khoan-3` | 0.031778 |
| 2 | `142-2026-ND-CP_dieu-42_khoan-2` | 0.031498 |
| 3 | `134-2025-QH15_dieu-17_khoan-3` | 0.030835 |
| 4 | `134-2025-QH15_dieu-17_khoan-2` | 0.030366 |
| 5 | `142-2026-ND-CP_dieu-44_khoan-2` | 0.030118 |

Possible reason: **rank dilution**

---

## eval023

Query: Quy định về bảo đảm khả năng kết nối và khai thác dữ liệu phục vụ trí tuệ nhân tạo là gì?

Gold chunks:

- `134-2025-QH15_dieu-17_khoan-2`
- `134-2025-QH15_dieu-17_khoan-3`

**BM25 top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `134-2025-QH15_dieu-17_khoan-6` | 29.495209 |
| 2 | `142-2026-ND-CP_dieu-32_khoan-5_diem-c` | 28.835317 |
| 3 | `134-2025-QH15_dieu-17_khoan-2` | 27.862393 |
| 4 | `142-2026-ND-CP_dieu-35_khoan-2_diem-c` | 27.561061 |
| 5 | `142-2026-ND-CP_dieu-31_khoan-1_diem-b` | 27.374106 |

**Dense top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-36_khoan-2` | 0.695196 |
| 2 | `142-2026-ND-CP_dieu-35_khoan-1` | 0.683721 |
| 3 | `142-2026-ND-CP_dieu-36_khoan-1` | 0.676160 |
| 4 | `142-2026-ND-CP_dieu-35_khoan-3_diem-c` | 0.675788 |
| 5 | `142-2026-ND-CP_dieu-31_khoan-2` | 0.659924 |

**Hybrid top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `134-2025-QH15_dieu-17_khoan-6` | 0.030886 |
| 2 | `142-2026-ND-CP_dieu-35_khoan-2_diem-d` | 0.029644 |
| 3 | `142-2026-ND-CP_dieu-36_khoan-2` | 0.029551 |
| 4 | `142-2026-ND-CP_dieu-35_khoan-1` | 0.029462 |
| 5 | `142-2026-ND-CP_dieu-30_khoan-1_diem-a` | 0.028405 |

Possible reason: **rank dilution**

---

## eval025

Query: Khi ứng dụng AI trong quản lý nhà nước, cơ quan vận hành phải đánh giá tác động trong trường hợp nào?

Gold chunks:

- `142-2026-ND-CP_dieu-20_khoan-1_diem-a`
- `142-2026-ND-CP_dieu-20_khoan-1_diem-b`
- `142-2026-ND-CP_dieu-20_khoan-2`
- `142-2026-ND-CP_dieu-20_khoan-7_diem-a`
- `142-2026-ND-CP_dieu-20_khoan-7_diem-b`
- `142-2026-ND-CP_dieu-20_khoan-7_diem-c`
- `142-2026-ND-CP_dieu-20_khoan-7_diem-d`

**BM25 top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `134-2025-QH15_dieu-27_khoan-3` | 23.133665 |
| 2 | `142-2026-ND-CP_dieu-20_khoan-3_diem-d` | 20.675106 |
| 3 | `142-2026-ND-CP_dieu-20_khoan-8` | 20.596081 |
| 4 | `134-2025-QH15_dieu-27_khoan-5` | 20.186786 |
| 5 | `142-2026-ND-CP_dieu-20_khoan-5` | 19.976884 |

**Dense top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-20_khoan-2` | 0.669670 |
| 2 | `142-2026-ND-CP_dieu-20_khoan-1_diem-b` | 0.634931 |
| 3 | `142-2026-ND-CP_dieu-20_khoan-7_diem-a` | 0.629555 |
| 4 | `142-2026-ND-CP_dieu-20_khoan-4` | 0.617236 |
| 5 | `142-2026-ND-CP_dieu-20_khoan-7_diem-d` | 0.613498 |

**Hybrid top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-20_khoan-2` | 0.031099 |
| 2 | `142-2026-ND-CP_dieu-20_khoan-8` | 0.030579 |
| 3 | `142-2026-ND-CP_dieu-20_khoan-5` | 0.030536 |
| 4 | `134-2025-QH15_dieu-27_khoan-3` | 0.030478 |
| 5 | `142-2026-ND-CP_dieu-20_khoan-7_diem-a` | 0.030366 |

Possible reason: **multi-chunk coverage**

---

## eval026

Query: Báo cáo đánh giá tác động khi sử dụng AI trong khu vực công cần đề cập những nội dung gì?

Gold chunks:

- `142-2026-ND-CP_dieu-20_khoan-3_diem-a`
- `142-2026-ND-CP_dieu-20_khoan-3_diem-b`
- `142-2026-ND-CP_dieu-20_khoan-3_diem-c`
- `142-2026-ND-CP_dieu-20_khoan-3_diem-d`

**BM25 top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `134-2025-QH15_dieu-27_khoan-4` | 24.471981 |
| 2 | `142-2026-ND-CP_dieu-20_khoan-4` | 22.609220 |
| 3 | `142-2026-ND-CP_dieu-20_khoan-8` | 22.117393 |
| 4 | `142-2026-ND-CP_dieu-20_khoan-5` | 20.177348 |
| 5 | `134-2025-QH15_dieu-27_khoan-3` | 19.088469 |

**Dense top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `142-2026-ND-CP_dieu-20_khoan-5` | 0.625979 |
| 2 | `134-2025-QH15_dieu-27_khoan-4` | 0.577837 |
| 3 | `142-2026-ND-CP_dieu-20_khoan-2` | 0.574630 |
| 4 | `142-2026-ND-CP_dieu-20_khoan-4` | 0.569237 |
| 5 | `134-2025-QH15_dieu-27_khoan-3` | 0.566151 |

**Hybrid top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `134-2025-QH15_dieu-27_khoan-4` | 0.032522 |
| 2 | `142-2026-ND-CP_dieu-20_khoan-5` | 0.032018 |
| 3 | `142-2026-ND-CP_dieu-20_khoan-4` | 0.031754 |
| 4 | `134-2025-QH15_dieu-27_khoan-3` | 0.030769 |
| 5 | `142-2026-ND-CP_dieu-20_khoan-8` | 0.029958 |

Possible reason: **both retrievers miss**

---

## eval027

Query: Nguyên tắc đạo đức khi phát triển và sử dụng trí tuệ nhân tạo được đặt ra như thế nào?

Gold chunks:

- `134-2025-QH15_dieu-26_khoan-1_diem-a`
- `134-2025-QH15_dieu-26_khoan-1_diem-b`
- `134-2025-QH15_dieu-26_khoan-1_diem-c`
- `134-2025-QH15_dieu-26_khoan-1_diem-d`

**BM25 top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `134-2025-QH15_dieu-27_khoan-2` | 26.477088 |
| 2 | `05-2026-TT-BKHCN_dieu-2_khoan-1` | 24.175414 |
| 3 | `134-2025-QH15_dieu-26_khoan-2` | 21.438766 |
| 4 | `142-2026-ND-CP_dieu-20_khoan-6` | 21.409374 |
| 5 | `134-2025-QH15_dieu-27_khoan-1` | 21.257089 |

**Dense top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `05-2026-TT-BKHCN_dieu-3_khoan-3_diem-c` | 0.682893 |
| 2 | `05-2026-TT-BKHCN_dieu-2_khoan-1` | 0.675326 |
| 3 | `05-2026-TT-BKHCN_dieu-3_khoan-1_diem-a` | 0.672773 |
| 4 | `134-2025-QH15_dieu-26_khoan-4` | 0.667470 |
| 5 | `05-2026-TT-BKHCN_dieu-3_khoan-2_diem-a` | 0.656711 |

**Hybrid top candidates**

| rank | chunk_id | score |
|---:|---|---:|
| 1 | `05-2026-TT-BKHCN_dieu-2_khoan-1` | 0.032258 |
| 2 | `134-2025-QH15_dieu-26_khoan-4` | 0.030777 |
| 3 | `05-2026-TT-BKHCN_dieu-3_khoan-3_diem-d` | 0.029199 |
| 4 | `05-2026-TT-BKHCN_dieu-3_khoan-1_diem-b` | 0.029199 |
| 5 | `05-2026-TT-BKHCN_dieu-3_khoan-3_diem-c` | 0.029052 |

Possible reason: **both retrievers miss**

---
