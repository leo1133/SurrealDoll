# BẢN ĐỒ PHÂN RÃ TÍNH NĂNG & ĐẶC TẢ HỆ THỐNG SURREALDOLL (FEATURE & SPEC MAP)

> **Mục đích:** Tài liệu tra cứu nhanh cấu trúc tính năng chi tiết (457 màn hình, 35 cụm gốc -> **73 cụm tính năng chi tiết**) dùng trực tiếp khi **Test / Verify Bug / Phân tích Spec** cho dự án SurrealDoll.
> **Cách sử dụng nhanh:** Khi kiểm thử hoặc verify bug, chỉ cần nêu **Mã màn hình** (VD: `BD500`, `AQ100`, `I303`, `K203`) hoặc **Tên tính năng** (VD: *2-shot*, *Payout*, *ACRCloud*, *Gacha*), AI sẽ tra cứu ngay cụm tính năng, spec cốt lõi, điểm cần verify và các màn hình liên quan chéo (Admin ↔ Agency ↔ App).
> **Nguồn dữ liệu gốc:** Google Spreadsheet `1pxox5GcjOXwKadMnzOa765ptG2huPJSxCiWsrH0_h7Y` (Sheet `Overview`) + Kho tài liệu local (`Q&A/`, `testcase_ui/`, `testcase_api/`, `bugs/`, `test_specs/`).

---

## I. TỔNG QUAN HỆ THỐNG & MA TRẬN LIÊN KẾT CHÉO (CROSS-ROLE MATRIX)

| Nhóm (Group) | Vai trò | Số cụm gốc | Số cụm chi tiết | Số màn hình |
| :--- | :--- | :---: | :---: | :---: |
| **Admin** | CMS Quản trị trung tâm toàn nền tảng | 16 | 20 | 82 |
| **Agency** | Cổng Portal cho Công ty quản lý / Đại lý Streamer | 7 | 8 | 28 |
| **App** | Ứng dụng Mobile (iOS/Android) & Webview tích hợp | 12 | 45 | 347 |
| **TỔNG** | **Toàn bộ hệ thống SurrealDoll** | **35** | **73** | **457** |

### Ma trận Nghiệp vụ Liên thông 3 Cổng (Admin ↔ Agency ↔ App)

> Dùng để kiểm tra ảnh hưởng dây chuyền (Regression / Side-effect) khi verify bug.

| Luồng Nghiệp vụ | Admin CMS | Agency Portal | Mobile App / Webview |
| :--- | :--- | :--- | :--- |
| **Quản lý Agency & Liên kết Liver** | `AD100`, `AD200`, `AD301`, `AD302` | `BA100`, `BB100-BB300`, `BC100`, `BC200` | `K203` (Join/Exit Agency) |
| **Hồ sơ User, eKYC & Xóa tài khoản** | `AE100`, `AE200`, `AE700`, `K2022` | `BC100`, `BC200` | `K000`, `K800`, `K205` (eKYC), `K2022` |
| **Tài sản, Billing & Doanh thu / Rút tiền** | `AE300-AE800`, `AS100`, `AS200`, `AS300`, `AS500` | `BD100-BD500` | `G501-G702`, `K601-K6013`, `K906-K9066` |
| **Giám sát Livestream, Ban & Archive** | `AG100-AG500`, `AY100-AY300` | `BF100-BF500`, `BY100`, `BY300` | `I099-I805`, `M100-M500`, `D701-D705`, `K9051-K9054`, `OBS` |
| **Quà tặng, 3D Model, BG & Gacha** | `AF100-AF500`, `AP000-AP400`, `AK201-AK303`, `AQ100-AQ500` | - | `A209`, `G200-G302`, `I600-I701`, `M0011-M00131`, `M20501-M20504` |
| **Karaoke, BGM & Bản quyền (JASRAC/ACRCloud)** | `AJ100-AJ400`, `AL100-AL400`, `AL600`, `AL700` | - | `I501-I509`, `M401-M409`, `M20514`, `K010-K0142`, `K209-New` |
| **Bài đăng Familia & Kiểm duyệt** | `AM100`, `AM101`, `AM200` | `BE100`, `BE200` | `L100-L600` |
| **Tin nhắn, Thông báo & Báo cáo Vi phạm** | `AH100-AH400`, `AI100-AI200`, `AX100-AX300` | `BG100-BG200`, `BX100` | `E201-E203`, `F100-F500`, `D2021-D2023`, `I804` |


---
## II. NHÓM: ADMIN (82 MÀN HÌNH)

### 1. Tài khoản Quản trị & Phân quyền (Auth & Permissions) (9 màn hình)

#### 1.1 Xác thực & Quên/Đổi mật khẩu Admin (5 màn hình)

- **Tính năng chính & Spec:** Đăng nhập CMS Admin (`AA000`), đổi mật khẩu khi đang đăng nhập (`AA003`), luồng yêu cầu quên mật khẩu qua email & đặt lại mật khẩu mới (`AB000`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra rule mật khẩu (độ dài, ký tự đặc biệt), token reset hết hạn, khóa tài khoản khi sai nhiều lần, session timeout.
- **Liên kết chéo:** Tương đồng luồng Auth với Agency (`BA100`, `BA200`, `BA1001-BA1003`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `AA000` | Login top | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=38-118&t=PP6ucS40pj6MfR2T-0) |
| `AA003` | Change Password | - | ADMIN | Spec done / Done / WIP / Backlog (sắp gửi) | Local: `Bug, SpecJSON` |
| `AB000` | Password change request completed | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=44-14&t=PP6ucS40pj6MfR2T-0) |
| `AB000` | Change password | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=44-14&t=jCGRsmLKUC6um4fM-4) |
| `AB000` | Password change request | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=38-241&t=PP6ucS40pj6MfR2T-0) |


#### 1.2 Quản lý Tài khoản & Phân quyền System Admin (4 màn hình)

- **Tính năng chính & Spec:** Danh sách/tìm kiếm System Admin (`AC100`), tạo mới (`AC200`), cập nhật/xóa (`AC300`), và cấu hình ma trận phân quyền RBAC (`AC400`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra phân quyền thực tế trên sidebar/API theo role được gán ở `AC400`, validate email trùng, không cho tự xóa/hạ quyền chính mình.
- **Liên kết chéo:** Áp dụng phân quyền cho toàn bộ module `AD`–`AY` trong Admin CMS.

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `AC100` | System Admin Manage - System Admin List, Search | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=30-2&t=PP6ucS40pj6MfR2T-0) |
| `AC200` | System Admin Manage - System Admin Create | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=31-62&t=PP6ucS40pj6MfR2T-0) |
| `AC300` | System Admin Manage - System Admin Update | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=37-2&t=PP6ucS40pj6MfR2T-0) |
| `AC400` | Phân quyền system admin | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | - |


### 2. Quản lý Agency / Đại lý (Agency Management) (4 màn hình)

#### 2.1 Quản lý Hồ sơ Agency & Danh sách Streamer trực thuộc (4 màn hình)

- **Tính năng chính & Spec:** Tìm kiếm/lọc danh sách Agency (`AD100`), đăng ký Agency mới (`AD200`), xem/sửa/xóa chi tiết Agency (`AD301`) và xem danh sách Streamer/Liver thuộc Agency (`AD302`).
- **Trọng tâm Test / Verify Bug:** Validate thông tin thuế/ngân hàng/email liên hệ Agency; khi xóa/khóa Agency kiểm tra trạng thái đăng nhập cổng Agency (`BA100`) và liên kết của Liver (`K203`).
- **Liên kết chéo:** Liên kết trực tiếp với Agency Portal (`BB100-BB300`, `BC100`) và App (`K203` Join/Exit Agency).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `AD302` | Agency Manage - Agency Streamer List | 事務所詳細 - ライバー一覧 | ADMIN | Spec done / Done / Done / Done (đã gửi) | - |
| `AD100` | Agency Manage - Agency List / Search | - | ADMIN | Spec done / Done / Done / Done (sắp gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=16-325&t=PP6ucS40pj6MfR2T-0) |
| `AD200` | Agency Manage - Register Agency | - | ADMIN | Spec done / Done / Done / Done (sắp gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=16-381&t=PP6ucS40pj6MfR2T-0) · Local: `Bug` |
| `AD301` | Agency Manage - Agency Detail, Update, Delete | - | ADMIN | Spec done / Done / Done / Done (sắp gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=16-473&t=PP6ucS40pj6MfR2T-0) |


### 3. Quản lý Người dùng (User Management) (9 màn hình)

#### 3.1 Hồ sơ Người dùng, Xác thực eKYC & Xóa tài khoản (4 màn hình)

- **Tính năng chính & Spec:** Danh sách/tìm kiếm người dùng (`AE100`), chi tiết hồ sơ (`AE200`), kiểm duyệt eKYC & OCR giấy tờ tùy thân (`AE700`), xóa tài khoản từ Admin (`K2022`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra trạng thái duyệt/từ chối eKYC đồng bộ về App (`K205`) và mở khóa tính năng rút tiền (`K906`); kiểm tra logic đóng tài khoản khi còn số dư GOLD/Point.
- **Liên kết chéo:** Liên kết với Agency (`BC100`, `BC200`) và App (`K000`, `K205`, `K2022`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `AE100` | User List | 利用者一覧 | ADMIN | Spec done / Done / Done / Done (đã gửi) | - |
| `AE200` | User Details | 利用者詳細 | ADMIN | Spec done / Done / Done / Done (đã gửi) | - |
| `AE700` | User Details - Ekyc and OCR | 利用者詳細 - 認証 | ADMIN | Spec done / Done / Done / Done (sắp gửi) | - |
| `K2022` | Delete ACCOUNT ADMIN | - | ADMIN | WIP / Backlog / Backlog / Backlog (chưa gửi) | - |


#### 3.2 Tài sản, Lịch sử sử dụng, Hóa đơn & Doanh thu Người dùng (5 màn hình)

- **Tính năng chính & Spec:** Xem vật phẩm sở hữu (`AE300`), lịch sử sử dụng (`AE400`), lịch sử nạp/gói tháng Billing Log (`AE500`), thông tin thanh toán (`AE600`) và chi tiết doanh thu cá nhân (`AE800`).
- **Trọng tâm Test / Verify Bug:** Đối chiếu số liệu tổng hợp với DB (`users`, `orders`, `payments`, `gifts`), kiểm tra phân trang, lọc theo khoảng ngày và export/tính toán hoa hồng.
- **Liên kết chéo:** Liên kết với Agency (`BD100-BD500`), Admin Sales (`AS100`) và App (`G600`, `K601`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `AE300` | User Details - Owned Items | 利用者詳細 - 所持アイテム | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | Local: `Bug` |
| `AE400` | User Details - Usage History | 利用者詳細 - 利用履歴 | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | - |
| `AE500` | User Details - Billing Log | 利用者詳細 - 課金情報 | ADMIN | Spec done / Done / Done / Done (sắp gửi) | - |
| `AE600` | User Details - Payment Information | 利用者詳細 - 決済情報 | ADMIN | Spec done / Done / Done / Done (sắp gửi) | - |
| `AE800` | User Detail - Revenue | ライバー個別売上詳細 | ADMIN | WIP / Backlog / Backlog / Backlog (chưa gửi) | - |


### 4. Quản lý Quà tặng (Gift Management) (5 màn hình)

#### 4.1 Danh mục, CRUD Quà tặng & Quà cao cấp (5 màn hình)

- **Tính năng chính & Spec:** Quản lý danh sách quà (`AF100`), tạo/sửa/xóa quà tặng (`AF200`, `AF300`), quản lý danh mục quà (`AF400`) và cấu hình quà cao cấp/hiệu ứng đặc biệt (`AF500`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra upload asset (animation/icon), giá coin, thứ tự hiển thị, trạng thái ON/OFF đồng bộ realtime lên danh sách quà trong phòng Live (`I600`).
- **Liên kết chéo:** Hiển thị trực tiếp trên App Livestream (`I600`, `I601`) và Wishlist (`M1011`, `M20507`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `AF100` | Gift Manage - Gift List | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=7-185&t=PP6ucS40pj6MfR2T-0) |
| `AF200` | Gift Manage - Gift Create | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=9-82&t=PP6ucS40pj6MfR2T-0) |
| `AF300` | Gift Manage - Gift Update, Delete | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=9-218&t=PP6ucS40pj6MfR2T-0) |
| `AF400` | Gift Manage - Gift Category Manage | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=10-2&t=PP6ucS40pj6MfR2T-0) |
| `AF500` | Quà cao cấp | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | - |


### 5. Giám sát & Quản lý Phòng Livestream (Stream Management) (5 màn hình)

#### 5.1 Giám sát Phòng Live đang phát, Xem trực tiếp & Archive (5 màn hình)

- **Tính năng chính & Spec:** Danh sách phòng đang live (`AG100`), xem luồng livestream trực tiếp (`AG200`), quản lý danh sách bị Ban (`AG300`), danh sách bị Force Stop (`AG400`), và xem lại các phiên đã kết thúc (`AG500`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra thao tác Force Stop từ Admin có ngắt phòng live trên App (`M200`/`I100`) ngay lập tức không; kiểm tra log lý do Ban/Force Stop và phát lại video Archive.
- **Liên kết chéo:** Liên kết 3 chiều với Agency (`BF100-BF500`) và App (`I100`, `M200`, `D701`, `K9051`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `AG100` | Stream Manage - List Stream | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=38-5&t=PP6ucS40pj6MfR2T-0) |
| `AG200` | Stream Manage - View Stream | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=38-46&t=PP6ucS40pj6MfR2T-0) |
| `AG300` | Stream Manage - List Ban | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=187-2&t=VkZJ0khbJSIUN0Bv-0) |
| `AG400` | Stream Manage - List Force Stop | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=233-2&t=V7Gh86GnJ5eyrL7M-0) |
| `AG500` | Stream Manage - List + View Stream（ENDED) | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout---Spec-PDF?node-id=4270-159&t=8pUolOlApo5cHGvm-0) |


### 6. Quản lý Thông báo & Tin nhắn Admin (Announcements & Messages) (5 màn hình)

#### 6.1 Quản lý Thông báo Hệ thống & Tin nhắn từ Admin (5 màn hình)

- **Tính năng chính & Spec:** Danh sách thông báo (`AH100`), tạo/sửa thông báo (`AH200`, `AH300`), xem trước nội dung (`AH301`) và gửi tin nhắn hệ thống từ Admin (`AH400`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra hẹn giờ đăng (publish schedule), đối tượng nhận (All/User/Streamer), render HTML/Webview trên App (`E201`, `E202`, `I804`) và tin nhắn hệ thống (`F103`).
- **Liên kết chéo:** Hiển thị tại App (`E201`, `E202`, `I804`, `I8041`, `F103`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `AH100` | Announcement Manage - Announcement List | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=12-125&t=PP6ucS40pj6MfR2T-0) |
| `AH200` | Announcement Manage - Announcement Create | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=12-199&t=PP6ucS40pj6MfR2T-0) |
| `AH300` | Announcement Manage - Announcement Edit | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=13-265&t=PP6ucS40pj6MfR2T-0) |
| `AH301` | Announcement Manage - Announcement Preview | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=247-22&t=MpuKPiNMSRzzDHbS-0) |
| `AH400` | Message Admin | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=523-2&t=sbky8gFpMmQK76Bf-0) |


### 7. Quản lý Báo cáo vi phạm (Report Management) (2 màn hình)

#### 7.1 Xử lý Báo cáo Vi phạm (Report Management) (2 màn hình)

- **Tính năng chính & Spec:** Danh sách báo cáo vi phạm (`AI100`) và chi tiết xử lý báo cáo (`AI200`) đối với user, bài đăng, tin nhắn hoặc livestream.
- **Trọng tâm Test / Verify Bug:** Kiểm tra lọc theo loại vi phạm/trạng thái xử lý, xem bằng chứng đính kèm, cập nhật trạng thái xử lý và đồng bộ với Agency (`BG100`, `BG200`).
- **Liên kết chéo:** Nhận dữ liệu từ App (`D2021-D2023`) và đồng bộ với Agency (`BG100`, `BG200`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `AI100` | Report Manage - Report List | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout---Spec-PDF?node-id=805-4432&t=nHgdT0MfbOkJnPqw-0) |
| `AI200` | Report Manage - Report Detail | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout---Spec-PDF?node-id=805-4432&t=nHgdT0MfbOkJnPqw-0) |


### 8. Quản lý BGM & Nhạc nền (BGM Management) (4 màn hình)

#### 8.1 Quản lý Kho BGM & Chuyển đổi định dạng Audio (4 màn hình)

- **Tính năng chính & Spec:** Danh sách nhạc nền BGM (`AJ100`), thêm mới (`AJ200`), chỉnh sửa (`AJ300`) và luồng convert MP3 sang WAV (`AJ400`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra upload file âm thanh, dung lượng/định dạng hợp lệ, quá trình convert MP3->WAV không lỗi, trạng thái hiển thị trong phòng live (`M20514`).
- **Liên kết chéo:** Cung cấp kho nhạc nền cho Streamer trên App (`M20514`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `AJ100` | BGM Manage - BGM List | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=20-2&t=PP6ucS40pj6MfR2T-0) |
| `AJ200` | BGM Manage - BGM Create | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=21-83&t=PP6ucS40pj6MfR2T-0) |
| `AJ300` | BGM Manage - BGM Edit | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=24-174&t=PP6ucS40pj6MfR2T-0) |
| `AJ400` | BGM Manage - MP3 WAV Convert | - | ADMIN | Spec done / Done / Done / Done (-) | - |


### 9. Quản lý Hình nền & Mini Garden (Background & Garden Management) (6 màn hình)

#### 9.1 Quản lý Hình nền Minh họa (Background Illustrations) (3 màn hình)

- **Tính năng chính & Spec:** Danh sách (`AK201`), tạo mới (`AK202`), chỉnh sửa (`AK203`) hình nền dùng trong livestream.
- **Trọng tâm Test / Verify Bug:** Kiểm tra upload ảnh/tỷ lệ khung hình, trạng thái kích hoạt và đồng bộ sang App (`M00131`, `M20504`).
- **Liên kết chéo:** Liên kết với App Streamer Background (`M00131`, `M20504`) và BG Gacha (`AQ500`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `AK201` | Background Illustrations Manage - Background Illustrations List | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=24-442&t=PP6ucS40pj6MfR2T-0) |
| `AK202` | Background Illustrations Manage - Background Illustrations Create | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=24-599&t=PP6ucS40pj6MfR2T-0) |
| `AK203` | Background Illustrations Manage - Background Illustrations Edit | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=24-633&t=PP6ucS40pj6MfR2T-0) |


#### 9.2 Quản lý Hình nền Mini Garden (3 màn hình)

- **Tính năng chính & Spec:** Danh sách (`AK301`), tạo mới (`AK302`), chỉnh sửa (`AK303`) hình nền Mini Garden.
- **Trọng tâm Test / Verify Bug:** Kiểm tra cấu hình asset Mini Garden, trạng thái hiển thị và liên kết với Mini Garden Gacha (`AQ400`).
- **Liên kết chéo:** Liên kết với Admin Gacha (`AQ400`) và App Shop/Gacha.

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `AK301` | Mini Garden Background Manage - Mini Garden Background List | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=24-486&t=PP6ucS40pj6MfR2T-0) |
| `AK302` | Mini Garden Background Manage - Mini Garden Background Create | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=24-534&t=PP6ucS40pj6MfR2T-0) |
| `AK303` | Mini Garden Background Manage - Mini Garden Background Edit | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=24-567&t=PP6ucS40pj6MfR2T-0) |


### 10. Quản lý Karaoke & Báo cáo Bản quyền (Karaoke & Copyright Reports) (9 màn hình)

#### 10.1 Quản lý Kho bài hát Karaoke & Yêu cầu thêm bài (5 màn hình)

- **Tính năng chính & Spec:** Danh sách bài hát (`AL100`), upload hàng loạt/file (`AL101`), tạo mới (`AL200`), chỉnh sửa (`AL300`) và danh sách yêu cầu thêm bài hát mới từ user (`AL400`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra đồng bộ file lyric/audio/beat, trạng thái duyệt request ở `AL400` phản hồi về `M4071`/`M4072`.
- **Liên kết chéo:** Cung cấp dữ liệu cho Karaoke trên App (`I501-I509`, `M401-M409`, `K010-K0142`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `AL100` | Karaoke Manage - Karaoke List | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=6-62&p=f&t=xoky5jpjZLSUcFOj-0) |
| `AL101` | Karaoke Manage - Karaoke Upload | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=437-288&t=kiFSV2uBo32aXJJc-0) |
| `AL200` | Karaoke Manage - Karaoke Create | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout---Spec-PDF?node-id=378-2&t=bQLcTTTRdjDgHb8A-0) |
| `AL300` | Karaoke Manage - Karaoke Edit | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=374-94&t=xrmOzOq1g2cuovrL-0) |
| `AL400` | Karaoke Manage - Karaoke Request List | - | ADMIN | Spec done / Done / Done / Done (IS CLOSE) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=383-175&t=xrmOzOq1g2cuovrL-0) |


#### 10.2 Báo cáo Bản quyền Âm nhạc (JASRAC / NEXTONE) & Nội dung trả phí (4 màn hình)

- **Tính năng chính & Spec:** Báo cáo bài hát sử dụng cho JASRAC/NEXTONE (`AL600`), danh sách & chi tiết báo cáo bài hát user đã dùng (`AL700`), danh sách nội dung trả phí (`AL700`).
- **Trọng tâm Test / Verify Bug:** Đối chiếu dữ liệu nhận diện ACRCloud/nhập tay từ App (`K209-New`), kiểm tra xuất file CSV/báo cáo chuẩn định dạng JASRAC/NEXTONE và tính toán kỳ báo cáo.
- **Liên kết chéo:** Nhận dữ liệu trực tiếp từ App (`K209-New` ACRCloud Report of Used Songs).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `AL600` | JASRAC / NEXTONE Used Song Reports | JASRAC・NEXTONE利用楽曲の報告 | ADMIN | Spec done / Done / Done / Done (đã gửi) | OK |
| `AL700` | User Used Song Report List | ユーザー利用曲目報告一覧 | ADMIN | Spec done / Done / Done / Done (đã gửi) | - |
| `AL700` | User Used Song Report Details | ユーザー利用曲目報告詳細 | ADMIN | Spec done / Done / Done / Done (đã gửi) | - |
| `AL700` | Paid Content List | 有料コンテンツ一覧 | ADMIN | Spec done / Done / Done / Done (đã gửi) | - |


### 11. Quản lý Bài đăng (Post Management) (3 màn hình)

#### 11.1 Quản lý & Kiểm duyệt Bài đăng Familia (Post Management) (3 màn hình)

- **Tính năng chính & Spec:** Danh sách toàn bộ bài đăng (`AM100`), bài đăng theo từng user (`AM101`) và chi tiết bài đăng (`AM200`) để kiểm duyệt/ẩn/xóa nội dung vi phạm.
- **Trọng tâm Test / Verify Bug:** Kiểm tra tìm kiếm theo user/từ khóa, xem media đính kèm (ảnh/video/audio) và thao tác ẩn/xóa bài đăng đồng bộ về Agency (`BE100-BE200`) và App (`L402-L406`).
- **Liên kết chéo:** Liên kết với Agency (`BE100`, `BE200`) và App Familia (`L202-L203`, `L402-L406`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `AM100` | Post List | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=274-2&t=JdxpsD2arSGxW8zb-0) |
| `AM101` | {user_name}'s Post List | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=279-125&t=JdxpsD2arSGxW8zb-0) |
| `AM200` | Post Details | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=280-179&t=JdxpsD2arSGxW8zb-0) |


### 12. Quản lý 3D Model & Avatar (3D Model & Avatar Management) (6 màn hình)

#### 12.1 Quản lý 3D Model, Bộ phận (Head/Body/Accessory) & Độ phân giải (6 màn hình)

- **Tính năng chính & Spec:** Danh sách 3D Model (`AP000`), cấu hình độ phân giải (`AP000`), chi tiết Model (`AP100`), chi tiết Head (`AP200`), Body (`AP300`) và Phụ kiện Accessory (`AP400`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra upload asset 3D/texture, cấu hình thông số độ phân giải đồng bộ với thiết lập trên App (`M100`, `M0011-M00121`) và Gacha Avatar (`AQ100-AQ300`).
- **Liên kết chéo:** Liên kết với App Model Setup (`M0011-M00121`, `M100`) và Admin Gacha (`AQ100`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `AP000` | List model | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout---Spec-PDF?node-id=1879-5896&t=Ocw6PySfCe7ijLko-4) |
| `AP100` | Model detail | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout---Spec-PDF?node-id=1879-5896&t=Ocw6PySfCe7ijLko-4) |
| `AP200` | Head detail | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout---Spec-PDF?node-id=1940-469&t=Ocw6PySfCe7ijLko-4) |
| `AP300` | Body Detail | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout---Spec-PDF?node-id=1940-469&t=Ocw6PySfCe7ijLko-4) |
| `AP400` | Accessory | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout---Spec-PDF?node-id=1940-469&t=Ocw6PySfCe7ijLko-4) |
| `AP000` | Admin Model - Setting độ phân giải | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | - |


### 13. Quản lý Gacha (Gacha Management) (5 màn hình)

#### 13.1 Quản lý Gacha (Avatar, Mini Garden & Background Gacha) (5 màn hình)

- **Tính năng chính & Spec:** Danh sách Avatar Gacha (`AQ100`), chi tiết (`AQ200`), thiết lập tỷ lệ & pool item (`AQ300`), quản lý Mini Garden Gacha (`AQ400`) và Background Gacha (`AQ500`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra tổng tỷ lệ rơi (%) phải bằng 100%, cấu hình thời gian mở/đóng banner, giá quay bằng Coin/Ticket, hiển thị bảng tỷ lệ trên Webview (`A209`) và Shop (`G200-G201`).
- **Liên kết chéo:** Liên kết trực tiếp với App Shop Gacha (`G200-G203`, `I700-I701`) và Webview tỷ lệ (`A209`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `AQ100` | Quản lý Gacha - avatar gacha | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout---Spec-PDF?node-id=2212-6649&t=TA0MmRBbs5dWb7GL-4) · OK |
| `AQ200` | Quản lý Gacha - avatar gacha detail | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | OK |
| `AQ300` | Quản lý Gacha - avatar gacha Setup | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | OK |
| `AQ400` | Quản lý Gacha -  mini garden gacha | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout---Spec-PDF?node-id=2212-6649&t=TA0MmRBbs5dWb7GL-4) · OK |
| `AQ500` | Quản lý Gacha - BG gacha | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout---Spec-PDF?node-id=2212-6649&t=TA0MmRBbs5dWb7GL-4) · OK |


### 14. Báo cáo Doanh thu & Rút tiền (Sales & Financial Analytics) (4 màn hình)

#### 14.1 Phân tích Doanh thu, Tỷ giá & Duyệt Yêu cầu Rút tiền (Payout) (4 màn hình)

- **Tính năng chính & Spec:** Dashboard phân tích doanh thu User (`AS100`), doanh thu theo Agency (`AS500`), cấu hình tỷ giá quy đổi (`AS300`) và xử lý yêu cầu rút tiền (`AS200`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra công thức tính doanh thu gộp/thuần (trừ phí Store Apple/Google, tỷ giá `AS300`, hoa hồng Agency), duyệt/từ chối Payout ở `AS200` cập nhật trạng thái về App (`K9064-K9066`).
- **Liên kết chéo:** Liên kết với Admin User Revenue (`AE800`), Agency (`BD500`) và App (`K601`, `K906-K9066`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `AS500` | Sales - Agency Revenue Analysis | 事業所個別売上詳細 | ADMIN | WIP / Backlog / Backlog / Backlog (chưa gửi) | - |
| `AS200` | Sales - Payout Request | 換金リクエスト | ADMIN | WIP / Backlog / Backlog / Backlog (chưa gửi) | - |
| `AS300` | Sales - Exchange Rate | 交換レート | ADMIN | WIP / Backlog / Backlog / Backlog (chưa gửi) | - |
| `AS100` | Sales - User Revenue Analysis | 売上分析ダッシューボード | ADMIN | Spec done / Done / Done / WIP (sắp gửi) | Local: `Bug` |


### 15. Quản lý & Giám sát Tin nhắn (User Messages Monitoring) (3 màn hình)

#### 15.1 Giám sát Tin nhắn Người dùng (User Messages Monitoring) (3 màn hình)

- **Tính năng chính & Spec:** Tìm kiếm hội thoại (`AX100`), xem chi tiết nội dung tin nhắn (`AX200`) và thông tin hội thoại/thành viên (`AX300`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra tìm kiếm theo user/khoảng thời gian/từ khóa, hiển thị đúng loại tin nhắn (text, stamp, 2shot invite) và phân quyền xem dữ liệu nhạy cảm.
- **Liên kết chéo:** Liên kết với Agency (`BX100`) và App Direct Messages (`F100-F500`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `AX100` | Message Manage - Search | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=524-2&t=lAsILjEWp13eQtp7-0) |
| `AX200` | Message Manage - Message Detail | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=537-2&t=lAsILjEWp13eQtp7-0) |
| `AX300` | Message Manage - Message Info | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout?node-id=542-443&t=lAsILjEWp13eQtp7-0) |


### 16. Giám sát Bình luận & Cấm Chat Livestream (Livestream Chat Monitoring) (3 màn hình)

#### 16.1 Giám sát Bình luận & Danh sách Cấm Chat Livestream (3 màn hình)

- **Tính năng chính & Spec:** Tìm kiếm bình luận livestream (`AY100`), xem chi tiết log chat của phiên live (`AY200`) và quản lý danh sách user bị Ban chat (`AY300`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra thao tác Ban/Unban chat từ Admin có hiệu lực ngay với phiên live và đồng bộ với Agency (`BY100`, `BY300`).
- **Liên kết chéo:** Liên kết với Agency (`BY100`, `BY300`) và App Livestream (`I100`, `I1013`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `AY100` | Livestream messsage - Search | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout---Spec-PDF?node-id=805-4243&t=plFaaXRqTT1M4rnp-0) |
| `AY200` | Livestream messsage - Detail | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout---Spec-PDF?node-id=1211-2&t=plFaaXRqTT1M4rnp-0) |
| `AY300` | Livestream messsage - BAN LIST | - | ADMIN | Spec done / Done / Done / Done (đã gửi) | [Link](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout---Spec-PDF?node-id=1117-146&t=plFaaXRqTT1M4rnp-0) |



---
## III. NHÓM: AGENCY (28 MÀN HÌNH)

### 1. Xác thực & Mật khẩu Agency (Auth & Password) (5 màn hình)

#### 1.1 Đăng nhập & Đổi/Quên mật khẩu Cổng Agency (5 màn hình)

- **Tính năng chính & Spec:** Đăng nhập cổng Agency (`BA100`), đổi mật khẩu khi đang đăng nhập (`BA200`), gửi yêu cầu quên mật khẩu (`BA1001`), màn hình hoàn tất gửi mail (`BA1002`) và đặt lại mật khẩu qua link token (`BA1003`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra Basic Auth + rule mật khẩu, khóa tài khoản Agency khi bị Admin disable (`AD301`), token hết hạn/đã sử dụng ở `BA1003`.
- **Liên kết chéo:** Tài khoản Agency được tạo/quản lý từ Admin (`AD200`, `AD301`) và nhân viên ở `BB200`.

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `BA100` | Login top | ログイントップ | Agency | Spec done / Done / WIP / Backlog (sắp gửi) | Local: `Bug, SpecJSON` |
| `BA200` | Change Password | パスワード変更 | Agency | Spec done / Done / WIP / Backlog (sắp gửi) | Local: `Bug, SpecJSON` |
| `BA1001` | Password change request | パスワード変更申込 | Agency | Spec done / Done / WIP / Backlog (sắp gửi) | Local: `Bug, SpecJSON` |
| `BA1002` | Password change request completed | パスワード変更申込完了 | Agency | Spec done / Done / WIP / Backlog (sắp gửi) | Local: `Bug, SpecJSON` |
| `BA1003` | Change password | パスワード再設定 | Agency | Spec done / Done / WIP / Backlog (sắp gửi) | Local: `Bug, SpecJSON` |


### 2. Quản lý Thông tin Agency & Quản trị viên (Agency Info & Staff Admin) (4 màn hình)

#### 2.1 Thông tin Agency & Quản lý Quản trị viên trực thuộc (4 màn hình)

- **Tính năng chính & Spec:** Xem chi tiết thông tin Agency (`BB101`), danh sách quản trị viên Agency (`BB100`), tạo mới (`BB200`) và xem/sửa chi tiết quản trị viên (`BB300`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra phân quyền Owner vs Staff Agency, validate email/tên đăng nhập trùng, cập nhật thông tin ở `BB101` đồng bộ với Admin (`AD301`).
- **Liên kết chéo:** Liên kết với Admin Agency (`AD301`) và Auth Agency (`BA100`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `BB101` | Agency Detail | 事務所詳細 | Agency | Spec done / WIP / WIP / Backlog (sắp gửi) | Local: `Bug` |
| `BB100` | Agency Admin List | 事務所管理者一覧 | Agency | Spec done / Done / WIP / Backlog (sắp gửi) | - |
| `BB200` | Agency Admin Create | 事務所管理者新規登録 | Agency | Spec done / Done / WIP / Backlog (sắp gửi) | - |
| `BB300` | Agency Admin Detail | 事務所管理者詳細 | Agency | Spec done / Done / WIP / Backlog (sắp gửi) | Local: `Bug` |


### 3. Quản lý Streamer / Liver & Tài chính (Streamer Management & Analytics) (7 màn hình)

#### 3.1 Quản lý Danh sách & Hồ sơ Streamer / Liver trực thuộc (2 màn hình)

- **Tính năng chính & Spec:** Danh sách Liver thuộc Agency (`BC100`) và chi tiết hồ sơ Liver (`BC200`), bao gồm duyệt/quản lý Liver tham gia hoặc rời Agency.
- **Trọng tâm Test / Verify Bug:** Kiểm tra chỉ hiển thị Liver thuộc Agency hiện tại (Data Isolation), xử lý yêu cầu gia nhập/rời Agency từ App (`K203`).
- **Liên kết chéo:** Liên kết với Admin (`AD302`, `AE100-AE200`) và App (`K203`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `BC200` | Liver Details | ライバー詳細 | Agency | Spec done / WIP / WIP / Backlog (sắp gửi) | Local: `Bug` |
| `BC100` | Liver List | ライバー一覧 | Agency | Spec done / WIP / WIP / Backlog (sắp gửi) | Local: `Bug` |


#### 3.2 Tài sản, Lịch sử, Billing & Doanh thu của Liver (5 màn hình)

- **Tính năng chính & Spec:** Xem vật phẩm sở hữu (`BD100`), lịch sử sử dụng (`BD200`), lịch sử gói tháng (`BD300`), thông tin thanh toán (`BD400`) và phân tích doanh thu Liver (`BD500`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra dữ liệu chỉ giới hạn trong phạm vi Liver của Agency; đối chiếu số liệu doanh thu/hoa hồng với Admin (`AE800`, `AS500`).
- **Liên kết chéo:** Liên kết với Admin (`AE300-AE600`, `AE800`, `AS500`) và App (`K601`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `BD100` | Liver Details - Owned Items | 所有アイテム | Agency | Spec done / Done / Done / Backlog (sắp gửi) | Local: `Bug` |
| `BD200` | Liver Details - Usage History | 利用履歴 | Agency | Spec done / Done / WIP / Backlog (sắp gửi) | Local: `Bug` |
| `BD300` | Liver Details - Billing Log | 月額課金管理 | Agency | Spec done / Done / WIP / Backlog (sắp gửi) | Local: `Bug` |
| `BD400` | Liver Details - Payment Information | 決済情報 | Agency | WIP / Backlog / Backlog / Backlog (chưa gửi) | - |
| `BD500` | Liver Detail - Revenue Analysis | 売上 | Agency | WIP / Backlog / Backlog / Backlog (chưa gửi) | - |


### 4. Quản lý Bài đăng của Streamer (Streamer Posts) (2 màn hình)

#### 4.1 Quản lý Bài đăng của Streamer (Streamer Posts) (2 màn hình)

- **Tính năng chính & Spec:** Danh sách bài đăng (`BE100`) và chi tiết bài đăng (`BE200`) của các Liver thuộc Agency.
- **Trọng tâm Test / Verify Bug:** Kiểm tra lọc theo Liver, xem nội dung/media bài đăng, đảm bảo không xem được bài của Liver thuộc Agency khác.
- **Liên kết chéo:** Liên kết với Admin (`AM100-AM200`) và App (`L402`, `L405`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `BE100` | Post list | 投稿一覧 | Agency | Spec done / Done / Done / Done (chưa gửi) | - |
| `BE200` | Post details | 投稿詳細 | Agency | Spec done / Done / Done / Done (chưa gửi) | - |


### 5. Giám sát Livestream của Streamer (Streamer Livestream Management) (5 màn hình)

#### 5.1 Giám sát Livestream, Archive, Ban & Force Stop của Agency (5 màn hình)

- **Tính năng chính & Spec:** Danh sách phòng live của Liver (`BF100`), xem chi tiết phòng live (`BF200`), xem lại Archive (`BF300`), danh sách Ban (`BF400`) và danh sách Force Stop (`BF500`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra quyền Force Stop/Ban của Agency đối với Liver trực thuộc và đồng bộ trạng thái với Admin (`AG100-AG500`).
- **Liên kết chéo:** Liên kết với Admin (`AG100-AG500`) và App (`M200`, `I100`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `BF200` | Livestream Detail | - | Agency | Spec done / WIP / WIP / Backlog (sắp gửi) | - |
| `BF300` | Archive Livestream - List + View | - | Agency | Spec done / WIP / WIP / Backlog (sắp gửi) | - |
| `BF400` | List Ban | - | Agency | Spec done / WIP / WIP / Backlog (sắp gửi) | - |
| `BF100` | List Stream | - | Agency | Spec done / WIP / WIP / Backlog (sắp gửi) | - |
| `BF500` | List Force Stop | - | Agency | Spec done / WIP / WIP / Backlog (sắp gửi) | - |


### 6. Quản lý Báo cáo vi phạm liên quan (Report Management) (2 màn hình)

#### 6.1 Quản lý Báo cáo Vi phạm liên quan đến Liver của Agency (2 màn hình)

- **Tính năng chính & Spec:** Danh sách báo cáo (`BG100`) và chi tiết báo cáo (`BG200`) liên quan đến các Liver trực thuộc Agency.
- **Trọng tâm Test / Verify Bug:** Kiểm tra phân tách dữ liệu theo Agency, cập nhật trạng thái xử lý và đối chiếu với Admin (`AI100`, `AI200`).
- **Liên kết chéo:** Liên kết với Admin (`AI100`, `AI200`) và App (`D2021-D2023`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `BG100` | Report List | - | Agency | Spec done / WIP / WIP / Backlog (sắp gửi) | - |
| `BG200` | Report Detail | - | Agency | Spec done / WIP / WIP / Backlog (sắp gửi) | - |


### 7. Giám sát Tin nhắn & Bình luận Chat (Message & Chat Monitoring) (3 màn hình)

#### 7.1 Giám sát Tin nhắn & Bình luận Chat của Liver (3 màn hình)

- **Tính năng chính & Spec:** Xem tin nhắn của Liver (`BX100`), bình luận livestream (`BY100`) và danh sách cấm chat livestream (`BY300`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra dữ liệu lọc đúng Liver thuộc Agency, thao tác Ban/Unban chat tại `BY300` đồng bộ với `AY300` và phòng live.
- **Liên kết chéo:** Liên kết với Admin (`AX100-AX300`, `AY100-AY300`) và App (`F100`, `I100`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `BX100` | User Message | - | Agency | Spec done / WIP / WIP / Backlog (sắp gửi) | - |
| `BY100` | Livestream Comment | - | Agency | Spec done / WIP / WIP / Backlog (sắp gửi) | - |
| `BY300` | List Ban (livestream chat) | - | Agency | Spec done / WIP / WIP / Backlog (sắp gửi) | - |



---
## IV. NHÓM: APP (347 MÀN HÌNH)

### 1. Đăng nhập & Khởi tạo tài khoản (Login & Authentication) (14 màn hình)

#### 1.1 Khởi động, Đăng nhập (SNS / SĐT OTP) & Điều khoản (10 màn hình)

- **Tính năng chính & Spec:** Màn hình Splash (`A000`), chọn phương thức đăng nhập (`A100`), popup đồng ý điều khoản (`A101`), nhập SĐT (`A1031`), nhập mã OTP (`A1032`) cho cả App & Web.
- **Trọng tâm Test / Verify Bug:** Kiểm tra gửi/hết hạn/nhập sai OTP, bắt buộc đồng ý điều khoản ở `A101` trước khi vào app, đồng bộ luồng App và Web.
- **Liên kết chéo:** Liên kết với `K202` (Account Settings), `K2025` (Phone Linkage).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `A000` | Slash | スプラッシュスクリーン | APP | Spec done / NA / Done / Done (IS CLOSE) | - |
| `A100` | Login | ログイン | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `A101` | Login - A popup requiring agreement to the Terms of Use | ログイン確認子画面 | APP | Spec done / NA / Done / Done (IS CLOSE) | - |
| `A1031` | Login - Enter phone number | 電話ログイン入力子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `A1032` | Login - Enter OTP | 電話ログイン認証コード子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `A000` | Slash | スプラッシュスクリーン | WEB | Spec done / NA / Done / Done (IS CLOSE) | - |
| `A100` | Login | ログイン | WEB | Spec done / NA / Done / Done (IS CLOSE) | - |
| `A101` | Login - A popup requiring agreement to the Terms of Use | ログイン確認子画面 | WEB | Spec done / NA / Done / Done (IS CLOSE) | - |
| `A1031` | Login - Enter phone number | 電話ログイン入力子画面 | WEB | Spec done / NA / Done / Done (IS CLOSE) | - |
| `A1032` | Login - Enter OTP | 電話ログイン認証コード子画面 | WEB | Spec done / NA / Done / Done (đã gửi) | - |


#### 1.2 Khởi tạo Hồ sơ, Quà tân thủ & Single-Device Session (4 màn hình)

- **Tính năng chính & Spec:** Thiết lập hồ sơ ban đầu (`A105`), nhận thưởng đăng nhập tân thủ (`A300`), và logic CR 1 UID chỉ được đăng nhập trên 1 thiết bị tại một thời điểm (`-`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra khi đăng nhập thiết bị B thì thiết bị A bị force logout (đặc biệt khi đang xem/phát livestream); kiểm tra nhận Login Bonus 1 lần duy nhất.
- **Liên kết chéo:** Liên kết với `K800` (Edit Profile) và `M200`/`I100` (xử lý ngắt kết nối khi đá session).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `A105` | Login - Init Account Setting | 初期プロフィール入力子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `A105` | Login - Init Account Setting | 初期プロフィール入力子画面 | WEB | Spec done / NA / Done / Done (IS CLOSE) | - |
| `A300` | Login bonus | 初心者ログインボーナス | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `-` | CR - [Login] 1 UID chỉ được phép đăng nhập trên 1 device tại một thời điểm | - | APP | - | - |


### 2. Hướng dẫn, Điều khoản & Trợ giúp Webview (Help, Policies & Legal) (12 màn hình)

#### 2.1 Trung tâm Trợ giúp & Gửi yêu cầu Hỗ trợ (Help & Inquiry) (6 màn hình)

- **Tính năng chính & Spec:** Trang chủ Help (`A201`), tìm kiếm, danh mục, chi tiết bài viết (`A201`), gửi & hoàn tất yêu cầu hỗ trợ Inquiry (`A202`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra tìm kiếm từ khóa tiếng Nhật, mở Webview mượt trên iOS/Android, submit form Inquiry gửi mail/ticket thành công.
- **Liên kết chéo:** Mở từ màn hình Login (`A100`) hoặc My Page Settings (`K100`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `A201` | Help Top Sub-screen | ヘルプトップ子画面 | WEB | Spec done / NA / Done / Done (đã gửi) | - |
| `A201` | Help Search Results Sub-screen | ヘルプ検索結果子画面 | WEB | Spec done / NA / Done / Done (IS CLOSE) | - |
| `A201` | Help Category Sub-screen | ヘルプカテゴリ子画面 | WEB | Spec done / NA / Done / Done (IS CLOSE) | - |
| `A201` | Help Details Sub-screen | ヘルプ詳細子画面 | WEB | Spec done / NA / Done / Done (IS CLOSE) | - |
| `A202` | Inquiry Completion Sub-screen | お問い合わせ完了子画面 | WEB | Spec done / NA / Done / Done (IS CLOSE) | - |
| `A202` | Inquiry Details Sub-screen | お問い合わせ詳細子画面 | WEB | Spec done / NA / Done / Done (IS CLOSE) | - |


#### 2.2 Điều khoản Pháp lý, Chính sách & Tỷ lệ Gacha (Webview) (6 màn hình)

- **Tính năng chính & Spec:** Chính sách bảo mật (`A204`), Điều khoản sử dụng (`A205`), Quy định tiền tệ trong app (`A206`), Điều khoản Hộp kho báu (`A207`), Luật giao dịch thương mại (`A208`) và Chi tiết tỷ lệ Gacha (`A209`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra hiển thị đúng nội dung pháp lý mới nhất, link điều hướng không 404, bảng tỷ lệ `A209` khớp với cấu hình trên Admin (`AQ100-AQ500`).
- **Liên kết chéo:** Liên kết với `A101`, `G201` (Gacha Detail), `I1021` (Treasure Box).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `A204` | Privacy Policy Sub-screen | プライバシーポリシー子画面 | WEB | Spec done / NA / NA / Done (IS CLOSE) | - |
| `A206` | In-app Currency Terms Sub-screen | アプリ専用通貨規約子画面 | WEB | Spec done / NA / NA / Done (đã gửi) | - |
| `A205` | Terms of Service Sub-screen | 利用規約子画面 | WEB | Spec done / NA / NA / Done (đã gửi) | - |
| `A207` | Treasure Box Terms of Use Sub-screen | 宝箱利用規約子画面 | WEB | Spec done / NA / NA / Done (IS CLOSE) | - |
| `A208` | Specified Commercial Transaction Act / Payment Services Act Sub-screen | 特商法／資金決済法子画面 | WEB | Spec done / NA / NA / Done (IS CLOSE) | - |
| `A209` | Gacha Rate | 画面一覧_ユーザーのガチャ提供割詳細子画面 | WEB | Spec done / Done / Done / Done (IS CLOSE) | - |


### 3. Trang chủ, Gợi ý & Nhiệm vụ (Home, Recommend & Missions) (12 màn hình)

#### 3.1 Trang chủ, Gợi ý Nội dung & Quảng cáo (Recommend & Ads) (7 màn hình)

- **Tính năng chính & Spec:** Các màn hình gợi ý bài đăng (`B001`), phòng live standby (`B002`), phòng live đang phát (`B003`), danh sách khởi tạo (`B100`), gợi ý (`B101`), theo danh mục (`B102`) và màn hình quảng cáo (`B300`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra phân trang/infinite scroll, lọc theo category, chuyển trạng thái real-time khi phòng live bắt đầu/kết thúc, hiển thị popup/banner quảng cáo đúng tần suất.
- **Liên kết chéo:** Điều hướng trực tiếp vào phòng live (`I099`, `I100`) hoặc bài đăng Familia (`L203`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `B001` | Recommend - Post | レコメンド_投稿 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `B002` | Recommend - Livestream standby | レコメンド_配信スタンバイ | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `B003` | Recommend - Livestream | レコメンド_配信 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `B100` | List Initial | リスト_初期 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `B101` | List Recommend | リスト_おすすめ | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `B102` | List Recommended Category | リスト_カテゴリー | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `B300` | Advertisement | 広告子画面 | APP | Backlog / Backlog / Backlog / Backlog (Sau release) | - |


#### 3.2 Bảng xếp hạng & Nhiệm vụ (Ranking & Missions) (5 màn hình)

- **Tính năng chính & Spec:** Bảng xếp hạng Ranker (`B103`), Gifter (`B104`), Dolls (`B104`) và danh sách Nhiệm vụ GĐ1+2, GĐ3 (`B200`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra tính toán điểm xếp hạng theo kỳ (ngày/tuần/tháng), tiến độ hoàn thành nhiệm vụ và nhận thưởng tự động.
- **Liên kết chéo:** Liên kết với `K901` (Dolls Ranking), `K902` (Gifter Ranking).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `B200` | Mission List GĐ1 + GĐ2 | ミッション子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `B200` | Mission List GĐ3 | ミッション子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `B104` | List Ranking Gifter | リスト_ランキング_ギフター | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `B104` | List Ranking Dolls | リスト_ランキング_ドールズ | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `B103` | List Ranker | リスト_ランカー | APP | Spec done / Done / Done / Done (đã gửi) | - |


### 4. Tìm kiếm (Search) (1 màn hình)

#### 4.1 Tìm kiếm Tổng hợp (Search Top) (1 màn hình)

- **Tính năng chính & Spec:** Màn hình tìm kiếm người dùng, livestream, bài đăng hoặc từ khóa (`C100`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra tìm kiếm ký tự đặc biệt/tiếng Nhật, lịch sử tìm kiếm, phân loại kết quả theo tab và chặn hiển thị user đã Block (`K207`).
- **Liên kết chéo:** Liên kết với `D100` (Profile), `I100` (Livestream), `K207` (Block).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `C100` | Search | 検索トップ | APP | Spec done / Done / Done / Done (đã gửi) | - |


### 5. Trang cá nhân người khác & Video lưu trữ (Other User Profile & Archive) (16 màn hình)

#### 5.1 Hồ sơ Người khác, Ghi chú, Nhạc yêu thích & Báo cáo/Block (11 màn hình)

- **Tính năng chính & Spec:** Xem hồ sơ (`D100`), menu chức năng mở rộng (`D202`), luồng báo cáo đối tượng/lý do/chi tiết (`D2021-D2023`), ghi chú cá nhân về user (`D203`), lịch sử hát & bài hát/ca sĩ yêu thích (`D301`, `D3021`, `D3022`), cài đặt thông báo (`D500`) và danh sách Soldier (`D600`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra logic Block/Unblock, Report gửi lên Admin (`AI100`)/Agency (`BG100`), bật/tắt thông báo theo từng user đồng bộ với `K2044`.
- **Liên kết chéo:** Liên kết với Admin (`AI100`), Agency (`BG100`), My Page (`K2044`, `K207`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `D100` | View OO's profile | 他人のプロフィール | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `D202` | View OO's profile_Function | 他人のプロフィール_そのほかの機能子画面 | APP | Spec done / NA / Done / Done (IS CLOSE) | - |
| `D2021` | View OO's profile _  Report target sub-screen | 他人のプロフィール_通報対象子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | Chưa test phần report post và report message |
| `D2022` | View OO's profile _ Report reason sub-screen | 他人のプロフィール_通報理由子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `D2023` | View OO's profile _ Report detail sub-screen | 他人のプロフィール_通報詳細内容子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `D203` | View OO's profile _ Note sub-screen | 他人のプロフィール_ノート子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `D301` | View OO's profile _ Singing history sub-screen | 他人のプロフィール_歌唱履歴子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `D3021` | View OO's profile _ Favorite artists sub-screen | 他人のプロフィール_お気に入りのアーティスト子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `D3022` | View OO's profile _ Favorite songs sub-screen | 他人のプロフィール_お気に入りの曲子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `D500` | View OO's profile _ Notification settings sub-screen | 他人のプロフィール_通知設定子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `D600` | View OO's profile _ Soldier members sub-screen | 他人のプロフィール_ソルジャーメンバー子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |


#### 5.2 Video Lưu trữ (Archive) của Người khác (5 màn hình)

- **Tính năng chính & Spec:** Danh sách Archive (`D701`), chi tiết phát video (`D702`), chọn ngôn ngữ phụ đề (`D703`), tốc độ phát (`D704`) và bình luận Archive (`D705`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra quyền xem Archive (public vs follower/familia), đồng bộ phụ đề đa ngôn ngữ, đổi tốc độ phát mượt mà và gửi/xem bình luận.
- **Liên kết chéo:** Dữ liệu Archive được cấu hình quyền hiển thị từ chủ sở hữu tại `K9051-K9054`.

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `D701` | View OO's profile - Archive List | 他人のプロフィール_配信アーカイブ一覧 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `D702` | View OO's profile - Archive Detail | 他人のプロフィール_配信アーカイブ詳細 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `D703` | View OO's profile - Archive Detail - Select language | 他人のプロフィール_配信アーカイブ字幕設定子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `D704` | View OO's profile - Archive Detail - replay speed setting | 他人のプロフィール_配信アーカイブ再生速度設定子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `D705` | View OO's profile - Archive Detail - Comment | 他人のプロフィール_配信アーカイブコメント子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |


### 6. Thông báo & Hoạt động (Announcements & Notifications) (5 màn hình)

#### 6.1 Thông báo Hệ thống, Hoạt động & Push Notification (5 màn hình)

- **Tính năng chính & Spec:** Danh sách thông báo (`E201`), chi tiết thông báo (`E202`), bản Webview trong live (`I8042`), danh sách hoạt động (`E203`) và thanh Push Noti UI (`E203`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra trạng thái đã đọc/chưa đọc (badge count), deep link khi bấm vào thông báo đẩy, nội dung thông báo đồng bộ từ Admin (`AH100-AH301`).
- **Liên kết chéo:** Nhận dữ liệu từ Admin (`AH100-AH301`) và cấu hình tại `K204`.

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `I8042` | Announcement Detail WEB | 配信共通_お知らせ詳細子画面 | WEB | Spec done / NA / Done / Done (IS CLOSE) | - |
| `E201` | Announcement List | 通知_おしらせ | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `E202` | Announcement Detail | 通知_おしらせ詳細 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `E203` | Activity List (Pushnoti List) | 通知_アクティビティ | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `E203` | Push Noti UI | 通知_共通バー | APP | Spec done / NA / Done / Done (IS CLOSE) | - |


### 7. Tin nhắn 1-1 / Hòm thư (Direct Messages) (17 màn hình)

#### 7.1 Hòm thư, Chat 1-1 & Yêu cầu 2-Shot qua Tin nhắn (10 màn hình)

- **Tính năng chính & Spec:** Danh sách hội thoại (`F100`), tạo chat 1-1 (`F200`), chat 1-1 (`F101`), gửi lời mời 2-shot (`F1011`), cài đặt chat & block (`F1012`, `F10121`), tin nhắn hệ thống (`F103`), tin nhắn của tôi (`F104`), xem trước chưa đọc (`F400`) và gửi Stamp (`F500`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra quyền nhắn tin (`K400` Message Access & tham gia Familia), logic chặn nhận tin từ user bị Block, nhận/từ chối lời mời 2-shot và hiển thị Stamp.
- **Liên kết chéo:** Liên kết với `K400`, `K207`, Admin (`AX100-AX300`), Agency (`BX100`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `F100` | Message Top | メッセージトップ | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `F101` | Message Details - 1-1 | メッセージ詳細_個人 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `F1011` | Message Details - 1-1 - 2shot invite | メッセージ詳細_2ショット申請 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `F1012` | Message Details - Individual - Settings | メッセージ詳細_個人_設定 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `F10121` | Message Details - Individual - Settings - Block | -メッセージ詳細_個人_設定-Block | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `F103` | Message Details - System | メッセージ詳細_システム | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `F104` | Message Details - My message | メッセージ詳細_自分 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `F400` | Message Details - Unread message preview | メッセージ詳細_未読プレビュー子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `F500` | Message Details - Stamp | メッセージ詳細_スタンプ子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `F200` | Create Message - 1-1 | メッセージ作成_個人 | APP | Spec done / Done / Done / Done (IS CLOSE) | Chưa thông luồng do chưa làm phần join familia |


#### 7.2 Nhóm Chat (Group Message & Quản lý thành viên) (7 màn hình)

- **Tính năng chính & Spec:** Tạo nhóm chat (`F300`), màn hình chat nhóm (`F102`), cài đặt nhóm của chủ phòng (`F1021`), thêm thành viên (`F1022`), xem thành viên (`F1023`), rời nhóm (`F1024`, `F1025`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra quyền Owner vs Member (thêm/xóa thành viên, giải tán nhóm khi Owner rời), cập nhật tin nhắn realtime cho tất cả thành viên.
- **Liên kết chéo:** Liên kết với Admin (`AX100-AX300`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `F102` | Message Details - Group | メッセージ詳細_グループ | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `F1021` | Message Details - Group - Settings - Owner | メッセージ詳細_グループ_設定_所有者 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `F1022` | Message Details - Group - Add Member (Subscreen) | メッセージ詳細_グループ_設定メンバー追加子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `F1023` | Message Details - Group - Settings - Members | メッセージ詳細_グループ_設定_メンバー | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `F1024` | Message Details - Group - Leave Group | メッセージ詳細_グループ_退出 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `F1025` | Message Details - Group - Settings - Leave Group | メッセージ詳細_グループ_設定_退出 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `F300` | Create Message - Group | メッセージ作成_グループ | APP | Spec done / Done / Done / Done (IS CLOSE) | - |


### 8. Cửa hàng, Nạp Coin, Gacha & Gói tháng (Shop, Currency, Gacha & Subscription) (21 màn hình)

#### 8.1 Cửa hàng Tổng hợp, Vé (Ticket) & Lịch sử Point/Coin (7 màn hình)

- **Tính năng chính & Spec:** Trang chủ Shop (`G100`), đổi vé (`G401`), lịch sử vé (`G402`), lịch sử Point/Coin trên App & Web (`G600`), nạp Point trên App (`G701`) và Web (`G702`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra thanh toán IAP (Apple/Google) và Web Payment, cộng số dư ngay sau khi thanh toán, trừ tiền đúng thứ tự Coin trả phí / miễn phí, ghi nhận log `G600`.
- **Liên kết chéo:** Đối chiếu với Admin Billing (`AE500`, `AE600`) và Revenue (`AS100`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `G100` | Shop Top | ショップトップ | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `G401` | Ticket Exchange Sub-screen | チケット交換子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `G402` | Ticket History Sub-screen | チケット履歴子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `G600` | Point / Coin History Sub-screen | ポイント・コイン履歴子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `G600` | Point / Coin History Sub-screen | ポイント・コイン履歴子画面 | WEB | Spec done / Done / Done / Done (đã gửi) | - |
| `G701` | Point Purchase Sub-screen (App) | ポイント購入子画面 - APP | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `G702` | Point Purchase Sub-screen (Web) | ポイント購入子画面 WEB | WEB | Spec done / Done / Done / Done (đã gửi) | - |


#### 8.2 Gói Hội viên Hàng tháng (Monthly Plans) (6 màn hình)

- **Tính năng chính & Spec:** Danh sách gói tháng (`G501`), Monthly Pass và chi tiết các hạng Silver, Gold, Royal, Platinum (`G5021`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra quyền lợi từng hạng, tự động gia hạn (auto-renew), nâng/hạ hạng và hủy gói; đồng bộ trạng thái gói lên Admin (`AE500`) và Agency (`BD300`).
- **Liên kết chéo:** Liên kết với Admin (`AE500`) và Agency (`BD300`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `G501` | Monthly Plan List | マンスリープラン一覧 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `G5021` | Monthly Pass | マンスリーパス | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `G5021` | Silver Plan Details | シルバープラン詳細 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `G5021` | Gold Plan Details | ゴールドプラン詳細 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `G5021` | Royal Plan Details | ロイヤルプラン詳細 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `G5021` | Platinum Plan Details | プラチナプラン詳細 | APP | Spec done / Done / Done / Done (đã gửi) | - |


#### 8.3 Gacha tại Shop & Trong Livestream, Đổi Mảnh (Fragment) (8 màn hình)

- **Tính năng chính & Spec:** Danh sách & chi tiết Gacha tại Shop (`G200`, `G201`), đổi mảnh Fragment (`G301`, `G302`), và Gacha trong lúc đang livestream (`G200-G203` Streamer View).
- **Trọng tâm Test / Verify Bug:** Kiểm tra trừ Coin/Ticket khi quay x1/x10, cộng vật phẩm/mảnh vào kho đồ, xử lý hiệu ứng chờ kết quả (`G203`) và hiển thị kết quả (`G202`).
- **Liên kết chéo:** Cấu hình pool & tỷ lệ từ Admin (`AQ100-AQ500`, `A209`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `G200` | Gacha List (SHOP) | ガチャ一覧 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `G201` | Gacha Detail (SHOP) | ガチャ詳細 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `G301` | Fragment Exchange | フラグメント交換 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `G302` | Fragment History Sub-screen | フラグメント履歴子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `G200` | (Streamer View) Now Streaming - Setting in livestream - Gacha List | 配信中_ガチャ一覧_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `G201` | (Streamer View) Now Streaming - Setting in livestream - Gacha details | 配信中_ガチャ詳細_子画面 | APP | Spec done / Done / Done / Done (đã gửi) | OK |
| `G202` | (Streamer View) Now Streaming - Setting in livestream - Gacha Result | 配信共通_ガチャ結果子画面 | APP | Spec done / Done / Done / Done (đã gửi) | OK |
| `G203` | (Streamer View) Now Streaming - Setting in livestream - Gacha details | 配信共通_ガチャ結果待ち子画面 | APP | Spec done / Done / Done / Done (đã gửi) | OK |


### 9. Livestream - Khán giả (Viewer Livestream Experience) (53 màn hình)

#### 9.1 Vào phòng Live, Chế độ phòng & Khóa Familia/Soldier (6 màn hình)

- **Tính năng chính & Spec:** Phòng chờ Standby (`I099`), phòng Live thường (`I100`), khóa Familia (`I202`), màn hình Familia (`I203`), và điều kiện cấp độ Soldier (`I104` Level 1/2).
- **Trọng tâm Test / Verify Bug:** Kiểm tra điều kiện vào phòng (phòng khóa Familia chỉ thành viên mới vào được, đạt Soldier Level mới xem/tương tác), chuyển trạng thái Standby -> Live -> End mượt mà.
- **Liên kết chéo:** Tương ứng với luồng phát của Streamer (`M100_final`, `M200`, `M500`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `I202` | (Viewer) LiveStream - Familia Lock | 配信閲覧_ファミリアロック | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I203` | (Viewer) LiveStream - Familia | 配信閲覧_ファミリア | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `I104` | (Viewer) LiveStream - Soldier Level 1 | 他人のプロフィール_ソルジャーメンバー子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `I104` | (Viewer) LiveStream - Soldier Level 2 | 配信閲覧_ソルジャーレベル条件2_子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `I099` | (Viewer) LiveStream - Stanby | 配信閲覧_スタンバイ | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `I100` | (Viewer) LiveStream - Normal | 配信閲覧_一般 | APP | Spec done / Done / Done / Done (đã gửi) | - |


#### 9.2 Chế độ 2-Shot (Đăng ký, Phòng riêng, Khóa, Gia hạn & Kết nối lại) (10 màn hình)

- **Tính năng chính & Spec:** Xác nhận/đăng ký 2-shot (`I301`), phòng 2-shot (`I303`), 2-shot Lock (`I302`), chuyển sang 2-shot Lock (`I305`), gia hạn 2-shot (`I304`), kết nối lại khi rớt mạng (`I3031`), xác nhận kết thúc (`I303`) và chế độ Broadcast (`I306`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra trừ Coin/Ticket khi được Streamer duyệt, đếm ngược thời gian 2-shot, gia hạn thêm giờ không bị ngắt âm thanh/hình ảnh, reconnect lại đúng phiên `I3031`.
- **Liên kết chéo:** Phối hợp 2 chiều với Streamer (`M300`, `M3001`, `M3002`, `M302`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `I301` | Request Live2Shot modal comfirm | 2ショット申込確認_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I301` | Request Live2Shot modal | 2ショット申込_子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `I303` | (Viewer) LiveStream - 2 shot | 配信閲覧_2ショット | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `I302` | (Viewer) LiveStream - 2 shot Lock | 配信閲覧_2ショットロック | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I304` | (Viewer) LiveStream - Extend Live 2 Shot | 2ショット延長申込確認_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I304` | (Viewer) LiveStream - Extend Live 2 Shot | 2ショット延長申込_子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `I3031` | (Viewer) LiveStream - 2 shot - Xử lý kết nối lại livestream 2shot | ログイン後_2ショット確認子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I303` | (Viewer) LiveStream - End 2shot, Confirm | 2ショット再確認 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `I306` | (Viewer) LiveStream - Board Cast | 配信閲覧_ブロードキャスト | APP | Spec done / NA / Done / Done (IS CLOSE) | - |
| `I305` | (Viewer) LiveStream - Change to 2 shot Lock | 配信閲覧_2ショット切替確認_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |


#### 9.3 Tương tác Khán giả (Chat, Whisper, Profile, Danh sách Listener) (6 màn hình)

- **Tính năng chính & Spec:** Danh sách khán giả (`I103`), tùy chọn bình luận (`I1013`), tùy chọn màn hình (`I1014`), chat thầm Whisper (`I402`), modal xem profile Viewer (`I1011`) và profile Streamer (`I1012`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra gửi chat thường & Whisper chat realtime, ẩn UI khi chọn Screen Option, xử lý user bị Ban chat từ Admin/Agency/Streamer.
- **Liên kết chéo:** Liên kết với Admin (`AY100-AY300`), Agency (`BY100`, `BY300`) và Streamer (`M201`, `M203`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `I402` | (Viewer) LiveStream - Normal - Whisper chat | 配信閲覧_ナイショ話_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I1013` | (Viewer) LiveStream - Comment Option | 配信共通_コメントオプション子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I1011` | (Viewer) LiveStream - Bottom Modal - User Profile | 他人のプロフィール_視聴者_LIVE子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | Rank, title, block chưa làm |
| `I1012` | (Viewer) LiveStream - Bottom Modal - Streamer Profile | 他人のプロフィール_ライバー_LIVE子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | Rank, title, block chưa làm |
| `I103` | (Viewer) LiveStream - Listener List | 配信閲覧_リスナー一覧_子画面 | APP | Spec done / NA / Done / Done (IS CLOSE) | - |
| `I1014` | (Viewer) LiveStream - Screen Option | 配信共通_画面オプション子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |


#### 9.4 Quà tặng, Gift Gacha & Hiệu ứng Quà cao cấp (4 màn hình)

- **Tính năng chính & Spec:** Danh sách quà tặng (`I600`), chế độ hiệu ứng quà cao cấp (`I601`), Gift Gacha (`I700`) và xác nhận Gift Gacha (`I701`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra gửi quà trừ đúng số dư, hiển thị animation/combo quà trên màn hình cả Viewer và Streamer, không lag/crash khi nhận nhiều quà cùng lúc.
- **Liên kết chéo:** Cấu hình quà từ Admin (`AF100-AF500`) và thống kê tại `K9091A`, `K909`.

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `I601` | (Viewer) LiveStream - Normal - High-Value Gift Animation Mode | 配信共通_高額ギフト演出モード | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `I600` | (Viewer) LiveStream - Normal - Gift List | 配信閲覧_ギフト_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I700` | (Viewer) LiveStream - Normal - Gift Gacha | 配信閲覧_ギフトガチャ_子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `I701` | (Viewer) LiveStream - Normal - Gift Gacha Confirm | 配信閲覧_ギフトガチャ確認_子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |


#### 9.5 Hộp Kho báu (Treasure Box) (7 màn hình)

- **Tính năng chính & Spec:** Chi tiết hộp kho báu (`I1021`), lịch sử gửi (`I1022`), tùy chỉnh hộp (`I1023`), danh sách hộp đang mở (`I1024`), hoạt ảnh mở hộp (`I1024`), kết quả (`I1025`) và danh sách người trúng (`I1026`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra điều kiện mở hộp (đếm ngược/comment), giới hạn số người trúng, cộng thưởng Coin/Point chính xác cho người trúng và đồng bộ lịch sử (`K9093`).
- **Liên kết chéo:** Liên kết với Điều khoản `A207` và My Page `K9093`.

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `I1021` | (Viewer) LiveStream - Treasure Box Details | 配信閲覧_宝箱詳細_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I1022` | (Viewer) LiveStream - Treasure Box Send History | 配信閲覧_宝箱送信履歴_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I1023` | (Viewer) LiveStream - Treasure Box Customization | 配信閲覧_宝箱カスタマイズ_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I1024` | (Viewer) LiveStream - List of Treasure Boxes to Open | 配信閲覧_開く宝箱一覧_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I1024` | (Viewer) LiveStream - Treasure Box Opening | 配信閲覧_宝箱開封_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I1025` | (Viewer) LiveStream - Treasure Box Opening Results | 配信閲覧_宝箱開封結果_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I1026` | (Viewer) LiveStream - List of Users Winning from Treasure Boxes | 配信閲覧_宝箱あたりユーザ一覧_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |


#### 9.6 Karaoke Khán giả (Tìm kiếm, Yêu cầu bài hát & Chấm điểm) (13 màn hình)

- **Tính năng chính & Spec:** Chế độ Karaoke (`I501`), cài đặt Karaoke (`I502`), tìm bài theo từ khóa/phổ biến/thập niên/chi tiết (`I5031-I5034`), tìm ca sĩ & bài của ca sĩ (`I5041-I5042`), danh sách yêu thích (`I5051-I5052`), lịch sử hát (`I507`), chấm điểm (`I508`) và gửi yêu cầu bài hát cho Streamer (`I509`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra đồng bộ lời bài hát (lyric timing) giữa Streamer và Viewer, gửi Song Request (`I509`) sang hàng đợi của Streamer (`M403`).
- **Liên kết chéo:** Liên kết với Admin Karaoke (`AL100-AL400`) và Streamer Karaoke (`M401-M409`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `I501` | (Viewer) LiveStream - Karaoke | 配信閲覧_カラオケ | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `I5031` | Viewer - Search song - Keyword | - | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `I5042` | Viewer - Search song - artirst - song list | 配信共通_アーティスト曲一覧 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `I5052` | Viewer - Favourite Song List | 配信閲覧_お気に入り曲一覧 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `I508` | Viewer - Karaoke Scoring | 配信共通_採点_子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `I502` | (Viewer) LiveStream - Karaoke - Setting | 配信閲覧_カラオケ設定_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I5032` | Viewer - Search song - popular | 配信共通_曲検索_人気 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I5033` | Viewer - Search song - Era | 配信共通_曲検索_年代 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I5034` | Viewer - Search song - Song Detail | 配信共通_曲詳細_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I5041` | Viewer - Search Artirst | 配信共通_アーティスト検索 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I5051` | Viewer - Favourite Artist List | 配信閲覧_お気に入りアーティスト一覧 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I507` | Viewer - Sing history | 配信共通_歌唱履歴 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I509` | Viewer - Song request | 配信共通_歌リク_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |


#### 9.7 Cài đặt trong Phòng Live & Picture-in-Picture (PiP) (7 màn hình)

- **Tính năng chính & Spec:** Menu cài đặt tổng hợp (`I800`), âm lượng mic (`I802`), âm lượng đối phương (`I803`), thông báo (`I804`, `I8041`), đồ họa (`I805`), và chế độ PiP ngoài/trong app (`CMR 63 - I1001`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra giữ âm thanh/hình ảnh mượt khi thu nhỏ PiP trong và ngoài app, chỉnh âm lượng/đồ họa có tác dụng tức thì không làm văng phòng.
- **Liên kết chéo:** Liên kết với Streamer Settings (`M205*`) và `CMR63`.

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `CMR 63 - I1001` | CMR63 PIP  out app | 配信閲覧_ピクチャインピクチャアプリ外_子画面 | APP | Spec done / NA / Done / Done (IS CLOSE) | - |
| `I803` | (Viewer) LiveStream - Livestream Setting - Incoming Volume | 配信共通_相手の音量子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I800` | (Viewer) LiveStream - Livestream Settingf | 配信閲覧_まとめ設定_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I802` | (Viewer) LiveStream - Livestream Setting - Microphone Volume | 配信共通_マイク音量子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I804` | (Viewer) LiveStream - Livestream Setting - Announcement | 配信共通_お知らせ子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I8041` | (Viewer) LiveStream - Livestream Setting - Announcement Detail - Webview | 配信共通_お知らせ詳細子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `I805` | (Viewer) LiveStream - Livestream Setting - Graphics | 配信共通_グラフィック子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |


### 10. Livestream - Streamer & OBS (Streamer Broadcasting & Tools) (69 màn hình)

#### 10.1 Thiết lập Model 3D, Trang phục & Hình nền Ban đầu (Initial Setup) (8 màn hình)

- **Tính năng chính & Spec:** Chọn model (`M0011`), chỉnh đầu (`M00111`), ngoại hình (`M00112`, `M00113`), biểu cảm (`M00114`), trang phục (`M0012`, `M00121`) và hình nền lần đầu (`M00131`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra lưu preset model/trang phục không bị mất khi thoát app, render avatar 3D đúng tỷ lệ, không xung đột phụ kiện.
- **Liên kết chéo:** Dùng dữ liệu Model từ Admin (`AP000-AP400`) và Background (`AK201-AK203`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `M0011` | Streaming Setup – Initial – Model Select | 配信準備_初期_モデル設定 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M00111` | Streaming Setup – Initial – Model Settings – Head | 配信準備_初期_モデル設定_頭 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M00112` | Streaming Setup – Initial – Model Settings – Appearance | 配信準備_初期_モデル設定_外観 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M00113` | Streaming Setup – Initial – Model Settings – Appearance Settings Sub-screen | 配信準備_初期_モデル設定_外観設定子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M00114` | Streaming Setup – Initial – Model Settings – Emotion Expression Sub-screen | 配信準備_初期_モデル設定_感情表現子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M0012` | Streaming Setup – Initial – Costume Settings | 配信準備_初期_コーデ設定 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `M00121` | Streaming Setup – Initial – Costume Settings – Custom Sub-screen | 配信準備_初期_コーデ設定_カスタム子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `M00131` | Background Setting - Lần đầu tiên - Background | 配信準備_初期_背景設定 | APP | Spec done / Done / Done / Done (đã gửi) | - |


#### 10.2 Chuẩn bị trước khi Phát sóng (Prepare to Stream) (6 màn hình)

- **Tính năng chính & Spec:** Màn hình Prepare TOP (`M100_final`), chọn độ phân giải (`M100`), chọn chủ đề Topic (`M1012`), chọn/thêm quà Wishlist (`M1011`), kiểm tra mời 2-shot (`M102`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra cấu hình độ phân giải tương thích thiết bị, lưu Topic & Wishlist hiển thị đúng ngay khi bấm Go Live.
- **Liên kết chéo:** Độ phân giải cấu hình tại Admin (`AP000`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `M100_final` | Prepare to stream TOP | 配信準備_トップ | APP | Spec done / NA / Done / Done (đã gửi) | - |
| `M1012` | Prepare to stream TOP - Livestream Tocpic | 配信準備_トピック_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M1011` | Prepare to stream TOP - Wishlist - Select gift | 配信準備_ほしいリスト選択_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M1011` | Prepare to stream TOP - Wishlist - Add wish gift | 配信準備_ほしいリスト_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M102` | Prepare to stream TOP - Live2shot invite Check | 配信準備_2ショット招待_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M100` | App Model - Chọn độ phân giải | - | APP | Spec done / Done / Done / Done (đã gửi) | - |


#### 10.3 Điều hành Phòng Live & Các Chế độ Phát (Normal/Test/Familia/Broadcast/PiP) (11 màn hình)

- **Tính năng chính & Spec:** Phát thường (`M200`), phát thử nghiệm (`M199`), chế độ Familia (`M500`), xác nhận & chuyển sang Broadcast (`M2071`, `M2073`), tùy chọn màn hình (`M2001`), đổi tiêu đề (`CMR64`), danh sách khán giả (`M203`), PiP cho streamer (`PIP streamer`, `CMR 63 - I1001`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra chuyển đổi qua lại giữa Normal <-> Familia <-> Broadcast không rớt stream; chế độ Test (`M199`) không gửi thông báo push tới follower.
- **Liên kết chéo:** Tương tác 2 chiều với Viewer (`I100`, `I202`, `I203`, `I306`) và Admin (`AG100-AG400`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `M200` | (Streamer View) Now Streaming - Normal | 配信中_配信室 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `M199` | (Streamer View) Now Streaming - TEST | 配信中_テスト配信 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `M203` | (Streamer View) Now Streaming - Listener List | 配信中_リスナー一覧_子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `M2071` | (Streamer View) Now Streaming - Setting in livestream - xác nhận chuyển sang boardcast | 配信中_ブロードキャスト確認子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M2073` | (Streamer View) Now Streaming - Setting in livestream - chuyển sang boardcast | 配信中_ブロードキャスト_バックグラウンド設定バー | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `M500` | (Streamer View) Now Streaming - Familia mode | - | APP | Spec done / Done / Done / Done (-) | - |
| `PIP streamer` | PIP cho streamer | - | APP | Spec done / NA / Done / Done (đã gửi) | - |
| `CMR 63 - I1001` | CMR63 PIIP in app | 配信閲覧_ピクチャインピクチャアプリ内_子画面 | APP | Spec done / NA / Done / Done (IS CLOSE) | - |
| `CMR64` | (Streamer View) Now Streaming - Change Title | 配信中_配信タイトルの設定_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M203` | (Streamer View) Now Streaming - Lich sử whisper | 配信中_ウィスパー履歴子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M2001` | (Streamer View) Now Streaming - Screen Option | -配信共通_画面オプション子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |


#### 10.4 Quản lý 2-Shot phía Streamer (Approve, Reconnect, Extend) (4 màn hình)

- **Tính năng chính & Spec:** Danh sách yêu cầu 2-shot (`M302`), phòng 2-shot (`M300`), xử lý 2-shot dang dở/quay lại (`M3001`) và xử lý gia hạn 2-shot (`M3002`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra duyệt/từ chối yêu cầu trong `M302`, tự động chuyển phòng sang 2-shot, xử lý khi 1 trong 2 bên rớt mạng và đồng ý gia hạn.
- **Liên kết chéo:** Phối hợp 2 chiều với Viewer (`I301-I305`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `M3001` | (Streamer View) Now Streaming - 2shot dở và quay lại | - | APP | Spec done / Done / Done / Done (-) | - |
| `M3002` | (Streamer View) Now Streaming - 2shotxử lý extend | - | APP | Spec done / Done / Done / Done (-) | - |
| `M302` | (Streamer View) Now Streaming - Danh sách request 2 shot | 配信中_2ショット承認リスト_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M300` | (Streamer View) Now Streaming - 2shot | -配信中_2ショット | APP | Spec done / Done / Done / Done (-) | - |


#### 10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live (21 màn hình)

- **Tính năng chính & Spec:** Menu cài đặt (`M205`), trả lời & lịch sử Whisper (`M201`, `M203`), đổi trang phục/ngoại hình/nền (`M20501`, `M20502`, `M20504`), bảng thông báo (`M20506`), cập nhật Wishlist (`M20507`), đổi Topic (`M2055`), chia sẻ (`M206`), Emote & Biểu cảm (`M2061`, `M2062`), thông báo (`M20515`), đồ họa (`M20516`), âm thanh/mic/echo/voice changer/BGM/voice monitor (`M20510-M20514`, `M20518`, CR Voice Monitor) và thống kê follow (`CMR60`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra đổi trang phục/nền/voice changer/BGM realtime hiển thị & phát đúng sang phía Viewer; kiểm tra Voice Monitor không bị vọng âm.
- **Liên kết chéo:** Dùng BGM từ `AJ100`, Background từ `AK201`, Gift từ `AF100`.

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `CMR60` | Thống kê số lượt follow | NA | APP | Spec done / Done / Done / Done (-) | - |
| `M2055` | (Streamer View) Now Streaming - Setting in livestream - Change Topic | -配信準備_トピック_子画面 | APP | Spec done / Done / Done / Done (-) | - |
| `M20507` | (Streamer View) Now Streaming - Setting in livestream - Update Wishlist | -配信準備_ほしいリスト_子画面 | APP | Spec done / Done / Done / Done (-) | - |
| `M20518` | (Streamer View) Now Streaming - Setting in livestream - Livestream sound | -配信中_音声設定_子画面 | APP | Spec done / Done / Done / Done (-) | - |
| `M205` | (Streamer View) Now Streaming - Setting in livestream | 配信中_設定まとめ一覧_子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `M201` | (Streamer View) Now Streaming - Comment Whisper - Reply | 配信中_ウィスパー返信送信_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M206` | (Streamer View) Now Streaming - Setting in livestream - Share Livestream | 配信中_配信シェア_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M20506` | (Streamer View) Now Streaming - Setting in livestream - Board | 配信中_配信ボード_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M20512` | (Streamer View) Now Streaming - Setting in livestream - Incoming Volume | -配信共通_相手の音量子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M20514` | (Streamer View) Now Streaming - Setting in livestream - BGM | 配信中_BGM子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M20516` | (Streamer View) Now Streaming - Setting in livestream - Graphics | -配信共通_グラフィック子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M20502` | (Streamer View) Now Streaming - Setting in livestreams - Costume | 配信中_コーデ設定 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `M20501` | (Streamer View) Now Streaming - Setting in livestream - Appearance | 配信中_モデル設定_外観 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `M20504` | (Streamer View) Now Streaming - Setting in livestream - Change Background | 配信中_背景設定 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `M20511` | (Streamer View) Now Streaming - Setting in livestream - Mic Echo | 配信中_マイクのエコー子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M20513` | (Streamer View) Now Streaming - Setting in livestream - Voice Changer | 配信中_ボイスチェンジャー子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `M2062` | Biểu cảm | 配信中_顔表情_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M20510` | (Streamer View) Now Streaming - Setting in livestream - Livestream Micro | -配信共通_マイク音量子画面 | APP | Spec done / Done / Done / Done (-) | - |
| `M20515` | (Streamer View) Now Streaming - Setting in livestream - Announcement | -配信中_お知らせ子画面 | APP | Spec done / Done / Done / Done (-) | - |
| `M205` | (Streamer View) Now Streaming - Setting in livestream - chuyển sang familia | - | APP | Spec done / Done / Done / Done (-) | - |
| `M2061` | Emote | 配信中_限定エモート_子画面 | APP | Spec done / WIP / WIP / Backlog (sắp gửi) | - |


#### 10.6 Karaoke Streamer & Đề xuất Bài hát mới (15 màn hình)

- **Tính năng chính & Spec:** Chế độ Karaoke (`M401`), cài đặt (`M402`), danh sách yêu cầu hát (`M403`), tìm bài & ca sĩ (`M4041-M4044`, `M4051-M4052`), yêu thích (`M4061-M4062`), đề xuất bài mới chưa có (`M4071`, `M4072`), lịch sử hát (`M408`) và chấm điểm (`M409`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra nhận bài từ Viewer (`I509`), phát beat & sync lyric, gửi đề xuất bài mới (`M4071`) lên Admin (`AL400`).
- **Liên kết chéo:** Liên kết với Admin (`AL100-AL400`) và Viewer (`I501-I509`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `M401` | (Streamer View) Now Streaming - Mode Karaoke | 配信中_配信室_カラオケ | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `M4043` | (Streamer View) Now Streaming - Search song - Era | -配信共通_曲検索_年代 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `M4052` | (Streamer View) Now Streaming - Search Artist - Artist song list | -配信共通_アーティスト曲一覧 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `M409` | (Streamer View) Now Streaming - Karaoke Scoring | -配信共通_採点_子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `M402` | (Streamer View) Now Streaming - Mode Karaoke - Karaoke Setting | 配信中_カラオケ設定_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M403` | (Streamer View) Now Streaming - Mode Karaoke - Song Request List | -配信共通_歌リク_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M4041` | (Streamer View) Now Streaming - Search song - keyword | -配信共通_曲検索_キーワード | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M4042` | (Streamer View) Now Streaming - Search song - Popular | -配信共通_曲検索_人気 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M4044` | (Streamer View) Now Streaming - Search song - Detail | -配信共通_曲詳細_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M4051` | (Streamer View) Now Streaming - Search Artist | -配信共通_アーティスト検索 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M4061` | (Streamer View) Now Streaming - Favourite Airtist List | -配信共通_お気に入りアーティスト一覧 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M4062` | (Streamer View) Now Streaming - Favourite Song List | -配信共通_お気に入り曲一覧 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M4071` | (Streamer View) Now Streaming - wish new song | 配信共通_未登録曲の追加申請 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M4072` | (Streamer View) Now Streaming - wish new song list | 配信共通_未登録曲の追加申請新規 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `M408` | (Streamer View) Now Streaming - Sing History | -配信共通_歌唱履歴 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |


#### 10.7 Phát sóng qua OBS (OBS Normal / Familia / 2-Shot / Viewer) (4 màn hình)

- **Tính năng chính & Spec:** Hỗ trợ phát và xem livestream qua OBS ở các chế độ Normal, Familia, 2-shot và Viewer All Mode (`OBS`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra stream key/RTMP kết nối ổn định, đồng bộ avatar/audio từ OBS sang App Viewer ở mọi chế độ.
- **Liên kết chéo:** Tương thích với các phòng Viewer (`I100`, `I202`, `I303`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `-` | CR - Voice Monitor | - | APP | - | [Link](https://docs.google.com/spreadsheets/d/1pxox5GcjOXwKadMnzOa765ptG2huPJSxCiWsrH0_h7Y/edit?gid=40498693#gid=40498693) |
| `OBS` | OBS thường, OBS Familia | - | App | Spec done / Done / Done / Done (đã gửi) | - |
| `OBS` | OBS 2shot | - | App | Spec done / Done / Done / Done (đã gửi) | - |
| `OBS` | OBS Viewer All mode | - | App | Spec done / NA / Done / Done (đã gửi) | - |


### 11. Trang cá nhân của tôi & Cài đặt hệ thống (My Page, Account & Settings) (82 màn hình)

#### 11.1 Hồ sơ Cá nhân (My Page Core, Edit, Rank & Danh hiệu) (8 màn hình)

- **Tính năng chính & Spec:** Trang cá nhân (`K000`), xem ảnh toàn màn hình (`K001`), chỉnh sửa hồ sơ & ngày sinh (`K800`), cắt ảnh đại diện & ảnh bìa (`K801`, `K802`), xem Rank (`K908`) và danh sách Danh hiệu (`K500`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra upload/crop ảnh, validate độ dài bio/nickname, tính điểm lên hạng Rank (`K908`) và gắn danh hiệu (`K500`).
- **Liên kết chéo:** Hiển thị công khai sang `D100` (Other User Profile).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `K001` | Màn hình Xem ảnh | 自分のプロフィール_画像全表示子画面 | APP | Spec done / NA / Done / Done (IS CLOSE) | - |
| `K000` | My Page | 自分のプロフィール_参照 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K800` | Edit Profile | 自分のプロフィール_編集 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K802` | Upload Cover picture | 自分のプロフィール_カバーイメージ切り抜き | APP | Spec done / NA / Done / Done (IS CLOSE) | - |
| `K500` | My Page - List of Titles | 自分のプロフィール_称号一覧子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K908` | My Page - Rank | 自分のランク詳細情報子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K800` | Edit DOB | 自分のプロフィール_誕生日入力子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K801` | Upload Profile picture | 自分のプロフィール_プロフィール画像切り抜き | APP | Spec done / NA / Done / Done (IS CLOSE) | - |


#### 11.2 Cài đặt Tài khoản, SĐT, Liên kết SNS, eKYC & Block (14 màn hình)

- **Tính năng chính & Spec:** Menu cài đặt (`K100`), cài đặt tài khoản & Facebook (`K202`), liên kết/đổi SĐT & chọn mã quốc gia/OTP (`K2025`), gỡ liên kết SNS (`K20241`, `K20242`), đăng xuất (`K2021`), xóa tài khoản (`K2022`), xác thực danh tính eKYC (`K205`), danh sách bạn SNS/danh bạ (`K206`), danh sách chặn & logic Block (`K207`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra không cho gỡ SNS cuối cùng (`K20242`), điều kiện xóa tài khoản (không còn gói tháng/số dư/payout pending), logic Block ẩn toàn bộ tương tác 2 chiều.
- **Liên kết chéo:** Liên kết với Admin (`AE700`, `K2022`) và Login (`A100`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `K100` | My Page - Settings | 自分のプロフィール_まとめ設定一覧 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K2025` | Phone SETTING | 自分のプロフィール_電話番号連携 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K2025` | Phone - Country select | 自分のプロフィール_国検索子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K2025` | Phone - Code | 自分のプロフィール_コード認証 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K206` | Public SNS/Contact - Facebook | 自分のプロフィール_連絡先とSNSの友達の表示 | APP | Backlog / Backlog / Backlog / Backlog (Sau release) | - |
| `K20241` | SNS Un-connect | 自分のプロフィール_アカウント解除子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K20242` | SNS can not Un-connect | 自分のプロフィール_アカウント解除不可確認子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K2021` | Logout | 自分のプロフィール_ログアウト確認子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K2022` | Delete ACCOUNT | 自分のプロフィール_退会確認子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K202` | My Page - Settings - Account | 自分のプロフィール_アカウント設定 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K207` | Block list và logic Block | 自分のプロフィール_ブロック済みのアカウント一覧 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K206` | Public SNS/Contact | 自分のプロフィール_連絡先とSNSの友達の表示 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K205` | My Page - Settings - Ekyc | 自分のプロフィール_本人確認 | APP | Spec done / Done / Done / Done (sắp gửi) | - |
| `K202` | My Page - Settings - Account - Facebook | 自分のプロフィール_アカウント設定 | APP | Backlog / Backlog / Backlog / Backlog (Sau release) | - |


#### 11.3 Liên kết Agency (Tham gia / Rời khỏi Agency) (2 màn hình)

- **Tính năng chính & Spec:** Đăng ký tham gia Agency hoặc xác nhận rời khỏi Agency (`K203`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra nhập mã Agency hợp lệ, trạng thái chờ duyệt/đã duyệt/từ chối và ràng buộc khi đang còn doanh thu/yêu cầu rút tiền.
- **Liên kết chéo:** Liên kết trực tiếp với Agency (`BC100`, `BC200`) và Admin (`AD302`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `K203` | My Page - Settings - Account -  Agency - Register | 自分のプロフィール_事務所参加申請子画面 | APP | Spec done / Done / Done / WIP (sắp gửi) | - |
| `K203` | My Page - Settings - Account -  Agency - Exit | 自分のプロフィール_退所確認子画面 | APP | Spec done / Done / Done / WIP (sắp gửi) | - |


#### 11.4 Cài đặt Thông báo Đẩy (Push Notification Settings) (5 màn hình)

- **Tính năng chính & Spec:** Cài đặt thông báo chung (`K204`), cài đặt theo người đang follow (`K2041`), bật/tắt hàng loạt (`K2042`, `K2043`) và cài đặt riêng từng user (`K2044`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra toggle từng mục & bật/tắt hàng loạt đồng bộ tức thì với `D500` và backend push notification.
- **Liên kết chéo:** Liên kết với `D500` và `E203`.

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `K2041` | Push Noti - Follow user setting | 自分のプロフィール_フォローユーザー通知設定 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K2042` | Push Noti - Follow user setting all | 自分のプロフィール_フォローユーザー通知一括切替子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K2044` | Push Noti - Follow user setting - by user | 自分のプロフィール_フォローユーザー個別通知設定子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K204` | Push Noti | 自分のプロフィール_通知一覧 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K2043` | Push Noti - Follow user setting all - confirm | 自分のプロフィール_フォローユーザー通知一括切替_確認子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |


#### 11.5 Kết nối Xã hội, Familia, Soldier & Quyền Nhắn tin (8 màn hình)

- **Tính năng chính & Spec:** Danh sách Dolls yêu thích (`K3011`), Soldier Level (`K3012`), Familia đã tham gia (`K302`), thành viên Familia (`K701`), Follower/Following (`K702`), quyền nhắn tin (`K400`), nhà tài trợ (`K208` List of Sponsors) và giới thiệu app (`K208`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra đồng bộ số lượng follower/following, quyền nhắn tin `K400` áp dụng đúng vào `F101`/`F200`.
- **Liên kết chéo:** Liên kết với `D600`, `F200`, `L100-L500`.

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `K208` | List of Sponsors | - | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K3011` | My Page - Dolls | 自分のプロフィール_推しドールズ | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K3012` | My Page - Soilder Level | 自分のプロフィール_ソルジャーメンバー | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K302` | My Page - Joined Familia | 自分のプロフィール_加入ファミリア | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K702` | Follower/Following | 自分のプロフィール_フォロー子画面 | APP | Spec done / Done / Done / Done (-) | - |
| `K701` | Familia Member | 自分のプロフィール_ファミリアメンバー子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K400` | My Page - Message Access | 自分のプロフィール_メッセージクラス権限設定 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K208` | About Surreal Doll | 自分のプロフィール_サリアルドールズについて | APP | Spec done / Done / Done / Done (IS CLOSE) | - |


#### 11.6 Quản lý GOLD, Đổi Point & Lịch Thưởng (Reward Calendar) (4 màn hình)

- **Tính năng chính & Spec:** Số dư & thông tin GOLD (`K601`), đổi GOLD sang Point (`K6012`), lịch sử đổi (`K6013`) và Lịch nhận thưởng (`K602`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra tỷ giá đổi GOLD -> Point, trừ GOLD và cộng Point nguyên tử (atomic), xử lý logic đóng tài khoản khi còn GOLD.
- **Liên kết chéo:** Liên kết với Admin (`AE800`, `AS300`) và Shop (`G600`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `K601` | My Page - GOLD | 自分のプロフィール_GOLD | APP | WIP / WIP / WIP / Backlog (chưa gửi) | cần xử lý thêm logic close tài khoản |
| `K6012` | My Page - GOLD to POINT | 自分のプロフィール_GOLD_ポイント交換 | APP | Spec done / Done / Done / Backlog (sắp gửi) | - |
| `K6013` | My Page - GOLD to POINT History | 自分のプロフィール_GOLD_ポイント交換履歴子画面 | APP | Spec done / Done / Done / Backlog (sắp gửi) | - |
| `K602` | My Page - Reward Calendar | 自分のプロフィール_リワードカレンダー | APP | Spec done / Done / Done / Backlog (sắp gửi) | - |


#### 11.7 Tài khoản Nhận tiền & Yêu cầu Rút tiền (Payout) (7 màn hình)

- **Tính năng chính & Spec:** Liên kết tài khoản ngân hàng (`K906`), xem trước (`K9061`), xác thực OTP (`K9062`), xác nhận (`K9063`), lịch sử tất cả (`K9064`), yêu cầu rút tiền tức thì (`K9065`) và lịch sử chi trả thành công (`K9066`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra bắt buộc hoàn tất eKYC (`K205`) trước khi rút tiền, validate thông tin ngân hàng, hạn mức rút tối thiểu/tối đa, trạng thái yêu cầu đồng bộ với Admin (`AS200`).
- **Liên kết chéo:** Liên kết chặt với Admin (`AS200`, `AE700`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `K906` | My Profile _ Payout Account Linkage | 自分のプロフィール_GOLD_自分のプロフィール_振込先連携 | APP | Spec done / Done / Done / Done (sắp gửi) | cần xử lý thêm logic close tài khoản |
| `K9061` | My Profile _ Payout Account Preview | 自分のプロフィール_GOLD_振込登録内容プレビュー | APP | Spec done / Done / Done / Done (sắp gửi) | - |
| `K9062` | My Profile _ Payout Account OTP code | 自分のプロフィール_GOLD_確認コード入力 | APP | Spec done / Done / Done / Done (sắp gửi) | - |
| `K9063` | My Profile _ Payout Account Confirmation | 自分のプロフィール_GOLD_振込先確認 | APP | Spec done / Done / Done / Done (sắp gửi) | - |
| `K9064` | My Profile _ Payout History - all | 自分のプロフィール_GOLD_振込履歴 | APP | WIP / Backlog / Backlog / Backlog (chưa gửi) | - |
| `K9065` | My Profile _ Instant Payout Request | 自分のプロフィール_GOLD_即時振込申請 | APP | WIP / Backlog / Backlog / Backlog (chưa gửi) | - |
| `K9066` | My Profile _Payout History - sucess | 自分のプロフィール_GOLD_支払履歴 | APP | WIP / Backlog / Backlog / Backlog (chưa gửi) | - |


#### 11.8 Thống kê LIVE, Bảng Xếp hạng & Nhật ký Tương tác (16 màn hình)

- **Tính năng chính & Spec:** Tổng quan phân tích LIVE (`K9071`), chọn lịch (`K9072`), danh sách phiên (`K9073`), chi tiết phiên (`K9074`), danh sách người xem (`K9075`); xếp hạng Dolls/Gifter (`K901`, `K902`); nhật ký người gửi quà/Gift Gacha/2-shot/Kho báu/Follower/Familia/Whisper (`K909`, `K9091A`, `K9092-K9096`), Likes (`K903`) và Keeps (`K904`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra độ chính xác số liệu thống kê (viewer, thời lượng, quà, GOLD nhận được) khớp với phiên live thực tế và dữ liệu DB.
- **Liên kết chéo:** Liên kết với `B103-B104`, `AE800`, `BD500`.

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `K9071` | My Page - LIVE Analysis Overview | 自分のプロフィール_LIVE分析概要 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K9072` | My Page - LIVE Analysis Overview: Calendar Selector Screen | 自分のプロフィール_LIVE分析概要カレンダー選択子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K9073` | My Page - LIVE Analysis List | 自分のプロフィール_LIVE分析一覧 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K9074` | My Page - LIVE Analysis Details | 自分のプロフィール_LIVE分析詳細 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K9075` | My Page - LIVE Viewer List | 自分のプロフィール_LIVE視聴者一覧 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K903` | My Page - Likes | 自分のプロフィール_いいね | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K904` | My Page - Keeps | 自分のプロフィール_キープ | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K9091A` | My Page - Gift Sender List | 自分のプロフィール_ギフト送信者一覧 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K9092` | My Page - 2 Shot History | 自分のプロフィール_２ショット申請履歴 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K9093` | My Page - Treasure Chest Sender List | 自分のプロフィール_宝箱送信者一覧 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K9094` | My Page - New follower list | 自分のプロフィール_新規フォロワー一覧 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K9095` | My Page - New familia member list | 自分のプロフィール_新規ファミリアメンバー一覧 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K9096` | My Page - Whisper sender list | 自分のプロフィール_ウィスパー送信者一覧 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K909` | My Page - Gift Gacha Sender List | 自分のプロフィール_ギフトガチャ送信者一覧 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K901` | My Page - Dolls Ranking | 自分のプロフィール_ドールズランキング | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K902` | My Page - Gifter Ranking | 自分のプロフィール_ギフターランキング | APP | Spec done / Done / Done / Done (đã gửi) | - |


#### 11.9 Quản lý Video Lưu trữ Cá nhân (My Archive) (4 màn hình)

- **Tính năng chính & Spec:** Danh sách Archive của tôi (`K9051` - không cho download video có gắn karaoke), chi tiết (`K9052`), cài đặt công khai (`K9053`) và tùy chọn Archive (`K9054`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra rule cấm tải xuống video có chứa nhạc Karaoke, cài đặt quyền riêng tư (Public/Familia/Private) phản ánh đúng sang `D701`.
- **Liên kết chéo:** Liên kết với `D701-D705`, Admin (`AG500`), Agency (`BF300`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `K9051` | My Page - Archive list (ko cho DL video có gắn karaoke) | 自分のプロフィール_配信アーカイブ一覧 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K9052` | My Page - Archive detail | 自分のプロフィール_配信アーカイブ詳細 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K9053` | My Page - Archive Setting | 自分のプロフィール_配信アーカイブ公開設定子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K9054` | My Page - Archive Option | 自分のプロフィール_アーカイブオプション子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |


#### 11.10 Karaoke Cá nhân & Báo cáo Bài hát đã sử dụng (ACRCloud) (14 màn hình)

- **Tính năng chính & Spec:** Kho Karaoke trên My Page (`K010`), lịch sử hát (`K011`), tìm bài & ca sĩ (`K0121-K0124`, `K0131-K0132`), danh sách yêu thích (`K0141-K0142`), và luồng báo cáo bài hát sử dụng ACRCloud (`K209-New` Xem/Tạo/Sửa).
- **Trọng tâm Test / Verify Bug:** Kiểm tra nhận diện/báo cáo bài hát bản quyền (`K209-New`) đồng bộ chính xác lên Admin (`AL600`, `AL700`).
- **Liên kết chéo:** Liên kết với Admin (`AL600`, `AL700`) và Karaoke Live (`M401`, `I501`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `K209-New` | ACRCLOUD - App  My Profile_Report of Used Songs | 自分のプロフィール_使用楽曲の報告 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K209-New` | My Profile_View Report of Used Songs | 自分のプロフィール_使用楽曲の報告参照 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K209-New` | My Profile_Create New Report of Used Songs | 自分のプロフィール_使用楽曲の報告新規 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K209-New` | My Profile_Edit Report of Used Songs | 自分のプロフィール_使用楽曲の報告変更 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K0132` | My Page - Search Artist - Artist song list | -配信共通_アーティスト曲一覧 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `K010` | My Page - Karaoke | 自分のプロフィール_カラオケ | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K011` | My Page - Karaoke Sing History | 自分のプロフィール_歌唱履歴 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K0121` | My Page - Search song - keyword | -配信共通_曲検索_キーワード | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K0122` | My Page - Search song - Popular | 配信共通_曲検索_人気 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K0123` | My Page - Search song - Era | 配信共通_曲検索_年代 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K0124` | My Page - Song detail | -配信共通_曲詳細_子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K0131` | My Page - Search Artist | -配信共通_アーティスト検索 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K0141` | My Page - Favourite Airtist List | -配信共通_お気に入りアーティスト一覧 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `K0142` | My Page - Favourite Song List | -配信共通_お気に入り曲一覧 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |


### 12. Cộng đồng Familia, Bài đăng & Backnumber (Familia Fanclub & Content) (45 màn hình)

#### 12.1 Trang chủ Familia, Khám phá & Tìm kiếm (8 màn hình)

- **Tính năng chính & Spec:** Trang chủ Familia (`L100`), bài mới từ Familia đã tham gia (`L1001`), Familia mới nổi bật (`L1002`), bài mới nổi bật (`L1003`), bảng xếp hạng bài đăng ngày (`L1004`), tìm kiếm theo Familia/Bài đăng/Tag (`L1021-L1023`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra phân loại feed đúng Familia đã join vs gợi ý, tìm kiếm chính xác theo tag và thứ hạng daily ranking.
- **Liên kết chéo:** Điều hướng tới `L200-L203` (Other Familia) hoặc `L300` (My Familia).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `L100` | Familia_Home | マイファミリア_ホーム | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L1001` | My Familia_Home_New Posts from Joined Familias | マイファミリア_ホーム_加入ファミリアの新着投稿 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L1002` | My Familia_Home_Featured New Familias | マイファミリア_ホーム_注目の新しいファミリア | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L1003` | My Familia_Home_Featured New Posts | マイファミリア_ホーム_注目の新着投稿 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L1004` | My Familia_Home_Post Daily Ranking | マイファミリア_ホーム_投稿デイリーランキング | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L1021` | Familia Search - Famila | マイファミリア_探す_ファミリア | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L1022` | Familia Search - Post | マイファミリア_探す_投稿 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L1023` | Familia Search - Tag | マイファミリア_探す_タグ | APP | Spec done / Done / Done / Done (IS CLOSE) | - |


#### 12.2 Quản lý Giới thiệu & Mục tiêu Yell của My Familia (8 màn hình)

- **Tính năng chính & Spec:** Xem/sửa trang giới thiệu (`L300`, `L301`, `L302`), upload portfolio (`L303`), danh sách mục tiêu (`L3041`), tạo/sửa mục tiêu (`L3042`, `L3043`) và danh sách người ủng hộ Yell (`L3044`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra upload media portfolio, tiến độ thanh mục tiêu Yell cập nhật realtime khi có user donate ở `L201`.
- **Liên kết chéo:** Liên kết với `L200`, `L201` (Other Familia Donate).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `L301` | My Familia Intro section | - マイファミリア_紹介 | APP | Spec done / Done / Done / Done (-) | - |
| `L303` | My Familia - Intro Edit - Modal up file | - マイファミリア_ポートフォリオアップロード | APP | Spec done / Done / Done / Done (-) | - |
| `L300` | My Familia Intro | マイファミリア_紹介参照 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L302` | My Familia - Intro Edit | マイファミリア_紹介変更 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L3041` | My Familia - Target List | マイファミリア_エール目標 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L3042` | My Familia - Create Target | -マイファミリア_新規目標作成フォーム | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L3043` | My Familia - Update Target | -マイファミリア_目標編集 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L3044` | My Familia - Yell Participants List | マイファミリア_エール支援者一覧子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |


#### 12.3 Quản lý Bài đăng, Tag & Bình luận của My Familia (9 màn hình)

- **Tính năng chính & Spec:** Gợi ý tag (`L401`), danh sách bài đăng (`L402`), tạo bài & thêm nội dung/upload file (`L403`, `L4041`, `L4042`), chi tiết bài (`L405`), chỉnh sửa/xóa bài & nội dung (`L406`, `L4061`) và bình luận bài đăng (`L407`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra phân quyền xem bài theo Class/Backnumber, upload đa phương tiện (ảnh/video/audio), xóa/sửa bài đồng bộ sang Admin (`AM100`) và Agency (`BE100`).
- **Liên kết chéo:** Liên kết với Admin (`AM100-AM200`) và Agency (`BE100-BE200`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `L401` | My Familia - Tag | マイファミリア_おすすめタグ | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L402` | My Familia - Post List | マイファミリア_投稿一覧 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L403` | My Familia - Post Create | マイファミリア_投稿新規 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L4041` | My Familia - Post Create - Post Content Create | マイファミリア_投稿コンテンツ子画面 - Create | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L4042` | My Familia - Post Create - Post Content Create - Modal upload content | -マイファミリア_投稿コンテンツ子画面 - Modal upload file | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L405` | My Familia - Post Detail | マイファミリア_投稿参照 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L406` | My Familia - Post Edit | マイファミリア_投稿変更 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L4061` | My Familia - Post Edit - Post Content Update, Delete | -マイファミリア_投稿変更コンテンツ子画面 - Update | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L407` | Post Comment | ファミリア_投稿コメント子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |


#### 12.4 Quản lý Hạng thành viên (Class), Stamp & Backnumber của tôi (5 màn hình)

- **Tính năng chính & Spec:** Danh sách hạng (`L501`), tạo/sửa hạng (`L502`, `L503`), thêm Stamp độc quyền (`L504`) và danh sách Backnumber của tôi (`L600`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra cấu hình giá/quyền lợi từng Class, upload Stamp sử dụng được trong chat (`F500`), bật/tắt bán Backnumber.
- **Liên kết chéo:** Liên kết với `F500` (Stamp) và `L205-L210` (Other Familia Subscribe/Backnumber).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `L504` | My Familia -  Add Stamp | マイファミリア_スタンプ | APP | Spec done / Done / Done / Done (-) | - |
| `L501` | My Familia - Class List | マイファミリア_クラス一覧 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `L502` | My Familia - Add New Class | マイファミリア_クラス新規 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `L503` | My Familia - Edit Class | マイファミリア_クラス変更 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `L600` | My Familia - Backnumber list | マイファミリア_バックナンバー一覧 | APP | Spec done / Done / Done / Done (đã gửi) | - |


#### 12.5 Xem Familia Người khác, Donate Yell & Trình phát Bài đăng (8 màn hình)

- **Tính năng chính & Spec:** Trang giới thiệu (`L200`), ủng hộ Yell (`L201`), danh sách & chi tiết bài đăng (`L202`, `L203`), xem chi tiết bài riêng lẻ (`L2041`), tùy chọn phát (`L2042`), tốc độ phát (`L2043`) và cài đặt phụ đề (`L2044`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra trừ Coin/Point khi Donate Yell (`L201`), khóa nội dung trả phí nếu chưa tham gia Class/mua Backnumber, đổi tốc độ và phụ đề video.
- **Liên kết chéo:** Liên kết với `L300`, `L3044`, `L402`.

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `L200` | Other User’s Familia_Introduction | 他人のファミリア_紹介 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L201` | Other User’s Familia_Donate Subscreen | 他人のファミリア_エール支援子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L202` | Other User’s Familia_Post List | 他人のファミリア_投稿一覧 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L203` | Other User’s Familia_Post Details | 他人のファミリア_投稿詳細 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L2041` | Other’s Familia_Post Details (Individual) | 他人のファミリア_投稿詳細個別 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L2042` | Other’s Familia_Post Details (Individual)_Options Subscreen | 他人のファミリア_投稿詳細個別_オプション子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L2043` | Other’s Familia_Post Details (Individual)_Options Subscreen_Speed | 他人のファミリア_再生速度設定子画面 | APP | Spec done / Done / Done / Done (IS CLOSE) | - |
| `L2044` | Other’s Familia_Post Details (Individual)_Options Subscreen_Subtitle | 他人のファミリア_字幕設定子画面 | APP | Spec done / Done / Done / Done (đã gửi) | - |


#### 12.6 Tham gia Class & Mua Backnumber Familia Người khác (7 màn hình)

- **Tính năng chính & Spec:** Danh sách Class (`L205`), đăng ký tham gia Class (`L206`), đổi Class (`L207`), hủy đăng ký (`L208`), danh sách Backnumber (`L209`), mua Backnumber (`L210`) và logic bật/tắt bán Backnumber (`-`).
- **Trọng tâm Test / Verify Bug:** Kiểm tra thanh toán khi join Class/mua Backnumber, nâng/hạ hạng (`L207`), hủy gia hạn (`L208`) vẫn giữ quyền đến hết chu kỳ, và ẩn nút mua khi Backnumber sale OFF.
- **Liên kết chéo:** Liên kết với `L501-L503`, `L600` và Billing (`G600`).

| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `L205` | Other's Familia - Class List | 他人のファミリア_クラス一覧 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `L206` | Other's Familia - Join Class - APP | 他人のファミリア_クラス参加 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `L207` | Other’s Familia - Class Change | 他人のファミリア_クラス変更 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `L208` | Other’s Familia - Cancel subcribe | 他人のファミリア_クラス退会 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `L209` | Other's Familia - Backnumber List | 他人のファミリア_バックナンバー一覧 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `L210` | Other's Familia - Backnumber Purchase | 他人のファミリア_バックナンバー購入 | APP | Spec done / Done / Done / Done (đã gửi) | - |
| `-` | Backnumber sale ON/OFF logic | - | App | - | - |



---
## V. CHỈ MỤC TRA CỨU NHANH THEO MÃ MÀN HÌNH (QUICK ID INDEX)

> Dùng `Ctrl+F` hoặc AI grep theo mã màn hình để định vị ngay cụm tính năng chi tiết.

| Mã ID | Nhóm | Cụm tính năng chi tiết | Tên màn hình (EN) |
| :--- | :---: | :--- | :--- |
| `-` | App | 12.6 Tham gia Class & Mua Backnumber Familia Người khác | Backnumber sale ON/OFF logic |
| `-` | App | 10.7 Phát sóng qua OBS (OBS Normal / Familia / 2-Shot / Viewer) | CR - Voice Monitor |
| `-` | App | 1.2 Khởi tạo Hồ sơ, Quà tân thủ & Single-Device Session | CR - [Login] 1 UID chỉ được phép đăng nhập trên 1 device tại một thời điểm |
| `A000` | App | 1.1 Khởi động, Đăng nhập (SNS / SĐT OTP) & Điều khoản | Slash |
| `A000` | App | 1.1 Khởi động, Đăng nhập (SNS / SĐT OTP) & Điều khoản | Slash |
| `A100` | App | 1.1 Khởi động, Đăng nhập (SNS / SĐT OTP) & Điều khoản | Login |
| `A100` | App | 1.1 Khởi động, Đăng nhập (SNS / SĐT OTP) & Điều khoản | Login |
| `A101` | App | 1.1 Khởi động, Đăng nhập (SNS / SĐT OTP) & Điều khoản | Login - A popup requiring agreement to the Terms of Use |
| `A101` | App | 1.1 Khởi động, Đăng nhập (SNS / SĐT OTP) & Điều khoản | Login - A popup requiring agreement to the Terms of Use |
| `A1031` | App | 1.1 Khởi động, Đăng nhập (SNS / SĐT OTP) & Điều khoản | Login - Enter phone number |
| `A1031` | App | 1.1 Khởi động, Đăng nhập (SNS / SĐT OTP) & Điều khoản | Login - Enter phone number |
| `A1032` | App | 1.1 Khởi động, Đăng nhập (SNS / SĐT OTP) & Điều khoản | Login - Enter OTP |
| `A1032` | App | 1.1 Khởi động, Đăng nhập (SNS / SĐT OTP) & Điều khoản | Login - Enter OTP |
| `A105` | App | 1.2 Khởi tạo Hồ sơ, Quà tân thủ & Single-Device Session | Login - Init Account Setting |
| `A105` | App | 1.2 Khởi tạo Hồ sơ, Quà tân thủ & Single-Device Session | Login - Init Account Setting |
| `A201` | App | 2.1 Trung tâm Trợ giúp & Gửi yêu cầu Hỗ trợ (Help & Inquiry) | Help Category Sub-screen |
| `A201` | App | 2.1 Trung tâm Trợ giúp & Gửi yêu cầu Hỗ trợ (Help & Inquiry) | Help Details Sub-screen |
| `A201` | App | 2.1 Trung tâm Trợ giúp & Gửi yêu cầu Hỗ trợ (Help & Inquiry) | Help Search Results Sub-screen |
| `A201` | App | 2.1 Trung tâm Trợ giúp & Gửi yêu cầu Hỗ trợ (Help & Inquiry) | Help Top Sub-screen |
| `A202` | App | 2.1 Trung tâm Trợ giúp & Gửi yêu cầu Hỗ trợ (Help & Inquiry) | Inquiry Completion Sub-screen |
| `A202` | App | 2.1 Trung tâm Trợ giúp & Gửi yêu cầu Hỗ trợ (Help & Inquiry) | Inquiry Details Sub-screen |
| `A204` | App | 2.2 Điều khoản Pháp lý, Chính sách & Tỷ lệ Gacha (Webview) | Privacy Policy Sub-screen |
| `A205` | App | 2.2 Điều khoản Pháp lý, Chính sách & Tỷ lệ Gacha (Webview) | Terms of Service Sub-screen |
| `A206` | App | 2.2 Điều khoản Pháp lý, Chính sách & Tỷ lệ Gacha (Webview) | In-app Currency Terms Sub-screen |
| `A207` | App | 2.2 Điều khoản Pháp lý, Chính sách & Tỷ lệ Gacha (Webview) | Treasure Box Terms of Use Sub-screen |
| `A208` | App | 2.2 Điều khoản Pháp lý, Chính sách & Tỷ lệ Gacha (Webview) | Specified Commercial Transaction Act / Payment Services Act Sub-screen |
| `A209` | App | 2.2 Điều khoản Pháp lý, Chính sách & Tỷ lệ Gacha (Webview) | Gacha Rate |
| `A300` | App | 1.2 Khởi tạo Hồ sơ, Quà tân thủ & Single-Device Session | Login bonus |
| `AA000` | Admin | 1.1 Xác thực & Quên/Đổi mật khẩu Admin | Login top |
| `AA003` | Admin | 1.1 Xác thực & Quên/Đổi mật khẩu Admin | Change Password |
| `AB000` | Admin | 1.1 Xác thực & Quên/Đổi mật khẩu Admin | Change password |
| `AB000` | Admin | 1.1 Xác thực & Quên/Đổi mật khẩu Admin | Password change request |
| `AB000` | Admin | 1.1 Xác thực & Quên/Đổi mật khẩu Admin | Password change request completed |
| `AC100` | Admin | 1.2 Quản lý Tài khoản & Phân quyền System Admin | System Admin Manage - System Admin List, Search |
| `AC200` | Admin | 1.2 Quản lý Tài khoản & Phân quyền System Admin | System Admin Manage - System Admin Create |
| `AC300` | Admin | 1.2 Quản lý Tài khoản & Phân quyền System Admin | System Admin Manage - System Admin Update |
| `AC400` | Admin | 1.2 Quản lý Tài khoản & Phân quyền System Admin | Phân quyền system admin |
| `AD100` | Admin | 2.1 Quản lý Hồ sơ Agency & Danh sách Streamer trực thuộc | Agency Manage - Agency List / Search |
| `AD200` | Admin | 2.1 Quản lý Hồ sơ Agency & Danh sách Streamer trực thuộc | Agency Manage - Register Agency |
| `AD301` | Admin | 2.1 Quản lý Hồ sơ Agency & Danh sách Streamer trực thuộc | Agency Manage - Agency Detail, Update, Delete |
| `AD302` | Admin | 2.1 Quản lý Hồ sơ Agency & Danh sách Streamer trực thuộc | Agency Manage - Agency Streamer List |
| `AE100` | Admin | 3.1 Hồ sơ Người dùng, Xác thực eKYC & Xóa tài khoản | User List |
| `AE200` | Admin | 3.1 Hồ sơ Người dùng, Xác thực eKYC & Xóa tài khoản | User Details |
| `AE300` | Admin | 3.2 Tài sản, Lịch sử sử dụng, Hóa đơn & Doanh thu Người dùng | User Details - Owned Items |
| `AE400` | Admin | 3.2 Tài sản, Lịch sử sử dụng, Hóa đơn & Doanh thu Người dùng | User Details - Usage History |
| `AE500` | Admin | 3.2 Tài sản, Lịch sử sử dụng, Hóa đơn & Doanh thu Người dùng | User Details - Billing Log |
| `AE600` | Admin | 3.2 Tài sản, Lịch sử sử dụng, Hóa đơn & Doanh thu Người dùng | User Details - Payment Information |
| `AE700` | Admin | 3.1 Hồ sơ Người dùng, Xác thực eKYC & Xóa tài khoản | User Details - Ekyc and OCR |
| `AE800` | Admin | 3.2 Tài sản, Lịch sử sử dụng, Hóa đơn & Doanh thu Người dùng | User Detail - Revenue |
| `AF100` | Admin | 4.1 Danh mục, CRUD Quà tặng & Quà cao cấp | Gift Manage - Gift List |
| `AF200` | Admin | 4.1 Danh mục, CRUD Quà tặng & Quà cao cấp | Gift Manage - Gift Create |
| `AF300` | Admin | 4.1 Danh mục, CRUD Quà tặng & Quà cao cấp | Gift Manage - Gift Update, Delete |
| `AF400` | Admin | 4.1 Danh mục, CRUD Quà tặng & Quà cao cấp | Gift Manage - Gift Category Manage |
| `AF500` | Admin | 4.1 Danh mục, CRUD Quà tặng & Quà cao cấp | Quà cao cấp |
| `AG100` | Admin | 5.1 Giám sát Phòng Live đang phát, Xem trực tiếp & Archive | Stream Manage - List Stream |
| `AG200` | Admin | 5.1 Giám sát Phòng Live đang phát, Xem trực tiếp & Archive | Stream Manage - View Stream |
| `AG300` | Admin | 5.1 Giám sát Phòng Live đang phát, Xem trực tiếp & Archive | Stream Manage - List Ban |
| `AG400` | Admin | 5.1 Giám sát Phòng Live đang phát, Xem trực tiếp & Archive | Stream Manage - List Force Stop |
| `AG500` | Admin | 5.1 Giám sát Phòng Live đang phát, Xem trực tiếp & Archive | Stream Manage - List + View Stream（ENDED) |
| `AH100` | Admin | 6.1 Quản lý Thông báo Hệ thống & Tin nhắn từ Admin | Announcement Manage - Announcement List |
| `AH200` | Admin | 6.1 Quản lý Thông báo Hệ thống & Tin nhắn từ Admin | Announcement Manage - Announcement Create |
| `AH300` | Admin | 6.1 Quản lý Thông báo Hệ thống & Tin nhắn từ Admin | Announcement Manage - Announcement Edit |
| `AH301` | Admin | 6.1 Quản lý Thông báo Hệ thống & Tin nhắn từ Admin | Announcement Manage - Announcement Preview |
| `AH400` | Admin | 6.1 Quản lý Thông báo Hệ thống & Tin nhắn từ Admin | Message Admin |
| `AI100` | Admin | 7.1 Xử lý Báo cáo Vi phạm (Report Management) | Report Manage - Report List |
| `AI200` | Admin | 7.1 Xử lý Báo cáo Vi phạm (Report Management) | Report Manage - Report Detail |
| `AJ100` | Admin | 8.1 Quản lý Kho BGM & Chuyển đổi định dạng Audio | BGM Manage - BGM List |
| `AJ200` | Admin | 8.1 Quản lý Kho BGM & Chuyển đổi định dạng Audio | BGM Manage - BGM Create |
| `AJ300` | Admin | 8.1 Quản lý Kho BGM & Chuyển đổi định dạng Audio | BGM Manage - BGM Edit |
| `AJ400` | Admin | 8.1 Quản lý Kho BGM & Chuyển đổi định dạng Audio | BGM Manage - MP3 WAV Convert |
| `AK201` | Admin | 9.1 Quản lý Hình nền Minh họa (Background Illustrations) | Background Illustrations Manage - Background Illustrations List |
| `AK202` | Admin | 9.1 Quản lý Hình nền Minh họa (Background Illustrations) | Background Illustrations Manage - Background Illustrations Create |
| `AK203` | Admin | 9.1 Quản lý Hình nền Minh họa (Background Illustrations) | Background Illustrations Manage - Background Illustrations Edit |
| `AK301` | Admin | 9.2 Quản lý Hình nền Mini Garden | Mini Garden Background Manage - Mini Garden Background List |
| `AK302` | Admin | 9.2 Quản lý Hình nền Mini Garden | Mini Garden Background Manage - Mini Garden Background Create |
| `AK303` | Admin | 9.2 Quản lý Hình nền Mini Garden | Mini Garden Background Manage - Mini Garden Background Edit |
| `AL100` | Admin | 10.1 Quản lý Kho bài hát Karaoke & Yêu cầu thêm bài | Karaoke Manage - Karaoke List |
| `AL101` | Admin | 10.1 Quản lý Kho bài hát Karaoke & Yêu cầu thêm bài | Karaoke Manage - Karaoke Upload |
| `AL200` | Admin | 10.1 Quản lý Kho bài hát Karaoke & Yêu cầu thêm bài | Karaoke Manage - Karaoke Create |
| `AL300` | Admin | 10.1 Quản lý Kho bài hát Karaoke & Yêu cầu thêm bài | Karaoke Manage - Karaoke Edit |
| `AL400` | Admin | 10.1 Quản lý Kho bài hát Karaoke & Yêu cầu thêm bài | Karaoke Manage - Karaoke Request List |
| `AL600` | Admin | 10.2 Báo cáo Bản quyền Âm nhạc (JASRAC / NEXTONE) & Nội dung trả phí | JASRAC / NEXTONE Used Song Reports |
| `AL700` | Admin | 10.2 Báo cáo Bản quyền Âm nhạc (JASRAC / NEXTONE) & Nội dung trả phí | Paid Content List |
| `AL700` | Admin | 10.2 Báo cáo Bản quyền Âm nhạc (JASRAC / NEXTONE) & Nội dung trả phí | User Used Song Report Details |
| `AL700` | Admin | 10.2 Báo cáo Bản quyền Âm nhạc (JASRAC / NEXTONE) & Nội dung trả phí | User Used Song Report List |
| `AM100` | Admin | 11.1 Quản lý & Kiểm duyệt Bài đăng Familia (Post Management) | Post List |
| `AM101` | Admin | 11.1 Quản lý & Kiểm duyệt Bài đăng Familia (Post Management) | {user_name}'s Post List |
| `AM200` | Admin | 11.1 Quản lý & Kiểm duyệt Bài đăng Familia (Post Management) | Post Details |
| `AP000` | Admin | 12.1 Quản lý 3D Model, Bộ phận (Head/Body/Accessory) & Độ phân giải | Admin Model - Setting độ phân giải |
| `AP000` | Admin | 12.1 Quản lý 3D Model, Bộ phận (Head/Body/Accessory) & Độ phân giải | List model |
| `AP100` | Admin | 12.1 Quản lý 3D Model, Bộ phận (Head/Body/Accessory) & Độ phân giải | Model detail |
| `AP200` | Admin | 12.1 Quản lý 3D Model, Bộ phận (Head/Body/Accessory) & Độ phân giải | Head detail |
| `AP300` | Admin | 12.1 Quản lý 3D Model, Bộ phận (Head/Body/Accessory) & Độ phân giải | Body Detail |
| `AP400` | Admin | 12.1 Quản lý 3D Model, Bộ phận (Head/Body/Accessory) & Độ phân giải | Accessory |
| `AQ100` | Admin | 13.1 Quản lý Gacha (Avatar, Mini Garden & Background Gacha) | Quản lý Gacha - avatar gacha |
| `AQ200` | Admin | 13.1 Quản lý Gacha (Avatar, Mini Garden & Background Gacha) | Quản lý Gacha - avatar gacha detail |
| `AQ300` | Admin | 13.1 Quản lý Gacha (Avatar, Mini Garden & Background Gacha) | Quản lý Gacha - avatar gacha Setup |
| `AQ400` | Admin | 13.1 Quản lý Gacha (Avatar, Mini Garden & Background Gacha) | Quản lý Gacha -  mini garden gacha |
| `AQ500` | Admin | 13.1 Quản lý Gacha (Avatar, Mini Garden & Background Gacha) | Quản lý Gacha - BG gacha |
| `AS100` | Admin | 14.1 Phân tích Doanh thu, Tỷ giá & Duyệt Yêu cầu Rút tiền (Payout) | Sales - User Revenue Analysis |
| `AS200` | Admin | 14.1 Phân tích Doanh thu, Tỷ giá & Duyệt Yêu cầu Rút tiền (Payout) | Sales - Payout Request |
| `AS300` | Admin | 14.1 Phân tích Doanh thu, Tỷ giá & Duyệt Yêu cầu Rút tiền (Payout) | Sales - Exchange Rate |
| `AS500` | Admin | 14.1 Phân tích Doanh thu, Tỷ giá & Duyệt Yêu cầu Rút tiền (Payout) | Sales - Agency Revenue Analysis |
| `AX100` | Admin | 15.1 Giám sát Tin nhắn Người dùng (User Messages Monitoring) | Message Manage - Search |
| `AX200` | Admin | 15.1 Giám sát Tin nhắn Người dùng (User Messages Monitoring) | Message Manage - Message Detail |
| `AX300` | Admin | 15.1 Giám sát Tin nhắn Người dùng (User Messages Monitoring) | Message Manage - Message Info |
| `AY100` | Admin | 16.1 Giám sát Bình luận & Danh sách Cấm Chat Livestream | Livestream messsage - Search |
| `AY200` | Admin | 16.1 Giám sát Bình luận & Danh sách Cấm Chat Livestream | Livestream messsage - Detail |
| `AY300` | Admin | 16.1 Giám sát Bình luận & Danh sách Cấm Chat Livestream | Livestream messsage - BAN LIST |
| `B001` | App | 3.1 Trang chủ, Gợi ý Nội dung & Quảng cáo (Recommend & Ads) | Recommend - Post |
| `B002` | App | 3.1 Trang chủ, Gợi ý Nội dung & Quảng cáo (Recommend & Ads) | Recommend - Livestream standby |
| `B003` | App | 3.1 Trang chủ, Gợi ý Nội dung & Quảng cáo (Recommend & Ads) | Recommend - Livestream |
| `B100` | App | 3.1 Trang chủ, Gợi ý Nội dung & Quảng cáo (Recommend & Ads) | List Initial |
| `B101` | App | 3.1 Trang chủ, Gợi ý Nội dung & Quảng cáo (Recommend & Ads) | List Recommend |
| `B102` | App | 3.1 Trang chủ, Gợi ý Nội dung & Quảng cáo (Recommend & Ads) | List Recommended Category |
| `B103` | App | 3.2 Bảng xếp hạng & Nhiệm vụ (Ranking & Missions) | List Ranker |
| `B104` | App | 3.2 Bảng xếp hạng & Nhiệm vụ (Ranking & Missions) | List Ranking Dolls |
| `B104` | App | 3.2 Bảng xếp hạng & Nhiệm vụ (Ranking & Missions) | List Ranking Gifter |
| `B200` | App | 3.2 Bảng xếp hạng & Nhiệm vụ (Ranking & Missions) | Mission List GĐ1 + GĐ2 |
| `B200` | App | 3.2 Bảng xếp hạng & Nhiệm vụ (Ranking & Missions) | Mission List GĐ3 |
| `B300` | App | 3.1 Trang chủ, Gợi ý Nội dung & Quảng cáo (Recommend & Ads) | Advertisement |
| `BA100` | Agency | 1.1 Đăng nhập & Đổi/Quên mật khẩu Cổng Agency | Login top |
| `BA1001` | Agency | 1.1 Đăng nhập & Đổi/Quên mật khẩu Cổng Agency | Password change request |
| `BA1002` | Agency | 1.1 Đăng nhập & Đổi/Quên mật khẩu Cổng Agency | Password change request completed |
| `BA1003` | Agency | 1.1 Đăng nhập & Đổi/Quên mật khẩu Cổng Agency | Change password |
| `BA200` | Agency | 1.1 Đăng nhập & Đổi/Quên mật khẩu Cổng Agency | Change Password |
| `BB100` | Agency | 2.1 Thông tin Agency & Quản lý Quản trị viên trực thuộc | Agency Admin List |
| `BB101` | Agency | 2.1 Thông tin Agency & Quản lý Quản trị viên trực thuộc | Agency Detail |
| `BB200` | Agency | 2.1 Thông tin Agency & Quản lý Quản trị viên trực thuộc | Agency Admin Create |
| `BB300` | Agency | 2.1 Thông tin Agency & Quản lý Quản trị viên trực thuộc | Agency Admin Detail |
| `BC100` | Agency | 3.1 Quản lý Danh sách & Hồ sơ Streamer / Liver trực thuộc | Liver List |
| `BC200` | Agency | 3.1 Quản lý Danh sách & Hồ sơ Streamer / Liver trực thuộc | Liver Details |
| `BD100` | Agency | 3.2 Tài sản, Lịch sử, Billing & Doanh thu của Liver | Liver Details - Owned Items |
| `BD200` | Agency | 3.2 Tài sản, Lịch sử, Billing & Doanh thu của Liver | Liver Details - Usage History |
| `BD300` | Agency | 3.2 Tài sản, Lịch sử, Billing & Doanh thu của Liver | Liver Details - Billing Log |
| `BD400` | Agency | 3.2 Tài sản, Lịch sử, Billing & Doanh thu của Liver | Liver Details - Payment Information |
| `BD500` | Agency | 3.2 Tài sản, Lịch sử, Billing & Doanh thu của Liver | Liver Detail - Revenue Analysis |
| `BE100` | Agency | 4.1 Quản lý Bài đăng của Streamer (Streamer Posts) | Post list |
| `BE200` | Agency | 4.1 Quản lý Bài đăng của Streamer (Streamer Posts) | Post details |
| `BF100` | Agency | 5.1 Giám sát Livestream, Archive, Ban & Force Stop của Agency | List Stream |
| `BF200` | Agency | 5.1 Giám sát Livestream, Archive, Ban & Force Stop của Agency | Livestream Detail |
| `BF300` | Agency | 5.1 Giám sát Livestream, Archive, Ban & Force Stop của Agency | Archive Livestream - List + View |
| `BF400` | Agency | 5.1 Giám sát Livestream, Archive, Ban & Force Stop của Agency | List Ban |
| `BF500` | Agency | 5.1 Giám sát Livestream, Archive, Ban & Force Stop của Agency | List Force Stop |
| `BG100` | Agency | 6.1 Quản lý Báo cáo Vi phạm liên quan đến Liver của Agency | Report List |
| `BG200` | Agency | 6.1 Quản lý Báo cáo Vi phạm liên quan đến Liver của Agency | Report Detail |
| `BX100` | Agency | 7.1 Giám sát Tin nhắn & Bình luận Chat của Liver | User Message |
| `BY100` | Agency | 7.1 Giám sát Tin nhắn & Bình luận Chat của Liver | Livestream Comment |
| `BY300` | Agency | 7.1 Giám sát Tin nhắn & Bình luận Chat của Liver | List Ban (livestream chat) |
| `C100` | App | 4.1 Tìm kiếm Tổng hợp (Search Top) | Search |
| `CMR 63 - I1001` | App | 10.3 Điều hành Phòng Live & Các Chế độ Phát (Normal/Test/Familia/Broadcast/PiP) | CMR63 PIIP in app |
| `CMR 63 - I1001` | App | 9.7 Cài đặt trong Phòng Live & Picture-in-Picture (PiP) | CMR63 PIP  out app |
| `CMR60` | App | 10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live | Thống kê số lượt follow |
| `CMR64` | App | 10.3 Điều hành Phòng Live & Các Chế độ Phát (Normal/Test/Familia/Broadcast/PiP) | (Streamer View) Now Streaming - Change Title |
| `D100` | App | 5.1 Hồ sơ Người khác, Ghi chú, Nhạc yêu thích & Báo cáo/Block | View OO's profile |
| `D202` | App | 5.1 Hồ sơ Người khác, Ghi chú, Nhạc yêu thích & Báo cáo/Block | View OO's profile_Function |
| `D2021` | App | 5.1 Hồ sơ Người khác, Ghi chú, Nhạc yêu thích & Báo cáo/Block | View OO's profile _  Report target sub-screen |
| `D2022` | App | 5.1 Hồ sơ Người khác, Ghi chú, Nhạc yêu thích & Báo cáo/Block | View OO's profile _ Report reason sub-screen |
| `D2023` | App | 5.1 Hồ sơ Người khác, Ghi chú, Nhạc yêu thích & Báo cáo/Block | View OO's profile _ Report detail sub-screen |
| `D203` | App | 5.1 Hồ sơ Người khác, Ghi chú, Nhạc yêu thích & Báo cáo/Block | View OO's profile _ Note sub-screen |
| `D301` | App | 5.1 Hồ sơ Người khác, Ghi chú, Nhạc yêu thích & Báo cáo/Block | View OO's profile _ Singing history sub-screen |
| `D3021` | App | 5.1 Hồ sơ Người khác, Ghi chú, Nhạc yêu thích & Báo cáo/Block | View OO's profile _ Favorite artists sub-screen |
| `D3022` | App | 5.1 Hồ sơ Người khác, Ghi chú, Nhạc yêu thích & Báo cáo/Block | View OO's profile _ Favorite songs sub-screen |
| `D500` | App | 5.1 Hồ sơ Người khác, Ghi chú, Nhạc yêu thích & Báo cáo/Block | View OO's profile _ Notification settings sub-screen |
| `D600` | App | 5.1 Hồ sơ Người khác, Ghi chú, Nhạc yêu thích & Báo cáo/Block | View OO's profile _ Soldier members sub-screen |
| `D701` | App | 5.2 Video Lưu trữ (Archive) của Người khác | View OO's profile - Archive List |
| `D702` | App | 5.2 Video Lưu trữ (Archive) của Người khác | View OO's profile - Archive Detail |
| `D703` | App | 5.2 Video Lưu trữ (Archive) của Người khác | View OO's profile - Archive Detail - Select language |
| `D704` | App | 5.2 Video Lưu trữ (Archive) của Người khác | View OO's profile - Archive Detail - replay speed setting |
| `D705` | App | 5.2 Video Lưu trữ (Archive) của Người khác | View OO's profile - Archive Detail - Comment |
| `E201` | App | 6.1 Thông báo Hệ thống, Hoạt động & Push Notification | Announcement List |
| `E202` | App | 6.1 Thông báo Hệ thống, Hoạt động & Push Notification | Announcement Detail |
| `E203` | App | 6.1 Thông báo Hệ thống, Hoạt động & Push Notification | Activity List (Pushnoti List) |
| `E203` | App | 6.1 Thông báo Hệ thống, Hoạt động & Push Notification | Push Noti UI |
| `F100` | App | 7.1 Hòm thư, Chat 1-1 & Yêu cầu 2-Shot qua Tin nhắn | Message Top |
| `F101` | App | 7.1 Hòm thư, Chat 1-1 & Yêu cầu 2-Shot qua Tin nhắn | Message Details - 1-1 |
| `F1011` | App | 7.1 Hòm thư, Chat 1-1 & Yêu cầu 2-Shot qua Tin nhắn | Message Details - 1-1 - 2shot invite |
| `F1012` | App | 7.1 Hòm thư, Chat 1-1 & Yêu cầu 2-Shot qua Tin nhắn | Message Details - Individual - Settings |
| `F10121` | App | 7.1 Hòm thư, Chat 1-1 & Yêu cầu 2-Shot qua Tin nhắn | Message Details - Individual - Settings - Block |
| `F102` | App | 7.2 Nhóm Chat (Group Message & Quản lý thành viên) | Message Details - Group |
| `F1021` | App | 7.2 Nhóm Chat (Group Message & Quản lý thành viên) | Message Details - Group - Settings - Owner |
| `F1022` | App | 7.2 Nhóm Chat (Group Message & Quản lý thành viên) | Message Details - Group - Add Member (Subscreen) |
| `F1023` | App | 7.2 Nhóm Chat (Group Message & Quản lý thành viên) | Message Details - Group - Settings - Members |
| `F1024` | App | 7.2 Nhóm Chat (Group Message & Quản lý thành viên) | Message Details - Group - Leave Group |
| `F1025` | App | 7.2 Nhóm Chat (Group Message & Quản lý thành viên) | Message Details - Group - Settings - Leave Group |
| `F103` | App | 7.1 Hòm thư, Chat 1-1 & Yêu cầu 2-Shot qua Tin nhắn | Message Details - System |
| `F104` | App | 7.1 Hòm thư, Chat 1-1 & Yêu cầu 2-Shot qua Tin nhắn | Message Details - My message |
| `F200` | App | 7.1 Hòm thư, Chat 1-1 & Yêu cầu 2-Shot qua Tin nhắn | Create Message - 1-1 |
| `F300` | App | 7.2 Nhóm Chat (Group Message & Quản lý thành viên) | Create Message - Group |
| `F400` | App | 7.1 Hòm thư, Chat 1-1 & Yêu cầu 2-Shot qua Tin nhắn | Message Details - Unread message preview |
| `F500` | App | 7.1 Hòm thư, Chat 1-1 & Yêu cầu 2-Shot qua Tin nhắn | Message Details - Stamp |
| `G100` | App | 8.1 Cửa hàng Tổng hợp, Vé (Ticket) & Lịch sử Point/Coin | Shop Top |
| `G200` | App | 8.3 Gacha tại Shop & Trong Livestream, Đổi Mảnh (Fragment) | (Streamer View) Now Streaming - Setting in livestream - Gacha List |
| `G200` | App | 8.3 Gacha tại Shop & Trong Livestream, Đổi Mảnh (Fragment) | Gacha List (SHOP) |
| `G201` | App | 8.3 Gacha tại Shop & Trong Livestream, Đổi Mảnh (Fragment) | (Streamer View) Now Streaming - Setting in livestream - Gacha details |
| `G201` | App | 8.3 Gacha tại Shop & Trong Livestream, Đổi Mảnh (Fragment) | Gacha Detail (SHOP) |
| `G202` | App | 8.3 Gacha tại Shop & Trong Livestream, Đổi Mảnh (Fragment) | (Streamer View) Now Streaming - Setting in livestream - Gacha Result |
| `G203` | App | 8.3 Gacha tại Shop & Trong Livestream, Đổi Mảnh (Fragment) | (Streamer View) Now Streaming - Setting in livestream - Gacha details |
| `G301` | App | 8.3 Gacha tại Shop & Trong Livestream, Đổi Mảnh (Fragment) | Fragment Exchange |
| `G302` | App | 8.3 Gacha tại Shop & Trong Livestream, Đổi Mảnh (Fragment) | Fragment History Sub-screen |
| `G401` | App | 8.1 Cửa hàng Tổng hợp, Vé (Ticket) & Lịch sử Point/Coin | Ticket Exchange Sub-screen |
| `G402` | App | 8.1 Cửa hàng Tổng hợp, Vé (Ticket) & Lịch sử Point/Coin | Ticket History Sub-screen |
| `G501` | App | 8.2 Gói Hội viên Hàng tháng (Monthly Plans) | Monthly Plan List |
| `G5021` | App | 8.2 Gói Hội viên Hàng tháng (Monthly Plans) | Gold Plan Details |
| `G5021` | App | 8.2 Gói Hội viên Hàng tháng (Monthly Plans) | Monthly Pass |
| `G5021` | App | 8.2 Gói Hội viên Hàng tháng (Monthly Plans) | Platinum Plan Details |
| `G5021` | App | 8.2 Gói Hội viên Hàng tháng (Monthly Plans) | Royal Plan Details |
| `G5021` | App | 8.2 Gói Hội viên Hàng tháng (Monthly Plans) | Silver Plan Details |
| `G600` | App | 8.1 Cửa hàng Tổng hợp, Vé (Ticket) & Lịch sử Point/Coin | Point / Coin History Sub-screen |
| `G600` | App | 8.1 Cửa hàng Tổng hợp, Vé (Ticket) & Lịch sử Point/Coin | Point / Coin History Sub-screen |
| `G701` | App | 8.1 Cửa hàng Tổng hợp, Vé (Ticket) & Lịch sử Point/Coin | Point Purchase Sub-screen (App) |
| `G702` | App | 8.1 Cửa hàng Tổng hợp, Vé (Ticket) & Lịch sử Point/Coin | Point Purchase Sub-screen (Web) |
| `I099` | App | 9.1 Vào phòng Live, Chế độ phòng & Khóa Familia/Soldier | (Viewer) LiveStream - Stanby |
| `I100` | App | 9.1 Vào phòng Live, Chế độ phòng & Khóa Familia/Soldier | (Viewer) LiveStream - Normal |
| `I1011` | App | 9.3 Tương tác Khán giả (Chat, Whisper, Profile, Danh sách Listener) | (Viewer) LiveStream - Bottom Modal - User Profile |
| `I1012` | App | 9.3 Tương tác Khán giả (Chat, Whisper, Profile, Danh sách Listener) | (Viewer) LiveStream - Bottom Modal - Streamer Profile |
| `I1013` | App | 9.3 Tương tác Khán giả (Chat, Whisper, Profile, Danh sách Listener) | (Viewer) LiveStream - Comment Option |
| `I1014` | App | 9.3 Tương tác Khán giả (Chat, Whisper, Profile, Danh sách Listener) | (Viewer) LiveStream - Screen Option |
| `I1021` | App | 9.5 Hộp Kho báu (Treasure Box) | (Viewer) LiveStream - Treasure Box Details |
| `I1022` | App | 9.5 Hộp Kho báu (Treasure Box) | (Viewer) LiveStream - Treasure Box Send History |
| `I1023` | App | 9.5 Hộp Kho báu (Treasure Box) | (Viewer) LiveStream - Treasure Box Customization |
| `I1024` | App | 9.5 Hộp Kho báu (Treasure Box) | (Viewer) LiveStream - List of Treasure Boxes to Open |
| `I1024` | App | 9.5 Hộp Kho báu (Treasure Box) | (Viewer) LiveStream - Treasure Box Opening |
| `I1025` | App | 9.5 Hộp Kho báu (Treasure Box) | (Viewer) LiveStream - Treasure Box Opening Results |
| `I1026` | App | 9.5 Hộp Kho báu (Treasure Box) | (Viewer) LiveStream - List of Users Winning from Treasure Boxes |
| `I103` | App | 9.3 Tương tác Khán giả (Chat, Whisper, Profile, Danh sách Listener) | (Viewer) LiveStream - Listener List |
| `I104` | App | 9.1 Vào phòng Live, Chế độ phòng & Khóa Familia/Soldier | (Viewer) LiveStream - Soldier Level 1 |
| `I104` | App | 9.1 Vào phòng Live, Chế độ phòng & Khóa Familia/Soldier | (Viewer) LiveStream - Soldier Level 2 |
| `I202` | App | 9.1 Vào phòng Live, Chế độ phòng & Khóa Familia/Soldier | (Viewer) LiveStream - Familia Lock |
| `I203` | App | 9.1 Vào phòng Live, Chế độ phòng & Khóa Familia/Soldier | (Viewer) LiveStream - Familia |
| `I301` | App | 9.2 Chế độ 2-Shot (Đăng ký, Phòng riêng, Khóa, Gia hạn & Kết nối lại) | Request Live2Shot modal |
| `I301` | App | 9.2 Chế độ 2-Shot (Đăng ký, Phòng riêng, Khóa, Gia hạn & Kết nối lại) | Request Live2Shot modal comfirm |
| `I302` | App | 9.2 Chế độ 2-Shot (Đăng ký, Phòng riêng, Khóa, Gia hạn & Kết nối lại) | (Viewer) LiveStream - 2 shot Lock |
| `I303` | App | 9.2 Chế độ 2-Shot (Đăng ký, Phòng riêng, Khóa, Gia hạn & Kết nối lại) | (Viewer) LiveStream - 2 shot |
| `I303` | App | 9.2 Chế độ 2-Shot (Đăng ký, Phòng riêng, Khóa, Gia hạn & Kết nối lại) | (Viewer) LiveStream - End 2shot, Confirm |
| `I3031` | App | 9.2 Chế độ 2-Shot (Đăng ký, Phòng riêng, Khóa, Gia hạn & Kết nối lại) | (Viewer) LiveStream - 2 shot - Xử lý kết nối lại livestream 2shot |
| `I304` | App | 9.2 Chế độ 2-Shot (Đăng ký, Phòng riêng, Khóa, Gia hạn & Kết nối lại) | (Viewer) LiveStream - Extend Live 2 Shot |
| `I304` | App | 9.2 Chế độ 2-Shot (Đăng ký, Phòng riêng, Khóa, Gia hạn & Kết nối lại) | (Viewer) LiveStream - Extend Live 2 Shot |
| `I305` | App | 9.2 Chế độ 2-Shot (Đăng ký, Phòng riêng, Khóa, Gia hạn & Kết nối lại) | (Viewer) LiveStream - Change to 2 shot Lock |
| `I306` | App | 9.2 Chế độ 2-Shot (Đăng ký, Phòng riêng, Khóa, Gia hạn & Kết nối lại) | (Viewer) LiveStream - Board Cast |
| `I402` | App | 9.3 Tương tác Khán giả (Chat, Whisper, Profile, Danh sách Listener) | (Viewer) LiveStream - Normal - Whisper chat |
| `I501` | App | 9.6 Karaoke Khán giả (Tìm kiếm, Yêu cầu bài hát & Chấm điểm) | (Viewer) LiveStream - Karaoke |
| `I502` | App | 9.6 Karaoke Khán giả (Tìm kiếm, Yêu cầu bài hát & Chấm điểm) | (Viewer) LiveStream - Karaoke - Setting |
| `I5031` | App | 9.6 Karaoke Khán giả (Tìm kiếm, Yêu cầu bài hát & Chấm điểm) | Viewer - Search song - Keyword |
| `I5032` | App | 9.6 Karaoke Khán giả (Tìm kiếm, Yêu cầu bài hát & Chấm điểm) | Viewer - Search song - popular |
| `I5033` | App | 9.6 Karaoke Khán giả (Tìm kiếm, Yêu cầu bài hát & Chấm điểm) | Viewer - Search song - Era |
| `I5034` | App | 9.6 Karaoke Khán giả (Tìm kiếm, Yêu cầu bài hát & Chấm điểm) | Viewer - Search song - Song Detail |
| `I5041` | App | 9.6 Karaoke Khán giả (Tìm kiếm, Yêu cầu bài hát & Chấm điểm) | Viewer - Search Artirst |
| `I5042` | App | 9.6 Karaoke Khán giả (Tìm kiếm, Yêu cầu bài hát & Chấm điểm) | Viewer - Search song - artirst - song list |
| `I5051` | App | 9.6 Karaoke Khán giả (Tìm kiếm, Yêu cầu bài hát & Chấm điểm) | Viewer - Favourite Artist List |
| `I5052` | App | 9.6 Karaoke Khán giả (Tìm kiếm, Yêu cầu bài hát & Chấm điểm) | Viewer - Favourite Song List |
| `I507` | App | 9.6 Karaoke Khán giả (Tìm kiếm, Yêu cầu bài hát & Chấm điểm) | Viewer - Sing history |
| `I508` | App | 9.6 Karaoke Khán giả (Tìm kiếm, Yêu cầu bài hát & Chấm điểm) | Viewer - Karaoke Scoring |
| `I509` | App | 9.6 Karaoke Khán giả (Tìm kiếm, Yêu cầu bài hát & Chấm điểm) | Viewer - Song request |
| `I600` | App | 9.4 Quà tặng, Gift Gacha & Hiệu ứng Quà cao cấp | (Viewer) LiveStream - Normal - Gift List |
| `I601` | App | 9.4 Quà tặng, Gift Gacha & Hiệu ứng Quà cao cấp | (Viewer) LiveStream - Normal - High-Value Gift Animation Mode |
| `I700` | App | 9.4 Quà tặng, Gift Gacha & Hiệu ứng Quà cao cấp | (Viewer) LiveStream - Normal - Gift Gacha |
| `I701` | App | 9.4 Quà tặng, Gift Gacha & Hiệu ứng Quà cao cấp | (Viewer) LiveStream - Normal - Gift Gacha Confirm |
| `I800` | App | 9.7 Cài đặt trong Phòng Live & Picture-in-Picture (PiP) | (Viewer) LiveStream - Livestream Settingf |
| `I802` | App | 9.7 Cài đặt trong Phòng Live & Picture-in-Picture (PiP) | (Viewer) LiveStream - Livestream Setting - Microphone Volume |
| `I803` | App | 9.7 Cài đặt trong Phòng Live & Picture-in-Picture (PiP) | (Viewer) LiveStream - Livestream Setting - Incoming Volume |
| `I804` | App | 9.7 Cài đặt trong Phòng Live & Picture-in-Picture (PiP) | (Viewer) LiveStream - Livestream Setting - Announcement |
| `I8041` | App | 9.7 Cài đặt trong Phòng Live & Picture-in-Picture (PiP) | (Viewer) LiveStream - Livestream Setting - Announcement Detail - Webview |
| `I8042` | App | 6.1 Thông báo Hệ thống, Hoạt động & Push Notification | Announcement Detail WEB |
| `I805` | App | 9.7 Cài đặt trong Phòng Live & Picture-in-Picture (PiP) | (Viewer) LiveStream - Livestream Setting - Graphics |
| `K000` | App | 11.1 Hồ sơ Cá nhân (My Page Core, Edit, Rank & Danh hiệu) | My Page |
| `K001` | App | 11.1 Hồ sơ Cá nhân (My Page Core, Edit, Rank & Danh hiệu) | Màn hình Xem ảnh |
| `K010` | App | 11.10 Karaoke Cá nhân & Báo cáo Bài hát đã sử dụng (ACRCloud) | My Page - Karaoke |
| `K011` | App | 11.10 Karaoke Cá nhân & Báo cáo Bài hát đã sử dụng (ACRCloud) | My Page - Karaoke Sing History |
| `K0121` | App | 11.10 Karaoke Cá nhân & Báo cáo Bài hát đã sử dụng (ACRCloud) | My Page - Search song - keyword |
| `K0122` | App | 11.10 Karaoke Cá nhân & Báo cáo Bài hát đã sử dụng (ACRCloud) | My Page - Search song - Popular |
| `K0123` | App | 11.10 Karaoke Cá nhân & Báo cáo Bài hát đã sử dụng (ACRCloud) | My Page - Search song - Era |
| `K0124` | App | 11.10 Karaoke Cá nhân & Báo cáo Bài hát đã sử dụng (ACRCloud) | My Page - Song detail |
| `K0131` | App | 11.10 Karaoke Cá nhân & Báo cáo Bài hát đã sử dụng (ACRCloud) | My Page - Search Artist |
| `K0132` | App | 11.10 Karaoke Cá nhân & Báo cáo Bài hát đã sử dụng (ACRCloud) | My Page - Search Artist - Artist song list |
| `K0141` | App | 11.10 Karaoke Cá nhân & Báo cáo Bài hát đã sử dụng (ACRCloud) | My Page - Favourite Airtist List |
| `K0142` | App | 11.10 Karaoke Cá nhân & Báo cáo Bài hát đã sử dụng (ACRCloud) | My Page - Favourite Song List |
| `K100` | App | 11.2 Cài đặt Tài khoản, SĐT, Liên kết SNS, eKYC & Block | My Page - Settings |
| `K202` | App | 11.2 Cài đặt Tài khoản, SĐT, Liên kết SNS, eKYC & Block | My Page - Settings - Account |
| `K202` | App | 11.2 Cài đặt Tài khoản, SĐT, Liên kết SNS, eKYC & Block | My Page - Settings - Account - Facebook |
| `K2021` | App | 11.2 Cài đặt Tài khoản, SĐT, Liên kết SNS, eKYC & Block | Logout |
| `K2022` | Admin | 3.1 Hồ sơ Người dùng, Xác thực eKYC & Xóa tài khoản | Delete ACCOUNT ADMIN |
| `K2022` | App | 11.2 Cài đặt Tài khoản, SĐT, Liên kết SNS, eKYC & Block | Delete ACCOUNT |
| `K20241` | App | 11.2 Cài đặt Tài khoản, SĐT, Liên kết SNS, eKYC & Block | SNS Un-connect |
| `K20242` | App | 11.2 Cài đặt Tài khoản, SĐT, Liên kết SNS, eKYC & Block | SNS can not Un-connect |
| `K2025` | App | 11.2 Cài đặt Tài khoản, SĐT, Liên kết SNS, eKYC & Block | Phone - Code |
| `K2025` | App | 11.2 Cài đặt Tài khoản, SĐT, Liên kết SNS, eKYC & Block | Phone - Country select |
| `K2025` | App | 11.2 Cài đặt Tài khoản, SĐT, Liên kết SNS, eKYC & Block | Phone SETTING |
| `K203` | App | 11.3 Liên kết Agency (Tham gia / Rời khỏi Agency) | My Page - Settings - Account -  Agency - Exit |
| `K203` | App | 11.3 Liên kết Agency (Tham gia / Rời khỏi Agency) | My Page - Settings - Account -  Agency - Register |
| `K204` | App | 11.4 Cài đặt Thông báo Đẩy (Push Notification Settings) | Push Noti |
| `K2041` | App | 11.4 Cài đặt Thông báo Đẩy (Push Notification Settings) | Push Noti - Follow user setting |
| `K2042` | App | 11.4 Cài đặt Thông báo Đẩy (Push Notification Settings) | Push Noti - Follow user setting all |
| `K2043` | App | 11.4 Cài đặt Thông báo Đẩy (Push Notification Settings) | Push Noti - Follow user setting all - confirm |
| `K2044` | App | 11.4 Cài đặt Thông báo Đẩy (Push Notification Settings) | Push Noti - Follow user setting - by user |
| `K205` | App | 11.2 Cài đặt Tài khoản, SĐT, Liên kết SNS, eKYC & Block | My Page - Settings - Ekyc |
| `K206` | App | 11.2 Cài đặt Tài khoản, SĐT, Liên kết SNS, eKYC & Block | Public SNS/Contact |
| `K206` | App | 11.2 Cài đặt Tài khoản, SĐT, Liên kết SNS, eKYC & Block | Public SNS/Contact - Facebook |
| `K207` | App | 11.2 Cài đặt Tài khoản, SĐT, Liên kết SNS, eKYC & Block | Block list và logic Block |
| `K208` | App | 11.5 Kết nối Xã hội, Familia, Soldier & Quyền Nhắn tin | About Surreal Doll |
| `K208` | App | 11.5 Kết nối Xã hội, Familia, Soldier & Quyền Nhắn tin | List of Sponsors |
| `K209-New` | App | 11.10 Karaoke Cá nhân & Báo cáo Bài hát đã sử dụng (ACRCloud) | ACRCLOUD - App  My Profile_Report of Used Songs |
| `K209-New` | App | 11.10 Karaoke Cá nhân & Báo cáo Bài hát đã sử dụng (ACRCloud) | My Profile_Create New Report of Used Songs |
| `K209-New` | App | 11.10 Karaoke Cá nhân & Báo cáo Bài hát đã sử dụng (ACRCloud) | My Profile_Edit Report of Used Songs |
| `K209-New` | App | 11.10 Karaoke Cá nhân & Báo cáo Bài hát đã sử dụng (ACRCloud) | My Profile_View Report of Used Songs |
| `K3011` | App | 11.5 Kết nối Xã hội, Familia, Soldier & Quyền Nhắn tin | My Page - Dolls |
| `K3012` | App | 11.5 Kết nối Xã hội, Familia, Soldier & Quyền Nhắn tin | My Page - Soilder Level |
| `K302` | App | 11.5 Kết nối Xã hội, Familia, Soldier & Quyền Nhắn tin | My Page - Joined Familia |
| `K400` | App | 11.5 Kết nối Xã hội, Familia, Soldier & Quyền Nhắn tin | My Page - Message Access |
| `K500` | App | 11.1 Hồ sơ Cá nhân (My Page Core, Edit, Rank & Danh hiệu) | My Page - List of Titles |
| `K601` | App | 11.6 Quản lý GOLD, Đổi Point & Lịch Thưởng (Reward Calendar) | My Page - GOLD |
| `K6012` | App | 11.6 Quản lý GOLD, Đổi Point & Lịch Thưởng (Reward Calendar) | My Page - GOLD to POINT |
| `K6013` | App | 11.6 Quản lý GOLD, Đổi Point & Lịch Thưởng (Reward Calendar) | My Page - GOLD to POINT History |
| `K602` | App | 11.6 Quản lý GOLD, Đổi Point & Lịch Thưởng (Reward Calendar) | My Page - Reward Calendar |
| `K701` | App | 11.5 Kết nối Xã hội, Familia, Soldier & Quyền Nhắn tin | Familia Member |
| `K702` | App | 11.5 Kết nối Xã hội, Familia, Soldier & Quyền Nhắn tin | Follower/Following |
| `K800` | App | 11.1 Hồ sơ Cá nhân (My Page Core, Edit, Rank & Danh hiệu) | Edit DOB |
| `K800` | App | 11.1 Hồ sơ Cá nhân (My Page Core, Edit, Rank & Danh hiệu) | Edit Profile |
| `K801` | App | 11.1 Hồ sơ Cá nhân (My Page Core, Edit, Rank & Danh hiệu) | Upload Profile picture |
| `K802` | App | 11.1 Hồ sơ Cá nhân (My Page Core, Edit, Rank & Danh hiệu) | Upload Cover picture |
| `K901` | App | 11.8 Thống kê LIVE, Bảng Xếp hạng & Nhật ký Tương tác | My Page - Dolls Ranking |
| `K902` | App | 11.8 Thống kê LIVE, Bảng Xếp hạng & Nhật ký Tương tác | My Page - Gifter Ranking |
| `K903` | App | 11.8 Thống kê LIVE, Bảng Xếp hạng & Nhật ký Tương tác | My Page - Likes |
| `K904` | App | 11.8 Thống kê LIVE, Bảng Xếp hạng & Nhật ký Tương tác | My Page - Keeps |
| `K9051` | App | 11.9 Quản lý Video Lưu trữ Cá nhân (My Archive) | My Page - Archive list (ko cho DL video có gắn karaoke) |
| `K9052` | App | 11.9 Quản lý Video Lưu trữ Cá nhân (My Archive) | My Page - Archive detail |
| `K9053` | App | 11.9 Quản lý Video Lưu trữ Cá nhân (My Archive) | My Page - Archive Setting |
| `K9054` | App | 11.9 Quản lý Video Lưu trữ Cá nhân (My Archive) | My Page - Archive Option |
| `K906` | App | 11.7 Tài khoản Nhận tiền & Yêu cầu Rút tiền (Payout) | My Profile _ Payout Account Linkage |
| `K9061` | App | 11.7 Tài khoản Nhận tiền & Yêu cầu Rút tiền (Payout) | My Profile _ Payout Account Preview |
| `K9062` | App | 11.7 Tài khoản Nhận tiền & Yêu cầu Rút tiền (Payout) | My Profile _ Payout Account OTP code |
| `K9063` | App | 11.7 Tài khoản Nhận tiền & Yêu cầu Rút tiền (Payout) | My Profile _ Payout Account Confirmation |
| `K9064` | App | 11.7 Tài khoản Nhận tiền & Yêu cầu Rút tiền (Payout) | My Profile _ Payout History - all |
| `K9065` | App | 11.7 Tài khoản Nhận tiền & Yêu cầu Rút tiền (Payout) | My Profile _ Instant Payout Request |
| `K9066` | App | 11.7 Tài khoản Nhận tiền & Yêu cầu Rút tiền (Payout) | My Profile _Payout History - sucess |
| `K9071` | App | 11.8 Thống kê LIVE, Bảng Xếp hạng & Nhật ký Tương tác | My Page - LIVE Analysis Overview |
| `K9072` | App | 11.8 Thống kê LIVE, Bảng Xếp hạng & Nhật ký Tương tác | My Page - LIVE Analysis Overview: Calendar Selector Screen |
| `K9073` | App | 11.8 Thống kê LIVE, Bảng Xếp hạng & Nhật ký Tương tác | My Page - LIVE Analysis List |
| `K9074` | App | 11.8 Thống kê LIVE, Bảng Xếp hạng & Nhật ký Tương tác | My Page - LIVE Analysis Details |
| `K9075` | App | 11.8 Thống kê LIVE, Bảng Xếp hạng & Nhật ký Tương tác | My Page - LIVE Viewer List |
| `K908` | App | 11.1 Hồ sơ Cá nhân (My Page Core, Edit, Rank & Danh hiệu) | My Page - Rank |
| `K909` | App | 11.8 Thống kê LIVE, Bảng Xếp hạng & Nhật ký Tương tác | My Page - Gift Gacha Sender List |
| `K9091A` | App | 11.8 Thống kê LIVE, Bảng Xếp hạng & Nhật ký Tương tác | My Page - Gift Sender List |
| `K9092` | App | 11.8 Thống kê LIVE, Bảng Xếp hạng & Nhật ký Tương tác | My Page - 2 Shot History |
| `K9093` | App | 11.8 Thống kê LIVE, Bảng Xếp hạng & Nhật ký Tương tác | My Page - Treasure Chest Sender List |
| `K9094` | App | 11.8 Thống kê LIVE, Bảng Xếp hạng & Nhật ký Tương tác | My Page - New follower list |
| `K9095` | App | 11.8 Thống kê LIVE, Bảng Xếp hạng & Nhật ký Tương tác | My Page - New familia member list |
| `K9096` | App | 11.8 Thống kê LIVE, Bảng Xếp hạng & Nhật ký Tương tác | My Page - Whisper sender list |
| `L100` | App | 12.1 Trang chủ Familia, Khám phá & Tìm kiếm | Familia_Home |
| `L1001` | App | 12.1 Trang chủ Familia, Khám phá & Tìm kiếm | My Familia_Home_New Posts from Joined Familias |
| `L1002` | App | 12.1 Trang chủ Familia, Khám phá & Tìm kiếm | My Familia_Home_Featured New Familias |
| `L1003` | App | 12.1 Trang chủ Familia, Khám phá & Tìm kiếm | My Familia_Home_Featured New Posts |
| `L1004` | App | 12.1 Trang chủ Familia, Khám phá & Tìm kiếm | My Familia_Home_Post Daily Ranking |
| `L1021` | App | 12.1 Trang chủ Familia, Khám phá & Tìm kiếm | Familia Search - Famila |
| `L1022` | App | 12.1 Trang chủ Familia, Khám phá & Tìm kiếm | Familia Search - Post |
| `L1023` | App | 12.1 Trang chủ Familia, Khám phá & Tìm kiếm | Familia Search - Tag |
| `L200` | App | 12.5 Xem Familia Người khác, Donate Yell & Trình phát Bài đăng | Other User’s Familia_Introduction |
| `L201` | App | 12.5 Xem Familia Người khác, Donate Yell & Trình phát Bài đăng | Other User’s Familia_Donate Subscreen |
| `L202` | App | 12.5 Xem Familia Người khác, Donate Yell & Trình phát Bài đăng | Other User’s Familia_Post List |
| `L203` | App | 12.5 Xem Familia Người khác, Donate Yell & Trình phát Bài đăng | Other User’s Familia_Post Details |
| `L2041` | App | 12.5 Xem Familia Người khác, Donate Yell & Trình phát Bài đăng | Other’s Familia_Post Details (Individual) |
| `L2042` | App | 12.5 Xem Familia Người khác, Donate Yell & Trình phát Bài đăng | Other’s Familia_Post Details (Individual)_Options Subscreen |
| `L2043` | App | 12.5 Xem Familia Người khác, Donate Yell & Trình phát Bài đăng | Other’s Familia_Post Details (Individual)_Options Subscreen_Speed |
| `L2044` | App | 12.5 Xem Familia Người khác, Donate Yell & Trình phát Bài đăng | Other’s Familia_Post Details (Individual)_Options Subscreen_Subtitle |
| `L205` | App | 12.6 Tham gia Class & Mua Backnumber Familia Người khác | Other's Familia - Class List |
| `L206` | App | 12.6 Tham gia Class & Mua Backnumber Familia Người khác | Other's Familia - Join Class - APP |
| `L207` | App | 12.6 Tham gia Class & Mua Backnumber Familia Người khác | Other’s Familia - Class Change |
| `L208` | App | 12.6 Tham gia Class & Mua Backnumber Familia Người khác | Other’s Familia - Cancel subcribe |
| `L209` | App | 12.6 Tham gia Class & Mua Backnumber Familia Người khác | Other's Familia - Backnumber List |
| `L210` | App | 12.6 Tham gia Class & Mua Backnumber Familia Người khác | Other's Familia - Backnumber Purchase |
| `L300` | App | 12.2 Quản lý Giới thiệu & Mục tiêu Yell của My Familia | My Familia Intro |
| `L301` | App | 12.2 Quản lý Giới thiệu & Mục tiêu Yell của My Familia | My Familia Intro section |
| `L302` | App | 12.2 Quản lý Giới thiệu & Mục tiêu Yell của My Familia | My Familia - Intro Edit |
| `L303` | App | 12.2 Quản lý Giới thiệu & Mục tiêu Yell của My Familia | My Familia - Intro Edit - Modal up file |
| `L3041` | App | 12.2 Quản lý Giới thiệu & Mục tiêu Yell của My Familia | My Familia - Target List |
| `L3042` | App | 12.2 Quản lý Giới thiệu & Mục tiêu Yell của My Familia | My Familia - Create Target |
| `L3043` | App | 12.2 Quản lý Giới thiệu & Mục tiêu Yell của My Familia | My Familia - Update Target |
| `L3044` | App | 12.2 Quản lý Giới thiệu & Mục tiêu Yell của My Familia | My Familia - Yell Participants List |
| `L401` | App | 12.3 Quản lý Bài đăng, Tag & Bình luận của My Familia | My Familia - Tag |
| `L402` | App | 12.3 Quản lý Bài đăng, Tag & Bình luận của My Familia | My Familia - Post List |
| `L403` | App | 12.3 Quản lý Bài đăng, Tag & Bình luận của My Familia | My Familia - Post Create |
| `L4041` | App | 12.3 Quản lý Bài đăng, Tag & Bình luận của My Familia | My Familia - Post Create - Post Content Create |
| `L4042` | App | 12.3 Quản lý Bài đăng, Tag & Bình luận của My Familia | My Familia - Post Create - Post Content Create - Modal upload content |
| `L405` | App | 12.3 Quản lý Bài đăng, Tag & Bình luận của My Familia | My Familia - Post Detail |
| `L406` | App | 12.3 Quản lý Bài đăng, Tag & Bình luận của My Familia | My Familia - Post Edit |
| `L4061` | App | 12.3 Quản lý Bài đăng, Tag & Bình luận của My Familia | My Familia - Post Edit - Post Content Update, Delete |
| `L407` | App | 12.3 Quản lý Bài đăng, Tag & Bình luận của My Familia | Post Comment |
| `L501` | App | 12.4 Quản lý Hạng thành viên (Class), Stamp & Backnumber của tôi | My Familia - Class List |
| `L502` | App | 12.4 Quản lý Hạng thành viên (Class), Stamp & Backnumber của tôi | My Familia - Add New Class |
| `L503` | App | 12.4 Quản lý Hạng thành viên (Class), Stamp & Backnumber của tôi | My Familia - Edit Class |
| `L504` | App | 12.4 Quản lý Hạng thành viên (Class), Stamp & Backnumber của tôi | My Familia -  Add Stamp |
| `L600` | App | 12.4 Quản lý Hạng thành viên (Class), Stamp & Backnumber của tôi | My Familia - Backnumber list |
| `M0011` | App | 10.1 Thiết lập Model 3D, Trang phục & Hình nền Ban đầu (Initial Setup) | Streaming Setup – Initial – Model Select |
| `M00111` | App | 10.1 Thiết lập Model 3D, Trang phục & Hình nền Ban đầu (Initial Setup) | Streaming Setup – Initial – Model Settings – Head |
| `M00112` | App | 10.1 Thiết lập Model 3D, Trang phục & Hình nền Ban đầu (Initial Setup) | Streaming Setup – Initial – Model Settings – Appearance |
| `M00113` | App | 10.1 Thiết lập Model 3D, Trang phục & Hình nền Ban đầu (Initial Setup) | Streaming Setup – Initial – Model Settings – Appearance Settings Sub-screen |
| `M00114` | App | 10.1 Thiết lập Model 3D, Trang phục & Hình nền Ban đầu (Initial Setup) | Streaming Setup – Initial – Model Settings – Emotion Expression Sub-screen |
| `M0012` | App | 10.1 Thiết lập Model 3D, Trang phục & Hình nền Ban đầu (Initial Setup) | Streaming Setup – Initial – Costume Settings |
| `M00121` | App | 10.1 Thiết lập Model 3D, Trang phục & Hình nền Ban đầu (Initial Setup) | Streaming Setup – Initial – Costume Settings – Custom Sub-screen |
| `M00131` | App | 10.1 Thiết lập Model 3D, Trang phục & Hình nền Ban đầu (Initial Setup) | Background Setting - Lần đầu tiên - Background |
| `M100` | App | 10.2 Chuẩn bị trước khi Phát sóng (Prepare to Stream) | App Model - Chọn độ phân giải |
| `M100_final` | App | 10.2 Chuẩn bị trước khi Phát sóng (Prepare to Stream) | Prepare to stream TOP |
| `M1011` | App | 10.2 Chuẩn bị trước khi Phát sóng (Prepare to Stream) | Prepare to stream TOP - Wishlist - Add wish gift |
| `M1011` | App | 10.2 Chuẩn bị trước khi Phát sóng (Prepare to Stream) | Prepare to stream TOP - Wishlist - Select gift |
| `M1012` | App | 10.2 Chuẩn bị trước khi Phát sóng (Prepare to Stream) | Prepare to stream TOP - Livestream Tocpic |
| `M102` | App | 10.2 Chuẩn bị trước khi Phát sóng (Prepare to Stream) | Prepare to stream TOP - Live2shot invite Check |
| `M199` | App | 10.3 Điều hành Phòng Live & Các Chế độ Phát (Normal/Test/Familia/Broadcast/PiP) | (Streamer View) Now Streaming - TEST |
| `M200` | App | 10.3 Điều hành Phòng Live & Các Chế độ Phát (Normal/Test/Familia/Broadcast/PiP) | (Streamer View) Now Streaming - Normal |
| `M2001` | App | 10.3 Điều hành Phòng Live & Các Chế độ Phát (Normal/Test/Familia/Broadcast/PiP) | (Streamer View) Now Streaming - Screen Option |
| `M201` | App | 10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live | (Streamer View) Now Streaming - Comment Whisper - Reply |
| `M203` | App | 10.3 Điều hành Phòng Live & Các Chế độ Phát (Normal/Test/Familia/Broadcast/PiP) | (Streamer View) Now Streaming - Lich sử whisper |
| `M203` | App | 10.3 Điều hành Phòng Live & Các Chế độ Phát (Normal/Test/Familia/Broadcast/PiP) | (Streamer View) Now Streaming - Listener List |
| `M205` | App | 10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live | (Streamer View) Now Streaming - Setting in livestream |
| `M205` | App | 10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live | (Streamer View) Now Streaming - Setting in livestream - chuyển sang familia |
| `M20501` | App | 10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live | (Streamer View) Now Streaming - Setting in livestream - Appearance |
| `M20502` | App | 10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live | (Streamer View) Now Streaming - Setting in livestreams - Costume |
| `M20504` | App | 10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live | (Streamer View) Now Streaming - Setting in livestream - Change Background |
| `M20506` | App | 10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live | (Streamer View) Now Streaming - Setting in livestream - Board |
| `M20507` | App | 10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live | (Streamer View) Now Streaming - Setting in livestream - Update Wishlist |
| `M20510` | App | 10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live | (Streamer View) Now Streaming - Setting in livestream - Livestream Micro |
| `M20511` | App | 10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live | (Streamer View) Now Streaming - Setting in livestream - Mic Echo |
| `M20512` | App | 10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live | (Streamer View) Now Streaming - Setting in livestream - Incoming Volume |
| `M20513` | App | 10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live | (Streamer View) Now Streaming - Setting in livestream - Voice Changer |
| `M20514` | App | 10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live | (Streamer View) Now Streaming - Setting in livestream - BGM |
| `M20515` | App | 10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live | (Streamer View) Now Streaming - Setting in livestream - Announcement |
| `M20516` | App | 10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live | (Streamer View) Now Streaming - Setting in livestream - Graphics |
| `M20518` | App | 10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live | (Streamer View) Now Streaming - Setting in livestream - Livestream sound |
| `M2055` | App | 10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live | (Streamer View) Now Streaming - Setting in livestream - Change Topic |
| `M206` | App | 10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live | (Streamer View) Now Streaming - Setting in livestream - Share Livestream |
| `M2061` | App | 10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live | Emote |
| `M2062` | App | 10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live | Biểu cảm |
| `M2071` | App | 10.3 Điều hành Phòng Live & Các Chế độ Phát (Normal/Test/Familia/Broadcast/PiP) | (Streamer View) Now Streaming - Setting in livestream - xác nhận chuyển sang boardcast |
| `M2073` | App | 10.3 Điều hành Phòng Live & Các Chế độ Phát (Normal/Test/Familia/Broadcast/PiP) | (Streamer View) Now Streaming - Setting in livestream - chuyển sang boardcast |
| `M300` | App | 10.4 Quản lý 2-Shot phía Streamer (Approve, Reconnect, Extend) | (Streamer View) Now Streaming - 2shot |
| `M3001` | App | 10.4 Quản lý 2-Shot phía Streamer (Approve, Reconnect, Extend) | (Streamer View) Now Streaming - 2shot dở và quay lại |
| `M3002` | App | 10.4 Quản lý 2-Shot phía Streamer (Approve, Reconnect, Extend) | (Streamer View) Now Streaming - 2shotxử lý extend |
| `M302` | App | 10.4 Quản lý 2-Shot phía Streamer (Approve, Reconnect, Extend) | (Streamer View) Now Streaming - Danh sách request 2 shot |
| `M401` | App | 10.6 Karaoke Streamer & Đề xuất Bài hát mới | (Streamer View) Now Streaming - Mode Karaoke |
| `M402` | App | 10.6 Karaoke Streamer & Đề xuất Bài hát mới | (Streamer View) Now Streaming - Mode Karaoke - Karaoke Setting |
| `M403` | App | 10.6 Karaoke Streamer & Đề xuất Bài hát mới | (Streamer View) Now Streaming - Mode Karaoke - Song Request List |
| `M4041` | App | 10.6 Karaoke Streamer & Đề xuất Bài hát mới | (Streamer View) Now Streaming - Search song - keyword |
| `M4042` | App | 10.6 Karaoke Streamer & Đề xuất Bài hát mới | (Streamer View) Now Streaming - Search song - Popular |
| `M4043` | App | 10.6 Karaoke Streamer & Đề xuất Bài hát mới | (Streamer View) Now Streaming - Search song - Era |
| `M4044` | App | 10.6 Karaoke Streamer & Đề xuất Bài hát mới | (Streamer View) Now Streaming - Search song - Detail |
| `M4051` | App | 10.6 Karaoke Streamer & Đề xuất Bài hát mới | (Streamer View) Now Streaming - Search Artist |
| `M4052` | App | 10.6 Karaoke Streamer & Đề xuất Bài hát mới | (Streamer View) Now Streaming - Search Artist - Artist song list |
| `M4061` | App | 10.6 Karaoke Streamer & Đề xuất Bài hát mới | (Streamer View) Now Streaming - Favourite Airtist List |
| `M4062` | App | 10.6 Karaoke Streamer & Đề xuất Bài hát mới | (Streamer View) Now Streaming - Favourite Song List |
| `M4071` | App | 10.6 Karaoke Streamer & Đề xuất Bài hát mới | (Streamer View) Now Streaming - wish new song |
| `M4072` | App | 10.6 Karaoke Streamer & Đề xuất Bài hát mới | (Streamer View) Now Streaming - wish new song list |
| `M408` | App | 10.6 Karaoke Streamer & Đề xuất Bài hát mới | (Streamer View) Now Streaming - Sing History |
| `M409` | App | 10.6 Karaoke Streamer & Đề xuất Bài hát mới | (Streamer View) Now Streaming - Karaoke Scoring |
| `M500` | App | 10.3 Điều hành Phòng Live & Các Chế độ Phát (Normal/Test/Familia/Broadcast/PiP) | (Streamer View) Now Streaming - Familia mode |
| `OBS` | App | 10.7 Phát sóng qua OBS (OBS Normal / Familia / 2-Shot / Viewer) | OBS 2shot |
| `OBS` | App | 10.7 Phát sóng qua OBS (OBS Normal / Familia / 2-Shot / Viewer) | OBS Viewer All mode |
| `OBS` | App | 10.7 Phát sóng qua OBS (OBS Normal / Familia / 2-Shot / Viewer) | OBS thường, OBS Familia |
| `PIP streamer` | App | 10.3 Điều hành Phòng Live & Các Chế độ Phát (Normal/Test/Familia/Broadcast/PiP) | PIP cho streamer |