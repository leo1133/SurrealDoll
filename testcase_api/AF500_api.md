# BẢNG KỊCH BẢN KIỂM THỬ BACKEND API (API TEST SUITE)
## Màn hình: AF500 — GIFT Animation Type (演出種類 trên `POST /gift/`, `PATCH /gift/{gift_id}/` & `GET /gift/`)
### Nguồn Spec: Google Sheet `AF500` (gid=`1458098150`)
### Áp dụng: `Universal_Rules/03_api_test_case_rule.md` & `API_controls/API_Viewpoint.md`

---

## 1. BÓC TÁCH THÔNG TIN CONTRACT API (API CONTRACT ANALYSIS)

| Thuộc tính Contract | Chi tiết Đặc tả Kỹ thuật |
| :--- | :--- |
| **Chức năng nghiệp vụ** | Kiểm thử trường `animation_type` (`通常演出`, `シャッター演出`, `継続演出`) và các ràng buộc đi kèm trên `POST /gift/`, `PATCH /gift/{gift_id}/` và `GET /gift/` |
| **Base URL (Dev / STG)** | `https://api-admin-dev.surrealdolls.com` / `https://api-admin-stg.surrealdolls.com` |
| **Headers bắt buộc** | `Authorization: Bearer <master_admin_token>`, `Accept: application/json` |

---

## 2. BẢNG CHI TIẾT TEST CASES BACKEND API (14 CỘT CHUẨN)

| ID | VP ID | API Name / Endpoint | Group / Viewpoint Group | Test Case / Scenario | Pre-condition | Request Data / Payload | Expected HTTP Status | Expected Response Body & DB State | Priority | Test Type | Assumption | R1 | R2 | Note / Business Rule |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `[AF500-API-01]` | `AUTH-001` | `POST /gift/` | Header - Authorization | Thiếu Authorization token | - | No `Authorization` | `401` | `401 Unauthorized` | High | Negative | `A9` | | | |
| `[AF500-API-02]` | `PERM-006` | `POST /gift/` | Authorization & permission | Role không có quyền tạo gift (Monitor/Agency) | Monitor token | Valid payload | `403` | `403 Forbidden` | High | Negative | `A10` | | | |
| `[AF500-API-03]` | `CRE-001` | `POST /gift/` | `通常演出` (Normal) | Tạo gift thường (`animation_type=normal`) với giá tự do, `category_id`, `image` | Admin token | `animation_type=normal, price=350, category_id=1` + `icon` + `image` | `201` | DB lưu `animation_type=normal` | High | Positive | - | | | Spec AF500 |
| `[AF500-API-04]` | `BIZ-01` | `POST /gift/` | `シャッター演出` (Shutter) | Tạo gift `shutter` với giá `5000`, không `category_id`, không `image` | Admin token | `animation_type=shutter, price=5000` + `icon` | `201` | Tạo thành công; `category_id = null` | High | Positive | - | | | Spec AF500 |
| `[AF500-API-05]` | `BIZ-01` | `POST /gift/` | `シャッター演出` (Shutter) | Tạo gift `shutter` với giá `10000`, không `category_id`, không `image` | Admin token | `animation_type=shutter, price=10000` + `icon` | `201` | Tạo thành công; `category_id = null` | High | Positive | - | | | Spec AF500 |
| `[AF500-API-06]` | `BIZ-02` | `POST /gift/` | `シャッター演出` (Shutter) | Tạo gift `shutter` với giá `1000` (ngoài `[5000, 10000]`) | Admin token | `animation_type=shutter, price=1000` | `400` | Từ chối giá không thuộc `[5000, 10000]` | High | Negative | - | | | Spec AF500 |
| `[AF500-API-07]` | `BIZ-02` | `POST /gift/` | `シャッター演出` (Shutter) | Tạo gift `shutter` với giá `3000` (ngoài `[5000, 10000]`) | Admin token | `animation_type=shutter, price=3000` | `400` | Từ chối giá không thuộc `[5000, 10000]` | High | Negative | - | | | Spec AF500 |
| `[AF500-API-08]` | `BIZ-02` | `POST /gift/` | `シャッター演出` (Shutter) | Tạo gift `shutter` với giá `0` | Admin token | `animation_type=shutter, price=0` | `400` | Từ chối giá không hợp lệ | High | Boundary | - | | | Spec AF500 |
| `[AF500-API-09]` | `BIZ-03` | `POST /gift/` | `継続演出` (Continuous) | Tạo gift `continuous` với giá `1000` | Admin token | `animation_type=continuous, price=1000` + `icon` | `201` | Tạo thành công với `price = 1000` | High | Positive | - | | | Spec AF500 |
| `[AF500-API-10]` | `BIZ-03` | `POST /gift/` | `継続演出` (Continuous) | Tạo gift `continuous` với giá `3000` | Admin token | `animation_type=continuous, price=3000` + `icon` | `201` | Tạo thành công với `price = 3000` | High | Positive | - | | | Spec AF500 |
| `[AF500-API-11]` | `BIZ-03` | `POST /gift/` | `継続演出` (Continuous) | Tạo gift `continuous` với giá `5000` | Admin token | `animation_type=continuous, price=5000` + `icon` | `201` | Tạo thành công với `price = 5000` | High | Positive | - | | | Spec AF500 |
| `[AF500-API-12]` | `BIZ-03` | `POST /gift/` | `継続演出` (Continuous) | Tạo gift `continuous` với giá `10000` | Admin token | `animation_type=continuous, price=10000` + `icon` | `201` | Tạo thành công với `price = 10000` | High | Positive | - | | | Spec AF500 |
| `[AF500-API-13]` | `BIZ-04` | `POST /gift/` | `継続演出` (Continuous) | Tạo gift `continuous` với giá `500` (ngoài danh sách) | Admin token | `animation_type=continuous, price=500` | `400` | Từ chối giá không hợp lệ | High | Negative | - | | | Spec AF500 |
| `[AF500-API-14]` | `BIZ-04` | `POST /gift/` | `継続演出` (Continuous) | Tạo gift `continuous` với giá `2000` (ngoài danh sách) | Admin token | `animation_type=continuous, price=2000` | `400` | Từ chối giá không hợp lệ | High | Negative | - | | | Spec AF500 |
| `[AF500-API-15]` | `BIZ-05` | `POST /gift/` | `シャッター演出` | Cố tình gửi `category_id` cho `shutter` | Admin token | `animation_type=shutter, category_id=1` | `400` | Từ chối hoặc ignore `category_id` | Medium | Boundary | - | | | Spec AF500 |
| `[AF500-API-16]` | `BIZ-06` | `POST /gift/` | `シャッター演出` | Cố tình gửi `image` cho `shutter` | Admin token | `animation_type=shutter, image=anim.gif` | `400` | Từ chối hoặc ignore `image` | Medium | Boundary | - | | | Spec AF500 |
| `[AF500-API-17]` | `BIZ-07` | `POST /gift/` | `継続演出` | Cố tình gửi `category_id` cho `continuous` | Admin token | `animation_type=continuous, category_id=1` | `400` | Từ chối hoặc ignore `category_id` | Medium | Boundary | - | | | Spec AF500 |
| `[AF500-API-18]` | `ENUM-004` | `POST /gift/` | Enum (`animation_type`) | `animation_type` ngoài enum (`"special"`) | Admin token | `animation_type="special"` | `400` | Lỗi enum invalid | High | Negative | `A5` | | | |
| `[AF500-API-19]` | `ENUM-005` | `POST /gift/` | Enum (`animation_type`) | `animation_type` sai hoa/thường (`"SHUTTER"`) | Admin token | `animation_type="SHUTTER"` | `400` | Lỗi enum invalid (case-sensitive) | Medium | Boundary | `A5` | | | |
| `[AF500-API-20]` | `ENUM-001` | `GET /gift/` | Filter `animation_type` | Lọc giá trị `animation_type=normal` | Có đủ 3 loại | `?animation_type=normal` | `200` | Chỉ trả gift `normal`, mỗi item có field `animation_type` | High | Positive | - | | | Spec AF500 |
| `[AF500-API-21]` | `ENUM-002` | `GET /gift/` | Filter `animation_type` | Lọc giá trị `animation_type=shutter` | Có đủ 3 loại | `?animation_type=shutter` | `200` | Chỉ trả gift `shutter` | High | Positive | - | | | Spec AF500 |
| `[AF500-API-22]` | `ENUM-003` | `GET /gift/` | Filter `animation_type` | Lọc giá trị `animation_type=continuous` | Có đủ 3 loại | `?animation_type=continuous` | `200` | Chỉ trả gift `continuous` | High | Positive | - | | | Spec AF500 |
| `[AF500-API-23]` | `RESP-001` | `GET /gift/` | Filter `animation_type` | Không truyền `animation_type` (mặc định all) | Có đủ 3 loại | `GET /gift/` | `200` | Trả về cả 3 loại kèm đầy đủ field `animation_type` | High | Positive | - | | | Spec AF500 |
| `[AF500-API-24]` | `ENUM-004` | `GET /gift/` | Filter `animation_type` | Truyền `animation_type` ngoài enum trên `GET /gift/` | Admin token | `?animation_type=abc` | `400` | Lỗi enum invalid | Medium | Negative | `A5` | | | |
| `[AF500-API-25]` | `UPD-001` | `PATCH /gift/{gift_id}/` | Update `animation_type` | Cập nhật gift `shutter` từ `5000` -> `10000` | Gift shutter | `{ "price": 10000 }` | `200` | DB cập nhật `price = 10000` | High | Positive | - | | | |
| `[AF500-API-26]` | `BIZ-08` | `PATCH /gift/{gift_id}/` | Update `animation_type` | Cập nhật gift `shutter` sang giá ngoài `[5000, 10000]` (`3000`) | Gift shutter | `{ "price": 3000 }` | `400` | Từ chối cập nhật giá không hợp lệ | High | Negative | - | | | Spec AF500 |
