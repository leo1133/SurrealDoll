# BẢNG ĐẶC TẢ KIỂM THỬ GIAO DIỆN THỦ CÔNG (MANUAL UI TEST SUITE)
## Màn hình: AF400 — Gift Manage: Gift Category Manage (Quản lý Danh mục Quà tặng)
### Phân hệ: Master Admin Web / Quản lý Quà tặng (`AF` Module)
### Áp dụng: Quy chuẩn Trụ cột 2 (`Universal_Rules/02_manual_ui_test_case_rule.md`) & Thư viện `UI_controls/`

---

## BẢNG ĐIỀU KHIỂN TIẾN ĐỘ & THỐNG KÊ (DASHBOARD HEADER)

| Thuộc tính | Giá trị | Thuộc tính | Giá trị | Round 1 Metric | Kết quả | Round 2 Metric | Kết quả |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Module Code** | `AF400` | **Environment** | `Dev-Admin` / `STG-Admin` | **Pass** | 0 | **Pass** | 0 |
| **Total Testcases** | **36** | **% Executed** | 0% | **Fail** | 0 | **Fail** | 0 |
| **Plan to Execute** | **36** | **Creator** | `QA` | **Impact** | 0 | **Impact** | 0 |
| **Spec Source** | `FEATURE_SPEC_MAP` / Figma | **Liên kết chéo** | `AF100`, `AF200`, `AF300`, `I600` | **Not Run** | 36 | **Not Run** | 0 |
| | | | | **Total** | 36 | **Total** | 0 |

---

## CHI TIẾT BẢNG TEST CASES (8 CỘT CHUẨN MARKDOWN)

| ID | Title | Big item | Steps | Pre-condition | Expected | Priority | Automation Feasibility |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| | **I. COMMON & NAVIGATION** | | | | | | |
| `[AF400-1]` | [0] Kiểm tra truy cập màn hình | Điều hướng từ Sidebar | 1. Đăng nhập Admin 2. Click menu 'ギフト管理 > カテゴリ管理' (Gift Category) | User là Master Admin | 1. Điều hướng sang AF400, menu con active highlight | High | Auto-UI |
| `[AF400-2]` | [0] Kiểm tra truy cập màn hình | Inbound Deep-link URL | 1. Truy cập trực tiếp URL màn AF400 | User là Master Admin | 1. Màn hình AF400 tải danh sách danh mục thành công | High | Auto-UI |
| `[AF400-3]` | [0] Kiểm tra truy cập màn hình | Phân quyền RBAC | 1. Đăng nhập tài khoản không có quyền Gift Manage 2. Truy cập URL AF400 | Tài khoản không có quyền | 1. Chặn truy cập, hiển thị CMMSG5: `この操作を行う権限がありません。` | High | Auto-API |
| `[AF400-4]` | [0] Kiểm tra truy cập màn hình | F5 Reload trang | 1. Đang ở AF400 2. Nhấn F5 | - | 1. Tải lại danh sách danh mục chính xác, không lỗi | Medium | Auto-UI |
| `[AF400-5]` | [1] Breadcrumbs | Check hiển thị & điều hướng | 1. Quan sát Breadcrumb trên AF400 2. Click node cha 'ギフト管理' | - | 1. Hiển thị đúng chuỗi `＞ ギフト管理 ＞ カテゴリ管理` theo CMR35 | Low | Auto-UI |
| | **II. MAIN SCREEN CONTROLS** | | | | | | |
| `[AF400-6]` | [2] Bảng danh mục - Header | Header cột ID | 1. Quan sát tiêu đề cột ID | - | 1. Hiển thị 'ID', căn giữa | Low | Auto-UI |
| `[AF400-7]` | [2] Bảng danh mục - Header | Header cột Tên danh mục | 1. Quan sát tiêu đề cột Tên danh mục | - | 1. Hiển thị đúng tiêu đề, căn trái | Low | Auto-UI |
| `[AF400-8]` | [2] Bảng danh mục - Header | Header cột Số lượng quà | 1. Quan sát tiêu đề cột Số lượng quà | - | 1. Hiển thị đúng tiêu đề, căn phải | Low | Auto-UI |
| `[AF400-9]` | [2] Bảng danh mục - Header | Header cột Thứ tự (Sort Order) | 1. Quan sát tiêu đề cột Thứ tự | - | 1. Hiển thị đúng tiêu đề, căn phải | Low | Auto-UI |
| `[AF400-10]` | [2] Bảng danh mục - Header | Header cột Thao tác (Edit/Delete) | 1. Quan sát tiêu đề cột Thao tác | - | 1. Hiển thị cột Thao tác, căn giữa | Low | Auto-UI |
| `[AF400-11]` | [2] Bảng danh mục - Data Cell | Mapping dữ liệu & Thứ tự | 1. Đối chiếu tên, số lượng quà, thứ tự trên bảng với DB `gift_categories` | Có >= 1 danh mục | 1. Dữ liệu khớp DB 100%, sắp xếp theo `sort_order` tăng dần | High | Auto-UI |
| `[AF400-12]` | [2] Bảng danh mục - Empty State | Trạng thái 0 danh mục | 1. Khi không có danh mục nào trong hệ thống | 0 bản ghi | 1. Hiển thị thông báo căn giữa CMMSG47: `一致する検索結果はありません。` | Medium | Auto-UI |
| `[AF400-13]` | [3] Nút Tạo danh mục (新規登録) | Click mở Form / Modal tạo mới | 1. Click nút [+ Tạo danh mục / 新規登録] | - | 1. Mở Modal/Form tạo mới danh mục ở trạng thái rỗng | High | Auto-UI |
| `[AF400-14]` | [4] Error Handling | Mất mạng / Lỗi 500 / Session Expired | 1. Ngắt mạng hoặc giả lập 500 / hết hạn token 2. Thao tác tải/lưu | - | 1. Hiển thị CMMSG8 (Mạng), CMMSG1 (500), CMMSG10 (Session Expired) | Medium | Auto-API |
| | **III. SUB-LAYOUTS / MODALS (CREATE / EDIT / DELETE)** | | | | | | |
| `[AF400-15]` | [5] Modal Tạo danh mục | Nhập tên hợp lệ (Nhật & Latin) | 1. Nhập tên 'イベントギフト / Event' + sort_order = 1 2. Click Lưu | Modal Tạo đang mở | 1. Báo CMMSG12/CMMSG17: `正常に保存されました。` 2. Xuất hiện trên AF400, dropdown AF200 và App `I600` | High | Auto-UI |
| `[AF400-16]` | [5] Modal Tạo danh mục | Bỏ trống tên danh mục (bắt buộc) | 1. Để trống ô Tên danh mục 2. Click Lưu | - | 1. Báo lỗi CMMSG29: `{Category Name}は空欄にできません。` | High | Auto-UI |
| `[AF400-17]` | [5] Modal Tạo danh mục | Nhập khoảng trắng đầu/cuối & toàn space | 1. Nhập `  Event  ` rồi Lưu; thử nhập `   ` rồi Lưu | - | 1. `  Event  ` tự trim thành `Event`; toàn space bị từ chối báo CMMSG29 | Medium | Auto-Data |
| `[AF400-18]` | [5] Modal Tạo danh mục | Vượt quá max length | 1. Nhập chuỗi `max + 1` ký tự vào Tên danh mục | - | 1. UI block hoặc báo CMMSG49 | Medium | Auto-Data |
| `[AF400-19]` | [5] Modal Tạo danh mục | Nhập tên trùng danh mục đã có | 1. Nhập tên trùng với danh mục đang tồn tại 2. Click Lưu | Đã có danh mục "Normal" | 1. Báo lỗi CMMSG57 (đã tồn tại) hoặc cho phép `[Pending Q&A #5]` | Medium | Auto-API |
| `[AF400-20]` | [5] Modal Tạo danh mục | Nhập sort_order âm / chữ | 1. Nhập `-1` hoặc `abc` vào ô Sort Order | - | 1. UI block hoặc báo CMMSG54: `半角数字のみ入力してください。` | Medium | Auto-Data |
| `[AF400-21]` | [5] Modal Tạo danh mục | Debounce chống double-click (CMR15) | 1. Nhập tên hợp lệ 2. Double-click nút Lưu | - | 1. Chỉ gọi API 1 lần, chỉ tạo 1 danh mục trong DB | High | Auto-UI |
| `[AF400-22]` | [5] Modal Tạo danh mục | Hủy khi đã nhập dữ liệu (CMR07) | 1. Nhập tên 2. Click [キャンセル] hoặc icon (X) | - | 1. Đóng modal (hoặc hỏi CMMSG46), không tạo bản ghi mới | Medium | Auto-UI |
| `[AF400-23]` | [6] Modal Sửa danh mục | Pre-fill dữ liệu hiện tại | 1. Click nút Edit trên 1 danh mục | Có ít nhất 1 danh mục | 1. Modal mở lên với đúng Tên và Sort Order hiện tại | High | Auto-UI |
| `[AF400-24]` | [6] Modal Sửa danh mục | Cập nhật tên & đồng bộ AF100/AF200 | 1. Đổi tên danh mục -> Click Lưu | - | 1. Báo CMMSG13/CMMSG17; tên mới đồng bộ sang AF100, dropdown AF200 và tab App `I600` | High | Auto-UI |
| `[AF400-25]` | [6] Modal Sửa danh mục | Xóa trắng tên khi sửa | 1. Xóa trắng ô Tên 2. Click Lưu | - | 1. Báo lỗi CMMSG29 | High | Auto-UI |
| `[AF400-26]` | [6] Modal Sửa danh mục | Cập nhật Sort Order | 1. Đổi thứ tự danh mục -> Click Lưu | - | 1. Thứ tự danh mục trên AF400 và tab danh mục App `I600` thay đổi đúng | Medium | Auto-UI |
| `[AF400-27]` | [7] Modal Xác nhận Xóa | Click nút Xóa mở Modal xác nhận | 1. Click nút Delete trên 1 dòng danh mục | - | 1. Mở Modal xác nhận CMMSG28: `このカテゴリを削除します。よろしいですか？` | High | Auto-UI |
| `[AF400-28]` | [7] Modal Xác nhận Xóa | Click [キャンセル] hủy xóa | 1. Mở Modal xóa 2. Click [キャンセル] | - | 1. Đóng modal, danh mục giữ nguyên | High | Auto-UI |
| `[AF400-29]` | [7] Modal Xác nhận Xóa | Xóa danh mục rỗng (0 quà) | 1. Chọn danh mục không có quà nào 2. Click Xóa -> [削除] | Danh mục có 0 quà | 1. Báo CMMSG14: `正常に削除されました。`; danh mục biến mất; DB soft-delete | High | Auto-UI |
| `[AF400-30]` | [7] Modal Xác nhận Xóa | Xóa danh mục đang có quà (Ràng buộc) | 1. Chọn danh mục đang chứa >= 1 quà 2. Click Xóa -> Confirm | Danh mục có >= 1 quà | 1. Hệ thống chặn xóa và báo lỗi ràng buộc HOẶC hỏi xóa cascade `[Pending Q&A #6]` | High | Manual-Only (Complex DB) |
| `[AF400-31]` | [8] Layout & Visual | Text overflow (CMR48) tên danh mục dài | 1. Xem danh mục có tên dài tối đa | - | 1. Cắt gọn bằng `…`, hover hiện tooltip đầy đủ | Low | Manual-Only (Visual) |
| `[AF400-32]` | [8] Layout & Visual | Hover row & Responsive | 1. Hover dòng bảng & thu nhỏ màn hình 1024px | - | 1. Hover đổi màu nền nhẹ; bảng không vỡ giao diện | Low | Manual-Only (Visual) |
| `[AF400-33]` | [8] Pagination | Phân trang (nếu số danh mục > PageSize) | 1. Kiểm tra chuyển trang, disabled Prev/Next, Reset trang 1 | Có > 10 danh mục | 1. Thanh phân trang hoạt động đúng chuẩn CMR23 | Medium | Auto-UI |
| `[AF400-34]` | [8] RBAC | Role Read-only trên AF400 | 1. Đăng nhập role chỉ xem | Role Monitor | 1. Ẩn/khóa nút Tạo, Sửa, Xóa | Medium | Auto-UI |
| `[AF400-35]` | [8] Cross-sync | Danh mục mới/sửa hiển thị trên App I600 | 1. Tạo/sửa danh mục có quà active 2. Kiểm tra App I600 | Có phòng Live | 1. Tab danh mục trên App `I600` cập nhật đúng tên và thứ tự | High | Manual-Only (Complex DB) |
| `[AF400-36]` | [8] Security | XSS trong tên danh mục | 1. Nhập `<script>alert(1)</script>` vào tên danh mục | - | 1. Escape an toàn hoặc từ chối, không thực thi JS | High | Auto-API |

---

## THỐNG KÊ AUTOMATION FEASIBILITY (AF400)

| Nhóm | Số lượng | Tỷ lệ |
|---| :---: | :---: |
| `Auto-UI` | 22 | 61.1% |
| `Auto-API` | 4 | 11.1% |
| `Auto-Data` | 3 | 8.3% |
| `Manual-Only` (Visual / Complex DB) | 7 | 19.4% |
| **Tổng cộng** | **36** | **~80.6% Auto / ~19.4% Manual** ✅ |
