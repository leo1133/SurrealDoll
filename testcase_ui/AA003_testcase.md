# BẢNG TEST CASE VÀ KẾT QUẢ KIỂM THỬ THỦ CÔNG - MÀN HÌNH AA003 (PASSWORD CHANGE MODAL)
## Màn hình: AA003 - パスワード変更 (Modal Đổi Mật Khẩu Khi Đang Đăng Nhập - Admin Master)
### Thuộc Task: [SURREALDOLLS-14231](https://issoh.backlog.com/view/SURREALDOLLS-14231) | BE: SURREALDOLLS-12839 | Rule: CMR43, CMR68
### Google Sheet Target: [Admin Master Test Case - Tab AA003 (gid=350559572)](https://docs.google.com/spreadsheets/d/1ZaL8llNgH6sCxpG-daLEi21IxXFpub-BbrRJRdUNMOg/edit?gid=350559572#gid=350559572)
### Báo cáo Bug chi tiết: [AA003_bugs.md](../bugs/AA003_bugs.md)

---

## 1. BẢNG THỐNG KÊ KẾT QUẢ THỰC THI (ROUND 1 SUMMARY)

| Chỉ số | Số lượng / Tỷ lệ | Trạng thái |
| :--- | :---: | :---: |
| **Tổng số Test Cases thiết kế (Total Created)** | **74** | 100% |
| **Số Test Cases đã thực thi (Executed)** | **74** | **100.0%** |
| **Số Test Cases ĐẠT (Pass)** | **70** | **94.6%** |
| **Số Test Cases KHÔNG ĐẠT (Fail)** | **4** | **5.4%** |
| **Tổng số lỗi phát hiện (Bugs Logged)** | **2 bugs lớn** (1 Major, 1 Minor) | Đã xuất bằng chứng DOM & ảnh chụp |

---

## 2. DANH SÁCH CHI TIẾT 4 CA KIỂM THỬ THẤT BẠI (FAIL)

| Mã TC | Hạng mục kiểm tra | Thao tác thực hiện | Kết quả kỳ vọng (Expected) | Kết quả thực tế (Actual) | Bug ID liên quan | File bằng chứng (Evidence) |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| `[AA003-8]` | Nút tài khoản cuối Side menu | Đăng nhập Admin $\rightarrow$ Quan sát nút tài khoản ở chân side menu | Hiển thị avatar tròn, Tên, Email và **icon tam giác ▲** ở mép phải nút | Nút tài khoản chỉ hiển thị Avatar, Tên và Email; **hoàn toàn thiếu icon tam giác ▲** | `BUG-AA003-1` | `evidence/evidence_AA003_TC08_missing_triangle_icon.png` |
| `[AA003-14]` | Header Menu tài khoản | Click mở menu tài khoản ở cuối side menu $\rightarrow$ Quan sát header menu | Hiển thị đầy đủ: Tên, Email, và **Tag role 「マスター」** | Header menu chỉ hiển thị Tên và Email; **thiếu Tag role 「マスター」** | `BUG-AA003-2` | `evidence/evidence_AA003_TC14_missing_role_tag.png` |
| `[AA003-15]` | Tag Role 管理者 | Đăng nhập tài khoản role 管理者 $\rightarrow$ Mở menu tài khoản | Hiển thị tag role 「管理者」 | Header menu thiếu container/logic render tag role | `BUG-AA003-2` | `evidence/evidence_AA003_TC14_missing_role_tag.png` |
| `[AA003-16]` | Tag Role 監視員 | Đăng nhập tài khoản role 監視員 $\rightarrow$ Mở menu tài khoản | Hiển thị tag role 「監視員」 | Header menu thiếu container/logic render tag role | `BUG-AA003-2` | `evidence/evidence_AA003_TC14_missing_role_tag.png` |

---

## 3. DANH MỤC TOÀN BỘ 74 TEST CASES & KẾT QUẢ ĐÃ GHI NHẬN LÊN GOOGLE SHEET

*(Đã ghi nhận trực tiếp kết quả vào Cột H (Round 1) tại Google Sheet tab `AA003`)*

| Mã TC | Nhóm chức năng | Tên Test Case | Kết quả Round 1 | Ghi chú kỹ thuật |
| :---: | :--- | :--- | :---: | :--- |
| `[AA003-1]` | `[0] Truy cập màn hình` | Check mở modal từ khu tài khoản cuối side menu | **Pass** | Modal hiển thị giữa màn hình có backdrop |
| `[AA003-2]` | `[0] Truy cập màn hình` | Check trạng thái khởi tạo modal | **Pass** | 3 ô trống, ẩn mật khẩu, focus ô 1 |
| `[AA003-3]` | `[0] Truy cập màn hình` | Check đóng modal bằng nút [X] | **Pass** | Đóng ngay, không hỏi confirm |
| `[AA003-4]` | `[0] Truy cập màn hình` | Check đóng modal bằng nút キャンセル | **Pass** | Đóng ngay, xóa sạch nội dung đã nhập |
| `[AA003-5]` | `[0] Truy cập màn hình` | Check đóng modal bằng phím Esc | **Pass** | Đóng ngay khi nhấn phím Esc |
| `[AA003-6]` | `[0] Truy cập màn hình` | Check đóng modal khi click Backdrop | **Pass** | Modal đóng lập tức khi click backdrop |
| `[AA003-7]` | `[0] Truy cập màn hình` | Check mở lại modal sau khi vừa đóng | **Pass** | Cả 3 ô rỗng, xóa sạch lỗi cũ |
| `[AA003-8]` | `[1] Khu tài khoản` | Check hiển thị nút tài khoản ở side menu | **Fail** | `BUG-AA003-1`: Thiếu icon tam giác ▲ ở mép phải |
| `[AA003-9]` | `[1] Khu tài khoản` | Check vị trí cố định khi cuộn side menu | **Pass** | Cố định ở đáy side menu |
| `[AA003-10]` | `[1] Khu tài khoản` | Check xử lý văn bản quá dài | **Pass** | Class truncate rút gọn bằng dấu 3 chấm … |
| `[AA003-11]` | `[1] Khu tài khoản` | Check hover chuột | **Pass** | Con trỏ pointer, hover đổi màu nhẹ |
| `[AA003-12]` | `[1] Khu tài khoản` | Check click mở / đóng menu tài khoản | **Pass** | Mở popup menu phía trên |
| `[AA003-13]` | `[1] Khu tài khoản` | Check đóng menu khi click ngoài hoặc Esc | **Pass** | Menu đóng khi nhấn Esc |
| `[AA003-14]` | `[2] Menu tài khoản` | Check hiển thị header menu role マスター | **Fail** | `BUG-AA003-2`: Thiếu Tag role 「マスター」 |
| `[AA003-15]` | `[2] Menu tài khoản` | Check hiển thị tag role 管理者 | **Fail** | `BUG-AA003-2`: Thiếu container render tag role |
| `[AA003-16]` | `[2] Menu tài khoản` | Check hiển thị tag role 監視員 | **Fail** | `BUG-AA003-2`: Thiếu container render tag role |
| `[AA003-17]` | `[2.1] Nút パスワード変更` | Check hiển thị | **Pass** | Icon chìa khóa kèm text 「パスワード変更」 |
| `[AA003-18]` | `[2.1] Nút パスワード変更` | Check click mở modal | **Pass** | Menu đóng, modal mở ra |
| `[AA003-19]` | `[2.2] Nút ログアウト` | Check hiển thị | **Pass** | Text đỏ cảnh báo |
| `[AA003-20]` | `[2.2] Nút ログアウト` | Check click đăng xuất | **Pass** | Đăng xuất chuyển về AA000 |
| `[AA003-21]` | `[3] Modal パスワード変更` | Check hiển thị tiêu đề và ghi chú 30 ngày | **Pass** | Hiển thị đủ tiêu đề và ghi chú CMR68 |
| `[AA003-22]` | `[4] Textbox 現在のパスワード` | Check hiển thị label và placeholder | **Pass** | Placeholder: 「現在のパスワードを入力」 |
| `[AA003-23]` | `[4] Textbox 現在のパスワード` | Check ẩn ký tự khi nhập | **Pass** | Dạng ●●● |
| `[AA003-24]` | `[4] Textbox 現在のパスワード` | Check khi để trống ô nhập | **Pass** | Báo lỗi CMMSG29 dưới ô + viền đỏ |
| `[AA003-25]` | `[4] Textbox 現在のパスワード` | Check tự động xóa lỗi khi gõ lại | **Pass** | Lỗi biến mất ngay khi gõ ký tự |
| `[AA003-26]` | `[4] Textbox 現在のパスワード` | Check chặn copy cut khi ẩn | **Pass** | Chặn copy/cut an toàn |
| `[AA003-27]` | `[4] Textbox 現在のパスワード` | Check nhập sai mật khẩu hiện tại (BE) | **Pass** | BE trả lỗi MSG24: パスワードが間違っています。 |
| `[AA003-28]` | `[4] Textbox 現在のパスワード` | Check ký tự đặc biệt & SQL injection | **Pass** | Xử lý an toàn, báo MSG24 không crash |
| `[AA003-29]` | `[5] Textbox 新しいパスワード` | Check hiển thị label và placeholder | **Pass** | Placeholder: 「新しいパスワードを入力」 |
| `[AA003-30]` | `[5] Textbox 新しいパスワード` | Check hiển thị dòng hướng dẫn rule tĩnh | **Pass** | Luôn hiển thị tĩnh đủ 3 dòng rule CMR43 |
| `[AA003-31]` | `[5] Textbox 新しいパスワード` | Check ẩn ký tự khi nhập | **Pass** | Dạng ●●● |
| `[AA003-32]` | `[5] Textbox 新しいパスワード` | Check khi để trống ô nhập | **Pass** | Báo CMMSG29: 新しいパスワードは空欄にできません。 |
| `[AA003-33]` | `[5] Textbox 新しいパスワード` | Check rule: 7 ký tự đủ 4 nhóm | **Pass** | Báo lỗi MSG13 dưới ô |
| `[AA003-34]` | `[5] Textbox 新しいパスワード` | Check rule: 8 ký tự thiếu hoa | **Pass** | Báo lỗi MSG13 |
| `[AA003-35]` | `[5] Textbox 新しいパスワード` | Check rule: 8 ký tự thiếu thường | **Pass** | Báo lỗi MSG13 |
| `[AA003-36]` | `[5] Textbox 新しいパスワード` | Check rule: 8 ký tự thiếu số | **Pass** | Báo lỗi MSG13 |
| `[AA003-37]` | `[5] Textbox 新しいパスワード` | Check rule: 8 ký tự thiếu ký hiệu | **Pass** | Báo lỗi MSG13 |
| `[AA003-38]` | `[5] Textbox 新しいパスワード` | Check rule: 8 ký tự đủ 4 nhóm | **Pass** | Hợp lệ, không báo MSG13 |
| `[AA003-39]` | `[5] Textbox 新しいパスワード` | Check các loại ký hiệu theo CMR43 | **Pass** | Chấp nhận đầy đủ tập ký hiệu quy chuẩn |
| `[AA003-40]` | `[5] Textbox 新しいパスワード` | Check tự động xóa lỗi MSG13 | **Pass** | Tự động xóa lỗi khi gõ đạt chuẩn |
| `[AA003-41]` | `[5] Textbox 新しいパスワード` | Check trùng mật khẩu hiện tại (PW-H0) | **Pass** | BE trả HTTP 400 MSG261 dưới ô |
| `[AA003-42]` | `[5] Textbox 新しいパスワード` | Check trùng mật khẩu lần đổi -1 | **Pass** | BE trả HTTP 400 MSG261 |
| `[AA003-43]` | `[5] Textbox 新しいパスワード` | Check trùng mật khẩu lần đổi -2 | **Pass** | BE trả HTTP 400 MSG261 |
| `[AA003-44]` | `[5] Textbox 新しいパスワード` | Check trùng mật khẩu lần đổi -3 | **Pass** | Hợp lệ (ngoài phạm vi 2 lần gần nhất) |
| `[AA003-45]` | `[5] Textbox 新しいパスワード` | Check sửa mật khẩu sau khi báo MSG261 | **Pass** | Gửi API bình thường sau khi sửa |
| `[AA003-46]` | `[5] Textbox 新しいパスワード` | Check sliding window lịch sử mật khẩu | **Pass** | Duy trì sliding window 2 mật khẩu gần nhất |
| `[AA003-47]` | `[5] Textbox 新しいパスワード` | Check lỗi rule từ BE (HTTP 422) | **Pass** | BE validate độc lập, an toàn |
| `[AA003-48]` | `[6] Textbox 新しいパスワード確認` | Check hiển thị label và placeholder | **Pass** | Placeholder: 「新しいパスワードを再入力」 |
| `[AA003-49]` | `[6] Textbox 新しいパスワード確認` | Check ẩn ký tự khi nhập | **Pass** | Dạng ●●● |
| `[AA003-50]` | `[6] Textbox 新しいパスワード確認` | Check khi để trống ô nhập | **Pass** | Báo CMMSG29: 新しいパスワード確認は空欄にできません。 |
| `[AA003-51]` | `[6] Textbox 新しいパスワード確認` | Check xác nhận: khác nhau | **Pass** | Báo lỗi MSG25 dưới ô xác nhận |
| `[AA003-52]` | `[6] Textbox 新しいパスワード確認` | Check xác nhận: khác chữ hoa/thường | **Pass** | Báo lỗi MSG25 |
| `[AA003-53]` | `[6] Textbox 新しいパスワード確認` | Check xác nhận: khớp nhau 100% | **Pass** | Không báo lỗi MSG25 |
| `[AA003-54]` | `[6] Textbox 新しいパスワード確認` | Check tự động xóa lỗi MSG25 | **Pass** | Xóa lỗi khi gõ sửa khớp |
| `[AA003-55]` | `[7] Icon 👁` | Check hiển thị icon tại 3 ô | **Pass** | Cả 3 ô đều có icon mắt riêng |
| `[AA003-56]` | `[7] Icon 👁` | Check bật tắt ẩn/hiện ô 1 | **Pass** | Bật tắt text rõ ô 1 độc lập |
| `[AA003-57]` | `[7] Icon 👁` | Check bật tắt ẩn/hiện ô 2 | **Pass** | Bật tắt text rõ ô 2 độc lập |
| `[AA003-58]` | `[7] Icon 👁` | Check bật tắt ẩn/hiện ô 3 | **Pass** | Bật tắt text rõ ô 3 độc lập |
| `[AA003-59]` | `[8] Button キャンセル` | Check hiển thị button | **Pass** | Hiển thị góc dưới bên trái |
| `[AA003-60]` | `[8] Button キャンセル` | Check click hủy và đóng modal | **Pass** | Xóa sạch nội dung, đóng an toàn |
| `[AA003-61]` | `[9] Button 変更する` | Check hiển thị button | **Pass** | Hiển thị góc dưới bên phải Primary |
| `[AA003-62]` | `[9] Button 変更する` | Check báo lỗi cả 3 ô khi để trống | **Pass** | Viền đỏ cả 3 ô đồng thời, hiện lỗi CMMSG29 |
| `[AA003-63]` | `[9] Button 変更する` | Check kích hoạt bằng phím Enter | **Pass** | Phím Enter trigger submit form |
| `[AA003-64]` | `[9] Button 変更する` | Check chống double click (CMR15) | **Pass** | Disable nút + hiển thị 変更中… |
| `[AA003-65]` | `[9] Button 変更する` | Check đổi mật khẩu thành công | **Pass** | Modal đóng, hiện Toast MSG33 |
| `[AA003-66]` | `[9] Button 変更する` | Check duy trì phiên hiện tại | **Pass** | Ở lại màn đang mở, giữ đăng nhập |
| `[AA003-67]` | `[9] Button 変更する` | Check thu hồi token mọi phiên khác (CMR43) | **Pass** | Các phiên khác bị thu hồi session token |
| `[AA003-68]` | `[9] Button 変更する` | Check đăng nhập lại bằng mật khẩu mới | **Pass** | Đăng nhập thành công bằng pass mới |
| `[AA003-69]` | `[9] Button 変更する` | Check role 管理者 tự đổi mật khẩu | **Pass** | Role 管理者 đổi mật khẩu của chính mình |
| `[AA003-70]` | `[9] Button 変更する` | Check role 監視員 tự đổi mật khẩu | **Pass** | Role 監視員 đổi mật khẩu của chính mình |
| `[AA003-71]` | `[9] Button 変更する` | Check thời hạn 30 ngày tính lại (CMR68) | **Pass** | 30 ngày bắt đầu tính từ lúc đổi |
| `[AA003-72]` | `[9] Button 変更する` | Check lỗi mạng hoặc server 500 | **Pass** | Báo CMMSG1, giữ nguyên modal |
| `[AA003-73]` | `[9] Button 変更する` | Check session hết hạn khi mở modal | **Pass** | Chuyển hướng về AA000 |
| `[AA003-74]` | `[9] Button 変更する` | Check đổi mật khẩu đồng thời 2 tab | **Pass** | Xử lý an toàn theo session token |
