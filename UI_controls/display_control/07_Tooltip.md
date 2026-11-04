# TEST CASE: 7. TOOLTIP

- **Mô tả chức năng:** Hộp chú thích nhỏ hiển thị khi di chuột (Hover) hoặc Focus vào một icon, văn bản rút gọn hoặc nút bấm
- **Tổng số Test Case:** **6** (`High: 3` | `Medium: 3` | `Low: 0`)
- **Phân bổ theo loại kiểm thử:** UI / Giao diện: **1**, Functional / Chức năng: **1**, Boundary / Giá trị biên: **2**, Usability & Accessibility: **1**, Security / Bảo mật: **1**

---

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_TTP_001`** [High] _UI / Giao diện_ — Kiểm tra giao diện hiển thị mặc định, độ tương phản và thứ tự lớp (Z-index) của Tooltip
- [ ] **`TC_TTP_002`** [High] _Functional / Chức năng_ — Kiểm tra kích hoạt hiện Tooltip khi Hover vào và tự động ẩn ngay khi di chuột ra ngoài
- [ ] **`TC_TTP_003`** [High] _Boundary / Giá trị biên_ — Kiểm tra tự động đổi hướng hiển thị (Auto-flip / Viewport Collision) khi phần tử nằm sát mép màn hình
- [ ] **`TC_TTP_004`** [Medium] _Boundary / Giá trị biên_ — Kiểm tra hiển thị khi nội dung văn bản trong Tooltip dài nhiều dòng
- [ ] **`TC_TTP_005`** [Medium] _Usability & Accessibility_ — Kiểm tra kích hoạt Tooltip bằng bàn phím (Focus) và trên màn hình cảm ứng (Mobile Touch)
- [ ] **`TC_TTP_006`** [Medium] _Security / Bảo mật_ — Kiểm tra bảo mật chống XSS khi nội dung Tooltip lấy động từ dữ liệu người dùng nhập

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_TTP_001` | UI / Giao diện | **High** | **Kiểm tra giao diện hiển thị mặc định, độ tương phản và thứ tự lớp (Z-index) của Tooltip** | Màn hình có các biểu tượng thông tin (`ℹ️`), nút chức năng hoặc văn bản rút gọn có gắn Tooltip. | 1. Di chuột (Hover) vào biểu tượng `ℹ️` để kích hoạt Tooltip.<br>2. Quan sát màu nền, màu chữ, cỡ chữ, bo góc, mũi tên trỏ (`Caret/Arrow`) và lớp hiển thị (`z-index`). | Hover vào icon `ℹ️` | - Tooltip hiển thị sắc nét, màu chữ và nền tương phản rõ ràng với phần nền bên dưới.<br>- Mũi tên nhỏ của Tooltip trỏ đúng vào chính giữa phần tử kích hoạt.<br>- Tooltip có `z-index` cao, nổi hoàn toàn lên trên các dòng bảng, thanh Header hoặc khung Card mà không bị cắt khuất (`overflow: hidden` của thẻ cha không được cắt mất Tooltip). | `Not Run` |
| `TC_TTP_002` | Functional / Chức năng | **High** | **Kiểm tra kích hoạt hiện Tooltip khi Hover vào và tự động ẩn ngay khi di chuột ra ngoài** | Trên màn hình có nhiều phần tử gắn Tooltip cạnh nhau. | 1. Di chuột vào phần tử A -> Quan sát Tooltip A.<br>2. Di chuột sang phần tử B bên cạnh -> Quan sát Tooltip A và B.<br>3. Di chuột ra vùng trống hoặc cuộn trang (Scroll). | Hover A -> Hover B -> Mouse Leave / Scroll | - Khi di chuột sang B: Tooltip của A phải biến mất ngay lập tức và chỉ hiển thị Tooltip của B (không bị hiện chồng 2 Tooltips cùng lúc).<br>- Khi di chuột ra ngoài hoặc cuộn trang: Tooltip tự động ẩn hoàn toàn, không bị lỗi 'kẹt' (Stuck tooltip) lơ lửng trên màn hình. | `Not Run` |
| `TC_TTP_003` | Boundary / Giá trị biên | **High** | **Kiểm tra tự động đổi hướng hiển thị (Auto-flip / Viewport Collision) khi phần tử nằm sát mép màn hình** | Các nút có Tooltip nằm ở sát mép phải, mép trái, mép trên cùng và mép dưới cùng của cửa sổ trình duyệt. | 1. Di chuột vào phần tử nằm sát mép ngoài cùng bên phải màn hình.<br>2. Cuộn trang để phần tử nằm sát mép trên cùng màn hình rồi di chuột vào. | Phần tử nằm sát 4 cạnh màn hình | - Tooltip tự động tính toán không gian trống và đảo chiều hiển thị (VD: từ `top` lật xuống `bottom`, từ `right` lật sang `left`) để toàn bộ hộp chú thích luôn nằm gọn 100% trong khung nhìn màn hình, không bị tràn khuất chữ. | `Not Run` |
| `TC_TTP_004` | Boundary / Giá trị biên | **Medium** | **Kiểm tra hiển thị khi nội dung văn bản trong Tooltip dài nhiều dòng** | Tooltip chứa đoạn giải thích công thức tính toán hoặc tên đầy đủ dài 200 ký tự. | 1. Di chuột vào phần tử để mở Tooltip có nội dung dài. | Nội dung Tooltip dài 200 ký tự | - Hộp Tooltip có giới hạn chiều rộng tối đa hợp lý (`max-width: 250px - 320px`) và tự động ngắt chữ xuống nhiều dòng dễ đọc, không bị kéo dài thành 1 dải ngang suốt chiều rộng màn hình. | `Not Run` |
| `TC_TTP_005` | Usability & Accessibility | **Medium** | **Kiểm tra kích hoạt Tooltip bằng bàn phím (Focus) và trên màn hình cảm ứng (Mobile Touch)** | Truy cập bằng bàn phím trên Desktop và chạm cảm ứng trên Mobile. | 1. Trên Desktop: Nhấn phím `Tab` di chuyển Focus vào icon/nút có Tooltip, sau đó nhấn `Esc`.<br>2. Trên Mobile: Chạm vào icon thông tin `ℹ️` rồi chạm ra vùng trống bên ngoài. | Keyboard Focus & Mobile Tap | - Trên Desktop: Khi phần tử nhận Focus bằng phím `Tab`, Tooltip tự động hiển thị; nhấn `Esc` hoặc `Tab` sang mục khác sẽ ẩn Tooltip.<br>- Trên Mobile: Chạm vào icon `ℹ️` mở chú thích và chạm ra ngoài sẽ đóng lại gọn gàng. | `Not Run` |
| `TC_TTP_006` | Security / Bảo mật | **Medium** | **Kiểm tra bảo mật chống XSS khi nội dung Tooltip lấy động từ dữ liệu người dùng nhập** | Một bản ghi có tên dài chứa đoạn mã `<img src=x onerror=alert(1)>` bị cắt ngắn trên bảng và hiển thị đầy đủ qua Tooltip khi Hover. | 1. Di chuột vào tên bản ghi đó để bật Tooltip. | Nội dung động chứa `<img src=x onerror=alert(1)>` | - Nội dung bên trong Tooltip được escape an toàn dưới dạng văn bản thuần, tuyệt đối không thực thi mã JavaScript. | `Not Run` |
