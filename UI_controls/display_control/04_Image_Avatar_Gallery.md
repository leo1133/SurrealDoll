# TEST CASE: 4. IMAGE / AVATAR / GALLERY

- **Mô tả chức năng:** Ảnh đại diện (Avatar), ảnh sản phẩm, bộ sưu tập ảnh (Gallery) và trình chiếu ảnh (Carousel)
- **Tổng số Test Case:** **6** (`High: 4` | `Medium: 2` | `Low: 0`)
- **Phân bổ theo loại kiểm thử:** UI / Giao diện: **1**, Validation & Negative: **1**, Functional / Chức năng: **2**, Boundary / Giá trị biên: **1**, Usability & Accessibility: **1**

---

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_IMG_001`** [High] _UI / Giao diện_ — Kiểm tra hiển thị Hình ảnh và Avatar đúng tỷ lệ khung hình, không bị méo hoặc vỡ nét
- [ ] **`TC_IMG_002`** [High] _Validation & Negative_ — Kiểm tra hiển thị Ảnh thay thế mặc định (Fallback Image / Initials Avatar) khi ảnh bị lỗi 404 hoặc rỗng
- [ ] **`TC_IMG_003`** [High] _Functional / Chức năng_ — Kiểm tra chức năng chọn ảnh Thumbnail và phóng to ảnh (Lightbox / Image Preview) trong Gallery
- [ ] **`TC_IMG_004`** [High] _Functional / Chức năng_ — Kiểm tra hoạt động của Slider trình chiếu ảnh (Carousel / Banner Slider)
- [ ] **`TC_IMG_005`** [Medium] _Boundary / Giá trị biên_ — Kiểm tra hiển thị Gallery / Carousel khi chỉ có duy nhất 1 bức ảnh
- [ ] **`TC_IMG_006`** [Medium] _Usability & Accessibility_ — Kiểm tra tối ưu tải ảnh (Lazy Loading, Skeleton) và thuộc tính văn bản thay thế (`alt`)

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_IMG_001` | UI / Giao diện | **High** | **Kiểm tra hiển thị Hình ảnh và Avatar đúng tỷ lệ khung hình, không bị méo hoặc vỡ nét** | Màn hình có hiển thị Avatar người dùng và ảnh sản phẩm/bài viết với nhiều kích thước gốc khác nhau (ảnh dọc, ảnh ngang, ảnh vuông). | 1. Quan sát các hình ảnh và Avatar trên giao diện. | Ảnh gốc tỷ lệ 16:9, 4:3, 9:16 | - Hình ảnh được xử lý `object-fit: cover` (hoặc `contain` tùy ngữ cảnh), giữ đúng tỷ lệ tự nhiên của vật thể trong ảnh, tuyệt đối không bị bóp méo chiều ngang hay kéo giãn chiều dọc.<br>- Avatar hiển thị dạng hình tròn (hoặc bo góc) sắc nét, căn chính giữa. | `Not Run` |
| `TC_IMG_002` | Validation & Negative | **High** | **Kiểm tra hiển thị Ảnh thay thế mặc định (Fallback Image / Initials Avatar) khi ảnh bị lỗi 404 hoặc rỗng** | - TH1: Người dùng chưa cập nhật ảnh đại diện (`avatar_url = null`).<br>- TH2: Đường dẫn ảnh bị hỏng hoặc trả về lỗi `404 Not Found`. | 1. Quan sát Avatar và Ảnh sản phẩm trong 2 trường hợp trên. | `avatar_url = null` & `image_url = 404` | - Hệ thống tự động bắt sự kiện `onerror` của thẻ `<img>` để thay thế bằng ảnh Placeholder mặc định (hoặc hiển thị chữ cái đầu tên người dùng như `"NA"` trên nền màu đối với Avatar).<br>- Tuyệt đối không hiển thị biểu tượng ảnh rách (Broken image icon) mặc định của trình duyệt. | `Not Run` |
| `TC_IMG_003` | Functional / Chức năng | **High** | **Kiểm tra chức năng chọn ảnh Thumbnail và phóng to ảnh (Lightbox / Image Preview) trong Gallery** | Trang chi tiết sản phẩm có 1 ảnh lớn chính và danh sách 5 ảnh nhỏ (Thumbnails) bên dưới. | 1. Click lần lượt vào từng ảnh Thumbnail bên dưới.<br>2. Click vào ảnh lớn chính để mở chế độ xem phóng to (Lightbox).<br>3. Trong Lightbox: Thử bấm nút `Next (>)`, `Prev (<)`, `Phóng to/Thu nhỏ (Zoom)` và nhấn nút `✕` (hoặc phím `Esc`). | Gallery 5 ảnh + Lightbox | - Bước 1: Ảnh chính đổi ngay theo ảnh Thumbnail vừa chọn; Thumbnail đang active có viền nổi bật.<br>- Bước 2-3: Lightbox mở ảnh độ phân giải cao giữa màn hình nền tối, chuyển qua lại giữa các ảnh mượt mà bằng cả chuột và phím mũi tên `Left`/`Right`, đóng lại khi nhấn `✕` hoặc `Esc`. | `Not Run` |
| `TC_IMG_004` | Functional / Chức năng | **High** | **Kiểm tra hoạt động của Slider trình chiếu ảnh (Carousel / Banner Slider)** | Trang có Banner Carousel gồm 4 slides ảnh. | 1. Quan sát Carousel tự động chuyển slide (Auto-play).<br>2. Di chuột (Hover) vào vùng Carousel và giữ yên.<br>3. Click nút mũi tên `Next (>)`, `Prev (<)` và các chấm tròn chỉ mục (Pagination Dots) bên dưới.<br>4. Trên Mobile: Dùng ngón tay vuốt ngang (Swipe Left / Right) trên Banner. | Carousel 4 slides | - Bước 1: Tự động chuyển slide đúng chu kỳ cài đặt (VD: 4 giây/lần) và lặp vòng từ slide 4 về slide 1.<br>- Bước 2: Tạm dừng tự động chạy (Pause on hover) khi người dùng đang di chuột xem.<br>- Bước 3-4: Chuyển đúng đến slide mong muốn khi click mũi tên/chấm tròn hoặc vuốt cảm ứng trên Mobile; chấm tròn Active cập nhật đúng vị trí slide hiện tại. | `Not Run` |
| `TC_IMG_005` | Boundary / Giá trị biên | **Medium** | **Kiểm tra hiển thị Gallery / Carousel khi chỉ có duy nhất 1 bức ảnh** | Sản phẩm hoặc Banner chỉ được cấu hình 1 bức ảnh duy nhất. | 1. Quan sát giao diện Carousel / Gallery. | Số lượng ảnh = 1 | - Hiển thị bức ảnh duy nhất.<br>- Tự động ẩn các nút mũi tên chuyển tiếp (`<`, `>`), ẩn dãy chấm tròn chỉ mục (Dots) và không chạy hiệu ứng trượt lặp lại. | `Not Run` |
| `TC_IMG_006` | Usability & Accessibility | **Medium** | **Kiểm tra tối ưu tải ảnh (Lazy Loading, Skeleton) và thuộc tính văn bản thay thế (`alt`)** | Trang danh sách có nhiều hình ảnh độ phân giải cao. | 1. Cuộn trang với tốc độ mạng chậm (Slow 3G) và quan sát quá trình ảnh tải lên.<br>2. Kiểm tra thuộc tính `alt` của các thẻ `<img>` trong DOM. | Slow 3G & Inspect `<img>` | - Trong lúc ảnh đang tải, khung ảnh giữ sẵn kích thước cố định kèm nền Skeleton (không gây giật nhảy bố cục `Cumulative Layout Shift - CLS` khi ảnh tải xong).<br>- Các thẻ `<img>` có thuộc tính `alt` mô tả nội dung ảnh đầy đủ. | `Not Run` |
