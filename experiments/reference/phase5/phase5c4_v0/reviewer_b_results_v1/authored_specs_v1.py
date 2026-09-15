# PRIVATE: independent B judgments, supplied packet order. No A material used.
item(1,
 ['Xác định tư cách nhà cung cấp khi thuê ngoài phát triển'],
 ['Công ty đưa hệ thống ra bán dưới thương hiệu mình','Nhóm khác thiết kế và huấn luyện'],
 ['Quyền kiểm soát kỹ thuật cụ thể của nhóm nhận thuê'],
 ['Nghĩa vụ tuân thủ theo từng mức rủi ro','Phân chia trách nhiệm theo hợp đồng'],
 'Công ty đưa sản phẩm ra thị trường và nhóm kỹ thuật','Hệ thống AI mang thương hiệu công ty',[
 aspect('Công ty là nhà cung cấp dù thuê bên thứ ba phát triển; tư cách nhà phát triển kỹ thuật không loại trừ tư cách này.', 'L3.4', context='L3.3')],
 applicability=True,quality='Câu hỏi tự nhiên, hẹp; phân biệt chủ thể theo thương hiệu với hoạt động kỹ thuật, thích hợp làm trường hợp kiểm soát áp dụng.')

item(2,
 ['Xây dựng phương án chia sẻ hạ tầng tư nhân vào mạng lưới quốc gia','Giữ quyền quản lý và quyền chọn công nghệ của khách hàng'],
 ['Thư viện tư nhân có năng lực tính toán AI nhàn rỗi','Dự kiến tự nguyện chia sẻ'],
 ['Điều khoản thỏa thuận','Đặc tả kết nối được cơ quan có thẩm quyền công bố'],
 ['Thiết kế kỹ thuật kết nối chi tiết','Ưu đãi tài chính cụ thể'],
 'Tổ chức tư nhân quản lý hạ tầng','Hạ tầng tham gia mạng lưới AI quốc gia',[
 aspect('Tham gia chia sẻ hạ tầng do tổ chức đầu tư trên cơ sở tự nguyện, qua thỏa thuận hoặc hợp đồng.','N30.1.b'),
 aspect('Kết nối không làm thay đổi quyền sở hữu, quản lý và khai thác hợp pháp, trừ quy định pháp luật khác.','N30.1.c'),
 aspect('Không áp đặt điều kiện kỹ thuật hoặc thương mại hạn chế khách hàng lựa chọn công nghệ, mô hình hay phương thức triển khai, trừ ngoại lệ pháp luật.','N29.2.b'),
 aspect('Phương án chia sẻ phải đáp ứng yêu cầu kỹ thuật kết nối, bảo vệ dữ liệu và kiểm soát truy cập an toàn.','N30.3',origin='scope_necessary')],
 broad=True,applicability=True,quality='Phạm vi hữu hạn theo việc tham gia mạng lưới; phân biệt tự nguyện tham gia với nghĩa vụ khi đã tham gia.')

item(3,
 ['Xác định có phải xếp trung bình chỉ vì sử dụng AI'],
 ['Hỗ trợ văn phòng, người dùng nhận biết rõ AI','Không mô phỏng gây nhầm lẫn','Đã xác định không nằm trong danh mục rủi ro cao'],
 [],['Thẩm định lại kết quả không thuộc danh mục cao'],
 'Doanh nghiệp sử dụng công cụ văn phòng','AI hỗ trợ văn phòng không thuộc nhóm cao',[
 aspect('Không xếp trung bình trong trường hợp công cụ văn phòng nhận biết rõ và không mô phỏng gây nhầm lẫn; với giả thiết không thuộc nhóm cao, thuộc nhóm thấp.','N9.3.b N6.3.c')],
 applicability=True,quality='Các điều kiện loại trừ được nêu rõ; một kết luận phân loại hữu hạn, không suy rộng mọi công cụ AI.')

item(4,
 ['Cung cấp tên và mã đăng ký tổ chức chứng nhận đang được phép hoạt động'],
 ['Muốn chọn một tổ chức chứng nhận cụ thể'],[],
 ['Chỉ mô tả tiêu chí năng lực tổ chức chứng nhận','Xác minh danh sách hiện hành ngoài corpus'],
 'Người lựa chọn tổ chức chứng nhận','Danh bạ tổ chức đánh giá sự phù hợp',[
 aspect('Phải công bố rằng corpus không cung cấp danh sách tên và mã đăng ký tổ chức chứng nhận đang được phép hoạt động.',status='no_support_in_corpus',
 unknown='Tên và mã đăng ký của từng tổ chức đang được phép chứng nhận.',context='L13.5 N13.4 N13.6.d N41.5',
 note='Ba văn bản quy định điều kiện, quản lý và thông tin công khai kết quả đánh giá; không chứa danh bạ tổ chức được đăng ký. Không dùng tên tổ chức theo từng kết quả công khai để suy ra danh sách hiện hành.')],
 quality='Yêu cầu danh bạ rõ ràng và tự nhiên; dùng để kiểm tra giới hạn corpus, không cộng điểm nội dung cho việc kể điều kiện chứng nhận.')

item(5,
 ['Xác định chủ thể tổng hợp đề xuất của các bộ và trình Thủ tướng về danh mục cao'],
 ['Doanh nghiệp phát triển AI','Có nhận định giao nhiệm vụ tổng hợp cho doanh nghiệp'],[],
 ['Nghĩa vụ tự phân loại sản phẩm','Nội dung danh mục cụ thể'],
 'Doanh nghiệp và Bộ Khoa học và Công nghệ','Quy trình xây dựng danh mục',[
 aspect('Nhiệm vụ chủ trì tổng hợp, xây dựng và trình danh mục thuộc Bộ Khoa học và Công nghệ, không phải nghĩa vụ của doanh nghiệp chỉ vì phát triển AI.',alternatives=['N7.2.d','N41.2.a'],context='N7.2.b')],
 applicability=True,quality='Phân biệt cơ quan ban hành/chủ trì với doanh nghiệp chịu quản lý; câu hỏi hẹp, có căn cứ trực tiếp.')

item(6,
 ['Xác định đúng hồ sơ, cơ quan nhận và thời hạn thủ tục chuyển dữ liệu cá nhân ra nước ngoài'],
 ['Chuyển dữ liệu cá nhân sang máy chủ nước ngoài để huấn luyện'],
 ['Loại dữ liệu và quy trình chuyển cụ thể'],
 ['Tư vấn toàn bộ quản trị dữ liệu AI','Tự điền thủ tục từ pháp luật ngoài corpus'],
 'Đơn vị chuyển dữ liệu cá nhân','Thủ tục chuyển dữ liệu ra nước ngoài',[
 aspect('Không thể xác định bộ hồ sơ, cơ quan nhận và thời hạn của thủ tục chuyển dữ liệu cá nhân ra nước ngoài chỉ từ corpus này.',status='no_support_in_corpus',
 unknown='Bộ hồ sơ, thẩm quyền tiếp nhận và thời hạn nộp của thủ tục chuyển dữ liệu cá nhân ra nước ngoài.',context='L7.3 L17.1 N35.1 N36.4',
 note='Các điều về dữ liệu và an toàn chỉ dẫn chiếu pháp luật dữ liệu, bảo vệ dữ liệu cá nhân; toàn corpus không quy định quy trình chuyển xuyên biên giới được hỏi.')],
 quality='Phạm vi thủ tục cụ thể, không biến nghĩa vụ tuân thủ pháp luật dữ liệu nói chung thành câu trả lời một phần cho thủ tục vắng mặt.')

item(7,
 ['Chuẩn bị khai thác dữ liệu quốc gia để thử mô hình nghiên cứu','Chuẩn bị công bố khoa học'],
 ['Nhóm nghiên cứu thuộc viện','Sử dụng dữ liệu AI quốc gia để thử mô hình'],
 ['Loại và điều kiện truy cập dữ liệu được công bố'],
 ['Mức phí cụ thể','Quyền tác giả đối với đầu ra','Đánh giá rủi ro một hệ thống chưa mô tả'],
 'Nhóm nghiên cứu khai thác dữ liệu','Thử mô hình hỗ trợ nghiên cứu',[
 aspect('Kiểm tra điều kiện truy cập, phạm vi và mục đích sử dụng đã công bố; việc khai thác độc lập với cơ chế hỗ trợ chia sẻ tự nguyện.','N35.1'),
 aspect('Sử dụng đúng mục đích, không làm sai lệch dữ liệu, không xâm phạm quyền sở hữu dữ liệu và sở hữu trí tuệ.','N35.5'),
 aspect('Tuân thủ điều kiện khai thác, an toàn trong phạm vi sử dụng dữ liệu; không tự coi quyền truy cập là quyền sử dụng vô hạn.','N36.2',origin='scope_necessary'),
 aspect('Nghiên cứu và công bố phải tuân thủ đạo đức nghiên cứu, liêm chính khoa học, phòng ngừa gian lận và đạo văn.','L6.3')],
 broad=True,quality='Kết hợp hợp lý sử dụng dữ liệu với công bố khoa học; cần Nghị định về khai thác và Luật về liêm chính.',d4='N35 quy định khai thác cụ thể; L6.3 quy định liêm chính nghiên cứu. Không có một văn bản thay thế đầy đủ cả hai phần.')

item(8,
 ['Xác định hồ sơ rút gọn','Cách nộp và thời gian xử lý hồ sơ hợp lệ','Hỗ trợ kỹ thuật có thể tiếp cận'],
 ['Doanh nghiệp nhỏ, thử nghiệm cấp độ 1 trong một tỉnh','Không thuộc cơ chế chuyên ngành','Hồ sơ hợp lệ'],
 ['Cơ quan có quản lý trực tiếp đơn vị hay không'],
 ['Soạn nội dung biểu mẫu không hiện diện trong corpus','Cam kết được tài trợ hoặc được chấp thuận'],
 'Doanh nghiệp nhỏ tham gia thử nghiệm','Sandbox cấp độ 1 tại một tỉnh',[
 aspect('Được dùng hồ sơ rút gọn gồm đơn theo mẫu tổ chức và mô tả khái quát hệ thống, rủi ro chính, biện pháp giảm thiểu; không yêu cầu thêm thành phần ngoài quy định.','N24.3 N24.5'),
 aspect('Nộp một bộ hồ sơ điện tử qua cổng Dịch vụ công quốc gia, liên thông sang cổng AI; thông thường thuộc UBND tỉnh đối với cấp độ 1 trong một tỉnh.','N23.2 N23.3.a',condition='Không có tình tiết đơn vị thuộc quản lý trực tiếp của bộ làm phát sinh tuyến thẩm quyền khác.',note='N23.3.b có tuyến cho đơn vị thuộc quản lý trực tiếp của bộ; câu hỏi là doanh nghiệp nhỏ tại một tỉnh, không khẳng định tình tiết đặc biệt đó.'),
 aspect('Với hồ sơ hợp lệ thuộc tuyến cấp tỉnh, thời hạn thẩm định và cấp giấy hoặc từ chối không quá 10 ngày làm việc; từ chối phải nêu lý do.','N23.5.a N23.6'),
 aspect('Doanh nghiệp tham gia sandbox được hỗ trợ tư vấn kỹ thuật, đánh giá rủi ro, kiểm thử an toàn và kết nối cơ sở thử nghiệm/kiểm định.','L25.4')],
 applicability=True,quality='Các điều kiện trọng yếu được nêu; giữ giới hạn về tuyến thẩm quyền và không hứa được cấp phép.',d4='N23–24 cho thủ tục cụ thể; L25.4 cho quyền hỗ trợ kỹ thuật, không coi Phiếu tài chính là bản thay thế đầy đủ.')

item(9,
 ['Xác định tư cách bên triển khai khi sử dụng cá nhân phi thương mại'],
 ['Sắp xếp ảnh gia đình','Hoàn toàn cá nhân, không kiếm tiền'],[],
 ['Tuyên bố miễn toàn bộ pháp luật đối với người sử dụng'],
 'Người dùng cá nhân','Ứng dụng sắp xếp ảnh',[
 aspect('Sử dụng cá nhân, phi thương mại bị loại khỏi định nghĩa bên triển khai; vẫn có thể là người sử dụng trực tiếp.','L3.5 L3.6')],
 applicability=True,quality='Đủ dữ kiện áp dụng ngoại lệ của định nghĩa; không đồng nhất người sử dụng với bên triển khai.')

item(10,
 ['Phân công phối hợp phân loại lại','Thời hạn thông báo sau rà soát','Thời điểm áp dụng biện pháp an toàn mới'],
 ['Bên vận hành tích hợp vào môi trường mới','Đã hoàn tất rà soát, tăng từ trung bình lên cao'],[],
 ['Thời gian chuyển tiếp hồ sơ theo thay đổi danh mục','Đánh giá lại kết luận phân loại đã cho'],
 'Bên triển khai và nhà cung cấp','Hệ thống đã xác định tăng mức rủi ro',[
 aspect('Bên triển khai phối hợp nhà cung cấp rà soát, phân loại lại khi tích hợp làm phát sinh rủi ro mới hoặc cao hơn.',alternatives=['N11.2','L10.2']),
 aspect('Nhà cung cấp và bên triển khai thông báo kết quả phân loại lại trong 15 ngày làm việc từ ngày hoàn thành rà soát.','N11.3.a'),
 aspect('Áp dụng ngay biện pháp quản lý rủi ro tương ứng mức mới, không đợi hoàn tất thông báo.','N11.3.a')],
 applicability=True,quality='Mốc thời gian và điều kiện tăng mức rõ; tách nghĩa vụ thông báo khỏi biện pháp áp dụng ngay, không tách vụn từng từ của một nghĩa vụ.')

item(11,
 ['Chuẩn bị vận hành phiên bản tích hợp mô hình và dữ liệu mới'],
 ['Nhà cung cấp AI cao đã đánh giá sự phù hợp','Thay đổi có thể ảnh hưởng đáng kể độ tin cậy'],
 ['Thay đổi cụ thể nguồn/loại dữ liệu','Có thuộc diện chứng nhận bắt buộc không','Có làm thay đổi tiêu chí phân loại không'],
 ['Kết luận kỹ thuật phiên bản đã đạt yêu cầu','Ấn định ngưỡng chất lượng số'],
 'Nhà cung cấp','Hệ thống rủi ro cao thay đổi mô hình/dữ liệu',[
 aspect('Thay đổi mô hình có thể ảnh hưởng độ tin cậy thuộc căn cứ đánh giá lại; thay đổi dữ liệu phải xét tác động đáng kể đến vận hành hoặc rủi ro.','N13.1.b N13.1.c',condition='Đánh giá lại theo tác động thay đổi đã mô tả; không suy rằng mọi cập nhật dữ liệu đều đáng kể.'),
 aspect('Rà soát, cập nhật quản lý rủi ro và chất lượng dữ liệu, giám sát con người khi thay đổi mô hình hoặc dữ liệu đáng kể.','N15.2'),
 aspect('Duy trì sự phù hợp và cập nhật thông tin kết quả đánh giá lại trên cổng; cập nhật hồ sơ kỹ thuật và nhật ký phục vụ kiểm tra.','N13.6 L14.1.c'),
 aspect('Thỏa thuận với bên cung cấp mô hình về phối hợp cung cấp thông tin kỹ thuật cần cho minh bạch và giải trình.','N16.6',origin='scope_necessary'),
 aspect('Nếu thay đổi chức năng hoặc ngữ cảnh ảnh hưởng tiêu chí phân loại ban đầu thì rà soát, phân loại lại.','N11.1.a',app='conditional',condition='Chỉ khi ảnh hưởng tiêu chí phân loại ban đầu; không giả định thay đổi này tự động làm tăng mức.',unknown=None)],
 broad=True,applicability=True,quality='Phạm vi chuyển phiên bản đủ hữu hạn; giữ riêng kiểm tra phân loại và đánh giá sự phù hợp, không chứng nhận thay doanh nghiệp.')

item(12,
 ['Chuẩn bị bàn giao cho đối tác trong nước vận hành'],
 ['Công ty nước ngoài đưa hệ thống mang thương hiệu mình vào Việt Nam','Đã xác định cao, không bắt buộc chứng nhận'],
 ['Hợp đồng bàn giao và mức độ kiểm soát của đối tác'],
 ['Điều kiện đầu tư, thuế, giấy phép chuyên ngành','Định danh bên đánh giá cụ thể'],
 'Nhà cung cấp nước ngoài và bên triển khai trong nước','AI cao không phải chứng nhận bắt buộc',[
 aspect('Công ty là nhà cung cấp theo thương hiệu; đối tác sử dụng dưới quyền kiểm soát trong dịch vụ là bên triển khai.','L3.4 L3.5',origin='scope_necessary'),
 aspect('Phải có đầu mối liên hệ hợp pháp tại Việt Nam; điều kiện hiện diện thương mại hoặc đại diện được ủy quyền thêm vào gắn với diện chứng nhận bắt buộc.','L14.6'),
 aspect('Có thể tự đánh giá sự phù hợp hoặc thuê tổ chức đủ điều kiện; tự đánh giá phải lập hồ sơ kỹ thuật và chịu trách nhiệm kết quả; công khai kết quả trước dùng.','N13.2.b N13.6'),
 aspect('Bàn giao thông tin mục đích, điều kiện vận hành an toàn, rủi ro và biện pháp quản lý; đối tác vận hành đúng giới hạn, giám sát, can thiệp và phối hợp xử lý.','N15.3 N15.4 N15.5'),
 aspect('Lập hồ sơ và thông báo phân loại cao trước đưa vào dùng; phân định trách nhiệm giải trình, minh bạch và sự cố theo vai trò.','N12.1 N14.1 N16.2 L12.2',origin='scope_necessary')],
 broad=True,applicability=True,quality='Phạm vi bàn giao hữu hạn gồm vai trò, đầu mối, điều kiện trước dùng và vận hành; không suy việc thuê đối tác xóa trách nhiệm nhà cung cấp.')

item(13,
 ['Xác định phạm vi Luật đối với hoạt động chỉ phục vụ quốc phòng'],
 ['Chỉ phục vụ quốc phòng, không mục đích dân sự'],[],
 ['Nghĩa vụ theo pháp luật quốc phòng ngoài corpus'],
 'Đơn vị vận hành phục vụ quốc phòng','AI chỉ phục vụ quốc phòng',[
 aspect('Hoạt động AI chỉ phục vụ quốc phòng không thuộc phạm vi điều chỉnh của Luật AI.','L1.2')],
 applicability=True,quality='Điều kiện chỉ phục vụ được xác lập; trường hợp kiểm soát phạm vi, không khẳng định miễn pháp luật khác.')

item(14,
 ['Điều kiện dùng dữ liệu quốc gia để huấn luyện','Mức phí chính thức mỗi lượt'],
 ['Nhóm muốn dùng cơ sở dữ liệu AI quốc gia'],
 ['Loại dữ liệu và điều kiện truy cập cụ thể'],
 ['Tính giá theo biểu phí bên ngoài corpus'],
 'Nhóm khai thác dữ liệu','Huấn luyện mô hình từ cơ sở dữ liệu quốc gia',[
 aspect('Tuân thủ điều kiện truy cập, phạm vi và mục đích sử dụng đã công bố cùng pháp luật dữ liệu, dữ liệu cá nhân và sở hữu trí tuệ.','N35.1'),
 aspect('Dùng đúng mục đích, không làm sai lệch hoặc sử dụng trái luật, tôn trọng quyền dữ liệu và sở hữu trí tuệ.','N35.5'),
 aspect('Không xác định được mức phí mỗi lượt từ corpus.',status='no_support_in_corpus',unknown='Mức phí chính thức cho một lượt khai thác.',context='N35.6',note='N35.6 dẫn chiếu pháp luật dữ liệu và phí, lệ phí; toàn corpus không có bảng giá hay công thức tính phí mỗi lượt.')],
 quality='Tách điều kiện sử dụng có căn cứ và khoản phí chưa có; không suy miễn phí từ quyền khai thác.')

item(15,
 ['Phạm vi phân loại rủi ro đối với mô hình độc lập'],
 ['Mới công bố mô hình','Chưa tích hợp vào hệ thống cụ thể'],[],
 ['Miễn trừ mọi nghĩa vụ khác khi công bố mô hình'],
 'Nhóm nghiên cứu mô hình','Mô hình AI độc lập',[
 aspect('Phân loại theo Nghị định chỉ áp dụng hệ thống, không áp dụng mô hình độc lập; ngoại lệ khi mô hình là thành phần của hệ thống cụ thể.','N6.2',context='N3.4')],
 applicability=True,quality='Phân biệt mô hình và hệ thống, giữ nguyên điều kiện ngoại lệ; câu hỏi ngắn tự nhiên.')

item(16,
 ['Chuẩn bị căn cứ chi phí và cách thanh toán Phiếu cho kiểm thử an toàn','Có nhận toàn bộ tiền rồi trả nhà cung cấp được không'],
 ['Doanh nghiệp được chấp thuận sandbox','Muốn thanh toán dịch vụ kiểm thử an toàn'],
 ['Phiếu đã được cấp chưa','Chi phí hợp lệ thực tế','Hạn mức ghi trên Phiếu'],
 ['Cam kết duyệt cấp Phiếu','Tính số tiền khi chưa có chi phí'],
 'Doanh nghiệp thử nghiệm và tổ chức cung cấp dịch vụ','Chi phí kiểm thử trong sandbox',[
 aspect('Dịch vụ kiểm thử an toàn phục vụ trực tiếp phạm vi thử nghiệm có thể được hỗ trợ đồng chi trả, tối đa 50% chi phí hợp lệ thực tế; không hỗ trợ trùng lặp.','N26.2 N26.3.c'),
 aspect('Chi phí hợp lệ phải phục vụ trực tiếp thử nghiệm, có hợp đồng, hóa đơn và chứng từ hợp pháp theo quy định kế toán, thuế, ngân sách.','N26.4'),
 aspect('Thanh toán trực tiếp cho bên cung cấp dịch vụ theo Phiếu, hợp đồng, khối lượng thực tế, hóa đơn/tài liệu xác nhận và dữ liệu đối soát; không qua người được cấp.','N26.5 N40.8'),
 aspect('Phiếu không quy đổi thành tiền, không chuyển nhượng; dùng trong mục đích, hạn mức, thời hạn, điều kiện đã ghi.','N40.3.c')],
 applicability=True,quality='Yêu cầu tài chính có số liệu định mức trong corpus; phân biệt trần hỗ trợ và quyền được cấp thực tế.')

item(17,
 ['Chuẩn bị trình bày tác phẩm tái hiện nhân vật trước công chúng theo quy định và Khung tự nguyện'],
 ['Bảo tàng tư nhân','AI tái hiện giọng nói và hình ảnh người có thật','Chủ động áp dụng Khung đạo đức'],
 ['Cách thức trình chiếu cụ thể'],
 ['Quyền hình ảnh, quyền tác giả ngoài corpus','Mặc định lĩnh vực nghệ thuật được miễn nhãn'],
 'Bảo tàng triển khai công khai tác phẩm','Nội dung nghệ thuật mô phỏng người thật',[
 aspect('Bên đưa nội dung ra công cộng phải gắn nhãn dễ nhận biết khi mô phỏng hình ảnh/giọng người thật; thông báo nếu có khả năng gây nhầm lẫn.','N18.1 N18.2.a'),
 aspect('Có thể đặt nhãn ở phần mở đầu, kết thúc, danh đề, mô tả hoặc tài liệu kèm theo phù hợp tác phẩm; phải bảo đảm nhận biết, không che giấu và không cản trở đáng kể thưởng thức.','N18.3 N18.6'),
 aspect('Việc áp dụng Khung đối với hoạt động tư nhân này là khuyến khích/tự nguyện theo giả thiết; bảo đảm minh bạch khả năng và giới hạn, tôn trọng văn hóa và lợi ích cộng đồng.','T1.3 T3.2.c T3.3.d',condition='Áp dụng tự nguyện đã nêu; không chuyển thành nghĩa vụ bắt buộc vì là bảo tàng.'),
 aspect('Trong phương án Khung tự nguyện, phân công trách nhiệm, đầu mối tiếp nhận phản ánh và khắc phục hậu quả.','T1.3 T3.4.b',origin='scope_necessary')],
 broad=True,applicability=True,quality='Phân biệt nghĩa vụ nhãn nội dung với việc tự nguyện dùng Khung; không suy ngoại lệ nghệ thuật thành miễn nhãn.')

item(18,
 ['Thời điểm và điều kiện gia hạn vận hành chuyển tiếp','Giá trị giấy hoàn thành đối với giấy phép chuyên ngành'],
 ['Đã có giấy hoàn thành sandbox','Đang vận hành trong giới hạn chuyển tiếp'],
 ['Ngày hết chuyển tiếp','Đã khắc phục sự cố theo yêu cầu hay chưa'],
 ['Gia hạn thời gian thử nghiệm khi chưa hoàn thành','Tự tính ngày lịch từ ngày chưa cung cấp'],
 'Đơn vị đã hoàn thành thử nghiệm','Vận hành chuyển tiếp sau sandbox',[
 aspect('Gửi đề nghị đến cơ quan cấp giấy hoàn thành chậm nhất 15 ngày trước hết thời gian chuyển tiếp; cơ quan xem xét trong 7 ngày làm việc từ đề nghị hợp lệ.','N27.6'),
 aspect('Chỉ gia hạn một lần tối đa 6 tháng khi đã hoàn thành thử nghiệm, khắc phục sự cố theo yêu cầu và tiếp tục duy trì biện pháp quản lý rủi ro được chấp thuận.','N27.6',app='conditional',condition='Đủ các điều kiện hoàn thành, khắc phục và duy trì quản lý rủi ro; chưa kết luận đơn vị thực tế đã đáp ứng.'),
 aspect('Giấy hoàn thành không thay giấy phép, chứng nhận, văn bản chấp thuận hoặc điều kiện kinh doanh; hết chuyển tiếp phải hoàn thành nghĩa vụ trước tiếp tục hoạt động.','N27.7 N27.8')],
 applicability=True,quality='Phân biệt gia hạn chuyển tiếp với gia hạn thử nghiệm, ngày thường với ngày làm việc; trả lời điều kiện chứ không phê duyệt thay cơ quan.')

item(19,
 ['Lịch báo cáo sự cố và lưu tài liệu','Nộp báo cáo có phải nhận lỗi'],
 ['Thiệt hại tài sản đáng kể','Không thuộc nhóm khẩn cấp đã liệt kê','Đủ thông tin xác nhận sự cố và khả năng cao từ lỗi AI'],
 ['Ngày xác nhận','Vai trò nhà cung cấp/bên triển khai cụ thể'],
 ['Tính ngày lịch cụ thể','Kết luận trách nhiệm bồi thường'],
 'Nhà cung cấp hoặc bên triển khai báo cáo','Sự cố nghiêm trọng tài sản không thuộc nhóm khẩn cấp',[
 aspect('Thiệt hại tài sản đáng kể thuộc sự cố nghiêm trọng; với các loại khẩn cấp đã loại trừ, báo cáo sơ bộ trong 5 ngày làm việc từ xác nhận qua cổng theo mẫu tổ chức.','N19.1.b N19.3.b',context='N19.3.a'),
 aspect('Mốc xác nhận là khi có thông tin ban đầu đủ xác định sự cố xảy ra và khả năng cao từ lỗi AI; không đợi điều tra toàn diện, báo cáo đúng hạn không đồng nghĩa thừa nhận lỗi/trách nhiệm.','N19.3.c'),
 aspect('Giữ nhật ký, dữ liệu và thông tin liên quan; gửi báo cáo chính thức kết quả khắc phục trong 15 ngày từ ngày nộp sơ bộ.','N19.4')],
 applicability=True,quality='Điều kiện chọn thời hạn báo cáo rõ; cần bảo toàn hai loại đơn vị ngày và ý nghĩa không thừa nhận lỗi.')

item(20,
 ['Kiểm tra nhận định bảo hiểm bắt buộc cho AI cao ngoài sandbox'],
 ['Vận hành thương mại hệ thống cao','Không tham gia sandbox'],[],
 ['Nghĩa vụ bảo hiểm theo pháp luật chuyên ngành khác'],
 'Bên triển khai thương mại ngoài sandbox','AI rủi ro cao',[
 aspect('Luật khuyến khích nhà cung cấp/bên triển khai tham gia bảo hiểm hoặc bảo đảm nghĩa vụ khác, không đặt nghĩa vụ bảo hiểm bắt buộc chỉ từ phân loại cao.','L14.5',counter='N24.1.d',note='N24.1.d áp dụng tổ chức/cá nhân tham gia thử nghiệm với khả năng gây hại được mô tả; thiếu điều kiện sandbox nên không áp đặt cho tình huống này.')],
 applicability=True,quality='Đối chiếu quy định chung khuyến khích với nghĩa vụ đặc thù thử nghiệm; không kết luận về luật bảo hiểm ngoài corpus.')

item(21,
 ['Có được tự đánh giá sự phù hợp','Ngưỡng số cụ thể cho chất lượng dữ liệu huấn luyện'],
 ['AI cao không thuộc diện chứng nhận bắt buộc'],
 ['Mục đích sử dụng và tiêu chuẩn kỹ thuật áp dụng'],
 ['Tự đặt ngưỡng số thay cơ quan kỹ thuật'],
 'Nhà cung cấp','AI cao không chứng nhận bắt buộc',[
 aspect('Được tự đánh giá hoặc sử dụng tổ chức đánh giá; tự đánh giá phải lập hồ sơ kỹ thuật và chịu trách nhiệm trước pháp luật về kết quả.','N13.2.b'),
 aspect('Corpus quy định chất lượng, tính phù hợp và tính đại diện của dữ liệu để hạn chế rủi ro, nhưng không đưa ngưỡng số bảo đảm đạt cho hệ thống này.','N15.2.b',status='partial_support',
 unknown='Ngưỡng số cụ thể để chất lượng dữ liệu huấn luyện được coi là đạt.',context='L14.1.b N13.3',note='Chỉ có tiêu chí định tính và dẫn chiếu tiêu chuẩn/quy chuẩn; không có thang số hay ngưỡng đạt tương ứng trong cả ba văn bản.')],
 quality='Hai nhu cầu tách biệt; phần dữ liệu có Q về tiêu chí và U về ngưỡng số, không cho điểm đủ đối với ngưỡng chưa biết.')

item(22,
 ['Có phải phân loại và đánh giá sự phù hợp lại chỉ vì đổi phiên bản'],
 ['Sửa lỗi kỹ thuật thường lệ','Không đổi bản chất rủi ro hoặc khả năng đáp ứng pháp lý','AI cao đã đánh giá'],[],
 ['Tự kiểm định đúng sai nhận định kỹ thuật của doanh nghiệp'],
 'Nhà cung cấp','Cập nhật kỹ thuật thường lệ AI cao',[
 aspect('Không phải rà soát/thông báo phân loại lại với sửa lỗi thông thường không đổi bản chất rủi ro.','N11.4'),
 aspect('Nâng phiên bản/sửa lỗi không đổi đáp ứng Điều 14 không được coi là thay đổi đáng kể để bắt buộc đánh giá lại sự phù hợp.','N13.1.đ')],
 applicability=True,quality='Dữ kiện ngoại lệ đầy đủ; phân biệt hai chế độ rà soát, không coi số phiên bản là sự kiện pháp lý tự thân.')

item(23,
 ['Tổ chức trách nhiệm đánh dấu giữa nhóm phát hành miễn phí và cửa hàng công khai video'],
 ['Hệ thống tạo video phát hành miễn phí','Cửa hàng dùng đầu ra quảng cáo công khai','Dự định cung cấp tài liệu cấu hình thay bật sẵn'],
 ['Video có mô phỏng người thật hoặc gây nhầm lẫn không'],
 ['Coi miễn phí là miễn mọi nghĩa vụ','Tiêu chuẩn kỹ thuật chưa có trong corpus'],
 'Nhà cung cấp miễn phí và bên triển khai công khai','AI tạo video',[
 aspect('Nhà cung cấp miễn phí có thể tích hợp sẵn đánh dấu hoặc công bố công khai công cụ/cấu hình/API/tài liệu cho phép bên triển khai cấu hình vận hành; tài liệu phải có khả năng thực hiện chức năng.','N17.5'),
 aspect('Cửa hàng dùng hệ thống đó cung cấp nội dung công cộng phải áp dụng giải pháp kỹ thuật đánh dấu đầu ra máy đọc.','N17.5.b N17.1'),
 aspect('Thông báo khi đầu ra có thể gây nhầm lẫn; gắn nhãn hiển thị nếu mô phỏng người thật/tái hiện sự kiện, tách với đánh dấu máy đọc.','N18.1 N18.2',app='conditional',condition='Nhãn/thông báo theo tính chất nội dung; query chưa xác định video thực tế có các tính chất này.'),
 aspect('Các bên duy trì thông tin minh bạch trong suốt quá trình cung cấp nội dung.','L11.5',origin='scope_necessary')],
 broad=True,applicability=True,quality='Tình huống miễn phí và công khai có điều kiện cụ thể; không suy video quảng cáo nào cũng là giả mạo.')

item(24,
 ['Địa chỉ endpoint chính thức','Schema JSON và từng trường kỹ thuật để gửi phân loại'],
 ['Bộ phận tích hợp cần kết nối tự động'],[],
 ['Chỉ nêu cách gửi qua API được phép','Tự thiết kế endpoint hay schema'],
 'Bộ phận tích hợp','API thông báo phân loại',[
 aspect('Corpus không xác định địa chỉ endpoint chính thức hoặc schema JSON chính xác của giao diện gửi phân loại.',status='no_support_in_corpus',
 unknown='Endpoint và đặc tả JSON từng trường, kiểu dữ liệu, cấu trúc thông điệp.',context='N14.3.b N4.4 N12.2',note='Nghị định cho phép API và liệt kê nội dung pháp lý hồ sơ; không ban hành URL, tên trường JSON hoặc schema kỹ thuật. Các nội dung pháp lý không đủ để suy ra hợp đồng API.')],
 quality='Nhu cầu kỹ thuật cụ thể, có liên quan pháp lý nhưng không thể suy endpoint từ quy định cho phép API.')

item(25,
 ['Có phải cấp độ 2 chỉ vì có người tham gia thực tế'],
 ['Đối tượng theo tiêu chí, địa điểm và thời hạn rõ','Kết quả không dùng thực tế, không cung cấp cho người dùng hay quyết định','Đã loại trừ cấp độ 3'],[],
 ['Đánh giá lại điều kiện cấp độ 3 đã giả thiết'],
 'Đơn vị đề xuất thử nghiệm','Thử nghiệm có người nhưng đầu ra không dùng thực tế',[
 aspect('Cấp độ 2 cần đồng thời người thực và việc dùng kết quả thực tế cùng điều kiện loại trừ cấp 3; người tham gia thật riêng lẻ chưa đủ.','N22.4'),
 aspect('Theo các dữ kiện đã nêu, phù hợp cấp độ 1; cơ quan có thẩm quyền xác định cấp độ khi nhận và xử lý hồ sơ.','N22.5 N22.6')],
 applicability=True,quality='Phân biệt AND của điều kiện cấp độ 2 với dấu hiệu đơn lẻ; có đủ dữ kiện cho kết luận cấp độ 1 trong phạm vi câu hỏi.')

item(26,
 ['Tổ chức AI hỗ trợ nghiên cứu trong lab khép kín'],
 ['Không người tham gia thực tế','Không đưa kết quả ra ngoài','AI hỗ trợ viết và thử ý tưởng nghiên cứu'],
 ['Nguồn dữ liệu và mức rủi ro của hệ thống'],
 ['Thủ tục sandbox ngoài phạm vi','Giấy phép chuyên ngành','Quyền tác giả phần AI tạo'],
 'Viện nghiên cứu','Nghiên cứu nội bộ khép kín',[
 aspect('Hoạt động khép kín không có người thử nghiệm thực tế và không tác động bên ngoài không thuộc cơ chế sandbox của Nghị định.','N21.3'),
 aspect('Dù không thuộc sandbox, nghiên cứu vẫn phải tuân thủ đạo đức, liêm chính, phòng ngừa gian lận và đạo văn.','L6.3'),
 aspect('Nội dung tạo ra trong nghiên cứu/thử nghiệm có kiểm soát không cung cấp công cộng thuộc ngoại lệ gắn nhãn hiển thị; không suy ra miễn toàn bộ minh bạch hay an toàn.','N18.4.d'),
 aspect('Bảo đảm an toàn, an ninh, độ tin cậy và phát hiện, khắc phục sự cố có thể gây hại trong phạm vi hoạt động nghiên cứu.','L12.1',origin='scope_necessary')],
 broad=True,applicability=True,quality='Phạm vi tổ chức lab hữu hạn; tách ngoại lệ sandbox/nhãn khỏi nghĩa vụ nghiên cứu và an toàn chung.')

item(27,
 ['Định hướng ưu tiên mua sắm công công nghệ huấn luyện hiệu năng cao','Tỷ lệ ưu đãi giá chính xác của hồ sơ dự thầu'],
 ['Doanh nghiệp phát triển công nghệ huấn luyện hiệu năng cao','Muốn bán cho cơ quan nhà nước'],
 ['Gói thầu và điều kiện ưu đãi theo luật đấu thầu'],
 ['Tính ưu đãi từ văn bản đấu thầu ngoài corpus'],
 'Doanh nghiệp công nghệ và cơ quan mua sắm','Công nghệ huấn luyện hiệu năng cao',[
 aspect('Công nghệ huấn luyện hiệu năng cao thuộc hướng ưu tiên; các cơ quan được quy định ưu tiên bố trí, sử dụng sản phẩm/giải pháp trong mua sắm công theo pháp luật đấu thầu.','N37.2.c N37.3.d'),
 aspect('Không có tỷ lệ phần trăm ưu đãi giá dự thầu cụ thể trong corpus.',status='no_support_in_corpus',unknown='Phần trăm ưu đãi giá chính xác áp dụng cho hồ sơ dự thầu.',context='L20.2.a N37.4 N38.2.b',note='Các điều mua sắm chỉ nêu chính sách ưu tiên và dẫn chiếu luật đấu thầu/ưu đãi; không có biểu phần trăm và điều kiện tính ưu đãi giá.')],
 applicability=True,quality='Phân biệt định hướng ưu tiên với quyền hưởng một tỷ lệ cụ thể, không suy doanh nghiệp chắc chắn trúng thầu.')

item(28,
 ['Tổ chức giao diện dịch vụ công dễ tiếp cận','Giúp dân hiểu khả năng AI','Có đầu mối phản ánh trở ngại'],
 ['Dịch vụ công','Người cao tuổi và vùng kết nối kém phải sử dụng'],
 ['Chủ thể vận hành cụ thể','Có dùng kết quả làm quyết định hành chính không'],
 ['Tự suy nghĩa vụ đánh giá tác động khi chưa đủ điều kiện','Chọn công nghệ giao diện cụ thể'],
 'Đơn vị phát triển/triển khai dịch vụ công','AI giao diện cho nhóm dễ tổn thương',[
 aspect('Khung đạo đức áp dụng cho chủ thể phát triển, cung cấp, triển khai, sử dụng AI phục vụ dịch vụ công; ưu tiên giao diện dễ tiếp cận, dễ dùng để thu hẹp khoảng cách số.','T1.2 T3.3.b'),
 aspect('Nhận diện, giảm thiểu thiên lệch dữ liệu/mô hình/vận hành, xem xét tác động đến người cao tuổi và nhóm yếu thế.','T3.2.b'),
 aspect('Thông báo việc dùng AI, mô tả hợp lý mục tiêu, phạm vi, cách hoạt động và giới hạn để không gây hiểu nhầm năng lực.','T3.2.c'),
 aspect('Phân định trách nhiệm, có đầu mối tiếp nhận xử lý khiếu nại và cơ chế phát hiện lỗi, khắc phục/dự phòng.','T3.4.b T3.1.d')],
 broad=True,applicability=True,quality='Yêu cầu thiết kế tiếp cận và phản ánh có phạm vi rõ; Thông tư đủ hỗ trợ toàn bộ, không buộc D4 chỉ vì Luật cũng liên quan.',d4='Toàn bộ phạm vi hỗ trợ bằng T1 và T3; Luật hoặc Nghị định không cần thiết như văn bản thứ hai.')

item(29,
 ['Xác định ngày bắt đầu thời gian chuyển tiếp 12 tháng khi đổi chức năng thành cao'],
 ['Đổi chức năng khiến phải phân loại lại cao','Không có quyết định mới sửa danh mục'],
 ['Không có ngày hiệu lực quyết định danh mục tương ứng'],
 ['Tự sửa điểm dẫn chiếu của văn bản','Tự lấy ngày đổi chức năng làm ngày bắt đầu'],
 'Nhà cung cấp/bên triển khai đổi chức năng','Phân loại lại cao do thay đổi chức năng',[
 aspect('N11.5 nêu tối đa 12 tháng và dẫn trường hợp N11.1.a, nhưng lại tính từ hiệu lực quyết định sửa danh mục; không thể xác định ngày bắt đầu cho dữ kiện không có quyết định đó.','N11.5 N11.1.a N11.1.c',status='partial_support',app='uncertain',
 condition='Mốc hiệu lực quyết định sửa danh mục để tính chuyển tiếp.',unknown='Ngày bắt đầu và khả năng áp dụng thực tế của chuyển tiếp 12 tháng trong trường hợp không có quyết định sửa danh mục.',
 note='CONFLICT: câu dẫn điểm a (đổi chức năng) trong N11.5 không khớp mốc hiệu lực quyết định danh mục (điểm c). Giữ nguyên văn bản, không tự chữa thành điểm c hoặc đặt mốc mới.')],
 applicability=True,admission='NEEDS_ADJUDICATION',quality='Bất nhất nội tại ảnh hưởng trực tiếp kết luận được hỏi; cần adjudication pháp lý trước admission/freeze, không dùng suy đoán sửa luật.')

item(30,
 ['Kế hoạch chuyển tiếp cho hệ thống giáo dục đã vận hành','Thông báo và công khai nếu cổng AI chưa vận hành'],
 ['Trường công dùng AI giáo dục từ tháng 2/2026','Giả thiết cổng chưa được công bố vận hành'],
 ['Phân loại rủi ro và chức năng cụ thể','Phương thức tiếp nhận thay thế được Bộ công bố'],
 ['Tự đoán địa chỉ cổng thay thế','Ấn định nghĩa vụ thông báo cho mọi hệ thống bất kể phân loại'],
 'Trường công và nhà cung cấp','AI giáo dục vận hành trước hiệu lực Luật',[
 aspect('Luật hiệu lực 1/3/2026; hệ thống giáo dục đã vận hành trước đó có thời hạn tuân thủ 18 tháng từ hiệu lực.','L34 L35.1.a'),
 aspect('Trong chuyển tiếp được tiếp tục hoạt động, nhưng cơ quan quản lý có thể yêu cầu tạm dừng/chấm dứt khi xác định nguy cơ thiệt hại nghiêm trọng.','L35.2'),
 aspect('Khi phát sinh thủ tục thông báo/báo cáo mà cổng AI chưa vận hành chính thức, dùng hệ thống điện tử/dịch vụ công hoặc phương thức Bộ công bố; giá trị pháp lý tương đương.','N46.1',condition='Chỉ những thông báo/báo cáo thuộc nghĩa vụ áp dụng; không tự kết luận mọi AI đều phải thông báo.',context='N14.1'),
 aspect('Trong giai đoạn cổng chưa vận hành, công khai trên cổng/trang chính thức của đơn vị có trách nhiệm, trừ quy định khác.','N46.2')],
 broad=True,applicability=True,quality='Phạm vi chỉ chuyển tiếp và kênh thực hiện; giữ ngoại lệ nguy cơ nghiêm trọng, không giả định mức rủi ro chưa cho.')

item(31,
 ['Gửi thông báo trung bình tự động','Cấp mã và xác nhận','Giới hạn yêu cầu bổ sung tài liệu'],
 ['Nhà cung cấp đã hoàn thành hồ sơ phân loại trung bình'],
 ['Đặc tả kết nối kỹ thuật thực tế'],
 ['Endpoint/schema JSON','Phê duyệt lại phân loại của cơ quan'],
 'Nhà cung cấp','Hệ thống trung bình thông báo điện tử',[
 aspect('Có thể gửi thông tin tự động qua API hoặc phương thức điện tử phù hợp thay kê khai tay; nội dung theo hồ sơ Điều 12.','N14.2 N14.3.b'),
 aspect('Cổng tự động ghi nhận, cấp mã định danh và gửi xác nhận điện tử ngay sau khi hoàn tất gửi thông báo.','N14.4'),
 aspect('Khi tiếp nhận không được yêu cầu tài liệu/thành phần thông tin ngoài khoản 2; vẫn có thanh tra, kiểm tra, hậu kiểm, nhà cung cấp tự chịu trách nhiệm nội dung.','N14.4 N14.1')],
 quality='Thủ tục điện tử có căn cứ cụ thể; không nhầm xác nhận tự động với phê duyệt chất lượng hệ thống.')

item(32,
 ['Phạm vi công khai dữ liệu hệ thống thuộc bí mật nhà nước','Ngoại lệ công khai có miễn bảo vệ bí mật không'],
 ['AI dùng cho quản lý dân sự','Hệ thống thuộc danh mục bí mật nhà nước'],[],
 ['Suy ngoại lệ toàn bộ Luật từ chức năng quốc phòng','Xác minh quyết định xếp bí mật'],
 'Cơ quan quản lý dân sự','Hệ thống thuộc danh mục bí mật nhà nước',[
 aspect('Hệ thống thuộc danh mục bí mật nhà nước nằm ngoài phạm vi phải thông báo, đăng ký, chia sẻ dữ liệu công khai trên cổng AI.','N4.3.d'),
 aspect('Ngoại lệ công khai không miễn các yêu cầu bảo vệ bí mật nhà nước, an ninh mạng và cơ yếu đối với hoạt động liên quan.','N1.3 N4.3.b')],
 applicability=True,quality='Phân biệt ngoại lệ thông báo/công khai trên cổng và nghĩa vụ bảo vệ bí mật; không mở rộng thành miễn toàn bộ Luật.')

item(33,
 ['Cập nhật báo cáo tác động trước tiếp tục sử dụng','Chuẩn bị năng lực cán bộ vận hành'],
 ['Cơ quan dùng kết quả AI làm căn cứ trực tiếp quyết định hành chính','Đổi nguồn dữ liệu chủ yếu, phát sinh rủi ro mới'],
 ['Nội dung dữ liệu được phép công khai'],
 ['Tự soạn toàn bộ Mẫu AI02 không có trong corpus','Mốc thời hạn ngoài quy định'],
 'Cơ quan nhà nước và cán bộ vận hành','AI làm căn cứ trực tiếp quyết định hành chính',[
 aspect('Phải đánh giá tác động bổ sung trước tiếp tục dùng khi đổi nguồn dữ liệu đầu vào chủ yếu làm phát sinh rủi ro mới.','N20.1.b N20.2 N20.7.a'),
 aspect('Báo cáo theo AI02 mô tả hệ thống/mục tiêu, nhận diện rủi ro, kiểm soát giảm thiểu và giám sát/can thiệp con người; người đứng đầu tổ chức lập, phê duyệt, chịu trách nhiệm trung thực đầy đủ.','N20.3 N20.4'),
 aspect('Công khai báo cáo trừ bí mật nhà nước, kinh doanh, dữ liệu cá nhân; AI không thay trách nhiệm quyết định của người có thẩm quyền.','N20.5 N20.6'),
 aspect('Đào tạo nhận thức, rủi ro đạo đức, kỹ năng sử dụng AI an toàn cho cán bộ; tăng cường hợp tác, học hỏi tiêu chuẩn đạo đức.','T1.2 T3.4.c')],
 applicability=True,quality='Đủ điều kiện cập nhật báo cáo trước dùng tiếp; phối hợp quy trình của Nghị định và năng lực nhân sự của Khung.')

item(34,
 ['Có được từ chối xem xét hỗ trợ chỉ vì chưa gửi mẫu điện tử'],
 ['Doanh nghiệp chia sẻ mô hình hợp pháp','Chưa dùng mẫu thông tin trên cổng'],
 ['Quy mô tài nguyên, tiêu chí và nguồn lực hỗ trợ'],
 ['Khẳng định chắc chắn được hỗ trợ'],
 'Doanh nghiệp chia sẻ mô hình','Hỗ trợ phi tài chính',[
 aspect('Việc cung cấp thông tin và dùng mẫu chỉ tự nguyện, không bắt buộc và không là điều kiện xem xét hỗ trợ; không được loại riêng vì chưa dùng mẫu.','N34.1 N34.6')],
 applicability=True,quality='Phân biệt điều kiện xem xét với công cụ hỗ trợ; không suy đủ điều kiện nhận hỗ trợ chỉ từ chia sẻ hợp pháp.')

item(35,
 ['Đầu mối liên hệ đã đủ thay hiện diện thương mại/đại diện ủy quyền chưa'],
 ['Nhà cung cấp nước ngoài cung cấp AI cao tại Việt Nam','Có đầu mối liên hệ hợp pháp','Chưa biết có bắt buộc chứng nhận'],
 ['Tình trạng thuộc danh mục chứng nhận bắt buộc'],
 ['Tự xác định danh mục không được cung cấp','Tư vấn điều kiện đầu tư khác'],
 'Nhà cung cấp nước ngoài','AI cao chưa biết điều kiện chứng nhận',[
 aspect('Đầu mối hợp pháp đáp ứng yêu cầu chung cho nhà cung cấp nước ngoài có AI cao; nếu thuộc diện chứng nhận bắt buộc còn phải có hiện diện thương mại hoặc đại diện ủy quyền, nên chưa thể kết luận đầu mối hiện tại đã đủ.','L14.6',status='partial_support',app='uncertain',
 condition='Hệ thống có thuộc diện bắt buộc chứng nhận trước sử dụng không.',unknown='Kết luận đầu mối hiện tại đủ hay phải bổ sung hiện diện thương mại/đại diện ủy quyền.',
 note='Luật cho quy tắc điều kiện đầy đủ, nhưng kết luận cụ thể bị chặn bởi tình trạng chứng nhận chưa biết; không dùng tên danh mục để đoán điều kiện.')],
 applicability=True,quality='Câu hỏi về đủ điều kiện thực tế; Q giữ quy tắc điều kiện và U nêu dữ kiện thiếu, không khẳng định đã tuân thủ.')

item(36,
 ['Đưa trách nhiệm môi trường và lợi ích xã hội vào kế hoạch triển khai'],
 ['Đơn vị công lập thiết kế dịch vụ công','Dự kiến hạ tầng trong mạng lưới quốc gia','Có nhiều phương án tiêu thụ tài nguyên khác nhau'],
 ['Số liệu năng lượng/phát thải cụ thể'],
 ['Tính phát thải định lượng','Chứng nhận kỹ thuật môi trường ngoài corpus'],
 'Đơn vị phát triển dịch vụ công và vận hành hạ tầng','AI dịch vụ công trên mạng lưới quốc gia',[
 aspect('Áp dụng Khung cho dịch vụ công; xác định lợi ích công cộng, giá trị gia tăng, tác động tích cực và phương án khắc phục tác động tiêu cực trước triển khai.','T1.2 T3.3.a'),
 aspect('Xem xét năng lượng, tài nguyên tính toán và tác động môi trường suốt vòng đời; ưu tiên giải pháp, hạ tầng, vận hành tiết kiệm năng lượng, hạn chế phát thải.','T3.3.c'),
 aspect('Khi tham gia mạng lưới hạ tầng, tuân thủ sử dụng năng lượng tiết kiệm hiệu quả, triển khai giảm phát thải và không đe dọa an toàn hệ thống điện quốc gia.','N29.2.đ'),
 aspect('Tổ chức tiếp cận dễ dùng, thu hẹp khoảng cách số để lợi ích dịch vụ công có tính bao trùm.','T3.3.b',origin='scope_necessary')],
 broad=True,applicability=True,quality='Tách cân nhắc vòng đời của Khung với điều kiện vận hành hạ tầng quốc gia; không tự đặt chỉ tiêu phát thải.')

item(37,
 ['Nghĩa vụ kỹ thuật và thông báo của nhà phát triển khi sự cố nghiêm trọng'],
 ['Nhóm chỉ phát triển kỹ thuật, không bán hoặc triển khai'],
 ['Biện pháp kỹ thuật khắc phục cụ thể'],
 ['Thời hạn báo cáo của nhà cung cấp/bên triển khai khi vai trò không tương ứng'],
 'Nhà phát triển','Hệ thống xảy ra sự cố nghiêm trọng',[
 aspect('Nhà phát triển cũng thuộc chủ thể phải khẩn trương áp dụng biện pháp kỹ thuật khắc phục, tạm dừng/thu hồi và thông báo cơ quan có thẩm quyền khi sự cố nghiêm trọng; không chỉ nhà cung cấp.','L12.2.a',context='L12.1')],
 applicability=True,quality='Căn cứ Luật trực tiếp theo vai trò phát triển, không suy tên chủ thể báo cáo ở Nghị định xóa nghĩa vụ trong Luật.')

item(38,
 ['Chuẩn bị xử lý thiệt hại dù vận hành đúng','Phát hiện nguy cơ và phối hợp nhà cung cấp trước tổn thất'],
 ['Thuê AI cao để vận hành dịch vụ'],
 ['Thỏa thuận hoàn trả với nhà cung cấp','Tình tiết lỗi nạn nhân, bất khả kháng hay can thiệp trái phép'],
 ['Công thức và mức trần bồi thường','Tuyên bố phải mua bảo hiểm ngoài sandbox'],
 'Bên triển khai thuê hệ thống và nhà cung cấp','AI rủi ro cao',[
 aspect('Khi quản lý/vận hành/sử dụng đúng mà vẫn thiệt hại, bên triển khai bồi thường người bị thiệt hại; yêu cầu các bên hoàn trả sau đó nếu có thỏa thuận.','L29.2'),
 aspect('Xem xét miễn trừ khi hoàn toàn do lỗi cố ý của nạn nhân, bất khả kháng/tình thế cấp thiết theo giới hạn luật; bên thứ ba can thiệp trái phép chịu trách nhiệm, bên triển khai/nhà cung cấp có lỗi có thể liên đới.','L29.3 L29.4',app='conditional',condition='Chỉ áp dụng ngoại lệ khi có tình tiết tương ứng, chưa giả định xảy ra.'),
 aspect('Giám sát phát hiện sai lệch/rủi ro, duy trì can thiệp con người, hạn chế rủi ro và phối hợp nhà cung cấp cập nhật biện pháp.','N15.5'),
 aspect('Khi phát hiện nguy cơ thiệt hại nghiêm trọng, kịp thời hạn chế rủi ro trong quyền kiểm soát và thông báo nhà cung cấp cùng cơ quan có thẩm quyền.','N15.6'),
 aspect('Có thể bố trí bảo hiểm trách nhiệm hoặc biện pháp bảo đảm nghĩa vụ phù hợp khác theo chính sách khuyến khích.','L14.5',origin='scope_necessary')],
 broad=True,applicability=True,quality='Phạm vi quản trị trước/sau thiệt hại hữu hạn; giữ điều kiện hoàn trả, miễn trừ và phân biệt khuyến khích bảo hiểm.')

item(39,
 ['Định hướng Quỹ hỗ trợ đào tạo nhân lực','Ngân sách đào tạo thực tế đã phân bổ năm 2026'],
 ['Chuẩn bị dự án đào tạo AI'],
 ['Dự án và quyết định phân bổ ngân sách cụ thể'],
 ['Tự ước lượng ngân sách hoặc quyền được tài trợ'],
 'Đơn vị dự án đào tạo','Hỗ trợ từ Quỹ AI quốc gia',[
 aspect('Quỹ được ưu tiên dùng đầu tư, tài trợ, hỗ trợ đào tạo, bồi dưỡng và thu hút nhân lực AI.','L22.3.d'),
 aspect('Corpus không cho số ngân sách đã phân bổ đào tạo trong năm 2026.',status='no_support_in_corpus',unknown='Số tiền thực tế phân bổ cho đào tạo năm 2026.',context='L22.2 L22.3 L22.5 N41.9',note='Các quy định về nguồn Quỹ, ưu tiên và cơ chế tài chính không phải quyết định phân bổ; toàn corpus không chứa bảng ngân sách đào tạo theo năm.')],
 quality='Phân biệt định hướng được hỗ trợ và dữ liệu ngân sách thực tế; số tiền không được suy từ chức năng Quỹ.')

item(40,
 ['Thông tin phải công bố khi mở dữ liệu Nhà nước qua API','Có chuyển quyền sở hữu dữ liệu không'],
 ['Đơn vị vận hành cơ sở dữ liệu do Nhà nước đầu tư','Muốn cấp quyền khai thác qua API'],
 ['Loại dữ liệu và điều kiện truy cập được duyệt'],
 ['Tự công khai dữ liệu bị hạn chế','Endpoint hoặc cấu trúc API'],
 'Đơn vị vận hành dữ liệu Nhà nước','Khai thác cơ sở dữ liệu AI qua API',[
 aspect('Công bố danh mục dữ liệu, điều kiện/phạm vi/mục đích truy cập, yêu cầu kỹ thuật kết nối, phương thức tiếp cận và đầu mối hỗ trợ trên cổng AI, liên thông cổng dữ liệu.','N35.2'),
 aspect('API là một hình thức cung cấp dữ liệu hợp lệ; phải quản lý truy cập, theo dõi khai thác, kiểm soát mục đích và bảo đảm an toàn dữ liệu.','N35.3.a N35.4'),
 aspect('Quyền khai thác phải tôn trọng quyền sở hữu dữ liệu/sở hữu trí tuệ; việc cấp truy cập không tự chuyển quyền sở hữu cho người dùng.','N35.1 N35.5.c',context='N35.3.c')],
 applicability=True,quality='Phạm vi công bố đối với dữ liệu Nhà nước và quyền sử dụng có căn cứ; không lấy ngoại lệ môi trường an toàn làm căn cứ duy nhất cho API.')

item(41,
 ['Phối hợp xưởng sản xuất và đơn vị phát hành về thông tin/nhãn AI'],
 ['Xưởng mô phỏng giọng người thật trong phim','Giao bản dựng cho đơn vị phát hành','Hợp đồng để bên phát hành lo nhãn'],
 ['Hình thức phát hành cụ thể'],
 ['Quyền giọng nói hoặc quyền tác giả ngoài corpus','Tự coi xưởng là nhà cung cấp hệ thống AI'],
 'Bên tạo/chỉnh sửa tác phẩm và bên trực tiếp công khai','Phim mô phỏng giọng người thật',[
 aspect('Nội dung mô phỏng giọng người thật phải gắn nhãn dễ nhận biết; tính chất điện ảnh chỉ cho cách thể hiện phù hợp, không miễn nghĩa vụ.','N18.2.a N18.6'),
 aspect('Xưởng tạo/chỉnh sửa phải cung cấp thông tin cần cho nghĩa vụ nhãn; bên trực tiếp đưa ra công cộng thực hiện thông báo/nhãn trên cơ sở đó.','N18.6'),
 aspect('Có thể đặt nhãn mở đầu/kết thúc/danh đề/mô tả/tài liệu kèm theo; người tiếp nhận phải nhận biết rõ nguồn gốc, không che giấu hoặc gây nhầm lẫn.','N18.3 N18.6')],
 applicability=True,quality='Phân công nghĩa vụ theo chuỗi sản xuất/phát hành rõ, không suy thỏa thuận hợp đồng xóa nghĩa vụ cung cấp thông tin của xưởng.')

item(42,
 ['Chính sách lưu hồ sơ kỹ thuật/nhật ký và số năm sau dừng hệ thống','Tài liệu cung cấp khi thanh tra'],
 ['Nhà cung cấp AI cao'],
 ['Yêu cầu lưu trữ của pháp luật chuyên ngành'],
 ['Tự ấn định số năm lưu sau ngừng','Suy quyền thanh tra vô hạn với dữ liệu bí mật'],
 'Nhà cung cấp','AI cao và hồ sơ sau ngừng hoạt động',[
 aspect('Phải lập, cập nhật, lưu hồ sơ kỹ thuật/nhật ký ở mức cần cho đánh giá sự phù hợp và kiểm tra; hồ sơ phân loại lưu suốt thời gian hoạt động.','L14.1.c N12.6'),
 aspect('Khi thanh tra cung cấp hồ sơ kỹ thuật, nhật ký, dữ liệu huấn luyện và thông tin cần để xác định nguyên nhân/phân trách nhiệm; yêu cầu phải cần thiết, tương xứng và bảo vệ bí mật/dữ liệu cá nhân/sở hữu trí tuệ.','L28.3 L31.2 L31.3'),
 aspect('Không thể cho số năm bắt buộc lưu hồ sơ/nhật ký sau khi ngừng hoạt động từ corpus.',status='no_support_in_corpus',unknown='Thời hạn tính bằng năm phải lưu hồ sơ kỹ thuật và nhật ký sau ngừng hoạt động.',context='L14.1.c N12.6 N16.2.c N19.4',note='Corpus quy định mục đích lưu, lưu hồ sơ phân loại trong thời gian hoạt động và tài liệu sự cố; không ấn định số năm hậu vận hành được hỏi.')],
 quality='Phân biệt hồ sơ phân loại với hồ sơ kỹ thuật/nhật ký; không biến thời hạn hoạt động thành thời hạn lưu sau ngừng.')

item(43,
 ['Hồ sơ công nhận cụm liên kết','Cơ chế điều phối','Quyền lợi hạ tầng và đào tạo sau công nhận'],
 ['Có doanh nghiệp, trường và tổ chức hỗ trợ đổi mới sáng tạo','Đã thống nhất liên kết nghiên cứu AI'],
 ['Thỏa thuận đã thành văn bản và đầu mối điều phối cụ thể'],
 ['Bảo đảm chắc chắn được công nhận hay nhận tài trợ','Thành lập pháp nhân mới bắt buộc'],
 'Các thành viên liên kết và tổ chức đại diện','Cụm liên kết AI',[
 aspect('Đáp ứng ít nhất hai trong ba nhóm chủ thể, mục tiêu AI rõ, thỏa thuận/quy chế/đề án bằng văn bản về phối hợp, lợi ích và trách nhiệm, có đầu mối và phương thức điều phối.','N39.1'),
 aspect('Đại diện nộp một bộ điện tử qua cổng Dịch vụ công quốc gia gồm văn bản đề nghị, danh sách thành viên, thỏa thuận/quy chế/đề án và tài liệu chứng minh tiêu chí; Bộ KH&CN xét trong 15 ngày làm việc từ hồ sơ hợp lệ, không yêu cầu thêm thành phần.','N39.2 N39.3'),
 aspect('Cụm hoạt động tự nguyện, tự chủ, hợp tác; không đổi tư cách pháp lý hay quyền/nghĩa vụ độc lập của thành viên, không tạo cơ quan quản lý nhà nước nội bộ.','N39.4'),
 aspect('Thành viên cụm được công nhận được ưu tiên truy cập hạ tầng, dữ liệu, nền tảng thử nghiệm với chi phí ưu đãi và hỗ trợ tham gia đào tạo nhân lực; tiếp cận cụ thể theo cơ chế pháp luật.','L24.3 N39.5.a N39.5.b')],
 applicability=True,quality='Tách tiêu chí công nhận, hồ sơ, điều phối và quyền lợi; không suy thỏa thuận miệng đã đáp ứng tiêu chí văn bản.')

item(44,
 ['Trách nhiệm nhóm phát triển đối với đầu độc dữ liệu/mô hình theo Khung'],
 ['Nhóm được thuê phát triển AI phục vụ dịch vụ công','Cho rằng chỉ người vận hành máy chủ chịu trách nhiệm'],[],
 ['Phân định bồi thường cụ thể','Kỹ thuật tấn công hoặc phòng vệ chi tiết'],
 'Nhà phát triển thuê ngoài','AI phục vụ dịch vụ công',[
 aspect('Phạm vi Thông tư bao gồm nhà phát triển AI phục vụ dịch vụ công; nhóm phát triển cũng áp dụng biện pháp phù hợp phòng ngừa, phát hiện, ngăn chặn, ứng phó đầu độc dữ liệu/mô hình và bảo vệ tính bí mật, toàn vẹn, sẵn sàng.','T1.2 T3.1.e',context='T2.2 T2.3')],
 applicability=True,quality='Cần ghép phạm vi chủ thể với nghĩa vụ bảo vệ hệ thống; không giao độc quyền nghĩa vụ cho người vận hành máy chủ.')

item(45,
 ['Xử lý phần đánh giá nước ngoài chưa được thừa nhận','Công khai kết quả và lưu hồ sơ trước dùng tại Việt Nam'],
 ['Nhà cung cấp AI cao','Cơ quan có thẩm quyền đã thừa nhận một phần kết quả nước ngoài'],
 ['Phần được thừa nhận cụ thể','Thuộc diện chứng nhận bắt buộc không'],
 ['Tự công nhận toàn bộ báo cáo nước ngoài','Thủ tục thừa nhận ngoài corpus'],
 'Nhà cung cấp','AI cao với kết quả nước ngoài thừa nhận một phần',[
 aspect('Dùng phần đã được thừa nhận để chứng minh yêu cầu tương ứng; tiếp tục đánh giá phần chưa được đánh giá hoặc thừa nhận theo chế độ Điều 13.','N13.5'),
 aspect('Nếu thuộc diện chứng nhận bắt buộc phải qua tổ chức đánh giá đủ điều kiện; nếu không có thể tự đánh giá hoặc thuê, tự đánh giá phải lập hồ sơ kỹ thuật và chịu trách nhiệm.','N13.2',app='conditional',condition='Lựa chọn phương thức theo tình trạng chứng nhận bắt buộc chưa được cho; không kết luận một phương thức duy nhất.'),
 aspect('Trước dùng phải công khai tên/phiên bản/mã nếu có, thông tin nhà cung cấp, phương thức, tổ chức đánh giá nếu có, kết luận, thời điểm hoàn thành/thừa nhận và cập nhật gần nhất; duy trì sự phù hợp và cập nhật khi đánh giá lại.','N13.6'),
 aspect('Lập, cập nhật, lưu hồ sơ kỹ thuật/nhật ký để chứng minh sự phù hợp và kiểm tra; cung cấp cần thiết, tương xứng, bảo vệ bí mật.','L14.1.c')],
 applicability=True,quality='Phân biệt thừa nhận một phần với đủ điều kiện toàn hệ thống; giữ lựa chọn phương thức dưới điều kiện chưa biết.')

item(46,
 ['Quản trị trước triển khai AI xếp hạng trợ cấp để bảo đảm công bằng'],
 ['Cơ quan dùng xếp hạng hồ sơ hưởng trợ cấp','Đầu ra là căn cứ trực tiếp ký quyết định hành chính'],
 ['Phân loại rủi ro','Nhóm dữ liệu và tiêu chí xếp hạng cụ thể'],
 ['Kết luận danh mục rủi ro cao khi chưa có dữ kiện','Xác định quyền hưởng trợ cấp cá nhân'],
 'Cơ quan nhà nước và người có thẩm quyền quyết định','AI xếp hạng chính sách trợ cấp',[
 aspect('Hệ thống xếp hạng và xác định đối tượng hưởng chính sách làm căn cứ trực tiếp quyết định thuộc diện đánh giá tác động trước sử dụng; báo cáo phải được người đứng đầu tổ chức lập và phê duyệt.','N20.1.b N20.7.b N20.7.c N20.4'),
 aspect('Báo cáo mô tả hệ thống/mục tiêu, rủi ro, biện pháp giảm thiểu, giám sát và can thiệp; công khai trừ thông tin được bảo vệ.','N20.3 N20.5'),
 aspect('AI không thay thẩm quyền, trách nhiệm quyết định của con người; duy trì khả năng giám sát/can thiệp thực chất.','N20.6 L27.2 T3.1.c'),
 aspect('Áp dụng Khung để rà soát quyền riêng tư/quyền bình đẳng, nhận diện giảm thiên lệch dữ liệu/mô hình/vận hành, xét nhóm dễ tổn thương.','T1.2 T3.2.a T3.2.b'),
 aspect('Minh bạch mục tiêu, phạm vi và giới hạn AI; phân định trách nhiệm giải trình và đầu mối khiếu nại/khắc phục.','T3.2.c T3.2.d T3.4.b')],
 broad=True,applicability=True,quality='Nhu cầu công bằng bao gồm thủ tục đánh giá và biện pháp đạo đức cụ thể; phạm vi hữu hạn trước triển khai.')

item(47,
 ['Định hướng ưu tiên phần cứng AI','Thuế suất thu nhập doanh nghiệp cụ thể'],
 ['Doanh nghiệp nghiên cứu phần cứng phục vụ AI'],
 ['Điều kiện ưu đãi thuế và loại dự án'],
 ['Tự tính thuế theo luật ngoài corpus'],
 'Doanh nghiệp nghiên cứu','Phần cứng AI',[
 aspect('Phần cứng, vi mạch bán dẫn và công nghệ tính toán phục vụ AI thuộc nhóm công nghệ cốt lõi ưu tiên làm chủ.',alternatives=['N37.2.d','L18.1']),
 aspect('Không xác định được thuế suất thu nhập doanh nghiệp cụ thể từ corpus.',status='no_support_in_corpus',unknown='Thuế suất phần trăm áp dụng cho doanh nghiệp/dự án này.',context='N37.4 L20.1 L20.2.d',note='Quy định AI dẫn chiếu pháp luật thuế, đầu tư và hỗ trợ; không cung cấp thuế suất hoặc đầy đủ điều kiện hưởng thuế suất.')],
 quality='Nhu cầu ưu tiên và thuế tách biệt; không đồng nhất định hướng ưu tiên với mức thuế tự động.')

item(48,
 ['Chuẩn bị đưa lần đầu hệ thống hỗ trợ đánh giá học sinh vào sử dụng'],
 ['Nhà cung cấp sắp bán','Học sinh tương tác trực tiếp','Đã phân loại cao, không chứng nhận bắt buộc'],
 ['Độ tuổi, dữ liệu và môi trường triển khai cụ thể','Trường công hay tư'],
 ['Tự phân loại lại','Mặc định bắt buộc Khung dịch vụ công cho mọi trường','Yêu cầu giấy phép giáo dục ngoài corpus'],
 'Nhà cung cấp và bên triển khai giáo dục','AI cao hỗ trợ đánh giá học sinh',[
 aspect('Chuẩn bị hồ sơ phân loại và thông báo kết quả cao trước sử dụng theo nội dung hồ sơ Điều 12.','N12.1 N12.2 N14.1'),
 aspect('Được tự đánh giá sự phù hợp hoặc thuê tổ chức đủ điều kiện; tự đánh giá lập hồ sơ kỹ thuật/chịu trách nhiệm; duy trì và công khai kết quả trước dùng.','N13.2.b N13.6'),
 aspect('Thiết lập quản lý rủi ro, chất lượng dữ liệu, giám sát/can thiệp con người; bàn giao thông tin điều kiện an toàn, rủi ro và biện pháp cho bên triển khai.','N15.1 N15.2 N15.3'),
 aspect('Trong giáo dục phải phù hợp lứa tuổi/phát triển người học, phòng rủi ro đánh giá/phân loại và tác động đến học sinh, bảo vệ an toàn dữ liệu/quyền riêng tư.','L6.2.b'),
 aspect('Thiết kế/vận hành để học sinh nhận biết đang tương tác AI; chuẩn bị thông tin giới hạn, đầu mối phối hợp phát hiện/khắc phục sự cố theo vai trò.','L11.1 N16.2.b L12.1 L12.2')],
 broad=True,applicability=True,quality='Phạm vi trước dùng lần đầu gắn rủi ro cao và học sinh; không tự gán tư cách dịch vụ công hoặc ngưỡng kỹ thuật chưa nêu.')

item(49,
 ['Vai trò trường và doanh nghiệp phối hợp đào tạo thực hành','Trách nhiệm chia sẻ tri thức của trường'],
 ['Trường đại học và doanh nghiệp cùng xây dựng chương trình thực hành AI','Gắn nhu cầu sản xuất'],[],
 ['Thủ tục công nhận chương trình đào tạo','Tỷ lệ ưu đãi tài chính'],
 'Trường đại học và doanh nghiệp','Đào tạo nhân lực AI gắn thực tiễn',[
 aspect('Các bên tham gia phát triển nhân lực có trách nhiệm phối hợp đào tạo, nghiên cứu ứng dụng và thực hành nghề nghiệp, gắn đào tạo với nhu cầu thực tế; ưu đãi theo pháp luật.','L23.5'),
 aspect('Cơ sở giáo dục đại học có trách nhiệm hợp tác, chia sẻ tri thức và tham gia mạng lưới quốc gia/quốc tế về đào tạo, nghiên cứu, phát triển nhân lực AI.','L23.6',context='L23.3')],
 applicability=True,quality='Phân biệt trách nhiệm phối hợp và trách nhiệm chia sẻ của trường; không kéo nhiệm vụ ban hành chương trình của Bộ vào doanh nghiệp.')

item(50,
 ['Kiểm soát truy cập môi trường dữ liệu','Phân công bên quản lý và bên nghiên cứu khai thác','Ngăn nguy cơ tái nhận dạng dữ liệu'],
 ['Đơn vị quản lý cơ sở dữ liệu phục vụ AI','Nhóm nghiên cứu huấn luyện ngay trong môi trường đơn vị'],
 ['Loại dữ liệu và thỏa thuận truy cập'],
 ['Cam kết dữ liệu khử nhận dạng luôn an toàn','Đặc tả kỹ thuật an ninh ngoài corpus'],
 'Đơn vị quản lý và nhóm khai thác','Môi trường khai thác dữ liệu an toàn',[
 aspect('Có thể tạo môi trường an toàn để xử lý/huấn luyện tại hạ tầng chủ quản mà không làm đổi quyền sở hữu dữ liệu.','N35.3.c',origin='scope_necessary'),
 aspect('Bên quản lý thiết lập quản lý truy cập, ghi nhận/theo dõi, kiểm soát đúng mục đích/phạm vi và biện pháp bảo vệ dữ liệu.','N35.4'),
 aspect('Nhóm khai thác phải tuân thủ điều kiện, mục đích và phạm vi, không làm sai lệch hoặc dùng trái luật, tôn trọng quyền dữ liệu và quyền sở hữu trí tuệ.','N35.5 N36.2'),
 aspect('Bên quản lý bảo đảm bí mật/toàn vẹn/khả dụng, phòng phát hiện xử lý sự cố và kiểm soát nguy cơ tấn công mô hình, tái nhận dạng dữ liệu cá nhân đã khử nhận dạng.','N36.1 N36.3')],
 applicability=True,quality='Các trách nhiệm hai bên tách rõ; phạm vi an toàn không biến dữ liệu đã khử nhận dạng thành dữ liệu được khai thác vô điều kiện.')

item(51,
 ['Có loại toàn bộ hoạt động hỗn hợp quốc phòng/dân sự khỏi Luật AI được không'],
 ['Cùng hệ thống phục vụ quốc phòng và dịch vụ dân sự tại Việt Nam'],[],
 ['Phân định bí mật/kiến trúc kỹ thuật','Điều kiện ngành quốc phòng ngoài corpus'],
 'Đơn vị có hoạt động hỗn hợp','AI phục vụ quốc phòng và dân sự',[
 aspect('Không được loại toàn bộ hoạt động hỗn hợp chỉ vì có mục đích quốc phòng: ngoại lệ chỉ dành hoạt động AI chỉ phục vụ quốc phòng/an ninh/cơ yếu; phần hoạt động dân sự tại Việt Nam thuộc phạm vi chung.','L1.1 L1.2')],
 applicability=True,quality='Điều kiện chỉ phục vụ không đáp ứng; phân biệt ngoại lệ theo hoạt động với loại toàn hệ thống hỗn hợp.')

item(52,
 ['Số điều Bộ luật Hình sự và khung tù cho hành vi giả mạo AI gây hại'],
 ['Người cố ý dùng giả mạo gây hại nghiêm trọng','Yêu cầu chỉ dựa ba văn bản AI'],
 ['Tình tiết đầy đủ định tội theo Bộ luật Hình sự'],
 ['Chỉ xác định hành vi bị cấm','Suy tội danh và hình phạt ngoài corpus'],
 'Người vi phạm','Yêu cầu định tội và khung phạt tù',[
 aspect('Không thể xác định số điều Bộ luật Hình sự hoặc khung phạt tù tương ứng từ corpus AI.',status='no_support_in_corpus',
 unknown='Điều khoản Bộ luật Hình sự và khoảng hình phạt tù tương ứng.',context='L7.2.b L29.1 N19.7',note='Luật AI cấm giả mạo gây hại và dẫn chiếu xử lý hình sự tùy tính chất/mức độ; corpus không có Bộ luật Hình sự hay bảng đối chiếu tội danh/hình phạt.')],
 quality='Giữ hẹp nhu cầu điều khoản và khung tù; cấm hành vi chỉ là ngữ cảnh, không biến thành substantive credit cho định tội.')

item(53,
 ['Danh mục dữ liệu cốt lõi/quan trọng','Mã chính thức từng nhóm dữ liệu để đối chiếu thử nghiệm'],
 ['Dự kiến thử nghiệm AI và cần đối chiếu dữ liệu'],[],
 ['Thay danh mục bằng mô tả cấp độ thử nghiệm','Tự phân loại dữ liệu'],
 'Nhóm dự kiến thử nghiệm','Danh mục dữ liệu cốt lõi và quan trọng',[
 aspect('Corpus không chứa nội dung và mã chính thức của danh mục dữ liệu cốt lõi hoặc dữ liệu quan trọng.',status='no_support_in_corpus',
 unknown='Danh mục chính thức cùng mã từng nhóm dữ liệu cốt lõi/quan trọng.',context='N22.3.a N32.2.c L17.5',note='N22.3.a viện dẫn loại dữ liệu để xét cấp độ; N32/L17 nói danh mục bộ dữ liệu phục vụ AI, không phải bảng mã dữ liệu cốt lõi/quan trọng. Toàn corpus không ban hành danh mục được hỏi.')],
 applicability=True,quality='Tên các danh mục gần nhau có thể gây nhầm; bằng chứng chủ đề không cung cấp danh mục chính thức.')

item(54,
 ['Liêm chính khi công bố bản thảo có AI hỗ trợ','Ai đương nhiên sở hữu quyền tác giả phần AI tự tạo'],
 ['Viện dùng AI soạn bản thảo nghiên cứu'],
 ['Mức đóng góp con người, thỏa thuận và loại tác phẩm'],
 ['Dùng luật sở hữu trí tuệ ngoài corpus','Suy quyền sở hữu từ quyền sử dụng công cụ'],
 'Viện và người nghiên cứu','Bản thảo nghiên cứu có phần AI tạo',[
 aspect('Ứng dụng AI trong nghiên cứu phải bảo đảm đạo đức, liêm chính, phòng ngừa gian lận và đạo văn trong nghiên cứu và công bố.','L6.3'),
 aspect('Không thể xác định người đương nhiên sở hữu quyền tác giả phần AI tự tạo từ corpus.',status='no_support_in_corpus',unknown='Chủ thể mặc nhiên sở hữu quyền tác giả phần do AI tự tạo.',context='L7.3 L17.1 T3.4.a',note='Các quy định yêu cầu tuân thủ/bảo vệ sở hữu trí tuệ không thiết lập quy tắc tác giả hay chuyển quyền mặc nhiên cho nội dung AI. Không có quy tắc đó trong ba văn bản.')],
 quality='Phân biệt liêm chính có căn cứ với phân bổ quyền tác giả thiếu căn cứ; không trả lời chủ sở hữu bằng suy đoán.')

item(55,
 ['Công thức tính tiền và mức trần bồi thường tài sản trong quy định AI'],
 ['Tài sản bị AI làm hỏng','Chỉ hỏi cách tính tiền'],
 ['Giá trị thiệt hại và tình tiết dân sự'],
 ['Ai có trách nhiệm bồi thường','Tự tính theo Bộ luật Dân sự ngoài corpus'],
 'Người bị thiệt hại tài sản','Định lượng bồi thường',[
 aspect('Corpus không ấn định công thức hoặc mức trần tiền bồi thường tài sản được hỏi.',status='no_support_in_corpus',unknown='Công thức tính và trần tiền bồi thường tài sản.',context='L29.1 L29.2 L29.3 L29.4 N3.3',note='L29 phân trách nhiệm/ngoại lệ và dẫn chiếu pháp luật dân sự; N3.3 là giá trị chịu rủi ro của sandbox, không phải công thức bồi thường hay trần. Rà soát toàn corpus không thấy quy tắc lượng hóa yêu cầu.')],
 quality='Giữ đúng giới hạn chỉ tính tiền; không kéo phân định người bồi thường vào nội dung yêu cầu để gán partially_answerable.')

item(56,
 ['Mức phạt tiền tối thiểu và tối đa cho cố ý xóa nhãn AI bắt buộc'],
 ['Doanh nghiệp cố ý xóa nhãn bắt buộc khỏi video công khai'],
 ['Văn bản xử phạt chuyên biệt và tình tiết áp dụng'],
 ['Chỉ xác nhận hành vi bị cấm','Lấy trần hỗ trợ hoặc chế tài khác làm mức phạt'],
 'Doanh nghiệp vi phạm','Định lượng phạt hành chính xóa nhãn AI',[
 aspect('Không thể xác định mức phạt tiền tối thiểu/tối đa riêng cho hành vi này từ corpus.',status='no_support_in_corpus',unknown='Khoảng tiền phạt tối thiểu và tối đa cho hành vi cố ý xóa nhãn bắt buộc.',context='L7.5 L29.1 L29.5 N18',note='L7.5 cấm xóa nhãn; L29.5 giao Chính phủ quy định xử phạt; Nghị định trong corpus quy định nhãn nhưng không có bảng mức phạt cho hành vi. Không suy số tiền từ điều cấm.')],
 quality='Yêu cầu định lượng chế tài rõ ràng; ngữ cảnh điều cấm không đủ trả lời khoản tiền.')

item(57,
 ['Khung đạo đức có bắt buộc với cửa hàng tư nhân chỉ dùng AI kinh doanh thông thường'],
 ['Cửa hàng tư nhân','Không quản lý nhà nước hoặc cung cấp dịch vụ công'],[],
 ['Miễn nghĩa vụ trong Luật/Nghị định khác','Xác định rủi ro hệ thống'],
 'Cửa hàng tư nhân','AI kinh doanh thông thường',[
 aspect('Phạm vi áp dụng bắt buộc của Thông tư gắn quản lý nhà nước/dịch vụ công; cửa hàng trong dữ kiện chỉ được khuyến khích áp dụng, không bắt buộc chỉ vì dùng AI.','T1.2 T1.3')],
 applicability=True,quality='Giới hạn kết luận vào Thông tư và mục đích hoạt động; không suy mọi trách nhiệm AI đều tự nguyện.')

item(58,
 ['Dùng tài liệu quốc tế khi không có dữ liệu huấn luyện thô','Thỏa thuận cần có với bên cung cấp mô hình'],
 ['Đóng gói mô hình bên khác thành dịch vụ mang thương hiệu mình','Đã phân loại trung bình','Không có quyền truy cập dữ liệu thô'],
 ['Nội dung tài liệu đối tác có đáp ứng yêu cầu hồ sơ không'],
 ['Bắt buộc lấy mã nguồn/dữ liệu thô bất chấp quyền tiếp cận','Kết luận tài liệu hiện có đương nhiên đủ'],
 'Nhà cung cấp hệ thống tích hợp và nhà cung cấp mô hình','AI trung bình dựa mô hình bên thứ ba',[
 aspect('Công ty là nhà cung cấp theo thương hiệu, phải lập hồ sơ phân loại trung bình; thông tin kỹ thuật/dữ liệu bên thứ ba chỉ trong quyền tiếp cận và kiểm soát hợp pháp.','L3.4 N12.1 N12.3'),
 aspect('Hồ sơ không bắt buộc tiết lộ dữ liệu huấn luyện thô/mã nguồn/tham số/thuật toán chi tiết/bí mật, trừ pháp luật có quy định khác; có thể dùng tài liệu quốc tế tương đương nếu đủ nội dung thông tin yêu cầu.','N12.4 N12.5',condition='Tài liệu quốc tế phải bao phủ đầy đủ nội dung theo N12.2–3; chưa xác nhận tài liệu thực tế đã đủ.',context='N12.2'),
 aspect('Phải thỏa thuận với bên cung cấp mô hình để phối hợp cung cấp thông tin kỹ thuật cần cho minh bạch, giải trình.','N16.6')],
 applicability=True,quality='Tách giới hạn tiếp cận hợp pháp với yêu cầu hồ sơ và phối hợp thông tin; không buộc tiết lộ tài sản kỹ thuật bị bảo vệ.')

item(59,
 ['Chuẩn bị thông tin xin hỗ trợ phi tài chính khi chia sẻ dữ liệu','Mẫu có bắt buộc không','Có phải báo cáo định kỳ không'],
 ['Cá nhân chia sẻ bộ dữ liệu hợp pháp','Muốn hỗ trợ phi tài chính'],
 ['Quy mô dữ liệu và nhu cầu hỗ trợ cụ thể'],
 ['Cam kết được hỗ trợ','Tự đặt báo cáo định kỳ'],
 'Cá nhân chia sẻ dữ liệu','Cơ chế hỗ trợ phi tài chính',[
 aspect('Nếu cung cấp thông tin, mô tả tài nguyên/kỹ thuật/phạm vi; quyền sở hữu hoặc sử dụng hợp pháp và cam kết tuân thủ; nhu cầu loại tài nguyên, mục đích, quy mô và thời gian hỗ trợ.','N34.2'),
 aspect('Cung cấp qua cổng và dùng mẫu đều tự nguyện, không là thủ tục hoặc điều kiện để được xem xét hỗ trợ.','N34.1 N34.6'),
 aspect('Dùng hỗ trợ đúng mục đích và phối hợp cung cấp kết quả khi cần đánh giá hiệu quả; không phát sinh chế độ báo cáo định kỳ hay nghĩa vụ hành chính thường xuyên.','N34.5')],
 applicability=True,quality='Ba nghĩa vụ/thủ tục được hỏi hữu hạn; không đồng nhất phối hợp cung cấp thông tin khi cần với báo cáo định kỳ.')

item(60,
 ['Phương án chia sẻ mô hình tiếng dân tộc thiểu số có trách nhiệm','Tìm hỗ trợ hạ tầng'],
 ['Nhóm chia sẻ mô hình cho cộng đồng nghiên cứu tái sử dụng','Tự nguyện theo Khung đạo đức'],
 ['Quyền đối với mô hình/dữ liệu và phạm vi giấy phép','Nguồn lực hỗ trợ khả dụng'],
 ['Cấp quyền khi chưa có quyền hợp pháp','Hứa mức tiền hỗ trợ hoặc hạ tầng chắc chắn'],
 'Nhóm chia sẻ mô hình','Mô hình tiếng dân tộc thiểu số và hỗ trợ phi tài chính',[
 aspect('Chia sẻ hợp pháp tự nguyện có thể được xem xét hỗ trợ phi tài chính về hạ tầng và dịch vụ kỹ thuật trong nguồn lực hiện có; mức độ phục vụ tiếng dân tộc thiểu số là một tiêu chí, không bảo đảm tự động được cấp.','N33.1 N33.2 N33.3.d'),
 aspect('Chia sẻ/hỗ trợ không đổi quyền sở hữu, sở hữu trí tuệ và khai thác hợp pháp, không giao dịch trái luật và không quy đổi hỗ trợ thành tiền/tương đương tiền.','N33.4'),
 aspect('Có thể cung cấp mô tả tài nguyên, quyền hợp pháp và nhu cầu hỗ trợ trên cổng; thông tin/mẫu tự nguyện, không là điều kiện được xem xét.','N34.1 N34.2 N34.6'),
 aspect('Theo Khung tự nguyện, thúc đẩy nghiên cứu mở/chia sẻ tri thức phù hợp luật và quyền sở hữu trí tuệ; tôn trọng văn hóa, tránh nội dung kỳ thị hay gây hại cộng đồng.','T1.3 T3.4.a T3.3.d',condition='Đây là thực hành Khung tự nguyện đã lựa chọn, không gán nghĩa vụ bắt buộc dịch vụ công.'),
 aspect('Cung cấp thông tin hợp lý về mục tiêu, phạm vi và giới hạn mô hình, phân định trách nhiệm và đầu mối tiếp nhận phản ánh/khắc phục.','T3.2.c T3.4.b',origin='scope_necessary',condition='Trong phương án chủ động áp dụng Khung đạo đức.')],
 broad=True,applicability=True,quality='Kết hợp cơ chế chia sẻ, quyền tài nguyên và Khung tự nguyện; không suy ưu tiên ngôn ngữ thành quyền nhận hỗ trợ vô điều kiện.')
