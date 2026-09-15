# Human Review Report

## Review summary

| query_id | gold_articles | gold_chunks | flag_reason | recommended_action | confidence |
|---|---:|---:|---|---|---|
| eval004 | 1 | 6 | Có 6 gold chunks; cần xác nhận khoản mở đầu và năm điểm có cùng cần thiết hay không. | KEEP | high |
| eval005 | 1 | 17 | Gold hiện có 17 chunks và query không xác định chủ thể hay phạm vi của “việc quản lý”. | SPLIT_QUERY | high |
| eval007 | 1 | 9 | Có 9 chunks, cần phân biệt yêu cầu chung và cách thức triển khai nhãn/thông báo. | KEEP | high |
| eval014 | 1 | 6 | Gold trộn hồ sơ thông thường bốn tài liệu và hồ sơ rút gọn hai tài liệu. | REWRITE_QUERY | high |
| eval015 | 2 | 2 | Gold lấy hai Article thuộc Luật và Nghị định; cần xác định quan hệ nguyên tắc–chi tiết. | KEEP | high |
| eval025 | 1 | 7 | Có 7 chunks cho câu hỏi chỉ hỏi điều kiện kích hoạt đánh giá tác động. | KEEP | medium |
| eval029 | 1 | 2 | Query không nêu khu vực áp dụng trong khi corpus có quy định chung và quy định riêng cho khu vực công. | REWRITE_QUERY | medium |
| eval030 | 2 | 2 | Gold gồm Luật và Khung đạo đức dù chunk của Luật có thể tự trả lời đầy đủ. | REMOVE_CHUNK | high |

---

# eval004

## Query

Nhà cung cấp hệ thống AI rủi ro cao phải duy trì những biện pháp quản lý nào?

## Current annotation

Query type: actor_obligation  
Difficulty: medium  
Annotation status: in_review

Gold documents:
- 142-2026-ND-CP

Gold articles:
- 142-2026-ND-CP_dieu-15

Gold chunks:
- 142-2026-ND-CP_dieu-15_khoan-1
- 142-2026-ND-CP_dieu-15_khoan-2_diem-a
- 142-2026-ND-CP_dieu-15_khoan-2_diem-b
- 142-2026-ND-CP_dieu-15_khoan-2_diem-c
- 142-2026-ND-CP_dieu-15_khoan-2_diem-d
- 142-2026-ND-CP_dieu-15_khoan-2_diem-đ

## Why this query was flagged

Có 6 gold chunks; cần xác nhận khoản mở đầu và năm điểm có cùng cần thiết hay không.

## Article context

### Article 142-2026-ND-CP_dieu-15

Title: Quản lý hệ thống trí tuệ nhân tạo có rủi ro cao  
Document: Nghị định hướng dẫn thi hành Luật Trí tuệ nhân tạo (142/2026/NĐ-CP)  
Structure: Chương II — PHÂN LOẠI VÀ ĐÁNH GIÁ SỰ PHÙ HỢP HỆ THỐNG TRÍ TUỆ NHÂN TẠO  
Review role: PRIMARY

Article context:
- `142-2026-ND-CP_dieu-15_khoan-1` — Nhà cung cấp hệ thống trí tuệ nhân tạo có rủi ro cao phải thiết lập và duy trì hệ thống quản lý rủi ro đối với hệ thống do mình cung cấp phù hợp với mục đích sử dụng, phạm vi triển khai và mức độ rủi ro của hệ thống.
- `142-2026-ND-CP_dieu-15_khoan-2_diem-a` — Xác định và đánh giá các rủi ro có thể phát sinh đối với quyền con người, an toàn, an ninh hoặc lợi ích công cộng trong quá trình thiết kế, phát triển và cung cấp hệ thống;
- `142-2026-ND-CP_dieu-15_khoan-2_diem-b` — Bảo đảm chất lượng, tính phù hợp và tính đại diện của dữ liệu huấn luyện, dữ liệu kiểm thử và dữ liệu đánh giá trong phạm vi cần thiết để hạn chế rủi ro phát sinh từ dữ liệu;
- `142-2026-ND-CP_dieu-15_khoan-2_diem-c` — Thiết kế và duy trì cơ chế giám sát và can thiệp của con người phù hợp với mức độ rủi ro của hệ thống;
- `142-2026-ND-CP_dieu-15_khoan-2_diem-d` — Áp dụng biện pháp kỹ thuật hoặc biện pháp quản lý nhằm phòng ngừa, hạn chế hoặc kiểm soát các rủi ro đã được xác định;
- `142-2026-ND-CP_dieu-15_khoan-2_diem-đ` — Rà soát và cập nhật biện pháp quản lý rủi ro khi hệ thống có thay đổi đáng kể về mô hình, dữ liệu, phương thức vận hành hoặc mục đích sử dụng.
- `142-2026-ND-CP_dieu-15_khoan-3` — Nhà cung cấp có trách nhiệm cung cấp cho bên triển khai các thông tin cần thiết về mục đích sử dụng của hệ thống, điều kiện vận hành an toàn, các rủi ro đã được xác định và biện pháp quản lý rủi ro tương ứng để bảo đảm việc triển khai và sử dụng hệ thống đúng mục đích.
- `142-2026-ND-CP_dieu-15_khoan-4` — Bên triển khai hệ thống trí tuệ nhân tạo có rủi ro cao phải tổ chức quản lý rủi ro trong quá trình triển khai và vận hành hệ thống phù hợp với mục đích sử dụng, phạm vi triển khai, mức độ rủi ro của hệ thống và hướng dẫn kỹ thuật của nhà cung cấp.
- `142-2026-ND-CP_dieu-15_khoan-5_diem-a` — Vận hành hệ thống đúng mục đích sử dụng, điều kiện sử dụng và giới hạn sử dụng do nhà cung cấp xác định;
- `142-2026-ND-CP_dieu-15_khoan-5_diem-b` — Tổ chức giám sát hoạt động của hệ thống nhằm phát hiện sai lệch, rủi ro hoặc sự cố có thể phát sinh;
- `142-2026-ND-CP_dieu-15_khoan-5_diem-c` — Thiết lập và duy trì cơ chế giám sát và can thiệp của con người trong quá trình sử dụng hệ thống theo quy định của pháp luật;
- `142-2026-ND-CP_dieu-15_khoan-5_diem-d` — Áp dụng biện pháp hạn chế hoặc kiểm soát rủi ro trong phạm vi quyền kiểm soát của mình khi phát hiện hệ thống hoạt động không đúng mục đích sử dụng hoặc phát sinh rủi ro mới;
- `142-2026-ND-CP_dieu-15_khoan-5_diem-đ` — Phối hợp với nhà cung cấp trong việc rà soát, cập nhật biện pháp quản lý rủi ro khi hệ thống có thay đổi đáng kể hoặc khi phát sinh sự cố.
- `142-2026-ND-CP_dieu-15_khoan-6` — Trường hợp phát hiện hệ thống có nguy cơ gây thiệt hại nghiêm trọng đến tính mạng, sức khỏe con người, quyền con người, tài sản, an ninh mạng, trật tự, an toàn xã hội hoặc lợi ích công cộng, bên triển khai phải kịp thời áp dụng biện pháp hạn chế rủi ro trong phạm vi quyền kiểm soát của mình và thông báo cho nhà cung cấp và cơ quan nhà nước có thẩm quyền theo quy định của pháp luật.

## Gold chunk review

### Chunk 1

chunk_id: `142-2026-ND-CP_dieu-15_khoan-1`

Legal location: 142/2026/NĐ-CP, Điều 15, khoản 1

Text:

Nhà cung cấp hệ thống trí tuệ nhân tạo có rủi ro cao phải thiết lập và duy trì hệ thống quản lý rủi ro đối với hệ thống do mình cung cấp phù hợp với mục đích sử dụng, phạm vi triển khai và mức độ rủi ro của hệ thống.

Reason selected:

Cần để xác lập phạm vi/nghĩa vụ hoặc giải nghĩa dẫn chiếu, nhưng không tự nó là toàn bộ đáp án.

Assessment:
- SUPPORTING

### Chunk 2

chunk_id: `142-2026-ND-CP_dieu-15_khoan-2_diem-a`

Legal location: 142/2026/NĐ-CP, Điều 15, khoản 2, điểm a

Text:

Xác định và đánh giá các rủi ro có thể phát sinh đối với quyền con người, an toàn, an ninh hoặc lợi ích công cộng trong quá trình thiết kế, phát triển và cung cấp hệ thống;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 3

chunk_id: `142-2026-ND-CP_dieu-15_khoan-2_diem-b`

Legal location: 142/2026/NĐ-CP, Điều 15, khoản 2, điểm b

Text:

Bảo đảm chất lượng, tính phù hợp và tính đại diện của dữ liệu huấn luyện, dữ liệu kiểm thử và dữ liệu đánh giá trong phạm vi cần thiết để hạn chế rủi ro phát sinh từ dữ liệu;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 4

chunk_id: `142-2026-ND-CP_dieu-15_khoan-2_diem-c`

Legal location: 142/2026/NĐ-CP, Điều 15, khoản 2, điểm c

Text:

Thiết kế và duy trì cơ chế giám sát và can thiệp của con người phù hợp với mức độ rủi ro của hệ thống;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 5

chunk_id: `142-2026-ND-CP_dieu-15_khoan-2_diem-d`

Legal location: 142/2026/NĐ-CP, Điều 15, khoản 2, điểm d

Text:

Áp dụng biện pháp kỹ thuật hoặc biện pháp quản lý nhằm phòng ngừa, hạn chế hoặc kiểm soát các rủi ro đã được xác định;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 6

chunk_id: `142-2026-ND-CP_dieu-15_khoan-2_diem-đ`

Legal location: 142/2026/NĐ-CP, Điều 15, khoản 2, điểm đ

Text:

Rà soát và cập nhật biện pháp quản lý rủi ro khi hệ thống có thay đổi đáng kể về mô hình, dữ liệu, phương thức vận hành hoặc mục đích sử dụng.

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

## Coverage analysis

Câu hỏi cần trả lời những ý nào?
1. Nghĩa vụ thiết lập và duy trì hệ thống quản lý rủi ro.
2. Nhận diện, đánh giá rủi ro.
3. Quản trị chất lượng dữ liệu.
4. Giám sát và can thiệp của con người.
5. Biện pháp kỹ thuật/quản lý để kiểm soát rủi ro.
6. Rà soát, cập nhật khi hệ thống thay đổi.

Gold hiện tại có bao phủ từng ý không?
- Ý 1 → `142-2026-ND-CP_dieu-15_khoan-1`.
- Ý 2 → `142-2026-ND-CP_dieu-15_khoan-2_diem-a`.
- Ý 3 → `142-2026-ND-CP_dieu-15_khoan-2_diem-b`.
- Ý 4 → `142-2026-ND-CP_dieu-15_khoan-2_diem-c`.
- Ý 5 → `142-2026-ND-CP_dieu-15_khoan-2_diem-d`.
- Ý 6 → `142-2026-ND-CP_dieu-15_khoan-2_diem-đ`.

Missing coverage:

Không.

Potential unnecessary chunks:

Không. Khoản 1 là mệnh đề nghĩa vụ chính; năm điểm khoản 2 là toàn bộ nội dung cấu thành hệ thống quản lý rủi ro.

## Ambiguity

Thấp. Cụm “duy trì những biện pháp quản lý” khớp hệ thống quản lý rủi ro và danh sách năm biện pháp của nhà cung cấp.

## Recommended human decision

Suggested action: **KEEP**

Reason:

Cả 6 chunks tạo thành một quy định hoàn chỉnh: khoản 1 xác lập nghĩa vụ, năm điểm của khoản 2 liệt kê các biện pháp.

## Human decision

- [ ] KEEP
- [ ] REMOVE_CHUNK
- [ ] ADD_CHUNK
- [ ] REWRITE_QUERY
- [ ] SPLIT_QUERY
- [ ] NEEDS_REVIEW

Human notes:


---

# eval005

## Query

Khi một hệ thống được xếp vào nhóm rủi ro cao thì việc quản lý được thực hiện ra sao?

## Current annotation

Query type: paraphrase  
Difficulty: hard  
Annotation status: in_review

Gold documents:
- 134-2025-QH15

Gold articles:
- 134-2025-QH15_dieu-14

Gold chunks:
- 134-2025-QH15_dieu-14_khoan-1_diem-a
- 134-2025-QH15_dieu-14_khoan-1_diem-b
- 134-2025-QH15_dieu-14_khoan-1_diem-c
- 134-2025-QH15_dieu-14_khoan-1_diem-d
- 134-2025-QH15_dieu-14_khoan-1_diem-đ
- 134-2025-QH15_dieu-14_khoan-1_diem-e
- 134-2025-QH15_dieu-14_khoan-1_diem-g
- 134-2025-QH15_dieu-14_khoan-2_diem-a
- 134-2025-QH15_dieu-14_khoan-2_diem-b
- 134-2025-QH15_dieu-14_khoan-2_diem-c
- 134-2025-QH15_dieu-14_khoan-2_diem-d
- 134-2025-QH15_dieu-14_khoan-2_diem-đ
- 134-2025-QH15_dieu-14_khoan-2_diem-e
- 134-2025-QH15_dieu-14_khoan-3
- 134-2025-QH15_dieu-14_khoan-4
- 134-2025-QH15_dieu-14_khoan-5
- 134-2025-QH15_dieu-14_khoan-6

## Why this query was flagged

Gold hiện có 17 chunks và query không xác định chủ thể hay phạm vi của “việc quản lý”.

## Article context

### Article 134-2025-QH15_dieu-14

Title: Quản lý hệ thống trí tuệ nhân tạo có rủi ro cao  
Document: Luật Trí tuệ nhân tạo (134/2025/QH15)  
Structure: Chương II — PHÂN LOẠI VÀ QUẢN LÝ  
Review role: PRIMARY

Article context:
- `134-2025-QH15_dieu-14_khoan-1_diem-a` — Thiết lập và duy trì biện pháp quản lý rủi ro và thường xuyên rà soát khi hệ thống có thay đổi đáng kể hoặc phát sinh rủi ro mới;
- `134-2025-QH15_dieu-14_khoan-1_diem-b` — Quản trị dữ liệu huấn luyện, kiểm thử và vận hành bảo đảm chất lượng trong phạm vi khả năng kỹ thuật và phù hợp với mục đích sử dụng của hệ thống;
- `134-2025-QH15_dieu-14_khoan-1_diem-c` — Lập, cập nhật, lưu giữ hồ sơ kỹ thuật và nhật ký hoạt động ở mức cần thiết cho việc đánh giá sự phù hợp và kiểm tra sau khi đưa vào sử dụng; cung cấp các thông tin này cho cơ quan nhà nước có thẩm quyền theo nguyên tắc cần thiết, tương xứng với mục đích kiểm tra và không làm lộ bí mật kinh doanh;
- `134-2025-QH15_dieu-14_khoan-1_diem-d` — Thiết kế hệ thống bảo đảm khả năng giám sát và can thiệp của con người đối với hệ thống;
- `134-2025-QH15_dieu-14_khoan-1_diem-đ` — Thực hiện nghĩa vụ minh bạch và xử lý sự cố theo quy định tại Điều 11 và Điều 12 của Luật này;
- `134-2025-QH15_dieu-14_khoan-1_diem-e` — Thực hiện trách nhiệm giải trình đối với cơ quan nhà nước có thẩm quyền về mục đích sử dụng, nguyên lý hoạt động ở mức mô tả chức năng, loại dữ liệu đầu vào chủ yếu, biện pháp quản lý và kiểm soát rủi ro cùng các nội dung cần thiết phục vụ thanh tra, kiểm tra; cung cấp cho người sử dụng và người bị ảnh hưởng các thông tin công khai ở mức mô tả chức năng, cách thức vận hành và cảnh báo rủi ro để bảo đảm an toàn trong sử dụng. Việc giải trình và cung cấp thông tin không được yêu cầu tiết lộ mã nguồn, thuật toán chi tiết, bộ tham số hoặc thông tin thuộc bí mật kinh doanh, bí mật công nghệ;
- `134-2025-QH15_dieu-14_khoan-1_diem-g` — Phối hợp với cơ quan nhà nước có thẩm quyền và bên triển khai trong kiểm tra, đánh giá, hậu kiểm và khắc phục sự cố liên quan đến hệ thống.
- `134-2025-QH15_dieu-14_khoan-2_diem-a` — Vận hành và giám sát hệ thống đúng mục đích, phạm vi và mức độ rủi ro đã được phân loại, không làm phát sinh rủi ro mới hoặc rủi ro cao hơn;
- `134-2025-QH15_dieu-14_khoan-2_diem-b` — Bảo đảm an toàn, bảo mật dữ liệu và khả năng can thiệp của con người trong quá trình sử dụng;
- `134-2025-QH15_dieu-14_khoan-2_diem-c` — Duy trì việc tuân thủ tiêu chuẩn, quy chuẩn kỹ thuật về trí tuệ nhân tạo trong quá trình vận hành hệ thống;
- `134-2025-QH15_dieu-14_khoan-2_diem-d` — Thực hiện nghĩa vụ minh bạch và xử lý sự cố theo quy định tại Điều 11 và Điều 12 của Luật này;
- `134-2025-QH15_dieu-14_khoan-2_diem-đ` — Thực hiện trách nhiệm giải trình đối với cơ quan nhà nước có thẩm quyền về việc vận hành hệ thống, biện pháp kiểm soát rủi ro, xử lý sự cố và các nội dung cần thiết phục vụ công tác thanh tra, kiểm tra; cung cấp cho người sử dụng và người bị ảnh hưởng các thông tin công khai ở mức mô tả chức năng, cách thức vận hành và cảnh báo rủi ro nhằm bảo đảm an toàn trong sử dụng;
- `134-2025-QH15_dieu-14_khoan-2_diem-e` — Phối hợp với nhà cung cấp và cơ quan nhà nước có thẩm quyền trong kiểm tra, đánh giá, hậu kiểm và khắc phục sự cố.
- `134-2025-QH15_dieu-14_khoan-3` — Người sử dụng hệ thống trí tuệ nhân tạo có rủi ro cao có trách nhiệm tuân thủ quy trình vận hành, hướng dẫn kỹ thuật và các biện pháp bảo đảm an toàn; không can thiệp trái phép làm thay đổi tính năng của hệ thống; thông báo kịp thời các sự cố phát sinh cho bên triền khai.
- `134-2025-QH15_dieu-14_khoan-4` — Việc giải trình phải phù hợp với khả năng kỹ thuật của hệ thống, không làm lộ bí mật kinh doanh theo quy định của pháp luật.
- `134-2025-QH15_dieu-14_khoan-5` — Khuyến khích nhà cung cấp, bên triển khai tham gia bảo hiểm trách nhiệm dân sự hoặc áp dụng biện pháp bảo đảm thực hiện nghĩa vụ phù hợp khác để kịp thời khắc phục sự cố và bồi thường thiệt hại.
- `134-2025-QH15_dieu-14_khoan-6` — Nhà cung cấp nước ngoài có hệ thống trí tuệ nhân tạo có rủi ro cao được cung cấp tại Việt Nam phải có đầu mối liên hệ hợp pháp tại Việt Nam; trường hợp hệ thống thuộc diện bắt buộc chứng nhận sự phù hợp trước khi đưa vào sử dụng, phải có hiện diện thương mại hoặc đại diện được ủy quyền tại Việt Nam.
- `134-2025-QH15_dieu-14_khoan-7` — Chính phủ quy định chi tiết Điều này.

## Gold chunk review

### Chunk 1

chunk_id: `134-2025-QH15_dieu-14_khoan-1_diem-a`

Legal location: 134/2025/QH15, Điều 14, khoản 1, điểm a

Text:

Thiết lập và duy trì biện pháp quản lý rủi ro và thường xuyên rà soát khi hệ thống có thay đổi đáng kể hoặc phát sinh rủi ro mới;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 2

chunk_id: `134-2025-QH15_dieu-14_khoan-1_diem-b`

Legal location: 134/2025/QH15, Điều 14, khoản 1, điểm b

Text:

Quản trị dữ liệu huấn luyện, kiểm thử và vận hành bảo đảm chất lượng trong phạm vi khả năng kỹ thuật và phù hợp với mục đích sử dụng của hệ thống;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 3

chunk_id: `134-2025-QH15_dieu-14_khoan-1_diem-c`

Legal location: 134/2025/QH15, Điều 14, khoản 1, điểm c

Text:

Lập, cập nhật, lưu giữ hồ sơ kỹ thuật và nhật ký hoạt động ở mức cần thiết cho việc đánh giá sự phù hợp và kiểm tra sau khi đưa vào sử dụng; cung cấp các thông tin này cho cơ quan nhà nước có thẩm quyền theo nguyên tắc cần thiết, tương xứng với mục đích kiểm tra và không làm lộ bí mật kinh doanh;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 4

chunk_id: `134-2025-QH15_dieu-14_khoan-1_diem-d`

Legal location: 134/2025/QH15, Điều 14, khoản 1, điểm d

Text:

Thiết kế hệ thống bảo đảm khả năng giám sát và can thiệp của con người đối với hệ thống;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 5

chunk_id: `134-2025-QH15_dieu-14_khoan-1_diem-đ`

Legal location: 134/2025/QH15, Điều 14, khoản 1, điểm đ

Text:

Thực hiện nghĩa vụ minh bạch và xử lý sự cố theo quy định tại Điều 11 và Điều 12 của Luật này;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 6

chunk_id: `134-2025-QH15_dieu-14_khoan-1_diem-e`

Legal location: 134/2025/QH15, Điều 14, khoản 1, điểm e

Text:

Thực hiện trách nhiệm giải trình đối với cơ quan nhà nước có thẩm quyền về mục đích sử dụng, nguyên lý hoạt động ở mức mô tả chức năng, loại dữ liệu đầu vào chủ yếu, biện pháp quản lý và kiểm soát rủi ro cùng các nội dung cần thiết phục vụ thanh tra, kiểm tra; cung cấp cho người sử dụng và người bị ảnh hưởng các thông tin công khai ở mức mô tả chức năng, cách thức vận hành và cảnh báo rủi ro để bảo đảm an toàn trong sử dụng. Việc giải trình và cung cấp thông tin không được yêu cầu tiết lộ mã nguồn, thuật toán chi tiết, bộ tham số hoặc thông tin thuộc bí mật kinh doanh, bí mật công nghệ;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 7

chunk_id: `134-2025-QH15_dieu-14_khoan-1_diem-g`

Legal location: 134/2025/QH15, Điều 14, khoản 1, điểm g

Text:

Phối hợp với cơ quan nhà nước có thẩm quyền và bên triển khai trong kiểm tra, đánh giá, hậu kiểm và khắc phục sự cố liên quan đến hệ thống.

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 8

chunk_id: `134-2025-QH15_dieu-14_khoan-2_diem-a`

Legal location: 134/2025/QH15, Điều 14, khoản 2, điểm a

Text:

Vận hành và giám sát hệ thống đúng mục đích, phạm vi và mức độ rủi ro đã được phân loại, không làm phát sinh rủi ro mới hoặc rủi ro cao hơn;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 9

chunk_id: `134-2025-QH15_dieu-14_khoan-2_diem-b`

Legal location: 134/2025/QH15, Điều 14, khoản 2, điểm b

Text:

Bảo đảm an toàn, bảo mật dữ liệu và khả năng can thiệp của con người trong quá trình sử dụng;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 10

chunk_id: `134-2025-QH15_dieu-14_khoan-2_diem-c`

Legal location: 134/2025/QH15, Điều 14, khoản 2, điểm c

Text:

Duy trì việc tuân thủ tiêu chuẩn, quy chuẩn kỹ thuật về trí tuệ nhân tạo trong quá trình vận hành hệ thống;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 11

chunk_id: `134-2025-QH15_dieu-14_khoan-2_diem-d`

Legal location: 134/2025/QH15, Điều 14, khoản 2, điểm d

Text:

Thực hiện nghĩa vụ minh bạch và xử lý sự cố theo quy định tại Điều 11 và Điều 12 của Luật này;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 12

chunk_id: `134-2025-QH15_dieu-14_khoan-2_diem-đ`

Legal location: 134/2025/QH15, Điều 14, khoản 2, điểm đ

Text:

Thực hiện trách nhiệm giải trình đối với cơ quan nhà nước có thẩm quyền về việc vận hành hệ thống, biện pháp kiểm soát rủi ro, xử lý sự cố và các nội dung cần thiết phục vụ công tác thanh tra, kiểm tra; cung cấp cho người sử dụng và người bị ảnh hưởng các thông tin công khai ở mức mô tả chức năng, cách thức vận hành và cảnh báo rủi ro nhằm bảo đảm an toàn trong sử dụng;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 13

chunk_id: `134-2025-QH15_dieu-14_khoan-2_diem-e`

Legal location: 134/2025/QH15, Điều 14, khoản 2, điểm e

Text:

Phối hợp với nhà cung cấp và cơ quan nhà nước có thẩm quyền trong kiểm tra, đánh giá, hậu kiểm và khắc phục sự cố.

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 14

chunk_id: `134-2025-QH15_dieu-14_khoan-3`

Legal location: 134/2025/QH15, Điều 14, khoản 3

Text:

Người sử dụng hệ thống trí tuệ nhân tạo có rủi ro cao có trách nhiệm tuân thủ quy trình vận hành, hướng dẫn kỹ thuật và các biện pháp bảo đảm an toàn; không can thiệp trái phép làm thay đổi tính năng của hệ thống; thông báo kịp thời các sự cố phát sinh cho bên triền khai.

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 15

chunk_id: `134-2025-QH15_dieu-14_khoan-4`

Legal location: 134/2025/QH15, Điều 14, khoản 4

Text:

Việc giải trình phải phù hợp với khả năng kỹ thuật của hệ thống, không làm lộ bí mật kinh doanh theo quy định của pháp luật.

Reason selected:

Cần để xác lập phạm vi/nghĩa vụ hoặc giải nghĩa dẫn chiếu, nhưng không tự nó là toàn bộ đáp án.

Assessment:
- SUPPORTING

### Chunk 16

chunk_id: `134-2025-QH15_dieu-14_khoan-5`

Legal location: 134/2025/QH15, Điều 14, khoản 5

Text:

Khuyến khích nhà cung cấp, bên triển khai tham gia bảo hiểm trách nhiệm dân sự hoặc áp dụng biện pháp bảo đảm thực hiện nghĩa vụ phù hợp khác để kịp thời khắc phục sự cố và bồi thường thiệt hại.

Reason selected:

Chỉ cần nếu giữ cách hiểu rộng hiện tại; có thể loại sau khi thu hẹp hoặc làm rõ query.

Assessment:
- QUESTIONABLE

### Chunk 17

chunk_id: `134-2025-QH15_dieu-14_khoan-6`

Legal location: 134/2025/QH15, Điều 14, khoản 6

Text:

Nhà cung cấp nước ngoài có hệ thống trí tuệ nhân tạo có rủi ro cao được cung cấp tại Việt Nam phải có đầu mối liên hệ hợp pháp tại Việt Nam; trường hợp hệ thống thuộc diện bắt buộc chứng nhận sự phù hợp trước khi đưa vào sử dụng, phải có hiện diện thương mại hoặc đại diện được ủy quyền tại Việt Nam.

Reason selected:

Chỉ cần nếu giữ cách hiểu rộng hiện tại; có thể loại sau khi thu hẹp hoặc làm rõ query.

Assessment:
- QUESTIONABLE

## Coverage analysis

Câu hỏi cần trả lời những ý nào?
1. Bảy nghĩa vụ của nhà cung cấp.
2. Sáu nghĩa vụ của bên triển khai.
3. Nghĩa vụ của người sử dụng.
4. Giới hạn của giải trình.
5. Khuyến khích bảo hiểm/bảo đảm nghĩa vụ.
6. Yêu cầu riêng với nhà cung cấp nước ngoài.

Gold hiện tại có bao phủ từng ý không?
- Ý 1 → `134-2025-QH15_dieu-14_khoan-1_diem-a`, `134-2025-QH15_dieu-14_khoan-1_diem-b`, `134-2025-QH15_dieu-14_khoan-1_diem-c`, `134-2025-QH15_dieu-14_khoan-1_diem-d`, `134-2025-QH15_dieu-14_khoan-1_diem-đ`, `134-2025-QH15_dieu-14_khoan-1_diem-e`, `134-2025-QH15_dieu-14_khoan-1_diem-g`.
- Ý 2 → `134-2025-QH15_dieu-14_khoan-2_diem-a`, `134-2025-QH15_dieu-14_khoan-2_diem-b`, `134-2025-QH15_dieu-14_khoan-2_diem-c`, `134-2025-QH15_dieu-14_khoan-2_diem-d`, `134-2025-QH15_dieu-14_khoan-2_diem-đ`, `134-2025-QH15_dieu-14_khoan-2_diem-e`.
- Ý 3 → `134-2025-QH15_dieu-14_khoan-3`.
- Ý 4 → `134-2025-QH15_dieu-14_khoan-4`.
- Ý 5 → `134-2025-QH15_dieu-14_khoan-5`.
- Ý 6 → `134-2025-QH15_dieu-14_khoan-6`.

Missing coverage:

Không nếu hiểu query là toàn bộ Điều 14; chính độ rộng làm gold phình lớn.

Potential unnecessary chunks:

Khoản 5 và khoản 6 là QUESTIONABLE đối với cách hiểu “quản lý nói chung”; khoản 4 là quy định hỗ trợ. Nếu tách theo chủ thể, chỉ giữ các chunks thuộc chủ thể tương ứng.

## Ambiguity

Cao. Có thể hỏi toàn bộ chế độ quản lý, riêng nhà cung cấp, riêng bên triển khai, hoặc cả người sử dụng và quy định bổ trợ.

## Recommended human decision

Suggested action: **SPLIT_QUERY**

Reason:

Nên tách tối thiểu thành: “Nhà cung cấp hệ thống AI rủi ro cao có những nghĩa vụ gì?” và “Bên triển khai hệ thống AI rủi ro cao có những nghĩa vụ gì?”. Có thể tạo query riêng về người sử dụng nếu cần đánh giá vai trò đó.

## Human decision

- [ ] KEEP
- [ ] REMOVE_CHUNK
- [ ] ADD_CHUNK
- [ ] REWRITE_QUERY
- [ ] SPLIT_QUERY
- [ ] NEEDS_REVIEW

Human notes:


---

# eval007

## Query

Nội dung do AI tạo ra phải được thông báo hoặc gắn nhãn như thế nào?

## Current annotation

Query type: transparency  
Difficulty: hard  
Annotation status: in_review

Gold documents:
- 142-2026-ND-CP

Gold articles:
- 142-2026-ND-CP_dieu-18

Gold chunks:
- 142-2026-ND-CP_dieu-18_khoan-3_diem-a
- 142-2026-ND-CP_dieu-18_khoan-3_diem-b
- 142-2026-ND-CP_dieu-18_khoan-3_diem-c
- 142-2026-ND-CP_dieu-18_khoan-3_diem-d
- 142-2026-ND-CP_dieu-18_khoan-3_diem-đ
- 142-2026-ND-CP_dieu-18_khoan-5_diem-a
- 142-2026-ND-CP_dieu-18_khoan-5_diem-b
- 142-2026-ND-CP_dieu-18_khoan-5_diem-c
- 142-2026-ND-CP_dieu-18_khoan-5_diem-d

## Why this query was flagged

Có 9 chunks, cần phân biệt yêu cầu chung và cách thức triển khai nhãn/thông báo.

## Article context

### Article 142-2026-ND-CP_dieu-18

Title: Thông báo và gắn nhãn hiển thị đối với nội dung do hệ thống trí tuệ nhân tạo tạo ra  
Document: Nghị định hướng dẫn thi hành Luật Trí tuệ nhân tạo (142/2026/NĐ-CP)  
Structure: Chương III — MINH BẠCH, GIẢI TRÌNH VÀ XỬ LÝ SỰ CỐ  
Review role: PRIMARY

Article context:
- `142-2026-ND-CP_dieu-18_khoan-1` — Bên triển khai phải thông báo rõ ràng khi cung cấp ra công cộng nội dung do hệ thống trí tuệ nhân tạo tạo ra hoặc chỉnh sửa có khả năng gây nhầm lẫn về tính xác thực của sự kiện, nhân vật hoặc nguồn gốc nội dung theo quy định tại khoản 3 Điều 11 của Luật Trí tuệ nhân tạo.
- `142-2026-ND-CP_dieu-18_khoan-2_diem-a` — Mô phỏng hoặc giả lập ngoại hình, giọng nói của người thật;
- `142-2026-ND-CP_dieu-18_khoan-2_diem-b` — Tái hiện sự kiện thực tế để phân biệt với nội dung thật, trừ trường hợp pháp luật có quy định khác.
- `142-2026-ND-CP_dieu-18_khoan-3_diem-a` — Rõ ràng, dễ hiểu và dễ nhận biết đối với người tiếp nhận;
- `142-2026-ND-CP_dieu-18_khoan-3_diem-b` — Được thực hiện trước hoặc tại thời điểm người tiếp nhận tiếp cận nội dung;
- `142-2026-ND-CP_dieu-18_khoan-3_diem-c` — Không được thiết kế theo cách che giấu hoặc làm giảm khả năng nhận biết bản chất của nội dung;
- `142-2026-ND-CP_dieu-18_khoan-3_diem-d` — Phù hợp với loại hình nội dung và phương thức cung cấp nội dung;
- `142-2026-ND-CP_dieu-18_khoan-3_diem-đ` — Không gây cản trở đáng kể việc hiển thị, trình diễn hoặc sử dụng nội dung.
- `142-2026-ND-CP_dieu-18_khoan-4_diem-a` — Nội dung được chỉnh sửa kỹ thuật nhằm cải thiện chất lượng âm thanh, hình ảnh hoặc video mà không làm thay đổi bản chất hoặc ngữ cảnh chính của nội dung;
- `142-2026-ND-CP_dieu-18_khoan-4_diem-b` — Văn bản được xử lý bằng công cụ hỗ trợ sửa lỗi chính tả, ngữ pháp, tóm tắt, diễn giải hoặc dịch thuật mà không làm sai lệch nội dung cơ bản của văn bản gốc;
- `142-2026-ND-CP_dieu-18_khoan-4_diem-c` — Nội dung được sử dụng trong phạm vi nội bộ của cơ quan, tổ chức, doanh nghiệp và không được cung cấp ra công cộng;
- `142-2026-ND-CP_dieu-18_khoan-4_diem-d` — Nội dung được tạo ra trong quá trình nghiên cứu, phát triển hoặc thử nghiệm trong môi trường kiểm soát và không được cung cấp ra công cộng.
- `142-2026-ND-CP_dieu-18_khoan-5_diem-a` — Hiển thị trực tiếp trên nội dung;
- `142-2026-ND-CP_dieu-18_khoan-5_diem-b` — Hiển thị tại tiêu đề, phần mô tả hoặc chú thích kèm theo nội dung;
- `142-2026-ND-CP_dieu-18_khoan-5_diem-c` — Hiển thị trên giao diện của nền tảng cung cấp nội dung;
- `142-2026-ND-CP_dieu-18_khoan-5_diem-d` — Phát thông báo bằng âm thanh hoặc hình thức phù hợp khác.
- `142-2026-ND-CP_dieu-18_khoan-6` — Đối với tác phẩm điện ảnh, chương trình nghệ thuật hoặc nội dung sáng tạo, việc thông báo và gắn nhãn hiển thị do bên triển khai trực tiếp đưa nội dung ra công cộng thực hiện và có thể được thực hiện tại phần mở đầu, phần kết thúc, phần danh đề, phần mô tả hoặc tài liệu kèm theo tác phẩm, phù hợp với đặc thù của từng loại hình. Việc thông báo và gắn nhãn phải bảo đảm người tiếp nhận có thể nhận biết rõ ràng nội dung được tạo ra hoặc được chỉnh sửa bằng hệ thống trí tuệ nhân tạo, không gây nhầm lẫn về nguồn gốc của nội dung. Trường hợp nội dung do hệ thống trí tuệ nhân tạo tạo ra hoặc chỉnh sửa trong quá trình sản xuất, bên thực hiện việc tạo ra hoặc chỉnh sửa nội dung có trách nhiệm cung cấp thông tin cần thiết để thực hiện nghĩa vụ quy định tại khoản này; bên trực tiếp đưa nội dung ra công cộng thực hiện nghĩa vụ trên cơ sở thông tin được cung cấp.
- `142-2026-ND-CP_dieu-18_khoan-7` — Bộ Khoa học và Công nghệ công bố và cập nhật hướng dẫn kỹ thuật tham chiếu về hình thức thông báo và gắn nhãn hiển thị quy định tại Điều này. Việc công bố quy định tại khoản này không làm phát sinh thủ tục hành chính, điều kiện đầu tư kinh doanh hoặc nghĩa vụ ngoài quy định của Nghị định này.

## Gold chunk review

### Chunk 1

chunk_id: `142-2026-ND-CP_dieu-18_khoan-3_diem-a`

Legal location: 142/2026/NĐ-CP, Điều 18, khoản 3, điểm a

Text:

Rõ ràng, dễ hiểu và dễ nhận biết đối với người tiếp nhận;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 2

chunk_id: `142-2026-ND-CP_dieu-18_khoan-3_diem-b`

Legal location: 142/2026/NĐ-CP, Điều 18, khoản 3, điểm b

Text:

Được thực hiện trước hoặc tại thời điểm người tiếp nhận tiếp cận nội dung;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 3

chunk_id: `142-2026-ND-CP_dieu-18_khoan-3_diem-c`

Legal location: 142/2026/NĐ-CP, Điều 18, khoản 3, điểm c

Text:

Không được thiết kế theo cách che giấu hoặc làm giảm khả năng nhận biết bản chất của nội dung;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 4

chunk_id: `142-2026-ND-CP_dieu-18_khoan-3_diem-d`

Legal location: 142/2026/NĐ-CP, Điều 18, khoản 3, điểm d

Text:

Phù hợp với loại hình nội dung và phương thức cung cấp nội dung;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 5

chunk_id: `142-2026-ND-CP_dieu-18_khoan-3_diem-đ`

Legal location: 142/2026/NĐ-CP, Điều 18, khoản 3, điểm đ

Text:

Không gây cản trở đáng kể việc hiển thị, trình diễn hoặc sử dụng nội dung.

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 6

chunk_id: `142-2026-ND-CP_dieu-18_khoan-5_diem-a`

Legal location: 142/2026/NĐ-CP, Điều 18, khoản 5, điểm a

Text:

Hiển thị trực tiếp trên nội dung;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 7

chunk_id: `142-2026-ND-CP_dieu-18_khoan-5_diem-b`

Legal location: 142/2026/NĐ-CP, Điều 18, khoản 5, điểm b

Text:

Hiển thị tại tiêu đề, phần mô tả hoặc chú thích kèm theo nội dung;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 8

chunk_id: `142-2026-ND-CP_dieu-18_khoan-5_diem-c`

Legal location: 142/2026/NĐ-CP, Điều 18, khoản 5, điểm c

Text:

Hiển thị trên giao diện của nền tảng cung cấp nội dung;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 9

chunk_id: `142-2026-ND-CP_dieu-18_khoan-5_diem-d`

Legal location: 142/2026/NĐ-CP, Điều 18, khoản 5, điểm d

Text:

Phát thông báo bằng âm thanh hoặc hình thức phù hợp khác.

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

## Coverage analysis

Câu hỏi cần trả lời những ý nào?
1. Nhãn/thông báo phải rõ ràng, đúng thời điểm và không che giấu.
2. Phải phù hợp loại nội dung và không cản trở đáng kể việc sử dụng.
3. Bốn hình thức thể hiện có thể lựa chọn.

Gold hiện tại có bao phủ từng ý không?
- Ý 1 → `142-2026-ND-CP_dieu-18_khoan-3_diem-a`, `142-2026-ND-CP_dieu-18_khoan-3_diem-b`, `142-2026-ND-CP_dieu-18_khoan-3_diem-c`.
- Ý 2 → `142-2026-ND-CP_dieu-18_khoan-3_diem-d`, `142-2026-ND-CP_dieu-18_khoan-3_diem-đ`.
- Ý 3 → `142-2026-ND-CP_dieu-18_khoan-5_diem-a`, `142-2026-ND-CP_dieu-18_khoan-5_diem-b`, `142-2026-ND-CP_dieu-18_khoan-5_diem-c`, `142-2026-ND-CP_dieu-18_khoan-5_diem-d`.

Missing coverage:

Không đối với câu hỏi về cách thức. Gold không cố đưa điều kiện phát sinh nghĩa vụ, ngoại lệ hay trường hợp tác phẩm sáng tạo vào.

Potential unnecessary chunks:

Không. Năm chunks khoản 3 là general rule; bốn chunks khoản 5 là implementation forms, đều trực tiếp trả lời “như thế nào”.

## Ambiguity

Thấp. Từ “như thế nào” hợp lý bao gồm cả tiêu chuẩn thể hiện và các hình thức thể hiện được lựa chọn.

## Recommended human decision

Suggested action: **KEEP**

Reason:

Giữ nguyên; 9 chunks là hai danh sách bổ sung nhau, không phải các trường hợp ngoại lệ bị gom quá rộng.

## Human decision

- [ ] KEEP
- [ ] REMOVE_CHUNK
- [ ] ADD_CHUNK
- [ ] REWRITE_QUERY
- [ ] SPLIT_QUERY
- [ ] NEEDS_REVIEW

Human notes:


---

# eval014

## Query

Hồ sơ tham gia thử nghiệm có kiểm soát cần những thành phần nào?

## Current annotation

Query type: procedure  
Difficulty: hard  
Annotation status: in_review

Gold documents:
- 142-2026-ND-CP

Gold articles:
- 142-2026-ND-CP_dieu-24

Gold chunks:
- 142-2026-ND-CP_dieu-24_khoan-2_diem-a
- 142-2026-ND-CP_dieu-24_khoan-2_diem-b
- 142-2026-ND-CP_dieu-24_khoan-2_diem-c
- 142-2026-ND-CP_dieu-24_khoan-2_diem-d
- 142-2026-ND-CP_dieu-24_khoan-3_diem-a
- 142-2026-ND-CP_dieu-24_khoan-3_diem-b

## Why this query was flagged

Gold trộn hồ sơ thông thường bốn tài liệu và hồ sơ rút gọn hai tài liệu.

## Article context

### Article 142-2026-ND-CP_dieu-24

Title: Điều kiện và hồ sơ tham gia thử nghiệm  
Document: Nghị định hướng dẫn thi hành Luật Trí tuệ nhân tạo (142/2026/NĐ-CP)  
Structure: Chương IV — CƠ CHẾ THỬ NGHIỆM CÓ KIỂM SOÁT  
Review role: PRIMARY

Article context:
- `142-2026-ND-CP_dieu-24_khoan-1_diem-a` — Có hệ thống trí tuệ nhân tạo hoặc giải pháp trí tuệ nhân tạo dự kiến thử nghiệm có yếu tố đổi mới sáng tạo, ứng dụng công nghệ mới hoặc mô hình triển khai mới;
- `142-2026-ND-CP_dieu-24_khoan-1_diem-b` — Có đề án thử nghiệm, trong đó xác định rõ mục tiêu, phạm vi, thời gian thử nghiệm, đối tượng tham gia và biện pháp kiểm soát rủi ro phù hợp với cấp độ thử nghiệm quy định tại Điều 22 của Nghị định này;
- `142-2026-ND-CP_dieu-24_khoan-1_diem-c` — Có biện pháp bảo vệ quyền và lợi ích hợp pháp của tổ chức, cá nhân chịu tác động trong quá trình thử nghiệm;
- `142-2026-ND-CP_dieu-24_khoan-1_diem-d` — Trường hợp hệ thống trí tuệ nhân tạo có khả năng trực tiếp gây thiệt hại đến tính mạng, sức khỏe con người hoặc gây thiệt hại tài sản quy mô lớn, tổ chức, cá nhân tham gia thử nghiệm phải áp dụng bảo hiểm trách nhiệm dân sự hoặc biện pháp bảo đảm tài chính tương đương phù hợp với phạm vi thử nghiệm.
- `142-2026-ND-CP_dieu-24_khoan-2_diem-a` — Đơn đề nghị tham gia cơ chế thử nghiệm có kiểm soát theo Mẫu AI03a đối với tổ chức hoặc Mẫu AI03b đối với cá nhân tại Phụ lục ban hành kèm theo Nghị định này;
- `142-2026-ND-CP_dieu-24_khoan-2_diem-b` — Đề án thử nghiệm, trong đó mô tả hệ thống trí tuệ nhân tạo dự kiến thử nghiệm, mục tiêu, phạm vi, thời gian thử nghiệm và phương án quản lý rủi ro;
- `142-2026-ND-CP_dieu-24_khoan-2_diem-c` — Tài liệu mô tả biện pháp bảo vệ quyền và lợi ích hợp pháp của tổ chức, cá nhân chịu tác động trong quá trình thử nghiệm;
- `142-2026-ND-CP_dieu-24_khoan-2_diem-d` — Tài liệu mô tả năng lực kỹ thuật, nhân sự hoặc hạ tầng phục vụ triển khai thử nghiệm có liên quan trực tiếp đến phạm vi thử nghiệm đề xuất.
- `142-2026-ND-CP_dieu-24_khoan-3_diem-a` — Đơn đề nghị tham gia cơ chế thử nghiệm có kiểm soát theo Mẫu AI03a đối với tổ chức hoặc Mẫu AI03b đối với cá nhân tại Phụ lục ban hành kèm theo Nghị định này;
- `142-2026-ND-CP_dieu-24_khoan-3_diem-b` — Tài liệu mô tả khái quát hệ thống trí tuệ nhân tạo dự kiến thử nghiệm, các rủi ro chính có thể phát sinh và biện pháp giảm thiểu rủi ro trong quá trình thử nghiệm.
- `142-2026-ND-CP_dieu-24_khoan-4` — Hồ sơ quy định tại khoản 2 và khoản 3 Điều này được nộp bằng phương thức điện tử theo quy định tại Điều 23 của Nghị định này.
- `142-2026-ND-CP_dieu-24_khoan-5` — Cơ quan nhà nước có thẩm quyền không được yêu cầu tổ chức, cá nhân cung cấp thêm thành phần hồ sơ ngoài quy định tại Điều này, trừ trường hợp pháp luật chuyên ngành quy định trực tiếp thành phần hồ sơ đối với hoạt động thử nghiệm trong lĩnh vực tương ứng.

## Gold chunk review

### Chunk 1

chunk_id: `142-2026-ND-CP_dieu-24_khoan-2_diem-a`

Legal location: 142/2026/NĐ-CP, Điều 24, khoản 2, điểm a

Text:

Đơn đề nghị tham gia cơ chế thử nghiệm có kiểm soát theo Mẫu AI03a đối với tổ chức hoặc Mẫu AI03b đối với cá nhân tại Phụ lục ban hành kèm theo Nghị định này;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 2

chunk_id: `142-2026-ND-CP_dieu-24_khoan-2_diem-b`

Legal location: 142/2026/NĐ-CP, Điều 24, khoản 2, điểm b

Text:

Đề án thử nghiệm, trong đó mô tả hệ thống trí tuệ nhân tạo dự kiến thử nghiệm, mục tiêu, phạm vi, thời gian thử nghiệm và phương án quản lý rủi ro;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 3

chunk_id: `142-2026-ND-CP_dieu-24_khoan-2_diem-c`

Legal location: 142/2026/NĐ-CP, Điều 24, khoản 2, điểm c

Text:

Tài liệu mô tả biện pháp bảo vệ quyền và lợi ích hợp pháp của tổ chức, cá nhân chịu tác động trong quá trình thử nghiệm;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 4

chunk_id: `142-2026-ND-CP_dieu-24_khoan-2_diem-d`

Legal location: 142/2026/NĐ-CP, Điều 24, khoản 2, điểm d

Text:

Tài liệu mô tả năng lực kỹ thuật, nhân sự hoặc hạ tầng phục vụ triển khai thử nghiệm có liên quan trực tiếp đến phạm vi thử nghiệm đề xuất.

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 5

chunk_id: `142-2026-ND-CP_dieu-24_khoan-3_diem-a`

Legal location: 142/2026/NĐ-CP, Điều 24, khoản 3, điểm a

Text:

Đơn đề nghị tham gia cơ chế thử nghiệm có kiểm soát theo Mẫu AI03a đối với tổ chức hoặc Mẫu AI03b đối với cá nhân tại Phụ lục ban hành kèm theo Nghị định này;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 6

chunk_id: `142-2026-ND-CP_dieu-24_khoan-3_diem-b`

Legal location: 142/2026/NĐ-CP, Điều 24, khoản 3, điểm b

Text:

Tài liệu mô tả khái quát hệ thống trí tuệ nhân tạo dự kiến thử nghiệm, các rủi ro chính có thể phát sinh và biện pháp giảm thiểu rủi ro trong quá trình thử nghiệm.

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

## Coverage analysis

Câu hỏi cần trả lời những ý nào?
1. Bốn thành phần của hồ sơ thông thường.
2. Hai thành phần của hồ sơ rút gọn.
3. Mẫu đơn tương ứng tổ chức/cá nhân trong mỗi chế độ.

Gold hiện tại có bao phủ từng ý không?
- Ý 1 → `142-2026-ND-CP_dieu-24_khoan-2_diem-a`, `142-2026-ND-CP_dieu-24_khoan-2_diem-b`, `142-2026-ND-CP_dieu-24_khoan-2_diem-c`, `142-2026-ND-CP_dieu-24_khoan-2_diem-d`.
- Ý 2 → `142-2026-ND-CP_dieu-24_khoan-3_diem-a`, `142-2026-ND-CP_dieu-24_khoan-3_diem-b`.
- Ý 3 → `142-2026-ND-CP_dieu-24_khoan-2_diem-a`, `142-2026-ND-CP_dieu-24_khoan-3_diem-a`.

Missing coverage:

Không, nhưng query không cho biết cần áp dụng chế độ nào.

Potential unnecessary chunks:

Không thể loại an toàn khi wording hiện tại vẫn hỏi chung. Sau khi rewrite, một trong hai nhóm chunks sẽ trở thành không cần thiết.

## Ambiguity

Cao nhưng không nằm ở tổ chức so với cá nhân: hai chủ thể dùng cùng thành phần, chỉ khác mẫu đơn AI03a/AI03b. Khác biệt thực sự là hồ sơ thông thường và hồ sơ rút gọn dành cho một số chủ thể thử nghiệm cấp độ 1.

## Recommended human decision

Suggested action: **REWRITE_QUERY**

Reason:

Nên đổi thành một trong hai câu rõ phạm vi: “Hồ sơ thông thường đăng ký tham gia thử nghiệm có kiểm soát gồm những tài liệu nào?” hoặc “Hồ sơ rút gọn cho chủ thể đủ điều kiện thử nghiệm cấp độ 1 gồm những tài liệu nào?”.

## Human decision

- [ ] KEEP
- [ ] REMOVE_CHUNK
- [ ] ADD_CHUNK
- [ ] REWRITE_QUERY
- [ ] SPLIT_QUERY
- [ ] NEEDS_REVIEW

Human notes:


---

# eval015

## Query

Khi nào cơ quan có thẩm quyền có thể tạm dừng hoặc chấm dứt thử nghiệm?

## Current annotation

Query type: condition  
Difficulty: hard  
Annotation status: in_review

Gold documents:
- 134-2025-QH15
- 142-2026-ND-CP

Gold articles:
- 134-2025-QH15_dieu-21
- 142-2026-ND-CP_dieu-25

Gold chunks:
- 134-2025-QH15_dieu-21_khoan-3
- 142-2026-ND-CP_dieu-25_khoan-1_diem-c

## Why this query was flagged

Gold lấy hai Article thuộc Luật và Nghị định; cần xác định quan hệ nguyên tắc–chi tiết.

## Article context

### Article 134-2025-QH15_dieu-21

Title: Cơ chế thử nghiệm có kiểm soát đối với trí tuệ nhân tạo  
Document: Luật Trí tuệ nhân tạo (134/2025/QH15)  
Structure: Chương IV — ỨNG DỤNG TRÍ TUỆ NHÂN TẠO, PHÁT TRIỂN HỆ SINH THÁI  
Review role: PRIMARY

Article context:
- `134-2025-QH15_dieu-21_khoan-1` — Cơ chế thử nghiệm có kiểm soát đối với trí tuệ nhân tạo thực hiện theo quy định của pháp luật về khoa học, công nghệ và đổi mới sáng tạo và quy định tại các khoản 2, 3 và 4 Điều này.
- `134-2025-QH15_dieu-21_khoan-2_diem-a` — Công nhận kết quả đánh giá sự phù hợp theo quy định của Luật này;
- `134-2025-QH15_dieu-21_khoan-2_diem-b` — Miễn, giảm hoặc điều chỉnh nghĩa vụ tuân thủ tương ứng của Luật này.
- `134-2025-QH15_dieu-21_khoan-3` — Cơ quan nhà nước có thẩm quyền chủ trì, phối hợp với cơ quan có liên quan tiếp nhận, thẩm định và xử lý hồ sơ theo quy trình thẩm định và phản hồi nhanh; giám sát quá trình thử nghiệm và quyết định tạm dừng hoặc chấm dứt thử nghiệm khi có rủi ro ảnh hưởng đến an toàn, an ninh hoặc quyền, lợi ích hợp pháp của tổ chức, cá nhân.
- `134-2025-QH15_dieu-21_khoan-4` — Chính phủ quy định chi tiết Điều này.

### Article 142-2026-ND-CP_dieu-25

Title: Giám sát và báo cáo trong quá trình thử nghiệm có kiểm soát  
Document: Nghị định hướng dẫn thi hành Luật Trí tuệ nhân tạo (142/2026/NĐ-CP)  
Structure: Chương IV — CƠ CHẾ THỬ NGHIỆM CÓ KIỂM SOÁT  
Review role: SUPPORTING

Article context:
- `142-2026-ND-CP_dieu-25_khoan-1_diem-a` — Tiếp nhận và đánh giá báo cáo định kỳ, báo cáo sự cố, báo cáo vượt giới hạn và báo cáo tổng kết thử nghiệm theo quy định của Nghị định này;
- `142-2026-ND-CP_dieu-25_khoan-1_diem-b` — Yêu cầu tổ chức, cá nhân tham gia thử nghiệm bổ sung biện pháp kiểm soát rủi ro hoặc đề xuất điều chỉnh phạm vi thử nghiệm để xem xét theo thẩm quyền khi phát sinh rủi ro ngoài phạm vi thử nghiệm;
- `142-2026-ND-CP_dieu-25_khoan-1_diem-c` — Quyết định tạm dừng thử nghiệm, chấm dứt thử nghiệm hoặc hiệu lực giấy xác nhận tham gia cơ chế thử nghiệm có kiểm soát khi tổ chức, cá nhân vi phạm các giới hạn thử nghiệm hoặc không khắc phục sự cố theo yêu cầu của cơ quan nhà nước có thẩm quyền.
- `142-2026-ND-CP_dieu-25_khoan-2_diem-a` — Cấp độ 1,2: 06 tháng một lần;
- `142-2026-ND-CP_dieu-25_khoan-2_diem-b` — Cấp độ 3: 03 tháng một lần.
- `142-2026-ND-CP_dieu-25_khoan-3_diem-a` — Hệ thống trí tuệ nhân tạo xảy ra sự cố nghiêm trọng theo khoản 8 Điều 3 Luật Trí tuệ nhân tạo;
- `142-2026-ND-CP_dieu-25_khoan-3_diem-b` — Hệ thống trí tuệ nhân tạo vượt giới hạn thử nghiệm đã được xác định trong giấy xác nhận. Báo cáo sự cố được thực hiện theo Mẫu AI06a đối với tổ chức hoặc Mẫu AI06b đối với cá nhân; báo cáo vượt giới hạn thử nghiệm được thực hiện theo Mẫu AI07a đối với tổ chức hoặc Mẫu AI07b đối với cá nhân tại Phụ lục ban hành kèm theo Nghị định này.
- `142-2026-ND-CP_dieu-25_khoan-4` — Chậm nhất 15 ngày trước khi kết thúc thời hạn thử nghiệm, tổ chức, cá nhân tham gia thử nghiệm phải nộp báo cáo tổng kết kết quả thử nghiệm thông qua cổng thông tin điện tử một cửa về trí tuệ nhân tạo theo Mẫu AI08a đối với tổ chức hoặc Mẫu AI08b đối với cá nhân tại Phụ lục ban hành kèm theo Nghị định này.

## Gold chunk review

### Chunk 1

chunk_id: `134-2025-QH15_dieu-21_khoan-3`

Legal location: 134/2025/QH15, Điều 21, khoản 3

Text:

Cơ quan nhà nước có thẩm quyền chủ trì, phối hợp với cơ quan có liên quan tiếp nhận, thẩm định và xử lý hồ sơ theo quy trình thẩm định và phản hồi nhanh; giám sát quá trình thử nghiệm và quyết định tạm dừng hoặc chấm dứt thử nghiệm khi có rủi ro ảnh hưởng đến an toàn, an ninh hoặc quyền, lợi ích hợp pháp của tổ chức, cá nhân.

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 2

chunk_id: `142-2026-ND-CP_dieu-25_khoan-1_diem-c`

Legal location: 142/2026/NĐ-CP, Điều 25, khoản 1, điểm c

Text:

Quyết định tạm dừng thử nghiệm, chấm dứt thử nghiệm hoặc hiệu lực giấy xác nhận tham gia cơ chế thử nghiệm có kiểm soát khi tổ chức, cá nhân vi phạm các giới hạn thử nghiệm hoặc không khắc phục sự cố theo yêu cầu của cơ quan nhà nước có thẩm quyền.

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

## Coverage analysis

Câu hỏi cần trả lời những ý nào?
1. Căn cứ chung: rủi ro ảnh hưởng an toàn, an ninh hoặc quyền/lợi ích hợp pháp.
2. Căn cứ chi tiết: vi phạm giới hạn thử nghiệm hoặc không khắc phục sự cố theo yêu cầu.

Gold hiện tại có bao phủ từng ý không?
- Ý 1 → `134-2025-QH15_dieu-21_khoan-3`.
- Ý 2 → `142-2026-ND-CP_dieu-25_khoan-1_diem-c`.

Missing coverage:

Không.

Potential unnecessary chunks:

Không. Điều 21 Luật là PRIMARY; Điều 25 Nghị định là SUPPORTING nhưng vẫn trực tiếp bổ sung điều kiện cụ thể, không chỉ liên quan chung.

## Ambiguity

Thấp. Hai căn cứ quy định các nhóm điều kiện khác nhau nhưng bổ sung trực tiếp cho cùng hành vi tạm dừng/chấm dứt.

## Recommended human decision

Suggested action: **KEEP**

Reason:

Giữ cả hai Article để không mất căn cứ rủi ro ở Luật hoặc các trường hợp vi phạm cụ thể ở Nghị định.

## Human decision

- [ ] KEEP
- [ ] REMOVE_CHUNK
- [ ] ADD_CHUNK
- [ ] REWRITE_QUERY
- [ ] SPLIT_QUERY
- [ ] NEEDS_REVIEW

Human notes:


---

# eval025

## Query

Khi ứng dụng AI trong quản lý nhà nước, cơ quan vận hành phải đánh giá tác động trong trường hợp nào?

## Current annotation

Query type: public_sector  
Difficulty: hard  
Annotation status: in_review

Gold documents:
- 142-2026-ND-CP

Gold articles:
- 142-2026-ND-CP_dieu-20

Gold chunks:
- 142-2026-ND-CP_dieu-20_khoan-1_diem-a
- 142-2026-ND-CP_dieu-20_khoan-1_diem-b
- 142-2026-ND-CP_dieu-20_khoan-2
- 142-2026-ND-CP_dieu-20_khoan-7_diem-a
- 142-2026-ND-CP_dieu-20_khoan-7_diem-b
- 142-2026-ND-CP_dieu-20_khoan-7_diem-c
- 142-2026-ND-CP_dieu-20_khoan-7_diem-d

## Why this query was flagged

Có 7 chunks cho câu hỏi chỉ hỏi điều kiện kích hoạt đánh giá tác động.

## Article context

### Article 142-2026-ND-CP_dieu-20

Title: Đánh giá tác động khi sử dụng hệ thống trí tuệ nhân tạo trong cơ quan nhà nước  
Document: Nghị định hướng dẫn thi hành Luật Trí tuệ nhân tạo (142/2026/NĐ-CP)  
Structure: Chương III — MINH BẠCH, GIẢI TRÌNH VÀ XỬ LÝ SỰ CỐ  
Review role: PRIMARY

Article context:
- `142-2026-ND-CP_dieu-20_khoan-1_diem-a` — Hệ thống thuộc nhóm hệ thống trí tuệ nhân tạo có rủi ro cao theo quy định của Luật;
- `142-2026-ND-CP_dieu-20_khoan-1_diem-b` — Hệ thống trí tuệ nhân tạo quy định tại khoản 7 Điều này mà kết quả của hệ thống được sử dụng làm căn cứ trực tiếp để người có thẩm quyền xem xét, quyết định ban hành quyết định hành chính.
- `142-2026-ND-CP_dieu-20_khoan-2` — Trường hợp hệ thống trí tuệ nhân tạo quy định tại khoản 1 Điều này có thay đổi về mục đích sử dụng, chức năng chính, nguồn dữ liệu đầu vào chủ yếu hoặc phạm vi đối tượng áp dụng làm phát sinh rủi ro mới hoặc làm thay đổi mức độ rủi ro của hệ thống, cơ quan, đơn vị triển khai phải thực hiện đánh giá tác động bổ sung trước khi tiếp tục sử dụng hệ thống.
- `142-2026-ND-CP_dieu-20_khoan-3_diem-a` — Thông tin mô tả hệ thống trí tuệ nhân tạo và mục đích sử dụng;
- `142-2026-ND-CP_dieu-20_khoan-3_diem-b` — Nhận diện và đánh giá rủi ro;
- `142-2026-ND-CP_dieu-20_khoan-3_diem-c` — Biện pháp kiểm soát và giảm thiểu rủi ro;
- `142-2026-ND-CP_dieu-20_khoan-3_diem-d` — Cơ chế bảo đảm khả năng giám sát và can thiệp của con người trong quá trình vận hành hệ thống.
- `142-2026-ND-CP_dieu-20_khoan-4` — Người đứng đầu cơ quan, đơn vị triển khai có trách nhiệm tổ chức lập, phê duyệt báo cáo đánh giá tác động trước khi đưa hệ thống trí tuệ nhân tạo vào sử dụng và chịu trách nhiệm trước pháp luật về nội dung, tính trung thực và đầy đủ của báo cáo.
- `142-2026-ND-CP_dieu-20_khoan-5` — Cơ quan, đơn vị triển khai phải công khai báo cáo đánh giá tác động theo quy định tại khoản 4 Điều 27 Luật Trí tuệ nhân tạo, trừ nội dung thuộc bí mật nhà nước, bí mật kinh doanh hoặc dữ liệu cá nhân theo quy định của pháp luật.
- `142-2026-ND-CP_dieu-20_khoan-6` — Việc sử dụng hệ thống trí tuệ nhân tạo trong cơ quan nhà nước phải tuân thủ Khung đạo đức trí tuệ nhân tạo quốc gia và không thay thế thẩm quyền, trách nhiệm quyết định của người có thẩm quyền theo quy định tại khoản 1 và khoản 2 Điều 27 Luật Trí tuệ nhân tạo.
- `142-2026-ND-CP_dieu-20_khoan-7_diem-a` — Kết quả của hệ thống được sử dụng làm căn cứ trong quá trình xem xét, quyết định trong hoạt động quản lý nhà nước hoặc cung cấp dịch vụ công;
- `142-2026-ND-CP_dieu-20_khoan-7_diem-b` — Được sử dụng để phân loại, chấm điểm, đánh giá hoặc xếp hạng tổ chức, cá nhân;
- `142-2026-ND-CP_dieu-20_khoan-7_diem-c` — Được sử dụng để phân bổ ngân sách, nguồn lực công hoặc xác định mức hưởng, đối tượng thụ hưởng chính sách, chế độ;
- `142-2026-ND-CP_dieu-20_khoan-7_diem-d` — Được sử dụng để phát hiện, lựa chọn, sàng lọc hoặc giám sát tổ chức, cá nhân phục vụ hoạt động quản lý nhà nước.
- `142-2026-ND-CP_dieu-20_khoan-8` — Bộ Khoa học và Công nghệ có trách nhiệm theo dõi, giám sát việc thực hiện đánh giá tác động đối với việc sử dụng hệ thống trí tuệ nhân tạo trong cơ quan nhà nước; tổng hợp, báo cáo Thủ tướng Chính phủ khi cần thiết.
- `142-2026-ND-CP_dieu-20_khoan-9` — Kinh phí thực hiện đánh giá tác động được bảo đảm từ nguồn ngân sách nhà nước theo phân cấp ngân sách, nguồn thu hợp pháp của đơn vị sự nghiệp công lập và nguồn kinh phí hợp pháp khác theo quy định của pháp luật.

## Gold chunk review

### Chunk 1

chunk_id: `142-2026-ND-CP_dieu-20_khoan-1_diem-a`

Legal location: 142/2026/NĐ-CP, Điều 20, khoản 1, điểm a

Text:

Hệ thống thuộc nhóm hệ thống trí tuệ nhân tạo có rủi ro cao theo quy định của Luật;

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 2

chunk_id: `142-2026-ND-CP_dieu-20_khoan-1_diem-b`

Legal location: 142/2026/NĐ-CP, Điều 20, khoản 1, điểm b

Text:

Hệ thống trí tuệ nhân tạo quy định tại khoản 7 Điều này mà kết quả của hệ thống được sử dụng làm căn cứ trực tiếp để người có thẩm quyền xem xét, quyết định ban hành quyết định hành chính.

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 3

chunk_id: `142-2026-ND-CP_dieu-20_khoan-2`

Legal location: 142/2026/NĐ-CP, Điều 20, khoản 2

Text:

Trường hợp hệ thống trí tuệ nhân tạo quy định tại khoản 1 Điều này có thay đổi về mục đích sử dụng, chức năng chính, nguồn dữ liệu đầu vào chủ yếu hoặc phạm vi đối tượng áp dụng làm phát sinh rủi ro mới hoặc làm thay đổi mức độ rủi ro của hệ thống, cơ quan, đơn vị triển khai phải thực hiện đánh giá tác động bổ sung trước khi tiếp tục sử dụng hệ thống.

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 4

chunk_id: `142-2026-ND-CP_dieu-20_khoan-7_diem-a`

Legal location: 142/2026/NĐ-CP, Điều 20, khoản 7, điểm a

Text:

Kết quả của hệ thống được sử dụng làm căn cứ trong quá trình xem xét, quyết định trong hoạt động quản lý nhà nước hoặc cung cấp dịch vụ công;

Reason selected:

Cần để xác lập phạm vi/nghĩa vụ hoặc giải nghĩa dẫn chiếu, nhưng không tự nó là toàn bộ đáp án.

Assessment:
- SUPPORTING

### Chunk 5

chunk_id: `142-2026-ND-CP_dieu-20_khoan-7_diem-b`

Legal location: 142/2026/NĐ-CP, Điều 20, khoản 7, điểm b

Text:

Được sử dụng để phân loại, chấm điểm, đánh giá hoặc xếp hạng tổ chức, cá nhân;

Reason selected:

Cần để xác lập phạm vi/nghĩa vụ hoặc giải nghĩa dẫn chiếu, nhưng không tự nó là toàn bộ đáp án.

Assessment:
- SUPPORTING

### Chunk 6

chunk_id: `142-2026-ND-CP_dieu-20_khoan-7_diem-c`

Legal location: 142/2026/NĐ-CP, Điều 20, khoản 7, điểm c

Text:

Được sử dụng để phân bổ ngân sách, nguồn lực công hoặc xác định mức hưởng, đối tượng thụ hưởng chính sách, chế độ;

Reason selected:

Cần để xác lập phạm vi/nghĩa vụ hoặc giải nghĩa dẫn chiếu, nhưng không tự nó là toàn bộ đáp án.

Assessment:
- SUPPORTING

### Chunk 7

chunk_id: `142-2026-ND-CP_dieu-20_khoan-7_diem-d`

Legal location: 142/2026/NĐ-CP, Điều 20, khoản 7, điểm d

Text:

Được sử dụng để phát hiện, lựa chọn, sàng lọc hoặc giám sát tổ chức, cá nhân phục vụ hoạt động quản lý nhà nước.

Reason selected:

Cần để xác lập phạm vi/nghĩa vụ hoặc giải nghĩa dẫn chiếu, nhưng không tự nó là toàn bộ đáp án.

Assessment:
- SUPPORTING

## Coverage analysis

Câu hỏi cần trả lời những ý nào?
1. Hệ thống rủi ro cao.
2. Hệ thống thuộc khoản 7 có đầu ra dùng trực tiếp cho quyết định hành chính.
3. Bốn nhóm hệ thống tại khoản 7 để giải nghĩa dẫn chiếu.
4. Đánh giá bổ sung khi thay đổi làm phát sinh hoặc đổi mức rủi ro.

Gold hiện tại có bao phủ từng ý không?
- Ý 1 → `142-2026-ND-CP_dieu-20_khoan-1_diem-a`.
- Ý 2 → `142-2026-ND-CP_dieu-20_khoan-1_diem-b`.
- Ý 3 → `142-2026-ND-CP_dieu-20_khoan-7_diem-a`, `142-2026-ND-CP_dieu-20_khoan-7_diem-b`, `142-2026-ND-CP_dieu-20_khoan-7_diem-c`, `142-2026-ND-CP_dieu-20_khoan-7_diem-d`.
- Ý 4 → `142-2026-ND-CP_dieu-20_khoan-2`.

Missing coverage:

Không.

Potential unnecessary chunks:

Không có chunk về nội dung báo cáo hay trách nhiệm ngoài điều kiện. Bốn điểm khoản 7 là SUPPORTING vì khoản 1 điểm b dẫn chiếu trực tiếp đến khoản này; chúng không phải điều kiện độc lập nếu thiếu yêu cầu đầu ra được dùng trực tiếp cho quyết định hành chính.

## Ambiguity

Trung bình. Cần phân biệt đánh giá ban đầu với đánh giá bổ sung; wording “trong trường hợp nào” đủ rộng để bao gồm cả hai.

## Recommended human decision

Suggested action: **KEEP**

Reason:

Giữ nguyên nhưng khi human review cần đọc khoản 1 điểm b cùng khoản 7 theo quan hệ liên kết, tránh diễn giải bốn điểm khoản 7 thành bốn trigger độc lập.

## Human decision

- [ ] KEEP
- [ ] REMOVE_CHUNK
- [ ] ADD_CHUNK
- [ ] REWRITE_QUERY
- [ ] SPLIT_QUERY
- [ ] NEEDS_REVIEW

Human notes:


---

# eval029

## Query

Khi hệ thống AI có thể ảnh hưởng đáng kể đến quyền con người thì cần áp dụng biện pháp kiểm soát nào?

## Current annotation

Query type: rights_risk  
Difficulty: hard  
Annotation status: in_review

Gold documents:
- 05-2026-TT-BKHCN

Gold articles:
- 05-2026-TT-BKHCN_dieu-3

Gold chunks:
- 05-2026-TT-BKHCN_dieu-3_khoan-1_diem-c
- 05-2026-TT-BKHCN_dieu-3_khoan-2_diem-a

## Why this query was flagged

Query không nêu khu vực áp dụng trong khi corpus có quy định chung và quy định riêng cho khu vực công.

## Article context

### Article 05-2026-TT-BKHCN_dieu-3

Title: Khung đạo đức trí tuệ nhân tạo quốc gia  
Document: Khung đạo đức trí tuệ nhân tạo quốc gia (05/2026/TT-BKHCN)  
Structure: Không chia chương  
Review role: PRIMARY

Article context:
- `05-2026-TT-BKHCN_dieu-3_khoan-1_diem-a` — Thiết kế an toàn ngay từ đầu: Tổ chức, cá nhân có trách nhiệm xác định trước các kịch bản gây hại có thể xảy ra đối với tính mạng, sức khỏe, danh dự, nhân phẩm và xây dựng biện pháp phòng ngừa.
- `05-2026-TT-BKHCN_dieu-3_khoan-1_diem-b` — Độ tin cậy và chất lượng: Tổ chức, cá nhân có trách nhiệm thiết lập tiêu chí chất lượng dữ liệu, mô hình, kết quả đầu ra; thực hiện xây dựng các cơ chế kiểm thử, xác nhận, kiểm định nội bộ trước khi triển khai.
- `05-2026-TT-BKHCN_dieu-3_khoan-1_diem-c` — Kiểm soát của con người: Tổ chức, cá nhân có trách nhiệm xây dựng cơ chế giám sát và can thiệp của con người phù hợp với mức độ ảnh hưởng của hệ thống; bảo đảm duy trì sự kiểm soát và khả năng can thiệp của con người đối với mọi quyết định và hành vi của hệ thống trí tuệ nhân tạo.
- `05-2026-TT-BKHCN_dieu-3_khoan-1_diem-d` — Khả năng phục hồi, ứng phó và bảo mật: Tổ chức, cá nhân xây dựng cơ chế tiếp nhận phản ánh, phát hiện lỗi và khắc phục; có kế hoạch dự phòng trong trường hợp hệ thống hoạt động sai lệch hoặc bị lạm dụng.
- `05-2026-TT-BKHCN_dieu-3_khoan-1_diem-e` — Bảo đảm an ninh của hệ thống trí tuệ nhân tạo: Tổ chức, cá nhân áp dụng biện pháp bảo vệ phù hợp để phòng ngừa, phát hiện, ngăn chặn và ứng phó với các hành vi xâm nhập, chiếm quyền điều khiển, đầu độc dữ liệu, đầu độc mô hình, tấn công đối nghịch, khai thác lỗ hổng, rò rỉ dữ liệu và lạm dụng hệ thống trí tuệ nhân tạo; bảo đảm tính bí mật, toàn vẹn và sẵn sàng của dữ liệu, mô hình, thuật toán và hạ tầng liên quan.
- `05-2026-TT-BKHCN_dieu-3_khoan-2_diem-a` — Tôn trọng quyền con người, quyền công dân: Tổ chức, cá nhân áp dụng biện pháp rà soát phù hợp để bảo đảm hệ thống trí tuệ nhân tạo không xâm phạm quyền riêng tư, dữ liệu cá nhân, tự do ý chí, quyền tiếp cận thông tin, quyền được đối xử bình đẳng và các quyền hợp pháp khác theo quy định của pháp luật.
- `05-2026-TT-BKHCN_dieu-3_khoan-2_diem-b` — Công bằng và không phân biệt đối xử: Tổ chức, cá nhân sử dụng các biện pháp nhận diện và giảm thiểu thiên lệch dữ liệu, thiên lệch mô hình và thiên lệch vận hành; bảo đảm xem xét đầy đủ tác động đến nhóm dễ bị tổn thương bao gồm trẻ em, người cao tuổi, người khuyết tật, nhóm yếu thế.
- `05-2026-TT-BKHCN_dieu-3_khoan-2_diem-c` — Minh bạch: Tổ chức, cá nhân xây dựng thông báo phù hợp về việc có sử dụng trí tuệ nhân tạo; bảo đảm cung cấp thông tin ở mức hợp lý về mục tiêu, phạm vi, dữ liệu, cách thức hoạt động tổng quát và giới hạn của hệ thống; bảo đảm không gây hiểu nhầm về năng lực của hệ thống.
- `05-2026-TT-BKHCN_dieu-3_khoan-2_diem-d` — Khả năng giải thích và trách nhiệm giải trình: Tổ chức, cá nhân xác định rõ các tác động mà hệ thống có thể gây ra, chuẩn bị tài liệu giải thích và bằng chứng về quá trình thiết kế, huấn luyện, kiểm thử. Phân định rõ chủ thể chịu trách nhiệm giải trình đối với các quyết định do hệ thống tạo ra.
- `05-2026-TT-BKHCN_dieu-3_khoan-3_diem-a` — Lợi ích xã hội: Tổ chức, cá nhân xác định rõ lợi ích công cộng, giá trị gia tăng và tác động tích cực của hệ thống đối với con người và cộng đồng; có phương án xử lý, khắc phục tác động tiêu cực trước khi triển khai.
- `05-2026-TT-BKHCN_dieu-3_khoan-3_diem-b` — Phát triển bao trùm: Tổ chức, cá nhân đảm bảo ưu tiên thiết kế giao diện dễ tiếp cận, dễ sử dụng; thu hẹp khoảng cách số giữa các vùng miền, nhóm dân cư.
- `05-2026-TT-BKHCN_dieu-3_khoan-3_diem-c` — Phát triển bền vững: Tổ chức, cá nhân phát triển hoặc triển khai hệ thống trí tuệ nhân tạo có trách nhiệm xem xét mức tiêu thụ năng lượng, tài nguyên tính toán và tác động môi trường trong suốt vòng đời hệ thống; ưu tiên lựa chọn giải pháp kỹ thuật, hạ tầng và quy trình vận hành tiết kiệm năng lượng, hạn chế phát thải.
- `05-2026-TT-BKHCN_dieu-3_khoan-3_diem-d` — Tôn trọng văn hóa và giá trị xã hội: Tổ chức, cá nhân thiết kế hệ thống trí tuệ nhân tạo theo hướng phù hợp chuẩn mực đạo đức xã hội và bản sắc văn hóa Việt Nam; không được tạo ra các nội dung kỳ thị, phân biệt đối xử hoặc ảnh hưởng đến lợi ích cộng đồng.
- `05-2026-TT-BKHCN_dieu-3_khoan-4_diem-a` — Khuyến khích đổi mới: Tổ chức, cá nhân triển khai thử nghiệm, thí điểm và mở rộng ứng dụng trí tuệ nhân tạo theo hướng có trách nhiệm; thúc đẩy nghiên cứu mở, chia sẻ tri thức phù hợp quy định pháp luật và bảo vệ quyền sở hữu trí tuệ.
- `05-2026-TT-BKHCN_dieu-3_khoan-4_diem-b` — Trách nhiệm xã hội: Tổ chức, cá nhân phát triển, triển khai và sử dụng hệ thống trí tuệ nhân tạo phân định rõ trách nhiệm của các chủ thể trong vòng đời hệ thống; bảo đảm có đầu mối tiếp nhận, xử lý khiếu nại và khắc phục hậu quả.
- `05-2026-TT-BKHCN_dieu-3_khoan-4_diem-c` — Nâng cao năng lực và hợp tác: Tổ chức, cá nhân chú trọng đào tạo về nhận thức, rủi ro đạo đức, kỹ năng sử dụng trí tuệ nhân tạo an toàn cho cán bộ, người lao động; tăng cường hợp tác và học hỏi các tiêu chuẩn quốc tế về đạo đức trí tuệ nhân tạo.
- `05-2026-TT-BKHCN_dieu-3_khoan-4_diem-d` — Hợp tác và học hỏi: Tổ chức, cá nhân tăng cường hợp tác quốc tế, tham gia sáng kiến, tiêu chuẩn, bộ quy tắc ứng xử về đạo đức trí tuệ nhân tạo; tận dụng sáng kiến khu vực tư nhân phục vụ lợi ích công theo điều kiện Việt Nam.

## Gold chunk review

### Chunk 1

chunk_id: `05-2026-TT-BKHCN_dieu-3_khoan-1_diem-c`

Legal location: 05/2026/TT-BKHCN, Điều 3, khoản 1, điểm c

Text:

Kiểm soát của con người: Tổ chức, cá nhân có trách nhiệm xây dựng cơ chế giám sát và can thiệp của con người phù hợp với mức độ ảnh hưởng của hệ thống; bảo đảm duy trì sự kiểm soát và khả năng can thiệp của con người đối với mọi quyết định và hành vi của hệ thống trí tuệ nhân tạo.

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 2

chunk_id: `05-2026-TT-BKHCN_dieu-3_khoan-2_diem-a`

Legal location: 05/2026/TT-BKHCN, Điều 3, khoản 2, điểm a

Text:

Tôn trọng quyền con người, quyền công dân: Tổ chức, cá nhân áp dụng biện pháp rà soát phù hợp để bảo đảm hệ thống trí tuệ nhân tạo không xâm phạm quyền riêng tư, dữ liệu cá nhân, tự do ý chí, quyền tiếp cận thông tin, quyền được đối xử bình đẳng và các quyền hợp pháp khác theo quy định của pháp luật.

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

## Coverage analysis

Câu hỏi cần trả lời những ý nào?
1. Cơ chế giám sát và can thiệp của con người tương xứng mức ảnh hưởng.
2. Rà soát để không xâm phạm các quyền hợp pháp.

Gold hiện tại có bao phủ từng ý không?
- Ý 1 → `05-2026-TT-BKHCN_dieu-3_khoan-1_diem-c`.
- Ý 2 → `05-2026-TT-BKHCN_dieu-3_khoan-2_diem-a`.

Missing coverage:

Thiếu căn cứ đánh giá tác động nếu người hỏi muốn nói riêng cơ quan nhà nước; không thiếu theo cách hiểu Khung đạo đức áp dụng chung.

Potential unnecessary chunks:

Không theo cách hiểu hiện tại.

## Ambiguity

Có hai cách hiểu. (1) Áp dụng chung: Khung đạo đức yêu cầu rà soát quyền và cơ chế giám sát/can thiệp tương xứng mức ảnh hưởng. (2) Khu vực công: Điều 27 Luật và Điều 20 Nghị định yêu cầu báo cáo đánh giá tác động, nhận diện rủi ro, biện pháp kiểm soát và giám sát con người. Gold hiện tại chỉ theo cách hiểu (1).

## Recommended human decision

Suggested action: **REWRITE_QUERY**

Reason:

Nên viết rõ “Theo Khung đạo đức AI quốc gia, tổ chức, cá nhân phải áp dụng biện pháp nào...” để giữ gold hiện tại; hoặc viết riêng câu về cơ quan nhà nước và đánh giá tác động.

## Human decision

- [ ] KEEP
- [ ] REMOVE_CHUNK
- [ ] ADD_CHUNK
- [ ] REWRITE_QUERY
- [ ] SPLIT_QUERY
- [ ] NEEDS_REVIEW

Human notes:


---

# eval030

## Query

Những yêu cầu nào giúp bảo đảm con người vẫn có khả năng giám sát và can thiệp vào hệ thống AI?

## Current annotation

Query type: human_oversight  
Difficulty: hard  
Annotation status: in_review

Gold documents:
- 134-2025-QH15
- 05-2026-TT-BKHCN

Gold articles:
- 134-2025-QH15_dieu-4
- 05-2026-TT-BKHCN_dieu-3

Gold chunks:
- 134-2025-QH15_dieu-4_khoan-2
- 05-2026-TT-BKHCN_dieu-3_khoan-1_diem-c

## Why this query was flagged

Gold gồm Luật và Khung đạo đức dù chunk của Luật có thể tự trả lời đầy đủ.

## Article context

### Article 134-2025-QH15_dieu-4

Title: Nguyên tắc cơ bản trong hoạt động trí tuệ nhân tạo  
Document: Luật Trí tuệ nhân tạo (134/2025/QH15)  
Structure: Chương I — QUY ĐỊNH CHUNG  
Review role: PRIMARY LEGAL BASIS

Article context:
- `134-2025-QH15_dieu-4_khoan-1` — Lấy con người làm trung tâm; bảo đảm quyền con người, quyền riêng tư, lợi ích quốc gia, lợi ích công cộng và an ninh quốc gia; tuân thủ Hiến pháp và pháp luật.
- `134-2025-QH15_dieu-4_khoan-2` — Trí tuệ nhân tạo phục vụ con người, không thay thế thẩm quyền và trách nhiệm của con người. Bảo đảm duy trì sự kiểm soát và khả năng can thiệp của con người đối với mọi quyết định và hành vi của hệ thống trí tuệ nhân tạo; an toàn hệ thống, an ninh dữ liệu và bảo mật thông tin; khả năng kiểm tra và giám sát quá trình phát triển và vận hành hệ thống trí tuệ nhân tạo.
- `134-2025-QH15_dieu-4_khoan-3` — Bảo đảm công bằng, minh bạch, không thiên lệch, không phân biệt đối xử và không gây hại cho con người hoặc xã hội; tuân thủ chuẩn mực đạo đức và giá trị văn hóa Việt Nam; thực hiện trách nhiệm giải trình về các quyết định và hệ quả của hệ thống trí tuệ nhân tạo.
- `134-2025-QH15_dieu-4_khoan-4` — Thúc đẩy phát triển trí tuệ nhân tạo xanh, bao trùm và bền vững; khuyến khích phát triển và ứng dụng các công nghệ trí tuệ nhân tạo theo hướng sử dụng hiệu quả năng lượng, tiết kiệm tài nguyên và giảm tác động tiêu cực đến môi trường.

### Article 05-2026-TT-BKHCN_dieu-3

Title: Khung đạo đức trí tuệ nhân tạo quốc gia  
Document: Khung đạo đức trí tuệ nhân tạo quốc gia (05/2026/TT-BKHCN)  
Structure: Không chia chương  
Review role: SUPPORTING GUIDANCE

Article context:
- `05-2026-TT-BKHCN_dieu-3_khoan-1_diem-a` — Thiết kế an toàn ngay từ đầu: Tổ chức, cá nhân có trách nhiệm xác định trước các kịch bản gây hại có thể xảy ra đối với tính mạng, sức khỏe, danh dự, nhân phẩm và xây dựng biện pháp phòng ngừa.
- `05-2026-TT-BKHCN_dieu-3_khoan-1_diem-b` — Độ tin cậy và chất lượng: Tổ chức, cá nhân có trách nhiệm thiết lập tiêu chí chất lượng dữ liệu, mô hình, kết quả đầu ra; thực hiện xây dựng các cơ chế kiểm thử, xác nhận, kiểm định nội bộ trước khi triển khai.
- `05-2026-TT-BKHCN_dieu-3_khoan-1_diem-c` — Kiểm soát của con người: Tổ chức, cá nhân có trách nhiệm xây dựng cơ chế giám sát và can thiệp của con người phù hợp với mức độ ảnh hưởng của hệ thống; bảo đảm duy trì sự kiểm soát và khả năng can thiệp của con người đối với mọi quyết định và hành vi của hệ thống trí tuệ nhân tạo.
- `05-2026-TT-BKHCN_dieu-3_khoan-1_diem-d` — Khả năng phục hồi, ứng phó và bảo mật: Tổ chức, cá nhân xây dựng cơ chế tiếp nhận phản ánh, phát hiện lỗi và khắc phục; có kế hoạch dự phòng trong trường hợp hệ thống hoạt động sai lệch hoặc bị lạm dụng.
- `05-2026-TT-BKHCN_dieu-3_khoan-1_diem-e` — Bảo đảm an ninh của hệ thống trí tuệ nhân tạo: Tổ chức, cá nhân áp dụng biện pháp bảo vệ phù hợp để phòng ngừa, phát hiện, ngăn chặn và ứng phó với các hành vi xâm nhập, chiếm quyền điều khiển, đầu độc dữ liệu, đầu độc mô hình, tấn công đối nghịch, khai thác lỗ hổng, rò rỉ dữ liệu và lạm dụng hệ thống trí tuệ nhân tạo; bảo đảm tính bí mật, toàn vẹn và sẵn sàng của dữ liệu, mô hình, thuật toán và hạ tầng liên quan.
- `05-2026-TT-BKHCN_dieu-3_khoan-2_diem-a` — Tôn trọng quyền con người, quyền công dân: Tổ chức, cá nhân áp dụng biện pháp rà soát phù hợp để bảo đảm hệ thống trí tuệ nhân tạo không xâm phạm quyền riêng tư, dữ liệu cá nhân, tự do ý chí, quyền tiếp cận thông tin, quyền được đối xử bình đẳng và các quyền hợp pháp khác theo quy định của pháp luật.
- `05-2026-TT-BKHCN_dieu-3_khoan-2_diem-b` — Công bằng và không phân biệt đối xử: Tổ chức, cá nhân sử dụng các biện pháp nhận diện và giảm thiểu thiên lệch dữ liệu, thiên lệch mô hình và thiên lệch vận hành; bảo đảm xem xét đầy đủ tác động đến nhóm dễ bị tổn thương bao gồm trẻ em, người cao tuổi, người khuyết tật, nhóm yếu thế.
- `05-2026-TT-BKHCN_dieu-3_khoan-2_diem-c` — Minh bạch: Tổ chức, cá nhân xây dựng thông báo phù hợp về việc có sử dụng trí tuệ nhân tạo; bảo đảm cung cấp thông tin ở mức hợp lý về mục tiêu, phạm vi, dữ liệu, cách thức hoạt động tổng quát và giới hạn của hệ thống; bảo đảm không gây hiểu nhầm về năng lực của hệ thống.
- `05-2026-TT-BKHCN_dieu-3_khoan-2_diem-d` — Khả năng giải thích và trách nhiệm giải trình: Tổ chức, cá nhân xác định rõ các tác động mà hệ thống có thể gây ra, chuẩn bị tài liệu giải thích và bằng chứng về quá trình thiết kế, huấn luyện, kiểm thử. Phân định rõ chủ thể chịu trách nhiệm giải trình đối với các quyết định do hệ thống tạo ra.
- `05-2026-TT-BKHCN_dieu-3_khoan-3_diem-a` — Lợi ích xã hội: Tổ chức, cá nhân xác định rõ lợi ích công cộng, giá trị gia tăng và tác động tích cực của hệ thống đối với con người và cộng đồng; có phương án xử lý, khắc phục tác động tiêu cực trước khi triển khai.
- `05-2026-TT-BKHCN_dieu-3_khoan-3_diem-b` — Phát triển bao trùm: Tổ chức, cá nhân đảm bảo ưu tiên thiết kế giao diện dễ tiếp cận, dễ sử dụng; thu hẹp khoảng cách số giữa các vùng miền, nhóm dân cư.
- `05-2026-TT-BKHCN_dieu-3_khoan-3_diem-c` — Phát triển bền vững: Tổ chức, cá nhân phát triển hoặc triển khai hệ thống trí tuệ nhân tạo có trách nhiệm xem xét mức tiêu thụ năng lượng, tài nguyên tính toán và tác động môi trường trong suốt vòng đời hệ thống; ưu tiên lựa chọn giải pháp kỹ thuật, hạ tầng và quy trình vận hành tiết kiệm năng lượng, hạn chế phát thải.
- `05-2026-TT-BKHCN_dieu-3_khoan-3_diem-d` — Tôn trọng văn hóa và giá trị xã hội: Tổ chức, cá nhân thiết kế hệ thống trí tuệ nhân tạo theo hướng phù hợp chuẩn mực đạo đức xã hội và bản sắc văn hóa Việt Nam; không được tạo ra các nội dung kỳ thị, phân biệt đối xử hoặc ảnh hưởng đến lợi ích cộng đồng.
- `05-2026-TT-BKHCN_dieu-3_khoan-4_diem-a` — Khuyến khích đổi mới: Tổ chức, cá nhân triển khai thử nghiệm, thí điểm và mở rộng ứng dụng trí tuệ nhân tạo theo hướng có trách nhiệm; thúc đẩy nghiên cứu mở, chia sẻ tri thức phù hợp quy định pháp luật và bảo vệ quyền sở hữu trí tuệ.
- `05-2026-TT-BKHCN_dieu-3_khoan-4_diem-b` — Trách nhiệm xã hội: Tổ chức, cá nhân phát triển, triển khai và sử dụng hệ thống trí tuệ nhân tạo phân định rõ trách nhiệm của các chủ thể trong vòng đời hệ thống; bảo đảm có đầu mối tiếp nhận, xử lý khiếu nại và khắc phục hậu quả.
- `05-2026-TT-BKHCN_dieu-3_khoan-4_diem-c` — Nâng cao năng lực và hợp tác: Tổ chức, cá nhân chú trọng đào tạo về nhận thức, rủi ro đạo đức, kỹ năng sử dụng trí tuệ nhân tạo an toàn cho cán bộ, người lao động; tăng cường hợp tác và học hỏi các tiêu chuẩn quốc tế về đạo đức trí tuệ nhân tạo.
- `05-2026-TT-BKHCN_dieu-3_khoan-4_diem-d` — Hợp tác và học hỏi: Tổ chức, cá nhân tăng cường hợp tác quốc tế, tham gia sáng kiến, tiêu chuẩn, bộ quy tắc ứng xử về đạo đức trí tuệ nhân tạo; tận dụng sáng kiến khu vực tư nhân phục vụ lợi ích công theo điều kiện Việt Nam.

## Gold chunk review

### Chunk 1

chunk_id: `134-2025-QH15_dieu-4_khoan-2`

Legal location: 134/2025/QH15, Điều 4, khoản 2

Text:

Trí tuệ nhân tạo phục vụ con người, không thay thế thẩm quyền và trách nhiệm của con người. Bảo đảm duy trì sự kiểm soát và khả năng can thiệp của con người đối với mọi quyết định và hành vi của hệ thống trí tuệ nhân tạo; an toàn hệ thống, an ninh dữ liệu và bảo mật thông tin; khả năng kiểm tra và giám sát quá trình phát triển và vận hành hệ thống trí tuệ nhân tạo.

Reason selected:

Trực tiếp cung cấp một phần nội dung cần có trong câu trả lời.

Assessment:
- DIRECT

### Chunk 2

chunk_id: `05-2026-TT-BKHCN_dieu-3_khoan-1_diem-c`

Legal location: 05/2026/TT-BKHCN, Điều 3, khoản 1, điểm c

Text:

Kiểm soát của con người: Tổ chức, cá nhân có trách nhiệm xây dựng cơ chế giám sát và can thiệp của con người phù hợp với mức độ ảnh hưởng của hệ thống; bảo đảm duy trì sự kiểm soát và khả năng can thiệp của con người đối với mọi quyết định và hành vi của hệ thống trí tuệ nhân tạo.

Reason selected:

Chỉ cần nếu giữ cách hiểu rộng hiện tại; có thể loại sau khi thu hẹp hoặc làm rõ query.

Assessment:
- QUESTIONABLE

## Coverage analysis

Câu hỏi cần trả lời những ý nào?
1. Không thay thế thẩm quyền và trách nhiệm con người.
2. Duy trì kiểm soát và khả năng can thiệp.
3. Cho phép kiểm tra, giám sát quá trình phát triển và vận hành.

Gold hiện tại có bao phủ từng ý không?
- Ý 1 → `134-2025-QH15_dieu-4_khoan-2`.
- Ý 2 → `134-2025-QH15_dieu-4_khoan-2`, `05-2026-TT-BKHCN_dieu-3_khoan-1_diem-c`.
- Ý 3 → `134-2025-QH15_dieu-4_khoan-2`.

Missing coverage:

Không sau khi chỉ giữ khoản 2 Điều 4 Luật.

Potential unnecessary chunks:

05-2026-TT-BKHCN_dieu-3_khoan-1_diem-c lặp lại nguyên tắc cốt lõi và chỉ bổ sung tính tương xứng mức ảnh hưởng; đây là SUPPORTING GUIDANCE, không cần để trả lời đầy đủ query retrieval hiện tại.

## Ambiguity

Thấp về nội dung, nhưng wording không yêu cầu hướng dẫn đạo đức nên ưu tiên căn cứ pháp lý trực tiếp và tối thiểu.

## Recommended human decision

Suggested action: **REMOVE_CHUNK**

Reason:

Đề xuất bỏ chunk của Thông tư khỏi gold và giữ 134-2025-QH15_dieu-4_khoan-2 làm PRIMARY LEGAL BASIS.

## Human decision

- [ ] KEEP
- [ ] REMOVE_CHUNK
- [ ] ADD_CHUNK
- [ ] REWRITE_QUERY
- [ ] SPLIT_QUERY
- [ ] NEEDS_REVIEW

Human notes:

