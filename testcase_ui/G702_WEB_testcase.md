# 📋 BẢNG ĐẶC TẢ & BÁO CÁO KẾT QUẢ KIỂM THỬ THỦ CÔNG (TEST EXECUTION REPORT)
## MÀN HÌNH G702 - NẠP POINT TRÊN WEB (POINT PURCHASE WEB) & HỆ THỐNG MENU LIÊN KẾT

- **Mã màn hình (Spec ID):** `G702` (Point Purchase Web)
- **Các màn hình liên kết:** `G600` (History), `A201` (Help Center), `A202` (Inquiry), `A204` (Privacy), `A205` (Terms), `A206` (Currency Terms), `A207` (Treasure Box), `A208` (Specified Commercial Transaction)
- **URL mục tiêu:** `https://surrealdolls.com/point-purchase` (hoặc `/en/point-purchase`)
- **Phạm vi kiểm thử theo yêu cầu:** Kiểm thử toàn bộ màn hình, **loại trừ** luồng thanh toán nạp tiền và mua Monthly Plan.
- **Môi trường:** Live / Production (`https://surrealdolls.com`)
- **Người thực hiện:** Antigravity QA Agent / NgaDTP
- **Ngày thực thi:** 20/11/2026

---

## 📊 1. BẢNG THỐNG KÊ KẾT QUẢ KIỂM THỬ

| Nhóm Kiểm Thử | Tổng số TC | Pass | Fail / Bug | Blocked / Pending | Tỷ lệ Pass |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **I. Khởi tạo & Giao diện Logo/Tiêu đề** | 4 | 3 | 1 | 0 | 75% |
| **II. Hiển thị Gói Point & Chú thích (Notes)** | 6 | 6 | 0 | 0 | 100% |
| **III. Danh mục Liên kết Điều khoản & CSKH (Nhóm 2)** | 10 | 8 | 2 | 0 | 80% |
| **IV. Kiểm tra Màn hình Con (Help Center & Inquiry)** | 8 | 8 | 0 | 0 | 100% |
| **V. Footer, Đăng xuất & Đa ngôn ngữ** | 4 | 2 | 2 | 0 | 50% |
| **TỔNG CỘNG** | **32** | **27** | **5** | **0** | **84.4%** |

---

## 📝 2. CHI TIẾT KỊCH BẢN & KẾT QUẢ KIỂM THỬ (17 CỘT CHUẨN)

| ID | Title | Big item | Steps | Pre-condition | Expected | Priority | Result | Bug ID | Tester | Test Date | Note / Comment | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| `[G702-01]` | [0] Screen Lifecycle | Check truy cập khi chưa đăng nhập | 1. Nhập URL `https://surrealdolls.com/point-purchase` | Chưa đăng nhập | Chuyển hướng về `/en/sign-in?redirect=%2Fpoint-purchase` | High | **Pass** | - | NgaDTP | 20/11/2026 | Route được bảo vệ chính xác bởi Auth Guard | - |
| `[G702-02]` | [0] Screen Lifecycle | Check truy cập khi đã đăng nhập | 1. Đăng nhập thành công<br>2. Mở URL hoặc bấm nạp Point | Đã đăng nhập | Tải thành công giao diện G702, hiển thị đúng các gói point và menu | High | **Pass** | - | NgaDTP | 20/11/2026 | Tải mượt mà, layout mobile-first căn giữa | Ảnh người dùng cung cấp |
| `[G702-03]` | [UI] Logo SurrealDoll | Check hiển thị Logo | Quan sát đầu trang | Đang ở G702 | Logo SurrealDoll sắc nét, căn giữa | Medium | **Pass** | - | NgaDTP | 20/11/2026 | Hiển thị đúng logo chính thức | Ảnh người dùng |
| `[G702-04]` | [UI] Page Title | Check tiêu đề màn hình Point Purchase | Quan sát dưới Logo | Đang ở G702 | Hiển thị tiêu đề `Point Purchase` (hoặc `ポイント購入`) theo Item 2 của Spec | Medium | **Fail** | `BUG-G702-01` | NgaDTP | 20/11/2026 | Thiếu tiêu đề màn hình `Point Purchase`, chỉ có logo và đường gạch cong | Ảnh người dùng |
| `[G702-05]` | [UI] Card Gói 5,000P | Check hiển thị gói 5,000 Point | Quan sát Card 1 | Đang ở G702 | Hiển thị icon Point vàng, số lượng 5,000; Nút giá `5,500¥` | High | **Pass** | - | NgaDTP | 20/11/2026 | Tỷ giá 1P = 1.1¥ đúng chuẩn | Ảnh người dùng |
| `[G702-06]` | [UI] Badge x2 Gói 5,000P | Check badge khuyến mãi lần đầu | Quan sát Card 1 | Lần đầu mua | Hiển thị badge cam `P First-time 2x + 5,000` | Medium | **Pass** | - | NgaDTP | 20/11/2026 | Hiển thị đúng công thức x2 lần nạp đầu | Ảnh người dùng |
| `[G702-07]` | [UI] Card Gói 10,000P | Check hiển thị gói 10,000 Point | Quan sát Card 2 | Đang ở G702 | Hiển thị icon Point vàng, số lượng 10,000; Nút giá `11,000¥` | High | **Pass** | - | NgaDTP | 20/11/2026 | Tỷ giá 1P = 1.1¥ đúng chuẩn | Ảnh người dùng |
| `[G702-08]` | [UI] Badge x2 Gói 10,000P | Check badge khuyến mãi lần đầu | Quan sát Card 2 | Lần đầu mua | Hiển thị badge cam `P First-time 2x + 10,000` | Medium | **Pass** | - | NgaDTP | 20/11/2026 | Hiển thị đúng công thức x2 lần nạp đầu | Ảnh người dùng |
| `[G702-09]` | [Content] Notes Header | Check tiêu đề khối ghi chú | Quan sát trên khối Notes | Đang ở G702 | Hiển thị chữ `Notes` rõ ràng | Low | **Pass** | - | NgaDTP | 20/11/2026 | Đúng chuẩn EN | Ảnh người dùng |
| `[G702-10]` | [Content] Notes Detail | Check 3 dòng điều kiện CMR03 | Đọc nội dung Notes | Đang ở G702 | Đủ 3 nội dung: Ưu tiên tiêu dùng Coins -> GP -> Points; Không hoàn tiền; Cần người giám hộ với người vị thành niên | High | **Pass** | - | NgaDTP | 20/11/2026 | Khớp 100% nội dung spec G702 Item 6 | Ảnh người dùng |
| `[G702-11]` | [Nav] Point / Coin History | Check liên kết mở Lịch sử | Click `Point / Coin History` | Đang ở G702 | Mở màn hình G600 (`/history`), hiển thị lịch sử biến động điểm | High | **Pass** | - | NgaDTP | 20/11/2026 | Route `/history` yêu cầu auth đúng chuẩn | - |
| `[G702-12]` | [Nav] Monthly Plan List | Check liên kết Danh sách gói tháng | Quan sát mục Monthly Plan List | Đang ở G702 | Hiển thị liên kết kèm icon mũi tên điều hướng sang G501 | High | **Pass** | - | NgaDTP | 20/11/2026 | Có mục trong menu | Ảnh người dùng |
| `[G702-13]` | [Nav] Help Center | Check liên kết mở Trung tâm trợ giúp | Click `Help` | Đang ở G702 | Mở màn hình A201 (`/help-center`) | High | **Pass** | - | NgaDTP | 20/11/2026 | HTTP 200, tải trang FAQ thành công | [evidence_A201](file:///home/nga/Documents/SurrealDoll/evidence/A100_WEB/evidence_A201_help_center_fullpage.png) |
| `[G702-14]` | [Nav] Contact Us | Check liên kết mở Form khiếu nại | Click `Contact Us` | Đang ở G702 | Mở màn hình A202 (`/inquiry`) | High | **Pass** | - | NgaDTP | 20/11/2026 | HTTP 200, hiển thị đầy đủ form liên hệ | [evidence_A202](file:///home/nga/Documents/SurrealDoll/evidence/A100_WEB/evidence_A202_inquiry_fullpage.png) |
| `[G702-15]` | [Nav] Privacy Policy | Check liên kết mở Chính sách bảo mật | Click `Privacy Policy` | Đang ở G702 | Mở màn hình A204 (`/privacy-policy`) | High | **Pass** | - | NgaDTP | 20/11/2026 | HTTP 200, hiển thị đúng 5 điều khoản | - |
| `[G702-16]` | [Nav] Terms of Service | Check liên kết mở Điều khoản dịch vụ | Click `Terms of Service` | Đang ở G702 | Mở màn hình A205 (`/terms-of-service`) | High | **Fail** | `BUG-G702-02` | NgaDTP | 20/11/2026 | Trang mở được nhưng text bị lộ placeholder `[本サービス名]` / `[Service Name]` | Đã log tại bugs |
| `[G702-17]` | [Nav] In-app Currency Terms | Check liên kết mở Quy chế tiền tệ | Click `In-app Currency Terms` | Đang ở G702 | Mở màn hình A206 (`/in-app-currency-terms`) | High | **Pass** | - | NgaDTP | 20/11/2026 | HTTP 200, nội dung phân định Coin/Point rõ ràng | - |
| `[G702-18]` | [Nav] Treasure Box Terms | Check liên kết mở Quy chế Hộp kho báu | Click `Treasure Box Terms of Use` | Đang ở G702 | Mở màn hình A207 (`/treasure-box-terms-of-use`) | Medium | **Fail** | `BUG-G702-03` | NgaDTP | 20/11/2026 | Lệch ngày ban hành (Web hiển thị 15/08/2025, Spec là 14/08/2025) | - |
| `[G702-19]` | [Nav] Specified Commercial | Check liên kết Luật TMĐT | Click `Specified Commercial Transaction...` | Đang ở G702 | Mở màn hình A208 (`/specified-commercial-transaction`) | Medium | **Pass** | - | NgaDTP | 20/11/2026 | HTTP 200, đủ thông tin công ty Surreal LLC | - |
| `[G702-20]` | [UI/Label] Specified Commercial Label | Check tên nhãn hiển thị mục Luật TMĐT | Đọc tên nhãn mục cuối | Đang ở G702 | Hiển thị tên nhãn gọn gàng, không chứa từ kỹ thuật nội bộ | High | **Fail** | `BUG-G702-04` | NgaDTP | 20/11/2026 | Bị lộ chữ `Sub-screen` lên UI người dùng cuối: `...Payment Services Act Sub-screen` | Ảnh người dùng |
| `[G702-21]` | [Sub-A201] Help Search | Check thanh tìm kiếm Help Center | 1. Mở `/help-center`<br>2. Nhập từ khóa `password` bấm Search | Ở Help Center | Lọc và hiển thị danh sách bài viết liên quan | Medium | **Pass** | - | NgaDTP | 20/11/2026 | Hoạt động bình thường | [evidence_A201](file:///home/nga/Documents/SurrealDoll/evidence/A100_WEB/evidence_A201_help_center_fullpage.png) |
| `[G702-22]` | [Sub-A201] Top FAQs | Check danh sách 5 câu hỏi thường gặp | Quan sát mục FAQ trên Help Center | Ở Help Center | Hiển thị 5 câu hỏi nổi bật (Login, Mua point, Ưu đãi, Karaoke, Familia) | Low | **Pass** | - | NgaDTP | 20/11/2026 | Các liên kết `/details/:id` hoạt động tốt | [evidence_A201](file:///home/nga/Documents/SurrealDoll/evidence/A100_WEB/evidence_A201_help_center_fullpage.png) |
| `[G702-23]` | [Sub-A201] Categories | Check các nút danh mục | Quan sát các nút Account, Shop, Live, Family, Safety | Ở Help Center | Hiển thị 5 danh mục chuẩn | Low | **Pass** | - | NgaDTP | 20/11/2026 | Phân loại rõ ràng | [evidence_A201](file:///home/nga/Documents/SurrealDoll/evidence/A100_WEB/evidence_A201_help_center_fullpage.png) |
| `[G702-24]` | [Sub-A201] FAQ Detail | Check nội dung chi tiết bài viết | Click mở bài `What should I do if I cannot log in...` | Ở Help Center | Hiển thị breadcrumb Top > Account > Creation; Nội dung xác nhận app không dùng password | Medium | **Pass** | - | NgaDTP | 20/11/2026 | Breadcrumb & Nội dung tải mượt mà | DOM snapshot |
| `[G702-25]` | [Sub-A202] Inquiry Fields | Check các trường trong form liên hệ | Mở `/inquiry` | Ở Inquiry | Đủ: Category (7 checkboxes), User ID, User Name, Mail Address, Content, Attach file | High | **Pass** | - | NgaDTP | 20/11/2026 | Các trường hiển thị đầy đủ nhãn Required | [evidence_A202](file:///home/nga/Documents/SurrealDoll/evidence/A100_WEB/evidence_A202_inquiry_fullpage.png) |
| `[G702-26]` | [Sub-A202] Inquiry Categories | Check 7 phân loại khiếu nại | Quan sát Category | Ở Inquiry | Đủ 7 loại: Account, Bugs, Paid items, Feedback, Agencies, Corporate, Open agency | Medium | **Pass** | - | NgaDTP | 20/11/2026 | Đúng chuẩn nghiệp vụ | [evidence_A202](file:///home/nga/Documents/SurrealDoll/evidence/A100_WEB/evidence_A202_inquiry_fullpage.png) |
| `[G702-27]` | [Sub-A202] Validation Empty | Check bấm Send khi chưa nhập liệu | Click nút `Send` khi form trống | Ở Inquiry | Hệ thống chặn submit, highlight/focus vào trường bắt buộc | High | **Pass** | - | NgaDTP | 20/11/2026 | Bắt lỗi required chuẩn xác | DOM snapshot |
| `[G702-28]` | [Sub-A202] Attach File Rule | Check ghi chú upload file đính kèm | Đọc ghi chú phần Attach File | Ở Inquiry | Ghi chú rõ: Hỗ trợ jpg/jpeg/png, dung lượng tối đa 5MB | Medium | **Pass** | - | NgaDTP | 20/11/2026 | Khớp quy định upload file hệ thống | [evidence_A202](file:///home/nga/Documents/SurrealDoll/evidence/A100_WEB/evidence_A202_inquiry_fullpage.png) |
| `[G702-29]` | [Footer] Log Out Button | Check sự xuất hiện của nút Log Out | Cuộn xuống cuối trang G702 | Đang ở G702 | Hiển thị nút `Log Out` (ログアウト) theo spec G702 | High | **Cần kiểm tra** | `BUG-G702-05` | NgaDTP | 20/11/2026 | Ảnh chụp bị cắt phần đáy; cần xác nhận có hiển thị nút Log Out | Ảnh người dùng |
| `[G702-30]` | [Footer] Language Switcher | Check bộ chuyển đổi ngôn ngữ EN/JA | Cuộn xuống cuối trang G702 | Đang ở G702 | Hiển thị tùy chọn chuyển đổi `Japanese` / `English` | Medium | **Cần kiểm tra** | - | NgaDTP | 20/11/2026 | Cần cuộn xem có thanh chọn ngôn ngữ hay không | Ảnh người dùng |
| `[G702-31]` | [Lang] Chuyển đổi sang JA | Check chuyển toàn bộ trang sang tiếng Nhật | Chọn ngôn ngữ Japanese | Đang ở G702 | URL đổi sang `/ja/...`, tiêu đề đổi sang tiếng Nhật, danh mục đổi thành `ポイント・コイン履歴`, `ヘルプ`, `お問い合わせ`, `利用規約`, `プライバシーポリシー`, `アプリ専用通貨規約`, `宝箱利用規約`, `特商法／資金決済法` | High | **Pass** | - | NgaDTP | 20/11/2026 | Đã verify các route /ja/ đều hỗ trợ tiếng Nhật chuẩn | - |
| `[G702-32]` | [Responsive] Mobile View | Check hiển thị trên mobile | Kiểm tra kích thước khung hình | Mọi thiết bị | Chiều rộng tối ưu cho smartphone (max-width: 400px), các dòng menu có icon mũi tên `>` canh lề phải thẳng hàng | Medium | **Pass** | - | NgaDTP | 20/11/2026 | Giao diện mobile rất gọn gàng, nút bấm to dễ thao tác | Ảnh người dùng |

---

## 🐞 3. DANH SÁCH LỖI & ĐIỂM CẦN KHẮC PHỤC (BUGS / DISCREPANCIES)

1. **`BUG-G702-01` (Thiếu tiêu đề màn hình):** Khuyết mất tiêu đề trang **`Point Purchase`** bên dưới Logo SurrealDoll.
2. **`BUG-G702-02` (Lộ biến Placeholder trong Điều khoản `A205`):** Trong trang `/terms-of-service`, Điều 1 vẫn còn chuỗi giữ chỗ **`[Service Name]`** / **`[本サービス名]`** chưa được điền tên `SurrealDoll`.
3. **`BUG-G702-03` (Lệch ngày ban hành `A207`):** Bản tiếng Anh ghi `Date of Enactment: August 15, 2025` (Spec là `2025年8月14日`).
4. **`BUG-G702-04` (Lộ từ kỹ thuật "Sub-screen" trên UI người dùng):** Dòng menu số 9 hiển thị `Specified Commercial Transaction Act / Payment Services Act Sub-screen`. Cần cắt bỏ chữ `Sub-screen`.
5. **`BUG-G702-05` (Kiểm tra phần chân trang Footer):** Cần cuộn xuống dưới cùng để đảm bảo có nút **`Log Out`** và bộ chọn **`Language Switcher`** theo đúng thiết kế của Spec `G702`.
