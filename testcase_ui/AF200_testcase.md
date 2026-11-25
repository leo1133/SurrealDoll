# BẢNG ĐẶC TẢ KIỂM THỬ GIAO DIỆN THỦ CÔNG (MANUAL UI TEST SUITE)
## Màn hình: AF200 — Gift Manage: Gift Create (ギフト登録)
### Phân hệ: Master Admin Web / 商品管理 (`AF` Module)
### Nguồn Spec: Google Sheet `AF200` (gid=`2030636358`) + `AF500` (gid=`1458098150`) + `CMR50`
### Áp dụng: `Universal_Rules/02_manual_ui_test_case_rule.md` & `UI_controls/`

---

## BẢNG ĐIỀU KHIỂN TIẾN ĐỘ & THỐNG KÊ (DASHBOARD HEADER)

| Thuộc tính | Giá trị | Thuộc tính | Giá trị | Round 1 Metric | Kết quả | Round 2 Metric | Kết quả |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Module Code** | `AF200` | **Environment** | `Dev-Admin` / `STG-Admin` | **Pass** | 0 | **Pass** | 0 |
| **Total Testcases** | **76** | **% Executed** | 0% | **Fail** | 0 | **Fail** | 0 |
| **Plan to Execute** | **76** | **Creator** | `QA` | **Impact** | 0 | **Impact** | 0 |
| **Spec Source** | Google Sheet `AF200` + `AF500` | **Liên kết chéo** | `AF100`, `AF400`, `I600`, `I601` | **Not Run** | 76 | **Not Run** | 0 |
| | | | | **Total** | 76 | **Total** | 0 |

---

## CHI TIẾT BẢNG TEST CASES (8 CỘT CHUẨN MARKDOWN)

| ID | Title | Big item | Steps | Pre-condition | Expected | Priority | Automation Feasibility |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| | **I. COMMON & NAVIGATION** | | | | | | |
| `[AF200-1]` | [0] Kiểm tra truy cập màn hình | Sidebar UI & Highlight | 1. Đăng nhập Admin 2. Quan sát Sidebar menu | User là Master Admin | 1. Menu `商品管理 > ギフト管理 > ギフト登録` được highlight active | High | Auto-UI |
| `[AF200-2]` | [0] Kiểm tra truy cập màn hình | Điều hướng từ AF100 (`新規登録`) | 1. Tại AF100 click nút `新規登録` | - | 1. Điều hướng sang AF200; Tab title = `商品管理｜ギフト管理`; Title = `ギフト登録` | High | Auto-UI |
| `[AF200-3]` | [0] Kiểm tra truy cập màn hình | Truy cập trực tiếp URL (Inbound) | 1. Truy cập trực tiếp URL AF200 | - | 1. Màn hình AF200 tải thành công; pulldown Category nạp từ `GET /gift/category/` | High | Auto-UI |
| `[AF200-4]` | [0] Kiểm tra truy cập màn hình | Phân quyền RBAC | 1. Đăng nhập tài khoản không có quyền tạo gift 2. Truy cập URL AF200 | Tài khoản không có quyền | 1. Chặn truy cập, báo CMMSG5: `この操作を行う権限がありません。` | High | Auto-API |
| `[AF200-5]` | [0] Kiểm tra truy cập màn hình | Autofocus (`CMR09`) | 1. Mở màn hình AF200 và quan sát vị trí con trỏ | - | 1. Tự động focus vào ô nhập liệu đầu tiên trên form | Medium | Auto-UI |
| `[AF200-6]` | [0] Kiểm tra truy cập màn hình | F5 Reload khi đang nhập dở | 1. Nhập dở dữ liệu vào form 2. Nhấn F5 | - | 1. Trang tải lại sạch sẽ, form reset về trạng thái mặc định ban đầu | Medium | Auto-UI |
| `[AF200-7]` | [0] Breadcrumbs | Hiển thị Breadcrumb | 1. Quan sát Breadcrumb phía trên form | - | 1. Hiển thị chính xác `ホーム＞ギフト管理＞ギフト登録` | Low | Auto-UI |
| `[AF200-8]` | [0] Breadcrumbs | Click `ギフト管理` trên Breadcrumb | 1. Click vào `ギフト管理` trên Breadcrumb | - | 1. Điều hướng quay về màn hình danh sách `AF100` | Medium | Auto-UI |
| | **II. MAIN SCREEN CONTROLS** | | | | | | |
| `[AF200-9]` | [1-AF500] Radio `演出種類` (`animation_type`) | Trạng thái mặc định `通常演出` | 1. Mở AF200 2. Quan sát 3 radio: `通常演出`, `シャッター演出`, `継続演出` | - | 1. `通常演出` được chọn mặc định; ô Giá cho nhập tự do; Category & Gift Content đang enabled | High | Auto-UI |
| `[AF200-10]` | [1-AF500] Radio `演出種類` (`animation_type`) | Chọn `シャッター演出` (Shutter) | 1. Click radio `シャッター演出` | - | 1. Giá chỉ cho chọn `5,000` hoặc `10,000` 2. Category KHÔNG cho chọn (disabled) 3. `ギフトコンテンツ` bị disable | High | Auto-UI |
| `[AF200-11]` | [1-AF500] Radio `演出種類` (`animation_type`) | Chọn `継続演出` (Continuous) | 1. Click radio `継続演出` | - | 1. Giá chỉ cho chọn `1000pt`, `3000pt`, `5,000pt`, `10,000pt` 2. Category bị disable 3. `ギフトコンテンツ` bị disable | High | Auto-UI |
| `[AF200-12]` | [1-AF500] Radio `演出種類` (`animation_type`) | Chuyển qua lại về `通常演出` | 1. Chọn `シャッター演出` rồi chuyển về `通常演出` | - | 1. Category và `ギフトコンテンツ` mở lại (enabled); ô Giá cho nhập tự do lại | High | Auto-UI |
| `[AF200-13]` | [1][2] Textbox `ギフト名` (`name`) | Label, dấu `*` & Placeholder | 1. Quan sát ô `ギフト名` khi trống | - | 1. Hiển thị label `ギフト名`, dấu `*` bắt buộc, placeholder `ギフト名を入力してください` | Medium | Manual-Only (Visual) |
| `[AF200-14]` | [1][2] Textbox `ギフト名` (`name`) | Hover, Focus & Blur | 1. Hover chuột, click Focus rồi click ra ngoài (Blur) | - | 1. Hover hiện con trỏ I-beam; focus highlight viền ô nhập | Low | Auto-UI |
| `[AF200-15]` | [1][2] Textbox `ギフト名` (`name`) | Nhập chữ Nhật hợp lệ (<= 10 ký tự) | 1. Nhập `スター` vào ô `ギフト名` | - | 1. Cho phép nhập và hiển thị chính xác ký tự tiếng Nhật | High | Auto-Data |
| `[AF200-16]` | [1][2] Textbox `ギフト名` (`name`) | Nhập chữ Latin hợp lệ (<= 10 ký tự) | 1. Nhập `StarGift10` vào ô `ギフト名` | - | 1. Cho phép nhập và hiển thị chính xác ký tự Latin | High | Auto-Data |
| `[AF200-17]` | [1][2] Textbox `ギフト名` (`name`) | Biên đúng Max = 10 ký tự | 1. Nhập chuỗi đúng 10 ký tự `1234567890` | - | 1. Cho phép nhập đủ 10 ký tự và lưu thành công | High | Auto-Data |
| `[AF200-18]` | [1][2] Textbox `ギフト名` (`name`) | Vượt Max = 11 ký tự (`CMMSG49`) | 1. Nhập hoặc paste 11 ký tự `12345678901` | - | 1. UI chặn ký tự thứ 11 hoặc báo CMMSG49 (`10文字以内で入力してください。`) | High | Auto-Data |
| `[AF200-19]` | [1][2] Textbox `ギフト名` (`name`) | Space đầu/cuối (`  Star#1  `) | 1. Nhập `  Star#1  ` 2. Lưu | - | 1. Tự động trim space đầu/cuối thành `Star#1` | Medium | Auto-Data |
| `[AF200-20]` | [1][2] Textbox `ギフト名` (`name`) | Nhập toàn khoảng trắng (`"     "`) | 1. Nhập `"     "` 2. Click `登録` | - | 1. Coi như rỗng, báo lỗi CMMSG29: `ギフト名は空欄にできません。` | High | Auto-Data |
| `[AF200-21]` | [1][2] Textbox `ギフト名` (`name`) | Bỏ trống ô `ギフト名` (Required) | 1. Để trống ô `ギフト名` 2. Click `登録` | - | 1. Báo lỗi CMMSG29: `ギフト名は空欄にできません。` | High | Auto-UI |
| `[AF200-22]` | [1][2] Textbox `ギフト名` (`name`) | Paste XSS (`<script>alert(1)</script>`) | 1. Paste `<script>alert(1)</script>` vào ô `ギフト名` | - | 1. Escape an toàn hoặc chặn, không thực thi JS | High | Auto-API |
| `[AF200-23]` | [3][4] Upload `ギフトアイコン` (`icon` - `CMR50`) | Giao diện nút Upload & nhãn `*` | 1. Quan sát vùng upload `ギフトアイコン` | - | 1. Hiển thị nút `アップロード`, nhãn `*`, hỗ trợ PNG/JPG/JPEG/SVG/WebP <= 5MB | Medium | Manual-Only (Visual) |
| `[AF200-24]` | [3][4] Upload `ギフトアイコン` (`icon` - `CMR50`) | Upload hợp lệ (.png, .jpg, .svg, .webp <= 5MB) | 1. Click `アップロード` -> chọn `icon.png` <= 5MB | File hợp lệ | 1. Hiển thị tên file tabable, nút `変更` & `削除`; chưa lưu server cho đến khi bấm `登録` | High | Auto-UI |
| `[AF200-25]` | [3][4] Upload `ギフトアイコン` (`icon` - `CMR50`) | Click tên file mở Modal Preview (`CMR50`) | 1. Click tên file icon đã upload | Đã upload icon | 1. Mở Modal `画像プレビュー` hiển thị ảnh icon rõ nét | High | Auto-UI |
| `[AF200-26]` | [3][4] Upload `ギフトアイコン` (`icon` - `CMR50`) | Click `閉じる` đóng Modal Preview | 1. Tại Modal Preview click nút `閉じる` | Modal đang mở | 1. Đóng Modal Preview, giữ nguyên file đã chọn | Medium | Auto-UI |
| `[AF200-27]` | [3][4] Upload `ギフトアイコン` (`icon` - `CMR50`) | Nút `変更` đổi ảnh icon mới | 1. Click `変更` -> chọn file `icon_new.png` | Đã upload icon | 1. Thay thế bằng tên file `icon_new.png` mới | High | Auto-UI |
| `[AF200-28]` | [3][4] Upload `ギフトアイコン` (`icon` - `CMR50`) | Nút `削除` xóa & upload lại file cũ | 1. Click `削除` 2. Upload lại chính file vừa xóa | Đã upload icon | 1. `削除` reset vùng upload; upload lại cùng file vẫn nhận bình thường | High | Auto-UI |
| `[AF200-29]` | [3][4] Upload `ギフトアイコン` (`icon` - `CMR50`) | Cancel OS File Dialog | 1. Đã có icon -> click `変更` -> bấm Cancel trên OS Dialog | Đã upload icon | 1. Giữ nguyên icon cũ, không báo lỗi | Low | Manual-Only (UX) |
| `[AF200-30]` | [3][4] Upload `ギフトアイコン` (`icon` - `CMR50`) | File rỗng 0 Byte | 1. Upload file `empty.png` (0 Byte) | - | 1. Chặn và báo lỗi file không hợp lệ | High | Auto-UI |
| `[AF200-31]` | [3][4] Upload `ギフトアイコン` (`icon` - `CMR50`) | Biên đúng 5MB | 1. Upload file ảnh đúng 5MB | - | 1. Upload thành công, hiển thị tên file | High | Auto-UI |
| `[AF200-32]` | [3][4] Upload `ギフトアイコン` (`icon` - `CMR50`) | Biên vượt 5MB (5.1MB) (`CMMSG45`) | 1. Upload file ảnh 5.1MB | - | 1. Chặn upload và báo lỗi `CMMSG45` | High | Auto-UI |
| `[AF200-33]` | [3][4] Upload `ギフトアイコン` (`icon` - `CMR50`) | Sai định dạng (.txt, .gif, .exe) (`CMMSG44`) | 1. Upload file `.txt` hoặc `.gif` vào ô icon | - | 1. FE/BE chặn và báo `CMMSG44` | High | Auto-UI |
| `[AF200-34]` | [3][4] Upload `ギフトアイコン` (`icon` - `CMR50`) | Giả mạo Magic Bytes (`malware.exe` -> `.png`) | 1. Đổi đuôi file `.exe` thành `.png` rồi upload | - | 1. Backend kiểm tra Magic Bytes chặn và báo `CMMSG44` | High | Auto-API |
| `[AF200-35]` | [3][4] Upload `ギフトアイコン` (`icon` - `CMR50`) | Bỏ trống Icon khi bấm `登録` (Required) | 1. Không upload icon 2. Click `登録` | - | 1. Báo lỗi `CMMSG29` yêu cầu upload `ギフトアイコン` | High | Auto-UI |
| `[AF200-36]` | [5][6] Upload `ギフトコンテンツ` (`image` - `CMR50`) | Hiển thị Hint text đúng spec | 1. Quan sát dòng gợi ý dưới vùng upload `ギフトコンテンツ` | - | 1. Hint đúng: `アップロード可能な画像形式：PNG、Lottie、GIF / 最大ファイルサイズ：5MB` | Low | Manual-Only (Visual) |
| `[AF200-37]` | [5][6] Upload `ギフトコンテンツ` (`image` - `CMR50`) | Upload hợp lệ (.png, .lottie, .gif <= 5MB) | 1. Upload file `.gif` hoặc `.json` (Lottie) <= 5MB | Đang chọn `通常演出` | 1. Upload thành công, hiển thị tên file, nút `変更` & `削除` | High | Auto-UI |
| `[AF200-38]` | [5][6] Upload `ギフトコンテンツ` (`image` - `CMR50`) | Nút `変更` đổi file content mới | 1. Click `変更` -> chọn file content khác | Đã upload content | 1. Cập nhật file mới thành công | Medium | Auto-UI |
| `[AF200-39]` | [5][6] Upload `ギフトコンテンツ` (`image` - `CMR50`) | Nút `削除` xóa & upload lại file cũ | 1. Click `削除` 2. Upload lại chính file cũ | Đã upload content | 1. Reset vùng upload và cho phép upload lại bình thường | Medium | Auto-UI |
| `[AF200-40]` | [5][6] Upload `ギフトコンテンツ` (`image` - `CMR50`) | Sai định dạng (.jpg, .mp4, .svg) (`CMMSG43`) | 1. Upload `.jpg` hoặc `.mp4` | Đang chọn `通常演出` | 1. Báo lỗi sai định dạng `CMMSG43` | High | Auto-UI |
| `[AF200-41]` | [5][6] Upload `ギフトコンテンツ` (`image` - `CMR50`) | Quá dung lượng > 5MB (`CMMSG45`) | 1. Upload file > 5MB | Đang chọn `通常演出` | 1. Báo lỗi `CMMSG45` | High | Auto-UI |
| `[AF200-42]` | [5][6] Upload `ギフトコンテンツ` (`image` - `CMR50`) | Bỏ trống khi chọn `通常演出` (Required) | 1. Ở `通常演出` bỏ trống -> Click `登録` | Đang chọn `通常演出` | 1. Báo lỗi required `CMMSG29` | High | Auto-UI |
| `[AF200-43]` | [7]-[9] Radio `ステータス` (`status`) | Trạng thái mặc định `公開` | 1. Mở AF200 2. Quan sát radio `ステータス` | - | 1. Mặc định chọn sẵn `公開` | High | Auto-UI |
| `[AF200-44]` | [7]-[9] Radio `ステータス` (`status`) | Chuyển đổi `公開` <-> `非公開` | 1. Click `非公開` 2. Click lại `公開` | - | 1. Chuyển đổi trạng thái chính xác, không lỗi | Medium | Auto-UI |
| `[AF200-45]` | [10][11] Textbox `並び順` (`sort_order`) | Nhập số nguyên dương & số trùng | 1. Nhập `1` 2. Thử nhập số trùng với gift khác | Có gift sort_order=1 | 1. Cho phép nhập số; khi trùng ưu tiên hiển thị theo `id` | High | Auto-UI |
| `[AF200-46]` | [10][11] Textbox `並び順` (`sort_order`) | Nhập số âm (`-1`) | 1. Nhập `-1` vào ô `並び順` | - | 1. Chặn nhập dấu `-` hoặc báo `CMMSG54` | Medium | Auto-Data |
| `[AF200-47]` | [10][11] Textbox `並び順` (`sort_order`) | Nhập số thập phân (`1.5`) | 1. Nhập `1.5` vào ô `並び順` | - | 1. Chặn dấu `.` hoặc báo `CMMSG54` | Medium | Auto-Data |
| `[AF200-48]` | [10][11] Textbox `並び順` (`sort_order`) | Nhập chữ (`abc`) | 1. Nhập `abc` vào ô `並び順` | - | 1. Chặn ký tự chữ hoặc báo `CMMSG54` | Medium | Auto-Data |
| `[AF200-49]` | [10][11] Textbox `並び順` (`sort_order`) | Bỏ trống `並び順` (Required) | 1. Để trống ô `並び順` 2. Click `登録` | - | 1. Báo lỗi bắt buộc nhập `CMMSG29` | High | Auto-UI |
| `[AF200-50]` | [12][13] Textbox `ギフト値段` (`price`) | Placeholder & Auto-format dấu phẩy 3 số | 1. Quan sát placeholder 2. Nhập `10000`, `1234567` | Đang chọn `通常演出` | 1. Placeholder `値段を入力してください`; tự động format `10,000`, `1,234,567` | High | Auto-UI |
| `[AF200-51]` | [12][13] Textbox `ギフト値段` (`price`) | Giá biên Min = `1` | 1. Nhập `1` 2. Điền đủ trường và lưu | Đang chọn `通常演出` | 1. Lưu thành công với giá trị số `1` | High | Auto-Data |
| `[AF200-52]` | [12][13] Textbox `ギフト値段` (`price`) | Nhập số `0` ở đầu (`0100`) | 1. Nhập `0100` vào ô `ギフト値段` | Đang chọn `通常演出` | 1. Chuẩn hóa thành `100` khi lưu | Medium | Auto-Data |
| `[AF200-53]` | [12][13] Textbox `ギフト値段` (`price`) | Nhập giá = `0` (`[Q&A AF200 #1]`) | 1. Nhập `0` 2. Click `登録` | Đang chọn `通常演出` | 1. Từ chối báo lỗi giá phải >= 1 (`[Q&A AF200 #1]`) | High | Manual-Only (Complex DB) |
| `[AF200-54]` | [12][13] Textbox `ギフト値段` (`price`) | Nhập số âm (`-10`) | 1. Nhập `-10` vào ô `ギフト値段` | Đang chọn `通常演出` | 1. UI chặn dấu `-` hoặc báo lỗi chỉ nhập số nguyên dương | High | Auto-Data |
| `[AF200-55]` | [12][13] Textbox `ギフト値段` (`price`) | Nhập số thập phân (`10.5`) | 1. Nhập `10.5` vào ô `ギフト値段` | Đang chọn `通常演出` | 1. UI chặn dấu `.` hoặc báo lỗi chỉ nhập số nguyên | High | Auto-Data |
| `[AF200-56]` | [12][13] Textbox `ギフト値段` (`price`) | Nhập/Paste chữ (`abc`, `100abc`) | 1. Nhập `abc` hoặc paste `100abc` | Đang chọn `通常演出` | 1. Chặn ký tự chữ hoặc báo `CMMSG54` | High | Auto-Data |
| `[AF200-57]` | [12][13] Textbox `ギフト値段` (`price`) | Bỏ trống giá (Required) | 1. Để trống ô `ギフト値段` 2. Click `登録` | Đang chọn `通常演出` | 1. Báo lỗi `CMMSG29` | High | Auto-UI |
| `[AF200-58]` | [14][15] Pulldown `ギフトカテゴリ` (`category_id`) | Optional (không chọn -> `未設定`) | 1. Không chọn category 2. Điền đủ trường khác -> bấm `登録` | Đang chọn `通常演出` | 1. Lưu thành công! Trên AF100 & App `I600` gift nằm ở nhóm `未設定` / tab `一般(General)` | High | Auto-UI |
| `[AF200-59]` | [14][15] Pulldown `ギフトカテゴリ` (`category_id`) | Chọn 1 category từ danh sách | 1. Mở pulldown -> chọn 1 category | Có >= 1 category | 1. Hiển thị đúng tên category đã chọn | High | Auto-UI |
| `[AF200-60]` | [14][15] Pulldown `ギフトカテゴリ` (`category_id`) | Click ngoài đóng pulldown | 1. Mở pulldown Category 2. Click ra vùng trống | - | 1. Pulldown tự đóng, giữ nguyên lựa chọn hiện tại | Low | Auto-UI |
| `[AF200-61]` | [16]-[19] Inline Popover `+` | Mở Popover `カテゴリを追加します` | 1. Click nút `+` cạnh pulldown Category | - | 1. Mở Shadcn Popover `カテゴリを追加します` với ô nhập trống và nút `追加する` | High | Auto-UI |
| `[AF200-62]` | [16]-[19] Inline Popover `+` | Validate bỏ trống trên Popover | 1. Để trống ô nhập 2. Click `追加する` | Popover đang mở | 1. Báo lỗi bắt buộc nhập `CMMSG29` | High | Auto-UI |
| `[AF200-63]` | [16]-[19] Inline Popover `+` | Validate vượt 20 ký tự trên Popover | 1. Nhập 21 ký tự 2. Click `追加する` | Popover đang mở | 1. Chặn hoặc báo lỗi `CMMSG49` (`20文字以内で入力してください。`) | High | Auto-Data |
| `[AF200-64]` | [16]-[19] Inline Popover `+` | Thêm category nhanh thành công | 1. Nhập `EventGift` (<= 20 ký tự) 2. Click `追加する` | Popover đang mở | 1. Gọi `POST /gift/category/`, đóng popover, category mới hiện ngay trong pulldown | High | Auto-UI |
| `[AF200-65]` | [20] Button `キャンセル` (`CMR07`) | Hủy khi chưa nhập dữ liệu | 1. Mở AF200 không sửa gì 2. Click `キャンセル` | Form chưa thay đổi | 1. Điều hướng quay về AF100 ngay lập tức, không hiện popup xác nhận | High | Auto-UI |
| `[AF200-66]` | [20] Button `キャンセル` (`CMR07`) | Hủy khi đã nhập dữ liệu | 1. Nhập dữ liệu vào form 2. Click `キャンセル` | Form đã thay đổi | 1. Hiển thị popup xác nhận `CMMSG46` | High | Auto-UI |
| `[AF200-67]` | [21] Button `登録` (Save) | Validate tất cả trường trống cùng lúc | 1. Để trống toàn bộ trường bắt buộc 2. Click `登録` | - | 1. Hiển thị đầy đủ lỗi `CMMSG29` tại từng trường thiếu | High | Auto-UI |
| `[AF200-68]` | [21] Button `登録` (Save) | Debounce chống double-click (`CMR15`) | 1. Điền đủ dữ liệu 2. Double-click liên tục vào `登録` | - | 1. Disable nút khi đang gửi, chỉ gọi `POST /gift/` đúng 1 lần | High | Auto-API |
| `[AF200-69]` | [21] Button `登録` (Save) | Tạo thành công & Kiểm tra AF100, DB, App `I600` | 1. Điền đủ dữ liệu hợp lệ -> Click `登録` | Có phòng Live | 1. Báo `CMMSG12`, quay về AF100, DB INSERT đúng, App `I600` hiển thị đúng | High | Manual-Only (Complex DB) |
| `[AF200-70]` | [-] Error Handling | Mất mạng (`CMMSG8`) | 1. Ngắt mạng -> bấm `登録` | - | 1. Hiển thị `CMMSG8: ネットワークエラー。接続を確認してください。` | Medium | Manual-Only (UX) |
| `[AF200-71]` | [-] Error Handling | Lỗi server 500 (`CMMSG1`) | 1. Giả lập `POST /gift/` trả 500 -> bấm `登録` | - | 1. Hiển thị `CMMSG1: 予期しないサーバーエラーが発生しました。` | Medium | Auto-API |
| `[AF200-72]` | [-] Error Handling | Hết phiên đăng nhập (`CMMSG10`) | 1. Token hết hạn -> bấm `登録` | - | 1. Hiển thị `CMMSG10` và redirect về trang Login | High | Auto-API |
| | **III. SUB-LAYOUTS / MODALS** | | | | | | |
| `[AF200-73]` | [CMR50-Modal] Modal Preview Ảnh/Animation | Hiển thị ảnh & phát animation Lottie/GIF | 1. Mở modal preview cho Icon và Gift Content | Đã upload | 1. Ảnh tĩnh, GIF hoặc Lottie animation phát mượt mà, đúng tỷ lệ | Medium | Manual-Only (Visual) |
| `[AF200-74]` | [CMR07-Modal] Modal Thoát chưa lưu | Click `[キャンセル]` trên popup `CMMSG46` | 1. Mở popup `CMMSG46` 2. Click `[キャンセル]` | Popup `CMMSG46` đang mở | 1. Đóng popup, giữ nguyên toàn bộ dữ liệu đang nhập trên form | High | Auto-UI |
| `[AF200-75]` | [CMR07-Modal] Modal Thoát chưa lưu | Click `[OK]` trên popup `CMMSG46` | 1. Mở popup `CMMSG46` 2. Click `[OK]` | Popup `CMMSG46` đang mở | 1. Hủy bỏ dữ liệu đang nhập và quay về màn hình `AF100` | High | Auto-UI |
| `[AF200-76]` | [-] Layout & A11y | Responsive 1024px & Tab order | 1. Resize 1024px và nhấn `Tab` qua các trường | - | 1. Không vỡ layout; thứ tự Tab hợp lý từ trên xuống dưới | Low | Manual-Only (UX) |

---

## THỐNG KÊ AUTOMATION FEASIBILITY (AF200)

| Nhóm | Số lượng | Tỷ lệ |
|---| :---: | :---: |
| `Auto-UI` | 46 | 60.5% |
| `Auto-API` | 6 | 7.9% |
| `Auto-Data` | 15 | 19.7% |
| `Manual-Only` (Visual / Complex DB / UX) | 9 | 11.8% |
| **Tổng cộng** | **76** | **88.2% Auto / 11.8% Manual** ✅ |
