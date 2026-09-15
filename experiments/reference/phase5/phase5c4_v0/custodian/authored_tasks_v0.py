"""Restricted ANNOTATOR_A authoring source; contains provisional HOLDOUT plaintext.
Local dataset authoring only. No project imports, inference, external law or API.
Sources: L=134-2025-QH15, N=142-2026-ND-CP, T=05-2026-TT-BKHCN.
Selector suffix is article.clause.point; | separates alternative AND bundles.
"""

TASKS = []

def P(proposition, refs, *, condition=None, origin='query_explicit'):
    return dict(proposition=proposition, refs=refs, role='substantive_supported', condition=condition, origin=origin)

def Q(proposition, refs, unsupported, *, condition, reason=None, concepts=None):
    return dict(proposition=proposition, refs=refs, role='qualified_partial', unsupported=unsupported, condition=condition, origin='query_explicit', reason=reason, concepts=concepts)

def U(request, refs, reason, concepts):
    return dict(proposition=request, refs=refs, role='unresolved_disclosure', unsupported=request, reason=reason, concepts=concepts, origin='query_explicit')

def add(key, family, split, cluster, query, scope, facts, unknown, aspects, *, broad=False, control=None, negative=None, d4=None, exclude=None):
    TASKS.append(dict(key=key, family=family, split=split, cluster=cluster, query=query,
        scope=scope, facts=facts, unknown=unknown, aspects=aspects, broad=broad,
        control=control, negative=negative, d4=d4, exclude=exclude))

# Legal structures were read before these finite legal tasks and queries were authored.
# Family 1: deployment / scope assessment.
add('A01',1,'DEV','research_integrity',
    'Viện của tôi muốn dùng AI hỗ trợ viết và thử nghiệm ý tưởng nghiên cứu trong phòng lab khép kín, không có người tham gia thực tế và không đưa kết quả ra ngoài. Nên tổ chức hoạt động này thế nào cho đúng quy định về AI?',
    'Liêm chính nghiên cứu, giới hạn cơ chế thử nghiệm có kiểm soát, kiểm soát con người trong hoạt động nghiên cứu nội bộ; không mở rộng sang thủ tục xuất bản hoặc sở hữu tác phẩm.',
    'Viện nghiên cứu; AI hỗ trợ nghiên cứu; lab khép kín; không người tham gia thực tế; không tác động bên ngoài.',
    'Loại dữ liệu và mức rủi ro không được xác định; không yêu cầu kết luận về các nghĩa vụ phụ thuộc hai thông tin này.',[
    P('Ứng dụng AI trong nghiên cứu khoa học phải tuân thủ đạo đức nghiên cứu, liêm chính khoa học và phòng ngừa gian lận, đạo văn trong nghiên cứu và công bố.', 'L6.3'),
    P('Thử nghiệm nội bộ khép kín với các điều kiện đã nêu không thuộc cơ chế thử nghiệm có kiểm soát của Nghị định.', 'N21.3'),
    P('AI không thay thế thẩm quyền và trách nhiệm con người; duy trì khả năng kiểm soát, can thiệp, kiểm tra và giám sát.', 'L4.2')],
    broad=True,control='Loại trừ thủ tục sandbox cho lab không có người tham gia thực tế và không tác động bên ngoài.',
    negative=('N24.2','not_applicable','unmet','Không phải hoạt động thuộc cơ chế thử nghiệm có kiểm soát.'),
    d4='Liêm chính nghiên cứu cụ thể chỉ ở L6.3; ngoại lệ lab khép kín chỉ ở N21.3. Nghị định không thay thế nghĩa vụ liêm chính; Luật không nêu ngoại lệ này.')

add('A02',1,'DEV','foreign_contact',
    'Công ty nước ngoài của chúng tôi đưa một hệ thống AI mang thương hiệu mình vào Việt Nam. Hệ thống đã được xác định rủi ro cao nhưng không thuộc diện bắt buộc chứng nhận. Chúng tôi thuê đối tác trong nước vận hành và muốn chuẩn bị việc bàn giao cho phù hợp.',
    'Tư cách nhà cung cấp/bên triển khai, đầu mối tại Việt Nam, phương thức đánh giá và thông tin an toàn bàn giao; không lập danh sách toàn bộ nghĩa vụ rủi ro cao.',
    'Nhà cung cấp nước ngoài mang thương hiệu riêng; rủi ro cao đã xác định; ngoài diện bắt buộc chứng nhận; đối tác vận hành thương mại tại Việt Nam.',
    'Không có thông tin về chứng nhận nước ngoài hoặc việc thay đổi hệ thống.',[
    P('Đơn vị đưa hệ thống ra thị trường dưới thương hiệu mình là nhà cung cấp; đối tác sử dụng trong hoạt động nghề nghiệp thuộc kiểm soát của mình là bên triển khai.', 'L3.4 L3.5'),
    P('Nhà cung cấp nước ngoài rủi ro cao phải có đầu mối liên hệ hợp pháp tại Việt Nam; yêu cầu hiện diện thương mại hoặc đại diện ủy quyền gắn với diện bắt buộc chứng nhận, không tự áp cho tình huống đã loại trừ diện này.', 'L14.6'),
    P('Với rủi ro cao ngoài diện bắt buộc chứng nhận, có thể tự đánh giá hoặc dùng tổ chức phù hợp; tự đánh giá phải lập hồ sơ kỹ thuật và chịu trách nhiệm về kết quả.', 'N13.2.b'),
    P('Bàn giao thông tin cần thiết về mục đích, điều kiện vận hành an toàn, rủi ro đã xác định và biện pháp quản lý tương ứng cho bên triển khai.', 'N15.3')],broad=True,
    d4='Đầu mối pháp lý của nhà cung cấp nước ngoài ở L14.6; nội dung bàn giao bắt buộc cho bên triển khai ở N15.3 và hồ sơ tự đánh giá ở N13.2.b không được một văn bản đơn lẻ bao phủ đầy đủ.')

add('A03',1,'DEV','education_release',
    'Chúng tôi sắp bán hệ thống AI hỗ trợ giáo viên đánh giá học sinh, học sinh cũng tương tác trực tiếp với hệ thống. Kết quả phân loại đã xác định rủi ro cao và không phải chứng nhận bắt buộc. Cần chuẩn bị gì cho lần đưa vào sử dụng đầu tiên?',
    'Bảo vệ người học đặc thù giáo dục, đánh giá sự phù hợp, thông báo phân loại và nhận biết tương tác; không tư vấn chương trình giáo dục hoặc suy luận lại danh mục.',
    'Nhà cung cấp; hệ thống mới; giáo dục; học sinh tương tác trực tiếp; rủi ro cao ngoài diện chứng nhận bắt buộc.',
    'Chưa có thông tin về dữ liệu cụ thể, không xác định tiêu chuẩn kỹ thuật bên ngoài corpus.',[
    P('Trong giáo dục phải phù hợp lứa tuổi và sự phát triển người học, phòng ngừa rủi ro đánh giá/phân loại và bảo đảm an toàn dữ liệu, quyền riêng tư.', 'L6.2.b'),
    P('Phải đánh giá sự phù hợp trước sử dụng; ngoài diện chứng nhận bắt buộc được tự đánh giá với hồ sơ kỹ thuật và trách nhiệm pháp lý hoặc thuê tổ chức phù hợp.', 'N13.1 N13.2.b'),
    P('Thông báo kết quả phân loại trước đưa vào sử dụng trên cổng một cửa; tự kê khai và chịu trách nhiệm nội dung.', 'N14.1'),
    P('Thiết kế và vận hành để học sinh nhận biết đang tương tác với AI, trừ ngoại lệ pháp luật được nêu trong điều khoản.', 'L11.1')],broad=True,
    d4='Bảo vệ đặc thù người học ở L6.2.b không được Nghị định trình bày đầy đủ; lựa chọn tự đánh giá kèm hồ sơ/trách nhiệm ở N13.2.b chi tiết hơn L13.2.b, nên hai tài liệu cần thiết.')

add('A04',1,'DEV','private_compute_sharing',
    'Thư viện tư nhân của tôi có hạ tầng tính toán đang dùng cho AI và muốn chia sẻ phần năng lực nhàn rỗi vào mạng lưới quốc gia. Chúng tôi muốn có phương án tham gia vẫn giữ được quyền quản lý hạ tầng và quyền chọn công nghệ của khách hàng.',
    'Tính tự nguyện và quyền sở hữu/quản lý khi chia sẻ; không khóa công nghệ; bảo mật, kiểm soát truy cập và yêu cầu năng lượng của bên vận hành hạ tầng tham gia mạng lưới.',
    'Thư viện tư nhân quản lý hạ tầng AI; dự định tham gia mạng lưới quốc gia và cung cấp cho khách hàng.',
    'Hợp đồng và quy chuẩn cụ thể chưa có; chỉ nêu nghĩa vụ nguyên tắc của corpus.',[
    P('Hạ tầng do tổ chức, doanh nghiệp đầu tư tham gia tự nguyện bằng thỏa thuận/hợp đồng; kết nối không tự thay đổi quyền sở hữu, quản lý, khai thác hợp pháp.', 'N30.1.b N30.1.c'),
    P('Không áp đặt điều kiện kỹ thuật hoặc thương mại hạn chế lựa chọn công nghệ, mô hình hoặc cách triển khai của người dùng, trừ trường hợp pháp luật quy định khác.', 'N29.2.b'),
    P('Bên vận hành tham gia phải bảo đảm an ninh, bảo vệ dữ liệu và bí mật, áp dụng biện pháp kỹ thuật/quản lý kiểm soát truy cập, khai thác.', 'N30.3.b N30.3.c'),
    P('Tuân thủ sử dụng năng lượng tiết kiệm, triển khai giải pháp giảm phát thải và không đe dọa an toàn hệ thống điện quốc gia.', 'N29.2.đ')],broad=True)

add('A05',1,'HOLDOUT_TEST','public_benefits_fairness',
    'Cơ quan tôi chuẩn bị dùng AI xếp hạng hồ sơ hưởng trợ cấp, kết quả là căn cứ trực tiếp để ký quyết định hành chính. Trước khi triển khai, chúng tôi cần xây dựng cách quản trị thế nào để người dân được đối xử công bằng?',
    'Đánh giá tác động trước triển khai, công khai có ngoại lệ, giảm thiên lệch và trách nhiệm quyết định của con người trong việc xét trợ cấp; không xác định điều kiện hưởng trợ cấp.',
    'Cơ quan nhà nước; AI xếp hạng hồ sơ và kết quả dùng trực tiếp cho quyết định hành chính.',
    'Chưa rõ thuộc danh mục rủi ro cao; điều kiện đánh giá tác động theo căn cứ trực tiếp đã được xác lập.',[
    P('Thuộc diện đánh giá tác động do kết quả làm căn cứ trực tiếp quyết định hành chính; người đứng đầu tổ chức lập và phê duyệt báo cáo trước sử dụng, chịu trách nhiệm trung thực và đầy đủ.', 'N20.1.b N20.7.b N20.4'),
    P('Báo cáo phải công khai trừ phần bí mật nhà nước, bí mật kinh doanh hoặc dữ liệu cá nhân.', 'N20.5|L27.4'),
    P('Áp dụng Khung đạo đức để nhận diện, giảm thiên lệch dữ liệu, mô hình và vận hành, xem xét đầy đủ tác động lên nhóm dễ bị tổn thương.', 'T1.2 T3.2.b'),
    P('AI không thay thế thẩm quyền, trách nhiệm quyết định; người ra quyết định chịu trách nhiệm xem xét và sử dụng kết quả.', 'L27.2|N20.6')],broad=True,
    d4='Quy trình phê duyệt báo cáo của người đứng đầu ở N20.4 và yêu cầu cụ thể về ba nguồn thiên lệch, nhóm dễ bị tổn thương ở T3.2.b cần kết hợp; Luật chỉ nguyên tắc chung.')

add('A06',1,'HOLDOUT_TEST','museum_synthetic_culture',
    'Bảo tàng tư nhân sẽ mở triển lãm dùng AI tái hiện giọng nói và hình ảnh nhân vật lịch sử có thật. Chúng tôi chủ động áp dụng Khung đạo đức quốc gia và muốn chuẩn bị cách đưa tác phẩm đến công chúng cho phù hợp.',
    'Gắn nhãn tác phẩm tái hiện người thật, truyền thông không gây nhầm lẫn, văn hóa và trách nhiệm tiếp nhận khiếu nại theo Khung tự nguyện; không giải quyết quyền hình ảnh hay bản quyền ngoài corpus.',
    'Bảo tàng tư nhân; công bố tác phẩm ra công chúng; mô phỏng người thật; chủ động áp dụng Khung đạo đức.',
    'Chưa có thông tin về sự đồng ý của nhân vật hoặc người thừa kế; loại trừ kết luận quyền hình ảnh.',[
    P('Bên đưa tác phẩm ra công chúng phải gắn nhãn cho hình ảnh/giọng nói mô phỏng người thật; có thể bố trí phù hợp tác phẩm ở mở đầu, kết thúc, danh đề, mô tả hoặc tài liệu kèm, nhưng phải giúp nhận biết rõ nguồn gốc.', 'N18.2.a N18.6'),
    P('Theo Khung được tự nguyện áp dụng, thiết kế phù hợp chuẩn mực và bản sắc văn hóa Việt Nam, không tạo nội dung kỳ thị hoặc ảnh hưởng lợi ích cộng đồng.', 'T1.3 T3.3.d'),
    P('Theo Khung tự nguyện, phân định trách nhiệm trong vòng đời và có đầu mối tiếp nhận, xử lý khiếu nại, khắc phục hậu quả.', 'T1.3 T3.4.b')],broad=True,
    d4='Phương thức nhãn dành cho tác phẩm ở N18.6 và quản trị văn hóa/đầu mối khiếu nại cụ thể ở T3.3.d, T3.4.b không có gói đơn tài liệu thay thế.')

add('A07',1,'HOLDOUT_TEST','open_source_marking',
    'Nhóm tôi phát hành miễn phí hệ thống AI tạo video, còn các cửa hàng dùng nó để làm video quảng cáo công khai. Chúng tôi định cung cấp tài liệu cấu hình đánh dấu thay vì bật sẵn tính năng. Nên tổ chức trách nhiệm giữa hai bên thế nào?',
    'Cơ chế đáp ứng nghĩa vụ đánh dấu với hệ thống miễn phí; trách nhiệm bên triển khai; duy trì chức năng và bảo vệ dấu hiệu bắt buộc, không mở rộng sang luật quảng cáo.',
    'Nhóm phát hành hệ thống miễn phí; đầu ra video; cửa hàng cung cấp nội dung công cộng; tài liệu cho phép cấu hình/vận hành đánh dấu.',
    'Chưa rõ video mô phỏng người thật hoặc gây nhầm lẫn; không kết luận nghĩa vụ nhãn hiển thị cho từng video.',[
    P('Nhà cung cấp hệ thống miễn phí có thể đáp ứng nghĩa vụ bằng công bố công khai tài liệu/công cụ/cấu hình/API cho phép bên triển khai cấu hình và vận hành đánh dấu, thay cho tích hợp sẵn.', 'N17.5'),
    P('Bên triển khai sử dụng cách này để cung cấp nội dung ra công cộng phải áp dụng giải pháp đánh dấu đầu ra.', 'N17.5.b'),
    P('Nhà cung cấp phải duy trì chức năng đánh dấu trong tạo, xuất, cung cấp nội dung trong phạm vi hệ thống kiểm soát.', 'N17.4'),
    P('Không được tẩy xóa, làm sai lệch thông tin, nhãn hoặc cảnh báo bắt buộc trong hoạt động AI.', 'L7.5')],broad=True,
    d4='N17.5 quy định riêng cơ chế miễn phí và phân công; L7.5 quy định hành vi cấm phá bỏ dấu hiệu bắt buộc. Nghị định không chứa đầy đủ lệnh cấm này.')

add('A08',1,'HOLDOUT_TEST','significant_integration',
    'Hệ thống AI rủi ro cao do công ty tôi cung cấp đã được đánh giá sự phù hợp. Chúng tôi sắp tích hợp mô hình của đối tác và nguồn dữ liệu mới, có thể ảnh hưởng đáng kể độ tin cậy. Nên chuẩn bị việc đưa phiên bản này vào vận hành thế nào?',
    'Đánh giá lại do thay đổi đáng kể, phối hợp thông tin mô hình bên thứ ba, cập nhật hồ sơ kỹ thuật và nhật ký, duy trì công khai kết quả; không kết luận cấp độ mới khi chưa đủ dữ kiện.',
    'Nhà cung cấp rủi ro cao; đã đánh giá; thay đổi mô hình và nguồn dữ liệu có ảnh hưởng đáng kể độ tin cậy.',
    'Chưa rõ phân loại mới và diện chứng nhận; không tự suy luận.',[
    P('Thay đổi mô hình/cấu hình chủ yếu hoặc nguồn dữ liệu ảnh hưởng đáng kể độ tin cậy, kết quả vận hành hoặc rủi ro là căn cứ đánh giá lại sự phù hợp.', 'N13.1.b N13.1.c'),
    P('Nhà cung cấp tích hợp mô hình bên khác phải thỏa thuận phối hợp cung cấp thông tin kỹ thuật cần thiết cho minh bạch và giải trình.', 'N16.6'),
    P('Nhà cung cấp rủi ro cao phải cập nhật, lưu hồ sơ kỹ thuật và nhật ký ở mức cần thiết cho đánh giá và hậu kiểm; cung cấp tương xứng, không làm lộ bí mật kinh doanh.', 'L14.1.c'),
    P('Duy trì sự phù hợp và cập nhật công khai kết quả đánh giá lại trên cổng một cửa.', 'N13.6')],broad=True,
    d4='Thỏa thuận thông tin mô hình bên thứ ba ở N16.6 và nghĩa vụ hồ sơ kỹ thuật/nhật ký không giới hạn ở sự cố tại L14.1.c cần hai tài liệu; N12.6 chỉ là hồ sơ phân loại.')

add('A09',1,'HOLDOUT_TEST','public_energy_design',
    'Đơn vị công lập đang thiết kế dịch vụ công có AI, dự kiến vận hành hạ tầng trong mạng lưới AI quốc gia và phải chọn giữa các phương án có mức tiêu thụ tài nguyên rất khác nhau. Chúng tôi muốn đưa trách nhiệm môi trường và lợi ích xã hội vào kế hoạch triển khai.',
    'Lợi ích công cộng và xử lý tác động tiêu cực, cân nhắc năng lượng toàn vòng đời, nghĩa vụ hạ tầng nếu tham gia mạng lưới quốc gia; không tính phát thải định lượng.',
    'Đơn vị cung cấp dịch vụ công; dự định vận hành hạ tầng trong mạng lưới AI quốc gia.',
    'Chưa có đo lường tiêu thụ hay tiêu chuẩn định lượng.',[
    P('Khung đạo đức áp dụng cho AI phục vụ dịch vụ công; xác định lợi ích công cộng và có phương án xử lý tác động tiêu cực trước triển khai.', 'T1.2 T3.3.a'),
    P('Xem xét năng lượng, tài nguyên tính toán, tác động môi trường suốt vòng đời; ưu tiên giải pháp kỹ thuật, hạ tầng, quy trình tiết kiệm năng lượng và hạn chế phát thải.', 'T3.3.c'),
    P('Bên vận hành hạ tầng trong mạng lưới quốc gia phải triển khai giải pháp giảm phát thải và không đe dọa an toàn hệ thống điện quốc gia.', 'N29.2.đ')],broad=True,
    d4='T3.3.c quy định cân nhắc toàn vòng đời và T3.3.a phương án lợi ích xã hội; N29.2.đ có giới hạn riêng an toàn hệ thống điện. Không tài liệu đơn lẻ đủ cả phạm vi.')

add('A10',1,'HOLDOUT_TEST','accessible_public_interface',
    'Chúng tôi làm giao diện AI cho một dịch vụ công mà người cao tuổi và người ở vùng kết nối kém cũng phải dùng. Đơn vị muốn xây dựng cách đưa dịch vụ vào sử dụng để người dân hiểu đúng khả năng của nó và còn có chỗ phản ánh khi gặp trở ngại.',
    'Khả năng tiếp cận, giới hạn hệ thống, đầu mối phản ánh và kế hoạch dự phòng; không ấn định chuẩn UI hoặc SLA bên ngoài corpus.',
    'Nhà phát triển/triển khai AI phục vụ dịch vụ công; người dùng cao tuổi và vùng khó tiếp cận.',
    'Không xác định rủi ro cao hay dùng AI làm căn cứ quyết định hành chính; không gán nghĩa vụ báo cáo tác động chỉ từ giao diện.',[
    P('Ưu tiên giao diện dễ tiếp cận, dễ sử dụng và thu hẹp khoảng cách số giữa vùng miền, nhóm dân cư.', 'T1.2 T3.3.b'),
    P('Thông báo sử dụng AI và thông tin hợp lý về mục tiêu, phạm vi, cách hoạt động tổng quát, giới hạn; không gây hiểu nhầm năng lực.', 'T3.2.c'),
    P('Xây dựng cơ chế tiếp nhận phản ánh, phát hiện lỗi và khắc phục, có phương án dự phòng khi sai lệch hoặc lạm dụng.', 'T3.1.d'),
    ],broad=True)

add('A11',1,'HOLDOUT_TEST','legacy_education_portal',
    'Trường công của tôi đã dùng AI trong giáo dục từ tháng 2/2026. Chúng tôi muốn lên kế hoạch chuyển sang tuân thủ quy định mới; giả sử cổng một cửa về AI vẫn chưa được công bố vận hành thì xử lý việc thông báo và công khai thế nào?',
    'Thời hạn chuyển tiếp hệ thống giáo dục trước hiệu lực, quyền yêu cầu dừng nếu nguy cơ nghiêm trọng, phương thức thông báo/công khai khi cổng chưa vận hành, hiệu lực Khung cho dịch vụ công.',
    'Trường công; AI giáo dục hoạt động 2/2026 trước 1/3/2026; giả định cổng chưa công bố chính thức.',
    'Chưa rõ mức rủi ro nên chỉ hướng dẫn phương thức khi có nghĩa vụ thông báo/công khai, không tuyên bố mọi hệ thống phải thông báo.',[
    P('Hệ thống giáo dục hoạt động trước hiệu lực Luật có thời hạn 18 tháng kể từ 1/3/2026 để tuân thủ; vẫn có thể bị cơ quan quản lý yêu cầu dừng/chấm dứt khi nguy cơ gây thiệt hại nghiêm trọng.', 'L34 L35.1.a L35.2'),
    P('Khi thuộc thủ tục thông báo/báo cáo mà cổng chưa vận hành, dùng phương thức do Bộ KH&CN công bố với giá trị tương đương.', 'N46.1',condition=('conditional','unknown','Nghĩa vụ thông báo cụ thể phụ thuộc phân loại; nhánh thủ tục được hỏi dưới giả định cổng chưa vận hành.')),
    P('Trong giai đoạn này, công khai thông tin thuộc nghĩa vụ trên cổng/trang điện tử chính thức của đơn vị chịu trách nhiệm công khai, trừ quy định khác.', 'N46.2',condition=('conditional','unknown','Chỉ áp dụng nếu phát sinh nghĩa vụ công khai theo Nghị định.')),
    P('Khung đạo đức áp dụng cho AI phục vụ dịch vụ công; Thông tư có hiệu lực từ 10/3/2026.', 'T1.2 T4')],broad=True,
    d4='Thời hạn chuyển tiếp giáo dục chỉ ở L35.1.a, phương thức dự phòng cổng chỉ ở N46.1–2; hiệu lực Thông tư ở T4. Cần ba tài liệu cho toàn tác vụ.')

add('A12',1,'HOLDOUT_TEST','harm_without_operator_fault',
    'Doanh nghiệp tôi thuê hệ thống AI rủi ro cao để vận hành dịch vụ. Chúng tôi muốn chuẩn bị cơ chế xử lý thiệt hại ngay cả khi đã vận hành đúng, đồng thời bố trí việc phát hiện nguy cơ và phối hợp với bên bán trước khi có tổn thất.',
    'Trách nhiệm bồi thường dù vận hành đúng, điều kiện miễn trừ/hoàn trả, phản ứng phòng ngừa của bên triển khai; không tính số tiền hay thủ tục khởi kiện.',
    'Doanh nghiệp là bên triển khai hệ thống rủi ro cao; tình huống giả định đã vận hành đúng nhưng phát sinh thiệt hại.',
    'Chưa có thỏa thuận hoàn trả, lỗi người bị thiệt hại hay tình thế cụ thể; phải bảo lưu điều kiện.',[
    P('Bên triển khai phải bồi thường khi hệ thống rủi ro cao vận hành đúng vẫn gây thiệt hại; yêu cầu bên cung cấp/phát triển/liên quan hoàn trả sau bồi thường nếu có thỏa thuận.', 'L29.2'),
    P('Miễn trừ theo nhánh thiệt hại hoàn toàn do lỗi cố ý người bị thiệt hại hoặc bất khả kháng/tình thế cấp thiết, với ngoại lệ pháp luật được nêu; không tự coi đã có miễn trừ.', 'L29.3',condition=('conditional','unknown','Chưa có dữ kiện xác lập miễn trừ; chỉ nêu các nhánh điều kiện.')),
    P('Khi phát hiện nguy cơ gây thiệt hại nghiêm trọng, bên triển khai kịp thời hạn chế rủi ro trong quyền kiểm soát và thông báo nhà cung cấp, cơ quan có thẩm quyền.', 'N15.6')],broad=True,
    d4='L29 quy định phân bổ bồi thường/miễn trừ; N15.6 yêu cầu phản ứng đối với nguy cơ và hai nơi thông báo. Không đồng nhất nguy cơ với sự cố đã xảy ra.')

add('A13',1,'RESERVE_DEV','research_integrity',
    'Nhóm nghiên cứu của viện muốn dùng dữ liệu trong cơ sở dữ liệu AI quốc gia để thử mô hình hỗ trợ công bố khoa học. Nên chuẩn bị việc sử dụng dữ liệu và công bố kết quả thế nào?',
    'Truy cập dữ liệu đúng phạm vi, nghĩa vụ không làm sai lệch/xâm phạm quyền, liêm chính nghiên cứu; không xin cấp quyền bản quyền cụ thể.',
    'Viện nghiên cứu; khai thác cơ sở dữ liệu AI; mục đích nghiên cứu và công bố.',
    'Điều kiện truy cập của bộ dữ liệu cụ thể chưa cung cấp.',[
    P('Khai thác khi đáp ứng điều kiện truy cập, mục đích và phạm vi được công bố hoặc thỏa thuận; không mặc định dữ liệu quốc gia đều mở.', 'N35.1'),
    P('Sử dụng đúng điều kiện; không làm sai lệch dữ liệu hoặc xâm phạm quyền sở hữu dữ liệu, sở hữu trí tuệ và lợi ích hợp pháp.', 'N35.5'),
    P('Ứng dụng AI trong nghiên cứu phải bảo đảm liêm chính, đạo đức và phòng ngừa gian lận, đạo văn khi nghiên cứu/công bố.', 'L6.3')],broad=True,
    d4='Quy tắc truy cập chi tiết N35 và liêm chính khoa học L6.3 bổ sung nhau.',
    control=None)

add('A14',1,'RESERVE_TEST','open_research_support',
    'Nhóm tôi muốn chia sẻ mô hình tiếng dân tộc thiểu số để cộng đồng nghiên cứu dùng lại, đồng thời tìm hỗ trợ hạ tầng. Chúng tôi tự nguyện theo Khung đạo đức và cần xây dựng phương án chia sẻ có trách nhiệm.',
    'Nghiên cứu mở với quyền sở hữu trí tuệ, điều kiện hỗ trợ phi tài chính và bảo toàn quyền tài nguyên; không định lượng hỗ trợ.',
    'Nhóm nghiên cứu chia sẻ mô hình tiếng dân tộc thiểu số; chọn áp dụng Khung tự nguyện.',
    'Nguồn lực chương trình và mức độ hoàn thiện mô hình chưa biết.',[
    P('Khung khuyến khích nghiên cứu mở, chia sẻ tri thức phù hợp pháp luật và bảo vệ sở hữu trí tuệ.', 'T1.3 T3.4.a'),
    P('Chia sẻ hợp pháp được xem xét hỗ trợ trong nguồn lực, theo quy mô, khả năng sử dụng, mức sẵn có và đóng góp cho ngôn ngữ/lợi ích công cộng; không bảo đảm được cấp.', 'N33.1 N33.3'),
    P('Hỗ trợ là phi tài chính, không quy đổi tiền và không tự thay đổi quyền sở hữu, sở hữu trí tuệ, khai thác hợp pháp tài nguyên.', 'N33.2.c N33.4')],broad=True)

add('A15',1,'RESERVE_DEV','exclusive_defence',
    'Hệ thống AI của đơn vị tôi chỉ phục vụ quốc phòng, không có mục đích dân sự. Có phải đưa hoạt động này vào phạm vi Luật Trí tuệ nhân tạo không?',
    'Chỉ xác định ngoại lệ phạm vi của Luật, không kết luận miễn trừ các luật khác.',
    'Mục đích duy nhất quốc phòng; không mục đích dân sự.', 'Không cần thông tin bổ sung cho phạm vi hẹp.',[
    P('Hoạt động AI chỉ phục vụ quốc phòng, an ninh, cơ yếu không thuộc phạm vi Luật này.', 'L1.2')],
    control='Ngoại lệ phạm vi minh thị, một khoản đủ.')

# Family 2: multi-duty procedural synthesis.
add('B01',2,'DEV','small_sandbox_entry',
    'Doanh nghiệp nhỏ của tôi có thử nghiệm AI cấp độ 1 tại một tỉnh, không thuộc cơ chế thử nghiệm chuyên ngành. Hồ sơ đã đủ điều kiện hợp lệ. Chúng tôi muốn dùng hồ sơ rút gọn và biết cách nộp, thời gian xử lý cũng như hỗ trợ kỹ thuật có thể tiếp cận.',
    'Hồ sơ rút gọn cho doanh nghiệp nhỏ cấp 1, kênh nộp/thẩm quyền/thời hạn, hỗ trợ tư vấn và kiểm thử; không tái phân loại hoặc mô tả hồ sơ thông thường.',
    'Doanh nghiệp nhỏ; cấp 1; một tỉnh; hồ sơ hợp lệ; không thuộc cơ chế chuyên ngành.',
    'Không yêu cầu cam kết mức tài trợ hay nội dung biểu mẫu phụ lục.',[
    P('Hồ sơ rút gọn gồm đơn đề nghị theo mẫu tổ chức và mô tả khái quát hệ thống, rủi ro chính, biện pháp giảm thiểu.', 'N24.3'),
    P('Nộp một bộ điện tử qua cổng Dịch vụ công quốc gia; cấp tỉnh xử lý cấp 1 trong một tỉnh, ban hành giấy hoặc từ chối trong tối đa 10 ngày làm việc với hồ sơ hợp lệ.', 'N23.2 N23.3.a N23.5.a'),
    P('Doanh nghiệp tham gia sandbox được hỗ trợ tư vấn kỹ thuật, đánh giá rủi ro, kiểm thử an toàn và kết nối cơ sở thử nghiệm/kiểm định theo pháp luật.', 'L25.4')],
    d4='N24.3/N23 cung cấp thủ tục rút gọn và mốc xử lý; L25.4 có quyền hỗ trợ tư vấn/kết nối cho doanh nghiệp sandbox. N26 chỉ hỗ trợ chi phí qua phiếu, không thay đầy đủ quyền hỗ trợ này.')

add('B02',2,'DEV','sandbox_voucher_settlement',
    'Doanh nghiệp đã được chấp thuận sandbox muốn dùng Phiếu hỗ trợ để thanh toán dịch vụ kiểm thử an toàn. Chúng tôi cần chuẩn bị căn cứ chi phí và cách thanh toán thế nào, có được nhận toàn bộ chi phí bằng tiền rồi trả nhà cung cấp không?',
    'Chi phí trực tiếp trong phạm vi thử nghiệm, trần hỗ trợ sandbox, chứng từ, thanh toán nhà cung cấp, không chuyển thành tiền cho bên nhận.',
    'Doanh nghiệp sandbox đã chấp thuận; dịch vụ kiểm thử an toàn; hỏi thanh toán qua phiếu.',
    'Chưa có giá trị phiếu, hạn mức nguồn lực hoặc tổng chi phí.',[
    P('Hỗ trợ chỉ cho chi phí trực tiếp trong phạm vi thử nghiệm được chấp thuận, đồng chi trả và không trùng lặp; tối đa 50% chi phí hợp lệ thực tế đối với dịch vụ nêu trong khoản.', 'N26.2 N26.3.c'),
    P('Chi phí phải có hợp đồng, hóa đơn/chứng từ hợp pháp, tuân thủ kế toán/thuế/ngân sách; thanh toán căn cứ dịch vụ thực tế và dữ liệu đối soát.', 'N26.4 N26.5'),
    P('Phiếu không quy đổi tiền, không chuyển nhượng; thanh toán trực tiếp cho bên cung cấp dịch vụ, không qua đối tượng được cấp phiếu.', 'N40.3.c N40.8')],
    control='Loại trừ nhận tiền mặt hoặc hoàn toàn bộ chi phí chỉ vì có phiếu; điều khoản cấm quy đổi trực tiếp áp dụng, không gán nhãn not_applicable cho điều khoản này.')

add('B03',2,'DEV','public_change_training',
    'Cơ quan nhà nước đang dùng kết quả AI làm căn cứ trực tiếp cho quyết định hành chính và đổi nguồn dữ liệu đầu vào chủ yếu làm phát sinh rủi ro mới. Chúng tôi phải xử lý báo cáo tác động trước khi dùng tiếp ra sao, và cần chuẩn bị năng lực cho cán bộ vận hành thế nào?',
    'Đánh giá tác động bổ sung trước sử dụng tiếp, trách nhiệm phê duyệt/chất lượng báo cáo, đào tạo rủi ro đạo đức và kỹ năng an toàn; không làm báo cáo thay cơ quan.',
    'Cơ quan nhà nước; AI làm căn cứ trực tiếp quyết định hành chính; thay đổi dữ liệu chủ yếu phát sinh rủi ro mới.',
    'Không có nội dung báo cáo hay lớp đào tạo cụ thể.',[
    P('Cơ quan triển khai phải đánh giá tác động bổ sung trước tiếp tục dùng khi thay đổi dữ liệu đầu vào chủ yếu phát sinh rủi ro mới.', 'N20.1.b N20.2'),
    P('Người đứng đầu tổ chức lập, phê duyệt và chịu trách nhiệm về tính trung thực, đầy đủ của báo cáo; bảo lưu mốc trước khi sử dụng trong phạm vi quy định.', 'N20.4'),
    P('Khung áp dụng cho dịch vụ/quản lý nhà nước; chú trọng đào tạo nhận thức, rủi ro đạo đức và kỹ năng AI an toàn cho cán bộ, người lao động.', 'T1.2 T3.4.c')],
    d4='Thủ tục bổ sung N20.2 và nội dung năng lực đạo đức T3.4.c không có phương án đơn tài liệu đầy đủ.')

add('B04',2,'DEV','voluntary_support_information',
    'Tôi chia sẻ hợp pháp một bộ dữ liệu và muốn xin hỗ trợ phi tài chính. Nếu cung cấp thông tin trên cổng thì nên chuẩn bị gì? Có phải dùng mẫu đó mới được xét và sau đó phải báo cáo định kỳ không?',
    'Thông tin tài nguyên/quyền/nhu cầu, tính tự nguyện của mẫu và việc cung cấp, cách xác định hỗ trợ và nghĩa vụ sử dụng đúng mục đích; không suy diễn thủ tục bắt buộc.',
    'Cá nhân chia sẻ dữ liệu hợp pháp; muốn hỗ trợ phi tài chính.',
    'Chưa có tiêu chí chương trình hay nguồn lực đã công bố.',[
    P('Thông tin gồm mô tả tài nguyên và phạm vi dùng, quyền sở hữu/sử dụng hợp pháp cùng cam kết tuân thủ, nhu cầu loại tài nguyên/mục đích/quy mô/thời gian.', 'N34.2'),
    P('Cung cấp thông tin và dùng mẫu đều tự nguyện, không là điều kiện xét hỗ trợ hoặc thủ tục hành chính bắt buộc.', 'N34.1 N34.6'),
    P('Bộ xác định mức/hình thức theo tiêu chí và nguồn lực rồi thông báo điện tử phạm vi, thời hạn, điều kiện; dùng đúng mục đích, cung cấp kết quả khi cần, không phát sinh chế độ báo cáo định kỳ.', 'N34.3 N34.4 N34.5')],
    control='Ngoại lệ rõ về mẫu bắt buộc và báo cáo định kỳ.',
    negative=('N25.2','not_applicable','unmet','Báo cáo định kỳ sandbox không chuyển thành nghĩa vụ của người chỉ chia sẻ để nhận hỗ trợ phi tài chính.'))

add('B05',2,'HOLDOUT_TEST','foreign_assessment_recognition',
    'Nhà cung cấp chúng tôi có hệ thống AI rủi ro cao được một tổ chức nước ngoài đánh giá. Cơ quan có thẩm quyền đã thừa nhận một phần kết quả. Trước khi đưa vào dùng tại Việt Nam, phần còn lại và việc công khai, lưu hồ sơ kỹ thuật phải làm ra sao?',
    'Dùng kết quả được thừa nhận trong phạm vi tương ứng, bổ sung phần còn lại, công khai kết quả, nghĩa vụ hồ sơ/nhật ký; không giải thích thủ tục thừa nhận ở luật khác.',
    'Nhà cung cấp; rủi ro cao; đánh giá nước ngoài; chỉ một phần được thừa nhận.',
    'Chưa biết danh sách nội dung đã đánh giá; kết luận phải giới hạn phạm vi tương ứng.',[
    P('Được dùng kết quả nước ngoài đã thừa nhận cho nội dung tương ứng; nội dung chưa đánh giá hoặc chưa thừa nhận phải tiếp tục đánh giá theo Nghị định.', 'N13.5'),
    P('Trước sử dụng phải công khai thông tin kết quả trên cổng, gồm nhận diện hệ thống/nhà cung cấp, phương thức, tổ chức khi có, kết luận, thời điểm hoàn thành/thừa nhận và cập nhật.', 'N13.6'),
    P('Nhà cung cấp rủi ro cao lập, cập nhật, giữ hồ sơ kỹ thuật và nhật ký cần thiết phục vụ đánh giá/hậu kiểm; cung cấp tương xứng và bảo vệ bí mật kinh doanh.', 'L14.1.c')],
    d4='N13.5–6 quy định thừa nhận một phần và trường công khai; L14.1.c quy định hồ sơ/nhật ký thường xuyên, không chỉ hồ sơ phân loại hoặc nhật ký sự cố.')

add('B06',2,'HOLDOUT_TEST','significant_integration',
    'Bên vận hành chúng tôi tích hợp hệ thống AI đã mua vào môi trường mới và phát sinh rủi ro cao hơn. Việc rà soát đã hoàn thành và kết luận chuyển từ trung bình sang cao. Ai phải phối hợp làm lại phân loại, khi nào thông báo và có được chờ thông báo xong mới áp dụng biện pháp an toàn mới không?',
    'Phân công bên triển khai/nhà cung cấp khi tích hợp gây rủi ro cao hơn, thông báo sau rà soát và áp dụng ngay quản lý rủi ro mới; không xác định thời gian chuyển tiếp N11.5 có dẫn chiếu bất nhất.',
    'Bên triển khai tích hợp môi trường mới; rà soát hoàn thành; kết quả mức rủi ro tăng từ trung bình lên cao.',
    'Chưa rõ thời điểm quyết định danh mục; không áp mốc chuyển tiếp 12 tháng.',[
    P('Bên triển khai phối hợp nhà cung cấp rà soát/phân loại lại khi tích hợp phát sinh rủi ro mới hoặc cao hơn.', 'N11.2|L10.2|N6.4'),
    P('Nhà cung cấp, bên triển khai thông báo kết quả tăng mức rủi ro trong 15 ngày làm việc từ ngày hoàn thành rà soát.', 'N11.3.a'),
    P('Biện pháp quản lý rủi ro tương ứng mức mới phải áp dụng ngay, không chờ hoàn tất thông báo.', 'N11.3.a')])

add('B07',2,'HOLDOUT_TEST','asset_incident_deadlines',
    'AI của công ty gây thiệt hại tài sản đáng kể nhưng không có thương vong, gián đoạn dịch vụ thiết yếu hay xâm phạm quyền không thể kiểm soát. Chúng tôi đã có căn cứ ban đầu xác nhận sự cố và khả năng cao do lỗi AI. Cần lập lịch báo cáo và giữ tài liệu thế nào; nộp báo cáo có đồng nghĩa nhận lỗi không?',
    'Báo cáo sơ bộ nhánh sự cố nghiêm trọng còn lại, thời điểm xác nhận, hiệu lực không nhận lỗi, nhật ký và báo cáo chính thức; không tính thiệt hại.',
    'Nhà cung cấp doanh nghiệp; thiệt hại tài sản đáng kể; loại trừ nhánh khẩn cấp đã nêu; đã đủ thông tin xác nhận.',
    'Nguyên nhân kỹ thuật cuối cùng chưa xác định; không cần chờ điều tra toàn diện.',[
    P('Sự cố tài sản đáng kể thuộc nghiêm trọng; nhánh còn lại báo cáo sơ bộ trong 05 ngày làm việc từ xác nhận qua cổng, mẫu dành cho tổ chức.', 'N19.1.b N19.3.b'),
    P('Xác nhận dựa trên thông tin ban đầu đủ về sự cố và khả năng cao lỗi AI, không chờ điều tra toàn diện; báo cáo đúng hạn không là thừa nhận lỗi kỹ thuật hay trách nhiệm pháp lý.', 'N19.3.c'),
    P('Nhà cung cấp và bên triển khai giữ nhật ký/dữ liệu/thông tin sự cố; gửi báo cáo chính thức kết quả khắc phục trong 15 ngày từ nộp sơ bộ.', 'N19.4')])

add('B08',2,'HOLDOUT_TEST','data_operator_access',
    'Đơn vị tôi quản lý cơ sở dữ liệu phục vụ AI và cho các nhóm nghiên cứu huấn luyện mô hình ngay trong môi trường của mình. Cần tổ chức kiểm soát truy cập và phân công trách nhiệm với nhóm khai thác thế nào, nhất là nguy cơ nhận dạng lại dữ liệu đã khử nhận dạng?',
    'Môi trường khai thác an toàn không đổi quyền sở hữu; quản lý và theo dõi truy cập; nghĩa vụ người khai thác và nguy cơ tái nhận dạng.',
    'Đơn vị quản lý cơ sở dữ liệu AI; cung cấp môi trường huấn luyện tại hạ tầng mình; dữ liệu đã khử nhận dạng.',
    'Không biết cơ chế khử nhận dạng cụ thể; không kết luận dữ liệu an toàn tuyệt đối.',[
    P('Có thể tổ chức môi trường xử lý/huấn luyện trên hạ tầng cơ quan quản lý mà không làm thay đổi quyền sở hữu dữ liệu.', 'N35.3.c'),
    P('Bên quản lý thiết lập quản lý truy cập, ghi nhận/theo dõi khai thác, kiểm soát đúng mục đích/phạm vi và biện pháp an toàn dữ liệu.', 'N35.4'),
    P('Bên khai thác dùng đúng điều kiện, không làm sai lệch hoặc dùng trái pháp luật, không xâm phạm quyền tài sản dữ liệu/sở hữu trí tuệ và lợi ích liên quan.', 'N35.5'),
    P('Bên quản lý phải phòng ngừa, kiểm soát nguy cơ tái nhận dạng dữ liệu cá nhân đã khử nhận dạng và khai thác điểm yếu mô hình.', 'N36.1 N36.3.c')])

add('B09',2,'HOLDOUT_TEST','third_party_brand_provider',
    'Chúng tôi đóng gói mô hình của bên khác thành dịch vụ AI mang thương hiệu mình, đã phân loại trung bình. Khi lập hồ sơ phân loại, chúng tôi không có quyền truy cập dữ liệu huấn luyện thô của đối tác. Có thể dùng tài liệu kỹ thuật quốc tế và cần thỏa thuận gì với đối tác?',
    'Tư cách nhà cung cấp, giới hạn thông tin có quyền tiếp cận, dùng tài liệu tương đương đáp ứng đầy đủ và phối hợp thông tin mô hình; không suy diễn bắt buộc công khai bí mật.',
    'Doanh nghiệp đưa hệ thống dưới thương hiệu mình; mô hình bên thứ ba; trung bình; không quyền truy cập dữ liệu thô.',
    'Chưa có tài liệu cụ thể để xác nhận đủ nội dung; chỉ trả lời điều kiện chấp nhận.',[
    P('Dùng mô hình bên thứ ba không loại tư cách nhà cung cấp khi hệ thống đưa ra dưới thương hiệu mình.', 'L3.4'),
    P('Chỉ phải cung cấp thông tin kỹ thuật/dữ liệu trong quyền tiếp cận, kiểm soát hợp pháp; hồ sơ không bắt buộc tiết lộ dữ liệu huấn luyện thô/bí mật, trừ quy định khác.', 'N12.3 N12.4'),
    P('Được dùng tài liệu mô hình/tài liệu tương đương theo tiêu chuẩn quốc tế nếu đáp ứng đầy đủ nội dung hồ sơ theo Nghị định.', 'N12.5'),
    P('Phải thỏa thuận với bên cung cấp mô hình để phối hợp thông tin kỹ thuật cần cho minh bạch, giải trình.', 'N16.6')],
    d4='Tư cách thương hiệu tại L3.4 không được định nghĩa lại trong Nghị định; N12.3–5 và N16.6 thêm giới hạn/thủ tục cụ thể chưa có đầy đủ ở Luật.')

add('B10',2,'HOLDOUT_TEST','film_label_handoff',
    'Xưởng của tôi dùng AI mô phỏng giọng người thật cho một bộ phim rồi giao bản dựng cho đơn vị phát hành. Hợp đồng định để bên phát hành lo nhãn. Khi giao và phát hành tác phẩm, hai bên phải phối hợp thế nào để thông tin AI không bị mất?',
    'Trách nhiệm cung cấp thông tin trong khâu sản xuất, bên công bố gắn nhãn, vị trí nhãn phù hợp và duy trì minh bạch; không đánh giá hợp đồng dân sự.',
    'Xưởng sản xuất nội dung AI; đơn vị khác trực tiếp đưa phim ra công cộng; mô phỏng giọng người thật.',
    'Chưa có hợp đồng chi tiết, không giải thích phân bổ trách nhiệm ngoài quy định.',[
    P('Bên tạo/chỉnh sửa trong sản xuất phải cung cấp thông tin cần thiết; bên trực tiếp đưa tác phẩm ra công cộng thực hiện thông báo/gắn nhãn dựa trên thông tin nhận.', 'N18.6'),
    P('Giọng người thật bị mô phỏng thuộc trường hợp gắn nhãn dễ nhận biết; với phim có thể dùng mở đầu/kết thúc/danh đề/mô tả/tài liệu phù hợp nhưng phải nhận biết nguồn gốc, không gây nhầm lẫn.', 'N18.2.a N18.6'),
    P('Nhà cung cấp và bên triển khai duy trì thông tin minh bạch suốt quá trình cung cấp hệ thống/sản phẩm/nội dung; không tẩy xóa, làm sai lệch thông tin/nhãn/cảnh báo bắt buộc.', 'L11.5 L7.5')],
    d4='Phân công bàn giao nội dung phim ở N18.6 và duy trì suốt quá trình/lệnh cấm tẩy xóa ở L11.5/L7.5 cần hai tài liệu.')

add('B11',2,'HOLDOUT_TEST','recognized_cluster_training',
    'Doanh nghiệp, trường đại học và tổ chức hỗ trợ đổi mới sáng tạo của chúng tôi đã thống nhất liên kết nghiên cứu AI. Muốn được công nhận cụm liên kết để tiếp cận hạ tầng và đào tạo nhân lực thì phải chuẩn bị hồ sơ, cơ chế điều phối và quyền lợi sau công nhận ra sao?',
    'Tiêu chí phối hợp, hồ sơ/kênh/thời hạn công nhận, hỗ trợ hạ tầng/đào tạo và tư cách độc lập thành viên; không bảo đảm mức tài trợ.',
    'Có doanh nghiệp, đại học và tổ chức hỗ trợ; hợp tác nghiên cứu AI; xin công nhận cụm.',
    'Chưa rõ đã có quy chế văn bản và đầu mối; phải hoàn thiện tiêu chí, không khẳng định đương nhiên đủ.',[
    P('Cần mục tiêu AI, hợp tác ít nhất hai nhóm theo quy định, văn bản thống nhất cơ chế lợi ích/trách nhiệm, đầu mối và phương thức điều phối.', 'N39.1'),
    P('Tổ chức đại diện nộp bộ hồ sơ điện tử qua Dịch vụ công quốc gia gồm văn bản đề nghị, thành viên, văn bản hợp tác/quy chế/đề án và chứng minh tiêu chí; Bộ KH&CN giải quyết trong 15 ngày làm việc từ đủ hồ sơ hợp lệ.', 'N39.2 N39.3'),
    P('Thành viên cụm được công nhận ưu tiên hạ tầng/dữ liệu/nền tảng thử nghiệm chi phí ưu đãi và hỗ trợ tham gia đào tạo nhân lực, xúc tiến thương mại, nhiệm vụ trọng điểm.', 'L24.3'),
    P('Cụm tự nguyện, tự chủ, không thay tư cách pháp lý và quyền/nghĩa vụ độc lập thành viên, không hình thành tổ chức quản lý nhà nước nội bộ.', 'N39.4')],
    d4='Thủ tục chi tiết N39 và quyền hỗ trợ chương trình đào tạo cụ thể L24.3.b cùng cần cho ý định; N39.5 không nêu đầy đủ đào tạo/xúc tiến thương mại.')

add('B12',2,'HOLDOUT_TEST','classification_electronic_notice',
    'Nhà cung cấp đã hoàn thành hồ sơ phân loại trung bình, muốn tự động gửi thông báo qua kết nối điện tử thay vì nhập tay. Sau khi gửi thì việc cấp mã, xác nhận và yêu cầu bổ sung tài liệu được xử lý thế nào?',
    'Hình thức thông báo điện tử, nội dung theo hồ sơ, thời điểm trước sử dụng, mã/xác nhận và giới hạn đòi thêm tài liệu; không viết mã API hay tra endpoint.',
    'Nhà cung cấp trung bình; hồ sơ hoàn thành; muốn gửi tự động.',
    'Chưa có đặc tả API; không thuộc phạm vi câu hỏi pháp lý này.',[
    P('Có thể gửi tự động qua API hoặc phương thức điện tử phù hợp; thông báo trước sử dụng, nội dung tuân thủ hồ sơ phân loại.', 'N14.1 N14.2 N14.3.b'),
    P('Cổng tự ghi nhận, cấp mã hệ thống và gửi xác nhận điện tử ngay sau hoàn tất gửi.', 'N14.4'),
    P('Khi tiếp nhận không được yêu cầu thêm tài liệu/thành phần ngoài nội dung quy định; vẫn thanh tra, kiểm tra, hậu kiểm theo pháp luật.', 'N14.4')],
    control='Quy trình pháp lý gọn trong một điều; không suy ra thủ tục phê duyệt trước hoặc tài liệu bổ sung tùy ý.')

add('B13',2,'RESERVE_TEST','public_data_publication',
    'Đơn vị vận hành cơ sở dữ liệu do Nhà nước đầu tư muốn mở quyền khai thác phục vụ AI qua API. Những thông tin nào cần công bố và việc mở truy cập có làm chuyển quyền sở hữu dữ liệu cho người dùng không?',
    'Nội dung công bố, phương thức API/môi trường an toàn, quản lý mục đích và bảo toàn quyền dữ liệu.',
    'Cơ sở dữ liệu nhà nước; chuẩn bị cung cấp quyền khai thác phục vụ AI.',
    'Chưa rõ dữ liệu mở/điều kiện/thương mại; không mặc định miễn phí.',[
    P('Công bố danh mục, điều kiện/phạm vi/mục đích, yêu cầu kỹ thuật, phương thức tiếp cận và đầu mối hỗ trợ trên cổng AI, liên thông cổng dữ liệu.', 'N35.2'),
    P('Có thể cung cấp qua API hoặc môi trường khai thác an toàn trên hạ tầng quản lý mà không thay quyền sở hữu dữ liệu.', 'N35.3.a N35.3.c'),
    P('Bên quản lý kiểm soát truy cập/khai thác đúng mục đích và bên dùng không xâm phạm quyền sở hữu dữ liệu hoặc sở hữu trí tuệ.', 'N35.4.c N35.5.c')])

add('B14',2,'RESERVE_TEST','post_sandbox_transition',
    'Chúng tôi đã có giấy hoàn thành sandbox và đang vận hành chuyển tiếp trong giới hạn được duyệt. Muốn gia hạn thời gian chuyển tiếp thì phải gửi khi nào, điều kiện gì và giấy hoàn thành có thay giấy phép chuyên ngành không?',
    'Gia hạn vận hành chuyển tiếp sau hoàn thành, không phải gia hạn thời gian thử nghiệm; giấy phép chuyên ngành và nghĩa vụ cuối chuyển tiếp.',
    'Đã hoàn thành sandbox; đang vận hành chuyển tiếp trong giới hạn.',
    'Chưa biết đã khắc phục sự cố; nêu điều kiện gia hạn, không bảo đảm được duyệt.',[
    P('Đề nghị trước hết chuyển tiếp chậm nhất 15 ngày; cơ quan cấp giấy hoàn thành xem xét trong 07 ngày làm việc từ đề nghị hợp lệ, gia hạn một lần không quá 06 tháng nếu hoàn thành thử nghiệm/khắc phục và giữ biện pháp rủi ro.', 'N27.6'),
    P('Kết thúc chuyển tiếp phải hoàn thành nghĩa vụ tuân thủ trước tiếp tục cung cấp/vận hành.', 'N27.7'),
    P('Giấy hoàn thành không thay giấy phép, giấy chứng nhận, chấp thuận hoặc điều kiện kinh doanh theo luật.', 'N27.8')])

add('B15',2,'RESERVE_DEV','academic_workforce_cooperation',
    'Trường đại học và doanh nghiệp đang xây dựng chương trình thực hành AI gắn với nhu cầu sản xuất. Vai trò phối hợp đào tạo của hai bên và việc chia sẻ tri thức của trường được quy định thế nào?',
    'Phối hợp đào tạo/nghiên cứu/thực hành, chia sẻ tri thức/mạng lưới; không thiết kế chương trình hoặc điều kiện công nhận bên ngoài corpus.',
    'Đại học và doanh nghiệp tham gia phát triển nhân lực AI.',
    'Không có nội dung chương trình quốc gia hay chính sách ưu đãi chi tiết.',[
    P('Các tổ chức tham gia phát triển nhân lực được hưởng khuyến khích/ưu đãi theo pháp luật, đồng thời phối hợp đào tạo, nghiên cứu ứng dụng, thực hành gắn nhu cầu thực tiễn.', 'L23.5'),
    P('Đại học có trách nhiệm hợp tác, chia sẻ tri thức và tham gia mạng lưới quốc gia/quốc tế về đào tạo, nghiên cứu, phát triển nhân lực AI.', 'L23.6')])

# Family 3: actor / condition applicability.
add('C01',3,'DEV','personal_noncommercial',
    'Tôi dùng một ứng dụng AI để sắp xếp ảnh gia đình, hoàn toàn cá nhân và không kiếm tiền. Chỉ vì trực tiếp dùng ứng dụng thì tôi có bị coi là bên triển khai theo Luật AI không?',
    'Phân biệt người sử dụng và bên triển khai theo mục đích cá nhân phi thương mại; không kết luận miễn mọi trách nhiệm người sử dụng.',
    'Cá nhân trực tiếp tương tác; ảnh gia đình; phi thương mại.', 'Không cần thông tin bổ sung cho phân biệt vai trò này.',[
    P('Sử dụng cá nhân phi thương mại được loại khỏi khái niệm bên triển khai; người trực tiếp tương tác hoặc dùng đầu ra vẫn thuộc khái niệm người sử dụng.', 'L3.5 L3.6')],
    control='Hai định nghĩa liền kề đủ phân biệt vai trò; không tự gán nghĩa vụ bên triển khai.',
    negative=('L14.2.a','not_applicable','unmet','Người dùng cá nhân phi thương mại không là bên triển khai trong tình huống này.'))

add('C02',3,'DEV','office_medium_exception',
    'Công ty dùng AI hỗ trợ công việc văn phòng, ai cũng biết đây là công cụ AI; nó không mô phỏng danh tính hay sự kiện và đã xác định không thuộc danh mục rủi ro cao. Có phải cứ có AI là xếp trung bình không?',
    'Ngoại lệ công cụ văn phòng nhận biết rõ và phân loại thấp khi đã loại cao/trung bình; không suy luận miễn mọi nghĩa vụ AI.',
    'Công cụ văn phòng nhận biết rõ; không mô phỏng gây nhầm lẫn; đã loại danh mục cao.', 'Không cần suy đoán danh mục.',[
    P('Công cụ văn phòng có bối cảnh nhận biết rõ là AI và không mô phỏng gây nhầm lẫn thuộc ngoại lệ không phân loại trung bình; khi cũng không thuộc cao thì thuộc thấp.', 'N9.3.b N6.3.c')],
    control='Ngoại lệ phân loại hẹp có điều kiện rõ.',
    negative=('N9.1','not_applicable','unmet','Điều kiện gây nhầm lẫn không được thiết lập; ngoại lệ khoản 3.b áp dụng.'))

add('C03',3,'DEV','private_ethics_scope',
    'Cửa hàng tư nhân dùng AI chỉ để kinh doanh hàng hóa thông thường, không cung cấp dịch vụ công hay làm nhiệm vụ quản lý nhà nước. Các trách nhiệm trong Thông tư về Khung đạo đức quốc gia có bắt buộc với cửa hàng chỉ vì dùng AI không?',
    'Phạm vi áp dụng bắt buộc/khuyến khích của Thông tư; không biến khuyến khích thành miễn nghĩa vụ của Luật hoặc Nghị định.',
    'Cửa hàng tư nhân tại Việt Nam; hoạt động kinh doanh thông thường; không quản lý nhà nước/dịch vụ công.', 'Không biết rủi ro; không kết luận các nghĩa vụ theo rủi ro.',[
    P('Thông tư áp dụng cho các vai trò trong AI phục vụ quản lý nhà nước/dịch vụ công; hoạt động AI khác tại Việt Nam được khuyến khích áp dụng, không trở thành đối tượng bắt buộc chỉ vì sử dụng AI.', 'T1.2 T1.3')],
    control='Phân biệt phạm vi áp dụng và khuyến khích trong một điều.',
    negative=('T3.3.b','not_applicable','unmet','Không có căn cứ áp như nghĩa vụ bắt buộc của Thông tư cho cửa hàng ngoài dịch vụ công; vẫn có thể áp dụng tự nguyện.'))

add('C04',3,'DEV','mixed_defence_civilian',
    'Đơn vị có hệ thống AI vừa phục vụ công việc quốc phòng vừa cung cấp dịch vụ dân sự tại Việt Nam. Chúng tôi có được loại toàn bộ hoạt động khỏi Luật AI vì có mục đích quốc phòng không?',
    'Kiểm tra từ điều kiện chỉ phục vụ quốc phòng đối với hệ thống dùng chung có mục đích dân sự; không xác định quy định an ninh chuyên ngành.',
    'AI dùng cho cả quốc phòng và dịch vụ dân sự tại Việt Nam.', 'Không có kiến trúc tách thành các hệ thống riêng; không giả định chia được phạm vi.',[
    P('Ngoại lệ chỉ dành cho hoạt động AI chỉ phục vụ quốc phòng/an ninh/cơ yếu; dữ kiện có hoạt động dân sự không cho phép viện ngoại lệ đó để loại toàn bộ hoạt động, trong khi hoạt động AI tại Việt Nam thuộc phạm vi chung.', 'L1.1 L1.2')],
    control='Điều kiện duy nhất về mục đích không được đáp ứng, nguồn gọn.',
    negative=('L1.2','not_applicable','unmet','Điều kiện chỉ phục vụ quốc phòng không đáp ứng do có mục đích dân sự.'))

add('C05',3,'HOLDOUT_TEST','standalone_model_classification',
    'Nhóm nghiên cứu mới công bố một mô hình AI, chưa gắn nó vào hệ thống cụ thể nào. Quy định phân loại rủi ro của Nghị định có áp dụng ngay cho mô hình độc lập này không?',
    'Phạm vi đối tượng phân loại: mô hình độc lập và mô hình trong hệ thống cụ thể; không tuyên bố miễn luật dữ liệu/sở hữu trí tuệ.',
    'Chỉ mô hình; chưa là thành phần hệ thống cụ thể.', 'Không cần xác định rủi ro giả định của ứng dụng tương lai.',[
    P('Phân loại theo điều này áp dụng cho hệ thống, không áp cho mô hình độc lập, trừ khi mô hình là thành phần hệ thống cụ thể.', 'N6.2')],
    control='Một khoản xác định đối tượng bị loại khỏi thủ tục phân loại.',
    negative=('N12.1','not_applicable','unmet','Chưa có hệ thống rủi ro cao/trung bình để áp nghĩa vụ hồ sơ phân loại.'))

add('C06',3,'HOLDOUT_TEST','third_party_brand_provider',
    'Công ty tôi thuê một nhóm khác thiết kế và huấn luyện AI nhưng tự đưa hệ thống ra bán dưới thương hiệu mình. Có thể nói nhóm làm kỹ thuật mới là nhà cung cấp, còn công ty tôi không phải nhà cung cấp vì không tự huấn luyện không?',
    'Phân biệt nhà phát triển và nhà cung cấp theo kiểm soát kỹ thuật và tên/thương hiệu, không kết luận trách nhiệm hợp đồng.',
    'Nhóm được thuê thiết kế/huấn luyện; công ty bán dưới thương hiệu mình.', 'Không nêu quyền kiểm soát kỹ thuật của nhóm hoặc phân loại rủi ro; không gán vô điều kiện vai trò nhà phát triển hay nghĩa vụ theo rủi ro.',[
    P('Công ty đưa hệ thống dưới thương hiệu mình là nhà cung cấp, không phụ thuộc tự phát triển hay bên thứ ba. Nhóm kỹ thuật thuộc định nghĩa nhà phát triển nếu có quyền kiểm soát trực tiếp phương pháp kỹ thuật, dữ liệu huấn luyện hoặc tham số mô hình; không cần xác nhận điều kiện đó để kết luận vai trò nhà cung cấp của công ty.', 'L3.3 L3.4',
      condition=('conditional','unknown','Quyền kiểm soát kỹ thuật của nhóm thuê ngoài chưa được nêu: chỉ kết luận nhánh nhà phát triển có điều kiện. Tư cách nhà cung cấp của công ty đã đủ dữ kiện thương hiệu.'))],
    control='Định nghĩa vai trò gọn, không đồng nhất làm kỹ thuật với đưa ra thị trường.')

add('C07',3,'HOLDOUT_TEST','regulator_catalogue_role',
    'Chúng tôi là doanh nghiệp phát triển AI. Đồng nghiệp đọc phần xây dựng danh mục rủi ro cao rồi cho rằng doanh nghiệp có nhiệm vụ tổng hợp đề xuất của các bộ để trình Thủ tướng. Nhiệm vụ đó thuộc doanh nghiệp hay cơ quan nào?',
    'Xác định chủ thể của nhiệm vụ tổng hợp/xây dựng/trình danh mục; không liệt kê toàn bộ thẩm quyền hoặc thay nghĩa vụ tự phân loại.',
    'Doanh nghiệp phát triển AI, không là Bộ KH&CN hay cơ quan quản lý.', 'Không cần dữ kiện hệ thống cụ thể cho chủ thể nhiệm vụ này.',[
    P('Nhiệm vụ chủ trì phối hợp tổng hợp, xây dựng và trình danh mục là của Bộ KH&CN; không chuyển nhiệm vụ quản lý nhà nước này thành nghĩa vụ doanh nghiệp phát triển.', 'N7.2.d|N41.2.a')],
    control='Loại bỏ nhiệm vụ cơ quan quản lý khỏi nghĩa vụ nhà phát triển.',
    negative=('N7.2.d','not_applicable','unmet','Doanh nghiệp không phải chủ thể Bộ KH&CN được giao nhiệm vụ.'))

add('C08',3,'HOLDOUT_TEST','routine_update_exception',
    'Nhà cung cấp chúng tôi chỉ sửa lỗi kỹ thuật thường lệ cho hệ thống AI rủi ro cao đã đánh giá sự phù hợp. Việc sửa không đổi bản chất rủi ro hay khả năng đáp ứng yêu cầu pháp lý. Có phải làm lại phân loại và đánh giá sự phù hợp chỉ vì đổi số phiên bản không?',
    'Ngoại lệ cập nhật thường lệ đối với phân loại lại và đánh giá lại; không cho phép bỏ qua thay đổi thực chất.',
    'Rủi ro cao đã đánh giá; sửa lỗi thường lệ; không đổi bản chất rủi ro hay đáp ứng yêu cầu Điều 14 của Luật.', 'Không có thay đổi đáng kể ngoài mô tả.',[
    P('Không phải rà soát/thông báo phân loại lại cho sửa lỗi thường lệ không đổi bản chất rủi ro.', 'N11.4'),
    P('Sửa lỗi/nâng phiên bản không thay việc đáp ứng yêu cầu pháp lý không được coi là thay đổi đáng kể để buộc đánh giá lại sự phù hợp theo khoản này.', 'N13.1.đ')],
    control='Hai ngoại lệ theo điều kiện cụ thể, không suy từ số phiên bản.',
    negative=('N13.1.b','not_applicable','unmet','Điều kiện thay đổi chủ yếu ảnh hưởng độ tin cậy/an toàn không xảy ra.'))

add('C09',3,'HOLDOUT_TEST','ordinary_insurance_vs_sandbox',
    'Chúng tôi vận hành thương mại một AI rủi ro cao, không tham gia sandbox. Có người nói quy định AI buộc chúng tôi mua bảo hiểm trách nhiệm dân sự vì hệ thống có thể gây thiệt hại tài sản lớn. Nhận định đó có đúng trong phạm vi các quy định này không?',
    'Phân biệt khuyến khích bảo hiểm trong quản lý cao với điều kiện bảo hiểm/đảm bảo tài chính khi đăng ký sandbox; không xác định bảo hiểm bắt buộc ở luật chuyên ngành.',
    'Bên triển khai thương mại; rủi ro cao; không sandbox; nguy cơ thiệt hại tài sản lớn.', 'Không biết lĩnh vực bảo hiểm chuyên ngành; ngoài phạm vi kết luận.',[
    P('Đối với nhà cung cấp/bên triển khai rủi ro cao, Luật khuyến khích bảo hiểm trách nhiệm dân sự hoặc biện pháp đảm bảo phù hợp, không đặt nghĩa vụ mua bảo hiểm trong khoản này.', 'L14.5'),
    P('Yêu cầu bảo hiểm hoặc đảm bảo tài chính tương đương trong điều kiện thử nghiệm áp dụng cho bên tham gia sandbox có nguy cơ trực tiếp gây thiệt hại nêu trong quy định; dữ kiện không sandbox không đáp ứng phạm vi đó.', 'N24.1.d')],
    control='Loại quy tắc sandbox khỏi hoạt động thương mại ngoài sandbox.',
    negative=('N24.1.d','not_applicable','unmet','Không đăng ký/tham gia cơ chế thử nghiệm có kiểm soát.'),
    d4='Mức khuyến khích tại L14.5 và phạm vi điều kiện bắt buộc ở N24.1.d là hai nội dung cần đối chiếu; không có đơn tài liệu đủ phân biệt.')

add('C10',3,'HOLDOUT_TEST','public_model_security_actor',
    'Nhóm được thuê phát triển AI phục vụ dịch vụ công cho rằng chỉ đơn vị vận hành máy chủ mới phải lo đầu độc dữ liệu và đầu độc mô hình. Nhóm phát triển có thuộc phạm vi trách nhiệm bảo vệ hệ thống theo Khung đạo đức không?',
    'Phạm vi nhà phát triển trong dịch vụ công và bảo vệ dữ liệu/mô hình trước đầu độc; không gán nghĩa vụ vận hành hạ tầng nhà nước cho nhóm.',
    'Nhà phát triển được thuê làm AI dịch vụ công, không là đơn vị máy chủ.', 'Chưa có tấn công thực tế; hỏi trách nhiệm phòng ngừa.',[
    P('Nhà phát triển AI phục vụ dịch vụ công thuộc đối tượng của Thông tư; biện pháp bảo vệ phải phù hợp để phòng ngừa/phát hiện/ngăn chặn/ứng phó đầu độc dữ liệu, mô hình và các tấn công vào hệ thống.', 'T1.2 T3.1.e')],
    control='Không cần suy diễn chuyển vai trò máy chủ; phạm vi trực tiếp đã ghi trong Thông tư.')

add('C11',3,'HOLDOUT_TEST','sandbox_level_one_real_people',
    'Đề án thử AI của chúng tôi có nhóm người tham gia theo tiêu chí, địa điểm và thời hạn rõ ràng. Kết quả không dùng vào công việc thực tế, không đưa cho người dùng hay làm căn cứ quyết định; đã xác định không thuộc các trường hợp cấp độ 3. Chỉ vì có người tham gia thật thì phải xếp thử nghiệm cấp độ 2 sao?',
    'Kiểm tra điều kiện cấp 1/2 của sandbox dựa vào việc dùng kết quả; không đồng nhất cấp thử nghiệm với mức rủi ro hệ thống.',
    'Người tham gia xác định; địa điểm/thời hạn rõ; đầu ra không sử dụng thực tế/cung cấp/ngụ ý tham chiếu quyết định; loại cấp 3.', 'Không có điều kiện cấp 2 khác ngoài mô tả.',[
    P('Cấp 2 đòi hỏi cả dùng kết quả trong hoạt động thực tế; với kết quả bị giới hạn như mô tả và không thuộc cấp 3/2, tình huống đáp ứng cấp 1, không chỉ dựa vào có người thật để xếp cấp 2.', 'N22.4 N22.5')],
    control='Phân biệt các điều kiện đồng thời tại cùng một điều.',
    negative=('N22.4.b','not_applicable','unmet','Kết quả không được sử dụng trong hoạt động thực tế.'))

add('C12',3,'HOLDOUT_TEST','state_secret_publication',
    'Một hệ thống AI của cơ quan dùng cho quản lý dân sự nhưng thuộc danh mục bí mật nhà nước. Có phải công khai dữ liệu hệ thống lên cổng một cửa như các hệ thống thông thường, và ngoại lệ công khai có nghĩa là không phải tuân thủ quy định bảo vệ bí mật không?',
    'Ngoại lệ thông báo/đăng ký/chia sẻ công khai trên cổng và nghĩa vụ pháp luật liên quan bí mật; không kết luận miễn toàn bộ Luật AI.',
    'Hệ thống AI dân sự của cơ quan; thuộc danh mục bí mật nhà nước.', 'Không yêu cầu công khai nội dung bí mật hay hướng dẫn xử lý dữ liệu thực.',[
    P('Hệ thống thuộc danh mục bí mật nhà nước không thuộc phạm vi phải thông báo, đăng ký, chia sẻ dữ liệu công khai trên cổng theo ngoại lệ này.', 'N4.3.d'),
    P('Hoạt động AI liên quan bí mật nhà nước còn phải tuân thủ pháp luật bảo vệ bí mật nhà nước, an ninh mạng, cơ yếu; ngoại lệ công khai không bãi bỏ trách nhiệm đó.', 'N1.3')],
    control='Ngoại lệ công khai và yêu cầu bảo vệ độc lập đều minh thị.',
    negative=('N4.1.d','not_applicable','unmet','Không thể chuyển nhiệm vụ công khai của cổng thành buộc công khai hệ thống bí mật thuộc ngoại lệ.'))

add('C13',3,'EXCLUDE','developer_incident_role',
    'Nhóm tôi chỉ phát triển kỹ thuật AI, không bán hay trực tiếp triển khai. Nếu hệ thống do mình phát triển xảy ra sự cố nghiêm trọng thì nghĩa vụ kỹ thuật và thông báo trong Luật có chỉ thuộc nhà cung cấp không?',
    'Trách nhiệm nhà phát triển trong sự cố nghiêm trọng, không áp độc lập mọi thủ tục báo cáo dành cho nhà cung cấp/bên triển khai.',
    'Nhóm phát triển có kiểm soát kỹ thuật; không cung cấp/triển khai; giả định sự cố nghiêm trọng.', 'Không có dữ kiện hậu quả cụ thể để chọn hạn báo cáo Nghị định.',[
    P('Luật giao cả nhà phát triển và nhà cung cấp khẩn trương biện pháp kỹ thuật khắc phục, tạm dừng hoặc thu hồi và thông báo cơ quan có thẩm quyền khi sự cố nghiêm trọng.', 'L12.2.a')],
    control='Phạm vi chủ thể được nêu trực tiếp, không cần chuyển nghĩa vụ giữa vai trò.',
    exclude='near_duplicate: so với câu lịch sử về trách nhiệm nhà cung cấp khi sự cố, việc thay sang nhà phát triển vẫn dùng cùng gói nghĩa vụ chung L12.2.a. Vai trò có khác nhưng tác vụ và mệnh đề quá gần để giữ trong cohort mới; loại theo sàng lọc thận trọng, không theo kết quả hệ thống.')

add('C14',3,'RESERVE_DEV','voluntary_support_information',
    'Doanh nghiệp chia sẻ một mô hình AI hợp pháp chưa gửi mẫu thông tin điện tử trên cổng. Cơ quan tiếp nhận có thể coi riêng việc chưa dùng mẫu là lý do doanh nghiệp không được xem xét hỗ trợ phi tài chính không?',
    'Tính không bắt buộc của mẫu thông tin trong cơ chế chia sẻ tự nguyện, không khẳng định đủ mọi điều kiện hỗ trợ.',
    'Chia sẻ mô hình hợp pháp; chưa dùng mẫu điện tử.', 'Tiêu chí chất lượng và nguồn lực chưa biết.',[
    P('Mẫu thông tin chỉ hỗ trợ, không bắt buộc và không là điều kiện được xem xét hỗ trợ; không thể loại chỉ vì chưa sử dụng mẫu.', 'N34.6')],
    control='Một khoản đủ loại điều kiện hồ sơ tự đặt.')

add('C15',3,'RESERVE_DEV','foreign_contact',
    'Công ty nước ngoài cung cấp AI rủi ro cao tại Việt Nam đã có đầu mối liên hệ hợp pháp. Chúng tôi chưa biết hệ thống có thuộc diện bắt buộc chứng nhận hay không. Như vậy đầu mối hiện có đã đủ thay cho hiện diện thương mại hoặc đại diện ủy quyền chưa?',
    'Đầu mối liên hệ và yêu cầu tăng cường nếu thuộc diện chứng nhận; kết luận đủ cho công ty còn thiếu điều kiện material.',
    'Nhà cung cấp nước ngoài; AI rủi ro cao; đã có đầu mối hợp pháp; chưa xác định diện chứng nhận.', 'Tình trạng thuộc diện bắt buộc chứng nhận chưa biết.',[
    P('Đầu mối liên hệ hợp pháp là yêu cầu đối với nhà cung cấp nước ngoài rủi ro cao tại Việt Nam.', 'L14.6'),
    Q('Nếu hệ thống thuộc diện bắt buộc chứng nhận thì phải có hiện diện thương mại hoặc đại diện được ủy quyền tại Việt Nam.', 'L14.6',
      'Chưa thể kết luận đầu mối hiện có đủ vì chưa biết có thuộc diện bắt buộc chứng nhận.',condition=('uncertain','unknown','Điều kiện thuộc diện bắt buộc chứng nhận chưa được người dùng xác định.'))])

# Family 4: corpus boundary / partial-answer handling.
# Each absent-support assertion is tied to the full 86-article scoped audit.
add('D01',4,'DEV','research_integrity',
    'Viện tôi dùng AI để soạn bản thảo bài nghiên cứu. Cần lưu ý gì về liêm chính khi công bố, và ai đương nhiên sở hữu quyền tác giả đối với phần do AI tự tạo?',
    'Liêm chính nghiên cứu/công bố và chủ sở hữu quyền tác giả của phần AI tạo; không mở rộng sang hợp đồng lao động hoặc luật sở hữu trí tuệ bên ngoài corpus.',
    'Viện nghiên cứu; AI soạn bản thảo; hỏi liêm chính và quyền tác giả.', 'Không có hợp đồng, mức đóng góp con người hoặc văn bản luật sở hữu trí tuệ trong corpus.',[
    P('Ứng dụng AI nghiên cứu phải tuân thủ đạo đức, liêm chính khoa học và phòng ngừa gian lận, đạo văn trong nghiên cứu/công bố.', 'L6.3'),
    U('Không đủ corpus để xác định ai đương nhiên sở hữu quyền tác giả đối với phần do AI tự tạo.', 'L7.3 N35.5.c T3.4.a',
      'Các điều chỉ yêu cầu tuân thủ/bảo vệ sở hữu trí tuệ và nghiên cứu mở; không định nghĩa tác giả hay phân bổ quyền đối với đầu ra AI. Quy tắc tác quyền ngoài ba văn bản không được nhập vào.',
      ['quyền tác giả','đầu ra AI','sở hữu trí tuệ','tác phẩm','nghiên cứu','chủ sở hữu'])])

add('D02',4,'DEV','core_technology_tax',
    'Doanh nghiệp nghiên cứu phần cứng phục vụ AI muốn biết có nằm trong định hướng công nghệ được ưu tiên không, và được hưởng thuế suất thu nhập doanh nghiệp cụ thể bao nhiêu phần trăm?',
    'Nhóm công nghệ lõi được ưu tiên và thuế suất TNDN cụ thể; không tự xác định doanh nghiệp đạt điều kiện ưu đãi thuế.',
    'Doanh nghiệp nghiên cứu phần cứng phục vụ AI.', 'Không có điều kiện ưu đãi thuế riêng hay văn bản thuế trong corpus.',[
    P('Phần cứng, vi mạch bán dẫn và công nghệ tính toán phục vụ AI thuộc nhóm công nghệ lõi ưu tiên thúc đẩy làm chủ.', 'N37.2.d|L18.1'),
    U('Không đủ corpus để đưa ra thuế suất thu nhập doanh nghiệp cụ thể cho doanh nghiệp.', 'N37.4 L18.3 L20.2.d',
      'Corpus nêu tiếp cận ưu đãi theo pháp luật thuế và chính sách khuyến khích; không có mức thuế suất TNDN, điều kiện hay thời hạn miễn giảm tương ứng. Không chuyển định hướng ưu tiên thành quyền tự động hưởng một tỷ lệ.',
      ['thuế suất','thu nhập doanh nghiệp','miễn giảm thuế','công nghệ cốt lõi','phần cứng','ưu đãi'])])

add('D03',4,'DEV','label_fine_amount',
    'Nếu doanh nghiệp cố ý xóa nhãn AI bắt buộc khỏi video công khai, mức phạt tiền tối thiểu và tối đa cho đúng hành vi này là bao nhiêu?',
    'Chỉ hỏi khoảng phạt tiền hành chính cụ thể cho hành vi xóa nhãn; không yêu cầu kết luận hành vi bị cấm hoặc tư vấn xử lý sự cố.',
    'Doanh nghiệp cố ý xóa nhãn AI bắt buộc trên video công khai.', 'Không có văn bản xử phạt chi tiết trong corpus.',[
    U('Không đủ corpus để xác định khoảng tiền phạt hành chính tối thiểu/tối đa đối với doanh nghiệp xóa nhãn AI.', 'L7.5 L29.1 L29.5',
      'Luật xác định hành vi cấm và dẫn chiếu trách nhiệm xử phạt, giao Chính phủ quy định chi tiết. Nghị định 142 không có bảng mức tiền phạt; Thông tư 05 không ấn định tiền phạt. Sự tồn tại lệnh cấm không trả lời yêu cầu định lượng.',
      ['xóa nhãn','tẩy xóa','xử phạt','phạt tiền','tối thiểu','tối đa','vi phạm hành chính'])])

add('D04',4,'DEV','notice_api_specification',
    'Bộ phận tích hợp của tôi cần địa chỉ endpoint chính thức và schema JSON chính xác để gửi thông báo phân loại AI tự động. Các văn bản hiện có cho biết endpoint và từng trường dữ liệu kỹ thuật đó thế nào?',
    'Đặc tả kỹ thuật endpoint/schema chính thức của API, không hỏi hình thức pháp lý hoặc nội dung nghiệp vụ hồ sơ.',
    'Bộ phận tích hợp muốn gửi tự động thông báo phân loại.', 'Không có hướng dẫn/API triển khai chính thức trong corpus.',[
    U('Không đủ corpus để cung cấp endpoint và schema JSON kỹ thuật chính thức cho API thông báo.', 'N14.3.b N12.2 N4.4',
      'Quy định cho phép gửi qua API, mô tả thông tin nghiệp vụ và giao ban hành hướng dẫn dữ liệu, nhưng không có endpoint, HTTP contract hoặc schema kỹ thuật. Không suy ra tên trường JSON từ tên thông tin pháp lý.',
      ['API','giao diện lập trình','endpoint','JSON','thông báo','mô hình dữ liệu','hướng dẫn kỹ thuật'])])

add('D05',4,'HOLDOUT_TEST','procurement_preference_rate',
    'Chúng tôi phát triển công nghệ huấn luyện AI hiệu năng cao và muốn chào sản phẩm cho cơ quan nhà nước. Quy định AI có định hướng ưu tiên mua sắm loại công nghệ này không, và hồ sơ dự thầu được cộng ưu đãi giá chính xác bao nhiêu phần trăm?',
    'Định hướng sử dụng sản phẩm công nghệ lõi trong mua sắm công và tỷ lệ ưu đãi giá hồ sơ dự thầu; không tư vấn thủ tục đấu thầu đầy đủ.',
    'Doanh nghiệp công nghệ huấn luyện AI hiệu năng cao; chào sản phẩm cho cơ quan nhà nước.', 'Không có hồ sơ mời thầu hoặc pháp luật đấu thầu chi tiết trong corpus.',[
    P('Công nghệ huấn luyện hiệu năng cao nằm trong nhóm ưu tiên; bộ/ngành/địa phương thực hiện ưu tiên bố trí, sử dụng sản phẩm/giải pháp trong mua sắm công theo pháp luật đấu thầu, không phải bảo đảm trúng thầu.', 'N37.2.c N37.3.d'),
    U('Không đủ corpus để xác định phần trăm ưu đãi giá cụ thể trong đánh giá hồ sơ dự thầu.', 'N37.3.d N38.2.b L20.2.a',
      'Các điều dẫn chiếu pháp luật đấu thầu và chính sách ưu tiên, không có công thức hoặc tỷ lệ ưu đãi giá. Trần hỗ trợ sandbox ở N26.3 là tài trợ dịch vụ, không phải ưu đãi chấm thầu.',
      ['đấu thầu','mua sắm công','ưu đãi giá','phần trăm','công nghệ huấn luyện','chấm thầu'])])

add('D06',4,'HOLDOUT_TEST','technical_log_retention_boundary',
    'Nhà cung cấp AI rủi ro cao chúng tôi muốn lập chính sách lưu hồ sơ kỹ thuật và nhật ký, nhất là phải giữ bao nhiêu năm sau khi hệ thống ngừng hoạt động. Khi bị thanh tra, cần cung cấp những loại tài liệu nào?',
    'Lưu hồ sơ kỹ thuật/nhật ký và khoảng thời gian sau ngừng hoạt động; loại tài liệu khi thanh tra với bảo vệ thông tin; phân biệt hồ sơ phân loại với hồ sơ kỹ thuật/nhật ký.',
    'Nhà cung cấp rủi ro cao; lập chính sách lưu; giả định thanh tra.', 'Corpus không có con số năm sau ngừng vận hành cho hồ sơ kỹ thuật/nhật ký.',[
    Q('Phải lập, cập nhật và lưu hồ sơ kỹ thuật, nhật ký ở mức cần thiết cho đánh giá sự phù hợp/hậu kiểm; chỉ hỗ trợ nguyên tắc lưu giữ, không hỗ trợ số năm sau ngừng hoạt động.', 'L14.1.c',
      'Không đủ corpus để ấn định số năm lưu hồ sơ kỹ thuật và nhật ký sau khi ngừng hệ thống.',
      condition=('direct','met','Vai trò nhà cung cấp rủi ro cao xác lập; thiếu quy tắc thời hạn hậu vận hành trong corpus, không phải thiếu điều kiện chủ thể.'),
      reason='L14.1.c quy định mức cần thiết; N12.6 chỉ yêu cầu hồ sơ phân loại trong thời gian hệ thống hoạt động; N19.4 nói lưu dữ liệu sự cố và hạn gửi báo cáo, không phải thời gian lưu sau ngừng. Không suy rộng giữa loại hồ sơ hoặc biến 15 ngày báo cáo thành hạn lưu.',
      concepts=['lưu giữ','nhật ký','hồ sơ kỹ thuật','ngừng hoạt động','thời hạn','hồ sơ phân loại','báo cáo sự cố']),
    P('Khi thanh tra/kiểm tra, tổ chức liên quan cung cấp hồ sơ kỹ thuật, nhật ký, dữ liệu huấn luyện và thông tin cần thiết xác định nguyên nhân/phân trách nhiệm; tuân thủ bảo vệ bí mật, dữ liệu cá nhân và sở hữu trí tuệ.', 'L28.3')])

add('D07',4,'HOLDOUT_TEST','dataset_access_fee',
    'Nhóm tôi muốn dùng dữ liệu trong cơ sở dữ liệu quốc gia về AI để huấn luyện mô hình. Phải tuân thủ điều kiện sử dụng gì và mức phí chính thức cho mỗi lượt khai thác là bao nhiêu?',
    'Điều kiện truy cập/phạm vi/mục đích và trách nhiệm người dùng dữ liệu; mức phí định lượng mỗi lượt; không giả định dữ liệu nào miễn phí.',
    'Nhóm nghiên cứu khai thác cơ sở dữ liệu quốc gia phục vụ AI.', 'Chưa có danh mục dữ liệu và biểu phí cụ thể trong corpus.',[
    P('Chỉ khai thác khi đáp ứng điều kiện truy cập, phạm vi và mục đích theo công bố/thỏa thuận và pháp luật liên quan; cơ chế truy cập độc lập cơ chế hỗ trợ chia sẻ tự nguyện.', 'N35.1'),
    P('Người khai thác dùng đúng mục đích/phạm vi/điều kiện, không làm sai lệch hoặc dùng trái pháp luật, không xâm phạm sở hữu dữ liệu/sở hữu trí tuệ.', 'N35.5'),
    U('Không đủ corpus để xác định phí chính thức mỗi lượt khai thác dữ liệu.', 'N35.6 N35.2',
      'N35.6 dẫn chiếu pháp luật dữ liệu/phí, lệ phí; nội dung công bố không chứa biểu phí định lượng. Quyền truy cập hoặc hỗ trợ hạ tầng không chứng minh giá bằng không; dữ liệu thương mại cũng không cung cấp biểu phí nhà nước.',
      ['phí','lệ phí','giá dữ liệu','mỗi lượt','khai thác dữ liệu','biểu phí'])])

add('D08',4,'HOLDOUT_TEST','conformity_numeric_threshold',
    'Công ty có hệ thống AI rủi ro cao nhưng không thuộc diện phải chứng nhận bắt buộc. Có được tự đánh giá sự phù hợp không, và chất lượng dữ liệu huấn luyện phải đạt ngưỡng số cụ thể nào để đạt?',
    'Quyền tự đánh giá cùng hồ sơ/trách nhiệm và chất lượng dữ liệu; thiếu ngưỡng định lượng cụ thể; không kết luận hệ thống đã đạt.',
    'Nhà cung cấp rủi ro cao; ngoài diện bắt buộc chứng nhận.', 'Không có tiêu chuẩn/quy chuẩn ngành hoặc số đo dữ liệu cụ thể.',[
    P('Được tự đánh giá hoặc thuê tổ chức phù hợp; tự đánh giá phải lập hồ sơ kỹ thuật và chịu trách nhiệm kết quả.', 'N13.2.b'),
    Q('Dữ liệu phải bảo đảm chất lượng, phù hợp và tính đại diện trong phạm vi cần thiết hạn chế rủi ro; corpus chỉ cho yêu cầu này, không cho ngưỡng số để kết luận đạt.', 'N15.2.b',
      'Không đủ corpus để ấn định ngưỡng số chất lượng dữ liệu huấn luyện dùng làm điều kiện đạt sự phù hợp.',
      condition=('direct','met','Chủ thể và rủi ro cao xác lập; thiếu đặc tả số chứ không phải không áp nghĩa vụ.'),
      reason='L14.1.b/N15.2.b đặt yêu cầu chất lượng theo mục đích/rủi ro; N13 dẫn tới tiêu chuẩn, quy chuẩn hoặc hướng dẫn, không chứa chỉ số hay ngưỡng số chất lượng dữ liệu. Không tự tạo tỷ lệ chính xác, đại diện hoặc sai số.',
      concepts=['chất lượng dữ liệu','tính đại diện','ngưỡng','tiêu chuẩn','đánh giá sự phù hợp','tỷ lệ'])])

add('D09',4,'HOLDOUT_TEST','compensation_quantification',
    'Tài sản của tôi bị hệ thống AI làm hỏng. Chỉ xét cách tính tiền bồi thường: quy định AI ấn định công thức tính và mức trần tiền bồi thường cho thiệt hại tài sản này như thế nào?',
    'Chỉ công thức và trần tiền bồi thường tài sản, không hỏi ai chịu trách nhiệm hay miễn trừ.',
    'Người bị thiệt hại tài sản do AI; hỏi định lượng bồi thường.', 'Không có luật dân sự/định giá tổn thất; không xác định sự kiện lỗi.',[
    U('Không đủ corpus để đưa công thức và mức trần tiền bồi thường tài sản.', 'L29.1 L29.2 L29.4',
      'L29 phân định trách nhiệm và dẫn pháp luật dân sự, không có công thức định giá tài sản hoặc trần tiền bồi thường. Quy tắc người chịu trách nhiệm không trả lời yêu cầu tính tiền; không suy trần hỗ trợ tài chính thành trần bồi thường.',
      ['bồi thường','thiệt hại tài sản','mức trần','công thức','dân sự','giá trị tài sản'])])

add('D10',4,'HOLDOUT_TEST','assessor_live_register',
    'Tôi cần tên và mã đăng ký của các tổ chức đang được phép chứng nhận sự phù hợp cho hệ thống AI tại Việt Nam để chọn một đơn vị. Ba văn bản về AI có danh sách cụ thể đó không?',
    'Danh sách tên/mã đăng ký tổ chức được phép, không hỏi điều kiện năng lực của tổ chức đánh giá.',
    'Muốn chọn đơn vị đánh giá; yêu cầu danh sách thực thể cụ thể trong ba văn bản.', 'Không có đăng bạ hoặc quyết định đăng ký của từng tổ chức trong corpus.',[
    U('Không đủ corpus để cung cấp tên và mã đăng ký cụ thể của các tổ chức được phép chứng nhận sự phù hợp AI.', 'N13.4 L13.5 N13.6.d',
      'Corpus có điều kiện tổ chức và nghĩa vụ nêu tên tổ chức trong công khai kết quả từng hệ thống, nhưng không có danh sách tổ chức đã đăng ký/thừa nhận. Điều kiện pháp lý không chứng minh một thực thể cụ thể đang được phép.',
      ['tổ chức đánh giá','đăng ký','thừa nhận','chứng nhận','danh sách','mã đăng ký'])])

add('D11',4,'HOLDOUT_TEST','core_data_catalogue_lookup',
    'Nhóm tôi cần tra danh mục dữ liệu cốt lõi và dữ liệu quan trọng để đối chiếu bộ dữ liệu dự kiến thử nghiệm AI. Xin cho nội dung danh mục và mã từng nhóm dữ liệu được ban hành chính thức.',
    'Nội dung/mã nhóm của danh mục dữ liệu cốt lõi/quan trọng; không hỏi hậu quả phân cấp sandbox khi đã biết loại dữ liệu.',
    'Nhóm chuẩn bị dữ liệu thử nghiệm AI; cần danh mục chính thức để đối chiếu.', 'Danh mục dữ liệu cốt lõi/quan trọng không nằm trong ba tài liệu.',[
    U('Không đủ corpus để cung cấp danh mục và mã nhóm dữ liệu cốt lõi, dữ liệu quan trọng chính thức.', 'N22.3.a N32.2.c L17.5',
      'N22 sử dụng tên loại dữ liệu theo pháp luật dữ liệu/bảo vệ dữ liệu; N32/L17 nói danh mục bộ dữ liệu phục vụ phát triển AI lĩnh vực thiết yếu, là danh mục khác và chỉ phân công ban hành. Không có nội dung bảng/mã của danh mục được hỏi.',
      ['dữ liệu cốt lõi','dữ liệu quan trọng','danh mục','mã dữ liệu','lĩnh vực thiết yếu'])])

add('D12',4,'HOLDOUT_TEST','cross_border_personal_data_procedure',
    'Đơn vị tôi muốn chuyển dữ liệu cá nhân sang máy chủ ở nước ngoài để huấn luyện AI. Xin hướng dẫn đúng hồ sơ, cơ quan nhận và thời hạn nộp theo thủ tục chuyển dữ liệu cá nhân ra nước ngoài.',
    'Chỉ thủ tục chuyên biệt chuyển dữ liệu cá nhân ra nước ngoài; không hỏi nguyên tắc bảo vệ dữ liệu hay hợp pháp hóa việc chuyển.',
    'Đơn vị chuyển dữ liệu cá nhân ra máy chủ nước ngoài để huấn luyện.', 'Không có văn bản bảo vệ dữ liệu quy định thủ tục chuyển ra nước ngoài trong corpus.',[
    U('Không đủ corpus để xác định hồ sơ, cơ quan nhận và thời hạn của thủ tục chuyển dữ liệu cá nhân ra nước ngoài.', 'L7.3 N16.5 N36.4 L32.1',
      'Corpus yêu cầu tuân thủ pháp luật dữ liệu/bảo vệ dữ liệu và hợp tác quốc tế nhưng không quy định thủ tục chuyển ra nước ngoài. N12.7 chỉ cho tích hợp hồ sơ đánh giá tác động dữ liệu vào hồ sơ phân loại AI, không cung cấp thủ tục được hỏi.',
      ['chuyển dữ liệu','nước ngoài','dữ liệu cá nhân','hồ sơ đánh giá tác động','cơ quan tiếp nhận','thời hạn'])])

add('D13',4,'RESERVE_DEV','fund_fiscal_allocation',
    'Chúng tôi đang chuẩn bị dự án đào tạo nhân lực AI. Quỹ Phát triển AI quốc gia có định hướng hỗ trợ hoạt động này không, và ngân sách đã phân bổ cho đào tạo trong năm 2026 chính xác là bao nhiêu?',
    'Nhóm mục tiêu hỗ trợ nhân lực của Quỹ và số phân bổ năm cụ thể; không xác nhận dự án được duyệt.',
    'Dự án đào tạo AI; hỏi mục tiêu Quỹ và phân bổ 2026.', 'Không có quyết định dự toán hoặc phân bổ ngân sách.',[
    P('Quỹ ưu tiên đầu tư/tài trợ/hỗ trợ đào tạo, bồi dưỡng và thu hút nhân lực AI.', 'L22.3.d'),
    U('Không đủ corpus để xác định ngân sách phân bổ đào tạo AI năm 2026.', 'L22.2 L22.3 L22.5 N41.9',
      'Nguồn tài chính, ưu tiên và phân công xây dựng cơ chế Quỹ không phải quyết định phân bổ niên độ; corpus không có số tiền ngân sách năm 2026 theo mục đào tạo.',
      ['Quỹ','đào tạo','ngân sách','phân bổ','2026','dự toán'])])

add('D14',4,'RESERVE_TEST','criminal_provision_lookup',
    'Một người cố tình dùng AI giả mạo để gây hại nghiêm trọng. Tôi cần biết số điều của Bộ luật Hình sự và khung hình phạt tù tương ứng, chỉ dựa trên các văn bản AI trong bộ tài liệu.',
    'Điều luật hình sự và khung tù cụ thể, không xác định hành vi cấm chung hoặc kết tội cá nhân.',
    'Tình huống giả định dùng AI giả mạo gây hại; chỉ yêu cầu căn cứ hình sự cụ thể.', 'Bộ luật Hình sự và chi tiết cấu thành không trong corpus.',[
    U('Không đủ corpus để xác định số điều Bộ luật Hình sự và khung tù tương ứng.', 'L7.2.b L29.1 N42.1',
      'Luật AI nêu hành vi cấm và khả năng truy cứu tùy tính chất/mức độ/hậu quả; Nghị định phân công xử lý. Không có điều Bộ luật Hình sự hoặc khung tù. Không kết luận tội danh từ mô tả khái quát.',
      ['hình sự','hình phạt','phạt tù','giả mạo','tội danh','Bộ luật Hình sự'])])

add('D15',4,'EXCLUDE','ambiguous_reclassification_transition',
    'Chúng tôi đổi chức năng AI làm hệ thống phải phân loại lại thành rủi ro cao, nhưng không có quyết định mới sửa danh mục. Thời gian chuyển tiếp mười hai tháng để làm hồ sơ được tính từ ngày nào?',
    'Chỉ thời điểm bắt đầu chuyển tiếp khi thay đổi chức năng mà không có quyết định danh mục; không tự chữa dẫn chiếu của Nghị định.',
    'Đổi chức năng phải phân loại cao; không có quyết định sửa danh mục.', 'Điểm a khoản 1 và mốc quyết định danh mục trong khoản 5 không khớp.',[
    U('Không đủ căn cứ corpus để xác định mốc bắt đầu chuyển tiếp cho tình huống chỉ đổi chức năng mà không có quyết định sửa danh mục.', 'N11.1.a N11.1.c N11.5',
      'Khoản 5 đồng thời dẫn điểm a khoản 1 về đổi chức năng và lấy mốc quyết định sửa danh mục liên quan điểm c. Không có quy tắc khác trong corpus giải quyết sự không khớp này. Nội dung về trần 12 tháng không trả lời mốc bắt đầu được hỏi; cần review nguồn độc lập, không tự sửa hoặc suy đoán ngày.',
      ['chuyển tiếp','12 tháng','đổi chức năng','quyết định danh mục','mốc bắt đầu','phân loại lại'])],
    exclude='corpus_error_suspicion / legal_ambiguity: N11.5 dẫn điểm a khoản 1 (đổi chức năng) nhưng mốc lại là quyết định danh mục, phù hợp điểm c. Không tự sửa hoặc đưa vào retained trước review nguồn độc lập.')
