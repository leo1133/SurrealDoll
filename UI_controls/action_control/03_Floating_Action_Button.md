# TEST CASE: 3. FLOATING ACTION BUTTON (FAB)

- **Mô tả chức năng:** Nút hành động nổi cố định ở góc màn hình (thường dùng trên Mobile / Web App)
- **Tổng số Test Case:** **7** (`High: 5` | `Medium: 2` | `Low: 0`)
- **Phân bổ theo loại kiểm thử:** UI / Giao diện: **3**, Functional / Chức năng: **2**, Usability & Accessibility: **1**, Boundary / Giá trị biên: **1**

---

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_FAB_001`** [High] _UI / Giao diện_ — Kiểm tra giao diện hiển thị, kích thước vùng chạm và hiệu ứng nổi của nút FAB
- [ ] **`TC_FAB_002`** [High] _UI / Giao diện_ — Kiểm tra vị trí cố định (Fixed Position) và hành vi của nút FAB khi cuộn trang (Scroll)
- [ ] **`TC_FAB_003`** [High] _UI / Giao diện_ — Kiểm tra xung đột che khuất nội dung cuối trang (Overlap) và thứ tự lớp (Z-index) với Modal
- [ ] **`TC_FAB_004`** [High] _Functional / Chức năng_ — Kiểm tra kích hoạt hành động khi chạm vào nút FAB (Single Action & Speed Dial Menu)
- [ ] **`TC_FAB_005`** [Medium] _Functional / Chức năng_ — Kiểm tra đóng menu con của Speed Dial FAB khi chạm ra ngoài hoặc nhấn lại nút đóng
- [ ] **`TC_FAB_006`** [High] _Usability & Accessibility_ — Kiểm tra hiển thị nút FAB khi bật bàn phím ảo (Virtual Keyboard) và khi xoay màn hình (Orientation)
- [ ] **`TC_FAB_007`** [Medium] _Boundary / Giá trị biên_ — Kiểm tra chạm liên tiếp nhiều lần thật nhanh (Rapid Tap) vào nút FAB

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_FAB_001` | UI / Giao diện | **High** | **Kiểm tra giao diện hiển thị, kích thước vùng chạm và hiệu ứng nổi của nút FAB** | Mở ứng dụng trên thiết bị Mobile hoặc trình duyệt chế độ Responsive Mobile. | 1. Quan sát nút FAB ở góc màn hình (thường là góc dưới bên phải).<br>2. Kiểm tra hình dáng (tròn hoặc viên thuốc Extended FAB), icon trung tâm và bóng đổ (`box-shadow` / `elevation`). | Màn hình Mobile (375x812) | - Nút FAB hiển thị nổi bật trên lớp giao diện chính, có bóng đổ tạo chiều sâu.<br>- Kích thước nút đạt chuẩn Touch Target tối thiểu `48x48px` (chuẩn Material Design là `56x56px`), icon căn chính giữa nút. | `Not Run` |
| `TC_FAB_002` | UI / Giao diện | **High** | **Kiểm tra vị trí cố định (Fixed Position) và hành vi của nút FAB khi cuộn trang (Scroll)** | Màn hình có danh sách nội dung dài có thể cuộn lên/xuống. | 1. Vuốt cuộn trang xuống cuối danh sách (Scroll Down).<br>2. Vuốt cuộn trang ngược lên đầu danh sách (Scroll Up). | Cuộn trang lên / xuống | - Nút FAB giữ vị trí cố định (`position: fixed`) ở góc màn hình, không bị trôi theo nội dung.<br>- Nếu thiết kế là Extended FAB (có cả Icon + Chữ) hoặc Auto-hide: Khi cuộn xuống nút thu gọn chỉ còn Icon (hoặc ẩn mượt mà), khi cuộn lên nút mở rộng/hiện trở lại. | `Not Run` |
| `TC_FAB_003` | UI / Giao diện | **High** | **Kiểm tra xung đột che khuất nội dung cuối trang (Overlap) và thứ tự lớp (Z-index) với Modal** | Danh sách có nhiều dòng dữ liệu, phân trang hoặc nút hành động ở đáy màn hình. | 1. Cuộn xuống kịch đáy trang và quan sát dòng dữ liệu cuối cùng.<br>2. Mở một Popup Modal / Bottom Sheet hoặc Drawer Menu. | Cuộn kịch đáy & Mở Modal | - Dòng cuối cùng của danh sách có khoảng đệm (`padding-bottom`) đủ rộng để nút FAB không che mất nút Sửa/Xóa hoặc phân trang của dòng cuối.<br>- Khi mở Modal / Bottom Sheet / Menu: Lớp phủ (Backdrop) và Modal phải nằm **trên** nút FAB (hoặc nút FAB tự ẩn đi), không để nút FAB đè lên trên Modal. | `Not Run` |
| `TC_FAB_004` | Functional / Chức năng | **High** | **Kiểm tra kích hoạt hành động khi chạm vào nút FAB (Single Action & Speed Dial Menu)** | Nút FAB đang hiển thị trên màn hình. | 1. Chạm (Tap/Click) vào nút FAB.<br>2. Nếu là FAB đơn: Kiểm tra màn hình chức năng mở ra.<br>3. Nếu là FAB mở rộng (Speed Dial): Quan sát các nút hành động phụ bung ra và chạm chọn 1 nút phụ. | Tap vào nút FAB | - TH1 (Single Action): Mở ngay màn hình Tạo mới / Soạn thảo (hoặc cuộn mượt lên đầu trang nếu là nút Back-to-top).<br>- TH2 (Speed Dial): Hiển thị lớp nền mờ (Backdrop) và bung ra danh sách các nút con kèm nhãn chú thích; icon nút chính xoay thành dấu đóng (`✕`). Chạm nút con kích hoạt đúng chức năng đó. | `Not Run` |
| `TC_FAB_005` | Functional / Chức năng | **Medium** | **Kiểm tra đóng menu con của Speed Dial FAB khi chạm ra ngoài hoặc nhấn lại nút đóng** | Menu Speed Dial của nút FAB đang được mở. | 1. Chạm vào vùng nền mờ (Backdrop) bên ngoài các nút FAB.<br>2. Mở lại Speed Dial rồi chạm vào chính nút FAB (`✕`). | Tap outside / Tap nút `✕` | - Cả hai trường hợp đều thu gọn các nút con lại, tắt lớp nền mờ và trả icon nút FAB về biểu tượng ban đầu (`+`). | `Not Run` |
| `TC_FAB_006` | Usability & Accessibility | **High** | **Kiểm tra hiển thị nút FAB khi bật bàn phím ảo (Virtual Keyboard) và khi xoay màn hình (Orientation)** | Truy cập trên thiết bị Mobile thực tế (iOS / Android). | 1. Chạm vào một ô tìm kiếm/nhập liệu trên màn hình để bàn phím ảo bật lên.<br>2. Xoay ngang màn hình điện thoại (Landscape) rồi xoay dọc lại (Portrait). | Virtual Keyboard ON & Rotate Screen | - Khi bàn phím ảo bật lên: Nút FAB tự động ẩn đi hoặc giữ cố định bên dưới, tuyệt đối không bị đẩy trồi lên che mất ô nhập liệu của người dùng.<br>- Đảm bảo khoảng cách an toàn với thanh điều hướng đáy màn hình (`safe-area-inset-bottom` trên iPhone/Android). | `Not Run` |
| `TC_FAB_007` | Boundary / Giá trị biên | **Medium** | **Kiểm tra chạm liên tiếp nhiều lần thật nhanh (Rapid Tap) vào nút FAB** | Nút FAB dùng để mở Popup tạo mới hoặc chuyển màn hình. | 1. Dùng ngón tay chạm liên tiếp 3-5 lần thật nhanh vào nút FAB. | Rapid tap 5 lần | - Hệ thống chỉ mở duy nhất 1 Popup / 1 màn hình tạo mới, không bị mở chồng 5 lớp Modal lên nhau. | `Not Run` |
