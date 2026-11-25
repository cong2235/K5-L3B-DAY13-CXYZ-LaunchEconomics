# Báo cáo cá nhân — TrinhMinhDuc-2A202604078

## 1. Thông tin thành viên

- Họ tên: Trịnh Minh Đức
- MSSV: 2A202604078
- Email:
- GitHub: Duc1306
- Vai trong nhóm: **người kiểm số** trước giải lao (CP1, CP2); **người viết code** sau giải lao (CP3–CP5), đổi vai với Nguyễn Cao Minh theo `PHAN_CONG.md`.

## 2. Phần việc phụ trách

| Checkpoint | Bước trong `PHAN_CONG.md` | Việc |
| --- | --- | --- |
| CP1 | 1.2, 1.4 | Đối chiếu ba phép thử A1, kiểm bảng A2, A3, A4 với output `lab13.py` |
| CP2 | 2.2, 2.5 | Kiểm quy tắc ½ và 2× của B1; kiểm B2 bằng tổng hai tác động riêng; kiểm B3, B4 |
| CP3 | 3.7 | Góp ý tên event trong cột "Phát hiện bằng gì" của `bang_loi.md` để khớp danh sách event CP5 |
| CP4 | 4.1, 4.3 | Viết phần cỡ mẫu D1 trong `src/lab13.py`; tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại |
| CP5 | 5.1 | Viết phần tính thử ba chỉ số E1 trong `src/lab13.py` |

## 3. Đóng góp cụ thể

**Kiểm số CP1.** Đối chiếu từng dòng `bang_chi_phi.md` với output `lab13.py` và với một lần tính độc lập từ hai file CSV; không có dòng nào lệch.

- A1: (1 − 0,2²)/0,8 = 1,20; 1/0,8 = 1,25; 1,24/0,992 = 1,25.
- Một dòng trace `run_00001`: 4759/1000 × 26 + 492/1000 × 130 = 187,69 đ token, 5 × 15 = 75 đ tool, tổng 262,69 đ.
- A2: tổng 4.373.585 đ ÷ 978 việc thành công = 4.472 đ/việc (simulated), gấp 16,3 lần hoá đơn 274,65 đ/yêu cầu.
- Chi phí cả hệ thống: (4.373.585 + 222 × 12.000) / 1.200 = 5.865 đ/yêu cầu = 0,49× (simulated).

**Kiểm số CP2.** Vì mô hình cộng tuyến tính, mỗi kịch bản chỉ cộng hoặc trừ một khoản vào tổng A2 rồi chia lại cho 978:

| Kịch bản | Cách tính | Kết quả (simulated) |
| --- | --- | ---: |
| Token gấp đôi | (4.373.585 + 245.585) / 978 | 4.723 đ (+5,6%) |
| Token giảm một nửa | (4.373.585 − 122.793) / 978 | 4.346 đ (−2,8%) |
| Xem lại gấp đôi | (4.373.585 + 1.780.000) / 978 | 6.292 đ (+40,7%) |
| Xem lại giảm một nửa | (4.373.585 − 890.000) / 978 | 3.562 đ (−20,3%) |
| Làm lại gấp đôi | (4.373.585 + 2.264.000) / 978 | 6.787 đ (+51,8%) |
| Làm lại giảm một nửa | (4.373.585 − 1.132.000) / 978 | 3.315 đ (−25,9%) |
| Lương tăng 25% | (4.373.585 + 2.022 phút × 500) / 978 | 5.506 đ (+23,1%) |
| B2: token và xem lại cùng gấp đôi | (4.373.585 + 245.585 + 1.780.000) / 978 | 6.543 đ (+46,3%) |

- Quy tắc ½ đúng cả ba cặp; B2 tăng 2.071 đ = 251 + 1.820, đúng tính cộng tuyến tính.
- B3: 3.621.781 + 319 × 12.000 = 7.449.781; 4.093.220 + 234 × 12.000 = 6.901.220 (rẻ nhất); 4.373.585 + 222 × 12.000 = 7.037.585.
- B4: 948 × 5 × 2.000 + 48 × 9 × 2.000 + 224.513 = 10.568.513 đ ÷ 900 = 11.743 đ = 0,98× (simulated).
- Hai kịch bản giới hạn số lần chạy (4.237 đ và 4.111 đ) đối chiếu bằng script độc lập, không tính tay.

**Góp ý event CP3.** Bảng khắc phục dùng hai event chưa có trong danh sách mẫu của CP5: `notification_sent` (ca 16) và `tool_schema_error` (ca 12); `agent_run_completed` cần thêm thuộc tính `depot` cho ca 12. Đề xuất danh sách 12 event thống nhất và chốt chung các giá trị `reason` của `handoff_to_staff` và `ticket_reopened`.

**Code CP4 (D1).** Thêm vào `src/lab13.py` các hàm `co_mau`, `he_so_thiet_ke`, `co_mau_hieu_dung`, `in_co_mau`:

- a) 1.251 yêu cầu mỗi nhóm; b) DE 2,48, 3.103 yêu cầu mỗi nhóm = 42 người mỗi nhóm, tổng 84 > 40; c) tối đa 1.000 < 1.251; d) tối đa 300; e) 859 mỗi nhóm, m ≥ 299 yêu cầu mỗi nhân viên, DE 6,96.
- Đánh đổi: nếu tác động thật chỉ +5 điểm, power với n = 859 còn 0,64.
- Tỉ lệ mở lại 7 ngày hiện tại: 4,25% (51/1.200) toàn mẫu, 3,97% (39/982) trong `noi_dia` + `hang_nang`.

**Code CP5 (E1).** Thêm hàm `in_chi_so` vào `src/lab13.py`. Chỉ số trong đợt chạy thử là:

- Chính: 82,83% (994/1.200) đóng trong 24 giờ và không mở lại trong 7 ngày.
- Dùng: 27,12% (48/177) gợi ý bị sửa hoặc bỏ.
- An toàn: 4,25% (51/1.200) mở lại trong 7 ngày.

## 4. Bằng chứng

- Commit `89b53a6` — Implement CP4: cỡ mẫu D1 và tỉ lệ mở lại 7 ngày (`src/lab13.py`).
- Commit phần E1 (`in_chi_so`) trong `src/lab13.py`.
- Bảng đối chiếu CP1, CP2 ở mục 3 của báo cáo này; số khớp với `report/team/bang_chi_phi.md`.
- Output `python lab13.py` in đủ A1–A4, B1–B4, D1, tỉ lệ mở lại và E1.

## 5. Công cụ AI đã dùng

- **Claude (Claude Code):** đọc đề và phân công, tính đối chiếu độc lập A1–B4 từ hai file CSV bằng script riêng không dùng `lab13.py`, gợi ý code cho D1 và E1, đề xuất danh sách event.
- **Cách tự kiểm tra:** so ba nguồn với nhau (bảng của nhóm, output `lab13.py`, số tính độc lập); kiểm B1, B2 bằng tính cộng tuyến tính trên tổng A2; câu e của D1 giải tay 20m ≥ 859 × (0,98 + 0,02m) → m ≥ 298,5 → 299; đếm lại ba chỉ số E1 bằng một đoạn đọc CSV không dùng pandas (994, 48/177, 51).

## 6. Tự đánh giá

- Làm được: kiểm số CP1, CP2 không còn dòng lệch; sau khi đổi vai, viết được phần D1 và E1 chạy hết trong `lab13.py`.
- Hiểu được: tử số tính mọi lần chạy vì lần lỗi vẫn tốn tiền, mẫu số chỉ đếm việc thành công; chia theo cụm thì số cụm quyết định cỡ mẫu hiệu dụng (luôn dưới c ÷ ICC), nên 20 nhân viên mỗi nhóm chỉ đủ cho mức chênh 6 điểm.
- Cần cải thiện: tự tính tay nhiều hơn thay vì dựa vào script đối chiếu, nhất là hai kịch bản giới hạn số lần chạy.
