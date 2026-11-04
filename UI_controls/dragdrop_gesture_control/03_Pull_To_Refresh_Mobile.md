# TEST CASES: 3. PULL-TO-REFRESH (MOBILE)

- **Mục đích:** Thao tác vuốt từ đỉnh màn hình xuống trên thiết bị di động để tải lại dữ liệu mới nhất
- **Tổng số Test Case:** **6** (`High`: 4 | `Medium`: 2 | `Low`: 0)

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_PTR_001`** (High): Kiểm tra giao diện biểu tượng vòng xoay và thông điệp theo 3 giai đoạn của Pull-to-Refresh
- [ ] **`TC_PTR_002`** (High): Kiểm tra kích hoạt gọi API lấy dữ liệu mới nhất và cập nhật danh sách khi thực hiện Pull-to-Refresh
- [ ] **`TC_PTR_003`** (High): Kiểm tra hủy làm mới khi chỉ kéo nhẹ chưa đạt ngưỡng (`< Threshold`) rồi thả tay hoặc kéo ngược lên
- [ ] **`TC_PTR_004`** (High): Kiểm tra chỉ kích hoạt Pull-to-Refresh khi ở đúng đỉnh trang (`scrollTop === 0`), không kích hoạt nhầm khi cuộn ngược lên
- [ ] **`TC_PTR_005`** (Medium): Kiểm tra chống gọi trùng lặp API khi kéo liên tiếp nhiều lần và xử lý đóng vòng xoay khi mất mạng
- [ ] **`TC_PTR_006`** (Medium): Kiểm tra không kích hoạt nhầm Pull-to-Refresh của trang nền khi đang vuốt trong Modal hoặc Bottom Sheet

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_PTR_001` | UI / Giao diện | **High** | **Kiểm tra giao diện biểu tượng vòng xoay và thông điệp theo 3 giai đoạn của Pull-to-Refresh** | Mở màn hình danh sách (Bảng tin, Đơn hàng, Thông báo) trên thiết bị Mobile khi đang ở đỉnh trang. | 1. Đặt ngón tay chạm và kéo từ từ màn hình xuống một đoạn ngắn (Giai đoạn 1: Đang kéo).<br>2. Tiếp tục kéo xuống vượt qua ngưỡng kích hoạt (Giai đoạn 2: Đủ ngưỡng thả).<br>3. Thả ngón tay ra (Giai đoạn 3: Đang tải dữ liệu). | 3 giai đoạn kéo Pull-to-Refresh | - **Giai đoạn 1**: Xuất hiện icon mũi tên hướng xuống cùng độ giãn đàn hồi (`Overscroll resistance`) và chữ `'Kéo xuống để làm mới'`.<br>- **Giai đoạn 2**: Mũi tên xoay ngược lên trên kèm chữ `'Thả tay để cập nhật'`.<br>- **Giai đoạn 3**: Chuyển thành vòng xoay Spinner `'Đang tải...'` mượt mà ở đầu danh sách. | `Not Run` |
| `TC_PTR_002` | Functional / Chức năng | **High** | **Kiểm tra kích hoạt gọi API lấy dữ liệu mới nhất và cập nhật danh sách khi thực hiện Pull-to-Refresh** | Trên Server vừa có thêm 2 bản ghi/đơn hàng mới. | 1. Tại đỉnh danh sách trên Mobile, vuốt kéo xuống qua ngưỡng kích hoạt (`>= 70px`) rồi thả tay.<br>2. Quan sát dữ liệu danh sách sau khi vòng xoay kết thúc. | Kéo vượt ngưỡng -> Thả tay | - Hệ thống gửi Request lấy dữ liệu trang 1 mới nhất từ Server.<br>- Ngay khi nhận dữ liệu, vòng xoay tự động thu gọn ẩn đi và 2 bản ghi mới nhất được hiển thị ở đầu danh sách. | `Not Run` |
| `TC_PTR_003` | Boundary / Giá trị biên | **High** | **Kiểm tra hủy làm mới khi chỉ kéo nhẹ chưa đạt ngưỡng (`< Threshold`) rồi thả tay hoặc kéo ngược lên** | Đang ở đỉnh danh sách trên Mobile. | 1. Chạm kéo màn hình xuống một đoạn ngắn (`~30px` chưa tới vạch kích hoạt) rồi thả tay ra.<br>2. Kéo màn hình xuống sâu (`100px`), nhưng chưa thả tay mà đẩy ngược ngón tay trở lên đỉnh màn hình rồi mới thả. | Kéo ngắn `< 30px` & Kéo xuống rồi đẩy ngược lên | - Ở cả 2 trường hợp: Khung danh sách tự động trượt đàn hồi thu về vị trí ban đầu và **tuyệt đối không gọi API làm mới dữ liệu**. | `Not Run` |
| `TC_PTR_004` | Validation & Negative | **High** | **Kiểm tra chỉ kích hoạt Pull-to-Refresh khi ở đúng đỉnh trang (`scrollTop === 0`), không kích hoạt nhầm khi cuộn ngược lên** | Người dùng đã cuộn danh sách xuống sâu ở dòng thứ 30. | 1. Từ dòng thứ 30, dùng ngón tay vuốt từ trên xuống dưới để cuộn ngược danh sách trở lên đầu trang. | Cuộn từ dòng 30 ngược lên đầu trang | - Thao tác vuốt chỉ thực hiện cuộn danh sách lên trên bình thường, **không** kích hoạt nhầm Pull-to-Refresh khi danh sách chưa chạm hẳn về đỉnh (`scrollTop === 0`). | `Not Run` |
| `TC_PTR_005` | Validation & Negative | **Medium** | **Kiểm tra chống gọi trùng lặp API khi kéo liên tiếp nhiều lần và xử lý đóng vòng xoay khi mất mạng** | Đang ở màn hình danh sách trên Mobile. | 1. Kéo Pull-to-Refresh lần 1 -> Trong lúc vòng xoay đang tải, tiếp tục kéo xuống thêm 3 lần nữa.<br>2. Tắt mạng Wifi/4G rồi thực hiện kéo Pull-to-Refresh. | Kéo lặp lại khi đang Loading & Kéo khi Offline | - Bước 1: Trong khi đang tải, khóa không phát sinh thêm Request trùng lặp.<br>- Bước 2: Khi mất mạng hoặc API lỗi, vòng xoay Pull-to-Refresh phải **tự động thu gọn đóng lại**, hiện Toast báo `'Không có kết nối mạng'` và **giữ nguyên danh sách dữ liệu cũ đang có trên màn hình** (không xóa trắng danh sách). | `Not Run` |
| `TC_PTR_006` | Validation & Negative | **Medium** | **Kiểm tra không kích hoạt nhầm Pull-to-Refresh của trang nền khi đang vuốt trong Modal hoặc Bottom Sheet** | Trên màn hình Mobile đang mở một hộp thoại Modal hoặc khung Bottom Sheet. | 1. Dùng ngón tay vuốt từ trên xuống dưới bên trong vùng Modal / Bottom Sheet. | Vuốt xuống khi đang mở Modal / Bottom Sheet | - Không kích hoạt Pull-to-Refresh của trang nền phía dưới và không làm tải lại trang trình duyệt ngoài ý muốn (`overscroll-behavior-y: contain`). | `Not Run` |
