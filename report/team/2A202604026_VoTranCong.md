# Báo cáo cá nhân — VoTranCong-2A202604026

## 1. Thông tin thành viên

- Họ tên: Võ Trần Công
- MSSV: 2A202604026
- Email:
- GitHub: cong2235
- Vai trong nhóm: **người gắn nhãn 2, kiêm giữ hồ sơ** và trưởng nhóm.

## 2. Phần việc phụ trách

| Checkpoint | Việc |
| --- | --- |
| CP0 | Điền `TEAM.md` (tên nhóm, lớp, bốn thành viên và vai); lập `PHAN_CONG.md` phân việc theo checkpoint; dựng khung `ho_so_launch_v0.md` |
| CP1, CP2 | Điền hồ sơ mục 1, 2, 3, 7 từ số của `bang_chi_phi.md` sau khi người kiểm số đối chiếu |
| CP3 | Gắn nhãn độc lập 20 ca; điền `bang_loi.md` (hai bộ nhãn, đồng thuận, quy tắc, bảng khắc phục 5 ca); hồ sơ mục 5 |
| CP4 | Điền `pilot_plan.yaml` (D1, D2, luật dừng, các trường nhóm quyết) từ số của người viết code và nháp của người gắn nhãn 1; chạy kiểm tra YAML; hồ sơ mục 6 |
| CP5 | Điền `chi_so.md`, hồ sơ mục 4 và dòng đề xuất; viết `group_report.md`; chuẩn bị slide và kịch bản debate; kiểm tra trước khi nộp |

## 3. Đóng góp cụ thể

**Hồ sơ launch v0.** Điền đủ bảy mục, mỗi mục có con số chính, trạng thái và người phụ trách là chức danh nghiệp vụ. Dòng cuối là **Go có điều kiện** cho pilot `noi_dia` + `hang_nang`, nêu năm số bất lợi và bốn điều kiện, mỗi điều kiện một người và một ngày kiểm tra. Các số bất lợi: power 0,64 nếu tác động thật chỉ 5 điểm; `hang_nang` mở lại 8,23% cao hơn trần 6%; xem lại 100% đạt 0,98× đến 1,03× mốc 12.000 đ; ca 20 và ca 7 là mất tiền trực tiếp; phút xem lại và làm lại là số giả lập.

**Gắn nhãn CP3.** Gắn độc lập 20 ca, không trao đổi với người gắn nhãn 1: Do người dùng 4 · Hệ thống 5 · Ngữ cảnh 4 · Giới hạn hệ thống 4 · Ngầm 3. Đồng thuận 20/20 = 100%. Bảng khắc phục 5 ca (14, 20, 16, 19, 12), mỗi ca có event, ngưỡng, tần suất và một vai trò phụ trách.

**Pilot plan.** Điền `pilot_plan.yaml` với chia theo nhân viên 20 + 20, `n_per_arm` 859, hệ số thiết kế 6,96, mức chênh 6 điểm, ba luật dừng đủ bốn vế. So bản luật của mình với bản của người gắn nhãn 1 và gộp ưu điểm của cả hai: ca hoàn trùng dừng ngay trong ngày, vế KHÔNG THÌ là việc bị cấm, chi phí chưa cộng cố định, chênh 2 điểm chỉ dùng từ bước 10 nhân viên (theo slide D1 của coach).

**Chỉ số, event, rủi ro (`chi_so.md`).** Ba chỉ số trong đợt chạy thử: 82,83% (994/1.200), 27,12% (48/177), 4,25% (51/1.200), cùng hai chỉ số tự đề xuất, 11 event có `trace_id` và bốn dòng rủi ro kinh tế lấy số từ bảng độ nhạy. Kiểm tra chéo: cả năm chỉ số tính được từ danh sách event.

**Sửa lỗi nhờ đối chiếu.** Người gắn nhãn 1 chỉ ra mục 3 hồ sơ ghi 222 yêu cầu "nhân viên phải làm lại", đúng là "làm thay"; đã sửa.

## 4. Bằng chứng

- Commit `7d9c8ce` — fill team.md.
- Commit `93b1dc8`, `5623970` — hồ sơ mục 1, 2, 3, 7.
- Commit `f3de58c`, `42110b9` — `bang_loi.md`: hai bộ nhãn, đồng thuận 20/20, bảng khắc phục 5 ca, hồ sơ mục 5.
- Commit `07509f7`, `caf68fd` — `pilot_plan.yaml`, hồ sơ mục 4, 6 và đề xuất, `chi_so.md`.
- Commit `ffba976` — `PHAN_CONG.md`.
- `report/team/group_report.md` và báo cáo này.

## 5. Công cụ AI đã dùng

- **Claude (Claude Code):** đọc đề và tài liệu hướng dẫn; đề xuất phân công; soạn nháp các bảng và hồ sơ từ số liệu trong repo; tính D1 và các tỉ lệ từ `logix_requests.csv`; dựng slide HTML và kịch bản debate; kiểm tra định dạng.
- **Không dùng AI để gắn nhãn:** 20 nhãn CP3 do mình tự gắn và gửi; Claude chỉ ghi lại nguyên văn vào bảng, không đưa ý kiến vào.
- **Cách tự kiểm tra:** chạy lại `python lab13.py` (ba phép thử ĐẠT); đối chiếu D1 với script tính riêng và với slide coach; kiểm tra `yaml.safe_load` và `grep` không còn dấu `?` hay từ bị cấm theo quy tắc nộp; so số của mình với commit của ba bạn trước khi đưa vào hồ sơ; sửa lại ngưỡng luật dừng khi phát hiện mâu thuẫn với slide coach.

## 6. Tự đánh giá

- Làm được: hồ sơ đủ bảy mục, đề xuất khớp số của chính nhóm và nêu số bất lợi; bộ nhãn độc lập đạt đồng thuận 20/20; `pilot_plan.yaml` đọc được, đủ trường, không còn dấu `?`.
- Hiểu được: gắn nhãn theo nguyên nhân gốc; chỉ được viết "chỉ số trong đợt chạy thử là…" vì không có nhóm đối chứng; cỡ mẫu hiệu dụng khi chia theo cụm luôn dưới số cụm ÷ ICC nên 20 nhân viên mỗi nhóm chỉ đủ cho mức chênh 6 điểm; chi phí cố định không được cộng vào ngưỡng luật dừng ở bước rollout nhỏ.
- Cần cải thiện: tự tính tay nhiều hơn các số trong hồ sơ thay vì dựa vào bảng của bạn cùng nhóm và script; ngưỡng 6%, 8.000 đ, 40% là lựa chọn của nhóm, cần dữ liệu thật ở pilot để căn lại.
