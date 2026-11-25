# BẢNG ĐẶC TẢ KIỂM THỬ GIAO DIỆN THỦ CÔNG (MANUAL UI TEST SUITE)
## Màn hình: AF500 — GIFT Animation Type (演出種類 — Luồng tích hợp trên AF200, AF300, AF100 & I600/I601)
### Phân hệ: Master Admin Web / 商品管理 (`AF` Module)
### Nguồn Spec: Google Sheet `AF500` (gid=`1458098150`) + `AF100` + `AF200` + `AF300`
### Áp dụng: `Universal_Rules/02_manual_ui_test_case_rule.md` & `UI_controls/`

---

## BẢNG ĐIỀU KHIỂN TIẾN ĐỘ & THỐNG KÊ (DASHBOARD HEADER)

| Thuộc tính | Giá trị | Thuộc tính | Giá trị | Round 1 Metric | Kết quả | Round 2 Metric | Kết quả |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Module Code** | `AF500` | **Environment** | `Dev-Admin` / `STG-Admin` | **Pass** | 0 | **Pass** | 0 |
| **Total Testcases** | **28** | **% Executed** | 0% | **Fail** | 0 | **Fail** | 0 |
| **Plan to Execute** | **28** | **Creator** | `QA` | **Impact** | 0 | **Impact** | 0 |
| **Spec Source** | Google Sheet `AF500` | **Liên kết chéo** | `AF100`, `AF200`, `AF300`, `I600`, `I601` | **Not Run** | 28 | **Not Run** | 0 |
| | | | | **Total** | 28 | **Total** | 0 |

---

## CHI TIẾT BẢNG TEST CASES (8 CỘT CHUẨN MARKDOWN)

| ID | Title | Big item | Steps | Pre-condition | Expected | Priority | Automation Feasibility |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| | **I. RADIO `演出種類` TRÊN AF200 / AF300** | | | | | | |
| `[AF500-1]` | [1] Radio `演出種類` | Hiển thị mặc định `通常演出` | 1. Mở AF200 (Tạo mới gift) | Đã đăng nhập Admin | 1. Hiển thị 3 Radio: `通常演出` (checked mặc định), `シャッター演出`, `継続演出` | High | Auto-UI |
| `[AF500-2]` | [1][2] `通常演出` (Default) | Giá nhập tự do + Category enabled + Gift Content enabled | 1. Giữ Radio = `通常演出` 2. Nhập giá `350` 3. Chọn Category 4. Upload `ギフトコンテンツ` | - | 1. Cho phép nhập giá tự do, chọn Category và upload `ギフトコンテンツ` bình thường | High | Auto-UI |
| `[AF500-3]` | [1][2] `シャッター演出` (Shutter) | Giá chỉ chọn `5,000` hoặc `10,000` | 1. Chọn Radio `シャッター演出` 2. Quan sát mục Giá | - | 1. Không cho nhập tự do; chỉ hiển thị lựa chọn giá `5,000` và `10,000` | High | Auto-UI |
| `[AF500-4]` | [1][2] `シャッター演出` (Shutter) | Category KHÔNG cho chọn (Disabled) | 1. Chọn Radio `シャッター演出` 2. Quan sát & thử click `ギフトカテゴリ` | - | 1. Trường `ギフトカテゴリ` (và nút `+`) bị Disabled / không cho chọn | High | Auto-UI |
| `[AF500-5]` | [1][2] `シャッター演出` (Shutter) | `ギフトコンテンツ` bị Disable (hiệu ứng cố định) | 1. Chọn Radio `シャッター演出` 2. Quan sát vùng upload `ギフトコンテンツ` | - | 1. Vùng upload `ギフトコンテンツ` bị Disabled (không cần/không cho upload vì dùng hiệu ứng cố định) | High | Auto-UI |
| `[AF500-6]` | [1][2] `継続演出` (Continuous) | Giá chỉ chọn `1000pt`, `3000pt`, `5,000pt`, `10,000pt` | 1. Chọn Radio `継続演出` 2. Quan sát mục Giá | - | 1. Chỉ hiển thị 4 mức giá: `1000pt`, `3000pt`, `5,000pt`, `10,000pt` | High | Auto-UI |
| `[AF500-7]` | [1][2] `継続演出` (Continuous) | Category bị Disable | 1. Chọn Radio `継続演出` 2. Quan sát trường `ギフトカテゴリ` | - | 1. Trường `ギフトカテゴリ` (và nút `+`) bị Disabled | High | Auto-UI |
| `[AF500-8]` | [1][2] `継続演出` (Continuous) | `ギフトコンテンツ` bị Disable | 1. Chọn Radio `継続演出` 2. Quan sát vùng upload `ギフトコンテンツ` | - | 1. Vùng upload `ギフトコンテンツ` bị Disabled | High | Auto-UI |
| `[AF500-9]` | [1][2] Chuyển đổi giữa 3 Radio | Chuyển `通常演出` -> `シャッター演出` -> `通常演出` | 1. Ở `通常演出` nhập giá `250` + chọn Category + upload Content 2. Chuyển sang `シャッター演出` 3. Chuyển lại `通常演出` | - | 1. Khi về `通常演出`, các trường Giá/Category/Content mở lại hoạt động bình thường `[Q&A AF500 #1]` | High | Auto-UI |
| `[AF500-10]` | [2] Tạo thành công | Tạo gift `シャッター演出` giá `5,000` | 1. Chọn `シャッター演出`, nhập tên + icon, chọn giá `5,000` 2. Click `登録` | - | 1. Tạo thành công (`CMMSG12`), không báo lỗi thiếu Category/Content; DB lưu `animation_type=shutter` | High | Auto-UI |
| `[AF500-11]` | [2] Tạo thành công | Tạo gift `継続演出` giá `3,000pt` | 1. Chọn `継続演出`, nhập tên + icon, chọn giá `3,000pt` 2. Click `登録` | - | 1. Tạo thành công (`CMMSG12`), DB lưu `animation_type=continuous` | High | Auto-UI |
| `[AF500-12]` | [2] Sửa trên AF300 | Mở AF300 của gift `シャッター演出` | 1. Mở chi tiết gift Shutter trên AF300 | Đã có gift Shutter | 1. Pre-fill đúng `シャッター演出`, giá `5,000`, Category & Content bị disable | High | Auto-UI |
| `[AF500-13]` | [2] Sửa trên AF300 | Mở AF300 của gift `継続演出` | 1. Mở chi tiết gift Continuous trên AF300 | Đã có gift Continuous | 1. Pre-fill đúng `継続演出`, giá tương ứng, Category & Content bị disable | High | Auto-UI |
| | **II. FILTER & CỘT `演出種類` TRÊN AF100** | | | | | | |
| `[AF500-14]` | [4] Pulldown Filter `演出種類` | Mặc định `全て演出種類` & danh sách 4 options | 1. Mở AF100 2. Click mở pulldown `演出種類` | - | 1. Hiển thị đúng 4 options: `全て演出種類`, `通常演出`, `シャッター演出`, `継続演出` | High | Auto-UI |
| `[AF500-15]` | [4] Pulldown Filter `演出種類` | Lọc theo `通常演出` | 1. Chọn `通常演出` -> bấm `検索` | Có dữ liệu | 1. Bảng chỉ trả về gift `通常演出` | High | Auto-UI |
| `[AF500-16]` | [4] Pulldown Filter `演出種類` | Lọc theo `シャッター演出` | 1. Chọn `シャッター演出` -> bấm `検索` | Có dữ liệu | 1. Bảng chỉ trả về gift `シャッター演出` | High | Auto-UI |
| `[AF500-17]` | [4] Pulldown Filter `演出種類` | Lọc theo `継続演出` | 1. Chọn `継続演出` -> bấm `検索` | Có dữ liệu | 1. Bảng chỉ trả về gift `継続演出` | High | Auto-UI |
| `[AF500-18]` | [4] Pulldown Filter `演出種類` | Kết hợp với Keyword và Status | 1. Nhập Keyword + chọn `シャッター演出` + `公開` -> `検索` | - | 1. Lọc AND chính xác đồng thời các điều kiện | Medium | Auto-UI |
| `[AF500-19]` | [4] Pulldown Filter `演出種類` | Nút `クリア` reset `演出種類` | 1. Đang lọc `シャッター演出` 2. Click nút `クリア` | - | 1. Reset pulldown `演出種類` về `全て演出種類` và reload danh sách | Medium | Auto-UI |
| `[AF500-20]` | [5] Cột `演出種類` | Hiển thị đúng nhãn trên bảng AF100 | 1. Quan sát cột `演出種類` của 3 loại gift trên bảng AF100 | Có đủ 3 loại gift | 1. Hiển thị chính xác text `通常演出`, `シャッター演出`, `継続演出` | High | Auto-UI |
| | **III. HIỂN THỊ & HIỆU ỨNG TRÊN APP (I600 / I601)** | | | | | | |
| `[AF500-21]` | [Cross-Sync] App `I600` | Gift `シャッター演出` hiển thị đúng trên App `I600` | 1. Mở danh sách quà trong phòng Live (`I600`) | Có phòng Live | 1. Hiển thị đúng icon, tên, giá (`5,000` hoặc `10,000`) | High | Manual-Only (Visual) |
| `[AF500-22]` | [Cross-Sync] App `I600` | Gift `継続演出` hiển thị đúng trên App `I600` | 1. Mở danh sách quà trong phòng Live (`I600`) | Có phòng Live | 1. Hiển thị đúng icon, tên, giá (`1000..10000pt`) | High | Manual-Only (Visual) |
| `[AF500-23]` | [Cross-Sync] App `I601` | Gửi gift `シャッター演出` trong phòng Live | 1. Viewer gửi gift `シャッター演出` | Phòng Live đang chạy | 1. Phát đúng hiệu ứng Shutter cố định trên màn hình cả Viewer và Streamer | High | Manual-Only (Visual) |
| `[AF500-24]` | [Cross-Sync] App `I601` | Gửi gift `継続演出` trong phòng Live | 1. Viewer gửi gift `継続演出` | Phòng Live đang chạy | 1. Phát đúng hiệu ứng Continuous cố định trên màn hình cả Viewer và Streamer | High | Manual-Only (Visual) |
| `[AF500-25]` | [Cross-Sync] App `I601` | Gửi nhiều gift hiệu ứng cao cấp liên tiếp | 1. Nhiều Viewer gửi liên tiếp Shutter / Continuous | Phòng Live đang chạy | 1. Hiệu ứng xếp hàng (queue) phát lần lượt, không lag/crash App | High | Manual-Only (UX) |
| `[AF500-26]` | [-] Error Handling | Mất kết nối mạng khi tạo/lọc (`CMMSG8`) | 1. Ngắt mạng (Offline) 2. Thực hiện tạo/lọc gift | - | 1. Hiển thị đúng thông báo lỗi mạng `CMMSG8` | Medium | Auto-API |
| `[AF500-27]` | [-] Error Handling | Lỗi Server 500 khi tạo/lọc (`CMMSG1`) | 1. Giả lập API trả HTTP 500 | - | 1. Hiển thị đúng thông báo lỗi hệ thống `CMMSG1` | Medium | Auto-API |
| `[AF500-28]` | [-] Error Handling | Hết phiên đăng nhập khi tạo/lọc (`CMMSG10`) | 1. Token hết hạn (401) 2. Thực hiện tạo/lọc gift | - | 1. Hiển thị `CMMSG10` và redirect về Login | Medium | Auto-API |

---

## THỐNG KÊ AUTOMATION FEASIBILITY (AF500)

| Nhóm | Số lượng | Tỷ lệ |
|---| :---: | :---: |
| `Auto-UI` | 20 | 71.4% |
| `Auto-API` | 3 | 10.7% |
| `Manual-Only` (Visual / UX) | 5 | 17.9% |
| **Tổng cộng** | **28** | **82.1% Auto / 17.9% Manual** ✅ |
