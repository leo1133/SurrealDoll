# TEST CASE: 5. BADGE / TAG / CHIP

- **Mô tả chức năng:** Thẻ nhỏ thể hiện trạng thái (Mới, Đã duyệt, Hết hàng), phân loại hoặc bộ lọc
- **Tổng số Test Case:** **6** (`High: 4` | `Medium: 2` | `Low: 0`)
- **Phân bổ theo loại kiểm thử:** UI / Giao diện: **1**, Functional / Chức năng: **3**, Boundary / Giá trị biên: **2**

---

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_BDG_001`** [High] _UI / Giao diện_ — Kiểm tra giao diện và quy ước màu sắc ngữ nghĩa (Semantic Colors) của các Badge trạng thái
- [ ] **`TC_BDG_002`** [High] _Functional / Chức năng_ — Kiểm tra cập nhật động của Badge trạng thái ngay sau khi thay đổi trạng thái nghiệp vụ
- [ ] **`TC_BDG_003`** [High] _Functional / Chức năng_ — Kiểm tra chức năng xóa thẻ trên Removable Chip / Tag (Click icon `✕` trên Chip)
- [ ] **`TC_BDG_004`** [Medium] _Functional / Chức năng_ — Kiểm tra chức năng chọn/bỏ chọn trên Filterable / Selectable Chip
- [ ] **`TC_BDG_005`** [High] _Boundary / Giá trị biên_ — Kiểm tra giới hạn số đếm trên Notification Badge (`0`, `1-99` và `> 99` hiển thị `99+`)
- [ ] **`TC_BDG_006`** [Medium] _Boundary / Giá trị biên_ — Kiểm tra hiển thị khi tên Tag quá dài hoặc một bản ghi có số lượng lớn Tags (Overflow `+N`)

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_BDG_001` | UI / Giao diện | **High** | **Kiểm tra giao diện và quy ước màu sắc ngữ nghĩa (Semantic Colors) của các Badge trạng thái** | Màn hình danh sách hoặc chi tiết hiển thị các Badge trạng thái khác nhau. | 1. Quan sát màu nền, màu chữ, cỡ chữ, bo góc (`border-radius`) của các loại Badge trạng thái. | Trạng thái: Mới, Đã duyệt, Chờ xử lý, Từ chối/Hết hàng, Đã hủy | - Màu sắc tuân thủ đúng ngữ nghĩa chuẩn UX:<br>  + **Tích cực (Đã duyệt / Hoàn thành / Còn hàng)**: Xanh lá (`Green`).<br>  + **Trung gian / Cảnh báo (Chờ duyệt / Đang xử lý / Sắp hết)**: Vàng / Cam (`Warning`).<br>  + **Tiêu cực (Từ chối / Lỗi / Hết hàng)**: Đỏ (`Danger/Red`).<br>  + **Thông tin / Mặc định (Mới / Nháp)**: Xanh dương hoặc Xám.<br>- Chữ bên trong Badge căn chính giữa, không bị rớt dòng. | `Not Run` |
| `TC_BDG_002` | Functional / Chức năng | **High** | **Kiểm tra cập nhật động của Badge trạng thái ngay sau khi thay đổi trạng thái nghiệp vụ** | Bản ghi đơn hàng đang có Badge `Chờ duyệt` (Màu vàng). | 1. Thực hiện thao tác 'Phê duyệt' đơn hàng đó.<br>2. Quan sát sự thay đổi của thẻ Badge trên màn hình. | Đổi trạng thái: `Chờ duyệt` -> `Đã duyệt` | - Ngay sau khi thao tác thành công, cả nội dung chữ lẫn màu sắc của Badge tự động cập nhật sang `Đã duyệt` (Màu xanh lá) mà không cần tải lại trang thủ công. | `Not Run` |
| `TC_BDG_003` | Functional / Chức năng | **High** | **Kiểm tra chức năng xóa thẻ trên Removable Chip / Tag (Click icon `✕` trên Chip)** | Khu vực hiển thị danh sách các bộ lọc đang áp dụng hoặc danh sách từ khóa dạng Chip có dấu `✕`. | 1. Click vào biểu tượng `✕` trên một thẻ Chip (VD: `Thương hiệu: Apple ✕`). | Click `✕` trên Chip | - Thẻ Chip đó bị gỡ bỏ khỏi giao diện ngay lập tức.<br>- Dữ liệu danh sách bên dưới tự động cập nhật lại theo các điều kiện còn lại. | `Not Run` |
| `TC_BDG_004` | Functional / Chức năng | **Medium** | **Kiểm tra chức năng chọn/bỏ chọn trên Filterable / Selectable Chip** | Màn hình có dãy các Chip lọc nhanh (VD: `Tất cả`, `Mới nhất`, `Bán chạy`, `Giảm giá`). | 1. Click vào Chip `Bán chạy`.<br>2. Click chuyển sang Chip `Giảm giá` (hoặc click lại để bỏ chọn nếu là Multi-select Chip). | Click chọn Chip | - Chip được chọn chuyển sang trạng thái Active (đổi màu nền/viền hoặc hiện dấu tick `✓`) và kích hoạt lọc dữ liệu tương ứng. | `Not Run` |
| `TC_BDG_005` | Boundary / Giá trị biên | **High** | **Kiểm tra giới hạn số đếm trên Notification Badge (`0`, `1-99` và `> 99` hiển thị `99+`)** | Biểu tượng Chuông thông báo hoặc Giỏ hàng có gắn Badge số lượng màu đỏ ở góc trên. | 1. Kiểm tra khi số lượng thông báo chưa đọc = `0`.<br>2. Kiểm tra khi số lượng = `5` và `99`.<br>3. Kiểm tra khi số lượng vượt quá 99 (VD: `120` thông báo). | - Số lượng = `0`<br>- Số lượng = `99`<br>- Số lượng = `120` | - Khi `= 0`: Ẩn chấm số Badge đi để giao diện gọn gàng.<br>- Khi `1 -> 99`: Hiển thị chính xác con số thực tế.<br>- Khi `> 99`: Rút gọn hiển thị thành **`99+`**, khung Badge dạng viên thuốc nhỏ gọn không che lấp icon chính. | `Not Run` |
| `TC_BDG_006` | Boundary / Giá trị biên | **Medium** | **Kiểm tra hiển thị khi tên Tag quá dài hoặc một bản ghi có số lượng lớn Tags (Overflow `+N`)** | Một bản ghi được gắn 10 Tags phân loại hoặc 1 Tag có tên dài 80 ký tự. | 1. Quan sát khu vực hiển thị Tags trong bảng hoặc thẻ Card. | 10 Tags / Tag dài 80 ký tự | - Tag có tên quá dài được giới hạn `max-width` và cắt chữ bằng `...` kèm Tooltip.<br>- Khi có quá nhiều Tags trong không gian hẹp: Chỉ hiển thị 2-3 Tags đầu tiên và gom phần còn lại thành thẻ **`+7`** (Hover vào `+7` sẽ hiện danh sách 7 Tags còn lại). | `Not Run` |
