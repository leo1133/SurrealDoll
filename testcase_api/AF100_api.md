# BẢNG KỊCH BẢN KIỂM THỬ BACKEND API (API TEST SUITE)
## Màn hình: AF100 — Gift Manage: Gift List (Danh sách Quà tặng & Toggle Trạng thái)
### Áp dụng: Quy chuẩn Trụ cột 3 (`Universal_Rules/03_api_test_case_rule.md`) & Bộ 419 Viewpoints (`API_controls/API_Viewpoint.md`)
### Phân hệ: Web Master Admin / Quản lý Quà tặng (`AF` Module)

---

## 1. BÓC TÁCH THÔNG TIN CONTRACT API (API CONTRACT ANALYSIS)

| Thuộc tính Contract | Chi tiết Đặc tả Kỹ thuật |
| :--- | :--- |
| **Chức năng nghiệp vụ** | 1. Lấy danh sách, tìm kiếm, lọc, phân trang, sắp xếp quà tặng (`GET /api/v1/admin/gifts`)<br>2. Bật/tắt trạng thái hiển thị quà ON/OFF (`PATCH /api/v1/admin/gifts/:id/status`) |
| **Base URL (Dev / STG)** | `https://api-admin-dev.surrealdolls.com` / `https://api-admin-stg.surrealdolls.com` |
| **Headers bắt buộc** | `Authorization: Bearer <master_admin_token>`<br>`Content-Type: application/json` (cho PATCH)<br>`Accept: application/json` |
| **Phân quyền RBAC** | Master Admin (có quyền Gift Manage). Role Monitor không có quyền sửa/tắt; Agency/User bị từ chối `403 Forbidden`. |

### Cấu trúc Tham số Request (`GET /api/v1/admin/gifts` — Query Params & `PATCH .../status` — Path + JSON Body):
| Tên trường (Field) | Vị trí | Kiểu dữ liệu | Bắt buộc | Ràng buộc kỹ thuật & Nghiệp vụ | Giả định áp dụng |
| :--- | :---: | :---: | :---: | :--- | :---: |
| `q` / `name` | Query (`GET`) | `String` | Optional | Từ khóa tìm kiếm tên quà (partial match) hoặc Gift ID. Tự động trim space đầu/cuối. | `A1`, `A8` |
| `category_id` | Query (`GET`) | `Integer` | Optional | ID danh mục quà (`>= 1`). Omit/rỗng = tất cả danh mục. | `A3` |
| `status` | Query (`GET`) | `Enum` | Optional | Trạng thái lọc: `active` (ON), `inactive` (OFF). Case-sensitive. | `A5` |
| `page` / `offset` | Query (`GET`) | `Integer` | Optional | Số trang (`>= 1`, Default `1`) hoặc offset (`>= 0`). | `A3`, `A13` |
| `limit` | Query (`GET`) | `Integer` | Optional | Số bản ghi/trang (Default `10`, Min `1`, Max `100`). | `A3`, `A4` |
| `sort_by` / `order` | Query (`GET`) | `String` | Optional | Cột sắp xếp (`sort_order`, `coin_price`, `created_at`, `updated_at`) & chiều (`asc`, `desc`). | `A2`, `A8` |
| `id` | Path (`PATCH`) | `Integer` | Required | ID quà tặng cần đổi trạng thái (`>= 1`). | `A6`, `A11` |
| `status` | JSON Body (`PATCH`) | `Enum` | Required | Giá trị mới: `active` hoặc `inactive`. | `A2`, `A5` |

---

## 2. MA TRẬN 419 VIEWPOINTS ĐÃ PHỦ THEO `API_controls/API_Viewpoint.md`

- **Header - General / Accept / Content-Type:** `HDR-001`, `HDR-002`, `ACC-001`..`ACC-007`, `CT-001`..`CT-009`
- **Header - Authorization & RBAC:** `AUTH-001`..`AUTH-016`, `PERM-001`, `PERM-002`, `PERM-008`
- **HTTP Method & Status:** `MTD-001`..`MTD-012`
- **Key / Parameter Name:** `KEY-001`..`KEY-007`
- **String / Search (`q`):** `STR-001`..`STR-005`, `STR-010`..`STR-013`, `STR-016`..`STR-025`
- **Integer (`category_id`) & Enum (`status`):** `INT-001`, `INT-006`..`INT-009`, `INT-012`, `INT-015`..`INT-019`, `ENUM-001`..`ENUM-012`
- **Pagination (`limit`, `offset/page`, `combination`) & Sorting:** `LIM-001`..`LIM-016`, `PAGE-001`..`PAGE-010`, `SORT-001`..`SORT-010`
- **Path Parameter & Update (`PATCH .../status`):** `PATH-001`..`PATH-012`, `BODY-002`..`BODY-009`, `UPD-008`..`UPD-014`
- **Response Validation, Security & Non-functional:** `RESP-001`..`RESP-019`, `SEC-001`..`SEC-017`, `NFR-001`..`NFR-005`
- **Business Logic Core (Pillar 3 L1-L5):** Đồng bộ DB `gifts.status`, không trả bản ghi đã soft-delete, đồng bộ realtime sang App `I600`.

---

## 3. BẢNG CHI TIẾT TEST CASES BACKEND API (14 CỘT CHUẨN)

| ID | VP ID | API Name / Endpoint | Group / Viewpoint Group | Test Case / Scenario | Pre-condition | Request Data / Payload | Expected HTTP Status | Expected Response Body & DB State | Priority | Test Type | Assumption | R1 | R2 | Note / Business Rule |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| | | | **1. GET /api/v1/admin/gifts — HEADER & AUTH** | | | | | | | | | | | |
| `[AF100-API-01]` | `HDR-001` | `GET /api/v1/admin/gifts` | Header - general | Gửi request không kèm bất kỳ Header nào | - | `Headers: {}` | `401` | `{ "code": "UNAUTHORIZED", "message": "CMMSG4..." }` | High | Negative | `A9`, `A13` | | | |
| `[AF100-API-02]` | `HDR-002` | `GET /api/v1/admin/gifts` | Header - general | Tên header viết chữ thường (`authorization`) | Admin token | `Headers: { "authorization": "Bearer <token>" }` | `200` | Trả về danh sách quà (HTTP headers case-insensitive) | Low | Positive | - | | | |
| `[AF100-API-03]` | `ACC-001` | `GET /api/v1/admin/gifts` | Header - Accept | Gửi `Accept: application/json` | Admin token | `Headers: { Accept: "application/json" }` | `200` | Response header `Content-Type: application/json; charset=utf-8` | High | Positive | - | | | |
| `[AF100-API-04]` | `ACC-002` | `GET /api/v1/admin/gifts` | Header - Accept | Thiếu header Accept | Admin token | Không gửi `Accept` | `200` | Fallback JSON mặc định | Medium | Negative | `A9` | | | |
| `[AF100-API-05]` | `ACC-006` | `GET /api/v1/admin/gifts` | Header - Accept | Gửi `Accept: text/xml` (không hỗ trợ) | Admin token | `Headers: { Accept: "text/xml" }` | `406` | `406 Not Acceptable` + error body JSON | High | Negative | `A13` | | | |
| `[AF100-API-06]` | `CT-001` | `GET /api/v1/admin/gifts` | Header - Content-Type | Gửi GET không kèm Content-Type | Admin token | Bỏ `Content-Type` | `200` | GET bỏ qua Content-Type | Medium | Positive | `A9` | | | |
| `[AF100-API-07]` | `CT-002` | `GET /api/v1/admin/gifts` | Header - Content-Type | Gửi GET với Content-Type rỗng / sai | Admin token | `Content-Type: invalid` | `200` | GET bỏ qua Content-Type | Low | Negative | `A9` | | | |
| `[AF100-API-08]` | `AUTH-001` | `GET /api/v1/admin/gifts` | Header - Authorization | Thiếu header Authorization | - | Không có `Authorization` | `401` | `{ "code": "UNAUTHORIZED" }` | High | Negative | `A9` | | | |
| `[AF100-API-09]` | `AUTH-002` | `GET /api/v1/admin/gifts` | Header - Authorization | Authorization rỗng | - | `Authorization: ""` | `401` | `{ "code": "UNAUTHORIZED" }` | High | Boundary | `A9` | | | |
| `[AF100-API-10]` | `AUTH-003` | `GET /api/v1/admin/gifts` | Header - Authorization | Chỉ gửi `Bearer` không kèm token | - | `Authorization: "Bearer "` | `401` | `{ "code": "UNAUTHORIZED" }` | High | Boundary | `A9` | | | |
| `[AF100-API-11]` | `AUTH-004` | `GET /api/v1/admin/gifts` | Header - Authorization | Sai scheme (`Basic <token>`) | - | `Authorization: "Basic <token>"` | `401` | `{ "code": "UNAUTHORIZED" }` | High | Negative | `A9` | | | |
| `[AF100-API-12]` | `AUTH-005` | `GET /api/v1/admin/gifts` | Header - Authorization | Thiếu tiền tố `Bearer` | - | `Authorization: "<jwt>"` | `401` | `{ "code": "UNAUTHORIZED" }` | High | Negative | `A9` | | | |
| `[AF100-API-13]` | `AUTH-007` | `GET /api/v1/admin/gifts` | Header - Authorization | Token sai định dạng JWT | - | `Authorization: "Bearer abc123"` | `401` | `{ "code": "UNAUTHORIZED" }` | High | Negative | `A9` | | | |
| `[AF100-API-14]` | `AUTH-008` | `GET /api/v1/admin/gifts` | Header - Authorization | Token bị sửa 1 ký tự (Tampered) | - | `Authorization: "Bearer <tampered>"` | `401` | Signature validation failed | High | Security | `A9` | | | |
| `[AF100-API-15]` | `AUTH-009` | `GET /api/v1/admin/gifts` | Header - Authorization | Token đã hết hạn (Expired) | Token hết hạn | `Authorization: "Bearer <expired>"` | `401` | `{ "code": "TOKEN_EXPIRED" }` (`CMMSG10`) | High | Negative | `A9` | | | |
| `[AF100-API-16]` | `AUTH-010` | `GET /api/v1/admin/gifts` | Header - Authorization | Token từ môi trường khác (STG -> DEV) | STG token | `Authorization: "Bearer <stg_token>"` | `401` | Từ chối token khác issuer/secret | High | Security | `A9` | | | |
| `[AF100-API-17]` | `AUTH-012` | `GET /api/v1/admin/gifts` | Header - Authorization | Token sau khi đã Logout | Token đã logout | `Authorization: "Bearer <revoked>"` | `401` | Token bị thu hồi | High | Negative | `A9` | | | |
| `[AF100-API-18]` | `AUTH-016` | `GET /api/v1/admin/gifts` | Header - Authorization | Truyền token qua URL query | Admin token | `?access_token=<token>` (no Header) | `401` | Không chấp nhận token qua URL | Medium | Security | `A9` | | | |
| `[AF100-API-19]` | `PERM-001` | `GET /api/v1/admin/gifts` | Authorization & permission | Gọi với quyền Master Admin | Admin token | `Authorization: Bearer <admin>` | `200` | Trả về đầy đủ danh sách quà | High | Positive | `A10` | | | |
| `[AF100-API-20]` | `PERM-002` | `GET /api/v1/admin/gifts` | Authorization & permission | Gọi với quyền Agency / Streamer / User | Agency/User token | `Authorization: Bearer <agency_token>` | `403` | `{ "code": "FORBIDDEN", "message": "CMMSG5: この操作を行う権限がありません。" }` | High | Negative | `A10` | | | |
| | | | **2. GET /api/v1/admin/gifts — HTTP METHOD & QUERY KEYS** | | | | | | | | | | | |
| `[AF100-API-21]` | `MTD-002` | `GET /api/v1/admin/gifts/invalid` | HTTP method & status | Đường dẫn không tồn tại | Admin token | `GET /api/v1/admin/gifts_not_found` | `404` | Trả 404 JSON body (không trả HTML) | High | Negative | `A13` | | | |
| `[AF100-API-22]` | `MTD-006` | `PUT /api/v1/admin/gifts` | HTTP method & status | Gửi PUT lên endpoint collection | Admin token | `PUT /api/v1/admin/gifts` | `405` | `405 Method Not Allowed` + header `Allow` | High | Negative | - | | | |
| `[AF100-API-23]` | `MTD-008` | `DELETE /api/v1/admin/gifts` | HTTP method & status | Gửi DELETE lên endpoint collection | Admin token | `DELETE /api/v1/admin/gifts` | `405` | `405 Method Not Allowed`, không xóa DB | High | Security | - | | | |
| `[AF100-API-24]` | `MTD-010` | `OPTIONS /api/v1/admin/gifts` | HTTP method & status | Preflight CORS OPTIONS | Admin token | `OPTIONS /api/v1/admin/gifts` | `200 / 204` | Trả về header `Allow` và CORS | Medium | Positive | - | | | |
| `[AF100-API-25]` | `KEY-001` | `GET /api/v1/admin/gifts` | Key / parameter name | Query key rỗng (`?=abc`) | Admin token | `?=abc` | `400` | `400 Bad Request` (hoặc ignore) | High | Negative | - | | | |
| `[AF100-API-26]` | `KEY-002` | `GET /api/v1/admin/gifts` | Key / parameter name | Query key sai chính tả / không tồn tại | Admin token | `?namex=Heart` | `200` | Unknown param bị bỏ qua, trả danh sách mặc định | Medium | Negative | `A1` | | | |
| `[AF100-API-27]` | `KEY-006` | `GET /api/v1/admin/gifts` | Key / parameter name | Query key sai hoa thường (`?STATUS=active`) | Admin token | `?STATUS=active` | `200` | Bị ignore vì key case-sensitive | Low | Negative | `A1`, `A2` | | | |
| `[AF100-API-28]` | `KEY-007` | `GET /api/v1/admin/gifts` | Key / parameter name | Trùng lặp query key | Admin token | `?status=active&status=inactive` | `200` | Lấy giá trị sau cùng (`inactive`), không lỗi 500 | Medium | Negative | `A3` | | | |
| | | | **3. GET /api/v1/admin/gifts — SEARCH (`q`), CATEGORY, STATUS** | | | | | | | | | | | |
| `[AF100-API-29]` | `STR-001` | `GET /api/v1/admin/gifts` | String / text (`q`) | Tìm kiếm theo chữ Latin hợp lệ | Có quà "Heart" | `?q=Heart` | `200` | Trả về quà chứa "Heart" | High | Positive | - | | | |
| `[AF100-API-30]` | `STR-002` | `GET /api/v1/admin/gifts` | String / text (`q`) | Tìm kiếm bằng chuỗi số | Có quà ID=10 | `?q=10` | `200` | Trả về quà có tên chứa "10" hoặc ID=10 | High | Positive | - | | | |
| `[AF100-API-31]` | `STR-003` | `GET /api/v1/admin/gifts` | String / text (`q`) | Ký tự đặc biệt URL-encoded | Admin token | `?q=%40%23%24%25` | `200` | Xử lý như text thuần, không lỗi 500 | High | Boundary | - | | | |
| `[AF100-API-32]` | `STR-005` | `GET /api/v1/admin/gifts` | String / text (`q`) | Khoảng trắng đầu/cuối (`"  Heart  "`) | Có quà "Heart" | `?q=%20%20Heart%20%20` | `200` | Tự động trim space, khớp với `?q=Heart` | Medium | Boundary | - | | | |
| `[AF100-API-33]` | `STR-010` | `GET /api/v1/admin/gifts` | String / text (`q`) | Ký tự tiếng Nhật / Unicode UTF-8 | Có quà "ハート" | `?q=ハート` | `200` | Tìm kiếm chính xác UTF-8 | Medium | Positive | - | | | |
| `[AF100-API-34]` | `STR-012` | `GET /api/v1/admin/gifts` | String / text (`q`) | Ký tự Emoji 4-byte | Admin token | `?q=🎁` | `200 / 400` | Không lỗi 500 | Low | Boundary | - | | | |
| `[AF100-API-35]` | `STR-019` | `GET /api/v1/admin/gifts` | String / text (`q`) | Ký tự SQL wildcard (`%` và `_`) | Admin token | `?q=%25` / `?q=_` | `200` | Escape wildcard, không trả toàn bộ bảng | Medium | Security | - | | | |
| `[AF100-API-36]` | `STR-020` | `GET /api/v1/admin/gifts` | String / text (`q`) | Tìm kiếm không khớp bản ghi nào | Admin token | `?q=zzzzzzzz999` | `200` | `{ data: [], total: 0 }` (không null, không 404) | High | Boundary | - | | | |
| `[AF100-API-37]` | `STR-021` | `GET /api/v1/admin/gifts` | String / text (`q`) | Tìm kiếm một phần (Partial match) | Có quà "Starlight" | `?q=Star` | `200` | Trả về "Starlight" | Medium | Positive | - | | | |
| `[AF100-API-38]` | `STR-024` | `GET /api/v1/admin/gifts` | String / text (`q`) | Toàn khoảng trắng | Admin token | `?q=%20%20%20` | `200` | Coi như rỗng, trả danh sách mặc định | Medium | Boundary | - | | | |
| `[AF100-API-39]` | `INT-001` | `GET /api/v1/admin/gifts` | Integer (`category_id`) | `category_id` hợp lệ | Có category ID=1 | `?category_id=1` | `200` | Chỉ trả quà thuộc `category_id=1` | High | Positive | - | | | |
| `[AF100-API-40]` | `INT-007` | `GET /api/v1/admin/gifts` | Integer (`category_id`) | `category_id` âm (`-1`) | Admin token | `?category_id=-1` | `400` | `400 Bad Request` + error body | High | Boundary | - | | | |
| `[AF100-API-41]` | `INT-008` | `GET /api/v1/admin/gifts` | Integer (`category_id`) | `category_id` số thập phân (`1.5`) | Admin token | `?category_id=1.5` | `400` | `400 Bad Request` | High | Negative | `A3` | | | |
| `[AF100-API-42]` | `INT-009` | `GET /api/v1/admin/gifts` | Integer (`category_id`) | `category_id` là chữ (`abc`) | Admin token | `?category_id=abc` | `400` | `400 Bad Request` | High | Negative | `A3` | | | |
| `[AF100-API-43]` | `ENUM-001` | `GET /api/v1/admin/gifts` | Enum (`status`) | Lọc từng giá trị hợp lệ (`active`, `inactive`) | Admin token | `?status=active` / `?status=inactive` | `200` | Số lượng khớp DB từng trạng thái | High | Positive | - | | | |
| `[AF100-API-44]` | `ENUM-004` | `GET /api/v1/admin/gifts` | Enum (`status`) | Giá trị ngoài enum (`unknown`) | Admin token | `?status=unknown` | `400` | `400 Bad Request` liệt kê giá trị hợp lệ | High | Negative | `A5` | | | |
| `[AF100-API-45]` | `ENUM-006` | `GET /api/v1/admin/gifts` | Enum (`status`) | Sai hoa/thường (`ACTIVE`) | Admin token | `?status=ACTIVE` | `400` | Enum case-sensitive (`A2`) | Medium | Negative | `A2` | | | |
| | | | **4. GET /api/v1/admin/gifts — PAGINATION & SORTING** | | | | | | | | | | | |
| `[AF100-API-46]` | `LIM-001` | `GET /api/v1/admin/gifts` | Pagination - limit | Không truyền `limit` | Admin token | `GET /api/v1/admin/gifts` | `200` | Default `limit=10`, `page=1` | Medium | Positive | `A13` | | | |
| `[AF100-API-47]` | `LIM-003` | `GET /api/v1/admin/gifts` | Pagination - limit | `limit = -1` | Admin token | `?limit=-1` | `400` | `400 Bad Request` | High | Boundary | - | | | |
| `[AF100-API-48]` | `LIM-004` | `GET /api/v1/admin/gifts` | Pagination - limit | `limit = 0` | Admin token | `?limit=0` | `400` | `400 Bad Request` | High | Boundary | - | | | |
| `[AF100-API-49]` | `LIM-007` | `GET /api/v1/admin/gifts` | Pagination - limit | `limit = 100` (max_limit) | Admin token | `?limit=100` | `200` | Trả tối đa 100 bản ghi | High | Boundary | - | | | |
| `[AF100-API-50]` | `LIM-008` | `GET /api/v1/admin/gifts` | Pagination - limit | `limit = 101` (max_limit + 1) | Admin token | `?limit=101` | `400` | `400 Bad Request` (hoặc cap về 100) | High | Boundary | `A4` | | | |
| `[AF100-API-51]` | `LIM-010` | `GET /api/v1/admin/gifts` | Pagination - limit | `limit` overflow 32-bit (`2147483648`) | Admin token | `?limit=2147483648` | `400` | `400 Bad Request`, không lỗi 500 | High | Boundary | - | | | |
| `[AF100-API-52]` | `LIM-013` | `GET /api/v1/admin/gifts` | Pagination - limit | `limit = abc` | Admin token | `?limit=abc` | `400` | `400 Bad Request` | High | Negative | - | | | |
| `[AF100-API-53]` | `PAGE-001` | `GET /api/v1/admin/gifts` | Pagination - combination | Kết hợp toàn bộ filters + phân trang | Admin token | `?q=Star&category_id=1&status=active&page=1&limit=5` | `200` | Kết hợp AND chính xác, `total` đúng | High | Positive | - | | | |
| `[AF100-API-54]` | `PAGE-003` | `GET /api/v1/admin/gifts` | Pagination - combination | Trang 1 và Trang 2 không trùng/sót bản ghi | Có >= 11 quà | `?page=1&limit=10` rồi `?page=2&limit=10` | `200` | Không có ID trùng hoặc sót giữa 2 trang | High | Positive | - | | | |
| `[AF100-API-55]` | `PAGE-005` | `GET /api/v1/admin/gifts` | Pagination - combination | `page` vượt quá tổng số trang | Admin token | `?page=99999` | `200` | `{ data: [], total: N }` | High | Boundary | - | | | |
| `[AF100-API-56]` | `PAGE-010` | `GET /api/v1/admin/gifts` | Pagination - combination | Bản ghi đã xóa mềm không xuất hiện | Có quà đã soft-delete | `GET /api/v1/admin/gifts?q=<deleted_name>` | `200` | Bản ghi đã xóa không trả về, `total` giảm | Medium | Positive | - | | | |
| `[AF100-API-57]` | `SORT-001` | `GET /api/v1/admin/gifts` | Sorting | Sort tăng dần theo `coin_price` / `sort_order` | Admin token | `?sort_by=coin_price&order=asc` | `200` | Danh sách sắp xếp tăng dần đúng thứ tự | Medium | Positive | - | | | |
| `[AF100-API-58]` | `SORT-002` | `GET /api/v1/admin/gifts` | Sorting | Sort giảm dần theo `created_at` | Admin token | `?sort_by=created_at&order=desc` | `200` | Bản ghi mới nhất lên đầu | Medium | Positive | - | | | |
| `[AF100-API-59]` | `SORT-004` | `GET /api/v1/admin/gifts` | Sorting | `sort_by` cột không tồn tại | Admin token | `?sort_by=non_exist_col` | `400` | `400 Bad Request` | Medium | Negative | - | | | |
| `[AF100-API-60]` | `SORT-005` | `GET /api/v1/admin/gifts` | Sorting | SQL Injection trong `sort_by` | Admin token | `?sort_by=name;DROP TABLE gifts` | `400` | Chặn whitelist cột, không thực thi SQL | High | Security | - | | | |
| | | | **5. GET /api/v1/admin/gifts — RESPONSE, SECURITY & NFR** | | | | | | | | | | | |
| `[AF100-API-61]` | `RESP-001` | `GET /api/v1/admin/gifts` | Response validation | Kiểm tra đúng tên fields và data types | Admin token | `GET /api/v1/admin/gifts` | `200` | Đủ fields: `id, name, coin_price, category_id, status, sort_order, icon_url, created_at, updated_at` | High | Positive | - | | | |
| `[AF100-API-62]` | `RESP-010` | `GET /api/v1/admin/gifts` | Response validation | Đối soát số lượng và giá trị với DB | Admin token | So sánh JSON với `SELECT COUNT(*) FROM gifts WHERE deleted_at IS NULL` | `200` | `total` và giá trị khớp DB 100% | High | Positive | - | | | Rule 07 |
| `[AF100-API-63]` | `RESP-016` | `GET /api/v1/admin/gifts` | Response validation | Không lộ stack trace khi trigger 4xx | Admin token | `?page=abc` | `400` | Không lộ SQL, file path, framework version | High | Security | - | | | |
| `[AF100-API-64]` | `SEC-001` | `GET /api/v1/admin/gifts` | Security | SQL Injection trong `q` | Admin token | `?q=' OR 1=1 --` | `200 / 400` | Không trả toàn bộ bảng, không lỗi SQL | High | Security | `A8` | | | |
| `[AF100-API-65]` | `SEC-006` | `GET /api/v1/admin/gifts` | Security | Reflected XSS trong `q` | Admin token | `?q=<script>alert(1)</script>` | `200 / 400` | JSON escape an toàn | High | Security | `A8` | | | |
| `[AF100-API-66]` | `SEC-014` | `GET /api/v1/admin/gifts` | Security | Rate limit (100 req/phút) | Admin token | Gửi 100+ request/phút | `429` | `429 Too Many Requests` + `Retry-After` | High | Security | `A14` | | | |
| `[AF100-API-67]` | `NFR-001` | `GET /api/v1/admin/gifts` | Non-functional | Response time bình thường | Admin token | `GET /api/v1/admin/gifts` | `200` | Thời gian phản hồi < 2000ms (p95) | Medium | Performance | - | | | |
| | | | **6. PATCH /api/v1/admin/gifts/:id/status — TOGGLE ON/OFF** | | | | | | | | | | | |
| `[AF100-API-68]` | `AUTH-001` | `PATCH /api/v1/admin/gifts/:id/status` | Header - Authorization | Thiếu header Authorization | - | Không gửi `Authorization`, Body: `{ "status": "inactive" }` | `401` | `{ "code": "UNAUTHORIZED" }` | High | Negative | `A9` | | | |
| `[AF100-API-69]` | `PERM-002` | `PATCH /api/v1/admin/gifts/:id/status` | Authorization & permission | Role không có quyền (Monitor / Agency) | Token Monitor/Agency | Body: `{ "status": "inactive" }` | `403` | `403 Forbidden` (`CMMSG5`) | High | Negative | `A10` | | | |
| `[AF100-API-70]` | `CT-003` | `PATCH /api/v1/admin/gifts/:id/status` | Header - Content-Type | Thiếu `Content-Type` | Admin token | Không có `Content-Type`, Body: `{"status":"inactive"}` | `415 / 400` | `415 Unsupported Media Type` | High | Negative | `A7` | | | |
| `[AF100-API-71]` | `CT-005` | `PATCH /api/v1/admin/gifts/:id/status` | Header - Content-Type | Gửi `Content-Type: text/plain` | Admin token | `Content-Type: text/plain` | `415` | `415 Unsupported Media Type` | High | Negative | `A7` | | | |
| `[AF100-API-72]` | `PATH-001` | `PATCH /api/v1/admin/gifts/:id/status` | Path parameter | Toggle ON -> OFF thành công | Quà ID=1 đang `active` | `PATCH /gifts/1/status`, Body: `{ "status": "inactive" }` | `200` | DB: `gifts.status = 'inactive'`, `updated_at` cập nhật; App `I600` ẩn quà | High | Positive | - | | | Rule 07 |
| `[AF100-API-73]` | `BIZ-01` | `PATCH /api/v1/admin/gifts/:id/status` | Business Logic | Toggle OFF -> ON thành công | Quà ID=1 đang `inactive` | `PATCH /gifts/1/status`, Body: `{ "status": "active" }` | `200` | DB: `gifts.status = 'active'`; App `I600` hiển thị lại quà | High | Positive | - | | | Rule 07 |
| `[AF100-API-74]` | `PATH-002` | `PATCH /api/v1/admin/gifts/:id/status` | Path parameter | ID không tồn tại | Admin token | `PATCH /gifts/999999/status`, Body: `{ "status": "inactive" }` | `404` | `{ "code": "NOT_FOUND" }` | High | Negative | `A11` | | | |
| `[AF100-API-75]` | `PATH-005` | `PATCH /api/v1/admin/gifts/:id/status` | Path parameter | ID là chữ (`abc`) | Admin token | `PATCH /gifts/abc/status` | `400` | `{ "code": "INVALID_PARAM" }` | High | Negative | `A6` | | | |
| `[AF100-API-76]` | `PATH-012` | `PATCH /api/v1/admin/gifts/:id/status` | Path parameter | Quà đã bị soft-delete | Quà đã xóa mềm | `PATCH /gifts/<deleted_id>/status` | `404` | Không cho đổi status bản ghi đã xóa | High | Negative | - | | | |
| `[AF100-API-77]` | `BODY-003` | `PATCH /api/v1/admin/gifts/:id/status` | Body - JSON structure | JSON lỗi cú pháp (thiếu ngoặc đóng) | Admin token | `Body: '{"status":"inactive"'` | `400` | `400 Bad Request` (Invalid JSON) | High | Negative | `A13` | | | |
| `[AF100-API-78]` | `UPD-009` | `PATCH /api/v1/admin/gifts/:id/status` | CRUD - Update | PATCH với body rỗng `{}` | Admin token | `Body: {}` | `400` | `400 Bad Request` | Medium | Negative | `A11` | | | |
| `[AF100-API-79]` | `ENUM-004` | `PATCH /api/v1/admin/gifts/:id/status` | Enum / droplist | Giá trị `status` ngoài enum (`"PENDING"`) | Admin token | `Body: { "status": "PENDING" }` | `400` | `400 Bad Request` | High | Negative | `A5` | | | |
| `[AF100-API-80]` | `UPD-014` | `PATCH /api/v1/admin/gifts/:id/status` | CRUD - Update | Gửi 2 request PATCH đồng thời (Active & Inactive) | Quà ID=1 | 2 concurrent PATCH requests | `200` | Trạng thái cuối cùng trên DB nhất quán, không lỗi 500 | Low | Boundary | - | | | |
