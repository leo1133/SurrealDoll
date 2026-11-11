# BÁO CÁO LỖI KIỂM THỬ THỦ CÔNG - MÀN HÌNH BA1001 (AGENCY FORGOT PASSWORD)

Theo quy chuẩn [06_bug_reporting_rule.md](Universal_Rules/06_bug_reporting_rule.md).  
Môi trường kiểm thử: **Dev-Agency** (`https://admin-dev.surrealdolls.com/forgot-password/agency`) theo cấu hình tại [TEST_CONFIG.md](TEST_CONFIG.md).

---

## 1. DANH SÁCH BÁO CÁO LỖI CHI TIẾT (DETAILED BUG REPORTS)

### [BUG-1] [BA1001] [Forgot Password API] API gửi mail quên mật khẩu trả về HTTP 500 Server Error khi submit email hợp lệ

- **Mã Test Case liên quan:** `[BA1001-26]`, `[BA1001-27]`, `[BA1001-38]`
- **Mức độ nghiêm trọng (Severity):** Critical (Chặn đứng luồng khôi phục mật khẩu sang BA1002)
- **Môi trường (Environment):** 
  - URL: `https://admin-dev.surrealdolls.com/forgot-password/agency`
  - Trình duyệt: Chromium / Chrome
  - Role: `Agency (Unauthenticated / User forgot password)`
- **Các bước tái hiện (Steps to Reproduce):**
  1. Truy cập màn hình quên mật khẩu Agency: `https://admin-dev.surrealdolls.com/forgot-password/agency`.
  2. Nhập một địa chỉ email Agency hợp lệ đã tồn tại trong DB (ví dụ: `ngadtp@mumesoft.vn`).
  3. Click button `送信`.
- **Kết quả kỳ vọng (Expected Result):**
  - API `POST /api/v1/agency/auth/forgot-password` xử lý thành công, trả về HTTP status `200 OK`.
  - Hệ thống gửi email chứa liên kết đặt lại mật khẩu đến hòm thư người dùng.
  - Giao diện tự động chuyển hướng sang màn hình **BA1002** (Màn hình thông báo gửi mail thành công: `パスワード再設定用のメールを送信しました`).
- **Kết quả thực tế (Actual Result):**
  - Backend API `POST /api/v1/agency/auth/forgot-password` trả về lỗi **`HTTP 500 Internal Server Error`**.
  - Frontend bắt lỗi và hiển thị banner thông báo: `サーバーエラーが発生しました。` ở đầu form.
  - Người dùng không nhận được email và màn hình bị giữ nguyên tại `BA1001`, không thể chuyển sang `BA1002`.
- **Bằng chứng đính kèm (Evidence):**
  - File ảnh chụp lỗi: `evidence/evidence_BA1001_TC26_R2_500_server_error.png`
  - Bằng chứng API Log & Response:
    ```http
    POST /api/v1/agency/auth/forgot-password HTTP/2
    Host: api-admin-dev.surrealdolls.com
    Content-Type: application/json
    Body: {"email": "ngadtp@mumesoft.vn"}

    HTTP/2 500 Internal Server Error
    {"detail":"予期しないサーバーエラーが発生しました。"}
    ```
  - Bằng chứng DOM HTML:
    ```html
    <div role="alert" class="border-danger-border bg-danger-soft text-danger flex w-full items-start gap-2 rounded-lg border-[0.5px] px-3 py-2.5 text-[13px] leading-[1.6]">
      <span class="min-w-0 flex-1">サーバーエラーが発生しました。</span>
    </div>
    ```

---

## 2. BẢNG TỔNG HỢP DANH SÁCH LỖI (FAIL SUMMARY TABLE)

| TC ID | Control / Chức năng | Các bước tái hiện (Steps) | Expected Result | Actual Result | Mức độ | File Evidence (Unique) & DOM Log | Bug ID |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `[BA1001-26]` | Button 送信 / Gọi API | 1. Vào `/forgot-password/agency`<br>2. Nhập email hợp lệ<br>3. Bấm 送信 | Gửi mail thành công, chuyển sang BA1002 | API trả về 500 Server Error, hiện toast/banner lỗi, không chuyển trang | Critical | `evidence_BA1001_TC26_R2_500_server_error.png`<br>`API 500: 予期しないサーバーエラーが発生しました。` | *(Để trống)* |
