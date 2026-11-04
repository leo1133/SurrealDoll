# TEST CASE: 6. PRINT VIEW & BROWSER PDF EXPORT (IN BÁO CÁO & XUẤT BẢN IN TRỰC TIẾP)

- **Mục đích:** Nút In ấn (Print 🖨) mở giao diện bản in chuẩn hoặc lưu thành PDF qua hộp thoại Print của trình duyệt
- **Tổng số kịch bản:** **4 Test Cases** (`High: 2`, `Medium: 2`, `Low: 0`)

---

## I. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_PRT_001`** ([High] - *UI & Functional*): Kiểm tra nút [In / Print 🖨] kích hoạt hộp thoại in và ẩn toàn bộ thanh điều hướng thừa (@media print)
- [ ] **`TC_PRT_002`** ([High] - *UI / Giao diện*): Kiểm tra bố cục bảng dữ liệu, màu sắc chữ và không bị mất nội dung nằm trong vùng cuộn khi In
- [ ] **`TC_PRT_003`** ([Medium] - *Boundary / Giá trị biên*): Kiểm tra ngắt trang thông minh (Page Break) không làm đứt đôi ảnh mã QR/Barcode hoặc khung chữ ký khi qua trang 2
- [ ] **`TC_PRT_004`** ([Medium] - *Functional / Chức năng*): Kiểm tra đóng hộp thoại In không làm hỏng bố cục hay đơ sự kiện trên màn hình chính

---

## II. Bảng Chi Tiết Kịch Bản Kiểm Thử

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_PRT_001` | UI & Functional | **High** | **Kiểm tra nút [In / Print 🖨] kích hoạt hộp thoại in và ẩn toàn bộ thanh điều hướng thừa (@media print)** | Màn hình Hóa đơn, Phiếu thu/chi, Đơn hàng hoặc Báo cáo có nút `[In phiếu / Print 🖨]`. | 1. Click vào nút `[In phiếu 🖨]` (hoặc nhấn `Ctrl + P`).<br>2. Quan sát khung Xem trước bản in (Print Preview). | Click [In phiếu 🖨] -> Xem Print Preview | - Hộp thoại Print Preview bật lên ngay lập tức.<br>- Toàn bộ các thành phần giao diện không liên quan như: Thanh Header/Navbar, Menu Sidebar bên trái, các nút `[Lưu]/[Xóa]/[In]`, thanh phân trang và Bong bóng Chat ở góc dưới **đều được tự động ẩn đi hoàn toàn (`@media print { display: none }`)**.<br>- Bản in chỉ hiển thị sạch sẽ nội dung Hóa đơn/Báo cáo, Logo công ty và khu vực ký tên. | `Not Run` |
| `TC_PRT_002` | UI / Giao diện | **High** | **Kiểm tra bố cục bảng dữ liệu, màu sắc chữ và không bị mất nội dung nằm trong vùng cuộn khi In** | Màn hình báo cáo có bảng dữ liệu nằm trong khung cuộn hoặc đang bật giao diện Chế độ tối (Dark Mode). | 1. Chuyển giao diện web sang Dark Mode -> Bấm `[In báo cáo 🖨]`.<br>2. Kiểm tra phần bảng dữ liệu trong Print Preview. | In báo cáo khi đang ở Dark Mode & Bảng dài | - Bản in tự động chuyển về nền trắng - chữ đen sắc nét để tiết kiệm mực và dễ đọc (không in cả nền đen xì của Dark Mode).<br>- Khung cuộn (`overflow: scroll`) được mở bung toàn bộ chiều dài trong bản in để in đủ tất cả các dòng dữ liệu chứ không chỉ chụp mỗi phần đang nhìn thấy trên màn hình. | `Not Run` |
| `TC_PRT_003` | Boundary / Giá trị biên | **Medium** | **Kiểm tra ngắt trang thông minh (Page Break) không làm đứt đôi ảnh mã QR/Barcode hoặc khung chữ ký khi qua trang 2** | Phiếu in dài sang trang thứ 2, cuối phiếu có mã QR thanh toán và khung chữ ký Người lập phiếu / Khách hàng. | 1. Mở Print Preview và kiểm tra vị trí giáp ranh giữa Trang 1 và Trang 2. | Kiểm tra ranh giới ngắt trang 1 -> 2 | - Áp dụng thuộc tính `page-break-inside: avoid` nên hình ảnh mã QR/Barcode và khối chữ ký được đẩy trọn vẹn sang trang mới, không bị cắt làm đôi nửa ở trang 1 nửa ở trang 2. | `Not Run` |
| `TC_PRT_004` | Functional / Chức năng | **Medium** | **Kiểm tra đóng hộp thoại In không làm hỏng bố cục hay đơ sự kiện trên màn hình chính** | Đang mở hộp thoại Print Preview trên trình duyệt. | 1. Bấm nút `[Hủy / Cancel]` để đóng hộp thoại In.<br>2. Thao tác tiếp các nút bấm trên màn hình ứng dụng. | Bấm Cancel trong hộp thoại Print | - Màn hình ứng dụng giữ nguyên trạng thái và bố cục ban đầu, mọi nút bấm và sự kiện vẫn phản hồi bình thường. | `Not Run` |
