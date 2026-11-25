# BẢNG ĐẶC TẢ KIỂM THỬ GIAO DIỆN THỦ CÔNG (MANUAL UI TEST SUITE)
## Màn hình: AF100 — Gift Manage: Gift List (Danh sách & Tìm kiếm Quà tặng)
### Phân hệ: Master Admin Web / Quản lý Quà tặng (`AF` Module)
### Áp dụng: Quy chuẩn Trụ cột 2 (`Universal_Rules/02_manual_ui_test_case_rule.md`) & Thư viện `UI_controls/`

---

## BẢNG ĐIỀU KHIỂN TIẾN ĐỘ & THỐNG KÊ (DASHBOARD HEADER)

| Thuộc tính | Giá trị | Thuộc tính | Giá trị | Round 1 Metric | Kết quả | Round 2 Metric | Kết quả |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Module Code** | `AF100` | **Environment** | `Dev-Admin` / `STG-Admin` | **Pass** | 0 | **Pass** | 0 |
| **Total Testcases** | **82** | **% Executed** | 0% | **Fail** | 0 | **Fail** | 0 |
| **Plan to Execute** | **82** | **Creator** | `QA` | **Impact** | 0 | **Impact** | 0 |
| **Spec Source** | `FEATURE_SPEC_MAP` / Figma | **Liên kết chéo** | `I600` (App Gift List), `AF200`, `AF300` | **Not Run** | 82 | **Not Run** | 0 |
| | | | | **Total** | 82 | **Total** | 0 |

---

## CHI TIẾT BẢNG TEST CASES (8 CỘT CHUẨN MARKDOWN)

| ID | Title | Big item | Steps | Pre-condition | Expected | Priority | Automation Feasibility |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| | **I. COMMON & NAVIGATION** | | | | | | |
| `[AF100-1]` | [0] Kiểm tra truy cập màn hình | Check hiển thị menu & sidebar | 1. Đăng nhập hệ thống Admin với tài khoản Master Admin 2. Quan sát menu Sidebar | User là Master Admin đăng nhập thành công | 1. Menu Sidebar hiển thị đầy đủ; menu cha 'ギフト管理' (Gift Manage) ở trạng thái mở rộng và menu con 'ギフト一覧' (Gift List) được highlight active | High | Auto-UI |
| `[AF100-2]` | [0] Kiểm tra truy cập màn hình | Check điều hướng menu sidebar | 1. Đang ở màn hình khác, click vào menu 'ギフト管理 > ギフト一覧' | - | 1. Hệ thống điều hướng thành công về màn hình AF100, URL hiển thị `/admin/gifts` (hoặc route danh sách quà tương ứng) | High | Auto-UI |
| `[AF100-3]` | [0] Kiểm tra truy cập màn hình | Check Inbound Deep-link mặc định | 1. Truy cập trực tiếp URL màn hình AF100 khi đã đăng nhập | - | 1. Màn hình AF100 tải thành công danh sách quà trang 1 với bộ lọc mặc định | High | Auto-UI |
| `[AF100-4]` | [0] Kiểm tra truy cập màn hình | Check Inbound Deep-link — Auto-fill & Auto-search | 1. Truy cập URL chứa query params `?q=Heart&status=active` | Có quà tên "Heart" đang active | 1. Ô tìm kiếm tự động điền 'Heart', dropdown trạng thái tự chọn 'ON', danh sách tự động search trả về đúng bản ghi khớp | High | Auto-UI |
| `[AF100-5]` | [0] Kiểm tra truy cập màn hình | Check Inbound Deep-link — Khớp dữ liệu | 1. Đối chiếu các dòng trả về khi mở URL `?q=Heart&category_id=1` | - | 1. Toàn bộ bản ghi trên bảng đều thỏa mãn đồng thời tên chứa "Heart" và thuộc category_id=1 | High | Auto-UI |
| `[AF100-6]` | [0] Kiểm tra truy cập màn hình | Check Inbound Deep-link — Tham số không có dữ liệu | 1. Truy cập URL chứa query params `?q=NonExistentGift999` | - | 1. Ô tìm kiếm điền giá trị; bảng dữ liệu hiển thị Empty State chuẩn CMMSG47: `一致する検索結果はありません。` | Medium | Auto-UI |
| `[AF100-7]` | [0] Kiểm tra truy cập màn hình | Check Inbound Deep-link — Tham số rỗng / không hợp lệ | 1. Truy cập URL chứa `?q=&status=invalid_val` | - | 1. Hệ thống xử lý an toàn, không crash; fallback về bộ lọc mặc định hoặc báo lỗi hợp lệ | Medium | Auto-API |
| `[AF100-8]` | [0] Kiểm tra truy cập màn hình | Check Screen Lifecycle F5 Reload | 1. Nhập từ khóa 'Star' và chọn status 'ON' 2. Nhấn phím F5 Reload trình duyệt | - | 1. Trang web tải lại thành công, bảo lưu nguyên vẹn từ khóa tìm kiếm và giá trị dropdown đã chọn (hoặc reload danh sách sạch không lỗi) | Medium | Auto-UI |
| `[AF100-9]` | [0] Kiểm tra truy cập màn hình | Check phân quyền RBAC | 1. Đăng nhập với tài khoản không có quyền Gift Manage 2. Truy cập trực tiếp URL màn AF100 | Tài khoản không có quyền Gift Manage | 1. Hệ thống chặn truy cập, hiển thị thông báo lỗi CMMSG5: `この操作を行う権限がありません。` (hoặc redirect về trang chủ) | High | Auto-API |
| `[AF100-10]` | [1] Breadcrumbs | Check hiển thị breadcrumb | 1. Quan sát thanh Breadcrumbs ở phía trên màn hình AF100 | - | 1. Hiển thị text đúng chuẩn CMR35: `＞ ギフト管理 ＞ ギフト一覧` | Low | Manual-Only (Visual) |
| `[AF100-11]` | [1] Breadcrumbs | Check click vào breadcrumb | 1. Click vào node 'ギフト管理' hoặc 'ギフト一覧' trên breadcrumb | - | 1. Ở nguyên màn hình AF100 hoặc điều hướng đúng node cha, không lỗi | Low | Auto-UI |
| | **II. MAIN SCREEN CONTROLS** | | | | | | |
| `[AF100-12]` | [2] Search box (Tên / ID quà) | Check hiển thị và placeholder | 1. Quan sát ô tìm kiếm từ khóa | - | 1. Hiển thị dạng search box, placeholder hiển thị đúng theo Spec/Figma | Medium | Manual-Only (Visual) |
| `[AF100-13]` | [2] Search box (Tên / ID quà) | Kiểm tra nhập ký tự chữ (Nhật & Latin) | 1. Click vào ô tìm kiếm 2. Nhập chữ tiếng Nhật 'ハート' và chữ Latin 'Heart' | - | 1. Con trỏ chuột dạng I-beam, hệ thống cho phép nhập đầy đủ ký tự | Medium | Auto-Data |
| `[AF100-14]` | [2] Search box (Tên / ID quà) | Kiểm tra nhập ký tự số | 1. Nhập chuỗi số '12345' vào ô tìm kiếm | - | 1. Hệ thống cho phép nhập số bình thường | Medium | Auto-Data |
| `[AF100-15]` | [2] Search box (Tên / ID quà) | Kiểm tra nhập ký tự đặc biệt | 1. Nhập chuỗi `!@#$%^&*()` vào ô tìm kiếm | - | 1. Hệ thống cho phép nhập ký tự đặc biệt, không crash giao diện | Low | Auto-Data |
| `[AF100-16]` | [2] Search box (Tên / ID quà) | Kiểm tra nhập khoảng trắng đầu/giữa/cuối | 1. Nhập `  Star Gift  ` vào ô tìm kiếm 2. Click 検索 | Có quà "Star Gift" | 1. Hệ thống tự động trim khoảng trắng đầu/cuối khi tìm kiếm, trả về đúng bản ghi "Star Gift" | Low | Auto-Data |
| `[AF100-17]` | [2] Search box (Tên / ID quà) | Kiểm tra paste dữ liệu | 1. Copy chuỗi `"Star Gift 123"` và paste vào ô tìm kiếm | - | 1. Ô tìm kiếm tiếp nhận chính xác chuỗi vừa paste | Low | Auto-UI |
| `[AF100-18]` | [2] Search box (Tên / ID quà) | Kiểm tra nút xóa nhanh (X) | 1. Nhập từ khóa vào ô tìm kiếm 2. Click vào icon (X) trong ô | - | 1. Xóa toàn bộ từ khóa trong ô tìm kiếm ngay lập tức | Low | Auto-UI |
| `[AF100-19]` | [2] Search box (Tên / ID quà) | Tìm kiếm bằng phím Enter | 1. Nhập tên quà 'Heart' 2. Nhấn phím Enter | - | 1. Hệ thống tự động kích hoạt tìm kiếm tương tự click nút 検索, tải danh sách khớp từ khóa | High | Auto-UI |
| `[AF100-20]` | [2] Search box (Tên / ID quà) | Nhấn Enter khi ô rỗng | 1. Để trống ô tìm kiếm 2. Nhấn phím Enter | - | 1. Hệ thống chặn request tìm kiếm thừa hoặc tải lại danh sách mặc định | Low | Auto-UI |
| `[AF100-21]` | [2] Search box (Tên / ID quà) | Tìm kiếm một phần tên quà (Partial match) | 1. Nhập một phần tên quà (VD: 'Ear' của 'Heart') 2. Bấm 検索 | Có quà "Heart" | 1. Bảng hiển thị các quà có tên chứa cụm 'Ear' (không phân biệt hoa/thường) | High | Auto-UI |
| `[AF100-22]` | [2] Search box (Tên / ID quà) | Tìm kiếm chính xác theo Gift ID | 1. Nhập chính xác mã Gift ID 2. Bấm 検索 | - | 1. Bảng hiển thị đúng duy nhất 1 bản ghi quà khớp Gift ID | High | Auto-UI |
| `[AF100-23]` | [3] Dropdown Danh mục (Category) | Check hiển thị và giá trị mặc định | 1. Quan sát dropdown lọc danh mục | - | 1. Hiển thị dropdown kèm icon mũi tên xổ xuống với giá trị mặc định là '全て' (Tất cả) | High | Auto-UI |
| `[AF100-24]` | [3] Dropdown Danh mục (Category) | Kiểm tra danh sách options | 1. Click mở dropdown danh mục | Có ≥ 2 danh mục trong `AF400` | 1. Danh sách hiển thị '全て' và đầy đủ các danh mục đang có trong hệ thống đúng thứ tự | Medium | Auto-UI |
| `[AF100-25]` | [3] Dropdown Danh mục (Category) | Chọn từng option danh mục cụ thể | 1. Mở dropdown -> Click chọn lần lượt từng danh mục (VD: Normal, Special) 2. Bấm 検索 | - | 1. Dropdown đóng lại, hiển thị tên danh mục đã chọn; bảng chỉ hiển thị các quà thuộc danh mục đó | High | Auto-UI |
| `[AF100-26]` | [3] Dropdown Danh mục (Category) | Click ra ngoài dropdown | 1. Click mở dropdown 2. Click vào khoảng trống ngoài dropdown | - | 1. Dropdown tự động đóng lại, giữ nguyên giá trị đã chọn trước đó | Low | Auto-UI |
| `[AF100-27]` | [4] Dropdown Trạng thái (Status) | Check hiển thị và giá trị mặc định | 1. Quan sát dropdown lọc trạng thái | - | 1. Hiển thị dropdown với giá trị mặc định là '全て' | High | Auto-UI |
| `[AF100-28]` | [4] Dropdown Trạng thái (Status) | Chọn option 'ON' (Active) | 1. Mở dropdown -> Click chọn 'ON' 2. Bấm 検索 | - | 1. Dropdown hiển thị 'ON'; bảng chỉ hiển thị các quà đang bật (ON) | High | Auto-UI |
| `[AF100-29]` | [4] Dropdown Trạng thái (Status) | Chọn option 'OFF' (Inactive) | 1. Mở dropdown -> Click chọn 'OFF' 2. Bấm 検索 | - | 1. Dropdown hiển thị 'OFF'; bảng chỉ hiển thị các quà đang tắt (OFF) | High | Auto-UI |
| `[AF100-30]` | [4] Dropdown Trạng thái (Status) | Chọn lại option '全て' | 1. Mở dropdown -> Click chọn '全て' 2. Bấm 検索 | - | 1. Bảng hiển thị toàn bộ quà ở cả 2 trạng thái ON và OFF | Medium | Auto-UI |
| `[AF100-31]` | [4] Dropdown Trạng thái (Status) | Click ra ngoài dropdown | 1. Click mở dropdown 2. Click ra ngoài vùng dropdown | - | 1. Dropdown tự đóng lại, giữ nguyên giá trị cũ | Low | Auto-UI |
| `[AF100-32]` | [5] Button 検索 (Search) | Tìm kiếm mặc định | 1. Giữ nguyên bộ lọc mặc định 2. Click nút 検索 | - | 1. Tải danh sách toàn bộ quà sắp xếp theo `sort_order` tăng dần (hoặc mới nhất theo Spec) | High | Auto-UI |
| `[AF100-33]` | [5] Button 検索 (Search) | Tìm kiếm kết hợp nhiều tiêu chí (AND logic) | 1. Nhập tên 'Star' + chọn Category 'Normal' + chọn Status 'ON' 2. Click 検索 | - | 1. Bảng chỉ trả về các quà thỏa mãn đồng thời cả 3 điều kiện lọc | High | Auto-UI |
| `[AF100-34]` | [5] Button 検索 (Search) | Debounce chống double-click (CMR15) | 1. Nhấp đúp liên tục vào nút 検索 | - | 1. Nút 検索 tạm thời bị disabled trong khi API đang xử lý theo CMR15, chỉ gửi 1 request | Medium | Auto-UI |
| `[AF100-35]` | [5] Button 検索 (Search) | Hiển thị trạng thái Loading (CMMSG27) | 1. Click nút 検索 khi mạng chậm (Slow 3G) | - | 1. Hiển thị Spinner / Skeleton screen theo CMMSG27 (`読み込み中、しばらくお待ちください...`), không vỡ layout | Medium | Manual-Only (Visual) |
| `[AF100-36]` | [6] Button クリア (Clear) | Reset toàn bộ điều kiện lọc | 1. Nhập từ khóa, chọn Category và Status 2. Click nút クリア | - | 1. Toàn bộ bộ lọc reset về mặc định ('', '全て', '全て') và tự động tải lại danh sách mặc định | High | Auto-UI |
| `[AF100-37]` | [7] Button 新規登録 (Create Gift) | Check hiển thị nút tạo mới | 1. Quan sát nút 新規登録 phía trên bảng | - | 1. Hiển thị nút Primary nổi bật với text '新規登録' | Medium | Manual-Only (Visual) |
| `[AF100-38]` | [7] Button 新規登録 (Create Gift) | Click điều hướng sang AF200 | 1. Click nút [新規登録] | - | 1. Điều hướng sang màn hình tạo mới quà tặng AF200 | High | Auto-UI |
| `[AF100-39]` | [8] Bảng dữ liệu - Header | Header cột ID | 1. Quan sát tiêu đề cột ID | - | 1. Hiển thị text 'ID', căn giữa | Low | Auto-UI |
| `[AF100-40]` | [8] Bảng dữ liệu - Header | Header cột Icon / Thumbnail | 1. Quan sát tiêu đề cột ảnh đại diện quà | - | 1. Hiển thị tiêu đề cột ảnh, căn giữa | Low | Auto-UI |
| `[AF100-41]` | [8] Bảng dữ liệu - Header | Header cột Tên quà (Gift Name) | 1. Quan sát tiêu đề cột tên quà | - | 1. Hiển thị đúng tiêu đề tên quà, căn trái | Low | Auto-UI |
| `[AF100-42]` | [8] Bảng dữ liệu - Header | Header cột Danh mục (Category) | 1. Quan sát tiêu đề cột danh mục | - | 1. Hiển thị đúng tiêu đề danh mục, căn trái | Low | Auto-UI |
| `[AF100-43]` | [8] Bảng dữ liệu - Header | Header cột Giá Coin (Coin Price) | 1. Quan sát tiêu đề cột giá coin | - | 1. Hiển thị đúng tiêu đề giá coin, căn phải | Low | Auto-UI |
| `[AF100-44]` | [8] Bảng dữ liệu - Header | Header cột Thứ tự (Sort Order) | 1. Quan sát tiêu đề cột thứ tự | - | 1. Hiển thị đúng tiêu đề thứ tự hiển thị, căn phải | Low | Auto-UI |
| `[AF100-45]` | [8] Bảng dữ liệu - Header | Header cột Trạng thái (Status) | 1. Quan sát tiêu đề cột trạng thái | - | 1. Hiển thị đúng tiêu đề trạng thái, căn giữa | Low | Auto-UI |
| `[AF100-46]` | [8] Bảng dữ liệu - Header | Header cột Ngày tạo / Ngày sửa | 1. Quan sát tiêu đề cột ngày tạo và ngày cập nhật | - | 1. Hiển thị đúng tiêu đề ngày tháng, căn giữa | Low | Auto-UI |
| `[AF100-47]` | [8] Bảng dữ liệu - Header | Header cột Thao tác (Action) | 1. Quan sát tiêu đề cột thao tác | - | 1. Hiển thị cột thao tác (Chi tiết / Sửa), căn giữa | Low | Auto-UI |
| `[AF100-48]` | [8] Bảng dữ liệu - Sort | Sort theo cột Giá coin / Thứ tự / Ngày | 1. Click vào header cột có hỗ trợ sort lần 1 2. Click lần 2 | - | 1. Lần 1 sắp xếp tăng dần; Lần 2 đảo chiều giảm dần (theo CMR36) | Medium | Auto-UI |
| `[AF100-49]` | [8] Bảng dữ liệu - Data Cell | Data mapping cột ID & Tên quà | 1. Đối chiếu ID và Tên quà hiển thị trên bảng với DB (`gifts`) | Có dữ liệu quà | 1. Hiển thị chính xác ID và tên quà từ DB | High | Auto-UI |
| `[AF100-50]` | [8] Bảng dữ liệu - Data Cell | Data mapping Icon / Thumbnail quà | 1. Quan sát ảnh thumbnail ở cột Icon | - | 1. Ảnh hiển thị rõ nét, không bị vỡ/méo tỷ lệ; hiển thị placeholder nếu thiếu ảnh | Medium | Manual-Only (Visual) |
| `[AF100-51]` | [8] Bảng dữ liệu - Data Cell | Data mapping Giá coin & Thứ tự | 1. Quan sát số coin và thứ tự trên từng dòng | Có quà giá ≥ 1,000 | 1. Giá coin định dạng dấu phẩy phân cách hàng nghìn (VD: `1,000`), thứ tự hiển thị đúng số nguyên | High | Auto-UI |
| `[AF100-52]` | [8] Bảng dữ liệu - Data Cell | Data mapping Danh mục & Ngày tháng | 1. Quan sát tên danh mục và ngày tạo/sửa | - | 1. Tên danh mục khớp `gift_categories`; ngày hiển thị chuẩn `YYYY/MM/DD` (hoặc `YYYY/MM/DD HH:MM`), giá trị trống hiển thị `ー` | Medium | Auto-UI |
| `[AF100-53]` | [8] Bảng dữ liệu - Action | Click tên quà / nút Edit điều hướng AF300 | 1. Click vào tên quà hoặc icon Chi tiết/Sửa trên 1 dòng | - | 1. Điều hướng sang màn hình AF300 của đúng `gift_id` đó | High | Auto-UI |
| `[AF100-54]` | [9] Toggle Switch Trạng thái (ON/OFF) | Giao diện 2 trạng thái ON và OFF | 1. Quan sát Toggle Switch ở dòng quà ON và dòng quà OFF | Có quà ON và quà OFF | 1. OFF: nút tròn bên trái nền xám; ON: nút tròn bên phải nền xanh; khớp trạng thái DB | High | Manual-Only (Visual) |
| `[AF100-55]` | [9] Toggle Switch Trạng thái (ON/OFF) | Bật (OFF -> ON) & Sync App I600 | 1. Gạt Toggle của 1 quà từ OFF sang ON 2. Kiểm tra App Viewer màn I600 trong phòng Live | Có phòng Live đang chạy | 1. Toggle chuyển sang ON; DB cập nhật `status = active`; quà xuất hiện realtime trong danh sách quà tại App `I600` | High | Manual-Only (Complex DB) |
| `[AF100-56]` | [9] Toggle Switch Trạng thái (ON/OFF) | Tắt (ON -> OFF) & Sync App I600 | 1. Gạt Toggle của 1 quà từ ON sang OFF 2. Kiểm tra App Viewer màn I600 | Có phòng Live đang chạy | 1. Toggle chuyển sang OFF; DB cập nhật `status = inactive`; quà biến mất realtime khỏi danh sách tại App `I600` | High | Manual-Only (Complex DB) |
| `[AF100-57]` | [9] Toggle Switch Trạng thái (ON/OFF) | Lưu bền vững sau F5 Reload | 1. Gạt Toggle từ OFF -> ON 2. Nhấn F5 tải lại trang | - | 1. Sau khi tải lại trang, Toggle vẫn giữ nguyên trạng thái ON | High | Auto-UI |
| `[AF100-58]` | [9] Toggle Switch Trạng thái (ON/OFF) | Rollback khi API trả lỗi 500/403 | 1. Giả lập API `PATCH /gifts/:id/status` trả về lỗi 500 2. Click gạt Toggle | - | 1. Hiển thị thông báo lỗi và tự động gạt trả (Rollback) Toggle về trạng thái ban đầu | High | Auto-UI |
| `[AF100-59]` | [9] Toggle Switch Trạng thái (ON/OFF) | Spam / Rapid Clicks (5-10 lần liên tiếp) | 1. Click liên tục 5 lần thật nhanh vào Toggle Switch | - | 1. Hệ thống debounce/khóa tạm thời; trạng thái cuối cùng trên UI đồng bộ 100% với DB | Medium | Auto-UI |
| `[AF100-60]` | [9] Toggle Switch Trạng thái (ON/OFF) | Điều khiển bằng bàn phím (Accessibility) | 1. Nhấn `Tab` focus vào Toggle 2. Nhấn `Space` hoặc `Enter` | - | 1. Toggle đổi trạng thái bình thường, hỗ trợ keyboard navigation | Low | Auto-UI |
| `[AF100-61]` | [10] Pagination (Phân trang) | Viewpoint 1: UI Mặc định | 1. Mở AF100 khi có > 10 bản ghi 2. Quan sát thanh phân trang | Tổng > 10 bản ghi | 1. Hiển thị đầy đủ `<<前`, số trang, `次>>`; Trang 1 active; tổng trang = `ceil(Total/PageSize)` | High | Auto-UI |
| `[AF100-62]` | [10] Pagination (Phân trang) | Viewpoint 2: Page Size cố định | 1. Đếm số dòng hiển thị trên Trang 1 | Tổng >= 10 bản ghi | 1. Hiển thị tối đa đúng 10 dòng/trang theo CMR01 | High | Auto-UI |
| `[AF100-63]` | [10] Pagination (Phân trang) | Viewpoint 3: Chuyển trang trực tiếp theo số | 1. Click vào số trang `2` | Tổng > 10 bản ghi | 1. Tải đúng dữ liệu trang 2, không trùng lặp hoặc sót bản ghi | High | Auto-UI |
| `[AF100-64]` | [10] Pagination (Phân trang) | Viewpoint 3: Nút Next (`次>>`) và Prev (`<<前`) | 1. Tại Trang 1 click `次>>` 2. Tại Trang 2 click `<<前` | Tổng > 10 bản ghi | 1. Chuyển tới Trang 2 và quay lại Trang 1 chính xác | Medium | Auto-UI |
| `[AF100-65]` | [10] Pagination (Phân trang) | Viewpoint 4: Disabled tại Trang 1 | 1. Đứng tại Trang 1 2. Kiểm tra nút `<<前` và First (`<<`) | - | 1. Nút `<<前` và `<<` bị Disabled, không click được | Medium | Auto-UI |
| `[AF100-66]` | [10] Pagination (Phân trang) | Viewpoint 4: Disabled tại Trang cuối | 1. Chuyển đến trang cuối 2. Kiểm tra nút `次>>` và Last (`>>`) | - | 1. Nút `次>>` và `>>` bị Disabled, không click được | Medium | Auto-UI |
| `[AF100-67]` | [10] Pagination (Phân trang) | Viewpoint 5: Biên 0 bản ghi | 1. Tìm kiếm tên không tồn tại | - | 1. Thanh phân trang ẩn hoàn toàn; giữa bảng hiển thị CMMSG47: `一致する検索結果はありません。` | High | Auto-UI |
| `[AF100-68]` | [10] Pagination (Phân trang) | Viewpoint 6: Biên đúng 10 bản ghi | 1. Lọc điều kiện trả về đúng 10 bản ghi | Đúng 10 bản ghi khớp | 1. Hiển thị trọn vẹn 10 dòng trên 1 trang, thanh phân trang ẩn hoặc Prev/Next đều disabled | Medium | Auto-UI |
| `[AF100-69]` | [10] Pagination (Phân trang) | Viewpoint 7: Biên 11 bản ghi | 1. Lọc điều kiện trả về đúng 11 bản ghi | Đúng 11 bản ghi khớp | 1. Tự động chia 2 trang: Trang 1 có 10 dòng, Trang 2 có đúng 1 dòng cuối | High | Auto-UI |
| `[AF100-70]` | [10] Pagination (Phân trang) | Viewpoint 8: Reset về Trang 1 khi search mới | 1. Đang ở Trang 2 2. Thay đổi từ khóa lọc và click 検索 | - | 1. Hệ thống tự động Reset về Trang 1 (chống lỗi đứng trang rỗng) | High | Auto-UI |
| `[AF100-71]` | [10] Pagination (Phân trang) | Viewpoint 9: Rút gọn dấu `…` (CMR23) | 1. Xem danh sách khi tổng số trang > 7 | Có > 70 bản ghi | 1. Dãy số trang rút gọn bằng `…` (VD: `1 2 3 4 5 … 10`), click `…` cho nhập nhanh số trang | Medium | Auto-UI |
| `[AF100-72]` | [10] Pagination (Phân trang) | Viewpoint 10: URL Tampering | 1. Đổi URL thành `?page=-1`, `?page=99999`, `?page=abc` | - | 1. Hệ thống xử lý an toàn đưa về Trang 1 hoặc Trang cuối, không lỗi 500 hay crash | Medium | Auto-API |
| `[AF100-73]` | [11] Empty State & Error Handling | Empty State chuẩn CMMSG47 | 1. Tìm kiếm ra 0 bản ghi | - | 1. Bảng hiển thị thông báo căn giữa CMMSG47: `一致する検索結果はありません。` | High | Auto-UI |
| `[AF100-74]` | [11] Empty State & Error Handling | Mất kết nối mạng Internet | 1. Ngắt mạng 2. Click 検索 hoặc chuyển trang | - | 1. Hiển thị thông báo lỗi mạng chuẩn CMMSG8: `ネットワークエラー。接続を確認してください。` | Medium | Manual-Only (UX) |
| `[AF100-75]` | [11] Empty State & Error Handling | Lỗi server 500 | 1. Giả lập API trả về HTTP 500 | - | 1. Hiển thị CMMSG1: `予期しないサーバーエラーが発生しました。` kèm nút Thử lại | Medium | Auto-API |
| `[AF100-76]` | [11] Empty State & Error Handling | Hết phiên đăng nhập (Session Expired) | 1. Xóa/hết hạn token 2. Click 検索 | - | 1. Hiển thị CMMSG10 / CMMSG4 và redirect về màn Login | High | Auto-API |
| | **III. SUB-LAYOUTS / MODALS & VISUAL** | | | | | | |
| `[AF100-77]` | [12] Layout & Overflow | Responsive / Horizontal Scroll | 1. Thu nhỏ cửa sổ trình duyệt xuống độ phân giải thấp (1024px) | - | 1. Bảng có thanh cuộn ngang, không bị vỡ/chồng chéo cột | Low | Manual-Only (Visual) |
| `[AF100-78]` | [12] Layout & Overflow | Hover row highlight | 1. Di chuyển chuột qua các dòng trong bảng | - | 1. Dòng đang hover đổi màu nền nhẹ giúp dễ quan sát | Low | Manual-Only (Visual) |
| `[AF100-79]` | [12] Layout & Overflow | Text overflow (CMR48) trên Tên quà dài | 1. Xem quà có tên dài vượt độ rộng cột | Có quà tên dài > 50 ký tự | 1. Tên quà tự động cắt bằng dấu `…` theo CMR48; hover chuột hiển thị tooltip toàn bộ tên | Low | Manual-Only (Visual) |
| `[AF100-80]` | [12] RBAC trên nút thao tác | Role chỉ xem (Read-only) | 1. Đăng nhập tài khoản chỉ có quyền xem Gift | Tài khoản Monitor / Read-only | 1. Nút [新規登録] và Toggle ON/OFF bị ẩn hoặc disabled | Medium | Auto-UI |
| `[AF100-81]` | [12] Điều hướng chéo | Link sang Quản lý Danh mục (AF400) | 1. Click tab/nút chuyển sang AF400 (nếu có trên header/sidebar) | - | 1. Điều hướng sang màn AF400 thành công | Medium | Auto-UI |
| `[AF100-82]` | [12] Điều hướng chéo | Link sang Cấu hình Quà cao cấp (AF500) | 1. Click tab/nút chuyển sang AF500 (nếu có) | - | 1. Điều hướng sang màn AF500 thành công | Medium | Auto-UI |

---

## THỐNG KÊ AUTOMATION FEASIBILITY (AF100)

| Nhóm | Số lượng | Tỷ lệ |
|---| :---: | :---: |
| `Auto-UI` | 55 | 67.1% |
| `Auto-API` | 5 | 6.1% |
| `Auto-Data` | 4 | 4.9% |
| `Manual-Only` (Visual / Complex DB / UX) | 18 | 21.9% |
| **Tổng cộng** | **82** | **~78% Auto / ~22% Manual** ✅ |
