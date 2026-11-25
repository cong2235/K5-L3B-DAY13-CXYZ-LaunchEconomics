# Phân công chi tiết · Nhóm CXYZ · Lab 13

Tài liệu nội bộ của nhóm, không nằm trong thư mục nộp. Nguồn: [CHECKPOINTS.md](CHECKPOINTS.md), [RUBRIC.md](RUBRIC.md), [hướng dẫn chi tiết](docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md). Giờ là mốc tại lớp, lớp học giờ khác thì theo coach.

## Vai và người

| Ký hiệu | Vai | Người |
| --- | --- | --- |
| **C** | Người viết code | Nguyễn Cao Minh (trước giải lao) |
| **K** | Người kiểm số | Trịnh Minh Đức |
| **N1** | Người gắn nhãn 1 | Trương Anh Đức |
| **N2** | Người gắn nhãn 2, kiêm giữ hồ sơ, trưởng nhóm | Võ Trần Công |

**Đề xuất đổi vai sau giải lao (15:35):** C và K đổi cho nhau. Trịnh Minh Đức thành người viết code, Nguyễn Cao Minh thành người kiểm số. Lý do: lúc CP3 hai người gắn nhãn bận, hai người còn lại vừa hoàn thiện CP2 vừa chuẩn bị CP4. Đổi như vậy thì cả hai đều đã tự tay tính chi phí, đúng yêu cầu của [TEAM.md](TEAM.md). Sau khi đổi, N2 cập nhật cột vai trò trong [TEAM.md](TEAM.md).

## Quy tắc chuyền việc

- Mỗi việc có **đầu vào** (chờ ai) và **đầu ra** (giao cho ai). Chưa có đầu vào thì làm việc chuẩn bị, không đoán số.
- C chạy xong thì **nhắn ngay** cho K và N2, kèm lệnh chạy hoặc output.
- K đối chiếu xong mới báo "số đã kiểm". Sai lệch trên 2% thì C sửa trước khi N2 đưa số vào hồ sơ.
- Chỉ N2 sửa `ho_so_launch_v0.md` và `group_report.md`. Mỗi người chỉ sửa file thuộc phần của mình để tránh xung đột git.
- Trước mỗi lần push: `git pull`. Sau mỗi checkpoint: commit và push.
- Số nào lấy từ cột `_simulated` đều ghi nhãn `simulated`. Người phụ trách ghi là vai trò, không ghi "cả đội".

---

## CP0 · Chuẩn bị (14:00 → 14:10)

| Bước | Ai | Việc | Xong khi |
| --: | --- | --- | --- |
| 0.1 | N2 | Điền [TEAM.md](TEAM.md), đã xong | Bảng 4 thành viên có đủ vai |
| 0.2 | C, K | Cài môi trường theo [src/README.md](src/README.md): tạo venv, cài `requirements.txt` | `python -c "import pandas, numpy, scipy, statsmodels; print('san sang')"` in `san sang` |
| 0.3 | N1 | Đọc đề, lập danh sách "Xong khi" của 5 nhiệm vụ | Có danh sách để theo dõi |
| 0.4 | N2 | Dựng khung hồ sơ: tên nhóm, lớp, người phụ trách từng mục | Đã xong và đã push |

## CP1 · Mô hình chi phí (14:00 → 14:53) · **Đã xong**

```text
C viết code ──► C chạy lab13.py ──► K tính tay đối chiếu ──► N1 điền bảng ──► N2 điền hồ sơ mục 1, 3
```

| Bước | Ai | Việc | Đầu vào | Đầu ra | Xong khi |
| --: | --- | --- | --- | --- | --- |
| 1.1 | C | Viết 3 hàm A1 ở dòng `TODO CP1` | `lab13.py` | Hàm chạy được | Ba phép thử ĐẠT (1,20 · 1,25 · 1,25) |
| 1.2 | K | Tính tay một con số A1 để đối chiếu, làm song song với 1.1 | Công thức trong [docs/du_lieu_va_cong_thuc.md](docs/du_lieu_va_cong_thuc.md) | Số tay | Khớp ba phép thử |
| 1.3 | C | Viết `mo_hinh`, gọi lại theo từng `loai` (A3), cộng chi phí cố định 40 triệu đ/tháng cho `noi_dia` + `hang_nang` (A4) | 1.1 xong | Output bảng A2, A3, A4 | `python lab13.py` in đủ bảng |
| 1.4 | K | Kiểm 1 số trong A2, ví dụ tổng chi phí hoặc 16,3× | 1.3 xong | "Số đã kiểm" | Lệch không quá 2% |
| 1.5 | N1 | Chép bảng A2 (9 dòng, 2 dòng `simulated`), A3 (4 dòng), A4 vào [bang_chi_phi.md](report/team/bang_chi_phi.md) | 1.3 xong | File điền đủ | A2 đủ 9 dòng, A3 đủ 4 dòng |
| 1.6 | N2 | Điền mục 1 và 3 hồ sơ | 1.4 xong | Mục 1, 3 trạng thái Giả lập | Đã push |

**Việc còn lại của CP1:** K xác nhận đã kiểm 16,3× và 5,865 đ chưa. Nếu chưa, kiểm ngay trước khi sang CP2.

## CP2 · Bảng độ nhạy (14:53 → 15:20)

```text
C chạy 9 kịch bản (B1) ──► K kiểm quy tắc ½ và 2× ──► N1 xếp hạng, viết B2 ──► C chạy B3, B4 ──► N1 viết trả lời ──► N2 điền mục 2, 7
```

| Bước | Ai | Việc | Đầu vào | Đầu ra | Xong khi |
| --: | --- | --- | --- | --- | --- |
| 2.1 | C | Ở `TODO CP2`, gọi lại `mo_hinh` cho 9 kịch bản B1 | CP1 xong | Bảng 9 dòng | In đủ 9 dòng |
| 2.2 | K | Kiểm: mỗi "giảm một nửa" bằng đúng nửa mức tăng của "gấp đôi" tương ứng | 2.1 | "Số đã kiểm" | Đúng với cả 3 cặp |
| 2.3 | C | B2: đổi một cặp. B3: giới hạn 1, 2, 3 lần, tính chi phí cả hệ thống. B4: xem lại 100% cho `noi_dia` + `hang_nang` | 2.1 | Số B2, B3, B4 | In đủ |
| 2.4 | N1 | Chép B1 vào [bang_chi_phi.md](report/team/bang_chi_phi.md). Xếp hạng 3 yếu tố mạnh nhất. Viết trả lời B3, B4, mỗi câu không quá 3 dòng và có số | 2.1, 2.3 | Bảng B1–B4 đủ | Không còn `...` |
| 2.5 | K | Đọc lại câu B2 để kiểm tra: tác động của một cặp bằng tổng hai tác động riêng | 2.4 | Xác nhận | Khớp |
| 2.6 | N2 | Điền mục 2 hồ sơ (ba yếu tố nhạy nhất) | 2.4 | Mục 2 | Giả lập |
| 2.7 | N2 | Nháp mục 7 (rủi ro kinh tế): ít nhất 2 dòng, số lấy từ B1 và A4 | 2.4 | Nháp trong hồ sơ | Dùng ở CP5 |
| 2.8 | Cả nhóm | Commit và push | | | `git pull` rồi `push` |

## Giải lao (15:20 → 15:35)

| Ai | Việc |
| --- | --- |
| Cả nhóm | **Đổi vai C và K.** N2 sửa [TEAM.md](TEAM.md). Người viết code mới chạy `python lab13.py` trên máy mình để chắc chạy được |
| N1, N2 | Lấy file đề `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, chuẩn bị giấy và bút. Đọc bảng 5 loại lỗi, **không mở bảng nhãn tham khảo** trong hướng dẫn |

## CP3 · Bảng lỗi và cách khắc phục (15:35 → 16:08)

```text
N1 và N2 gắn nhãn độc lập (8 phút) ──► so nhãn (3 phút) ──► thống nhất, viết quy tắc (5 phút) ──► chọn 5 ca, viết khắc phục (14 phút) ──► N2 điền mục 5
                                              ║
C và K hoàn thiện CP2 song song ─────────────╝
```

| Bước | Ai | Việc | Đầu vào | Đầu ra | Xong khi |
| --: | --- | --- | --- | --- | --- |
| 3.1 | N1, N2 | Ngồi tách nhau, gắn nhãn độc lập 20 ca trong 8 phút. Không trao đổi, không xem bảng tham khảo | File đề | Mỗi người một bộ nhãn viết ra giấy | Đủ 20 ca mỗi người |
| 3.2 | C, K | Hoàn thiện các ô còn trống của B1–B4 nếu có | CP2 | Bảng đủ | Không còn `...` |
| 3.3 | N1, N2 | So nhãn, tính tỉ lệ đồng thuận = số ca trùng ÷ 20 | 3.1 | Tỉ lệ | Từ 16/20. Dưới 16 thì viết lại định nghĩa 5 loại trước khi đi tiếp |
| 3.4 | N2 | Ghi hai bộ nhãn, tỉ lệ vào [bang_loi.md](report/team/bang_loi.md) | 3.3 | Bảng 20 dòng | Không còn `...` |
| 3.5 | N1, N2 | Với ca không trùng: thống nhất nhãn, mỗi ca viết một câu quy tắc phân biệt | 3.3 | Quy tắc | Mỗi ca không trùng có một câu |
| 3.6 | N1 | Chọn 5 ca, mỗi loại một ca. Viết "Phát hiện bằng gì" đo được (event, ngưỡng, tần suất) và "Khắc phục thế nào" | 3.5 | Bảng khắc phục nháp | Đủ 5 loại |
| 3.7 | C | Góp ý event trong cột phát hiện sao cho khớp với danh sách event của CP5 | 3.6 | Góp ý | Tên event thống nhất |
| 3.8 | N2 | Điền cột "Ai phụ trách" (một vai trò, không "cả đội") và mục 5 hồ sơ | 3.6 | Bảng đủ, mục 5 | Trạng thái Xong, có bằng chứng nếu có đủ hai bộ nhãn |
| 3.9 | Cả nhóm | Commit và push | | | `git pull` rồi `push` |

## CP4 · pilot_plan.yaml (16:08 → 16:36)

```text
C mới tính D1 ──► K mới kiểm tay ──► N1 trả lời D2 ──► N2 điền YAML ──► K chạy kiểm tra YAML ──► N2 điền mục 6
        └──► C tính mo_lai_trong_7_ngay ──► N1 viết luật dừng
```

| Bước | Ai | Việc | Đầu vào | Đầu ra | Xong khi |
| --: | --- | --- | --- | --- | --- |
| 4.1 | C (mới) | Ở `TODO CP4`, tính 5 câu D1: cỡ mẫu theo yêu cầu, theo nhân viên, theo depot, và mức chênh 6 điểm | Số cho sẵn: baseline, mục tiêu, alpha, power, ICC | Kết quả D1 | In đủ 5 câu |
| 4.2 | K (mới) | Tính tay ít nhất một câu D1 | 4.1 | "Số đã kiểm" | Lệch không quá 2% |
| 4.3 | C | Tính `reqs.mo_lai_trong_7_ngay.mean()` trước khi đặt luật an toàn | | Tỉ lệ hiện tại | Có con số |
| 4.4 | N1 | Trả lời 5 câu D2 "tách được tác động" | 4.1 | 5 câu | Mỗi câu có Có/Không kèm lý do |
| 4.5 | N1 | Viết 3 luật dừng (an toàn, chi phí, mức độ sử dụng) theo mẫu NẾU – TRONG – THÌ – KHÔNG THÌ, có ngưỡng, thời hạn, người có quyền dừng | 4.3 | 3 luật | Đủ 4 vế |
| 4.6 | N2 | Điền [pilot_plan.yaml](report/team/pilot_plan.yaml): D1, D2, các trường, chọn cách chia | 4.1, 4.4, 4.5 | File YAML | Không còn `?` |
| 4.7 | K | Chạy kiểm tra: `python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml'))"` và `grep -v '^ *#' ../report/team/pilot_plan.yaml \| grep -n '?'` | 4.6 | Kết quả | Không lỗi, không in gì |
| 4.8 | N2 | Điền mục 6 hồ sơ | 4.6 | Mục 6 | Có số cụm mỗi nhóm hoặc ghi rõ đánh đổi |
| 4.9 | Cả nhóm | Commit và push | | | |

## CP5 · Chỉ số, rủi ro, hồ sơ, duyệt chéo (16:36 → 18:00)

```text
C tính 3 chỉ số ──► K kiểm ──► N1 đề xuất chỉ số + event ──► N2 rủi ro, hồ sơ, đề xuất ──► gửi 17:00 ──► chấm chéo ──► báo cáo ──► push
```

| Bước | Ai | Việc | Đầu vào | Đầu ra | Xong khi |
| --: | --- | --- | --- | --- | --- |
| 5.1 | C | Tính thử 3 chỉ số: chính, dùng, an toàn | `logix_requests.csv` | 3 con số | Có số |
| 5.2 | K | Kiểm tay một chỉ số | 5.1 | "Số đã kiểm" | Lệch không quá 2% |
| 5.3 | N1 | Đề xuất thêm 1 chỉ số dùng, 1 chỉ số an toàn. Liệt kê ít nhất 6 event, mỗi event có `trace_id` | 5.1 | Mục trong [chi_so.md](report/team/chi_so.md) | Mỗi chỉ số chỉ ra event dùng để tính |
| 5.4 | N2 | Điền ít nhất 2 dòng rủi ro kinh tế, số lấy từ bảng độ nhạy | CP2 | Bảng rủi ro | Mỗi dòng có tác động, dấu hiệu, hành động, người phụ trách |
| 5.5 | N2 | Hoàn thiện [ho_so_launch_v0.md](report/team/ho_so_launch_v0.md): mục 4, 7, đề xuất cuối | 5.1–5.4 | Hồ sơ đủ 7 mục | Mục nào cũng có số, trạng thái, vai trò |
| 5.6 | N2 | Viết dòng **Đề xuất**: một trong Go, Go có điều kiện, No-go. Nêu cả số bất lợi (xem rubric C6) và cách xử lý | 5.5 | Dòng cuối | Khớp số của chính nhóm |
| 5.7 | K | Chạy `grep -rni production ../report/team` | 5.5 | Kết quả | Không in gì |
| 5.8 | **N2** | **17:00 gửi hồ sơ** cho nhóm hội đồng | 5.5 | Đã gửi | Đúng giờ |
| 5.9 | Cả nhóm | 17:10: đọc hồ sơ nhóm n+1, chấm vào [phieu_cham.md](report/team/phieu_cham.md), viết quyết định, lý do và một câu hỏi | Hồ sơ nhóm bạn | Phiếu | Điền đủ |
| 5.10 | N2 | 17:25: trình 1 phút, công bố 1 phút, trả lời 1 phút | | | |
| 5.11 | N2 | 17:45: điền [group_report.md](report/team/group_report.md) | | | |
| 5.12 | Từng người | Viết báo cáo cá nhân `report/team/MSSV_HoTen.md` (xem bảng dưới) | | File riêng | Có phần việc, đóng góp, bằng chứng |
| 5.13 | N2 | `git pull`, kiểm checklist cuối, commit, push | | Commit chốt | Điền URL, nhánh, commit chốt vào [TEAM.md](TEAM.md) |

### Tên file báo cáo cá nhân

| Người | File |
| --- | --- |
| Võ Trần Công | `report/team/2A202604026_VoTranCong.md` |
| Trịnh Minh Đức | `report/team/2A202604078_TrinhMinhDuc.md` |
| Trương Anh Đức | `report/team/2A202604096_TruongAnhDuc.md` |
| Nguyễn Cao Minh | `report/team/2A202604099_NguyenCaoMinh.md` |

## Checklist trước khi nộp (N2 chạy, K xác nhận)

- [ ] `python lab13.py` chạy hết trên một máy khác trong nhóm
- [ ] Ba phép thử A1 in ra ĐẠT
- [ ] Mọi số từ cột `_simulated` có nhãn `simulated`
- [ ] `pilot_plan.yaml` đọc được bằng `yaml.safe_load` và không còn dấu `?`
- [ ] Ít nhất 3 luật dừng đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ
- [ ] Mỗi mục hồ sơ có người phụ trách là một vai trò, không ghi "cả đội"
- [ ] `grep -rni production ../report/team` không in gì
- [ ] Mọi file nằm trong `report/team/`
- [ ] 4 báo cáo cá nhân đã có

## Nếu trễ giờ

Ưu tiên theo thứ tự: số đúng ở CP1–CP2, hồ sơ đủ 7 mục, bảng lỗi, rồi mới đến phần đẹp. Mục chưa xong ghi **Chưa** hoặc **Giả lập**, không điền số đoán.
