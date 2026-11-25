# Báo cáo cá nhân — TruongAnhDuc-2A202604096

## 1. Thông tin thành viên

- Họ tên: Trương Anh Đức
- MSSV: 2A202604096
- Email:
- GitHub: TADIZB
- Vai trong nhóm: **người gắn nhãn 1** (đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3).

## 2. Phần việc phụ trách

| Checkpoint | Bước trong `PHAN_CONG.md` | Việc |
| --- | --- | --- |
| CP0 | 0.3 | Đọc đề, lập danh sách "Xong khi" của năm nhiệm vụ để theo dõi |
| CP1 | 1.5 | Soát `bang_chi_phi.md` theo điều kiện "Xong khi", bổ sung các ý còn thiếu của A2, A3, A4 |
| CP2 | 2.4 (soát) | Đối chiếu bảng B1–B4 với điều kiện "Xong khi" và quy tắc ½ – 2× |
| CP3 | 3.1, 3.3, 3.5 | Gắn nhãn độc lập 20 ca; so nhãn với người gắn nhãn 2; nêu ba ca dễ phân vân và quy tắc chốt |
| CP4 | 4.4, 4.5 (hỗ trợ 4.3) | Tính tỉ lệ mở lại hiện tại; viết nháp năm câu D2 và ba luật dừng |

## 3. Đóng góp cụ thể

**Theo dõi "Xong khi" CP1, CP2.** Đối chiếu từng số trong `bang_chi_phi.md` với bảng đáp án của hướng dẫn và với output `python lab13.py` chạy trên máy mình; không có dòng nào lệch quá 2%. Bổ sung vào `bang_chi_phi.md`:

- A2: xem lại chiếm 40,7% (1.780.000 / 4.373.585), giờ nhân viên chiếm 92,5% tổng chi phí (simulated).
- A2: câu giải thích vì sao tử số tính mọi lần chạy (lần lỗi vẫn tốn token và tool, 93.804 đ ở lần chạy 2 và 3) còn mẫu số chỉ đếm 978 việc thành công.
- A2: so với 12.000 đ phải dùng chi phí cả hệ thống (4.373.585 + 222 × 12.000) / 1.200 = 5.865 đ/yêu cầu = 0,49× (simulated, tính tay).
- A3: kết luận phạm vi, loại `quoc_te` (1,88×) và `doi_tac` (0,85×), giữ `noi_dia` + `hang_nang`.
- A4: số trước khi cộng cố định là 3.414 đ/việc (4.599 − 1.185), và nhắc ghi rõ đã cộng cố định chưa, ở khối lượng nào.
- CP2: kiểm quy tắc ½ – 2× đủ ba cặp (5,6 / 2,8 · 40,7 / 20,3 · 51,8 / 25,9) và B2 = 5,6 + 40,7 = 46,3%; nêu câu B3 "thêm 85 yêu cầu" là so với giới hạn 2 lần (319 − 234), không phải 3 lần.
- Báo người giữ hồ sơ sửa mục 3: 222 yêu cầu là nhân viên "làm thay", không phải "làm lại" (tên một khoản chi phí khác).

**Gắn nhãn CP3.** Gắn độc lập 20 ca trên phiếu `phieu_gan_nhan_CP3.md`, không trao đổi với người gắn nhãn 2 và không xem bảng tham khảo. Phân bố nhãn: Do người dùng 4 · Hệ thống 5 · Ngữ cảnh 4 · Giới hạn hệ thống 4 · Ngầm 3. Đồng thuận với người gắn nhãn 2: 20/20 = 100%. Ghi ba ca dễ phân vân và lý do chốt, nhóm dùng làm quy tắc trong `bang_loi.md`:

- Ca 1 chốt Do người dùng (gốc là khách nhập thiếu số), dù trợ lý có thể kiểm tra số tài khoản.
- Ca 13 chốt Giới hạn hệ thống (gốc là ngoài phạm vi), dù trợ lý trả lời chung chung.
- Ca 17 chốt Ngầm (không ai nhận ra, chỉ lộ qua kiểm tra mẫu), dù gốc kỹ thuật là bộ nhớ đệm cũ.

**Nháp CP4.** Tính từ `logix_requests.csv` để đặt ngưỡng theo tỉ lệ hiện tại, không đặt theo cảm tính:

- Mở lại 7 ngày: 4,25% (51/1.200) toàn mẫu, 3,97% (39/982) trong phạm vi; riêng `hang_nang` 8,23% (13/158).
- Ca được xem lại bị sửa hoặc bỏ gợi ý: 27,1% (48/177).
- Ba luật dừng theo mẫu NẾU – TRONG – THÌ – KHÔNG THÌ: an toàn (trần 6% hoặc chênh 2 điểm so với đối chứng; 1 ca hoàn trùng là dừng ngay), chi phí (8.000 đ/việc), mức độ sử dụng (40% sửa hoặc bỏ gợi ý).
- Sửa luật chi phí sang chi phí **chưa cộng cố định**: ở bước rollout 10% (khoảng 4.500 yêu cầu/tháng), riêng cố định đã là 40.000.000 / (4.500 × 0,75) ≈ 11.852 đ/việc, luật sẽ kích ngay tuần đầu. Kiểm tra ngưỡng: 8.000 + 2.370 = 10.370 đ < 12.000 đ (0,86×) ở nửa khối lượng.
- Năm câu D2 cho cách chia theo nhân viên 20 + 20. Người giữ hồ sơ đã chép luật dừng và D2 vào `pilot_plan.yaml` (commit `07509f7`, `caf68fd`).

## 4. Bằng chứng

- Commit `287c122` — CP1 done: bổ sung `report/team/bang_chi_phi.md`.
- Commit `8f056c7` — cp3.1 done: `phieu_gan_nhan_CP3.md`, bộ nhãn độc lập 20 ca.
- Commit `a8a9238` — cp4: `nhap_CP4_N1.md`, tỉ lệ mở lại, D2, ba luật dừng.
- Commit `4a10651` — sua luat: sửa ba luật dừng (vế KHÔNG THÌ, hoàn trùng, chi phí chưa cộng cố định).
- Cột "Nhãn người 1" và ba quy tắc chốt trong `report/team/bang_loi.md`; mục `stop_rules` và phần chú thích D2 trong `report/team/pilot_plan.yaml`.

## 5. Công cụ AI đã dùng

- **Claude (Claude Code):** tóm tắt checkpoint và phân vai; đối chiếu số trong `bang_chi_phi.md` với hướng dẫn; cài môi trường và chạy `lab13.py`; dựng phiếu gắn nhãn trống từ file đề; tính tỉ lệ mở lại và tỉ lệ sửa/bỏ gợi ý; viết nháp D2 và luật dừng.
- **Không dùng AI để gắn nhãn:** phiếu do AI dựng chỉ có mô tả ca và định nghĩa, cột nhãn để trống; 20 nhãn và ghi chú do mình tự gắn rồi mới đưa vào phiếu.
- **Cách tự kiểm tra:** chạy `python lab13.py` trên máy mình và so với bảng của nhóm; tính tay 5.865 đ, 3.414 đ và 11.852 đ; kiểm lại bốn vế của từng luật dừng và đọc lại xem vế KHÔNG THÌ có phải là việc bị cấm không; tự đặt câu hỏi liệu ngưỡng có làm pilot dừng ngay tuần đầu không trước khi chốt.

## 6. Tự đánh giá

- Làm được: bộ nhãn độc lập đạt đồng thuận 20/20; phát hiện luật chi phí bản đầu sẽ dừng pilot sai ở bước rollout nhỏ và sửa lại.
- Hiểu được: gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa; ngưỡng an toàn phải đặt từ tỉ lệ hiện tại (3,97%), nếu đặt 3% thì pilot dừng ngay tuần đầu; chi phí cố định chia cho khối lượng nhỏ làm sai lệch luật chi phí.
- Cần cải thiện: tự tính tay nhiều hơn thay vì dựa vào script; tham gia sớm hơn vào phần chỉ số và event của CP5.
