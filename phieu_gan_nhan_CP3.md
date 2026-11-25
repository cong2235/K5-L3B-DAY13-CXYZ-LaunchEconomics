# Phiếu gắn nhãn CP3 · Người gắn nhãn 1

Người gắn nhãn: Trương Anh Đức (N1) · Bắt đầu lúc: ____ · Kết thúc lúc: ____

Tài liệu nháp nội bộ, không nằm trong thư mục nộp. Nguồn: `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, mục "Hai mươi ca lỗi".

**Luật:** 8 phút, gắn độc lập cả 20 ca, không trao đổi với N2, không xem bảng nhãn tham khảo trong hướng dẫn. Đã so nhãn xong thì **không sửa** bộ nhãn này. Gắn theo **nguyên nhân gốc**, không theo chỗ cần sửa.

## Năm loại lỗi (Google PAIR)

| Mã | Loại | Nghĩa là |
| --- | --- | --- |
| **ND** | Do người dùng | Người dùng nhập sai hoặc chọn sai |
| **HT** | Hệ thống | Hệ thống trả lời sai hoặc làm sai so với thiết kế và chính sách |
| **NC** | Ngữ cảnh | Hệ thống làm đúng thiết kế nhưng người dùng thấy là sai, vì giả định của hệ thống không khớp hoàn cảnh của họ |
| **GH** | Giới hạn hệ thống | Hệ thống không thể trả lời, do thiếu dữ liệu, ngoài phạm vi, hoặc dạng đầu vào không xử lý được |
| **NG** | Ngầm | Có sai nhưng cả người dùng lẫn hệ thống đều không nhận ra |

## Hai mươi ca lỗi

Ghi một mã vào cột **Nhãn**. Cột **Ghi chú** để ghi lý do ngắn nếu phân vân, dùng khi thống nhất với N2.

| Ca | Mô tả | Nhãn | Ghi chú |
| --: | --- | :---: | --- |
| 1 | Khách nhập số tài khoản nhận hoàn tiền thiếu hai chữ số. Trợ lý tạo lệnh hoàn, ngân hàng trả về lỗi. | **ND** | Người dùng nhập thiếu số tài khoản. Phân vân: nếu chính sách/thiết kế bắt buộc trợ lý phải validate số tài khoản trước khi tạo lệnh thì có thể xếp HT vì thiếu kiểm tra. **Chốt ND.** |
| 2 | Kiện nội địa 28 kg. Trợ lý gọi tool tra bảng giá với tham số hàng thường thay vì hàng nặng, hoàn thiếu 45.000 đ. Khách mở lại sau 2 ngày. | **HT** | Trợ lý gọi tool sai tham số: "hàng thường" thay vì "hàng nặng", dẫn tới hoàn thiếu. Lỗi hệ thống. |
| 3 | Theo thiết kế, trợ lý hoàn tiền về ví LogiX trong 5 phút. Khách chờ tiền về tài khoản ngân hàng và báo "chưa được hoàn". | **NC** | Hệ thống đúng thiết kế: hoàn về ví LogiX trong 5 phút. Khách giả định hoàn về tài khoản ngân hàng nên thấy sai. |
| 4 | Khách yêu cầu hoàn phí cho chặng do hãng nước ngoài giao. LogiX không có dữ liệu chặng này. Trợ lý nói không xác định được trạng thái và chuyển cho nhân viên. | **GH** | Thiếu dữ liệu chặng do hãng nước ngoài giao; trợ lý nói không xác định được và chuyển nhân viên. Đúng hướng xử lý giới hạn. |
| 5 | Kiểm tra mẫu cuối tuần thấy 14 đơn có mã giảm giá bị hoàn theo giá trước giảm, thừa trung bình 12.000 đ mỗi đơn. Không khách nào báo, không cảnh báo nào kích. | **NG** | Hoàn theo giá trước giảm cho 14 đơn, không khách nào báo, không cảnh báo. Lỗi âm thầm cả người dùng và hệ thống không nhận ra. |
| 6 | Khách chọn mục "Hoàn phí giao trễ" nhưng nội dung mô tả hàng bị vỡ. Trợ lý xử lý theo luồng giao trễ và từ chối vì đơn giao đúng hạn. | **ND** | Khách chọn nhầm mục "Hoàn phí giao trễ" trong khi nội dung là hàng vỡ. Lỗi gốc do người dùng chọn sai. |
| 7 | API sổ cái trả lỗi 503 ở bước ghi hoàn tiền. Trợ lý thử lại 3 lần rồi vẫn báo khách "đã hoàn tiền thành công". | **HT** | API sổ cái lỗi 503 nhưng trợ lý vẫn báo "đã hoàn tiền thành công". Hệ thống báo sai so với thực tế. |
| 8 | Trợ lý dẫn "Điều 7.2 chính sách hoàn phí" làm căn cứ. Bản chính sách hiện hành không có điều 7.2. Số tiền hoàn vẫn đúng. | **HT** | Trợ lý dẫn "Điều 7.2" không tồn tại. Số tiền đúng nhưng căn cứ sai — lỗi hệ thống. |
| 9 | Khách nhập mã đơn của sàn thương mại điện tử thay vì mã vận đơn. Trợ lý báo "mã không hợp lệ" rồi dừng, không gợi ý gì. | **ND** | Khách nhập mã đơn sàn TMĐT thay vì mã vận đơn. Trợ lý báo không hợp lệ là đúng; có thể cải thiện gợi ý nhưng gốc lỗi là người dùng nhập sai. |
| 10 | Đơn giao trễ do bão. Trợ lý từ chối hoàn theo điều khoản bất khả kháng, đúng chính sách. Khách thấy vô lý vì ứng dụng vẫn hiện "cam kết giao 24 giờ". | **NC** | Trợ lý từ chối hoàn do bất khả kháng, đúng chính sách. Khách thấy vô lý vì ứng dụng vẫn hiện "cam kết giao 24 giờ" — bất khớp giữa chính sách và kỳ vọng/UI. |
| 11 | Khách gửi tin nhắn thoại 40 giây. Trợ lý không xử lý được âm thanh, trả lời "vui lòng nhập bằng chữ". | **GH** | Đầu vào là tin nhắn thoại, hệ thống không xử lý được âm thanh. Giới hạn dạng đầu vào. |
| 12 | Tool tra đơn của depot D05 trả thiếu một trường. Trợ lý vẫn ra kết quả đúng sau nhiều lần gọi, nên tiền token của D05 gấp 3 lần depot khác suốt 3 tuần mà không ai thấy. | **NG** | Tool trả thiếu trường khiến trợ lý gọi lại nhiều lần, token D05 gấp 3 lần suốt 3 tuần mà không ai thấy. Kết quả cuối đúng nhưng có lỗi vận hành âm thầm. |
| 13 | Khách hỏi hoàn phí bảo hiểm hàng hoá, sản phẩm của công ty bảo hiểm đối tác, ngoài phạm vi trợ lý. Trợ lý trả lời chung chung về phí vận chuyển, không nói rõ là mình không xử lý được. | **GH** | Câu hỏi về bảo hiểm hàng hóa của đối tác nằm ngoài phạm vi. Trợ lý đáng lẽ phải nói rõ không xử lý được; mình chọn GH vì gốc là ngoài phạm vi. Phân vân: nếu chấm theo "trả lời sai" có thể xếp HT. **Chốt GH.** |
| 14 | Khách bấm nhầm "Xác nhận đã nhận tiền" khi chưa nhận. Yêu cầu bị đóng. | **ND** | Khách bấm nhầm "Xác nhận đã nhận tiền". Lỗi gốc do người dùng. |
| 15 | Đơn trễ 26 giờ. Chính sách: trễ 24–48 giờ hoàn 50%. Trợ lý tính hoàn 100%. Nhân viên xem lại bắt được trước khi gửi. | **HT** | Đơn trễ 26 giờ, chính sách hoàn 50% nhưng trợ lý tính 100%. Sai so với chính sách, dù nhân viên bắt được trước khi gửi. |
| 16 | Theo thiết kế "gửi ngay khi xong", trợ lý gửi thông báo hoàn tiền qua Zalo lúc 2:14 sáng. Khách phản ánh bị làm phiền. | **NC** | Hệ thống gửi ngay khi xong theo đúng thiết kế, nhưng gửi Zalo lúc 2:14 sáng nên khách thấy bị làm phiền. Thiết kế không khớp hoàn cảnh người dùng. |
| 17 | Bảng giá đổi từ ngày 01/11 nhưng trợ lý vẫn dùng bản cũ trong bộ nhớ đệm cho đơn dưới 2 kg. Lệch 1.000–2.000 đ mỗi đơn, 212 đơn trong 9 ngày, không ai mở lại. | **NG** | Dùng bảng giá cũ trong bộ nhớ đệm, lệch 1.000–2.000 đ/đơn, 212 đơn trong 9 ngày, không ai mở lại. Lỗi âm thầm. Gốc kỹ thuật: cache cũ — nếu bị phát hiện thì là HT. **Chốt NG.** |
| 18 | Trợ lý tính đúng: phí giao 30.000 đ, hoàn 50%. Tin nhắn chỉ ghi "Đã hoàn 15.000 đ", không kèm cách tính. Khách cho là hoàn thiếu và mở lại yêu cầu. | **NC** | Trợ lý tính đúng 15.000 đ nhưng tin nhắn không kèm cách tính. Khách hiểu là hoàn thiếu và mở lại. Hệ thống đúng số tiền nhưng thiếu ngữ cảnh giải thích. |
| 19 | Khách yêu cầu hoàn phí cho đơn từ 14 tháng trước. Trợ lý chỉ truy cập được dữ liệu 12 tháng. Trợ lý nói rõ không tra được và chuyển cho nhân viên kèm tóm tắt. | **GH** | Đơn 14 tháng trước, hệ thống chỉ tra được 12 tháng. Trợ lý nói rõ không tra được và chuyển nhân viên kèm tóm tắt — đúng xử lý giới hạn dữ liệu. |
| 20 | Khách gửi lại yêu cầu sau 10 phút vì chưa thấy phản hồi. Trợ lý hoàn hai lần cho cùng một đơn vì lệnh thứ hai không có khoá chống trùng. | **HT** | Lệnh hoàn thứ hai không có khoá chống trùng nên hoàn hai lần cùng một đơn. Lỗi hệ thống. |

Đếm nhanh (để tự soát đã gắn đủ 20 ca): ND 4 · HT 5 · NC 4 · GH 4 · NG 3 · Tổng 20 / 20

## Sau khi so với N2 (bước 3.3–3.5)

Số ca trùng: ___ / 20 = ___ % (cần từ 16/20, tức 80%)

| Ca không trùng | Nhãn N1 | Nhãn N2 | Nhãn thống nhất | Một câu quy tắc phân biệt |
| --: | :---: | :---: | :---: | --- |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

Dưới 80% thì viết lại định nghĩa năm loại ở đây trước khi đi tiếp:

-

## Nháp bảng khắc phục (bước 3.6)

Chọn 5 ca, mỗi loại một ca. "Phát hiện bằng gì" phải đo được: tên event, ngưỡng, tần suất kiểm tra. Cột phụ trách do N2 điền (một vai trò, không ghi "cả đội").

| Ca | Loại | Phát hiện bằng gì (event · ngưỡng · tần suất) | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| | Do người dùng | | | |
| | Hệ thống | | | |
| | Ngữ cảnh | | | |
| | Giới hạn hệ thống | | | |
| | Ngầm | | | |
