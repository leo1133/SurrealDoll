# BẢNG KỊCH BẢN KIỂM THỬ BACKEND API (API TEST SUITE)
## Màn hình: AF200 — Gift Manage: Gift Create (ギフト登録)
### Nguồn Spec: Google Sheet `AF200` (gid=`2030636358`) + `AF500` + Postman `Live2d_BE/gift`
### Áp dụng: `Universal_Rules/03_api_test_case_rule.md` & `API_controls/API_Viewpoint.md`

---

## 1. BÓC TÁCH THÔNG TIN CONTRACT API (API CONTRACT ANALYSIS)

| Thuộc tính Contract | Chi tiết Đặc tả Kỹ thuật |
| :--- | :--- |
| **Chức năng nghiệp vụ** | 1. Tạo mới gift (`POST /gift/`)<br>2. Tạo mới category inline (`POST /gift/category/`)<br>3. Lấy danh sách category (`GET /gift/category/`) |
| **Base URL (Dev / STG)** | `https://api-admin-dev.surrealdolls.com` / `https://api-admin-stg.surrealdolls.com` |
| **Headers bắt buộc** | `Authorization: Bearer <master_admin_token>`, `Content-Type: multipart/form-data` (hoặc `application/json`), `Accept: application/json` |

---

## 2. BẢNG CHI TIẾT TEST CASES BACKEND API (14 CỘT CHUẨN)

| ID | VP ID | API Name / Endpoint | Group / Viewpoint Group | Test Case / Scenario | Pre-condition | Request Data / Payload | Expected HTTP Status | Expected Response Body & DB State | Priority | Test Type | Assumption | R1 | R2 | Note / Business Rule |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| | | | **1. POST /gift/ — AUTH, CONTENT-TYPE & BODY STRUCTURE** | | | | | | | | | | | |
| `[AF200-API-01]` | `AUTH-001` | `POST /gift/` | Header - Authorization | Thiếu Authorization | - | No `Authorization` | `401` | `401 Unauthorized` | High | Negative | `A9` | | | |
| `[AF200-API-02]` | `AUTH-007` | `POST /gift/` | Header - Authorization | Token sai định dạng JWT | - | `Bearer invalid` | `401` | `401 Unauthorized` | High | Negative | `A9` | | | |
| `[AF200-API-03]` | `AUTH-009` | `POST /gift/` | Header - Authorization | Token hết hạn | Expired token | `Bearer <expired>` | `401` | `401 Unauthorized` (`CMMSG10`) | High | Negative | `A9` | | | |
| `[AF200-API-04]` | `PERM-006` | `POST /gift/` | Authorization & permission | Role không có quyền tạo | Agency/Monitor | Valid payload | `403` | `403 Forbidden` (`CMMSG5`) | High | Negative | `A10` | | | |
| `[AF200-API-05]` | `CT-003` | `POST /gift/` | Header - Content-Type | Thiếu `Content-Type` | Admin token | No `Content-Type` | `415` | `415 Unsupported Media Type` | High | Negative | `A7` | | | |
| `[AF200-API-06]` | `CT-005` | `POST /gift/` | Header - Content-Type | Gửi `Content-Type: text/plain` | Admin token | `text/plain` | `415` | `415 Unsupported Media Type` | High | Negative | `A7` | | | |
| `[AF200-API-07]` | `BODY-002` | `POST /gift/` | Body structure | Body là plain text | Admin token | `"hello world"` | `400` | `400 Bad Request` | High | Negative | `A13` | | | |
| `[AF200-API-08]` | `BODY-003` | `POST /gift/` | Body structure | JSON thiếu ngoặc đóng | Admin token | `'{"name":"Star"'` | `400` | `400 Bad Request` | High | Negative | `A13` | | | |
| `[AF200-API-09]` | `BODY-004` | `POST /gift/` | Body structure | JSON trailing comma | Admin token | `'{"name":"Star",}'` | `400` | `400 Bad Request` | High | Negative | `A13` | | | |
| `[AF200-API-10]` | `BODY-006` | `POST /gift/` | Body structure | Empty body (không gửi body) | Admin token | `(none)` | `400` | `400 Bad Request` | High | Negative | `A13` | | | |
| `[AF200-API-11]` | `BODY-008` | `POST /gift/` | Body structure | Body = `null` | Admin token | `null` | `400` | `400 Bad Request` | Medium | Negative | `A13` | | | |
| `[AF200-API-12]` | `BODY-009` | `POST /gift/` | Body structure | Body = Array `[{...}]` | Admin token | `[{"name":"Star"}]` | `400` | `400 Bad Request` | Medium | Negative | `A13` | | | |
| | | | **2. POST /gift/ — HAPPY PATH & AF500 ANIMATION TYPE** | | | | | | | | | | | |
| `[AF200-API-13]` | `CRE-001` | `POST /gift/` | CRUD - Create (`通常演出`) | Tạo gift thường hợp lệ đầy đủ trường | Có `category_id` | `animation_type=normal, name="StarGift", price=250` + files | `201` | DB INSERT `gifts`; `GET /gift/` khớp 100% | High | Positive | - | | | Rule 07 |
| `[AF200-API-14]` | `REQ-002` | `POST /gift/` | Optional (`category_id`) | Tạo gift thường không gửi `category_id` | Admin token | Omit `category_id` | `201` | Lưu với `category_id = null` (`未設定`) | High | Positive | - | | | Spec AF200 |
| `[AF200-API-15]` | `BIZ-01` | `POST /gift/` | AF500 (`シャッター演出`) | Tạo gift `shutter` với giá `5000` | Admin token | `animation_type=shutter, price=5000` + `icon` | `201` | Tạo thành công với `price=5000`, `category_id=null` | High | Positive | - | | | AF500 |
| `[AF200-API-16]` | `BIZ-01` | `POST /gift/` | AF500 (`シャッター演出`) | Tạo gift `shutter` với giá `10000` | Admin token | `animation_type=shutter, price=10000` + `icon` | `201` | Tạo thành công với `price=10000`, `category_id=null` | High | Positive | - | | | AF500 |
| `[AF200-API-17]` | `BIZ-02` | `POST /gift/` | AF500 (`シャッター演出`) | Tạo gift `shutter` với giá ngoài `[5000, 10000]` (`250`) | Admin token | `animation_type=shutter, price=250` | `400` | Từ chối giá không hợp lệ | High | Negative | - | | | AF500 |
| `[AF200-API-18]` | `BIZ-03` | `POST /gift/` | AF500 (`継続演出`) | Tạo gift `continuous` với giá `1000` | Admin token | `animation_type=continuous, price=1000` + `icon` | `201` | Tạo thành công với `price=1000` | High | Positive | - | | | AF500 |
| `[AF200-API-19]` | `BIZ-03` | `POST /gift/` | AF500 (`継続演出`) | Tạo gift `continuous` với giá `3000` | Admin token | `animation_type=continuous, price=3000` + `icon` | `201` | Tạo thành công với `price=3000` | High | Positive | - | | | AF500 |
| `[AF200-API-20]` | `BIZ-03` | `POST /gift/` | AF500 (`継続演出`) | Tạo gift `continuous` với giá `5000` | Admin token | `animation_type=continuous, price=5000` + `icon` | `201` | Tạo thành công với `price=5000` | High | Positive | - | | | AF500 |
| `[AF200-API-21]` | `BIZ-03` | `POST /gift/` | AF500 (`継続演出`) | Tạo gift `continuous` với giá `10000` | Admin token | `animation_type=continuous, price=10000` + `icon` | `201` | Tạo thành công với `price=10000` | High | Positive | - | | | AF500 |
| `[AF200-API-22]` | `BIZ-04` | `POST /gift/` | AF500 (`継続演出`) | Tạo gift `continuous` giá ngoài list (`2000`) | Admin token | `animation_type=continuous, price=2000` | `400` | Từ chối giá không hợp lệ | High | Negative | - | | | AF500 |
| `[AF200-API-23]` | `BIZ-05` | `POST /gift/` | AF500 (`shutter`) | Gửi kèm `category_id` cho `shutter` | Admin token | `animation_type=shutter, category_id=1` | `400` | Từ chối hoặc ignore `category_id`, đảm bảo không gán category | Medium | Boundary | - | | | AF500 |
| `[AF200-API-24]` | `BIZ-06` | `POST /gift/` | AF500 (`shutter`) | Gửi kèm `image` cho `shutter` | Admin token | `animation_type=shutter, image=anim.gif` | `400` | Từ chối hoặc ignore `image` | Medium | Boundary | - | | | AF500 |
| | | | **3. POST /gift/ — REQUIRED & FIELD VALIDATION** | | | | | | | | | | | |
| `[AF200-API-25]` | `REQ-001` | `POST /gift/` | Required (`name`) | Thiếu trường bắt buộc `name` | Admin token | Omit `name` | `400` | Lỗi thiếu `name` | High | Negative | `A2` | | | |
| `[AF200-API-26]` | `REQ-002` | `POST /gift/` | Required (`price`) | Thiếu trường bắt buộc `price` | Admin token | Omit `price` | `400` | Lỗi thiếu `price` | High | Negative | `A2` | | | |
| `[AF200-API-27]` | `REQ-003` | `POST /gift/` | Required (`sort_order`) | Thiếu trường bắt buộc `sort_order` | Admin token | Omit `sort_order` | `400` | Lỗi thiếu `sort_order` | High | Negative | `A2` | | | |
| `[AF200-API-28]` | `REQ-004` | `POST /gift/` | Required (`icon`) | Thiếu file bắt buộc `icon` | Admin token | Omit `icon` | `400` | Lỗi thiếu `icon` | High | Negative | `A2` | | | |
| `[AF200-API-29]` | `REQ-005` | `POST /gift/` | Required (`image`) | Thiếu file bắt buộc `image` khi chọn `通常演出` | Admin token | `animation_type=normal`, omit `image` | `400` | Lỗi thiếu `image` | High | Negative | `A2` | | | |
| `[AF200-API-30]` | `STR-001` | `POST /gift/` | String (`name`) | `name` là chuỗi rỗng `""` | Admin token | `name=""` | `400` | Lỗi validation không được rỗng | High | Negative | `A6` | | | |
| `[AF200-API-31]` | `STR-002` | `POST /gift/` | String (`name`) | `name` toàn khoảng trắng `"   "` | Admin token | `name="   "` | `400` | Lỗi validation không được rỗng | High | Negative | `A6` | | | |
| `[AF200-API-32]` | `STR-008` | `POST /gift/` | String (`name` max 10) | `name` đúng 10 ký tự UTF-8 | Admin token | `name="あいうえおかきくけこ"` | `201` | Tạo thành công | High | Boundary | `A6` | | | Spec AF200 |
| `[AF200-API-33]` | `STR-009` | `POST /gift/` | String (`name` max+1 = 11) | `name` vượt 10 ký tự (11 ký tự) | Admin token | `name="12345678901"` | `400` | Lỗi vượt 10 ký tự | High | Boundary | `A6` | | | Spec AF200 |
| `[AF200-API-34]` | `STR-005` | `POST /gift/` | String (`name`) | `name` có space đầu/cuối (`"  Star  "`) | Admin token | `name="  Star  "` | `201` | Trim space còn `"Star"` | Medium | Boundary | `A1` | | | |
| `[AF200-API-35]` | `INT-005` | `POST /gift/` | Integer (`price`) | `price = 1` (biên Min hợp lệ) | Admin token | `price: 1` | `201` | Tạo thành công với `price = 1` | High | Boundary | - | | | |
| `[AF200-API-36]` | `INT-006` | `POST /gift/` | Integer (`price`) | `price = 0` | Admin token | `price: 0` | `400` | Lỗi `price >= 1` | High | Boundary | - | | | |
| `[AF200-API-37]` | `INT-007` | `POST /gift/` | Integer (`price`) | `price = -1` (số âm) | Admin token | `price: -1` | `400` | Lỗi số âm | High | Boundary | - | | | |
| `[AF200-API-38]` | `INT-008` | `POST /gift/` | Integer (`price`) | `price = 1.5` (thập phân) | Admin token | `price: 1.5` | `400` | Lỗi không phải số nguyên | High | Negative | `A3` | | | |
| `[AF200-API-39]` | `INT-009` | `POST /gift/` | Integer (`price`) | `price = "abc"` (chữ) | Admin token | `price: "abc"` | `400` | Lỗi kiểu dữ liệu | High | Negative | `A3` | | | |
| `[AF200-API-40]` | `INT-012` | `POST /gift/` | Integer (`price`) | `price` overflow 32-bit (`2147483648`) | Admin token | `price: 2147483648` | `400` | Không lỗi 500 | High | Boundary | - | | | |
| `[AF200-API-41]` | `INT-007` | `POST /gift/` | Integer (`sort_order`) | `sort_order = -1` (số âm) | Admin token | `sort_order: -1` | `400` | Lỗi validation `sort_order >= 0` | Medium | Boundary | `A3` | | | |
| `[AF200-API-42]` | `INT-009` | `POST /gift/` | Integer (`sort_order`) | `sort_order = "abc"` (chữ) | Admin token | `sort_order: "abc"` | `400` | Lỗi kiểu dữ liệu số nguyên | Medium | Negative | `A3` | | | |
| `[AF200-API-43]` | `CRE-005` | `POST /gift/` | Foreign Key (`category_id`) | `category_id` không tồn tại (`999999`) | Admin token | `category_id: 999999` | `404` | Lỗi FK không tồn tại (`400` hoặc `404`) | High | Negative | - | | | |
| `[AF200-API-44]` | `ENUM-001` | `POST /gift/` | Enum (`status`) | Tạo gift với `status = private` (`非公開`) | Admin token | `status: "private"` | `201` | DB lưu đúng trạng thái `private` | High | Positive | - | | | |
| `[AF200-API-45]` | `ENUM-004` | `POST /gift/` | Enum (`status`) | `status` ngoài enum (`"UNKNOWN"`) | Admin token | `status: "UNKNOWN"` | `400` | Lỗi enum invalid | High | Negative | `A5` | | | |
| `[AF200-API-46]` | `ENUM-005` | `POST /gift/` | Enum (`animation_type`) | `animation_type` ngoài enum (`"special"`) | Admin token | `animation_type: "special"` | `400` | Lỗi enum invalid | High | Negative | `A5` | | | |
| `[AF200-API-47]` | `CRE-004` | `POST /gift/` | CRUD & Security | Client gửi `id` / `created_at` read-only | Admin token | `{ "id": 999999, ... }` | `201` | Server tự sinh `id`, ignore `999999` | High | Security | - | | | |
| `[AF200-API-48]` | `SEC-001` | `POST /gift/` | Security - SQLi | SQLi trong `name` (`"'; DROP TABLE gifts;--"`) | Admin token | `name="'; DROP TABLE gifts;--"` | `400` | Sanitize an toàn, không lỗi SQL | High | Security | `A8` | | | |
| `[AF200-API-49]` | `SEC-007` | `POST /gift/` | Security - XSS | XSS trong `name` (`<script>alert(1)</script>`) | Admin token | `name="<script>alert(1)</script>"` | `400` | Chặn hoặc escape an toàn | High | Security | `A8` | | | |
| | | | **4. FILE UPLOAD (`icon` & `image`) — 5MB & FORMAT** | | | | | | | | | | | |
| `[AF200-API-50]` | `FILE-001` | `POST /gift/` | File upload (`icon`) | `icon` hợp lệ `.png` (`<= 5MB`) | Admin token | `icon=icon.png` | `201` | Lưu S3 thành công | High | Positive | - | | | Spec AF200 |
| `[AF200-API-51]` | `FILE-001` | `POST /gift/` | File upload (`icon`) | `icon` hợp lệ `.svg` hoặc `.webp` (`<= 5MB`) | Admin token | `icon=icon.webp` | `201` | Lưu S3 thành công | Medium | Positive | - | | | Spec AF200 |
| `[AF200-API-52]` | `FILE-003` | `POST /gift/` | File upload (`icon`) | `icon` sai định dạng (`.txt`, `.exe`) | Admin token | `icon=test.txt` | `415` | Từ chối (`CMMSG44`) | High | Negative | `A8` | | | |
| `[AF200-API-53]` | `FILE-007` | `POST /gift/` | File upload (`icon`) | `icon` giả mạo Magic Bytes (`malware.exe` -> `.png`) | Admin token | Spoofed `.png` | `415` | Từ chối (`CMMSG44`) | High | Security | - | | | |
| `[AF200-API-54]` | `FILE-011` | `POST /gift/` | File upload (`icon`) | `icon` dung lượng `5MB + 1 byte` | Admin token | `icon` size `> 5MB` | `413` | Từ chối (`CMMSG45`) | High | Boundary | `A8` | | | |
| `[AF200-API-55]` | `FILE-012` | `POST /gift/` | File upload (`icon`) | `icon` file rỗng `0 KB` | Admin token | 0 Byte `icon.png` | `400` | `400 Bad Request` | High | Boundary | - | | | |
| `[AF200-API-56]` | `FILE-001` | `POST /gift/` | File upload (`image`) | `image` hợp lệ `.gif` (`<= 5MB`) | Admin token | `image=anim.gif` | `201` | Lưu S3 thành công | High | Positive | - | | | Spec AF200 |
| `[AF200-API-57]` | `FILE-001` | `POST /gift/` | File upload (`image`) | `image` hợp lệ `.lottie` (JSON `<= 5MB`) | Admin token | `image=anim.json` | `201` | Lưu S3 thành công | High | Positive | - | | | Spec AF200 |
| `[AF200-API-58]` | `FILE-003` | `POST /gift/` | File upload (`image`) | `image` sai định dạng (`.jpg`, `.mp4`, `.svg`) | Admin token | `image=video.mp4` | `415` | Từ chối (`CMMSG43`) | High | Negative | `A8` | | | |
| `[AF200-API-59]` | `FILE-011` | `POST /gift/` | File upload (`image`) | `image` dung lượng `5MB + 1 byte` | Admin token | `image` size `> 5MB` | `413` | Từ chối (`CMMSG45`) | High | Boundary | `A8` | | | |
| `[AF200-API-60]` | `FILE-012` | `POST /gift/` | File upload (`image`) | `image` file rỗng `0 KB` | Admin token | 0 Byte `image.png` | `400` | `400 Bad Request` | High | Boundary | - | | | |
| `[AF200-API-61]` | `FILE-018` | `POST /gift/` | File upload Security | Path traversal filename (`../../etc/passwd.png`) | Admin token | `../../etc/passwd.png` | `400` | Strip path hoặc từ chối an toàn | High | Security | - | | | |
| | | | **5. POST /gift/category/ — TẠO CATEGORY INLINE** | | | | | | | | | | | |
| `[AF200-API-62]` | `AUTH-001` | `POST /gift/category/` | Header - Authorization | Thiếu token khi tạo category inline | - | No token | `401` | `401 Unauthorized` | High | Negative | `A9` | | | |
| `[AF200-API-63]` | `CRE-001` | `POST /gift/category/` | CRUD - Create Category | Tạo category inline hợp lệ (`name <= 20` ký tự) | Admin token | `{ "name": "EventGift" }` | `201` | DB INSERT `gift_categories` | High | Positive | - | | | Spec AF200 |
| `[AF200-API-64]` | `STR-008` | `POST /gift/category/` | String (`name` max 20) | `name` đúng 20 ký tự | Admin token | 20 chars | `201` | Tạo thành công | High | Boundary | `A6` | | | Spec AF200 |
| `[AF200-API-65]` | `STR-009` | `POST /gift/category/` | String (`name` max 20) | `name` vượt 20 ký tự (`21` ký tự) | Admin token | 21 chars | `400` | Lỗi validation max 20 ký tự | High | Boundary | `A6` | | | Spec AF200 |
| `[AF200-API-66]` | `STR-001` | `POST /gift/category/` | String (`name` empty) | `name` rỗng hoặc toàn space `"   "` | Admin token | `{ "name": "   " }` | `400` | Lỗi validation không được rỗng | High | Negative | `A6` | | | Spec AF200 |
