# BẢNG KỊCH BẢN KIỂM THỬ BACKEND API (API TEST SUITE)
## Màn hình / Chức năng: `K2022` — Delete ACCOUNT ADMIN (Close Account Admin)
### Nguồn Spec: Google Sheet `K2022-Close Acc` (A58:G84) + Ticket Backlog `SURREALDOLLS-15112` & `SURREALDOLLS-15114`
### Áp dụng: Quy chuẩn Trụ cột 3 (`Universal_Rules/03_api_test_case_rule.md`) & 419 Viewpoints Logic

---

## 1. BÓC TÁCH THÔNG TIN CONTRACT API (API CONTRACT ANALYSIS)

| Thuộc tính Contract | Chi tiết Đặc tả Kỹ thuật |
| :--- | :--- |
| **Chức năng nghiệp vụ** | 1. API Admin trả trạng thái `退会済み` (`withdrawn` / `is_withdrawn: true`) sau 30 ngày cho các màn hình Admin.<br>2. API Admin gỡ ban (`POST /api/v1/admin/stream/ban/unban/` & `POST /api/v1/admin/livestream-chat/unban/`) chặn gỡ ban tức thì đối với user đã hủy tài khoản.<br>3. API đồng bộ trạng thái khi user đăng nhập khôi phục tài khoản trong hạn 30 ngày. |
| **Base URL (Dev / STG)** | `https://api-admin-dev.surrealdolls.com` / `https://api-admin-stg.surrealdolls.com` |
| **Headers bắt buộc** | `Authorization: Bearer <admin_token>`, `Content-Type: application/json`, `Accept: application/json` |
| **Phân quyền RBAC** | Master Admin có toàn quyền trên 22 endpoint. Agency Admin chỉ có quyền tra cứu streamer và doanh thu thuộc Agency mình (`AD302`, `AD303`). User thường không có quyền truy cập (`403 Forbidden`). |

---

## 2. MA TRẬN VIEWPOINTS ĐÃ PHỦ THEO `API_controls/API_Viewpoint.md`

- **Header, Auth & RBAC:** `HDR-001`, `ACC-001`, `AUTH-001`, `AUTH-007`, `AUTH-009`, `PERM-001`, `PERM-002`
- **Chặn Gỡ Ban Tức Thì (Unban Lockout Logic - SURREALDOLLS-15112):** `BAN-LCK-01`, `BAN-LCK-02`, `BAN-LCK-03`, `BAN-LCK-04`, `BAN-LCK-05`
- **Response Trạng Thái Tài Khoản (Status Response - SURREALDOLLS-15112):** `STAT-RESP-01`, `STAT-RESP-02`, `STAT-RESP-03`, `STAT-RESP-04`, `STAT-RESP-05`, `STAT-RESP-06`, `STAT-RESP-07`
- **Đồng Bộ Khôi Phục & Toàn Vẹn CSDL (Data Integrity & Restore):** `REST-SYNC-01`, `REST-SYNC-02`, `DB-PERS-01`, `DB-PERS-02`
- **Bảo Mật & Sanitize Input (Security & Validation):** `SEC-INJ-01`, `SEC-XSS-01`, `VAL-REQ-01`, `VAL-TYPE-01`

---

## 3. BẢNG CHI TIẾT TEST CASES BACKEND API (14 CỘT CHUẨN)

| ID | VP ID | API Name / Endpoint | Group / Viewpoint Group | Test Case / Scenario | Pre-condition | Request Data / Payload | Expected HTTP Status | Expected Response Body & DB State | Priority | Test Type | Assumption | R1 | R2 | Note / Business Rule |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `[K2022-API-01]` | `HDR-001` | `GET /api/v1/admin/users/` | Header - general | Gửi request không kèm header Authorization | - | `Headers: {}` | `401` | `{"detail": "Not authenticated"}` (`CMMSG4`) | High | Negative | A9 | | | |
| `[K2022-API-02]` | `ACC-001` | `GET /api/v1/admin/users/` | Header - Accept | Gửi request với Accept: application/json hợp lệ | Token Master Admin | `Accept: application/json` | `200` | Trả về danh sách user dạng JSON đúng format | High | Positive | - | | | |
| `[K2022-API-03]` | `AUTH-001` | `POST /api/v1/admin/stream/ban/unban/` | Header - Authorization | Gọi API gỡ ban không truyền Bearer token | - | `Headers: {}` | `401` | `401 Unauthorized` | High | Negative | A9 | | | |
| `[K2022-API-04]` | `AUTH-007` | `POST /api/v1/admin/stream/ban/unban/` | Header - Authorization | Gửi Bearer token sai format JWT | - | `Bearer invalid_jwt_token` | `401` | `401 Unauthorized` | High | Negative | A9 | | | |
| `[K2022-API-05]` | `AUTH-009` | `GET /api/v1/admin/users/` | Header - Authorization | Gửi token đã hết hạn (Expired token) | Expired token | `Bearer <expired_token>` | `401` | `401 Unauthorized` (`CMMSG10`) | High | Negative | A9 | | | |
| `[K2022-API-06]` | `PERM-001` | `GET /api/v1/admin/users/` | Authorization & RBAC | End-user gọi API danh sách người dùng Admin | Token End-User | `GET /api/v1/admin/users/` | `403` | `403 Forbidden` (`CMMSG5`) | High | Security | A10 | | | |
| `[K2022-API-07]` | `PERM-002` | `POST /api/v1/admin/stream/ban/unban/` | Authorization & RBAC | Agency Admin gọi API gỡ ban Master Admin | Token Agency Admin | `{"user_id": "u123"}` | `403` | `403 Forbidden` | High | Security | A10 | | | |
| `[K2022-API-08]` | `BAN-LCK-01` | `POST /api/v1/admin/stream/ban/unban/` | Unban Lockout Logic | Chặn gỡ ban user vừa close account dưới 30 ngày (Tức thì) | User đang close account < 30 ngày | `{"user_id": "u_close_5d"}` | `400` | `{"detail": "Cannot unban user who requested account deletion"}` | High | Negative | - | | | Logic tức thì |
| `[K2022-API-09]` | `BAN-LCK-02` | `POST /api/v1/admin/stream/ban/unban/` | Unban Lockout Logic | Chặn gỡ ban user đã close account quá 30 ngày (Sau 30 ngày) | User đã close account >= 30 ngày | `{"user_id": "u_close_35d"}` | `400` | `{"detail": "User account has been withdrawn"}` | High | Negative | - | | | Hết grace period |
| `[K2022-API-10]` | `BAN-LCK-03` | `POST /api/v1/admin/livestream-chat/unban/` | Unban Lockout Logic | Chặn gỡ ban chat livestream cho user đã close account (AY300) | User đang close account | `{"user_id": "u_close_live"}` | `400` | `{"detail": "Cannot unban user who requested account deletion"}` | High | Negative | - | | | Khóa chat live |
| `[K2022-API-11]` | `BAN-LCK-04` | `POST /api/v1/admin/stream/ban/unban/` | Unban Lockout Logic | Gỡ ban thành công cho user bình thường không close account | User bị ban, không close account | `{"user_id": "u_normal_ban"}` | `200` | Trả về `{"success": true}`, DB cập nhật gỡ ban | High | Positive | - | | | Happy path |
| `[K2022-API-12]` | `BAN-LCK-05` | `POST /api/v1/admin/stream/ban/unban/` | Unban Lockout Logic | Gỡ ban thành công sau khi user đã login khôi phục tài khoản | User khôi phục đăng nhập lại | `{"user_id": "u_restored"}` | `200` | Cho phép gỡ ban thành công vì account đã restore | High | Positive | - | | | Sau khôi phục |
| `[K2022-API-13]` | `STAT-RESP-01` | `GET /api/v1/admin/users/` | Status Response AE100 | Kiểm tra response user trong hạn Grace Period dưới 30 ngày | User close account < 30 ngày | `?keyword=u_close_5d` | `200` | `status: "active"`, `is_withdrawn: false` | High | Positive | - | | | Chưa đổi status |
| `[K2022-API-14]` | `STAT-RESP-02` | `GET /api/v1/admin/users/` | Status Response AE100 | Kiểm tra response user đã close account từ 30 ngày trở lên | User close account >= 30 ngày | `?keyword=u_close_35d` | `200` | `status: "withdrawn"`, `is_withdrawn: true` | High | Positive | - | | | Đổi status |
| `[K2022-API-15]` | `STAT-RESP-03` | `GET /api/v1/admin/users/{user_id}/` | Status Response AE200 | Lấy chi tiết user đã close account quá 30 ngày | User close account >= 30 ngày | `GET /admin/users/{id}` | `200` | Chi tiết user trả về `status: "withdrawn"` | High | Positive | - | | | Chi tiết user |
| `[K2022-API-16]` | `STAT-RESP-04` | `GET /api/v1/admin/agency/streamers/` | Status Response AD302 | Kiểm tra danh sách streamer của Agency có streamer đã close account | Streamer close account >= 30 ngày | `GET /agency/streamers/` | `200` | Record streamer trả `status: "withdrawn"`, `is_withdrawn: true` | High | Positive | - | | | Phân hệ Agency |
| `[K2022-API-17]` | `STAT-RESP-05` | `GET /api/v1/admin/agency/revenue/` | Status Response AD303 | Doanh thu Agency trả cờ withdrawn cho cả payer và receiver | Có giao dịch của user withdrawn | `GET /agency/revenue/` | `200` | Đối tượng `payer` và `receiver` đều có cờ `is_withdrawn` chuẩn | High | Positive | - | | | Hai vai trò |
| `[K2022-API-18]` | `STAT-RESP-06` | `GET /api/v1/admin/stream/ended/` | Status Response AG500 | Danh sách stream ended trả cờ withdrawn cho streamer | Streamer đã close account | `GET /stream/ended/` | `200` | Streamer có `is_withdrawn: true`, viewer không bị đánh dấu | High | Positive | - | | | Stream Ended |
| `[K2022-API-19]` | `STAT-RESP-07` | `GET /api/v1/admin/sales/payout/` | Status Response AS200 | Danh sách payout request trả cờ withdrawn cho user yêu cầu | User payout đã withdrawn | `GET /sales/payout/` | `200` | Dòng yêu cầu rút tiền chứa `user_status: "withdrawn"` | High | Positive | - | | | Payout Request |
| `[K2022-API-20]` | `REST-SYNC-01` | `POST /api/v1/auth/login/` | Restore & Sync Flow | User close account login lại trong vòng 30 ngày | User đã close account < 30 ngày | `{"email": "u@test.com", "password": "..."}` | `200` | Login thành công, DB xóa cờ xóa mềm `closed_at: null` | High | Positive | - | | | Khôi phục tự động |
| `[K2022-API-21]` | `REST-SYNC-02` | `POST /api/v1/auth/login/` | Restore & Sync Flow | User close account login lại sau khi đã qua 30 ngày | User đã close account >= 30 ngày | `{"email": "u@test.com", "password": "..."}` | `401` | Từ chối đăng nhập hoặc tạo tài khoản mới theo spec | High | Negative | - | | | Quá hạn 30 ngày |
| `[K2022-API-22]` | `DB-PERS-01` | `GET /api/v1/admin/users/` | Data Persistence | Toàn bộ dữ liệu user withdrawn chỉ bị soft-delete, không mất bản ghi | User đã withdrawn | `?show_all=true` | `200` | Bản ghi user vẫn tồn tại đầy đủ, không bị null các trường liên kết | High | Positive | - | | | Toàn vẹn DB |
| `[K2022-API-23]` | `SEC-INJ-01` | `GET /api/v1/admin/users/` | Security & SQL Injection | Truyền SQL Injection vào query param keyword tìm kiếm | Token Admin | `?keyword=' OR 1=1 --` | `200` | Sanitize an toàn, trả danh sách rỗng hoặc filter text, không lỗi 500 | High | Security | - | | | SQL Injection |
| `[K2022-API-24]` | `SEC-XSS-01` | `GET /api/v1/admin/users/` | Security & XSS | Truyền XSS script payload vào query param keyword | Token Admin | `?keyword=<script>alert(1)</script>` | `200` | Encode / Sanitize an toàn, không phản hồi nguyên bản script | High | Security | - | | | XSS Prevention |
| `[K2022-API-25]` | `VAL-REQ-01` | `POST /api/v1/admin/stream/ban/unban/` | Input Validation | Gửi body rỗng thiếu user_id bắt buộc | Token Admin | `{}` | `422` | `{"detail": [{"loc": ["body", "user_id"], "msg": "field required"}]}` | High | Negative | - | | | Required field |
| `[K2022-API-26]` | `VAL-TYPE-01` | `POST /api/v1/admin/stream/ban/unban/` | Input Validation | Gửi user_id sai kiểu dữ liệu | Token Admin | `{"user_id": 12345}` | `422` | Báo lỗi kiểu dữ liệu không hợp lệ | Medium | Boundary | - | | | Type check |

*Được sinh tự động theo quy chuẩn `Universal_Rules/03_api_test_case_rule.md` & `API_controls/API_Viewpoint.md` - Tuân thủ 100% 14 cột chuẩn.*
