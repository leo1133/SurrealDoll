# TEST CASES: 8. CAPTCHA / SLIDER PUZZLE

- **Mục đích:** Hộp kiểm 'I'm not a robot' hoặc thanh trượt kéo mảnh ghép vào đúng vị trí để chống spam/bot tự động
- **Tổng số Test Case:** **6** (`High`: 5 | `Medium`: 1 | `Low`: 0)

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_CAP_001`** (High): Kiểm tra giao diện hiển thị của hộp kiểm Captcha ('I'm not a robot') và khung kéo mảnh ghép Slider Puzzle
- [ ] **`TC_CAP_002`** (High): Kiểm tra xác thực thành công khi kéo mảnh ghép khớp đúng vào vị trí ô khuyết (trong ngưỡng sai số `±3px - 5px`)
- [ ] **`TC_CAP_003`** (High): Kiểm tra xử lý khi kéo mảnh ghép lệch vị trí (Tự động bật thanh trượt về đầu và đổi câu đố mới)
- [ ] **`TC_CAP_004`** (High): Kiểm tra chặn gửi biểu mẫu (Submit Form) khi người dùng chưa hoàn thành xác thực Captcha
- [ ] **`TC_CAP_005`** (Medium): Kiểm tra nút `Làm mới câu đố (Refresh 🔄)` và xử lý khi phiên Captcha bị hết hạn (`Captcha Expired`)
- [ ] **`TC_CAP_006`** (High): Kiểm tra xác thực Token Captcha ở phía Backend (Chống Bypass Captcha qua Postman/API và chống dùng lại Token cũ)

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_CAP_001` | UI / Giao diện | **High** | **Kiểm tra giao diện hiển thị của hộp kiểm Captcha ('I'm not a robot') và khung kéo mảnh ghép Slider Puzzle** | Màn hình Đăng nhập, Đăng ký hoặc Quên mật khẩu có tích hợp Captcha / Slider Puzzle. | 1. Quan sát khung Captcha hoặc hộp thoại Slider Puzzle (bức ảnh nền có ô khuyết, mảnh ghép nổi bên trái, thanh trượt kéo bên dưới và nút làm mới ảnh `🔄`). | Giao diện Captcha / Slider Puzzle | - Hình ảnh câu đố rõ nét, vị trí ô khuyết có viền đổ bóng dễ nhận diện.<br>- Mảnh ghép nằm đúng cùng độ cao trục dọc (`Y-axis`) với ô khuyết trên ảnh. | `Not Run` |
| `TC_CAP_002` | Functional / Chức năng | **High** | **Kiểm tra xác thực thành công khi kéo mảnh ghép khớp đúng vào vị trí ô khuyết (trong ngưỡng sai số `±3px - 5px`)** | Khung Slider Puzzle đang hiển thị. | 1. Nhấn giữ chuột (hoặc ngón tay trên Mobile) vào nút kéo thanh trượt.<br>2. Kéo mảnh ghép di chuyển ngang đến khớp vào đúng vị trí ô khuyết trên ảnh (lệch nhẹ khoảng `1-3px`) rồi thả chuột ra. | Kéo mảnh ghép khớp vị trí (`±3px`) | - Mảnh ghép di chuyển đồng bộ theo con trượt chuột không bị trễ.<br>- Khi thả chuột khớp vị trí (trong dung sai cho phép `±3px - 5px`), hệ thống báo xác thực thành công (hiện dấu tích xanh `✓` kèm thời gian hoàn thành, VD: `'Xác thực thành công trong 1.2s'`) và cho phép gửi biểu mẫu. | `Not Run` |
| `TC_CAP_003` | Validation & Negative | **High** | **Kiểm tra xử lý khi kéo mảnh ghép lệch vị trí (Tự động bật thanh trượt về đầu và đổi câu đố mới)** | Khung Slider Puzzle đang hiển thị. | 1. Kéo mảnh ghép dừng ở vị trí lệch xa ô khuyết (hoặc kéo quá lố sang kịch mép phải) rồi thả chuột. | Kéo lệch vị trí ô khuyết | - Khung thanh trượt chuyển sang màu đỏ kèm hiệu ứng rung cảnh báo lỗi.<br>- Con trượt tự động trượt lùi về điểm xuất phát ban đầu.<br>- Bức ảnh và vị trí ô khuyết tự động làm mới sang một vị trí ngẫu nhiên khác để chống bot thử lặp lại tọa độ cũ. | `Not Run` |
| `TC_CAP_004` | Validation & Negative | **High** | **Kiểm tra chặn gửi biểu mẫu (Submit Form) khi người dùng chưa hoàn thành xác thực Captcha** | Biểu mẫu Đăng ký / Đăng nhập có bắt buộc xác thực Captcha. | 1. Điền đầy đủ tài khoản và mật khẩu hợp lệ nhưng **bỏ qua không tích/kéo Captcha**.<br>2. Click nút `Đăng nhập / Gửi`. | Submit Form khi chưa qua Captcha | - Hệ thống chặn gửi Request và hiển thị thông báo `'Vui lòng hoàn thành xác thực bảo mật (Captcha)'` (hoặc tự động bật popup Slider Puzzle yêu cầu người dùng kéo mảnh ghép). | `Not Run` |
| `TC_CAP_005` | Functional / Chức năng | **Medium** | **Kiểm tra nút `Làm mới câu đố (Refresh 🔄)` và xử lý khi phiên Captcha bị hết hạn (`Captcha Expired`)** | Đang ở màn hình có Captcha. | 1. Click vào biểu tượng `🔄 (Làm mới)` trên góc khung Captcha.<br>2. Hoàn thành tích chọn Captcha `I'm not a robot`, nhưng giữ nguyên trang không bấm Submit trong 2 phút cho đến khi Captcha hết hạn. | Click `🔄 Refresh` & Chờ 2 phút hết hạn | - Bước 1: Tải bức ảnh/mã Captcha mới ngay lập tức để người dùng dễ nhìn hơn.<br>- Bước 2: Sau 2 phút không gửi form, dấu tích xanh tự động hủy và hiện thông báo `'Phiên xác thực đã hết hạn, vui lòng xác thực lại'`. | `Not Run` |
| `TC_CAP_006` | Security / Bảo mật | **High** | **Kiểm tra xác thực Token Captcha ở phía Backend (Chống Bypass Captcha qua Postman/API và chống dùng lại Token cũ)** | API xử lý Đăng nhập / Đăng ký có kiểm tra `captcha_token`. | 1. Dùng công cụ API (Postman/cURL) gửi thẳng Request lên Server với `captcha_token = ""` hoặc chuỗi giả mạo.<br>2. Dùng lại 1 `captcha_token` hợp lệ vừa sử dụng thành công ở lần trước để gửi Request lần thứ 2. | Gửi `captcha_token` rỗng/giả hoặc Replay Token cũ | - Server Backend từ chối xử lý (`400 Bad Request` / `403 Forbidden`) ở cả 2 trường hợp; mỗi Token Captcha chỉ có giá trị xác thực duy nhất 1 lần. | `Not Run` |
