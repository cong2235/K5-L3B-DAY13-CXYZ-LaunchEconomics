# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: CXYZ · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn bộ 4 loại yêu cầu: 4.472 đ/việc (tổng 4.373.585 đ / 978 việc), gấp 16,3× hoá đơn token và tool (274,65 đ/yêu cầu). Phạm vi `noi_dia` + `hang_nang`: 3.414 đ/việc chưa cộng cố định; 4.599 đ/việc đã cộng cố định 40 triệu đ/tháng ở 45.000 yêu cầu/tháng | Giả lập | Người viết code |
| 2 · Ba yếu tố nhạy nhất | Theo B1, so với 4.472 đ/việc: (1) số ca làm lại gấp đôi +51,8% lên 6.787 đ; (2) tỉ lệ xem lại gấp đôi +40,7% lên 6.292 đ; (3) lương nhân viên +25% thì +23,1% lên 5.506 đ. Giá token gấp đôi chỉ +5,6%, nên chi phí do giờ nhân viên quyết định, không phải hoá đơn token | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Mốc 12.000 đ/yêu cầu. Cả hệ thống, tính cả 222 yêu cầu nhân viên phải làm lại: 5.865 đ/yêu cầu = 0,49×. Phạm vi pilot đã cộng cố định: 0,38× (45.000 yêu cầu/tháng), 0,48× (22.500 yêu cầu/tháng). Số bất lợi: `quoc_te` 1,88× và `doi_tac` 0,85× nên loại khỏi phạm vi | Giả lập | Người viết code |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chưa có số (đợi CP5) | Chưa | Người gắn nhãn 1 |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận 20/20 ca (100%) giữa hai người gắn nhãn độc lập. Phân bố: Do người dùng 4, Hệ thống 5, Ngữ cảnh 4, Giới hạn hệ thống 4, Ngầm 3. Bảng khắc phục 5 ca (14, 20, 16, 19, 12), mỗi ca có event, ngưỡng, tần suất kiểm tra và một vai trò phụ trách | Xong, có bằng chứng | Người gắn nhãn 2 kiêm giữ hồ sơ |
| 6 · Pilot plan | Chia theo nhân viên, 20 + 20 (20 cụm mỗi nhóm), phạm vi `noi_dia` + `hang_nang`. Cỡ mẫu 859 mỗi nhóm, mỗi nhân viên từ 299 yêu cầu, hệ số thiết kế 6,96, chỉ thấy mức chênh 6 điểm. Số bất lợi: nếu tác động thật chỉ 5 điểm thì power còn khoảng 0,64. Mở lại 7 ngày hiện tại 3,97% trong phạm vi, `hang_nang` riêng 8,23%. Ba luật dừng có ngưỡng, thời hạn và người có quyền dừng; quyết định 2027-01-05 | Giả lập | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | (a) Số ca làm lại gấp đôi: 6.787 đ/việc, +51,8%. (b) Phải xem lại 100% ở `noi_dia` + `hang_nang`: 11.743 đ = 0,98× mốc 12.000 đ (12.415 đ = 1,03× nếu làm lại 15,3 phút/ca), tức không còn tiết kiệm. (c) Khối lượng giảm một nửa còn 22.500 yêu cầu/tháng: 5.784 đ/việc so với 4.599 đ vì chi phí cố định 40 triệu đ/tháng. (d) Giới hạn chạy 1 lần có chi phí mỗi việc thấp nhất (4.111 đ) nhưng thêm 85 yêu cầu thất bại; giới hạn 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ) | Giả lập | Người kiểm số |

**Đề xuất:** Go · Go có điều kiện · No-go (giữ một). Go có điều kiện: ghi từng điều kiện, người phụ trách, ngày kiểm tra. No-go: ghi việc phải làm để quay lại cổng.

- ...
