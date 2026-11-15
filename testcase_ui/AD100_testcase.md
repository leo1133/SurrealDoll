# BẢNG ĐẶC TẢ KIỂM THỬ GIAO DIỆN THỦ CÔNG (MANUAL UI TEST SUITE)
## Màn hình: AD100_Agency List / Search (Danh Sách & Tìm Kiếm Agency - 事務所一覧・検索)
### Phân hệ: Master Admin Web (`AA000`) / Quản lý Agency (`AD` Module)
### Áp dụng: Quy chuẩn Trụ cột 2 (`Universal_Rules/02_manual_ui_test_case_rule.md`) & Thư viện `UI_controls/`

---

## BẢNG ĐIỀU KHIỂN TIẾN ĐỘ & THỐNG KÊ (DASHBOARD HEADER)

| Thuộc tính | Giá trị | Thuộc tính | Giá trị | Round 1 Metric | Kết quả | Round 2 Metric | Kết quả |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Module Code** | `AD100` | **Environment** | `Dev-Admin` / `STG-Admin` | **Pass** | 0 | **Pass** | 0 |
| **Total Testcases** | **78** | **% Executed** | 0% | **Fail** | 0 | **Fail** | 0 |
| **Plan to Execute** | **78** | **Creator** | `NgaDTP` | **Impact** | 0 | **Impact** | 0 |
| **Spec Source** | `Surreal SPEC` | **Google Sheet Tab** | `AD100` (gid=1636466169) | **Not Run** | 78 | **Not Run** | 0 |
| | | | | **Total** | 78 | **Total** | 0 |

---

## CHI TIẾT BẢNG TEST CASES (7 CỘT CHUẨN MARKDOWN)

| ID | Title | Big item | Steps | Pre-condition | Expected | Priority |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| | **I. COMMON & NAVIGATION** | | | | | |
| `[AD100-1]` | [0] Kiểm tra truy cập màn hình | Check hiển thị menu & sidebar | 1. Đăng nhập hệ thống Admin với tài khoản Master Admin 2. Quan sát menu Sidebar | User là Master Admin đăng nhập thành công | 1. Menu Sidebar hiển thị đầy đủ; menu cha '事務所管理' ở trạng thái mở rộng và menu con '事務所一覧' được highlight active | **High** |
| `[AD100-2]` | [0] Kiểm tra truy cập màn hình | Check điều hướng menu sidebar | 1. Đang ở màn hình khác, click vào menu '事務所管理 > 事務所一覧' | - | 1. Hệ thống điều hướng thành công về màn hình danh sách AD100, URL hiển thị `/admin/agencies` | **High** |
| `[AD100-3]` | [0] Kiểm tra truy cập màn hình | Check điều hướng Inbound Deep-link | 1. Truy cập trực tiếp URL `https://admin-dev.surrealdolls.com/admin/agencies` | - | 1. Màn hình AD100 tải thành công danh sách Agency trang 1 với bộ lọc mặc định | **High** |
| `[AD100-4]` | [0] Kiểm tra truy cập màn hình | Check Inbound với query params | 1. Truy cập URL chứa query params `?q=Tokyo&status=1` | - | 1. Ô tìm kiếm tự động điền 'Tokyo', dropdown trạng thái tự chọn '利用中', danh sách tự động search trả về đúng kết quả | **High** |
| `[AD100-5]` | [0] Kiểm tra truy cập màn hình | Check Inbound với params không có data | 1. Truy cập URL chứa query params `?q=NonExistentAgency999` | - | 1. Ô tìm kiếm điền giá trị; bảng dữ liệu hiển thị thông báo Empty state CMMSG47: 一致する検索結果はありません。 | **Medium** |
| `[AD100-6]` | [0] Kiểm tra truy cập màn hình | Check Screen Lifecycle F5 Reload | 1. Nhập từ khóa 'Agency A' và chọn status '利用中' 2. Nhấn phím F5 Reload trình duyệt | - | 1. Trang web tải lại thành công, bảo lưu nguyên vẹn từ khóa tìm kiếm và giá trị dropdown đã chọn | **Medium** |
| `[AD100-7]` | [0] Kiểm tra truy cập màn hình | Check phân quyền RBAC | 1. Đăng nhập với tài khoản Agency Admin hoặc User thông thường 2. Truy cập URL `/admin/agencies` | - | 1. Hệ thống chặn truy cập, hiển thị thông báo lỗi CMMSG5: この操作を行う権限がありません。 (hoặc redirect về trang đăng nhập tương ứng) | **High** |
| `[AD100-8]` | [0] Breadcrumbs | Check hiển thị breadcrumb | 1. Quan sát thanh Breadcrumbs ở phía trên bảng | - | 1. Hiển thị text đúng: '＞ 事務所管理' theo chuẩn CMR35 | **Low** |
| `[AD100-9]` | [0] Breadcrumbs | Check click breadcrumb | 1. Click vào text '事務所管理' trên breadcrumb | - | 1. Ở nguyên màn hình AD100, không bị reload lại trang | **Low** |
| | **II. MAIN SCREEN CONTROLS** | | | | | |
| `[AD100-10]` | [2] Search box | Check hiển thị và placeholder | 1. Quan sát ô tìm kiếm từ khóa | - | 1. Hiển thị dạng search box, placeholder hiển thị text: '事務所名・事務所ID' | **Medium** |
| `[AD100-11]` | [2] Search box | Kiểm tra nhập ký tự chữ | 1. Click vào ô tìm kiếm 2. Nhập ký tự chữ tiếng Nhật '事務所' và chữ Latin 'Agency' | - | 1. Con trỏ chuột dạng I-beam, hệ thống cho phép nhập đầy đủ ký tự | **Medium** |
| `[AD100-12]` | [2] Search box | Kiểm tra nhập ký tự số | 1. Nhập chuỗi số '123456' vào ô tìm kiếm | - | 1. Hệ thống cho phép nhập số bình thường | **Medium** |
| `[AD100-13]` | [2] Search box | Kiểm tra nhập ký tự đặc biệt | 1. Nhập chuỗi ký tự đặc biệt '!@#$%^&*()' vào ô tìm kiếm | - | 1. Hệ thống cho phép nhập ký tự đặc biệt | **Low** |
| `[AD100-14]` | [2] Search box | Kiểm tra nhập khoảng trắng | 1. Nhập khoảng trắng ở đầu, giữa và cuối chuỗi từ khóa (VD: '  Agency  ') | - | 1. Hệ thống nhận ký tự space; khi tìm kiếm tự động trim khoảng trắng ở đầu và cuối | **Low** |
| `[AD100-15]` | [2] Search box | Kiểm tra paste dữ liệu | 1. Copy một chuỗi văn bản và paste vào ô tìm kiếm | - | 1. Hệ thống tiếp nhận chuỗi ký tự vừa paste | **Low** |
| `[AD100-16]` | [2] Search box | Kiểm tra nút xóa nhanh (X) | 1. Nhập từ khóa vào ô tìm kiếm 2. Click vào icon (X) trong ô | - | 1. Xóa toàn bộ từ khóa trong ô tìm kiếm ngay lập tức | **Low** |
| `[AD100-17]` | [2] Search box | Tìm kiếm bằng phím Enter | 1. Nhập mã Agency ID hợp lệ vào ô tìm kiếm 2. Nhấn phím Enter trên bàn phím | - | 1. Hệ thống tự động kích hoạt tìm kiếm tương tự click nút 検索, tải danh sách khớp từ khóa | **High** |
| `[AD100-18]` | [2] Search box | Nhấn Enter khi ô rỗng | 1. Để trống ô tìm kiếm 2. Nhấn phím Enter | - | 1. Hệ thống chặn request tìm kiếm thừa hoặc tải lại toàn bộ danh sách mặc định | **Low** |
| `[AD100-19]` | [2] Search box | Tìm kiếm một phần tên Agency | 1. Nhập một phần tên Agency (Partial match) 2. Bấm 検索 | - | 1. Bảng dữ liệu hiển thị toàn bộ Agency có tên chứa cụm từ vừa nhập | **High** |
| `[AD100-20]` | [2] Search box | Tìm kiếm chính xác Agency ID | 1. Nhập chính xác mã Agency ID (Exact match) 2. Bấm 検索 | - | 1. Bảng dữ liệu hiển thị đúng duy nhất 1 bản ghi Agency khớp mã ID đó | **High** |
| `[AD100-21]` | [2] Search box | Tìm kiếm chính xác System ID | 1. Nhập chính xác mã System ID 2. Bấm 検索 | - | 1. Bảng dữ liệu hiển thị đúng bản ghi khớp System ID do hệ thống tự sinh | **High** |
| `[AD100-22]` | [3] Dropdown ステータス | Check hiển thị và giá trị mặc định | 1. Quan sát dropdown lọc trạng thái | - | 1. Hiển thị dropdown với giá trị mặc định là '全て' | **High** |
| `[AD100-23]` | [3] Dropdown ステータス | Kiểm tra danh sách options | 1. Click mở dropdown ステータス | - | 1. Danh sách hiển thị đầy đủ 3 lựa chọn đúng thứ tự Spec: '全て', '利用中', '停止中' | **Medium** |
| `[AD100-24]` | [3] Dropdown ステータス | Chọn option '利用中' | 1. Mở dropdown -> Click chọn '利用中' 2. Bấm 検索 | - | 1. Dropdown hiển thị '利用中'; bảng dữ liệu chỉ hiển thị các Agency có trạng thái 利用中 (Active) | **High** |
| `[AD100-25]` | [3] Dropdown ステータス | Chọn option '停止中' | 1. Mở dropdown -> Click chọn '停止中' 2. Bấm 検索 | - | 1. Dropdown hiển thị '停止中'; bảng dữ liệu chỉ hiển thị các Agency có trạng thái 停止中 (Inactive, hàng bị làm xám) | **High** |
| `[AD100-26]` | [3] Dropdown ステータス | Chọn lại option '全て' | 1. Mở dropdown -> Click chọn '全て' 2. Bấm 検索 | - | 1. Bảng dữ liệu hiển thị toàn bộ Agency của cả 2 trạng thái | **Medium** |
| `[AD100-27]` | [3] Dropdown ステータス | Click ra ngoài dropdown | 1. Click mở dropdown 2. Click vào khoảng trống ngoài dropdown | - | 1. Dropdown tự động đóng lại, giữ nguyên giá trị đã chọn trước đó | **Low** |
| `[AD100-28]` | [4] Button 検索 | Tìm kiếm mặc định | 1. Giữ nguyên bộ lọc mặc định (Trống từ khóa, Status = 全て) 2. Click nút 検索 | - | 1. Gọi API tải danh sách Agency toàn hệ thống, sắp xếp theo ngày cập nhật mới nhất (updated_at DESC) | **High** |
| `[AD100-29]` | [4] Button 検索 | Tìm kiếm kết hợp (AND logic) | 1. Nhập tên Agency và chọn Status = '利用中' 2. Click nút 検索 | - | 1. Danh sách trả về chỉ chứa các Agency vừa khớp tên vừa có trạng thái '利用中' | **High** |
| `[AD100-30]` | [4] Button 検索 | Debounce chống double-click | 1. Nhấp đúp (Double-click liên tục) vào nút 検索 | - | 1. Nút 検索 tạm thời bị vô hiệu hóa (Disabled) theo CMR15, chỉ gửi duy nhất 1 request lên server | **Medium** |
| `[AD100-31]` | [4] Button 検索 | Hiển thị trạng thái Loading | 1. Click nút 検索 khi mạng chậm | - | 1. Hiển thị hiệu ứng loading (Spinner / Skeleton screen) theo CMMSG27, bảng dữ liệu không bị vỡ layout | **Medium** |
| `[AD100-32]` | [4] Button クリア | Reset điều kiện tìm kiếm | 1. Nhập từ khóa 'Agency Test', chọn status '停止中' 2. Click nút クリア | - | 1. Ô tìm kiếm bị xóa trắng, dropdown tự chuyển về '全て', hệ thống tự động kích hoạt tìm kiếm tải lại danh sách mặc định | **High** |
| `[AD100-33]` | [5] Button 新規登録 | Check hiển thị nút 新規登録 | 1. Quan sát nút 新規登録 phía trên bảng | - | 1. Hiển thị nút bấm Primary màu xanh nổi bật với text '新規登録' | **Medium** |
| `[AD100-34]` | [5] Button 新規登録 | Click điều hướng sang AD200 | 1. Click nút [新規登録] | - | 1. Hệ thống điều hướng sang màn hình tạo mới Agency AD200, URL hiển thị `/admin/agencies/create` | **High** |
| `[AD100-35]` | Bảng dữ liệu - Header | Header cột [6] ID | 1. Quan sát tiêu đề cột ID | - | 1. Hiển thị text 'ID', căn giữa | **Low** |
| `[AD100-36]` | Bảng dữ liệu - Header | Header cột [7] 事務所ID | 1. Quan sát tiêu đề cột 事務所ID | - | 1. Hiển thị text '事務所ID', căn trái | **Low** |
| `[AD100-37]` | Bảng dữ liệu - Header | Header cột [8] 事務所名 | 1. Quan sát tiêu đề cột 事務所名 | - | 1. Hiển thị text '事務所名', căn trái | **Low** |
| `[AD100-38]` | Bảng dữ liệu - Header | Header cột [9] 連絡先 オーナー名 | 1. Quan sát tiêu đề cột 連絡先 オーナー名 | - | 1. Hiển thị text '連絡先 オーナー名', căn trái | **Low** |
| `[AD100-39]` | Bảng dữ liệu - Header | Header cột [10] ライバー数 | 1. Quan sát tiêu đề cột ライバー数 | - | 1. Hiển thị text 'ライバー数', căn phải (hoặc giữa) theo CR 06/11/2025 | **Low** |
| `[AD100-40]` | Bảng dữ liệu - Header | Header cột [10] ポイント売上 | 1. Quan sát tiêu đề cột ポイント売上 | - | 1. Hiển thị text 'ポイント売上', căn phải | **Low** |
| `[AD100-41]` | Bảng dữ liệu - Header | Header cột [10] ファミリア売上 | 1. Quan sát tiêu đề cột ファミリア売上 | - | 1. Hiển thị text 'ファミリア売上', căn phải | **Low** |
| `[AD100-42]` | Bảng dữ liệu - Header | Header cột [10] 売上合計 | 1. Quan sát tiêu đề cột 売上合計 | - | 1. Hiển thị text '売上合計', căn phải | **Low** |
| `[AD100-43]` | Bảng dữ liệu - Header | Header cột [11] ステータス | 1. Quan sát tiêu đề cột ステータス | - | 1. Hiển thị text 'ステータス', căn giữa | **Low** |
| `[AD100-44]` | Bảng dữ liệu - Header | Header cột [12] 作成日 | 1. Quan sát tiêu đề cột 作成日 kèm icon sort | - | 1. Hiển thị text '作成日', căn giữa, có icon sắp xếp | **Low** |
| `[AD100-45]` | Bảng dữ liệu - Header | Header cột [13] 変更日 | 1. Quan sát tiêu đề cột 変更日 kèm icon sort | - | 1. Hiển thị text '変更日', căn giữa, có icon sắp xếp | **Low** |
| `[AD100-46]` | Bảng dữ liệu - Header | Header cột [14] Thao tác | 1. Quan sát tiêu đề cột hành động | - | 1. Cột thao tác hiển thị icon chi tiết | **Low** |
| `[AD100-47]` | Bảng dữ liệu - Sort | Sort cột 作成日 | 1. Click vào header cột 作成日 lần 1 2. Click lần 2 | - | 1. Lần 1: Sắp xếp theo ngày tạo cũ nhất -> mới nhất; Lần 2: Sắp xếp mới nhất -> cũ nhất | **Medium** |
| `[AD100-48]` | Bảng dữ liệu - Sort | Sort cột 変更日 | 1. Click vào header cột 変更日 | - | 1. Danh sách đảo chiều sắp xếp theo ngày cập nhật thông tin | **Medium** |
| `[AD100-49]` | Bảng dữ liệu - Data Cell | Data mapping cột ID & 事務所ID | 1. Đối chiếu ID hệ thống và mã 事務所ID trên từng dòng | - | 1. Hiển thị chính xác System ID và Agency Code tương ứng | **Medium** |
| `[AD100-50]` | Bảng dữ liệu - Data Cell | Data mapping Logo & Tên Agency | 1. Quan sát ô 事務所名 trên bảng | - | 1. Hiển thị ảnh logo đại diện thu nhỏ (thumbnail) cùng tên Agency, ảnh không bị méo tỷ lệ | **Medium** |
| `[AD100-51]` | Bảng dữ liệu - Data Cell | Check hiển thị ライバー数 | 1. Kiểm tra số lượng user trực thuộc tại cột ライバー数 | - | 1. Hiển thị tổng số user có status 所属済み (active + inactive); không gồm user đã rời/xóa (CR 06/11/2025) | **High** |
| `[AD100-52]` | Bảng dữ liệu - Action | Click ライバー数 điều hướng sang AD302 | 1. Click vào con số ở cột [10] ライバー数 của 1 Agency | - | 1. Hệ thống điều hướng sang màn hình AD302 (Tab ライバー一覧) của đúng Agency đó | **High** |
| `[AD100-53]` | Bảng dữ liệu - Data Cell | Check số liệu doanh thu 3 cột | 1. Đối chiếu ポイント売上, ファミリア売上 và 売上合計 | - | 1. 売上合計 = ポイント売上 + ファミリア売上; các giá trị tiền/điểm có định dạng dấu phẩy phân cách hàng nghìn | **High** |
| `[AD100-54]` | Bảng dữ liệu - Data Cell | Check hiển thị trạng thái ステータス | 1. Quan sát badge trạng thái tại cột ステータス | - | 1. Hiển thị badge màu tương ứng: '利用中' (màu xanh/active) hoặc '停止中' (màu xám/inactive) | **Medium** |
| `[AD100-55]` | Bảng dữ liệu - Data Cell | Hiển thị hàng Agency bị 停止中 | 1. Quan sát dòng của Agency có trạng thái 停止中 | - | 1. Toàn bộ dòng của Agency 停止中 bị làm mờ/xám (grey out) nhưng vẫn cho phép click vào xem chi tiết | **Medium** |
| `[AD100-56]` | Bảng dữ liệu - Data Cell | Format ngày tháng 作成日 & 変更日 | 1. Quan sát định dạng ngày tại cột [12] và [13] | - | 1. Định dạng hiển thị chuẩn `YYYY/MM/DD` | **Low** |
| `[AD100-57]` | Bảng dữ liệu - Action | Click icon Chi tiết / Click dòng | 1. Click vào nút Chi tiết (hoặc click vào dòng Agency) | - | 1. Điều hướng sang màn hình chi tiết Agency AD301 tương ứng (`/admin/agencies/{id}`) | **High** |
| `[AD100-58]` | Bảng dữ liệu - Action | Kiểm tra KHÔNG CÓ nút Xóa (CR 13/08/2026) | 1. Quan sát toàn bộ các nút hành động trên từng dòng bảng AD100 | - | 1. Không hiển thị nút Xóa (thùng rác) trên bảng AD100 theo CR 13/08/2026 (chỉ xóa trong AD301) | **High** |
| `[AD100-59]` | [Pagination] Phân trang | Viewpoint 1: UI Mặc định phân trang | 1. Mở màn hình AD100 2. Quan sát thanh phân trang phía dưới bảng | Dữ liệu tổng > 10 bản ghi | 1. Hiển thị đầy đủ thanh phân trang theo CMR23; Trang 1 được highlight active | **High** |
| `[AD100-60]` | [Pagination] Phân trang | Viewpoint 2: Page Size cố định | 1. Đếm số bản ghi hiển thị trên Trang 1 | Tổng số bản ghi $\ge 10$ | 1. Hiển thị tối đa đúng 10 dòng/trang theo chuẩn CMR01 | **High** |
| `[AD100-61]` | [Pagination] Phân trang | Viewpoint 3: Chuyển trang trực tiếp | 1. Click vào số trang '2' trên thanh phân trang | - | 1. Hệ thống chuyển sang Trang 2, tải danh sách các bản ghi từ 11 đến 20 không bị trùng lặp | **High** |
| `[AD100-62]` | [Pagination] Phân trang | Viewpoint 3: Nút Next (次>>) và Prev (<<前) | 1. Đang ở Trang 1, click nút '次>>' 2. Tại Trang 2, click nút '<<前' | - | 1. '次>>' chuyển sang Trang 2; '<<前' quay lại Trang 1 thành công | **Medium** |
| `[AD100-63]` | [Pagination] Phân trang | Viewpoint 4: Disabled tại Trang 1 | 1. Đang ở Trang 1, quan sát nút '<<前' và First ('<<') | - | 1. Nút '<<前' và '<<' bị khóa (Disabled), không click được | **Medium** |
| `[AD100-64]` | [Pagination] Phân trang | Viewpoint 4: Disabled tại Trang cuối | 1. Điều hướng đến trang cuối cùng của danh sách 2. Quan sát nút '次>>' và Last ('>>') | - | 1. Nút '次>>' và '>>' bị khóa (Disabled), không click được | **Medium** |
| `[AD100-65]` | [Pagination] Phân trang | Viewpoint 5: Biên 0 bản ghi | 1. Nhập từ khóa không tồn tại để tìm kiếm ra 0 bản ghi | - | 1. Thanh phân trang ẩn hoàn toàn; giữa bảng hiển thị CMMSG47: 一致する検索結果はありません。 | **High** |
| `[AD100-66]` | [Pagination] Phân trang | Viewpoint 6: Biên 10 bản ghi | 1. Tìm kiếm điều kiện trả về đúng 10 bản ghi | Dữ liệu lọc có đúng 10 records | 1. Hiển thị đủ 10 dòng trên 1 trang duy nhất, thanh phân trang ẩn hoặc nút Next/Prev đều disabled | **Medium** |
| `[AD100-67]` | [Pagination] Phân trang | Viewpoint 7: Biên 11 bản ghi | 1. Tìm kiếm điều kiện trả về đúng 11 bản ghi | Dữ liệu lọc có đúng 11 records | 1. Tự động chia làm 2 trang: Trang 1 có 10 bản ghi đầu, Trang 2 có đúng 1 bản ghi lẻ cuối | **High** |
| `[AD100-68]` | [Pagination] Phân trang | Viewpoint 8: Reset về Trang 1 khi search mới | 1. Đang đứng ở Trang 3 2. Nhập từ khóa mới và click nút 検索 | - | 1. Hệ thống tự động reset về Trang 1 để hiển thị kết quả tìm kiếm mới, không bị lưu ở trang rỗng | **High** |
| `[AD100-69]` | [Pagination] Phân trang | Viewpoint 9: Rút gọn dấu '…' (CMR23) | 1. Xem danh sách khi tổng số trang > 7 | Hệ thống có > 70 bản ghi | 1. Dãy số trang tự động rút gọn bằng ký hiệu '…' (VD: `1 2 3 4 5 … 10`) | **Medium** |
| `[AD100-70]` | [Pagination] Phân trang | Viewpoint 10: Xử lý an toàn URL tampering | 1. Sửa tham số URL thành `?page=-1` hoặc `?page=99999` hoặc `?page=abc` | - | 1. Hệ thống xử lý an toàn đưa về Trang 1 hoặc Trang cuối, tuyệt đối không bị lỗi 500 hay crash trắng trang | **Medium** |
| `[AD100-71]` | Empty State | Check hiển thị khi không có bản ghi nào | 1. Tìm kiếm với điều kiện không có dữ liệu | - | 1. Giữa bảng hiển thị thông báo căn giữa chuẩn CMMSG47: 一致する検索結果はありません。 | **High** |
| `[AD100-72]` | Error Handling | Xử lý khi mất kết nối mạng Internet | 1. Ngắt kết nối mạng Internet 2. Click nút 検索 hoặc click chuyển trang | - | 1. Hệ thống hiển thị thông báo lỗi mạng chuẩn CMMSG8: ネットワークエラー。接続を確認してください。 | **Medium** |
| `[AD100-73]` | Error Handling | Xử lý khi server lỗi 500 | 1. Giả lập API `/agency/` trả về HTTP Status 500 | - | 1. Hiển thị thông báo lỗi hệ thống CMMSG1: 予期しないサーバーエラーが発生しました。 kèm nút thử lại | **Medium** |
| `[AD100-74]` | Error Handling | Hết phiên đăng nhập (Session Expired) | 1. Để phiên làm việc quá hạn hoặc xóa token đăng nhập 2. Click nút 検索 | - | 1. Hiển thị thông báo CMMSG10 (hoặc CMMSG4) và tự động chuyển hướng về trang đăng nhập Master Admin | **High** |
| | **III. SUB-LAYOUTS / MODALS** | | | | | |
| `[AD100-75]` | Sub-layout | Kiểm tra Layout Responsive | 1. Thu nhỏ kích thước trình duyệt hoặc test trên màn hình độ phân giải thấp | - | 1. Xuất hiện thanh cuộn ngang (horizontal scrollbar) cho bảng dữ liệu, không bị tràn cắt vỡ giao diện | **Low** |
| `[AD100-76]` | Sub-layout | Hover trên từng dòng bảng dữ liệu | 1. Di chuyển chuột qua từng dòng bản ghi của bảng | - | 1. Dòng đang hover đổi màu nền nhẹ (highlight row) giúp dễ quan sát | **Low** |
| `[AD100-77]` | Sub-layout | Kiểm tra text dài tên Agency | 1. Xem Agency có tên dài tối đa 20 ký tự | - | 1. Tên Agency hiển thị đầy đủ hoặc cắt gọn bằng '…' theo CMR48, hover chuột hiển thị tooltip đầy đủ | **Low** |
| `[AD100-78]` | Sub-layout | Phân quyền thao tác nút 新規登録 | 1. Đăng nhập tài khoản Admin chỉ có quyền xem (Monitor / Giám sát) | - | 1. Nút 新規登録 bị ẩn hoặc disabled không thể click tạo mới | **Medium** |
