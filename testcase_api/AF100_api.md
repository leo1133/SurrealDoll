# BẢNG KỊCH BẢN KIỂM THỬ BACKEND API (API TEST SUITE)
## Màn hình: AF100 — Gift Manage: Gift List (ギフト一覧)
### Nguồn Spec: Google Sheet `AF100` (gid=`217442794`) + `AF500` + Postman `Live2d_BE/gift`
### Áp dụng: `Universal_Rules/03_api_test_case_rule.md` & `API_controls/API_Viewpoint.md`

---

## 1. BÓC TÁCH THÔNG TIN CONTRACT API (API CONTRACT ANALYSIS)

| Thuộc tính Contract | Chi tiết Đặc tả Kỹ thuật |
| :--- | :--- |
| **Chức năng nghiệp vụ** | 1. Lấy danh sách & tìm kiếm/lọc gift (`GET /gift/`)<br>2. Xóa gift (`DELETE /gift/{gift_id}/`)<br>3. Lấy danh sách category cho dropdown (`GET /gift/category/`) |
| **Base URL (Dev / STG)** | `https://api-admin-dev.surrealdolls.com` / `https://api-admin-stg.surrealdolls.com` |
| **Headers bắt buộc** | `Authorization: Bearer <master_admin_token>`, `Accept: application/json` |
| **Phân quyền RBAC** | Master Admin có quyền Gift Manage. Agency/Streamer/User bị từ chối `403 Forbidden`. |

### Cấu trúc Tham số Request (`GET /gift/`):
| Tên trường (Field) | Vị trí | Kiểu dữ liệu | Bắt buộc | Ràng buộc kỹ thuật & Nghiệp vụ | Giả định áp dụng |
| :--- | :---: | :---: | :---: | :--- | :---: |
| `keyword` | Query | `String` | Optional | Partial match `name`; Exact match `id` hoặc `price`. | `A1`, `A8` |
| `category` / `category_id` | Query | `Integer` | Optional | ID danh mục (`>= 1`). Omit = `全てカテゴリー`. | `A3` |
| `status` | Query | `Enum` | Optional | `public` (`公開`) / `private` (`非公開`). Omit = `全てステータス`. | `A5` |
| `animation_type` | Query | `Enum` | Optional | `normal` (`通常演出`), `shutter` (`シャッター演出`), `continuous` (`継続演出`) từ `AF500`. | `A5` |
| `page` | Query | `Integer` | Optional | Default `1` (`>= 1`). | `A3`, `A13` |
| `items_per_page` | Query | `Integer` | Optional | Default `10` (`CMR01`). | `A3`, `A4` |
| `sort` / `order` | Query | `String` | Optional | Sort `price` (`asc` / `desc`), mặc định sort `id`. | `A2`, `A8` |

---

## 2. MA TRẬN VIEWPOINTS ĐÃ PHỦ THEO `API_controls/API_Viewpoint.md`

- **Header, Auth & RBAC:** `HDR-001`, `ACC-001`, `ACC-006`, `AUTH-001`, `AUTH-007`, `AUTH-008`, `AUTH-009`, `PERM-002`
- **HTTP Method & Query Keys:** `MTD-002`, `MTD-004`, `MTD-006`, `KEY-002`, `KEY-005`
- **String (`keyword`), Integer (`category`), Enum (`status`, `animation_type`):** `STR-001`..`STR-025`, `INT-001`..`INT-012`, `ENUM-001`..`ENUM-004`
- **Pagination, Sorting & Delete (`DELETE /gift/{gift_id}/`):** `LIM-001`..`LIM-010`, `PAGE-001`..`PAGE-008`, `SORT-001`..`SORT-006`, `PATH-001`..`PATH-005`, `DEL-001`..`DEL-004`
- **Response, Security & NFR:** `RESP-001`, `RESP-010`, `SEC-001`, `SEC-007`, `NFR-001`

---

## 3. BẢNG CHI TIẾT TEST CASES BACKEND API (14 CỘT CHUẨN)

| ID | VP ID | API Name / Endpoint | Group / Viewpoint Group | Test Case / Scenario | Pre-condition | Request Data / Payload | Expected HTTP Status | Expected Response Body & DB State | Priority | Test Type | Assumption | R1 | R2 | Note / Business Rule |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| | | | **1. GET /gift/ — HEADER, AUTH & METHOD** | | | | | | | | | | | |
| `[AF100-API-01]` | `HDR-001` | `GET /gift/` | Header - general | Không kèm bất kỳ Header nào | - | `Headers: {}` | `401` | `{ "detail": "Not authenticated" }` (`CMMSG4`) | High | Negative | `A9` | | | |
| `[AF100-API-02]` | `ACC-001` | `GET /gift/` | Header - Accept | Truyền `Accept: application/json` hợp lệ | Admin token | `Accept: application/json` | `200` | Trả về JSON danh sách gift | High | Positive | - | | | |
| `[AF100-API-03]` | `ACC-006` | `GET /gift/` | Header - Accept | `Accept: text/xml` không hỗ trợ | Admin token | `Accept: text/xml` | `406` | Không lỗi 500, từ chối hoặc fallback JSON | Medium | Negative | `A13` | | | |
| `[AF100-API-04]` | `AUTH-001` | `GET /gift/` | Header - Authorization | Thiếu header Authorization | - | No `Authorization` | `401` | `401 Unauthorized` | High | Negative | `A9` | | | |
| `[AF100-API-05]` | `AUTH-007` | `GET /gift/` | Header - Authorization | Token sai định dạng JWT | - | `Bearer invalid_format` | `401` | `401 Unauthorized` | High | Negative | `A9` | | | |
| `[AF100-API-06]` | `AUTH-009` | `GET /gift/` | Header - Authorization | Token đã hết hạn (Expired) | Expired token | `Bearer <expired_token>` | `401` | `401 Unauthorized` (`CMMSG10`) | High | Negative | `A9` | | | |
| `[AF100-API-07]` | `AUTH-008` | `GET /gift/` | Header - Authorization | Token bị sửa chữ ký (Tampered) | - | `Bearer <tampered>` | `401` | `401 Unauthorized` | High | Security | `A9` | | | |
| `[AF100-API-08]` | `PERM-002` | `GET /gift/` | Authorization & permission | Agency / Streamer / User gọi API Admin | Agency token | `GET /gift/` | `403` | `403 Forbidden` (`CMMSG5`) | High | Negative | `A10` | | | |
| `[AF100-API-09]` | `MTD-002` | `PUT /gift/` | HTTP method & status | Gửi `PUT` lên endpoint danh sách `/gift/` | Admin token | `PUT /gift/` | `405` | `405 Method Not Allowed` | High | Security | - | | | |
| `[AF100-API-10]` | `MTD-004` | `PATCH /gift/` | HTTP method & status | Gửi `PATCH` lên endpoint danh sách `/gift/` | Admin token | `PATCH /gift/` | `405` | `405 Method Not Allowed` | High | Security | - | | | |
| `[AF100-API-11]` | `MTD-006` | `DELETE /gift/` | HTTP method & status | Gửi `DELETE` lên endpoint danh sách `/gift/` | Admin token | `DELETE /gift/` | `405` | `405 Method Not Allowed`, không xóa DB | High | Security | - | | | |
| | | | **2. GET /gift/ — SEARCH (`keyword`), CATEGORY, STATUS & ANIMATION TYPE** | | | | | | | | | | | |
| `[AF100-API-12]` | `KEY-002` | `GET /gift/` | Key / parameter name | Query key sai chính tả (`?keywordx=Heart`) | Admin token | `?keywordx=Heart` | `200` | Bỏ qua param lạ, trả danh sách mặc định | Medium | Negative | `A1` | | | |
| `[AF100-API-13]` | `KEY-005` | `GET /gift/` | Key / parameter name | Truyền trùng key (`?status=public&status=private`) | Admin token | `?status=public&status=private` | `200` | Xử lý nhất quán, không lỗi 500 | Low | Boundary | `A13` | | | |
| `[AF100-API-14]` | `STR-001` | `GET /gift/` | String (`keyword`) | `keyword` rỗng (`?keyword=`) | Admin token | `?keyword=` | `200` | Trả về toàn bộ danh sách mặc định | Medium | Boundary | - | | | |
| `[AF100-API-15]` | `STR-021` | `GET /gift/` | String (`keyword`) | Partial match theo `name` | Có quà "Heart" | `?keyword=Ear` | `200` | Trả về các quà có `name` chứa `Ear` | High | Positive | - | | | |
| `[AF100-API-16]` | `STR-002` | `GET /gift/` | String (`keyword`) | Exact match theo `id` | Có quà ID=15 | `?keyword=15` | `200` | Trả về đúng quà có `id = 15` | High | Positive | - | | | |
| `[AF100-API-17]` | `STR-003` | `GET /gift/` | String (`keyword`) | Exact match theo `price` | Có quà price=5000 | `?keyword=5000` | `200` | Trả về các quà có `price = 5000` | High | Positive | - | | | |
| `[AF100-API-18]` | `STR-005` | `GET /gift/` | String (`keyword`) | Khoảng trắng đầu/cuối (`"  Heart  "`) | Có quà "Heart" | `?keyword=%20%20Heart%20%20` | `200` | Tự động trim space, trả về quà "Heart" | Medium | Boundary | `A1` | | | |
| `[AF100-API-19]` | `STR-010` | `GET /gift/` | String (`keyword`) | Ký tự tiếng Nhật UTF-8 (`ハート`) | Có quà "ハート" | `?keyword=ハート` | `200` | Khớp chính xác UTF-8 | Medium | Positive | - | | | |
| `[AF100-API-20]` | `STR-015` | `GET /gift/` | String (`keyword`) | Ký tự wildcard SQL LIKE (`%` và `_`) | Admin token | `?keyword=%25` | `200` | Escape wildcard an toàn, không trả toàn bộ bảng | Medium | Security | `A8` | | | |
| `[AF100-API-21]` | `STR-020` | `GET /gift/` | String (`keyword`) | Không khớp bản ghi nào | Admin token | `?keyword=ZZZZ999` | `200` | `{ total_count: 0, has_more: false, data: [] }` | High | Boundary | - | | | |
| `[AF100-API-22]` | `INT-001` | `GET /gift/` | Integer (`category`) | Lọc theo `category` hợp lệ (`category=1`) | Có category ID=1 | `?category=1` | `200` | Chỉ trả quà thuộc `category_id=1` | High | Positive | - | | | |
| `[AF100-API-23]` | `INT-006` | `GET /gift/` | Integer (`category`) | `category = 0` | Admin token | `?category=0` | `400` | Trả về lỗi validation `category >= 1` | Medium | Boundary | `A3` | | | |
| `[AF100-API-24]` | `INT-007` | `GET /gift/` | Integer (`category`) | `category` âm (`-1`) | Admin token | `?category=-1` | `400` | `400 Bad Request` / `422` | High | Negative | `A3` | | | |
| `[AF100-API-25]` | `INT-009` | `GET /gift/` | Integer (`category`) | `category` là chữ (`abc`) | Admin token | `?category=abc` | `400` | `400 Bad Request` / `422` | High | Negative | `A3` | | | |
| `[AF100-API-26]` | `INT-011` | `GET /gift/` | Integer (`category`) | `category` không tồn tại (`999999`) | Admin token | `?category=999999` | `200` | Trả danh sách rỗng `data: []`, `total_count: 0` | Medium | Boundary | - | | | |
| `[AF100-API-27]` | `ENUM-001` | `GET /gift/` | Enum (`status`) | Lọc `status = public` (`公開`) | Có quà `公開` | `?status=public` | `200` | Chỉ trả quà `公開` khớp DB | High | Positive | - | | | |
| `[AF100-API-28]` | `ENUM-002` | `GET /gift/` | Enum (`status`) | Lọc `status = private` (`非公開`) | Có quà `非公開` | `?status=private` | `200` | Chỉ trả quà `非公開` khớp DB | High | Positive | - | | | |
| `[AF100-API-29]` | `ENUM-004` | `GET /gift/` | Enum (`status`) | `status` ngoài enum (`unknown`) | Admin token | `?status=unknown` | `400` | Lỗi enum invalid | High | Negative | `A5` | | | |
| `[AF100-API-30]` | `ENUM-001` | `GET /gift/` | Enum (`animation_type` - AF500) | Lọc `animation_type = normal` (`通常演出`) | Có dữ liệu | `?animation_type=normal` | `200` | Chỉ trả gift `通常演出` | High | Positive | - | | | AF500 |
| `[AF100-API-31]` | `ENUM-002` | `GET /gift/` | Enum (`animation_type` - AF500) | Lọc `animation_type = shutter` (`シャッター演出`) | Có dữ liệu | `?animation_type=shutter` | `200` | Chỉ trả gift `シャッター演出` | High | Positive | - | | | AF500 |
| `[AF100-API-32]` | `ENUM-003` | `GET /gift/` | Enum (`animation_type` - AF500) | Lọc `animation_type = continuous` (`継続演出`) | Có dữ liệu | `?animation_type=continuous` | `200` | Chỉ trả gift `継続演出` | High | Positive | - | | | AF500 |
| `[AF100-API-33]` | `ENUM-004` | `GET /gift/` | Enum (`animation_type` - AF500) | `animation_type` ngoài enum (`invalid_type`) | Admin token | `?animation_type=invalid_type` | `400` | Lỗi enum invalid | High | Negative | `A5` | | | AF500 |
| `[AF100-API-34]` | `RESP-005` | `GET /gift/` | Combined Filters | Lọc AND kết hợp `keyword` + `category` + `status` + `animation_type` | Có dữ liệu khớp | `?keyword=Star&category=1&status=public&animation_type=normal` | `200` | Trả về đúng bản ghi thỏa mãn đồng thời 4 điều kiện | High | Positive | - | | | |
| | | | **3. GET /gift/ — PAGINATION, SORTING, SECURITY & DB** | | | | | | | | | | | |
| `[AF100-API-35]` | `LIM-001` | `GET /gift/` | Pagination (`items_per_page`) | Default `page=1, items_per_page=10` | Admin token | `GET /gift/` | `200` | Trả `total_count, has_more, page: 1, items_per_page: 10` | High | Positive | `A13` | | | |
| `[AF100-API-36]` | `LIM-003` | `GET /gift/` | Pagination (`items_per_page`) | `items_per_page = -1` | Admin token | `?items_per_page=-1` | `400` | Lỗi validation `items_per_page >= 1` | High | Boundary | - | | | |
| `[AF100-API-37]` | `LIM-004` | `GET /gift/` | Pagination (`items_per_page`) | `items_per_page = 0` | Admin token | `?items_per_page=0` | `400` | Lỗi validation `items_per_page >= 1` | High | Boundary | - | | | |
| `[AF100-API-38]` | `LIM-005` | `GET /gift/` | Pagination (`items_per_page`) | `items_per_page` là chữ (`abc`) | Admin token | `?items_per_page=abc` | `400` | Lỗi validation kiểu số nguyên | High | Negative | `A3` | | | |
| `[AF100-API-39]` | `LIM-008` | `GET /gift/` | Pagination (`items_per_page`) | `items_per_page` vượt quá giới hạn max (`1000`) | Admin token | `?items_per_page=1000` | `400` | Từ chối hoặc giới hạn về max cho phép, không OOM | Medium | Boundary | `A4` | | | |
| `[AF100-API-40]` | `PAGE-001` | `GET /gift/` | Pagination (`page`) | `page = 0` | Admin token | `?page=0` | `400` | Lỗi validation `page >= 1` | High | Boundary | - | | | |
| `[AF100-API-41]` | `PAGE-002` | `GET /gift/` | Pagination (`page`) | `page = -1` | Admin token | `?page=-1` | `400` | Lỗi validation `page >= 1` | High | Boundary | - | | | |
| `[AF100-API-42]` | `PAGE-003` | `GET /gift/` | Pagination (`page`) | Trang 1 & Trang 2 không trùng/sót bản ghi | Có >= 11 gift | `?page=1` & `?page=2` | `200` | Trang 1 và Trang 2 không trùng ID, đủ tổng số lượng | High | Positive | - | | | |
| `[AF100-API-43]` | `PAGE-005` | `GET /gift/` | Pagination (`page`) | `page` là chữ (`abc`) | Admin token | `?page=abc` | `400` | Lỗi validation kiểu số nguyên | High | Negative | `A3` | | | |
| `[AF100-API-44]` | `PAGE-007` | `GET /gift/` | Pagination (`page`) | `page` vượt tổng số trang (`99999`) | Admin token | `?page=99999` | `200` | Trả về `data: []`, `has_more: false` | Medium | Boundary | - | | | |
| `[AF100-API-45]` | `SORT-001` | `GET /gift/` | Sorting | Sort `price` tăng dần (`asc`) | Có >= 2 gift khác giá | `?sort=price&order=asc` | `200` | Danh sách sắp xếp giá từ thấp đến cao | High | Positive | - | | | |
| `[AF100-API-46]` | `SORT-002` | `GET /gift/` | Sorting | Sort `price` giảm dần (`desc`) | Có >= 2 gift khác giá | `?sort=price&order=desc` | `200` | Danh sách sắp xếp giá từ cao xuống thấp | High | Positive | - | | | |
| `[AF100-API-47]` | `SORT-004` | `GET /gift/` | Sorting | Truyền tên cột sort không hợp lệ (`?sort=unknown_col`) | Admin token | `?sort=unknown_col` | `400` | Từ chối cột sort ngoài whitelist, không lỗi 500 | Medium | Negative | - | | | |
| `[AF100-API-48]` | `SORT-005` | `GET /gift/` | Sorting Security | SQLi trong tham số `sort` | Admin token | `?sort=price;DROP TABLE gifts` | `400` | Chặn SQLi an toàn, không 500 | High | Security | - | | | |
| `[AF100-API-49]` | `SEC-001` | `GET /gift/` | Security | SQLi trong `keyword` (`' OR 1=1 --`) | Admin token | `?keyword=' OR 1=1 --` | `200` | Sanitize an toàn, không trả toàn bộ bảng hay lỗi SQL | High | Security | `A8` | | | |
| `[AF100-API-50]` | `SEC-007` | `GET /gift/` | Security | XSS trong `keyword` (`<script>alert(1)</script>`) | Admin token | `?keyword=<script>alert(1)</script>` | `200` | Escape/xử lý an toàn, không lỗi 500 | High | Security | `A8` | | | |
| `[AF100-API-51]` | `RESP-010` | `GET /gift/` | Response & DB | Đối soát `total_count` & tất cả field từng item với DB | Admin token | `GET /gift/` | `200` | Khớp 100% DB `gifts` (`deleted_at IS NULL`) | High | Positive | - | | | Rule 07 |
| `[AF100-API-52]` | `NFR-001` | `GET /gift/` | Performance | Thời gian phản hồi danh sách (`<= 1000ms`) | Có >= 100 gift | `GET /gift/` | `200` | Latency `< 1000ms` | Medium | Performance | - | | | |
| | | | **4. DELETE /gift/{gift_id}/ — XÓA GIFT** | | | | | | | | | | | |
| `[AF100-API-53]` | `AUTH-001` | `DELETE /gift/{gift_id}/` | Header - Authorization | Thiếu header Authorization | - | No token | `401` | `401 Unauthorized` | High | Negative | `A9` | | | |
| `[AF100-API-54]` | `AUTH-007` | `DELETE /gift/{gift_id}/` | Header - Authorization | Token sai/hết hạn | - | `Bearer invalid` | `401` | `401 Unauthorized` | High | Negative | `A9` | | | |
| `[AF100-API-55]` | `PERM-007` | `DELETE /gift/{gift_id}/` | Authorization & permission | Role không có quyền xóa (Monitor/Agency) | Monitor/Agency | `DELETE /gift/1/` | `403` | `403 Forbidden` | High | Negative | `A10` | | | |
| `[AF100-API-56]` | `DEL-001` | `DELETE /gift/{gift_id}/` | CRUD - Delete | Xóa thành công & soft-delete DB | Gift ID hợp lệ | `DELETE /gift/{id}/` | `200` | Soft-delete trong DB (`deleted_at IS NOT NULL`); `GET /gift/` không còn gift này | High | Positive | - | | | Rule 07 |
| `[AF100-API-57]` | `DEL-002` | `DELETE /gift/{gift_id}/` | Business Logic | Xóa gift từng có user mua vẫn giữ lịch sử mua | Gift từng được mua | `DELETE /gift/{id}/` | `200` | Lịch sử mua gift trong DB vẫn nguyên vẹn | High | Positive | - | | | Spec AF100 |
| `[AF100-API-58]` | `DEL-003` | `DELETE /gift/{gift_id}/` | CRUD - Delete Idempotency | Xóa lần 2 cùng `gift_id` đã xóa (`A12`) | Gift vừa xóa | `DELETE /gift/{id}/` | `404` | `404 Not Found` | Medium | Negative | `A12` | | | |
| `[AF100-API-59]` | `DEL-004` | `DELETE /gift/{gift_id}/` | Path parameter | Xóa `gift_id` không tồn tại (`999999`) | Admin token | `DELETE /gift/999999/` | `404` | `404 Not Found` | High | Negative | `A11` | | | |
| `[AF100-API-60]` | `PATH-005` | `DELETE /gift/{gift_id}/` | Path parameter | Xóa `gift_id` sai định dạng (`abc`) | Admin token | `DELETE /gift/abc/` | `400` | `400 Bad Request` | High | Negative | `A6` | | | |
| `[AF100-API-61]` | `PATH-004` | `DELETE /gift/{gift_id}/` | Path parameter | Xóa `gift_id` số âm (`-1`) | Admin token | `DELETE /gift/-1/` | `400` | `400 Bad Request` / `404` | Medium | Boundary | `A6` | | | |
| | | | **5. GET /gift/category/ — DANH MỤC CHO FILTER** | | | | | | | | | | | |
| `[AF100-API-62]` | `AUTH-001` | `GET /gift/category/` | Header - Authorization | Thiếu Authorization | - | No token | `401` | `401 Unauthorized` | High | Negative | `A9` | | | |
| `[AF100-API-63]` | `PERM-002` | `GET /gift/category/` | Authorization & permission | Agency / User gọi API danh mục Admin | Agency token | `GET /gift/category/` | `403` | `403 Forbidden` | High | Negative | `A10` | | | |
| `[AF100-API-64]` | `RESP-001` | `GET /gift/category/` | Response validation | Lấy danh sách danh mục cho pulldown | Admin token | `GET /gift/category/` | `200` | Trả về danh sách category đúng thứ tự `sort_order` | High | Positive | - | | | |
| `[AF100-API-65]` | `RESP-008` | `GET /gift/category/` | Response Empty | Khi chưa có category nào trong DB | 0 category | `GET /gift/category/` | `200` | Trả về mảng rỗng `[]`, không lỗi 500 | Medium | Boundary | - | | | |
