# TÀI LIỆU BÓC TÁCH ĐẶC TẢ KỸ THUẬT & LÀM RÕ YÊU CẦU (SPEC ANALYSIS & CLARIFICATION REPORT)
## Màn hình: AD100_Agency List / Search (Danh Sách & Tìm Kiếm Agency - 事務所一覧・検索)
### Phân hệ: Web Master Admin Portal (`AA000`) / Quản lý Agency (`AD` Module)
### Áp dụng: Quy chuẩn Trụ Cột 1 (`Universal_Rules/01_core_spec_analysis_rule.md`) & Master Policy (`GEMINI.md`)

---

## BẢNG THÔNG TIN TỔNG QUAN ĐẶC TẢ (SPECIFICATION METADATA)

| Thuộc tính | Chi tiết |
| :--- | :--- |
| **Mã màn hình** | `AD100` |
| **Tên màn hình** | `AD100_Agency List / Search` (事務所管理_事務所一覧・検索) |
| **Phân hệ / Module** | Master Admin Web (`AA000`) / Phân hệ Quản lý Agency (`AD` Module - 事務所管理) |
| **Người tạo Spec (Created by)** | `Ly` |
| **Ngày tạo (Created Date)** | July-14 (Cập nhật CR: 13/08/2026, 06/11/2025) |
| **Nguồn Spec Google Sheets** | [Google Spreadsheet - Tab AD100 (gid=1636466169)](https://docs.google.com/spreadsheets/d/1pxox5GcjOXwKadMnzOa765ptG2huPJSxCiWsrH0_h7Y/edit?gid=1636466169#gid=1636466169) |
| **Nguồn Tham chiếu Nghiệp vụ** | Tab `CommonSpec` (gid=170791648), `Common MSG` (gid=1080253487), `MSG` (gid=1862733901) |
| **Nguồn Thiết kế Figma** | [Figma AD100 (node-id=907-3689)](https://www.figma.com/design/r5RjkwIfMhChaq83OsBkf8/Admin-Layout---Spec-PDF?node-id=907-3689&t=CHjpqKXsbfmyHBR7-4) |
| **Luồng Điều hướng Vào** | Master Admin Menu Sidebar $\rightarrow$ Chọn `事務所管理` (Agency Management) $\rightarrow$ Mở `AD100` |
| **Luồng Điều hướng Ra** | • Click nút `新規登録` `[5]` $\rightarrow$ Mở `AD200`<br>• Click dòng / icon chi tiết `[14]` $\rightarrow$ Mở `AD301`<br>• Click cột `ライバー数` `[10]` $\rightarrow$ Mở danh sách Liver `AD302` tương ứng |
| **Ngôn ngữ hiển thị chính** | Tiếng Nhật (`JA`) |

---

## I. KẾT QUẢ QUÉT ĐẶC TẢ 2 BƯỚC BẮT BUỘC (2-PASS SCANNING PROTOCOL)

### 1. Pass 1 - Bóc Tách UI Controls Có `[No.]` (Item [1] đến [14])

| No. | Tên phần tử (Value JP) | Loại UI Control | Placeholder / Giá trị | Ràng buộc kỹ thuật & Nghiệp vụ (SRS & CR) |
| :---: | :--- | :--- | :--- | :--- |
| `[1]` | Bảng danh sách | Data Table | - | Hiển thị bảng danh sách các Agency theo layout Figma. |
| `[2]` | `事務所名・事務所ID` | Textbox Input | `事務所名・事務所ID` | • Nhập từ khóa tìm kiếm theo **CMR02**.<br>• Tìm kiếm đúng một phần (Partial match): Tên Agency (`name`).<br>• Tìm kiếm chính xác (Exact match): Mã Agency (`agency_code`) và System ID (`id`).<br>• Sắp xếp mặc định: Theo ngày cập nhật mới nhất $\rightarrow$ cũ nhất (`updated_at DESC`). |
| `[3]` | `ステータス` (Bộ lọc) | Pulldown Select | `全て` (Default) | • Gồm 3 tùy chọn: `全て` (Tất cả), `利用中` (Đang hoạt động), `停止中` (Tạm dừng).<br>• Chọn 1 trạng thái để lọc danh sách. |
| `[4]` | `検索` | Button (Primary) | `検索` | Gửi request tìm kiếm theo từ khóa và trạng thái. |
| `[4]` | `クリア` | Button (Secondary) | `クリア` | Xóa từ khóa, đưa dropdown về `全て`, tải lại dữ liệu mặc định ban đầu. |
| `[5]` | `新規登録` | Button (Primary) | `新規登録` | Điều hướng sang màn hình đăng ký tạo mới Agency `AD200`. |
| `[6]` | `ID` | Table Column | - | System ID do hệ thống tự sinh (`id`). |
| `[7]` | `事務所ID` | Table Column | - | Mã Agency do Admin tự định nghĩa khi tạo (`agency_code`). |
| `[8]` | `事務所名` | Table Column | - | Tên Agency kèm ảnh Logo đại diện. |
| `[9]` | `連絡先 オーナー名` | Table Column | - | Tên người đại diện liên hệ của Agency (`contact_name`). |
| `[10]` | `ライバー数` | Table Column | - | **CR 06/11/2025:** Tổng số user trực thuộc Agency (`member_count`).<br>• Chỉ gồm các user đã được accept vào Agency (status `所属済み`).<br>• Bao gồm cả status Active và Inactive.<br>• Không bao gồm user đã bị xóa hoặc đã rời Agency.<br>• Click vào số lượng sẽ điều hướng sang màn danh sách Liver tương ứng `AD302`. |
| `[10]` | `ポイント売上` | Table Column | - | **CR 06/11/2025:** Doanh thu Point mà các Liver trực thuộc kiếm được qua Livestream (Gift, 2shot, Whisper) và Familia (Donate GP Yell). |
| `[10]` | `ファミリア売上` | Table Column | - | **CR 06/11/2025:** Doanh thu Yên từ các gói Familia (Tham gia Class + Mua Backnumber trên App & Web). |
| `[10]` | `売上合計` | Table Column | - | **CR 06/11/2025:** Tổng doanh thu = `ポイント売上` + `ファミリア売上`. |
| `[11]` | `ステータス` | Table Column | - | Trạng thái Agency: `利用中` (Active) hoặc `停止中` (Inactive). |
| `[12]` | `作成日` | Table Column | - | Ngày tạo Agency theo format `YYYY/MM/DD`. Hỗ trợ sắp xếp Sort mới $\rightarrow$ cũ, cũ $\rightarrow$ mới. |
| `[13]` | `変更日` | Table Column | - | Ngày cập nhật thông tin gần nhất `YYYY/MM/DD`. Hỗ trợ sắp xếp Sort mới $\rightarrow$ cũ, cũ $\rightarrow$ mới. |
| `[14]` | Nút Chi tiết / Click dòng | Row Action | - | Điều hướng sang màn hình chi tiết `AD301`. |
| `[14]` | Nút Xóa | Row Action | - | **CR 13/08/2026 (QUAN TRỌNG):** ĐÃ BỎ nút xóa trên AD100. Hành động xóa chỉ được phép thực hiện bên trong trang chi tiết `AD301` sau khi xác nhận popup `MSG66`. |

---

### 2. Pass 2 - Quét Các Phần Tử & Logic Không Có `[No.]`

- **`[0] Screen Access & Lifecycle`:** Breadcrumbs: `＞ 事務所管理`. Đường dẫn URL: `/admin/agencies`. Phân trang theo **CMR01/CMR23** (10, 20, 50, 100 bản ghi/trang).
- **`[Common] Business Rules`:** Phân quyền Master Admin. Agency bị `停止中` vẫn hiển thị trong bảng nhưng bị làm xám (Grey out), vẫn click xem chi tiết `AD301` được.
- **`[Empty State]`:** Khi tìm kiếm không có kết quả $\rightarrow$ Hiển thị **`CMMSG47`** (`一致する検索結果はありません。`).
- **`[Error Handling]`:** Lỗi server báo **`CMMSG1`**, lỗi mạng báo **`CMMSG8`**.

---

## II. MA TRẬN LOGIC NGHIỆP VỤ & API SCOPE

### 1. Phân định API
- **In-Scope:** `POST /agency/` (Lấy danh sách phân trang kèm search: `q`, `status`, `page`, `items_per_page`, `sort_query`).
- **Out-of-Scope:** `DELETE /agency/{agency_id}/` (Đã chuyển vào `AD301`).

### 2. Bảng Q&A Làm Rõ Yêu Cầu

| No. | Control / Logic | Vấn đề chưa rõ | Câu hỏi làm rõ | Đề xuất Option A / Option B | Giả định tạm thời khi viết TC | Trạng thái |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| `Q1` | `[10] ライバー数` | Click vào số lượng Liver | Khi click vào số lượng Liver tại cột [10], hệ thống điều hướng sang AD302 với bộ lọc gì? | **Option A:** Điều hướng sang AD302 của đúng Agency đó với bộ lọc mặc định (`全ての所属状態`).<br>**Option B:** Điều hướng sang AD302 chỉ lọc các Liver đang ở trạng thái `所属済み`. | **Tạm giả định theo Option A** (Điều hướng sang AD302 với bộ lọc mặc định). | `Pending` |
| `Q2` | `[14] Bỏ nút Xóa` | Xóa trên danh sách AD100 | CR 13/08/2026 đã ghi chú bỏ nút Xóa trên AD100, xác nhận giao diện live không còn nút Xóa? | **Option A:** Hoàn toàn không hiển thị nút Xóa trên AD100.<br>**Option B:** Vẫn còn nút Xóa nhưng click hiện popup MSG66. | **Tạm giả định theo Option A** (Theo CR mới nhất: Bỏ nút xóa trên AD100). | `Pending` |
