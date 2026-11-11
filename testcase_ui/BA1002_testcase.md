# BẢNG TEST CASE KIỂM THỬ GIAO DIỆN THỦ CÔNG (MANUAL UI TEST SUITE)
## Màn hình: BA1002 (Retest Round 2)
### Áp dụng: Quy chuẩn Trụ cột 4 (04_manual_test_execution_rule.md) & GEMINI.md

---

## BẢNG ĐIỀU KHIỂN TIẾN ĐỘ & THỐNG KÊ (DASHBOARD HEADER)

| Thuộc tính | Giá trị | Thuộc tính | Giá trị | Round 1 Metric | Kết quả | Round 2 Metric | Kết quả |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Module Code** |  | **Environment** |  | **Total TCs** | 14 | **Pass** | 13 |
| **Total Testcases** | **14** | **Tester** |  | **Executed** | 100% | **Fail** | 0 |
| **Pass Rate (R2)** | **100.0%** | **Test Date** |  | **Pass Rate (R1)** | - | **Impact** | 0 |
| **Spec Source** |  | **Google Sheet Tab** |  | | | **Blocked** | 1 |

---

## CHI TIẾT BẢNG TEST CASES (17 CỘT CHUẨN)

| ID | Title | Big item | Steps | Pre-condition | Expected | Priority | R1 Result | R1 Bug ID | R1 Tester | R1 Date | R1 Note | R2 Result | R2 Bug ID | R2 Tester | R2 Comment | R2 Note |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :---: | :---: | :---: | :--- | :--- |
|  | [0] Kiểm tra truy cập màn hình | Check hiển thị màn hình sau khi gửi yêu cầu | 1. Tại BA1001, nhập email hợp lệ và click button 送信 | Đã submit yêu cầu từ BA1001 | 1. <br>- Di chuyển đến màn BA1002 メール送信完了<br>- Hiển thị UI giống với Figma<br>- Header có logo, text 「事務所管理画面」 và KHÔNG có nút 「マスター管理画面へ」 | High | Pass |  | NgaDTP | 06/11/2026 |  | **Pass** |  | NgaDTP | Di chuyển đến màn BA1002 メール送信完了, UI giống Figma | |
|  |  | Check không hiển thị nút về Master | 1. Quan sát toàn bộ thanh Header |  | 1. Không hiển thị nút マスター管理画面へ trên Header | High | Pass |  | NgaDTP | 06/11/2026 |  | **Pass** |  | NgaDTP | Không hiển thị nút マスター管理画面へ trên Header | |
|  | [1] Label メール送信完了 | Kiểm tra tiêu đề Card | 1. Thực hiện kiểm tra tiêu đề Card |  | 1. Hiển thị text tiêu đề: メール送信完了 | High | Pass |  | NgaDTP | 06/11/2026 |  | **Pass** |  | NgaDTP | Hiển thị đúng tiêu đề Card: メール送信完了 | |
|  | [2] Label パスワード再設定用のメールを送信しました... | Kiểm tra nội dung hướng dẫn | 1. Thực hiện kiểm tra nội dung văn bản hướng dẫn |  | 1. Hiển thị nguyên văn chuỗi thông báo:<br>パスワード再設定用のメールを送信しました。受信したメールに記載されているURLにアクセスし、パスワードを再設定してください。 | High | Pass |  | NgaDTP | 06/11/2026 |  | **Pass** |  | NgaDTP | Hiển thị chuỗi thông báo hướng dẫn gửi email thành công | |
|  | [3] Label ※ URLの有効期限は、メール発送時点から24時間です。 | Kiểm tra nội dung thời hạn | 1. Thực hiện kiểm tra dòng ghi chú thời hạn |  | 1. Hiển thị nguyên văn chuỗi ghi chú:<br>※ URLの有効期限は、メール発送時点から24時間です。 | High | Pass |  | NgaDTP | 06/11/2026 |  | **Pass** |  | NgaDTP | Hiển thị chính xác dòng ghi chú thời hạn: ※ URLの有効期限は、メール発送時点から24時間です。 | |
|  | [4] Button ログインへ戻る | Kiểm tra hiển thị button | 1. Quan sát button ログインへ戻る |  | 1. Hiển thị button với text căn giữa: ログインへ戻る | High | Pass |  | NgaDTP | 06/11/2026 |  | **Pass** |  | NgaDTP | Hiển thị button với text căn giữa: ログインへ戻る | |
|  |  | Kiểm tra khi di chuyển con trỏ chuột vào button | 1. Thực hiện di chuyển chuột vào button ログインへ戻る |  | 1. <br>- Con trỏ chuột hiển thị hình bàn tay<br>- Màu sắc button có sự thay đổi | Medium | Pass |  | NgaDTP | 06/11/2026 |  | **Pass** |  | NgaDTP | Con trỏ chuột hiển thị pointer khi hover button | |
|  |  | Kiểm tra khi click button | 1. Click button ログインへ戻る |  | 1. Di chuyển về màn đăng nhập Agency BA100 | High | Pass |  | NgaDTP | 06/11/2026 |  | **Pass** |  | NgaDTP | Click button ログインへ戻る di chuyển về màn đăng nhập Agency BA100 (/sign-in/agency) | |
|  |  | Kiểm tra kích hoạt bằng phím Enter | 1. Focus vào button ログインへ戻る, nhấn phím Enter |  | 1. Di chuyển về màn đăng nhập Agency BA100 | Medium | Pass |  | NgaDTP | 06/11/2026 |  | **Pass** |  | NgaDTP | Focus vào button ログインへ戻る và nhấn phím Enter di chuyển về BA100 | |
|  | [Email] Nội dung & Liên kết Email | Kiểm tra tiêu đề và người gửi email | 1. Mở email reset mật khẩu trong hộp thư đến |  | 1. <br>- Người gửi: noreply@surrealdolls.com<br>- Tiêu đề: 【SURREALDOLLS】パスワード再設定のお知らせ | High | Pass |  | NgaDTP | 06/11/2026 |  | **Pass** |  | NgaDTP | Email thực tế gửi từ noreply@surrealdolls.com đến hộp thư ngadtp@mumesoft.vn | |
|  |  | Kiểm tra tên Owner trong nội dung mail | 1. Đọc nội dung email gửi đến Owner | Email gửi đến Owner | 1. Hiển thị đúng tên Owner: {{user_name}} 様 (lấy オーナー名 từ AD200/BB101) | High | Pass |  | NgaDTP | 06/11/2026 |  | **Pass** |  | NgaDTP | Nội dung email hiển thị chính xác tên Owner: 123 様 | |
|  |  | Kiểm tra tên Admin con trong nội dung mail | 1. Đọc nội dung email gửi đến Admin con | Email gửi đến Admin con | 1. Hiển thị đúng tên Admin: {{user_name}} 様 (lấy 名前 từ BB200) | High | Pass |  | NgaDTP | 06/11/2026 |  | **Blocked** |  | NgaDTP | Pre-condition: Cần kiểm tra tên Admin con trong nội dung email | |
|  |  | Kiểm tra link mở đúng màn BA1003 Agency | 1. Click link パスワード再設定 trong nội dung email |  | 1. Mở đúng màn hình BA1003 bản Agency (có Header 事務所管理画面, không mở màn master) | High | Pass |  | NgaDTP | 06/11/2026 |  | **Pass** |  | NgaDTP | Link từ email mở đúng màn BA1003 bản Agency (Header 事務所管理画面, không mở master) | |
|  |  | Kiểm tra sử dụng lại link cũ chưa quá 24h | 1. Gửi yêu cầu 2 lần<br>2. Mở email lần 1 và click link khi chưa quá 24h và chưa dùng | Link lần 1 chưa dùng, chưa quá 24h | 2. Link lần 1 vẫn mở được màn BA1003 ở trạng thái hợp lệ để đổi mật khẩu | High | Pass |  | NgaDTP | 06/11/2026 |  | **Pass** |  | NgaDTP | Link chưa quá 24h mở được form BA1003 hợp lệ để đặt lại mật khẩu | |
