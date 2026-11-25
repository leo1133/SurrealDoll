# BẢNG KỊCH BẢN KIỂM THỬ BACKEND API (API TEST SUITE)
## Màn hình: AF400 — Gift Manage: Gift Category Manage (Quản lý Danh mục Quà tặng)
### Áp dụng: Quy chuẩn Trụ cột 3 (`Universal_Rules/03_api_test_case_rule.md`) & Bộ 419 Viewpoints (`API_controls/API_Viewpoint.md`)
### Phân hệ: Web Master Admin / Quản lý Quà tặng (`AF` Module)

---

## 1. BÓC TÁCH THÔNG TIN CONTRACT API (API CONTRACT ANALYSIS)

| Thuộc tính Contract | Chi tiết Đặc tả Kỹ thuật |
| :--- | :--- |
| **Chức năng nghiệp vụ** | CRUD Danh mục quà tặng: `GET`, `POST`, `PUT`, `DELETE` `/api/v1/admin/gift-categories` |
| **Base URL (Dev / STG)** | `https://api-admin-dev.surrealdolls.com` / `https://api-admin-stg.surrealdolls.com` |
| **Headers bắt buộc** | `Authorization: Bearer <master_admin_token>`, `Content-Type: application/json`, `Accept: application/json` |
| **Phân quyền RBAC** | Master Admin toàn quyền; Role Read-only / Agency / Streamer bị chặn `403 Forbidden`. |

### Cấu trúc Tham số Request:
| Tên trường (Field) | Vị trí | Kiểu dữ liệu | Bắt buộc | Ràng buộc kỹ thuật & Nghiệp vụ | Giả định áp dụng |
| :--- | :---: | :---: | :---: | :--- | :---: |
| `id` | Path (`PUT/DELETE`) | `Integer` | Required | ID danh mục (`>= 1`). | `A6`, `A11` |
| `name` | JSON Body | `String` | Required | Tên danh mục. Trim space đầu/cuối. | `A1`, `A2`, `A6` |
| `sort_order` | JSON Body | `Integer` | Optional | Thứ tự sắp xếp (`>= 0`). | `A3` |

---

## 2. MA TRẬN 419 VIEWPOINTS ĐÃ PHỦ THEO `API_controls/API_Viewpoint.md`

- **Header, Auth & RBAC:** `HDR-001`, `ACC-006`, `CT-003`..`CT-008`, `AUTH-001`..`AUTH-009`, `PERM-001`, `PERM-002`, `PERM-006`, `PERM-007`
- **HTTP Method & Path Param:** `MTD-005`..`MTD-008`, `PATH-001`..`PATH-012`
- **Body JSON & Required Fields:** `BODY-002`..`BODY-009`, `REQ-001`..`REQ-011`
- **String & Integer Validation:** `STR-001`..`STR-018`, `INT-001`..`INT-012`
- **CRUD (Create / Update / Delete) & DB Persistence:** `CRE-001`..`CRE-007`, `UPD-001`..`UPD-007`, `DEL-001`..`DEL-008`
- **Response Validation & Security:** `RESP-001`, `RESP-010`, `RESP-016`, `SEC-004`, `SEC-007`

---

## 3. BẢNG CHI TIẾT TEST CASES BACKEND API (14 CỘT CHUẨN)

| ID | VP ID | API Name / Endpoint | Group / Viewpoint Group | Test Case / Scenario | Pre-condition | Request Data / Payload | Expected HTTP Status | Expected Response Body & DB State | Priority | Test Type | Assumption | R1 | R2 | Note / Business Rule |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| | | | **1. GET /api/v1/admin/gift-categories — DANH SÁCH DANH MỤC** | | | | | | | | | | | |
| `[AF400-API-01]` | `AUTH-001` | `GET /api/v1/admin/gift-categories` | Header - Authorization | Thiếu Authorization | - | No header | `401` | `{ "code": "UNAUTHORIZED" }` | High | Negative | `A9` | | | |
| `[AF400-API-02]` | `PERM-002` | `GET /api/v1/admin/gift-categories` | Authorization & permission | Role Agency / User gọi GET | Agency token | Valid token | `403` | `403 Forbidden` (`CMMSG5`) | High | Negative | `A10` | | | |
| `[AF400-API-03]` | `RESP-010` | `GET /api/v1/admin/gift-categories` | Response validation | Lấy danh sách & đối soát DB | Admin token | `GET /gift-categories` | `200` | Trả mảng danh mục sắp xếp theo `sort_order`, `gift_count` khớp DB | High | Positive | - | | | Rule 07 |
| `[AF400-API-04]` | `MTD-008` | `DELETE /api/v1/admin/gift-categories` | HTTP method & status | Gửi DELETE trực tiếp trên collection | Admin token | `DELETE /gift-categories` | `405` | `405 Method Not Allowed`, không xóa DB | High | Security | - | | | |
| | | | **2. POST /api/v1/admin/gift-categories — TẠO DANH MỤC** | | | | | | | | | | | |
| `[AF400-API-05]` | `AUTH-001` | `POST /api/v1/admin/gift-categories` | Header - Authorization | Thiếu Authorization | - | Valid body, no token | `401` | `{ "code": "UNAUTHORIZED" }` | High | Negative | `A9` | | | |
| `[AF400-API-06]` | `PERM-006` | `POST /api/v1/admin/gift-categories` | Authorization & permission | Role không có quyền tạo | Monitor token | Valid body | `403` | `403 Forbidden` | High | Negative | `A10` | | | |
| `[AF400-API-07]` | `CT-003` | `POST /api/v1/admin/gift-categories` | Header - Content-Type | Thiếu `Content-Type` | Admin token | No `Content-Type` | `415 / 400` | `415 Unsupported Media Type` | High | Negative | `A7` | | | |
| `[AF400-API-08]` | `BODY-003` | `POST /api/v1/admin/gift-categories` | Body - JSON structure | JSON thiếu ngoặc đóng | Admin token | `'{"name":"Normal"'` | `400` | `400 Bad Request` | High | Negative | `A13` | | | |
| `[AF400-API-09]` | `CRE-001` | `POST /api/v1/admin/gift-categories` | CRUD - Create | Tạo danh mục hợp lệ | Admin token | `{ "name": "Event Gift", "sort_order": 1 }` | `201` | DB `gift_categories` INSERT bản ghi mới | High | Positive | - | | | Rule 07 |
| `[AF400-API-10]` | `REQ-001` | `POST /api/v1/admin/gift-categories` | Required / optional | Thiếu `name` | Admin token | `{ "sort_order": 1 }` | `400 / 422` | Lỗi `name is required` | High | Negative | `A2` | | | |
| `[AF400-API-11]` | `REQ-005` | `POST /api/v1/admin/gift-categories` | Required / optional | `name = ""` hoặc `"   "` | Admin token | `{ "name": "   " }` | `400 / 422` | Lỗi `name cannot be empty` | High | Negative | `A2` | | | |
| `[AF400-API-12]` | `STR-005` | `POST /api/v1/admin/gift-categories` | String / text | `name` có space đầu/cuối (`"  Event  "`) | Admin token | `{ "name": "  Event  " }` | `201` | DB lưu `"Event"` (trimmed) | Medium | Boundary | `A1` | | | |
| `[AF400-API-13]` | `STR-009` | `POST /api/v1/admin/gift-categories` | String / text | `name` vượt `max_length` | Admin token | `name` dài `{max}+1` ký tự | `400 / 422` | Lỗi vượt độ dài | Medium | Boundary | `A6` | | | |
| `[AF400-API-14]` | `STR-018` | `POST /api/v1/admin/gift-categories` | String / text | Trùng tên danh mục đã tồn tại | Đã có "Event Gift" | `{ "name": "Event Gift" }` | `409 / 400` | Báo lỗi trùng tên (`[Pending Q&A #5]`) | Medium | Negative | - | | | |
| `[AF400-API-15]` | `INT-007` | `POST /api/v1/admin/gift-categories` | Integer (`sort_order`) | `sort_order = -1` hoặc `"abc"` (`INT-009`) | Admin token | `{ "name": "A", "sort_order": -1 }` | `400 / 422` | Lỗi validation số nguyên | Medium | Boundary | `A3` | | | |
| `[AF400-API-16]` | `SEC-007` | `POST /api/v1/admin/gift-categories` | Security | Stored XSS trong `name` | Admin token | `{ "name": "<script>alert(1)</script>" }` | `201 / 400` | Lưu escaped hoặc từ chối | High | Security | `A8` | | | |
| | | | **3. PUT /api/v1/admin/gift-categories/:id — CẬP NHẬT DANH MỤC** | | | | | | | | | | | |
| `[AF400-API-17]` | `AUTH-001` | `PUT /api/v1/admin/gift-categories/:id` | Header - Authorization | Thiếu Authorization | - | No token | `401` | `{ "code": "UNAUTHORIZED" }` | High | Negative | `A9` | | | |
| `[AF400-API-18]` | `PERM-002` | `PUT /api/v1/admin/gift-categories/:id` | Authorization & permission | Role không có quyền sửa | Monitor token | Valid body | `403` | `403 Forbidden` | High | Negative | `A10` | | | |
| `[AF400-API-19]` | `UPD-001` | `PUT /api/v1/admin/gift-categories/:id` | CRUD - Update | Cập nhật tên & sort_order hợp lệ | Category ID=1 | `{ "name": "Special Gift", "sort_order": 2 }` | `200` | DB cập nhật `name, sort_order, updated_at` | High | Positive | - | | | Rule 07 |
| `[AF400-API-20]` | `UPD-002` | `PUT /api/v1/admin/gift-categories/:id` | CRUD - Update | Thiếu `name` khi PUT | Category ID=1 | `{ "sort_order": 2 }` | `400 / 422` | Báo lỗi thiếu `name`, DB giữ nguyên | High | Negative | `A2` | | | |
| `[AF400-API-21]` | `UPD-003` | `PUT /api/v1/admin/gift-categories/:id` | CRUD - Update | ID không tồn tại | - | `PUT /gift-categories/999999` | `404` | `{ "code": "NOT_FOUND" }` | High | Negative | `A11` | | | |
| `[AF400-API-22]` | `PATH-005` | `PUT /api/v1/admin/gift-categories/:id` | Path parameter | ID sai định dạng (`abc`) | Admin token | `PUT /gift-categories/abc` | `400` | `{ "code": "INVALID_PARAM" }` | Medium | Negative | `A6` | | | |
| | | | **4. DELETE /api/v1/admin/gift-categories/:id — XÓA DANH MỤC** | | | | | | | | | | | |
| `[AF400-API-23]` | `AUTH-001` | `DELETE /api/v1/admin/gift-categories/:id` | Header - Authorization | Thiếu Authorization | - | No token | `401` | `{ "code": "UNAUTHORIZED" }` | High | Negative | `A9` | | | |
| `[AF400-API-24]` | `PERM-007` | `DELETE /api/v1/admin/gift-categories/:id` | Authorization & permission | Role không có quyền xóa | Monitor token | `DELETE /gift-categories/1` | `403` | `403 Forbidden`, DB giữ nguyên | High | Negative | `A10` | | | |
| `[AF400-API-25]` | `DEL-001` | `DELETE /api/v1/admin/gift-categories/:id` | CRUD - Delete | Xóa danh mục rỗng (0 quà) | Category rỗng | `DELETE /gift-categories/<empty_id>` | `200 / 204` | DB soft-delete (`deleted_at IS NOT NULL`) | High | Positive | - | | | Rule 07 |
| `[AF400-API-26]` | `DEL-003` | `DELETE /api/v1/admin/gift-categories/:id` | CRUD - Delete | Xóa lần 2 cùng ID đã xóa | Category vừa xóa | `DELETE /gift-categories/<empty_id>` | `404` | `{ "code": "NOT_FOUND" }` (`A12`) | Medium | Negative | `A12` | | | |
| `[AF400-API-27]` | `DEL-004` | `DELETE /api/v1/admin/gift-categories/:id` | CRUD - Delete | Xóa ID không tồn tại | - | `DELETE /gift-categories/999999` | `404` | `{ "code": "NOT_FOUND" }` | High | Negative | `A11` | | | |
| `[AF400-API-28]` | `DEL-006` | `DELETE /api/v1/admin/gift-categories/:id` | CRUD - Delete | Xóa danh mục đang chứa quà | Category có >= 1 quà | `DELETE /gift-categories/<has_gifts_id>` | `400 / 409` | Chặn xóa do ràng buộc khóa ngoại (hoặc cascade `[Pending Q&A #6]`) | High | Negative | - | | | |
