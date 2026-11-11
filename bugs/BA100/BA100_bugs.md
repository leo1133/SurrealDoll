# BÁO CÁO LỖI KIỂM THỬ THỦ CÔNG - MÀN HÌNH BA100 (AGENCY LOGIN)

Theo quy chuẩn [06_bug_reporting_rule.md](../../Universal_Rules/06_bug_reporting_rule.md).  
Môi trường kiểm thử: **Dev-Agency** (`https://admin-dev.surrealdolls.com/sign-in/agency`) theo cấu hình tại [TEST_CONFIG.md](../../TEST_CONFIG.md).

---

## 1. TỔNG QUAN KẾT QUẢ KIỂM THỬ (TEST SUMMARY)

- **Tổng số ca kiểm thử:** 79 ca
- **Pass (Đạt):** 57 ca (72.2%)
- **Fail (Lỗi):** 0 ca (0%)
- **Blocked / Pending (Chặn bởi dữ liệu):** 22 ca (27.8%)
  - 14 ca yêu cầu điều kiện tiên quyết (Pre-condition) về tài khoản đặc thù chưa có trên môi trường: tài khoản Agency/Admin con bị `停止中` (tạm dừng), tài khoản bị xóa, tài khoản Admin con, đổi ID/Email chưa xác thực PEM4.
  - 7 ca yêu cầu tiền đề tài khoản có mật khẩu quá hạn > 30 ngày theo quy tắc CMR68 (chưa được seed dữ liệu mẫu trong DB).
  - 1 ca `[BA100-79]` bị chặn bởi BUG-1 tại màn hình BA1003 (API đặt mật khẩu lần đầu trả về 500 nên tài khoản tạo mới chưa hoàn tất kích hoạt).

---

## 2. DANH SÁCH YÊU CẦU DỮ LIỆU KIỂM THỬ (TEST DATA SEEDING REQUIREMENTS)

Theo quy chuẩn [Universal_Rules/04_manual_test_execution_rule.md](../../Universal_Rules/04_manual_test_execution_rule.md) Section 3.2:

1. **Tài khoản Agency tạm dừng (`停止中`):**
   - 01 tài khoản Agency ở trạng thái `status = 停止中` (hoặc `status_code = suspended`) để test `[BA100-6]`, `[BA100-62]`, `[BA100-65]`.
2. **Tài khoản Admin con (`事務所管理者`):**
   - 01 tài khoản Admin con ở trạng thái `利用中` và 01 tài khoản ở trạng thái `停止中` để test `[BA100-7]`, `[BA100-9]`, `[BA100-25]`, `[BA100-26]`, `[BA100-63]`.
3. **Tài khoản hết hạn mật khẩu > 30 ngày (CMR68):**
   - Cần cập nhật trường `password_updated_at` trong Database về mốc thời gian quá 30 ngày trước (ví dụ: lùi về 45 ngày trước) đối với 01 tài khoản Owner và 01 tài khoản Admin con để thực thi các ca kiểm thử: `[BA100-72]`, `[BA100-73]`, `[BA100-74]`, `[BA100-75]`, `[BA100-76]`, `[BA100-77]`, `[BA100-78]`.
