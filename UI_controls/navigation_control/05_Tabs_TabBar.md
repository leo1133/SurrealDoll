# TEST CASE: 5. TABS (TAB BAR)

- **Mô tả chức năng:** Thanh tab chuyển đổi qua lại giữa các nội dung cùng cấp mà không cần tải lại trang
- **Tổng số Test Case:** **7** (`High: 3` | `Medium: 4` | `Low: 0`)
- **Phân bổ theo loại kiểm thử:** UI / Giao diện: **2**, Functional / Chức năng: **3**, Boundary / Giá trị biên: **1**, Usability & Accessibility: **1**

---

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_TAB_001`** [High] _UI / Giao diện_ — Kiểm tra giao diện hiển thị mặc định của thanh Tab Bar
- [ ] **`TC_TAB_002`** [High] _Functional / Chức năng_ — Kiểm tra chuyển đổi qua lại giữa các Tab không cần tải lại toàn bộ trang
- [ ] **`TC_TAB_003`** [High] _Functional / Chức năng_ — Kiểm tra đồng bộ dữ liệu và chống xung đột (Race Condition) khi click chuyển Tab liên tục
- [ ] **`TC_TAB_004`** [Medium] _Functional / Chức năng_ — Kiểm tra giữ trạng thái Tab đang mở khi tải lại trang (F5) hoặc chia sẻ URL
- [ ] **`TC_TAB_005`** [Medium] _Boundary / Giá trị biên_ — Kiểm tra hiển thị khi có nhiều Tab hoặc tên Tab dài trên màn hình Mobile
- [ ] **`TC_TAB_006`** [Medium] _UI / Giao diện_ — Kiểm tra Tab ở trạng thái Disabled và bộ đếm số lượng (Badge Counter) trên tiêu đề Tab
- [ ] **`TC_TAB_007`** [Medium] _Usability & Accessibility_ — Kiểm tra điều hướng giữa các Tab bằng bàn phím (Tab + Phím mũi tên Left / Right)

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_TAB_001` | UI / Giao diện | **High** | **Kiểm tra giao diện hiển thị mặc định của thanh Tab Bar** | Màn hình có chia nội dung thành các Tab (VD: Thông tin chung \| Lịch sử giao dịch \| Cài đặt). | 1. Quan sát các tiêu đề Tab trên thanh Tab Bar.<br>2. Kiểm tra Tab được chọn mặc định (Default Active Tab) và hiệu ứng khi Hover vào các Tab chưa chọn. | N/A | - Các tiêu đề Tab hiển thị rõ ràng, thẳng hàng, có thanh gạch chân hoặc màu nền nổi bật tại Tab đang Active.<br>- Mặc định mở đúng Tab đầu tiên (hoặc Tab quy định trong tài liệu) và tải sẵn nội dung của Tab đó. | `Not Run` |
| `TC_TAB_002` | Functional / Chức năng | **High** | **Kiểm tra chuyển đổi qua lại giữa các Tab không cần tải lại toàn bộ trang** | Màn hình có 3 Tab: Tab 1, Tab 2, Tab 3. | 1. Click vào tiêu đề 'Tab 2'.<br>2. Click vào tiêu đề 'Tab 3'.<br>3. Click quay lại 'Tab 1'. | Tab 1 -> Tab 2 -> Tab 3 -> Tab 1 | - Khi click vào Tab nào, chỉ có vùng nội dung bên dưới (Tab Panel) chuyển đổi sang nội dung của Tab đó mà không làm reload toàn bộ trang web.<br>- Tại mọi thời điểm chỉ có duy nhất 1 Tab ở trạng thái Active. | `Not Run` |
| `TC_TAB_003` | Functional / Chức năng | **High** | **Kiểm tra đồng bộ dữ liệu và chống xung đột (Race Condition) khi click chuyển Tab liên tục** | Mỗi Tab gọi API riêng để lấy danh sách dữ liệu (VD: Đơn hàng Mới / Đang giao / Đã hủy). | 1. Click nhanh liên tiếp từ Tab 'Mới' (mạng chậm) -> sang Tab 'Đã hủy' (phản hồi nhanh). | Click chuyển Tab nhanh khi API chưa trả về xong | - Nội dung hiển thị cuối cùng phải khớp 100% với Tab đang được chọn ('Đã hủy').<br>- Kết quả trả về muộn của Tab 'Mới' không được ghi đè làm hiển thị nhầm dữ liệu đơn 'Mới' bên trong Tab 'Đã hủy'. | `Not Run` |
| `TC_TAB_004` | Functional / Chức năng | **Medium** | **Kiểm tra giữ trạng thái Tab đang mở khi tải lại trang (F5) hoặc chia sẻ URL** | Thanh Tab đồng bộ với URL (VD: `?tab=history` hoặc `#history`). | 1. Click chuyển sang Tab 2 ('Lịch sử giao dịch').<br>2. Nhấn F5 tải lại trang trình duyệt. | URL có `?tab=history` + F5 | - Sau khi nhấn F5 (theo thiết kế có lưu state lên URL), hệ thống vẫn mở đúng tại Tab 2 ('Lịch sử giao dịch') thay vì bị reset về Tab 1. | `Not Run` |
| `TC_TAB_005` | Boundary / Giá trị biên | **Medium** | **Kiểm tra hiển thị khi có nhiều Tab hoặc tên Tab dài trên màn hình Mobile** | Thanh Tab Bar có 8-10 Tabs được mở trên màn hình Mobile (375px). | 1. Quan sát thanh Tab Bar trên màn hình hẹp.<br>2. Vuốt ngang trên thanh Tab hoặc bấm nút mũi tên `<` `>`. | 8 Tabs trên màn hình rộng 375px | - Thanh Tab Bar cho phép vuốt cuộn ngang mượt mà (Horizontal scroll) và tự động cuộn đưa Tab vừa được click ra giữa màn hình, không làm rớt dòng vỡ khung. | `Not Run` |
| `TC_TAB_006` | UI / Giao diện | **Medium** | **Kiểm tra Tab ở trạng thái Disabled và bộ đếm số lượng (Badge Counter) trên tiêu đề Tab** | Thanh Tab có 1 Tab bị Disabled và các Tab có hiển thị số lượng như `Chờ duyệt (5)`. | 1. Thử click vào Tab đang ở trạng thái Disabled.<br>2. Thực hiện duyệt 1 bản ghi trong Tab `Chờ duyệt (5)` và quan sát con số trên tiêu đề Tab. | Tab Disabled & Badge `(5)` -> `(4)` | - Tab Disabled hiển thị mờ, con trỏ `not-allowed`, click không chuyển Tab.<br>- Sau khi duyệt 1 bản ghi, số lượng trên tiêu đề Tab cập nhật ngay thành `Chờ duyệt (4)`. | `Not Run` |
| `TC_TAB_007` | Usability & Accessibility | **Medium** | **Kiểm tra điều hướng giữa các Tab bằng bàn phím (Tab + Phím mũi tên Left / Right)** | Đang Focus tại tiêu đề Tab 1. | 1. Nhấn phím mũi tên `Right` / `Left` để di chuyển giữa các Tab.<br>2. Nhấn `Enter` hoặc `Space` để kích hoạt Tab. | Phím Left / Right Arrow | - Phím mũi tên cho phép chuyển đổi qua lại giữa các Tab đang Enabled theo đúng chuẩn WAI-ARIA (`role="tablist"`, `role="tab"`, `aria-selected`). | `Not Run` |
