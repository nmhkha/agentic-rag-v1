# BM25-simple-v0 Failure Analysis

This report is diagnostic only; it does not alter queries, gold labels, tokenizer, or retrieval configuration.

## eval001

Query: Các mức phân loại rủi ro của hệ thống trí tuệ nhân tạo gồm những mức nào?  
Difficulty: easy  
Query type: classification

Gold article IDs:
- `134-2025-QH15_dieu-9`

Gold chunk IDs:
- `134-2025-QH15_dieu-9_khoan-1_diem-a`
- `134-2025-QH15_dieu-9_khoan-1_diem-b`
- `134-2025-QH15_dieu-9_khoan-1_diem-c`

Top-5 retrieved chunks:

| rank | chunk_id | article_id | score | text excerpt |
|---:|---|---|---:|---|
| 1 | `134-2025-QH15_dieu-9_khoan-2` | `134-2025-QH15_dieu-9` | 22.713995 | Việc phân loại rủi ro của hệ thống trí tuệ nhân tạo được xác định trên cơ sở các tiêu chí về mức độ tác động đến quyền con người, an toàn, an ninh; lĩnh vực sử dụng của hệ thống, đặc biệt là lĩnh vực thiết yếu hoặc liên  |
| 2 | `142-2026-ND-CP_dieu-11_khoan-3_diem-b` | `142-2026-ND-CP_dieu-11` | 22.152272 | Trường hợp kết quả phân loại lại xác định mức độ rủi ro của hệ thống thấp hơn mức đã phân loại, nhà cung cấp, bên triển khai có quyền thực hiện thông báo kết quả phân loại lại cho cơ quan nhà nước có thẩm quyền để được á |
| 3 | `142-2026-ND-CP_dieu-11_khoan-1_diem-c` | `142-2026-ND-CP_dieu-11` | 22.141043 | Có quyết định của Thủ tướng Chính phủ về việc sửa đổi, bổ sung Danh mục hệ thống trí tuệ nhân tạo có rủi ro cao làm thay đổi mức độ rủi ro của hệ thống; |
| 4 | `142-2026-ND-CP_dieu-11_khoan-3_diem-a` | `142-2026-ND-CP_dieu-11` | 22.118427 | Trường hợp kết quả phân loại lại xác định mức độ rủi ro của hệ thống cao hơn mức đã phân loại, nhà cung cấp, bên triển khai phải thực hiện thông báo kết quả phân loại lại cho cơ quan nhà nước có thẩm quyền trong thời hạn |
| 5 | `142-2026-ND-CP_dieu-11_khoan-1_diem-b` | `142-2026-ND-CP_dieu-11` | 22.053020 | Hệ thống xảy ra sự cố nghiêm trọng chứng minh mức độ rủi ro thực tế cao hơn mức đã được phân loại; |

Possible failure type: **lexical mismatch**

---

## eval002

Query: Ai có thẩm quyền ban hành danh mục hệ thống trí tuệ nhân tạo có rủi ro cao?  
Difficulty: easy  
Query type: authority

Gold article IDs:
- `142-2026-ND-CP_dieu-7`

Gold chunk IDs:
- `142-2026-ND-CP_dieu-7_khoan-2_diem-d`

Top-5 retrieved chunks:

| rank | chunk_id | article_id | score | text excerpt |
|---:|---|---|---:|---|
| 1 | `142-2026-ND-CP_dieu-7_khoan-1_diem-a` | `142-2026-ND-CP_dieu-7` | 28.500710 | Danh mục các hệ thống trí tuệ nhân tạo được xác định là có rủi ro cao; |
| 2 | `142-2026-ND-CP_dieu-7_khoan-1_diem-b` | `142-2026-ND-CP_dieu-7` | 27.672165 | Danh mục các hệ thống trí tuệ nhân tạo có rủi ro cao phải chứng nhận sự phù hợp trước khi đưa vào sử dụng. |
| 3 | `142-2026-ND-CP_dieu-7_khoan-2_diem-c` | `142-2026-ND-CP_dieu-7` | 25.903154 | Cơ quan trung ương của tổ chức chính trị, tổ chức chính trị - xã hội có quyền đề xuất bổ sung vào Danh mục đối với các hệ thống trí tuệ nhân tạo có rủi ro cao được sử dụng trong công tác đánh giá, quy hoạch, luân chuyển, |
| 4 | `142-2026-ND-CP_dieu-7_khoan-2_diem-a` | `142-2026-ND-CP_dieu-7` | 25.668343 | Ủy ban nhân dân cấp tỉnh trong phạm vi nhiệm vụ, quyền hạn của mình có trách nhiệm rà soát, đánh giá việc triển khai hệ thống trí tuệ nhân tạo trên địa bàn; đề xuất sửa đổi, bổ sung Danh mục và gửi bộ quản lý ngành, lĩnh |
| 5 | `142-2026-ND-CP_dieu-7_khoan-2_diem-b` | `142-2026-ND-CP_dieu-7` | 25.528553 | Các bộ, cơ quan ngang bộ trong phạm vi nhiệm vụ, quyền hạn của mình chịu trách nhiệm rà soát, đánh giá và đề xuất, sửa đổi, bổ sung Danh mục đối với hệ thống trí tuệ nhân tạo thuộc lĩnh vực quản lý, gửi Bộ Khoa học và Cô |

Possible failure type: **alias**

---

## eval004

Query: Nhà cung cấp hệ thống AI rủi ro cao phải duy trì những biện pháp quản lý nào?  
Difficulty: medium  
Query type: actor_obligation

Gold article IDs:
- `142-2026-ND-CP_dieu-15`

Gold chunk IDs:
- `142-2026-ND-CP_dieu-15_khoan-1`
- `142-2026-ND-CP_dieu-15_khoan-2_diem-a`
- `142-2026-ND-CP_dieu-15_khoan-2_diem-b`
- `142-2026-ND-CP_dieu-15_khoan-2_diem-c`
- `142-2026-ND-CP_dieu-15_khoan-2_diem-d`
- `142-2026-ND-CP_dieu-15_khoan-2_diem-đ`

Top-5 retrieved chunks:

| rank | chunk_id | article_id | score | text excerpt |
|---:|---|---|---:|---|
| 1 | `142-2026-ND-CP_dieu-15_khoan-1` | `142-2026-ND-CP_dieu-15` | 21.865478 | Nhà cung cấp hệ thống trí tuệ nhân tạo có rủi ro cao phải thiết lập và duy trì hệ thống quản lý rủi ro đối với hệ thống do mình cung cấp phù hợp với mục đích sử dụng, phạm vi triển khai và mức độ rủi ro của hệ thống. |
| 2 | `134-2025-QH15_dieu-14_khoan-1_diem-a` | `134-2025-QH15_dieu-14` | 20.568262 | Thiết lập và duy trì biện pháp quản lý rủi ro và thường xuyên rà soát khi hệ thống có thay đổi đáng kể hoặc phát sinh rủi ro mới; |
| 3 | `134-2025-QH15_dieu-14_khoan-2_diem-c` | `134-2025-QH15_dieu-14` | 16.222403 | Duy trì việc tuân thủ tiêu chuẩn, quy chuẩn kỹ thuật về trí tuệ nhân tạo trong quá trình vận hành hệ thống; |
| 4 | `134-2025-QH15_dieu-14_khoan-6` | `134-2025-QH15_dieu-14` | 15.946447 | Nhà cung cấp nước ngoài có hệ thống trí tuệ nhân tạo có rủi ro cao được cung cấp tại Việt Nam phải có đầu mối liên hệ hợp pháp tại Việt Nam; trường hợp hệ thống thuộc diện bắt buộc chứng nhận sự phù hợp trước khi đưa vào |
| 5 | `142-2026-ND-CP_dieu-10_khoan-2` | `142-2026-ND-CP_dieu-10` | 15.931823 | Nhà cung cấp không bắt buộc phải sử dụng Công cụ hỗ trợ phân loại rủi ro tự động quy định tại khoản 1 Điều này. Cơ quan nhà nước có thẩm quyền không được yêu cầu nhà cung cấp phải nộp kết quả phân loại xuất từ Công cụ nà |

Possible failure type: **multi-chunk coverage**

---

## eval005a

Query: Nhà cung cấp hệ thống trí tuệ nhân tạo có rủi ro cao phải thực hiện những nghĩa vụ quản lý nào?  
Difficulty: hard  
Query type: actor_obligation

Gold article IDs:
- `134-2025-QH15_dieu-14`

Gold chunk IDs:
- `134-2025-QH15_dieu-14_khoan-1_diem-a`
- `134-2025-QH15_dieu-14_khoan-1_diem-b`
- `134-2025-QH15_dieu-14_khoan-1_diem-c`
- `134-2025-QH15_dieu-14_khoan-1_diem-d`
- `134-2025-QH15_dieu-14_khoan-1_diem-đ`
- `134-2025-QH15_dieu-14_khoan-1_diem-e`
- `134-2025-QH15_dieu-14_khoan-1_diem-g`

Top-5 retrieved chunks:

| rank | chunk_id | article_id | score | text excerpt |
|---:|---|---|---:|---|
| 1 | `134-2025-QH15_dieu-14_khoan-6` | `134-2025-QH15_dieu-14` | 24.711711 | Nhà cung cấp nước ngoài có hệ thống trí tuệ nhân tạo có rủi ro cao được cung cấp tại Việt Nam phải có đầu mối liên hệ hợp pháp tại Việt Nam; trường hợp hệ thống thuộc diện bắt buộc chứng nhận sự phù hợp trước khi đưa vào |
| 2 | `134-2025-QH15_dieu-14_khoan-5` | `134-2025-QH15_dieu-14` | 24.596076 | Khuyến khích nhà cung cấp, bên triển khai tham gia bảo hiểm trách nhiệm dân sự hoặc áp dụng biện pháp bảo đảm thực hiện nghĩa vụ phù hợp khác để kịp thời khắc phục sự cố và bồi thường thiệt hại. |
| 3 | `142-2026-ND-CP_dieu-15_khoan-1` | `142-2026-ND-CP_dieu-15` | 23.844765 | Nhà cung cấp hệ thống trí tuệ nhân tạo có rủi ro cao phải thiết lập và duy trì hệ thống quản lý rủi ro đối với hệ thống do mình cung cấp phù hợp với mục đích sử dụng, phạm vi triển khai và mức độ rủi ro của hệ thống. |
| 4 | `134-2025-QH15_dieu-14_khoan-1_diem-đ` | `134-2025-QH15_dieu-14` | 23.248946 | Thực hiện nghĩa vụ minh bạch và xử lý sự cố theo quy định tại Điều 11 và Điều 12 của Luật này; |
| 5 | `134-2025-QH15_dieu-14_khoan-2_diem-d` | `134-2025-QH15_dieu-14` | 23.248946 | Thực hiện nghĩa vụ minh bạch và xử lý sự cố theo quy định tại Điều 11 và Điều 12 của Luật này; |

Possible failure type: **multi-chunk coverage**

---

## eval005b

Query: Bên triển khai hệ thống trí tuệ nhân tạo có rủi ro cao phải thực hiện những nghĩa vụ quản lý nào?  
Difficulty: hard  
Query type: actor_obligation

Gold article IDs:
- `134-2025-QH15_dieu-14`

Gold chunk IDs:
- `134-2025-QH15_dieu-14_khoan-2_diem-a`
- `134-2025-QH15_dieu-14_khoan-2_diem-b`
- `134-2025-QH15_dieu-14_khoan-2_diem-c`
- `134-2025-QH15_dieu-14_khoan-2_diem-d`
- `134-2025-QH15_dieu-14_khoan-2_diem-đ`
- `134-2025-QH15_dieu-14_khoan-2_diem-e`

Top-5 retrieved chunks:

| rank | chunk_id | article_id | score | text excerpt |
|---:|---|---|---:|---|
| 1 | `134-2025-QH15_dieu-14_khoan-5` | `134-2025-QH15_dieu-14` | 25.603723 | Khuyến khích nhà cung cấp, bên triển khai tham gia bảo hiểm trách nhiệm dân sự hoặc áp dụng biện pháp bảo đảm thực hiện nghĩa vụ phù hợp khác để kịp thời khắc phục sự cố và bồi thường thiệt hại. |
| 2 | `142-2026-ND-CP_dieu-15_khoan-4` | `142-2026-ND-CP_dieu-15` | 24.303689 | Bên triển khai hệ thống trí tuệ nhân tạo có rủi ro cao phải tổ chức quản lý rủi ro trong quá trình triển khai và vận hành hệ thống phù hợp với mục đích sử dụng, phạm vi triển khai, mức độ rủi ro của hệ thống và hướng dẫn |
| 3 | `134-2025-QH15_dieu-14_khoan-1_diem-đ` | `134-2025-QH15_dieu-14` | 23.248946 | Thực hiện nghĩa vụ minh bạch và xử lý sự cố theo quy định tại Điều 11 và Điều 12 của Luật này; |
| 4 | `134-2025-QH15_dieu-14_khoan-2_diem-d` | `134-2025-QH15_dieu-14` | 23.248946 | Thực hiện nghĩa vụ minh bạch và xử lý sự cố theo quy định tại Điều 11 và Điều 12 của Luật này; |
| 5 | `142-2026-ND-CP_dieu-11_khoan-2` | `142-2026-ND-CP_dieu-11` | 22.807566 | Bên triển khai phải phối hợp với nhà cung cấp thực hiện phân loại lại hệ thống trí tuệ nhân tạo trong trường hợp bên triển khai thực hiện sửa đổi, tích hợp hoặc thay đổi chức năng làm phát sinh rủi ro mới hoặc rủi ro cao |

Possible failure type: **multi-chunk coverage**

---

## eval007

Query: Nội dung do AI tạo ra phải được thông báo hoặc gắn nhãn như thế nào?  
Difficulty: hard  
Query type: transparency

Gold article IDs:
- `142-2026-ND-CP_dieu-18`

Gold chunk IDs:
- `142-2026-ND-CP_dieu-18_khoan-3_diem-a`
- `142-2026-ND-CP_dieu-18_khoan-3_diem-b`
- `142-2026-ND-CP_dieu-18_khoan-3_diem-c`
- `142-2026-ND-CP_dieu-18_khoan-3_diem-d`
- `142-2026-ND-CP_dieu-18_khoan-3_diem-đ`
- `142-2026-ND-CP_dieu-18_khoan-5_diem-a`
- `142-2026-ND-CP_dieu-18_khoan-5_diem-b`
- `142-2026-ND-CP_dieu-18_khoan-5_diem-c`
- `142-2026-ND-CP_dieu-18_khoan-5_diem-d`

Top-5 retrieved chunks:

| rank | chunk_id | article_id | score | text excerpt |
|---:|---|---|---:|---|
| 1 | `142-2026-ND-CP_dieu-18_khoan-6` | `142-2026-ND-CP_dieu-18` | 29.270588 | Đối với tác phẩm điện ảnh, chương trình nghệ thuật hoặc nội dung sáng tạo, việc thông báo và gắn nhãn hiển thị do bên triển khai trực tiếp đưa nội dung ra công cộng thực hiện và có thể được thực hiện tại phần mở đầu, phầ |
| 2 | `142-2026-ND-CP_dieu-18_khoan-1` | `142-2026-ND-CP_dieu-18` | 26.513518 | Bên triển khai phải thông báo rõ ràng khi cung cấp ra công cộng nội dung do hệ thống trí tuệ nhân tạo tạo ra hoặc chỉnh sửa có khả năng gây nhầm lẫn về tính xác thực của sự kiện, nhân vật hoặc nguồn gốc nội dung theo quy |
| 3 | `142-2026-ND-CP_dieu-18_khoan-4_diem-d` | `142-2026-ND-CP_dieu-18` | 25.642398 | Nội dung được tạo ra trong quá trình nghiên cứu, phát triển hoặc thử nghiệm trong môi trường kiểm soát và không được cung cấp ra công cộng. |
| 4 | `142-2026-ND-CP_dieu-18_khoan-3_diem-b` | `142-2026-ND-CP_dieu-18` | 25.106758 | Được thực hiện trước hoặc tại thời điểm người tiếp nhận tiếp cận nội dung; |
| 5 | `142-2026-ND-CP_dieu-18_khoan-4_diem-c` | `142-2026-ND-CP_dieu-18` | 24.852874 | Nội dung được sử dụng trong phạm vi nội bộ của cơ quan, tổ chức, doanh nghiệp và không được cung cấp ra công cộng; |

Possible failure type: **multi-chunk coverage**

---

## eval010

Query: Nhà cung cấp cần làm gì khi phát hiện sự cố liên quan đến hệ thống trí tuệ nhân tạo?  
Difficulty: easy  
Query type: incident

Gold article IDs:
- `134-2025-QH15_dieu-12`

Gold chunk IDs:
- `134-2025-QH15_dieu-12_khoan-2_diem-a`

Top-5 retrieved chunks:

| rank | chunk_id | article_id | score | text excerpt |
|---:|---|---|---:|---|
| 1 | `134-2025-QH15_dieu-10_khoan-5_diem-c` | `134-2025-QH15_dieu-10` | 22.223315 | Hệ thống trí tuệ nhân tạo có rủi ro thấp được theo dõi, kiểm tra khi có sự cố, phản ánh hoặc khi cần bảo đảm an toàn, không làm phát sinh nghĩa vụ không cần thiết cho tổ chức, cá nhân. |
| 2 | `142-2026-ND-CP_dieu-20_khoan-8` | `142-2026-ND-CP_dieu-20` | 20.072054 | Bộ Khoa học và Công nghệ có trách nhiệm theo dõi, giám sát việc thực hiện đánh giá tác động đối với việc sử dụng hệ thống trí tuệ nhân tạo trong cơ quan nhà nước; tổng hợp, báo cáo Thủ tướng Chính phủ khi cần thiết. |
| 3 | `134-2025-QH15_dieu-12_khoan-3` | `134-2025-QH15_dieu-12` | 19.536711 | Cơ quan quản lý nhà nước có thẩm quyền tiếp nhận, xác minh và hướng dẫn xử lý sự cố; khi cần thiết, có quyền yêu cầu tạm dừng, thu hồi hoặc đánh giá lại hệ thống trí tuệ nhân tạo. |
| 4 | `134-2025-QH15_dieu-12_khoan-1` | `134-2025-QH15_dieu-12` | 19.289118 | Nhà phát triển, nhà cung cấp, bên triển khai và người sử dụng hệ thống trí tuệ nhân tạo có trách nhiệm bảo đảm an toàn, an ninh, độ tin cậy và kịp thời phát hiện, khắc phục sự cố có khả năng gây tổn hại đến con người, tà |
| 5 | `134-2025-QH15_dieu-14_khoan-1_diem-c` | `134-2025-QH15_dieu-14` | 19.199525 | Lập, cập nhật, lưu giữ hồ sơ kỹ thuật và nhật ký hoạt động ở mức cần thiết cho việc đánh giá sự phù hợp và kiểm tra sau khi đưa vào sử dụng; cung cấp các thông tin này cho cơ quan nhà nước có thẩm quyền theo nguyên tắc c |

Possible failure type: **lexical mismatch**

---

## eval011

Query: Cơ chế thử nghiệm có kiểm soát cho phép tổ chức, cá nhân được hưởng những cơ chế gì trong phạm vi thử nghiệm?  
Difficulty: medium  
Query type: sandbox

Gold article IDs:
- `134-2025-QH15_dieu-21`

Gold chunk IDs:
- `134-2025-QH15_dieu-21_khoan-2_diem-a`
- `134-2025-QH15_dieu-21_khoan-2_diem-b`

Top-5 retrieved chunks:

| rank | chunk_id | article_id | score | text excerpt |
|---:|---|---|---:|---|
| 1 | `142-2026-ND-CP_dieu-26_khoan-2_diem-c` | `142-2026-ND-CP_dieu-26` | 31.868007 | Chỉ hỗ trợ đối với chi phí phục vụ trực tiếp cho hoạt động thử nghiệm có kiểm soát trong phạm vi thử nghiệm đã được cơ quan có thẩm quyền chấp thuận; |
| 2 | `142-2026-ND-CP_dieu-23_khoan-1` | `142-2026-ND-CP_dieu-23` | 31.467476 | Cơ quan nhà nước có thẩm quyền chấp thuận việc tham gia cơ chế thử nghiệm có kiểm soát đối với hệ thống trí tuệ nhân tạo theo quy định tại Điều 21 Luật Trí tuệ nhân tạo và Nghị định này. Giấy xác nhận là căn cứ để tổ chứ |
| 3 | `142-2026-ND-CP_dieu-27_khoan-3` | `142-2026-ND-CP_dieu-27` | 30.983013 | Tổ chức, cá nhân tham gia thử nghiệm được tiếp tục vận hành hệ thống trí tuệ nhân tạo trong thời gian chuyển tiếp không quá 12 tháng kể từ ngày được cấp Giấy xác nhận hoàn thành thử nghiệm có kiểm soát, trong phạm vi, đi |
| 4 | `142-2026-ND-CP_dieu-25_khoan-1_diem-c` | `142-2026-ND-CP_dieu-25` | 30.555941 | Quyết định tạm dừng thử nghiệm, chấm dứt thử nghiệm hoặc hiệu lực giấy xác nhận tham gia cơ chế thử nghiệm có kiểm soát khi tổ chức, cá nhân vi phạm các giới hạn thử nghiệm hoặc không khắc phục sự cố theo yêu cầu của cơ  |
| 5 | `142-2026-ND-CP_dieu-26_khoan-2_diem-a` | `142-2026-ND-CP_dieu-26` | 30.007277 | Thực hiện theo cơ chế đồng chi trả giữa Nhà nước và tổ chức, cá nhân tham gia thử nghiệm; |

Possible failure type: **lexical mismatch**

---

## eval012

Query: Cơ quan nào quyết định chấp thuận tham gia cơ chế thử nghiệm có kiểm soát?  
Difficulty: medium  
Query type: authority

Gold article IDs:
- `142-2026-ND-CP_dieu-23`

Gold chunk IDs:
- `142-2026-ND-CP_dieu-23_khoan-3_diem-a`
- `142-2026-ND-CP_dieu-23_khoan-3_diem-b`
- `142-2026-ND-CP_dieu-23_khoan-3_diem-c`

Top-5 retrieved chunks:

| rank | chunk_id | article_id | score | text excerpt |
|---:|---|---|---:|---|
| 1 | `142-2026-ND-CP_dieu-23_khoan-6` | `142-2026-ND-CP_dieu-23` | 29.705148 | Trường hợp từ chối chấp thuận, cơ quan có thẩm quyền phải trả lời bằng văn bản và nêu rõ lý do. |
| 2 | `142-2026-ND-CP_dieu-23_khoan-1` | `142-2026-ND-CP_dieu-23` | 28.986056 | Cơ quan nhà nước có thẩm quyền chấp thuận việc tham gia cơ chế thử nghiệm có kiểm soát đối với hệ thống trí tuệ nhân tạo theo quy định tại Điều 21 Luật Trí tuệ nhân tạo và Nghị định này. Giấy xác nhận là căn cứ để tổ chứ |
| 3 | `142-2026-ND-CP_dieu-23_khoan-7_diem-b` | `142-2026-ND-CP_dieu-23` | 27.748716 | Quy mô và giới hạn thử nghiệm; |
| 4 | `142-2026-ND-CP_dieu-23_khoan-7_diem-a` | `142-2026-ND-CP_dieu-23` | 27.468970 | Phạm vi, địa bàn và thời gian thử nghiệm; |
| 5 | `142-2026-ND-CP_dieu-23_khoan-7_diem-đ` | `142-2026-ND-CP_dieu-23` | 27.468970 | Trường hợp tạm dừng hoặc chấm dứt thử nghiệm; |

Possible failure type: **lexical mismatch**

---

## eval013

Query: Việc phân loại cấp độ thử nghiệm có kiểm soát dựa trên những tiêu chí nào?  
Difficulty: medium  
Query type: sandbox

Gold article IDs:
- `142-2026-ND-CP_dieu-22`

Gold chunk IDs:
- `142-2026-ND-CP_dieu-22_khoan-1_diem-a`
- `142-2026-ND-CP_dieu-22_khoan-1_diem-b`
- `142-2026-ND-CP_dieu-22_khoan-1_diem-c`
- `142-2026-ND-CP_dieu-22_khoan-1_diem-d`
- `142-2026-ND-CP_dieu-22_khoan-2`

Top-5 retrieved chunks:

| rank | chunk_id | article_id | score | text excerpt |
|---:|---|---|---:|---|
| 1 | `142-2026-ND-CP_dieu-22_khoan-6` | `142-2026-ND-CP_dieu-22` | 25.540442 | Cơ quan nhà nước có thẩm quyền xác định cấp độ thử nghiệm có kiểm soát đối với hệ thống trí tuệ nhân tạo trên cơ sở các tiêu chí quy định tại Điều này khi tiếp nhận và xử lý hồ sơ tham gia cơ chế thử nghiệm có kiểm soát. |
| 2 | `142-2026-ND-CP_dieu-22_khoan-2` | `142-2026-ND-CP_dieu-22` | 25.083276 | Trường hợp hệ thống trí tuệ nhân tạo đồng thời đáp ứng tiêu chí của nhiều cấp độ thử nghiệm khác nhau thì hệ thống được phân loại theo cấp độ thử nghiệm cao nhất. Việc phân loại cấp độ thử nghiệm được xác định trên cơ sở |
| 3 | `142-2026-ND-CP_dieu-22_khoan-5_diem-a` | `142-2026-ND-CP_dieu-22` | 23.348067 | Đối tượng tham gia thử nghiệm được xác định theo tiêu chí cụ thể; |
| 4 | `142-2026-ND-CP_dieu-44_khoan-5` | `142-2026-ND-CP_dieu-44` | 17.146403 | Tiếp nhận, thẩm định và cấp văn bản chấp thuận tham gia cơ chế thử nghiệm có kiểm soát đối với hệ thống trí tuệ nhân tạo cấp độ 1 và cấp độ 2 thuộc thẩm quyền; phối hợp với Bộ Khoa học và Công nghệ trong việc tổ chức tri |
| 5 | `142-2026-ND-CP_dieu-22_khoan-1_diem-a` | `142-2026-ND-CP_dieu-22` | 16.790073 | Mức độ rủi ro của hệ thống trí tuệ nhân tạo theo quy định của Luật Trí tuệ nhân tạo; |

Possible failure type: **multi-chunk coverage**

---

## eval014

Query: Hồ sơ thông thường để tham gia cơ chế thử nghiệm có kiểm soát gồm những thành phần nào?  
Difficulty: medium  
Query type: procedure

Gold article IDs:
- `142-2026-ND-CP_dieu-24`

Gold chunk IDs:
- `142-2026-ND-CP_dieu-24_khoan-2_diem-a`
- `142-2026-ND-CP_dieu-24_khoan-2_diem-b`
- `142-2026-ND-CP_dieu-24_khoan-2_diem-c`
- `142-2026-ND-CP_dieu-24_khoan-2_diem-d`

Top-5 retrieved chunks:

| rank | chunk_id | article_id | score | text excerpt |
|---:|---|---|---:|---|
| 1 | `142-2026-ND-CP_dieu-24_khoan-5` | `142-2026-ND-CP_dieu-24` | 30.195379 | Cơ quan nhà nước có thẩm quyền không được yêu cầu tổ chức, cá nhân cung cấp thêm thành phần hồ sơ ngoài quy định tại Điều này, trừ trường hợp pháp luật chuyên ngành quy định trực tiếp thành phần hồ sơ đối với hoạt động t |
| 2 | `142-2026-ND-CP_dieu-23_khoan-4` | `142-2026-ND-CP_dieu-23` | 24.543169 | Trong thời hạn 03 ngày làm việc kể từ ngày nhận hồ sơ, cơ quan có thẩm quyền phải kiểm tra tính hợp lệ của hồ sơ và thông báo một lần bằng văn bản điện tử về yêu cầu sửa đổi, bổ sung hồ sơ. |
| 3 | `142-2026-ND-CP_dieu-23_khoan-2` | `142-2026-ND-CP_dieu-23` | 24.206620 | Tổ chức, cá nhân nộp 01 bộ hồ sơ bằng phương thức điện tử thông qua cổng Dịch vụ công quốc gia để tiếp nhận, xử lý theo quy định của pháp luật. Hồ sơ được liên thông, đồng bộ về cổng thông tin điện tử một cửa về trí tuệ  |
| 4 | `142-2026-ND-CP_dieu-22_khoan-6` | `142-2026-ND-CP_dieu-22` | 22.401349 | Cơ quan nhà nước có thẩm quyền xác định cấp độ thử nghiệm có kiểm soát đối với hệ thống trí tuệ nhân tạo trên cơ sở các tiêu chí quy định tại Điều này khi tiếp nhận và xử lý hồ sơ tham gia cơ chế thử nghiệm có kiểm soát. |
| 5 | `142-2026-ND-CP_dieu-24_khoan-2_diem-a` | `142-2026-ND-CP_dieu-24` | 22.267946 | Đơn đề nghị tham gia cơ chế thử nghiệm có kiểm soát theo Mẫu AI03a đối với tổ chức hoặc Mẫu AI03b đối với cá nhân tại Phụ lục ban hành kèm theo Nghị định này; |

Possible failure type: **multi-chunk coverage**

---

## eval016

Query: Tổ chức hoặc cá nhân phải báo cáo gì trong quá trình thử nghiệm có kiểm soát?  
Difficulty: medium  
Query type: procedure

Gold article IDs:
- `142-2026-ND-CP_dieu-25`

Gold chunk IDs:
- `142-2026-ND-CP_dieu-25_khoan-2_diem-a`
- `142-2026-ND-CP_dieu-25_khoan-2_diem-b`
- `142-2026-ND-CP_dieu-25_khoan-3_diem-a`
- `142-2026-ND-CP_dieu-25_khoan-3_diem-b`
- `142-2026-ND-CP_dieu-25_khoan-4`

Top-5 retrieved chunks:

| rank | chunk_id | article_id | score | text excerpt |
|---:|---|---|---:|---|
| 1 | `142-2026-ND-CP_dieu-25_khoan-4` | `142-2026-ND-CP_dieu-25` | 27.560938 | Chậm nhất 15 ngày trước khi kết thúc thời hạn thử nghiệm, tổ chức, cá nhân tham gia thử nghiệm phải nộp báo cáo tổng kết kết quả thử nghiệm thông qua cổng thông tin điện tử một cửa về trí tuệ nhân tạo theo Mẫu AI08a đối  |
| 2 | `142-2026-ND-CP_dieu-25_khoan-3_diem-b` | `142-2026-ND-CP_dieu-25` | 26.318932 | Hệ thống trí tuệ nhân tạo vượt giới hạn thử nghiệm đã được xác định trong giấy xác nhận. Báo cáo sự cố được thực hiện theo Mẫu AI06a đối với tổ chức hoặc Mẫu AI06b đối với cá nhân; báo cáo vượt giới hạn thử nghiệm được t |
| 3 | `142-2026-ND-CP_dieu-25_khoan-1_diem-b` | `142-2026-ND-CP_dieu-25` | 25.329286 | Yêu cầu tổ chức, cá nhân tham gia thử nghiệm bổ sung biện pháp kiểm soát rủi ro hoặc đề xuất điều chỉnh phạm vi thử nghiệm để xem xét theo thẩm quyền khi phát sinh rủi ro ngoài phạm vi thử nghiệm; |
| 4 | `142-2026-ND-CP_dieu-25_khoan-1_diem-c` | `142-2026-ND-CP_dieu-25` | 25.237062 | Quyết định tạm dừng thử nghiệm, chấm dứt thử nghiệm hoặc hiệu lực giấy xác nhận tham gia cơ chế thử nghiệm có kiểm soát khi tổ chức, cá nhân vi phạm các giới hạn thử nghiệm hoặc không khắc phục sự cố theo yêu cầu của cơ  |
| 5 | `142-2026-ND-CP_dieu-25_khoan-1_diem-a` | `142-2026-ND-CP_dieu-25` | 24.585332 | Tiếp nhận và đánh giá báo cáo định kỳ, báo cáo sự cố, báo cáo vượt giới hạn và báo cáo tổng kết thử nghiệm theo quy định của Nghị định này; |

Possible failure type: **multi-chunk coverage**

---

## eval021

Query: Những loại dữ liệu nào có thể được đưa vào cơ sở dữ liệu phục vụ trí tuệ nhân tạo?  
Difficulty: easy  
Query type: data_governance

Gold article IDs:
- `142-2026-ND-CP_dieu-32`

Gold chunk IDs:
- `142-2026-ND-CP_dieu-32_khoan-1_diem-a`
- `142-2026-ND-CP_dieu-32_khoan-1_diem-b`
- `142-2026-ND-CP_dieu-32_khoan-1_diem-c`

Top-5 retrieved chunks:

| rank | chunk_id | article_id | score | text excerpt |
|---:|---|---|---:|---|
| 1 | `134-2025-QH15_dieu-17_khoan-1` | `134-2025-QH15_dieu-17` | 23.365684 | Cơ sở dữ liệu phục vụ trí tuệ nhân tạo là thành phần quan trọng của hạ tầng trí tuệ nhân tạo quốc gia, bao gồm Cơ sở dữ liệu quốc gia, cơ sở dữ liệu của Bộ, cơ quan ngang Bộ, cơ quan thuộc Chính phủ, Ủy ban nhân dân các  |
| 2 | `134-2025-QH15_dieu-17_khoan-3` | `134-2025-QH15_dieu-17` | 22.122502 | Cơ sở dữ liệu phục vụ trí tuệ nhân tạo của Bộ, cơ quan ngang Bộ, cơ quan thuộc Chính phủ và Ủy ban nhân dân các cấp được xây dựng, cập nhật và kết nối thống nhất với Cơ sở dữ liệu quốc gia về trí tuệ nhân tạo; bảo đảm ti |
| 3 | `134-2025-QH15_dieu-17_khoan-4` | `134-2025-QH15_dieu-17` | 21.704470 | Cơ sở dữ liệu của tổ chức, cá nhân phục vụ trí tuệ nhân tạo được khuyến khích chia sẻ với cơ quan nhà nước và tổ chức, cá nhân khác theo cơ chế thỏa thuận; việc chia sẻ phải tuân thủ pháp luật về dữ liệu, bảo vệ dữ liệu  |
| 4 | `134-2025-QH15_dieu-17_khoan-6` | `134-2025-QH15_dieu-17` | 21.303696 | Chính phủ quy định chi tiết về nguyên tắc kết nối, cơ chế chia sẻ, khai thác và bảo đảm an toàn dữ liệu trong cơ sở dữ liệu phục vụ trí tuệ nhân tạo. |
| 5 | `134-2025-QH15_dieu-17_khoan-2` | `134-2025-QH15_dieu-17` | 20.770506 | Cơ sở dữ liệu quốc gia về trí tuệ nhân tạo do Nhà nước đầu tư, xây dựng và vận hành tại Trung tâm dữ liệu quốc gia; được tổ chức theo nguyên tắc mở, an toàn, có kiểm soát, đáp ứng yêu cầu về chất lượng, khả năng kết nối  |

Possible failure type: **lexical mismatch**

---

## eval022

Query: Cơ quan quản lý có trách nhiệm gì đối với việc xây dựng và cập nhật dữ liệu mở phục vụ AI?  
Difficulty: medium  
Query type: actor_obligation

Gold article IDs:
- `142-2026-ND-CP_dieu-32`

Gold chunk IDs:
- `142-2026-ND-CP_dieu-32_khoan-5_diem-a`
- `142-2026-ND-CP_dieu-32_khoan-5_diem-b`
- `142-2026-ND-CP_dieu-32_khoan-5_diem-c`

Top-5 retrieved chunks:

| rank | chunk_id | article_id | score | text excerpt |
|---:|---|---|---:|---|
| 1 | `142-2026-ND-CP_dieu-32_khoan-5_diem-a` | `142-2026-ND-CP_dieu-32` | 29.655199 | Xây dựng, cập nhật dữ liệu mở, dữ liệu mở có điều kiện, dữ liệu thương mại thuộc phạm vi quản lý; |
| 2 | `134-2025-QH15_dieu-17_khoan-3` | `134-2025-QH15_dieu-17` | 22.063331 | Cơ sở dữ liệu phục vụ trí tuệ nhân tạo của Bộ, cơ quan ngang Bộ, cơ quan thuộc Chính phủ và Ủy ban nhân dân các cấp được xây dựng, cập nhật và kết nối thống nhất với Cơ sở dữ liệu quốc gia về trí tuệ nhân tạo; bảo đảm ti |
| 3 | `134-2025-QH15_dieu-17_khoan-2` | `134-2025-QH15_dieu-17` | 20.284659 | Cơ sở dữ liệu quốc gia về trí tuệ nhân tạo do Nhà nước đầu tư, xây dựng và vận hành tại Trung tâm dữ liệu quốc gia; được tổ chức theo nguyên tắc mở, an toàn, có kiểm soát, đáp ứng yêu cầu về chất lượng, khả năng kết nối  |
| 4 | `142-2026-ND-CP_dieu-42_khoan-2` | `142-2026-ND-CP_dieu-42` | 19.890638 | Chủ trì tổ chức xây dựng, vận hành và cung cấp hạ tầng trí tuệ nhân tạo phục vụ quản lý nhà nước tập trung tại các trung tâm dữ liệu quốc gia theo quy định tại khoản 6 Điều 28 của Nghị định này; phối hợp với Bộ Khoa học  |
| 5 | `142-2026-ND-CP_dieu-42_khoan-3` | `142-2026-ND-CP_dieu-42` | 18.599098 | Là cơ quan chủ quản, chịu trách nhiệm xây dựng, quản lý, vận hành Cơ sở dữ liệu quốc gia về trí tuệ nhân tạo tại Trung tâm dữ liệu quốc gia theo quy định của Nghị định này và pháp luật về dữ liệu. |

Possible failure type: **alias**

---

## eval025

Query: Khi ứng dụng AI trong quản lý nhà nước, cơ quan vận hành phải đánh giá tác động trong trường hợp nào?  
Difficulty: hard  
Query type: public_sector

Gold article IDs:
- `142-2026-ND-CP_dieu-20`

Gold chunk IDs:
- `142-2026-ND-CP_dieu-20_khoan-1_diem-a`
- `142-2026-ND-CP_dieu-20_khoan-1_diem-b`
- `142-2026-ND-CP_dieu-20_khoan-2`
- `142-2026-ND-CP_dieu-20_khoan-7_diem-a`
- `142-2026-ND-CP_dieu-20_khoan-7_diem-b`
- `142-2026-ND-CP_dieu-20_khoan-7_diem-c`
- `142-2026-ND-CP_dieu-20_khoan-7_diem-d`

Top-5 retrieved chunks:

| rank | chunk_id | article_id | score | text excerpt |
|---:|---|---|---:|---|
| 1 | `134-2025-QH15_dieu-27_khoan-3` | `134-2025-QH15_dieu-27` | 23.133665 | Cơ quan vận hành hệ thống trí tuệ nhân tạo có rủi ro cao hoặc có tác động đáng kể đến quyền con người, công bằng xã hội hoặc lợi ích công cộng phải lập báo cáo đánh giá tác động việc sử dụng hệ thống; báo cáo gồm việc xá |
| 2 | `142-2026-ND-CP_dieu-20_khoan-3_diem-d` | `142-2026-ND-CP_dieu-20` | 20.675106 | Cơ chế bảo đảm khả năng giám sát và can thiệp của con người trong quá trình vận hành hệ thống. |
| 3 | `142-2026-ND-CP_dieu-20_khoan-8` | `142-2026-ND-CP_dieu-20` | 20.596081 | Bộ Khoa học và Công nghệ có trách nhiệm theo dõi, giám sát việc thực hiện đánh giá tác động đối với việc sử dụng hệ thống trí tuệ nhân tạo trong cơ quan nhà nước; tổng hợp, báo cáo Thủ tướng Chính phủ khi cần thiết. |
| 4 | `134-2025-QH15_dieu-27_khoan-5` | `134-2025-QH15_dieu-27` | 20.186786 | Chính phủ quy định chi tiết nội dung, quy trình và trách nhiệm đánh giá tác động, quản lý rủi ro và giám sát việc sử dụng hệ thống trí tuệ nhân tạo trong quản lý nhà nước và cung cấp dịch vụ công. |
| 5 | `142-2026-ND-CP_dieu-20_khoan-5` | `142-2026-ND-CP_dieu-20` | 19.976884 | Cơ quan, đơn vị triển khai phải công khai báo cáo đánh giá tác động theo quy định tại khoản 4 Điều 27 Luật Trí tuệ nhân tạo, trừ nội dung thuộc bí mật nhà nước, bí mật kinh doanh hoặc dữ liệu cá nhân theo quy định của ph |

Possible failure type: **multi-chunk coverage**

---

## eval026

Query: Báo cáo đánh giá tác động khi sử dụng AI trong khu vực công cần đề cập những nội dung gì?  
Difficulty: medium  
Query type: public_sector

Gold article IDs:
- `142-2026-ND-CP_dieu-20`

Gold chunk IDs:
- `142-2026-ND-CP_dieu-20_khoan-3_diem-a`
- `142-2026-ND-CP_dieu-20_khoan-3_diem-b`
- `142-2026-ND-CP_dieu-20_khoan-3_diem-c`
- `142-2026-ND-CP_dieu-20_khoan-3_diem-d`

Top-5 retrieved chunks:

| rank | chunk_id | article_id | score | text excerpt |
|---:|---|---|---:|---|
| 1 | `134-2025-QH15_dieu-27_khoan-4` | `134-2025-QH15_dieu-27` | 24.471981 | Cơ quan lập báo cáo đánh giá tác động chịu trách nhiệm về nội dung, tính trung thực và đầy đủ của báo cáo; báo cáo được công khai theo quy định của pháp luật, trừ nội dung thuộc bí mật nhà nước, bí mật kinh doanh hoặc dữ |
| 2 | `142-2026-ND-CP_dieu-20_khoan-4` | `142-2026-ND-CP_dieu-20` | 22.609220 | Người đứng đầu cơ quan, đơn vị triển khai có trách nhiệm tổ chức lập, phê duyệt báo cáo đánh giá tác động trước khi đưa hệ thống trí tuệ nhân tạo vào sử dụng và chịu trách nhiệm trước pháp luật về nội dung, tính trung th |
| 3 | `142-2026-ND-CP_dieu-20_khoan-8` | `142-2026-ND-CP_dieu-20` | 22.117393 | Bộ Khoa học và Công nghệ có trách nhiệm theo dõi, giám sát việc thực hiện đánh giá tác động đối với việc sử dụng hệ thống trí tuệ nhân tạo trong cơ quan nhà nước; tổng hợp, báo cáo Thủ tướng Chính phủ khi cần thiết. |
| 4 | `142-2026-ND-CP_dieu-20_khoan-5` | `142-2026-ND-CP_dieu-20` | 20.177348 | Cơ quan, đơn vị triển khai phải công khai báo cáo đánh giá tác động theo quy định tại khoản 4 Điều 27 Luật Trí tuệ nhân tạo, trừ nội dung thuộc bí mật nhà nước, bí mật kinh doanh hoặc dữ liệu cá nhân theo quy định của ph |
| 5 | `134-2025-QH15_dieu-27_khoan-3` | `134-2025-QH15_dieu-27` | 19.088469 | Cơ quan vận hành hệ thống trí tuệ nhân tạo có rủi ro cao hoặc có tác động đáng kể đến quyền con người, công bằng xã hội hoặc lợi ích công cộng phải lập báo cáo đánh giá tác động việc sử dụng hệ thống; báo cáo gồm việc xá |

Possible failure type: **alias**

---

## eval027

Query: Nguyên tắc đạo đức khi phát triển và sử dụng trí tuệ nhân tạo được đặt ra như thế nào?  
Difficulty: medium  
Query type: ethics

Gold article IDs:
- `134-2025-QH15_dieu-26`

Gold chunk IDs:
- `134-2025-QH15_dieu-26_khoan-1_diem-a`
- `134-2025-QH15_dieu-26_khoan-1_diem-b`
- `134-2025-QH15_dieu-26_khoan-1_diem-c`
- `134-2025-QH15_dieu-26_khoan-1_diem-d`

Top-5 retrieved chunks:

| rank | chunk_id | article_id | score | text excerpt |
|---:|---|---|---:|---|
| 1 | `134-2025-QH15_dieu-27_khoan-2` | `134-2025-QH15_dieu-27` | 26.477088 | Hệ thống trí tuệ nhân tạo không thay thế thẩm quyền và trách nhiệm quyết định của người ra quyết định theo quy định của pháp luật. Người ra quyết định chịu trách nhiệm về việc xem xét và sử dụng kết quả do hệ thống trí t |
| 2 | `05-2026-TT-BKHCN_dieu-2_khoan-1` | `05-2026-TT-BKHCN_dieu-2` | 24.175414 | Đạo đức trí tuệ nhân tạo là hệ giá trị, nguyên tắc và chuẩn mực định hướng việc nghiên cứu, phát triển, cung cấp, triển khai và sử dụng trí tuệ nhân tạo nhằm bảo đảm tôn trọng con người, quyền con người, lợi ích công cộn |
| 3 | `134-2025-QH15_dieu-26_khoan-2` | `134-2025-QH15_dieu-26` | 21.438766 | Khung đạo đức trí tuệ nhân tạo quốc gia được rà soát, cập nhật định kỳ hoặc khi có thay đổi lớn về công nghệ, pháp luật và thực tiễn quản lý. |
| 4 | `142-2026-ND-CP_dieu-20_khoan-6` | `142-2026-ND-CP_dieu-20` | 21.409374 | Việc sử dụng hệ thống trí tuệ nhân tạo trong cơ quan nhà nước phải tuân thủ Khung đạo đức trí tuệ nhân tạo quốc gia và không thay thế thẩm quyền, trách nhiệm quyết định của người có thẩm quyền theo quy định tại khoản 1 v |
| 5 | `134-2025-QH15_dieu-27_khoan-1` | `134-2025-QH15_dieu-27` | 21.257089 | Việc sử dụng hệ thống trí tuệ nhân tạo trong quản lý nhà nước và cung cấp dịch vụ công phải bảo đảm công khai, minh bạch và có trách nhiệm tuân thủ Khung đạo đức trí tuệ nhân tạo quốc gia. |

Possible failure type: **lexical mismatch**

---
