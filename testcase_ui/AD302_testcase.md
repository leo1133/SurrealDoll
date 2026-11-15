# BẢNG ĐẶC TẢ KIỂM THỬ GIAO DIỆN THỦ CÔNG (MANUAL UI TEST SUITE)
## Màn hình: AD302_Agency Streamer List (Danh Sách Liver Trực Thuộc Agency - 事務所詳細_ライバー一覧)
### Phân hệ: Master Admin Web (`AA000`) / Quản lý Agency (`AD` Module)
### Áp dụng: Quy chuẩn Trụ cột 2 (`Universal_Rules/02_manual_ui_test_case_rule.md`) & Thư viện `UI_controls/`

---

## BẢNG ĐIỀU KHIỂN TIẾN ĐỘ & THỐNG KÊ (DASHBOARD HEADER)

| Thuộc tính | Giá trị | Thuộc tính | Giá trị | Round 1 Metric | Kết quả | Round 2 Metric | Kết quả |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Module Code** | `AD302` | **Environment** | `Dev-Admin` / `STG-Admin` | **Pass** | 0 | **Pass** | 0 |
| **Total Testcases** | **86** | **% Executed** | 0% | **Fail** | 0 | **Fail** | 0 |
| **Plan to Execute** | **86** | **Creator** | `NgaDTP` | **Impact** | 0 | **Impact** | 0 |
| **Spec Source** | `Surreal SPEC` | **Google Sheet Tab** | `AD302` (gid=1019623612) | **Not Run** | 86 | **Not Run** | 0 |
| | | | | **Total** | 86 | **Total** | 0 |

---

## CHI TIẾT BẢNG TEST CASES (7 CỘT CHUẨN MARKDOWN)

| ID | Title | Big item | Steps | Pre-condition | Expected | Priority |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| | **I. COMMON & NAVIGATION** | | | | | |
| `[AD302-1]` | [0] Kiểm tra truy cập màn hình | Check điều hướng từ AD100 qua cột [10] | 1. Tại AD100, click vào số lượng Liver tại cột [10] ライバー数 của Agency ID=5 | User là Master Admin đăng nhập thành công | 1. Điều hướng sang màn hình AD302 của đúng Agency ID=5, URL hiển thị `/admin/agencies/5/livers` | **High** |
| `[AD302-2]` | [0] Kiểm tra truy cập màn hình | Check điều hướng chuyển Tab từ AD301/AD303 | 1. Đang ở màn hình AD301 hoặc AD303 2. Click vào Tab [ライバー一覧] | - | 1. Chuyển sang Tab AD302, hiển thị danh sách Liver trực thuộc Agency hiện tại | **High** |
| `[AD302-3]` | [0] Kiểm tra truy cập màn hình | Check Inbound với agency_id hợp lệ | 1. Mở trực tiếp URL `/admin/agencies/5/livers` trên trình duyệt | Agency ID=5 tồn tại | 1. Tải thành công toàn bộ danh sách streamer của Agency 5 theo đúng Prototype | **High** |
| `[AD302-4]` | [0] Kiểm tra truy cập màn hình | Check Inbound với agency_id không tồn tại | 1. Mở URL `/admin/agencies/999999/livers` | - | 1. Hệ thống báo lỗi CMMSG3 (Resource not found) hoặc chuyển hướng về trang AD100 | **Medium** |
| `[AD302-5]` | [0] Kiểm tra truy cập màn hình | Check Screen Lifecycle F5 Reload | 1. Đang xem danh sách Liver với bộ lọc đã chọn 2. Nhấn phím F5 Reload | - | 1. Trang web reload thành công, bảo lưu nguyên vẹn tab ライバー一覧 và các tham số lọc | **Medium** |
| `[AD302-6]` | [0] Kiểm tra truy cập màn hình | Check phân quyền RBAC | 1. Đăng nhập tài khoản Agency Admin 2. Cố tình mở URL danh sách liver của Agency khác | - | 1. Hệ thống chặn truy cập với lỗi CMMSG5: この操作を行う権限がありません。 | **High** |
| `[AD302-7]` | [0] Breadcrumbs | Check hiển thị breadcrumb | 1. Quan sát thanh Breadcrumbs ở đầu màn hình AD302 | - | 1. Hiển thị text: '＞ 事務所一覧 ＞ 事務所詳細' | **Low** |
| `[AD302-8]` | [0] Breadcrumbs | Click '事務所一覧' trên breadcrumb | 1. Click link '事務所一覧' trên breadcrumb | - | 1. Điều hướng quay về danh sách Agency AD100 và bảo lưu bộ lọc trước đó | **Medium** |
| `[AD302-9]` | [0] Tabs Navigation | Check hiển thị và active Tab 'ライバー一覧' | 1. Quan sát thanh tab chuyển đổi phân hệ | - | 1. Tab 'ライバー一覧' được highlight active nổi bật, 2 tab '詳細' và '売上' ở trạng thái bình thường | **Medium** |
| | **II. MAIN SCREEN CONTROLS** | | | | | |
| `[AD302-10]` | [1] Ô tìm kiếm | Check hiển thị và placeholder | 1. Quan sát ô tìm kiếm từ khóa | - | 1. Hiển thị ô search box, placeholder: 'ライバー名・ID' | **Low** |
| `[AD302-11]` | [1] Ô tìm kiếm | Tìm kiếm một phần username (CMR02) | 1. Nhập một phần tên streamer (VD: 'Sakura') 2. Click 検索 | - | 1. Bảng dữ liệu lọc ra toàn bộ Liver có username chứa từ khóa 'Sakura' | **High** |
| `[AD302-12]` | [1] Ô tìm kiếm | Tìm kiếm chính xác User System ID | 1. Nhập chính xác User System ID (VD: '485') 2. Click 検索 | - | 1. Bảng dữ liệu lọc ra đúng duy nhất Liver có ID là 485 | **High** |
| `[AD302-13]` | [1] Ô tìm kiếm | Tìm kiếm bằng phím Enter | 1. Nhập từ khóa vào ô tìm kiếm 2. Nhấn phím Enter trên bàn phím | - | 1. Tự động kích hoạt tìm kiếm tương tự click nút 検索 | **Medium** |
| `[AD302-14]` | [1] Ô tìm kiếm | Click icon (X) xóa nhanh từ khóa | 1. Nhập từ khóa vào ô tìm kiếm 2. Click icon (X) | - | 1. Xóa toàn bộ từ khóa trong ô ngay lập tức | **Low** |
| `[AD302-15]` | [2] Pulldown 全ステータス | Check hiển thị và giá trị mặc định | 1. Quan sát pulldown lọc trạng thái tài khoản User | - | 1. Hiển thị giá trị mặc định là '全ステータス' | **Medium** |
| `[AD302-16]` | [2] Pulldown 全ステータス | Check danh sách options | 1. Click mở pulldown 全ステータス | - | 1. Danh sách hiển thị đủ 4 options: '全ステータス', '利用中', '停止中', '退会済み' | **Medium** |
| `[AD302-17]` | [2] Pulldown 全ステータス | Chọn option '利用中' | 1. Mở pulldown -> Chọn '利用中' (value=1) 2. Click 検索 | - | 1. Bảng chỉ hiển thị các Liver có tài khoản đang hoạt động (利用中) | **High** |
| `[AD302-18]` | [2] Pulldown 全ステータス | Chọn option '停止中' | 1. Mở pulldown -> Chọn '停止中' (value=2) 2. Click 検索 | - | 1. Bảng chỉ hiển thị các Liver đang bị tạm dừng tài khoản (停止中) | **High** |
| `[AD302-19]` | [2] Pulldown 全ステータス | Chọn option '退会済み' | 1. Mở pulldown -> Chọn '退会済み' (value=3) 2. Click 検索 | - | 1. Bảng chỉ hiển thị các Liver đã rời khỏi hệ thống (退会済み) | **Medium** |
| `[AD302-20]` | [3] Pulldown 全ての所属状態 | Check hiển thị và giá trị mặc định | 1. Quan sát pulldown lọc trạng thái trực thuộc Agency | - | 1. Hiển thị giá trị mặc định là '全ての所属状態' | **Medium** |
| `[AD302-21]` | [3] Pulldown 全ての所属状態 | Check danh sách options | 1. Click mở pulldown 全ての所属状態 | - | 1. Danh sách hiển thị đủ 5 options: '全ての所属状態', '申請中', '所属済み', '退所申請中', '退所済み' | **Medium** |
| `[AD302-22]` | [3] Pulldown 全ての所属状態 | Chọn option '申請中' | 1. Mở pulldown -> Chọn '申請中' (value=3) 2. Click 検索 | - | 1. Bảng chỉ hiển thị các Liver đang nộp đơn xin gia nhập Agency | **High** |
| `[AD302-23]` | [3] Pulldown 全ての所属状態 | Chọn option '所属済み' | 1. Mở pulldown -> Chọn '所属済み' (value=1) 2. Click 検索 | - | 1. Bảng chỉ hiển thị các Liver đã là thành viên chính thức của Agency | **High** |
| `[AD302-24]` | [3] Pulldown 全ての所属状態 | Chọn option '退所申請中' | 1. Mở pulldown -> Chọn '退所申請中' (value=5) 2. Click 検索 | - | 1. Bảng chỉ hiển thị các Liver đang nộp đơn xin rời Agency | **High** |
| `[AD302-25]` | [3] Pulldown 全ての所属状態 | Chọn option '退所済み' | 1. Mở pulldown -> Chọn '退所済み' (value=6) 2. Click 検索 | - | 1. Bảng chỉ hiển thị các Liver đã rời khỏi Agency trong quá khứ | **High** |
| `[AD302-26]` | [3] Pulldown 全ての所属状態 | Xác nhận KHÔNG hiển thị trạng thái 却下 | 1. Kiểm tra Liver bị từ chối đơn gia nhập (却下) | - | 1. Bảng AD302 không hiển thị Liver có trạng thái 却下 theo đúng quy định Spec | **High** |
| `[AD302-27]` | [4] Pulldown Streamer Type | Check hiển thị và giá trị mặc định | 1. Quan sát pulldown lọc loại Liver | - | 1. Hiển thị giá trị mặc định là '全て' | **Low** |
| `[AD302-28]` | [4] Pulldown Streamer Type | Check danh sách options | 1. Click mở pulldown loại Liver | - | 1. Danh sách hiển thị đủ 3 options: '全て', 'Vライバー', '2.5次元V' | **Medium** |
| `[AD302-29]` | [4] Pulldown Streamer Type | Chọn option 'Vライバー' | 1. Mở pulldown -> Chọn 'Vライバー' (value=1) 2. Click 検索 | - | 1. Bảng chỉ hiển thị các streamer loại Vライバー | **Medium** |
| `[AD302-30]` | [4] Pulldown Streamer Type | Chọn option '2.5次元V' | 1. Mở pulldown -> Chọn '2.5次元V' (value=2) 2. Click 検索 | - | 1. Bảng chỉ hiển thị các streamer loại 2.5次元V | **Medium** |
| `[AD302-31]` | [5] Button クリア | Reset toàn bộ bộ lọc | 1. Nhập từ khóa, đổi cả 3 dropdown 2. Click nút クリア | - | 1. Xóa trắng ô tìm kiếm, đưa cả 3 dropdown về giá trị mặc định, tự động kích hoạt tìm kiếm tải lại danh sách | **High** |
| `[AD302-32]` | [6] Button 検索 | Tìm kiếm kết hợp đa tiêu chí | 1. Thiết lập từ khóa + Status User + Status Agency + Streamer Type 2. Click 検索 | - | 1. Gọi API tải danh sách thỏa mãn đồng thời tất cả các tiêu chí (AND logic) | **High** |
| `[AD302-33]` | [6] Button 検索 | Debounce chống spam request | 1. Nhấp đúp liên tục vào nút 検索 | - | 1. Nút 検索 bị disable tạm thời (CMR15), chỉ gửi duy nhất 1 request | **Medium** |
| `[AD302-34]` | [7] Button Toggle » / « | Check trạng thái mặc định (Ẩn 2 nhóm cột) | 1. Mở màn hình AD302 lần đầu | - | 1. Nút hiển thị icon `»`; 2 nhóm cột chi tiết (cột 16-19 và 23-28) ở trạng thái ẩn thu gọn | **High** |
| `[AD302-35]` | [7] Button Toggle » / « | Click nút `»` để mở rộng cột | 1. Click nút toggle `»` | - | 1. Nút chuyển thành `«`; bảng dữ liệu mở rộng hiển thị đầy đủ Nhóm 1 (2ショット, ギフト, ウィスパー, エール) và Nhóm 2 (通常配信時間, 2ショット時間, ファミ限時間, カラオケ時間, BC時間, OBS時間) | **High** |
| `[AD302-36]` | [7] Button Toggle » / « | Click nút `«` để thu gọn cột | 1. Đang ở trạng thái mở rộng, click nút `«` | - | 1. Nút chuyển lại thành `»`; 2 nhóm cột chi tiết tự động ẩn đi, bảng thu gọn lại | **High** |
| `[AD302-37]` | Bảng dữ liệu - Header | Header cột [8] ID | 1. Quan sát tiêu đề cột ID kèm icon sort | - | 1. Hiển thị text 'ID', căn giữa, có icon sắp xếp tăng/giảm | **Low** |
| `[AD302-38]` | Bảng dữ liệu - Header | Header cột [9] ライバー名 | 1. Quan sát tiêu đề cột ライバー名 | - | 1. Hiển thị text 'ライバー名', căn trái | **Low** |
| `[AD302-39]` | Bảng dữ liệu - Header | Header cột [10] ライバー種類 | 1. Quan sát tiêu đề cột ライバー種類 | - | 1. Hiển thị text 'ライバー種類', căn giữa | **Low** |
| `[AD302-40]` | Bảng dữ liệu - Header | Header cột [11] フォロー | 1. Quan sát tiêu đề cột フォロー kèm icon sort | - | 1. Hiển thị text 'フォロー', căn phải, có icon sort | **Low** |
| `[AD302-41]` | Bảng dữ liệu - Header | Header cột [12] フォロワー | 1. Quan sát tiêu đề cột フォロワー kèm icon sort | - | 1. Hiển thị text 'フォロワー', căn phải, có icon sort | **Low** |
| `[AD302-42]` | Bảng dữ liệu - Header | Header cột [13] ファミリアメンバー | 1. Quan sát tiêu đề cột ファミリアメンバー kèm icon sort | - | 1. Hiển thị text 'ファミリアメンバー', căn phải, có icon sort | **Low** |
| `[AD302-43]` | Bảng dữ liệu - Header | Header cột [14] いいね数 | 1. Quan sát tiêu đề cột いいね数 kèm icon sort | - | 1. Hiển thị text 'いいね数', căn phải, có icon sort | **Low** |
| `[AD302-44]` | Bảng dữ liệu - Header | Header cột [15] ポイント売上 | 1. Quan sát tiêu đề cột ポイント売上 kèm icon sort | - | 1. Hiển thị text 'ポイント売上', căn phải, có icon sort | **Low** |
| `[AD302-45]` | Bảng dữ liệu - Header | Header cột [16] 2ショット (Nhóm 1) | 1. Mở rộng cột, quan sát header cột 2ショット | - | 1. Hiển thị text '2ショット', căn phải, có icon sort | **Low** |
| `[AD302-46]` | Bảng dữ liệu - Header | Header cột [17] ギフト (Nhóm 1) | 1. Mở rộng cột, quan sát header cột ギフト | - | 1. Hiển thị text 'ギフト', căn phải, có icon sort | **Low** |
| `[AD302-47]` | Bảng dữ liệu - Header | Header cột [18] ウィスパー (Nhóm 1) | 1. Mở rộng cột, quan sát header cột ウィスパー | - | 1. Hiển thị text 'ウィスパー', căn phải, có icon sort | **Low** |
| `[AD302-48]` | Bảng dữ liệu - Header | Header cột [19] エール (Nhóm 1) | 1. Mở rộng cột, quan sát header cột エール | - | 1. Hiển thị text 'エール', căn phải, có icon sort | **Low** |
| `[AD302-49]` | Bảng dữ liệu - Header | Header cột [20] ファミリア売上 | 1. Quan sát tiêu đề cột ファミリア売上 kèm icon sort | - | 1. Hiển thị text 'ファミリア売上', căn phải, có icon sort | **Low** |
| `[AD302-50]` | Bảng dữ liệu - Header | Header cột [21] 合計売上 | 1. Quan sát tiêu đề cột 合計売上 kèm icon sort | - | 1. Hiển thị text '合計売上', căn phải, có icon sort | **Low** |
| `[AD302-51]` | Bảng dữ liệu - Header | Header cột [22] 合計配信時間 | 1. Quan sát tiêu đề cột 合計配信時間 kèm icon sort | - | 1. Hiển thị text '合計配信時間', căn giữa, có icon sort | **Low** |
| `[AD302-52]` | Bảng dữ liệu - Header | Header cột [23] 通常配信時間 (Nhóm 2) | 1. Mở rộng cột, quan sát header cột 通常配信時間 | - | 1. Hiển thị text '通常配信時間', căn giữa, có icon sort | **Low** |
| `[AD302-53]` | Bảng dữ liệu - Header | Header cột [24] 2ショット時間 (Nhóm 2) | 1. Mở rộng cột, quan sát header cột 2ショット時間 | - | 1. Hiển thị text '2ショット時間', căn giữa, có icon sort | **Low** |
| `[AD302-54]` | Bảng dữ liệu - Header | Header cột [25] ファミ限時間 (Nhóm 2) | 1. Mở rộng cột, quan sát header cột ファミ限時間 | - | 1. Hiển thị text 'ファミ限時間', căn giữa, có icon sort | **Low** |
| `[AD302-55]` | Bảng dữ liệu - Header | Header cột [26] カラオケ時間 (Nhóm 2) | 1. Mở rộng cột, quan sát header cột カラオケ時間 | - | 1. Hiển thị text 'カラオケ時間', căn giữa, có icon sort | **Low** |
| `[AD302-56]` | Bảng dữ liệu - Header | Header cột [27] BC時間 (Nhóm 2) | 1. Mở rộng cột, quan sát header cột BC時間 | - | 1. Hiển thị text 'BC時間', căn giữa, có icon sort | **Low** |
| `[AD302-57]` | Bảng dữ liệu - Header | Header cột [28] OBS時間 (Nhóm 2) | 1. Mở rộng cột, quan sát header cột OBS時間 | - | 1. Hiển thị text 'OBS時間', căn giữa, có icon sort | **Low** |
| `[AD302-58]` | Bảng dữ liệu - Header | Header cột [29] ステータス | 1. Quan sát tiêu đề cột ステータス | - | 1. Hiển thị text 'ステータス', căn giữa | **Low** |
| `[AD302-59]` | Bảng dữ liệu - Header | Header cột [30] 事務所ステータス | 1. Quan sát tiêu đề cột 事務所ステータス | - | 1. Hiển thị text '事務所ステータス', căn giữa | **Low** |
| `[AD302-60]` | Bảng dữ liệu - Header | Header cột [31] 配信権限 | 1. Quan sát tiêu đề cột 配信権限 | - | 1. Hiển thị text '配信権限', căn giữa | **Low** |
| `[AD302-61]` | Bảng dữ liệu - Header | Header cột [32] 加入日時 | 1. Quan sát tiêu đề cột 加入日時 kèm icon sort | - | 1. Hiển thị text '加入日時', căn giữa, có icon sort | **Low** |
| `[AD302-62]` | Bảng dữ liệu - Header | Header cột [33] 詳細 | 1. Quan sát tiêu đề cột 詳細 | - | 1. Cột thao tác hiển thị text '詳細' hoặc icon link | **Low** |
| `[AD302-63]` | Bảng dữ liệu - Sort | Sort cột ID | 1. Click header ID lần 1 2. Click lần 2 | - | 1. Mặc định sort ID mới -> cũ; click đảo chiều sắp xếp cũ -> mới | **Medium** |
| `[AD302-64]` | Bảng dữ liệu - Sort | Sort các cột doanh thu [15, 20, 21] | 1. Click header cột 合計売上 | - | 1. Danh sách sắp xếp theo tổng doanh thu tăng dần/giảm dần | **Medium** |
| `[AD302-65]` | Bảng dữ liệu - Sort | Sort cột thời lượng live [22] | 1. Click header cột 合計配信時間 | - | 1. Danh sách sắp xếp theo tổng thời lượng livestream tăng dần/giảm dần | **Medium** |
| `[AD302-66]` | Bảng dữ liệu - Sort | Sort cột ngày gia nhập [32] | 1. Click header cột 加入日時 | - | 1. Sắp xếp danh sách theo thời điểm Liver gia nhập Agency (mới -> cũ, cũ -> mới) | **Medium** |
| `[AD302-67]` | Bảng dữ liệu - Data Cell | Công thức doanh thu Point (CR 13/10/2026) | 1. Đối chiếu cột ポイント売上 với các cột [16, 17, 18, 19] | - | 1. ポイント売上 = 2ショット + ギフト + ウィスパー + エール. Tuyệt đối KHÔNG cộng doanh thu từ Gift Gacha | **High** |
| `[AD302-68]` | Bảng dữ liệu - Data Cell | Công thức doanh thu Tổng 合計売上 | 1. Đối chiếu cột 合計売上 với cột [15] và [20] | - | 1. 合計売上 = ポイント売上 + ファミリア売上; định dạng số có dấu phẩy phân cách hàng nghìn | **High** |
| `[AD302-69]` | Bảng dữ liệu - Data Cell | Format thời lượng livestream [22-28] | 1. Quan sát giá trị thời lượng livestream | - | 1. Định dạng chuẩn `hh:mm:ss` (VD: `12:30:45`); nếu chưa từng live hiển thị `00:00:00` | **Medium** |
| `[AD302-70]` | Bảng dữ liệu - Data Cell | Check hiển thị trạng thái 事務所ステータス | 1. Quan sát badge trạng thái Agency trên từng dòng | - | 1. Hiển thị đúng 1 trong 4 trạng thái: 申請中, 所属済み, 退所申請中, 退所済み | **High** |
| `[AD302-71]` | Bảng dữ liệu - Data Cell | Cưỡng chế rời Agency do không live 1 tuần (CR 11/11/2026) | 1. Liver không live suốt 1 tuần (一週間未配信) nộp đơn sang Agency khác và được duyệt 2. Mở kiểm tra AD302 của Agency hiện tại | - | 1. Liver tự động bị cưỡng chế rời (強制退所) và trạng thái trên bảng AD302 chuyển thành 退所済み | **High** |
| `[AD302-72]` | Bảng dữ liệu - Data Cell | Check cột 配信権限 (Quyền livestream) | 1. Quan sát badge cột 配信権限 | - | 1. Hiển thị nhãn 'あり' (Có) hoặc 'なし' (Không); mặc định tài khoản mới tạo là 'あり' | **Medium** |
| `[AD302-73]` | Bảng dữ liệu - Data Cell | Format thời gian 加入日時 | 1. Quan sát cột 加入日時 | - | 1. Định dạng chuẩn `YYYY/MM/DD HH:mm` | **Low** |
| `[AD302-74]` | Bảng dữ liệu - Action | Click nút 詳細 điều hướng sang AE200 | 1. Click nút [詳細] tại dòng của một Liver | - | 1. Hệ thống điều hướng mở màn hình quản lý chi tiết User AE200 của streamer đó | **High** |
| `[AD302-75]` | Bảng dữ liệu - Action | Xác nhận KHÔNG CÓ chức năng Xóa user | 1. Quan sát toàn bộ các hành động trên bảng AD302 | - | 1. Không có nút xóa user trên bảng AD302 theo đúng ghi chú Spec ("Không có chức năng xoá ở đây") | **High** |
| `[AD302-76]` | [Pagination] Phân trang | Viewpoint 1: Hiển thị thanh phân trang mặc định | 1. Mở màn hình AD302 khi có > 10 streamer | - | 1. Hiển thị thanh phân trang chuẩn CMR23; Trang 1 được highlight active | **High** |
| `[AD302-77]` | [Pagination] Phân trang | Viewpoint 2: Page Size cố định 10 dòng | 1. Đếm số dòng Liver hiển thị trên Trang 1 | - | 1. Hiển thị tối đa đúng 10 dòng/trang theo CMR01 | **Medium** |
| `[AD302-78]` | [Pagination] Phân trang | Viewpoint 3: Chuyển trang trực tiếp | 1. Click vào số trang '2' | - | 1. Chuyển sang Trang 2 tải các streamer từ 11 đến 20 không bị trùng lặp | **High** |
| `[AD302-79]` | [Pagination] Phân trang | Viewpoint 4: Disabled tại Trang 1 & Trang cuối | 1. Kiểm tra nút '<<前' tại Trang 1 2. Kiểm tra nút '次>>' tại Trang cuối | - | 1. Nút điều hướng bị disabled tương ứng | **Medium** |
| `[AD302-80]` | [Pagination] Phân trang | Viewpoint 5: Biên 0 bản ghi | 1. Tìm kiếm streamer không tồn tại | - | 1. Phân trang ẩn hoàn toàn; hiển thị CMMSG47: 一致する検索結果はありません。 | **High** |
| `[AD302-81]` | [Pagination] Phân trang | Viewpoint 8: Reset về Trang 1 khi search | 1. Đang ở Trang 2, thay đổi pulldown hoặc từ khóa và bấm 検索 | - | 1. Tự động reset về Trang 1 để hiển thị kết quả tìm kiếm mới | **High** |
| `[AD302-82]` | [Pagination] Phân trang | Viewpoint 10: Xử lý an toàn URL tampering | 1. Sửa URL thành `?page=-1` hoặc `?page=99999` | - | 1. Hệ thống xử lý an toàn đưa về Trang 1 hoặc Trang cuối, không bị lỗi 500 | **Medium** |
| `[AD302-83]` | Empty State | Check hiển thị khi Agency chưa có Liver | 1. Mở AD302 của một Agency mới tạo chưa có Liver nào | - | 1. Bảng dữ liệu hiển thị thông báo căn giữa CMMSG47: 一致する検索結果はありません。 | **High** |
| `[AD302-84]` | Error Handling | Xử lý khi mất mạng | 1. Ngắt kết nối Internet 2. Click nút 検索 hoặc chuyển trang | - | 1. Hiển thị thông báo CMMSG8: ネットワークエラー。接続を確認してください。 | **Medium** |
| `[AD302-85]` | Error Handling | Xử lý khi API lỗi 500 | 1. Giả lập API `/agency/list/{agency_id}` trả về HTTP 500 | - | 1. Hiển thị thông báo CMMSG1: 予期しないサーバーエラーが発生しました。 | **Medium** |
| | **III. SUB-LAYOUTS / MODALS** | | | | | |
| `[AD302-86]` | Sub-layout | Thanh cuộn ngang khi mở rộng 2 nhóm cột | 1. Click nút toggle `»` để mở rộng bảng | - | 1. Xuất hiện thanh cuộn ngang (horizontal scrollbar), layout bảng hiển thị mượt mà không bị vỡ giao diện | **Low** |
