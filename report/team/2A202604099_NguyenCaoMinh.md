# Báo cáo cá nhân — Nguyễn Cao Minh-2A202604099

## 1. Thông tin thành viên

- Họ tên: Nguyễn Cao Minh
- MSSV: 2A202604099
- Email: 26ai.minhnc@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người viết code

## 2. Phần việc phụ trách

- Viết và kiểm tra code tính chi phí ở CP1 và phân tích độ nhạy ở CP2 trong `src/lab13.py`.
- Ghi kết quả A1–A4 và B1–B4 vào bảng chi phí của nhóm.
- Sửa font tiếng Việt và cải thiện giao diện bộ slide debate của nhóm.

## 3. Đóng góp cụ thể

- **CP1:** Viết ba hàm về xác suất và số lần chạy lại, cùng mô hình tính chi phí mỗi việc thành công. Mô hình cộng tiền token, tool, xem lại và làm lại cho toàn bộ mẫu, rồi chia cho số yêu cầu thành công. Tính tiếp kết quả cho bốn loại yêu cầu và phân bổ chi phí cố định cho nội địa và hàng nặng ở hai mức khối lượng.
- **CP2:** Chạy đủ 9 kịch bản độ nhạy, tính tác động khi giá token và tỉ lệ xem lại cùng tăng, và xếp hạng ba yếu tố ảnh hưởng mạnh nhất. Mô phỏng giới hạn 1, 2 và 3 lượt chạy, tính thêm chi phí nhân viên xử lý các yêu cầu chưa thành công, rồi kiểm tra kịch bản xem lại 100% ca có lượt chạy `ok` trong phạm vi pilot.
- **Slide debate:** Chỉnh font và font dự phòng cho chữ tiếng Việt, thiết kế lại trang bìa, bảng, thẻ số liệu và thanh điều hướng. Thêm bộ đếm slide, điều chỉnh bố cục cho màn hình nhỏ và giữ nguyên nội dung, thứ tự, kịch bản nói của cả 15 slide.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- **CP1:** Commit `cc3a03c`. Cả ba phép thử A1 đều đạt **1,20 · 1,25 · 1,25**. A2 tính được **978 việc thành công** với chi phí **4.472 đ/việc** (`simulated`). [Code CP1–CP2](../../src/lab13.py)
- **CP2:** Commit `7d4df08`. B3 cho thấy giới hạn 2 lượt có chi phí cả hệ thống thấp nhất, **6.901.220 đ**. B4 cho kết quả **11.743–12.415 đ/việc** tùy số phút làm lại (`simulated`). [Bảng kết quả A1–B4](bang_chi_phi.md)

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- **ChatGPT trong Codex:** Hỗ trợ giải thích đề, triển khai mô hình CP1–CP2, chỉnh giao diện slide và soạn báo cáo cá nhân.
- **Kiểm tra code:** Chạy `python lab13.py` từ `src/`, đối chiếu ba mốc A1 và số trong bảng với đầu ra. Dùng số chưa làm tròn để kiểm tra mức giảm của từng kịch bản “giảm một nửa” bằng nửa mức tăng của kịch bản “gấp đôi”.
- **Kiểm tra slide:** Mở file bằng Chromium, kiểm tra chữ tiếng Việt, chuyển slide, bật/tắt kịch bản nói và cuộn bảng trên màn hình nhỏ.

## 6. Tự đánh giá

- Qua CP1 và CP2, tôi hiểu vì sao chi phí mỗi việc thành công phải tính cả lượt chạy lỗi, và vì sao giới hạn chạy rẻ nhất cho trợ lý có thể khác giới hạn rẻ nhất cho cả hệ thống.
- Nếu làm lại, tôi sẽ chuẩn bị sớm một bộ kiểm tra cho các kịch bản CP2 để nhóm đối chiếu kết quả nhanh hơn khi đổi giả định.
