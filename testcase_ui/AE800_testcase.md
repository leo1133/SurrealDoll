# BẢNG TEST CASE KIỂM THỬ GIAO DIỆN THỦ CÔNG (MANUAL UI TEST SUITE)
## Màn hình: AE800_User Detail - Revenue (Chi Tiết Doanh Thu Người Dùng)
### Áp dụng: Quy chuẩn Trụ cột 2 (02_manual_ui_test_case_rule.md) & Thư viện UI_controls

---

## BẢNG ĐIỀU KHIỂN TIẾN ĐỘ & THỐNG KÊ (DASHBOARD HEADER)

| Thuộc tính | Giá trị | Thuộc tính | Giá trị | Round 1 Metric | Kết quả | Round 2 Metric | Kết quả |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Module Code** | `AE800` | **Environment** | `PC` | **Pass** | 0 | **Pass** | 0 |
| **Total Testcases** | **183** | **% Executed** | 0% | **Fail** | 0 | **Fail** | 0 |
| **Plan to Execute** | **183** | **Creator** | `NgaDTP` | **Impact** | 0 | **Impact** | 0 |
| **Spec Source** | `Surreal SPEC` | **Google Sheet Tab** | `AE800_new` | **Not Run** | 183 | **Not Run** | 0 |
| | | | | **Total** | 183 | **Total** | 0 |

---

## CHI TIẾT BẢNG TEST CASES (7 CỘT CHUẨN MARKDOWN)

| ID | Title | Big item | Steps | Pre-condition | Expected | Priority |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| | **I. COMMON & NAVIGATION** | | | | | |
| `[AE800-1]` | [0] Kiểm tra truy cập màn hình | Check hiển thị menu | 1. Đăng nhập hệ thống Admin với quyền Master Admin. | User là Master Admin đăng nhập thành công. | 1. Menu Sidebar hiển thị đầy đủ các phân hệ quản trị. | **High** |
| `[AE800-2]` | [0] Kiểm tra truy cập màn hình | Check hiển thị menu | 1. Quan sát menu cha '利用者管理' trên Sidebar. | - | 1. Menu cha '利用者管理' ở trạng thái mở rộng (expanded). | **Medium** |
| `[AE800-3]` | [0] Kiểm tra truy cập màn hình | Check hiển thị menu | 1. Quan sát menu con '利用者一覧' trên Sidebar. | - | 1. Menu con '利用者一覧' được highlight active nổi bật. | **Medium** |
| `[AE800-4]` | [0] Kiểm tra truy cập màn hình | Check hiển thị breadcrumb | 1. Quan sát thanh Breadcrumb ở góc trên màn hình AE800. | - | 1. Hiển thị đúng chuỗi text: 'ホーム > 利用者一覧 > 利用者詳細 > 売上'. | **Medium** |
| `[AE800-5]` | [0] Kiểm tra truy cập màn hình | Check hiển thị breadcrumb | 1. Quan sát trạng thái liên kết của các cấp 'ホーム', '利用者一覧', '利用者詳細'. | - | 1. Hiển thị dạng hyperlink có gạch chân hoặc đổi màu khi hover, cho phép click. | **Medium** |
| `[AE800-6]` | [0] Kiểm tra truy cập màn hình | Check hiển thị breadcrumb | 1. Quan sát chữ '売上' ở cuối Breadcrumb. | - | 1. Hiển thị text tĩnh '売上', không có liên kết, con trỏ dạng default. | **Low** |
| `[AE800-7]` | [0] Kiểm tra truy cập màn hình | Check điều hướng breadcrumb | 1. Click [ホーム] trên Breadcrumb. | - | 1. Di chuyển về màn trang chủ Dashboard (AA000). | **Medium** |
| `[AE800-8]` | [0] Kiểm tra truy cập màn hình | Check điều hướng breadcrumb | 1. Click [利用者一覧] trên Breadcrumb. | - | 1. Di chuyển về màn danh sách người dùng AE100. | **High** |
| `[AE800-9]` | [0] Kiểm tra truy cập màn hình | Check điều hướng breadcrumb | 1. Kiểm tra trạng thái bộ lọc sau khi click [利用者一覧]. | - | 1. Bảo lưu nguyên vẹn điều kiện tìm kiếm trước đó tại màn AE100. | **Medium** |
| `[AE800-10]` | [0] Kiểm tra truy cập màn hình | Check điều hướng breadcrumb | 1. Click [利用者詳細] trên Breadcrumb. | - | 1. Di chuyển về màn chi tiết người dùng AE200 của user hiện tại. | **High** |
| `[AE800-11]` | [0] Kiểm tra truy cập màn hình | Check điều hướng breadcrumb | 1. Click vào chữ [売上] trên Breadcrumb. | - | 1. Ở nguyên màn AE800, không thực hiện reload trang. | **Low** |
| `[AE800-12]` | [0] Kiểm tra truy cập màn hình | Check điều hướng Inbound từ AE200 | 1. Click tab '売上' tại màn hình AE200 của user ID=474. | Bản ghi User ID=474 tồn tại trong hệ thống. | 1. Mở trang AE800 với URL chứa query param hợp lệ (VD: ?user_id=474). | **High** |
| `[AE800-13]` | [0] Kiểm tra truy cập màn hình | Check điều hướng Inbound từ AE200 | 1. Quan sát vùng thông tin tóm tắt người dùng ở đầu trang AE800. | - | 1. Tự động điền đúng Username và User ID tương ứng với tham số user_id từ URL. | **High** |
| `[AE800-14]` | [0] Kiểm tra truy cập màn hình | Check điều hướng Inbound từ AE200 | 1. Theo dõi Network request ngay khi trang AE800 tải xong. | - | 1. Tự động kích hoạt API tìm kiếm tải dữ liệu với user_id và thời gian mặc định. | **High** |
| `[AE800-15]` | [0] Kiểm tra truy cập màn hình | Check điều hướng Inbound từ AE200 | 1. Đối chiếu danh sách giao dịch hiển thị tại bảng 各取引の詳細. | - | 1. 100% bản ghi hiển thị khớp đúng với User ID tương ứng trên URL. | **High** |
| `[AE800-16]` | [0] Kiểm tra truy cập màn hình | Check điều hướng Inbound từ AE200 | 1. Quan sát 9 thẻ số liệu KPI tổng quan khi vừa tải trang. | - | 1. Cập nhật khối thẻ KPI phản ánh chính xác số liệu doanh thu của user trong kỳ. | **High** |
| `[AE800-17]` | [0] Kiểm tra truy cập màn hình | Check điều hướng Inbound từ AE200 | 1. Mở trang AE800 với URL chứa user_id không tồn tại (VD: ?user_id=999999). | - | 1. Bảng dữ liệu hiển thị thông báo căn giữa CMMSG47: 一致する検索結果はありません。 và các thẻ hiển thị 0. | **High** |
| `[AE800-18]` | [0] Kiểm tra truy cập màn hình | Check điều hướng Inbound từ AE200 | 1. Mở trang AE800 với URL không truyền tham số user_id (VD: /admin/users/revenue). | - | 1. Hệ thống báo lỗi hợp lệ hoặc tự động redirect về trang danh sách AE100. | **Medium** |
| `[AE800-19]` | [0] Kiểm tra truy cập màn hình | Check điều hướng Inbound từ AE200 | 1. Click nút Back của trình duyệt khi đang ở AE800. | - | 1. Di chuyển về màn AE200 của user tương ứng và bảo lưu dữ liệu trước đó. | **High** |
| `[AE800-20]` | [0] Kiểm tra truy cập màn hình | Check Screen Lifecycle | 1. Nhấn phím F5 trên trình duyệt khi đang xem trang AE800. | - | 1. Trang web tải lại thành công, bảo lưu nguyên vẹn param user_id và dữ liệu đang xem. | **Medium** |
| `[AE800-21]` | [0] Kiểm tra truy cập màn hình | Check Screen Lifecycle | 1. Quan sát tiêu đề trang AE800 sau khi tải xong. | - | 1. Hiển thị text tiêu đề '売上管理_売上'. | **Medium** |
| | **II. MAIN SCREEN CONTROLS** | | | | | |
| `[AE800-22]` | [1] 期間 | Check hiển thị & Giá trị mặc định | 1. Quan sát nhãn '期間'. | - | 1. Hiển thị text '期間'. | **Low** |
| `[AE800-23]` | [1] 期間 | Check hiển thị & Giá trị mặc định | 1. Quan sát 2 ô nhập ngày và ký tự '~' ở giữa. | - | 1. Hiển thị 2 ô input Datepicker kèm ký tự '~' ở giữa và icon lịch. | **Low** |
| `[AE800-24]` | [1] 期間 | Check hiển thị & Giá trị mặc định | 1. Quan sát giá trị ban đầu tại ô Từ ngày (Start Date). | - | 1. Hiển thị ngày 01 của tháng trước theo giờ JST theo định dạng YYYY/MM/DD. | **High** |
| `[AE800-25]` | [1] 期間 | Check hiển thị & Giá trị mặc định | 1. Quan sát giá trị ban đầu tại ô Đến ngày (End Date). | - | 1. Hiển thị ngày cuối cùng của tháng trước theo giờ JST theo định dạng YYYY/MM/DD. | **High** |
| `[AE800-26]` | [1] 期間 | Check chọn ngày qua popup lịch | 1. Click vào icon lịch ô Từ ngày. | - | 1. Popup lịch mở ra trực quan hiển thị tháng và năm hiện tại. | **Medium** |
| `[AE800-27]` | [1] 期間 | Check chọn ngày qua popup lịch | 1. Click chọn ngày 2026/08/01 trên popup lịch ô Từ ngày. | - | 1. Ô Từ ngày tiếp nhận giá trị '2026/08/01' và popup lịch tự động đóng lại. | **High** |
| `[AE800-28]` | [1] 期間 | Check chọn ngày qua popup lịch | 1. Click chọn ngày 2026/08/31 trên popup lịch ô Đến ngày. | - | 1. Ô Đến ngày tiếp nhận giá trị '2026/08/31' và popup lịch tự động đóng lại. | **High** |
| `[AE800-29]` | [1] 期間 | Check chọn ngày qua popup lịch | 1. Chọn Từ ngày và Đến ngày cùng là ngày 2026/08/15. | - | 1. Hệ thống cho phép chọn, tìm kiếm dữ liệu từ 00:00:00 đến 23:59:59 của ngày 2026/08/15. | **Medium** |
| `[AE800-30]` | [1] 期間 | Check chọn ngày qua popup lịch | 1. Chọn Từ ngày = 2026/08/20 và mở popup lịch ô Đến ngày. | - | 1. Trên popup lịch ô Đến ngày, các ngày trước 2026/08/20 bị làm mờ (disabled) không cho chọn theo CMR38. | **High** |
| `[AE800-31]` | [1] 期間 | Check chọn ngày qua popup lịch | 1. Click ra vùng trống bên ngoài khi popup lịch đang mở. | - | 1. Popup lịch tự động đóng lại và giữ nguyên giá trị trước đó. | **Low** |
| `[AE800-32]` | [1] 期間 | Check nhập liệu bàn phím & validation | 1. Thực hiện nhập ký tự là '2026/07/01' vào ô Từ ngày. | - | 1. Hệ thống cho phép nhập đúng định dạng YYYY/MM/DD. | **Medium** |
| `[AE800-33]` | [1] 期間 | Check nhập liệu bàn phím & validation | 1. Thực hiện nhập ký tự là chữ 'abcde' vào ô ngày. | - | 1. Hệ thống tự động ngăn chặn nhập ký tự chữ theo CMR04 (blocking UX). | **Low** |
| `[AE800-34]` | [1] 期間 | Check nhập liệu bàn phím & validation | 1. Thực hiện nhập ký tự đặc biệt '@#$%^' vào ô ngày. | - | 1. Hệ thống tự động ngăn chặn nhập ký tự đặc biệt theo CMR04. | **Low** |
| `[AE800-35]` | [1] 期間 | Check nhập liệu bàn phím & validation | 1. Thực hiện nhập ngày không tồn tại là '2026/02/31' và click [検索]. | - | 1. Hiển thị thông báo lỗi CMMSG36: 期間の日付の形式が無効です。正しい形式を使用してください（例：DD/MM/YYYY）。 | **Medium** |
| `[AE800-36]` | [1] 期間 | Check nhập liệu bàn phím & validation | 1. Thực hiện nhập tay Từ ngày = '2026/08/20' và Đến ngày = '2026/08/10' rồi click [検索]. | - | 1. Hiển thị thông báo lỗi CMMSG39: 期間の開始日は終了日より前でなければなりません。 | **High** |
| `[AE800-37]` | [1] 期間 | Check nhập liệu bàn phím & validation | 1. Thực hiện paste chuỗi ký tự '  2026/08/10  ' có khoảng trắng ở đầu và cuối vào ô ngày. | - | 1. Hệ thống tự động trim khoảng trắng thừa và tiếp nhận giá trị '2026/08/10'. | **Low** |
| `[AE800-38]` | [1] 期間 | Check nhập liệu bàn phím & validation | 1. Xóa toàn bộ nội dung trong ô Từ ngày hoặc Đến ngày. | - | 1. Ô input trở về trạng thái trống, khi tìm kiếm hệ thống không giới hạn mốc thời gian đã xóa. | **Medium** |
| `[AE800-39]` | [2] 今日 / 昨日 / 今週 / 今月 / 先月 | Check hiển thị | 1. Quan sát nhóm 5 nút chọn nhanh thời gian. | - | 1. Hiển thị đầy đủ 5 nút: '昨日', '今日', '今週', '今月', '先月'. | **Low** |
| `[AE800-40]` | [2] 今日 / 昨日 / 今週 / 今月 / 先月 | Check click nút | 1. Click [昨日]. | - | 1. Ô Từ ngày và Đến ngày tự động điền ngày hôm qua (00:00:00 ~ 23:59:59 JST). | **Medium** |
| `[AE800-41]` | [2] 今日 / 昨日 / 今週 / 今月 / 先月 | Check click nút | 1. Click [今日]. | - | 1. Ô Từ ngày và Đến ngày tự động điền ngày hôm nay (00:00:00 ~ 23:59:59 JST). | **Medium** |
| `[AE800-42]` | [2] 今日 / 昨日 / 今週 / 今月 / 先月 | Check click nút | 1. Click [今週]. | - | 1. Ô Từ ngày tự động điền Thứ Hai đầu tuần hiện tại, Đến ngày điền Chủ Nhật cuối tuần hiện tại. | **Medium** |
| `[AE800-43]` | [2] 今日 / 昨日 / 今週 / 今月 / 先月 | Check click nút | 1. Click [今月]. | - | 1. Ô Từ ngày tự động điền ngày 01 tháng hiện tại, Đến ngày điền ngày cuối cùng của tháng hiện tại. | **Medium** |
| `[AE800-44]` | [2] 今日 / 昨日 / 今週 / 今月 / 先月 | Check click nút | 1. Click [先月]. | - | 1. Ô Từ ngày tự động điền ngày 01 tháng trước, Đến ngày điền ngày cuối cùng tháng trước. | **Medium** |
| `[AE800-45]` | [2] 今日 / 昨日 / 今週 / 今月 / 先月 | Check click nút | 1. Quan sát trạng thái active của nút vừa click. | - | 1. Nút vừa click được highlight active nổi bật so với các nút còn lại. | **Low** |
| `[AE800-46]` | [3] 全サービス | Check hiển thị | 1. Quan sát dropdown [3] ở trạng thái mặc định. | - | 1. Hiển thị text mặc định '全サービス' kèm icon mũi tên xổ xuống. | **Low** |
| `[AE800-47]` | [3] 全サービス | Check hiển thị | 1. Click vào dropdown [3] để mở danh sách tùy chọn. | - | 1. Danh sách xổ xuống hiển thị đầy đủ 9 options tiếng Nhật đúng thứ tự Spec. | **Medium** |
| `[AE800-48]` | [3] 全サービス | Check chọn từng option | 1. Click chọn option '全サービス'. | - | 1. Dropdown đóng lại, ô hiển thị text '全サービス'. | **Medium** |
| `[AE800-49]` | [3] 全サービス | Check chọn từng option | 1. Click chọn option 'ウィスパー'. | - | 1. Dropdown đóng lại, ô hiển thị text 'ウィスパー'. | **Medium** |
| `[AE800-50]` | [3] 全サービス | Check chọn từng option | 1. Click chọn option 'ギフト'. | - | 1. Dropdown đóng lại, ô hiển thị text 'ギフト'. | **Medium** |
| `[AE800-51]` | [3] 全サービス | Check chọn từng option | 1. Click chọn option 'ギフトガチャ'. | - | 1. Dropdown đóng lại, ô hiển thị text 'ギフトガチャ'. | **Medium** |
| `[AE800-52]` | [3] 全サービス | Check chọn từng option | 1. Click chọn option '2ショットチケット消費'. | - | 1. Dropdown đóng lại, ô hiển thị text '2ショットチケット消費'. | **Medium** |
| `[AE800-53]` | [3] 全サービス | Check chọn từng option | 1. Click chọn option '宝箱'. | - | 1. Dropdown đóng lại, ô hiển thị text '宝箱'. | **Medium** |
| `[AE800-54]` | [3] 全サービス | Check chọn từng option | 1. Click chọn option 'クラス参加'. | - | 1. Dropdown đóng lại, ô hiển thị text 'クラス参加'. | **Medium** |
| `[AE800-55]` | [3] 全サービス | Check chọn từng option | 1. Click chọn option 'バックナンバー購入'. | - | 1. Dropdown đóng lại, ô hiển thị text 'バックナンバー購入'. | **Medium** |
| `[AE800-56]` | [3] 全サービス | Check chọn từng option | 1. Click chọn option 'エール'. | - | 1. Dropdown đóng lại, ô hiển thị text 'エール'. | **Medium** |
| `[AE800-57]` | [3] 全サービス | Check đóng khi click ngoài | 1. Click ra vùng trống bên ngoài dropdown khi danh sách đang mở. | - | 1. Danh sách tự động đóng lại và giữ nguyên option đã chọn trước đó. | **Low** |
| `[AE800-58]` | [4] 全獲得種別 | Check hiển thị | 1. Quan sát dropdown [4] ở trạng thái mặc định. | - | 1. Hiển thị text mặc định '全獲得種別' kèm icon mũi tên xổ xuống. | **Low** |
| `[AE800-59]` | [4] 全獲得種別 | Check chọn từng option | 1. Click chọn option '全獲得種別'. | - | 1. Dropdown đóng lại, ô hiển thị text '全獲得種別'. | **Medium** |
| `[AE800-60]` | [4] 全獲得種別 | Check chọn từng option | 1. Click chọn option 'ポイント'. | - | 1. Dropdown đóng lại, ô hiển thị text 'ポイント'. | **Medium** |
| `[AE800-61]` | [4] 全獲得種別 | Check chọn từng option | 1. Click chọn option 'ギフトポイント'. | - | 1. Dropdown đóng lại, ô hiển thị text 'ギフトポイント'. | **Medium** |
| `[AE800-62]` | [4] 全獲得種別 | Check chọn từng option | 1. Click chọn option 'ファミリア売上'. | - | 1. Dropdown đóng lại, ô hiển thị text 'ファミリア売上'. | **Medium** |
| `[AE800-63]` | [4] 全獲得種別 | Check phụ thuộc động (Cascade) | 1. Chọn Item 3 = '全サービス' và mở dropdown Item 4. | - | 1. Danh sách Item 4 chỉ hiển thị đúng 4 options: 全獲得種別, ポイント, ギフトポイント, ファミリア売上. | **High** |
| `[AE800-64]` | [4] 全獲得種別 | Check phụ thuộc động (Cascade) | 1. Chọn Item 3 = 'ウィスパー' và mở dropdown Item 4. | - | 1. Danh sách Item 4 chỉ hiển thị đúng 3 options: 全獲得種別, ポイント, ギフトポイント. | **High** |
| `[AE800-65]` | [4] 全獲得種別 | Check phụ thuộc động (Cascade) | 1. Chọn Item 3 = 'ギフト' và mở dropdown Item 4. | - | 1. Danh sách Item 4 chỉ hiển thị đúng 3 options: 全獲得種別, ポイント, ギフトポイント. | **Medium** |
| `[AE800-66]` | [4] 全獲得種別 | Check phụ thuộc động (Cascade) | 1. Chọn Item 3 = 'ギフトガチャ' và mở dropdown Item 4. | - | 1. Danh sách Item 4 chỉ hiển thị đúng 3 options: 全獲得種別, ポイント, ギフトポイント. | **Medium** |
| `[AE800-67]` | [4] 全獲得種別 | Check phụ thuộc động (Cascade) | 1. Chọn Item 3 = '2ショットチケット消費' và mở dropdown Item 4. | - | 1. Danh sách Item 4 chỉ hiển thị đúng 3 options: 全獲得種別, ポイント, ギフトポイント. | **Medium** |
| `[AE800-68]` | [4] 全獲得種別 | Check phụ thuộc động (Cascade) | 1. Chọn Item 3 = '宝箱' và mở dropdown Item 4. | - | 1. Danh sách Item 4 chỉ hiển thị đúng 3 options: 全獲得種別, ポイント, ギフトポイント. | **Medium** |
| `[AE800-69]` | [4] 全獲得種別 | Check phụ thuộc động (Cascade) | 1. Chọn Item 3 = 'クラス参加' và mở dropdown Item 4. | - | 1. Danh sách Item 4 chỉ hiển thị đúng 2 options: 全獲得種別, ファミリア売上. | **High** |
| `[AE800-70]` | [4] 全獲得種別 | Check phụ thuộc động (Cascade) | 1. Chọn Item 3 = 'バックナンバー購入' và mở dropdown Item 4. | - | 1. Danh sách Item 4 chỉ hiển thị đúng 2 options: 全獲得種別, ファミリア売上. | **High** |
| `[AE800-71]` | [4] 全獲得種別 | Check phụ thuộc động (Cascade) | 1. Chọn Item 3 = 'エール' và mở dropdown Item 4. | - | 1. Danh sách Item 4 chỉ hiển thị đúng 3 options: 全獲得種別, ギフトポイント, ファミリア売上. | **High** |
| `[AE800-72]` | [4] 全獲得種別 | Check quy tắc Auto-switch | 1. Đang chọn Item 4 = 'ポイント', đổi Item 3 sang 'クラス参加' (loại chỉ có familia). | - | 1. Item 4 tự động chuyển từ 'ポイント' sang 'ファミリア売上' (hoặc 全獲得種別) theo Spec. | **High** |
| `[AE800-73]` | [4] 全獲得種別 | Check quy tắc Auto-switch | 1. Đang chọn Item 4 = 'ポイント', đổi Item 3 sang 'エール' (loại chỉ có GP + familia). | - | 1. Item 4 tự động chuyển từ 'ポイント' sang 'ギフトポイント' (hoặc 全獲得種別). | **High** |
| `[AE800-74]` | [4] 全獲得種別 | Check quy tắc Auto-switch | 1. Đang chọn Item 4 = 'ファミリア売上', đổi Item 3 sang 'ウィスパー' (loại chỉ có P + GP). | - | 1. Item 4 tự động chuyển từ 'ファミリア売上' sang '全獲得種別' (hoặc ポイント). | **High** |
| `[AE800-75]` | [4] 全獲得種別 | Check đóng khi click ngoài | 1. Click ra vùng trống bên ngoài dropdown [4] khi danh sách đang mở. | - | 1. Danh sách tự động đóng lại và giữ nguyên giá trị đã chọn. | **Low** |
| `[AE800-76]` | [5] 検索 | Check hiển thị | 1. Quan sát nút [検索]. | - | 1. Hiển thị text '検索', dạng Primary Button nổi bật, con trỏ chuột dạng Pointer. | **Low** |
| `[AE800-77]` | [5] 検索 | Check thực hiện tìm kiếm | 1. Click [検索] với điều kiện mặc định ban đầu. | - | 1. Hệ thống gọi API tìm kiếm, bảng tải danh sách giao dịch tháng trước của user. | **High** |
| `[AE800-78]` | [5] 検索 | Check thực hiện tìm kiếm | 1. Thay đổi khoảng thời gian và click [検索]. | - | 1. Bảng tải danh sách giao dịch phát sinh trong khoảng thời gian vừa chọn. | **High** |
| `[AE800-79]` | [5] 検索 | Check thực hiện tìm kiếm | 1. Chọn dịch vụ = 'ギフト' và click [検索]. | - | 1. Bảng chỉ hiển thị các giao dịch tặng quà (Gift). | **High** |
| `[AE800-80]` | [5] 検索 | Check thực hiện tìm kiếm | 1. Chọn loại tiền = 'ポイント' và click [検索]. | - | 1. Bảng chỉ hiển thị các giao dịch thanh toán bằng Point (P). | **High** |
| `[AE800-81]` | [5] 検索 | Check thực hiện tìm kiếm | 1. Kết hợp lọc Ngày + Dịch vụ 'ギフト' + Loại tiền 'ギフトポイント' và click [検索]. | - | 1. Dữ liệu bảng lọc chính xác theo đồng thời 3 điều kiện (Logic AND). | **High** |
| `[AE800-82]` | [5] 検索 | Check Debounce & Loading | 1. Thực hiện click liên tục 2 lần (double-click) vào nút [検索]. | - | 1. Nút tạm thời bị vô hiệu hóa (disabled) trong khi API đang gọi theo CMR15 (Debounce), chống gửi trùng request. | **High** |
| `[AE800-83]` | [5] 検索 | Check Debounce & Loading | 1. Theo dõi giao diện trong suốt thời gian API tìm kiếm đang phản hồi. | - | 1. Hiển thị hiệu ứng Loading spinner hoặc thông báo CMMSG27: 読み込み中、しばらくお待ちください... trên vùng bảng. | **Medium** |
| `[AE800-84]` | [6] クリア | Check hiển thị | 1. Quan sát nút [クリア]. | - | 1. Hiển thị text 'クリア', dạng Secondary/Ghost Button. | **Low** |
| `[AE800-85]` | [6] クリア | Check click nút | 1. Thay đổi các bộ lọc (Ngày, Dịch vụ, Loại tiền), sau đó click [クリア]. | - | 1. Toàn bộ các ô bộ lọc tự động khôi phục về giá trị mặc định ban đầu. | **High** |
| `[AE800-86]` | [6] クリア | Check click nút | 1. Quan sát bảng dữ liệu ngay sau khi click [クリア]. | - | 1. Hệ thống tự động kích hoạt tìm kiếm và tải lại dữ liệu mặc định của bảng mà không cần bấm 検索. | **High** |
| `[AE800-87]` | [7] 総売上（円）：{amount} | Check hiển thị | 1. Quan sát nhãn của [7] 総売上（円）：{amount}. | - | 1. Hiển thị text nhãn '総売上（円）：' kèm con số số liệu. | **Low** |
| `[AE800-88]` | [7] 総売上（円）：{amount} | Check định dạng | 1. Quan sát định dạng số liệu trên [7] 総売上（円）：{amount}. | - | 1. Định dạng phân cách hàng nghìn bằng dấu phẩy ',' (VD: 1,500,000). | **Medium** |
| `[AE800-89]` | [7] 総売上（円）：{amount} | Check tính toán | 1. Đối chiếu số liệu [7] 総売上（円）：{amount} với công thức nghiệp vụ Spec. | - | 1. Khớp chính xác 100%: tổng doanh thu của tất cả các giao dịch sử dụng Point/Yên trong kỳ lọc (Thẻ 7 = Thẻ 8 + Thẻ 9 + Thẻ 10). | **High** |
| `[AE800-90]` | [7] 総売上（円）：{amount} | Check giá trị biên | 1. Khi khoảng thời gian lọc không phát sinh bất kỳ số liệu nào. | - | 1. Thẻ hiển thị số 0: '総売上（円）：0', tuyệt đối không để trống ô số liệu. | **Medium** |
| `[AE800-91]` | [7] 総売上（円）：{amount} | Check phản ứng | 1. Thay đổi dải ngày tìm kiếm và click [検索]. | - | 1. Số liệu [7] 総売上（円）：{amount} tự động tính toán lại tức thì phản ánh đúng kỳ mới. | **High** |
| `[AE800-92]` | [8] 総カラオケ配信以外売上（円）：{amount} | Check hiển thị | 1. Quan sát nhãn của [8] 総カラオケ配信以外売上（円）：{amount}. | - | 1. Hiển thị text nhãn '総カラオケ配信以外売上（円）：' kèm con số số liệu. | **Low** |
| `[AE800-93]` | [8] 総カラオケ配信以外売上（円）：{amount} | Check định dạng | 1. Quan sát định dạng số liệu trên [8] 総カラオケ配信以外売上（円）：{amount}. | - | 1. Định dạng phân cách hàng nghìn bằng dấu phẩy ',' (VD: 1,500,000). | **Medium** |
| `[AE800-94]` | [8] 総カラオケ配信以外売上（円）：{amount} | Check tính toán | 1. Đối chiếu số liệu [8] 総カラオケ配信以外売上（円）：{amount} với công thức nghiệp vụ Spec. | - | 1. Khớp chính xác 100%: tổng doanh thu các giao dịch thường không thuộc livestream karaoke và không thuộc familia (khớp tổng cột 25). | **High** |
| `[AE800-95]` | [8] 総カラオケ配信以外売上（円）：{amount} | Check giá trị biên | 1. Khi khoảng thời gian lọc không phát sinh bất kỳ số liệu nào. | - | 1. Thẻ hiển thị số 0: '総カラオケ配信以外売上（円）：0', tuyệt đối không để trống ô số liệu. | **Medium** |
| `[AE800-96]` | [8] 総カラオケ配信以外売上（円）：{amount} | Check phản ứng | 1. Thay đổi dải ngày tìm kiếm và click [検索]. | - | 1. Số liệu [8] 総カラオケ配信以外売上（円）：{amount} tự động tính toán lại tức thì phản ánh đúng kỳ mới. | **High** |
| `[AE800-97]` | [9] 総カラオケ配信売上（円）：{amount} | Check hiển thị | 1. Quan sát nhãn của [9] 総カラオケ配信売上（円）：{amount}. | - | 1. Hiển thị text nhãn '総カラオケ配信売上（円）：' kèm con số số liệu. | **Low** |
| `[AE800-98]` | [9] 総カラオケ配信売上（円）：{amount} | Check định dạng | 1. Quan sát định dạng số liệu trên [9] 総カラオケ配信売上（円）：{amount}. | - | 1. Định dạng phân cách hàng nghìn bằng dấu phẩy ',' (VD: 1,500,000). | **Medium** |
| `[AE800-99]` | [9] 総カラオケ配信売上（円）：{amount} | Check tính toán | 1. Đối chiếu số liệu [9] 総カラオケ配信売上（円）：{amount} với công thức nghiệp vụ Spec. | - | 1. Khớp chính xác 100%: tổng doanh thu phát sinh từ các buổi livestream có tính năng Karaoke (khớp tổng cột 26). | **High** |
| `[AE800-100]` | [9] 総カラオケ配信売上（円）：{amount} | Check giá trị biên | 1. Khi khoảng thời gian lọc không phát sinh bất kỳ số liệu nào. | - | 1. Thẻ hiển thị số 0: '総カラオケ配信売上（円）：0', tuyệt đối không để trống ô số liệu. | **Medium** |
| `[AE800-101]` | [9] 総カラオケ配信売上（円）：{amount} | Check phản ứng | 1. Thay đổi dải ngày tìm kiếm và click [検索]. | - | 1. Số liệu [9] 総カラオケ配信売上（円）：{amount} tự động tính toán lại tức thì phản ánh đúng kỳ mới. | **High** |
| `[AE800-102]` | [10] 総ファミリア売上（円）：{amount} | Check hiển thị | 1. Quan sát nhãn của [10] 総ファミリア売上（円）：{amount}. | - | 1. Hiển thị text nhãn '総ファミリア売上（円）：' kèm con số số liệu. | **Low** |
| `[AE800-103]` | [10] 総ファミリア売上（円）：{amount} | Check định dạng | 1. Quan sát định dạng số liệu trên [10] 総ファミリア売上（円）：{amount}. | - | 1. Định dạng phân cách hàng nghìn bằng dấu phẩy ',' (VD: 1,500,000). | **Medium** |
| `[AE800-104]` | [10] 総ファミリア売上（円）：{amount} | Check tính toán | 1. Đối chiếu số liệu [10] 総ファミリア売上（円）：{amount} với công thức nghiệp vụ Spec. | - | 1. Khớp chính xác 100%: tổng doanh thu phát sinh từ mua Class và mua Backnumber (khớp tổng cột 27). | **High** |
| `[AE800-105]` | [10] 総ファミリア売上（円）：{amount} | Check giá trị biên | 1. Khi khoảng thời gian lọc không phát sinh bất kỳ số liệu nào. | - | 1. Thẻ hiển thị số 0: '総ファミリア売上（円）：0', tuyệt đối không để trống ô số liệu. | **Medium** |
| `[AE800-106]` | [10] 総ファミリア売上（円）：{amount} | Check phản ứng | 1. Thay đổi dải ngày tìm kiếm và click [検索]. | - | 1. Số liệu [10] 総ファミリア売上（円）：{amount} tự động tính toán lại tức thì phản ánh đúng kỳ mới. | **High** |
| `[AE800-107]` | [11] 総ポイント売上（P＋GP） | Check hiển thị | 1. Quan sát nhãn của [11] 総ポイント売上（P＋GP）. | - | 1. Hiển thị text nhãn '総ポイント売上（P＋GP）：' kèm con số số liệu. | **Low** |
| `[AE800-108]` | [11] 総ポイント売上（P＋GP） | Check định dạng | 1. Quan sát định dạng số liệu trên [11] 総ポイント売上（P＋GP）. | - | 1. Định dạng phân cách hàng nghìn bằng dấu phẩy ',' (VD: 1,500,000). | **Medium** |
| `[AE800-109]` | [11] 総ポイント売上（P＋GP） | Check tính toán | 1. Đối chiếu số liệu [11] 総ポイント売上（P＋GP） với công thức nghiệp vụ Spec. | - | 1. Khớp chính xác 100%: tổng của Thẻ 12 (P) + Thẻ 13 (GP), bằng tổng số P và GP viewer đã tặng cho user. | **High** |
| `[AE800-110]` | [11] 総ポイント売上（P＋GP） | Check giá trị biên | 1. Khi khoảng thời gian lọc không phát sinh bất kỳ số liệu nào. | - | 1. Thẻ hiển thị số 0: '総ポイント売上（P＋GP）：0', tuyệt đối không để trống ô số liệu. | **Medium** |
| `[AE800-111]` | [11] 総ポイント売上（P＋GP） | Check phản ứng | 1. Thay đổi dải ngày tìm kiếm và click [検索]. | - | 1. Số liệu [11] 総ポイント売上（P＋GP） tự động tính toán lại tức thì phản ánh đúng kỳ mới. | **High** |
| `[AE800-112]` | [12] 総ポイント売上（P） | Check hiển thị | 1. Quan sát nhãn của [12] 総ポイント売上（P）. | - | 1. Hiển thị text nhãn '総ポイント売上（P）：' kèm con số số liệu. | **Low** |
| `[AE800-113]` | [12] 総ポイント売上（P） | Check định dạng | 1. Quan sát định dạng số liệu trên [12] 総ポイント売上（P）. | - | 1. Định dạng phân cách hàng nghìn bằng dấu phẩy ',' (VD: 1,500,000). | **Medium** |
| `[AE800-114]` | [12] 総ポイント売上（P） | Check tính toán | 1. Đối chiếu số liệu [12] 総ポイント売上（P） với công thức nghiệp vụ Spec. | - | 1. Khớp chính xác 100%: tổng số Point (P) mà viewer đã tặng cho user trong kỳ. | **High** |
| `[AE800-115]` | [12] 総ポイント売上（P） | Check giá trị biên | 1. Khi khoảng thời gian lọc không phát sinh bất kỳ số liệu nào. | - | 1. Thẻ hiển thị số 0: '総ポイント売上（P）：0', tuyệt đối không để trống ô số liệu. | **Medium** |
| `[AE800-116]` | [12] 総ポイント売上（P） | Check phản ứng | 1. Thay đổi dải ngày tìm kiếm và click [検索]. | - | 1. Số liệu [12] 総ポイント売上（P） tự động tính toán lại tức thì phản ánh đúng kỳ mới. | **High** |
| `[AE800-117]` | [13] 総ポイント売上（GP） | Check hiển thị | 1. Quan sát nhãn của [13] 総ポイント売上（GP）. | - | 1. Hiển thị text nhãn '総ポイント売上（GP）：' kèm con số số liệu. | **Low** |
| `[AE800-118]` | [13] 総ポイント売上（GP） | Check định dạng | 1. Quan sát định dạng số liệu trên [13] 総ポイント売上（GP）. | - | 1. Định dạng phân cách hàng nghìn bằng dấu phẩy ',' (VD: 1,500,000). | **Medium** |
| `[AE800-119]` | [13] 総ポイント売上（GP） | Check tính toán | 1. Đối chiếu số liệu [13] 総ポイント売上（GP） với công thức nghiệp vụ Spec. | - | 1. Khớp chính xác 100%: tổng số Gift Point (GP) mà viewer đã tặng cho user trong kỳ. | **High** |
| `[AE800-120]` | [13] 総ポイント売上（GP） | Check giá trị biên | 1. Khi khoảng thời gian lọc không phát sinh bất kỳ số liệu nào. | - | 1. Thẻ hiển thị số 0: '総ポイント売上（GP）：0', tuyệt đối không để trống ô số liệu. | **Medium** |
| `[AE800-121]` | [13] 総ポイント売上（GP） | Check phản ứng | 1. Thay đổi dải ngày tìm kiếm và click [検索]. | - | 1. Số liệu [13] 総ポイント売上（GP） tự động tính toán lại tức thì phản ánh đúng kỳ mới. | **High** |
| `[AE800-122]` | [14] 総獲得GOLD（G） | Check hiển thị | 1. Quan sát nhãn của thẻ [14]. | - | 1. Hiển thị text nhãn '総獲得GOLD（G）：' kèm số lượng GOLD. | **Low** |
| `[AE800-123]` | [14] 総獲得GOLD（G） | Check định dạng | 1. Quan sát định dạng số lượng GOLD trên thẻ [14]. | - | 1. Định dạng phân cách hàng nghìn bằng dấu phẩy ','. | **Low** |
| `[AE800-124]` | [14] 総獲得GOLD（G） | Check tính toán & RBAC Streamer tự do | 1. Xem màn hình AE800 của Streamer tự do (không thuộc agency) và đối chiếu với tổng cột [28] (GOLD). | User là Streamer tự do. | 1. Khớp 100% tổng số GOLD streamer thực nhận theo tỷ lệ thưởng cá nhân tương ứng. | **High** |
| `[AE800-125]` | [14] 総獲得GOLD（G） | Check tính toán & RBAC Streamer Agency | 1. Xem màn hình AE800 của Streamer trực thuộc một Agency. | User là Streamer thuộc Agency. | 1. Thẻ [14] hiển thị số 0 (hoặc ký tự 'ー' theo spec) vì điểm thưởng được tính cho Agency tại thẻ [15]. | **High** |
| `[AE800-126]` | [14] 総獲得GOLD（G） | Check giá trị biên | 1. Khi streamer tự do không có giao dịch nào trong kỳ lọc. | User là Streamer tự do. | 1. Thẻ [14] hiển thị số 0: '総獲得GOLD（G）：0'. | **Medium** |
| `[AE800-127]` | [14] 総獲得GOLD（G） | Check phản ứng | 1. Thay đổi bộ lọc và click [検索]. | - | 1. Thẻ [14] tự động cập nhật lại số liệu tức thì. | **Medium** |
| `[AE800-128]` | [15] 総事務所獲得ポイント（P） | Check hiển thị | 1. Quan sát nhãn của thẻ [15]. | - | 1. Hiển thị text nhãn '総事務所獲得ポイント（P）：' kèm số point. | **Low** |
| `[AE800-129]` | [15] 総事務所獲得ポイント（P） | Check định dạng | 1. Quan sát định dạng số point trên thẻ [15]. | - | 1. Định dạng phân cách hàng nghìn bằng dấu phẩy ','. | **Low** |
| `[AE800-130]` | [15] 総事務所獲得ポイント（P） | Check tính toán & RBAC Streamer Agency | 1. Xem màn hình AE800 của Streamer trực thuộc Agency và đối chiếu với tổng cột [30] (事務所獲得ポイント). | User là Streamer trực thuộc Agency. | 1. Khớp 100% tổng số point Agency nhận được: livestream = số P/GP viewer tặng; familia = giá tiền do streamer setup quy đổi sang point. | **High** |
| `[AE800-131]` | [15] 総事務所獲得ポイント（P） | Check tính toán & RBAC Streamer tự do | 1. Xem màn hình AE800 của Streamer tự do (không thuộc agency). | User là Streamer tự do. | 1. Thẻ [15] hiển thị số 0 (hoặc 'ー') vì không phát sinh điểm thưởng cho công ty quản lý. | **High** |
| `[AE800-132]` | [15] 総事務所獲得ポイント（P） | Check giá trị biên | 1. Khi streamer thuộc agency không có giao dịch nào trong kỳ lọc. | User là Streamer thuộc Agency. | 1. Thẻ [15] hiển thị số 0: '総事務所獲得ポイント（P）：0'. | **Medium** |
| `[AE800-133]` | [15] 総事務所獲得ポイント（P） | Check phản ứng | 1. Thay đổi bộ lọc và click [検索]. | - | 1. Thẻ [15] tự động cập nhật lại số liệu tức thì. | **Medium** |
| `[AE800-134]` | [-] Bảng 各取引の詳細 & Batch update | Check hiển thị tiêu đề bảng | 1. Quan sát tiêu đề bảng giao dịch. | - | 1. Hiển thị text '各取引の詳細' theo chuẩn CMR03. | **Low** |
| `[AE800-135]` | [-] Bảng 各取引の詳細 & Batch update | Check hiển thị thời gian chạy batch | 1. Quan sát dòng text ghi chú thời gian cập nhật bên cạnh tiêu đề bảng. | - | 1. Hiển thị text format '(yyyy/mm/dd hh:mm:ss)' theo giờ JST, phản ánh lần chạy batch 15 phút/lần gần nhất. | **Medium** |
| `[AE800-136]` | [-] Nút CSV出力 | Check hiển thị nút CSV | 1. Quan sát nút [CSV出力] ở góc trên bên phải bảng. | - | 1. Hiển thị nút 'CSV出力', cho phép click. | **Low** |
| `[AE800-137]` | [-] Nút CSV出力 | Check xuất file CSV | 1. Click [CSV出力] khi bảng có dữ liệu. | - | 1. Trình duyệt tải xuống file CSV thành công, tên file đúng chuẩn '{startdate}-{endate}.csv' (VD: 20260901-20260930.csv). | **High** |
| `[AE800-138]` | [-] Nút CSV出力 | Check xuất file CSV | 1. Mở file CSV vừa tải về bằng Microsoft Excel. | - | 1. File được mã hóa UTF-8 with BOM, hiển thị tiếng Nhật rõ ràng không bị lỗi vỡ font (mojibake). | **High** |
| `[AE800-139]` | [-] Nút CSV出力 | Check xuất file CSV | 1. So sánh nội dung trong file CSV với dữ liệu trên bảng giao dịch. | - | 1. Chứa đầy đủ và chính xác 100% các dòng và cột khớp với bộ lọc đang chọn. | **High** |
| `[AE800-140]` | [-] Nút CSV出力 | Check xuất file CSV | 1. Click [CSV出力] khi tìm kiếm ra 0 bản ghi. | - | 1. Tải về file CSV chỉ chứa dòng tiêu đề các cột, không có dòng dữ liệu (hoặc báo không có dữ liệu để xuất). | **Medium** |
| `[AE800-141]` | [16] 開始日時 | Check tên cột & căn lề | 1. Quan sát cột header '開始日時'. | - | 1. Hiển thị tên cột '開始日時', nội dung căn giữa, sắp xếp mặc định từ mới đến cũ. | **Low** |
| `[AE800-142]` | [17] 終了日時 | Check tên cột & căn lề | 1. Quan sát cột header '終了日時'. | - | 1. Hiển thị tên cột '終了日時', nội dung căn giữa, click icon sort chuyển đổi 2 chiều: mới -> cũ và cũ -> mới. | **Medium** |
| `[AE800-143]` | [18] 利用者 | Check tên cột & căn lề | 1. Quan sát cột header '利用者'. | - | 1. Hiển thị tên cột '利用者', nội dung dữ liệu căn trái. | **Low** |
| `[AE800-144]` | [19] 報酬率（ランク） | Check tên cột & căn lề | 1. Quan sát cột header '報酬率（ランク）'. | - | 1. Hiển thị tên cột '報酬率（ランク）', nội dung dữ liệu căn giữa. | **Low** |
| `[AE800-145]` | [20] 事務所 | Check tên cột & căn lề | 1. Quan sát cột header '事務所'. | - | 1. Hiển thị tên cột '事務所', nội dung dữ liệu căn trái. | **Low** |
| `[AE800-146]` | [21] 配信状態 | Check tên cột & căn lề | 1. Quan sát cột header '配信状態'. | - | 1. Hiển thị tên cột '配信状態', nội dung dữ liệu căn giữa. | **Low** |
| `[AE800-147]` | [22] サービス | Check tên cột & căn lề | 1. Quan sát cột header 'サービス'. | - | 1. Hiển thị tên cột 'サービス', nội dung dữ liệu căn giữa. | **Low** |
| `[AE800-148]` | [23] 元ソース | Check tên cột & căn lề | 1. Quan sát cột header '元ソース'. | - | 1. Hiển thị tên cột '元ソース', nội dung dữ liệu căn giữa. | **Low** |
| `[AE800-149]` | [24] ポイント売上 | Check tên cột & căn lề | 1. Quan sát cột header 'ポイント売上'. | - | 1. Hiển thị tên cột 'ポイント売上', nội dung dữ liệu căn phải. | **Low** |
| `[AE800-150]` | [25] カラオケ配信以外売上 | Check tên cột & căn lề | 1. Quan sát cột header 'カラオケ配信以外売上'. | - | 1. Hiển thị tên cột 'カラオケ配信以外売上', nội dung dữ liệu căn phải. | **Low** |
| `[AE800-151]` | [26] カラオケ配信売上 | Check tên cột & căn lề | 1. Quan sát cột header 'カラオケ配信売上'. | - | 1. Hiển thị tên cột 'カラオケ配信売上', nội dung dữ liệu căn phải. | **Low** |
| `[AE800-152]` | [27] ファミリア売上 | Check tên cột & căn lề | 1. Quan sát cột header 'ファミリア売上'. | - | 1. Hiển thị tên cột 'ファミリア売上', nội dung dữ liệu căn phải. | **Low** |
| `[AE800-153]` | [28] GOLD（G） | Check tên cột & căn lề | 1. Quan sát cột header 'GOLD（G）'. | - | 1. Hiển thị tên cột 'GOLD（G）', nội dung dữ liệu căn phải. | **Low** |
| `[AE800-154]` | [29] 報酬支払（円） | Check tên cột & căn lề | 1. Quan sát cột header '報酬支払（円）'. | - | 1. Hiển thị tên cột '報酬支払（円）', nội dung dữ liệu căn phải. | **Low** |
| `[AE800-155]` | [30] 事務所獲得ポイント | Check tên cột & căn lề | 1. Quan sát cột header '事務所獲得ポイント'. | - | 1. Hiển thị tên cột '事務所獲得ポイント', nội dung dữ liệu căn phải. | **Low** |
| `[AE800-156]` | [-] Data Mapping từng dòng (<td>) | Check điều kiện ghi nhận livestream | 1. Kiểm tra điều kiện tổng kết giao dịch livestream trong bảng. | - | 1. Chỉ ghi nhận và hiển thị các giao dịch trong buổi livestream sau khi livestream đã kết thúc hoàn toàn. | **High** |
| `[AE800-157]` | [-] Data Mapping từng dòng (<td>) | Check mapping cột [16] & [17] | 1. Quan sát dòng giao dịch livestream và dòng giao dịch familia tại cột [16], [17]. | - | 1. Giao dịch livestream hiển thị start/end time; giao dịch familia hiển thị thời điểm xảy ra tại [16] và hiển thị 'ー' tại [17]. | **Medium** |
| `[AE800-158]` | [-] Data Mapping từng dòng (<td>) | Check link cột [18] 利用者 | 1. Click vào username tại cột [18] 利用者. | - | 1. Mở tab trình duyệt mới điều hướng đến màn hình AE200 của user tương ứng (target="_blank"), bảo lưu trang AE800 gốc. | **High** |
| `[AE800-159]` | [-] Data Mapping từng dòng (<td>) | Check mapping cột [19] 報酬率（ランク） | 1. Quan sát cột [19] của streamer tự do và streamer thuộc agency. | - | 1. Streamer tự do hiển thị tỷ lệ % kèm rank (VD: 60% (S0)); streamer thuộc agency hiển thị 'ー (S0)'. | **Medium** |
| `[AE800-160]` | [-] Data Mapping từng dòng (<td>) | Check mapping cột [20] 事務所 | 1. Quan sát cột [20] của streamer tự do và streamer thuộc agency. | - | 1. Không thuộc agency hiển thị 'なし'; thuộc agency hiển thị text format '{agency_name} ({agencyID})'. | **Medium** |
| `[AE800-161]` | [-] Data Mapping từng dòng (<td>) | Check mapping cột [21] 配信状態 | 1. Quan sát loại hình phát sóng tại cột [21]. | - | 1. Livestream hiển thị đúng 1 trong 3 trạng thái: '通常', '2ショット', 'ファミリア限定'; non-livestream hiển thị 'ー'. | **Medium** |
| `[AE800-162]` | [-] Data Mapping từng dòng (<td>) | Check mapping cột [22] サービス | 1. Quan sát giá trị dịch vụ tại cột [22]. | - | 1. Hiển thị chính xác tên loại giao dịch (ウィスパー, ギフト, 宝箱, クラス参加...). | **Medium** |
| `[AE800-163]` | [-] Data Mapping từng dòng (<td>) | Check link cột [23] 元ソース | 1. Click vào Stream ID tại cột [23] 元ソース. | - | 1. Mở tab trình duyệt mới điều hướng đến màn hình lưu trữ stream archive AG500 (target="_blank"); giao dịch non-stream hiển thị 'ー'. | **High** |
| `[AE800-164]` | [-] Data Mapping từng dòng (<td>) | Check mapping cột [24] ポイント売上 | 1. Quan sát định dạng điểm thưởng tại cột [24]. | - | 1. Hiển thị đúng định dạng '{amount} P' hoặc '{amount} GP' kèm dấu phẩy phân cách hàng nghìn; giao dịch không dùng P/GP hiển thị 'ー'. | **Medium** |
| `[AE800-165]` | [-] Data Mapping từng dòng (<td>) | Check mapping cột doanh thu [25], [26], [27] | 1. Quan sát số tiền tại các cột [25], [26], [27]. | - | 1. Hiển thị số tiền yên kèm phân cách hàng nghìn nếu đúng phân loại doanh thu; nếu không phải hiển thị 'ー'. | **Medium** |
| `[AE800-166]` | [-] Data Mapping từng dòng (<td>) | Check mapping cột [28] & [29] | 1. Quan sát số GOLD và tiền yên quy đổi tại cột [28], [29]. | - | 1. Streamer tự do hiển thị số GOLD thực nhận tại [28] và số yên quy đổi tại [29]; streamer thuộc agency hiển thị 'ー'. | **High** |
| `[AE800-167]` | [-] Data Mapping từng dòng (<td>) | Check mapping cột [30] 事務所獲得ポイント | 1. Quan sát điểm point của agency tại cột [30]. | - | 1. Streamer thuộc agency hiển thị số point agency kiếm được; streamer tự do hiển thị 'ー'. | **High** |
| `[AE800-168]` | [-] Thanh phân trang (Pagination) | Check hiển thị phân trang | 1. Quan sát thanh phân trang ở cuối bảng khi có nhiều trang dữ liệu. | - | 1. Hiển thị đầy đủ nút '<<前', các số trang (1, 2, 3...), nút '次>>', highlight active Trang 1, tổng số trang = roundup(Tổng / 10). | **High** |
| `[AE800-169]` | [-] Thanh phân trang (Pagination) | Check số bản ghi mỗi trang | 1. Đếm số dòng hiển thị trên Trang 1. | - | 1. Hiển thị tối đa đúng 10 dòng/trang theo Spec. | **High** |
| `[AE800-170]` | [-] Thanh phân trang (Pagination) | Check chuyển trang bằng số trang | 1. Click vào nút số '2' trên thanh phân trang. | - | 1. Bảng tải đúng dữ liệu dòng 11 đến 20 của Trang 2, số 2 được highlight active, không trùng hay sót bản ghi. | **High** |
| `[AE800-171]` | [-] Thanh phân trang (Pagination) | Check chuyển trang bằng nút Next & Prev | 1. Click nút [次>>] để chuyển trang tiếp và click [<<前] để lùi trang. | - | 1. Hệ thống chuyển tuần tự sang trang kế tiếp và lùi lại trang trước mượt mà. | **High** |
| `[AE800-172]` | [-] Thanh phân trang (Pagination) | Check nút First & Last | 1. Click nút [>>] (Last) và nút [<<] (First). | - | 1. Hệ thống nhảy trực tiếp đến trang cuối cùng và quay lại trang 1 thành công. | **Medium** |
| `[AE800-173]` | [-] Thanh phân trang (Pagination) | Check khóa nút disabled | 1. Kiểm tra trạng thái các nút điều hướng khi đang đứng ở Trang 1 và khi ở Trang cuối. | - | 1. Tại Trang 1: Nút '<<前' và First bị vô hiệu hóa (disabled); tại Trang cuối: Nút '次>>' và Last bị vô hiệu hóa (disabled). | **High** |
| `[AE800-174]` | [-] Thanh phân trang (Pagination) | Check biên 0 bản ghi | 1. Tìm kiếm với điều kiện không có bất kỳ bản ghi nào. | - | 1. Thanh phân trang ẩn hoàn toàn, bảng hiển thị thông báo Empty state căn giữa CMMSG47: 一致する検索結果はありません。. | **High** |
| `[AE800-175]` | [-] Thanh phân trang (Pagination) | Check biên 10 bản ghi | 1. Tìm kiếm dữ liệu có tổng số bản ghi đúng bằng 10. | - | 1. Hiển thị trọn vẹn trên 1 trang duy nhất, thanh phân trang ẩn hoặc cả nút Prev và Next đều disabled. | **Medium** |
| `[AE800-176]` | [-] Thanh phân trang (Pagination) | Check biên 11 bản ghi | 1. Tìm kiếm dữ liệu có tổng số bản ghi bằng 11. | - | 1. Tự động tách thành 2 trang: Trang 1 có 10 dòng đầu, Trang 2 có đúng 1 dòng lẻ cuối cùng. | **High** |
| `[AE800-177]` | [-] Thanh phân trang (Pagination) | Check đồng bộ phân trang với tìm kiếm | 1. Đang đứng ở Trang > 1, thay đổi bộ lọc hoặc bấm [検索] mới. | - | 1. Hệ thống bắt buộc tự động reset về Trang 1; khi chuyển qua lại giữa các trang thì bảo lưu nguyên vẹn bộ lọc. | **High** |
| `[AE800-178]` | [-] Thanh phân trang (Pagination) | Check rút gọn số trang … (CMR23) | 1. Tìm kiếm dữ liệu có tổng số trang > 7 (VD: 11 trang). | - | 1. Dãy số trang tự động rút gọn theo định dạng chuẩn CMR23: '<<前 1 2 3 4 5 … 11 次>>', click vào '…' mở ô input nhỏ để nhập số trang. | **Medium** |
| `[AE800-179]` | [-] Thanh phân trang (Pagination) | Check URL Tampering & Negative | 1. Thử sửa trực tiếp tham số ?page= trên URL trình duyệt thành ?page=-1, ?page=99999 hoặc ?page=abc. | - | 1. Hệ thống xử lý an toàn đưa người dùng về Trang 1 hoặc Trang cuối hợp lệ, không bị lỗi 500 hay crash ứng dụng. | **Medium** |
| | **III. SUB-LAYOUTS / MODALS CON / POPUPS** | | | | | |
| `[AE800-180]` | [-] Error Handling & RBAC | Check mất kết nối mạng | 1. Ngắt kết nối Internet trong lúc bấm [検索]. | - | 1. Hiển thị thông báo lỗi CMMSG8: ネットワークエラー。接続を確認してください。 | **Medium** |
| `[AE800-181]` | [-] Error Handling & RBAC | Check lỗi máy chủ 500 | 1. Giả lập API tìm kiếm trả về mã lỗi HTTP 500 Internal Server Error. | - | 1. Hiển thị thông báo lỗi CMMSG1: 予期しないサーバーエラーが発生しました。 kèm nút 再試行. | **Medium** |
| `[AE800-182]` | [-] Error Handling & RBAC | Check phân quyền Master Admin & Admin | 1. Đăng nhập với tài khoản Master Admin hoặc Admin và truy cập AE800. | - | 1. Cho phép truy cập đầy đủ tính năng xem số liệu, lọc và click [CSV出力] tải file thành công. | **High** |
| `[AE800-183]` | [-] Error Handling & RBAC | Check phân quyền Monitor / Giám sát viên | 1. Đăng nhập với tài khoản role Monitor/Staff và truy cập AE800. | - | 1. Xem được bảng dữ liệu và thẻ thống kê, nhưng nút [CSV出力] bị vô hiệu hóa (disabled) hoặc ẩn để bảo vệ dữ liệu nhạy cảm. | **Medium** |