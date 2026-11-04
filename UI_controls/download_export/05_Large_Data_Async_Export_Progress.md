# TEST CASE: 5. LARGE DATA ASYNC EXPORT & PROGRESS (XUẤT DỮ LIỆU LỚN CHẠY NGẦM & LỊCH SỬ XUẤT)

- **Mục đích:** Xử lý xuất tập dữ liệu lớn (10,000 - 100,000+ dòng) qua tiến trình chạy ngầm (Background Job), thanh tiến trình và Trung tâm tải xuống
- **Tổng số kịch bản:** **6 Test Cases** (`High: 3`, `Medium: 2`, `Low: 1`)

---

## I. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_ASY_001`** ([High] - *Functional & Performance*): Kiểm tra xuất tập dữ liệu lớn (10,000 - 100,000 dòng) bằng tiến trình chạy ngầm không làm đơ trình duyệt hay Timeout
- [ ] **`TC_ASY_002`** ([High] - *Functional / Chức năng*): Kiểm tra nhận thông báo hoàn tất (Notification / Toast / Email) và tải file từ Trung tâm Lịch sử Xuất (Export Center)
- [ ] **`TC_ASY_003`** ([Medium] - *Functional / Chức năng*): Kiểm tra nút [Hủy / Cancel] khi tiến trình xuất dữ liệu lớn đang chạy dở
- [ ] **`TC_ASY_004`** ([High] - *Boundary / Giá trị biên*): Kiểm tra giới hạn số lượng bản ghi tối đa cho phép xuất trong 1 lần (Max Export Limit)
- [ ] **`TC_ASY_005`** ([Medium] - *Validation & Negative*): Kiểm tra trạng thái báo lỗi và nút [Thử lại / Retry] khi tiến trình xuất dữ liệu ngầm gặp sự cố trên Server
- [ ] **`TC_ASY_006`** ([Low] - *Validation & Negative*): Kiểm tra cảnh báo khi người dùng đóng tab trình duyệt trong lúc đang tải file trực tiếp phía Client

---

## II. Bảng Chi Tiết Kịch Bản Kiểm Thử

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_ASY_001` | Functional & Performance | **High** | **Kiểm tra xuất tập dữ liệu lớn (10,000 - 100,000 dòng) bằng tiến trình chạy ngầm không làm đơ trình duyệt hay Timeout** | Bảng dữ liệu có từ 20,000 đến 100,000 bản ghi cần xuất báo cáo. | 1. Chọn xuất toàn bộ 50,000 bản ghi ra Excel/CSV.<br>2. Trong lúc hệ thống đang xử lý xuất file, thử chuyển sang tab/màn hình khác để làm việc tiếp. | Export 50,000 dòng dữ liệu | - Không xảy ra lỗi `504 Gateway Timeout` hay treo đơ giao diện trình duyệt.<br>- Hệ thống hiển thị thanh tiến trình (`Đang xuất dữ liệu: 35%...`) hoặc thông báo `'Yêu cầu xuất file đang được xử lý ngầm. Bạn sẽ nhận được thông báo ngay khi file sẵn sàng'`.<br>- Người dùng vẫn có thể di chuyển và thao tác ở các màn hình khác bình thường trong lúc chờ. | `Not Run` |
| `TC_ASY_002` | Functional / Chức năng | **High** | **Kiểm tra nhận thông báo hoàn tất (Notification / Toast / Email) và tải file từ Trung tâm Lịch sử Xuất (Export Center)** | Tiến trình xuất 50,000 dòng ở `TC_ASY_001` đã xử lý xong trên Server. | 1. Quan sát thông báo bật lên (Toast hoặc chuông Notification).<br>2. Mở danh sách `'Lịch sử xuất file (Export History / Download Center)'`.<br>3. Click vào nút `[Tải xuống]` tại dòng yêu cầu vừa hoàn tất (`Trạng thái: Hoàn thành`). | Job hoàn tất -> Tải từ Export Center | - Khi Job chạy xong, hệ thống đẩy thông báo tức thì kèm nút `[Tải xuống ngay]`.<br>- Trong màn hình Lịch sử xuất file hiển thị rõ: Tên báo cáo, Người tạo, Thời gian tạo, Trạng thái (`Đang xử lý` -> `Hoàn thành`), Thời hạn lưu trữ và nút `[Tải xuống]` hoạt động chính xác. | `Not Run` |
| `TC_ASY_003` | Functional / Chức năng | **Medium** | **Kiểm tra nút [Hủy / Cancel] khi tiến trình xuất dữ liệu lớn đang chạy dở** | Đang trong quá trình xuất một báo cáo lớn (Thanh tiến trình đang ở mức 25%). | 1. Click vào nút `[Hủy xuất / Cancel]` trên thanh tiến trình.<br>2. Kiểm tra xem có file nào tự động tải về sau đó không. | Click [Hủy] khi đang Export ở 25% | - Tiến trình xuất bị dừng lại ngay lập tức, đóng thanh tiến trình và hủy tác vụ để giải phóng tài nguyên, không tự động tải file về nữa. | `Not Run` |
| `TC_ASY_004` | Boundary / Giá trị biên | **High** | **Kiểm tra giới hạn số lượng bản ghi tối đa cho phép xuất trong 1 lần (Max Export Limit)** | Hệ thống quy định chỉ cho phép xuất tối đa `50,000 dòng/lần` nhưng kết quả lọc hiện tại có `250,000 dòng`. | 1. Để bộ lọc rộng (250,000 dòng) và bấm nút `[Xuất tất cả]`.  | 250,000 dòng vượt ngưỡng tối đa 50,000 dòng | - Hệ thống hiển thị thông báo rõ ràng: `'Số lượng bản ghi (250,000) vượt quá giới hạn cho phép xuất một lần (tối đa 50,000 dòng). Vui lòng thu hẹp bộ lọc khoảng thời gian trước khi xuất'`. | `Not Run` |
| `TC_ASY_005` | Validation & Negative | **Medium** | **Kiểm tra trạng thái báo lỗi và nút [Thử lại / Retry] khi tiến trình xuất dữ liệu ngầm gặp sự cố trên Server** | Giả lập tiến trình tạo file báo cáo ngầm bị lỗi giữa chừng. | 1. Quan sát trạng thái bản ghi trong Trung tâm lịch sử xuất file. | Background Export Job bị lỗi Failed | - Trạng thái chuyển sang `'Thất bại (Failed)'` (không bị treo mãi ở `'Đang xử lý 99%'` vô thời hạn) và cung cấp nút `[Thử lại]` cho người dùng. | `Not Run` |
| `TC_ASY_006` | Validation & Negative | **Low** | **Kiểm tra cảnh báo khi người dùng đóng tab trình duyệt trong lúc đang tải file trực tiếp phía Client** | Quá trình tạo/tải file lớn phía Client-side đang diễn ra. | 1. Bấm đóng tab trình duyệt (`Ctrl + W`) khi tiến trình tải đang ở 50%. | Đóng tab khi đang Export Client-side | - Hiển thị hộp thoại cảnh báo xác nhận rời trang hoặc duy trì tiến trình tải của trình duyệt không bị ngắt đột ngột. | `Not Run` |
