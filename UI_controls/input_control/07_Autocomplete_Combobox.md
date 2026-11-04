# TEST CASE: 7. AUTOCOMPLETE / COMBOBOX

- **Mô tả chức năng:** Ô nhập gợi ý dữ liệu khi người dùng bắt đầu gõ ký tự
- **Tổng số Test Case:** **7** (`High: 4` | `Medium: 3` | `Low: 0`)
- **Phân bổ theo loại kiểm thử:** UI / Giao diện: **1**, Functional / Chức năng: **3**, Validation & Negative: **2**, Usability & Accessibility: **1**

---

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_AUT_001`** [High] _UI / Giao diện_ — Kiểm tra giao diện mặc định của ô Autocomplete / Combobox
- [ ] **`TC_AUT_002`** [High] _Functional / Chức năng_ — Kiểm tra hiển thị danh sách gợi ý (Suggestions) khi bắt đầu gõ ký tự hợp lệ
- [ ] **`TC_AUT_003`** [High] _Functional / Chức năng_ — Kiểm tra tìm kiếm không phân biệt hoa/thường và hỗ trợ tiếng Việt không dấu
- [ ] **`TC_AUT_004`** [Medium] _Functional / Chức năng_ — Kiểm tra cập nhật danh sách gợi ý khi gõ thêm, xóa bớt ký tự hoặc bấm nút Clear (x)
- [ ] **`TC_AUT_005`** [High] _Validation & Negative_ — Kiểm tra khi nhập từ khóa không khớp với bất kỳ kết quả nào (No matching results)
- [ ] **`TC_AUT_006`** [Medium] _Validation & Negative_ — Kiểm tra nhập từ khóa có khoảng trắng thừa hoặc chứa ký tự đặc biệt (%, _, \, ')
- [ ] **`TC_AUT_007`** [Medium] _Usability & Accessibility_ — Kiểm tra chọn gợi ý bằng bàn phím (Mũi tên Up/Down, Enter, Esc) và cơ chế Debounce / Race Condition

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_AUT_001` | UI / Giao diện | **High** | **Kiểm tra giao diện mặc định của ô Autocomplete / Combobox** | Màn hình chứa ô Autocomplete đã tải xong. | 1. Quan sát ô nhập liệu Autocomplete.<br>2. Kiểm tra Label, Placeholder, icon tìm kiếm/mũi tên. | N/A | - Hiển thị đúng thiết kế, có Placeholder hướng dẫn rõ ràng (VD: "Nhập tên sản phẩm để tìm kiếm..."). | `Not Run` |
| `TC_AUT_002` | Functional / Chức năng | **High** | **Kiểm tra hiển thị danh sách gợi ý (Suggestions) khi bắt đầu gõ ký tự hợp lệ** | Hệ thống có sẵn dữ liệu danh mục (VD: Hà Nội, Hà Giang, Hà Tĩnh, Hải Phòng, TP. Hồ Chí Minh). | 1. Focus vào ô Autocomplete và gõ từ khóa "Hà".<br>2. Quan sát danh sách gợi ý xổ xuống và phần chữ được tô đậm (Highlight).<br>3. Click chọn "Hà Nội" từ danh sách gợi ý. | Từ khóa: "Hà" | - Danh sách gợi ý xuất hiện nhanh chóng, chỉ liệt kê các kết quả có chứa từ khóa "Hà" (Hà Nội, Hà Giang, Hà Tĩnh).<br>- Từ khóa trùng khớp được in đậm hoặc highlight.<br>- Khi click chọn "Hà Nội", giá trị được điền đầy đủ vào ô input và đóng popup gợi ý. | `Not Run` |
| `TC_AUT_003` | Functional / Chức năng | **High** | **Kiểm tra tìm kiếm không phân biệt hoa/thường và hỗ trợ tiếng Việt không dấu** | Danh mục có dữ liệu tiếng Việt có dấu (VD: "Nguyễn Văn An", "Đà Nẵng"). | 1. Nhập chữ thường không dấu: "nguyen van" hoặc "da nang".<br>2. Nhập chữ in hoa toàn bộ: "ĐÀ NẴNG". | - "nguyen van"<br>- "da nang"<br>- "ĐÀ NẴNG" | - Hệ thống tìm kiếm không phân biệt chữ hoa/thường (Case-insensitive).<br>- Hỗ trợ gợi ý chính xác cả khi người dùng gõ tiếng Việt không dấu. | `Not Run` |
| `TC_AUT_004` | Functional / Chức năng | **Medium** | **Kiểm tra cập nhật danh sách gợi ý khi gõ thêm, xóa bớt ký tự hoặc bấm nút Clear (x)** | Ô Autocomplete đang có từ khóa "Hà N" và đang hiển thị gợi ý. | 1. Nhấn Backspace xóa bớt ký tự thành "Hà".<br>2. Nhấn nút `x` (Clear) ở góc phải ô input. | "Hà N" -> "Hà" -> Clear | - Bước 1: Danh sách gợi ý tự động mở rộng lại tương ứng với từ khóa "Hà".<br>- Bước 2: Khi nhấn nút `x`, ô input được xóa trắng, danh sách gợi ý đóng lại (hoặc về danh sách mặc định) và con trỏ vẫn Focus tại ô. | `Not Run` |
| `TC_AUT_005` | Validation & Negative | **High** | **Kiểm tra khi nhập từ khóa không khớp với bất kỳ kết quả nào (No matching results)** | Ô Autocomplete đang Focus. | 1. Nhập chuỗi ký tự không tồn tại trong hệ thống: "xyz987654321".<br>2. Quan sát popup gợi ý. | Từ khóa: "xyz987654321" | - Popup hiển thị thông báo rõ ràng: "Không tìm thấy kết quả phù hợp" (No results found).<br>- Nếu là Combobox bắt buộc chọn từ danh sách có sẵn (Strict mode): Khi Blur ra ngoài, hệ thống xóa giá trị không hợp lệ hoặc hiển thị thông báo lỗi. | `Not Run` |
| `TC_AUT_006` | Validation & Negative | **Medium** | **Kiểm tra nhập từ khóa có khoảng trắng thừa hoặc chứa ký tự đặc biệt (%, _, \, ')** | Ô Autocomplete đang Focus. | 1. Nhập từ khóa có khoảng trắng ở đầu/cuối: "   Hà Nội   ".<br>2. Nhập các ký tự đặc biệt của SQL/Regex: `%`, `_`, `\`, `'`, `[`, `]`, `<script>`. | - "   Hà Nội   "<br>- "%_\'[]" | - Khoảng trắng đầu/cuối được tự động trim để tìm ra kết quả "Hà Nội".<br>- Các ký tự đặc biệt `%`, `_` không bị hiểu nhầm thành wildcard lấy toàn bộ DB, không gây lỗi crash JS Regex hay lỗi 500 từ API. | `Not Run` |
| `TC_AUT_007` | Usability & Accessibility | **Medium** | **Kiểm tra chọn gợi ý bằng bàn phím (Mũi tên Up/Down, Enter, Esc) và cơ chế Debounce / Race Condition** | Ô Autocomplete gọi API tìm kiếm động. | 1. Gõ nhanh liên tiếp một chuỗi 10 ký tự vào ô tìm kiếm.<br>2. Dùng phím mũi tên `Down` / `Up` để di chuyển qua các dòng gợi ý.<br>3. Nhấn phím `Enter` để chọn dòng đang highlight.<br>4. Nhấn phím `Esc` khi danh sách đang mở. | Gõ nhanh + Điều hướng phím | - Có cơ chế Debounce (~300ms) để không bắn request API ở từng ký tự gõ nhanh, và kết quả của request cũ trả về muộn không ghi đè kết quả của từ khóa mới nhất (chống Race Condition).<br>- Phím mũi tên `Up`/`Down`, `Enter`, `Esc` hoạt động mượt mà, cuộn danh sách theo vạch sáng chọn. | `Not Run` |
