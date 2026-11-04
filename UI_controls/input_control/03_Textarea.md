# TEST CASE: 3. TEXTAREA

- **Mô tả chức năng:** Ô nhập văn bản nhiều dòng (mô tả, địa chỉ, ghi chú...)
- **Tổng số Test Case:** **9** (`High: 4` | `Medium: 5` | `Low: 0`)
- **Phân bổ theo loại kiểm thử:** UI / Giao diện: **4**, Functional / Chức năng: **2**, Boundary / Giá trị biên: **1**, Validation & Negative: **1**, Security / Bảo mật: **1**

---

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_TXA_001`** [High] _UI / Giao diện_ — Kiểm tra giao diện mặc định của ô Textarea (ô nhập văn bản nhiều dòng)
- [ ] **`TC_TXA_002`** [High] _Functional / Chức năng_ — Kiểm tra nhập văn bản nhiều dòng bằng phím Enter và tự động xuống dòng (Word Wrap)
- [ ] **`TC_TXA_003`** [Medium] _UI / Giao diện_ — Kiểm tra thanh cuộn dọc (Vertical Scrollbar) khi nhập nội dung vượt quá chiều cao khung
- [ ] **`TC_TXA_004`** [Medium] _Functional / Chức năng_ — Kiểm tra bộ đếm ký tự (Character Counter) cập nhật theo thời gian thực
- [ ] **`TC_TXA_005`** [High] _Boundary / Giá trị biên_ — Kiểm tra giới hạn ký tự tối đa (Maxlength) và đồng bộ cách đếm ký tự xuống dòng (\r\n vs \n)
- [ ] **`TC_TXA_006`** [Medium] _UI / Giao diện_ — Kiểm tra tính năng kéo giãn kích thước (Resize handle) của ô Textarea
- [ ] **`TC_TXA_007`** [Medium] _Validation & Negative_ — Kiểm tra chỉ nhập toàn dấu cách (Space) hoặc chỉ nhấn Enter nhiều dòng trống
- [ ] **`TC_TXA_008`** [Medium] _UI / Giao diện_ — Kiểm tra nhập chuỗi ký tự dài liên tiếp không có khoảng trắng (Word-break test)
- [ ] **`TC_TXA_009`** [High] _Security / Bảo mật_ — Kiểm tra nhập thẻ HTML, mã XSS và biểu tượng Emoji trong Textarea

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_TXA_001` | UI / Giao diện | **High** | **Kiểm tra giao diện mặc định của ô Textarea (ô nhập văn bản nhiều dòng)** | Màn hình chứa ô Textarea (Mô tả / Ghi chú / Địa chỉ) đã tải xong. | 1. Quan sát ô Textarea.<br>2. Kiểm tra chiều cao mặc định (số dòng hiển thị), Label, Placeholder và bộ đếm ký tự (VD: `0/500`). | N/A | - Hiển thị khung nhập liệu nhiều dòng đúng kích thước thiết kế.<br>- Chữ Placeholder nằm ở góc trên bên trái của ô.<br>- Bộ đếm ký tự hiển thị chính xác `0/[Maxlength]` ở góc dưới. | `Not Run` |
| `TC_TXA_002` | Functional / Chức năng | **High** | **Kiểm tra nhập văn bản nhiều dòng bằng phím Enter và tự động xuống dòng (Word Wrap)** | Ô Textarea đang được Focus. | 1. Nhập một câu văn dài liên tục vượt quá chiều ngang của ô Textarea.<br>2. Nhấn phím Enter để chủ động xuống dòng mới và nhập tiếp dòng thứ 2, 3, 4.<br>3. Nhấn Lưu và kiểm tra dữ liệu hiển thị lại. | "Dòng 1: Văn bản mô tả chi tiết sản phẩm dài tự động xuống dòng.<br>Dòng 2: Ghi chú giao hàng giờ hành chính.<br>Dòng 3: Liên hệ trước 30 phút." | - Khi gõ hết chiều ngang, chữ tự động ngắt xuống dòng tiếp theo (Word wrap), không xuất hiện thanh cuộn ngang.<br>- Phím Enter tạo dòng mới bình thường (không tự động Submit form như Textbox).<br>- Khi lưu và hiển thị lại, hệ thống giữ nguyên các vị trí ngắt dòng (`\n`). | `Not Run` |
| `TC_TXA_003` | UI / Giao diện | **Medium** | **Kiểm tra thanh cuộn dọc (Vertical Scrollbar) khi nhập nội dung vượt quá chiều cao khung** | Ô Textarea hiển thị mặc định 4 dòng. | 1. Nhập hoặc Paste đoạn văn bản dài 15 dòng vào ô Textarea.<br>2. Sử dụng con lăn chuột hoặc kéo thanh cuộn dọc lên/xuống, dùng phím PageUp/PageDown/Mũi tên. | Đoạn văn bản dài 15 dòng | - Thanh cuộn dọc (Vertical scrollbar) tự động xuất hiện bên phải ô Textarea.<br>- Cuộn lên/xuống mượt mà, xem được đầy đủ từ dòng đầu tiên đến dòng cuối cùng. | `Not Run` |
| `TC_TXA_004` | Functional / Chức năng | **Medium** | **Kiểm tra bộ đếm ký tự (Character Counter) cập nhật theo thời gian thực** | Ô Textarea có bộ đếm ký tự tối đa 500 ký tự (`0/500`). | 1. Gõ 20 ký tự vào ô Textarea.<br>2. Paste thêm một đoạn 100 ký tự.<br>3. Bôi đen và xóa 50 ký tự. | Chuỗi văn bản bất kỳ | - Bước 1: Bộ đếm cập nhật ngay thành `20/500`.<br>- Bước 2: Bộ đếm cập nhật thành `120/500`.<br>- Bước 3: Bộ đếm giảm về `70/500` chính xác theo thời gian thực. | `Not Run` |
| `TC_TXA_005` | Boundary / Giá trị biên | **High** | **Kiểm tra giới hạn ký tự tối đa (Maxlength) và đồng bộ cách đếm ký tự xuống dòng (\r\n vs \n)** | Ô Textarea giới hạn tối đa Maxlength = 500 ký tự. | 1. Nhập văn bản có chứa nhiều dấu xuống dòng (Enter) sao cho tổng độ dài đúng bằng 500 ký tự.<br>2. Nhấn Lưu.<br>3. Paste đoạn văn bản dài 600 ký tự vào ô Textarea. | - Đoạn văn 500 ký tự (có chứa 10 lần xuống dòng)<br>- Đoạn văn 600 ký tự | - Tại 500 ký tự: Lưu thành công, không xảy ra lỗi lệch số ký tự giữa Frontend (đếm `\n` là 1 ký tự) và Backend (đếm `\r\n` là 2 ký tự).<br>- Tại 600 ký tự: Tự động cắt giữ lại 500 ký tự đầu hoặc hiển thị thông báo lỗi vượt quá giới hạn. | `Not Run` |
| `TC_TXA_006` | UI / Giao diện | **Medium** | **Kiểm tra tính năng kéo giãn kích thước (Resize handle) của ô Textarea** | Quan sát góc dưới bên phải của ô Textarea. | 1. Dùng chuột nắm góc dưới bên phải của ô Textarea và kéo rộng ra theo chiều ngang và chiều dọc.<br>2. Kiểm tra bố cục (Layout) các thành phần xung quanh. | N/A | - Nếu cho phép resize (chỉ dọc `resize: vertical` hoặc cố định `resize: none`): Khung Textarea chỉ giãn trong phạm vi cho phép, tuyệt đối không làm vỡ layout hoặc đè lấp các nút/trường nhập liệu bên cạnh. | `Not Run` |
| `TC_TXA_007` | Validation & Negative | **Medium** | **Kiểm tra chỉ nhập toàn dấu cách (Space) hoặc chỉ nhấn Enter nhiều dòng trống** | Ô Textarea là trường bắt buộc. | 1. Chỉ nhấn phím Enter 5 lần và phím Space 10 lần.<br>2. Nhấn nút Lưu / Submit. | "\n\n\n\n          " | - Hệ thống trim các khoảng trắng và dòng trống vô nghĩa, xác định trường đang rỗng và hiển thị thông báo lỗi bắt buộc nhập. | `Not Run` |
| `TC_TXA_008` | UI / Giao diện | **Medium** | **Kiểm tra nhập chuỗi ký tự dài liên tiếp không có khoảng trắng (Word-break test)** | Ô Textarea đang hoạt động. | 1. Nhập chuỗi 500 ký tự viết liền không có dấu cách (VD: `aaaa...aaaa`).<br>2. Lưu lại và kiểm tra màn hình hiển thị chi tiết. | 500 ký tự 'a' viết liền không khoảng trắng | - Cả ở trong ô Textarea lẫn màn hình hiển thị sau khi lưu đều tự động ngắt dòng (`word-break: break-word` / `overflow-wrap: anywhere`), không làm tràn chữ ra ngoài khung giao diện. | `Not Run` |
| `TC_TXA_009` | Security / Bảo mật | **High** | **Kiểm tra nhập thẻ HTML, mã XSS và biểu tượng Emoji trong Textarea** | Ô Textarea đang hoạt động. | 1. Nhập đoạn văn có chứa Emoji (`😀🎉🚀`), thẻ HTML (`<h1>Tiêu đề</h1>`) và script (`<script>alert(1)</script>`).<br>2. Nhấn Lưu và tải lại trang. | `Xin chào 😀 <h1>Test</h1> <script>alert(1)</script>` | - Emoji được lưu và hiển thị đúng (hỗ trợ chuẩn UTF-8 / utf8mb4).<br>- Các thẻ HTML và script được hiển thị dưới dạng văn bản thuần (plain text) đã escape, không thực thi mã độc. | `Not Run` |
