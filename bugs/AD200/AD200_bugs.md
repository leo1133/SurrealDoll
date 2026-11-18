# BÁO CÁO LỖI VÀ KẾT QUẢ XÁC MINH RETEST - MÀN HÌNH AD200 (AGENCY CREATE) / BA1001

Theo quy chuẩn [06_bug_reporting_rule.md](../../Universal_Rules/06_bug_reporting_rule.md) & [GEMINI.md](../../GEMINI.md).  
Môi trường kiểm thử: **Dev** (`https://admin-dev.surrealdolls.com`) và **Staging** (`https://admin-stg.surrealdolls.com`).

---

## 1. CHI TIẾT BUG VÀ KẾT QUẢ RETEST

### [BUG-1] [AD200 / BB200 / BA1001] Cho phép nhập email có đuôi +@gmail.com khi tạo mới agency/admin agency nhưng báo lỗi khi reset mật khẩu

- **Backlog Ticket:** [SURREALDOLLS-14376](https://issoh.backlog.com/view/SURREALDOLLS-14376)
- **Trạng thái Retest:** **Closed (Pass)** — Hệ thống đã cập nhật bộ lọc kiểm tra định dạng email (email regex validation) đồng bộ trên toàn bộ form tạo mới (AD200) và quên mật khẩu (BA1001). Cụ thể: các email kết thúc bằng `+@gmail.com` (như `test+@gmail.com`, `agency+@gmail.com`, `+@gmail.com`) đã bị chặn và báo lỗi định dạng ngay tại form tạo mới, không cho phép tạo tài khoản có định dạng không hợp lệ.
- **Mức độ nghiêm trọng (Severity):** Major (Đã được khắc phục)
- **Môi trường xác minh (Environment):**
  - Dev Admin: `https://admin-dev.surrealdolls.com/agencies/create`
  - STG Admin: `https://admin-stg.surrealdolls.com/agencies/create`
  - Dev Agency Forgot Password: `https://admin-dev.surrealdolls.com/forgot-password/agency`
  - STG Agency Forgot Password: `https://admin-stg.surrealdolls.com/forgot-password/agency`

### Kết quả kiểm tra đối chiếu thực tế (Actual Verification Results):

1. **Màn hình tạo mới Agency (AD200):**
   - Khi nhập email có đuôi `+@gmail.com` (ví dụ: `test+@gmail.com`, `agency+@gmail.com`, `+@gmail.com`):
     - **STG:** Hệ thống viền đỏ ô email và hiển thị thông báo lỗi: `無効なメールアドレスです。`. Chặn submit thành công.
     - **DEV:** Hệ thống viền đỏ ô email và hiển thị thông báo lỗi: `有効なメールアドレスを入力してください。`. Chặn submit thành công.
   - Khi nhập email hợp lệ có subaddressing đúng chuẩn (ví dụ: `test+1@gmail.com`, `test+sub@gmail.com`): Hệ thống chấp nhận hợp lệ không báo lỗi format.

2. **Màn hình Quên mật khẩu Agency (BA1001):**
   - Khi nhập `test+@gmail.com`, `agency+@gmail.com`, hoặc `+@gmail.com`: Hệ thống báo lỗi `無効なメールアドレスです。` và chặn submit.
   - Khi nhập subaddressing hợp lệ có tag (ví dụ: `test+1@gmail.com`, `test+sub@gmail.com`): Hệ thống gửi yêu cầu và điều hướng sang BA1002 thành công.

- **Bằng chứng đính kèm (Evidence Screenshots):**
  - Chặn email `test+@gmail.com` tại AD200 trên STG: [evidence/AD200/evidence_AD200_SURREALDOLLS_14376_create_agency_blocks_plus_email_STG.png](../../evidence/AD200/evidence_AD200_SURREALDOLLS_14376_create_agency_blocks_plus_email_STG.png)
  - Chặn email `test+@gmail.com` tại AD200 trên DEV: [evidence/AD200/evidence_AD200_SURREALDOLLS_14376_create_agency_blocks_plus_email_DEV.png](../../evidence/AD200/evidence_AD200_SURREALDOLLS_14376_create_agency_blocks_plus_email_DEV.png)
  - Chặn email `test+@gmail.com` tại BA1001: [evidence/BA1001/evidence_BA1001_SURREALDOLLS_14376_forgot_password_blocks_plus_email.png](../../evidence/BA1001/evidence_BA1001_SURREALDOLLS_14376_forgot_password_blocks_plus_email.png)

---

## 2. BẢNG TỔNG HỢP KẾT QUẢ RETEST

| Bug Ticket | Chức năng / Control | Input thử nghiệm | Kết quả mong đợi | Kết quả thực tế sau Retest | Trạng thái Retest | Evidence Link |
| :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| **SURREALDOLLS-14376** | Tạo mới Agency (AD200) | `test+@gmail.com` | Chặn tạo mới, báo lỗi định dạng email | Viền đỏ ô nhập, báo lỗi định dạng (STG: `無効なメールアドレスです。`, DEV: `有効なメールアドレスを入力してください。`), chặn submit | **Pass / Closed** | [evidence_AD200_STG.png](../../evidence/AD200/evidence_AD200_SURREALDOLLS_14376_create_agency_blocks_plus_email_STG.png)<br>[evidence_AD200_DEV.png](../../evidence/AD200/evidence_AD200_SURREALDOLLS_14376_create_agency_blocks_plus_email_DEV.png) |
| **SURREALDOLLS-14376** | Quên mật khẩu (BA1001) | `test+@gmail.com` | Báo lỗi định dạng email không hợp lệ | Viền đỏ ô nhập, hiển thị thông báo lỗi `無効なメールアドレスです。` | **Pass / Closed** | [evidence_BA1001_plus.png](../../evidence/BA1001/evidence_BA1001_SURREALDOLLS_14376_forgot_password_blocks_plus_email.png) |
