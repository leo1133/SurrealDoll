# BẢNG ĐẶC TẢ KIỂM THỬ GIAO DIỆN THỦ CÔNG (MANUAL UI TEST SUITE)
## Màn hình: AF400 — Gift Manage: Gift Category (ギフトカテゴリ管理)
### Phân hệ: Master Admin Web / 商品管理 (`AF` Module)
### Nguồn Spec: Google Sheet `AF400` (gid=`993447379`) + Postman `Live2d_BE/gift/category`
### Áp dụng: `Universal_Rules/02_manual_ui_test_case_rule.md` & `UI_controls/`

---

## BẢNG ĐIỀU KHIỂN TIẾN ĐỘ & THỐNG KÊ (DASHBOARD HEADER)

| Thuộc tính | Giá trị | Thuộc tính | Giá trị | Round 1 Metric | Kết quả | Round 2 Metric | Kết quả |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Module Code** | `AF400` | **Environment** | `Dev-Admin` / `STG-Admin` | **Pass** | 0 | **Pass** | 0 |
| **Total Testcases** | **35** | **% Executed** | 0% | **Fail** | 0 | **Fail** | 0 |
| **Plan to Execute** | **35** | **Creator** | `QA` | **Impact** | 0 | **Impact** | 0 |
| **Spec Source** | Google Sheet `AF400` | **Liên kết chéo** | `AF100`, `AF200`, `AF300`, `I600` | **Not Run** | 35 | **Not Run** | 0 |
| | | | | **Total** | 35 | **Total** | 0 |

---

## CHI TIẾT BẢNG TEST CASES (8 CỘT CHUẨN MARKDOWN)

| ID | Title | Big item | Steps | Pre-condition | Expected | Priority | Automation Feasibility |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| | **I. COMMON & NAVIGATION** | | | | | | |
| `[AF400-1]` | [0] Kiểm tra truy cập màn hình | Sidebar UI & Tab title | 1. Đăng nhập Admin 2. Click `ギフト管理 > ギフトカテゴリ管理` | User là Master Admin | 1. Sidebar highlight `ギフトカテゴリ管理`; Tab title `商品管理｜ギフトカテゴリ管理`; Title `カテゴリ一覧` | High | Auto-UI |
| `[AF400-2]` | [0] Kiểm tra truy cập màn hình | Inbound URL & Breadcrumb | 1. Truy cập trực tiếp URL AF400 2. Quan sát Breadcrumb | Đã đăng nhập Admin | 1. Breadcrumb hiển thị đúng `ホーム＞ギフトカテゴリ管理` | Medium | Auto-UI |
| `[AF400-3]` | [0] Kiểm tra truy cập màn hình | F5 Reload giữ nguyên thứ tự | 1. Mở AF400 2. Nhấn F5 | Có >= 2 category | 1. Tải lại danh sách category đúng thứ tự `sort_order` | Medium | Auto-UI |
| `[AF400-4]` | [0] Kiểm tra truy cập màn hình | Phân quyền RBAC | 1. Đăng nhập tài khoản không có quyền 2. Truy cập AF400 | Role không có quyền | 1. Báo CMMSG5: `この操作を行う権限がありません。` | High | Auto-API |
| | **II. MAIN SCREEN CONTROLS** | | | | | | |
| `[AF400-5]` | [1] Danh sách Category - Header | Cột `カテゴリ名`, `gift_count`, Icon 6 dots, Nút Xóa | 1. Quan sát các cột trên bảng AF400 | - | 1. Hiển thị đầy đủ icon kéo thả 6 dots, `カテゴリ名` (tabable text), số lượng gift (`gift_count`), nút Xóa | Low | Auto-UI |
| `[AF400-6]` | [1] Danh sách Category - Infinite Scroll (`CMR01`) | Cuộn vô hạn (Infinite Scroll) | 1. Mở AF400 khi có nhiều category (> 20) 2. Cuộn xuống cuối danh sách | Có > 20 category | 1. Tự động tải thêm trang tiếp theo khi cuộn xuống đáy danh sách | High | Auto-UI |
| `[AF400-7]` | [1] Danh sách Category - Empty State | Không có dữ liệu category | 1. Mở AF400 khi hệ thống có 0 category | 0 category trong DB | 1. Hiển thị Empty State `CMMSG47` | Medium | Auto-UI |
| `[AF400-8]` | [6] Kéo thả Sort Order (Icon 6 dots) | Kéo thả thay đổi thứ tự category | 1. Nhấn giữ icon 6 dots của Category B kéo lên trên Category A 2. Nhấn F5 3. Kiểm tra tab Category trên App `I600` | Có >= 2 category | 1. Gọi `PUT /gift/category/sort-order/{id}`; sau F5 thứ tự mới giữ nguyên; App `I600` & pulldown AF100/AF200 cập nhật đúng thứ tự | High | Manual-Only (UX) |
| `[AF400-9]` | [2] Button `新規登録` | Mở Modal tạo mới category | 1. Click nút `新規登録` | - | 1. Mở Modal `カテゴリを追加します` với ô nhập tên trống và nút `追加` | High | Auto-UI |
| `[AF400-10]` | [7] Tabable Text `カテゴリ名` | Click vào tên category mở Modal Sửa | 1. Click vào tên 1 category trên bảng | Có >= 1 category | 1. Mở Modal `カテゴリを編集します` pre-fill đúng tên hiện tại và nút `保存` | High | Auto-UI |
| `[AF400-11]` | [7] Tabable Text `カテゴリ名` | Nhấn `Tab + Enter` mở Modal Sửa | 1. Nhấn phím `Tab` focus vào tên category 2. Nhấn `Enter` | Có >= 1 category | 1. Mở Modal `カテゴリを編集します` pre-fill đúng tên hiện tại | Medium | Auto-UI |
| `[AF400-12]` | [8] Cột `gift_count` | Đối soát số lượng gift thuộc category | 1. Đối chiếu số hiển thị với DB `gifts` (`WHERE category_id = X AND deleted_at IS NULL`) | - | 1. Số lượng `gift_count` khớp 100% với DB | High | Auto-UI |
| `[AF400-13]` | [9] Nút Xóa Category | Xóa category rỗng (0 gift) thành công | 1. Chọn category có 0 gift 2. Click nút Xóa và xác nhận | Category có 0 gift | 1. Báo thành công (`CMMSG14`), category bị xóa khỏi danh sách và soft-delete trong DB | High | Auto-UI |
| `[AF400-14]` | [9] Nút Xóa Category | Hủy xóa trên popup xác nhận | 1. Click nút Xóa 2. Nhấn Hủy/Đóng popup xác nhận (nếu có `[Q&A #2]`) | Category có >= 1 gift | 1. Đóng popup, category vẫn tồn tại nguyên vẹn trong danh sách | Medium | Auto-UI |
| `[AF400-15]` | [9] Nút Xóa Category | Xóa category đang có gift -> Gift chuyển thành `未設定` | 1. Chọn category đang có >= 1 gift 2. Click nút Xóa và xác nhận 3. Kiểm tra gift đó ở AF100 & App `I600` | Category có >= 1 gift | 1. Xóa category thành công (`CMMSG14`); các gift trực thuộc KHÔNG bị xóa mà chuyển thành không có category (`未設定` / tab `一般` trên `I600`) | High | Manual-Only (Complex DB) |
| `[AF400-16]` | [-] Error Handling | Mất kết nối mạng (`CMMSG8`) | 1. Ngắt mạng (Offline) 2. Thực hiện tải danh sách hoặc lưu category | - | 1. Hiển thị đúng thông báo lỗi mạng `CMMSG8` | High | Auto-API |
| `[AF400-17]` | [-] Error Handling | Lỗi Server 500 (`CMMSG1`) | 1. Giả lập API trả HTTP 500 | - | 1. Hiển thị đúng thông báo lỗi hệ thống `CMMSG1` | High | Auto-API |
| `[AF400-18]` | [-] Error Handling | Hết phiên đăng nhập (`CMMSG10`) | 1. Giả lập token hết hạn (HTTP 401) 2. Thực hiện thao tác trên màn hình | - | 1. Hiển thị đúng thông báo hết phiên `CMMSG10` và điều hướng về Login | High | Auto-API |
| | **III. SUB-LAYOUTS / MODALS (CREATE & EDIT)** | | | | | | |
| `[AF400-19]` | [3]-[5] Modal Tạo mới (`カテゴリを追加します`) | Tạo mới thành công (<= 20 ký tự) & Sort order ở cuối | 1. Nhập tên hợp lệ (<= 20 ký tự) 2. Click `追加` | Modal Tạo đang mở | 1. Đóng modal, báo thành công; category mới nằm ở cuối danh sách (sort_order lớn nhất) | High | Auto-UI |
| `[AF400-20]` | [3]-[5] Modal Tạo mới (`カテゴリを追加します`) | Biên Max = 20 ký tự hợp lệ | 1. Nhập đúng 20 ký tự 2. Click `追加` | Modal Tạo đang mở | 1. Cho phép nhập đủ 20 ký tự và lưu thành công | High | Auto-Data |
| `[AF400-21]` | [3]-[5] Modal Tạo mới (`カテゴリを追加します`) | Biên vượt Max = 21 ký tự | 1. Nhập hoặc paste 21 ký tự 2. Click `追加` | Modal Tạo đang mở | 1. Chặn nhập quá 20 ký tự hoặc báo lỗi `CMMSG49` (`20文字以内で入力してください。`) | High | Auto-Data |
| `[AF400-22]` | [3]-[5] Modal Tạo mới (`カテゴリを追加します`) | Bỏ trống ô tên category | 1. Để trống ô nhập 2. Click `追加` | Modal Tạo đang mở | 1. Báo lỗi bắt buộc nhập `CMMSG29` | High | Auto-Data |
| `[AF400-23]` | [3]-[5] Modal Tạo mới (`カテゴリを追加します`) | Nhập toàn khoảng trắng `"   "` | 1. Nhập `"   "` 2. Click `追加` | Modal Tạo đang mở | 1. Không cho lưu, báo lỗi `CMMSG29` | High | Auto-Data |
| `[AF400-24]` | [3]-[5] Modal Tạo mới (`カテゴリを追加します`) | Khoảng trắng đầu/cuối (`"  Cat  "`) | 1. Nhập `"  Cat  "` 2. Click `追加` | Modal Tạo đang mở | 1. Tự động trim space đầu/cuối thành `"Cat"` trước khi lưu | Medium | Auto-Data |
| `[AF400-25]` | [3]-[5] Modal Tạo mới (`カテゴリを追加します`) | Trùng tên category đã tồn tại (`[Q&A #1]`) | 1. Nhập tên trùng với category đang có 2. Click `追加` | Đã có category cùng tên | 1. Xử lý/báo lỗi trùng tên theo quy định `[Q&A #1]` | Medium | Auto-Data |
| `[AF400-26]` | [3]-[5] Modal Tạo mới (`カテゴリを追加します`) | Debounce nút `追加` (`CMR15`) | 1. Nhập tên hợp lệ 2. Double-click nhanh vào nút `追加` | Modal Tạo đang mở | 1. Disable nút khi đang gửi request, chỉ gọi API `POST /gift/category/` đúng 1 lần | Medium | Auto-API |
| `[AF400-27]` | [3]-[5] Modal Tạo mới (`カテゴリを追加します`) | Bảo mật XSS (`<script>alert(1)</script>`) | 1. Nhập `<script>alert(1)</script>` 2. Click `追加` | Modal Tạo đang mở | 1. Chuỗi được escape an toàn khi hiển thị trên bảng, không thực thi script | Medium | Auto-API |
| `[AF400-28]` | [3]-[5] Modal Tạo mới (`カテゴリを追加します`) | Hủy tạo mới (`CMR07`) | 1. Nhập tên mới 2. Đóng modal (nút Close/Cancel) không bấm `追加` | Modal Tạo đang mở | 1. Đóng modal, không tạo category mới | Medium | Auto-UI |
| `[AF400-29]` | [10]-[12] Modal Sửa (`カテゴリを編集します`) | Sửa tên hợp lệ (<= 20 ký tự) -> Click `保存` | 1. Đổi tên mới <= 20 ký tự 2. Click `保存` | Modal Sửa đang mở | 1. Đóng modal, tên mới cập nhật trên AF400, AF100, AF200 và App `I600` | High | Auto-UI |
| `[AF400-30]` | [10]-[12] Modal Sửa (`カテゴリを編集します`) | Xóa trắng tên category khi sửa | 1. Xóa trắng ô tên 2. Click `保存` | Modal Sửa đang mở | 1. Báo lỗi `CMMSG29`, không cho lưu | High | Auto-Data |
| `[AF400-31]` | [10]-[12] Modal Sửa (`カテゴリを編集します`) | Nhập 21 ký tự khi sửa | 1. Nhập 21 ký tự 2. Click `保存` | Modal Sửa đang mở | 1. Chặn hoặc báo lỗi `CMMSG49` (`20文字以内で入力してください。`) | High | Auto-Data |
| `[AF400-32]` | [10]-[12] Modal Sửa (`カテゴリを編集します`) | Hủy sửa (`CMR07`) | 1. Sửa tên trong ô nhập 2. Đóng modal không bấm `保存` | Modal Sửa đang mở | 1. Đóng modal, giữ nguyên tên category cũ | Medium | Auto-UI |
| `[AF400-33]` | [-] Visual | Text overflow (`CMR48`) tên 20 ký tự | 1. Tạo category dài 20 ký tự chữ hoa/chữ Nhật 2. Quan sát ô bảng | Có category 20 ký tự | 1. Hiển thị đầy đủ hoặc cắt `…` kèm tooltip, không tràn sang cột khác | Low | Manual-Only (Visual) |
| `[AF400-34]` | [-] Visual | Responsive màn hình 1024px | 1. Thu hẹp viewport về 1024px 2. Quan sát bảng và modal | - | 1. Layout bảng và modal không vỡ, các nút thao tác không bị che khuất | Low | Manual-Only (Visual) |
| `[AF400-35]` | [-] RBAC Visual | Role chỉ xem (Read-only) | 1. Đăng nhập tài khoản chỉ có quyền xem 2. Mở AF400 | Role Read-only | 1. Ẩn hoặc khóa các nút Tạo (`新規登録`), Sửa, Xóa và icon kéo thả 6 dots | High | Manual-Only (Visual) |

*(Tổng 35 kịch bản atomic chuẩn Spec `AF400` — đã tách riêng từng điều kiện biên, từng mã lỗi `CMMSG`, Infinite Scroll, Drag & Drop 6 dots, Tabable Edit, Max 20 chars và logic xóa chuyển gift về `未設定`)*

---

## THỐNG KÊ AUTOMATION FEASIBILITY (AF400)

| Nhóm | Số lượng | Tỷ lệ |
|---| :---: | :---: |
| `Auto-UI` | 16 | 45.7% |
| `Auto-API` | 6 | 17.1% |
| `Auto-Data` | 8 | 22.9% |
| `Manual-Only` (Visual / Complex DB / UX) | 5 | 14.3% |
| **Tổng cộng** | **35** | **~85.7% Auto / ~14.3% Manual** ✅ |
