# TEST CASE: 4. CUSTOM EXPORT CONFIGURATION MODAL (HỘP THOẠI TÙY CHỈNH CỘT & TÙY CHỌN XUẤT)

- **Mục đích:** Hộp thoại cấu hình nâng cao cho phép chọn các cột dữ liệu cần xuất, chọn khoảng thời gian, định dạng file trước khi tải
- **Tổng số kịch bản:** **5 Test Cases** (`High: 3`, `Medium: 1`, `Low: 1`)

---

## I. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_CFG_001`** ([High] - *UI & Functional*): Kiểm tra giao diện hộp thoại Tùy chỉnh xuất dữ liệu và tính năng chọn/bỏ chọn các cột muốn xuất
- [ ] **`TC_CFG_002`** ([Medium] - *Functional / Chức năng*): Kiểm tra nút 'Chọn tất cả cột (Select All)' / 'Bỏ chọn tất cả' và khôi phục mặc định trong Modal Export
- [ ] **`TC_CFG_003`** ([High] - *Validation & Negative*): Kiểm tra chặn xuất file khi người dùng bỏ chọn hết tất cả các cột (0 cột được chọn) hoặc khoảng ngày không hợp lệ
- [ ] **`TC_CFG_004`** ([High] - *Validation & Security*): Kiểm tra che giấu dữ liệu nhạy cảm (PII Data Masking) hoặc ẩn cột bảo mật trong file xuất theo phân quyền
- [ ] **`TC_CFG_005`** ([Low] - *Functional / Chức năng*): Kiểm tra lưu mẫu cấu hình cột thường xuất (Save Export Template / Preset)

---

## II. Bảng Chi Tiết Kịch Bản Kiểm Thử

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_CFG_001` | UI & Functional | **High** | **Kiểm tra giao diện hộp thoại Tùy chỉnh xuất dữ liệu và tính năng chọn/bỏ chọn các cột muốn xuất** | Click nút `[Xuất dữ liệu]` mở ra Modal cấu hình xuất báo cáo (có danh sách 10 cột dữ liệu để chọn). | 1. Bỏ tích 6 cột, chỉ giữ lại 4 cột: `Mã KH`, `Họ tên`, `Số điện thoại`, `Tổng chi tiêu`.<br>2. Click nút `[Xuất file]` và mở file Excel tải về. | Chọn 4/10 cột trong Modal Export | - File Excel tải về chỉ hiển thị đúng **4 cột** đã được người dùng tích chọn theo đúng thứ tự, không chứa 6 cột đã bỏ tích. | `Not Run` |
| `TC_CFG_002` | Functional / Chức năng | **Medium** | **Kiểm tra nút 'Chọn tất cả cột (Select All)' / 'Bỏ chọn tất cả' và khôi phục mặc định trong Modal Export** | Đang mở Modal Tùy chỉnh xuất dữ liệu. | 1. Click vào checkbox `'Bỏ chọn tất cả'`.<br>2. Click vào `'Chọn tất cả'`.<br>3. Đóng Modal bằng nút `[Hủy]` rồi mở lại. | Select All / Deselect All Columns | - Bước 1: Tất cả các cột được bỏ tích nhanh chóng.<br>- Bước 2: Tất cả các cột được tích chọn đầy đủ.<br>- Bước 3: Khi bấm `[Hủy]`, không có file nào được tải về và Modal đóng lại. | `Not Run` |
| `TC_CFG_003` | Validation & Negative | **High** | **Kiểm tra chặn xuất file khi người dùng bỏ chọn hết tất cả các cột (0 cột được chọn) hoặc khoảng ngày không hợp lệ** | Đang mở Modal Tùy chỉnh xuất dữ liệu. | 1. Bỏ tích toàn bộ các cột dữ liệu (0 cột được chọn) và quan sát nút `[Xuất file]`.<br>2. Chọn khoảng ngày xuất có `Từ ngày > Đến ngày` rồi bấm `[Xuất file]`.  | Chọn 0 cột & Từ ngày > Đến ngày | - Bước 1: Khi 0 cột được chọn, nút `[Xuất file]` bị vô hiệu hóa (`Disabled`) hoặc hiển thị thông báo `'Vui lòng chọn ít nhất 1 cột dữ liệu để xuất'`.<br>- Bước 2: Hiển thị lỗi `'Ngày bắt đầu không được lớn hơn ngày kết thúc'` và chặn gửi yêu cầu. | `Not Run` |
| `TC_CFG_004` | Validation & Security | **High** | **Kiểm tra che giấu dữ liệu nhạy cảm (PII Data Masking) hoặc ẩn cột bảo mật trong file xuất theo phân quyền** | Đăng nhập bằng tài khoản Nhân viên CSKH (không có quyền xem đầy đủ Số điện thoại / CCCD của khách hàng). | 1. Thực hiện xuất danh sách Khách hàng ra file Excel / CSV.<br>2. Mở file kiểm tra cột Số điện thoại và Email. | Tài khoản bị giới hạn quyền PII thực hiện Export | - Dữ liệu trong file Excel xuất ra vẫn phải tuân thủ quy tắc che giấu bảo mật (VD: `098***4321`) giống như trên giao diện Web, **tuyệt đối không để lộ nguyên văn dữ liệu gốc (Plaintext) qua tính năng Export**. | `Not Run` |
| `TC_CFG_005` | Functional / Chức năng | **Low** | **Kiểm tra lưu mẫu cấu hình cột thường xuất (Save Export Template / Preset)** | Modal Export có tùy chọn lưu cấu hình cột yêu thích. | 1. Chọn 5 cột thường dùng -> Tích `'Ghi nhớ lựa chọn cho lần sau'` -> Xuất file.<br>2. Mở lại Modal Export lần tiếp theo. | Ghi nhớ cấu hình cột đã chọn | - Hệ thống tự động tích sẵn đúng 5 cột mà người dùng đã lưu ở lần xuất trước. | `Not Run` |
