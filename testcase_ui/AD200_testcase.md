# BẢNG ĐẶC TẢ KIỂM THỬ GIAO DIỆN THỦ CÔNG (MANUAL UI TEST SUITE)
## Màn hình: AD200_Register Agency (Đăng Ký Tạo Mới Agency - 事務所新規登録)
### Phân hệ: Master Admin Web (`AA000`) / Quản lý Agency (`AD` Module)
### Áp dụng: Quy chuẩn Trụ cột 2 (`Universal_Rules/02_manual_ui_test_case_rule.md`) & Thư viện `UI_controls/`

---

## BẢNG ĐIỀU KHIỂN TIẾN ĐỘ & THỐNG KÊ (DASHBOARD HEADER)

| Thuộc tính | Giá trị | Thuộc tính | Giá trị | Round 1 Metric | Kết quả | Round 2 Metric | Kết quả |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Module Code** | `AD200` | **Environment** | `Dev-Admin` / `STG-Admin` | **Pass** | 0 | **Pass** | 0 |
| **Total Testcases** | **65** | **% Executed** | 0% | **Fail** | 0 | **Fail** | 0 |
| **Plan to Execute** | **65** | **Creator** | `NgaDTP` | **Impact** | 0 | **Impact** | 0 |
| **Spec Source** | `Surreal SPEC` | **Google Sheet Tab** | `AD200` (gid=2093029291) | **Not Run** | 65 | **Not Run** | 0 |
| | | | | **Total** | 65 | **Total** | 0 |

---

## CHI TIẾT BẢNG TEST CASES (7 CỘT CHUẨN MARKDOWN)

| ID | Title | Big item | Steps | Pre-condition | Expected | Priority |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| | **I. COMMON & NAVIGATION** | | | | | |
| `[AD200-1]` | [0] Kiểm tra truy cập màn hình | Check điều hướng từ AD100 | 1. Tại màn hình AD100, click nút [新規登録] | User là Master Admin đăng nhập thành công | 1. Điều hướng thành công sang màn hình tạo mới AD200, URL hiển thị `/admin/agencies/create` | **High** |
| `[AD200-2]` | [0] Kiểm tra truy cập màn hình | Check truy cập Inbound trực tiếp | 1. Nhập trực tiếp URL `/admin/agencies/create` trên thanh địa chỉ trình duyệt | - | 1. Màn hình AD200 tải thành công form tạo mới Agency đúng thiết kế Figma 907-3040 | **High** |
| `[AD200-3]` | [0] Kiểm tra truy cập màn hình | Check phân quyền RBAC | 1. Đăng nhập với tài khoản Agency Admin hoặc User 2. Truy cập URL `/admin/agencies/create` | - | 1. Bị chặn truy cập, hiển thị thông báo lỗi CMMSG5: この操作を行う権限がありません。 | **High** |
| `[AD200-4]` | [0] Kiểm tra truy cập màn hình | Check Screen Lifecycle F5 Reload | 1. Nhập một số thông tin trên form AD200 2. Nhấn phím F5 Reload trình duyệt | - | 1. Trang web reload thành công, form mở lại ở trạng thái khởi tạo an toàn | **Medium** |
| `[AD200-5]` | [0] Breadcrumbs | Check hiển thị breadcrumb | 1. Quan sát thanh Breadcrumbs ở phía trên | - | 1. Hiển thị text đúng: '＞ 事務所管理 ＞ 事務所新規登録' | **Low** |
| `[AD200-6]` | [0] Breadcrumbs | Check click link '事務所管理' | 1. Đang ở màn AD200 (chưa nhập dữ liệu) 2. Click '事務所管理' trên breadcrumb | - | 1. Điều hướng quay về danh sách Agency AD100 | **Medium** |
| | **II. MAIN SCREEN CONTROLS** | | | | | |
| `[AD200-7]` | Form Layout | Check hiển thị tiêu đề và nhãn bắt buộc | 1. Quan sát toàn bộ giao diện form AD200 | - | 1. Hiển thị đầy đủ 6 trường thông tin kèm dấu hoa thị bắt buộc (Required ◯): 事務所名, 事務所ID, 事務所ロゴ, 連絡先 オーナー名, 電話番号, メールアドレス | **Medium** |
| `[AD200-8]` | [2] 事務所名 | Check hiển thị và placeholder | 1. Quan sát ô nhập 事務所名 | - | 1. Placeholder hiển thị text: '事務所名を入力してください' | **Low** |
| `[AD200-9]` | [2] 事務所名 | Nhập ký tự hợp lệ thông thường | 1. Nhập tên Agency bằng chữ Kanji, Hiragana, Katakana, Romaji (VD: 'テスト事務所') | - | 1. Hệ thống cho phép nhập bình thường | **High** |
| `[AD200-10]` | [2] 事務所名 | Nhập ký tự đặc biệt | 1. Nhập tên Agency có chứa ký tự đặc biệt (VD: 'Agency & Co., Ltd #1') | - | 1. Cho phép nhập ký tự đặc biệt theo đúng mô tả Spec | **Medium** |
| `[AD200-11]` | [2] 事務所名 | Kiểm tra độ dài biên Min = 1 ký tự | 1. Nhập 1 ký tự duy nhất (VD: 'A') | - | 1. Hệ thống chấp nhận giá trị hợp lệ | **Medium** |
| `[AD200-12]` | [2] 事務所名 | Kiểm tra độ dài biên Max = 20 ký tự | 1. Nhập chuỗi có đúng 20 ký tự | - | 1. Hệ thống chấp nhận giá trị hợp lệ | **Medium** |
| `[AD200-13]` | [2] 事務所名 | Kiểm tra vượt quá Max = 21 ký tự | 1. Nhập chuỗi có 21 ký tự vào ô 事務所名 | - | 1. Bị chặn nhập ở ký tự thứ 20 trên UI hoặc báo lỗi CMMSG49: 事務所名は文字数が多すぎます。20文字以内で入力してください。 | **High** |
| `[AD200-14]` | [2] 事務所名 | Để trống trường bắt buộc | 1. Để trống ô 事務所名 2. Click nút 登録 | - | 1. Báo lỗi trường bắt buộc CMMSG29: 事務所名は空欄にできません。 | **High** |
| `[AD200-15]` | [2] 事務所名 | Kiểm tra trùng tên Agency (CR 15/10/2026) | 1. Nhập tên trùng 100% với tên một Agency đã tồn tại trên hệ thống 2. Bấm 登録 | Hệ thống đã có Agency mang tên 'Tokyo Live' | 1. Báo lỗi trùng lặp tên CMMSG57: 事務所名は既に存在しています。 | **High** |
| `[AD200-16]` | [2] 事務所名 | Kiểm tra cắt tỉa khoảng trắng | 1. Nhập tên Agency có khoảng trắng ở đầu và cuối (VD: '  Agency Test  ') | - | 1. Hệ thống tự động trim khoảng trắng khi lưu dữ liệu | **Low** |
| `[AD200-17]` | [3] 事務所ID | Check hiển thị, placeholder và text gợi ý | 1. Quan sát ô nhập 事務所ID và dòng text dưới ô | - | 1. Placeholder: 'IDを入力してください'; text gợi ý: '・使用可能文字：英文字、数字 \n ・文字数制限：3 〜 20文字' | **Medium** |
| `[AD200-18]` | [3] 事務所ID | Nhập chuỗi chữ cái Latin và số hợp lệ | 1. Nhập ID bằng chữ thường, chữ hoa và số (VD: 'Agency01Live') | - | 1. Hệ thống chấp nhận giá trị hợp lệ | **High** |
| `[AD200-19]` | [3] 事務所ID | Kiểm tra độ dài biên Min = 3 ký tự | 1. Nhập đúng 3 ký tự (VD: 'AG1') | - | 1. Hệ thống chấp nhận giá trị hợp lệ | **Medium** |
| `[AD200-20]` | [3] 事務所ID | Kiểm tra độ dài nhỏ hơn Min = 2 ký tự | 1. Nhập 2 ký tự (VD: 'AG') 2. Click 登録 | - | 1. Báo lỗi độ dài CMMSG52: 事務所IDは文字数が足りません。3文字以上で入力してください。 | **High** |
| `[AD200-21]` | [3] 事務所ID | Kiểm tra độ dài biên Max = 20 ký tự | 1. Nhập chuỗi 20 ký tự hợp lệ | - | 1. Hệ thống chấp nhận giá trị hợp lệ | **Medium** |
| `[AD200-22]` | [3] 事務所ID | Kiểm tra vượt quá Max = 21 ký tự | 1. Nhập chuỗi 21 ký tự vào ô 事務所ID | - | 1. Bị chặn nhập ở ký tự thứ 20 hoặc báo lỗi CMMSG49: 事務所IDは文字数が多すぎます。20文字以内で入力してください。 | **High** |
| `[AD200-23]` | [3] 事務所ID | Chặn nhập ký tự đặc biệt | 1. Nhập ký tự đặc biệt '!@#$%^&*' vào ô 事務所ID 2. Click 登録 | - | 1. Hệ thống chặn nhập hoặc báo lỗi chuẩn CMMSG55: 半角英字（a-z）と数字（0-9）のみ入力してください。 | **High** |
| `[AD200-24]` | [3] 事務所ID | Chặn nhập tiếng Nhật toàn giác | 1. Nhập ký tự tiếng Nhật hoặc chữ toàn giác (Zen-kaku) vào ô 事務所ID | - | 1. Báo lỗi CMMSG55: 半角英字（a-z）と数字（0-9）のみ入力してください。 | **High** |
| `[AD200-25]` | [3] 事務所ID | Để trống trường bắt buộc | 1. Để trống ô 事務所ID 2. Click 登録 | - | 1. Báo lỗi trường bắt buộc CMMSG29: 事務所IDは空欄にできません。 | **High** |
| `[AD200-26]` | [3] 事務所ID | Kiểm tra trùng mã Agency ID đã có | 1. Nhập mã ID đã được gán cho một Agency khác 2. Click 登録 | Hệ thống đã có Agency mang ID 'agency01' | 1. Báo lỗi trùng mã định danh MSG15: このIDは登録済みです。 | **High** |
| `[AD200-27]` | [3] 事務所ID | Kiểm tra trùng login ID hoặc email | 1. Nhập mã ID trùng với login ID hoặc email của tài khoản khác | - | 1. Báo lỗi trùng tài khoản MSG145: このメールアドレスまたはIDは登録済みです。 | **High** |
| `[AD200-28]` | [4] 事務所ロゴ | Check hiển thị và text gợi ý | 1. Quan sát vùng upload logo Agency | - | 1. Hiển thị text hướng dẫn: 'アップロード可能な画像形式：PNG、JPG／JPEG、SVG、WebP \n 最大ファイルサイズ：5MB' | **Low** |
| `[AD200-29]` | [4] 事務所ロゴ | Check Logo mặc định (CR 15/10/2026) | 1. Mở màn hình tạo mới AD200 khi chưa chọn file nào | - | 1. Mặc định có sẵn ảnh Logo hệ thống hiển thị trong khung xem trước | **High** |
| `[AD200-30]` | [4] 事務所ロゴ | Upload định dạng PNG hợp lệ | 1. Chọn file ảnh PNG có dung lượng < 5MB | File `valid_png_5mb.png` | 1. Upload thành công, ảnh xem trước được cập nhật | **High** |
| `[AD200-31]` | [4] 事務所ロゴ | Upload định dạng JPG / JPEG hợp lệ | 1. Chọn file ảnh JPG dung lượng < 5MB | File ảnh JPG hợp lệ | 1. Upload thành công, cập nhật ảnh xem trước | **Medium** |
| `[AD200-32]` | [4] 事務所ロゴ | Upload định dạng SVG hợp lệ | 1. Chọn file vector SVG dung lượng < 5MB | File `valid_svg_5mb.svg` | 1. Upload thành công, hiển thị vector sắc nét | **Medium** |
| `[AD200-33]` | [4] 事務所ロゴ | Upload định dạng WebP hợp lệ | 1. Chọn file ảnh WebP dung lượng < 5MB | File ảnh WebP hợp lệ | 1. Upload thành công | **Medium** |
| `[AD200-34]` | [4] 事務所ロゴ | Chặn file sai định dạng (GIF, PDF...) | 1. Chọn file định dạng không cho phép (file .gif hoặc .pdf) | File `invalid_file_gif.gif` | 1. Hệ thống từ chối file và báo lỗi CMMSG43: 無効な画像形式です。サポート形式: PNG, JPG, JPEG, SVG, WebP。 | **High** |
| `[AD200-35]` | [4] 事務所ロゴ | Chặn file quá dung lượng 5MB | 1. Chọn file ảnh có dung lượng > 5MB (VD: 8MB) | File `valid_jpg_8mb.jpg` | 1. Hệ thống từ chối file và báo lỗi CMMSG45: ファイルサイズは5MB以下にしてください。 | **High** |
| `[AD200-36]` | [4] 事務所ロゴ | Thay đổi ảnh sau khi đã chọn | 1. Upload ảnh A 2. Tiếp tục chọn upload ảnh B hợp lệ khác | - | 1. Ảnh xem trước cập nhật sang ảnh B, ảnh cũ bị thay thế | **Low** |
| `[AD200-37]` | [4] 事務所ロゴ | Cơ chế lưu ảnh chỉ khi submit thành công | 1. Upload ảnh nhưng click Cancel không lưu form | - | 1. Ảnh tạm thời không được gắn vào Agency trên server | **Medium** |
| `[AD200-38]` | [5] 連絡先 オーナー名 | Check hiển thị và placeholder | 1. Quan sát ô nhập 連絡先 オーナー名 | - | 1. Placeholder hiển thị text: '連絡先の名前を入力してください' | **Low** |
| `[AD200-39]` | [5] 連絡先 オーナー名 | Nhập tên người đại diện hợp lệ | 1. Nhập tên đại diện bằng chữ Kanji/Katakana/Romaji (VD: '山田 太郎') | - | 1. Hệ thống chấp nhận giá trị hợp lệ | **Medium** |
| `[AD200-40]` | [5] 連絡先 オーナー名 | Kiểm tra độ dài biên Min = 1 ký tự | 1. Nhập đúng 1 ký tự | - | 1. Hệ thống chấp nhận giá trị hợp lệ | **Low** |
| `[AD200-41]` | [5] 連絡先 オーナー名 | Kiểm tra độ dài biên Max = 20 ký tự | 1. Nhập đúng 20 ký tự | - | 1. Hệ thống chấp nhận giá trị hợp lệ | **Medium** |
| `[AD200-42]` | [5] 連絡先 オーナー名 | Kiểm tra vượt quá Max = 21 ký tự | 1. Nhập chuỗi 21 ký tự vào ô オーナー名 | - | 1. Bị chặn ở ký tự 20 hoặc báo lỗi CMMSG49: オーナー名は文字数が多すぎます。20文字以内で入力してください。 | **High** |
| `[AD200-43]` | [5] 連絡先 オーナー名 | Để trống trường bắt buộc | 1. Để trống ô 連絡先 オーナー名 2. Click 登録 | - | 1. Báo lỗi trường bắt buộc CMMSG29: 連絡先 オーナー名は空欄にできません。 | **High** |
| `[AD200-44]` | [6] 電話番号 | Check hiển thị và placeholder | 1. Quan sát ô nhập 電話番号 | - | 1. Placeholder hiển thị text: '電話番号を入力してください' | **Low** |
| `[AD200-45]` | [6] 電話番号 | Nhập số điện thoại hợp lệ (CMR04) | 1. Nhập số điện thoại chuẩn Nhật Bản (VD: '03-1234-5678' hoặc '09012345678') | - | 1. Hệ thống chấp nhận nhập tự do theo chuẩn CMR04 | **Medium** |
| `[AD200-46]` | [6] 電話番号 | Kiểm tra độ dài biên Min = 5 ký tự | 1. Nhập số điện thoại 5 ký tự | - | 1. Hệ thống chấp nhận giá trị hợp lệ | **Low** |
| `[AD200-47]` | [6] 電話番号 | Kiểm tra độ dài nhỏ hơn Min = 4 ký tự | 1. Nhập chuỗi 4 ký tự 2. Click 登録 | - | 1. Báo lỗi CMMSG52: 電話番号は文字数が足りません。5文字以上で入力してください。 | **High** |
| `[AD200-48]` | [6] 電話番号 | Kiểm tra độ dài biên Max = 20 ký tự | 1. Nhập chuỗi đúng 20 ký tự | - | 1. Hệ thống chấp nhận giá trị hợp lệ | **Medium** |
| `[AD200-49]` | [6] 電話番号 | Kiểm tra vượt quá Max = 21 ký tự | 1. Nhập chuỗi 21 ký tự vào ô 電話番号 | - | 1. Bị chặn ở ký tự 20 hoặc báo lỗi CMMSG49: 電話番号は文字数が多すぎます。20文字以内で入力してください。 | **High** |
| `[AD200-50]` | [6] 電話番号 | Để trống trường bắt buộc | 1. Để trống ô 電話番号 2. Click 登録 | - | 1. Báo lỗi trường bắt buộc CMMSG29: 電話番号は空欄にできません。 | **High** |
| `[AD200-51]` | [7] メールアドレス | Check hiển thị và placeholder | 1. Quan sát ô nhập メールアドレス | - | 1. Placeholder hiển thị text: 'メールアドレスを入力してください' | **Low** |
| `[AD200-52]` | [7] メールアドレス | Nhập email hợp lệ theo CMR42 | 1. Nhập email đúng định dạng `a@b.c` (VD: 'owner@agency.com') | - | 1. Hệ thống chấp nhận định dạng hợp lệ | **High** |
| `[AD200-53]` | [7] メールアドレス | Chặn sai định dạng email | 1. Nhập email sai format (VD: 'plainaddress', '@domain.com', 'a@b') 2. Click 登録 | - | 1. Báo lỗi định dạng email theo chuẩn CMR42 | **High** |
| `[AD200-54]` | [7] メールアドレス | Kiểm tra độ dài biên Min = 3 ký tự | 1. Nhập email độ dài 5 ký tự 'a@b.c' | - | 1. Hệ thống chấp nhận giá trị hợp lệ | **Low** |
| `[AD200-55]` | [7] メールアドレス | Kiểm tra độ dài Max = 254 ký tự (#13003) | 1. Nhập email đúng 254 ký tự | - | 1. Hệ thống chấp nhận giá trị hợp lệ | **Medium** |
| `[AD200-56]` | [7] メールアドレス | Kiểm tra vượt quá Max = 255 ký tự | 1. Nhập email 255 ký tự | - | 1. Báo lỗi CMMSG49: メールアドレスは文字数が多すぎます。254文字以内で入力してください。 | **High** |
| `[AD200-57]` | [7] メールアドレス | Để trống trường bắt buộc | 1. Để trống ô メールアドレス 2. Click 登録 | - | 1. Báo lỗi trường bắt buộc CMMSG29: メールアドレスは空欄にできません。 | **High** |
| `[AD200-58]` | [7] メールアドレス | Kiểm tra trùng email đã đăng ký | 1. Nhập email đã tồn tại trong hệ thống (của user hoặc admin khác) 2. Click 登録 | - | 1. Báo lỗi email đã tồn tại MSG14: このメールアドレスは登録済みです。 | **High** |
| `[AD200-59]` | [8] Button キャンセル | Hủy thao tác khi form chưa nhập | 1. Mở màn hình AD200 khi chưa nhập gì 2. Click nút キャンセル | - | 1. Hệ thống điều hướng ngay lập tức về danh sách Agency AD100 | **Medium** |
| `[AD200-60]` | [8] Button キャンセル | Hủy thao tác khi form đã nhập liệu | 1. Đã nhập dữ liệu vào các trường trên form 2. Click nút キャンセル | - | 1. Hiển thị popup cảnh báo mất dữ liệu CMMSG46: 戻ってもよろしいですか？保存されていない変更は失われます。 | **High** |
| `[AD200-61]` | [8] Button 登録 | Debounce chống double-click (CMR15) | 1. Nhập đầy đủ thông tin hợp lệ 2. Nhấp đúp (Double-click liên tục) vào nút 登録 | - | 1. Nút 登録 tạm thời bị disable (CMR15), chỉ gửi 1 request tạo agency duy nhất | **Medium** |
| `[AD200-62]` | [8] Button 登録 | Tạo mới Agency thành công | 1. Nhập toàn bộ dữ liệu hợp lệ cho tất cả 6 trường 2. Click nút 登録 | - | 1. Gọi API `POST /agency/create/`, hiển thị thông báo thành công CMMSG12: 正常に作成されました。, điều hướng về AD100 và danh sách xuất hiện Agency mới | **High** |
| `[AD200-63]` | [8] Button 登録 | Sinh mật khẩu tạm thời & Gửi email PEM3 (CR 21/10/2026) | 1. Kiểm tra sau khi tạo Agency thành công | - | 1. BE tự sinh mật khẩu tạm 12 ký tự chuẩn CMR43 (không lộ ra UI); tự động gửi email mời PEM3 tới địa chỉ email của Owner | **High** |
| `[AD200-64]` | [8] Button 登録 | Kiểm tra link kích hoạt PEM3 có hạn 30 ngày (CMR68) | 1. Mở email PEM3 gửi tới hòm thư Owner 2. Kiểm tra link chuyển đến BA1003 | - | 1. Link có thời hạn kích hoạt 30 ngày (CMR68); truy cập link mở màn hình đặt mật khẩu mới BA1003 theo chuẩn CMR43 | **High** |
| `[AD200-65]` | Error Handling | Xử lý khi mất mạng khi đang submit | 1. Ngắt kết nối mạng Internet 2. Click nút 登録 | - | 1. Hiển thị thông báo lỗi mạng chuẩn CMMSG8: ネットワークエラー。接続を確認してください。 | **Medium** |
