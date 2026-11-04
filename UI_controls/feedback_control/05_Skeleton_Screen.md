# TEST CASES: 5. SKELETON SCREEN

- **Mục đích:** Khung xám giả lập bố cục màn hình trong lúc chờ dữ liệu tải về
- **Tổng số Test Case:** **6** (`High`: 3 | `Medium`: 2 | `Low`: 1)

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_SKL_001`** (High): Kiểm tra bố cục khung xương (Skeleton Layout) khớp đồng bộ với cấu trúc giao diện thực tế
- [ ] **`TC_SKL_002`** (Medium): Kiểm tra hiệu ứng ánh sáng chuyển động (Shimmer / Pulse Animation) và màu sắc trên Light / Dark Mode
- [ ] **`TC_SKL_003`** (High): Kiểm tra chuyển tiếp mượt mà từ Skeleton sang dữ liệu thật mà không gây giật nhảy bố cục (CLS = 0)
- [ ] **`TC_SKL_004`** (High): Kiểm tra thoát khỏi Skeleton Screen khi API trả về danh sách rỗng `[]` hoặc bị lỗi mạng/Server
- [ ] **`TC_SKL_005`** (Medium): Kiểm tra hiển thị Skeleton cục bộ (Component-level Skeleton) khi tải độc lập từng khối hoặc khi Lọc/Phân trang
- [ ] **`TC_SKL_006`** (Low): Kiểm tra vô hiệu hóa sự kiện click chuột trên các khối giả lập của Skeleton Screen

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_SKL_001` | UI / Giao diện | **High** | **Kiểm tra bố cục khung xương (Skeleton Layout) khớp đồng bộ với cấu trúc giao diện thực tế** | Màn hình danh sách sản phẩm (Card Grid), bảng dữ liệu (Table) hoặc trang chi tiết có áp dụng Skeleton Screen. | 1. Chỉnh tốc độ mạng trình duyệt về `Slow 3G` và tải lại trang.<br>2. Quan sát hình dáng, kích thước và số lượng các khối xám (Avatar tròn, khung ảnh chữ nhật, các thanh chữ dài/ngắn) trên Skeleton Screen.<br>3. So sánh với giao diện thật ngay khi dữ liệu tải xong. | Mạng Slow 3G -> So sánh Skeleton vs Giao diện thật | - Cấu trúc của Skeleton Screen mô phỏng đúng bố cục của giao diện thật (Avatar hình tròn nằm đúng vị trí Avatar thật, khung ảnh và số dòng tiêu đề tương ứng với Card thật). | `Not Run` |
| `TC_SKL_002` | UI / Giao diện | **Medium** | **Kiểm tra hiệu ứng ánh sáng chuyển động (Shimmer / Pulse Animation) và màu sắc trên Light / Dark Mode** | Trang đang ở trạng thái hiển thị Skeleton Screen. | 1. Quan sát hiệu ứng chuyển động trên các khối xám của Skeleton.<br>2. Chuyển đổi giao diện giữa Chế độ Sáng (Light Mode) và Chế độ Tối (Dark Mode). | Shimmer Animation & Light/Dark Mode | - Hiệu ứng ánh sáng lướt qua (`Shimmer`) hoặc nhấp nháy nhẹ (`Pulse`) chạy mượt mà, đồng bộ giữa các khối, báo hiệu cho người dùng biết trang đang hoạt động tải dữ liệu.<br>- Ở Dark Mode, màu nền khối Skeleton chuyển sang tông xám tối dịu mắt, không bị chói trắng. | `Not Run` |
| `TC_SKL_003` | Functional / Chức năng | **High** | **Kiểm tra chuyển tiếp mượt mà từ Skeleton sang dữ liệu thật mà không gây giật nhảy bố cục (CLS = 0)** | Trang đang tải dữ liệu và hiển thị Skeleton Screen. | 1. Quan sát khoảnh khắc API trả dữ liệu về và Skeleton được thay thế bằng nội dung thật. | Chuyển tiếp Skeleton -> Real Content | - Toàn bộ khung Skeleton biến mất hoàn toàn và nhường chỗ cho dữ liệu thật.<br>- Kích thước chiều cao của khối Skeleton tương đương với khối dữ liệu thật nên trang không bị giật nhảy hay đẩy tụt các phần tử bên dưới (`Cumulative Layout Shift - CLS` thấp). | `Not Run` |
| `TC_SKL_004` | Validation & Negative | **High** | **Kiểm tra thoát khỏi Skeleton Screen khi API trả về danh sách rỗng `[]` hoặc bị lỗi mạng/Server** | Trang đang hiển thị Skeleton Screen trong lúc chờ API. | 1. TH1: API trả về kết quả thành công nhưng có 0 bản ghi (`[]`).<br>2. TH2: API trả về lỗi `500` hoặc mất mạng. | API trả về `[]` hoặc lỗi `500` | - Bước 1: Skeleton Screen tắt ngay và chuyển sang hiển thị màn hình **Empty State** ('Chưa có dữ liệu').<br>- Bước 2: Skeleton Screen tắt ngay và hiển thị thông báo lỗi kèm nút `[Thử lại]`, tuyệt đối không bị treo kẹt ở khung xám Skeleton mãi mãi. | `Not Run` |
| `TC_SKL_005` | Functional / Chức năng | **Medium** | **Kiểm tra hiển thị Skeleton cục bộ (Component-level Skeleton) khi tải độc lập từng khối hoặc khi Lọc/Phân trang** | Trang Dashboard gồm nhiều khối dữ liệu (Biểu đồ, Bảng đơn hàng mới, Thống kê) lấy từ các API khác nhau. | 1. Mở trang Dashboard khi 1 API trả về nhanh (200ms) và 1 API trả về chậm (3s).<br>2. Trên bảng dữ liệu, bấm chuyển sang Trang 2. | Tải từng phần độc lập & Phân trang | - Khối nào tải xong trước sẽ hiển thị dữ liệu thật ngay, chỉ khối nào đang chờ API chậm mới hiển thị Skeleton cục bộ của riêng khối đó.<br>- Khi chuyển trang hoặc lọc: Chỉ phần nội dung bảng/danh sách hiển thị Skeleton, thanh Header và bộ lọc phía trên vẫn giữ nguyên. | `Not Run` |
| `TC_SKL_006` | Usability & Accessibility | **Low** | **Kiểm tra vô hiệu hóa sự kiện click chuột trên các khối giả lập của Skeleton Screen** | Màn hình đang hiển thị các khối Skeleton. | 1. Thử click chuột hoặc bôi đen văn bản vào các thanh xám trên Skeleton Screen. | Click chuột vào khối Skeleton | - Các khối Skeleton hoàn toàn không nhận sự kiện click (`pointer-events: none`, `user-select: none`), không gây lỗi JavaScript hay điều hướng sang đường dẫn rỗng `/undefined`. | `Not Run` |
