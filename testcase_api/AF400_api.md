# BẢNG KỊCH BẢN KIỂM THỬ BACKEND API (API TEST SUITE)
## Màn hình: AF400 — Gift Manage: Gift Category (ギフトカテゴリ管理)
### Nguồn Spec: Google Sheet `AF400` (gid=`993447379`) + Postman `Live2d_BE/gift/category`
### Áp dụng: `Universal_Rules/03_api_test_case_rule.md` & `API_controls/API_Viewpoint.md`

---

## 1. BÓC TÁCH THÔNG TIN CONTRACT API (API CONTRACT ANALYSIS)

| Thuộc tính Contract | Chi tiết Đặc tả Kỹ thuật |
| :--- | :--- |
| **Chức năng nghiệp vụ** | 1. `GET /gift/category/` (List)<br>2. `POST /gift/category/` (Create)<br>3. `GET /gift/category/{category_id}` (Detail)<br>4. `PUT /gift/category/{category_id}` (Update)<br>5. `DELETE /gift/category/{category_id}` (Delete — gift về `未設定`)<br>6. `PUT /gift/category/sort-order/{category_id}` (Update Sort Order) |
| **Base URL (Dev / STG)** | `https://api-admin-dev.surrealdolls.com` / `https://api-admin-stg.surrealdolls.com` |
| **Headers bắt buộc** | `Authorization: Bearer <master_admin_token>`, `Content-Type: application/json`, `Accept: application/json` |

---

## 2. BẢNG CHI TIẾT TEST CASES BACKEND API (14 CỘT CHUẨN)

| ID | VP ID | API Name / Endpoint | Group / Viewpoint Group | Test Case / Scenario | Pre-condition | Request Data / Payload | Expected HTTP Status | Expected Response Body & DB State | Priority | Test Type | Assumption | R1 | R2 | Note / Business Rule |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `[AF400-API-01]` | `AUTH-001` | `GET /gift/category/` | Header - Auth | Thiếu header `Authorization` | - | No token | `401` | Trả về `401 Unauthorized` | High | Negative | `A9` | | | |
| `[AF400-API-02]` | `AUTH-002` | `GET /gift/category/` | Header - Auth | Token sai chữ ký hoặc đã hết hạn | - | `Bearer invalid_token` | `401` | Trả về `401 Unauthorized` | High | Negative | `A9` | | | |
| `[AF400-API-03]` | `PERM-001` | `GET /gift/category/` | Header - RBAC | Role không có quyền Master Admin (VD: Agency token) | - | Agency token | `403` | Trả về `403 Forbidden` | High | Negative | `A10` | | | |
| `[AF400-API-04]` | `RESP-010` | `GET /gift/category/` | Response & DB | Lấy danh sách sort theo `sort_order`, kiểm tra `gift_count` khớp DB | Admin token | `GET /gift/category/` | `200` | `gift_count` khớp `COUNT(gifts)` chưa xóa | High | Positive | - | | | Rule 07 |
| `[AF400-API-05]` | `CRE-001` | `POST /gift/category/` | CRUD - Create | Tạo category hợp lệ (`name <= 20` ký tự), kiểm tra `sort_order` ở cuối | Admin token | `{ "name": "EventGift" }` | `201` | DB INSERT `gift_categories`, `sort_order = max + 1` | High | Positive | - | | | Spec AF400 |
| `[AF400-API-06]` | `STR-008` | `POST /gift/category/` | String (`name` max 20) | Boundary: `name` đúng 20 ký tự | Admin token | `{ "name": "12345678901234567890" }` | `201` | Tạo thành công với độ dài 20 ký tự | High | Boundary | - | | | Spec AF400 |
| `[AF400-API-07]` | `STR-009` | `POST /gift/category/` | String (`name` max 20) | Boundary: `name` vượt 21 ký tự | Admin token | `{ "name": "123456789012345678901" }` | `400` | Trả về lỗi validation max 20 ký tự | High | Boundary | `A6` | | | Spec AF400 |
| `[AF400-API-08]` | `STR-002` | `POST /gift/category/` | String (`name` whitespace) | `name` toàn khoảng trắng `"   "` | Admin token | `{ "name": "   " }` | `400` | Trả về lỗi validation không cho phép rỗng | High | Negative | `A6` | | | Spec AF400 |
| `[AF400-API-09]` | `REQ-001` | `POST /gift/category/` | Required Field | Thiếu trường bắt buộc `name` trong payload | Admin token | `{}` | `400` | Trả về lỗi thiếu trường `name` | High | Negative | `A6` | | | Spec AF400 |
| `[AF400-API-10]` | `STR-018` | `POST /gift/category/` | String (`name` unique) | Trùng tên category đã tồn tại (`[Q&A #1]`) | Đã có "EventGift" | `{ "name": "EventGift" }` | `409` | Trả về lỗi trùng tên theo `[Q&A #1]` | Medium | Negative | - | | | |
| `[AF400-API-11]` | `SEC-007` | `POST /gift/category/` | Security - XSS | Payload chứa chuỗi XSS (`<script>alert(1)</script>`) | Admin token | `{ "name": "<script>alert(1)</script>" }` | `400` | Chặn hoặc escape an toàn, không trả `500` | Medium | Security | - | | | |
| `[AF400-API-12]` | `CT-003` | `POST /gift/category/` | Header - Content-Type | Thiếu hoặc sai `Content-Type` header (`text/plain`) | Admin token | `Content-Type: text/plain` | `415` | Trả về `415 Unsupported Media Type` | High | Negative | `A7` | | | |
| `[AF400-API-13]` | `BODY-003` | `POST /gift/category/` | Body Format | JSON body lỗi cú pháp | Admin token | `'{"name":"X"'` | `400` | Trả về `400 Bad Request`, không `500` | High | Negative | `A13` | | | |
| `[AF400-API-14]` | `UPD-001` | `PUT /gift/category/{category_id}` | CRUD - Update | Cập nhật tên category hợp lệ (`<= 20` ký tự) | Category ID=1 | `{ "name": "NewCat" }` | `200` | DB cập nhật `name`, `updated_at` | High | Positive | - | | | Rule 07 |
| `[AF400-API-15]` | `REQ-002` | `PUT /gift/category/{category_id}` | Required Field | Thiếu trường `name` khi cập nhật category | Category ID=1 | `{}` | `400` | Trả về lỗi validation thiếu `name` | High | Negative | `A6` | | | |
| `[AF400-API-16]` | `STR-010` | `PUT /gift/category/{category_id}` | String (`name` max 20) | Cập nhật `name` vượt quá 20 ký tự (21 ký tự) | Category ID=1 | `{ "name": "123456789012345678901" }` | `400` | Trả về lỗi validation max 20 ký tự | High | Boundary | `A6` | | | |
| `[AF400-API-17]` | `PATH-003` | `PUT /gift/category/{category_id}` | Path Parameter | Cập nhật `category_id` không tồn tại (`999999`) | Admin token | `{ "name": "NewCat" }` | `404` | Trả về `404 Not Found` | High | Negative | `A11` | | | |
| `[AF400-API-18]` | `PATH-002` | `PUT /gift/category/{category_id}` | Path Parameter | Cập nhật với `category_id` sai kiểu dữ liệu (`abc`) | Admin token | `{ "name": "NewCat" }` | `400` | Trả về `400 Bad Request` | High | Negative | `A11` | | | |
| `[AF400-API-19]` | `BIZ-01` | `PUT /gift/category/sort-order/{category_id}` | Business Logic (Drag & Drop) | Cập nhật `sort_order` khi kéo thả icon 6 dots | Có >= 2 category | `{ "sort_order": 1 }` (theo schema Postman) | `200` | Thứ tự các category trong DB cập nhật chính xác | High | Positive | - | | | Spec AF400 + Postman |
| `[AF400-API-20]` | `INT-007` | `PUT /gift/category/sort-order/{category_id}` | Integer (`sort_order`) | `sort_order` giá trị âm (`-1`) | Category ID=1 | `{ "sort_order": -1 }` | `400` | Trả về lỗi validation số nguyên dương | High | Boundary | `A3` | | | |
| `[AF400-API-21]` | `INT-003` | `PUT /gift/category/sort-order/{category_id}` | Integer (`sort_order`) | `sort_order` sai kiểu dữ liệu (`"abc"`) | Category ID=1 | `{ "sort_order": "abc" }` | `400` | Trả về lỗi validation kiểu số nguyên | High | Negative | `A3` | | | |
| `[AF400-API-22]` | `AUTH-003` | `PUT /gift/category/sort-order/{category_id}` | Header - Auth | Thiếu token khi gọi cập nhật `sort_order` | - | No token | `401` | Trả về `401 Unauthorized` | High | Negative | `A9` | | | |
| `[AF400-API-23]` | `PATH-004` | `PUT /gift/category/sort-order/{category_id}` | Path Parameter | `category_id` không tồn tại (`999999`) khi sort-order | Admin token | `{ "sort_order": 1 }` | `404` | Trả về `404 Not Found` | High | Negative | `A11` | | | |
| `[AF400-API-24]` | `DEL-006` | `DELETE /gift/category/{category_id}` | Business Logic (Xóa có gift) | Xóa category đang chứa gift -> kiểm tra DB `gifts.category_id` | Category có >= 1 gift | `DELETE /gift/category/{id}` | `200` | Category bị xóa mềm; các gift thuộc category này có `category_id = NULL` (`未設定`) | High | Positive | - | | | Spec AF400 |
| `[AF400-API-25]` | `DEL-003` | `DELETE /gift/category/{category_id}` | CRUD - Delete | Xóa lần 2 cùng `category_id` đã bị xóa | Category đã xóa | `DELETE /gift/category/{deleted_id}` | `404` | Trả về `404 Not Found` | High | Negative | `A11` | | | |
| `[AF400-API-26]` | `PATH-005` | `DELETE /gift/category/{category_id}` | Path Parameter | Xóa `category_id` không tồn tại (`999999`) | Admin token | `DELETE /gift/category/999999` | `404` | Trả về `404 Not Found` | High | Negative | `A11` | | | |
| `[AF400-API-27]` | `PATH-006` | `DELETE /gift/category/{category_id}` | Path Parameter | Xóa `category_id` sai kiểu dữ liệu (`abc`) | Admin token | `DELETE /gift/category/abc` | `400` | Trả về `400 Bad Request` | High | Negative | `A11` | | | |
| `[AF400-API-28]` | `MTD-002` | `DELETE /gift/category/` | HTTP Method | Gọi `DELETE` lên endpoint collection không có ID | Admin token | `DELETE /gift/category/` | `405` | Trả về `405 Method Not Allowed` | Medium | Negative | `A12` | | | |
