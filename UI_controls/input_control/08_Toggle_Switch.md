# TEST CASE: 8. TOGGLE SWITCH

- **Mô tả chức năng:** Công tắc bật/tắt 2 trạng thái (On/Off, Enable/Disable)
- **Tổng số Test Case:** **6** (`High: 4` | `Medium: 2` | `Low: 0`)
- **Phân bổ theo loại kiểm thử:** UI / Giao diện: **1**, Functional / Chức năng: **2**, Validation & Negative: **1**, Boundary / Giá trị biên: **1**, Usability & Accessibility: **1**

---

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_TOG_001`** [High] _UI / Giao diện_ — Kiểm tra giao diện hiển thị của Toggle Switch ở 2 trạng thái Bật (On) và Tắt (Off)
- [ ] **`TC_TOG_002`** [High] _Functional / Chức năng_ — Kiểm tra thao tác Bật (Off -> On) và Tắt (On -> Off) công tắc Toggle Switch
- [ ] **`TC_TOG_003`** [High] _Functional / Chức năng_ — Kiểm tra lưu trạng thái bền vững sau khi tải lại trang (F5 / Reload)
- [ ] **`TC_TOG_004`** [High] _Validation & Negative_ — Kiểm tra xử lý lỗi và tự động hoàn tác (Rollback) khi API lưu trạng thái thất bại
- [ ] **`TC_TOG_005`** [Medium] _Boundary / Giá trị biên_ — Kiểm tra click liên tục nhiều lần thật nhanh (Spam / Rapid Clicks) vào Toggle Switch
- [ ] **`TC_TOG_006`** [Medium] _Usability & Accessibility_ — Kiểm tra trạng thái Disabled và điều khiển Toggle Switch bằng bàn phím (Tab + Space/Enter)

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_TOG_001` | UI / Giao diện | **High** | **Kiểm tra giao diện hiển thị của Toggle Switch ở 2 trạng thái Bật (On) và Tắt (Off)** | Màn hình cài đặt chứa Toggle Switch đã tải xong. | 1. Quan sát Toggle Switch khi ở trạng thái Off (Disable).<br>2. Quan sát Toggle Switch khi ở trạng thái On (Enable). | N/A | - Trạng thái Off: Nút tròn nằm bên trái, nền công tắc màu xám/trung tính.<br>- Trạng thái On: Nút tròn trượt sang bên phải, nền công tắc đổi sang màu chủ đạo (Xanh lá / Xanh dương).<br>- Trạng thái mặc định hiển thị đúng với dữ liệu hiện tại của người dùng trong hệ thống. | `Not Run` |
| `TC_TOG_002` | Functional / Chức năng | **High** | **Kiểm tra thao tác Bật (Off -> On) và Tắt (On -> Off) công tắc Toggle Switch** | Toggle Switch đang ở trạng thái Off và Enabled. | 1. Click chuột vào Toggle Switch lần 1.<br>2. Kiểm tra hiệu ứng chuyển trạng thái và tính năng liên quan.<br>3. Click chuột vào Toggle Switch lần 2 (hoặc click vào Label đi kèm). | Off -> On -> Off | - Lần 1: Công tắc trượt mượt mà sang trạng thái `On`, tính năng/cài đặt tương ứng được kích hoạt ngay lập tức.<br>- Lần 2: Công tắc trượt về trạng thái `Off`, tính năng tương ứng bị vô hiệu hóa. | `Not Run` |
| `TC_TOG_003` | Functional / Chức năng | **High** | **Kiểm tra lưu trạng thái bền vững sau khi tải lại trang (F5 / Reload)** | Toggle Switch tự động lưu (Auto-save) hoặc lưu qua nút Save. | 1. Gạt Toggle Switch từ Off sang On (và nhấn Lưu nếu có).<br>2. Tải lại trang trình duyệt (F5). | Trạng thái = On | - Sau khi tải lại trang, Toggle Switch vẫn giữ nguyên trạng thái `On` đúng như đã lưu trên Server. | `Not Run` |
| `TC_TOG_004` | Validation & Negative | **High** | **Kiểm tra xử lý lỗi và tự động hoàn tác (Rollback) khi API lưu trạng thái thất bại** | Toggle Switch gọi API ngay khi người dùng gạt công tắc. | 1. Ngắt kết nối mạng (Offline) hoặc giả lập API trả về lỗi 500/403.<br>2. Click gạt Toggle Switch từ Off sang On. | Network Offline / HTTP 500 | - Khi API báo lỗi: Hệ thống hiển thị thông báo lỗi (Toast/Alert) VÀ tự động gạt trả (Rollback) Toggle Switch về lại trạng thái `Off` ban đầu (đảm bảo UI không hiển thị sai lệch với DB). | `Not Run` |
| `TC_TOG_005` | Boundary / Giá trị biên | **Medium** | **Kiểm tra click liên tục nhiều lần thật nhanh (Spam / Rapid Clicks) vào Toggle Switch** | Toggle Switch đang hoạt động. | 1. Click chuột liên tục 5-10 lần thật nhanh vào Toggle Switch.<br>2. Đợi các request hoàn tất và kiểm tra trạng thái trên UI so với trạng thái trong Database. | Rapid clicks (10 lần liên tiếp) | - Hệ thống khóa tạm thời (loading/debounce) trong lúc đang xử lý request hoặc hủy request cũ, đảm bảo trạng thái cuối cùng trên giao diện đồng bộ 100% với trạng thái lưu trong Database. | `Not Run` |
| `TC_TOG_006` | Usability & Accessibility | **Medium** | **Kiểm tra trạng thái Disabled và điều khiển Toggle Switch bằng bàn phím (Tab + Space/Enter)** | Có Toggle Switch ở trạng thái Enabled và Disabled. | 1. Thử click vào Toggle Switch đang bị Disabled.<br>2. Dùng phím `Tab` focus vào Toggle Switch đang Enabled rồi nhấn phím `Space` hoặc `Enter`. | Disabled & Keyboard test | - Toggle Disabled: Làm mờ, con trỏ `not-allowed`, click không đổi trạng thái.<br>- Toggle Enabled: Có thể bật/tắt bằng phím `Space` hoặc `Enter`, có thuộc tính `role="switch"` và `aria-checked` cập nhật đúng. | `Not Run` |
