# BÁO CÁO KẾT QUẢ KIỂM THỬ THỦ CÔNG - MÀN HÌNH BA1003 (AGENCY RESET PASSWORD)

Theo quy chuẩn [06_bug_reporting_rule.md](../../Universal_Rules/06_bug_reporting_rule.md).  
Môi trường kiểm thử: **Dev-Agency** (`https://admin-dev.surrealdolls.com/reset-password/agency`) theo cấu hình tại [TEST_CONFIG.md](../../TEST_CONFIG.md).

---

## 1. TỔNG QUAN KẾT QUẢ RETEST ROUND 2 (RETEST SUMMARY)

- **Tổng số ca kiểm thử:** 55 ca
- **Pass (Đạt):** **53 ca** (100% các ca kiểm thử giao diện, validation và API submit)
- **Fail (Lỗi):** **0 ca**
- **Impact (Bị ảnh hưởng):** **0 ca** (Toàn bộ 48 ca bị ảnh hưởng trước đây đã được giải phóng hoàn toàn!)
- **Blocked (Chờ dữ liệu kích hoạt PEM3/PEM7):** **2 ca** (`[BA1003-2]`, `[BA1003-3]`)
- **Tỷ lệ Pass (trên số ca thực thi được):** **100.0%** (53/53 ca)
- **Tình trạng Bug:** **0 Bug Open.** Toàn bộ các lỗi trước đây đã được Backend & Frontend fix triệt để và nghiệm thu thành công trên môi trường live!

---

## 2. LỊCH SỬ XỬ LÝ VÀ NGHIỆM THU CÁC LỖI (BUG STATUS HISTORY)

### [BUG-1] [BA1003] [CLOSED - PASS] API GET xác thực token và POST đặt lại mật khẩu trả về HTTP 500
- **Trạng thái:** **CLOSED (PASS)**
- **Xác thực Live:**
  - `GET /api/v1/agency/auth/reset-password?token=...`: Trả về **`HTTP 200 OK`**, form đặt lại mật khẩu hiển thị đầy đủ và hoàn thiện theo design Figma.
  - `POST /api/v1/agency/auth/reset-password`: Trả về **`HTTP 200 OK`** (`{"detail":"パスワードが正常に変更されました。"}`), cập nhật mật khẩu thành công trong DB và tự động chuyển hướng về màn đăng nhập `BA100`.
  - Mật khẩu mới vừa đặt (`Surreal2026@AgencyReset!`) đã được kiểm thử đăng nhập thực tế tại `BA100` thành công chuyển hướng vào trang quản trị (`https://admin-dev.surrealdolls.com/agencies/info`).

### [BUG-2] [BA1003] [CLOSED - PASS] Xử lý validation & hiển thị thông báo lỗi
- **Trạng thái:** **CLOSED (PASS)**
- **Xác thực Live:**
  - Đã kiểm tra đầy đủ các ca validation: để trống cả 2 ô, để trống từng ô, mật khẩu dưới 8 ký tự, thiếu chữ hoa, thiếu chữ thường, thiếu chữ số, thiếu ký tự đặc biệt, mật khẩu xác nhận không khớp, mật khẩu xác nhận khác chữ hoa thường.
  - Tất cả đều hiển thị viền đỏ và text lỗi cảnh báo chuẩn xác dưới ô nhập liệu.

### [BUG-3] [BA1003] [CLOSED - PASS] Màn hình blank container khi truy cập token không hợp lệ
- **Trạng thái:** **CLOSED (PASS)**
- **Xác thực Live:**
  - Khi truy cập link không có token, token giả mạo, hoặc token đã qua sử dụng, hệ thống hiển thị chính xác Error Card: `パスワード再設定リンクが無効または期限切れです。` kèm nút `ログインへ戻る`. Click nút điều hướng chuẩn về `BA100`.

---

## 3. DANH SÁCH BẰNG CHỨNG THỰC TẾ (LIVE EVIDENCE FILES)

| Tên File | Mô tả bằng chứng | Đường dẫn |
| :--- | :--- | :--- |
| `evidence_BA1003_form_loaded.png` | Màn hình tải form hợp lệ (Header, Card, 2 ô mật khẩu, rule text tĩnh, button submit) | [Xem ảnh](../../evidence/BA1003/evidence_BA1003_form_loaded.png) |
| `evidence_BA1003_empty_submit.png` | Lỗi viền đỏ và thông báo lỗi khi để trống form submit | [Xem ảnh](../../evidence/BA1003/evidence_BA1003_empty_submit.png) |
| `evidence_BA1003_TC_mismatch.png` | Lỗi mật khẩu xác nhận không khớp: `パスワードと確認用のパスワードが一致しません。` | [Xem ảnh](../../evidence/BA1003/evidence_BA1003_TC_mismatch.png) |
| `evidence_BA1003_TC_be_200_success.png` | Submit đổi mật khẩu thành công (API 200) và điều hướng về BA100 | [Xem ảnh](../../evidence/BA1003/evidence_BA1003_TC_be_200_success.png) |
