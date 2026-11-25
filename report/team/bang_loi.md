# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Trương Anh Đức · Người gắn nhãn 2: Võ Trần Công (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

Không có ca không trùng (20/20), nên không cần viết lại định nghĩa. Ba ca Người gắn nhãn 1 ghi là dễ phân vân, và quy tắc nhóm đã dùng để chốt:

- Ca 1: gốc lỗi là khách nhập thiếu số tài khoản, nên xếp Do người dùng, dù trợ lý có thể kiểm tra số trước khi tạo lệnh.
- Ca 13: gốc lỗi là yêu cầu ngoài phạm vi, nên xếp Giới hạn hệ thống, dù trợ lý trả lời chung chung thay vì nói rõ.
- Ca 17: gốc lỗi là bảng giá cũ trong bộ nhớ đệm mà không ai nhận ra, nên xếp Ngầm vì chỉ phát hiện qua kiểm tra mẫu.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 14 | Do người dùng | Event `ticket_reopened` có `reason = xac_nhan_nham` trong 7 ngày sau `ticket_closed`; cảnh báo khi vượt 1% số ticket đóng, kiểm tra hằng tuần | Thêm bước xác nhận lần hai ("Bạn đã nhận tiền vào tài khoản chưa?") và cho hoàn tác trong 24 giờ trước khi đóng; chỉ đóng khi `refund_ledger_write` trả `ok` | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát mỗi giờ: số `request_id` có nhiều hơn 1 bản ghi `refund_ledger_write` với `ket_qua = ok`; ngưỡng 0 ca | Khoá chống trùng `idempotency_key` theo `request_id`; yêu cầu gửi lại trong 10 phút thì trả "đang xử lý", không tạo lệnh hoàn mới | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | Event `notification_sent` có `sent_at` từ 22:00 đến 07:00, đối chiếu với `ticket_reopened` có `reason = lam_phien`; cảnh báo khi thông báo ngoài giờ vượt 2% số thông báo trong tuần, kiểm tra hằng tuần | Đặt giờ yên lặng 22:00–07:00: xếp hàng và gửi lúc 07:00; vẫn hiện trạng thái hoàn trong ứng dụng ngay khi xong | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Event `handoff_to_staff` có `reason = ngoai_pham_vi_du_lieu`, theo loại yêu cầu; cảnh báo khi vượt 3% số yêu cầu trong tuần hoặc bất kỳ ca chuyển nào thiếu `tom_tat`, kiểm tra hằng tuần | Giữ cách chuyển kèm tóm tắt; ghi giới hạn 12 tháng ngay trên ứng dụng để khách biết trước; nếu vượt 3% thì cân nhắc mở rộng phạm vi dữ liệu | PM trợ lý hoàn phí |
| 12 | Ngầm | Event `agent_run_completed`: số lần gọi tool và token trung bình mỗi yêu cầu theo depot; cảnh báo khi một depot vượt 1,5 lần trung bình toàn hệ thống trong 3 ngày liên tiếp, kiểm tra hằng ngày | Kiểm tra schema dữ liệu tool trả về và ghi `tool_schema_error` khi thiếu trường; sửa tool tra đơn của depot D05; đặt trần số lần gọi tool mỗi yêu cầu | Kỹ sư trưởng agent |
