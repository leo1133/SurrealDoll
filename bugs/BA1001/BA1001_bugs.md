# BÁO CÁO LỖI KIỂM THỬ THỦ CÔNG - MÀN HÌNH BA1001 (AGENCY FORGOT PASSWORD)

Theo quy chuẩn [06_bug_reporting_rule.md](../../Universal_Rules/06_bug_reporting_rule.md).  
Môi trường kiểm thử: **Dev-Agency** (`https://admin-dev.surrealdolls.com/forgot-password/agency`) theo cấu hình tại [TEST_CONFIG.md](../../TEST_CONFIG.md).

---

## 1. DANH SÁCH BÁO CÁO LỖI CHI TIẾT (DETAILED BUG REPORTS)

### [BUG-1] [BA1001] [Forgot Password API] API gửi mail quên mật khẩu trả về HTTP 500 Server Error khi submit email hợp lệ hoặc chưa đăng ký (ĐÃ FIX - VERIFIED PASS / CLOSED)

- **Trạng thái Retest:** **Closed (Pass)** — Backend đã sửa lỗi gửi mail và xử lý exception. API trả về `HTTP 200 OK` (`{"detail":"パスワード再設定用のメールを送信しました。"}`) và hệ thống điều hướng chính xác sang màn hình **BA1002**.
- **Mã Test Case liên quan:** `[BA1001-17]`, `[BA1001-37]`, `[BA1001-38]`, `[BA1001-41]` (Đã chuyển thành Pass)
- **Mức độ nghiêm trọng (Severity):** Critical (Đã được khắc phục)
- **Môi trường (Environment):** 
  - URL: `https://admin-dev.surrealdolls.com/forgot-password/agency`
  - Trình duyệt: Chromium / Chrome
  - Role: `Agency (Unauthenticated)`
- **Các bước tái hiện (Steps to Reproduce):**
  1. Truy cập màn hình quên mật khẩu Agency: `https://admin-dev.surrealdolls.com/forgot-password/agency`.
  2. Nhập một địa chỉ email Agency hợp lệ đã tồn tại trong DB (ví dụ: `ngadtp@mumesoft.vn`) hoặc email chưa đăng ký.
  3. Click button `送信`.
- **Kết quả kỳ vọng (Expected Result):**
  - API `POST /api/v1/agency/auth/forgot-password` xử lý thành công, trả về HTTP status `200 OK`.
  - Hệ thống gửi email chứa liên kết đặt lại mật khẩu đến hòm thư người dùng.
  - Giao diện tự động chuyển hướng sang màn hình **BA1002** (Màn hình thông báo gửi mail thành công: `メール送信完了`).
- **Kết quả thực tế (Actual Result):**
  - Backend API `POST /api/v1/agency/auth/forgot-password` trả về lỗi **`HTTP 500 Internal Server Error`** (`{"detail":"予期しないサーバーエラーが発生しました。"}`).
  - Frontend bắt lỗi và hiển thị banner thông báo: `サーバーエラーが発生しました。` ở đầu form.
  - Người dùng không nhận được email và màn hình bị giữ nguyên tại `BA1001`, không thể chuyển sang `BA1002`.
- **Bằng chứng đính kèm (Evidence):**
  - File ảnh chụp lỗi (email hợp lệ): [evidence/BA1001/evidence_BA1001_TC37_500_server_error.png](../../evidence/BA1001/evidence_BA1001_TC37_500_server_error.png)
  - File ảnh chụp lỗi (email chưa đăng ký): [evidence/BA1001/evidence_BA1001_TC38_unregistered_500.png](../../evidence/BA1001/evidence_BA1001_TC38_unregistered_500.png)
  - File ảnh chụp lỗi (email master): [evidence/BA1001/evidence_BA1001_TC41_master_account_500.png](../../evidence/BA1001/evidence_BA1001_TC41_master_account_500.png)
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

### [BUG-2] [BA1001] [Email Format Validation] Thông báo lỗi định dạng email hiển thị sai text so với tài liệu đặc tả Spec

- **Backlog Ticket:** [SURREALDOLLS-14374](https://issoh.backlog.com/view/SURREALDOLLS-14374)
- **Mã Test Case liên quan:** `[BA1001-24]`, `[BA1001-25]`, `[BA1001-26]`, `[BA1001-27]`
- **Mức độ nghiêm trọng (Severity):** Minor (Wording mismatch)
- **Môi trường (Environment):** 
  - URL: `https://admin-dev.surrealdolls.com/forgot-password/agency`
  - Trình duyệt: Chromium / Chrome
- **Các bước tái hiện (Steps to Reproduce):**
  1. Truy cập `https://admin-dev.surrealdolls.com/forgot-password/agency`.
  2. Nhập email sai định dạng (ví dụ: thiếu `@`, thiếu domain, thiếu local-part hoặc có space ở giữa).
  3. Click button `送信`.
- **Kết quả kỳ vọng (Expected Result):**
  - Viền ô chuyển màu đỏ.
  - Dưới ô hiển thị thông báo lỗi nguyên văn theo Spec: `無効なメールアドレスです。`.
- **Kết quả thực tế (Actual Result):**
  - Dưới ô hiển thị thông báo lỗi: `有効なメールアドレスを入力してください。`.
- **Bằng chứng đính kèm (Evidence):**
  - File ảnh chụp lỗi (thiếu @): [evidence/BA1001/evidence_BA1001_TC_format_BA1001-24.png](../../evidence/BA1001/evidence_BA1001_TC_format_BA1001-24.png)
  - File ảnh chụp lỗi (thiếu domain): [evidence/BA1001/evidence_BA1001_TC_format_BA1001-25.png](../../evidence/BA1001/evidence_BA1001_TC_format_BA1001-25.png)
  - File ảnh chụp lỗi (thiếu local-part): [evidence/BA1001/evidence_BA1001_TC_format_BA1001-26.png](../../evidence/BA1001/evidence_BA1001_TC_format_BA1001-26.png)
  - File ảnh chụp lỗi (có space): [evidence/BA1001/evidence_BA1001_TC_format_BA1001-27.png](../../evidence/BA1001/evidence_BA1001_TC_format_BA1001-27.png)
  - Bằng chứng DOM HTML:
    ```html
    <p data-slot="form-message" id="_R_15klubsnpflb_-form-item-message" class="text-danger text-xs">有効なメールアドレスを入力してください。</p>
    ```

---

## 2. BẢNG TỔNG HỢP DANH SÁCH LỖI & KẾT QUẢ RETEST (FAIL & RETEST SUMMARY TABLE)

| TC ID | Control / Chức năng | Các bước tái hiện (Steps) | Expected Result | Actual Result | Mức độ | Trạng thái Retest | Bug ID |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| `[BA1001-17]` | Nhập Email Owner | 1. Vào `/forgot-password/agency`<br>2. Nhập `ngadtp@mumesoft.vn`<br>3. Bấm 送信 | Gửi email thành công, chuyển sang BA1002 | API 200 OK, chuyển sang BA1002 thành công | Critical | **Closed (Pass)** | - |
| `[BA1001-24]` | Format thiếu @ | 1. Nhập `example.com`<br>2. Bấm 送信 | Hiển thị: `無効なメールアドレスです。` | Hiển thị: `有効なメールアドレスを入力してください。` | Minor | **Open (Fail)** | [SURREALDOLLS-14374](https://issoh.backlog.com/view/SURREALDOLLS-14374) |
| `[BA1001-25]` | Format thiếu domain | 1. Nhập `user@`<br>2. Bấm 送信 | Hiển thị: `無効なメールアドレスです。` | Hiển thị: `有効なメールアドレスを入力してください。` | Minor | **Open (Fail)** | [SURREALDOLLS-14374](https://issoh.backlog.com/view/SURREALDOLLS-14374) |
| `[BA1001-26]` | Format thiếu local-part | 1. Nhập `@example.com`<br>2. Bấm 送信 | Hiển thị: `無効なメールアドレスです。` | Hiển thị: `有効なメールアドレスを入力してください。` | Minor | **Open (Fail)** | [SURREALDOLLS-14374](https://issoh.backlog.com/view/SURREALDOLLS-14374) |
| `[BA1001-27]` | Format space ở giữa | 1. Nhập `user name@example.com`<br>2. Bấm 送信 | Hiển thị: `無効なメールアドレスです。` | Hiển thị: `有効なメールアドレスを入力してください。` | Minor | **Open (Fail)** | [SURREALDOLLS-14374](https://issoh.backlog.com/view/SURREALDOLLS-14374) |
| `[BA1001-37]` | Button 送信 / API | 1. Nhập email hợp lệ<br>2. Bấm 送信 | Chuyển sang màn BA1002, gửi mail reset | API 200 OK, chuyển sang BA1002 thành công | Critical | **Closed (Pass)** | - |
| `[BA1001-38]` | Anti-enumeration chưa đăng ký | 1. Nhập email chưa đăng ký<br>2. Bấm 送信 | Vẫn chuyển sang BA1002 | API 200 OK, chuyển sang BA1002 an toàn | Critical | **Closed (Pass)** | - |
| `[BA1001-41]` | Anti-enumeration Master | 1. Nhập `admin@admin.com`<br>2. Bấm 送信 | Vẫn chuyển sang BA1002 | API 200 OK, chuyển sang BA1002 an toàn | Critical | **Closed (Pass)** | - |
