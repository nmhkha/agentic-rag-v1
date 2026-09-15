"""Build the generation annotation audit v1 artifact from the frozen v0 draft."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GEN = ROOT / "annotation/generation"
V0 = GEN / "generation_eval_v0.json"
V1 = GEN / "generation_eval_v1.json"
MANIFEST = GEN / "generation_eval_v1_manifest.json"
REPORT = GEN / "generation_annotation_v1_report.md"
REVIEW = GEN / "generation_annotation_v1_review.md"
RETRIEVAL = ROOT / "eval-sets/retrieval/retrieval_eval.jsonl"
CORPUS = ROOT / "data/versions/corpus-v0.1/chunks.jsonl"


def p(point_id: str, description: str, importance: str, *chunks: str) -> dict:
    return {
        "point_id": point_id,
        "description": description,
        "importance": importance,
        "supporting_chunk_ids": list(chunks),
    }


def build_points() -> dict[str, list[dict]]:
    q = {}
    q["eval001"] = [
        p("P1", "Rủi ro cao: có thể gây thiệt hại đáng kể đến các lợi ích được luật bảo vệ.", "required", "134-2025-QH15_dieu-9_khoan-1_diem-a"),
        p("P2", "Rủi ro trung bình: có thể gây nhầm lẫn, tác động hoặc thao túng vì người sử dụng không nhận biết được AI hoặc nội dung AI.", "required", "134-2025-QH15_dieu-9_khoan-1_diem-b"),
        p("P3", "Rủi ro thấp: không thuộc trường hợp rủi ro cao hoặc trung bình.", "required", "134-2025-QH15_dieu-9_khoan-1_diem-c"),
    ]
    q["eval002"] = [
        p("P1", "Thủ tướng Chính phủ có thẩm quyền ban hành, sửa đổi, bổ sung Danh mục hệ thống AI có rủi ro cao.", "required", "142-2026-ND-CP_dieu-7_khoan-2_diem-d"),
        p("P2", "Bộ Khoa học và Công nghệ chủ trì phối hợp xây dựng và trình Danh mục trên cơ sở tiêu chí, nguyên tắc của Nghị định.", "important", "142-2026-ND-CP_dieu-7_khoan-2_diem-d"),
    ]
    q["eval003"] = [
        p("P1", "Phải lập hồ sơ phân loại trước khi đưa hệ thống AI rủi ro cao hoặc trung bình vào sử dụng.", "required", "142-2026-ND-CP_dieu-12_khoan-1"),
    ]
    q["eval004"] = [
        p("P1", "Thiết lập và duy trì hệ thống quản lý rủi ro phù hợp với mục đích, phạm vi triển khai và mức độ rủi ro.", "required", "142-2026-ND-CP_dieu-15_khoan-1"),
        p("P2", "Xác định và đánh giá các rủi ro có thể phát sinh đối với quyền, an toàn, an ninh hoặc lợi ích công cộng.", "required", "142-2026-ND-CP_dieu-15_khoan-2_diem-a"),
        p("P3", "Bảo đảm chất lượng, tính phù hợp và tính đại diện của dữ liệu huấn luyện, kiểm thử và đánh giá trong phạm vi cần thiết.", "required", "142-2026-ND-CP_dieu-15_khoan-2_diem-b"),
        p("P4", "Thiết kế và duy trì cơ chế giám sát, can thiệp của con người phù hợp với mức độ rủi ro.", "required", "142-2026-ND-CP_dieu-15_khoan-2_diem-c"),
        p("P5", "Áp dụng biện pháp kỹ thuật hoặc quản lý để phòng ngừa, hạn chế hoặc kiểm soát rủi ro đã xác định.", "required", "142-2026-ND-CP_dieu-15_khoan-2_diem-d"),
        p("P6", "Rà soát và cập nhật biện pháp quản lý rủi ro khi mô hình, dữ liệu, phương thức vận hành hoặc mục đích sử dụng thay đổi đáng kể.", "required", "142-2026-ND-CP_dieu-15_khoan-2_diem-đ"),
    ]
    q["eval005a"] = [
        p("P1", "Nhà cung cấp phải thiết lập, duy trì và rà soát biện pháp quản lý rủi ro khi có thay đổi đáng kể hoặc rủi ro mới.", "required", "134-2025-QH15_dieu-14_khoan-1_diem-a"),
        p("P2", "Nhà cung cấp phải quản trị dữ liệu huấn luyện, kiểm thử và vận hành, bảo đảm chất lượng trong phạm vi khả năng kỹ thuật và phù hợp mục đích sử dụng.", "required", "134-2025-QH15_dieu-14_khoan-1_diem-b"),
        p("P3", "Nhà cung cấp phải lập, cập nhật, lưu giữ hồ sơ kỹ thuật và nhật ký ở mức cần thiết; cung cấp thông tin cần thiết, tương xứng cho kiểm tra nhưng không làm lộ bí mật kinh doanh.", "required", "134-2025-QH15_dieu-14_khoan-1_diem-c"),
        p("P4", "Nhà cung cấp phải thiết kế hệ thống bảo đảm khả năng giám sát và can thiệp của con người.", "required", "134-2025-QH15_dieu-14_khoan-1_diem-d"),
        p("P5", "Nhà cung cấp phải thực hiện nghĩa vụ minh bạch và xử lý sự cố.", "required", "134-2025-QH15_dieu-14_khoan-1_diem-đ"),
        p("P6", "Nhà cung cấp phải giải trình và cung cấp thông tin cần thiết cho cơ quan, người sử dụng và người bị ảnh hưởng; việc cung cấp không được bộc lộ mã nguồn, thuật toán chi tiết, tham số, bí mật kinh doanh hoặc bí mật công nghệ.", "required", "134-2025-QH15_dieu-14_khoan-1_diem-e"),
        p("P7", "Nhà cung cấp phải phối hợp với cơ quan nhà nước có thẩm quyền và bên triển khai trong kiểm tra, đánh giá, hậu kiểm và khắc phục sự cố.", "required", "134-2025-QH15_dieu-14_khoan-1_diem-g"),
    ]
    q["eval005b"] = [
        p("P1", "Bên triển khai phải vận hành và giám sát hệ thống đúng mục đích, phạm vi và mức rủi ro đã phân loại, không làm phát sinh rủi ro mới hoặc cao hơn.", "required", "134-2025-QH15_dieu-14_khoan-2_diem-a"),
        p("P2", "Bên triển khai phải bảo đảm an toàn, bảo mật dữ liệu và khả năng can thiệp của con người trong quá trình sử dụng.", "required", "134-2025-QH15_dieu-14_khoan-2_diem-b"),
        p("P3", "Bên triển khai phải duy trì tuân thủ tiêu chuẩn, quy chuẩn kỹ thuật về AI trong quá trình vận hành.", "required", "134-2025-QH15_dieu-14_khoan-2_diem-c"),
        p("P4", "Bên triển khai phải thực hiện nghĩa vụ minh bạch và xử lý sự cố.", "required", "134-2025-QH15_dieu-14_khoan-2_diem-d"),
        p("P5", "Bên triển khai phải giải trình và cung cấp thông tin cần thiết cho cơ quan, người sử dụng và người bị ảnh hưởng về việc vận hành, kiểm soát rủi ro và sự cố.", "required", "134-2025-QH15_dieu-14_khoan-2_diem-đ"),
        p("P6", "Bên triển khai phải phối hợp với nhà cung cấp và cơ quan nhà nước có thẩm quyền trong kiểm tra, đánh giá, hậu kiểm và khắc phục sự cố.", "required", "134-2025-QH15_dieu-14_khoan-2_diem-e"),
    ]
    q["eval006"] = [
        p("P1", "Bảo đảm người sử dụng biết mình đang tương tác với AI, trừ trường hợp pháp luật có quy định khác.", "required", "134-2025-QH15_dieu-11_khoan-1"),
        p("P2", "Đánh dấu âm thanh, hình ảnh và video do AI tạo ra ở định dạng máy đọc theo quy định.", "required", "134-2025-QH15_dieu-11_khoan-2"),
        p("P3", "Nhà cung cấp và bên triển khai phải duy trì thông tin minh bạch trong suốt quá trình cung cấp hệ thống, sản phẩm hoặc nội dung.", "required", "134-2025-QH15_dieu-11_khoan-5"),
    ]
    q["eval007"] = [
        p("P1", "Thông báo hoặc nhãn phải rõ ràng, dễ hiểu và dễ nhận biết đối với người tiếp nhận.", "required", "142-2026-ND-CP_dieu-18_khoan-3_diem-a"),
        p("P2", "Thông báo hoặc nhãn phải được thực hiện trước hoặc tại thời điểm người tiếp nhận tiếp cận nội dung.", "required", "142-2026-ND-CP_dieu-18_khoan-3_diem-b"),
        p("P3", "Thông báo hoặc nhãn không được che giấu hoặc làm giảm khả năng nhận biết bản chất nội dung.", "required", "142-2026-ND-CP_dieu-18_khoan-3_diem-c"),
        p("P4", "Thông báo hoặc nhãn phải phù hợp với loại hình và phương thức cung cấp nội dung.", "required", "142-2026-ND-CP_dieu-18_khoan-3_diem-d"),
        p("P5", "Thông báo hoặc nhãn không được gây cản trở đáng kể việc hiển thị, trình diễn hoặc sử dụng nội dung.", "required", "142-2026-ND-CP_dieu-18_khoan-3_diem-đ"),
        p("P6", "Có thể hiển thị trực tiếp trên nội dung, tại tiêu đề/mô tả/chú thích, trên giao diện nền tảng, hoặc thông báo bằng âm thanh hay hình thức phù hợp khác.", "important", "142-2026-ND-CP_dieu-18_khoan-5_diem-a", "142-2026-ND-CP_dieu-18_khoan-5_diem-b", "142-2026-ND-CP_dieu-18_khoan-5_diem-c", "142-2026-ND-CP_dieu-18_khoan-5_diem-d"),
    ]
    q["eval008"] = [
        p("P1", "Bên triển khai phải thông báo rõ ràng khi đưa ra công cộng nội dung AI tạo hoặc chỉnh sửa có khả năng gây nhầm lẫn về tính xác thực của sự kiện, nhân vật hoặc nguồn gốc.", "required", "142-2026-ND-CP_dieu-18_khoan-1"),
        p("P2", "Phạm vi đáng chú ý gồm nội dung mô phỏng/giả lập ngoại hình, giọng nói người thật hoặc tái hiện sự kiện thực tế; trường hợp tái hiện sự kiện có ngoại lệ khi pháp luật quy định khác.", "important", "142-2026-ND-CP_dieu-18_khoan-2_diem-a", "142-2026-ND-CP_dieu-18_khoan-2_diem-b"),
        p("P3", "Đối với điện ảnh, chương trình nghệ thuật hoặc nội dung sáng tạo, bên triển khai trực tiếp đưa nội dung ra công cộng thực hiện thông báo/gắn nhãn theo đặc thù nhưng vẫn phải bảo đảm người tiếp nhận nhận biết rõ nguồn gốc AI.", "important", "142-2026-ND-CP_dieu-18_khoan-6"),
    ]
    q["eval009"] = [
        p("P1", "Người sử dụng phải nhận biết đang tương tác với AI, trừ trường hợp pháp luật có quy định khác.", "required", "134-2025-QH15_dieu-11_khoan-1"),
    ]
    q["eval010"] = [
        p("P1", "Khẩn trương áp dụng biện pháp kỹ thuật để khắc phục, tạm dừng hoặc thu hồi hệ thống.", "required", "134-2025-QH15_dieu-12_khoan-2_diem-a"),
        p("P2", "Đồng thời thông báo sự cố cho cơ quan có thẩm quyền.", "required", "134-2025-QH15_dieu-12_khoan-2_diem-a"),
    ]
    q["eval011"] = [
        p("P1", "Có thể được công nhận kết quả đánh giá sự phù hợp trong phạm vi thử nghiệm.", "required", "134-2025-QH15_dieu-21_khoan-2_diem-a"),
        p("P2", "Có thể được miễn, giảm hoặc điều chỉnh nghĩa vụ tuân thủ tương ứng trong phạm vi thử nghiệm.", "required", "134-2025-QH15_dieu-21_khoan-2_diem-b"),
    ]
    q["eval012"] = [
        p("P1", "Ủy ban nhân dân cấp tỉnh quyết định đối với hệ thống cấp độ 1 hoặc 2 triển khai trong phạm vi một tỉnh.", "required", "142-2026-ND-CP_dieu-23_khoan-3_diem-a"),
        p("P2", "Bộ hoặc cơ quan ngang bộ quyết định đối với hệ thống cấp độ 1 hoặc 2 thuộc phạm vi quản lý nhà nước và triển khai từ hai tỉnh trở lên, hoặc do đơn vị thuộc phạm vi quản lý trực tiếp triển khai.", "required", "142-2026-ND-CP_dieu-23_khoan-3_diem-b"),
        p("P3", "Bộ Công an quyết định đối với hệ thống AI cấp độ 3.", "required", "142-2026-ND-CP_dieu-23_khoan-3_diem-c"),
        p("P4", "Nếu hệ thống thuộc phạm vi quản lý của nhiều bộ, bộ quản lý ngành/lĩnh vực có phạm vi quản lý trực tiếp đối với hoạt động sử dụng chính có thẩm quyền.", "required", "142-2026-ND-CP_dieu-23_khoan-3_diem-c"),
    ]
    q["eval013"] = [
        p("P1", "Mức độ rủi ro của hệ thống AI.", "required", "142-2026-ND-CP_dieu-22_khoan-1_diem-a"),
        p("P2", "Tính chất của dữ liệu được sử dụng.", "required", "142-2026-ND-CP_dieu-22_khoan-1_diem-b"),
        p("P3", "Phạm vi và quy mô triển khai thử nghiệm.", "required", "142-2026-ND-CP_dieu-22_khoan-1_diem-c"),
        p("P4", "Mức độ tác động đối với an ninh, trật tự, an toàn xã hội và quyền, lợi ích hợp pháp.", "required", "142-2026-ND-CP_dieu-22_khoan-1_diem-d"),
        p("P5", "Nếu đáp ứng nhiều cấp độ thì phân loại theo cấp cao nhất, xét chức năng, mục đích sử dụng và tác động tổng thể, kể cả hệ thống nhiều thành phần.", "required", "142-2026-ND-CP_dieu-22_khoan-2"),
    ]
    q["eval014"] = [
        p("P1", "Đơn đề nghị tham gia cơ chế thử nghiệm theo mẫu tương ứng với tổ chức hoặc cá nhân.", "required", "142-2026-ND-CP_dieu-24_khoan-2_diem-a"),
        p("P2", "Đề án thử nghiệm mô tả hệ thống, mục tiêu, phạm vi, thời gian và phương án quản lý rủi ro.", "required", "142-2026-ND-CP_dieu-24_khoan-2_diem-b"),
        p("P3", "Tài liệu mô tả biện pháp bảo vệ quyền và lợi ích hợp pháp của tổ chức, cá nhân chịu tác động.", "required", "142-2026-ND-CP_dieu-24_khoan-2_diem-c"),
        p("P4", "Tài liệu mô tả năng lực kỹ thuật, nhân sự hoặc hạ tầng liên quan trực tiếp đến phạm vi thử nghiệm.", "required", "142-2026-ND-CP_dieu-24_khoan-2_diem-d"),
    ]
    q["eval015"] = [
        p("P1", "Có rủi ro ảnh hưởng đến an toàn, an ninh hoặc quyền, lợi ích hợp pháp của tổ chức, cá nhân.", "required", "134-2025-QH15_dieu-21_khoan-3"),
        p("P2", "Tổ chức, cá nhân vi phạm giới hạn thử nghiệm hoặc không khắc phục sự cố theo yêu cầu của cơ quan có thẩm quyền.", "required", "142-2026-ND-CP_dieu-25_khoan-1_diem-c"),
    ]
    q["eval016"] = [
        p("P1", "Thử nghiệm cấp độ 1 hoặc 2 phải báo cáo định kỳ 06 tháng một lần.", "required", "142-2026-ND-CP_dieu-25_khoan-2_diem-a"),
        p("P2", "Thử nghiệm cấp độ 3 phải báo cáo định kỳ 03 tháng một lần.", "required", "142-2026-ND-CP_dieu-25_khoan-2_diem-b"),
        p("P3", "Phải báo cáo khi hệ thống xảy ra sự cố nghiêm trọng hoặc vượt giới hạn thử nghiệm đã xác định.", "required", "142-2026-ND-CP_dieu-25_khoan-3_diem-a", "142-2026-ND-CP_dieu-25_khoan-3_diem-b"),
        p("P4", "Phải nộp báo cáo tổng kết chậm nhất 15 ngày trước khi kết thúc thời hạn thử nghiệm.", "required", "142-2026-ND-CP_dieu-25_khoan-4"),
    ]
    q["eval017"] = [
        p("P1", "Được đề nghị gia hạn bằng đơn gia hạn và báo cáo tổng kết nộp chậm nhất 15 ngày làm việc trước khi hết hạn.", "required", "142-2026-ND-CP_dieu-27_khoan-1"),
        p("P2", "Cơ quan có thẩm quyền thẩm định, quyết định và cấp gia hạn trong 10 ngày làm việc.", "required", "142-2026-ND-CP_dieu-27_khoan-1"),
        p("P3", "Nếu không chấp thuận hoặc không gia hạn thì phải trả lời bằng văn bản và nêu rõ lý do.", "required", "142-2026-ND-CP_dieu-27_khoan-1"),
    ]
    q["eval018"] = [
        p("P1", "Trong 15 ngày làm việc từ khi nhận báo cáo tổng kết, cơ quan có thẩm quyền đánh giá và cấp giấy xác nhận hoàn thành.", "required", "142-2026-ND-CP_dieu-27_khoan-1"),
        p("P2", "Nếu từ chối cấp giấy xác nhận hoàn thành thì phải nêu rõ lý do.", "required", "142-2026-ND-CP_dieu-27_khoan-1"),
        p("P3", "Có thể công nhận toàn bộ hoặc một phần kết quả thử nghiệm để đánh giá sự phù hợp.", "required", "142-2026-ND-CP_dieu-27_khoan-2_diem-a"),
        p("P4", "Có thể miễn, giảm hoặc điều chỉnh nghĩa vụ tuân thủ trên cơ sở kết quả được công nhận.", "required", "142-2026-ND-CP_dieu-27_khoan-2_diem-b"),
    ]
    q["eval019"] = [
        p("P1", "Cơ sở dữ liệu quốc gia về AI được tổ chức theo nguyên tắc mở.", "required", "134-2025-QH15_dieu-17_khoan-2"),
        p("P2", "Cơ sở dữ liệu quốc gia về AI được tổ chức theo nguyên tắc an toàn.", "required", "134-2025-QH15_dieu-17_khoan-2"),
        p("P3", "Cơ sở dữ liệu quốc gia về AI được tổ chức theo nguyên tắc có kiểm soát.", "required", "134-2025-QH15_dieu-17_khoan-2"),
    ]
    q["eval020"] = [
        p("P1", "Dữ liệu mở có điều kiện được truy cập, sử dụng khi đáp ứng điều kiện về đăng ký, mục đích sử dụng và bảo mật theo pháp luật.", "required", "142-2026-ND-CP_dieu-3_khoan-7"),
    ]
    q["eval021"] = [
        p("P1", "Dữ liệu mở có thể được đưa vào cơ sở dữ liệu phục vụ AI.", "required", "142-2026-ND-CP_dieu-32_khoan-1_diem-a"),
        p("P2", "Dữ liệu mở có điều kiện có thể được đưa vào cơ sở dữ liệu phục vụ AI.", "required", "142-2026-ND-CP_dieu-32_khoan-1_diem-b"),
        p("P3", "Dữ liệu thương mại của tổ chức, doanh nghiệp theo pháp luật có thể được đưa vào cơ sở dữ liệu phục vụ AI.", "required", "142-2026-ND-CP_dieu-32_khoan-1_diem-c"),
    ]
    q["eval022"] = [
        p("P1", "Trong phạm vi quản lý, cơ quan có trách nhiệm xây dựng và cập nhật dữ liệu mở phục vụ AI.", "required", "142-2026-ND-CP_dieu-32_khoan-5_diem-a"),
        p("P2", "Cơ quan phải tổ chức thu thập, tạo lập, cập nhật, bảo đảm chất lượng, gán nhãn, chú thích và chuẩn hóa các bộ dữ liệu thiết yếu phục vụ phát triển AI.", "required", "142-2026-ND-CP_dieu-32_khoan-5_diem-b"),
        p("P3", "Cơ quan phải thực hiện kết nối thống nhất, chia sẻ và khai thác Cơ sở dữ liệu quốc gia về AI theo pháp luật.", "required", "142-2026-ND-CP_dieu-32_khoan-5_diem-c"),
    ]
    q["eval023"] = [
        p("P1", "Cơ sở dữ liệu quốc gia về AI phải bảo đảm chất lượng, khả năng kết nối và khai thác.", "required", "134-2025-QH15_dieu-17_khoan-2"),
        p("P2", "Cơ sở dữ liệu của các bộ, cơ quan và địa phương phải được xây dựng, cập nhật, kết nối thống nhất với cơ sở dữ liệu quốc gia, bảo đảm tiêu chuẩn, chất lượng dữ liệu và an toàn thông tin.", "required", "134-2025-QH15_dieu-17_khoan-3"),
    ]
    q["eval024"] = [
        p("P1", "Nghiêm cấm lợi dụng điểm yếu của nhóm người dễ bị tổn thương để gây tổn hại cho chính họ hoặc người khác.", "required", "134-2025-QH15_dieu-7_khoan-2_diem-c"),
    ]
    q["eval025"] = [
        p("P1", "Phải đánh giá tác động khi hệ thống thuộc nhóm AI có rủi ro cao.", "required", "142-2026-ND-CP_dieu-20_khoan-1_diem-a"),
        p("P2", "Phải đánh giá tác động khi hệ thống thuộc các trường hợp sử dụng tại khoản 7 Điều 20 và kết quả được dùng làm căn cứ trực tiếp để người có thẩm quyền ban hành quyết định hành chính.", "required", "142-2026-ND-CP_dieu-20_khoan-1_diem-b", "142-2026-ND-CP_dieu-20_khoan-7_diem-a", "142-2026-ND-CP_dieu-20_khoan-7_diem-b", "142-2026-ND-CP_dieu-20_khoan-7_diem-c", "142-2026-ND-CP_dieu-20_khoan-7_diem-d"),
        p("P3", "Phải đánh giá tác động bổ sung trước khi tiếp tục sử dụng nếu thay đổi về mục đích, chức năng, dữ liệu đầu vào hoặc phạm vi áp dụng làm phát sinh rủi ro mới hoặc thay đổi mức độ rủi ro.", "required", "142-2026-ND-CP_dieu-20_khoan-2"),
    ]
    q["eval026"] = [
        p("P1", "Báo cáo phải mô tả hệ thống và mục đích sử dụng.", "required", "142-2026-ND-CP_dieu-20_khoan-3_diem-a"),
        p("P2", "Báo cáo phải nhận diện và đánh giá rủi ro.", "required", "142-2026-ND-CP_dieu-20_khoan-3_diem-b"),
        p("P3", "Báo cáo phải nêu biện pháp kiểm soát và giảm thiểu rủi ro.", "required", "142-2026-ND-CP_dieu-20_khoan-3_diem-c"),
        p("P4", "Báo cáo phải nêu cơ chế giám sát và can thiệp của con người khi vận hành.", "required", "142-2026-ND-CP_dieu-20_khoan-3_diem-d"),
    ]
    q["eval027"] = [
        p("P1", "Bảo đảm an toàn, độ tin cậy và không gây hại cho con người.", "required", "134-2025-QH15_dieu-26_khoan-1_diem-a"),
        p("P2", "Tôn trọng quyền con người, quyền công dân, bảo đảm công bằng, minh bạch và không phân biệt đối xử.", "required", "134-2025-QH15_dieu-26_khoan-1_diem-b"),
        p("P3", "Thúc đẩy hạnh phúc, thịnh vượng và phát triển bền vững của con người, cộng đồng và xã hội.", "required", "134-2025-QH15_dieu-26_khoan-1_diem-c"),
        p("P4", "Khuyến khích đổi mới sáng tạo và trách nhiệm xã hội trong nghiên cứu, phát triển và ứng dụng AI.", "required", "134-2025-QH15_dieu-26_khoan-1_diem-d"),
    ]
    q["eval028"] = [
        p("P1", "Tổ chức, cá nhân phải xác định rõ các tác động mà hệ thống có thể gây ra.", "required", "05-2026-TT-BKHCN_dieu-3_khoan-2_diem-d"),
        p("P2", "Phải chuẩn bị tài liệu giải thích và bằng chứng về quá trình thiết kế, huấn luyện và kiểm thử.", "required", "05-2026-TT-BKHCN_dieu-3_khoan-2_diem-d"),
        p("P3", "Phải phân định rõ chủ thể chịu trách nhiệm giải trình đối với các quyết định do hệ thống tạo ra.", "required", "05-2026-TT-BKHCN_dieu-3_khoan-2_diem-d"),
        p("P4", "Phải phân định trách nhiệm của các chủ thể trong vòng đời hệ thống và bảo đảm đầu mối tiếp nhận, xử lý khiếu nại, khắc phục hậu quả.", "required", "05-2026-TT-BKHCN_dieu-3_khoan-4_diem-b"),
    ]
    q["eval029"] = [
        p("P1", "Xây dựng cơ chế giám sát và can thiệp của con người phù hợp với mức độ ảnh hưởng, đồng thời duy trì kiểm soát và khả năng can thiệp đối với mọi quyết định, hành vi của AI.", "required", "05-2026-TT-BKHCN_dieu-3_khoan-1_diem-c"),
        p("P2", "Áp dụng biện pháp rà soát phù hợp để bảo đảm hệ thống không xâm phạm quyền riêng tư, dữ liệu cá nhân, tự do ý chí, quyền tiếp cận thông tin, bình đẳng và các quyền hợp pháp khác.", "required", "05-2026-TT-BKHCN_dieu-3_khoan-2_diem-a"),
    ]
    q["eval030"] = [
        p("P1", "AI phục vụ con người và không thay thế thẩm quyền, trách nhiệm của con người.", "required", "134-2025-QH15_dieu-4_khoan-2"),
        p("P2", "Duy trì sự kiểm soát và khả năng can thiệp của con người đối với mọi quyết định và hành vi của AI.", "required", "134-2025-QH15_dieu-4_khoan-2"),
        p("P3", "Bảo đảm an toàn hệ thống, an ninh dữ liệu và bảo mật thông tin.", "required", "134-2025-QH15_dieu-4_khoan-2"),
        p("P4", "Bảo đảm khả năng kiểm tra và giám sát quá trình phát triển, vận hành hệ thống.", "required", "134-2025-QH15_dieu-4_khoan-2"),
    ]
    return q


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def build_review(dataset: dict, corpus: list[dict]) -> str:
    chunk_text = {row["chunk_id"]: row["text"] for row in corpus}
    sections = [
        "# Generation annotation v1 human review",
        "",
        "Review each point against the query and the complete supporting gold chunk text. Do not mark a record verified from this sheet; update the dataset only after human legal review.",
        "",
    ]
    for item in dataset["items"]:
        sections.extend([f"## {item['query_id']}", "", "QUERY", "", item["query"], ""])
        for point in item["required_points"]:
            sections.extend([
                f"REQUIRED POINT {point['point_id']}",
                "",
                f"description: {point['description']}",
                f"importance: {point['importance']}",
                f"supporting chunks: {', '.join(point['supporting_chunk_ids'])}",
                "",
                "full chunk text",
                "",
            ])
            for chunk_id in point["supporting_chunk_ids"]:
                sections.extend([f"### {chunk_id}", "", "```text", chunk_text[chunk_id], "```", ""])
        sections.extend([
            "REFERENCE ANSWER",
            "",
            item["reference_answer"],
            "",
            "REVIEW:",
            "[ ] PASS",
            "[ ] NEEDS EDIT",
            "",
            "HUMAN NOTE:",
            "",
            "---",
            "",
        ])
    return "\n".join(sections)


def main() -> None:
    source = json.loads(V0.read_text(encoding="utf-8"))
    original = copy.deepcopy(source)
    point_map = build_points()
    reference_overrides = {
        "eval002": "Thủ tướng Chính phủ là người có thẩm quyền ban hành, sửa đổi, bổ sung Danh mục hệ thống AI có rủi ro cao. Bộ Khoa học và Công nghệ chủ trì phối hợp xây dựng và trình Danh mục.",
        "eval019": "Cơ sở dữ liệu quốc gia về AI được tổ chức theo các nguyên tắc mở, an toàn và có kiểm soát.",
        "eval022": "Đối với dữ liệu mở phục vụ AI, cơ quan quản lý phải xây dựng, cập nhật dữ liệu trong phạm vi quản lý; tổ chức thu thập, tạo lập, cập nhật, bảo đảm chất lượng, gán nhãn, chú thích và chuẩn hóa các bộ dữ liệu thiết yếu; đồng thời kết nối thống nhất, chia sẻ và khai thác Cơ sở dữ liệu quốc gia về AI theo pháp luật.",
        "eval025": "Phải đánh giá tác động khi hệ thống AI có rủi ro cao hoặc thuộc trường hợp sử dụng tại khoản 7 Điều 20 mà kết quả là căn cứ trực tiếp để ban hành quyết định hành chính. Phải đánh giá bổ sung trước khi tiếp tục sử dụng nếu thay đổi về mục đích, chức năng, dữ liệu đầu vào hoặc phạm vi áp dụng làm phát sinh rủi ro mới hoặc thay đổi mức độ rủi ro.",
    }
    unchanged_ids = {"eval003", "eval009", "eval020", "eval024"}
    original_by_id = {item["query_id"]: item for item in original["items"]}
    for item in source["items"]:
        qid = item["query_id"]
        item["required_points"] = copy.deepcopy(original_by_id[qid]["required_points"] if qid in unchanged_ids else point_map[qid])
        if qid in reference_overrides:
            item["reference_answer"] = reference_overrides[qid]
        item["annotation_notes"] = f"Generation Annotation Audit v1 applied; annotation remains draft. {item['annotation_notes']}"
        item["annotation_status"] = "draft"
    source["evaluation_version"] = "generation-eval-v1"
    source["dataset_status"] = "draft"
    V1.write_text(json.dumps(source, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    retrieval = load_jsonl(RETRIEVAL)
    corpus = load_jsonl(CORPUS)
    corpus_ids = {row["chunk_id"] for row in corpus}
    gold_chunk_ids = {c for row in retrieval for c in row["gold_chunk_ids"]}
    assert len(source["items"]) == 31
    assert all(c in corpus_ids and c in gold_chunk_ids for i in source["items"] for pnt in i["required_points"] for c in pnt["supporting_chunk_ids"])
    v0_count = sum(len(i["required_points"]) for i in original["items"])
    v1_count = sum(len(i["required_points"]) for i in source["items"])
    changed = [i["query_id"] for i, j in zip(original["items"], source["items"]) if i["required_points"] != j["required_points"]]
    unchanged = [i["query_id"] for i, j in zip(original["items"], source["items"]) if i["required_points"] == j["required_points"]]
    answer_changed = [i["query_id"] for i, j in zip(original["items"], source["items"]) if i["reference_answer"] != j["reference_answer"]]
    manifest = {
        "evaluation_version": "generation-eval-v1",
        "dataset_status": "draft",
        "dataset_sha256": sha256(V1),
        "source_dataset": "annotation/generation/generation_eval_v0.json",
        "source_dataset_sha256": sha256(V0),
        "source_retrieval_eval": "eval-sets/retrieval/retrieval_eval.jsonl",
        "source_retrieval_eval_sha256": sha256(RETRIEVAL),
        "corpus_chunks": "data/versions/corpus-v0.1/chunks.jsonl",
        "corpus_chunks_sha256": sha256(CORPUS),
        "query_count": len(source["items"]),
        "required_point_count": v1_count,
        "v0_required_point_count": v0_count,
        "point_count_delta": v1_count - v0_count,
        "answerability_counts": {"answerable": sum(i["answerability"] == "answerable" for i in source["items"]), "insufficient_evidence": sum(i["answerability"] == "insufficient_evidence" for i in source["items"])},
        "annotation_status_counts": {"draft": len(source["items"])},
        "note": "Generation Annotation Audit v1 applied to v0; no annotation is verified.",
    }
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    deltas = []
    for old, new in zip(original["items"], source["items"]):
        deltas.append(f"| {old['query_id']} | {len(old['required_points'])} | {len(new['required_points'])} | {len(new['required_points']) - len(old['required_points']):+d} |")
    report = f"""# Generation annotation v1 report

## Summary

- v0 required-point count: **{v0_count}**
- v1 required-point count: **{v1_count}**
- Point-count delta: **+{v1_count - v0_count}**
- Queries: **{len(source['items'])}**; all query IDs and query texts remain frozen.
- Dataset status: **draft**; all 31 records retain `annotation_status = \"draft\"`.

## 1. Point-count delta per query

| Query | v0 | v1 | Delta |
|---|---:|---:|---:|
{chr(10).join(deltas)}

## 2. Changed queries

{', '.join(changed)}.

The changes apply the audit's independently scorable semantic propositions. No point was merged.

## 3. Unchanged queries

{', '.join(unchanged)}.

These queries already had semantically coherent point granularity and were copied from v0 unchanged.

## 4. Reference answers changed

{', '.join(answer_changed)}. Changes were limited to direct answering and scope/condition clarification, especially authority in `eval002`, organisational principles in `eval019`, open-data scope in `eval022`, and the direct-administrative-decision condition in `eval025`.

## 5. Scope clarifications

- `eval002`: the Prime Minister's issuing authority is the core answer; the Ministry of Science and Technology's preparation/submission role is contextual and marked `important`.
- `eval006`: the ongoing transparency duty is attributed to both provider and deployer, as stated by the corpus.
- `eval019`: the reference answer is limited to organisational principles; data categories and quality/connectivity/exploitation are not required points.
- `eval022`: points and reference answer are scoped to the asked open-data responsibility, without turning every data category in the gold chunk into a required point.
- `eval025`: paragraph-7 use contexts count only together with the condition that the result is a direct basis for an administrative decision; no invented threshold was added.
- `eval029`: the query's significant-rights-impact language remains framing for the general framework principles, not a new legal threshold.

## 6. Low/medium confidence annotations

No low-confidence annotation is present. Dataset `annotation_confidence = \"medium\"` remains unchanged for `eval022` and `eval025`. The audit proposal itself marked `eval008`, `eval025`, and `eval028` as medium confidence; these labels were not silently changed in the dataset.

## 7. Potential remaining ambiguity

- `eval008`: the boundary between the general trigger, listed simulation/recreation cases, and creative-content handling may merit human review.
- `eval019`: whether quality, connectivity, and exploitation should be retained as an `important` performance point depends on the intended evaluation scope; v1 follows the instruction to keep the answer on organisational principles.
- `eval022`: the underlying statutory sentence covers open, conditional-open, and commercial data, while the query asks about open data; v1 preserves the query scope.
- `eval028`: the framework's accountability principles are general guidance; reviewers may decide how much evidence a generated answer must provide for each split point.

## 8. Independent-scoring quality check

For the required minimum set (`eval001`, `eval005a`, `eval005b`, `eval006`, `eval007`, `eval014`, `eval019`, `eval022`, `eval025`, `eval027`, `eval028`, `eval029`, `eval030`), a human reviewer can independently decide coverage for each required point from the point description and its supporting gold chunk(s). Result: **YES for all listed queries**; no query is flagged.

## Validation basis

The v1 manifest records hashes for the v0 source, frozen retrieval evaluation, and frozen corpus. Supporting chunks are restricted to existing retrieval gold chunks. Run `python3 tools/validation/validate_generation_eval.py` and the unit tests after generation.
"""
    REPORT.write_text(report, encoding="utf-8")
    REVIEW.write_text(build_review(source, corpus), encoding="utf-8")
    print(f"Wrote {V1}, {MANIFEST}, {REPORT}, and {REVIEW}; {v1_count} points across {len(source['items'])} queries.")


if __name__ == "__main__":
    main()
