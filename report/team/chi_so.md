# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200) (simulated) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48/177) (simulated) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200) (simulated) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm dùng trợ lý được mở bằng trợ lý | Số yêu cầu có `agent_suggestion_shown`, chia số yêu cầu `refund_request_created` của nhóm can thiệp (`arm = tro_ly`), theo tuần. Ngưỡng theo dõi: dưới 60% thì xem lại thói quen dùng | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 12, 17) | Số mẫu có `so_tien_da_hoan` khác `so_tien_dung`, chia số mẫu `audit_sample_checked` (100 đơn mỗi tuần). Ngưỡng: trên 1% thì Kế toán trưởng dừng và rà trace | Không cần tính |

Chỉ số trong đợt chạy thử là 82,83% (994/1.200), trong phạm vi `noi_dia` + `hang_nang` là 92,26% (906/982). Đợt chạy thử không có nhóm đối chứng nên không kết luận trợ lý đã nâng chỉ số so với mức 0,70 của nhân viên tự làm. Số trên chỉ là mức khởi điểm của chỉ số, tính từ dữ liệu giả lập (simulated).

## Danh sách event

Mỗi event có `trace_id` để nối với trace của agent. Mười một event, thêm ba event so với danh sách mẫu để phục vụ bảng khắc phục ở `bang_loi.md`.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Ứng dụng khách | request_id, loai, so_tien, arm, staff_id, created_at, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status, depot, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên | quyet_dinh (giu, sua, bo), phut_xem_lai đo thật, staff_id, trace_id | Khi nhân viên bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai đo thật, ly_do, trace_id | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ |
| `handoff_to_staff` | Agent | reason, tom_tat, trace_id | Khi chuyển nhân viên |
| `ticket_closed` | Hệ thống ticket | closed_at, trace_id | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi khách mở lại |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, tuan, trace_id | Hằng tuần, mẫu 100 đơn |
| `notification_sent` | Dịch vụ thông báo | kenh, sent_at, trace_id | Khi gửi thông báo cho khách (dùng cho ca 16) |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, event dùng để tính.

- Chỉ số chính: `refund_request_created` (created_at), `ticket_closed` (closed_at) để biết đóng trong 24 giờ, và `ticket_reopened` để loại các yêu cầu mở lại trong 7 ngày. Tính được.
- Chỉ số dùng (bỏ qua gợi ý): `agent_suggestion_shown` và `staff_review_decision` (quyet_dinh là `sua` hoặc `bo`). Tính được.
- Chỉ số an toàn (mở lại 7 ngày): `ticket_reopened` chia `refund_request_created`. Tính được.
- Chỉ số dùng tự đề xuất: `agent_suggestion_shown` chia `refund_request_created` theo `arm` và `staff_id`. Tính được.
- Chỉ số an toàn tự đề xuất: `audit_sample_checked`. Tính được.
- Phút xem lại và làm lại hiện là số giả lập; chỉ đo thật được khi bật `staff_review_decision` và `staff_rework_completed` (điều kiện 3 của hồ sơ).

Cả năm chỉ số tính được từ danh sách event, nên không có chỉ số nào chưa đo được.

## E2 · Rủi ro kinh tế

Số lấy từ bảng độ nhạy trong `bang_chi_phi.md` (simulated).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công lên 6.787 đ, tăng 51,8% (B1) | Tỉ lệ làm lại hằng tuần trên 7% số yêu cầu (đợt chạy thử: 4,9%, 48/982 trong phạm vi), theo `staff_rework_completed` | Thu hẹp về `noi_dia`, rà 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ/việc = 0,98× mốc 12.000 đ, hoặc 12.415 đ = 1,03× nếu làm lại 15,3 phút mỗi ca (B4), tức không còn tiết kiệm | Tỉ lệ yêu cầu được xem lại cuối bước rollout 25% còn trên 50% (đợt chạy thử: 13,0%, 128/982 trong phạm vi) | Giảm xem lại theo bậc khi tỉ lệ sửa cộng bỏ dưới 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa; tổng 5.784 đ/việc (A4) | Số việc thành công hằng tuần dưới 50% kế hoạch | Không mở rộng pilot; xem lại hợp đồng chi phí cố định, không kết luận trợ lý đắt | PM trợ lý hoàn phí |
| Lương nhân viên tăng | Tăng 25% thì chi phí lên 5.506 đ/việc, tăng 23,1% (B1) | Đơn giá phút nhân viên trong báo cáo nhân sự hằng quý | Cập nhật lại mô hình chi phí, kiểm tra ngưỡng 8.000 đ của luật dừng | Giám đốc vận hành LogiX-VN |
