# BẢNG KỊCH BẢN KIỂM THỬ BACKEND API (API TEST SUITE)
## Màn hình: AF300 — Gift Manage: Gift Update / Delete (ギフト更新・削除)
### Nguồn Spec: Google Sheet `AF300` (gid=`213255523`) + `AF500` + Postman `Live2d_BE/gift`
### Áp dụng: `Universal_Rules/03_api_test_case_rule.md` & `API_controls/API_Viewpoint.md`

---

## 1. BÓC TÁCH THÔNG TIN CONTRACT API (API CONTRACT ANALYSIS)

| Thuộc tính Contract | Chi tiết Đặc tả Kỹ thuật |
| :--- | :--- |
| **Chức năng nghiệp vụ** | 1. Lấy chi tiết gift (`GET /gift/{gift_id}/`)<br>2. Cập nhật gift (`PATCH /gift/{gift_id}/`)<br>3. Xóa gift (`DELETE /gift/{gift_id}/`)<br>4. Lấy & tạo category inline (`GET / POST /gift/category/`) |
| **Base URL (Dev / STG)** | `https://api-admin-dev.surrealdolls.com` / `https://api-admin-stg.surrealdolls.com` |
| **Headers bắt buộc** | `Authorization: Bearer <master_admin_token>`, `Content-Type: multipart/form-data` / `application/json`, `Accept: application/json` |

---

## 2. BẢNG CHI TIẾT TEST CASES BACKEND API (14 CỘT CHUẨN)

| ID | VP ID | API Name / Endpoint | Group / Viewpoint Group | Test Case / Scenario | Pre-condition | Request Data / Payload | Expected HTTP Status | Expected Response Body & DB State | Priority | Test Type | Assumption | R1 | R2 | Note / Business Rule |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| | | | **1. GET /gift/{gift_id}/ — CHI TIẾT GIFT** | | | | | | | | | | | |
| `[AF300-API-01]` | `AUTH-001` | `GET /gift/{gift_id}/` | Header - Authorization | Thiếu Authorization | - | No `Authorization` | `401` | `401 Unauthorized` | High | Negative | `A9` | | | |
| `[AF300-API-02]` | `AUTH-007` | `GET /gift/{gift_id}/` | Header - Authorization | Token sai/hết hạn | - | `Bearer invalid` | `401` | `401 Unauthorized` | High | Negative | `A9` | | | |
| `[AF300-API-03]` | `PERM-002` | `GET /gift/{gift_id}/` | Authorization & permission | Role không có quyền (Agency/User) | Agency token | `GET /gift/1/` | `403` | `403 Forbidden` | High | Negative | `A10` | | | |
| `[AF300-API-04]` | `PATH-001` | `GET /gift/{gift_id}/` | Path parameter | ID hợp lệ, đối chiếu 100% DB | Gift ID=1 | `GET /gift/1/` | `200` | Khớp DB: `id, name, icon, image, status, sort_order, price, category_id, animation_type` | High | Positive | - | | | Rule 07 |
| `[AF300-API-05]` | `PATH-002` | `GET /gift/{gift_id}/` | Path parameter | ID không tồn tại (`999999`) | Admin token | `GET /gift/999999/` | `404` | `404 Not Found` | High | Negative | `A11` | | | |
| `[AF300-API-06]` | `PATH-004` | `GET /gift/{gift_id}/` | Path parameter | ID âm (`-1`) | Admin token | `GET /gift/-1/` | `400` | Không lỗi 500 | High | Boundary | `A6` | | | |
| `[AF300-API-07]` | `PATH-005` | `GET /gift/{gift_id}/` | Path parameter | ID là chữ (`abc`) | Admin token | `GET /gift/abc/` | `400` | `400 Bad Request` | High | Negative | `A6` | | | |
| `[AF300-API-08]` | `PATH-011` | `GET /gift/{gift_id}/` | Path parameter | SQLi trong Path (`1%20OR%201=1`) | Admin token | `GET /gift/1%20OR%201=1/` | `400` | Không thực thi SQL | High | Security | - | | | |
| `[AF300-API-09]` | `PATH-012` | `GET /gift/{gift_id}/` | Path parameter | Gift đã bị soft-delete | Gift đã xóa | `GET /gift/<deleted_id>/` | `404` | `404 Not Found` | High | Negative | - | | | |
| `[AF300-API-10]` | `MTD-005` | `POST /gift/{gift_id}/` | HTTP method & status | Gửi `POST` lên endpoint chi tiết | Admin token | `POST /gift/1/` | `405` | `405 Method Not Allowed` | High | Negative | - | | | |
| | | | **2. PATCH /gift/{gift_id}/ — CẬP NHẬT GIFT** | | | | | | | | | | | |
| `[AF300-API-11]` | `AUTH-001` | `PATCH /gift/{gift_id}/` | Header - Authorization | Thiếu Authorization | - | No token | `401` | `401 Unauthorized` | High | Negative | `A9` | | | |
| `[AF300-API-12]` | `PERM-002` | `PATCH /gift/{gift_id}/` | Authorization & permission | Role không có quyền sửa | Monitor/Agency | Valid payload | `403` | `403 Forbidden` | High | Negative | `A10` | | | |
| `[AF300-API-13]` | `CT-003` | `PATCH /gift/{gift_id}/` | Header - Content-Type | Thiếu `Content-Type` header | Admin token | No `Content-Type` | `415` | `415 Unsupported Media Type` | High | Negative | `A7` | | | |
| `[AF300-API-14]` | `CT-005` | `PATCH /gift/{gift_id}/` | Header - Content-Type | Sai `Content-Type: text/plain` | Admin token | `text/plain` | `415` | `415 Unsupported Media Type` | High | Negative | `A7` | | | |
| `[AF300-API-15]` | `BODY-003` | `PATCH /gift/{gift_id}/` | Body structure | JSON thiếu ngoặc đóng | Admin token | `'{"name":"X"'` | `400` | `400 Bad Request` | High | Negative | `A13` | | | |
| `[AF300-API-16]` | `BODY-004` | `PATCH /gift/{gift_id}/` | Body structure | JSON trailing comma | Admin token | `'{"name":"X",}'` | `400` | `400 Bad Request` | High | Negative | `A13` | | | |
| `[AF300-API-17]` | `UPD-009` | `PATCH /gift/{gift_id}/` | CRUD - Update | PATCH body rỗng `{}` | Admin token | `{}` | `400` | `400 Bad Request` | Medium | Negative | `A11` | | | |
| `[AF300-API-18]` | `UPD-008` | `PATCH /gift/{gift_id}/` | CRUD - Partial Update | Chỉ đổi `name` & `price`, giữ nguyên `icon`/`image` cũ | Gift ID=1 | `{ "name": "NewName", "price": 500 }` | `200` | `name`/`price` đổi, `icon`/`image` cũ giữ nguyên | High | Positive | - | | | Rule 07 |
| `[AF300-API-19]` | `UPD-001` | `PATCH /gift/{gift_id}/` | CRUD - Remove Category | Set `category_id = null` chuyển về nhóm `未設定` | Gift có category | `{ "category_id": null }` | `200` | DB `category_id = NULL` (`未設定`) | High | Positive | - | | | Spec AF300 |
| `[AF300-API-20]` | `BIZ-01` | `PATCH /gift/{gift_id}/` | AF500 (`shutter`) | Cập nhật sang `shutter` với giá `5000` | Gift ID=1 | `{ "animation_type": "shutter", "price": 5000 }` | `200` | Cập nhật thành công `animation_type=shutter` | High | Positive | - | | | AF500 |
| `[AF300-API-21]` | `BIZ-02` | `PATCH /gift/{gift_id}/` | AF500 (`shutter`) | Cập nhật sang `shutter` với giá không hợp lệ (`250`) | Gift ID=1 | `{ "animation_type": "shutter", "price": 250 }` | `400` | Từ chối giá ngoài `[5000, 10000]` | High | Negative | - | | | AF500 |
| `[AF300-API-22]` | `BIZ-03` | `PATCH /gift/{gift_id}/` | AF500 (`continuous`) | Cập nhật sang `continuous` với giá `3000` | Gift ID=1 | `{ "animation_type": "continuous", "price": 3000 }` | `200` | Cập nhật thành công `animation_type=continuous` | High | Positive | - | | | AF500 |
| `[AF300-API-23]` | `BIZ-04` | `PATCH /gift/{gift_id}/` | AF500 (`continuous`) | Cập nhật sang `continuous` với giá không hợp lệ (`2000`) | Gift ID=1 | `{ "animation_type": "continuous", "price": 2000 }` | `400` | Từ chối giá ngoài `[1000, 3000, 5000, 10000]` | High | Negative | - | | | AF500 |
| `[AF300-API-24]` | `STR-008` | `PATCH /gift/{gift_id}/` | String (`name` max 10) | `name` đúng 10 ký tự UTF-8 | Gift ID=1 | `name` = 10 chars | `200` | Thành công | High | Boundary | `A6` | | | Spec AF300 |
| `[AF300-API-25]` | `STR-009` | `PATCH /gift/{gift_id}/` | String (`name` max+1 = 11) | `name` vượt 10 ký tự (11 ký tự) | Gift ID=1 | `name` = 11 chars | `400` | Lỗi vượt 10 ký tự | High | Boundary | `A6` | | | Spec AF300 |
| `[AF300-API-26]` | `UPD-013` | `PATCH /gift/{gift_id}/` | String (`name = null`) | Set `name = null` | Gift ID=1 | `{ "name": null }` | `400` | Không cho set null vào required field | High | Negative | `A2` | | | |
| `[AF300-API-27]` | `STR-001` | `PATCH /gift/{gift_id}/` | String (`name = ""`) | Set `name = ""` (rỗng) | Gift ID=1 | `{ "name": "" }` | `400` | Không cho set rỗng vào required field | High | Negative | `A2` | | | |
| `[AF300-API-28]` | `INT-007` | `PATCH /gift/{gift_id}/` | Integer (`price`) | `price = -50` (số âm) | Gift ID=1 | `{ "price": -50 }` | `400` | Lỗi validation `price >= 1` | High | Boundary | `A3` | | | |
| `[AF300-API-29]` | `INT-008` | `PATCH /gift/{gift_id}/` | Integer (`price`) | `price = 12.5` (thập phân) | Gift ID=1 | `{ "price": 12.5 }` | `400` | Lỗi validation số nguyên | High | Negative | `A3` | | | |
| `[AF300-API-30]` | `INT-009` | `PATCH /gift/{gift_id}/` | Integer (`price`) | `price = "abc"` (chữ) | Gift ID=1 | `{ "price": "abc" }` | `400` | Lỗi kiểu dữ liệu | High | Negative | `A3` | | | |
| `[AF300-API-31]` | `INT-007` | `PATCH /gift/{gift_id}/` | Integer (`sort_order`) | `sort_order = -1` (số âm) | Gift ID=1 | `{ "sort_order": -1 }` | `400` | Lỗi validation số nguyên dương | Medium | Boundary | `A3` | | | |
| `[AF300-API-32]` | `ENUM-004` | `PATCH /gift/{gift_id}/` | Enum (`status`) | Đổi `status` ngoài enum (`"UNKNOWN"`) | Gift ID=1 | `{ "status": "UNKNOWN" }` | `400` | Lỗi enum invalid | High | Negative | `A5` | | | |
| `[AF300-API-33]` | `FILE-001` | `PATCH /gift/{gift_id}/` | File upload (`icon`) | Thay `icon` hợp lệ `.png` (`<= 5MB`) | Gift ID=1 | `icon=new_icon.png` | `200` | Lưu S3 thành công, cập nhật URL icon mới | High | Positive | - | | | |
| `[AF300-API-34]` | `FILE-011` | `PATCH /gift/{gift_id}/` | File upload (`icon`) | Thay `icon` vượt quá `5MB` | Gift ID=1 | `icon > 5MB` | `413` | Từ chối (`CMMSG45`) | High | Boundary | `A8` | | | |
| `[AF300-API-35]` | `FILE-001` | `PATCH /gift/{gift_id}/` | File upload (`image`) | Thay `image` hợp lệ `.gif` / `.lottie` (`<= 5MB`) | Gift ID=1 | `image=new_anim.gif` | `200` | Lưu S3 thành công, cập nhật URL content mới | High | Positive | - | | | |
| `[AF300-API-36]` | `FILE-003` | `PATCH /gift/{gift_id}/` | File upload (`image`) | Thay `image` sai định dạng (`.mp4`) | Gift ID=1 | `image=video.mp4` | `415` | Từ chối (`CMMSG43`) | High | Negative | `A8` | | | |
| `[AF300-API-37]` | `FILE-011` | `PATCH /gift/{gift_id}/` | File upload (`image`) | Thay `image` vượt quá `5MB` | Gift ID=1 | `image > 5MB` | `413` | Từ chối (`CMMSG45`) | High | Boundary | `A8` | | | |
| `[AF300-API-38]` | `UPD-003` | `PATCH /gift/{gift_id}/` | CRUD - Update | ID không tồn tại (`999999`) | Admin token | `PATCH /gift/999999/` | `404` | `404 Not Found` | High | Negative | `A11` | | | |
| `[AF300-API-39]` | `UPD-004` | `PATCH /gift/{gift_id}/` | CRUD - Update Security | `id` trong body khác `id` trên URL (`body.id=2` trên `/gift/1/`) | Gift ID=1 & ID=2 | `{ "id": 2, "name": "X" }` | `400` | URL ID thắng hoặc báo 400; ID=2 không bị sửa | Medium | Security | - | | | |
| `[AF300-API-40]` | `SEC-007` | `PATCH /gift/{gift_id}/` | Security | Stored XSS trong `name` (`<img src=x onerror=alert(1)>`) | Gift ID=1 | XSS payload | `400` | Escape an toàn hoặc từ chối | High | Security | `A8` | | | |
| | | | **3. DELETE /gift/{gift_id}/ — XÓA GIFT** | | | | | | | | | | | |
| `[AF300-API-41]` | `AUTH-001` | `DELETE /gift/{gift_id}/` | Header - Authorization | Thiếu Authorization token | - | No token | `401` | `401 Unauthorized` | High | Negative | `A9` | | | |
| `[AF300-API-42]` | `PERM-007` | `DELETE /gift/{gift_id}/` | Authorization & permission | Role không có quyền xóa (Monitor/Agency) | Monitor/Agency | `DELETE /gift/1/` | `403` | `403 Forbidden` | High | Negative | `A10` | | | |
| `[AF300-API-43]` | `DEL-001` | `DELETE /gift/{gift_id}/` | CRUD - Delete & Soft Delete | Xóa thành công -> `GET /gift/{id}/` trả 404 -> `GET /gift/` không còn | Gift tồn tại | `DELETE /gift/{id}/` | `200` | Soft-delete trong DB; App `I600` ẩn gift | High | Positive | - | | | Rule 07 |
| `[AF300-API-44]` | `DEL-002` | `DELETE /gift/{gift_id}/` | Business Logic | Xóa gift từng có user mua vẫn giữ lịch sử mua | Gift từng được mua | `DELETE /gift/{id}/` | `200` | Lịch sử mua gift trong DB vẫn nguyên vẹn | High | Positive | - | | | Spec AF300 |
| `[AF300-API-45]` | `DEL-003` | `DELETE /gift/{gift_id}/` | CRUD - Delete Idempotency | Xóa lần 2 cùng ID đã xóa | Gift vừa xóa | `DELETE /gift/{id}/` | `404` | `404 Not Found` | Medium | Negative | `A12` | | | |
| `[AF300-API-46]` | `DEL-004` | `DELETE /gift/{gift_id}/` | CRUD - Delete | Xóa ID không tồn tại (`999999`) | Admin token | `DELETE /gift/999999/` | `404` | `404 Not Found` | High | Negative | `A11` | | | |
| `[AF300-API-47]` | `DEL-005` | `DELETE /gift/{gift_id}/` | CRUD - Delete | Xóa ID sai định dạng (`abc`) | Admin token | `DELETE /gift/abc/` | `400` | `400 Bad Request` | High | Negative | `A6` | | | |
| `[AF300-API-48]` | `DEL-007` | `DELETE /gift/` | CRUD - Delete Security | Gọi DELETE trực tiếp trên collection `/gift/` | Admin token | `DELETE /gift/` | `405` | `405 Method Not Allowed`, không xóa DB | High | Security | - | | | |
