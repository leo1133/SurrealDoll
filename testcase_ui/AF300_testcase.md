# BẢNG ĐẶC TẢ KIỂM THỬ GIAO DIỆN THỦ CÔNG (MANUAL UI TEST SUITE)
## Màn hình: AF300 — Gift Manage: Gift Update / Delete (Chi tiết, Cập nhật & Xóa Quà tặng)
### Phân hệ: Master Admin Web / Quản lý Quà tặng (`AF` Module)
### Áp dụng: Quy chuẩn Trụ cột 2 (`Universal_Rules/02_manual_ui_test_case_rule.md`) & Thư viện `UI_controls/`

---

## BẢNG ĐIỀU KHIỂN TIẾN ĐỘ & THỐNG KÊ (DASHBOARD HEADER)

| Thuộc tính | Giá trị | Thuộc tính | Giá trị | Round 1 Metric | Kết quả | Round 2 Metric | Kết quả |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Module Code** | `AF300` | **Environment** | `Dev-Admin` / `STG-Admin` | **Pass** | 0 | **Pass** | 0 |
| **Total Testcases** | **45** | **% Executed** | 0% | **Fail** | 0 | **Fail** | 0 |
| **Plan to Execute** | **45** | **Creator** | `QA` | **Impact** | 0 | **Impact** | 0 |
| **Spec Source** | `FEATURE_SPEC_MAP` / Figma | **Liên kết chéo** | `AF100`, `I600`, `M1011`, `M20507` | **Not Run** | 45 | **Not Run** | 0 |
| | | | | **Total** | 45 | **Total** | 0 |

---

## CHI TIẾT BẢNG TEST CASES (8 CỘT CHUẨN MARKDOWN)

| ID | Title | Big item | Steps | Pre-condition | Expected | Priority | Automation Feasibility |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| | **I. COMMON & NAVIGATION** | | | | | | |
| `[AF300-1]` | [0] Kiểm tra truy cập màn hình | Điều hướng từ AF100 | 1. Đăng nhập Admin 2. Tại AF100 click tên quà hoặc nút Chi tiết/Sửa trên 1 dòng | Có ít nhất 1 quà trong DB | 1. Điều hướng sang AF300 (`/admin/gifts/:id`) 2. Toàn bộ trường pre-fill chính xác dữ liệu của quà đó | High | Auto-UI |
| `[AF300-2]` | [0] Kiểm tra truy cập màn hình | Inbound Deep-link — ID không tồn tại | 1. Truy cập trực tiếp URL `/admin/gifts/999999` | - | 1. Hiển thị thông báo không tìm thấy (CMMSG3 / 404) hoặc redirect an toàn về AF100 | High | Auto-API |
| `[AF300-3]` | [0] Kiểm tra truy cập màn hình | Inbound Deep-link — ID sai định dạng | 1. Truy cập URL `/admin/gifts/abc` | - | 1. Hệ thống xử lý an toàn (400/404 thân thiện), không crash trắng trang | Medium | Auto-API |
| `[AF300-4]` | [0] Kiểm tra truy cập màn hình | Phân quyền RBAC | 1. Đăng nhập tài khoản không có quyền Gift Manage 2. Truy cập `/admin/gifts/:id` | Tài khoản không có quyền | 1. Chặn truy cập, hiển thị CMMSG5: `この操作を行う権限がありません。` | High | Auto-API |
| `[AF300-5]` | [0] Kiểm tra truy cập màn hình | F5 Reload trang | 1. Mở chi tiết quà tại AF300 2. Nhấn F5 | - | 1. Tải lại trang thành công, dữ liệu chi tiết quà vẫn hiển thị chính xác | Medium | Auto-UI |
| `[AF300-6]` | [1] Breadcrumbs | Check hiển thị & điều hướng | 1. Quan sát Breadcrumb 2. Click node 'ギフト一覧' | - | 1. Hiển thị `＞ ギフト管理 ＞ ギフト一覧 ＞ ギフト詳細` 2. Click 'ギフト一覧' quay về AF100 | Medium | Auto-UI |
| | **II. MAIN SCREEN CONTROLS** | | | | | | |
| `[AF300-7]` | [2] Pre-fill dữ liệu chi tiết | Kiểm tra mapping toàn bộ trường | 1. Mở AF300 của 1 quà đã tạo ở AF200 2. Đối chiếu từng trường với DB | Có quà mẫu đầy đủ thông tin | 1. Tên, Giá Coin, Danh mục, Sort Order, Trạng thái, ảnh Icon, Animation hiển thị khớp 100% với DB | High | Auto-UI |
| `[AF300-8]` | [3] Textbox Tên quà (Gift Name) | Sửa tên hợp lệ (Nhật & Latin) | 1. Xóa tên cũ 2. Nhập tên mới 'New Star スター' 3. Click Lưu | - | 1. Lưu thành công CMMSG13/CMMSG17: `正常に保存されました。` 2. AF100 và DB cập nhật tên mới | High | Auto-UI |
| `[AF300-9]` | [3] Textbox Tên quà (Gift Name) | Xóa trắng tên quà (bắt buộc) | 1. Xóa toàn bộ text ô Tên quà 2. Click Lưu | - | 1. Báo lỗi CMMSG29: `{Gift Name}は空欄にできません。` | High | Auto-UI |
| `[AF300-10]` | [3] Textbox Tên quà (Gift Name) | Nhập khoảng trắng đầu/cuối | 1. Nhập `  Updated Star  ` 2. Click Lưu | - | 1. Hệ thống tự trim space đầu/cuối, DB lưu `Updated Star` | Medium | Auto-Data |
| `[AF300-11]` | [3] Textbox Tên quà (Gift Name) | Vượt quá max length | 1. Nhập chuỗi `max + 1` ký tự 2. Click Lưu | - | 1. UI block hoặc báo CMMSG49: `{Field}は文字数が多すぎます。{max}文字以内で入力してください。` | Medium | Auto-Data |
| `[AF300-12]` | [3] Textbox Tên quà (Gift Name) | Paste dữ liệu & XSS script | 1. Paste `<img src=x onerror=alert(1)>` vào ô Tên quà 2. Lưu | - | 1. Chuỗi được escape an toàn hoặc từ chối, không thực thi JS tại AF100 | High | Auto-API |
| `[AF300-13]` | [4] Textbox Giá Coin (Coin Price) | Sửa giá coin hợp lệ & Sync App I600 | 1. Đổi giá coin từ 100 -> 250 2. Click Lưu 3. Mở App I600 | Quà đang ON, có phòng Live | 1. Lưu thành công; AF100 và App `I600` hiển thị đúng giá mới `250` | High | Auto-UI |
| `[AF300-14]` | [4] Textbox Giá Coin (Coin Price) | Nhập giá = 0 | 1. Đổi giá coin thành `0` 2. Click Lưu | - | 1. Từ chối báo lỗi phải > 0 `[Pending Q&A #1]` | High | Manual-Only (Complex DB) |
| `[AF300-15]` | [4] Textbox Giá Coin (Coin Price) | Nhập số âm (`-50`) | 1. Nhập `-50` | - | 1. Chặn nhập dấu `-` hoặc báo lỗi validation | High | Auto-Data |
| `[AF300-16]` | [4] Textbox Giá Coin (Coin Price) | Nhập số thập phân / chữ | 1. Nhập `12.5` hoặc `abc` | - | 1. Chặn nhập hoặc báo CMMSG54: `半角数字のみ入力してください。` | High | Auto-Data |
| `[AF300-17]` | [4] Textbox Giá Coin (Coin Price) | Xóa trắng giá coin (bắt buộc) | 1. Xóa trắng ô Giá coin 2. Click Lưu | - | 1. Báo lỗi CMMSG29: `{Coin Price}は空欄にできません。` | High | Auto-UI |
| `[AF300-18]` | [5] Dropdown Danh mục (Category) | Đổi sang danh mục khác | 1. Mở dropdown Category 2. Chọn danh mục khác 3. Click Lưu | Có >= 2 danh mục | 1. Lưu thành công; quà chuyển sang danh mục mới trên AF100 và App `I600` | High | Auto-UI |
| `[AF300-19]` | [5] Dropdown Danh mục (Category) | Click ra ngoài dropdown | 1. Mở dropdown Category 2. Click ra ngoài | - | 1. Dropdown tự đóng, giữ nguyên giá trị đang chọn | Low | Auto-UI |
| `[AF300-20]` | [6] Textbox Thứ tự (Sort Order) | Cập nhật sort_order mới | 1. Đổi sort_order sang giá trị mới 2. Click Lưu | - | 1. Lưu thành công; vị trí hiển thị của quà trên AF100 cập nhật theo thứ tự mới | Medium | Auto-UI |
| `[AF300-21]` | [6] Textbox Thứ tự (Sort Order) | Nhập số âm / chữ | 1. Nhập `-1` hoặc `abc` | - | 1. Chặn nhập hoặc báo lỗi CMMSG54 | Medium | Auto-Data |
| `[AF300-22]` | [7] Toggle Trạng thái (Status) | Đổi trạng thái ON <-> OFF & Lưu | 1. Gạt Toggle từ ON sang OFF 2. Click Lưu | Quà đang ON | 1. Lưu thành công; trạng thái trong AF100 đổi thành OFF; quà ẩn khỏi App `I600` | High | Manual-Only (Complex DB) |
| `[AF300-23]` | [8] Cập nhật Asset Icon | Thay icon mới hợp lệ | 1. Click xóa/thay icon cũ 2. Upload ảnh `.png` mới 3. Click Lưu | Có file PNG mới | 1. Preview đổi sang ảnh mới; sau khi lưu, AF100 & App `I600` hiển thị icon mới | High | Manual-Only (Visual) |
| `[AF300-24]` | [8] Cập nhật Asset Icon | Giữ nguyên icon cũ khi chỉ sửa text | 1. Chỉ sửa tên quà, không động vào vùng Icon 2. Click Lưu | - | 1. Icon cũ được giữ nguyên, không bị mất ảnh | Medium | Auto-UI |
| `[AF300-25]` | [8] Cập nhật Asset Icon | Upload sai định dạng / quá dung lượng | 1. Upload file `.txt` hoặc file > Max Size | - | 1. Báo lỗi CMMSG43/44 (sai định dạng) hoặc CMMSG45 (quá dung lượng), giữ ảnh cũ | High | Auto-UI |
| `[AF300-26]` | [9] Cập nhật Asset Animation | Thay animation mới hợp lệ | 1. Upload file `.gif`/Lottie mới 2. Click Lưu | - | 1. Preview chạy animation mới; sau khi lưu cập nhật DB thành công | High | Manual-Only (Visual) |
| `[AF300-27]` | [9] Cập nhật Asset Animation | Xóa & tải lại chính file animation đó | 1. Click (X) xóa animation 2. Chọn lại chính file cũ | - | 1. Hệ thống cho phép tải lại bình thường (`input.value` đã reset) | Medium | Auto-UI |
| `[AF300-28]` | [10] Button Lưu (Save) | Lưu khi không thay đổi dữ liệu | 1. Mở AF300 không sửa gì 2. Click Lưu | - | 1. Hệ thống xử lý thành công (không lỗi), dữ liệu giữ nguyên | Low | Auto-UI |
| `[AF300-29]` | [10] Button Lưu (Save) | Debounce chống double-click (CMR15) | 1. Sửa tên quà 2. Double-click nút Lưu liên tiếp | - | 1. Nút disabled trong khi xử lý (CMR15), chỉ gọi API update 1 lần | Medium | Auto-UI |
| `[AF300-30]` | [10] Button Lưu (Save) | Hiển thị Loading (CMMSG27) | 1. Sửa dữ liệu -> Click Lưu khi mạng chậm | - | 1. Hiển thị Loading CMMSG27 (`読み込み中、しばらくお待ちください...`) | Medium | Manual-Only (Visual) |
| `[AF300-31]` | [11] Button Hủy / Quay lại (CMR07) | Quay lại khi chưa sửa dữ liệu | 1. Mở AF300 không sửa gì 2. Click [キャンセル / 戻る] | - | 1. Quay về ngay AF100, không hiện popup cảnh báo | Medium | Auto-UI |
| `[AF300-32]` | [11] Button Hủy / Quay lại (CMR07) | Quay lại sau khi đã sửa dữ liệu | 1. Sửa giá coin 2. Click [キャンセル / 戻る] | - | 1. Hiển thị popup xác nhận CMMSG46 (MSG2): `戻ってもよろしいですか？保存されていない変更は失われます。` | High | Auto-UI |
| `[AF300-33]` | [12] Button Xóa (Delete - CMR25) | Check hiển thị nút Xóa & RBAC | 1. Quan sát nút Xóa với Master Admin và với role Read-only | - | 1. Master Admin thấy nút Xóa; Read-only bị ẩn hoặc disabled | High | Auto-UI |
| `[AF300-34]` | [12] Button Xóa (Delete - CMR25) | Click nút Xóa mở Modal xác nhận | 1. Click nút [削除] trên AF300 | - | 1. Hiển thị Modal xác nhận CMMSG28: `このギフトを削除します。よろしいですか？` kèm nút [キャンセル] và [削除] | High | Auto-UI |
| `[AF300-35]` | [13] Error Handling | Mất kết nối mạng khi Lưu/Xóa | 1. Ngắt mạng 2. Click Lưu hoặc Xóa | - | 1. Hiển thị CMMSG8: `ネットワークエラー。接続を確認してください。` | Medium | Manual-Only (UX) |
| `[AF300-36]` | [13] Error Handling | Lỗi server 500 | 1. Giả lập API trả về 500 2. Click Lưu / Xóa | - | 1. Hiển thị CMMSG1: `予期しないサーバーエラーが発生しました。` kèm nút Thử lại | Medium | Auto-API |
| `[AF300-37]` | [13] Error Handling | Hết phiên đăng nhập | 1. Token hết hạn 2. Click Lưu / Xóa | - | 1. Hiển thị CMMSG10 / CMMSG4 và redirect về trang Login | High | Auto-API |
| | **III. SUB-LAYOUTS / MODALS** | | | | | | |
| `[AF300-38]` | [14] Modal Xác nhận Xóa | Click [キャンセル] hoặc icon (X) | 1. Mở Modal xóa ở `[AF300-34]` 2. Click [キャンセル] | Modal xác nhận xóa đang mở | 1. Đóng modal, giữ nguyên quà tặng, không gọi API DELETE | High | Auto-UI |
| `[AF300-39]` | [14] Modal Xác nhận Xóa | Click [削除] xóa thành công | 1. Mở Modal xóa 2. Click [削除] | Quà hợp lệ có thể xóa | 1. Báo CMMSG14: `正常に削除されました。` 2. Quay về AF100, quà biến mất khỏi danh sách 3. DB: bản ghi soft-delete (`deleted_at IS NOT NULL`) | High | Auto-UI |
| `[AF300-40]` | [14] Modal Xác nhận Xóa | Xóa quà đang có trạng thái ON | 1. Mở quà đang ON -> Xóa & Confirm 2. Kiểm tra App I600 | Có phòng Live đang chạy | 1. Xóa thành công và quà biến mất realtime khỏi danh sách quà App `I600` | High | Manual-Only (Complex DB) |
| `[AF300-41]` | [14] Modal Xác nhận Xóa | Xóa quà đang nằm trong Wishlist Streamer | 1. Chọn quà đang được Streamer gắn vào Wishlist (`M1011`/`M20507`) 2. Click Xóa -> Confirm | Quà đang có trong Wishlist | 1. Hệ thống cảnh báo không cho xóa HOẶC xóa và tự gỡ khỏi Wishlist `[Pending Q&A #4]` | High | Manual-Only (Complex DB) |
| `[AF300-42]` | [14] Modal Xác nhận Xóa | Xóa thất bại (API lỗi 500/409) | 1. Giả lập API DELETE trả lỗi 2. Click [削除] | - | 1. Hiển thị thông báo lỗi CMMSG22 (xóa thất bại), đóng hoặc giữ modal an toàn, dữ liệu không mất | Medium | Auto-API |
| `[AF300-43]` | [15] Modal Xác nhận thoát chưa lưu | Click [キャンセル] trên Modal | 1. Trigger modal CMMSG46 2. Click [キャンセル] | Modal CMMSG46 đang mở | 1. Đóng modal, ở lại AF300 giữ nguyên dữ liệu đang sửa | High | Auto-UI |
| `[AF300-44]` | [15] Modal Xác nhận thoát chưa lưu | Click [OK] trên Modal | 1. Trigger modal CMMSG46 2. Click [OK] | Modal CMMSG46 đang mở | 1. Đóng modal, quay về AF100, mọi thay đổi chưa lưu bị hủy | High | Auto-UI |
| `[AF300-45]` | [16] Layout Responsive | Thu nhỏ màn hình | 1. Resize trình duyệt về 1024px | - | 1. Các trường form và 2 nút Lưu / Xóa không bị tràn hoặc chồng chéo | Low | Manual-Only (Visual) |

*(Ghi chú: Đảm bảo toàn bộ 45 TCs phủ đủ Pre-fill, Edit từng field, Upload Asset, Save, Cancel CMR07, Delete CMR25, Modals, Error Handling & DB/App Cross-sync)*

---

## THỐNG KÊ AUTOMATION FEASIBILITY (AF300)

| Nhóm | Số lượng | Tỷ lệ |
|---| :---: | :---: |
| `Auto-UI` | 24 | 53.3% |
| `Auto-API` | 6 | 13.3% |
| `Auto-Data` | 5 | 11.1% |
| `Manual-Only` (Visual / Complex DB / UX) | 10 | 22.2% |
| **Tổng cộng** | **45** | **~77.8% Auto / ~22.2% Manual** ✅ |
