# BÁO CÁO KẾT QUẢ KIỂM THỬ THỦ CÔNG - MÀN HÌNH BA1002 (AGENCY FORGOT PASSWORD COMPLETE)

Theo quy chuẩn [06_bug_reporting_rule.md](../../Universal_Rules/06_bug_reporting_rule.md).  
Môi trường kiểm thử: **Dev-Agency** theo cấu hình tại [TEST_CONFIG.md](../../TEST_CONFIG.md).

---

## 1. TỔNG QUAN KẾT QUẢ RETEST (RETEST SUMMARY)

- **Tổng số ca kiểm thử:** 14 ca
- **Pass (Đạt):** **13 ca** (100% các ca kiểm thử giao diện, điều hướng, xác thực email và liên kết mở BA1003)
- **Fail (Lỗi):** **0 ca**
- **Blocked:** **1 ca** (`[BA1002-12]` chờ mail tài khoản Admin con)
- **Tình trạng Bug:** **0 Bug trực tiếp phát sinh.**
  - **Điểm sáng:** Sau khi Backend fix lỗi `[BUG-1]` tại màn hình `BA1001` (API 500), luồng điều hướng sang `BA1002` và việc gửi mail qua SES/SMTP đã hoạt động chuẩn xác 100%.
  - Toàn bộ giao diện tĩnh, tiêu đề Card `メール送信完了`, văn bản hướng dẫn thời hạn 24 giờ, và nút điều hướng `ログインへ戻る` trở về `BA100` (`/sign-in/agency`) đều hoạt động chính xác theo đặc tả Figma.
  - Email reset mật khẩu thực tế gửi về hộp thư `ngadtp@mumesoft.vn` hiển thị chính xác người gửi `noreply@surrealdolls.com` và lời chào tên Owner `123 様`.
  - Đường link đặt lại mật khẩu trong email mở chính xác màn hình `BA1003` bản Agency và còn nguyên hiệu lực 24 giờ.

---

## 2. BẢNG TỔNG HỢP KẾT QUẢ KIỂM THỬ THỰC TẾ

| TC ID | Tiêu đề / Chức năng | Thao tác thực hiện | Kết quả thực tế kiểm thử live | Trạng thái Retest |
| :--- | :--- | :--- | :--- | :---: |
| `[BA1002-1]` | Check hiển thị màn hình sau khi gửi yêu cầu | Tại BA1001 nhập email hợp lệ và submit | Chuyển hướng thành công sang `/sent-reset-password-successfully/agency`, UI khớp Figma | **Pass** |
| `[BA1002-2]` | Check không hiển thị nút về Master trên Header | Quan sát thanh Header | Không hiển thị nút `マスター管理画面へ` | **Pass** |
| `[BA1002-3]` | Check tiêu đề Card メール送信完了 | Kiểm tra tiêu đề Card | Hiển thị chính xác text: `メール送信完了` | **Pass** |
| `[BA1002-4]` | Check nội dung văn bản hướng dẫn | Kiểm tra chuỗi hướng dẫn | Hiển thị thông báo gửi email đặt lại mật khẩu | **Pass** |
| `[BA1002-5]` | Check dòng ghi chú thời hạn 24 giờ | Kiểm tra text thời hạn | Hiển thị chính xác: `※ URLの有効期限は、メール発送時点から24時間です。` | **Pass** |
| `[BA1002-6]` | Check hiển thị button ログインへ戻る | Quan sát button | Hiển thị button với text căn giữa: `ログインへ戻る` | **Pass** |
| `[BA1002-7]` | Check hover button ログインへ戻る | Hover chuột vào button | Con trỏ chuột chuyển sang dạng `pointer` | **Pass** |
| `[BA1002-8]` | Check click button ログインへ戻る | Click button | Điều hướng chính xác về màn đăng nhập Agency `BA100` (`/sign-in/agency`) | **Pass** |
| `[BA1002-9]` | Check Enter button ログインへ戻る | Focus và nhấn phím Enter | Kích hoạt điều hướng về màn đăng nhập `BA100` | **Pass** |
| `[BA1002-10]` | Check tiêu đề và người gửi email | Mở email reset mật khẩu | Xác nhận email thực tế từ `noreply@surrealdolls.com` gửi về hộp thư `ngadtp@mumesoft.vn` | **Pass** |
| `[BA1002-11]` | Check tên Owner trong nội dung mail | Đọc nội dung email gửi Owner | Nội dung email hiển thị chính xác tên Owner: `123 様` | **Pass** |
| `[BA1002-12]` | Check tên Admin con trong mail | Đọc nội dung email gửi Admin con | Pre-condition: Cần mail gửi đến tài khoản Admin con | **Blocked** |
| `[BA1002-13]` | Check link mở đúng màn BA1003 | Click link trong email | Link từ email mở đúng màn BA1003 bản Agency (Header 事務所管理画面, không mở master) | **Pass** |
| `[BA1002-14]` | Check sử dụng lại link cũ chưa quá 24h | Gửi yêu cầu 2 lần | Link chưa quá 24h mở được form BA1003 hợp lệ để đặt lại mật khẩu | **Pass** |
