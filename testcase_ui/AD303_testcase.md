# BẢNG TEST CASE KIỂM THỬ GIAO DIỆN THỦ CÔNG (MANUAL UI TEST SUITE)
## Màn hình: AD303_Revenue Analysis (Phân Tích Doanh Thu Agency)
### Áp dụng: Quy chuẩn Trụ cột 2 (02_manual_ui_test_case_rule.md) & Thư viện UI_controls

---

## BẢNG ĐIỀU KHIỂN TIẾN ĐỘ & THỐNG KÊ (DASHBOARD HEADER)

| Thuộc tính | Giá trị | Thuộc tính | Giá trị | Round 1 Metric | Kết quả | Round 2 Metric | Kết quả |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Module Code** | `AD303` | **Environment** | `PC` | **Pass** | 0 | **Pass** | 0 |
| **Total Testcases** | **203** | **% Executed** | 0% | **Fail** | 0 | **Fail** | 0 |
| **Plan to Execute** | **203** | **Creator** | `NgaDTP` | **Impact** | 0 | **Impact** | 0 |
| **Spec Source** | `Surreal SPEC` | **Google Sheet Tab** | `AD303` | **Not Run** | 203 | **Not Run** | 0 |
| | | | | **Total** | 203 | **Total** | 0 |

---

## CHI TIẾT BẢNG TEST CASES (7 CỘT CHUẨN MARKDOWN)

| ID | Title | Big item | Steps | Pre-condition | Expected | Priority |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| | **I. COMMON & NAVIGATION** | | | | | |
| `[AD303-1]` | [0] Kiểm tra truy cập màn hình | Check hiển thị menu & sidebar | 1. Đăng nhập hệ thống Admin với quyền Master Admin. | User là Master Admin đăng nhập thành công. | 1. Menu Sidebar hiển thị đầy đủ các phân hệ quản trị. | **High** |
| `[AD303-2]` | [0] Kiểm tra truy cập màn hình | Check hiển thị menu & sidebar | 1. Quan sát menu cha '事務所管理' trên Sidebar. | - | 1. Menu cha '事務所管理' ở trạng thái mở rộng (expanded). | **Medium** |
| `[AD303-3]` | [0] Kiểm tra truy cập màn hình | Check hiển thị menu & sidebar | 1. Quan sát menu con '事務所一覧' trên Sidebar. | - | 1. Menu con '事務所一覧' được highlight active nổi bật. | **Medium** |
| `[AD303-4]` | [0] Kiểm tra truy cập màn hình | Check hiển thị breadcrumb | 1. Quan sát thanh Breadcrumbs ở góc trên màn hình AD303. | - | 1. Hiển thị text đúng chuỗi: '＞ 事務所管理 ＞ 事務所詳細'. | **Medium** |
| `[AD303-5]` | [0] Kiểm tra truy cập màn hình | Check điều hướng breadcrumb | 1. Click [事務所管理] trên Breadcrumb. | - | 1. Di chuyển về màn danh sách Agency AD100 và bảo lưu bộ lọc trước đó. | **High** |
| `[AD303-6]` | [0] Kiểm tra truy cập màn hình | Check điều hướng breadcrumb | 1. Click [事務所詳細] trên Breadcrumb. | - | 1. Di chuyển về màn thông tin cơ bản AD301 của Agency hiện tại. | **Medium** |
| `[AD303-7]` | [0] Kiểm tra truy cập màn hình | Check hiển thị tab navigation | 1. Quan sát thanh Tab chuyển đổi phân hệ chi tiết Agency. | - | 1. Hiển thị đầy đủ 3 Tab: '詳細' (AD301), 'ライバー一覧' (AD302), '売上' (AD303). | **High** |
| `[AD303-8]` | [0] Kiểm tra truy cập màn hình | Check hiển thị tab navigation | 1. Quan sát trạng thái active của Tab '売上'. | - | 1. Tab '売上' được highlight active nổi bật theo CMR40. | **Medium** |
| `[AD303-9]` | [0] Kiểm tra truy cập màn hình | Check điều hướng tab | 1. Click Tab [詳細]. | - | 1. Di chuyển về màn thông tin cơ bản AD301 của cùng Agency. | **Medium** |
| `[AD303-10]` | [0] Kiểm tra truy cập màn hình | Check điều hướng tab | 1. Click Tab [ライバー一覧]. | - | 1. Di chuyển về màn danh sách streamer AD302 của cùng Agency. | **Medium** |
| `[AD303-11]` | [0] Kiểm tra truy cập màn hình | Check điều hướng tab | 1. Click Tab [売上]. | - | 1. Ở nguyên màn AD303, không reload lại trang. | **Low** |
| `[AD303-12]` | [0] Kiểm tra truy cập màn hình | Check điều hướng Inbound với agency_id | 1. Mở màn hình AD303 với URL chứa tham số agency_id hợp lệ (VD: ?agency_id=12). | Bản ghi Agency ID=12 tồn tại trong hệ thống. | 1. Màn hình AD303 tải thành công đúng thiết kế Figma. | **High** |
| `[AD303-13]` | [0] Kiểm tra truy cập màn hình | Check điều hướng Inbound với agency_id | 1. Quan sát ô thông tin Agency trên màn hình AD303. | - | 1. Hệ thống tự động điền đúng tên và mã Agency tương ứng với tham số trên URL. | **High** |
| `[AD303-14]` | [0] Kiểm tra truy cập màn hình | Check điều hướng Inbound với agency_id | 1. Theo dõi Network request khi vừa mở trang AD303. | - | 1. Tự động kích hoạt API tìm kiếm tải dữ liệu bảng và thẻ số dư với agency_id tương ứng. | **High** |
| `[AD303-15]` | [0] Kiểm tra truy cập màn hình | Check điều hướng Inbound với agency_id | 1. Đối chiếu danh sách giao dịch hiển thị tại 2 bảng dữ liệu. | - | 1. 100% bản ghi hiển thị thuộc về đúng Agency ID trên URL. | **High** |
| `[AD303-16]` | [0] Kiểm tra truy cập màn hình | Check điều hướng Inbound với agency_id | 1. Quan sát các khối thẻ KPI (Số dư rút và Tổng quan doanh thu). | - | 1. Cập nhật khối thẻ KPI phản ánh chính xác số liệu của agency trong kỳ. | **High** |
| `[AD303-17]` | [0] Kiểm tra truy cập màn hình | Check điều hướng Inbound với agency_id | 1. Mở màn hình AD303 với URL chứa agency_id không tồn tại (VD: ?agency_id=999999). | - | 1. Bảng dữ liệu hiển thị thông báo căn giữa CMMSG47: 一致する検索結果はありません。 và các thẻ hiển thị 0. | **High** |
| `[AD303-18]` | [0] Kiểm tra truy cập màn hình | Check điều hướng Inbound với agency_id | 1. Mở màn hình AD303 với URL không truyền agency_id. | - | 1. Hệ thống báo lỗi hợp lệ hoặc redirect về trang danh sách Agency AD100. | **Medium** |
| `[AD303-19]` | [0] Kiểm tra truy cập màn hình | Check điều hướng Inbound với agency_id | 1. Click nút Back của trình duyệt khi đang ở AD303. | - | 1. Di chuyển về màn AD301 hoặc AD100 và bảo lưu bộ lọc trước đó. | **High** |
| `[AD303-20]` | [0] Kiểm tra truy cập màn hình | Check Screen Lifecycle | 1. Nhấn phím F5 trên trình duyệt khi đang xem AD303. | - | 1. Trang web tải lại thành công, bảo lưu nguyên vẹn param agency_id và dữ liệu đang xem. | **Medium** |
| `[AD303-21]` | [0] Kiểm tra truy cập màn hình | Check Screen Lifecycle | 1. Quan sát tiêu đề trang AD303 sau khi tải xong. | - | 1. Hiển thị text tiêu đề 'AD303_Revenue Analysis'. | **Medium** |
| | **II. MAIN SCREEN CONTROLS** | | | | | |
| `[AD303-22]` | [1] 期間 | Check hiển thị & Giá trị mặc định | 1. Quan sát khu vực chọn thời gian 期間. | - | 1. Hiển thị 2 ô input Datepicker kèm ký tự '~' ở giữa và icon lịch. | **Low** |
| `[AD303-23]` | [1] 期間 | Check hiển thị & Giá trị mặc định | 1. Quan sát giá trị ban đầu tại ô Từ ngày (Start Date). | - | 1. Hiển thị ngày 01 của tháng trước theo giờ JST theo định dạng YYYY/MM/DD. | **High** |
| `[AD303-24]` | [1] 期間 | Check hiển thị & Giá trị mặc định | 1. Quan sát giá trị ban đầu tại ô Đến ngày (End Date). | - | 1. Hiển thị ngày cuối cùng của tháng trước theo giờ JST theo định dạng YYYY/MM/DD. | **High** |
| `[AD303-25]` | [1] 期間 | Check chọn ngày qua popup lịch | 1. Click vào icon lịch ô Từ ngày. | - | 1. Popup lịch mở ra trực quan hiển thị tháng và năm hiện tại. | **Medium** |
| `[AD303-26]` | [1] 期間 | Check chọn ngày qua popup lịch | 1. Click chọn ngày 2026/08/01 trên popup lịch ô Từ ngày. | - | 1. Ô Từ ngày tiếp nhận giá trị '2026/08/01' và popup lịch tự động đóng lại. | **High** |
| `[AD303-27]` | [1] 期間 | Check chọn ngày qua popup lịch | 1. Click chọn ngày 2026/08/31 trên popup lịch ô Đến ngày. | - | 1. Ô Đến ngày tiếp nhận giá trị '2026/08/31' và popup lịch tự động đóng lại. | **High** |
| `[AD303-28]` | [1] 期間 | Check chọn ngày qua popup lịch | 1. Chọn Từ ngày và Đến ngày cùng là ngày 2026/08/15. | - | 1. Hệ thống cho phép chọn, tìm kiếm dữ liệu từ 00:00:00 đến 23:59:59 của ngày 2026/08/15. | **Medium** |
| `[AD303-29]` | [1] 期間 | Check chọn ngày qua popup lịch | 1. Chọn Từ ngày = 2026/08/20 và mở popup lịch ô Đến ngày. | - | 1. Trên popup lịch ô Đến ngày, các ngày trước 2026/08/20 bị làm mờ (disabled) không cho chọn theo CMR38. | **High** |
| `[AD303-30]` | [1] 期間 | Check chọn ngày qua popup lịch | 1. Click ra vùng trống bên ngoài khi popup lịch đang mở. | - | 1. Popup lịch tự động đóng lại và giữ nguyên giá trị trước đó. | **Low** |
| `[AD303-31]` | [1] 期間 | Check nhập liệu bàn phím & validation | 1. Thực hiện nhập ký tự là '2026/07/01' vào ô Từ ngày. | - | 1. Hệ thống cho phép nhập đúng định dạng YYYY/MM/DD. | **Medium** |
| `[AD303-32]` | [1] 期間 | Check nhập liệu bàn phím & validation | 1. Thực hiện nhập ký tự là chữ 'abcdef' vào ô ngày. | - | 1. Hệ thống tự động ngăn chặn nhập ký tự chữ theo CMR04 (blocking UX). | **Low** |
| `[AD303-33]` | [1] 期間 | Check nhập liệu bàn phím & validation | 1. Thực hiện nhập ký tự đặc biệt '!@#$%' vào ô ngày. | - | 1. Hệ thống tự động ngăn chặn nhập ký tự đặc biệt theo CMR04. | **Low** |
| `[AD303-34]` | [1] 期間 | Check nhập liệu bàn phím & validation | 1. Thực hiện nhập ngày không tồn tại là '2026/02/31' và click [検索]. | - | 1. Hiển thị thông báo lỗi CMMSG36: 期間の日付の形式が無効です。正しい形式を使用してください（例：DD/MM/YYYY）。 | **Medium** |
| `[AD303-35]` | [1] 期間 | Check nhập liệu bàn phím & validation | 1. Thực hiện nhập tay Từ ngày = '2026/08/20' và Đến ngày = '2026/08/10' rồi click [検索]. | - | 1. Hiển thị thông báo lỗi CMMSG39: 期間の開始日は終了日より前でなければなりません。 | **High** |
| `[AD303-36]` | [1] 期間 | Check nhập liệu bàn phím & validation | 1. Thực hiện paste chuỗi ký tự '  2026/08/10  ' có khoảng trắng ở đầu và cuối vào ô ngày. | - | 1. Hệ thống tự động trim khoảng trắng thừa và tiếp nhận giá trị '2026/08/10'. | **Low** |
| `[AD303-37]` | [1] 期間 | Check nhập liệu bàn phím & validation | 1. Xóa toàn bộ nội dung ô Từ ngày hoặc Đến ngày. | - | 1. Ô input trở về trạng thái trống, khi tìm kiếm không giới hạn mốc thời gian đã xóa. | **Medium** |
| `[AD303-38]` | [2] 今日 / 今週 / 今月 / 先月 | Check hiển thị | 1. Quan sát nhóm 4 nút chọn nhanh thời gian. | - | 1. Hiển thị đầy đủ 4 nút: '今日', '今週', '今月', '先月'. | **Low** |
| `[AD303-39]` | [2] 今日 / 今週 / 今月 / 先月 | Check click nút | 1. Click [今日]. | - | 1. Ô Từ ngày và Đến ngày tự động điền ngày hôm nay (00:00:00 ~ 23:59:59 JST). | **Medium** |
| `[AD303-40]` | [2] 今日 / 今週 / 今月 / 先月 | Check click nút | 1. Click [今週]. | - | 1. Ô Từ ngày tự động điền Thứ Hai đầu tuần hiện tại, Đến ngày điền Chủ Nhật cuối tuần. | **Medium** |
| `[AD303-41]` | [2] 今日 / 今週 / 今月 / 先月 | Check click nút | 1. Click [今月]. | - | 1. Ô Từ ngày tự động điền ngày 01 tháng hiện tại, Đến ngày điền ngày cuối cùng tháng hiện tại. | **Medium** |
| `[AD303-42]` | [2] 今日 / 今週 / 今月 / 先月 | Check click nút | 1. Click [先月]. | - | 1. Ô Từ ngày tự động điền ngày 01 tháng trước, Đến ngày điền ngày cuối cùng tháng trước. | **Medium** |
| `[AD303-43]` | [2] 今日 / 今週 / 今月 / 先月 | Check click nút | 1. Quan sát trạng thái active của nút sau khi click. | - | 1. Nút vừa click được highlight active nổi bật so với các nút còn lại. | **Low** |
| `[AD303-44]` | [2] 今日 / 今週 / 今月 / 先月 | Check phạm vi ảnh hưởng của bộ lọc | 1. Kiểm tra phạm vi ảnh hưởng của bộ lọc thời gian đối với khối số dư rút. | - | 1. Bộ lọc thời gian áp dụng cho 2 bảng dữ liệu và khối tổng quan doanh thu; không làm thay đổi khối số dư có thể rút ([6] - [9]) theo Spec. | **High** |
| `[AD303-45]` | [3] 全ライバー | Check hiển thị | 1. Quan sát dropdown [3] ở trạng thái mặc định. | - | 1. Hiển thị text mặc định '全ライバー' kèm icon mũi tên xổ xuống. | **Low** |
| `[AD303-46]` | [3] 全ライバー | Check hiển thị | 1. Click vào dropdown [3] để mở danh sách tùy chọn. | - | 1. Danh sách xổ xuống hiển thị option '全ライバー' và toàn bộ danh sách streamer trực thuộc agency. | **Medium** |
| `[AD303-47]` | [3] 全ライバー | Check chọn từng option | 1. Click chọn option '全ライバー'. | - | 1. Dropdown đóng lại, ô tiếp nhận text '全ライバー'. | **Medium** |
| `[AD303-48]` | [3] 全ライバー | Check chọn từng option | 1. Click chọn một Streamer cụ thể trong danh sách. | - | 1. Dropdown đóng lại, ô hiển thị tên streamer đã chọn. | **High** |
| `[AD303-49]` | [3] 全ライバー | Check đóng khi click ngoài | 1. Click ra vùng trống bên ngoài dropdown khi danh sách đang mở. | - | 1. Danh sách tự động đóng lại và giữ nguyên streamer đã chọn trước đó. | **Low** |
| `[AD303-50]` | [4] 検索 | Check hiển thị | 1. Quan sát nút [検索]. | - | 1. Hiển thị text '検索', dạng Primary Button nổi bật, con trỏ chuột dạng Pointer. | **Low** |
| `[AD303-51]` | [4] 検索 | Check thực hiện tìm kiếm | 1. Click [検索] với điều kiện mặc định ban đầu. | - | 1. Hệ thống gọi API tìm kiếm, tải dữ liệu cho 2 bảng và cập nhật khối thẻ tổng quan doanh thu. | **High** |
| `[AD303-52]` | [4] 検索 | Check thực hiện tìm kiếm | 1. Thay đổi khoảng thời gian và click [検索]. | - | 1. Dữ liệu 2 bảng và khối tổng quan doanh thu cập nhật đúng theo khoảng thời gian vừa chọn. | **High** |
| `[AD303-53]` | [4] 検索 | Check thực hiện tìm kiếm | 1. Chọn 1 streamer cụ thể tại dropdown [3] và click [検索]. | - | 1. Dữ liệu bảng 2 chỉ hiển thị các giao dịch phát sinh bởi streamer tương ứng. | **High** |
| `[AD303-54]` | [4] 検索 | Check thực hiện tìm kiếm | 1. Kết hợp lọc Thời gian + Streamer cụ thể và click [検索]. | - | 1. Dữ liệu lọc chính xác theo đồng thời cả 2 tiêu chí (Logic AND). | **High** |
| `[AD303-55]` | [4] 検索 | Check Debounce & Loading | 1. Thực hiện click liên tục 2 lần (double-click) vào nút [検索]. | - | 1. Nút tạm thời bị vô hiệu hóa (disabled) trong khi API đang gọi theo CMR15 (Debounce). | **High** |
| `[AD303-56]` | [4] 検索 | Check Debounce & Loading | 1. Theo dõi giao diện trong suốt thời gian API tìm kiếm đang phản hồi. | - | 1. Hiển thị hiệu ứng Loading spinner hoặc thông báo CMMSG27: 読み込み中、しばらくお待ちください... trên vùng các bảng. | **Medium** |
| `[AD303-57]` | [5] クリア | Check hiển thị | 1. Quan sát nút [クリア]. | - | 1. Hiển thị text 'クリア', dạng Secondary/Ghost Button. | **Low** |
| `[AD303-58]` | [5] クリア | Check click nút | 1. Thay đổi các bộ lọc (Thời gian, Streamer), sau đó click [クリア]. | - | 1. Toàn bộ các ô bộ lọc tự động khôi phục về giá trị mặc định ban đầu. | **High** |
| `[AD303-59]` | [5] クリア | Check click nút | 1. Quan sát dữ liệu các bảng ngay sau khi click [クリア]. | - | 1. Hệ thống tự động kích hoạt tìm kiếm và tải lại dữ liệu mặc định của các bảng mà không cần bấm 検索. | **High** |
| `[AD303-60]` | [6] 報酬ポイント合計（P）：{amount} | Check hiển thị | 1. Quan sát thẻ [6] 報酬ポイント合計（P）：{amount}. | - | 1. Hiển thị text nhãn '報酬ポイント合計（P）：' kèm con số point. | **Low** |
| `[AD303-61]` | [6] 報酬ポイント合計（P）：{amount} | Check định dạng | 1. Quan sát số point trên thẻ [6] 報酬ポイント合計（P）：{amount}. | - | 1. Định dạng phân cách hàng nghìn bằng dấu phẩy ',' (VD: 50,000 P). | **Low** |
| `[AD303-62]` | [6] 報酬ポイント合計（P）：{amount} | Check tính toán | 1. Đối chiếu số liệu thẻ [6] 報酬ポイント合計（P）：{amount} với định nghĩa Spec. | - | 1. Khớp chính xác 100%: Thẻ [6] = Thẻ [7] + Thẻ [8] + Thẻ [9], phản ánh tổng số dư P agency có thể rút. | **High** |
| `[AD303-63]` | [6] 報酬ポイント合計（P）：{amount} | Check giá trị biên | 1. Khi agency không có số dư tại thẻ [6] 報酬ポイント合計（P）：{amount}. | - | 1. Thẻ hiển thị số 0: '報酬ポイント合計（P）：0'. | **Medium** |
| `[AD303-64]` | [6] 報酬ポイント合計（P）：{amount} | Check tính bất biến theo filter | 1. Thay đổi bộ lọc thời gian và click [検索]. | - | 1. Số liệu thẻ [6] giữ nguyên không đổi vì số dư rút phản ánh số dư tức thời hiện tại của agency. | **High** |
| `[AD303-65]` | [7] カラオケ以外ポイント（P)：{amount} | Check hiển thị | 1. Quan sát thẻ [7] カラオケ以外ポイント（P)：{amount}. | - | 1. Hiển thị text nhãn 'カラオケ以外ポイント（P）：' kèm con số point. | **Low** |
| `[AD303-66]` | [7] カラオケ以外ポイント（P)：{amount} | Check định dạng | 1. Quan sát số point trên thẻ [7] カラオケ以外ポイント（P)：{amount}. | - | 1. Định dạng phân cách hàng nghìn bằng dấu phẩy ',' (VD: 50,000 P). | **Low** |
| `[AD303-67]` | [7] カラオケ以外ポイント（P)：{amount} | Check tính toán | 1. Đối chiếu số liệu thẻ [7] カラオケ以外ポイント（P)：{amount} với định nghĩa Spec. | - | 1. Khớp chính xác 100%: tổng số dư point non-karaoke agency có thể rút. | **High** |
| `[AD303-68]` | [7] カラオケ以外ポイント（P)：{amount} | Check giá trị biên | 1. Khi agency không có số dư tại thẻ [7] カラオケ以外ポイント（P)：{amount}. | - | 1. Thẻ hiển thị số 0: 'カラオケ以外ポイント（P）：0'. | **Medium** |
| `[AD303-69]` | [8] カラオケポイント（P）：{amount} | Check hiển thị | 1. Quan sát thẻ [8] カラオケポイント（P）：{amount}. | - | 1. Hiển thị text nhãn 'カラオケポイント（P）：' kèm con số point. | **Low** |
| `[AD303-70]` | [8] カラオケポイント（P）：{amount} | Check định dạng | 1. Quan sát số point trên thẻ [8] カラオケポイント（P）：{amount}. | - | 1. Định dạng phân cách hàng nghìn bằng dấu phẩy ',' (VD: 50,000 P). | **Low** |
| `[AD303-71]` | [8] カラオケポイント（P）：{amount} | Check tính toán | 1. Đối chiếu số liệu thẻ [8] カラオケポイント（P）：{amount} với định nghĩa Spec. | - | 1. Khớp chính xác 100%: tổng số dư point karaoke agency có thể rút. | **High** |
| `[AD303-72]` | [8] カラオケポイント（P）：{amount} | Check giá trị biên | 1. Khi agency không có số dư tại thẻ [8] カラオケポイント（P）：{amount}. | - | 1. Thẻ hiển thị số 0: 'カラオケポイント（P）：0'. | **Medium** |
| `[AD303-73]` | [9] ファミリア報酬P換算（P）：{amount} | Check hiển thị | 1. Quan sát thẻ [9] ファミリア報酬P換算（P）：{amount}. | - | 1. Hiển thị text nhãn 'ファミリア報酬P換算（P）：' kèm con số point. | **Low** |
| `[AD303-74]` | [9] ファミリア報酬P換算（P）：{amount} | Check định dạng | 1. Quan sát số point trên thẻ [9] ファミリア報酬P換算（P）：{amount}. | - | 1. Định dạng phân cách hàng nghìn bằng dấu phẩy ',' (VD: 50,000 P). | **Low** |
| `[AD303-75]` | [9] ファミリア報酬P換算（P）：{amount} | Check tính toán | 1. Đối chiếu số liệu thẻ [9] ファミリア報酬P換算（P）：{amount} với định nghĩa Spec. | - | 1. Khớp chính xác 100%: tổng số dư P familia agency có thể rút (quy đổi từ yên sang point theo tỷ lệ 1:1). | **High** |
| `[AD303-76]` | [9] ファミリア報酬P換算（P）：{amount} | Check giá trị biên | 1. Khi agency không có số dư tại thẻ [9] ファミリア報酬P換算（P）：{amount}. | - | 1. Thẻ hiển thị số 0: 'ファミリア報酬P換算（P）：0'. | **Medium** |
| `[AD303-77]` | [-] Bảng 報酬履歴 & Tiêu đề | Check hiển thị tiêu đề bảng 1 | 1. Quan sát tiêu đề bảng 1. | - | 1. Hiển thị text tiêu đề '報酬履歴'. | **Low** |
| `[AD303-78]` | [-] Nút CSV出力 Bảng 1 | Check hiển thị nút CSV Bảng 1 | 1. Quan sát nút [CSV出力] trên bảng 1. | - | 1. Hiển thị nút 'CSV出力', cho phép click. | **Low** |
| `[AD303-79]` | [-] Nút CSV出力 Bảng 1 | Check xuất file CSV Bảng 1 | 1. Click [CSV出力] trên bảng 1 khi có dữ liệu. | - | 1. Tải về file CSV thành công, tên file '{startdate}-{endate}.csv', định dạng UTF-8 with BOM. | **High** |
| `[AD303-80]` | [-] Nút CSV出力 Bảng 1 | Check xuất file CSV Bảng 1 | 1. Kiểm tra dữ liệu trong file CSV vừa tải. | - | 1. Khớp chính xác 100% các cột và dòng lịch sử chuyển tiền trong bảng 1. | **High** |
| `[AD303-81]` | [10] 振込日 | Check tên cột & căn lề Bảng 1 | 1. Quan sát cột header '振込日'. | - | 1. Hiển thị tên cột '振込日', nội dung căn giữa theo format YYYY/MM/DD. | **Low** |
| `[AD303-82]` | [11] 報酬月 | Check tên cột & căn lề Bảng 1 | 1. Quan sát cột header '報酬月'. | - | 1. Hiển thị tên cột '報酬月', nội dung căn giữa theo format YYYY/MM. | **Low** |
| `[AD303-83]` | [12] 報酬ポイント合計 | Check tên cột & căn lề Bảng 1 | 1. Quan sát cột header '報酬ポイント合計'. | - | 1. Hiển thị tên cột '報酬ポイント合計', nội dung căn phải kèm dấu phẩy phân cách hàng nghìn. | **Low** |
| `[AD303-84]` | [13] 報酬ポイント・カラオケ以外 | Check tên cột & căn lề Bảng 1 | 1. Quan sát cột header '報酬ポイント・カラオケ以外'. | - | 1. Hiển thị tên cột '報酬ポイント・カラオケ以外', nội dung căn phải. | **Low** |
| `[AD303-85]` | [14] 報酬ポイント・カラオケ | Check tên cột & căn lề Bảng 1 | 1. Quan sát cột header '報酬ポイント・カラオケ'. | - | 1. Hiển thị tên cột '報酬ポイント・カラオケ', nội dung căn phải. | **Low** |
| `[AD303-86]` | [15] 報酬ポイント・ファミリア | Check tên cột & căn lề Bảng 1 | 1. Quan sát cột header '報酬ポイント・ファミリア'. | - | 1. Hiển thị tên cột '報酬ポイント・ファミリア', nội dung căn phải. | **Low** |
| `[AD303-87]` | [16] 報酬率 | Check tên cột & căn lề Bảng 1 | 1. Quan sát cột header '報酬率'. | - | 1. Hiển thị tên cột '報酬率', nội dung căn phải kèm ký hiệu '%'. | **Low** |
| `[AD303-88]` | [17] 報酬額合計（円） | Check tên cột & căn lề Bảng 1 | 1. Quan sát cột header '報酬額合計（円）'. | - | 1. Hiển thị tên cột '報酬額合計（円）', nội dung căn phải kèm dấu phẩy phân cách. | **Low** |
| `[AD303-89]` | [18] 報酬額（円）・カラオケ以外 | Check tên cột & căn lề Bảng 1 | 1. Quan sát cột header '報酬額（円）・カラオケ以外'. | - | 1. Hiển thị tên cột '報酬額（円）・カラオケ以外', nội dung căn phải. | **Low** |
| `[AD303-90]` | [19] 報酬額（円）・カラオケ | Check tên cột & căn lề Bảng 1 | 1. Quan sát cột header '報酬額（円）・カラオケ'. | - | 1. Hiển thị tên cột '報酬額（円）・カラオケ', nội dung căn phải. | **Low** |
| `[AD303-91]` | [20] 報酬額（円）・ファミリア | Check tên cột & căn lề Bảng 1 | 1. Quan sát cột header '報酬額（円）・ファミリア'. | - | 1. Hiển thị tên cột '報酬額（円）・ファミリア', nội dung căn phải. | **Low** |
| `[AD303-92]` | [-] Data Mapping Bảng 1 | Check data mapping bảng 1 | 1. Quan sát dữ liệu các dòng trong bảng 報酬履歴. | - | 1. Hiển thị chính xác các bản ghi chuyển thưởng do Admin nhập, định dạng tiền và point rõ ràng. | **High** |
| `[AD303-93]` | [-] Data Mapping Bảng 1 | Check phân trang bảng 1 | 1. Kiểm tra phân trang bảng 1 khi có nhiều hơn 10 bản ghi. | - | 1. Phân trang 10 dòng/trang, chuyển trang mượt mà, disabled nút hợp lệ. | **High** |
| `[AD303-94]` | [-] Data Mapping Bảng 1 | Check empty state bảng 1 | 1. Khi agency chưa có bất kỳ lịch sử chuyển thưởng nào. | - | 1. Bảng 1 hiển thị thông báo căn giữa CMMSG47: 一致する検索結果はありません。. | **High** |
| `[AD303-95]` | [37] 報酬記録追加 | Check mở modal tạo bản ghi | 1. Click nút [報酬記録追加] ở đầu bảng 1. | - | 1. Mở Modal AD3031 để tạo mới bản ghi chuyển thưởng cho agency. | **High** |
| `[AD303-96]` | [38] Icon Chỉnh sửa | Check mở modal sửa bản ghi | 1. Click vào icon Sửa (Edit) tại một dòng trong bảng 1. | - | 1. Mở Modal AD3032 chứa đầy đủ dữ liệu của bản ghi tương ứng để chỉnh sửa. | **High** |
| `[AD303-97]` | [39] Icon Xóa | Check mở popup xác nhận xóa | 1. Click vào icon Xóa (Delete) tại một dòng trong bảng 1. | - | 1. Hiển thị popup xác nhận xóa CMMSG28: 本当に進みますか？ kèm 2 nút [キャンセル] và [削除]. | **High** |
| `[AD303-98]` | [39] Icon Xóa | Check hủy thao tác xóa | 1. Tại popup xác nhận xóa, click [キャンセル]. | - | 1. Popup đóng lại, bản ghi trong bảng 1 được giữ nguyên không bị xóa. | **Medium** |
| `[AD303-99]` | [39] Icon Xóa | Check xác nhận xóa bản ghi | 1. Tại popup xác nhận xóa, click [削除]. | - | 1. Hệ thống gọi API xóa, hiển thị thông báo CMMSG14: 正常に削除されました。, đóng popup, xóa bản ghi khỏi bảng 1 và cập nhật phản ánh lên màn AS100. | **High** |
| `[AD303-100]` | [21] 合計売上（円）：{amount} | Check hiển thị | 1. Quan sát thẻ [21] 合計売上（円）：{amount}. | - | 1. Hiển thị text nhãn '合計売上（円）：' kèm số tiền. | **Low** |
| `[AD303-101]` | [21] 合計売上（円）：{amount} | Check định dạng | 1. Quan sát số tiền thẻ [21] 合計売上（円）：{amount}. | - | 1. Định dạng phân cách hàng nghìn bằng dấu phẩy ','. | **Low** |
| `[AD303-102]` | [21] 合計売上（円）：{amount} | Check tính toán | 1. Đối chiếu số liệu thẻ [21] 合計売上（円）：{amount} với công thức nghiệp vụ Spec. | - | 1. Khớp chính xác 100%: Thẻ [21] = Thẻ [22] + Thẻ [23] + Thẻ [24], chỉ tính các giao dịch sử dụng point/yên. | **High** |
| `[AD303-103]` | [21] 合計売上（円）：{amount} | Check giá trị biên | 1. Khi không phát sinh doanh thu trong kỳ lọc. | - | 1. Thẻ hiển thị số 0: '合計売上（円）：0'. | **Medium** |
| `[AD303-104]` | [21] 合計売上（円）：{amount} | Check phản ứng | 1. Thay đổi bộ lọc thời gian và click [検索]. | - | 1. Số liệu thẻ [21] 合計売上（円）：{amount} tự động cập nhật lại tức thì. | **High** |
| `[AD303-105]` | [22] カラオケ配信売上（円）：{amount} | Check hiển thị | 1. Quan sát thẻ [22] カラオケ配信売上（円）：{amount}. | - | 1. Hiển thị text nhãn 'カラオケ配信売上（円）：' kèm số tiền. | **Low** |
| `[AD303-106]` | [22] カラオケ配信売上（円）：{amount} | Check định dạng | 1. Quan sát số tiền thẻ [22] カラオケ配信売上（円）：{amount}. | - | 1. Định dạng phân cách hàng nghìn bằng dấu phẩy ','. | **Low** |
| `[AD303-107]` | [22] カラオケ配信売上（円）：{amount} | Check tính toán | 1. Đối chiếu số liệu thẻ [22] カラオケ配信売上（円）：{amount} với công thức nghiệp vụ Spec. | - | 1. Khớp chính xác 100%: tổng doanh thu phát sinh từ các buổi livestream karaoke trong kỳ (khớp tổng cột 35). | **High** |
| `[AD303-108]` | [22] カラオケ配信売上（円）：{amount} | Check giá trị biên | 1. Khi không phát sinh doanh thu trong kỳ lọc. | - | 1. Thẻ hiển thị số 0: 'カラオケ配信売上（円）：0'. | **Medium** |
| `[AD303-109]` | [22] カラオケ配信売上（円）：{amount} | Check phản ứng | 1. Thay đổi bộ lọc thời gian và click [検索]. | - | 1. Số liệu thẻ [22] カラオケ配信売上（円）：{amount} tự động cập nhật lại tức thì. | **High** |
| `[AD303-110]` | [23] カラオケ配信以外売上（円）：{amount} | Check hiển thị | 1. Quan sát thẻ [23] カラオケ配信以外売上（円）：{amount}. | - | 1. Hiển thị text nhãn 'カラオケ配信以外売上（円）：' kèm số tiền. | **Low** |
| `[AD303-111]` | [23] カラオケ配信以外売上（円）：{amount} | Check định dạng | 1. Quan sát số tiền thẻ [23] カラオケ配信以外売上（円）：{amount}. | - | 1. Định dạng phân cách hàng nghìn bằng dấu phẩy ','. | **Low** |
| `[AD303-112]` | [23] カラオケ配信以外売上（円）：{amount} | Check tính toán | 1. Đối chiếu số liệu thẻ [23] カラオケ配信以外売上（円）：{amount} với công thức nghiệp vụ Spec. | - | 1. Khớp chính xác 100%: tổng doanh thu thường non-karaoke và non-familia trong kỳ (khớp tổng cột 34). | **High** |
| `[AD303-113]` | [23] カラオケ配信以外売上（円）：{amount} | Check giá trị biên | 1. Khi không phát sinh doanh thu trong kỳ lọc. | - | 1. Thẻ hiển thị số 0: 'カラオケ配信以外売上（円）：0'. | **Medium** |
| `[AD303-114]` | [23] カラオケ配信以外売上（円）：{amount} | Check phản ứng | 1. Thay đổi bộ lọc thời gian và click [検索]. | - | 1. Số liệu thẻ [23] カラオケ配信以外売上（円）：{amount} tự động cập nhật lại tức thì. | **High** |
| `[AD303-115]` | [24] ファミリア売上（円）：{amount} | Check hiển thị | 1. Quan sát thẻ [24] ファミリア売上（円）：{amount}. | - | 1. Hiển thị text nhãn 'ファミリア売上（円）：' kèm số tiền. | **Low** |
| `[AD303-116]` | [24] ファミリア売上（円）：{amount} | Check định dạng | 1. Quan sát số tiền thẻ [24] ファミリア売上（円）：{amount}. | - | 1. Định dạng phân cách hàng nghìn bằng dấu phẩy ','. | **Low** |
| `[AD303-117]` | [24] ファミリア売上（円）：{amount} | Check tính toán | 1. Đối chiếu số liệu thẻ [24] ファミリア売上（円）：{amount} với công thức nghiệp vụ Spec. | - | 1. Khớp chính xác 100%: tổng doanh thu phát sinh từ mua Class và mua Backnumber (khớp tổng cột 36). | **High** |
| `[AD303-118]` | [24] ファミリア売上（円）：{amount} | Check giá trị biên | 1. Khi không phát sinh doanh thu trong kỳ lọc. | - | 1. Thẻ hiển thị số 0: 'ファミリア売上（円）：0'. | **Medium** |
| `[AD303-119]` | [24] ファミリア売上（円）：{amount} | Check phản ứng | 1. Thay đổi bộ lọc thời gian và click [検索]. | - | 1. Số liệu thẻ [24] ファミリア売上（円）：{amount} tự động cập nhật lại tức thì. | **High** |
| `[AD303-120]` | [-] Bảng 各取引の詳細 & CSV出力 Bảng 2 | Check hiển thị tiêu đề bảng 2 | 1. Quan sát tiêu đề bảng 2. | - | 1. Hiển thị text tiêu đề '各取引の詳細'. | **Low** |
| `[AD303-121]` | [-] Bảng 各取引の詳細 & CSV出力 Bảng 2 | Check hiển thị nút CSV Bảng 2 | 1. Quan sát nút [CSV出力] trên bảng 2. | - | 1. Hiển thị nút 'CSV出力', cho phép click. | **Low** |
| `[AD303-122]` | [-] Bảng 各取引の詳細 & CSV出力 Bảng 2 | Check xuất file CSV Bảng 2 | 1. Click [CSV出力] trên bảng 2 khi có dữ liệu. | - | 1. Tải về file CSV thành công, tên file '{startdate}-{endate}.csv', định dạng UTF-8 with BOM. | **High** |
| `[AD303-123]` | [-] Bảng 各取引の詳細 & CSV出力 Bảng 2 | Check xuất file CSV Bảng 2 | 1. Kiểm tra dữ liệu trong file CSV vừa tải. | - | 1. Khớp chính xác 100% các dòng và cột giao dịch chi tiết theo bộ lọc hiện tại. | **High** |
| `[AD303-124]` | [25] 開始時間 | Check tên cột & căn lề Bảng 2 | 1. Quan sát cột header '開始時間'. | - | 1. Hiển thị tên cột '開始時間', nội dung căn giữa, sắp xếp mặc định từ mới đến cũ. | **Low** |
| `[AD303-125]` | [26] 終了時間 | Check tên cột & căn lề Bảng 2 | 1. Quan sát cột header '終了時間'. | - | 1. Hiển thị tên cột '終了時間', nội dung căn giữa, click sort chuyển đổi 2 chiều: mới -> cũ và cũ -> mới. | **Medium** |
| `[AD303-126]` | [27] 利用者 | Check tên cột & căn lề Bảng 2 | 1. Quan sát cột header '利用者'. | - | 1. Hiển thị tên cột '利用者', nội dung dữ liệu căn trái. | **Low** |
| `[AD303-127]` | [28] 配信者 | Check tên cột & căn lề Bảng 2 | 1. Quan sát cột header '配信者'. | - | 1. Hiển thị tên cột '配信者', nội dung dữ liệu căn trái. | **Low** |
| `[AD303-128]` | [29] 配信状態 | Check tên cột & căn lề Bảng 2 | 1. Quan sát cột header '配信状態'. | - | 1. Hiển thị tên cột '配信状態', nội dung dữ liệu căn giữa. | **Low** |
| `[AD303-129]` | [30] サービス | Check tên cột & căn lề Bảng 2 | 1. Quan sát cột header 'サービス'. | - | 1. Hiển thị tên cột 'サービス', nội dung dữ liệu căn giữa. | **Low** |
| `[AD303-130]` | [31] 元ソース | Check tên cột & căn lề Bảng 2 | 1. Quan sát cột header '元ソース'. | - | 1. Hiển thị tên cột '元ソース', nội dung dữ liệu căn giữa. | **Low** |
| `[AD303-131]` | [32] ポイント売上 | Check tên cột & căn lề Bảng 2 | 1. Quan sát cột header 'ポイント売上'. | - | 1. Hiển thị tên cột 'ポイント売上', nội dung dữ liệu căn phải. | **Low** |
| `[AD303-132]` | [33] 事務所獲得ポイント | Check tên cột & căn lề Bảng 2 | 1. Quan sát cột header '事務所獲得ポイント'. | - | 1. Hiển thị tên cột '事務所獲得ポイント', nội dung dữ liệu căn phải. | **Low** |
| `[AD303-133]` | [34] カラオケ配信以外売上（円） | Check tên cột & căn lề Bảng 2 | 1. Quan sát cột header 'カラオケ配信以外売上（円）'. | - | 1. Hiển thị tên cột 'カラオケ配信以外売上（円）', nội dung căn phải. | **Low** |
| `[AD303-134]` | [35] カラオケ配信売上（円） | Check tên cột & căn lề Bảng 2 | 1. Quan sát cột header 'カラオケ配信売上（円）'. | - | 1. Hiển thị tên cột 'カラオケ配信売上（円）', nội dung căn phải. | **Low** |
| `[AD303-135]` | [36] ファミリア売上（円） | Check tên cột & căn lề Bảng 2 | 1. Quan sát cột header 'ファミリア売上（円）'. | - | 1. Hiển thị tên cột 'ファミリア売上（円）', nội dung căn phải. | **Low** |
| `[AD303-136]` | [-] Data Mapping Bảng 2 | Check mapping cột [25] & [26] | 1. Quan sát thời gian tại cột [25], [26]. | - | 1. Livestream hiển thị start/end time; giao dịch familia hiển thị thời điểm xảy ra tại [25] và 'ー' tại [26]. | **Medium** |
| `[AD303-137]` | [-] Data Mapping Bảng 2 | Check link cột [27] 利用者 | 1. Click vào username tại cột [27] 利用者. | - | 1. Mở tab trình duyệt mới điều hướng đến màn hình AE200 của viewer (target="_blank"), bảo lưu trang AD303 gốc. | **High** |
| `[AD303-138]` | [-] Data Mapping Bảng 2 | Check link cột [28] 配信者 | 1. Click vào tên streamer tại cột [28] 配信者. | - | 1. Mở tab trình duyệt mới điều hướng đến màn hình AE200 của streamer (target="_blank"), bảo lưu trang AD303 gốc. | **High** |
| `[AD303-139]` | [-] Data Mapping Bảng 2 | Check mapping cột [29] 配信状態 | 1. Quan sát loại hình phát sóng tại cột [29]. | - | 1. Livestream hiển thị đúng: '通常', '2ショット', 'ファミリア限定'; non-livestream hiển thị 'ー'. | **Medium** |
| `[AD303-140]` | [-] Data Mapping Bảng 2 | Check mapping cột [30] サービス | 1. Quan sát loại dịch vụ tại cột [30]. | - | 1. Hiển thị đúng tên giao dịch (ウィスパー, ギフト, 宝箱, クラス参加...). | **Medium** |
| `[AD303-141]` | [-] Data Mapping Bảng 2 | Check link cột [31] 元ソース | 1. Click vào Stream ID tại cột [31] 元ソース. | - | 1. Mở tab mới điều hướng đến màn hình AG500 (target="_blank"); non-stream hiển thị 'ー'. | **High** |
| `[AD303-142]` | [-] Data Mapping Bảng 2 | Check mapping cột [32] ポイント売上 | 1. Quan sát số điểm tại cột [32]. | - | 1. Hiển thị đúng '{amount} P' hoặc '{amount} GP' kèm phân cách hàng nghìn; giao dịch không dùng P/GP hiển thị 'ー'. | **Medium** |
| `[AD303-143]` | [-] Data Mapping Bảng 2 | Check mapping cột [33] 事務所獲得ポイント | 1. Quan sát số point agency tại cột [33]. | - | 1. Hiển thị số point agency kiếm được; nếu không có hiển thị 'ー'. | **High** |
| `[AD303-144]` | [-] Data Mapping Bảng 2 | Check mapping cột doanh thu [34], [35], [36] | 1. Quan sát số tiền tại các cột [34], [35], [36]. | - | 1. Hiển thị số tiền yên kèm phân cách hàng nghìn nếu đúng loại doanh thu; nếu không phải hiển thị 'ー'. | **Medium** |
| `[AD303-145]` | [-] Data Mapping Bảng 2 | Check phân trang Bảng 2 (10 dòng/trang) | 1. Kiểm tra phân trang bảng 2 khi có nhiều trang dữ liệu. | - | 1. Phân trang đúng 10 dòng/trang, chuyển trang mượt mà, highlight active trang hiện tại. | **High** |
| `[AD303-146]` | [-] Data Mapping Bảng 2 | Check empty state Bảng 2 | 1. Tìm kiếm không có giao dịch nào thỏa mãn bộ lọc. | - | 1. Bảng 2 hiển thị thông báo căn giữa CMMSG47: 一致する検索結果はありません。 và ẩn thanh phân trang. | **High** |
| | **III. SUB-LAYOUTS / MODALS CON / POPUPS** | | | | | |
| `[AD303-147]` | [-] Modal AD3031 (Thêm bản ghi) | Check hiển thị số dư Agency trên Modal AD3031 | 1. Quan sát các thẻ số dư hiển thị ở đầu Modal AD3031. | - | 1. Hiển thị đầy đủ 4 nhãn: [40] 報酬ポイント合計（P）, [41] カラオケ以外ポイント（P）, [42] カラオケポイント（P）, [43] ファミリア報酬P換算（P） khớp 100% với số dư của agency. | **High** |
| `[AD303-148]` | [44] 報酬月 | Check hiển thị [44] 報酬月 | 1. Quan sát ô Datepicker [44] 報酬月. | - | 1. Hiển thị nhãn '報酬月', có dấu sao đỏ (*), format YYYY/MM. | **Medium** |
| `[AD303-149]` | [44] 報酬月 | Check chọn tháng hợp lệ [44] | 1. Click chọn tháng hợp lệ trên lịch (VD: 2026/09). | - | 1. Ô tiếp nhận giá trị '2026/09'. | **Medium** |
| `[AD303-150]` | [44] 報酬月 | Check để trống [44] | 1. Để trống ô [44] và kiểm tra validation. | - | 1. Hiển thị thông báo lỗi CMMSG29: 報酬月は空欄にできません。 | **High** |
| `[AD303-151]` | [45] 振込日 | Check hiển thị [45] 振込日 | 1. Quan sát ô Datepicker [45] 振込日. | - | 1. Hiển thị nhãn '振込日', có dấu sao đỏ (*), format YYYY/MM/DD. | **Medium** |
| `[AD303-152]` | [45] 振込日 | Check chọn ngày hợp lệ [45] | 1. Click chọn ngày chuyển tiền hợp lệ trên lịch (VD: 2026/10/05). | - | 1. Ô tiếp nhận giá trị '2026/10/05'. | **Medium** |
| `[AD303-153]` | [45] 振込日 | Check để trống [45] | 1. Để trống ô [45] và kiểm tra validation. | - | 1. Hiển thị thông báo lỗi CMMSG29: 振込日は空欄にできません。 | **High** |
| `[AD303-154]` | [46] 報酬ポイント・カラオケ以外 | Check giá trị mặc định [46] | 1. Quan sát giá trị mặc định của ô [46]. | - | 1. Hiển thị giá trị mặc định ban đầu là '10'. | **Low** |
| `[AD303-155]` | [46] 報酬ポイント・カラオケ以外 | Check chặn ký tự chữ [46] | 1. Thực hiện nhập ký tự là chữ 'abc' vào ô [46]. | - | 1. Hệ thống tự động ngăn chặn hoặc báo lỗi CMMSG54: 半角数字のみ入力してください。. | **Medium** |
| `[AD303-156]` | [46] 報酬ポイント・カラオケ以外 | Check giá trị âm [46] | 1. Thực hiện nhập số âm '-5' vào ô [46]. | - | 1. Hiển thị thông báo lỗi CMMSG41: 報酬ポイント・カラオケ以外は0以上の値を入力してください。. | **High** |
| `[AD303-157]` | [46] 報酬ポイント・カラオケ以外 | Check vượt quá Max [46] | 1. Thực hiện nhập số point lớn hơn số dư tại [41] vào ô [46]. | - | 1. Hiển thị thông báo lỗi CMMSG42: 報酬ポイント・カラオケ以外は{max}以下の値を入力してください。. | **High** |
| `[AD303-158]` | [46] 報酬ポイント・カラオケ以外 | Check giá trị hợp lệ [46] | 1. Thực hiện nhập số hợp lệ trong khoảng [0, max] vào ô [46]. | - | 1. Hệ thống cho phép nhập giá trị hợp lệ. | **Medium** |
| `[AD303-159]` | [46] 報酬ポイント・カラオケ以外 | Check để trống [46] | 1. Xóa trống ô [46] và kiểm tra validation. | - | 1. Hiển thị thông báo lỗi CMMSG29: 報酬ポイント・カラオケ以外は空欄にできません。. | **High** |
| `[AD303-160]` | [47] 報酬ポイント・カラオケ | Check giá trị mặc định [47] | 1. Quan sát giá trị mặc định của ô [47]. | - | 1. Hiển thị giá trị mặc định ban đầu là '10'. | **Low** |
| `[AD303-161]` | [47] 報酬ポイント・カラオケ | Check chặn ký tự chữ [47] | 1. Thực hiện nhập ký tự là chữ 'xyz' vào ô [47]. | - | 1. Hệ thống tự động ngăn chặn hoặc báo lỗi CMMSG54: 半角数字のみ入力してください。. | **Medium** |
| `[AD303-162]` | [47] 報酬ポイント・カラオケ | Check giá trị âm [47] | 1. Thực hiện nhập số âm '-5' vào ô [47]. | - | 1. Hiển thị thông báo lỗi CMMSG41: 報酬ポイント・カラオケは0以上の値を入力してください。. | **High** |
| `[AD303-163]` | [47] 報酬ポイント・カラオケ | Check vượt quá Max [47] | 1. Thực hiện nhập số point lớn hơn số dư tại [42] vào ô [47]. | - | 1. Hiển thị thông báo lỗi CMMSG42: 報酬ポイント・カラオケは{max}以下の値を入力してください。. | **High** |
| `[AD303-164]` | [47] 報酬ポイント・カラオケ | Check giá trị hợp lệ [47] | 1. Thực hiện nhập số hợp lệ trong khoảng [0, max] vào ô [47]. | - | 1. Hệ thống cho phép nhập giá trị hợp lệ. | **Medium** |
| `[AD303-165]` | [47] 報酬ポイント・カラオケ | Check để trống [47] | 1. Xóa trống ô [47] và kiểm tra validation. | - | 1. Hiển thị thông báo lỗi CMMSG29: 報酬ポイント・カラオケは空欄にできません。. | **High** |
| `[AD303-166]` | [48] 報酬ポイント・ファミリア | Check giá trị mặc định [48] | 1. Quan sát giá trị mặc định của ô [48]. | - | 1. Hiển thị giá trị mặc định ban đầu là '10'. | **Low** |
| `[AD303-167]` | [48] 報酬ポイント・ファミリア | Check chặn ký tự chữ [48] | 1. Thực hiện nhập ký tự là chữ 'def' vào ô [48]. | - | 1. Hệ thống tự động ngăn chặn hoặc báo lỗi CMMSG54: 半角数字のみ入力してください。. | **Medium** |
| `[AD303-168]` | [48] 報酬ポイント・ファミリア | Check giá trị âm [48] | 1. Thực hiện nhập số âm '-5' vào ô [48]. | - | 1. Hiển thị thông báo lỗi CMMSG41: 報酬ポイント・ファミリアは0以上の値を入力してください。. | **High** |
| `[AD303-169]` | [48] 報酬ポイント・ファミリア | Check vượt quá Max [48] | 1. Thực hiện nhập số point lớn hơn số dư tại [43] vào ô [48]. | - | 1. Hiển thị thông báo lỗi CMMSG42: 報酬ポイント・ファミリアは{max}以下の値を入力してください。. | **High** |
| `[AD303-170]` | [48] 報酬ポイント・ファミリア | Check giá trị hợp lệ [48] | 1. Thực hiện nhập số hợp lệ trong khoảng [0, max] vào ô [48]. | - | 1. Hệ thống cho phép nhập giá trị hợp lệ. | **Medium** |
| `[AD303-171]` | [48] 報酬ポイント・ファミリア | Check để trống [48] | 1. Xóa trống ô [48] và kiểm tra validation. | - | 1. Hiển thị thông báo lỗi CMMSG29: 報酬ポイント・ファミリアは空欄にできません。. | **High** |
| `[AD303-172]` | [49] 報酬率 | Check giá trị mặc định [49] | 1. Quan sát giá trị mặc định của ô [49]. | - | 1. Hiển thị giá trị mặc định là '10' kèm ký hiệu '%'. | **Low** |
| `[AD303-173]` | [49] 報酬率 | Check chặn ký tự chữ [49] | 1. Thực hiện nhập ký tự là chữ vào ô [49]. | - | 1. Hệ thống tự động chặn ký tự chữ theo CMR04. | **Low** |
| `[AD303-174]` | [49] 報酬率 | Check giá trị âm [49] | 1. Thực hiện nhập số âm '-5' vào ô [49]. | - | 1. Hiển thị thông báo lỗi CMMSG41: 報酬率は0以上の値を入力してください。. | **High** |
| `[AD303-175]` | [49] 報酬率 | Check vượt quá 100% [49] | 1. Thực hiện nhập số '105' vào ô [49]. | - | 1. Hiển thị thông báo lỗi CMMSG42: 報酬率は100以下の値を入力してください。. | **High** |
| `[AD303-176]` | [49] 報酬率 | Check số thập phân [49] | 1. Thực hiện nhập số thập phân '55.5' vào ô [49]. | - | 1. Hệ thống cho phép nhập số thập phân hợp lệ. | **Medium** |
| `[AD303-177]` | [49] 報酬率 | Check để trống [49] | 1. Xóa trống ô [49] và kiểm tra validation. | - | 1. Hiển thị thông báo lỗi CMMSG29: 報酬率は空欄にできません。. | **High** |
| `[AD303-178]` | [50] 計算 | Check click nút [50] 計算 | 1. Nhập các trường point và tỷ lệ thưởng, sau đó click [計算]. | - | 1. Hệ thống thực hiện tính toán quy đổi point sang tiền yên: số P * tỷ lệ thưởng. | **High** |
| `[AD303-179]` | [50] 計算 | Check làm tròn xuống khi tính | 1. Kiểm tra kết quả tính toán khi ra số lẻ thập phân. | - | 1. Hệ thống tự động làm tròn xuống (round down) thành số nguyên theo Spec. | **High** |
| `[AD303-180]` | [51] カラオケ以外報酬（円）： | Check hiển thị nhãn [51] | 1. Quan sát số tiền tại nhãn [51] カラオケ以外報酬（円）： sau khi bấm 計算. | - | 1. Hiển thị đúng số tiền thưởng non-karaoke quy đổi kèm dấu phẩy phân cách hàng nghìn. | **Medium** |
| `[AD303-181]` | [52] カラオケ報酬（円）： | Check hiển thị nhãn [52] | 1. Quan sát số tiền tại nhãn [52] カラオケ報酬（円）： sau khi bấm 計算. | - | 1. Hiển thị đúng số tiền thưởng karaoke quy đổi kèm dấu phẩy phân cách. | **Medium** |
| `[AD303-182]` | [53] ファミリア報酬（円）： | Check hiển thị nhãn [53] | 1. Quan sát số tiền tại nhãn [53] ファミリア報酬（円）： sau khi bấm 計算. | - | 1. Hiển thị đúng số tiền thưởng familia quy đổi kèm dấu phẩy phân cách. | **Medium** |
| `[AD303-183]` | [54] 合計（円）： | Check hiển thị nhãn [54] | 1. Quan sát số tiền tại nhãn [54] 合計（円）： sau khi bấm 計算. | - | 1. Khớp chính xác tổng tiền thưởng admin sẽ chuyển: [54] = [51] + [52] + [53]. | **High** |
| `[AD303-184]` | [55] キャンセル | Check hủy khi chưa sửa | 1. Chưa thay đổi dữ liệu trong modal, click [キャンセル]. | - | 1. Modal AD3031 đóng lại ngay lập tức, quay về màn AD303. | **Low** |
| `[AD303-185]` | [55] キャンセル | Check cảnh báo thoát khi đã sửa (CMMSG46) | 1. Đã nhập/sửa dữ liệu trong modal, click [キャンセル]. | - | 1. Hiển thị popup cảnh báo CMMSG46: 戻ってもよろしいですか？保存されていない変更は失われます。 kèm 2 lựa chọn. | **High** |
| `[AD303-186]` | [55] キャンセル | Check ở lại modal khi cảnh báo | 1. Tại popup CMMSG46, click [キャンセル] (ở lại). | - | 1. Đóng popup cảnh báo, ở lại modal AD3031 và giữ nguyên dữ liệu đang nhập. | **Medium** |
| `[AD303-187]` | [55] キャンセル | Check xác nhận thoát khi cảnh báo | 1. Tại popup CMMSG46, click [OK] (xác nhận thoát). | - | 1. Đóng modal AD3031, hủy bỏ các thay đổi và trở về màn AD303. | **Medium** |
| `[AD303-188]` | [56] 完了 | Check disabled nút [56] khi chưa hợp lệ | 1. Khi chưa nhập đủ các trường required hoặc chưa click nút [50] 計算. | - | 1. Nút [完了] ở trạng thái bị khóa (disabled), không thể click. | **High** |
| `[AD303-189]` | [56] 完了 | Check enabled nút [56] khi hợp lệ | 1. Sau khi nhập đủ, hợp lệ toàn bộ các trường và click [50] 計算 thành công. | - | 1. Nút [完了] chuyển sang trạng thái kích hoạt (enabled), cho phép click. | **High** |
| `[AD303-190]` | [56] 完了 | Check click tạo bản ghi thành công | 1. Click nút [完了] khi nút enabled. | - | 1. Hệ thống gọi API tạo bản ghi, hiển thị thông báo thành công CMMSG12: 正常に作成されました。 (hoặc CMMSG17: 正常に保存されました。). | **High** |
| `[AD303-191]` | [56] 完了 | Check cập nhật giao diện sau khi tạo | 1. Quan sát giao diện sau khi tạo thành công. | - | 1. Modal AD3031 tự động đóng lại, bảng 1 (報酬履歴) tự động cập nhật dòng mới, đồng thời số liệu được phản ánh lên màn AS100. | **High** |
| `[AD303-192]` | [-] Modal AD3032 (Sửa bản ghi) | Check hiển thị dữ liệu ban đầu trên Modal AD3032 | 1. Mở modal AD3032 từ bảng 1. | - | 1. Modal hiển thị đầy đủ và chính xác toàn bộ dữ liệu ban đầu của bản ghi đang sửa. | **High** |
| `[AD303-193]` | [-] Modal AD3032 (Sửa bản ghi) | Check giới hạn Max của các trường Point khi Edit | 1. Kiểm tra giới hạn Max cho phép nhập tại các trường [46], [47], [48] khi edit. | - | 1. Giá trị Max = số dư hiện tại của agency + số point của chính bản ghi đang edit theo Spec. | **High** |
| `[AD303-194]` | [-] Modal AD3032 (Sửa bản ghi) | Check giới hạn Max của các trường Point khi Edit | 1. Nhập số point vượt quá (số dư hiện tại + số point của bản ghi đang edit). | - | 1. Hiển thị thông báo lỗi CMMSG42: 報酬ポイントは{max}以下の値を入力してください。. | **High** |
| `[AD303-195]` | [57] 削除 | Check nút [57] 削除 trong modal AD3032 | 1. Click nút [削除] trên modal AD3032. | - | 1. Hiển thị popup xác nhận xóa CMMSG28: 本当に進みますか？ kèm nút [キャンセル] và [削除]. | **High** |
| `[AD303-196]` | [57] 削除 | Check nút [57] 削除 trong modal AD3032 | 1. Tại popup CMMSG28, click [キャンセル]. | - | 1. Đóng popup xác nhận, ở lại modal AD3032 giữ nguyên dữ liệu. | **Medium** |
| `[AD303-197]` | [57] 削除 | Check nút [57] 削除 trong modal AD3032 | 1. Tại popup CMMSG28, click [削除]. | - | 1. Hệ thống gọi API xóa bản ghi, hiển thị thông báo CMMSG14: 正常に削除されました。, đóng modal và cập nhật bảng 1 cùng màn AS100. | **High** |
| `[AD303-198]` | [58] 保存 | Check nút [58] 保存 (Lưu chỉnh sửa) | 1. Sửa dữ liệu trong modal AD3032 nhưng chưa click [計算]. | - | 1. Nút [保存] bị khóa (disabled) không cho lưu. | **High** |
| `[AD303-199]` | [58] 保存 | Check nút [58] 保存 (Lưu chỉnh sửa) | 1. Sửa dữ liệu, click [計算] thành công và click [保存]. | - | 1. Hệ thống gọi API lưu thay đổi, hiển thị thông báo cập nhật thành công CMMSG13: 正常に更新されました。, đóng modal và cập nhật dữ liệu bảng 1 cùng màn AS100. | **High** |
| `[AD303-200]` | [-] Error Handling & RBAC | Check mất kết nối mạng khi submit | 1. Ngắt kết nối Internet trong lúc bấm [完了] / [保存] / [削除]. | - | 1. Hiển thị thông báo lỗi CMMSG8: ネットワークエラー。接続を確認してください。 | **Medium** |
| `[AD303-201]` | [-] Error Handling & RBAC | Check lỗi máy chủ 500 khi submit | 1. Giả lập API server trả về mã lỗi HTTP 500 khi lưu hoặc xóa bản ghi. | - | 1. Hiển thị thông báo lỗi CMMSG1: 予期しないサーバーエラーが発生しました。 kèm nút 再試行. | **Medium** |
| `[AD303-202]` | [-] Error Handling & RBAC | Check phân quyền Master Admin & Admin | 1. Đăng nhập với tài khoản Master Admin hoặc Admin và thao tác trên AD303. | - | 1. Cho phép thực hiện đầy đủ các quyền: xem, tìm kiếm, xuất CSV, tạo mới, chỉnh sửa và xóa bản ghi chuyển thưởng. | **High** |
| `[AD303-203]` | [-] Error Handling & RBAC | Check phân quyền Monitor / Giám sát viên | 1. Đăng nhập với tài khoản role Monitor/Staff và truy cập AD303. | - | 1. Cho phép xem số liệu và tìm kiếm; các nút [報酬記録追加], [CSV出力], icon Sửa và Xóa bị vô hiệu hóa (disabled) hoặc ẩn. | **High** |