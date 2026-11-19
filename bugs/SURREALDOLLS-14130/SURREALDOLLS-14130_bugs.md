# BÁO CÁO XÁC MINH LỖI TICKET SURREALDOLLS-14130
## [BUG] - [BB101] - Hệ thống không kiểm tra trùng lặp email và cho phép lưu email đã tồn tại
### Áp dụng: Master Agent Policy (GEMINI.md) & Trụ cột 6 (06_bug_reporting_rule.md)

---

## 1. THÔNG TIN TỔNG QUAN

- **Ticket ID:** [SURREALDOLLS-14130](https://issoh.backlog.com/view/SURREALDOLLS-14130)
- **Màn hình / Phân hệ:** `BB101` - 事務所詳細 / 情報 (Agency Detail / Info)
- **Môi trường định tuyến:** **DEV** (URL: `https://admin-dev.surrealdolls.com/agencies/info`)
- **Tài khoản kiểm thử:** Agency: `agency01` | `Phgnga1998@` (HTTP Basic Auth: `suriaru` / `suriaru`)
- **Trạng thái Backlog tiếp nhận:** `Need Verify (Dev)`
- **Thời lượng ước tính (Est):** 0.15h (9 phút)
- **Thời lượng thực tế (Actual):** 0.20h (12 phút)
- **Tester:** `NgaDTP` / `Antigravity QA`
- **Ngày kiểm tra:** 18/11/2026
- **Kết luận:** <span style="color:green; font-weight:bold;">VERIFIED PASS (ĐÃ SỬA XONG / RESOLVED)</span>

---

## 2. KẾT QUẢ ĐỐI SOÁT CHI TIẾT

| Tiêu chí | Mô tả kiểm thử thực tế | Kết luận |
| :--- | :--- | :---: |
| **Các bước tái hiện** | 1. Đăng nhập Agency Dev: `https://admin-dev.surrealdolls.com/sign-in/agency`<br>2. Truy cập màn hình BB101: `/agencies/info`<br>3. Tại trường `メールアドレス` (contact_email), nhập email đã tồn tại trong hệ thống: `admin@admin.com`<br>4. Nhấp nút `保存` | **PASS** |
| **Kết quả kỳ vọng (Expected)** | Hệ thống chặn lại không cho lưu thành công; API trả về mã lỗi 4xx kèm thông báo MSG14; Frontend hiển thị thông báo lỗi `このメールアドレスは既に登録されています。` (hoặc `このメールアドレスは登録済みです。`) ngay dưới ô input. | **PASS** |
| **Kết quả thực tế cũ (Old Actual)** | API PATCH `/api/v1/my-agency/` trả về status 200 và cho phép cập nhật đè email đã tồn tại, không có validation trùng lặp. | **FAIL (Old)** |
| **Kết quả thực tế mới (New Actual)** | 1. API `PATCH /api/v1/my-agency/` trả về HTTP `422 Unprocessable Entity` với body: `{"detail":"このメールアドレスは登録済みです。"}`.<br>2. Frontend mapping chính xác lỗi inline ngay dưới ô input `メールアドレス`: `「このメールアドレスは登録済みです。」`.<br>3. Form không bị lưu, dữ liệu được bảo vệ toàn vẹn. | <span style="color:green; font-weight:bold;">PASS</span> |

---

## 3. BẰNG CHỨNG XÁC THỰC TRỰC QUAN (VISUAL EVIDENCE & DOM/API LOG)

- **Ảnh bằng chứng có viền nổi bật (Overview with Bounding Box):**
  - File: [evidence_BB101_SURREALDOLLS-14130_DEV_PASS_duplicate_email.png](file:///home/nga/Documents/SurrealDoll/evidence/BB101/evidence_BB101_SURREALDOLLS-14130_DEV_PASS_duplicate_email.png)
  - Đánh dấu: Khung viền xanh lá `#16a34a` (3px) bao quanh ô input `メールアドレス` và thông báo lỗi `このメールアドレスは登録済みです。` kèm badge `🔍 RE-TEST PASS: BÁO LỖI TRÙNG EMAIL MSG14 [SURREALDOLLS-14130]`.

- **API Request & Response Log:**
  ```http
  PATCH /api/v1/my-agency/ HTTP/1.1
  Host: api-admin-dev.surrealdolls.com
  Content-Type: application/json
  Authorization: Bearer <access_token>

  {
    "contact_email": "admin@admin.com"
  }

  HTTP/1.1 422 Unprocessable Entity
  Content-Type: application/json

  {
    "detail": "このメールアドレスは登録済みです。"
  }
  ```

---

## 4. ĐỀ XUẤT ĐỒNG BỘ BACKLOG

- **Trạng thái mới:** `Resolved` (hoặc `WaitBuid(STG)-PM`)
- **Assignee đề xuất:** `Mume_ハイ（フロントエンド）` / `Mume_ナム（バックエンド）`
- **Mẫu comment Backlog:**
  > QA đã re-test trên môi trường DEV (Web Agency: `/agencies/info`). Khi nhập email đã tồn tại (`admin@admin.com`) và bấm Lưu, API trả về 422 kèm detail `このメールアドレスは登録済みです。` và UI hiển thị thông báo lỗi inline chính xác dưới ô input. Hệ thống đã chặn thành công trường hợp trùng email. Kết quả: PASS. Đính kèm ảnh bằng chứng highlight.
