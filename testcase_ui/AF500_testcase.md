# BẢNG ĐẶC TẢ KIỂM THỬ GIAO DIỆN THỦ CÔNG (MANUAL UI TEST SUITE)
## Màn hình: AF500 — Quà cao cấp (High-Value Gift Configuration)
### Phân hệ: Master Admin Web / Quản lý Quà tặng (`AF` Module)
### Áp dụng: Quy chuẩn Trụ cột 2 (`Universal_Rules/02_manual_ui_test_case_rule.md`) & Thư viện `UI_controls/`

> [!NOTE]
> `AF500` chưa có link Figma trong `FEATURE_SPEC_MAP.md`. Bộ testcase dưới đây áp dụng cấu trúc chuẩn Admin CMS + liên kết chéo `I601` (High-Value Gift Animation Mode) và gắn cờ `[Pending Q&A #7]` cho các điểm cần đối chiếu lại với Spec/Figma chi tiết khi có.

---

## BẢNG ĐIỀU KHIỂN TIẾN ĐỘ & THỐNG KÊ (DASHBOARD HEADER)

| Thuộc tính | Giá trị | Thuộc tính | Giá trị | Round 1 Metric | Kết quả | Round 2 Metric | Kết quả |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Module Code** | `AF500` | **Environment** | `Dev-Admin` / `STG-Admin` | **Pass** | 0 | **Pass** | 0 |
| **Total Testcases** | **23** | **% Executed** | 0% | **Fail** | 0 | **Fail** | 0 |
| **Plan to Execute** | **23** | **Creator** | `QA` | **Impact** | 0 | **Impact** | 0 |
| **Spec Source** | `FEATURE_SPEC_MAP` | **Liên kết chéo** | `I601` (App Animation), `AF100` | **Not Run** | 23 | **Not Run** | 0 |
| | | | | **Total** | 23 | **Total** | 0 |

---

## CHI TIẾT BẢNG TEST CASES (8 CỘT CHUẨN MARKDOWN)

| ID | Title | Big item | Steps | Pre-condition | Expected | Priority | Automation Feasibility |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| | **I. COMMON & NAVIGATION** | | | | | | |
| `[AF500-1]` | [0] Kiểm tra truy cập màn hình | Điều hướng từ Sidebar | 1. Đăng nhập Admin 2. Click menu 'ギフト管理 > 高額ギフト設定' (Quà cao cấp) | User là Master Admin | 1. Điều hướng sang AF500, menu con active highlight | High | Auto-UI |
| `[AF500-2]` | [0] Kiểm tra truy cập màn hình | Inbound Deep-link URL | 1. Truy cập trực tiếp URL màn AF500 | User là Master Admin | 1. Màn hình AF500 tải thành công cấu hình hiện tại từ DB | High | Auto-UI |
| `[AF500-3]` | [0] Kiểm tra truy cập màn hình | Phân quyền RBAC | 1. Đăng nhập tài khoản không có quyền Gift Manage 2. Truy cập URL AF500 | Tài khoản không có quyền | 1. Chặn truy cập, hiển thị CMMSG5: `この操作を行う権限がありません。` | High | Auto-API |
| `[AF500-4]` | [0] Kiểm tra truy cập màn hình | F5 Reload trang | 1. Đang ở AF500 2. Nhấn F5 | - | 1. Trang tải lại đúng dữ liệu cấu hình đã lưu | Medium | Auto-UI |
| `[AF500-5]` | [1] Breadcrumbs | Check hiển thị & điều hướng | 1. Quan sát Breadcrumb trên AF500 | - | 1. Hiển thị đúng chuỗi Breadcrumb theo CMR35 | Low | Auto-UI |
| | **II. MAIN SCREEN CONTROLS** | | | | | | |
| `[AF500-6]` | [2] Ngưỡng giá trị Coin (Threshold) | Pre-fill giá trị ngưỡng hiện tại | 1. Mở AF500 2. Quan sát ô nhập ngưỡng Coin | Đã có cấu hình ngưỡng | 1. Hiển thị đúng giá trị ngưỡng hiện tại từ DB | High | Auto-UI |
| `[AF500-7]` | [2] Ngưỡng giá trị Coin (Threshold) | Nhập ngưỡng hợp lệ & Lưu | 1. Nhập ngưỡng = `500` 2. Click Lưu | - | 1. Báo CMMSG17: `正常に保存されました。` 2. DB lưu ngưỡng = 500 `[Pending Q&A #7]` | High | Auto-UI |
| `[AF500-8]` | [2] Ngưỡng giá trị Coin (Threshold) | Nhập ngưỡng = 0 | 1. Nhập `0` 2. Click Lưu | - | 1. Báo lỗi validation (ngưỡng phải > 0) | High | Auto-Data |
| `[AF500-9]` | [2] Ngưỡng giá trị Coin (Threshold) | Nhập số âm / thập phân / chữ | 1. Nhập `-100`, `10.5`, `abc` | - | 1. UI block (CMR04) hoặc báo CMMSG54: `半角数字のみ入力してください。` | High | Auto-Data |
| `[AF500-10]` | [2] Ngưỡng giá trị Coin (Threshold) | Bỏ trống ô ngưỡng (bắt buộc) | 1. Xóa trắng ô ngưỡng 2. Click Lưu | - | 1. Báo lỗi CMMSG29: `{Threshold}は空欄にできません。` | High | Auto-UI |
| `[AF500-11]` | [2] Ngưỡng giá trị Coin (Threshold) | Nhập khoảng trắng / số 0 đầu (`0500`) | 1. Nhập `0500` 2. Click Lưu | - | 1. Lưu thành công với giá trị số `500` | Low | Auto-Data |
| `[AF500-12]` | [3] Danh sách / Toggle Quà cao cấp | Bật High-Value = ON cho 1 quà | 1. Chọn 1 quà -> gạt Toggle High-Value sang ON 2. Click Lưu (nếu có) | Có quà trong AF100 | 1. DB cập nhật cờ `is_premium = true` (hoặc tương đương) | High | Auto-UI |
| `[AF500-13]` | [3] Danh sách / Toggle Quà cao cấp | Tắt High-Value = OFF | 1. Gạt Toggle High-Value sang OFF 2. Click Lưu | - | 1. DB cập nhật `is_premium = false` | High | Auto-UI |
| `[AF500-14]` | [3] Danh sách / Toggle Quà cao cấp | Rollback khi API lỗi | 1. Giả lập API lỗi 500 2. Gạt Toggle | - | 1. Hiển thị CMMSG1 và tự động rollback Toggle về trạng thái ban đầu | Medium | Auto-UI |
| `[AF500-15]` | [4] Cấu hình hiệu ứng Animation | Chọn / Upload hiệu ứng đặc biệt | 1. Chọn loại animation hoặc upload asset hiệu ứng (nếu Spec có) 2. Lưu | - | 1. Lưu thành công, file đúng định dạng theo CMR10 `[Pending Q&A #7]` | Medium | Manual-Only (Visual) |
| `[AF500-16]` | [5] Button Lưu (Save) | Debounce chống double-click (CMR15) | 1. Sửa ngưỡng 2. Double-click nút Lưu liên tiếp | - | 1. Chỉ gọi API 1 lần, hiển thị Loading CMMSG27 | Medium | Auto-UI |
| `[AF500-17]` | [6] Button Hủy / Quay lại (CMR07) | Quay lại khi đã thay đổi chưa lưu | 1. Sửa giá trị ngưỡng 2. Click Hủy / Quay lại | - | 1. Hiển thị popup xác nhận CMMSG46 (`[キャンセル]` ở lại, `[OK]` hủy thay đổi) | High | Auto-UI |
| `[AF500-18]` | [7] Error Handling | Mất mạng / Lỗi 500 / Hết phiên | 1. Ngắt mạng hoặc giả lập 500 / hết hạn token 2. Click Lưu | - | 1. Hiển thị CMMSG8 (Mạng), CMMSG1 (500), CMMSG10 (Hết phiên) | High | Auto-API |
| | **III. SUB-LAYOUTS / CROSS-PLATFORM APP (I601)** | | | | | | |
| `[AF500-19]` | [8] Đồng bộ App I601 (E2E) | Gửi quà đúng bằng ngưỡng (`= 500`) | 1. Đặt ngưỡng = 500 2. Trên App Viewer gửi quà 500 coin vào phòng Live | Phòng Live đang chạy, Viewer đủ coin | 1. Chế độ High-Value Gift Animation (`I601`) kích hoạt trên màn hình cả Viewer và Streamer | High | Manual-Only (Visual) |
| `[AF500-20]` | [8] Đồng bộ App I601 (E2E) | Gửi quà dưới ngưỡng (`= 499`) | 1. Trên App Viewer gửi quà 499 coin | Phòng Live đang chạy | 1. Chỉ hiển thị hiệu ứng quà thường, KHÔNG kích hoạt chế độ `I601` | High | Manual-Only (Visual) |
| `[AF500-21]` | [8] Đồng bộ App I601 (E2E) | Gửi quà vượt ngưỡng (`> 500`) | 1. Trên App Viewer gửi quà 1,000 coin | Phòng Live đang chạy | 1. Kích hoạt chế độ `I601` mượt mà, trừ đúng coin và cộng đúng GOLD | High | Manual-Only (Visual) |
| `[AF500-22]` | [8] Đồng bộ App I601 (E2E) | Nhiều Viewer gửi quà cao cấp đồng thời | 1. 3 Viewer gửi quà cao cấp liên tiếp trong 2 giây | Phòng Live đang chạy | 1. Animation xếp hàng (queue) phát lần lượt đầy đủ, không lag/crash App | High | Manual-Only (UX) |
| `[AF500-23]` | [9] Layout & RBAC | Responsive & Role Read-only | 1. Kiểm tra trên độ phân giải 1024px và với tài khoản chỉ xem | - | 1. Không vỡ layout; role chỉ xem bị khóa nút Lưu/Toggle | Low | Auto-UI |

*(Lưu ý: Khi có Spec/Figma chi tiết của `AF500`, bổ sung thêm các control đặc thù nếu có)*

---

## THỐNG KÊ AUTOMATION FEASIBILITY (AF500)

| Nhóm | Số lượng | Tỷ lệ |
|---| :---: | :---: |
| `Auto-UI` | 13 | 56.5% |
| `Auto-API` | 2 | 8.7% |
| `Auto-Data` | 3 | 13.0% |
| `Manual-Only` (Visual / UX) | 5 | 21.7% |
| **Tổng cộng** | **23** | **~78.3% Auto / ~21.7% Manual** ✅ |
