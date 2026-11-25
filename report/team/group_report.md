# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: CXYZ
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Trả lời câu hỏi của Gate 2a: trợ lý hoàn phí của LogiX-VN có đáng chạy thử không, và nếu có thì chạy thử thế nào để biết được kết quả. Nhóm đi theo năm bước: tính chi phí thật của mỗi việc thành công từ trace, tìm yếu tố làm chi phí thay đổi nhiều nhất, phân loại lỗi và cách khắc phục, thiết kế pilot tách được tác động và đủ cỡ mẫu, rồi ghép thành một hồ sơ để hội đồng ra quyết định. Mọi con số từ cột `_simulated` được ghi nhãn `simulated`.

## 3. Giải pháp

| Nhiệm vụ | Cách làm | File |
| --- | --- | --- |
| A · Mô hình chi phí | Tính chi phí mỗi việc thành công: tử số tính mọi lần chạy, mẫu số chỉ đếm `thanh_cong`; tách theo loại yêu cầu; cộng chi phí cố định cho phạm vi pilot | `src/lab13.py`, `report/team/bang_chi_phi.md` |
| B · Độ nhạy | Chín kịch bản đổi một yếu tố, một kịch bản đổi một cặp, giới hạn chạy lại 1, 2, 3 lần, và kịch bản xem lại 100% | `report/team/bang_chi_phi.md` |
| C · Bảng lỗi | Hai người gắn nhãn độc lập 20 ca theo năm loại của Google PAIR, so nhãn, chọn 5 ca khắc phục mỗi ca có event, ngưỡng và vai trò phụ trách | `report/team/bang_loi.md` |
| D · Pilot | Tính cỡ mẫu theo ba cách chia, chọn chia theo nhân viên 20 + 20, viết ba luật dừng và các trường tách tác động | `report/team/pilot_plan.yaml` |
| E · Chỉ số và hồ sơ | Ba chỉ số, 11 event có `trace_id`, rủi ro kinh tế lấy từ bảng độ nhạy, hồ sơ một trang với đề xuất cuối | `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md` |

## 4. Kết quả

- **Chi phí:** 4.472 đ mỗi việc thành công, gấp 16,3 lần hoá đơn token và tool (274,65 đ/yêu cầu), vì giờ nhân viên chiếm 92,5% (simulated). Cả hệ thống, tính cả 222 yêu cầu phải nhân viên làm thay: 5.865 đ/yêu cầu = 0,49× mốc 12.000 đ.
- **Phạm vi:** `noi_dia` (0,22×) và `hang_nang` (0,69×). Loại `quoc_te` (1,88×) và `doi_tac` (0,85×). Sau khi cộng cố định 40 triệu đ/tháng: 4.599 đ/việc = 0,38× ở 45.000 yêu cầu/tháng (simulated).
- **Độ nhạy:** ba yếu tố nhạy nhất là số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1%); giá token gấp đôi chỉ +5,6%. Xem lại 100% đưa chi phí lên 0,98× đến 1,03× mốc 12.000 đ, tức không còn tiết kiệm (simulated).
- **Lỗi:** đồng thuận 20/20 giữa hai người gắn nhãn độc lập.
- **Pilot:** chia theo nhân viên, 20 + 20, 859 yêu cầu hiệu dụng mỗi nhóm (mỗi nhân viên từ 299 yêu cầu, hệ số thiết kế 6,96), chỉ thấy mức chênh 6 điểm; nếu tác động thật chỉ 5 điểm thì power còn khoảng 0,64. Quyết định ngày 2027-01-05 nếu bắt đầu ngày 2026-12-07.
- **Chỉ số trong đợt chạy thử** (không có nhóm đối chứng): chính 82,83%, dùng 27,12%, an toàn 4,25% (simulated).
- **Đề xuất: Go có điều kiện** cho pilot `noi_dia` + `hang_nang`, bốn điều kiện, mỗi điều kiện một người và một ngày kiểm tra. Gate 2a chỉ duyệt kế hoạch pilot.
- **Kết quả duyệt chéo:** ghi bổ sung sau khi hội đồng công bố quyết định.

## 5. Khó khăn và cách xử lý

- **Cỡ mẫu không đủ cho mức chênh 5 điểm:** với 40 nhân viên không cách chia nào đạt. Nhóm chọn chia theo nhân viên (20 cụm mỗi nhóm), chấp nhận nhìn mức 6 điểm và nêu rõ power 0,64.
- **Luật chi phí bản đầu sẽ dừng pilot sai:** nếu cộng chi phí cố định vào ngưỡng 8.000 đ thì ở bước rollout nhỏ chi phí vọt lên khoảng 11.852 đ đến 15.300 đ. Nhóm đổi sang chi phí chưa cộng cố định và đưa chi phí cố định vào rủi ro kinh tế.
- **Luật an toàn dừng quá sớm ở bước 4 nhân viên:** chênh 2 điểm so với đối chứng chỉ là nhiễu khi chỉ có 4 người, nên chỉ dùng từ bước 10; ca hoàn trùng thì dừng ngay trong ngày.
- **Mô tả sai trong hồ sơ:** 222 yêu cầu là nhân viên làm thay, không phải làm lại; được người gắn nhãn 1 phát hiện khi đối chiếu và đã sửa.
- **Phối hợp trên một repo:** mỗi người chỉ sửa file phần mình, `git pull` trước khi push, đổi vai người viết code và người kiểm số sau giải lao; không phát sinh conflict.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md` và báo cáo cá nhân trong `report/team/`.

- **Nguyễn Cao Minh (người viết code, trước giải lao):** viết các hàm A1, `mo_hinh`, A3, A4 và các phần độ nhạy B1–B4 trong `src/lab13.py`.
- **Trịnh Minh Đức (người kiểm số, sau giải lao là người viết code):** đối chiếu độc lập CP1, CP2; viết D1 (cỡ mẫu), tỉ lệ mở lại và ba chỉ số E1 trong `src/lab13.py`.
- **Trương Anh Đức (người gắn nhãn 1):** theo dõi "Xong khi", bổ sung bảng A2–A4, gắn nhãn độc lập 20 ca, viết nháp D2 và ba luật dừng.
- **Võ Trần Công (người gắn nhãn 2, giữ hồ sơ, trưởng nhóm):** phân công, gắn nhãn độc lập, điền `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`, hồ sơ launch v0 và báo cáo nhóm.

## 7. Hạn chế và hướng cải thiện

- Phút xem lại và làm lại là số giả lập. Điều kiện 3 của hồ sơ yêu cầu thay bằng phút đo thật sau tuần 1 của pilot.
- Đợt chạy thử không có nhóm đối chứng, nên không kết luận trợ lý đã nâng chỉ số so với mức 0,70.
- `hang_nang` mở lại 8,23%, cao hơn trần 6% của luật dừng (trần tính trên cả phạm vi, 3,97%); phải theo dõi riêng.
- Ngưỡng 6%, 8.000 đ, 40% là lựa chọn của nhóm, chưa suy ra từ công thức; cần căn lại bằng số đo thật.
- Cỡ mẫu chỉ đủ cho mức chênh 6 điểm.

## 8. Tài liệu tham khảo

- Đề bài và hướng dẫn chi tiết của lab: `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, `docs/du_lieu_va_cong_thuc.md`.
- Slide "D1 · Ba cách chia ai được dùng trợ lý" do coach cung cấp (luật dừng khi mở dần, chi phí cố định và ngưỡng 8.000 đ).
- Google PAIR, *People + AI Guidebook*: năm loại lỗi (do người dùng, hệ thống, ngữ cảnh, giới hạn hệ thống, ngầm).
- Công cụ AI: Claude (Claude Code), xem mục 5 của từng báo cáo cá nhân.
