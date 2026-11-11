# BÁO CÁO LỖI KIỂM THỬ THỦ CÔNG - MÀN HÌNH BA1003 (AGENCY RESET PASSWORD)

Theo quy chuẩn [06_bug_reporting_rule.md](Universal_Rules/06_bug_reporting_rule.md).  
Môi trường kiểm thử: **Dev-Agency** (`https://admin-dev.surrealdolls.com/reset-password/agency`) theo cấu hình tại [TEST_CONFIG.md](TEST_CONFIG.md).

---

## 1. DANH SÁCH BÁO CÁO LỖI CHI TIẾT (DETAILED BUG REPORTS)

### [BUG-1] [BA1003] [Token Verification & Reset Password API] Cả 2 API `GET` xác thực token và `POST` đặt lại mật khẩu đều trả về HTTP 500 Server Error với link kích hoạt PEM3 hợp lệ

- **Mã Test Case liên quan:** `[BA1003-1]`, `[BA1003-2]`, `[BA1003-43]`, `[BA1003-55]` (chặn đứng tiếp luồng `[BA100-79]`)
- **Mức độ nghiêm trọng (Severity):** Critical (Blocker - Người dùng nhận mail kích hoạt PEM3 hoặc email reset không thể mở form thiết lập mật khẩu để kích hoạt tài khoản)
- **Môi trường (Environment):** 
  - URL kích hoạt: `https://admin-dev.surrealdolls.com/reset-password/agency?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im5nYWR0cCsyQG11bWVzb2Z0LnZuIiwiYXVkIjoiYWdlbmN5IiwiZXhwIjoxNzk0NDU3MjU2LCJ0b2tlbl90eXBlIjoicmVzZXRfcGFzc3dvcmQiLCJqdGkiOiIyNDZjNDBjYS1kMzZkLTRiMzgtYjVmYy1jYmVkZThjNTk5ODMifQ.bTpDYb-OSnW-jsz-H36x71zffxLIHZbJ56DwxtnRpoQ`
  - Tài khoản: `agency02` (`ngadtp+2@mumesoft.vn`)
  - Trình duyệt: Chromium / Chrome
  - Role: `Agency Owner (First-time password setup via PEM3)`
- **Các bước tái hiện (Steps to Reproduce):**
  1. Mở email kích hoạt tài khoản PEM3 gửi đến hòm thư `ngadtp+2@mumesoft.vn` (thời hạn 24h).
  2. Click vào đường link đặt mật khẩu: `https://admin-dev.surrealdolls.com/reset-password/agency?token=...`.
  3. Hoặc gửi trực tiếp request `POST /api/v1/agency/auth/reset-password` với token hợp lệ và mật khẩu mới hợp lệ thỏa mãn CMR43.
- **Kết quả kỳ vọng (Expected Result):**
  - Bước 2: API `GET /api/v1/agency/auth/reset-password?token=...` trả về HTTP 200 kèm payload `{ message, email, token }`. Giao diện màn hình `BA1003` hiển thị form đặt mật khẩu gồm 2 ô nhập mật khẩu và nút submit `パスワード再設定`.
  - Bước 3: Người dùng nhập mật khẩu mới và mật khẩu xác nhận hợp lệ, click submit thì BE cập nhật mật khẩu, kích hoạt tài khoản và chuyển hướng về màn đăng nhập `BA100`.
- **Kết quả thực tế (Actual Result):**
  - Tại Bước 2: API `GET /api/v1/agency/auth/reset-password?token=...` trả về lỗi **`HTTP 500 Internal Server Error`** (`{"detail":"予期しないサーバーエラーが発生しました。"}`).
  - Frontend bắt lỗi 500 và hiển thị màn hình thông báo lỗi hệ thống:
    - Text: `サーバーエラーが発生しました。`
    - 2 button: `再試行` và `ログインへ戻る`
    - Form đặt lại mật khẩu hoàn toàn không được hiển thị.
  - Tại Bước 3: Khi gọi trực tiếp `POST /api/v1/agency/auth/reset-password` với token trên và mật khẩu mới hợp lệ, BE cũng trả về **`HTTP 500 Internal Server Error`** (`{"detail":"予期しないサーバーエラーが発生しました。"}`).
- **Bằng chứng đính kèm (Evidence):**
  - File ảnh chụp màn hình: [evidence/evidence_BA1003_500_server_error_PEM3.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_BA1003_500_server_error_PEM3.png)
  - Log curl trực tiếp kiểm chứng:
    ```bash
    curl -i "https://api-admin-dev.surrealdolls.com/api/v1/agency/auth/reset-password?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    HTTP/2 500
    {"detail":"予期しないサーバーエラーが発生しました。"}
    ```
    ```bash
    curl -i -X POST "https://api-admin-dev.surrealdolls.com/api/v1/agency/auth/reset-password" \
      -H "Content-Type: application/json" \
      -d '{"token":"...","new_password":"ValidPassword123!","confirm_password":"ValidPassword123!"}'
    HTTP/2 500
    {"detail":"予期しないサーバーエラーが発生しました。"}
    ```

---

### [BUG-2] [BA1003] [Error Placement] Khi BE trả về lỗi 400 (MSG261), thông báo lỗi hiển thị ở banner đầu form thay vì dưới ô `新しいパスワード`

- **Mã Test Case liên quan:** `[BA1003-50]`, `[BA1003-51]`, `[BA1003-52]`
- **Mức độ nghiêm trọng (Severity):** Medium (Sai lệch vị trí hiển thị so với đặc tả chi tiết tại checklist ticket SURREALDOLLS-14231)
- **Môi trường (Environment):** 
  - URL: `https://admin-dev.surrealdolls.com/reset-password/agency`
  - Trình duyệt: Chromium / Chrome
- **Đặc tả yêu cầu (Specification):**
  - Theo mục 2 trong checklist việc cần làm của ticket `SURREALDOLLS-14231`:
    > *"Lỗi BE: 422 -> MSG13, 400 -> MSG261, hiện dưới ô 新しいパスワード."*
- **Các bước tái hiện (Steps to Reproduce):**
  1. Mở màn hình `BA1003` với token hợp lệ.
  2. Nhập mật khẩu mới trùng với mật khẩu cũ (BE trả về 400 với thông báo MSG261: `過去に使用したパスワードは設定できません。`).
  3. Click button `パスワード再設定`.
- **Kết quả kỳ vọng (Expected Result):**
  - Viền ô `新しいパスワード` đổi màu đỏ.
  - Thông báo lỗi MSG261 `過去に使用したパスワードは設定できません。` hiển thị ngay **dưới ô `新しいパスワード`** (cùng vị trí với thông báo lỗi validation MSG13).
- **Kết quả thực tế (Actual Result):**
  - Lỗi MSG261 hiển thị bên trong banner alert chung ở **đầu form** (`<div class="mb-5 empty:hidden"><div role="alert"...`), nằm phía trên ô `新しいパスワード`.
  - Phía dưới ô `新しいパスワード` không hiển thị thông báo lỗi này.
- **Bằng chứng đính kèm (Evidence):**
  - File ảnh chụp màn hình: [evidence/evidence_BA1003_BE_400_placed_at_top_not_under_input.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_BA1003_BE_400_placed_at_top_not_under_input.png)
  - DOM snippet:
    ```html
    <div class="mb-5 empty:hidden">
      <div role="alert" class="border-danger-border bg-danger-soft text-danger flex w-full items-start gap-2 rounded-lg border-[0.5px] px-3 py-2.5 text-[13px] leading-[1.6]">
        <svg ...></svg>
        <span class="min-w-0 flex-1">過去に使用したパスワードは設定できません。</span>
      </div>
    </div>
    <div data-slot="form-item" class="flex flex-col justify-center mb-5 gap-[6px]">
      <label ...>新しいパスワード </label>
      <input ...>
      <!-- Thiếu text lỗi MSG261 dưới ô -->
      <p data-slot="form-description" ...>8文字以上・英大文字・小文字・数字・記号を各1文字以上</p>
    </div>
    ```
