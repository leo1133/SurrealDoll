# BẢNG KỊCH BẢN KIỂM THỬ BACKEND API (API TEST SUITE)
## Màn hình: AF200 — Gift Manage: Gift Create (Tạo mới Quà tặng & Upload Asset)
### Áp dụng: Quy chuẩn Trụ cột 3 (`Universal_Rules/03_api_test_case_rule.md`) & Bộ 419 Viewpoints (`API_controls/API_Viewpoint.md`)
### Phân hệ: Web Master Admin / Quản lý Quà tặng (`AF` Module)

---

## 1. BÓC TÁCH THÔNG TIN CONTRACT API (API CONTRACT ANALYSIS)

| Thuộc tính Contract | Chi tiết Đặc tả Kỹ thuật |
| :--- | :--- |
| **Chức năng nghiệp vụ** | 1. Tạo mới quà tặng (`POST /api/v1/admin/gifts`)<br>2. Upload file Icon / Animation lên S3 (`POST /api/v1/admin/gifts/upload-asset`) |
| **Base URL (Dev / STG)** | `https://api-admin-dev.surrealdolls.com` / `https://api-admin-stg.surrealdolls.com` |
| **Headers bắt buộc** | `Authorization: Bearer <master_admin_token>`<br>`Content-Type: application/json` (POST gifts) \| `multipart/form-data` (Upload)<br>`Accept: application/json` |
| **Phân quyền RBAC** | Master Admin có quyền tạo mới. Role Read-only / Agency / Streamer bị từ chối `403 Forbidden`. |

### Cấu trúc Tham số Request:
| Tên trường (Field) | Vị trí | Kiểu dữ liệu | Bắt buộc | Ràng buộc kỹ thuật & Nghiệp vụ | Giả định áp dụng |
| :--- | :---: | :---: | :---: | :--- | :---: |
| `name` | JSON Body | `String` | Required | Tên quà tặng. Tự động trim space đầu/cuối. Max length (VD: 50/255 ký tự UTF-8). | `A1`, `A2`, `A6` |
| `coin_price` | JSON Body | `Integer` | Required | Giá quà bằng Coin (`>= 1`). Không chấp nhận số âm, float, chữ. | `A3` |
| `category_id` | JSON Body | `Integer` | Required | Khóa ngoại trỏ tới `gift_categories.id` đang tồn tại và chưa bị xóa. | `A3` |
| `sort_order` | JSON Body | `Integer` | Optional | Thứ tự hiển thị (`>= 0`). Default tự động theo Spec. | `A3` |
| `status` | JSON Body | `Enum` | Optional | `active` hoặc `inactive` (Default: `active`). | `A5` |
| `icon_url` | JSON Body | `String` | Required* | URL ảnh icon đã upload (`[Pending Q&A #3]`). | `A2` |
| `animation_url` | JSON Body | `String` | Optional | URL file animation (GIF/Lottie). | `A2` |
| `file` | Form-data (`upload`) | `File` | Required | File ảnh/animation hợp lệ (`.png`, `.jpg`, `.gif`, `.json`), `<= max_file_size`. | `A7`, `A8` |

---

## 2. MA TRẬN 419 VIEWPOINTS ĐÃ PHỦ THEO `API_controls/API_Viewpoint.md`

- **Header - Accept / Content-Type / Authorization & RBAC:** `ACC-001`, `ACC-006`, `CT-003`..`CT-009`, `AUTH-001`..`AUTH-012`, `PERM-001`, `PERM-006`, `PERM-008`
- **HTTP Method & Status:** `MTD-002`, `MTD-006`, `MTD-008`, `MTD-010`, `MTD-012`
- **Body - JSON Structure:** `BODY-001`..`BODY-015`
- **Required / Optional / Empty:** `REQ-001`..`REQ-011`
- **String (`name`):** `STR-001`..`STR-010`, `STR-012`..`STR-017`
- **Integer (`coin_price`, `category_id`, `sort_order`):** `INT-001`..`INT-019`
- **Enum (`status`):** `ENUM-001`..`ENUM-012`
- **CRUD - Create & DB Persistence:** `CRE-001`..`CRE-008`
- **Form-data & File Upload (`upload-asset`):** `FORM-001`..`FORM-005`, `FILE-001`..`FILE-019`, `FILE-023`, `FILE-024`
- **Response Validation, Security & NFR:** `RESP-001`..`RESP-017`, `SEC-004`..`SEC-008`, `NFR-005`, `NFR-006`

---

## 3. BẢNG CHI TIẾT TEST CASES BACKEND API (14 CỘT CHUẨN)

| ID | VP ID | API Name / Endpoint | Group / Viewpoint Group | Test Case / Scenario | Pre-condition | Request Data / Payload | Expected HTTP Status | Expected Response Body & DB State | Priority | Test Type | Assumption | R1 | R2 | Note / Business Rule |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| | | | **1. POST /api/v1/admin/gifts — HEADER, AUTH & METHOD** | | | | | | | | | | | |
| `[AF200-API-01]` | `AUTH-001` | `POST /api/v1/admin/gifts` | Header - Authorization | Thiếu header Authorization | - | Không gửi `Authorization`, valid body | `401` | `{ "code": "UNAUTHORIZED", "message": "CMMSG4..." }` | High | Negative | `A9` | | | |
| `[AF200-API-02]` | `AUTH-007` | `POST /api/v1/admin/gifts` | Header - Authorization | Token sai định dạng / hết hạn (`AUTH-009`) | - | `Authorization: Bearer invalid` | `401` | `{ "code": "UNAUTHORIZED" }` | High | Negative | `A9` | | | |
| `[AF200-API-03]` | `PERM-006` | `POST /api/v1/admin/gifts` | Authorization & permission | User Read-only / Agency gọi POST | Agency token | Valid body | `403` | `403 Forbidden` (`CMMSG5`), không có bản ghi mới trong DB | High | Negative | `A10` | | | |
| `[AF200-API-04]` | `PERM-008` | `POST /api/v1/admin/gifts` | Authorization & permission | Leo thang đặc quyền qua body (`"role": "admin"`) | Agency token | `{ ..., "role": "admin" }` | `403` | Bị chặn 403, không đổi quyền | High | Security | `A10` | | | |
| `[AF200-API-05]` | `CT-003` | `POST /api/v1/admin/gifts` | Header - Content-Type | Thiếu `Content-Type` | Admin token | Valid JSON body, no `Content-Type` | `415 / 400` | `415 Unsupported Media Type` | High | Negative | `A7` | | | |
| `[AF200-API-06]` | `CT-004` | `POST /api/v1/admin/gifts` | Header - Content-Type | `Content-Type` rỗng | Admin token | `Content-Type: ""` | `415 / 400` | `415 Unsupported Media Type` | High | Negative | `A7` | | | |
| `[AF200-API-07]` | `CT-005` | `POST /api/v1/admin/gifts` | Header - Content-Type | `Content-Type: text/plain` | Admin token | `Content-Type: text/plain` | `415` | `415 Unsupported Media Type` | High | Negative | `A7` | | | |
| `[AF200-API-08]` | `CT-006` | `POST /api/v1/admin/gifts` | Header - Content-Type | `Content-Type: text/xml` | Admin token | XML body + `text/xml` | `415` | `415 Unsupported Media Type` | High | Negative | `A7` | | | |
| `[AF200-API-09]` | `CT-008` | `POST /api/v1/admin/gifts` | Header - Content-Type | Header `application/json` nhưng gửi form-urlencoded | Admin token | `Content-Type: application/json`, Body: `name=Star` | `400` | `400 Bad Request` (Invalid JSON) | High | Negative | `A13` | | | |
| `[AF200-API-10]` | `CT-009` | `POST /api/v1/admin/gifts` | Header - Content-Type | `application/json; charset=utf-8` | Admin token | Valid JSON + charset | `201` | Tạo thành công | Medium | Positive | - | | | |
| `[AF200-API-11]` | `ACC-006` | `POST /api/v1/admin/gifts` | Header - Accept | `Accept: text/xml` | Admin token | `Accept: text/xml` | `406` | `406 Not Acceptable` | High | Negative | - | | | |
| `[AF200-API-12]` | `MTD-012` | `POST /api/v1/admin/gifts` | HTTP method & status | Giả mạo `X-HTTP-Method-Override: DELETE` | Admin token | Header `X-HTTP-Method-Override: DELETE` | `201` | Bị phớt lờ, thực thi đúng POST | Medium | Security | - | | | |
| | | | **2. POST /api/v1/admin/gifts — BODY JSON STRUCTURE** | | | | | | | | | | | |
| `[AF200-API-13]` | `BODY-001` | `POST /api/v1/admin/gifts` | Body - JSON structure | Valid JSON body đầy đủ các trường | Có `category_id=1` | `{ "name": "Star Gift", "coin_price": 100, "category_id": 1, "sort_order": 5, "status": "active", "icon_url": "https://..." }` | `201` | Response trả về bản ghi mới kèm `id`; DB `gifts` INSERT 1 dòng | High | Positive | - | | | |
| `[AF200-API-14]` | `BODY-002` | `POST /api/v1/admin/gifts` | Body - JSON structure | Body là plain text | Admin token | `"hello world"` | `400` | `400 Bad Request` | High | Negative | `A13` | | | |
| `[AF200-API-15]` | `BODY-003` | `POST /api/v1/admin/gifts` | Body - JSON structure | JSON thiếu ngoặc đóng | Admin token | `'{"name": "Star"'` | `400` | `400 Bad Request` (Invalid JSON) | High | Negative | `A13` | | | |
| `[AF200-API-16]` | `BODY-004` | `POST /api/v1/admin/gifts` | Body - JSON structure | JSON có dấu phẩy thừa cuối (Trailing comma) | Admin token | `'{"name": "Star",}'` | `400` | `400 Bad Request` | High | Negative | `A13` | | | |
| `[AF200-API-17]` | `BODY-005` | `POST /api/v1/admin/gifts` | Body - JSON structure | JSON dùng nháy đơn (Single quotes) | Admin token | `"{'name': 'Star'}"` | `400` | `400 Bad Request` | Medium | Negative | `A13` | | | |
| `[AF200-API-18]` | `BODY-006` | `POST /api/v1/admin/gifts` | Body - JSON structure | Empty body (không gửi body) | Admin token | Body: `(none)` | `400` | `400 Bad Request` | High | Negative | `A13` | | | |
| `[AF200-API-19]` | `BODY-008` | `POST /api/v1/admin/gifts` | Body - JSON structure | Body = `null` | Admin token | Body: `null` | `400` | `400 Bad Request` | Medium | Negative | `A13` | | | |
| `[AF200-API-20]` | `BODY-009` | `POST /api/v1/admin/gifts` | Body - JSON structure | Body = Array `[{...}]` | Admin token | `[{"name":"Star"}]` | `400` | `400 Bad Request` (Root phải là Object) | Medium | Negative | `A13` | | | |
| `[AF200-API-21]` | `BODY-012` | `POST /api/v1/admin/gifts` | Body - JSON structure | Deeply nested JSON (1000 cấp) | Admin token | `{ "a": { "b": ... } }` | `400 / 413` | Từ chối an toàn, không StackOverflow | Low | Security | - | | | |
| `[AF200-API-22]` | `BODY-013` | `POST /api/v1/admin/gifts` | Body - JSON structure | Payload quá lớn (> server limit) | Admin token | Padding string > 2MB | `413` | `413 Payload Too Large` | Medium | Boundary | - | | | |
| | | | **3. POST /api/v1/admin/gifts — REQUIRED & FIELD VALIDATION** | | | | | | | | | | | |
| `[AF200-API-23]` | `REQ-008` | `POST /api/v1/admin/gifts` | Required / optional | Thiếu từng trường bắt buộc (`name`, `coin_price`, `category_id`) | Admin token | Lần lượt bỏ 1 field bắt buộc | `400 / 422` | Error trỏ đúng field bị thiếu | High | Negative | `A2`, `A13` | | | |
| `[AF200-API-24]` | `REQ-009` | `POST /api/v1/admin/gifts` | Required / optional | Gửi object rỗng `{}` (thiếu tất cả) | Admin token | `{}` | `400 / 422` | Liệt kê tất cả required fields thiếu | High | Negative | `A13` | | | |
| `[AF200-API-25]` | `REQ-010` | `POST /api/v1/admin/gifts` | Required / optional | Tất cả required fields = `null` | Admin token | `{ "name": null, "coin_price": null, "category_id": null }` | `400 / 422` | `400 Bad Request` | High | Negative | `A13` | | | |
| `[AF200-API-26]` | `REQ-002` | `POST /api/v1/admin/gifts` | Required / optional | Bỏ qua các trường Optional (`sort_order`, `status`, `animation_url`) | Admin token | Chỉ gửi `name, coin_price, category_id, icon_url` | `201` | Tạo thành công với giá trị default | High | Positive | - | | | |
| `[AF200-API-27]` | `REQ-011` | `POST /api/v1/admin/gifts` | Required / optional | Gửi thêm trường lạ không có trong spec (`unknown_field`) | Admin token | `{ ..., "extra_xyz": 123 }` | `201` | Unknown field bị ignore (`A10`) | Medium | Boundary | `A10` | | | |
| `[AF200-API-28]` | `STR-005` | `POST /api/v1/admin/gifts` | String / text (`name`) | `name` có khoảng trắng đầu/cuối (`"  Star  "`) | Admin token | `{ ..., "name": "  Star  " }` | `201` | DB lưu `name = "Star"` (đã trim) | Medium | Boundary | `A1` | | | |
| `[AF200-API-29]` | `STR-008` | `POST /api/v1/admin/gifts` | String / text (`name`) | `name` đúng bằng `max_length` | Admin token | `name` = chuỗi `{max}` ký tự | `201` | Tạo thành công | High | Boundary | `A6` | | | |
| `[AF200-API-30]` | `STR-009` | `POST /api/v1/admin/gifts` | String / text (`name`) | `name` vượt `max_length` (`{max}+1`) | Admin token | `name` = chuỗi `{max}+1` ký tự | `400 / 422` | Lỗi vượt quá độ dài | High | Boundary | `A6` | | | |
| `[AF200-API-31]` | `STR-014` | `POST /api/v1/admin/gifts` | String / text (`name`) | `name` gửi sai kiểu (số `123` / boolean `true`) | Admin token | `{ ..., "name": 123 }` | `400 / 422` | Lỗi kiểu dữ liệu | Medium | Negative | - | | | |
| `[AF200-API-32]` | `STR-017` | `POST /api/v1/admin/gifts` | String / text (`name`) | `name` chứa XSS `<script>alert(1)</script>` | Admin token | `{ ..., "name": "<script>alert(1)</script>" }` | `201 / 400` | Lưu escaped an toàn hoặc từ chối | High | Security | `A8` | | | |
| `[AF200-API-33]` | `INT-002` | `POST /api/v1/admin/gifts` | Integer (`coin_price`) | `coin_price = 1` (Min boundary) | Admin token | `{ ..., "coin_price": 1 }` | `201` | Tạo thành công | High | Boundary | - | | | |
| `[AF200-API-34]` | `INT-006` | `POST /api/v1/admin/gifts` | Integer (`coin_price`) | `coin_price = 0` | Admin token | `{ ..., "coin_price": 0 }` | `400 / 422` | Lỗi `coin_price >= 1` (`[Pending Q&A #1]`) | High | Boundary | - | | | |
| `[AF200-API-35]` | `INT-007` | `POST /api/v1/admin/gifts` | Integer (`coin_price`) | `coin_price = -1` (Số âm) | Admin token | `{ ..., "coin_price": -1 }` | `400 / 422` | Lỗi validation số âm | High | Boundary | - | | | |
| `[AF200-API-36]` | `INT-008` | `POST /api/v1/admin/gifts` | Integer (`coin_price`) | `coin_price = 1.5` (Số thập phân) | Admin token | `{ ..., "coin_price": 1.5 }` | `400 / 422` | Lỗi không phải số nguyên | High | Negative | `A3` | | | |
| `[AF200-API-37]` | `INT-009` | `POST /api/v1/admin/gifts` | Integer (`coin_price`) | `coin_price = "abc"` (Chuỗi chữ) | Admin token | `{ ..., "coin_price": "abc" }` | `400 / 422` | Lỗi kiểu dữ liệu | High | Negative | `A3` | | | |
| `[AF200-API-38]` | `INT-012` | `POST /api/v1/admin/gifts` | Integer (`coin_price`) | `coin_price` overflow 32-bit (`2147483648`) | Admin token | `{ ..., "coin_price": 2147483648 }` | `400 / 422` | Không lỗi 500 | High | Boundary | - | | | |
| `[AF200-API-39]` | `ENUM-004` | `POST /api/v1/admin/gifts` | Enum (`status`) | `status` giá trị ngoài enum (`"PENDING"`) | Admin token | `{ ..., "status": "PENDING" }` | `400` | Lỗi enum invalid | High | Negative | `A5` | | | |
| `[AF200-API-40]` | `ENUM-006` | `POST /api/v1/admin/gifts` | Enum (`status`) | `status` sai hoa/thường (`"ACTIVE"`) | Admin token | `{ ..., "status": "ACTIVE" }` | `400` | Enum case-sensitive (`A2`) | Medium | Negative | `A2` | | | |
| | | | **4. POST /api/v1/admin/gifts — CRUD, DB PERSISTENCE & SECURITY** | | | | | | | | | | | |
| `[AF200-API-41]` | `CRE-002` | `POST /api/v1/admin/gifts` | CRUD - Create | Record persisted (Verify qua GET & DB) | Admin token | Tạo thành công -> Gọi `GET /gifts/:new_id` | `200` | Dữ liệu GET & DB khớp 100% payload đã POST | High | Positive | - | | | Rule 07 |
| `[AF200-API-42]` | `CRE-003` | `POST /api/v1/admin/gifts` | CRUD - Create | Trường server tự sinh (`id, created_at, updated_at`) | Admin token | POST hợp lệ | `201` | Server tự gán `id, created_at, updated_at` chuẩn UTC/JST | Medium | Positive | - | | | |
| `[AF200-API-43]` | `CRE-004` | `POST /api/v1/admin/gifts` | CRUD - Create | Client cố gửi trường read-only (`id: 999, created_at`) | Admin token | `{ "id": 999, "created_at": "2000-01-01", ... }` | `201` | Server bỏ qua `id` và `created_at` client gửi lên | High | Security | - | | | |
| `[AF200-API-44]` | `CRE-005` | `POST /api/v1/admin/gifts` | CRUD - Create | Khóa ngoại `category_id` không tồn tại / đã bị xóa | Admin token | `{ ..., "category_id": 999999 }` | `400 / 404 / 422` | Lỗi FK không tồn tại; DB không tạo bản ghi rác | High | Negative | - | | | |
| `[AF200-API-45]` | `CRE-007` | `POST /api/v1/admin/gifts` | CRUD - Create | Double submit (2 POST giống nhau trong < 500ms) | Admin token | 2 concurrent POST requests | `201 / 409` | Đảm bảo không lỗi 500; xử lý idempotent theo Spec | Medium | Boundary | - | | | |
| `[AF200-API-46]` | `SEC-004` | `POST /api/v1/admin/gifts` | Security | SQL Injection trong body `name` | Admin token | `{ "name": "'; DROP TABLE gifts;--" }` | `201 / 400` | Bảng `gifts` nguyên vẹn, không thực thi SQL | High | Security | `A8` | | | |
| `[AF200-API-47]` | `SEC-008` | `POST /api/v1/admin/gifts` | Security | Mass Assignment (`is_deleted=true`, `deleted_at`) | Admin token | `{ ..., "is_deleted": true }` | `201` | Các trường nội bộ bị bỏ qua, bản ghi mới vẫn active | High | Security | - | | | |
| | | | **5. POST /api/v1/admin/gifts/upload-asset — FILE UPLOAD (24 VIEWPOINTS)** | | | | | | | | | | | |
| `[AF200-API-48]` | `AUTH-001` | `POST /api/v1/admin/gifts/upload-asset` | Header - Authorization | Thiếu Authorization khi upload | - | `file=icon.png`, no `Authorization` | `401` | `{ "code": "UNAUTHORIZED" }` | High | Negative | `A9` | | | |
| `[AF200-API-49]` | `FORM-001` | `POST /api/v1/admin/gifts/upload-asset` | Body - form-data | Gửi `application/json` thay vì `multipart/form-data` | Admin token | `Content-Type: application/json`, `{}` | `415` | `415 Unsupported Media Type` | High | Negative | `A7` | | | |
| `[AF200-API-50]` | `FORM-003` | `POST /api/v1/admin/gifts/upload-asset` | Body - form-data | Multipart rỗng (không có part nào) | Admin token | Empty multipart | `400` | `400 Bad Request` (`file is required`) | High | Negative | - | | | |
| `[AF200-API-51]` | `FILE-001` | `POST /api/v1/admin/gifts/upload-asset` | File upload | Upload PNG / GIF / Lottie JSON hợp lệ | Admin token | `file=gift_icon.png` (<= max size) | `200 / 201` | Trả về S3 URL hợp lệ (`CMR10`) | High | Positive | - | | | |
| `[AF200-API-52]` | `FILE-002` | `POST /api/v1/admin/gifts/upload-asset` | File upload | Gửi field `file` dạng text thay vì binary file | Admin token | `file="abc"` (text part) | `400` | `400 Bad Request` | High | Negative | - | | | |
| `[AF200-API-53]` | `FILE-003` | `POST /api/v1/admin/gifts/upload-asset` | File upload | Đuôi file cấm (`.exe`, `.php`, `.txt`, `.mp4`) | Admin token | `file=malware.exe` | `415 / 400` | Từ chối upload, không lưu trên S3 | High | Negative | `A8` | | | |
| `[AF200-API-54]` | `FILE-004` | `POST /api/v1/admin/gifts/upload-asset` | File upload | Đuôi file viết hoa (`ICON.PNG`) | Admin token | `file=ICON.PNG` | `200 / 201` | Kiểm tra extension case-insensitive | Medium | Boundary | - | | | |
| `[AF200-API-55]` | `FILE-005` | `POST /api/v1/admin/gifts/upload-asset` | File upload | File không có đuôi (`test`) | Admin token | `file=test` | `415 / 400` | Từ chối upload | Medium | Boundary | `A8` | | | |
| `[AF200-API-56]` | `FILE-006` | `POST /api/v1/admin/gifts/upload-asset` | File upload | Double extension (`shell.php.png`) | Admin token | `file=shell.php.png` | `400 / 201` | Từ chối hoặc sanitize an toàn, không thể thực thi | High | Security | - | | | |
| `[AF200-API-57]` | `FILE-007` | `POST /api/v1/admin/gifts/upload-asset` | File upload | Giả mạo đuôi file (Magic Bytes spoofing) | Admin token | Đổi `malware.exe` -> `fake.png` | `415 / 400` | Kiểm tra magic bytes thực tế, từ chối | High | Security | - | | | |
| `[AF200-API-58]` | `FILE-008` | `POST /api/v1/admin/gifts/upload-asset` | File upload | Sai Content-Type trong part header (`image/png` cho file PDF) | Admin token | Part header `image/png`, content PDF | `415 / 400` | Từ chối do mismatch nội dung | Medium | Security | - | | | |
| `[AF200-API-59]` | `FILE-010` | `POST /api/v1/admin/gifts/upload-asset` | File upload | Dung lượng đúng bằng `max_file_size` | Admin token | File size = `{max}` | `200 / 201` | Upload thành công | High | Boundary | - | | | |
| `[AF200-API-60]` | `FILE-011` | `POST /api/v1/admin/gifts/upload-asset` | File upload | Dung lượng `max_file_size + 1 byte` | Admin token | File size = `{max} + 1 byte` | `413 / 400` | `413 Payload Too Large` (`CMMSG45`), không lưu | High | Boundary | `A8` | | | |
| `[AF200-API-61]` | `FILE-012` | `POST /api/v1/admin/gifts/upload-asset` | File upload | File rỗng `0 KB` | Admin token | Empty file (0 byte) | `400` | `400 Bad Request` | High | Boundary | - | | | |
| `[AF200-API-62]` | `FILE-013` | `POST /api/v1/admin/gifts/upload-asset` | File upload | File bị hỏng (Corrupted PNG header) | Admin token | Truncated PNG bytes | `400 / 415` | Từ chối file lỗi | Medium | Negative | - | | | |
| `[AF200-API-63]` | `FILE-015` | `POST /api/v1/admin/gifts/upload-asset` | File upload | Tên file quá dài (`256+` ký tự) | Admin token | Filename 260 chars `.png` | `400 / 201` | Cắt gọn tên an toàn hoặc báo 400, không 500 | Medium | Boundary | - | | | |
| `[AF200-API-64]` | `FILE-016` | `POST /api/v1/admin/gifts/upload-asset` | File upload | Tên file chứa ký tự đặc biệt (`icon @#$.png`) | Admin token | `file="icon @#$.png"` | `201 / 400` | Sanitize tên file an toàn | Medium | Boundary | - | | | |
| `[AF200-API-65]` | `FILE-018` | `POST /api/v1/admin/gifts/upload-asset` | File upload | Path traversal trong tên file (`../../etc/passwd.png`) | Admin token | `filename="../../etc/passwd.png"` | `201 / 400` | Strip path, không ghi ra ngoài thư mục upload | High | Security | - | | | |
| `[AF200-API-66]` | `FILE-024` | `POST /api/v1/admin/gifts/upload-asset` | File upload | Truy xuất lại file vừa upload qua URL trả về | Upload thành công | `GET <returned_url>` | `200` | Tải được file, hash khớp 100% file gốc | High | Positive | - | | | |
