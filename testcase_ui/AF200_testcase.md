# BẢNG ĐẶC TẢ KIỂM THỬ GIAO DIỆN THỦ CÔNG (MANUAL UI TEST SUITE)
## Màn hình: AF200 — Gift Manage: Gift Create (Tạo mới Quà tặng)
### Phân hệ: Master Admin Web / Quản lý Quà tặng (`AF` Module)
### Áp dụng: Quy chuẩn Trụ cột 2 (`Universal_Rules/02_manual_ui_test_case_rule.md`) & Thư viện `UI_controls/`

---

## BẢNG ĐIỀU KHIỂN TIẾN ĐỘ & THỐNG KÊ (DASHBOARD HEADER)

| Thuộc tính | Giá trị | Thuộc tính | Giá trị | Round 1 Metric | Kết quả | Round 2 Metric | Kết quả |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Module Code** | `AF200` | **Environment** | `Dev-Admin` / `STG-Admin` | **Pass** | 0 | **Pass** | 0 |
| **Total Testcases** | **58** | **% Executed** | 0% | **Fail** | 0 | **Fail** | 0 |
| **Plan to Execute** | **58** | **Creator** | `QA` | **Impact** | 0 | **Impact** | 0 |
| **Spec Source** | `FEATURE_SPEC_MAP` / Figma | **Liên kết chéo** | `AF100`, `AF400`, `I600` | **Not Run** | 58 | **Not Run** | 0 |
| | | | | **Total** | 58 | **Total** | 0 |

---

## CHI TIẾT BẢNG TEST CASES (8 CỘT CHUẨN MARKDOWN)

| ID | Title | Big item | Steps | Pre-condition | Expected | Priority | Automation Feasibility |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| | **I. COMMON & NAVIGATION** | | | | | | |
| `[AF200-1]` | [0] Kiểm tra truy cập màn hình | Điều hướng từ AF100 | 1. Đăng nhập Admin 2. Tại AF100 click nút [新規登録] | User là Master Admin | 1. Điều hướng sang màn AF200 (`/admin/gifts/create`) 2. Form tạo mới hiển thị rỗng với giá trị mặc định | High | Auto-UI |
| `[AF200-2]` | [0] Kiểm tra truy cập màn hình | Truy cập trực tiếp URL (Inbound) | 1. Truy cập trực tiếp URL `/admin/gifts/create` | User là Master Admin | 1. Màn hình AF200 tải thành công 2. Dropdown Category nạp đầy đủ danh sách từ `AF400` | High | Auto-UI |
| `[AF200-3]` | [0] Kiểm tra truy cập màn hình | Phân quyền RBAC | 1. Đăng nhập tài khoản Read-only / Agency 2. Truy cập `/admin/gifts/create` | Tài khoản không có quyền tạo | 1. Chặn truy cập, hiển thị CMMSG5: `この操作を行う権限がありません。` hoặc redirect | High | Auto-API |
| `[AF200-4]` | [0] Kiểm tra truy cập màn hình | Autofocus ô đầu tiên (CMR09) | 1. Mở màn hình AF200 2. Quan sát vị trí con trỏ | - | 1. Con trỏ tự động focus vào ô nhập liệu đầu tiên (Tên quà) theo CMR09 | Low | Auto-UI |
| `[AF200-5]` | [0] Kiểm tra truy cập màn hình | F5 Reload trang | 1. Nhập dở dữ liệu vào form 2. Nhấn F5 | - | 1. Trình duyệt reload lại trang AF200 trạng thái trắng sạch ban đầu, không lỗi | Medium | Auto-UI |
| `[AF200-6]` | [1] Breadcrumbs | Check hiển thị & điều hướng | 1. Quan sát Breadcrumb trên AF200 2. Click node 'ギフト一覧' | - | 1. Hiển thị `＞ ギフト管理 ＞ ギフト一覧 ＞ 新規登録` 2. Click 'ギフト一覧' quay về AF100 | Medium | Auto-UI |
| | **II. MAIN SCREEN CONTROLS** | | | | | | |
| `[AF200-7]` | [2] Textbox Tên quà (Gift Name) | Nhập chữ tiếng Nhật & Latin | 1. Click ô Tên quà 2. Nhập 'スターギフト' và 'Star Gift' | - | 1. Cho phép nhập đầy đủ ký tự tiếng Nhật và Latin | High | Auto-UI |
| `[AF200-8]` | [2] Textbox Tên quà (Gift Name) | Nhập số & ký tự đặc biệt | 1. Nhập 'Gift 2026 #1!' vào ô Tên quà | - | 1. Cho phép nhập bình thường | Medium | Auto-Data |
| `[AF200-9]` | [2] Textbox Tên quà (Gift Name) | Nhập khoảng trắng đầu/cuối | 1. Nhập `  Star Gift  ` 2. Điền đủ các trường khác và Lưu | - | 1. Hệ thống tự động trim khoảng trắng đầu/cuối, lưu với tên `Star Gift` | Medium | Auto-Data |
| `[AF200-10]` | [2] Textbox Tên quà (Gift Name) | Nhập toàn khoảng trắng | 1. Nhập `     ` vào ô Tên quà 2. Click Lưu | - | 1. Coi như rỗng, báo lỗi CMMSG29: `{Gift Name}は空欄にできません。` | High | Auto-Data |
| `[AF200-11]` | [2] Textbox Tên quà (Gift Name) | Bỏ trống trường bắt buộc | 1. Để trống ô Tên quà 2. Click Lưu | - | 1. Báo lỗi CMMSG29: `{Gift Name}は空欄にできません。`, không gọi API | High | Auto-UI |
| `[AF200-12]` | [2] Textbox Tên quà (Gift Name) | Độ dài tối đa (Max length) | 1. Nhập chuỗi đúng bằng max ký tự (VD: 50 hoặc 255 ký tự theo Spec) | - | 1. Cho phép nhập và lưu thành công | Medium | Auto-Data |
| `[AF200-13]` | [2] Textbox Tên quà (Gift Name) | Vượt quá max length | 1. Nhập hoặc paste chuỗi `max + 1` ký tự | - | 1. UI block ký tự thứ `max + 1` HOẶC báo lỗi CMMSG49: `{Field}は文字数が多すぎます。{max}文字以内で入力してください。` | Medium | Auto-Data |
| `[AF200-14]` | [2] Textbox Tên quà (Gift Name) | Paste dữ liệu & XSS script | 1. Paste chuỗi `<script>alert(1)</script>` vào ô Tên quà 2. Lưu | - | 1. Chuỗi được escape an toàn hoặc từ chối, không thực thi JS khi hiển thị ở AF100 | High | Auto-API |
| `[AF200-15]` | [3] Textbox Giá Coin (Coin Price) | Nhập giá nguyên dương hợp lệ | 1. Nhập `100` vào ô Giá Coin | - | 1. Cho phép nhập, hiển thị `100` | High | Auto-UI |
| `[AF200-16]` | [3] Textbox Giá Coin (Coin Price) | Nhập giá = 1 (Min boundary) | 1. Nhập `1` vào ô Giá Coin | - | 1. Hợp lệ, cho phép lưu | High | Auto-Data |
| `[AF200-17]` | [3] Textbox Giá Coin (Coin Price) | Nhập giá = 0 | 1. Nhập `0` vào ô Giá Coin 2. Click Lưu | - | 1. Từ chối báo lỗi phải > 0 (hoặc cho phép nếu Spec hỗ trợ quà 0 coin) `[Pending Q&A #1]` | High | Manual-Only (Complex DB) |
| `[AF200-18]` | [3] Textbox Giá Coin (Coin Price) | Nhập số âm (`-10`) | 1. Nhập `-10` vào ô Giá Coin | - | 1. UI chặn ký tự `-` (CMR04) hoặc báo lỗi validation | High | Auto-Data |
| `[AF200-19]` | [3] Textbox Giá Coin (Coin Price) | Nhập số thập phân (`10.5`) | 1. Nhập `10.5` vào ô Giá Coin | - | 1. UI chặn dấu `.` hoặc báo lỗi chỉ nhập số nguyên | High | Auto-Data |
| `[AF200-20]` | [3] Textbox Giá Coin (Coin Price) | Nhập chữ / ký tự đặc biệt | 1. Nhập `abc@#` vào ô Giá Coin | - | 1. UI block (CMR04) hoặc báo CMMSG54: `半角数字のみ入力してください。` | High | Auto-Data |
| `[AF200-21]` | [3] Textbox Giá Coin (Coin Price) | Paste chữ vào ô số | 1. Copy `"100abc"` và paste vào ô Giá Coin 2. Click Lưu | - | 1. Lọc bỏ chữ hoặc báo lỗi CMMSG54 | Medium | Auto-Data |
| `[AF200-22]` | [3] Textbox Giá Coin (Coin Price) | Nhập số `0` ở đầu (`0100`) | 1. Nhập `0100` 2. Lưu và kiểm tra ở AF100 | - | 1. Lưu thành công với giá trị số `100` | Low | Auto-Data |
| `[AF200-23]` | [3] Textbox Giá Coin (Coin Price) | Bỏ trống giá coin (bắt buộc) | 1. Để trống ô Giá Coin 2. Click Lưu | - | 1. Báo lỗi CMMSG29: `{Coin Price}は空欄にできません。` | High | Auto-UI |
| `[AF200-24]` | [4] Dropdown Danh mục (Category) | Hiển thị mặc định & mở danh sách | 1. Quan sát dropdown Category 2. Click mở dropdown | Có danh mục từ `AF400` | 1. Hiển thị placeholder "Chọn danh mục" và mũi tên xổ xuống; mở ra đủ options từ `AF400` | High | Auto-UI |
| `[AF200-25]` | [4] Dropdown Danh mục (Category) | Chọn từng option danh mục | 1. Lần lượt click chọn từng danh mục trong danh sách | - | 1. Dropdown đóng lại, ô nhận đúng giá trị danh mục đã chọn | High | Auto-UI |
| `[AF200-26]` | [4] Dropdown Danh mục (Category) | Click ra ngoài dropdown | 1. Mở dropdown 2. Click ra ngoài vùng dropdown | - | 1. Dropdown tự đóng lại, giữ nguyên giá trị trước đó | Low | Auto-UI |
| `[AF200-27]` | [4] Dropdown Danh mục (Category) | Bỏ trống danh mục (bắt buộc) | 1. Không chọn Category 2. Click Lưu | - | 1. Báo lỗi CMMSG29: `{Category}は空欄にできません。` | High | Auto-UI |
| `[AF200-28]` | [5] Textbox Thứ tự (Sort Order) | Nhập thứ tự hợp lệ | 1. Nhập `5` vào ô Sort Order | - | 1. Cho phép nhập số nguyên dương | Medium | Auto-UI |
| `[AF200-29]` | [5] Textbox Thứ tự (Sort Order) | Nhập số âm / chữ | 1. Nhập `-1` hoặc `abc` | - | 1. Chặn nhập hoặc báo lỗi CMMSG54 | Medium | Auto-Data |
| `[AF200-30]` | [5] Textbox Thứ tự (Sort Order) | Nhập trùng sort_order đã có | 1. Nhập sort_order trùng với quà khác 2. Click Lưu | Có quà đang có sort_order = 1 | 1. Cho phép lưu (sắp xếp phụ theo ID/created_at) HOẶC báo lỗi trùng `[Pending Q&A #2]` | Medium | Manual-Only (Complex DB) |
| `[AF200-31]` | [6] Toggle / Radio Trạng thái | Trạng thái mặc định & chuyển đổi | 1. Quan sát trạng thái mặc định ON/OFF 2. Click chuyển ON <-> OFF | - | 1. Hiển thị đúng mặc định Spec, chuyển trạng thái mượt mà | Medium | Auto-UI |
| `[AF200-32]` | [7] Upload Icon / Thumbnail | Giao diện nút Upload & Drag-Drop | 1. Quan sát vùng upload Icon 2. Kéo file di chuột vào vùng thả | - | 1. Hiển thị ghi chú định dạng (.PNG/.JPG) & dung lượng tối đa; drag-over đổi màu viền | Medium | Manual-Only (Visual) |
| `[AF200-33]` | [7] Upload Icon / Thumbnail | Upload file hợp lệ bằng Click | 1. Click nút Upload -> chọn file `gift_icon.png` hợp lệ | Có file trong `test_files/` | 1. Hiển thị progress bar, tải thành công (CMMSG15), hiển thị ảnh preview thumbnail và nút Xóa | High | Auto-UI |
| `[AF200-34]` | [7] Upload Icon / Thumbnail | Upload file hợp lệ bằng Drag & Drop | 1. Kéo thả file `gift_icon.png` vào vùng upload | - | 1. Tải thành công và hiển thị ảnh preview tương tự Click | Medium | Auto-UI |
| `[AF200-35]` | [7] Upload Icon / Thumbnail | Xóa file & tải lại chính file đó | 1. Click icon (X) xóa file vừa chọn 2. Chọn lại chính file `gift_icon.png` | Đã upload `gift_icon.png` | 1. Ảnh bị gỡ ở B1; B2 vẫn trigger `onChange` và upload lại thành công | Medium | Auto-UI |
| `[AF200-36]` | [7] Upload Icon / Thumbnail | Mở hộp thoại chọn file rồi bấm Cancel | 1. Đã có sẵn ảnh preview 2. Click Upload -> bấm Cancel trên OS Dialog | Đã có sẵn 1 ảnh | 1. Giữ nguyên ảnh cũ, không mất dữ liệu và không báo lỗi | Low | Manual-Only (UX) |
| `[AF200-37]` | [7] Upload Icon / Thumbnail | Biên dung lượng (0 Byte, Max Size, > Max Size) | 1. Upload file 0 Byte 2. Upload file đúng Max Size 3. Upload file > Max Size | - | 1. 0 Byte: từ chối báo lỗi 2. Max Size: thành công 3. > Max Size: chặn & báo CMMSG45 | High | Auto-UI |
| `[AF200-38]` | [7] Upload Icon / Thumbnail | Sai định dạng (.txt, .pdf, .exe) | 1. Upload file `.txt` hoặc `.exe` | - | 1. Chặn và báo lỗi CMMSG43 / CMMSG44 (sai định dạng ảnh/file) | High | Auto-UI |
| `[AF200-39]` | [7] Upload Icon / Thumbnail | Giả mạo đuôi file (Extension Spoofing) | 1. Đổi tên `test.exe` thành `fake.png` rồi upload | - | 1. Hệ thống kiểm tra Magic Bytes / MIME thực tế và từ chối upload | High | Auto-API |
| `[AF200-40]` | [7] Upload Icon / Thumbnail | Không upload Icon khi tạo mới | 1. Điền các trường text, bỏ trống Icon 2. Click Lưu | - | 1. Báo lỗi yêu cầu upload Icon (nếu bắt buộc theo Spec) `[Pending Q&A #3]` | High | Manual-Only (Complex DB) |
| `[AF200-41]` | [8] Upload Animation Asset | Upload file animation hợp lệ (GIF/Lottie) | 1. Click upload file `.gif` hoặc `.json` (Lottie) hợp lệ | Có file animation hợp lệ | 1. Upload thành công, preview animation chạy mượt mà | High | Manual-Only (Visual) |
| `[AF200-42]` | [8] Upload Animation Asset | Upload sai định dạng (.mp4, .avi) | 1. Upload file `.mp4` vào ô Animation | - | 1. Báo lỗi CMMSG43 / CMMSG44 | High | Auto-UI |
| `[AF200-43]` | [8] Upload Animation Asset | Upload quá dung lượng tối đa | 1. Upload file animation > Max Size | - | 1. Báo lỗi CMMSG45 | High | Auto-UI |
| `[AF200-44]` | [8] Upload Animation Asset | Hủy upload giữa chừng / mất mạng | 1. Đang upload file lớn (Slow 3G) -> ngắt mạng hoặc bấm Cancel | - | 1. Dừng upload, báo lỗi kết nối CMMSG8 và cho phép thử lại | Medium | Manual-Only (UX) |
| `[AF200-45]` | [9] Button Lưu (Save / Submit) | Validate toàn bộ form khi để trống | 1. Để trống tất cả trường bắt buộc 2. Click [保存 / 登録] | - | 1. Hiển thị đồng thời tất cả thông báo lỗi CMMSG29 dưới từng trường, không gọi API | High | Auto-UI |
| `[AF200-46]` | [9] Button Lưu (Save / Submit) | Lưu thành công với đầy đủ dữ liệu hợp lệ | 1. Nhập Tên, Coin, chọn Category, Sort order, Upload Icon & Animation 2. Click Lưu | - | 1. Hiển thị Loading CMMSG27 2. Báo thành công CMMSG12/CMMSG17: `正常に保存されました。` 3. Quay về AF100 thấy quà mới 4. DB `gifts` INSERT bản ghi mới | High | Auto-UI |
| `[AF200-47]` | [9] Button Lưu (Save / Submit) | Đồng bộ quà mới sang App I600 | 1. Tạo quà với trạng thái ON ở B46 2. Mở App Viewer màn I600 | Có phòng Live đang chạy | 1. Quà vừa tạo hiển thị đúng Icon, Tên, Giá Coin trên danh sách quà App `I600` | High | Manual-Only (Complex DB) |
| `[AF200-48]` | [9] Button Lưu (Save / Submit) | Debounce chống double-click (CMR15) | 1. Điền đủ dữ liệu hợp lệ 2. Double-click nút Lưu liên tiếp | - | 1. Nút disabled trong khi xử lý (CMR15), chỉ gọi API 1 lần, DB chỉ có 1 bản ghi | High | Auto-UI |
| `[AF200-49]` | [10] Button Hủy / Quay lại (Cancel - CMR07) | Hủy khi chưa nhập gì | 1. Mở AF200, không sửa đổi gì 2. Click [キャンセル / 戻る] | - | 1. Điều hướng quay về AF100 ngay lập tức, không hiện popup cảnh báo | Medium | Auto-UI |
| `[AF200-50]` | [10] Button Hủy / Quay lại (Cancel - CMR07) | Hủy khi đã nhập dữ liệu | 1. Nhập Tên quà "Test" 2. Click [キャンセル / 戻る] | - | 1. Hiển thị popup xác nhận CMMSG46 (MSG2): `戻ってもよろしいですか？保存されていない変更は失われます。` | High | Auto-UI |
| `[AF200-51]` | [11] Error Handling | Mất kết nối mạng khi bấm Lưu | 1. Điền đủ form 2. Ngắt mạng 3. Click Lưu | - | 1. Hiển thị CMMSG8: `ネットワークエラー。接続を確認してください。`, giữ nguyên dữ liệu đã nhập trên form | Medium | Manual-Only (UX) |
| `[AF200-52]` | [11] Error Handling | Lỗi server 500 khi bấm Lưu | 1. Giả lập API `POST /gifts` trả về 500 2. Click Lưu | - | 1. Hiển thị CMMSG1: `予期しないサーバーエラーが発生しました。` kèm nút thử lại | Medium | Auto-API |
| `[AF200-53]` | [11] Error Handling | Hết phiên đăng nhập khi bấm Lưu | 1. Token hết hạn 2. Click Lưu | - | 1. Hiển thị CMMSG10 / CMMSG4 và redirect về màn Login | High | Auto-API |
| | **III. SUB-LAYOUTS / MODALS** | | | | | | |
| `[AF200-54]` | [12] Modal Xác nhận thoát chưa lưu | Click [キャンセル] trên Modal | 1. Trigger modal ở `[AF200-50]` 2. Click [キャンセル] hoặc icon (X) | Modal CMMSG46 đang mở | 1. Đóng modal, ở lại màn hình AF200 và giữ nguyên toàn bộ dữ liệu đã nhập | High | Auto-UI |
| `[AF200-55]` | [12] Modal Xác nhận thoát chưa lưu | Click [OK] trên Modal | 1. Trigger modal ở `[AF200-50]` 2. Click [OK] | Modal CMMSG46 đang mở | 1. Đóng modal, quay về AF100, không lưu dữ liệu mới | High | Auto-UI |
| `[AF200-56]` | [12] Preview Media | Xem trước Icon / Animation | 1. Sau khi upload Icon & Animation, quan sát khung Preview | Đã upload file hợp lệ | 1. Icon hiển thị đúng tỷ lệ, không méo; Animation phát đúng khung hình | Medium | Manual-Only (Visual) |
| `[AF200-57]` | [12] Layout Responsive | Thu nhỏ màn hình | 1. Resize cửa sổ trình duyệt về độ phân giải 1024px | - | 1. Các ô nhập liệu và nút Lưu/Hủy không bị tràn hay chồng chéo | Low | Manual-Only (Visual) |
| `[AF200-58]` | [12] Keyboard Navigation | Tab order trên Form | 1. Nhấn `Tab` liên tục qua các trường trên form AF200 | - | 1. Thứ tự focus đi tuần tự từ trên xuống dưới, từ trái sang phải hợp lý | Low | Manual-Only (UX) |

---

## THỐNG KÊ AUTOMATION FEASIBILITY (AF200)

| Nhóm | Số lượng | Tỷ lệ |
|---| :---: | :---: |
| `Auto-UI` | 29 | 50.0% |
| `Auto-API` | 5 | 8.6% |
| `Auto-Data` | 11 | 19.0% |
| `Manual-Only` (Visual / Complex DB / UX) | 13 | 22.4% |
| **Tổng cộng** | **58** | **~77.6% Auto / ~22.4% Manual** ✅ |
