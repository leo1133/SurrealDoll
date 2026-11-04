# TEST CASE: 8. SEARCH BAR

- **Mô tả chức năng:** Thanh tìm kiếm dữ liệu theo từ khóa
- **Tổng số Test Case:** **8** (`High: 7` | `Medium: 1` | `Low: 0`)
- **Phân bổ theo loại kiểm thử:** UI / Giao diện: **1**, Functional / Chức năng: **4**, Validation & Negative: **1**, Security / Bảo mật: **1**, Usability & Accessibility: **1**

---

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_SRC_001`** [High] _UI / Giao diện_ — Kiểm tra giao diện hiển thị mặc định của thanh tìm kiếm (Search Bar)
- [ ] **`TC_SRC_002`** [High] _Functional / Chức năng_ — Kiểm tra tìm kiếm khớp chính xác (Exact Match) và khớp một phần (Partial Match) bằng phím Enter & nút Tìm kiếm
- [ ] **`TC_SRC_003`** [High] _Functional / Chức năng_ — Kiểm tra tìm kiếm không phân biệt chữ hoa/thường và hỗ trợ tiếng Việt có dấu / không dấu
- [ ] **`TC_SRC_004`** [High] _Functional / Chức năng_ — Kiểm tra tự động cắt khoảng trắng thừa ở đầu và cuối từ khóa (Auto-trim Spaces)
- [ ] **`TC_SRC_005`** [High] _Functional / Chức năng_ — Kiểm tra nút xóa nhanh từ khóa (`✕` Clear) để khôi phục danh sách ban đầu
- [ ] **`TC_SRC_006`** [High] _Validation & Negative_ — Kiểm tra hiển thị khi từ khóa tìm kiếm không có kết quả nào phù hợp (Empty Search Result)
- [ ] **`TC_SRC_007`** [High] _Security / Bảo mật_ — Kiểm tra nhập ký tự đặc biệt (`%`, `_`, `\`, `'`) và chống SQL Injection / XSS trên Search Bar
- [ ] **`TC_SRC_008`** [Medium] _Usability & Accessibility_ — Kiểm tra cơ chế Debounce (tìm kiếm tức thì khi gõ) và Lịch sử tìm kiếm gần đây (Recent Searches)

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_SRC_001` | UI / Giao diện | **High** | **Kiểm tra giao diện hiển thị mặc định của thanh tìm kiếm (Search Bar)** | Màn hình danh sách hoặc trang chủ có thanh Search Bar. | 1. Quan sát ô Search Bar, icon kính lúp 🔍 và dòng chữ gợi ý (Placeholder).<br>2. Gõ một vài ký tự vào ô và quan sát sự xuất hiện của nút xóa nhanh (`✕`). | N/A | - Hiển thị đúng kích thước, viền và icon kính lúp.<br>- Placeholder mô tả rõ các tiêu chí có thể tìm kiếm (VD: "Tìm theo mã đơn hàng, tên hoặc SĐT khách hàng...").<br>- Nút xóa nhanh (`✕`) chỉ xuất hiện khi trong ô đã có ký tự và ẩn đi khi ô đang trống. | `Not Run` |
| `TC_SRC_002` | Functional / Chức năng | **High** | **Kiểm tra tìm kiếm khớp chính xác (Exact Match) và khớp một phần (Partial Match) bằng phím Enter & nút Tìm kiếm** | Hệ thống có dữ liệu sản phẩm: `iPhone 16 Pro Max`, `iPhone 15`, `Samsung Galaxy S24`. | 1. Nhập đầy đủ `"iPhone 16 Pro Max"` rồi nhấn phím `Enter`.<br>2. Nhập một phần từ khóa `"iPhone"` hoặc `"Pro"` rồi click vào nút icon kính lúp 🔍. | - Từ khóa 1: `"iPhone 16 Pro Max"`<br>- Từ khóa 2: `"iPhone"` | - Cả hai cách (nhấn `Enter` và click nút 🔍) đều kích hoạt tìm kiếm.<br>- Trả về chính xác các bản ghi có chứa từ khóa tương ứng. | `Not Run` |
| `TC_SRC_003` | Functional / Chức năng | **High** | **Kiểm tra tìm kiếm không phân biệt chữ hoa/thường và hỗ trợ tiếng Việt có dấu / không dấu** | Trong hệ thống có bản ghi tên khách hàng: `"Nguyễn Văn An"`. | 1. Nhập chữ thường toàn bộ: `"nguyễn văn an"` -> Tìm kiếm.<br>2. Nhập chữ hoa toàn bộ: `"NGUYỄN VĂN AN"` -> Tìm kiếm.<br>3. Nhập tiếng Việt không dấu: `"nguyen van an"` -> Tìm kiếm. | - `"nguyễn văn an"`<br>- `"NGUYỄN VĂN AN"`<br>- `"nguyen van an"` | - Hệ thống tìm kiếm không phân biệt hoa/thường (Case-insensitive) và trả về đúng bản ghi `"Nguyễn Văn An"` ở cả 3 trường hợp. | `Not Run` |
| `TC_SRC_004` | Functional / Chức năng | **High** | **Kiểm tra tự động cắt khoảng trắng thừa ở đầu và cuối từ khóa (Auto-trim Spaces)** | Người dùng thường vô tình copy-paste từ khóa có dính khoảng trắng ở đầu hoặc cuối. | 1. Nhập từ khóa có dấu cách ở đầu và cuối: `"   iPhone 16   "`.<br>2. Nhấn Enter tìm kiếm. | `"   iPhone 16   "` | - Hệ thống tự động `trim()` khoảng trắng thừa ở hai đầu và trả về đúng kết quả của `"iPhone 16"` (không bị báo 'Không tìm thấy kết quả' do thừa dấu cách). | `Not Run` |
| `TC_SRC_005` | Functional / Chức năng | **High** | **Kiểm tra nút xóa nhanh từ khóa (`✕` Clear) để khôi phục danh sách ban đầu** | Đang hiển thị kết quả tìm kiếm của từ khóa `"iPhone"`. | 1. Click vào icon `✕` (Clear) bên phải ô Search Bar. | Click nút `✕` | - Từ khóa trong ô Search Bar bị xóa sạch.<br>- Danh sách dữ liệu tự động tải lại toàn bộ bản ghi mặc định ban đầu (hoặc chờ nhấn Enter theo thiết kế nhất quán). | `Not Run` |
| `TC_SRC_006` | Validation & Negative | **High** | **Kiểm tra hiển thị khi từ khóa tìm kiếm không có kết quả nào phù hợp (Empty Search Result)** | Ô Search Bar đang hoạt động. | 1. Nhập từ khóa không tồn tại trong hệ thống: `"san_pham_khong_ton_tai_9999"`.<br>2. Nhấn Enter. | `"san_pham_khong_ton_tai_9999"` | - Hiển thị giao diện Empty State rõ ràng, thân thiện: "Không tìm thấy kết quả nào phù hợp với từ khóa..." (kèm nút 'Xóa tìm kiếm' nếu có). | `Not Run` |
| `TC_SRC_007` | Security / Bảo mật | **High** | **Kiểm tra nhập ký tự đặc biệt (`%`, `_`, `\`, `'`) và chống SQL Injection / XSS trên Search Bar** | Ô Search Bar đang hoạt động. | 1. Chỉ nhập ký tự `%` hoặc `_` vào ô tìm kiếm và nhấn Enter.<br>2. Nhập chuỗi SQLi `' OR 1=1 --` và XSS `<script>alert('XSS')</script>` vào ô tìm kiếm. | - Wildcard: `%`, `_`<br>- SQLi: `' OR 1=1 --`<br>- XSS: `<script>alert('XSS')</script>` | - Khi nhập `%` hoặc `_`: Hệ thống phải hiểu là tìm ký tự phần trăm/gạch dưới thực tế (đã escape wildcard trong câu lệnh `LIKE`), KHÔNG được trả về toàn bộ dữ liệu như khi không lọc.<br>- Không bị lỗi SQL Injection (500 Error) và không thực thi đoạn mã XSS khi hiển thị lại câu thông báo kết quả tìm kiếm. | `Not Run` |
| `TC_SRC_008` | Usability & Accessibility | **Medium** | **Kiểm tra cơ chế Debounce (tìm kiếm tức thì khi gõ) và Lịch sử tìm kiếm gần đây (Recent Searches)** | Thanh Search Bar tự động tìm kiếm khi người dùng gõ (Live Search). | 1. Gõ liên tiếp nhanh một từ khóa dài 12 ký tự.<br>2. Kiểm tra số lượng Request API trong tab Network của DevTools. | Gõ nhanh 12 ký tự liên tiếp | - Hệ thống áp dụng Debounce (~300ms - 500ms), chỉ gửi Request tìm kiếm khi người dùng ngừng tay gõ, hiển thị icon xoay Loading nhỏ và hủy các Request cũ chưa hoàn tất. | `Not Run` |
