# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: CXYZ · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn bộ 4 loại yêu cầu: 4.472 đ/việc (tổng 4.373.585 đ / 978 việc), gấp 16,3× hoá đơn token và tool (274,65 đ/yêu cầu). Phạm vi `noi_dia` + `hang_nang`: 3.414 đ/việc chưa cộng cố định; 4.599 đ/việc đã cộng cố định 40 triệu đ/tháng ở 45.000 yêu cầu/tháng | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Theo B1, so với 4.472 đ/việc: (1) số ca làm lại gấp đôi +51,8% lên 6.787 đ; (2) tỉ lệ xem lại gấp đôi +40,7% lên 6.292 đ; (3) lương nhân viên +25% thì +23,1% lên 5.506 đ. Giá token gấp đôi chỉ +5,6%, nên chi phí do giờ nhân viên quyết định, không phải hoá đơn token | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Mốc 12.000 đ/yêu cầu. Cả hệ thống, tính cả 222 yêu cầu trợ lý không xử lý được và nhân viên phải làm thay: 5.865 đ/yêu cầu = 0,49×. Phạm vi pilot đã cộng cố định: 0,38× (45.000 yêu cầu/tháng), 0,48× (22.500 yêu cầu/tháng). Số bất lợi: `quoc_te` 1,88× và `doi_tac` 0,85× nên loại khỏi phạm vi | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử (không có đối chứng): chính 82,83% (994/1.200); dùng, tỉ lệ bỏ qua gợi ý 27,12% (48/177); an toàn, mở lại 7 ngày 4,25% (51/1.200). Thêm hai chỉ số tự đề xuất: % yêu cầu nhóm can thiệp được mở bằng trợ lý, và % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần. Cả năm chỉ số tính được từ 11 event có `trace_id` | Giả lập | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận 20/20 ca (100%) giữa hai người gắn nhãn độc lập. Phân bố: Do người dùng 4, Hệ thống 5, Ngữ cảnh 4, Giới hạn hệ thống 4, Ngầm 3. Bảng khắc phục 5 ca (14, 20, 16, 19, 12), mỗi ca có event, ngưỡng, tần suất kiểm tra và một vai trò phụ trách | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên, 20 + 20 (20 cụm mỗi nhóm), phạm vi `noi_dia` + `hang_nang`. Cỡ mẫu 859 mỗi nhóm, mỗi nhân viên từ 299 yêu cầu, hệ số thiết kế 6,96, chỉ thấy mức chênh 6 điểm. Số bất lợi: nếu tác động thật chỉ 5 điểm thì power còn khoảng 0,64. Mở lại 7 ngày hiện tại 3,97% trong phạm vi, `hang_nang` riêng 8,23%. Ba luật dừng có ngưỡng, thời hạn và người có quyền dừng; quyết định 2027-01-05 | Giả lập | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | (a) Số ca làm lại gấp đôi: 6.787 đ/việc, +51,8%. (b) Phải xem lại 100% ở `noi_dia` + `hang_nang`: 11.743 đ = 0,98× mốc 12.000 đ (12.415 đ = 1,03× nếu làm lại 15,3 phút/ca), tức không còn tiết kiệm. (c) Khối lượng giảm một nửa còn 22.500 yêu cầu/tháng: 5.784 đ/việc so với 4.599 đ vì chi phí cố định 40 triệu đ/tháng. (d) Giới hạn chạy 1 lần có chi phí mỗi việc thấp nhất (4.111 đ) nhưng thêm 85 yêu cầu thất bại; giới hạn 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện**, cho pilot `noi_dia` + `hang_nang`, chia theo nhân viên 20 + 20. Gate 2a chỉ duyệt kế hoạch pilot, chưa duyệt chạy chính thức.

Vì sao không phải Go: có năm con số bất lợi (simulated). (1) Nếu tác động thật chỉ 5 điểm thì power còn khoảng 0,64, không phải 0,8. (2) `hang_nang` mở lại 8,23%, cao hơn trần 6% của luật dừng. (3) Xem lại 100% đưa chi phí lên 0,98× đến 1,03× mốc 12.000 đ, không còn tiết kiệm. (4) Ca 20 (hoàn hai lần do thiếu khoá chống trùng) và ca 7 (báo đã hoàn khi sổ cái lỗi) là mất tiền trực tiếp. (5) Phút xem lại và làm lại hiện là số giả lập. Vì sao không phải No-go: chi phí mỗi việc thành công trong phạm vi chỉ 0,38× mốc 12.000 đ sau khi cộng cố định, và các rủi ro trên có cách kiểm soát đo được.

Điều kiện, mỗi điều kiện có người phụ trách và ngày kiểm tra (giả định pilot bắt đầu 2026-12-07):

1. Sửa khoá chống trùng và đối soát sổ cái (ca 20, ca 7) trước khi bắt đầu. Kỹ sư trưởng agent, kiểm tra ngày 2026-12-04.
2. Ký chấp nhận mức chênh 6 điểm, power khoảng 0,64 nếu tác động thật là 5 điểm. Giám đốc vận hành LogiX-VN, kiểm tra ngày 2026-12-04.
3. Bật đủ 11 event có `trace_id`; thay phút xem lại và làm lại giả lập bằng phút đo thật sau tuần 1; theo dõi riêng tỉ lệ mở lại của `hang_nang`. PM trợ lý hoàn phí, kiểm tra ngày 2026-12-14.
4. Có kế hoạch giảm xem lại theo bậc, vì xem lại 100% thì không tiết kiệm. Trưởng nhóm CSKH, kiểm tra ngày 2026-12-21.
