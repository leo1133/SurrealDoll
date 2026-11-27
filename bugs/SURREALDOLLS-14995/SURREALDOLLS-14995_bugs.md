# BÁO CÁO XÁC THỰC LỖI & RETEST (BUG VERIFICATION REPORT)
## Ticket: [SURREALDOLLS-14995](https://issoh.backlog.com/view/SURREALDOLLS-14995) - Màn hình: `BF300` (配信アーカイブ閲覧)
### Môi trường xác thực: `STG` (`admin-stg.surrealdolls.com`) | Ngày kiểm tra: 27/11/2026
### Áp dụng: Quy chuẩn Trụ cột 6 (`Universal_Rules/06_bug_reporting_rule.md`) & Master Policy (`GEMINI.md`)

---

## 1. TỔNG QUAN TÌNH TRẠNG & KẾT LUẬN RETEST

- **Mã Ticket:** `[SURREALDOLLS-14995]`
- **Tiêu đề Bug:** `[BUG] - [BF300 配信アーカイブ閲覧] - Tài khoản 事務所: 視聴者一覧 báo 「視聴者情報を取得できませんでした」 và ギフト演出 lỗi (getGiftTimeline 500)`
- **Màn hình liên quan:** `BF300` (Agency Archive Stream View) & `BF100` (Agency Archive Stream List)
- **Môi trường kiểm tra:** `STG` (Theo đúng định tuyến bắt buộc `Need Verify (STG)`)
- **Tài khoản test:** `agency123` | `123456aA@` (ID: 36, Code: `agency123`, Name: `agency1234`)
- **Kết luận thẩm định:** <span style="color:orange; font-weight:bold;">BLOCKED PRE-CONDITION / PENDING DATA SEEDING (CHƯA THỂ E2E DO THIẾU DATA)</span>
- **Đề xuất hành động:** **GIỮ NGUYÊN TRẠNG THÁI `Need Verify (STG)`** (Tuyệt đối không đổi trạng thái trên Backlog theo Red Line Rule 10; tiến hành tạo Liver & Archive theo quy trình bên dưới).
- **Actual Time đối soát:** `0.25h` (15 phút kiểm tra trạng thái Backend API & đối soát dữ liệu Agency STG).

---

## 2. KẾT QUẢ ĐỐI SOÁT CHI TIẾT TRÊN MÔI TRƯỜNG STG

| STT | Tiêu chí kiểm thử | Kết quả kỳ vọng (Expected) | Kết quả thực tế trên STG (Actual) | Đánh giá | Trạng thái kỹ thuật |
| :-: | :--- | :--- | :--- | :-: | :--- |
| **1** | **Xác thực sự tồn tại của 2 API Scoped mới trên STG Backend** | Backend STG (`api-admin-stg.surrealdolls.com`) đã deploy 2 endpoint mới: `GET .../participants` và `GET .../gift-timeline` | Đã kiểm tra `openapi.json` trên STG: Cả 2 endpoint `/my-agency/streams/archive-stream/{stream_id}/participants` và `.../gift-timeline` đều **ĐÃ ĐƯỢC DEPLOY HỢP LỆ** | **PASS (Code/API)** | Backend sẵn sàng |
| **2** | **Kiểm tra dữ liệu Liver của Agency trên STG** | Tài khoản 事務所 `agency123` sở hữu ít nhất 1 Liver đã liên kết | Gọi API `GET /api/v1/agency/list/36` $\rightarrow$ `total_count: 0` (Agency 123 chưa có Liver nào) | **FAIL (Data)** | Thiếu dữ liệu Liver |
| **3** | **Kiểm tra danh sách Archive Streams của Agency trên STG** | Màn `BF100` có ít nhất 1 bản ghi Archive livestream để mở chi tiết `BF300` | Gọi API `POST /api/v1/my-agency/streams/archive-stream` $\rightarrow$ Trả về `{"data": [], "total_count": 0}` (Trống hoàn toàn) | **BLOCKED (Flow)** | Không có Archive để mở `BF300` |
| **4** | **Kiểm tra Danh sách người xem (視聴者一覧) trên màn `BF300`** | Hiển thị người xem + Point, không lỗi `「視聴者情報を取得できませんでした」` | Chưa thể kiểm tra E2E do không có bản ghi Archive để click mở | **BLOCKED** | Chờ Data Seeding |
| **5** | **Kiểm tra Hiệu ứng quà (ギフト演出) khi phát lại Video** | Player hiển thị quà đúng thời điểm, API không bị lỗi HTTP 500 | Chưa thể kiểm tra E2E do chưa có video archive có quà | **BLOCKED** | Chờ Data Seeding |

---

## 3. PHÂN TÍCH NGUYÊN NHÂN & DỮ LIỆU ĐỐI SOÁT KỸ THUẬT

### 3.1. Nguyên nhân gốc của Bug (Root Cause):
1. **Lỗi Danh sách người xem (視聴者一覧):** Trước đây màn hình FE đọc trực tiếp từ Firestore `FirebaseService.getArchiveParticipants`, nhưng document stream trên Firestore có `agency_id = null`, khiến Firestore Security Rules chặn quyền đọc của tài khoản Agency $\rightarrow$ Báo lỗi `「視聴者情報を取得できませんでした」`.
2. **Lỗi Hiệu ứng quà (ギフト演出):** Cloud Functions `getGiftTimeline` trước đây chưa phân quyền cho tài khoản Agency, đồng thời logic xử lý lỗi ánh xạ sai khiến các mã 403/404 bị trả về dưới dạng HTTP 500.

### 3.2. Tiến độ Sửa lỗi từ Đội ngũ Phát triển:
- **Backend (Kim / Nam):** PR #2495 đã deploy lên STG Backend (`api-admin-stg.surrealdolls.com`), bổ sung 2 endpoint có phân quyền SQL scope:
  - `GET /api/v1/my-agency/streams/archive-stream/{stream_id}/participants`
  - `GET /api/v1/my-agency/streams/archive-stream/{stream_id}/gift-timeline`
- **Firebase (Kim / Nam):** PR #522 đã deploy lên Staging, sửa lỗi mapping mã lỗi của `getGiftTimeline`.
- **Frontend (Đức / Uyên):** PR #1743 / #1758 đã deploy lên `admin-stg.surrealdolls.com`.

### 3.3. Log kiểm tra API thực tế trên môi trường STG:
```http
POST https://api-admin-stg.surrealdolls.com/api/v1/agency/auth/login/
Content-Type: application/json
{"email_user_id": "agency123", "password": "..."}

HTTP/2 200 OK
{"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...", "token_type": "bearer"}

---
POST https://api-admin-stg.surrealdolls.com/api/v1/my-agency/streams/archive-stream
Authorization: Bearer <access_token>
Content-Type: application/json
{}

HTTP/2 200 OK
{
  "data": [],
  "total_count": 0,
  "has_more": false,
  "page": 1,
  "items_per_page": 10
}
```

---

## 4. QUY TRÌNH THIẾT LẬP DỮ LIỆU MẪU ĐỂ HOÀN TẤT RETEST E2E

Căn cứ theo Ranh giới đỏ số 3 (*Proactive Preconditions & Data Seeding*), để hoàn thành bước nghiệm thu E2E cuối cùng trên STG:

1. **Bước 1 (Gia nhập Agency):** Dùng 1 tài khoản Liver trên App STG 190 gửi yêu cầu gia nhập vào `agency123` $\rightarrow$ Đăng nhập Web Admin STG duyệt gia nhập.
2. **Bước 2 (Tạo phiên Live kèm Quà):**
   - Liver mở livestream trên App STG.
   - Dùng 1 tài khoản Viewer vào xem buổi live và tặng ít nhất 1 phần quà có hiệu ứng (Gift Event).
   - Liver bấm Kết thúc livestream để hệ thống xử lý đóng gói bản ghi `配信アーカイブ`.
3. **Bước 3 (Thao tác đối soát trên Web):**
   - Đăng nhập `admin-stg.surrealdolls.com/sign-in/agency` bằng `agency123`.
   - Vào `配信管理` $\rightarrow$ `配信アーカイブ` $\rightarrow$ Nhấn 👁 mở archive vừa tạo.
   - Đối soát mục `視聴者一覧` (phải hiện danh sách người xem) và phát video kiểm tra `ギフト演出` (không còn lỗi 500).

---

## 5. MẪU COMMENT CHUẨN SẴN SÀNG CHO BACKLOG

```markdown
【Verify STG - SURREALDOLLS-14995】: PENDING E2E (Chờ tạo Archive Stream có Viewer/Gift)
- Kiểm tra Backend STG: 2 endpoint scoped (/participants & /gift-timeline) đã có mặt trên api-admin-stg.surrealdolls.com (Code/API PASS).
- Hiện trạng dữ liệu STG: Tài khoản 事務所 agency123 hiện có 0 liver và 0 archive stream (total_count=0), chưa thể mở màn BF300 để kiểm tra hiển thị thực tế trên UI.
- Bước tiếp theo: Cần tạo 1 buổi live test trên STG có viewer và quà cho liver thuộc agency123 để sinh archive, sau đó e2e đối soát 視聴者一覧 và video playback.
- Đề xuất trạng thái: Giữ nguyên Need Verify (STG).
```
