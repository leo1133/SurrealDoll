# TÀI LIỆU BÓC TÁCH ĐẶC TẢ KỸ THUẬT & LÀM RÕ YÊU CẦU (SPEC ANALYSIS & CLARIFICATION REPORT)
## Màn hình: AD200_Register Agency (Đăng Ký Tạo Mới Agency - 事務所新規登録)
### Phân hệ: Web Master Admin Portal (`AA000`) / Quản lý Agency (`AD` Module)
### Áp dụng: Quy chuẩn Trụ Cột 1 (`Universal_Rules/01_core_spec_analysis_rule.md`) & Master Policy (`GEMINI.md`)

---

## BẢNG THÔNG TIN TỔNG QUAN ĐẶC TẢ (SPECIFICATION METADATA)

| Thuộc tính | Chi tiết |
| :--- | :--- |
| **Mã màn hình** | `AD200` |
| **Tên màn hình** | `AD200_Register Agency` (事務所管理_事務所新規登録) |
| **Phân hệ / Module** | Master Admin Web (`AA000`) / Phân hệ Quản lý Agency (`AD` Module) |
| **Người tạo Spec (Created by)** | `Ly` |
| **Ngày tạo (Created Date)** | July-15 (Cập nhật CR: 15/10/2026, 21/10/2026 GMO Sec-12) |
| **Nguồn Spec Google Sheets** | [Google Spreadsheet - Tab AD200 (gid=2093029291)](https://docs.google.com/spreadsheets/d/1pxox5GcjOXwKadMnzOa765ptG2huPJSxCiWsrH0_h7Y/edit?gid=2093029291#gid=2093029291) |
| **Nguồn Tham chiếu Nghiệp vụ** | Tab `CommonSpec` (CMR04, CMR15, CMR26, CMR30, CMR42, CMR43, CMR50, CMR68), `Common MSG`, `MSG` |
| **Nguồn Thiết kế Figma** | [Figma AD200 (node-id=907-3040)](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout---Spec-PDF?node-id=907-3040&t=CHjpqKXsbfmyHBR7-4) |
| **Luồng Điều hướng Vào** | Từ màn hình danh sách `AD100` $\rightarrow$ Click nút `新規登録` `[5]` $\rightarrow$ Mở `AD200` |
| **Luồng Điều hướng Ra** | Bấm `登録` (thành công) hoặc `キャンセル` $\rightarrow$ Điều hướng về danh sách `AD100` |
| **Ngôn ngữ hiển thị chính** | Tiếng Nhật (`JA`) |

---

## I. KẾT QUẢ QUÉT ĐẶC TẢ 2 BƯỚC BẮT BUỘC (2-PASS SCANNING PROTOCOL)

### 1. Pass 1 - Bóc Tách UI Controls Có `[No.]` (Item [1] đến [8])

| No. | Tên phần tử (Value JP) | Loại UI Control | Placeholder | Ràng buộc Validate & Nghiệp vụ (SRS & CR) |
| :---: | :--- | :--- | :--- | :--- |
| `[1]` | Side Bar UI | Navigation | - | Thanh menu điều hướng Master Admin. |
| `[2]` | `事務所名` | Textbox Input (Required ◯) | `事務所名を入力してください` | • Min 1, Max 20 ký tự. Cho phép ký tự đặc biệt.<br>• **CR 15/10/2026:** Bắt buộc duy nhất toàn hệ thống. Trùng tên với Agency khác $\rightarrow$ Báo lỗi `CMMSG57` (`事務所名は既に存在しています。`). |
| `[3]` | `事務所ID` | Textbox Input (Required ◯) | `IDを入力してください` | • Min 3, Max 20 ký tự. Chỉ cho phép chữ cái Latin và chữ số (không ký tự đặc biệt).<br>• Sai định dạng: Báo `CMMSG55` (`半角英字（a-z）と数字（0-9）のみ入力してください。`).<br>• Trùng ID đã có: Báo `MSG15` (`このIDは登録済みです。`).<br>• Trùng login ID / Email: Báo `MSG145` (`このメールアドレスまたはIDは登録済みです。`). |
| `[4]` | `事務所ロゴ` | File Upload (Required ◯) | - | • Tuân thủ **CMR50**. Định dạng: PNG, JPG/JPEG, SVG, WebP $\rightarrow$ Sai định dạng báo `CMMSG43`.<br>• Dung lượng tối đa: 5MB $\rightarrow$ Quá dung lượng báo `CMMSG45`.<br>• **CR 15/10/2026:** Bắt buộc. Mở màn để sẵn Logo mặc định = Logo hệ thống; Master có thể upload thay thế. Chỉ lưu ảnh khi bấm tạo thành công. |
| `[5]` | `連絡先 オーナー名` | Textbox Input (Required ◯) | `連絡先の名前を入力してください` | Tên người đại diện Agency. Min 1, Max 20 ký tự. Để trống báo `CMMSG29`. |
| `[6]` | `電話番号` | Textbox Input (Required ◯) | `電話番号を入力してください` | Số điện thoại đại diện. Min 5, Max 20 ký tự. Nhập tự do theo chuẩn **CMR04**. |
| `[7]` | `メールアドレス` | Textbox Input (Required ◯) | `メールアドレスを入力してください` | • Min 3, Max 254 ký tự. Định dạng email chuẩn `a@b.c` theo **CMR42**.<br>• Bắt buộc chưa từng đăng ký trên hệ thống $\rightarrow$ Trùng email báo `MSG14` (`このメールアドレスは登録済みです。`).<br>• Email dùng để đăng nhập vào portal Agency (`https://admin-dev.surrealdolls.com/sign-in/agency`). |
| `[8]` | `キャンセル` | Button (Secondary) | `キャンセル` | Tuân thủ **CMR26**. Quay về `AD100`. Hiển thị popup xác nhận nếu form đã bị chỉnh sửa (**CMMSG46**). |
| `[8]` | `登録` | Button (Primary) | `登録` | • Tuân thủ **CMR15** (chống double click / debounce).<br>• Bấm tạo Agency và tài khoản Agency Owner. Thông báo qua email mời `PEM3`.<br>• **CR 21/10/2026 (GMO Sec-12 / #12839):** BE tự sinh mật khẩu tạm 12 ký tự thỏa mãn CMR43 (không hiển thị ra UI, không gửi cho ai). Owner tự kích hoạt đặt mật khẩu qua link trong mail `PEM3` (màn `BA1003`) theo chuẩn CMR43 với thời hạn 30 ngày (**CMR68**). |

---

### 2. Pass 2 - Quét Các Phần Tử & Logic Không Có `[No.]`

- **`[0] Screen Access & Lifecycle`:** Breadcrumbs: `＞ 事務所管理 ＞ 事務所新規登録`. URL: `/admin/agencies/create`.
- **`[Common] Business Rules`:** Chỉ Master Admin được phép tạo Agency.
- **`[Feedback / Toast]`:** Tạo thành công hiển thị Toast **`CMMSG12`** (`正常に作成されました。`) và tự động chuyển về danh sách `AD100`.
- **`[Error Handling]`:** Lỗi server báo **`CMMSG1`**, lỗi mạng báo **`CMMSG8`**.

---

## II. MA TRẬN LOGIC NGHIỆP VỤ & API SCOPE

### 1. Phân định API
- **In-Scope:** `POST /agency/create/` (Payload: `name`, `code`, `image_name`, `image_path`, `contact_name`, `contact_phone`, `contact_email`).
- **Out-of-Scope:** Luồng đặt mật khẩu `BA1003` và luồng gửi mail của backend.

### 2. Bảng Q&A Làm Rõ Yêu Cầu

| No. | Control / Logic | Vấn đề chưa rõ | Câu hỏi làm rõ | Đề xuất Option A / Option B | Giả định tạm thời khi viết TC | Trạng thái |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| `Q1` | `[4] Logo mặc định` | Cơ chế Logo mặc định hệ thống | Nếu Admin xóa ảnh vừa upload nhưng không chọn ảnh mới thì form sẽ gửi ảnh nào? | **Option A:** Tự động khôi phục về Logo hệ thống mặc định.<br>**Option B:** Báo lỗi yêu cầu upload ảnh bắt buộc (`CMMSG29`). | **Tạm giả định theo Option A** (Mặc định luôn có sẵn logo hệ thống theo CR 15/10/2026). | `Pending` |
| `Q2` | `[8] Link PEM3 hết hạn` | Hết hạn 30 ngày kích hoạt | Khi link trong thư mời PEM3 quá 30 ngày bị hết hạn, Owner truy cập màn BA1003 báo lỗi gì? | **Option A:** Hiển thị thông báo `MSG19` (`無効または期限切れのリンクです。`).<br>**Option B:** Redirect về màn hình đăng nhập Agency BA100. | **Tạm giả định theo Option A** (Báo lỗi `MSG19` theo đúng mô tả Spec). | `Pending` |
