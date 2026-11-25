# BẢNG KỊCH BẢN KIỂM THỬ BACKEND API (API TEST SUITE)
## Màn hình: AF300 — Gift Manage: Gift Update / Delete (Chi tiết, Cập nhật & Xóa Quà tặng)
### Áp dụng: Quy chuẩn Trụ cột 3 (`Universal_Rules/03_api_test_case_rule.md`) & Bộ 419 Viewpoints (`API_controls/API_Viewpoint.md`)
### Phân hệ: Web Master Admin / Quản lý Quà tặng (`AF` Module)

---

## 1. BÓC TÁCH THÔNG TIN CONTRACT API (API CONTRACT ANALYSIS)

| Thuộc tính Contract | Chi tiết Đặc tả Kỹ thuật |
| :--- | :--- |
| **Chức năng nghiệp vụ** | 1. Lấy chi tiết quà (`GET /api/v1/admin/gifts/:id`)<br>2. Cập nhật quà (`PUT/PATCH /api/v1/admin/gifts/:id`)<br>3. Xóa quà (`DELETE /api/v1/admin/gifts/:id`) |
| **Base URL (Dev / STG)** | `https://api-admin-dev.surrealdolls.com` / `https://api-admin-stg.surrealdolls.com` |
| **Headers bắt buộc** | `Authorization: Bearer <master_admin_token>`<br>`Content-Type: application/json` (PUT/PATCH)<br>`Accept: application/json` |
| **Phân quyền RBAC** | Master Admin có quyền xem/sửa/xóa. Read-only / Agency / Streamer bị từ chối `403 Forbidden`. |

### Cấu trúc Tham số Request:
| Tên trường (Field) | Vị trí | Kiểu dữ liệu | Bắt buộc | Ràng buộc kỹ thuật & Nghiệp vụ | Giả định áp dụng |
| :--- | :---: | :---: | :---: | :--- | :---: |
| `id` | Path | `Integer` | Required | ID quà tặng (`>= 1`), chưa bị soft-delete. | `A6`, `A11` |
| `name` | JSON Body | `String` | Required (PUT) | Tên quà tặng. Trim space đầu/cuối. | `A1`, `A2`, `A6` |
| `coin_price` | JSON Body | `Integer` | Required (PUT) | Giá coin (`>= 1`). | `A3` |
| `category_id` | JSON Body | `Integer` | Required (PUT) | Khóa ngoại trỏ tới `gift_categories.id` tồn tại. | `A3` |
| `sort_order` | JSON Body | `Integer` | Optional | Thứ tự hiển thị (`>= 0`). | `A3` |
| `status` | JSON Body | `Enum` | Optional | `active` hoặc `inactive`. | `A5` |

---

## 2. MA TRẬN 419 VIEWPOINTS ĐÃ PHỦ THEO `API_controls/API_Viewpoint.md`

- **Header & Authorization / RBAC:** `HDR-001`, `ACC-006`, `CT-003`..`CT-008`, `AUTH-001`..`AUTH-009`, `PERM-001`, `PERM-002`, `PERM-007`, `PERM-008`
- **Path Parameter (`:id`) cho GET / PUT / DELETE:** `PATH-001`..`PATH-015`
- **Body JSON Structure:** `BODY-002`..`BODY-009`
- **CRUD - Update (`PUT / PATCH`):** `UPD-001`..`UPD-014`
- **CRUD - Delete (`DELETE`):** `DEL-001`..`DEL-008`
- **Field Validation & Security:** `STR-005`, `STR-009`, `INT-006`..`INT-012`, `ENUM-004`, `SEC-004`, `SEC-007`, `SEC-008`
- **Response Validation & DB Persistence:** `RESP-001`, `RESP-010`, `RESP-016`

---

## 3. BẢNG CHI TIẾT TEST CASES BACKEND API (14 CỘT CHUẨN)

| ID | VP ID | API Name / Endpoint | Group / Viewpoint Group | Test Case / Scenario | Pre-condition | Request Data / Payload | Expected HTTP Status | Expected Response Body & DB State | Priority | Test Type | Assumption | R1 | R2 | Note / Business Rule |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| | | | **1. GET /api/v1/admin/gifts/:id — CHI TIẾT QUÀ** | | | | | | | | | | | |
| `[AF300-API-01]` | `AUTH-001` | `GET /api/v1/admin/gifts/:id` | Header - Authorization | Thiếu Authorization | - | No `Authorization` header | `401` | `{ "code": "UNAUTHORIZED" }` | High | Negative | `A9` | | | |
| `[AF300-API-02]` | `PERM-002` | `GET /api/v1/admin/gifts/:id` | Authorization & permission | Agency / User gọi GET detail | Agency token | `GET /gifts/1` | `403` | `403 Forbidden` (`CMMSG5`) | High | Negative | `A10` | | | |
| `[AF300-API-03]` | `PATH-001` | `GET /api/v1/admin/gifts/:id` | Path parameter | ID hợp lệ, bản ghi tồn tại | Quà ID=1 tồn tại | `GET /gifts/1` | `200` | Trả đủ fields khớp DB 100% (`RESP-010`) | High | Positive | - | | | Rule 07 |
| `[AF300-API-04]` | `PATH-002` | `GET /api/v1/admin/gifts/:id` | Path parameter | ID không tồn tại | - | `GET /gifts/999999` | `404` | `{ "code": "NOT_FOUND" }` | High | Negative | `A11` | | | |
| `[AF300-API-05]` | `PATH-003` | `GET /api/v1/admin/gifts/:id` | Path parameter | `id = 0` | - | `GET /gifts/0` | `400 / 404` | Không trả dữ liệu | High | Boundary | - | | | |
| `[AF300-API-06]` | `PATH-004` | `GET /api/v1/admin/gifts/:id` | Path parameter | `id = -1` (âm) | - | `GET /gifts/-1` | `400 / 404` | Không lỗi 500 | High | Boundary | `A6` | | | |
| `[AF300-API-07]` | `PATH-005` | `GET /api/v1/admin/gifts/:id` | Path parameter | `id = abc` (chữ) | - | `GET /gifts/abc` | `400` | `{ "code": "INVALID_PARAM" }` | High | Negative | `A6` | | | |
| `[AF300-API-08]` | `PATH-006` | `GET /api/v1/admin/gifts/:id` | Path parameter | `id = 1.5` (thập phân) | - | `GET /gifts/1.5` | `400` | `{ "code": "INVALID_PARAM" }` | Medium | Negative | `A6` | | | |
| `[AF300-API-09]` | `PATH-011` | `GET /api/v1/admin/gifts/:id` | Path parameter | SQL Injection trong path (`/gifts/1%20OR%201=1`) | - | `GET /gifts/1%20OR%201=1` | `400 / 404` | Không thực thi SQL | High | Security | - | | | |
| `[AF300-API-10]` | `PATH-012` | `GET /api/v1/admin/gifts/:id` | Path parameter | Quà đã bị soft-delete | Quà đã xóa mềm | `GET /gifts/<deleted_id>` | `404` | `{ "code": "NOT_FOUND" }` | High | Negative | - | | | |
| | | | **2. PUT / PATCH /api/v1/admin/gifts/:id — CẬP NHẬT QUÀ** | | | | | | | | | | | |
| `[AF300-API-11]` | `AUTH-001` | `PUT /api/v1/admin/gifts/:id` | Header - Authorization | Thiếu Authorization | - | Valid body, no `Authorization` | `401` | `{ "code": "UNAUTHORIZED" }` | High | Negative | `A9` | | | |
| `[AF300-API-12]` | `PERM-002` | `PUT /api/v1/admin/gifts/:id` | Authorization & permission | Role không có quyền sửa (Monitor/Agency) | Monitor token | Valid body | `403` | `403 Forbidden`, DB không đổi | High | Negative | `A10` | | | |
| `[AF300-API-13]` | `CT-003` | `PUT /api/v1/admin/gifts/:id` | Header - Content-Type | Thiếu `Content-Type` | Admin token | Valid JSON, no `Content-Type` | `415 / 400` | `415 Unsupported Media Type` | High | Negative | `A7` | | | |
| `[AF300-API-14]` | `CT-005` | `PUT /api/v1/admin/gifts/:id` | Header - Content-Type | `Content-Type: text/plain` | Admin token | `Content-Type: text/plain` | `415` | `415 Unsupported Media Type` | High | Negative | `A7` | | | |
| `[AF300-API-15]` | `BODY-003` | `PUT /api/v1/admin/gifts/:id` | Body - JSON structure | JSON thiếu ngoặc đóng | Admin token | `'{"name":"New"'` | `400` | `400 Bad Request` | High | Negative | `A13` | | | |
| `[AF300-API-16]` | `BODY-004` | `PUT /api/v1/admin/gifts/:id` | Body - JSON structure | JSON có dấu phẩy thừa cuối | Admin token | `'{"name":"New",}'` | `400` | `400 Bad Request` | High | Negative | `A13` | | | |
| `[AF300-API-17]` | `UPD-001` | `PUT /api/v1/admin/gifts/:id` | CRUD - Update | PUT cập nhật toàn bộ trường hợp lệ | Quà ID=1 | `{ "name": "New Star", "coin_price": 250, "category_id": 2, "sort_order": 3, "status": "active" }` | `200` | Response cập nhật đủ fields; DB `updated_at` đổi mới, giá trị khớp 100% | High | Positive | - | | | Rule 07 |
| `[AF300-API-18]` | `UPD-002` | `PUT /api/v1/admin/gifts/:id` | CRUD - Update | PUT thiếu trường bắt buộc (`name`) | Quà ID=1 | `{ "coin_price": 250, "category_id": 1 }` | `400 / 422` | Báo lỗi thiếu `name`, DB giữ nguyên | High | Negative | `A2` | | | |
| `[AF300-API-19]` | `UPD-003` | `PUT /api/v1/admin/gifts/:id` | CRUD - Update | PUT ID không tồn tại | - | `PUT /gifts/999999` + valid body | `404` | `{ "code": "NOT_FOUND" }` | High | Negative | `A11` | | | |
| `[AF300-API-20]` | `UPD-004` | `PUT /api/v1/admin/gifts/:id` | CRUD - Update | `id` trong body khác `id` trên URL | Quà ID=1 & ID=2 | `PUT /gifts/1`, Body: `{ "id": 2, "name": "X", ... }` | `200 / 400` | URL ID thắng hoặc báo 400; bản ghi ID=2 tuyệt đối không bị sửa | Medium | Security | - | | | |
| `[AF300-API-21]` | `UPD-006` | `PUT /api/v1/admin/gifts/:id` | CRUD - Update | Gửi trường read-only (`created_at`) trong PUT | Quà ID=1 | `{ ..., "created_at": "1999-01-01" }` | `200` | `created_at` trong DB không bị ghi đè | Medium | Security | - | | | |
| `[AF300-API-22]` | `UPD-007` | `PUT /api/v1/admin/gifts/:id` | CRUD - Update | PUT idempotent (gửi cùng payload 3 lần) | Quà ID=1 | 3 PUT giống nhau | `200` | Cả 3 lần đều `200`, trạng thái cuối cùng nhất quán | Medium | Positive | - | | | |
| `[AF300-API-23]` | `UPD-008` | `PATCH /api/v1/admin/gifts/:id` | CRUD - Update | PATCH partial update (chỉ đổi `coin_price`) | Quà ID=1 | `{ "coin_price": 500 }` | `200` | Chỉ `coin_price` đổi thành 500, các trường khác giữ nguyên | High | Positive | - | | | |
| `[AF300-API-24]` | `UPD-009` | `PATCH /api/v1/admin/gifts/:id` | CRUD - Update | PATCH với body rỗng `{}` | Quà ID=1 | `{}` | `400` | `400 Bad Request` | Medium | Negative | `A11` | | | |
| `[AF300-API-25]` | `UPD-010` | `PATCH /api/v1/admin/gifts/:id` | CRUD - Update | PATCH giá trị sai (`coin_price = -50`) | Quà ID=1 | `{ "coin_price": -50 }` | `400 / 422` | Lỗi validation, DB giữ nguyên | High | Negative | - | | | |
| `[AF300-API-26]` | `UPD-011` | `PATCH /api/v1/admin/gifts/:id` | CRUD - Update | PATCH kèm field lạ (`unknown_field`) | Quà ID=1 | `{ "coin_price": 300, "unknown_xyz": 1 }` | `200` | `unknown_xyz` bị ignore (`A10`) | Low | Negative | `A10` | | | |
| `[AF300-API-27]` | `UPD-012` | `PATCH /api/v1/admin/gifts/:id` | CRUD - Update | PATCH ID không tồn tại | - | `PATCH /gifts/999999`, `{ "coin_price": 300 }` | `404` | `{ "code": "NOT_FOUND" }` | High | Negative | `A11` | | | |
| `[AF300-API-28]` | `UPD-013` | `PATCH /api/v1/admin/gifts/:id` | CRUD - Update | PATCH set trường bắt buộc = `null` | Quà ID=1 | `{ "name": null }` | `400 / 422` | Không cho set null vào required field | Medium | Negative | `A2` | | | |
| `[AF300-API-29]` | `UPD-014` | `PUT /api/v1/admin/gifts/:id` | CRUD - Update | Concurrent update (2 admin sửa cùng 1 quà) | Quà ID=1 | 2 PUT đồng thời | `200 / 409` | Không hỏng dữ liệu DB | Low | Boundary | - | | | |
| `[AF300-API-30]` | `CRE-005` | `PUT /api/v1/admin/gifts/:id` | Business Logic | Update `category_id` không tồn tại | Quà ID=1 | `{ ..., "category_id": 999999 }` | `400 / 404` | Lỗi khóa ngoại, không lưu | High | Negative | - | | | |
| `[AF300-API-31]` | `SEC-007` | `PUT /api/v1/admin/gifts/:id` | Security | Stored XSS trong `name` khi update | Quà ID=1 | `{ ..., "name": "<img src=x onerror=alert(1)>" }` | `200 / 400` | Lưu escaped hoặc từ chối | High | Security | `A8` | | | |
| | | | **3. DELETE /api/v1/admin/gifts/:id — XÓA QUÀ** | | | | | | | | | | | |
| `[AF300-API-32]` | `AUTH-001` | `DELETE /api/v1/admin/gifts/:id` | Header - Authorization | Thiếu Authorization | - | No `Authorization` | `401` | `{ "code": "UNAUTHORIZED" }` | High | Negative | `A9` | | | |
| `[AF300-API-33]` | `PERM-007` | `DELETE /api/v1/admin/gifts/:id` | Authorization & permission | User Read-only / Agency gọi DELETE | Monitor/Agency token | `DELETE /gifts/1` | `403` | `403 Forbidden`, quà vẫn tồn tại trong DB | High | Negative | `A10` | | | |
| `[AF300-API-34]` | `DEL-001` | `DELETE /api/v1/admin/gifts/:id` | CRUD - Delete | Xóa thành công quà hợp lệ | Quà ID=1 tồn tại | `DELETE /gifts/1` | `200 / 204` | DB: bản ghi soft-delete (`deleted_at IS NOT NULL`) | High | Positive | - | | | Rule 07 |
| `[AF300-API-35]` | `DEL-002` | `DELETE /api/v1/admin/gifts/:id` | CRUD - Delete | Gọi GET sau khi xóa | Quà ID=1 vừa xóa | `GET /gifts/1` | `404` | `{ "code": "NOT_FOUND" }` | High | Positive | - | | | |
| `[AF300-API-36]` | `DEL-003` | `DELETE /api/v1/admin/gifts/:id` | CRUD - Delete | Xóa lần 2 cùng ID đã xóa (`A12`) | Quà ID=1 đã xóa | `DELETE /gifts/1` | `404` | `{ "code": "NOT_FOUND" }` (`A12`) | Medium | Negative | `A12` | | | |
| `[AF300-API-37]` | `DEL-004` | `DELETE /api/v1/admin/gifts/:id` | CRUD - Delete | Xóa ID không tồn tại | - | `DELETE /gifts/999999` | `404` | `{ "code": "NOT_FOUND" }` | High | Negative | `A11` | | | |
| `[AF300-API-38]` | `DEL-005` | `DELETE /api/v1/admin/gifts/:id` | CRUD - Delete | Xóa ID sai định dạng (`abc`) | - | `DELETE /gifts/abc` | `400` | `{ "code": "INVALID_PARAM" }` | High | Negative | `A6` | | | |
| `[AF300-API-39]` | `DEL-006` | `DELETE /api/v1/admin/gifts/:id` | CRUD - Delete | Xóa quà đang được tham chiếu (Wishlist `M1011` / `gift_logs`) | Quà đang trong Wishlist | `DELETE /gifts/<wishlist_gift_id>` | `409 / 200` | Không tạo orphan data; báo lỗi ràng buộc hoặc tự gỡ khỏi Wishlist `[Pending Q&A #4]` | Medium | Negative | - | | | |
| `[AF300-API-40]` | `DEL-007` | `DELETE /api/v1/admin/gifts/` | CRUD - Delete | Gọi DELETE trực tiếp trên collection | Admin token | `DELETE /api/v1/admin/gifts/` | `405` | `405 Method Not Allowed`, không xóa dữ liệu | High | Security | - | | | |
| `[AF300-API-41]` | `DEL-008` | `DELETE /api/v1/admin/gifts/:id` | CRUD - Delete | Kiểm tra danh sách AF100 sau khi xóa | Quà ID=1 vừa xóa | `GET /api/v1/admin/gifts` | `200` | Quà đã xóa không xuất hiện trong list, `total` giảm đi 1 | Medium | Positive | - | | | |
