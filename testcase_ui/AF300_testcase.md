# BẢNG ĐẶC TẢ KIỂM THỬ GIAO DIỆN THỦ CÔNG (MANUAL UI TEST SUITE)
## Màn hình: AF300 — Gift Manage: Gift Update / Delete (ギフト更新・削除)
### Phân hệ: Master Admin Web / 商品管理 (`AF` Module)
### Nguồn Spec: Google Sheet `AF300` (gid=`213255523`) + `AF500` (gid=`1458098150`) + `CMR50`
### Áp dụng: `Universal_Rules/02_manual_ui_test_case_rule.md` & `UI_controls/`

---

## BẢNG ĐIỀU KHIỂN TIẾN ĐỘ & THỐNG KÊ (DASHBOARD HEADER)

| Thuộc tính | Giá trị | Thuộc tính | Giá trị | Round 1 Metric | Kết quả | Round 2 Metric | Kết quả |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Module Code** | `AF300` | **Environment** | `Dev-Admin` / `STG-Admin` | **Pass** | 0 | **Pass** | 0 |
| **Total Testcases** | **68** | **% Executed** | 0% | **Fail** | 0 | **Fail** | 0 |
| **Plan to Execute** | **68** | **Creator** | `QA` | **Impact** | 0 | **Impact** | 0 |
| **Spec Source** | Google Sheet `AF300` + `AF500` | **Liên kết chéo** | `AF100`, `I600`, `I601`, `AE400` | **Not Run** | 68 | **Not Run** | 0 |
| | | | | **Total** | 68 | **Total** | 0 |

---

## CHI TIẾT BẢNG TEST CASES (8 CỘT CHUẨN MARKDOWN)

| ID | Title | Big item | Steps | Pre-condition | Expected | Priority | Automation Feasibility |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| | **I. COMMON & NAVIGATION** | | | | | | |
| `[AF300-1]` | [0] Kiểm tra truy cập màn hình | Sidebar UI & Điều hướng từ AF100 | 1. Tại AF100 click nút Edit `[13]` trên 1 gift 2. Quan sát Sidebar & Tab title | Có gift trong DB | 1. Sidebar `ギフト一覧` highlight; Tab title `商品管理｜ギフト管理`; Title `ギフト更新` | High | Auto-UI |
| `[AF300-2]` | [0] Kiểm tra truy cập màn hình | Inbound Deep-link — ID không tồn tại | 1. Mở URL `/admin/gifts/999999` | - | 1. Hiển thị CMMSG3 / 404 thân thiện hoặc redirect về AF100 | High | Auto-API |
| `[AF300-3]` | [0] Kiểm tra truy cập màn hình | Inbound Deep-link — ID sai định dạng (`abc`) | 1. Mở URL `/admin/gifts/abc` | - | 1. Xử lý an toàn (400/404), không crash trắng trang | Medium | Auto-API |
| `[AF300-4]` | [0] Kiểm tra truy cập màn hình | Phân quyền RBAC | 1. Đăng nhập tài khoản không có quyền 2. Truy cập AF300 | Role không có quyền | 1. Báo CMMSG5: `この操作を行う権限がありません。` | High | Auto-API |
| `[AF300-5]` | [0] Kiểm tra truy cập màn hình | F5 Reload giữ nguyên dữ liệu | 1. Mở AF300 của 1 gift 2. Nhấn F5 | - | 1. Tải lại đúng dữ liệu chi tiết của gift đó, không lỗi 500 | Medium | Auto-UI |
| `[AF300-6]` | [0] Breadcrumbs | Hiển thị & click Breadcrumb | 1. Quan sát Breadcrumb `ホーム＞ギフト管理＞ギフト更新` 2. Click `ギフト管理` | - | 1. Hiển thị đúng Breadcrumb; click `ギフト管理` quay về AF100 | Medium | Auto-UI |
| | **II. MAIN SCREEN CONTROLS** | | | | | | |
| `[AF300-7]` | [Init] Pre-fill dữ liệu chi tiết | Mapping toàn bộ trường từ `GET /gift/{gift_id}/` | 1. Mở AF300 2. Đối chiếu mọi field với DB | Có gift mẫu | 1. `animation_type`, `name`, tên file `icon` & `image`, `status`, `sort_order`, `price`, `category_id` khớp DB 100% | High | Auto-UI |
| `[AF300-8]` | [1-AF500] Radio `演出種類` (`animation_type`) | Chuyển sang `シャッター演出` | 1. Chọn radio `シャッター演出` | - | 1. Giá chỉ chọn `5,000` hoặc `10,000`, disable Category & `ギフトコンテンツ` (`[Q&A AF300 #1]`) | High | Auto-UI |
| `[AF300-9]` | [1-AF500] Radio `演出種類` (`animation_type`) | Chuyển sang `継続演出` | 1. Chọn radio `継続演出` | - | 1. Giá chỉ chọn `1000pt..10,000pt`, disable Category & `ギフトコンテンツ` (`[Q&A AF300 #1]`) | High | Auto-UI |
| `[AF300-10]` | [1][2] Textbox `ギフト名` (`name`) | Label, dấu `*` & Placeholder | 1. Quan sát ô `ギフト名` -> Hover, Focus, Blur | - | 1. Label `ギフト名`, dấu `*`, placeholder `ギフト名を入力してください` | Medium | Manual-Only (Visual) |
| `[AF300-11]` | [1][2] Textbox `ギフト名` (`name`) | Sửa tên hợp lệ (Nhật/Latin <= 10 ký tự) & Lưu | 1. Đổi tên thành `新ギフト10` 2. Click `保存` | - | 1. Báo `CMMSG13`; AF100 & DB cập nhật tên mới | High | Auto-UI |
| `[AF300-12]` | [1][2] Textbox `ギフト名` (`name`) | Biên đúng Max = 10 ký tự | 1. Nhập chuỗi đúng 10 ký tự 2. Click `保存` | - | 1. Cho phép nhập đủ 10 ký tự và lưu thành công | High | Auto-Data |
| `[AF300-13]` | [1][2] Textbox `ギフト名` (`name`) | Biên vượt Max = 11 ký tự (`CMMSG49`) | 1. Nhập hoặc paste 11 ký tự 2. Click `保存` | - | 1. Chặn ký tự 11 hoặc báo `CMMSG49` (`10文字以内で入力してください。`) | High | Auto-Data |
| `[AF300-14]` | [1][2] Textbox `ギフト名` (`name`) | Space đầu/cuối (`  Star  `) | 1. Nhập `  Star  ` 2. Click `保存` | - | 1. Tự động trim space đầu/cuối thành `Star` | Medium | Auto-Data |
| `[AF300-15]` | [1][2] Textbox `ギフト名` (`name`) | Nhập toàn khoảng trắng (`"   "`) | 1. Nhập `"   "` 2. Click `保存` | - | 1. Báo lỗi `CMMSG29`, không cho lưu | High | Auto-Data |
| `[AF300-16]` | [1][2] Textbox `ギフト名` (`name`) | Xóa trắng tên (Required) | 1. Xóa trắng ô `ギフト名` 2. Click `保存` | - | 1. Báo lỗi CMMSG29: `ギフト名は空欄にできません。` | High | Auto-UI |
| `[AF300-17]` | [1][2] Textbox `ギフト名` (`name`) | Paste XSS (`<img src=x onerror=alert(1)>`) | 1. Paste `<img src=x onerror=alert(1)>` -> `保存` | - | 1. Escape an toàn hoặc từ chối, không thực thi JS | High | Auto-API |
| `[AF300-18]` | [3][4] Upload `ギフトアイコン` (`icon` - `CMR50`) | Preview Modal & nút `閉じる` | 1. Click tên file icon 2. Click `閉じる` | Gift đã có icon | 1. Modal preview ảnh rõ nét; click `閉じる` đóng modal | High | Auto-UI |
| `[AF300-19]` | [3][4] Upload `ギフトアイコン` (`icon` - `CMR50`) | Nút `変更` đổi sang `.png` mới | 1. Click `変更` chọn `.png` mới | Gift đã có icon | 1. Đổi tên file mới; chỉ lưu lên server khi bấm `保存` | High | Auto-UI |
| `[AF300-20]` | [3][4] Upload `ギフトアイコン` (`icon` - `CMR50`) | Nút `削除` xóa & upload lại file cũ | 1. Click `削除` 2. Upload lại chính file cũ | Gift đã có icon | 1. `削除` reset UI upload; upload lại cùng file vẫn nhận bình thường | High | Auto-UI |
| `[AF300-21]` | [3][4] Upload `ギフトアイコン` (`icon` - `CMR50`) | Giữ nguyên Icon cũ khi chỉ sửa text | 1. Chỉ sửa tên quà -> bấm `保存` | - | 1. Icon cũ được giữ nguyên trong DB | High | Auto-UI |
| `[AF300-22]` | [3][4] Upload `ギフトアイコン` (`icon` - `CMR50`) | File rỗng 0 Byte | 1. Click `変更` -> upload file `empty.png` (0 Byte) | - | 1. Chặn và báo lỗi file không hợp lệ | High | Auto-UI |
| `[AF300-23]` | [3][4] Upload `ギフトアイコン` (`icon` - `CMR50`) | Biên đúng 5MB | 1. Click `変更` -> upload file đúng 5MB | - | 1. Upload thành công, hiển thị tên file | High | Auto-UI |
| `[AF300-24]` | [3][4] Upload `ギフトアイコン` (`icon` - `CMR50`) | Biên vượt 5MB (5.1MB) (`CMMSG45`) | 1. Click `変更` -> upload file 5.1MB | - | 1. Chặn và báo lỗi `CMMSG45` | High | Auto-UI |
| `[AF300-25]` | [3][4] Upload `ギフトアイコン` (`icon` - `CMR50`) | Sai định dạng (`.txt`, `.exe`) (`CMMSG44`) | 1. Upload file `.txt` vào ô icon | - | 1. FE/BE chặn và báo `CMMSG44` | High | Auto-UI |
| `[AF300-26]` | [3][4] Upload `ギフトアイコン` (`icon` - `CMR50`) | Giả mạo Magic Bytes (`malware.exe` -> `.png`) | 1. Đổi đuôi file `.exe` thành `.png` rồi upload | - | 1. Backend kiểm tra Magic Bytes chặn và báo `CMMSG44` | High | Auto-API |
| `[AF300-27]` | [5][6] Upload `ギフトコンテンツ` (`image` - `CMR50`) | Hint text & Preview Modal | 1. Quan sát hint text 2. Click tên file mở preview `image` | Đang chọn `通常演出` | 1. Hint text chuẩn Spec; Modal preview phát đúng ảnh/animation | High | Auto-UI |
| `[AF300-28]` | [5][6] Upload `ギフトコンテンツ` (`image` - `CMR50`) | Nút `変更` đổi sang `.gif`/Lottie mới <= 5MB | 1. Click `変更` chọn file `.gif`/Lottie mới <= 5MB | Đang chọn `通常演出` | 1. Cập nhật file mới thành công | High | Auto-UI |
| `[AF300-29]` | [5][6] Upload `ギフトコンテンツ` (`image` - `CMR50`) | Nút `削除` xóa & upload lại file cũ | 1. Click `削除` 2. Upload lại chính file cũ | Đang chọn `通常演出` | 1. Reset vùng upload và nhận lại file cũ bình thường | Medium | Auto-UI |
| `[AF300-30]` | [5][6] Upload `ギフトコンテンツ` (`image` - `CMR50`) | Sai format `.jpg`/`.mp4` (`CMMSG43`) | 1. Upload `.mp4` hoặc `.jpg` | Đang chọn `通常演出` | 1. Báo lỗi `CMMSG43` | High | Auto-UI |
| `[AF300-31]` | [5][6] Upload `ギフトコンテンツ` (`image` - `CMR50`) | Quá dung lượng > 5MB (`CMMSG45`) | 1. Upload file > 5MB | Đang chọn `通常演出` | 1. Báo lỗi `CMMSG45` | High | Auto-UI |
| `[AF300-32]` | [5][6] Upload `ギフトコンテンツ` (`image` - `CMR50`) | Cancel OS File Dialog | 1. Click `変更` -> bấm Cancel OS Dialog | Đã có content | 1. Giữ nguyên content cũ, không báo lỗi | Low | Manual-Only (UX) |
| `[AF300-33]` | [5][6] Upload `ギフトコンテンツ` (`image` - `CMR50`) | Giữ nguyên content cũ khi chỉ sửa text | 1. Chỉ sửa tên quà -> bấm `保存` | - | 1. Content cũ giữ nguyên trong DB | High | Auto-UI |
| `[AF300-34]` | [7]-[9] Radio `ステータス` (`status`) | Đổi `公開` <-> `非公開` & Lưu | 1. Chuyển từ `公開` sang `非公開` -> bấm `保存` 2. Kiểm tra App `I600` | Có phòng Live | 1. DB & AF100 đổi thành `非公開`; quà ẩn khỏi App `I600` | High | Manual-Only (Complex DB) |
| `[AF300-35]` | [10][11] Textbox `並び順` (`sort_order`) | Sửa số hợp lệ & số trùng | 1. Đổi `sort_order` hợp lệ -> `保存` | - | 1. Cập nhật thứ tự; nếu trùng ưu tiên theo `id` | High | Auto-UI |
| `[AF300-36]` | [10][11] Textbox `並び順` (`sort_order`) | Nhập số âm (`-1`) | 1. Nhập `-1` vào ô `並び順` | - | 1. Chặn nhập dấu `-` hoặc báo `CMMSG54` | Medium | Auto-Data |
| `[AF300-37]` | [10][11] Textbox `並び順` (`sort_order`) | Nhập số thập phân (`1.5`) | 1. Nhập `1.5` vào ô `並び順` | - | 1. Chặn dấu `.` hoặc báo `CMMSG54` | Medium | Auto-Data |
| `[AF300-38]` | [10][11] Textbox `並び順` (`sort_order`) | Nhập chữ (`abc`) | 1. Nhập `abc` vào ô `並び順` | - | 1. Chặn ký tự chữ hoặc báo `CMMSG54` | Medium | Auto-Data |
| `[AF300-39]` | [10][11] Textbox `並び順` (`sort_order`) | Bỏ trống `並び順` (Required) | 1. Xóa trắng `並び順` 2. Click `保存` | - | 1. Báo lỗi bắt buộc nhập `CMMSG29` | High | Auto-UI |
| `[AF300-40]` | [12][13] Textbox `ギフト値段` (`price`) | Auto-format dấu phẩy 3 số & Sửa giá hợp lệ | 1. Nhập `123456` 2. Bấm `保存` 3. Kiểm tra App `I600` | Đang chọn `通常演出` | 1. Format `123,456`; lưu thành công; App `I600` hiển thị đúng giá mới | High | Auto-UI |
| `[AF300-41]` | [12][13] Textbox `ギフト値段` (`price`) | Giá biên Min = `1` | 1. Nhập `1` -> `保存` | Đang chọn `通常演出` | 1. Lưu thành công với giá trị số `1` | High | Auto-Data |
| `[AF300-42]` | [12][13] Textbox `ギフト値段` (`price`) | Nhập số `0` đầu (`0100`) | 1. Nhập `0100` -> `保存` | Đang chọn `通常演出` | 1. Chuẩn hóa thành `100` khi lưu | Medium | Auto-Data |
| `[AF300-43]` | [12][13] Textbox `ギフト値段` (`price`) | Nhập giá = `0` (`[Q&A AF200 #1]`) | 1. Nhập `0` -> `保存` | Đang chọn `通常演出` | 1. Báo lỗi giá phải >= 1 | High | Manual-Only (Complex DB) |
| `[AF300-44]` | [12][13] Textbox `ギフト値段` (`price`) | Nhập số âm (`-50`) | 1. Nhập `-50` vào ô `ギフト値段` | Đang chọn `通常演出` | 1. UI chặn dấu `-` hoặc báo lỗi chỉ nhập số nguyên dương | High | Auto-Data |
| `[AF300-45]` | [12][13] Textbox `ギフト値段` (`price`) | Nhập số thập phân (`12.5`) | 1. Nhập `12.5` vào ô `ギフト値段` | Đang chọn `通常演出` | 1. UI chặn dấu `.` hoặc báo lỗi chỉ nhập số nguyên | High | Auto-Data |
| `[AF300-46]` | [12][13] Textbox `ギフト値段` (`price`) | Nhập/Paste chữ (`abc`, `100abc`) | 1. Nhập `abc` hoặc paste `100abc` | Đang chọn `通常演出` | 1. Chặn chữ hoặc báo `CMMSG54` | High | Auto-Data |
| `[AF300-47]` | [12][13] Textbox `ギフト値段` (`price`) | Bỏ trống giá (Required) | 1. Xóa trắng ô `ギフト値段` 2. Click `保存` | Đang chọn `通常演出` | 1. Báo lỗi bắt buộc nhập `CMMSG29` | High | Auto-UI |
| `[AF300-48]` | [14][15] Pulldown `ギフトカテゴリ` (`category_id`) | Đổi sang category khác và lưu | 1. Chọn category mới trong pulldown 2. Click `保存` | Có >= 2 category | 1. Lưu thành công, AF100 & DB cập nhật category mới | High | Auto-UI |
| `[AF300-49]` | [14][15] Pulldown `ギフトカテゴリ` (`category_id`) | Bỏ chọn category về `未設定` (Optional) | 1. Bỏ chọn category (`未設定`) 2. Click `保存` | Gift đang có category | 1. Lưu thành công với `category_id = null`; trên `I600` về tab `一般(General)` | High | Auto-UI |
| `[AF300-50]` | [16]-[19] Inline Popover `+` | Validate bỏ trống khi thêm category từ AF300 | 1. Click `+` 2. Để trống tên category 3. Click `追加する` | - | 1. Báo lỗi `CMMSG29` | High | Auto-UI |
| `[AF300-51]` | [16]-[19] Inline Popover `+` | Thêm category nhanh thành công từ AF300 | 1. Click `+` 2. Nhập `NewCat` (<= 20 ký tự) 3. Click `追加する` | - | 1. Gọi `POST /gift/category/`, đóng popover & thêm vào pulldown | High | Auto-UI |
| `[AF300-52]` | [20] Button `キャンセル` (`CMR07`) | Hủy khi chưa sửa gì | 1. Mở AF300 không sửa gì 2. Click `キャンセル` | Form chưa thay đổi | 1. Quay về AF100 ngay lập tức, không hiện popup xác nhận | High | Auto-UI |
| `[AF300-53]` | [20] Button `キャンセル` (`CMR07`) | Hủy khi đã sửa dữ liệu | 1. Sửa tên gift 2. Click `キャンセル` | Form đã thay đổi | 1. Hiển thị popup xác nhận `CMMSG46` | High | Auto-UI |
| `[AF300-54]` | [22] Button `保存` (Save) | Lưu khi không sửa gì | 1. Mở AF300 không sửa gì 2. Click `保存` | - | 1. Lưu thành công (`CMMSG13`), không lỗi | Medium | Auto-UI |
| `[AF300-55]` | [22] Button `保存` (Save) | Debounce `CMR15` & Loading `CMMSG27` | 1. Sửa tên 2. Double-click `保存` | - | 1. Chỉ gọi `PATCH /gift/{id}/` 1 lần, hiển thị loading `CMMSG27` | High | Auto-API |
| `[AF300-56]` | [21] Button `削除` (Delete - `CMR25`) | RBAC nút Xóa với role Read-only | 1. Đăng nhập role Read-only 2. Mở AF300 | Role Read-only | 1. Nút `削除` bị ẩn hoặc disabled | High | Manual-Only (Visual) |
| `[AF300-57]` | [21] Button `削除` (Delete - `CMR25`) | Master Admin click `削除` mở Modal `CMMSG28` | 1. Đăng nhập Master Admin 2. Click nút `削除` | - | 1. Mở popup xác nhận xóa `CMMSG28` | High | Auto-UI |
| `[AF300-58]` | [-] Error Handling | Mất mạng (`CMMSG8`) | 1. Ngắt mạng -> bấm `保存` | - | 1. Hiển thị `CMMSG8: ネットワークエラー。接続を確認してください。` | Medium | Manual-Only (UX) |
| `[AF300-59]` | [-] Error Handling | Lỗi server 500 (`CMMSG1`) | 1. Giả lập API trả 500 -> bấm `保存` | - | 1. Hiển thị `CMMSG1: 予期しないサーバーエラーが発生しました。` | Medium | Auto-API |
| `[AF300-60]` | [-] Error Handling | Hết phiên đăng nhập (`CMMSG10`) | 1. Token hết hạn -> bấm `保存` | - | 1. Hiển thị `CMMSG10` và redirect về trang Login | High | Auto-API |
| | **III. SUB-LAYOUTS / MODALS** | | | | | | |
| `[AF300-61]` | [21-Modal] Modal Xác nhận Xóa | Click `キャンセル` hủy xóa | 1. Mở Modal `CMMSG28` 2. Click `キャンセル` | Modal đang mở | 1. Đóng modal, giữ nguyên gift | High | Auto-UI |
| `[AF300-62]` | [21-Modal] Modal Xác nhận Xóa | Xác nhận xóa -> Ẩn trên App Livestream (`I600`) | 1. Click đồng ý xóa trên Modal 2. Check App `I600` | Gift đang tồn tại | 1. Báo `CMMSG14`, về AF100; Livestream `I600` KHÔNG hiện gift đã xóa | High | Manual-Only (Complex DB) |
| `[AF300-63]` | [21-Modal] Modal Xác nhận Xóa | Gift đã xóa vẫn giữ tại Lịch sử mua gift | 1. Xóa gift từng có user mua 2. Check màn Lịch sử mua gift (`AE400`/`K9091A`) | Gift từng được mua | 1. Màn hình Lịch sử mua VẪN hiển thị đầy đủ gift đã xóa | High | Manual-Only (Complex DB) |
| `[AF300-64]` | [21-Modal] Modal Xác nhận Xóa | Xóa gift đang nằm trong Wishlist (`M1011`/`M20507`) | 1. Xóa gift đang trong Wishlist của Streamer | Gift trong Wishlist | 1. Wishlist tự ẩn/xử lý theo `[Q&A AF300 #2]` | Medium | Manual-Only (Complex DB) |
| `[AF300-65]` | [21-Modal] Modal Xác nhận Xóa | Xóa thất bại (`CMMSG22`) | 1. Giả lập `DELETE /gift/{id}/` trả lỗi 500 | - | 1. Hiển thị thông báo lỗi `CMMSG22`, dữ liệu không mất | Medium | Auto-API |
| `[AF300-66]` | [CMR07-Modal] Modal Thoát chưa lưu | Click `[キャンセル]` trên `CMMSG46` | 1. Mở `CMMSG46` 2. Click `[キャンセル]` | Popup `CMMSG46` đang mở | 1. Ở lại màn AF300, giữ nguyên dữ liệu vừa sửa | High | Auto-UI |
| `[AF300-67]` | [CMR07-Modal] Modal Thoát chưa lưu | Click `[OK]` trên `CMMSG46` | 1. Mở `CMMSG46` 2. Click `[OK]` | Popup `CMMSG46` đang mở | 1. Quay về AF100 và hủy bỏ thay đổi chưa lưu | High | Auto-UI |
| `[AF300-68]` | [-] Layout & Visual | Preview modal `CMR50` & Responsive 1024px | 1. Mở preview modal; resize màn hình 1024px | - | 1. Ảnh/animation rõ nét; layout không vỡ | Low | Manual-Only (Visual) |

---

## THỐNG KÊ AUTOMATION FEASIBILITY (AF300)

| Nhóm | Số lượng | Tỷ lệ |
|---| :---: | :---: |
| `Auto-UI` | 37 | 54.4% |
| `Auto-API` | 9 | 13.2% |
| `Auto-Data` | 12 | 17.6% |
| `Manual-Only` (Visual / Complex DB / UX) | 10 | 14.7% |
| **Tổng cộng** | **68** | **85.3% Auto / 14.7% Manual** ✅ |
