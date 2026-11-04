# TEST CASE: 3. LIST VIEW / CARD

- **Mô tả chức năng:** Hiển thị danh sách các mục dưới dạng thẻ (Card Grid) hoặc danh sách hàng dọc (List View)
- **Tổng số Test Case:** **6** (`High: 4` | `Medium: 2` | `Low: 0`)
- **Phân bổ theo loại kiểm thử:** UI / Giao diện: **2**, Boundary / Giá trị biên: **1**, Functional / Chức năng: **2**, Validation & Negative: **1**

---

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_CRD_001`** [High] _UI / Giao diện_ — Kiểm tra bố cục giao diện và sự đồng đều chiều cao giữa các thẻ Card trên cùng một hàng
- [ ] **`TC_CRD_002`** [High] _Boundary / Giá trị biên_ — Kiểm tra giới hạn số dòng hiển thị (Line Clamp) của Tiêu đề và Mô tả trong Card
- [ ] **`TC_CRD_003`** [High] _UI / Giao diện_ — Kiểm tra khả năng đáp ứng (Responsive Grid) và chuyển đổi chế độ xem Grid View <-> List View
- [ ] **`TC_CRD_004`** [High] _Functional / Chức năng_ — Kiểm tra sự kiện Click vào thẻ Card (Xem chi tiết) độc lập với các nút hành động con bên trong Card
- [ ] **`TC_CRD_005`** [Medium] _Functional / Chức năng_ — Kiểm tra tải thêm dữ liệu danh sách Card bằng Infinite Scroll hoặc nút 'Xem thêm' (Load More)
- [ ] **`TC_CRD_006`** [Medium] _Validation & Negative_ — Kiểm tra hiển thị Card khi bản ghi khuyết thiếu dữ liệu tùy chọn (Optional fields)

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_CRD_001` | UI / Giao diện | **High** | **Kiểm tra bố cục giao diện và sự đồng đều chiều cao giữa các thẻ Card trên cùng một hàng** | Màn hình hiển thị danh sách dạng lưới thẻ (Card Grid, VD: Danh sách sản phẩm / Khóa học / Bài viết). | 1. Quan sát các thành phần bên trong mỗi Card (Ảnh, Tiêu đề, Mô tả, Giá, Nút bấm).<br>2. So sánh chiều cao và vị trí nút bấm của các Card nằm trên cùng 1 hàng khi có Card tiêu đề ngắn (1 dòng) và Card tiêu đề dài (3 dòng). | Hàng có 3-4 Cards với độ dài chữ khác nhau | - Tất cả các Card trên cùng một hàng phải có **chiều cao bằng nhau** (`equal height`).<br>- Phần chân Card (Giá tiền / Nút 'Mua ngay') luôn được đẩy xuống đáy Card thẳng hàng ngang với nhau, tạo bố cục gọn gàng chuyên nghiệp. | `Not Run` |
| `TC_CRD_002` | Boundary / Giá trị biên | **High** | **Kiểm tra giới hạn số dòng hiển thị (Line Clamp) của Tiêu đề và Mô tả trong Card** | Có bản ghi tiêu đề dài 200 ký tự và mô tả dài 500 ký tự. | 1. Quan sát cách hiển thị Tiêu đề và Mô tả trên thẻ Card. | Tiêu đề 200 ký tự, Mô tả 500 ký tự | - Tiêu đề tự động giới hạn tối đa 2 dòng (`-webkit-line-clamp: 2`) và Mô tả tối đa 2-3 dòng kèm dấu `...` ở cuối, không làm thẻ Card bị kéo dài bất thường. | `Not Run` |
| `TC_CRD_003` | UI / Giao diện | **High** | **Kiểm tra khả năng đáp ứng (Responsive Grid) và chuyển đổi chế độ xem Grid View <-> List View** | Màn hình danh sách hỗ trợ xem trên nhiều kích thước màn hình và có nút đổi chế độ xem Grid / List. | 1. Thay đổi kích thước màn hình từ Desktop (1920px) -> Laptop (1366px) -> Tablet (768px) -> Mobile (375px).<br>2. Click nút chuyển từ chế độ Lưới (**Grid View**) sang chế độ Danh sách ngang (**List View**) và ngược lại. | Responsive Breakpoints & Toggle Grid/List | - Số lượng Card trên mỗi hàng tự động co giãn hợp lý (VD: 4 -> 3 -> 2 -> 1 cột), khoảng cách `gap` giữa các Card đều nhau.<br>- Khi chuyển sang List View: Bố cục chuyển sang dạng hàng ngang trải dài mà không làm mất dữ liệu hay điều kiện lọc hiện tại. | `Not Run` |
| `TC_CRD_004` | Functional / Chức năng | **High** | **Kiểm tra sự kiện Click vào thẻ Card (Xem chi tiết) độc lập với các nút hành động con bên trong Card** | Thẻ Card cho phép click vào để mở trang chi tiết, đồng thời trên Card có nút 'Yêu thích ❤️' và nút 'Thêm vào giỏ 🛒'. | 1. Click vào ảnh hoặc tiêu đề của Card.<br>2. Quay lại danh sách, click trực tiếp vào nút 'Yêu thích ❤️' hoặc nút menu `⋮` nằm ở góc trên của Card. | Click Card vs Click nút con trong Card | - Bước 1: Điều hướng mở đúng trang chi tiết của mục đó.<br>- Bước 2: Khi click vào nút 'Yêu thích ❤️' hoặc menu `⋮`, chỉ thực thi hành động Yêu thích/mở menu, **không** bị lan truyền sự kiện (`Event Bubbling`) làm chuyển sang trang chi tiết. | `Not Run` |
| `TC_CRD_005` | Functional / Chức năng | **Medium** | **Kiểm tra tải thêm dữ liệu danh sách Card bằng Infinite Scroll hoặc nút 'Xem thêm' (Load More)** | Danh sách có tổng cộng 50 Cards, mỗi lần tải 12 Cards. | 1. Cuộn xuống cuối danh sách (hoặc bấm nút 'Xem thêm').<br>2. Tiếp tục cuộn/bấm cho đến khi tải hết 50 Cards. | 50 Cards (12 Cards / lần tải) | - Hiển thị hiệu ứng Loading ở cuối danh sách và nối tiếp 12 Cards mới vào ngay bên dưới mà không làm nhảy vị trí thanh cuộn.<br>- Khi đã tải đủ toàn bộ 50 Cards: Ẩn nút 'Xem thêm' và không gọi thêm API khi cuộn tiếp. | `Not Run` |
| `TC_CRD_006` | Validation & Negative | **Medium** | **Kiểm tra hiển thị Card khi bản ghi khuyết thiếu dữ liệu tùy chọn (Optional fields)** | Một bản ghi không có ảnh, không có nhãn giảm giá và không có mô tả ngắn. | 1. Quan sát thẻ Card của bản ghi khuyết thông tin so với các Card đầy đủ bên cạnh. | Bản ghi thiếu ảnh & thiếu mô tả | - Hiển thị ảnh Placeholder mặc định.<br>- Bố cục Card vẫn giữ nguyên khung chuẩn, không bị xô lệch hay sập chiều cao. | `Not Run` |
