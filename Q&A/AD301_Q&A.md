# TÀI LIỆU BÓC TÁCH ĐẶC TẢ KỸ THUẬT & LÀM RÕ YÊU CẦU (SPEC ANALYSIS & CLARIFICATION REPORT)
## Màn hình: AD301_Agency Information (Chi Tiết & Chỉnh Sửa Thông Tin Agency - 事務所詳細_詳細)
### Phân hệ: Web Master Admin Portal (`AA000`) / Quản lý Agency (`AD` Module)
### Áp dụng: Quy chuẩn Trụ Cột 1 (`Universal_Rules/01_core_spec_analysis_rule.md`) & Master Policy (`GEMINI.md`)

---

## BẢNG THÔNG TIN TỔNG QUAN ĐẶC TẢ (SPECIFICATION METADATA)

| Thuộc tính | Chi tiết |
| :--- | :--- |
| **Mã màn hình** | `AD301` |
| **Tên màn hình** | `AD301_Agency Information` (事務所管理_事務所詳細_詳細・情報編集) |
| **Phân hệ / Module** | Master Admin Web (`AA000`) / Phân hệ Quản lý Agency (`AD` Module) |
| **Người tạo Spec (Created by)** | `Ly` |
| **Ngày tạo (Created Date)** | July-15 (Cập nhật CR: 15/10/2026, 19/10/2026, 21/10/2026 GMO Sec-12) |
| **Nguồn Spec Google Sheets** | [Google Spreadsheet - Tab AD301 (gid=406207487)](https://docs.google.com/spreadsheets/d/1pxox5GcjOXwKadMnzOa765ptG2huPJSxCiWsrH0_h7Y/edit?gid=406207487#gid=406207487) |
| **Nguồn Tham chiếu Nghiệp vụ** | Tab `CommonSpec` (CMR04, CMR15, CMR20, CMR26, CMR42, CMR43, CMR50, CMR68), `Common MSG`, `MSG` |
| **Nguồn Thiết kế Figma** | [Figma AD301 (node-id=911-4648)](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout---Spec-PDF?node-id=911-4648&t=CHjpqKXsbfmyHBR7-4) |
| **Luồng Điều hướng Vào** | Từ danh sách Agency `AD100` $\rightarrow$ Click vào dòng / nút chi tiết `[14]` $\rightarrow$ Mở `AD301` |
| **Luồng Điều hướng Ra** | • Chuyển tab sang `AD302` (ライバー一覧) hoặc `AD303` (売上)<br>• Click Xóa Agency / Cancel $\rightarrow$ Quay về danh sách `AD100` |
| **Ngôn ngữ hiển thị chính** | Tiếng Nhật (`JA`) |

---

## I. KẾT QUẢ QUÉT ĐẶC TẢ 2 BƯỚC BẮT BUỘC (2-PASS SCANNING PROTOCOL)

### 1. Pass 1 - Bóc Tách UI Controls Có `[No.]` (Item [2] đến [11])

| No. | Tên phần tử (Value JP) | Loại UI Control | Placeholder | Ràng buộc Validate & Nghiệp vụ (SRS & CR) |
| :---: | :--- | :--- | :--- | :--- |
| `[2]` | `詳細` / `ライバー` / `売上` | Tab Navigation | - | Tuân thủ **CMR20** gồm 3 tab: `詳細` (Default khi mở màn hình), `ライバー` (AD302), `売上` (AD303). |
| `[3]` | `事務所名` | Textbox Input (Required ◯) | - | Min 1, Max 20 ký tự. Cho phép ký tự đặc biệt.<br>• **CR 15/10/2026:** Bắt buộc duy nhất toàn hệ thống (không tính chính Agency đang sửa). Trùng tên báo lỗi `CMMSG57` (`事務所名は既に存在しています。`). |
| `[4]` | `事務所ID` | Textbox Input (Required ◯) | - | Min 3, Max 20 ký tự. Chỉ chữ cái Latin và chữ số. Trùng Agency khác báo `MSG15` (`このIDは登録済みです。`). |
| `[5]` | `事務所ロゴ` | File Upload (Required ◯) | - | Chuẩn **CMR50**. Định dạng PNG, JPG/JPEG, SVG, WebP $\rightarrow$ Sai format báo `CMMSG43`. Max 5MB $\rightarrow$ Quá kích thước báo `CMMSG45`.<br>• **CR 15/10/2026:** Nếu Agency dữ liệu cũ chưa có logo $\rightarrow$ Hiển thị logo hệ thống. |
| `[6]` | `連絡先 オーナー名` | Textbox Input (Required ◯) | - | Min 1, Max 20 ký tự. |
| `[7]` | `電話番号` | Textbox Input (Required ◯) | - | Min 5, Max 20 ký tự, nhập tự do theo **CMR04**. |
| `[8]` | `メールアドレス` | Textbox Input (Required ◯) | - | Min 3, Max 254 ký tự (#13003). Format `a@b.c` theo **CMR42**. Trùng tài khoản khác báo `MSG14`.<br>• **CR 19/10/2026 (Quy trình xác thực đổi Email 2 bước):**<br>  + Khi bấm `保存` với email mới: Các thông tin khác lưu ngay; Email CHƯA đổi ngay. Gửi email xác thực `PEM4` tới email mới với link có hạn 7 ngày, dùng 1 lần.<br>  + Trong thời gian chờ xác thực: Cạnh ô email hiển thị nhãn `「認証待ち：{新メールアドレス}」` (kể cả khi F5 reload trang). Ô textbox vẫn hiển thị email cũ.<br>  + Chủ sở hữu Agency vẫn đăng nhập vào portal (`BA100`) và thực hiện quên mật khẩu (`BA1001`) bằng email cũ.<br>  + Bấm link trong mail còn hạn $\rightarrow$ Email mới có hiệu lực, nhãn mất, email cũ không dùng được nữa.<br>  + Quá 7 ngày không xác thực $\rightarrow$ Link hết hạn, nhãn mất, email giữ nguyên giá trị cũ.<br>  + Nếu đang chờ mà đổi email lần nữa $\rightarrow$ Hủy link cũ, gửi `PEM4` mới. Nếu nhập lại đúng email cũ $\rightarrow$ Hủy yêu cầu xác thực, nhãn mất. |
| `[9]` | `ログインパスワードリセット` | Group Control & Button | `リセット` | • Nhấn nút `[リセット]` để hiển thị ô textbox nhập mật khẩu mới cho Owner Agency.<br>• **CR 21/10/2026 (GMO Sec-12 / #12839, #13285):** Mật khẩu nhập theo **CMR43** ($\ge 8$ ký tự, đủ chữ hoa, chữ thường, số, ký tự đặc biệt). Sai quy tắc báo `MSG13` (`パスワードは8文字以上で、英大文字・小文字・数字・記号をそれぞれ1文字以上含めてください。`).<br>• **Kiểm tra trùng mật khẩu:** CẤM trùng mật khẩu hiện tại hoặc 2 mật khẩu gần nhất trước đó của Owner $\rightarrow$ Trùng báo lỗi `MSG261` (`過去2回以内に使用したパスワードは再利用できません。`).<br>• **Thu hồi phiên làm việc:** Lưu thành công $\rightarrow$ Tính lại hạn 30 ngày (**CMR68**), BE lập tức thu hồi token, **cưỡng chế đăng xuất toàn bộ phiên đang đăng nhập** của Owner. Master Admin tự thông báo mật khẩu mới cho Owner. |
| `[10]` | `ステータス` | Radio Button | `利用中` | • Gồm 2 radio: `利用中` (Active - Mặc định) và `停止中` (Inactive).<br>• Khi chọn `停止中` và bấm Lưu $\rightarrow$ Bắt buộc hiển thị popup cảnh báo **`MSG65`** (`利用を停止すると事務所に関連するユーザーも引き続き利用できます、よろしいですか。`).<br>• Sau khi Inactive: Toàn bộ member trực thuộc chuyển thành user tự do, các request đang xin tham gia chuyển thành từ chối, các tài khoản Admin Agency bị chặn đăng nhập. Agency bị làm xám trên danh sách `AD100` nhưng vẫn bấm vào sửa được. |
| `[11]` | `キャンセル` | Button (Secondary) | `キャンセル` | Tuân thủ **CMR26**. Hủy bỏ chỉnh sửa, hoàn nguyên dữ liệu. |
| `[11]` | `保存` | Button (Primary) | `保存` | Tuân thủ **CMR15**. Lưu cập nhật Agency (xử lý PEM4 nếu đổi email, thu hồi phiên nếu đổi pass). |
| `[11]` | `削除` | Button (Danger) | `削除` | Click hiển thị popup xác nhận xóa **`MSG66`** (`削除すると事務所に関連するユーザーも引き続き利用できます、よろしいですか。`). Nếu xác nhận $\rightarrow$ Xóa mềm Agency, giải phóng các Liver trực thuộc thành tự do, xóa mềm tài khoản Admin Agency, điều hướng về `AD100`. |

---

### 2. Pass 2 - Quét Các Phần Tử & Logic Không Có `[No.]`

- **`[0] Screen Access & Lifecycle`:** Breadcrumbs: `＞ 事務所管理 ＞ 事務所詳細`. URL: `/admin/agencies/{agency_id}`. Khi không truyền `agency_id` hoặc truyền ID không tồn tại $\rightarrow$ Redirect về `AD100` báo `CMMSG3`.
- **`[Common-Tabs]`:** Nhấp chuyển đổi giữa 3 tab `詳細`, `ライバー一覧`, `売上` mà không làm mất thông tin định danh Agency.
- **`[Feedback / Toast]`:** Lưu thành công hiển thị Toast **`CMMSG13`** (`正常に更新されました。`).

---

## II. MA TRẬN LOGIC NGHIỆP VỤ & API SCOPE

### 1. Phân định API
- **In-Scope:**
  + `GET /agency/{agency_id}/` (Lấy dữ liệu chi tiết Agency).
  + `PATCH /agency/{agency_id}/` (Cập nhật thông tin Agency).
  + `DELETE /agency/{agency_id}/` (Xóa mềm Agency).
- **Out-of-Scope:** API của các phân hệ Liver hoặc Stream.

### 2. Bảng Q&A Làm Rõ Yêu Cầu

| No. | Control / Logic | Vấn đề chưa rõ | Câu hỏi làm rõ | Đề xuất Option A / Option B | Giả định tạm thời khi viết TC | Trạng thái |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| `Q1` | `[8] Email xác thực PEM4` | Thời gian hiệu lực link | Sau khi link xác thực PEM4 gửi đi quá 7 ngày mà Owner không bấm, trạng thái ô email như thế nào? | **Option A:** Nhãn `認証待ち` tự biến mất, email giữ nguyên giá trị cũ, link xác thực bị vô hiệu hóa.<br>**Option B:** Ô email tiếp tục hiển thị trạng thái chờ cho đến khi Admin bấm gửi lại. | **Tạm giả định theo Option A** (Tuân thủ mô tả Spec: Quá 7 ngày chưa xác thực $\rightarrow$ Hết hạn, nhãn mất, email giữ nguyên). | `Pending` |
| `Q2` | `[9] Reset Password` | Đổi mật khẩu nhưng không lưu | Nếu Admin nhập mật khẩu mới tại ô [9] nhưng bấm nút `キャンセル` ở [11] thì sao? | **Option A:** Hủy bỏ toàn bộ thao tác reset mật khẩu, mật khẩu cũ của Owner giữ nguyên hiệu lực.<br>**Option B:** Vẫn lưu mật khẩu mới. | **Tạm giả định theo Option A** (Hủy bỏ hành động tạo mật khẩu mới khi bấm Cancel). | `Pending` |
