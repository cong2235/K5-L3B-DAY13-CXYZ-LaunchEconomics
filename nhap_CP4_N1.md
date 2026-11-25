# Nháp CP4 · Phần của Người gắn nhãn 1 (bước 4.3 hỗ trợ, 4.4, 4.5)

Tài liệu nháp nội bộ, không nằm trong thư mục nộp. N2 chép sang `report/team/pilot_plan.yaml` (bước 4.6). Số tính bằng `src/.venv` trên `logix_requests.csv`, lệnh ở cuối file. Mọi số từ dữ liệu là `simulated`.

## Đầu vào đã tính (hỗ trợ bước 4.3, C đối chiếu lại)

| Số | Giá trị | Cách tính |
| --- | ---: | --- |
| Tỉ lệ `mo_lai_trong_7_ngay`, toàn mẫu | **4,25%** (51/1.200) | `mean()` trên cả file |
| Tỉ lệ mở lại, phạm vi `noi_dia` + `hang_nang` | **3,97%** (39/982) | lọc `loai` rồi `mean()` |
| Riêng `noi_dia` | 3,16% (26/824) | |
| Riêng `hang_nang` | **8,23%** (13/158) | |
| Depot có tỉ lệ cao nhất | D06 5,1% · D02 5,0% | `groupby('depot')` |
| Ca được xem lại | 177/1.200 | `duoc_xem_lai == 1` |
| Trong ca được xem lại: giữ · sửa · bỏ | 72,9% · 23,2% · 4,0% | `quyet_dinh_xem_lai` |
| Sửa hoặc bỏ gợi ý (không dùng nguyên câu trả lời) | **27,1%** (48/177) | sửa + bỏ |

Nhận xét cho luật an toàn: ngưỡng tuyệt đối 3% sẽ làm pilot dừng ngay tuần đầu (hiện đã 3,97%). `hang_nang` một mình đã 8,23%, nên trần tuyệt đối phải áp cho cả phạm vi, và theo dõi riêng `hang_nang` bằng mức chênh so với đối chứng.

## Bước 4.5 · Ba luật dừng (NẾU – TRONG – THÌ – KHÔNG THÌ)

1. **An toàn:** "NẾU tỉ lệ mở lại 7 ngày của nhóm trợ lý cao hơn nhóm đối chứng từ 2 điểm trở lên, hoặc vượt 6% trên phạm vi noi_dia + hang_nang (hiện 3,97%, simulated), hoặc có từ 1 ca hoàn trùng TRONG 3 ngày liên tiếp THÌ Giám đốc vận hành tắt trợ lý trong 30 phút và chuyển toàn bộ yêu cầu về nhân viên tự làm KHÔNG THÌ không được sang bước rollout tiếp theo"
2. **Chi phí:** "NẾU chi phí mỗi việc thành công (đã cộng chi phí cố định) vượt 8.000 đ TRONG 2 tuần liên tiếp THÌ PM thu hẹp phạm vi về noi_dia và giới hạn tối đa 2 lần chạy KHÔNG THÌ không được mở rộng sang hang_nang"
   - Căn cứ: mức hiện tại 5.784 đ/việc ở nửa khối lượng (A4, simulated). 8.000 đ là mức tăng khoảng 38%, tương đương kịch bản xem lại gấp đôi (+40,7%, B1). Vẫn dưới 12.000 đ (0,67×).
3. **Mức độ sử dụng:** "NẾU tỉ lệ nhân viên sửa hoặc bỏ gợi ý vượt 40% TRONG 1 tuần THÌ Trưởng nhóm CSKH phỏng vấn 5 nhân viên trong 3 ngày và gửi PM danh sách lý do KHÔNG THÌ không được chuyển bước rollout"
   - Căn cứ: hiện 27,1% (48/177 ca được xem lại, simulated). 40% là cao hơn hiện tại khoảng 13 điểm.

## Bước 4.4 · Năm câu D2 "tách được tác động"

Câu 1, 2, 4 không phụ thuộc cách chia. Câu 3 và 5 viết **giả định chia theo nhân viên, 20 + 20** (phương án phổ biến khi D1 cho thấy theo depot chỉ 6 cụm và theo yêu cầu thì tràn tác động cao). **Nếu nhóm chọn cách chia khác sau D1 thì sửa lại câu 3 và 5.**

1. **Đối chứng chạy cùng thời gian:** Có. Nhóm đối chứng làm cùng tuần, cùng depot, cùng loại yêu cầu với nhóm trợ lý.
2. **Chia ngẫu nhiên hay do người chọn:** Ngẫu nhiên. Bốc thăm bằng code với seed ghi trước, phân tầng theo depot để mỗi depot có người ở cả hai nhóm.
3. **Ảnh hưởng gián tiếp và cách giảm:** Có rủi ro nhân viên cùng depot chia sẻ câu trả lời của trợ lý. Giảm bằng quyền truy cập trợ lý theo tài khoản và log lượt mở trợ lý theo `staff_id` để phát hiện nhóm đối chứng dùng ké.
4. **Viết trước:** Có. Chỉ số chính `dong_trong_24h_khong_mo_lai_7_ngay`, ngưỡng, ba luật dừng và ngày quyết định chốt trong file này trước ngày bắt đầu, không đổi giữa chừng.
5. **Ít nhất 20 cụm mỗi nhóm:** Có, đúng 20 nhân viên mỗi nhóm (công ty có 40 nhân viên CSKH).

## Còn chờ người khác

- **C (4.1):** năm câu D1. Từ đó cả nhóm chốt cách chia và mức chênh (5 hay 6 điểm), rồi kiểm lại câu 3 và 5 ở trên.
- **C (4.3):** chạy lại tỉ lệ mở lại để đối chiếu với bảng trên.
- **N2 (4.6):** chép luật dừng vào `stop_rules`, D2 vào phần chú thích đầu file và `identifiability`.

## Lệnh đã chạy (trong `src/`)

```python
import pandas as pd
r = pd.read_csv('logix_requests.csv', keep_default_na=False)
s = r[r.loai.isin(['noi_dia', 'hang_nang'])]
r.mo_lai_trong_7_ngay.mean(), s.mo_lai_trong_7_ngay.mean()
r.groupby('loai').mo_lai_trong_7_ngay.agg(['sum', 'count', 'mean'])
r.groupby('depot').mo_lai_trong_7_ngay.mean()
r[r.duoc_xem_lai == 1].quyet_dinh_xem_lai.value_counts(normalize=True)
```
