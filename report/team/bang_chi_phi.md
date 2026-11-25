# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 lần · ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 lần · ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25× · ĐẠT |

## A2 · Mô hình chi phí từ trace

| Khoản | Kết quả | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 đ | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 đ | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 đ | Token và tool của các dòng có `attempt > 1` | đo từ trace |
| Xem lại | 1.780.000 đ | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 đ | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 đ | Token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 việc | `ket_qua == 'thanh_cong'` | |
| Chi phí mỗi việc thành công | 4.472 đ/việc | Tổng chi phí chia cho 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,65 đ/yêu cầu | Token + tool chia cho 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,3 lần** hoá đơn token và tool trên mỗi yêu cầu (`simulated`).
- Làm lại chiếm tỉ trọng lớn nhất, **51,8%** tổng chi phí, tiếp theo là xem lại **40,7%** (1.780.000 / 4.373.585); giờ nhân viên chiếm **92,5%** tổng chi phí (`simulated`).
- Vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm `thanh_cong`: lần chạy lỗi vẫn tốn token và tool (93.804 đ là của lần chạy 2 và 3), còn công ty chỉ nhận giá trị từ **978** việc thành công, nên chia cho 1.200 sẽ làm chi phí trông rẻ hơn thật.
- Khi so với 12.000 đ: 4.472 đ chưa tính 222 yêu cầu không thành công mà nhân viên phải làm. Chi phí cả hệ thống = (4.373.585 + 222 × 12.000) / 1.200 = **5.865 đ/yêu cầu = 0,49×** (`simulated`, tính tay).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công (simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

- `quoc_te` đạt **27,3%** thành công và tốn **1,88×** mốc 12.000 đ (`simulated`). Chạy lại cho ít kết quả, với tỉ lệ `ok` giảm từ **30,0%** ở lần 1 xuống **11,4%** ở lần 2 và **2,2%** ở lần 3.
- Kết luận phạm vi: loại `quoc_te` (1,88×, lỗi lặp lại trên cùng yêu cầu nên chạy lại chỉ tốn thêm tiền); `doi_tac` sát ngưỡng (**0,85×**, thành công 54,4%) và có điều khoản riêng nên cũng loại. Phạm vi pilot: `noi_dia` + `hang_nang` (`simulated`).

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định (simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| Một nửa khối lượng (22.500 yêu cầu/tháng) | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Chi phí mỗi việc thành công vẫn dưới **12.000 đ** ở cả hai mức. Khi khối lượng giảm từ **45.000** còn **22.500** yêu cầu/tháng, chi phí tăng từ **4.599 đ** lên **5.784 đ/việc** (`simulated`).
- Trước khi cộng cố định, chi phí mỗi việc thành công trong phạm vi là 3.072.513 / 900 = **3.414 đ**. Khi đưa số vào hồ sơ phải ghi rõ đã cộng cố định chưa và ở khối lượng nào (`simulated`).

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (simulated) | Thay đổi so với A2 (simulated) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có `attempt > 2`. Yêu cầu có `so_lan_chay > 2` chuyển nhân viên, với 0 phút xem lại và làm lại trong mô hình trợ lý. | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Áp dụng cùng quy tắc với giới hạn 1. | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token và tỉ lệ xem lại cùng gấp đôi đưa chi phí lên **6.543 đ/việc**, tăng **46,3%** (`simulated`). Mỗi yếu tố làm tăng một khoản riêng, số việc thành công giữ nguyên, nên mức tăng bằng **5,6% + 40,7%** sau làm tròn.
- Ba yếu tố có mức thay đổi tuyệt đối lớn nhất theo B1 là **số ca làm lại (51,8%)**, **tỉ lệ xem lại (40,7%)** và **lương nhân viên (23,1%)** (`simulated`).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý (simulated) | Số yêu cầu không thành công | Chi phí cả hệ thống (simulated) | Chi phí mỗi việc thành công (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- **2 lần** rẻ nhất cho cả hệ thống (**6.901.220 đ**). **1 lần** cho chi phí mỗi việc thành công thấp nhất (**4.111 đ**), nhưng có thêm **85** yêu cầu không thành công mà mô hình tính **12.000 đ/ca** cho nhân viên làm thay (`simulated`).

## B4 · Nếu phải xem lại tất cả

- Xem lại đủ **948** ca có lần chạy `ok` trong phạm vi `noi_dia` + `hang_nang`, mỗi ca **5 phút**. Với **48** ca làm lại, chi phí là **11.743 đ/việc (0,98×)** nếu làm lại mất **9 phút/ca**, hoặc **12.415 đ/việc (1,03×)** nếu mất **15,3 phút/ca** (`simulated`).
- Pilot cần đo mức giảm tỉ lệ xem lại vẫn an toàn và thời gian xem lại thực tế. Với độ phủ xem lại 100%, ngưỡng hòa vốn lần lượt khoảng **5,1** và **4,8 phút xem lại/ca** (`simulated`).
