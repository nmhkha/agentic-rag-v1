# dense-jina-v3-v0 Failure Analysis

Diagnostic analysis only; retrieval configuration and gold labels were not changed.

## BM25 complete failures

| query_id | dense first gold rank | dense Hit@5 | dense Recall@5 |
|---|---:|---:|---:|
| eval002 | 4 | 1 | 1.000000 |
| eval010 | 1 | 1 | 1.000000 |
| eval011 | not in top 10 | 0 | 0.000000 |
| eval012 | 3 | 1 | 0.666667 |
| eval026 | not in top 10 | 0 | 0.000000 |

## Dense failures

### eval004

Query: Nhà cung cấp hệ thống AI rủi ro cao phải duy trì những biện pháp quản lý nào?  
First gold rank: 1  
Hit@5: 1  
Recall@5: 0.166667

| rank | chunk_id | article_id | score |
|---:|---|---|---:|
| 1 | `142-2026-ND-CP_dieu-15_khoan-1` | `142-2026-ND-CP_dieu-15` | 0.628401 |
| 2 | `142-2026-ND-CP_dieu-15_khoan-3` | `142-2026-ND-CP_dieu-15` | 0.576546 |
| 3 | `134-2025-QH15_dieu-14_khoan-3` | `134-2025-QH15_dieu-14` | 0.576406 |
| 4 | `142-2026-ND-CP_dieu-15_khoan-4` | `142-2026-ND-CP_dieu-15` | 0.569794 |
| 5 | `142-2026-ND-CP_dieu-11_khoan-5` | `142-2026-ND-CP_dieu-11` | 0.554248 |

### eval005a

Query: Nhà cung cấp hệ thống trí tuệ nhân tạo có rủi ro cao phải thực hiện những nghĩa vụ quản lý nào?  
First gold rank: not in top 10  
Hit@5: 0  
Recall@5: 0.000000

| rank | chunk_id | article_id | score |
|---:|---|---|---:|
| 1 | `142-2026-ND-CP_dieu-15_khoan-3` | `142-2026-ND-CP_dieu-15` | 0.707783 |
| 2 | `142-2026-ND-CP_dieu-15_khoan-1` | `142-2026-ND-CP_dieu-15` | 0.703611 |
| 3 | `134-2025-QH15_dieu-14_khoan-3` | `134-2025-QH15_dieu-14` | 0.674401 |
| 4 | `134-2025-QH15_dieu-15_khoan-1_diem-b` | `134-2025-QH15_dieu-15` | 0.667376 |
| 5 | `142-2026-ND-CP_dieu-15_khoan-4` | `142-2026-ND-CP_dieu-15` | 0.660683 |

### eval005b

Query: Bên triển khai hệ thống trí tuệ nhân tạo có rủi ro cao phải thực hiện những nghĩa vụ quản lý nào?  
First gold rank: 6  
Hit@5: 0  
Recall@5: 0.000000

| rank | chunk_id | article_id | score |
|---:|---|---|---:|
| 1 | `142-2026-ND-CP_dieu-15_khoan-3` | `142-2026-ND-CP_dieu-15` | 0.720054 |
| 2 | `142-2026-ND-CP_dieu-15_khoan-4` | `142-2026-ND-CP_dieu-15` | 0.718635 |
| 3 | `142-2026-ND-CP_dieu-15_khoan-1` | `142-2026-ND-CP_dieu-15` | 0.699636 |
| 4 | `134-2025-QH15_dieu-15_khoan-1_diem-c` | `134-2025-QH15_dieu-15` | 0.697789 |
| 5 | `134-2025-QH15_dieu-14_khoan-3` | `134-2025-QH15_dieu-14` | 0.695665 |

### eval006

Query: Trách nhiệm minh bạch của nhà cung cấp hệ thống trí tuệ nhân tạo bao gồm những gì?  
First gold rank: 2  
Hit@5: 1  
Recall@5: 0.333333

| rank | chunk_id | article_id | score |
|---:|---|---|---:|
| 1 | `142-2026-ND-CP_dieu-16_khoan-1` | `142-2026-ND-CP_dieu-16` | 0.722704 |
| 2 | `134-2025-QH15_dieu-11_khoan-5` | `134-2025-QH15_dieu-11` | 0.676217 |
| 3 | `134-2025-QH15_dieu-15_khoan-1_diem-b` | `134-2025-QH15_dieu-15` | 0.635072 |
| 4 | `134-2025-QH15_dieu-12_khoan-1` | `134-2025-QH15_dieu-12` | 0.634359 |
| 5 | `142-2026-ND-CP_dieu-16_khoan-6` | `142-2026-ND-CP_dieu-16` | 0.631570 |

### eval007

Query: Nội dung do AI tạo ra phải được thông báo hoặc gắn nhãn như thế nào?  
First gold rank: 10  
Hit@5: 0  
Recall@5: 0.000000

| rank | chunk_id | article_id | score |
|---:|---|---|---:|
| 1 | `142-2026-ND-CP_dieu-18_khoan-6` | `142-2026-ND-CP_dieu-18` | 0.739672 |
| 2 | `142-2026-ND-CP_dieu-18_khoan-1` | `142-2026-ND-CP_dieu-18` | 0.680208 |
| 3 | `142-2026-ND-CP_dieu-18_khoan-4_diem-d` | `142-2026-ND-CP_dieu-18` | 0.644078 |
| 4 | `134-2025-QH15_dieu-11_khoan-4` | `134-2025-QH15_dieu-11` | 0.639843 |
| 5 | `142-2026-ND-CP_dieu-18_khoan-7` | `142-2026-ND-CP_dieu-18` | 0.616425 |

### eval011

Query: Cơ chế thử nghiệm có kiểm soát cho phép tổ chức, cá nhân được hưởng những cơ chế gì trong phạm vi thử nghiệm?  
First gold rank: not in top 10  
Hit@5: 0  
Recall@5: 0.000000

| rank | chunk_id | article_id | score |
|---:|---|---|---:|
| 1 | `142-2026-ND-CP_dieu-26_khoan-1` | `142-2026-ND-CP_dieu-26` | 0.584427 |
| 2 | `142-2026-ND-CP_dieu-23_khoan-1` | `142-2026-ND-CP_dieu-23` | 0.551450 |
| 3 | `142-2026-ND-CP_dieu-21_khoan-3` | `142-2026-ND-CP_dieu-21` | 0.525513 |
| 4 | `142-2026-ND-CP_dieu-26_khoan-3_diem-c` | `142-2026-ND-CP_dieu-26` | 0.525375 |
| 5 | `142-2026-ND-CP_dieu-25_khoan-1_diem-c` | `142-2026-ND-CP_dieu-25` | 0.516325 |

### eval013

Query: Việc phân loại cấp độ thử nghiệm có kiểm soát dựa trên những tiêu chí nào?  
First gold rank: 1  
Hit@5: 1  
Recall@5: 0.400000

| rank | chunk_id | article_id | score |
|---:|---|---|---:|
| 1 | `142-2026-ND-CP_dieu-22_khoan-2` | `142-2026-ND-CP_dieu-22` | 0.664429 |
| 2 | `142-2026-ND-CP_dieu-22_khoan-6` | `142-2026-ND-CP_dieu-22` | 0.596321 |
| 3 | `142-2026-ND-CP_dieu-22_khoan-4_diem-a` | `142-2026-ND-CP_dieu-22` | 0.580422 |
| 4 | `142-2026-ND-CP_dieu-22_khoan-1_diem-c` | `142-2026-ND-CP_dieu-22` | 0.579512 |
| 5 | `142-2026-ND-CP_dieu-22_khoan-3_diem-a` | `142-2026-ND-CP_dieu-22` | 0.573605 |

### eval014

Query: Hồ sơ thông thường để tham gia cơ chế thử nghiệm có kiểm soát gồm những thành phần nào?  
First gold rank: 1  
Hit@5: 1  
Recall@5: 0.250000

| rank | chunk_id | article_id | score |
|---:|---|---|---:|
| 1 | `142-2026-ND-CP_dieu-24_khoan-2_diem-a` | `142-2026-ND-CP_dieu-24` | 0.468657 |
| 2 | `142-2026-ND-CP_dieu-24_khoan-3_diem-a` | `142-2026-ND-CP_dieu-24` | 0.468221 |
| 3 | `142-2026-ND-CP_dieu-23_khoan-4` | `142-2026-ND-CP_dieu-23` | 0.460737 |
| 4 | `142-2026-ND-CP_dieu-23_khoan-2` | `142-2026-ND-CP_dieu-23` | 0.439827 |
| 5 | `142-2026-ND-CP_dieu-23_khoan-1` | `142-2026-ND-CP_dieu-23` | 0.414808 |

### eval016

Query: Tổ chức hoặc cá nhân phải báo cáo gì trong quá trình thử nghiệm có kiểm soát?  
First gold rank: 1  
Hit@5: 1  
Recall@5: 0.400000

| rank | chunk_id | article_id | score |
|---:|---|---|---:|
| 1 | `142-2026-ND-CP_dieu-25_khoan-4` | `142-2026-ND-CP_dieu-25` | 0.596240 |
| 2 | `142-2026-ND-CP_dieu-25_khoan-3_diem-b` | `142-2026-ND-CP_dieu-25` | 0.524695 |
| 3 | `142-2026-ND-CP_dieu-25_khoan-1_diem-a` | `142-2026-ND-CP_dieu-25` | 0.522950 |
| 4 | `142-2026-ND-CP_dieu-25_khoan-1_diem-b` | `142-2026-ND-CP_dieu-25` | 0.509293 |
| 5 | `142-2026-ND-CP_dieu-25_khoan-1_diem-c` | `142-2026-ND-CP_dieu-25` | 0.508108 |

### eval018

Query: Sau khi kết thúc thử nghiệm, cơ quan có thẩm quyền xử lý kết quả như thế nào?  
First gold rank: 1  
Hit@5: 1  
Recall@5: 0.333333

| rank | chunk_id | article_id | score |
|---:|---|---|---:|
| 1 | `142-2026-ND-CP_dieu-27_khoan-1` | `142-2026-ND-CP_dieu-27` | 0.554123 |
| 2 | `142-2026-ND-CP_dieu-27_khoan-6_diem-a` | `142-2026-ND-CP_dieu-27` | 0.546954 |
| 3 | `142-2026-ND-CP_dieu-27_khoan-9` | `142-2026-ND-CP_dieu-27` | 0.518373 |
| 4 | `142-2026-ND-CP_dieu-25_khoan-4` | `142-2026-ND-CP_dieu-25` | 0.504803 |
| 5 | `142-2026-ND-CP_dieu-27_khoan-5` | `142-2026-ND-CP_dieu-27` | 0.504078 |

### eval021

Query: Những loại dữ liệu nào có thể được đưa vào cơ sở dữ liệu phục vụ trí tuệ nhân tạo?  
First gold rank: 4  
Hit@5: 1  
Recall@5: 0.333333

| rank | chunk_id | article_id | score |
|---:|---|---|---:|
| 1 | `134-2025-QH15_dieu-17_khoan-1` | `134-2025-QH15_dieu-17` | 0.604472 |
| 2 | `142-2026-ND-CP_dieu-35_khoan-1` | `142-2026-ND-CP_dieu-35` | 0.564434 |
| 3 | `134-2025-QH15_dieu-17_khoan-2` | `134-2025-QH15_dieu-17` | 0.548825 |
| 4 | `142-2026-ND-CP_dieu-32_khoan-1_diem-c` | `142-2026-ND-CP_dieu-32` | 0.540386 |
| 5 | `142-2026-ND-CP_dieu-3_khoan-8` | `142-2026-ND-CP_dieu-3` | 0.517458 |

### eval022

Query: Cơ quan quản lý có trách nhiệm gì đối với việc xây dựng và cập nhật dữ liệu mở phục vụ AI?  
First gold rank: not in top 10  
Hit@5: 0  
Recall@5: 0.000000

| rank | chunk_id | article_id | score |
|---:|---|---|---:|
| 1 | `142-2026-ND-CP_dieu-42_khoan-3` | `142-2026-ND-CP_dieu-42` | 0.595165 |
| 2 | `134-2025-QH15_dieu-31_khoan-1` | `134-2025-QH15_dieu-31` | 0.573920 |
| 3 | `142-2026-ND-CP_dieu-42_khoan-2` | `142-2026-ND-CP_dieu-42` | 0.555000 |
| 4 | `142-2026-ND-CP_dieu-44_khoan-2` | `142-2026-ND-CP_dieu-44` | 0.554927 |
| 5 | `142-2026-ND-CP_dieu-28_khoan-6` | `142-2026-ND-CP_dieu-28` | 0.549850 |

### eval023

Query: Quy định về bảo đảm khả năng kết nối và khai thác dữ liệu phục vụ trí tuệ nhân tạo là gì?  
First gold rank: not in top 10  
Hit@5: 0  
Recall@5: 0.000000

| rank | chunk_id | article_id | score |
|---:|---|---|---:|
| 1 | `142-2026-ND-CP_dieu-36_khoan-2` | `142-2026-ND-CP_dieu-36` | 0.695196 |
| 2 | `142-2026-ND-CP_dieu-35_khoan-1` | `142-2026-ND-CP_dieu-35` | 0.683721 |
| 3 | `142-2026-ND-CP_dieu-36_khoan-1` | `142-2026-ND-CP_dieu-36` | 0.676160 |
| 4 | `142-2026-ND-CP_dieu-35_khoan-3_diem-c` | `142-2026-ND-CP_dieu-35` | 0.675788 |
| 5 | `142-2026-ND-CP_dieu-31_khoan-2` | `142-2026-ND-CP_dieu-31` | 0.659924 |

### eval026

Query: Báo cáo đánh giá tác động khi sử dụng AI trong khu vực công cần đề cập những nội dung gì?  
First gold rank: not in top 10  
Hit@5: 0  
Recall@5: 0.000000

| rank | chunk_id | article_id | score |
|---:|---|---|---:|
| 1 | `142-2026-ND-CP_dieu-20_khoan-5` | `142-2026-ND-CP_dieu-20` | 0.625979 |
| 2 | `134-2025-QH15_dieu-27_khoan-4` | `134-2025-QH15_dieu-27` | 0.577837 |
| 3 | `142-2026-ND-CP_dieu-20_khoan-2` | `142-2026-ND-CP_dieu-20` | 0.574630 |
| 4 | `142-2026-ND-CP_dieu-20_khoan-4` | `142-2026-ND-CP_dieu-20` | 0.569237 |
| 5 | `134-2025-QH15_dieu-27_khoan-3` | `134-2025-QH15_dieu-27` | 0.566151 |

### eval027

Query: Nguyên tắc đạo đức khi phát triển và sử dụng trí tuệ nhân tạo được đặt ra như thế nào?  
First gold rank: not in top 10  
Hit@5: 0  
Recall@5: 0.000000

| rank | chunk_id | article_id | score |
|---:|---|---|---:|
| 1 | `05-2026-TT-BKHCN_dieu-3_khoan-3_diem-c` | `05-2026-TT-BKHCN_dieu-3` | 0.682893 |
| 2 | `05-2026-TT-BKHCN_dieu-2_khoan-1` | `05-2026-TT-BKHCN_dieu-2` | 0.675326 |
| 3 | `05-2026-TT-BKHCN_dieu-3_khoan-1_diem-a` | `05-2026-TT-BKHCN_dieu-3` | 0.672773 |
| 4 | `134-2025-QH15_dieu-26_khoan-4` | `134-2025-QH15_dieu-26` | 0.667470 |
| 5 | `05-2026-TT-BKHCN_dieu-3_khoan-2_diem-a` | `05-2026-TT-BKHCN_dieu-3` | 0.656711 |

### eval028

Query: Tổ chức phát triển hoặc triển khai AI cần bảo đảm trách nhiệm giải trình ra sao?  
First gold rank: 8  
Hit@5: 0  
Recall@5: 0.000000

| rank | chunk_id | article_id | score |
|---:|---|---|---:|
| 1 | `142-2026-ND-CP_dieu-16_khoan-1` | `142-2026-ND-CP_dieu-16` | 0.611676 |
| 2 | `134-2025-QH15_dieu-12_khoan-1` | `134-2025-QH15_dieu-12` | 0.591307 |
| 3 | `134-2025-QH15_dieu-15_khoan-1_diem-b` | `134-2025-QH15_dieu-15` | 0.589954 |
| 4 | `142-2026-ND-CP_dieu-15_khoan-3` | `142-2026-ND-CP_dieu-15` | 0.573592 |
| 5 | `134-2025-QH15_dieu-15_khoan-2_diem-b` | `134-2025-QH15_dieu-15` | 0.565712 |
