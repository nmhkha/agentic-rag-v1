# Generation annotation v1 human review

Review each point against the query and the complete supporting gold chunk text. Do not mark a record verified from this sheet; update the dataset only after human legal review.

## eval001

QUERY

Các mức phân loại rủi ro của hệ thống trí tuệ nhân tạo gồm những mức nào?

REQUIRED POINT P1

description: Rủi ro cao: có thể gây thiệt hại đáng kể đến các lợi ích được luật bảo vệ.
importance: required
supporting chunks: 134-2025-QH15_dieu-9_khoan-1_diem-a

full chunk text

### 134-2025-QH15_dieu-9_khoan-1_diem-a

```text
Hệ thống trí tuệ nhân tạo có rủi ro cao là hệ thống có thể gây thiệt hại đáng kể đến tính mạng, sức khỏe, quyền và lợi ích hợp pháp của tổ chức, cá nhân, lợi ích quốc gia, lợi ích công cộng, an ninh quốc gia;
```

REQUIRED POINT P2

description: Rủi ro trung bình: có thể gây nhầm lẫn, tác động hoặc thao túng vì người sử dụng không nhận biết được AI hoặc nội dung AI.
importance: required
supporting chunks: 134-2025-QH15_dieu-9_khoan-1_diem-b

full chunk text

### 134-2025-QH15_dieu-9_khoan-1_diem-b

```text
Hệ thống trí tuệ nhân tạo có rủi ro trung bình là hệ thống có khả năng gây nhầm lẫn, tác động hoặc thao túng người sử dụng do không nhận biết được chủ thể tương tác là hệ thống trí tuệ nhân tạo hoặc nội dung do hệ thống tạo ra;
```

REQUIRED POINT P3

description: Rủi ro thấp: không thuộc trường hợp rủi ro cao hoặc trung bình.
importance: required
supporting chunks: 134-2025-QH15_dieu-9_khoan-1_diem-c

full chunk text

### 134-2025-QH15_dieu-9_khoan-1_diem-c

```text
Hệ thống trí tuệ nhân tạo có rủi ro thấp là hệ thống không thuộc trường hợp quy định tại điểm a và điểm b khoản này.
```

REFERENCE ANSWER

Gồm rủi ro cao (có thể gây thiệt hại đáng kể), trung bình (có thể gây nhầm lẫn, tác động hoặc thao túng vì không nhận biết AI/nội dung AI), và thấp (không thuộc hai trường hợp trên).

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval002

QUERY

Ai có thẩm quyền ban hành danh mục hệ thống trí tuệ nhân tạo có rủi ro cao?

REQUIRED POINT P1

description: Thủ tướng Chính phủ có thẩm quyền ban hành, sửa đổi, bổ sung Danh mục hệ thống AI có rủi ro cao.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-7_khoan-2_diem-d

full chunk text

### 142-2026-ND-CP_dieu-7_khoan-2_diem-d

```text
Bộ Khoa học và Công nghệ có trách nhiệm chủ trì, phối hợp với các bộ, cơ quan ngang bộ và các tổ chức liên quan tổng hợp, xây dựng và trình Thủ tướng Chính phủ ban hành, sửa đổi, bổ sung Danh mục quy định tại khoản 1 Điều này trên cơ sở tiêu chí, nguyên tắc quy định tại Điều 8 của Nghị định này.
```

REQUIRED POINT P2

description: Bộ Khoa học và Công nghệ chủ trì phối hợp xây dựng và trình Danh mục trên cơ sở tiêu chí, nguyên tắc của Nghị định.
importance: important
supporting chunks: 142-2026-ND-CP_dieu-7_khoan-2_diem-d

full chunk text

### 142-2026-ND-CP_dieu-7_khoan-2_diem-d

```text
Bộ Khoa học và Công nghệ có trách nhiệm chủ trì, phối hợp với các bộ, cơ quan ngang bộ và các tổ chức liên quan tổng hợp, xây dựng và trình Thủ tướng Chính phủ ban hành, sửa đổi, bổ sung Danh mục quy định tại khoản 1 Điều này trên cơ sở tiêu chí, nguyên tắc quy định tại Điều 8 của Nghị định này.
```

REFERENCE ANSWER

Thủ tướng Chính phủ là người có thẩm quyền ban hành, sửa đổi, bổ sung Danh mục hệ thống AI có rủi ro cao. Bộ Khoa học và Công nghệ chủ trì phối hợp xây dựng và trình Danh mục.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval003

QUERY

Nhà cung cấp phải lập hồ sơ phân loại rủi ro vào thời điểm nào?

REQUIRED POINT P1

description: Trước khi đưa hệ thống rủi ro cao hoặc trung bình vào sử dụng.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-12_khoan-1

full chunk text

### 142-2026-ND-CP_dieu-12_khoan-1

```text
Nhà cung cấp phải lập hồ sơ phân loại rủi ro đối với hệ thống trí tuệ nhân tạo có rủi ro cao và hệ thống trí tuệ nhân tạo có rủi ro trung bình trước khi đưa hệ thống vào sử dụng theo quy định tại khoản 1 Điều 10 của Luật Trí tuệ nhân tạo.
```

REFERENCE ANSWER

Trước khi đưa hệ thống vào sử dụng, đối với hệ thống AI rủi ro cao và trung bình.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval004

QUERY

Nhà cung cấp hệ thống AI rủi ro cao phải duy trì những biện pháp quản lý nào?

REQUIRED POINT P1

description: Thiết lập và duy trì hệ thống quản lý rủi ro phù hợp với mục đích, phạm vi triển khai và mức độ rủi ro.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-15_khoan-1

full chunk text

### 142-2026-ND-CP_dieu-15_khoan-1

```text
Nhà cung cấp hệ thống trí tuệ nhân tạo có rủi ro cao phải thiết lập và duy trì hệ thống quản lý rủi ro đối với hệ thống do mình cung cấp phù hợp với mục đích sử dụng, phạm vi triển khai và mức độ rủi ro của hệ thống.
```

REQUIRED POINT P2

description: Xác định và đánh giá các rủi ro có thể phát sinh đối với quyền, an toàn, an ninh hoặc lợi ích công cộng.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-15_khoan-2_diem-a

full chunk text

### 142-2026-ND-CP_dieu-15_khoan-2_diem-a

```text
Xác định và đánh giá các rủi ro có thể phát sinh đối với quyền con người, an toàn, an ninh hoặc lợi ích công cộng trong quá trình thiết kế, phát triển và cung cấp hệ thống;
```

REQUIRED POINT P3

description: Bảo đảm chất lượng, tính phù hợp và tính đại diện của dữ liệu huấn luyện, kiểm thử và đánh giá trong phạm vi cần thiết.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-15_khoan-2_diem-b

full chunk text

### 142-2026-ND-CP_dieu-15_khoan-2_diem-b

```text
Bảo đảm chất lượng, tính phù hợp và tính đại diện của dữ liệu huấn luyện, dữ liệu kiểm thử và dữ liệu đánh giá trong phạm vi cần thiết để hạn chế rủi ro phát sinh từ dữ liệu;
```

REQUIRED POINT P4

description: Thiết kế và duy trì cơ chế giám sát, can thiệp của con người phù hợp với mức độ rủi ro.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-15_khoan-2_diem-c

full chunk text

### 142-2026-ND-CP_dieu-15_khoan-2_diem-c

```text
Thiết kế và duy trì cơ chế giám sát và can thiệp của con người phù hợp với mức độ rủi ro của hệ thống;
```

REQUIRED POINT P5

description: Áp dụng biện pháp kỹ thuật hoặc quản lý để phòng ngừa, hạn chế hoặc kiểm soát rủi ro đã xác định.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-15_khoan-2_diem-d

full chunk text

### 142-2026-ND-CP_dieu-15_khoan-2_diem-d

```text
Áp dụng biện pháp kỹ thuật hoặc biện pháp quản lý nhằm phòng ngừa, hạn chế hoặc kiểm soát các rủi ro đã được xác định;
```

REQUIRED POINT P6

description: Rà soát và cập nhật biện pháp quản lý rủi ro khi mô hình, dữ liệu, phương thức vận hành hoặc mục đích sử dụng thay đổi đáng kể.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-15_khoan-2_diem-đ

full chunk text

### 142-2026-ND-CP_dieu-15_khoan-2_diem-đ

```text
Rà soát và cập nhật biện pháp quản lý rủi ro khi hệ thống có thay đổi đáng kể về mô hình, dữ liệu, phương thức vận hành hoặc mục đích sử dụng.
```

REFERENCE ANSWER

Phải duy trì hệ thống quản lý rủi ro phù hợp mục đích, phạm vi và mức rủi ro; nhận diện rủi ro, bảo đảm dữ liệu phù hợp trong phạm vi cần thiết, có giám sát/can thiệp con người và biện pháp kiểm soát. Rà soát, cập nhật khi mô hình, dữ liệu, vận hành hoặc mục đích thay đổi đáng kể.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval005a

QUERY

Nhà cung cấp hệ thống trí tuệ nhân tạo có rủi ro cao phải thực hiện những nghĩa vụ quản lý nào?

REQUIRED POINT P1

description: Nhà cung cấp phải thiết lập, duy trì và rà soát biện pháp quản lý rủi ro khi có thay đổi đáng kể hoặc rủi ro mới.
importance: required
supporting chunks: 134-2025-QH15_dieu-14_khoan-1_diem-a

full chunk text

### 134-2025-QH15_dieu-14_khoan-1_diem-a

```text
Thiết lập và duy trì biện pháp quản lý rủi ro và thường xuyên rà soát khi hệ thống có thay đổi đáng kể hoặc phát sinh rủi ro mới;
```

REQUIRED POINT P2

description: Nhà cung cấp phải quản trị dữ liệu huấn luyện, kiểm thử và vận hành, bảo đảm chất lượng trong phạm vi khả năng kỹ thuật và phù hợp mục đích sử dụng.
importance: required
supporting chunks: 134-2025-QH15_dieu-14_khoan-1_diem-b

full chunk text

### 134-2025-QH15_dieu-14_khoan-1_diem-b

```text
Quản trị dữ liệu huấn luyện, kiểm thử và vận hành bảo đảm chất lượng trong phạm vi khả năng kỹ thuật và phù hợp với mục đích sử dụng của hệ thống;
```

REQUIRED POINT P3

description: Nhà cung cấp phải lập, cập nhật, lưu giữ hồ sơ kỹ thuật và nhật ký ở mức cần thiết; cung cấp thông tin cần thiết, tương xứng cho kiểm tra nhưng không làm lộ bí mật kinh doanh.
importance: required
supporting chunks: 134-2025-QH15_dieu-14_khoan-1_diem-c

full chunk text

### 134-2025-QH15_dieu-14_khoan-1_diem-c

```text
Lập, cập nhật, lưu giữ hồ sơ kỹ thuật và nhật ký hoạt động ở mức cần thiết cho việc đánh giá sự phù hợp và kiểm tra sau khi đưa vào sử dụng; cung cấp các thông tin này cho cơ quan nhà nước có thẩm quyền theo nguyên tắc cần thiết, tương xứng với mục đích kiểm tra và không làm lộ bí mật kinh doanh;
```

REQUIRED POINT P4

description: Nhà cung cấp phải thiết kế hệ thống bảo đảm khả năng giám sát và can thiệp của con người.
importance: required
supporting chunks: 134-2025-QH15_dieu-14_khoan-1_diem-d

full chunk text

### 134-2025-QH15_dieu-14_khoan-1_diem-d

```text
Thiết kế hệ thống bảo đảm khả năng giám sát và can thiệp của con người đối với hệ thống;
```

REQUIRED POINT P5

description: Nhà cung cấp phải thực hiện nghĩa vụ minh bạch và xử lý sự cố.
importance: required
supporting chunks: 134-2025-QH15_dieu-14_khoan-1_diem-đ

full chunk text

### 134-2025-QH15_dieu-14_khoan-1_diem-đ

```text
Thực hiện nghĩa vụ minh bạch và xử lý sự cố theo quy định tại Điều 11 và Điều 12 của Luật này;
```

REQUIRED POINT P6

description: Nhà cung cấp phải giải trình và cung cấp thông tin cần thiết cho cơ quan, người sử dụng và người bị ảnh hưởng; việc cung cấp không được bộc lộ mã nguồn, thuật toán chi tiết, tham số, bí mật kinh doanh hoặc bí mật công nghệ.
importance: required
supporting chunks: 134-2025-QH15_dieu-14_khoan-1_diem-e

full chunk text

### 134-2025-QH15_dieu-14_khoan-1_diem-e

```text
Thực hiện trách nhiệm giải trình đối với cơ quan nhà nước có thẩm quyền về mục đích sử dụng, nguyên lý hoạt động ở mức mô tả chức năng, loại dữ liệu đầu vào chủ yếu, biện pháp quản lý và kiểm soát rủi ro cùng các nội dung cần thiết phục vụ thanh tra, kiểm tra; cung cấp cho người sử dụng và người bị ảnh hưởng các thông tin công khai ở mức mô tả chức năng, cách thức vận hành và cảnh báo rủi ro để bảo đảm an toàn trong sử dụng. Việc giải trình và cung cấp thông tin không được yêu cầu tiết lộ mã nguồn, thuật toán chi tiết, bộ tham số hoặc thông tin thuộc bí mật kinh doanh, bí mật công nghệ;
```

REQUIRED POINT P7

description: Nhà cung cấp phải phối hợp với cơ quan nhà nước có thẩm quyền và bên triển khai trong kiểm tra, đánh giá, hậu kiểm và khắc phục sự cố.
importance: required
supporting chunks: 134-2025-QH15_dieu-14_khoan-1_diem-g

full chunk text

### 134-2025-QH15_dieu-14_khoan-1_diem-g

```text
Phối hợp với cơ quan nhà nước có thẩm quyền và bên triển khai trong kiểm tra, đánh giá, hậu kiểm và khắc phục sự cố liên quan đến hệ thống.
```

REFERENCE ANSWER

Phải quản lý rủi ro, quản trị dữ liệu trong khả năng kỹ thuật và đúng mục đích, lưu giữ hồ sơ/nhật ký cần thiết, bảo đảm giám sát con người, minh bạch, xử lý sự cố, giải trình và phối hợp kiểm tra, hậu kiểm, khắc phục. Cung cấp thông tin không được buộc lộ bí mật kinh doanh/công nghệ.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval005b

QUERY

Bên triển khai hệ thống trí tuệ nhân tạo có rủi ro cao phải thực hiện những nghĩa vụ quản lý nào?

REQUIRED POINT P1

description: Bên triển khai phải vận hành và giám sát hệ thống đúng mục đích, phạm vi và mức rủi ro đã phân loại, không làm phát sinh rủi ro mới hoặc cao hơn.
importance: required
supporting chunks: 134-2025-QH15_dieu-14_khoan-2_diem-a

full chunk text

### 134-2025-QH15_dieu-14_khoan-2_diem-a

```text
Vận hành và giám sát hệ thống đúng mục đích, phạm vi và mức độ rủi ro đã được phân loại, không làm phát sinh rủi ro mới hoặc rủi ro cao hơn;
```

REQUIRED POINT P2

description: Bên triển khai phải bảo đảm an toàn, bảo mật dữ liệu và khả năng can thiệp của con người trong quá trình sử dụng.
importance: required
supporting chunks: 134-2025-QH15_dieu-14_khoan-2_diem-b

full chunk text

### 134-2025-QH15_dieu-14_khoan-2_diem-b

```text
Bảo đảm an toàn, bảo mật dữ liệu và khả năng can thiệp của con người trong quá trình sử dụng;
```

REQUIRED POINT P3

description: Bên triển khai phải duy trì tuân thủ tiêu chuẩn, quy chuẩn kỹ thuật về AI trong quá trình vận hành.
importance: required
supporting chunks: 134-2025-QH15_dieu-14_khoan-2_diem-c

full chunk text

### 134-2025-QH15_dieu-14_khoan-2_diem-c

```text
Duy trì việc tuân thủ tiêu chuẩn, quy chuẩn kỹ thuật về trí tuệ nhân tạo trong quá trình vận hành hệ thống;
```

REQUIRED POINT P4

description: Bên triển khai phải thực hiện nghĩa vụ minh bạch và xử lý sự cố.
importance: required
supporting chunks: 134-2025-QH15_dieu-14_khoan-2_diem-d

full chunk text

### 134-2025-QH15_dieu-14_khoan-2_diem-d

```text
Thực hiện nghĩa vụ minh bạch và xử lý sự cố theo quy định tại Điều 11 và Điều 12 của Luật này;
```

REQUIRED POINT P5

description: Bên triển khai phải giải trình và cung cấp thông tin cần thiết cho cơ quan, người sử dụng và người bị ảnh hưởng về việc vận hành, kiểm soát rủi ro và sự cố.
importance: required
supporting chunks: 134-2025-QH15_dieu-14_khoan-2_diem-đ

full chunk text

### 134-2025-QH15_dieu-14_khoan-2_diem-đ

```text
Thực hiện trách nhiệm giải trình đối với cơ quan nhà nước có thẩm quyền về việc vận hành hệ thống, biện pháp kiểm soát rủi ro, xử lý sự cố và các nội dung cần thiết phục vụ công tác thanh tra, kiểm tra; cung cấp cho người sử dụng và người bị ảnh hưởng các thông tin công khai ở mức mô tả chức năng, cách thức vận hành và cảnh báo rủi ro nhằm bảo đảm an toàn trong sử dụng;
```

REQUIRED POINT P6

description: Bên triển khai phải phối hợp với nhà cung cấp và cơ quan nhà nước có thẩm quyền trong kiểm tra, đánh giá, hậu kiểm và khắc phục sự cố.
importance: required
supporting chunks: 134-2025-QH15_dieu-14_khoan-2_diem-e

full chunk text

### 134-2025-QH15_dieu-14_khoan-2_diem-e

```text
Phối hợp với nhà cung cấp và cơ quan nhà nước có thẩm quyền trong kiểm tra, đánh giá, hậu kiểm và khắc phục sự cố.
```

REFERENCE ANSWER

Phải vận hành, giám sát đúng mục đích, phạm vi và mức rủi ro đã phân loại, không phát sinh rủi ro mới/cao hơn; bảo đảm an toàn, bảo mật dữ liệu, can thiệp con người; tuân thủ chuẩn, minh bạch, xử lý sự cố, giải trình và phối hợp kiểm tra, hậu kiểm, khắc phục.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval006

QUERY

Trách nhiệm minh bạch của nhà cung cấp hệ thống trí tuệ nhân tạo bao gồm những gì?

REQUIRED POINT P1

description: Bảo đảm người sử dụng biết mình đang tương tác với AI, trừ trường hợp pháp luật có quy định khác.
importance: required
supporting chunks: 134-2025-QH15_dieu-11_khoan-1

full chunk text

### 134-2025-QH15_dieu-11_khoan-1

```text
Nhà cung cấp bảo đảm hệ thống trí tuệ nhân tạo tương tác trực tiếp với con người được thiết kế và vận hành để người sử dụng nhận biết khi đang tương tác với hệ thống, trừ trường hợp pháp luật có quy định khác.
```

REQUIRED POINT P2

description: Đánh dấu âm thanh, hình ảnh và video do AI tạo ra ở định dạng máy đọc theo quy định.
importance: required
supporting chunks: 134-2025-QH15_dieu-11_khoan-2

full chunk text

### 134-2025-QH15_dieu-11_khoan-2

```text
Nhà cung cấp bảo đảm các nội dung âm thanh, hình ảnh, video do hệ thống trí tuệ nhân tạo tạo ra được đánh dấu ở định dạng máy đọc theo quy định của Chính phủ.
```

REQUIRED POINT P3

description: Nhà cung cấp và bên triển khai phải duy trì thông tin minh bạch trong suốt quá trình cung cấp hệ thống, sản phẩm hoặc nội dung.
importance: required
supporting chunks: 134-2025-QH15_dieu-11_khoan-5

full chunk text

### 134-2025-QH15_dieu-11_khoan-5

```text
Nhà cung cấp và bên triển khai có trách nhiệm duy trì thông tin minh bạch theo quy định tại Điều này trong suốt quá trình cung cấp hệ thống, sản phẩm hoặc nội dung cho người sử dụng.
```

REFERENCE ANSWER

Phải bảo đảm người dùng biết đang tương tác với AI, trừ trường hợp pháp luật quy định khác; đánh dấu âm thanh, hình ảnh, video AI tạo ra ở định dạng máy đọc; và duy trì thông tin minh bạch suốt quá trình cung cấp.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval007

QUERY

Nội dung do AI tạo ra phải được thông báo hoặc gắn nhãn như thế nào?

REQUIRED POINT P1

description: Thông báo hoặc nhãn phải rõ ràng, dễ hiểu và dễ nhận biết đối với người tiếp nhận.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-18_khoan-3_diem-a

full chunk text

### 142-2026-ND-CP_dieu-18_khoan-3_diem-a

```text
Rõ ràng, dễ hiểu và dễ nhận biết đối với người tiếp nhận;
```

REQUIRED POINT P2

description: Thông báo hoặc nhãn phải được thực hiện trước hoặc tại thời điểm người tiếp nhận tiếp cận nội dung.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-18_khoan-3_diem-b

full chunk text

### 142-2026-ND-CP_dieu-18_khoan-3_diem-b

```text
Được thực hiện trước hoặc tại thời điểm người tiếp nhận tiếp cận nội dung;
```

REQUIRED POINT P3

description: Thông báo hoặc nhãn không được che giấu hoặc làm giảm khả năng nhận biết bản chất nội dung.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-18_khoan-3_diem-c

full chunk text

### 142-2026-ND-CP_dieu-18_khoan-3_diem-c

```text
Không được thiết kế theo cách che giấu hoặc làm giảm khả năng nhận biết bản chất của nội dung;
```

REQUIRED POINT P4

description: Thông báo hoặc nhãn phải phù hợp với loại hình và phương thức cung cấp nội dung.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-18_khoan-3_diem-d

full chunk text

### 142-2026-ND-CP_dieu-18_khoan-3_diem-d

```text
Phù hợp với loại hình nội dung và phương thức cung cấp nội dung;
```

REQUIRED POINT P5

description: Thông báo hoặc nhãn không được gây cản trở đáng kể việc hiển thị, trình diễn hoặc sử dụng nội dung.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-18_khoan-3_diem-đ

full chunk text

### 142-2026-ND-CP_dieu-18_khoan-3_diem-đ

```text
Không gây cản trở đáng kể việc hiển thị, trình diễn hoặc sử dụng nội dung.
```

REQUIRED POINT P6

description: Có thể hiển thị trực tiếp trên nội dung, tại tiêu đề/mô tả/chú thích, trên giao diện nền tảng, hoặc thông báo bằng âm thanh hay hình thức phù hợp khác.
importance: important
supporting chunks: 142-2026-ND-CP_dieu-18_khoan-5_diem-a, 142-2026-ND-CP_dieu-18_khoan-5_diem-b, 142-2026-ND-CP_dieu-18_khoan-5_diem-c, 142-2026-ND-CP_dieu-18_khoan-5_diem-d

full chunk text

### 142-2026-ND-CP_dieu-18_khoan-5_diem-a

```text
Hiển thị trực tiếp trên nội dung;
```

### 142-2026-ND-CP_dieu-18_khoan-5_diem-b

```text
Hiển thị tại tiêu đề, phần mô tả hoặc chú thích kèm theo nội dung;
```

### 142-2026-ND-CP_dieu-18_khoan-5_diem-c

```text
Hiển thị trên giao diện của nền tảng cung cấp nội dung;
```

### 142-2026-ND-CP_dieu-18_khoan-5_diem-d

```text
Phát thông báo bằng âm thanh hoặc hình thức phù hợp khác.
```

REFERENCE ANSWER

Nhãn phải rõ ràng, dễ hiểu, dễ nhận biết, xuất hiện trước hoặc khi tiếp cận nội dung, không che giấu bản chất, phù hợp loại hình/cách cung cấp và không cản trở đáng kể việc sử dụng. Có thể hiển thị trực tiếp, ở tiêu đề/mô tả/chú thích, trên giao diện nền tảng hoặc bằng âm thanh/hình thức phù hợp khác.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval008

QUERY

Trường hợp nào nội dung do AI tạo ra cần giúp người tiếp nhận nhận biết rõ nguồn gốc?

REQUIRED POINT P1

description: Bên triển khai phải thông báo rõ ràng khi đưa ra công cộng nội dung AI tạo hoặc chỉnh sửa có khả năng gây nhầm lẫn về tính xác thực của sự kiện, nhân vật hoặc nguồn gốc.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-18_khoan-1

full chunk text

### 142-2026-ND-CP_dieu-18_khoan-1

```text
Bên triển khai phải thông báo rõ ràng khi cung cấp ra công cộng nội dung do hệ thống trí tuệ nhân tạo tạo ra hoặc chỉnh sửa có khả năng gây nhầm lẫn về tính xác thực của sự kiện, nhân vật hoặc nguồn gốc nội dung theo quy định tại khoản 3 Điều 11 của Luật Trí tuệ nhân tạo.
```

REQUIRED POINT P2

description: Phạm vi đáng chú ý gồm nội dung mô phỏng/giả lập ngoại hình, giọng nói người thật hoặc tái hiện sự kiện thực tế; trường hợp tái hiện sự kiện có ngoại lệ khi pháp luật quy định khác.
importance: important
supporting chunks: 142-2026-ND-CP_dieu-18_khoan-2_diem-a, 142-2026-ND-CP_dieu-18_khoan-2_diem-b

full chunk text

### 142-2026-ND-CP_dieu-18_khoan-2_diem-a

```text
Mô phỏng hoặc giả lập ngoại hình, giọng nói của người thật;
```

### 142-2026-ND-CP_dieu-18_khoan-2_diem-b

```text
Tái hiện sự kiện thực tế để phân biệt với nội dung thật, trừ trường hợp pháp luật có quy định khác.
```

REQUIRED POINT P3

description: Đối với điện ảnh, chương trình nghệ thuật hoặc nội dung sáng tạo, bên triển khai trực tiếp đưa nội dung ra công cộng thực hiện thông báo/gắn nhãn theo đặc thù nhưng vẫn phải bảo đảm người tiếp nhận nhận biết rõ nguồn gốc AI.
importance: important
supporting chunks: 142-2026-ND-CP_dieu-18_khoan-6

full chunk text

### 142-2026-ND-CP_dieu-18_khoan-6

```text
Đối với tác phẩm điện ảnh, chương trình nghệ thuật hoặc nội dung sáng tạo, việc thông báo và gắn nhãn hiển thị do bên triển khai trực tiếp đưa nội dung ra công cộng thực hiện và có thể được thực hiện tại phần mở đầu, phần kết thúc, phần danh đề, phần mô tả hoặc tài liệu kèm theo tác phẩm, phù hợp với đặc thù của từng loại hình. Việc thông báo và gắn nhãn phải bảo đảm người tiếp nhận có thể nhận biết rõ ràng nội dung được tạo ra hoặc được chỉnh sửa bằng hệ thống trí tuệ nhân tạo, không gây nhầm lẫn về nguồn gốc của nội dung. Trường hợp nội dung do hệ thống trí tuệ nhân tạo tạo ra hoặc chỉnh sửa trong quá trình sản xuất, bên thực hiện việc tạo ra hoặc chỉnh sửa nội dung có trách nhiệm cung cấp thông tin cần thiết để thực hiện nghĩa vụ quy định tại khoản này; bên trực tiếp đưa nội dung ra công cộng thực hiện nghĩa vụ trên cơ sở thông tin được cung cấp.
```

REFERENCE ANSWER

Phải thông báo rõ khi đưa ra công cộng nội dung AI tạo/sửa có thể gây nhầm lẫn về tính xác thực của sự kiện, nhân vật hoặc nguồn gốc, như mô phỏng người thật hoặc tái hiện sự kiện thực tế (trừ trường hợp pháp luật quy định khác). Với nội dung sáng tạo, bên đưa ra công cộng thực hiện theo đặc thù để người nhận biết rõ nguồn gốc.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval009

QUERY

Hệ thống AI tương tác trực tiếp với con người phải được thiết kế theo yêu cầu gì?

REQUIRED POINT P1

description: Người dùng nhận biết tương tác AI, trừ trường hợp pháp luật quy định khác.
importance: required
supporting chunks: 134-2025-QH15_dieu-11_khoan-1

full chunk text

### 134-2025-QH15_dieu-11_khoan-1

```text
Nhà cung cấp bảo đảm hệ thống trí tuệ nhân tạo tương tác trực tiếp với con người được thiết kế và vận hành để người sử dụng nhận biết khi đang tương tác với hệ thống, trừ trường hợp pháp luật có quy định khác.
```

REFERENCE ANSWER

Phải được thiết kế và vận hành để người dùng nhận biết đang tương tác với AI, trừ trường hợp pháp luật quy định khác.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval010

QUERY

Nhà cung cấp cần làm gì khi phát hiện sự cố liên quan đến hệ thống trí tuệ nhân tạo?

REQUIRED POINT P1

description: Khẩn trương áp dụng biện pháp kỹ thuật để khắc phục, tạm dừng hoặc thu hồi hệ thống.
importance: required
supporting chunks: 134-2025-QH15_dieu-12_khoan-2_diem-a

full chunk text

### 134-2025-QH15_dieu-12_khoan-2_diem-a

```text
Nhà phát triển, nhà cung cấp phải khẩn trương áp dụng biện pháp kỹ thuật để khắc phục, tạm dừng hoặc thu hồi hệ thống, đồng thời thông báo cho cơ quan có thẩm quyền;
```

REQUIRED POINT P2

description: Đồng thời thông báo sự cố cho cơ quan có thẩm quyền.
importance: required
supporting chunks: 134-2025-QH15_dieu-12_khoan-2_diem-a

full chunk text

### 134-2025-QH15_dieu-12_khoan-2_diem-a

```text
Nhà phát triển, nhà cung cấp phải khẩn trương áp dụng biện pháp kỹ thuật để khắc phục, tạm dừng hoặc thu hồi hệ thống, đồng thời thông báo cho cơ quan có thẩm quyền;
```

REFERENCE ANSWER

Khẩn trương áp dụng biện pháp kỹ thuật để khắc phục, tạm dừng hoặc thu hồi hệ thống, đồng thời thông báo cơ quan có thẩm quyền.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval011

QUERY

Cơ chế thử nghiệm có kiểm soát cho phép tổ chức, cá nhân được hưởng những cơ chế gì trong phạm vi thử nghiệm?

REQUIRED POINT P1

description: Có thể được công nhận kết quả đánh giá sự phù hợp trong phạm vi thử nghiệm.
importance: required
supporting chunks: 134-2025-QH15_dieu-21_khoan-2_diem-a

full chunk text

### 134-2025-QH15_dieu-21_khoan-2_diem-a

```text
Công nhận kết quả đánh giá sự phù hợp theo quy định của Luật này;
```

REQUIRED POINT P2

description: Có thể được miễn, giảm hoặc điều chỉnh nghĩa vụ tuân thủ tương ứng trong phạm vi thử nghiệm.
importance: required
supporting chunks: 134-2025-QH15_dieu-21_khoan-2_diem-b

full chunk text

### 134-2025-QH15_dieu-21_khoan-2_diem-b

```text
Miễn, giảm hoặc điều chỉnh nghĩa vụ tuân thủ tương ứng của Luật này.
```

REFERENCE ANSWER

Có thể được công nhận kết quả đánh giá sự phù hợp và miễn, giảm hoặc điều chỉnh nghĩa vụ tuân thủ tương ứng.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval012

QUERY

Cơ quan nào quyết định chấp thuận tham gia cơ chế thử nghiệm có kiểm soát?

REQUIRED POINT P1

description: Ủy ban nhân dân cấp tỉnh quyết định đối với hệ thống cấp độ 1 hoặc 2 triển khai trong phạm vi một tỉnh.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-23_khoan-3_diem-a

full chunk text

### 142-2026-ND-CP_dieu-23_khoan-3_diem-a

```text
Ủy ban nhân dân cấp tỉnh có thẩm quyền tiếp nhận, thẩm định và ban hành giấy xác nhận đối với hệ thống trí tuệ nhân tạo cấp độ 1 hoặc cấp độ 2 được triển khai trong phạm vi một tỉnh, thành phố trực thuộc trung ương;
```

REQUIRED POINT P2

description: Bộ hoặc cơ quan ngang bộ quyết định đối với hệ thống cấp độ 1 hoặc 2 thuộc phạm vi quản lý nhà nước và triển khai từ hai tỉnh trở lên, hoặc do đơn vị thuộc phạm vi quản lý trực tiếp triển khai.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-23_khoan-3_diem-b

full chunk text

### 142-2026-ND-CP_dieu-23_khoan-3_diem-b

```text
Bộ, cơ quan ngang bộ chỉ có thẩm quyền tiếp nhận, thẩm định và ban hành giấy xác nhận đối với hệ thống trí tuệ nhân tạo cấp độ 1 hoặc cấp độ 2 khi hệ thống đó thuộc phạm vi quản lý nhà nước của bộ, cơ quan ngang bộ và được triển khai trên phạm vi từ hai tỉnh, thành phố trực thuộc trung ương trở lên; hoặc do cơ quan, tổ chức thuộc phạm vi quản lý trực tiếp của bộ, cơ quan ngang bộ triển khai;
```

REQUIRED POINT P3

description: Bộ Công an quyết định đối với hệ thống AI cấp độ 3.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-23_khoan-3_diem-c

full chunk text

### 142-2026-ND-CP_dieu-23_khoan-3_diem-c

```text
Bộ Công an có thẩm quyền tiếp nhận, thẩm định và ban hành giấy xác nhận đối với hệ thống trí tuệ nhân tạo cấp độ 3. Trường hợp hệ thống trí tuệ nhân tạo thuộc phạm vi quản lý của nhiều bộ, cơ quan ngang bộ, bộ, cơ quan ngang bộ quản lý ngành, lĩnh vực có phạm vi quản lý trực tiếp đối với hoạt động sử dụng chính của hệ thống có thẩm quyền tiếp nhận, thẩm định và ban hành giấy xác nhận.
```

REQUIRED POINT P4

description: Nếu hệ thống thuộc phạm vi quản lý của nhiều bộ, bộ quản lý ngành/lĩnh vực có phạm vi quản lý trực tiếp đối với hoạt động sử dụng chính có thẩm quyền.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-23_khoan-3_diem-c

full chunk text

### 142-2026-ND-CP_dieu-23_khoan-3_diem-c

```text
Bộ Công an có thẩm quyền tiếp nhận, thẩm định và ban hành giấy xác nhận đối với hệ thống trí tuệ nhân tạo cấp độ 3. Trường hợp hệ thống trí tuệ nhân tạo thuộc phạm vi quản lý của nhiều bộ, cơ quan ngang bộ, bộ, cơ quan ngang bộ quản lý ngành, lĩnh vực có phạm vi quản lý trực tiếp đối với hoạt động sử dụng chính của hệ thống có thẩm quyền tiếp nhận, thẩm định và ban hành giấy xác nhận.
```

REFERENCE ANSWER

UBND cấp tỉnh xử lý cấp 1/2 trong một tỉnh; bộ/cơ quan ngang bộ xử lý cấp 1/2 thuộc phạm vi quản lý trong trường hợp liên tỉnh hoặc đơn vị trực thuộc; Bộ Công an xử lý cấp 3. Nếu nhiều bộ cùng quản lý, bộ quản lý trực tiếp hoạt động sử dụng chính có thẩm quyền.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval013

QUERY

Việc phân loại cấp độ thử nghiệm có kiểm soát dựa trên những tiêu chí nào?

REQUIRED POINT P1

description: Mức độ rủi ro của hệ thống AI.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-22_khoan-1_diem-a

full chunk text

### 142-2026-ND-CP_dieu-22_khoan-1_diem-a

```text
Mức độ rủi ro của hệ thống trí tuệ nhân tạo theo quy định của Luật Trí tuệ nhân tạo;
```

REQUIRED POINT P2

description: Tính chất của dữ liệu được sử dụng.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-22_khoan-1_diem-b

full chunk text

### 142-2026-ND-CP_dieu-22_khoan-1_diem-b

```text
Tính chất của dữ liệu được sử dụng, bao gồm dữ liệu cá nhân, dữ liệu cá nhân nhạy cảm, dữ liệu cá nhân của trẻ em hoặc dữ liệu thuộc danh mục hạn chế theo quy định của pháp luật về dữ liệu và bảo vệ dữ liệu cá nhân;
```

REQUIRED POINT P3

description: Phạm vi và quy mô triển khai thử nghiệm.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-22_khoan-1_diem-c

full chunk text

### 142-2026-ND-CP_dieu-22_khoan-1_diem-c

```text
Phạm vi và quy mô triển khai thử nghiệm, bao gồm địa bàn triển khai, số lượng điểm thử nghiệm, đối tượng tham gia thử nghiệm và mức độ kết nối với hệ thống dữ liệu hoặc hệ thống thông tin;
```

REQUIRED POINT P4

description: Mức độ tác động đối với an ninh, trật tự, an toàn xã hội và quyền, lợi ích hợp pháp.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-22_khoan-1_diem-d

full chunk text

### 142-2026-ND-CP_dieu-22_khoan-1_diem-d

```text
Mức độ tác động đối với an ninh quốc gia, trật tự, an toàn xã hội và quyền, lợi ích hợp pháp của tổ chức, cá nhân.
```

REQUIRED POINT P5

description: Nếu đáp ứng nhiều cấp độ thì phân loại theo cấp cao nhất, xét chức năng, mục đích sử dụng và tác động tổng thể, kể cả hệ thống nhiều thành phần.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-22_khoan-2

full chunk text

### 142-2026-ND-CP_dieu-22_khoan-2

```text
Trường hợp hệ thống trí tuệ nhân tạo đồng thời đáp ứng tiêu chí của nhiều cấp độ thử nghiệm khác nhau thì hệ thống được phân loại theo cấp độ thử nghiệm cao nhất. Việc phân loại cấp độ thử nghiệm được xác định trên cơ sở chức năng, mục đích sử dụng và tác động tổng thể của hệ thống trí tuệ nhân tạo, bao gồm cả trường hợp hệ thống được triển khai thông qua nhiều thành phần, mô-đun hoặc dịch vụ kết hợp với nhau.
```

REFERENCE ANSWER

Dựa trên mức rủi ro, tính chất dữ liệu, phạm vi/quy mô thử nghiệm và mức tác động. Nếu đáp ứng nhiều cấp độ thì xếp cấp cao nhất, xét chức năng, mục đích sử dụng và tác động tổng thể, kể cả hệ thống nhiều thành phần.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval014

QUERY

Hồ sơ thông thường để tham gia cơ chế thử nghiệm có kiểm soát gồm những thành phần nào?

REQUIRED POINT P1

description: Đơn đề nghị tham gia cơ chế thử nghiệm theo mẫu tương ứng với tổ chức hoặc cá nhân.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-24_khoan-2_diem-a

full chunk text

### 142-2026-ND-CP_dieu-24_khoan-2_diem-a

```text
Đơn đề nghị tham gia cơ chế thử nghiệm có kiểm soát theo Mẫu AI03a đối với tổ chức hoặc Mẫu AI03b đối với cá nhân tại Phụ lục ban hành kèm theo Nghị định này;
```

REQUIRED POINT P2

description: Đề án thử nghiệm mô tả hệ thống, mục tiêu, phạm vi, thời gian và phương án quản lý rủi ro.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-24_khoan-2_diem-b

full chunk text

### 142-2026-ND-CP_dieu-24_khoan-2_diem-b

```text
Đề án thử nghiệm, trong đó mô tả hệ thống trí tuệ nhân tạo dự kiến thử nghiệm, mục tiêu, phạm vi, thời gian thử nghiệm và phương án quản lý rủi ro;
```

REQUIRED POINT P3

description: Tài liệu mô tả biện pháp bảo vệ quyền và lợi ích hợp pháp của tổ chức, cá nhân chịu tác động.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-24_khoan-2_diem-c

full chunk text

### 142-2026-ND-CP_dieu-24_khoan-2_diem-c

```text
Tài liệu mô tả biện pháp bảo vệ quyền và lợi ích hợp pháp của tổ chức, cá nhân chịu tác động trong quá trình thử nghiệm;
```

REQUIRED POINT P4

description: Tài liệu mô tả năng lực kỹ thuật, nhân sự hoặc hạ tầng liên quan trực tiếp đến phạm vi thử nghiệm.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-24_khoan-2_diem-d

full chunk text

### 142-2026-ND-CP_dieu-24_khoan-2_diem-d

```text
Tài liệu mô tả năng lực kỹ thuật, nhân sự hoặc hạ tầng phục vụ triển khai thử nghiệm có liên quan trực tiếp đến phạm vi thử nghiệm đề xuất.
```

REFERENCE ANSWER

Gồm đơn đề nghị theo mẫu; đề án nêu hệ thống, mục tiêu, phạm vi, thời gian, quản lý rủi ro; tài liệu bảo vệ quyền/lợi ích người chịu tác động; và tài liệu về năng lực kỹ thuật, nhân sự hoặc hạ tầng liên quan trực tiếp.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval015

QUERY

Khi nào cơ quan có thẩm quyền có thể tạm dừng hoặc chấm dứt thử nghiệm?

REQUIRED POINT P1

description: Có rủi ro ảnh hưởng đến an toàn, an ninh hoặc quyền, lợi ích hợp pháp của tổ chức, cá nhân.
importance: required
supporting chunks: 134-2025-QH15_dieu-21_khoan-3

full chunk text

### 134-2025-QH15_dieu-21_khoan-3

```text
Cơ quan nhà nước có thẩm quyền chủ trì, phối hợp với cơ quan có liên quan tiếp nhận, thẩm định và xử lý hồ sơ theo quy trình thẩm định và phản hồi nhanh; giám sát quá trình thử nghiệm và quyết định tạm dừng hoặc chấm dứt thử nghiệm khi có rủi ro ảnh hưởng đến an toàn, an ninh hoặc quyền, lợi ích hợp pháp của tổ chức, cá nhân.
```

REQUIRED POINT P2

description: Tổ chức, cá nhân vi phạm giới hạn thử nghiệm hoặc không khắc phục sự cố theo yêu cầu của cơ quan có thẩm quyền.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-25_khoan-1_diem-c

full chunk text

### 142-2026-ND-CP_dieu-25_khoan-1_diem-c

```text
Quyết định tạm dừng thử nghiệm, chấm dứt thử nghiệm hoặc hiệu lực giấy xác nhận tham gia cơ chế thử nghiệm có kiểm soát khi tổ chức, cá nhân vi phạm các giới hạn thử nghiệm hoặc không khắc phục sự cố theo yêu cầu của cơ quan nhà nước có thẩm quyền.
```

REFERENCE ANSWER

Khi có rủi ro ảnh hưởng an toàn, an ninh hoặc quyền, lợi ích hợp pháp; hoặc tổ chức/cá nhân vi phạm giới hạn thử nghiệm hay không khắc phục sự cố theo yêu cầu.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval016

QUERY

Tổ chức hoặc cá nhân phải báo cáo gì trong quá trình thử nghiệm có kiểm soát?

REQUIRED POINT P1

description: Thử nghiệm cấp độ 1 hoặc 2 phải báo cáo định kỳ 06 tháng một lần.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-25_khoan-2_diem-a

full chunk text

### 142-2026-ND-CP_dieu-25_khoan-2_diem-a

```text
Cấp độ 1,2: 06 tháng một lần;
```

REQUIRED POINT P2

description: Thử nghiệm cấp độ 3 phải báo cáo định kỳ 03 tháng một lần.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-25_khoan-2_diem-b

full chunk text

### 142-2026-ND-CP_dieu-25_khoan-2_diem-b

```text
Cấp độ 3: 03 tháng một lần.
```

REQUIRED POINT P3

description: Phải báo cáo khi hệ thống xảy ra sự cố nghiêm trọng hoặc vượt giới hạn thử nghiệm đã xác định.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-25_khoan-3_diem-a, 142-2026-ND-CP_dieu-25_khoan-3_diem-b

full chunk text

### 142-2026-ND-CP_dieu-25_khoan-3_diem-a

```text
Hệ thống trí tuệ nhân tạo xảy ra sự cố nghiêm trọng theo khoản 8 Điều 3 Luật Trí tuệ nhân tạo;
```

### 142-2026-ND-CP_dieu-25_khoan-3_diem-b

```text
Hệ thống trí tuệ nhân tạo vượt giới hạn thử nghiệm đã được xác định trong giấy xác nhận. Báo cáo sự cố được thực hiện theo Mẫu AI06a đối với tổ chức hoặc Mẫu AI06b đối với cá nhân; báo cáo vượt giới hạn thử nghiệm được thực hiện theo Mẫu AI07a đối với tổ chức hoặc Mẫu AI07b đối với cá nhân tại Phụ lục ban hành kèm theo Nghị định này.
```

REQUIRED POINT P4

description: Phải nộp báo cáo tổng kết chậm nhất 15 ngày trước khi kết thúc thời hạn thử nghiệm.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-25_khoan-4

full chunk text

### 142-2026-ND-CP_dieu-25_khoan-4

```text
Chậm nhất 15 ngày trước khi kết thúc thời hạn thử nghiệm, tổ chức, cá nhân tham gia thử nghiệm phải nộp báo cáo tổng kết kết quả thử nghiệm thông qua cổng thông tin điện tử một cửa về trí tuệ nhân tạo theo Mẫu AI08a đối với tổ chức hoặc Mẫu AI08b đối với cá nhân tại Phụ lục ban hành kèm theo Nghị định này.
```

REFERENCE ANSWER

Báo cáo định kỳ: cấp 1/2 mỗi 6 tháng, cấp 3 mỗi 3 tháng; báo cáo sự cố nghiêm trọng hoặc vượt giới hạn; và nộp báo cáo tổng kết chậm nhất 15 ngày trước khi hết hạn.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval017

QUERY

Có thể gia hạn thời gian thử nghiệm có kiểm soát hay không và thủ tục thế nào?

REQUIRED POINT P1

description: Được đề nghị gia hạn bằng đơn gia hạn và báo cáo tổng kết nộp chậm nhất 15 ngày làm việc trước khi hết hạn.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-27_khoan-1

full chunk text

### 142-2026-ND-CP_dieu-27_khoan-1

```text
Trong thời hạn 15 ngày làm việc kể từ ngày nhận được báo cáo tổng kết theo quy định tại Nghị định này, cơ quan đã ban hành giấy xác nhận tham gia cơ chế thử nghiệm có kiểm soát tổ chức đánh giá kết quả thử nghiệm và cấp Giấy xác nhận hoàn thành thử nghiệm có kiểm soát theo Mẫu AI04 tại Phụ lục ban hành kèm theo Nghị định này. Trường hợp từ chối cấp Giấy xác nhận, cơ quan có thẩm quyền phải trả lời bằng văn bản và nêu rõ lý do. Trường hợp có nhu cầu gia hạn thời gian thử nghiệm, chậm nhất 15 ngày làm việc trước khi kết thúc thời hạn, tổ chức, cá nhân nộp Đơn đề nghị gia hạn theo mẫu tại Phụ lục AI03c hoặc AI03d và Báo cáo tổng kết quá trình thử nghiệm theo mẫu tại Phụ lục AI08a hoặc AI08b. Trong thời hạn 10 ngày làm việc, cơ quan có thẩm quyền thẩm định, quyết định gia hạn và cấp gia hạn Giấy xác nhận tham gia thử nghiệm; trường hợp không chấp thuận hoặc không gia hạn Giấy xác nhận tham gia thử nghiệm phải có văn bản trả lời và nêu rõ lý do.
```

REQUIRED POINT P2

description: Cơ quan có thẩm quyền thẩm định, quyết định và cấp gia hạn trong 10 ngày làm việc.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-27_khoan-1

full chunk text

### 142-2026-ND-CP_dieu-27_khoan-1

```text
Trong thời hạn 15 ngày làm việc kể từ ngày nhận được báo cáo tổng kết theo quy định tại Nghị định này, cơ quan đã ban hành giấy xác nhận tham gia cơ chế thử nghiệm có kiểm soát tổ chức đánh giá kết quả thử nghiệm và cấp Giấy xác nhận hoàn thành thử nghiệm có kiểm soát theo Mẫu AI04 tại Phụ lục ban hành kèm theo Nghị định này. Trường hợp từ chối cấp Giấy xác nhận, cơ quan có thẩm quyền phải trả lời bằng văn bản và nêu rõ lý do. Trường hợp có nhu cầu gia hạn thời gian thử nghiệm, chậm nhất 15 ngày làm việc trước khi kết thúc thời hạn, tổ chức, cá nhân nộp Đơn đề nghị gia hạn theo mẫu tại Phụ lục AI03c hoặc AI03d và Báo cáo tổng kết quá trình thử nghiệm theo mẫu tại Phụ lục AI08a hoặc AI08b. Trong thời hạn 10 ngày làm việc, cơ quan có thẩm quyền thẩm định, quyết định gia hạn và cấp gia hạn Giấy xác nhận tham gia thử nghiệm; trường hợp không chấp thuận hoặc không gia hạn Giấy xác nhận tham gia thử nghiệm phải có văn bản trả lời và nêu rõ lý do.
```

REQUIRED POINT P3

description: Nếu không chấp thuận hoặc không gia hạn thì phải trả lời bằng văn bản và nêu rõ lý do.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-27_khoan-1

full chunk text

### 142-2026-ND-CP_dieu-27_khoan-1

```text
Trong thời hạn 15 ngày làm việc kể từ ngày nhận được báo cáo tổng kết theo quy định tại Nghị định này, cơ quan đã ban hành giấy xác nhận tham gia cơ chế thử nghiệm có kiểm soát tổ chức đánh giá kết quả thử nghiệm và cấp Giấy xác nhận hoàn thành thử nghiệm có kiểm soát theo Mẫu AI04 tại Phụ lục ban hành kèm theo Nghị định này. Trường hợp từ chối cấp Giấy xác nhận, cơ quan có thẩm quyền phải trả lời bằng văn bản và nêu rõ lý do. Trường hợp có nhu cầu gia hạn thời gian thử nghiệm, chậm nhất 15 ngày làm việc trước khi kết thúc thời hạn, tổ chức, cá nhân nộp Đơn đề nghị gia hạn theo mẫu tại Phụ lục AI03c hoặc AI03d và Báo cáo tổng kết quá trình thử nghiệm theo mẫu tại Phụ lục AI08a hoặc AI08b. Trong thời hạn 10 ngày làm việc, cơ quan có thẩm quyền thẩm định, quyết định gia hạn và cấp gia hạn Giấy xác nhận tham gia thử nghiệm; trường hợp không chấp thuận hoặc không gia hạn Giấy xác nhận tham gia thử nghiệm phải có văn bản trả lời và nêu rõ lý do.
```

REFERENCE ANSWER

Có. Nộp đơn gia hạn và báo cáo tổng kết chậm nhất 15 ngày làm việc trước khi hết hạn. Trong 10 ngày làm việc, cơ quan có thẩm quyền thẩm định, quyết định và cấp gia hạn; nếu không chấp thuận phải trả lời bằng văn bản, nêu rõ lý do.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval018

QUERY

Sau khi kết thúc thử nghiệm, cơ quan có thẩm quyền xử lý kết quả như thế nào?

REQUIRED POINT P1

description: Trong 15 ngày làm việc từ khi nhận báo cáo tổng kết, cơ quan có thẩm quyền đánh giá và cấp giấy xác nhận hoàn thành.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-27_khoan-1

full chunk text

### 142-2026-ND-CP_dieu-27_khoan-1

```text
Trong thời hạn 15 ngày làm việc kể từ ngày nhận được báo cáo tổng kết theo quy định tại Nghị định này, cơ quan đã ban hành giấy xác nhận tham gia cơ chế thử nghiệm có kiểm soát tổ chức đánh giá kết quả thử nghiệm và cấp Giấy xác nhận hoàn thành thử nghiệm có kiểm soát theo Mẫu AI04 tại Phụ lục ban hành kèm theo Nghị định này. Trường hợp từ chối cấp Giấy xác nhận, cơ quan có thẩm quyền phải trả lời bằng văn bản và nêu rõ lý do. Trường hợp có nhu cầu gia hạn thời gian thử nghiệm, chậm nhất 15 ngày làm việc trước khi kết thúc thời hạn, tổ chức, cá nhân nộp Đơn đề nghị gia hạn theo mẫu tại Phụ lục AI03c hoặc AI03d và Báo cáo tổng kết quá trình thử nghiệm theo mẫu tại Phụ lục AI08a hoặc AI08b. Trong thời hạn 10 ngày làm việc, cơ quan có thẩm quyền thẩm định, quyết định gia hạn và cấp gia hạn Giấy xác nhận tham gia thử nghiệm; trường hợp không chấp thuận hoặc không gia hạn Giấy xác nhận tham gia thử nghiệm phải có văn bản trả lời và nêu rõ lý do.
```

REQUIRED POINT P2

description: Nếu từ chối cấp giấy xác nhận hoàn thành thì phải nêu rõ lý do.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-27_khoan-1

full chunk text

### 142-2026-ND-CP_dieu-27_khoan-1

```text
Trong thời hạn 15 ngày làm việc kể từ ngày nhận được báo cáo tổng kết theo quy định tại Nghị định này, cơ quan đã ban hành giấy xác nhận tham gia cơ chế thử nghiệm có kiểm soát tổ chức đánh giá kết quả thử nghiệm và cấp Giấy xác nhận hoàn thành thử nghiệm có kiểm soát theo Mẫu AI04 tại Phụ lục ban hành kèm theo Nghị định này. Trường hợp từ chối cấp Giấy xác nhận, cơ quan có thẩm quyền phải trả lời bằng văn bản và nêu rõ lý do. Trường hợp có nhu cầu gia hạn thời gian thử nghiệm, chậm nhất 15 ngày làm việc trước khi kết thúc thời hạn, tổ chức, cá nhân nộp Đơn đề nghị gia hạn theo mẫu tại Phụ lục AI03c hoặc AI03d và Báo cáo tổng kết quá trình thử nghiệm theo mẫu tại Phụ lục AI08a hoặc AI08b. Trong thời hạn 10 ngày làm việc, cơ quan có thẩm quyền thẩm định, quyết định gia hạn và cấp gia hạn Giấy xác nhận tham gia thử nghiệm; trường hợp không chấp thuận hoặc không gia hạn Giấy xác nhận tham gia thử nghiệm phải có văn bản trả lời và nêu rõ lý do.
```

REQUIRED POINT P3

description: Có thể công nhận toàn bộ hoặc một phần kết quả thử nghiệm để đánh giá sự phù hợp.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-27_khoan-2_diem-a

full chunk text

### 142-2026-ND-CP_dieu-27_khoan-2_diem-a

```text
Công nhận toàn bộ hoặc một phần kết quả thử nghiệm phục vụ đánh giá sự phù hợp đối với hệ thống trí tuệ nhân tạo;
```

REQUIRED POINT P4

description: Có thể miễn, giảm hoặc điều chỉnh nghĩa vụ tuân thủ trên cơ sở kết quả được công nhận.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-27_khoan-2_diem-b

full chunk text

### 142-2026-ND-CP_dieu-27_khoan-2_diem-b

```text
Áp dụng biện pháp miễn, giảm hoặc điều chỉnh nghĩa vụ tuân thủ.
```

REFERENCE ANSWER

Trong 15 ngày làm việc từ khi nhận báo cáo tổng kết, cơ quan đánh giá và cấp giấy xác nhận hoàn thành; từ chối phải nêu lý do. Có thể công nhận toàn bộ/một phần kết quả để đánh giá sự phù hợp và miễn, giảm hoặc điều chỉnh nghĩa vụ.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval019

QUERY

Cơ sở dữ liệu quốc gia phục vụ trí tuệ nhân tạo được tổ chức theo những nguyên tắc nào?

REQUIRED POINT P1

description: Cơ sở dữ liệu quốc gia về AI được tổ chức theo nguyên tắc mở.
importance: required
supporting chunks: 134-2025-QH15_dieu-17_khoan-2

full chunk text

### 134-2025-QH15_dieu-17_khoan-2

```text
Cơ sở dữ liệu quốc gia về trí tuệ nhân tạo do Nhà nước đầu tư, xây dựng và vận hành tại Trung tâm dữ liệu quốc gia; được tổ chức theo nguyên tắc mở, an toàn, có kiểm soát, đáp ứng yêu cầu về chất lượng, khả năng kết nối và khai thác; bao gồm dữ liệu mở, dữ liệu mở có điều kiện và dữ liệu thương mại theo quy định của pháp luật.
```

REQUIRED POINT P2

description: Cơ sở dữ liệu quốc gia về AI được tổ chức theo nguyên tắc an toàn.
importance: required
supporting chunks: 134-2025-QH15_dieu-17_khoan-2

full chunk text

### 134-2025-QH15_dieu-17_khoan-2

```text
Cơ sở dữ liệu quốc gia về trí tuệ nhân tạo do Nhà nước đầu tư, xây dựng và vận hành tại Trung tâm dữ liệu quốc gia; được tổ chức theo nguyên tắc mở, an toàn, có kiểm soát, đáp ứng yêu cầu về chất lượng, khả năng kết nối và khai thác; bao gồm dữ liệu mở, dữ liệu mở có điều kiện và dữ liệu thương mại theo quy định của pháp luật.
```

REQUIRED POINT P3

description: Cơ sở dữ liệu quốc gia về AI được tổ chức theo nguyên tắc có kiểm soát.
importance: required
supporting chunks: 134-2025-QH15_dieu-17_khoan-2

full chunk text

### 134-2025-QH15_dieu-17_khoan-2

```text
Cơ sở dữ liệu quốc gia về trí tuệ nhân tạo do Nhà nước đầu tư, xây dựng và vận hành tại Trung tâm dữ liệu quốc gia; được tổ chức theo nguyên tắc mở, an toàn, có kiểm soát, đáp ứng yêu cầu về chất lượng, khả năng kết nối và khai thác; bao gồm dữ liệu mở, dữ liệu mở có điều kiện và dữ liệu thương mại theo quy định của pháp luật.
```

REFERENCE ANSWER

Cơ sở dữ liệu quốc gia về AI được tổ chức theo các nguyên tắc mở, an toàn và có kiểm soát.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval020

QUERY

Dữ liệu mở có điều kiện được hiểu là gì?

REQUIRED POINT P1

description: Được truy cập/sử dụng khi đáp ứng điều kiện đăng ký, mục đích sử dụng và bảo mật.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-3_khoan-7

full chunk text

### 142-2026-ND-CP_dieu-3_khoan-7

```text
Dữ liệu mở có điều kiện là dữ liệu được phép truy cập, sử dụng khi cơ quan, tổ chức, cá nhân đáp ứng các điều kiện về đăng ký, mục đích sử dụng và yêu cầu bảo mật theo quy định của pháp luật.
```

REFERENCE ANSWER

Là dữ liệu được phép truy cập, sử dụng khi đáp ứng điều kiện về đăng ký, mục đích sử dụng và yêu cầu bảo mật theo pháp luật.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval021

QUERY

Những loại dữ liệu nào có thể được đưa vào cơ sở dữ liệu phục vụ trí tuệ nhân tạo?

REQUIRED POINT P1

description: Dữ liệu mở có thể được đưa vào cơ sở dữ liệu phục vụ AI.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-32_khoan-1_diem-a

full chunk text

### 142-2026-ND-CP_dieu-32_khoan-1_diem-a

```text
Dữ liệu mở;
```

REQUIRED POINT P2

description: Dữ liệu mở có điều kiện có thể được đưa vào cơ sở dữ liệu phục vụ AI.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-32_khoan-1_diem-b

full chunk text

### 142-2026-ND-CP_dieu-32_khoan-1_diem-b

```text
Dữ liệu mở có điều kiện;
```

REQUIRED POINT P3

description: Dữ liệu thương mại của tổ chức, doanh nghiệp theo pháp luật có thể được đưa vào cơ sở dữ liệu phục vụ AI.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-32_khoan-1_diem-c

full chunk text

### 142-2026-ND-CP_dieu-32_khoan-1_diem-c

```text
Dữ liệu thương mại của tổ chức, doanh nghiệp theo quy định của pháp luật.
```

REFERENCE ANSWER

Dữ liệu mở, dữ liệu mở có điều kiện và dữ liệu thương mại của tổ chức, doanh nghiệp theo quy định pháp luật.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval022

QUERY

Cơ quan quản lý có trách nhiệm gì đối với việc xây dựng và cập nhật dữ liệu mở phục vụ AI?

REQUIRED POINT P1

description: Trong phạm vi quản lý, cơ quan có trách nhiệm xây dựng và cập nhật dữ liệu mở phục vụ AI.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-32_khoan-5_diem-a

full chunk text

### 142-2026-ND-CP_dieu-32_khoan-5_diem-a

```text
Xây dựng, cập nhật dữ liệu mở, dữ liệu mở có điều kiện, dữ liệu thương mại thuộc phạm vi quản lý;
```

REQUIRED POINT P2

description: Cơ quan phải tổ chức thu thập, tạo lập, cập nhật, bảo đảm chất lượng, gán nhãn, chú thích và chuẩn hóa các bộ dữ liệu thiết yếu phục vụ phát triển AI.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-32_khoan-5_diem-b

full chunk text

### 142-2026-ND-CP_dieu-32_khoan-5_diem-b

```text
Tổ chức thu thập, tạo lập, cập nhật, bảo đảm chất lượng, gán nhãn, chú thích và chuẩn hóa đối với các bộ dữ liệu thuộc Danh mục bộ dữ liệu phục vụ phát triển trí tuệ nhân tạo trong các lĩnh vực thiết yếu;
```

REQUIRED POINT P3

description: Cơ quan phải thực hiện kết nối thống nhất, chia sẻ và khai thác Cơ sở dữ liệu quốc gia về AI theo pháp luật.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-32_khoan-5_diem-c

full chunk text

### 142-2026-ND-CP_dieu-32_khoan-5_diem-c

```text
Thực hiện kết nối thống nhất, chia sẻ dữ liệu và khai thác Cơ sở dữ liệu quốc gia về trí tuệ nhân tạo theo quy định của pháp luật.
```

REFERENCE ANSWER

Đối với dữ liệu mở phục vụ AI, cơ quan quản lý phải xây dựng, cập nhật dữ liệu trong phạm vi quản lý; tổ chức thu thập, tạo lập, cập nhật, bảo đảm chất lượng, gán nhãn, chú thích và chuẩn hóa các bộ dữ liệu thiết yếu; đồng thời kết nối thống nhất, chia sẻ và khai thác Cơ sở dữ liệu quốc gia về AI theo pháp luật.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval023

QUERY

Quy định về bảo đảm khả năng kết nối và khai thác dữ liệu phục vụ trí tuệ nhân tạo là gì?

REQUIRED POINT P1

description: Cơ sở dữ liệu quốc gia về AI phải bảo đảm chất lượng, khả năng kết nối và khai thác.
importance: required
supporting chunks: 134-2025-QH15_dieu-17_khoan-2

full chunk text

### 134-2025-QH15_dieu-17_khoan-2

```text
Cơ sở dữ liệu quốc gia về trí tuệ nhân tạo do Nhà nước đầu tư, xây dựng và vận hành tại Trung tâm dữ liệu quốc gia; được tổ chức theo nguyên tắc mở, an toàn, có kiểm soát, đáp ứng yêu cầu về chất lượng, khả năng kết nối và khai thác; bao gồm dữ liệu mở, dữ liệu mở có điều kiện và dữ liệu thương mại theo quy định của pháp luật.
```

REQUIRED POINT P2

description: Cơ sở dữ liệu của các bộ, cơ quan và địa phương phải được xây dựng, cập nhật, kết nối thống nhất với cơ sở dữ liệu quốc gia, bảo đảm tiêu chuẩn, chất lượng dữ liệu và an toàn thông tin.
importance: required
supporting chunks: 134-2025-QH15_dieu-17_khoan-3

full chunk text

### 134-2025-QH15_dieu-17_khoan-3

```text
Cơ sở dữ liệu phục vụ trí tuệ nhân tạo của Bộ, cơ quan ngang Bộ, cơ quan thuộc Chính phủ và Ủy ban nhân dân các cấp được xây dựng, cập nhật và kết nối thống nhất với Cơ sở dữ liệu quốc gia về trí tuệ nhân tạo; bảo đảm tiêu chuẩn, quy chuẩn kỹ thuật, chất lượng dữ liệu và an toàn thông tin.
```

REFERENCE ANSWER

CSDL quốc gia phải đáp ứng chất lượng, kết nối và khai thác. CSDL của các cơ quan phải được xây dựng, cập nhật, kết nối thống nhất với CSDL quốc gia, bảo đảm tiêu chuẩn, chất lượng dữ liệu và an toàn thông tin.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval024

QUERY

Những hành vi nào liên quan đến AI bị nghiêm cấm khi lợi dụng nhóm người dễ bị tổn thương?

REQUIRED POINT P1

description: Lợi dụng điểm yếu nhóm dễ bị tổn thương để gây tổn hại cho họ hoặc người khác.
importance: required
supporting chunks: 134-2025-QH15_dieu-7_khoan-2_diem-c

full chunk text

### 134-2025-QH15_dieu-7_khoan-2_diem-c

```text
Lợi dụng điểm yếu của nhóm người dễ bị tổn thương, bao gồm trẻ em, người cao tuổi, người khuyết tật, người dân tộc thiểu số hoặc người mất năng lực hành vi dân sự, người bị hạn chế năng lực hành vi dân sự, người có khó khăn trong nhận thức, làm chủ hành vi để gây tổn hại cho chính họ hoặc người khác;
```

REFERENCE ANSWER

Nghiêm cấm lợi dụng điểm yếu của nhóm dễ bị tổn thương, gồm các nhóm được điều khoản liệt kê, để gây tổn hại cho chính họ hoặc người khác.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval025

QUERY

Khi ứng dụng AI trong quản lý nhà nước, cơ quan vận hành phải đánh giá tác động trong trường hợp nào?

REQUIRED POINT P1

description: Phải đánh giá tác động khi hệ thống thuộc nhóm AI có rủi ro cao.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-20_khoan-1_diem-a

full chunk text

### 142-2026-ND-CP_dieu-20_khoan-1_diem-a

```text
Hệ thống thuộc nhóm hệ thống trí tuệ nhân tạo có rủi ro cao theo quy định của Luật;
```

REQUIRED POINT P2

description: Phải đánh giá tác động khi hệ thống thuộc các trường hợp sử dụng tại khoản 7 Điều 20 và kết quả được dùng làm căn cứ trực tiếp để người có thẩm quyền ban hành quyết định hành chính.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-20_khoan-1_diem-b, 142-2026-ND-CP_dieu-20_khoan-7_diem-a, 142-2026-ND-CP_dieu-20_khoan-7_diem-b, 142-2026-ND-CP_dieu-20_khoan-7_diem-c, 142-2026-ND-CP_dieu-20_khoan-7_diem-d

full chunk text

### 142-2026-ND-CP_dieu-20_khoan-1_diem-b

```text
Hệ thống trí tuệ nhân tạo quy định tại khoản 7 Điều này mà kết quả của hệ thống được sử dụng làm căn cứ trực tiếp để người có thẩm quyền xem xét, quyết định ban hành quyết định hành chính.
```

### 142-2026-ND-CP_dieu-20_khoan-7_diem-a

```text
Kết quả của hệ thống được sử dụng làm căn cứ trong quá trình xem xét, quyết định trong hoạt động quản lý nhà nước hoặc cung cấp dịch vụ công;
```

### 142-2026-ND-CP_dieu-20_khoan-7_diem-b

```text
Được sử dụng để phân loại, chấm điểm, đánh giá hoặc xếp hạng tổ chức, cá nhân;
```

### 142-2026-ND-CP_dieu-20_khoan-7_diem-c

```text
Được sử dụng để phân bổ ngân sách, nguồn lực công hoặc xác định mức hưởng, đối tượng thụ hưởng chính sách, chế độ;
```

### 142-2026-ND-CP_dieu-20_khoan-7_diem-d

```text
Được sử dụng để phát hiện, lựa chọn, sàng lọc hoặc giám sát tổ chức, cá nhân phục vụ hoạt động quản lý nhà nước.
```

REQUIRED POINT P3

description: Phải đánh giá tác động bổ sung trước khi tiếp tục sử dụng nếu thay đổi về mục đích, chức năng, dữ liệu đầu vào hoặc phạm vi áp dụng làm phát sinh rủi ro mới hoặc thay đổi mức độ rủi ro.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-20_khoan-2

full chunk text

### 142-2026-ND-CP_dieu-20_khoan-2

```text
Trường hợp hệ thống trí tuệ nhân tạo quy định tại khoản 1 Điều này có thay đổi về mục đích sử dụng, chức năng chính, nguồn dữ liệu đầu vào chủ yếu hoặc phạm vi đối tượng áp dụng làm phát sinh rủi ro mới hoặc làm thay đổi mức độ rủi ro của hệ thống, cơ quan, đơn vị triển khai phải thực hiện đánh giá tác động bổ sung trước khi tiếp tục sử dụng hệ thống.
```

REFERENCE ANSWER

Phải đánh giá tác động khi hệ thống AI có rủi ro cao hoặc thuộc trường hợp sử dụng tại khoản 7 Điều 20 mà kết quả là căn cứ trực tiếp để ban hành quyết định hành chính. Phải đánh giá bổ sung trước khi tiếp tục sử dụng nếu thay đổi về mục đích, chức năng, dữ liệu đầu vào hoặc phạm vi áp dụng làm phát sinh rủi ro mới hoặc thay đổi mức độ rủi ro.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval026

QUERY

Báo cáo đánh giá tác động khi sử dụng AI trong khu vực công cần đề cập những nội dung gì?

REQUIRED POINT P1

description: Báo cáo phải mô tả hệ thống và mục đích sử dụng.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-20_khoan-3_diem-a

full chunk text

### 142-2026-ND-CP_dieu-20_khoan-3_diem-a

```text
Thông tin mô tả hệ thống trí tuệ nhân tạo và mục đích sử dụng;
```

REQUIRED POINT P2

description: Báo cáo phải nhận diện và đánh giá rủi ro.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-20_khoan-3_diem-b

full chunk text

### 142-2026-ND-CP_dieu-20_khoan-3_diem-b

```text
Nhận diện và đánh giá rủi ro;
```

REQUIRED POINT P3

description: Báo cáo phải nêu biện pháp kiểm soát và giảm thiểu rủi ro.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-20_khoan-3_diem-c

full chunk text

### 142-2026-ND-CP_dieu-20_khoan-3_diem-c

```text
Biện pháp kiểm soát và giảm thiểu rủi ro;
```

REQUIRED POINT P4

description: Báo cáo phải nêu cơ chế giám sát và can thiệp của con người khi vận hành.
importance: required
supporting chunks: 142-2026-ND-CP_dieu-20_khoan-3_diem-d

full chunk text

### 142-2026-ND-CP_dieu-20_khoan-3_diem-d

```text
Cơ chế bảo đảm khả năng giám sát và can thiệp của con người trong quá trình vận hành hệ thống.
```

REFERENCE ANSWER

Nêu mô tả hệ thống, mục đích sử dụng; nhận diện, đánh giá rủi ro; biện pháp kiểm soát, giảm thiểu; và cơ chế giám sát, can thiệp của con người khi vận hành.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval027

QUERY

Nguyên tắc đạo đức khi phát triển và sử dụng trí tuệ nhân tạo được đặt ra như thế nào?

REQUIRED POINT P1

description: Bảo đảm an toàn, độ tin cậy và không gây hại cho con người.
importance: required
supporting chunks: 134-2025-QH15_dieu-26_khoan-1_diem-a

full chunk text

### 134-2025-QH15_dieu-26_khoan-1_diem-a

```text
Bảo đảm an toàn, độ tin cậy và không gây hại đến tính mạng, sức khỏe, danh dự, nhân phẩm và đời sống tinh thần của con người;
```

REQUIRED POINT P2

description: Tôn trọng quyền con người, quyền công dân, bảo đảm công bằng, minh bạch và không phân biệt đối xử.
importance: required
supporting chunks: 134-2025-QH15_dieu-26_khoan-1_diem-b

full chunk text

### 134-2025-QH15_dieu-26_khoan-1_diem-b

```text
Tôn trọng quyền con người, quyền công dân, bảo đảm công bằng, minh bạch và không phân biệt đối xử trong phát triển và sử dụng trí tuệ nhân tạo;
```

REQUIRED POINT P3

description: Thúc đẩy hạnh phúc, thịnh vượng và phát triển bền vững của con người, cộng đồng và xã hội.
importance: required
supporting chunks: 134-2025-QH15_dieu-26_khoan-1_diem-c

full chunk text

### 134-2025-QH15_dieu-26_khoan-1_diem-c

```text
Thúc đẩy hạnh phúc, thịnh vượng và sự phát triển bền vững của con người, cộng đồng và xã hội;
```

REQUIRED POINT P4

description: Khuyến khích đổi mới sáng tạo và trách nhiệm xã hội trong nghiên cứu, phát triển và ứng dụng AI.
importance: required
supporting chunks: 134-2025-QH15_dieu-26_khoan-1_diem-d

full chunk text

### 134-2025-QH15_dieu-26_khoan-1_diem-d

```text
Khuyến khích đổi mới sáng tạo và trách nhiệm xã hội trong nghiên cứu, phát triển và ứng dụng trí tuệ nhân tạo.
```

REFERENCE ANSWER

Bảo đảm an toàn, độ tin cậy, không gây hại; tôn trọng quyền con người/công dân, công bằng, minh bạch, không phân biệt đối xử; thúc đẩy hạnh phúc, thịnh vượng, phát triển bền vững, đổi mới sáng tạo và trách nhiệm xã hội.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval028

QUERY

Tổ chức phát triển hoặc triển khai AI cần bảo đảm trách nhiệm giải trình ra sao?

REQUIRED POINT P1

description: Tổ chức, cá nhân phải xác định rõ các tác động mà hệ thống có thể gây ra.
importance: required
supporting chunks: 05-2026-TT-BKHCN_dieu-3_khoan-2_diem-d

full chunk text

### 05-2026-TT-BKHCN_dieu-3_khoan-2_diem-d

```text
Khả năng giải thích và trách nhiệm giải trình: Tổ chức, cá nhân xác định rõ các tác động mà hệ thống có thể gây ra, chuẩn bị tài liệu giải thích và bằng chứng về quá trình thiết kế, huấn luyện, kiểm thử. Phân định rõ chủ thể chịu trách nhiệm giải trình đối với các quyết định do hệ thống tạo ra.
```

REQUIRED POINT P2

description: Phải chuẩn bị tài liệu giải thích và bằng chứng về quá trình thiết kế, huấn luyện và kiểm thử.
importance: required
supporting chunks: 05-2026-TT-BKHCN_dieu-3_khoan-2_diem-d

full chunk text

### 05-2026-TT-BKHCN_dieu-3_khoan-2_diem-d

```text
Khả năng giải thích và trách nhiệm giải trình: Tổ chức, cá nhân xác định rõ các tác động mà hệ thống có thể gây ra, chuẩn bị tài liệu giải thích và bằng chứng về quá trình thiết kế, huấn luyện, kiểm thử. Phân định rõ chủ thể chịu trách nhiệm giải trình đối với các quyết định do hệ thống tạo ra.
```

REQUIRED POINT P3

description: Phải phân định rõ chủ thể chịu trách nhiệm giải trình đối với các quyết định do hệ thống tạo ra.
importance: required
supporting chunks: 05-2026-TT-BKHCN_dieu-3_khoan-2_diem-d

full chunk text

### 05-2026-TT-BKHCN_dieu-3_khoan-2_diem-d

```text
Khả năng giải thích và trách nhiệm giải trình: Tổ chức, cá nhân xác định rõ các tác động mà hệ thống có thể gây ra, chuẩn bị tài liệu giải thích và bằng chứng về quá trình thiết kế, huấn luyện, kiểm thử. Phân định rõ chủ thể chịu trách nhiệm giải trình đối với các quyết định do hệ thống tạo ra.
```

REQUIRED POINT P4

description: Phải phân định trách nhiệm của các chủ thể trong vòng đời hệ thống và bảo đảm đầu mối tiếp nhận, xử lý khiếu nại, khắc phục hậu quả.
importance: required
supporting chunks: 05-2026-TT-BKHCN_dieu-3_khoan-4_diem-b

full chunk text

### 05-2026-TT-BKHCN_dieu-3_khoan-4_diem-b

```text
Trách nhiệm xã hội: Tổ chức, cá nhân phát triển, triển khai và sử dụng hệ thống trí tuệ nhân tạo phân định rõ trách nhiệm của các chủ thể trong vòng đời hệ thống; bảo đảm có đầu mối tiếp nhận, xử lý khiếu nại và khắc phục hậu quả.
```

REFERENCE ANSWER

Phải xác định tác động, chuẩn bị tài liệu giải thích và bằng chứng về thiết kế, huấn luyện, kiểm thử; phân định chủ thể giải trình các quyết định AI và trách nhiệm trong vòng đời; có đầu mối tiếp nhận, xử lý khiếu nại, khắc phục hậu quả.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval029

QUERY

Theo Khung đạo đức trí tuệ nhân tạo quốc gia, khi hệ thống AI có thể ảnh hưởng đáng kể đến quyền con người thì cần áp dụng những biện pháp kiểm soát nào?

REQUIRED POINT P1

description: Xây dựng cơ chế giám sát và can thiệp của con người phù hợp với mức độ ảnh hưởng, đồng thời duy trì kiểm soát và khả năng can thiệp đối với mọi quyết định, hành vi của AI.
importance: required
supporting chunks: 05-2026-TT-BKHCN_dieu-3_khoan-1_diem-c

full chunk text

### 05-2026-TT-BKHCN_dieu-3_khoan-1_diem-c

```text
Kiểm soát của con người: Tổ chức, cá nhân có trách nhiệm xây dựng cơ chế giám sát và can thiệp của con người phù hợp với mức độ ảnh hưởng của hệ thống; bảo đảm duy trì sự kiểm soát và khả năng can thiệp của con người đối với mọi quyết định và hành vi của hệ thống trí tuệ nhân tạo.
```

REQUIRED POINT P2

description: Áp dụng biện pháp rà soát phù hợp để bảo đảm hệ thống không xâm phạm quyền riêng tư, dữ liệu cá nhân, tự do ý chí, quyền tiếp cận thông tin, bình đẳng và các quyền hợp pháp khác.
importance: required
supporting chunks: 05-2026-TT-BKHCN_dieu-3_khoan-2_diem-a

full chunk text

### 05-2026-TT-BKHCN_dieu-3_khoan-2_diem-a

```text
Tôn trọng quyền con người, quyền công dân: Tổ chức, cá nhân áp dụng biện pháp rà soát phù hợp để bảo đảm hệ thống trí tuệ nhân tạo không xâm phạm quyền riêng tư, dữ liệu cá nhân, tự do ý chí, quyền tiếp cận thông tin, quyền được đối xử bình đẳng và các quyền hợp pháp khác theo quy định của pháp luật.
```

REFERENCE ANSWER

Xây dựng giám sát và can thiệp con người phù hợp mức ảnh hưởng, duy trì kiểm soát với mọi quyết định/hành vi AI; đồng thời rà soát để không xâm phạm quyền riêng tư, dữ liệu cá nhân, tự do ý chí, tiếp cận thông tin, bình đẳng và quyền hợp pháp khác.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---

## eval030

QUERY

Những yêu cầu nào giúp bảo đảm con người vẫn có khả năng giám sát và can thiệp vào hệ thống AI?

REQUIRED POINT P1

description: AI phục vụ con người và không thay thế thẩm quyền, trách nhiệm của con người.
importance: required
supporting chunks: 134-2025-QH15_dieu-4_khoan-2

full chunk text

### 134-2025-QH15_dieu-4_khoan-2

```text
Trí tuệ nhân tạo phục vụ con người, không thay thế thẩm quyền và trách nhiệm của con người. Bảo đảm duy trì sự kiểm soát và khả năng can thiệp của con người đối với mọi quyết định và hành vi của hệ thống trí tuệ nhân tạo; an toàn hệ thống, an ninh dữ liệu và bảo mật thông tin; khả năng kiểm tra và giám sát quá trình phát triển và vận hành hệ thống trí tuệ nhân tạo.
```

REQUIRED POINT P2

description: Duy trì sự kiểm soát và khả năng can thiệp của con người đối với mọi quyết định và hành vi của AI.
importance: required
supporting chunks: 134-2025-QH15_dieu-4_khoan-2

full chunk text

### 134-2025-QH15_dieu-4_khoan-2

```text
Trí tuệ nhân tạo phục vụ con người, không thay thế thẩm quyền và trách nhiệm của con người. Bảo đảm duy trì sự kiểm soát và khả năng can thiệp của con người đối với mọi quyết định và hành vi của hệ thống trí tuệ nhân tạo; an toàn hệ thống, an ninh dữ liệu và bảo mật thông tin; khả năng kiểm tra và giám sát quá trình phát triển và vận hành hệ thống trí tuệ nhân tạo.
```

REQUIRED POINT P3

description: Bảo đảm an toàn hệ thống, an ninh dữ liệu và bảo mật thông tin.
importance: required
supporting chunks: 134-2025-QH15_dieu-4_khoan-2

full chunk text

### 134-2025-QH15_dieu-4_khoan-2

```text
Trí tuệ nhân tạo phục vụ con người, không thay thế thẩm quyền và trách nhiệm của con người. Bảo đảm duy trì sự kiểm soát và khả năng can thiệp của con người đối với mọi quyết định và hành vi của hệ thống trí tuệ nhân tạo; an toàn hệ thống, an ninh dữ liệu và bảo mật thông tin; khả năng kiểm tra và giám sát quá trình phát triển và vận hành hệ thống trí tuệ nhân tạo.
```

REQUIRED POINT P4

description: Bảo đảm khả năng kiểm tra và giám sát quá trình phát triển, vận hành hệ thống.
importance: required
supporting chunks: 134-2025-QH15_dieu-4_khoan-2

full chunk text

### 134-2025-QH15_dieu-4_khoan-2

```text
Trí tuệ nhân tạo phục vụ con người, không thay thế thẩm quyền và trách nhiệm của con người. Bảo đảm duy trì sự kiểm soát và khả năng can thiệp của con người đối với mọi quyết định và hành vi của hệ thống trí tuệ nhân tạo; an toàn hệ thống, an ninh dữ liệu và bảo mật thông tin; khả năng kiểm tra và giám sát quá trình phát triển và vận hành hệ thống trí tuệ nhân tạo.
```

REFERENCE ANSWER

AI phục vụ con người, không thay thế thẩm quyền và trách nhiệm con người; phải duy trì kiểm soát và khả năng can thiệp với mọi quyết định, hành vi AI, cùng an toàn hệ thống, an ninh dữ liệu, bảo mật và khả năng kiểm tra, giám sát quá trình phát triển/vận hành.

REVIEW:
[ ] PASS
[ ] NEEDS EDIT

HUMAN NOTE:

---
