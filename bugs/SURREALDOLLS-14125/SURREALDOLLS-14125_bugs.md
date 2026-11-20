# BÁO CÁO XÁC MINH LỖI TICKET SURREALDOLLS-14125
## [BUG] - [BB300] - Sai lệch nội dung thông báo lỗi định dạng email khi chỉnh sửa quản trị viên
### Áp dụng: Master Agent Policy (GEMINI.md) & Trụ cột 6 (06_bug_reporting_rule.md)

---

## 1. THÔNG TIN TỔNG QUAN

- **Ticket ID:** [SURREALDOLLS-14125](https://issoh.backlog.com/view/SURREALDOLLS-14125)
- **Màn hình:** BB300 - 事務所管理者詳細 / 編集 (Agency Administrator Detail / Edit)
- **Môi trường định tuyến:** **DEV** (Dev-Agency Web: `https://admin-dev.surrealdolls.com/sign-in/agency`)
- **Trạng thái Backlog tiếp nhận:** `Need Verify (Dev)`
- **Thời lượng ước tính (Est):** 0.15h (9 phút)
- **Thời lượng thực tế (Actual):** 0.20h (12 phút)
- **Tester:** `ngadtp` / `Antigravity QA`
- **Ngày kiểm tra:** 18/11/2026
- **Kết luận:** <span style="color:green; font-weight:bold;">VERIFIED PASS (ĐÃ SỬA XONG / RESOLVED)</span>

---

## 2. KẾT QUẢ ĐỐI SOÁT CHI TIẾT (RE-TEST RESULT)

| STT | Ca kiểm thử / Dữ liệu nhập | Đặc tả kỳ vọng (Expected) | Thực tế trên live DEV (Actual) | Đánh giá | Bằng chứng kiểm thử (Evidence) |
| :---: | :--- | :--- | :--- | :---: | :--- |
| 1 | **Thiếu domain**<br>`test@` | Hiển thị thông báo CMMSG30:<br>`「有効なメールアドレスを入力してください。」` | Hiển thị chính xác:<br>`「有効なメールアドレスを入力してください。」` | <span style="color:green; font-weight:bold;">PASS</span> | [evidence_BB300_SURREALDOLLS-14125_DEV_PASS_no_domain.png](file:///home/nga/Documents/SurrealDoll/evidence/BB300/evidence_BB300_SURREALDOLLS-14125_DEV_PASS_no_domain.png) |
| 2 | **Thiếu ký tự @**<br>`invalidemail.com` | Hiển thị thông báo CMMSG30:<br>`「有効なメールアドレスを入力してください。」` | Hiển thị chính xác:<br>`「有効なメールアドレスを入力してください。」` | <span style="color:green; font-weight:bold;">PASS</span> | [evidence_BB300_SURREALDOLLS-14125_DEV_PASS_no_at.png](file:///home/nga/Documents/SurrealDoll/evidence/BB300/evidence_BB300_SURREALDOLLS-14125_DEV_PASS_no_at.png) |
| 3 | **Ký tự đặc biệt không hợp lệ**<br>`test!#$@domain.com` | Hiển thị thông báo CMMSG30:<br>`「有効なメールアドレスを入力してください。」` | Hiển thị chính xác:<br>`「有効なメールアドレスを入力してください。」` | <span style="color:green; font-weight:bold;">PASS</span> | [evidence_BB300_SURREALDOLLS-14125_DEV_PASS_invalid_symbols.png](file:///home/nga/Documents/SurrealDoll/evidence/BB300/evidence_BB300_SURREALDOLLS-14125_DEV_PASS_invalid_symbols.png) |
| 4 | **Bắt đầu bằng dấu chấm**<br>`.abc@test.com` | Hiển thị thông báo CMMSG30:<br>`「有効なメールアドレスを入力してください。」` | Hiển thị chính xác:<br>`「有効なメールアドレスを入力してください。」` | <span style="color:green; font-weight:bold;">PASS</span> | [evidence_BB300_SURREALDOLLS-14125_DEV_PASS_leading_dot.png](file:///home/nga/Documents/SurrealDoll/evidence/BB300/evidence_BB300_SURREALDOLLS-14125_DEV_PASS_leading_dot.png) |
| 5 | **Dấu chấm liên tiếp**<br>`ab..c@test.com` | Hiển thị thông báo CMMSG30:<br>`「有効なメールアドレスを入力してください。」` | Hiển thị chính xác:<br>`「有効なメールアドレスを入力してください。」` | <span style="color:green; font-weight:bold;">PASS</span> | [evidence_BB300_SURREALDOLLS-14125_DEV_PASS_consecutive_dots.png](file:///home/nga/Documents/SurrealDoll/evidence/BB300/evidence_BB300_SURREALDOLLS-14125_DEV_PASS_consecutive_dots.png) |
| 6 | **Negative check: Bỏ trống email**<br>`""` (blank) | Hiển thị thông báo CMMSG29:<br>`「メールアドレスは空欄にできません。」` | Hiển thị chính xác:<br>`「メールアドレスは空欄にできません。」` | <span style="color:green; font-weight:bold;">PASS</span> | [evidence_BB300_SURREALDOLLS-14125_DEV_PASS_blank_email.png](file:///home/nga/Documents/SurrealDoll/evidence/BB300/evidence_BB300_SURREALDOLLS-14125_DEV_PASS_blank_email.png) |
| 7 | **Positive check: Email hợp lệ**<br>`adm42841_valid@test.com` | Không hiển thị lỗi định dạng, hợp lệ | Không hiển thị thông báo lỗi | <span style="color:green; font-weight:bold;">PASS</span> | [evidence_BB300_SURREALDOLLS-14125_DEV_PASS_valid_format.png](file:///home/nga/Documents/SurrealDoll/evidence/BB300/evidence_BB300_SURREALDOLLS-14125_DEV_PASS_valid_format.png) |

---

## 3. BẰNG CHỨNG DOM VÀ KỸ THUẬT (TECHNICAL EVIDENCE)

- **DOM Element xác thực thực tế trên DEV (`https://admin-dev.surrealdolls.com/agencies/admins/detail/351`):**
  ```html
  <p data-slot="form-message" id="_r_7_-form-item-message" class="text-danger text-xs">有効なメールアドレスを入力してください。</p>
  ```
- Chuỗi thông báo lỗi đã được cập nhật chuẩn xác theo hằng số `CMMSG30`, loại bỏ hoàn toàn chuỗi cũ `「無効なメールアドレスです。」`.

---

## 4. DANH SÁCH BẰNG CHỨNG HÌNH ẢNH (ATOMIC SCREENSHOTS)

Tất cả hình ảnh bằng chứng đã được inject khung viền màu xanh lá `#16a34a` (Pass) kèm nhãn trực quan:
- [evidence_BB300_SURREALDOLLS-14125_DEV_PASS_no_domain.png](file:///home/nga/Documents/SurrealDoll/evidence/BB300/evidence_BB300_SURREALDOLLS-14125_DEV_PASS_no_domain.png)
- [evidence_BB300_SURREALDOLLS-14125_DEV_PASS_no_at.png](file:///home/nga/Documents/SurrealDoll/evidence/BB300/evidence_BB300_SURREALDOLLS-14125_DEV_PASS_no_at.png)
- [evidence_BB300_SURREALDOLLS-14125_DEV_PASS_invalid_symbols.png](file:///home/nga/Documents/SurrealDoll/evidence/BB300/evidence_BB300_SURREALDOLLS-14125_DEV_PASS_invalid_symbols.png)
- [evidence_BB300_SURREALDOLLS-14125_DEV_PASS_leading_dot.png](file:///home/nga/Documents/SurrealDoll/evidence/BB300/evidence_BB300_SURREALDOLLS-14125_DEV_PASS_leading_dot.png)
- [evidence_BB300_SURREALDOLLS-14125_DEV_PASS_consecutive_dots.png](file:///home/nga/Documents/SurrealDoll/evidence/BB300/evidence_BB300_SURREALDOLLS-14125_DEV_PASS_consecutive_dots.png)
- [evidence_BB300_SURREALDOLLS-14125_DEV_PASS_blank_email.png](file:///home/nga/Documents/SurrealDoll/evidence/BB300/evidence_BB300_SURREALDOLLS-14125_DEV_PASS_blank_email.png)
- [evidence_BB300_SURREALDOLLS-14125_DEV_PASS_valid_format.png](file:///home/nga/Documents/SurrealDoll/evidence/BB300/evidence_BB300_SURREALDOLLS-14125_DEV_PASS_valid_format.png)

---

## 5. ĐỒNG BỘ KẾT QUẢ & HÀNH ĐỘNG TIẾP THEO

1. **Google Sheet Test Case (Khối Round 2):** Đã cập nhật `Pass` tại cột M, `SURREALDOLLS-14125` tại cột N, `ngadtp` tại cột O, `18/11/2026` tại cột P và ghi chú tại cột Q cho các dòng 54, 55, 56 trên sheet `'BB300'` (`1342RUX4IBu9uzLRxLGRANE5MJ4gen7mTP4BRAFg8hLc`).
2. **Backlog Ticket:**
   - Chuyển trạng thái sang: **`Resolved`**
   - Đính kèm comment kết quả xác minh và link bằng chứng.
   - Log thời gian thực tế: **Actual Hours = 0.2h (12 phút)**.
