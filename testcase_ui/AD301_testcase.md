# BẢNG ĐẶC TẢ KIỂM THỬ GIAO DIỆN THỦ CÔNG (MANUAL UI TEST SUITE)
## Màn hình: AD301_Agency Information (Chi Tiết & Chỉnh Sửa Thông Tin Agency - 事務所詳細_詳細)
### Phân hệ: Master Admin Web (`AA000`) / Quản lý Agency (`AD` Module)
### Áp dụng: Quy chuẩn Trụ cột 2 (`Universal_Rules/02_manual_ui_test_case_rule.md`) & Thư viện `UI_controls/`

---

## BẢNG ĐIỀU KHIỂN TIẾN ĐỘ & THỐNG KÊ (DASHBOARD HEADER)

| Thuộc tính | Giá trị | Thuộc tính | Giá trị | Round 1 Metric | Kết quả | Round 2 Metric | Kết quả |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Module Code** | `AD301` | **Environment** | `Dev-Admin` / `STG-Admin` | **Pass** | 0 | **Pass** | 0 |
| **Total Testcases** | **74** | **% Executed** | 0% | **Fail** | 0 | **Fail** | 0 |
| **Plan to Execute** | **74** | **Creator** | `NgaDTP` | **Impact** | 0 | **Impact** | 0 |
| **Spec Source** | `Surreal SPEC` | **Google Sheet Tab** | `AD301` (gid=406207487) | **Not Run** | 74 | **Not Run** | 0 |
| | | | | **Total** | 74 | **Total** | 0 |

---

## CHI TIẾT BẢNG TEST CASES (7 CỘT CHUẨN MARKDOWN)

| ID | Title | Big item | Steps | Pre-condition | Expected | Priority |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| | **I. COMMON & NAVIGATION** | | | | | |
| `[AD301-1]` | [0] Kiểm tra truy cập màn hình | Check điều hướng từ AD100 | 1. Tại AD100, click vào dòng Agency hoặc icon chi tiết của Agency ID=5 | User là Master Admin đăng nhập thành công | 1. Điều hướng thành công sang màn hình chi tiết AD301, URL hiển thị `/admin/agencies/5` | **High** |
| `[AD301-2]` | [0] Kiểm tra truy cập màn hình | Check Inbound với agency_id hợp lệ | 1. Mở trực tiếp URL `/admin/agencies/5` trên trình duyệt | Bản ghi Agency ID=5 tồn tại | 1. Tải thành công toàn bộ thông tin chi tiết của Agency ID=5 đúng thiết kế Figma 911-4648 | **High** |
| `[AD301-3]` | [0] Kiểm tra truy cập màn hình | Check Inbound với ID không tồn tại | 1. Mở URL `/admin/agencies/999999` với ID không tồn tại | - | 1. Hệ thống báo lỗi CMMSG3 (Resource not found) hoặc tự động chuyển hướng về danh sách AD100 | **Medium** |
| `[AD301-4]` | [0] Kiểm tra truy cập màn hình | Check Screen Lifecycle F5 Reload | 1. Đang xem thông tin Agency, nhấn F5 Reload trình duyệt | - | 1. Trang web reload thành công, giữ nguyên màn hình AD301 và toàn bộ dữ liệu chi tiết của Agency | **Medium** |
| `[AD301-5]` | [0] Kiểm tra truy cập màn hình | Check phân quyền RBAC | 1. Đăng nhập tài khoản Agency Admin 2. Cố tình truy cập URL `/admin/agencies/{other_agency_id}` | - | 1. Hệ thống chặn truy cập, hiển thị thông báo lỗi CMMSG5: この操作を行う権限がありません。 | **High** |
| `[AD301-6]` | [0] Breadcrumbs | Check hiển thị breadcrumb | 1. Quan sát thanh Breadcrumbs ở đầu trang | - | 1. Hiển thị text: '＞ 事務所管理 ＞ 事務所詳細' | **Low** |
| `[AD301-7]` | [0] Breadcrumbs | Click '事務所管理' trên breadcrumb | 1. Click link '事務所管理' trên breadcrumb | - | 1. Điều hướng quay về danh sách Agency AD100 và bảo lưu bộ lọc trước đó | **High** |
| `[AD301-8]` | [2] Tabs Navigation | Check hiển thị 3 tab (CMR20) | 1. Quan sát thanh tab chuyển đổi phân hệ chi tiết Agency | - | 1. Hiển thị đầy đủ 3 Tab: '詳細' (AD301), 'ライバー一覧' (AD302), '売上' (AD303) | **High** |
| `[AD301-9]` | [2] Tabs Navigation | Check active mặc định Tab '詳細' | 1. Mở màn hình chi tiết Agency AD300 | - | 1. Tab '詳細' được highlight active mặc định theo CMR40 | **Medium** |
| `[AD301-10]` | [2] Tabs Navigation | Chuyển sang Tab 'ライバー一覧' | 1. Click Tab [ライバー一覧] | - | 1. Chuyển mượt mà sang màn hình danh sách streamer AD302 của cùng Agency đó | **High** |
| `[AD301-11]` | [2] Tabs Navigation | Chuyển sang Tab '売上' | 1. Click Tab [売上] | - | 1. Chuyển mượt mà sang màn hình phân tích doanh thu AD303 của cùng Agency đó | **High** |
| `[AD301-12]` | [2] Tabs Navigation | Click lại Tab '詳細' | 1. Click vào Tab [詳細] khi đang ở chính màn này | - | 1. Ở nguyên màn AD301, không bị reload lại trang | **Low** |
| | **II. MAIN SCREEN CONTROLS** | | | | | |
| `[AD301-13]` | Form Load Data | Check tải dữ liệu ban đầu | 1. Đối chiếu các trường trên form với dữ liệu DB | - | 1. Tự động đổ chính xác: 事務所名, 事務所ID, Logo, 連絡先, 電話番号, メールアドレス, ステータス | **High** |
| `[AD301-14]` | [3] 事務所名 | Nhập tên Agency mới hợp lệ | 1. Xóa tên cũ, nhập tên mới 1-20 ký tự (VD: '新事務所2026') 2. Click 保存 | - | 1. Cho phép cập nhật và hiển thị tên mới | **High** |
| `[AD301-15]` | [3] 事務所名 | Giữ nguyên tên hiện tại của Agency | 1. Không sửa ô 事務所名, sửa trường khác 2. Click 保存 | - | 1. Lưu thành công, không bị báo lỗi trùng tên với chính nó | **High** |
| `[AD301-16]` | [3] 事務所名 | Kiểm tra trùng tên Agency khác (CR 15/10/2026) | 1. Sửa tên Agency trùng với tên một Agency khác đang có trên hệ thống 2. Click 保存 | - | 1. Báo lỗi trùng tên CMMSG57: 事務所名は既に存在しています。 | **High** |
| `[AD301-17]` | [3] 事務所名 | Xóa trắng ô tên bắt buộc | 1. Xóa toàn bộ ký tự trong ô 事務所名 2. Click 保存 | - | 1. Báo lỗi trường bắt buộc CMMSG29: 事務所名は空欄にできません。 | **High** |
| `[AD301-18]` | [3] 事務所名 | Kiểm tra độ dài vượt quá 20 ký tự | 1. Nhập tên dài 21 ký tự | - | 1. Bị chặn ở ký tự 20 hoặc báo lỗi CMMSG49: 事務所名は文字数が多すぎます。20文字以内で入力してください。 | **Medium** |
| `[AD301-19]` | [4] 事務所ID | Check hiển thị và chỉnh sửa mã ID | 1. Quan sát ô 事務所ID và chỉnh sửa mã ID mới hợp lệ | - | 1. Hiển thị mã hiện tại; cho phép chỉnh sửa nếu đáp ứng quy tắc chữ Latin + số từ 3-20 ký tự | **Medium** |
| `[AD301-20]` | [4] 事務所ID | Sửa trùng mã Agency ID khác | 1. Sửa mã ID trùng với ID của một Agency khác 2. Click 保存 | - | 1. Báo lỗi trùng ID MSG15: このIDは登録済みです。 | **High** |
| `[AD301-21]` | [4] 事務所ID | Chặn ký tự đặc biệt ở ô 事務所ID | 1. Nhập ký tự đặc biệt hoặc tiếng Nhật vào ô 事務所ID | - | 1. Báo lỗi chuẩn CMMSG55: 半角英字（a-z）と数字（0-9）のみ入力してください。 | **High** |
| `[AD301-22]` | [4] 事務所ID | Xóa trắng ô 事務所ID bắt buộc | 1. Xóa trắng ô 事務所ID 2. Click 保存 | - | 1. Báo lỗi trường bắt buộc CMMSG29: 事務所IDは空欄にできません。 | **High** |
| `[AD301-23]` | [5] 事務所ロゴ | Check hiển thị ảnh Logo hiện tại | 1. Quan sát khung logo Agency | - | 1. Hiển thị ảnh logo hiện tại của Agency; nếu dữ liệu cũ chưa có logo thì hiển thị logo hệ thống (CR 15/10/2026) | **Medium** |
| `[AD301-24]` | [5] 事務所ロゴ | Upload ảnh logo mới hợp lệ | 1. Chọn file ảnh PNG/JPG/SVG/WebP mới dung lượng < 5MB | File ảnh hợp lệ | 1. Khung xem trước cập nhật ảnh mới; bấm 保存 sẽ lưu ảnh mới thành công | **High** |
| `[AD301-25]` | [5] 事務所ロゴ | Chặn file sai định dạng | 1. Chọn file định dạng cấm (file .gif / .pdf) | - | 1. Báo lỗi CMMSG43: 無効な画像形式です。サポート形式: PNG, JPG, JPEG, SVG, WebP。 | **High** |
| `[AD301-26]` | [5] 事務所ロゴ | Chặn file quá kích thước 5MB | 1. Chọn file ảnh dung lượng > 5MB | File `valid_jpg_8mb.jpg` | 1. Báo lỗi CMMSG45: ファイルサイズは5MB以下にしてください。 | **High** |
| `[AD301-27]` | [6] 連絡先 オーナー名 | Sửa tên người đại diện hợp lệ | 1. Nhập tên người đại diện mới 1-20 ký tự 2. Click 保存 | - | 1. Lưu thành công thông tin người đại diện | **Medium** |
| `[AD301-28]` | [6] 連絡先 オーナー名 | Xóa trắng trường bắt buộc | 1. Xóa trắng ô オーナー名 2. Click 保存 | - | 1. Báo lỗi CMMSG29: 連絡先 オーナー名は空欄にできません。 | **High** |
| `[AD301-29]` | [6] 連絡先 オーナー名 | Nhập quá 20 ký tự | 1. Nhập chuỗi 21 ký tự vào ô オーナー名 | - | 1. Bị chặn ở ký tự 20 hoặc báo lỗi CMMSG49 | **Low** |
| `[AD301-30]` | [7] 電話番号 | Sửa số điện thoại hợp lệ | 1. Nhập số điện thoại mới 5-20 ký tự (VD: '03-9876-5432') 2. Click 保存 | - | 1. Lưu thành công theo chuẩn CMR04 | **Medium** |
| `[AD301-31]` | [7] 電話番号 | Nhập số điện thoại < 5 ký tự | 1. Nhập 4 ký tự vào ô 電話番号 2. Click 保存 | - | 1. Báo lỗi CMMSG52: 電話番号は文字数が足りません。5文字以上で入力してください。 | **High** |
| `[AD301-32]` | [7] 電話番号 | Xóa trắng ô số điện thoại bắt buộc | 1. Xóa trắng ô 電話番号 2. Click 保存 | - | 1. Báo lỗi CMMSG29: 電話番号は空欄にできません。 | **High** |
| `[AD301-33]` | [8] メールアドレス | Giữ nguyên email hiện tại | 1. Không thay đổi ô email, thay đổi trường khác 2. Bấm 保存 | - | 1. Lưu bình thường, không kích hoạt luồng gửi mail xác thực | **High** |
| `[AD301-34]` | [8] メールアドレス | Nhập email sai định dạng CMR42 | 1. Nhập chuỗi không đúng định dạng `a@b.c` 2. Click 保存 | - | 1. Báo lỗi định dạng email theo chuẩn CMR42 | **High** |
| `[AD301-35]` | [8] メールアドレス | Xóa trắng ô email bắt buộc | 1. Xóa trắng ô メールアドレス 2. Click 保存 | - | 1. Báo lỗi CMMSG29: メールアドレスは空欄にできません。 | **High** |
| `[AD301-36]` | [8] メールアドレス | Nhập email đã tồn tại trên hệ thống | 1. Nhập email trùng với một user hoặc admin khác 2. Click 保存 | - | 1. Báo lỗi email đã tồn tại MSG14: このメールアドレスは登録済みです。 | **High** |
| `[AD301-37]` | [8] メールアドレス | Đổi email mới kích hoạt luồng PEM4 (CR 19/10/2026) | 1. Nhập email mới chưa từng đăng ký 2. Click nút 保存 | - | 1. Các trường khác lưu ngay; Email CHƯA đổi ngay; Hệ thống gửi mail xác thực PEM4 tới email mới; Cạnh ô hiện nhãn `「認証待ち：{新メールアドレス}」` | **High** |
| `[AD301-38]` | [8] メールアドレス | Check hiển thị nhãn '認証待ち' khi reload | 1. Đang có yêu cầu đổi email chờ xác thực 2. Nhấn F5 Reload lại trang AD301 | - | 1. Nhãn `「認証待ち：{新メールアドレス}」` vẫn hiển thị cạnh ô email; ô textbox vẫn hiển thị email cũ | **High** |
| `[AD301-39]` | [8] メールアドレス | Đăng nhập portal bằng email cũ khi đang chờ xác thực | 1. Dùng email cũ đăng nhập cổng Agency BA100 2. Dùng email mới đăng nhập | - | 1. Email cũ đăng nhập thành công; Email mới chưa đăng nhập được | **High** |
| `[AD301-40]` | [8] メールアドレス | Xác thực thành công qua link mail PEM4 | 1. Mở mail PEM4 gửi đến email mới 2. Click link xác thực còn hạn (trong 7 ngày) | Link còn hạn 7 ngày | 1. Mở màn hình thông báo xác thực thành công; email mới chính thức có hiệu lực; nhãn 認証待ち biến mất; email cũ bị vô hiệu hóa | **High** |
| `[AD301-41]` | [8] メールアドレス | Quá hạn 7 ngày chưa xác thực email | 1. Kiểm tra sau khi link xác thực PEM4 quá 7 ngày | Link quá 7 ngày | 1. Yêu cầu đổi email tự động hết hạn, nhãn 認証待ち biến mất, email giữ nguyên giá trị cũ | **Medium** |
| `[AD301-42]` | [8] メールアドレス | Đổi email lần nữa khi đang chờ xác thực | 1. Đang có nhãn 認証待ち 2. Nhập một email mới thứ ba và bấm 保存 | - | 1. Link xác thực cũ bị vô hiệu, gửi PEM4 mới tới email thứ ba, nhãn cập nhật địa chỉ mới | **Medium** |
| `[AD301-43]` | [8] メールアドレス | Nhập lại email hiện tại để hủy yêu cầu xác thực | 1. Đang có nhãn 認証待ち 2. Nhập lại đúng email hiện tại và bấm 保存 | - | 1. Yêu cầu xác thực bị hủy, nhãn 認証待ち lập tức biến mất | **Medium** |
| `[AD301-44]` | [9] Reset Password | Check hiển thị nút [リセット] | 1. Quan sát khu vực ログインパスワードリセット | - | 1. Hiển thị nhãn 'ログインパスワードリセット' kèm nút bấm 'リセット' | **Low** |
| `[AD301-45]` | [9] Reset Password | Click nút [リセット] mở ô nhập mật khẩu | 1. Click nút [リセット] | - | 1. Hiển thị ô textbox để nhập mật khẩu mới cho Owner | **Medium** |
| `[AD301-46]` | [9] Reset Password | Nhập mật khẩu hợp lệ chuẩn CMR43 | 1. Nhập mật khẩu $\ge 8$ ký tự gồm chữ hoa, chữ thường, số, ký tự đặc biệt (VD: `Pass@2026Admin`) 2. Click 保存 | - | 1. Mật khẩu được ghi nhận; lưu thành công hiển thị CMMSG13 | **High** |
| `[AD301-47]` | [9] Reset Password | Chặn sai định dạng mật khẩu CMR43 | 1. Nhập mật khẩu thiếu chữ hoa hoặc ký tự đặc biệt (VD: `password123`) 2. Click 保存 | - | 1. Báo lỗi chuẩn dưới ô MSG13: パスワードは8文字以上で、英大文字・小文字・数字・記号をそれぞれ1文字以上含めてください。 | **High** |
| `[AD301-48]` | [9] Reset Password | Chặn trùng mật khẩu cũ gần nhất (CR 21/10/2026) | 1. Nhập mật khẩu mới trùng với mật khẩu hiện tại hoặc 2 mật khẩu gần nhất của Owner 2. Click 保存 | - | 1. Báo lỗi dưới ô MSG261: 過去2回以内に使用したパスワードは再利用できません。, không cho phép lưu | **High** |
| `[AD301-49]` | [9] Reset Password | Thu hồi phiên làm việc cưỡng chế đăng xuất | 1. Đặt mật khẩu mới thành công cho Owner và bấm 保存 | Owner đang đăng nhập portal BA100 trên thiết bị khác | 1. BE lập tức thu hồi token, mọi phiên làm việc hiện tại của Owner bị đăng xuất cưỡng chế; hạn 30 ngày tính lại từ lúc lưu (CMR68) | **High** |
| `[AD301-50]` | [9] Reset Password | Hủy thao tác reset khi bấm Cancel | 1. Bấm [リセット], nhập mật khẩu nhưng sau đó bấm nút [キャンセル] ở cuối trang | - | 1. Hủy bỏ việc đổi mật khẩu, mật khẩu cũ của Owner giữ nguyên hiệu lực | **Medium** |
| `[AD301-51]` | [10] ステータス | Check hiển thị 2 lựa chọn radio | 1. Quan sát mục ステータス | - | 1. Hiển thị 2 radio button: '利用中' (Active) và '停止中' (Inactive) | **Low** |
| `[AD301-52]` | [10] ステータス | Giữ nguyên trạng thái '利用中' | 1. Form đang là 利用中, chỉnh sửa thông tin khác 2. Bấm 保存 | - | 1. Lưu thành công mà không hiển thị cảnh báo MSG65 | **Medium** |
| `[AD301-53]` | [10] ステータス | Chọn '停止中' và bấm Lưu kích hoạt MSG65 | 1. Chọn radio button '停止中' 2. Click nút 保存 | - | 1. Hiển thị popup cảnh báo xác nhận MSG65: 利用を停止すると事務所に関連するユーザーも引き続き利用できます、よろしいですか。 kèm nút [キャンセル] và [OK] | **High** |
| `[AD301-54]` | [10] ステータス | Hủy chuyển sang '停止中' trên popup MSG65 | 1. Tại popup MSG65, click nút [キャンセル] | - | 1. Đóng popup, không thay đổi trạng thái Agency, giữ nguyên form AD301 | **Medium** |
| `[AD301-55]` | [10] ステータス | Xác nhận chuyển sang '停止中' | 1. Tại popup MSG65, click nút [OK/保存] | - | 1. Trạng thái chuyển thành 停止中; toàn bộ streamer trực thuộc trở thành tự do, đơn xin gia nhập bị hủy, admin agency không đăng nhập được; Agency bị grey out trên AD100 | **High** |
| `[AD301-56]` | [10] ステータス | Khôi phục lại trạng thái '利用中' từ '停止中' | 1. Agency đang ở trạng thái 停止中 2. Chọn lại radio '利用中' 3. Bấm 保存 | - | 1. Lưu thành công, Agency được kích hoạt hoạt động trở lại | **High** |
| `[AD301-57]` | [11] Button キャンセル | Hủy thay đổi khi chưa sửa gì | 1. Không thay đổi bất kỳ trường nào 2. Click nút キャンセル | - | 1. Điều hướng quay về danh sách Agency AD100 | **Low** |
| `[AD301-58]` | [11] Button キャンセル | Hủy thay đổi khi đã nhập dữ liệu mới | 1. Đã sửa một số trường thông tin 2. Click nút キャンセル | - | 1. Hiển thị dialog cảnh báo mất dữ liệu CMMSG46: 戻ってもよろしいですか？保存されていない変更は失われます。 | **Medium** |
| `[AD301-59]` | [11] Button 保存 | Debounce chống double-click (CMR15) | 1. Chỉnh sửa thông tin hợp lệ 2. Nhấp đúp liên tục vào nút 保存 | - | 1. Nút 保存 bị disable tạm thời (CMR15), chỉ gửi duy nhất 1 request cập nhật | **Medium** |
| `[AD301-60]` | [11] Button 保存 | Cập nhật thông tin thành công | 1. Chỉnh sửa các trường hợp lệ 2. Click nút 保存 | - | 1. Gọi API `PATCH /agency/{id}/`, hiển thị Toast CMMSG13: 正常に更新されました。 và cập nhật dữ liệu mới | **High** |
| `[AD301-61]` | [11] Button 削除 | Check hiển thị nút 削除 | 1. Quan sát nút 削除 ở cuối trang AD301 | - | 1. Hiển thị nút Danger màu đỏ nổi bật với text '削除' | **Medium** |
| `[AD301-62]` | [11] Button 削除 | Click nút 削除 hiển thị popup MSG66 | 1. Click nút [削除] | - | 1. Hiển thị popup xác nhận xóa với nội dung chuẩn MSG66: 削除すると事務所に関連するユーザーも引き続き利用できます、よろしいですか。 kèm 2 nút [キャンセル] và [削除] | **High** |
| `[AD301-63]` | [11] Button 削除 | Hủy thao tác xóa trên popup MSG66 | 1. Tại popup MSG66, click nút [キャンセル] | - | 1. Đóng popup, Agency không bị xóa, giữ nguyên dữ liệu trên màn hình AD301 | **Medium** |
| `[AD301-64]` | [11] Button 削除 | Xác nhận xóa Agency thành công | 1. Tại popup MSG66, click nút [削除] | - | 1. Gọi API `DELETE /agency/{id}/`, thực hiện xóa mềm Agency; hiển thị thông báo CMMSG14: 正常に削除されました。 và tự động chuyển về AD100 | **High** |
| `[AD301-65]` | [11] Button 削除 | Kiểm tra tác động sau khi xóa Agency | 1. Kiểm tra các tài khoản Liver trực thuộc Agency bị xóa 2. Kiểm tra tài khoản Agency Admin | - | 1. Tất cả member trở thành tự do (không trực thuộc agency); các request gia nhập chuyển thành từ chối; tài khoản admin agency bị xóa mềm không thể đăng nhập | **High** |
| | **III. SUB-LAYOUTS / MODALS** | | | | | |
| `[AD301-66]` | Modal & Popups | Check giao diện popup MSG65 | 1. Quan sát giao diện popup khi chọn 停止中 | - | 1. Popup hiển thị căn giữa, có icon cảnh báo, nội dung text MSG65 chuẩn Unicode không bị vỡ font | **Low** |
| `[AD301-67]` | Modal & Popups | Check giao diện popup MSG66 | 1. Quan sát giao diện popup khi bấm nút Xóa | - | 1. Popup hiển thị căn giữa, nút [削除] màu đỏ cảnh báo nguy hiểm, nút [キャンセル] viền xám | **Low** |
| `[AD301-68]` | Modal & Popups | Đóng popup bằng phím Esc hoặc click ngoài | 1. Mở popup MSG65 hoặc MSG66 2. Nhấn phím Esc trên bàn phím | - | 1. Popup tự động đóng lại an toàn, giữ nguyên màn hình AD301 | **Low** |
| `[AD301-69]` | Feedback & Toast | Check hiển thị Toast thông báo thành công | 1. Lưu thông tin Agency thành công | - | 1. Toast màu xanh xuất hiện góc trên/dưới màn hình với text CMMSG13, tự động biến mất sau 3 giây | **Low** |
| `[AD301-70]` | Error Handling | Xử lý khi mất mạng khi đang lưu | 1. Ngắt kết nối mạng Internet 2. Click nút 保存 | - | 1. Hiển thị thông báo lỗi mạng chuẩn CMMSG8: ネットワークエラー。接続を確認してください。 | **Medium** |
| `[AD301-71]` | Error Handling | Xử lý khi API trả về lỗi server 500 | 1. Giả lập API cập nhật trả về HTTP 500 | - | 1. Hiển thị thông báo CMMSG1: 予期しないサーバーエラーが発生しました。 kèm nút thử lại | **Medium** |
| `[AD301-72]` | Error Handling | Hết phiên làm việc khi đang sửa form | 1. Để phiên làm việc hết hạn 2. Click nút 保存 | - | 1. Báo lỗi hết hạn phiên CMMSG10 và chuyển hướng về trang đăng nhập Master Admin | **High** |
| `[AD301-73]` | Form Interaction | Chuyển đổi qua lại giữa các ô nhập | 1. Dùng phím Tab trên bàn phím chuyển đổi tuần tự qua các field | - | 1. Focus di chuyển tuần tự từ trên xuống dưới hợp lý, có viền highlight ô đang focus | **Low** |
| `[AD301-74]` | Phân quyền thao tác | Phân quyền nút Xóa và Reset Password | 1. Đăng nhập tài khoản Admin chỉ có quyền xem (Monitor) | - | 1. Các nút 保存, 削除, [リセット] bị ẩn hoặc disabled | **Medium** |
