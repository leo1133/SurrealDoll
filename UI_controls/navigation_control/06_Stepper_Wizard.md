# TEST CASE: 6. STEPPER / WIZARD

- **Mô tả chức năng:** Thanh hiển thị các bước của một quy trình (Bước 1: Giỏ hàng -> Bước 2: Thanh toán -> Bước 3: Hoàn tất)
- **Tổng số Test Case:** **7** (`High: 6` | `Medium: 1` | `Low: 0`)
- **Phân bổ theo loại kiểm thử:** UI / Giao diện: **1**, Functional / Chức năng: **3**, Validation & Negative: **2**, Security / Bảo mật: **1**

---

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_STP_001`** [High] _UI / Giao diện_ — Kiểm tra giao diện thanh Stepper và hiển thị rõ 3 trạng thái: Đã qua, Hiện tại và Tiếp theo
- [ ] **`TC_STP_002`** [High] _Functional / Chức năng_ — Kiểm tra chuyển tiếp tuần tự qua các bước (Next Step) khi dữ liệu hợp lệ
- [ ] **`TC_STP_003`** [High] _Validation & Negative_ — Kiểm tra chặn chuyển sang bước tiếp theo khi dữ liệu ở bước hiện tại chưa hợp lệ
- [ ] **`TC_STP_004`** [High] _Functional / Chức năng_ — Kiểm tra quay lại bước trước (Previous Step) và bảo toàn dữ liệu đã nhập
- [ ] **`TC_STP_005`** [High] _Functional / Chức năng_ — Kiểm tra cập nhật dữ liệu phụ thuộc ở các bước sau khi quay lại sửa dữ liệu ở bước trước
- [ ] **`TC_STP_006`** [High] _Validation & Negative_ — Kiểm tra hoàn tất quy trình tại bước cuối cùng và chặn gửi lặp lại khi bấm nút Back của trình duyệt
- [ ] **`TC_STP_007`** [Medium] _Security / Bảo mật_ — Kiểm tra chặn truy cập nhảy cóc qua URL trực tiếp (Deep Link Bypass)

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_STP_001` | UI / Giao diện | **High** | **Kiểm tra giao diện thanh Stepper và hiển thị rõ 3 trạng thái: Đã qua, Hiện tại và Tiếp theo** | Màn hình quy trình gồm 3 bước (VD: Bước 1: Giỏ hàng -> Bước 2: Thanh toán -> Bước 3: Hoàn tất). | 1. Quan sát thanh Stepper khi đang ở Bước 2. | Đang ở Bước 2 trên tổng số 3 bước | - **Bước 1 (Completed)**: Hiển thị dấu tick hoàn thành (`✓`), đường kẻ nối từ Bước 1 sang Bước 2 đổi sang màu hoàn thành.<br>- **Bước 2 (Active/Current)**: Vòng tròn số `2` và tên bước được tô màu chủ đạo nổi bật nhất.<br>- **Bước 3 (Upcoming/Inactive)**: Hiển thị màu xám mờ. | `Not Run` |
| `TC_STP_002` | Functional / Chức năng | **High** | **Kiểm tra chuyển tiếp tuần tự qua các bước (Next Step) khi dữ liệu hợp lệ** | Người dùng đang ở Bước 1 của Wizard. | 1. Điền đầy đủ thông tin hợp lệ ở Bước 1 -> Nhấn nút 'Tiếp theo' (Next).<br>2. Điền đầy đủ thông tin hợp lệ ở Bước 2 -> Nhấn nút 'Tiếp theo' (Next). | Bước 1 -> Bước 2 -> Bước 3 | - Hệ thống kiểm tra dữ liệu hợp lệ, chuyển mượt mà từ Bước 1 sang Bước 2, rồi sang Bước 3.<br>- Trạng thái trên thanh Stepper cập nhật chính xác theo từng bước. | `Not Run` |
| `TC_STP_003` | Validation & Negative | **High** | **Kiểm tra chặn chuyển sang bước tiếp theo khi dữ liệu ở bước hiện tại chưa hợp lệ** | Người dùng đang ở Bước 1, các trường bắt buộc còn đang để trống hoặc nhập sai. | 1. Nhấn nút 'Tiếp theo' (Next).<br>2. Thử click trực tiếp vào biểu tượng 'Bước 2' hoặc 'Bước 3' trên thanh Stepper. | Dữ liệu Bước 1 không hợp lệ | - Hệ thống **chặn** không cho chuyển sang Bước 2 hoặc Bước 3.<br>- Giữ người dùng ở lại Bước 1 và hiển thị thông báo lỗi validation tại các trường chưa hợp lệ. | `Not Run` |
| `TC_STP_004` | Functional / Chức năng | **High** | **Kiểm tra quay lại bước trước (Previous Step) và bảo toàn dữ liệu đã nhập** | Người dùng đã điền xong Bước 1 và hiện đang ở Bước 2. | 1. Nhấn nút 'Quay lại' (Back / Previous) hoặc click vào tiêu đề 'Bước 1' đã hoàn thành trên thanh Stepper.<br>2. Quan sát dữ liệu trong các ô nhập liệu của Bước 1. | Quay lại từ Bước 2 về Bước 1 | - Hệ thống quay trở lại màn hình Bước 1.<br>- **Toàn bộ dữ liệu** người dùng đã nhập ở Bước 1 trước đó vẫn được giữ nguyên đầy đủ, không bị xóa trắng bắt nhập lại. | `Not Run` |
| `TC_STP_005` | Functional / Chức năng | **High** | **Kiểm tra cập nhật dữ liệu phụ thuộc ở các bước sau khi quay lại sửa dữ liệu ở bước trước** | Đã qua Bước 1 (Chọn 2 sản phẩm = 500k) và sang Bước 2 (Hiển thị tổng tiền thanh toán = 500k). | 1. Từ Bước 2, nhấn 'Quay lại' Bước 1.<br>2. Thay đổi số lượng thành 3 sản phẩm (= 750k) rồi nhấn 'Tiếp theo' sang lại Bước 2. | Sửa Bước 1 (500k -> 750k) -> Sang Bước 2 | - Khi sang lại Bước 2, thông tin tóm tắt đơn hàng và tổng số tiền phải được tính toán và cập nhật mới thành `750k` (không bị lưu cache giá trị cũ 500k). | `Not Run` |
| `TC_STP_006` | Validation & Negative | **High** | **Kiểm tra hoàn tất quy trình tại bước cuối cùng và chặn gửi lặp lại khi bấm nút Back của trình duyệt** | Người dùng đã hoàn tất quy trình và đang ở Bước 3 (Màn hình Hoàn tất / Thành công). | 1. Tại màn hình Hoàn tất (Bước 3), nhấn nút `Back` của trình duyệt hoặc thử click lại Bước 2 trên thanh Stepper. | Đã hoàn tất ở Bước 3 -> Nhấn Browser Back | - Các bước 1, 2 trên thanh Stepper ở màn hình Hoàn tất không còn cho phép click quay lại sửa.<br>- Nếu nhấn nút `Back` của trình duyệt, hệ thống điều hướng về trang Danh sách đơn hàng / Trang chủ thay vì cho phép Submit trùng lặp lại đơn hàng vừa tạo. | `Not Run` |
| `TC_STP_007` | Security / Bảo mật | **Medium** | **Kiểm tra chặn truy cập nhảy cóc qua URL trực tiếp (Deep Link Bypass)** | Người dùng chưa thực hiện Bước 1 và Bước 2. | 1. Gõ trực tiếp URL của Bước 3 (VD: `/checkout/step-3`) lên thanh địa chỉ trình duyệt và nhấn Enter. | Truy cập thẳng `/checkout/step-3` | - Hệ thống kiểm tra trạng thái phiên giao dịch, phát hiện chưa qua Bước 1-2 và tự động điều hướng (Redirect) người dùng quay về **Bước 1**. | `Not Run` |
