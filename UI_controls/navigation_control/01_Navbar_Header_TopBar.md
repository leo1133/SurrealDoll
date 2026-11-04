# TEST CASE: 1. NAVBAR / HEADER / TOP BAR

- **Mô tả chức năng:** Thanh điều hướng trên cùng của website (Logo, Menu chính, Thông báo, User Profile...)
- **Tổng số Test Case:** **8** (`High: 6` | `Medium: 2` | `Low: 0`)
- **Phân bổ theo loại kiểm thử:** UI / Giao diện: **3**, Functional / Chức năng: **3**, Security / Bảo mật: **1**, Usability & Accessibility: **1**

---

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_NAV_001`** [High] _UI / Giao diện_ — Kiểm tra giao diện bố cục hiển thị mặc định của thanh Navbar / Header
- [ ] **`TC_NAV_002`** [High] _Functional / Chức năng_ — Kiểm tra điều hướng về Trang chủ khi click vào Logo trên Navbar
- [ ] **`TC_NAV_003`** [High] _Functional / Chức năng_ — Kiểm tra điều hướng các mục Menu trên Navbar và trạng thái nổi bật (Active State)
- [ ] **`TC_NAV_004`** [Medium] _Functional / Chức năng_ — Kiểm tra hoạt động của Menu con thả xuống (Dropdown Sub-menu / Mega Menu) trên Navbar
- [ ] **`TC_NAV_005`** [High] _UI / Giao diện_ — Kiểm tra hành vi cố định thanh điều hướng (Sticky / Fixed Navbar) khi cuộn trang
- [ ] **`TC_NAV_006`** [High] _UI / Giao diện_ — Kiểm tra giao diện Responsive của Navbar trên màn hình Tablet và Mobile (Hamburger Menu)
- [ ] **`TC_NAV_007`** [High] _Security / Bảo mật_ — Kiểm tra hiển thị các mục trên Navbar theo trạng thái Đăng nhập và Phân quyền (Role-based)
- [ ] **`TC_NAV_008`** [Medium] _Usability & Accessibility_ — Kiểm tra điều hướng trên Navbar bằng bàn phím (Tab, Enter, Esc)

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_NAV_001` | UI / Giao diện | **High** | **Kiểm tra giao diện bố cục hiển thị mặc định của thanh Navbar / Header** | Trang web đã được tải thành công. | 1. Quan sát thanh Navbar trên cùng màn hình.<br>2. Kiểm tra vị trí Logo, các mục Menu điều hướng chính, khu vực tìm kiếm, icon thông báo và Avatar/tên người dùng. | Màn hình Desktop (1366x768 / 1920x1080) | - Các thành phần trên Navbar hiển thị đầy đủ, căn chỉnh thẳng hàng ngang, đúng font chữ, màu sắc và khoảng cách theo thiết kế.<br>- Không có hiện tượng chữ bị rớt dòng hoặc các phần tử đè lên nhau. | `Not Run` |
| `TC_NAV_002` | Functional / Chức năng | **High** | **Kiểm tra điều hướng về Trang chủ khi click vào Logo trên Navbar** | Người dùng đang ở một trang con bất kỳ (khác Trang chủ). | 1. Di chuột vào Logo hệ thống ở góc trái Navbar.<br>2. Click chuột trái vào Logo. | Đang ở trang `/san-pham/chi-tiet` | - Con trỏ chuột khi di vào Logo chuyển thành hình bàn tay (`cursor: pointer`).<br>- Khi click vào Logo, hệ thống điều hướng người dùng quay về Trang chủ (`/` hoặc `/dashboard`). | `Not Run` |
| `TC_NAV_003` | Functional / Chức năng | **High** | **Kiểm tra điều hướng các mục Menu trên Navbar và trạng thái nổi bật (Active State)** | Thanh Navbar có các mục: Trang chủ, Sản phẩm, Đơn hàng, Báo cáo. | 1. Click lần lượt vào từng mục Menu trên Navbar.<br>2. Quan sát URL, nội dung trang đích và trạng thái hiển thị của mục Menu đang chọn.<br>3. Nhấn F5 (Reload) hoặc nhập trực tiếp URL của mục đó lên trình duyệt. | Click các mục Menu trên Navbar | - Mỗi mục Menu điều hướng chính xác đến trang đích tương ứng.<br>- Mục Menu của trang hiện tại luôn được làm nổi bật (Active state: in đậm, đổi màu hoặc có gạch chân bên dưới) kể cả khi truy cập trực tiếp bằng URL hay nhấn F5. | `Not Run` |
| `TC_NAV_004` | Functional / Chức năng | **Medium** | **Kiểm tra hoạt động của Menu con thả xuống (Dropdown Sub-menu / Mega Menu) trên Navbar** | Trên Navbar có mục Menu chứa các danh mục con. | 1. Di chuột (Hover) hoặc Click vào mục Menu cha.<br>2. Chọn một mục trong danh sách Menu con.<br>3. Mở lại Menu con rồi click ra ngoài (Click outside). | Menu cha -> Sub-menu | - Menu con xổ xuống mượt mà, hiển thị đầy đủ danh sách và nằm đè lên trên nội dung trang (z-index chuẩn).<br>- Chọn mục con chuyển đúng đến trang đích và tự động đóng Menu con.<br>- Click ra ngoài hoặc di chuột ra khỏi vùng Menu sẽ đóng Menu con. | `Not Run` |
| `TC_NAV_005` | UI / Giao diện | **High** | **Kiểm tra hành vi cố định thanh điều hướng (Sticky / Fixed Navbar) khi cuộn trang** | Trang có nội dung dài hơn chiều cao màn hình. | 1. Cuộn trang xuống dưới cuối trang (Scroll Down).<br>2. Quan sát vị trí của thanh Navbar và phần nội dung trượt bên dưới.<br>3. Mở một Popup Modal khi đang ở giữa trang. | Cuộn dọc trang web | - Nếu thiết kế là Sticky/Fixed Header: Thanh Navbar luôn bám cố định ở cạnh trên cùng màn hình.<br>- Nội dung trang khi cuộn lên sẽ luồn xuống bên dưới Navbar (không bị nhìn xuyên thấu gây rối mắt) và phần đầu trang không bị Navbar che khuất.<br>- Khi mở Popup Modal, lớp phủ Backdrop của Modal phải che lên cả Navbar. | `Not Run` |
| `TC_NAV_006` | UI / Giao diện | **High** | **Kiểm tra giao diện Responsive của Navbar trên màn hình Tablet và Mobile (Hamburger Menu)** | Thu nhỏ kích thước trình duyệt hoặc mở trên thiết bị Mobile (375px) và Tablet (768px). | 1. Quan sát sự thay đổi bố cục của thanh Navbar trên màn hình nhỏ.<br>2. Chạm vào biểu tượng Hamburger Menu (`☰`). | Viewport: 375x812 (Mobile) & 768x1024 (Tablet) | - Các mục menu dài tự động được thu gọn vào trong nút Hamburger Menu (`☰`), không gây tràn màn hình ngang.<br>- Khi bấm vào nút `☰`, danh sách menu mở ra đầy đủ để người dùng điều hướng. | `Not Run` |
| `TC_NAV_007` | Security / Bảo mật | **High** | **Kiểm tra hiển thị các mục trên Navbar theo trạng thái Đăng nhập và Phân quyền (Role-based)** | Hệ thống có nhiều nhóm quyền (Khách chưa đăng nhập, User thường, Admin). | 1. Truy cập khi chưa đăng nhập (Guest).<br>2. Đăng nhập bằng tài khoản User thường.<br>3. Đăng nhập bằng tài khoản Admin. | Guest vs User vs Admin | - Khi chưa đăng nhập: Hiển thị nút 'Đăng nhập / Đăng ký'.<br>- Khi đã đăng nhập: Hiển thị Avatar, Tên người dùng, Thông báo và nút 'Đăng xuất'.<br>- Tài khoản User thường tuyệt đối không nhìn thấy các mục menu chỉ dành riêng cho Admin. | `Not Run` |
| `TC_NAV_008` | Usability & Accessibility | **Medium** | **Kiểm tra điều hướng trên Navbar bằng bàn phím (Tab, Enter, Esc)** | Đang ở đầu trang web. | 1. Nhấn phím `Tab` liên tiếp để di chuyển qua Logo và các mục trên Navbar.<br>2. Nhấn `Enter` để mở menu con hoặc chuyển trang, nhấn `Esc` để đóng menu con. | Keyboard Navigation | - Thứ tự Focus bằng phím `Tab` đi lần lượt từ trái sang phải đúng theo bố cục hiển thị.<br>- Có viền Focus rõ ràng tại từng mục. | `Not Run` |
