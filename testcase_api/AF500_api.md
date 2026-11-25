# BẢNG KỊCH BẢN KIỂM THỬ BACKEND API (API TEST SUITE)
## Màn hình: AF500 — Quà cao cấp (High-Value Gift Configuration)
### Áp dụng: Quy chuẩn Trụ cột 3 (`Universal_Rules/03_api_test_case_rule.md`) & Bộ 419 Viewpoints (`API_controls/API_Viewpoint.md`)
### Phân hệ: Web Master Admin / Quản lý Quà tặng (`AF` Module)

---

## 1. BÓC TÁCH THÔNG TIN CONTRACT API (API CONTRACT ANALYSIS)

| Thuộc tính Contract | Chi tiết Đặc tả Kỹ thuật |
| :--- | :--- |
| **Chức năng nghiệp vụ** | Lấy & cập nhật cấu hình Quà cao cấp (`GET / PUT /api/v1/admin/high-value-gift/config`) kích hoạt hiệu ứng `I601` trên App |
| **Base URL (Dev / STG)** | `https://api-admin-dev.surrealdolls.com` / `https://api-admin-stg.surrealdolls.com` |
| **Headers bắt buộc** | `Authorization: Bearer <master_admin_token>`, `Content-Type: application/json`, `Accept: application/json` |
| **Phân quyền RBAC** | Master Admin toàn quyền; Role Read-only / Agency / Streamer bị chặn `403 Forbidden`. |

### Cấu trúc Tham số Request:
| Tên trường (Field) | Vị trí | Kiểu dữ liệu | Bắt buộc | Ràng buộc kỹ thuật & Nghiệp vụ | Giả định áp dụng |
| :--- | :---: | :---: | :---: | :--- | :---: |
| `threshold` | JSON Body | `Integer` | Required | Ngưỡng coin kích hoạt chế độ quà cao cấp (`>= 1`). | `A3` |
| `is_enabled` | JSON Body | `Boolean` | Optional | Bật/tắt chế độ hiệu ứng quà cao cấp toàn hệ thống. | - |
| `gift_ids` | JSON Body | `Array[Int]` | Optional | Danh sách ID quà được đánh dấu cao cấp (nếu cấu hình theo list). | `A7` |

---

## 2. MA TRẬN 419 VIEWPOINTS ĐÃ PHỦ THEO `API_controls/API_Viewpoint.md`

- **Header, Auth & RBAC:** `HDR-001`, `ACC-006`, `CT-003`..`CT-008`, `AUTH-001`..`AUTH-009`, `PERM-001`, `PERM-002`
- **HTTP Method & Body JSON:** `MTD-005`, `MTD-008`, `BODY-002`..`BODY-009`
- **Required, Integer (`threshold`), Boolean (`is_enabled`), Array (`gift_ids`):** `REQ-001`..`REQ-011`, `INT-001`..`INT-019`, `BOOL-001`..`BOOL-010`, `ARR-001`..`ARR-005`
- **Update, Response & Security:** `UPD-001`, `UPD-002`, `UPD-007`, `RESP-001`, `RESP-010`, `SEC-008`

---

## 3. BẢNG CHI TIẾT TEST CASES BACKEND API (14 CỘT CHUẨN)

| ID | VP ID | API Name / Endpoint | Group / Viewpoint Group | Test Case / Scenario | Pre-condition | Request Data / Payload | Expected HTTP Status | Expected Response Body & DB State | Priority | Test Type | Assumption | R1 | R2 | Note / Business Rule |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| | | | **1. GET /api/v1/admin/high-value-gift/config — LẤY CẤU HÌNH** | | | | | | | | | | | |
| `[AF500-API-01]` | `AUTH-001` | `GET /api/v1/admin/high-value-gift/config` | Header - Authorization | Thiếu Authorization | - | No header | `401` | `{ "code": "UNAUTHORIZED" }` | High | Negative | `A9` | | | |
| `[AF500-API-02]` | `PERM-002` | `GET /api/v1/admin/high-value-gift/config` | Authorization & permission | Role Agency / User gọi GET | Agency token | Valid token | `403` | `403 Forbidden` (`CMMSG5`) | High | Negative | `A10` | | | |
| `[AF500-API-03]` | `RESP-010` | `GET /api/v1/admin/high-value-gift/config` | Response validation | Lấy cấu hình hiện tại khớp DB | Admin token | `GET .../config` | `200` | Trả về `threshold`, `is_enabled`, `gift_ids` khớp DB `[Pending Q&A #7]` | High | Positive | - | | | |
| `[AF500-API-04]` | `MTD-008` | `DELETE /api/v1/admin/high-value-gift/config` | HTTP method & status | Gửi DELETE lên endpoint config | Admin token | `DELETE .../config` | `405` | `405 Method Not Allowed` | High | Security | - | | | |
| | | | **2. PUT /api/v1/admin/high-value-gift/config — CẬP NHẬT CẤU HÌNH** | | | | | | | | | | | |
| `[AF500-API-05]` | `AUTH-001` | `PUT /api/v1/admin/high-value-gift/config` | Header - Authorization | Thiếu Authorization | - | No token | `401` | `{ "code": "UNAUTHORIZED" }` | High | Negative | `A9` | | | |
| `[AF500-API-06]` | `AUTH-009` | `PUT /api/v1/admin/high-value-gift/config` | Header - Authorization | Token hết hạn | Expired token | Valid body | `401` | `{ "code": "TOKEN_EXPIRED" }` | High | Negative | `A9` | | | |
| `[AF500-API-07]` | `PERM-002` | `PUT /api/v1/admin/high-value-gift/config` | Authorization & permission | Role không có quyền sửa | Monitor token | `{ "threshold": 500 }` | `403` | `403 Forbidden`, DB giữ nguyên | High | Negative | `A10` | | | |
| `[AF500-API-08]` | `CT-003` | `PUT /api/v1/admin/high-value-gift/config` | Header - Content-Type | Thiếu `Content-Type` | Admin token | No `Content-Type` | `415 / 400` | `415 Unsupported Media Type` | High | Negative | `A7` | | | |
| `[AF500-API-09]` | `BODY-003` | `PUT /api/v1/admin/high-value-gift/config` | Body - JSON structure | JSON thiếu ngoặc đóng | Admin token | `'{"threshold":500'` | `400` | `400 Bad Request` | High | Negative | `A13` | | | |
| `[AF500-API-10]` | `UPD-001` | `PUT /api/v1/admin/high-value-gift/config` | CRUD - Update | Cập nhật cấu hình hợp lệ | Admin token | `{ "threshold": 500, "is_enabled": true }` | `200` | DB cập nhật `threshold = 500`, `updated_at` đổi mới | High | Positive | - | | | Rule 07 |
| `[AF500-API-11]` | `REQ-001` | `PUT /api/v1/admin/high-value-gift/config` | Required / optional | Thiếu trường `threshold` | Admin token | `{ "is_enabled": true }` | `400 / 422` | Lỗi `threshold is required` | High | Negative | `A2` | | | |
| `[AF500-API-12]` | `INT-002` | `PUT /api/v1/admin/high-value-gift/config` | Integer (`threshold`) | `threshold = 1` (min boundary) | Admin token | `{ "threshold": 1 }` | `200` | Lưu thành công | High | Boundary | - | | | |
| `[AF500-API-13]` | `INT-006` | `PUT /api/v1/admin/high-value-gift/config` | Integer (`threshold`) | `threshold = 0` | Admin token | `{ "threshold": 0 }` | `400 / 422` | Lỗi `threshold >= 1` | High | Boundary | - | | | |
| `[AF500-API-14]` | `INT-007` | `PUT /api/v1/admin/high-value-gift/config` | Integer (`threshold`) | `threshold = -100` (âm) | Admin token | `{ "threshold": -100 }` | `400 / 422` | Lỗi validation số âm | High | Boundary | - | | | |
| `[AF500-API-15]` | `INT-008` | `PUT /api/v1/admin/high-value-gift/config` | Integer (`threshold`) | `threshold = 500.5` (float) | Admin token | `{ "threshold": 500.5 }` | `400 / 422` | Lỗi không phải số nguyên | High | Negative | `A3` | | | |
| `[AF500-API-16]` | `INT-009` | `PUT /api/v1/admin/high-value-gift/config` | Integer (`threshold`) | `threshold = "abc"` (text) | Admin token | `{ "threshold": "abc" }` | `400 / 422` | Lỗi kiểu dữ liệu | High | Negative | `A3` | | | |
| `[AF500-API-17]` | `INT-012` | `PUT /api/v1/admin/high-value-gift/config` | Integer (`threshold`) | `threshold` overflow 32-bit (`2147483648`) | Admin token | `{ "threshold": 2147483648 }` | `400 / 422` | Không lỗi 500 | High | Boundary | - | | | |
| `[AF500-API-18]` | `BOOL-009` | `PUT /api/v1/admin/high-value-gift/config` | Boolean (`is_enabled`) | `is_enabled = "abc"` (sai kiểu) | Admin token | `{ "threshold": 500, "is_enabled": "abc" }` | `400 / 422` | Lỗi kiểu boolean | Medium | Negative | - | | | |
| `[AF500-API-19]` | `ARR-004` | `PUT /api/v1/admin/high-value-gift/config` | Array (`gift_ids`) | `gift_ids` là string `"1"` thay vì array | Admin token | `{ "threshold": 500, "gift_ids": "1" }` | `400 / 422` | Lỗi kiểu array | Medium | Negative | - | | | |
| `[AF500-API-20]` | `ARR-005` | `PUT /api/v1/admin/high-value-gift/config` | Array (`gift_ids`) | `gift_ids` chứa ID quà không tồn tại (`[999999]`) | Admin token | `{ "threshold": 500, "gift_ids": [999999] }` | `400 / 404` | Lỗi khóa ngoại không tồn tại | High | Negative | - | | | |
| `[AF500-API-21]` | `UPD-007` | `PUT /api/v1/admin/high-value-gift/config` | CRUD - Update | PUT idempotent (gửi cùng payload 3 lần) | Admin token | 3 PUT giống nhau | `200` | Trạng thái cuối cùng nhất quán | Medium | Positive | - | | | |
