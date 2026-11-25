# BẢNG ĐẶC TẢ KIỂM THỬ GIAO DIỆN THỦ CÔNG (MANUAL UI TEST SUITE)
## Màn hình: AF100 — Gift Manage: Gift List (ギフト一覧)
### Phân hệ: Master Admin Web / 商品管理 (`AF` Module)
### Nguồn Spec: Google Sheet `AF100` (gid=`217442794`) + `AF500` (gid=`1458098150`)
### Áp dụng: `Universal_Rules/02_manual_ui_test_case_rule.md` & `UI_controls/`

---

## BẢNG ĐIỀU KHIỂN TIẾN ĐỘ & THỐNG KÊ (DASHBOARD HEADER)

| Thuộc tính | Giá trị | Thuộc tính | Giá trị | Round 1 Metric | Kết quả | Round 2 Metric | Kết quả |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Module Code** | `AF100` | **Environment** | `Dev-Admin` / `STG-Admin` | **Pass** | 0 | **Pass** | 0 |
| **Total Testcases** | **88** | **% Executed** | 0% | **Fail** | 0 | **Fail** | 0 |
| **Plan to Execute** | **88** | **Creator** | `QA` | **Impact** | 0 | **Impact** | 0 |
| **Spec Source** | Google Sheet `AF100` + `AF500` | **Liên kết chéo** | `AF200`, `AF300`, `I600`, `I601` | **Not Run** | 88 | **Not Run** | 0 |
| | | | | **Total** | 88 | **Total** | 0 |

---

## CHI TIẾT BẢNG TEST CASES (8 CỘT CHUẨN MARKDOWN)

| ID | Title | Big item | Steps | Pre-condition | Expected | Priority | Automation Feasibility |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| | **I. COMMON & NAVIGATION** | | | | | | |
| `[AF100-1]` | [0] Kiểm tra truy cập màn hình | Check hiển thị Sidebar UI | 1. Đăng nhập Master Admin 2. Quan sát Sidebar menu | Đã đăng nhập Admin | 1. Menu `商品管理 > ギフト管理` mở rộng; mục con `ギフト一覧` highlight active, hiển thị mục `ギフト登録` | High | Auto-UI |
| `[AF100-2]` | [0] Kiểm tra truy cập màn hình | Điều hướng từ Sidebar `ギフト一覧` | 1. Click `ギフト一覧` trên Sidebar | Đang ở màn khác | 1. Điều hướng sang đúng URL màn hình `AF100` | High | Auto-UI |
| `[AF100-3]` | [0] Kiểm tra truy cập màn hình | Kiểm tra Tab title trình duyệt | 1. Mở màn hình AF100 2. Quan sát tiêu đề tab trình duyệt | - | 1. Tab title hiển thị chính xác `商品管理｜ギフト管理` | Medium | Auto-UI |
| `[AF100-4]` | [0] Kiểm tra truy cập màn hình | Inbound Deep-link mặc định | 1. Truy cập trực tiếp URL màn AF100 | - | 1. Gọi `GET /gift/` & `GET /gift/category/`; sort mặc định theo `id`, hiển thị 10 bản ghi/trang | High | Auto-UI |
| `[AF100-5]` | [0] Kiểm tra truy cập màn hình | Inbound Deep-link với query params | 1. Truy cập URL kèm `?keyword=Heart&status=public` | Có quà "Heart" | 1. Ô tìm kiếm điền `Heart`, dropdown Status chọn `公開`, tự động lọc danh sách | High | Auto-UI |
| `[AF100-6]` | [0] Kiểm tra truy cập màn hình | Inbound Deep-link không có data | 1. Truy cập URL kèm `?keyword=NoGift999` | - | 1. Hiển thị Empty State: `一致する結果はありません` (CMMSG47), ẩn phân trang | Medium | Auto-UI |
| `[AF100-7]` | [0] Kiểm tra truy cập màn hình | F5 Reload trang | 1. Nhập điều kiện lọc 2. Nhấn F5 | - | 1. Tải lại trang thành công, không lỗi 500 hay trắng trang | Medium | Auto-UI |
| `[AF100-8]` | [0] Kiểm tra truy cập màn hình | Phân quyền RBAC | 1. Đăng nhập tài khoản không có quyền Gift Manage 2. Truy cập URL AF100 | Role không có quyền | 1. Chặn truy cập, báo lỗi CMMSG5: `この操作を行う権限がありません。` | High | Auto-API |
| `[AF100-9]` | [0] Breadcrumbs | Hiển thị Breadcrumb | 1. Quan sát Breadcrumb phía trên bảng | - | 1. Hiển thị `ホーム＞ギフト管理` | Low | Manual-Only (Visual) |
| `[AF100-10]` | [0] Breadcrumbs | Click node Breadcrumb | 1. Click `ホーム` trên Breadcrumb | - | 1. Điều hướng về trang chủ Admin | Low | Auto-UI |
| | **II. MAIN SCREEN CONTROLS** | | | | | | |
| `[AF100-11]` | [1] Search box (`ギフト名・ギフトID・ギフト値段`) | Hiển thị ô tìm kiếm | 1. Quan sát ô tìm kiếm `[1]` | - | 1. Hiển thị ô nhập text, cho phép focus với con trỏ I-beam | Low | Auto-UI |
| `[AF100-12]` | [1] Search box (`ギフト名・ギフトID・ギフト値段`) | Hiển thị Placeholder | 1. Quan sát placeholder khi ô tìm kiếm trống | - | 1. Hiển thị placeholder đúng `ギフト名・ギフトID・ギフト値段` | Medium | Manual-Only (Visual) |
| `[AF100-13]` | [1] Search box (`ギフト名・ギフトID・ギフト値段`) | Nhập chữ Nhật | 1. Nhập `ハート` vào ô tìm kiếm | - | 1. Cho phép nhập đầy đủ ký tự tiếng Nhật (Hiragana/Katakana/Kanji) | Medium | Auto-Data |
| `[AF100-14]` | [1] Search box (`ギフト名・ギフトID・ギフト値段`) | Nhập chữ Latin | 1. Nhập `Heart` vào ô tìm kiếm | - | 1. Cho phép nhập đầy đủ ký tự Latin hoa/thường | Medium | Auto-Data |
| `[AF100-15]` | [1] Search box (`ギフト名・ギフトID・ギフト値段`) | Nhập số | 1. Nhập `1000` vào ô tìm kiếm | - | 1. Cho phép nhập số bình thường | Low | Auto-Data |
| `[AF100-16]` | [1] Search box (`ギフト名・ギフトID・ギフト値段`) | Nhập ký tự đặc biệt | 1. Nhập `!@#$%` vào ô tìm kiếm | - | 1. Cho phép nhập bình thường, không lỗi giao diện | Low | Auto-Data |
| `[AF100-17]` | [1] Search box (`ギフト名・ギフトID・ギフト値段`) | Nhập khoảng trắng đầu/cuối | 1. Nhập `  Star  ` 2. Click `検索` | Có quà "Star" | 1. Tự động trim space đầu/cuối, trả về đúng quà "Star" | Medium | Auto-Data |
| `[AF100-18]` | [1] Search box (`ギフト名・ギフトID・ギフト値段`) | Paste dữ liệu vào ô tìm kiếm | 1. Copy và Paste chuỗi `"Star"` vào ô tìm kiếm | - | 1. Tiếp nhận đầy đủ chuỗi paste | Low | Auto-UI |
| `[AF100-19]` | [1] Search box (`ギフト名・ギフトID・ギフト値段`) | Click nút xóa nhanh (X) | 1. Nhập chuỗi `"Star"` 2. Click icon `(X)` | Ô tìm kiếm có text | 1. Xóa trắng nội dung ô tìm kiếm ngay lập tức | Low | Auto-UI |
| `[AF100-20]` | [1] Search box (`ギフト名・ギフトID・ギフト値段`) | Tìm kiếm 1 phần tên (Partial match) | 1. Nhập `Ear` 2. Click `検索` | Có quà "Heart" | 1. Trả về các quà có `name` chứa `Ear` (CMR02) | High | Auto-UI |
| `[AF100-21]` | [1] Search box (`ギフト名・ギフトID・ギフト値段`) | Tìm kiếm chính xác Gift ID | 1. Nhập chính xác Gift ID (VD: `15`) 2. Click `検索` | Có quà ID=15 | 1. Trả về đúng quà có ID=15 (Exact match) | High | Auto-UI |
| `[AF100-22]` | [1] Search box (`ギフト名・ギフトID・ギフト値段`) | Tìm kiếm chính xác Gift Price | 1. Nhập chính xác giá (VD: `5000`) 2. Click `検索` | Có quà giá 5,000 | 1. Trả về đúng các quà có giá = `5,000` (Exact match) | High | Auto-UI |
| `[AF100-23]` | [1] Search box (`ギフト名・ギフトID・ギフト値段`) | Nhấn Enter khi có từ khóa | 1. Nhập `Heart` -> nhấn phím Enter | - | 1. Tự động kích hoạt tìm kiếm tương tự click `検索` | High | Auto-UI |
| `[AF100-24]` | [1] Search box (`ギフト名・ギフトID・ギフト値段`) | Nhấn Enter khi ô rỗng | 1. Để trống ô tìm kiếm -> nhấn Enter | - | 1. Chặn request thừa hoặc tải danh sách mặc định | Low | Auto-UI |
| `[AF100-25]` | [2] Pulldown Category | Giá trị mặc định `全てカテゴリー` | 1. Mở màn hình AF100 2. Quan sát pulldown Category | - | 1. Mặc định hiển thị `全てカテゴリー` | Medium | Auto-UI |
| `[AF100-26]` | [2] Pulldown Category | Danh sách options khớp API | 1. Click mở pulldown Category | Có category từ AF400 | 1. Liệt kê đủ các category từ `GET /gift/category/` đúng thứ tự `sort_order` | High | Auto-UI |
| `[AF100-27]` | [2] Pulldown Category | Chọn 1 category và lọc | 1. Chọn 1 category -> bấm `検索` | Có quà thuộc category | 1. Chỉ hiển thị các quà thuộc category đã chọn | High | Auto-UI |
| `[AF100-28]` | [2] Pulldown Category | Click ngoài đóng pulldown | 1. Click mở pulldown Category 2. Click ra vùng trống bên ngoài | - | 1. Pulldown tự đóng lại, giữ nguyên giá trị đang chọn | Low | Auto-UI |
| `[AF100-29]` | [-] Pulldown Status | Giá trị mặc định `全てステータス` | 1. Mở màn hình AF100 2. Quan sát pulldown Status | - | 1. Mặc định hiển thị `全てステータス` | Medium | Auto-UI |
| `[AF100-30]` | [-] Pulldown Status | Chọn `公開` để lọc | 1. Mở pulldown Status -> chọn `公開` -> bấm `検索` | Có quà `公開` | 1. Chỉ hiển thị các gift trạng thái `公開` | High | Auto-UI |
| `[AF100-31]` | [-] Pulldown Status | Chọn `非公開` để lọc | 1. Chọn `非公開` -> bấm `検索` | Có quà `非公開` | 1. Chỉ hiển thị các gift trạng thái `非公開` | High | Auto-UI |
| `[AF100-32]` | [-] Pulldown Status | Chọn lại `全てステータス` | 1. Đang lọc `非公開` -> chọn lại `全てステータス` -> bấm `検索` | Có cả `公開` và `非公開` | 1. Hiển thị lại tất cả các gift thuộc mọi trạng thái | Medium | Auto-UI |
| `[AF100-33]` | [4-AF500] Pulldown Animation Type (`演出種類`) | Giá trị mặc định `全て演出種類` | 1. Mở AF100 2. Quan sát pulldown `演出種類` | - | 1. Mặc định hiển thị `全て演出種類` | Medium | Auto-UI |
| `[AF100-34]` | [4-AF500] Pulldown Animation Type (`演出種類`) | Chọn `通常演出` để lọc | 1. Chọn `通常演出` -> bấm `検索` | Có gift `通常演出` | 1. Chỉ hiển thị các gift loại `通常演出` | High | Auto-UI |
| `[AF100-35]` | [4-AF500] Pulldown Animation Type (`演出種類`) | Chọn `シャッター演出` | 1. Chọn `シャッター演出` -> bấm `検索` | Có gift Shutter | 1. Chỉ hiển thị các gift `シャッター演出` | High | Auto-UI |
| `[AF100-36]` | [4-AF500] Pulldown Animation Type (`演出種類`) | Chọn `継続演出` | 1. Chọn `継続演出` -> bấm `検索` | Có gift Continuous | 1. Chỉ hiển thị các gift `継続演出` | High | Auto-UI |
| `[AF100-37]` | [-] Button `検索` | Tìm kiếm kết hợp (AND) 4 điều kiện | 1. Nhập keyword + chọn Category + Status + Animation Type -> bấm `検索` | - | 1. Lọc AND chính xác đồng thời cả 4 điều kiện | High | Auto-UI |
| `[AF100-38]` | [-] Button `検索` | Debounce chống double-click (`CMR15`) | 1. Double-click liên tục vào nút `検索` | - | 1. Nút tạm disabled (CMR15), chỉ gọi 1 request API | Medium | Auto-UI |
| `[AF100-39]` | [-] Button `検索` | Hiển thị Loading (`CMMSG27`) | 1. Click `検索` khi mạng chậm | - | 1. Hiển thị Loading `CMMSG27`, không vỡ layout | Medium | Manual-Only (Visual) |
| `[AF100-40]` | [-] Button `クリア` | Reset toàn bộ bộ lọc | 1. Chọn các bộ lọc 2. Click `クリア` | - | 1. Reset toàn bộ về mặc định (`""`, `全てカテゴリー`, `全てステータス`, `全て演出種類`) và tự reload danh sách | High | Auto-UI |
| `[AF100-41]` | [3] Button `新規登録` | Click điều hướng sang AF200 | 1. Click nút `新規登録` | - | 1. Điều hướng sang màn hình tạo mới gift `AF200` | High | Auto-UI |
| `[AF100-42]` | [4] Bảng dữ liệu - Header | Cột `ID` | 1. Quan sát header cột ID | - | 1. Hiển thị text `ID`, căn giữa | Low | Auto-UI |
| `[AF100-43]` | [5] Bảng dữ liệu - Header | Cột `ギフト名` | 1. Quan sát header cột Gift Name | - | 1. Hiển thị text `ギフト名`, căn trái | Low | Auto-UI |
| `[AF100-44]` | [8] Bảng dữ liệu - Header | Cột `ステータス` | 1. Quan sát header cột Status | - | 1. Hiển thị text `ステータス`, căn giữa | Low | Auto-UI |
| `[AF100-45]` | [10] Bảng dữ liệu - Header | Cột `カテゴリ` | 1. Quan sát header cột Category | - | 1. Hiển thị text `カテゴリ`, căn trái | Low | Auto-UI |
| `[AF100-46]` | [11] Bảng dữ liệu - Header | Cột `値段` (có icon Sort) | 1. Quan sát header cột Price | - | 1. Hiển thị text `値段`, căn phải, có icon sort asc/desc | Low | Auto-UI |
| `[AF100-47]` | [5-AF500] Bảng dữ liệu - Header | Cột `演出種類` | 1. Quan sát header cột Animation Type | - | 1. Hiển thị tiêu đề cột `演出種類`, căn giữa | Low | Auto-UI |
| `[AF100-48]` | [16] Bảng dữ liệu - Header | Cột `作成者` | 1. Quan sát header cột Creator | - | 1. Hiển thị text `作成者`, căn trái | Low | Auto-UI |
| `[AF100-49]` | [18] Bảng dữ liệu - Header | Cột `作成日` | 1. Quan sát header cột Created Date | - | 1. Hiển thị text `作成日`, căn giữa | Low | Auto-UI |
| `[AF100-50]` | [20] Bảng dữ liệu - Header | Cột `変更日` | 1. Quan sát header cột Updated Date | - | 1. Hiển thị text `変更日`, căn giữa | Low | Auto-UI |
| `[AF100-51]` | [13] Bảng dữ liệu - Header | Cột Hành động — nút Edit `[13]` | 1. Quan sát cột nút Edit trên bảng | - | 1. Hiển thị nút Edit đúng vị trí trên mỗi dòng | Low | Auto-UI |
| `[AF100-52]` | [14] Bảng dữ liệu - Header | Cột Hành động — nút Delete `[14]` | 1. Quan sát cột nút Delete trên bảng | - | 1. Hiển thị nút Delete đúng vị trí trên mỗi dòng | Low | Auto-UI |
| `[AF100-53]` | [11] Bảng dữ liệu - Sort | Sort cột `値段` tăng dần | 1. Click header `値段` lần 1 | Có >= 2 quà khác giá | 1. Sắp xếp danh sách theo giá tăng dần (asc) | High | Auto-UI |
| `[AF100-54]` | [11] Bảng dữ liệu - Sort | Sort cột `値段` giảm dần | 1. Click header `値段` lần 2 | Đang sort tăng dần | 1. Sắp xếp danh sách theo giá giảm dần (desc) | High | Auto-UI |
| `[AF100-55]` | [4],[7] Bảng dữ liệu - Data Cell | Mapping `ID` và `ギフト名` `[7]` | 1. Đối chiếu ID và tên gift trên dòng đầu tiên với DB | Có quà trong DB | 1. Giá trị `ID` và `ギフト名` khớp 100% với DB | High | Auto-UI |
| `[AF100-56]` | [6] Bảng dữ liệu - Data Cell | Hiển thị ảnh thumbnail `icon` `[6]` | 1. Quan sát ảnh thumbnail `icon` trên bảng | Có quà trong DB | 1. Ảnh `icon` hiển thị rõ nét, đúng tỷ lệ, không bị vỡ/méo | Medium | Manual-Only (Visual) |
| `[AF100-57]` | [8] Bảng dữ liệu - Data Cell | Mapping cột `ステータス` | 1. Kiểm tra cột `ステータス` với quà công khai và ẩn | Có quà `公開` và `非公開` | 1. Hiển thị đúng nhãn `公開` hoặc `非公開` khớp DB | High | Auto-UI |
| `[AF100-58]` | [10] Bảng dữ liệu - Data Cell | Mapping cột `カテゴリ` (`未設定`) | 1. Kiểm tra gift có category và gift không có category | Có gift `category_id = null` | 1. Hiển thị tên category tương ứng hoặc `未設定` khi không có category | High | Auto-UI |
| `[AF100-59]` | [5-AF500] Bảng dữ liệu - Data Cell | Mapping cột `演出種類` | 1. Kiểm tra gift thuộc 3 loại `演出種類` | Có đủ 3 loại gift | 1. Hiển thị chính xác nhãn `通常演出`, `シャッター演出`, `継続演出` | High | Auto-UI |
| `[AF100-60]` | [11] Bảng dữ liệu - Data Cell | Format cột `値段` | 1. Kiểm tra quà có giá >= 1,000 trên bảng | Có quà giá >= 1,000 | 1. Giá hiển thị đúng format dấu phẩy phân cách hàng nghìn (VD: `10,000`) | Medium | Auto-UI |
| `[AF100-61]` | [16]-[21] Bảng dữ liệu - Data Cell | Mapping `作成者` và format `作成日`, `変更日` | 1. Kiểm tra cột người tạo và ngày tạo/sửa | Có quà trong DB | 1. `作成者` đúng tên Admin; `作成日`, `変更日` hiển thị format `yyyy/mm/dd hh:mm` | Medium | Auto-UI |
| `[AF100-62]` | [13] Bảng dữ liệu - Action | Click nút Edit `[13]` sang AF300 | 1. Click nút Edit trên 1 dòng | - | 1. Điều hướng sang màn `AF300` của đúng `gift_id` đó | High | Auto-UI |
| `[AF100-63]` | [14] Bảng dữ liệu - Action | Click nút Delete `[14]` mở Modal `CMMSG28` | 1. Click nút Delete trên 1 dòng | - | 1. Mở popup xác nhận xóa `CMMSG28` | High | Auto-UI |
| `[AF100-64]` | [15] Pagination (`CMR01`) | UI Mặc định thanh phân trang | 1. Mở AF100 khi tổng > 10 bản ghi | Tổng > 10 bản ghi | 1. Hiển thị đầy đủ `<<前`, số trang, `次>>`, Trang 1 active | High | Auto-UI |
| `[AF100-65]` | [15] Pagination (`CMR01`) | Page Size cố định 10 bản ghi/trang | 1. Đếm số dòng trên Trang 1 | Tổng >= 10 bản ghi | 1. Hiển thị đúng 10 dòng/trang (`items_per_page: 10`) | High | Auto-UI |
| `[AF100-66]` | [15] Pagination (`CMR01`) | Chuyển trang trực tiếp theo số trang | 1. Click số trang `2` | Tổng > 10 bản ghi | 1. Tải đúng các bản ghi từ 11–20, không trùng/sót | High | Auto-UI |
| `[AF100-67]` | [15] Pagination (`CMR01`) | Nút Next (`次>>`) | 1. Tại Trang 1 click nút `次>>` | Tổng > 10 bản ghi | 1. Chuyển sang Trang 2 chính xác | Medium | Auto-UI |
| `[AF100-68]` | [15] Pagination (`CMR01`) | Nút Prev (`<<前`) | 1. Tại Trang 2 click nút `<<前` | Đang ở Trang 2 | 1. Quay lại Trang 1 chính xác | Medium | Auto-UI |
| `[AF100-69]` | [15] Pagination (`CMR01`) | Disabled nút `<<` / `<<前` tại Trang 1 | 1. Đứng tại Trang 1 quan sát nút lùi | - | 1. Nút `<<` và `<<前` bị Disabled | Medium | Auto-UI |
| `[AF100-70]` | [15] Pagination (`CMR01`) | Disabled nút `>>` / `次>>` tại Trang cuối | 1. Chuyển đến trang cuối cùng | - | 1. Nút `>>` và `次>>` bị Disabled | Medium | Auto-UI |
| `[AF100-71]` | [15] Pagination (`CMR01`) | Biên 0 bản ghi | 1. Tìm kiếm tên không tồn tại | - | 1. Thanh phân trang ẩn hoàn toàn; bảng hiện `一致する結果はありません` | High | Auto-UI |
| `[AF100-72]` | [15] Pagination (`CMR01`) | Biên đúng 10 bản ghi | 1. Lọc kết quả có đúng 10 bản ghi | Đúng 10 bản ghi | 1. Hiển thị trọn vẹn 10 dòng trên 1 trang, nút Next/Prev disabled hoặc ẩn | Medium | Auto-UI |
| `[AF100-73]` | [15] Pagination (`CMR01`) | Biên 11 bản ghi | 1. Lọc kết quả có đúng 11 bản ghi | Đúng 11 bản ghi | 1. Tự tách 2 trang: Trang 1 có 10 dòng, Trang 2 có 1 dòng | High | Auto-UI |
| `[AF100-74]` | [15] Pagination (`CMR01`) | Reset về Trang 1 khi search mới | 1. Đứng ở Trang 2 -> đổi filter -> bấm `検索` | - | 1. Tự động reset về Trang 1 | High | Auto-UI |
| `[AF100-75]` | [15] Pagination (`CMR01`) | Rút gọn `…` (`CMR23`) khi > 7 trang | 1. Xem danh sách có > 70 bản ghi | > 70 bản ghi | 1. Dãy số trang rút gọn bằng `…`, click `…` mở ô nhập nhanh | Medium | Auto-UI |
| `[AF100-76]` | [15] Pagination (`CMR01`) | URL Tampering (`?page=-1`) | 1. Sửa URL `?page=-1` | - | 1. Đưa về Trang 1 an toàn, không lỗi 500 | Medium | Auto-API |
| `[AF100-77]` | [15] Pagination (`CMR01`) | URL Tampering (`?page=99999`) | 1. Sửa URL `?page=99999` | - | 1. Xử lý an toàn (trang rỗng hoặc trang cuối), không lỗi 500 hay trắng trang | Medium | Auto-API |
| `[AF100-78]` | [15] Pagination (`CMR01`) | URL Tampering (`?page=abc`) | 1. Sửa URL `?page=abc` | - | 1. Đưa về Trang 1 an toàn, không lỗi 500 hay trắng trang | Medium | Auto-API |
| `[AF100-79]` | [-] Error Handling | Mất mạng (`CMMSG8`) | 1. Ngắt mạng -> bấm `検索` | - | 1. Hiển thị `CMMSG8: ネットワークエラー。接続を確認してください。` | Medium | Manual-Only (UX) |
| `[AF100-80]` | [-] Error Handling | Lỗi server 500 (`CMMSG1`) | 1. Giả lập `GET /gift/` trả 500 | - | 1. Hiển thị `CMMSG1: 予期しないサーバーエラーが発生しました。` | Medium | Auto-API |
| `[AF100-81]` | [-] Error Handling | Hết phiên đăng nhập (`CMMSG10`) | 1. Xóa/hết hạn token -> bấm `検索` | - | 1. Hiển thị `CMMSG10` và redirect về trang Login | High | Auto-API |
| | **III. SUB-LAYOUTS / MODALS & VISUAL** | | | | | | |
| `[AF100-82]` | [14-Modal] Modal Xác nhận Xóa | Click Hủy (`キャンセル`) trên popup `CMMSG28` | 1. Mở popup xóa ở `[AF100-63]` 2. Click `キャンセル` | Popup đang mở | 1. Đóng popup, dữ liệu giữ nguyên | High | Auto-UI |
| `[AF100-83]` | [14-Modal] Modal Xác nhận Xóa | Đồng ý xóa -> Ẩn gift trên App `I600` | 1. Click đồng ý xóa trên popup 2. Kiểm tra App Livestream (`I600`) | Gift đang tồn tại | 1. Báo `CMMSG14`, xóa khỏi list AF100; màn Livestream `I600` KHÔNG hiện gift đã xóa | High | Manual-Only (Complex DB) |
| `[AF100-84]` | [14-Modal] Modal Xác nhận Xóa | Gift đã xóa vẫn giữ tại Lịch sử mua | 1. Xóa gift từng có user mua 2. Kiểm tra màn Lịch sử mua gift (`AE400`/`K9091A`) | Gift từng có user mua | 1. Màn hình Lịch sử mua gift VẪN hiển thị đầy đủ gift đã xóa | High | Manual-Only (Complex DB) |
| `[AF100-85]` | [-] Visual & Layout | Text overflow (`CMR48`) trên tên gift dài | 1. Quan sát gift có tên dài vượt độ rộng cột | - | 1. Cắt bằng `…`, hover hiện tooltip toàn bộ tên | Low | Manual-Only (Visual) |
| `[AF100-86]` | [-] Visual & Layout | Hover row highlight trên bảng | 1. Di chuột qua các dòng dữ liệu trên bảng | - | 1. Dòng được hover đổi màu nền nhẹ rõ ràng | Low | Manual-Only (Visual) |
| `[AF100-87]` | [-] Visual & Layout | Responsive màn hình 1024px | 1. Thu nhỏ trình duyệt về độ rộng 1024px | - | 1. Bảng cuộn ngang mượt mà, không vỡ layout hay che khuất nút | Low | Manual-Only (Visual) |
| `[AF100-88]` | [-] RBAC | Role chỉ xem (Read-only / Monitor) | 1. Đăng nhập role chỉ xem -> mở AF100 | Role Monitor | 1. Nút `新規登録` và nút Xóa bị ẩn hoặc disabled | Medium | Manual-Only (Visual) |

---

## THỐNG KÊ AUTOMATION FEASIBILITY (AF100)

| Nhóm | Số lượng | Tỷ lệ |
|---| :---: | :---: |
| `Auto-UI` | 66 | 75.0% |
| `Auto-Data` | 5 | 5.7% |
| `Auto-API` | 6 | 6.8% |
| `Manual-Only` (Visual / Complex DB / UX) | 11 | 12.5% |
| **Tổng cộng** | **88** | **87.5% Auto / 12.5% Manual** ✅ |
