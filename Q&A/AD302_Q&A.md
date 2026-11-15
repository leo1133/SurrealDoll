# TÀI LIỆU BÓC TÁCH ĐẶC TẢ KỸ THUẬT & LÀM RÕ YÊU CẦU (SPEC ANALYSIS & CLARIFICATION REPORT)
## Màn hình: AD302_Agency Streamer List (Danh Sách Liver Trực Thuộc Agency - 事務所詳細_ライバー一覧)
### Phân hệ: Web Master Admin Portal (`AA000`) / Quản lý Agency (`AD` Module)
### Áp dụng: Quy chuẩn Trụ Cột 1 (`Universal_Rules/01_core_spec_analysis_rule.md`) & Master Policy (`GEMINI.md`)

---

## BẢNG THÔNG TIN TỔNG QUAN ĐẶC TẢ (SPECIFICATION METADATA)

| Thuộc tính | Chi tiết |
| :--- | :--- |
| **Mã màn hình** | `AD302` |
| **Tên màn hình** | `AD302 Agency Manage - Agency Streamer List` (事務所詳細_ライバー一覧) |
| **Phân hệ / Module** | Master Admin Web (`AA000`) / Phân hệ Quản lý Agency (`AD` Module) |
| **Người tạo Spec (Created by)** | `Quynh Anh` |
| **Ngày tạo (Created Date)** | September-4 (Cập nhật CR: 13/10/2026, 11/11/2026) |
| **Nguồn Spec Google Sheets** | [Google Spreadsheet - Tab AD302 (gid=1019623612)](https://docs.google.com/spreadsheets/d/1pxox5GcjOXwKadMnzOa765ptG2huPJSxCiWsrH0_h7Y/edit?gid=1019623612#gid=1019623612) |
| **Nguồn Tham chiếu Nghiệp vụ** | Tab `CommonSpec` (CMR02, CMR14A), `Common MSG`, `MSG` |
| **Nguồn Thiết kế & Prototype** | • [Prototype AD302 Drive](https://drive.google.com/file/d/1t0kIlpEA6fvxcj9x6VPkhgzrEHSEAos6/view?usp=drive_link)<br>• [Frontend HTML AD302 Drive](https://drive.google.com/file/d/1lC68FExTLfbKGZS1ZuH4bIiyMFguPK5j/view?usp=drive_link)<br>• [Testcase Sheet AD302](https://docs.google.com/spreadsheets/d/1Bg_DHqqT86bp6gsuuoqdQ1ypqovu7Wt3yNJJClvqOs4/edit?gid=1265321952#gid=1265321952) |
| **Luồng Điều hướng Vào** | • Từ `AD100`: Click số lượng Liver tại cột `[10]`<br>• Từ `AD301` hoặc `AD303`: Click Tab `ライバー一覧` `[0]` |
| **Luồng Điều hướng Ra** | Click cột `詳細` `[33]` $\rightarrow$ Điều hướng sang màn hình quản lý chi tiết User `AE200` |
| **Ngôn ngữ hiển thị chính** | Tiếng Nhật (`JA`) |

---

## I. KẾT QUẢ QUÉT ĐẶC TẢ 2 BƯỚC BẮT BUỘC (2-PASS SCANNING PROTOCOL)

### 1. Pass 1 - Bóc Tách UI Controls Có `[No.]` (Item [0] đến [33])

| No. | Tên phần tử (Value JP) | Loại UI Control | Placeholder / Giá trị | Ràng buộc Validate & Nghiệp vụ (SRS & CR) |
| :---: | :--- | :--- | :--- | :--- |
| `[0]` | `ライバー一覧` | Tab Item | - | Tab thứ 2 của màn hình chi tiết Agency `AD300`. |
| `[1]` | Tìm kiếm từ khóa | Textbox Input | `ライバー名・ID` | Nhập từ khóa theo **CMR02**: Tìm kiếm đúng 1 phần theo username, tìm kiếm chính xác theo User System ID (`user_uid`). |
| `[2]` | `全ステータス` | Pulldown Select | `全ステータス` (Default) | Lọc theo trạng thái User: `全ステータス`, `利用中` (1), `停止中` (2), `退会済み` (3). |
| `[3]` | `全ての所属状態` | Pulldown Select | `全ての所属状態` (Default) | Lọc theo quan hệ với Agency: `全ての所属状態`, `申請中` (3), `所属済み` (1), `退所申請中` (5), `退所済み` (6). |
| `[4]` | `全て` (Loại Liver) | Pulldown Select | `全て` (Default) | Lọc theo loại hình Liver: `全て`, `Vライバー` (1), `2.5次元V` (2). |
| `[5]` | `クリア` | Button (Secondary) | `クリア` | Xóa bộ lọc về mặc định ban đầu. |
| `[6]` | `検索` | Button (Primary) | `検索` | Thực hiện tìm kiếm theo các điều kiện lọc. |
| `[7]` | Mở rộng / Thu gọn cột | Toggle Button | `»` / `«` | Ẩn/hiện 2 nhóm cột (Mặc định: Ẩn):<br>• Nhóm 1: `2ショット ~ エール` (cột 16-19).<br>• Nhóm 2: `通常配信時間 ~ OBS時間` (cột 23-28). Bấm `»` để mở rộng, bấm `«` để thu gọn. |
| `[8]` | `ID` | Table Column | - | User System ID (hỗ trợ sort tăng/giảm). |
| `[9]` | `ライバー名` | Table Column | - | Tên hiển thị của Liver (`user_name`). |
| `[10]` | `ライバー種類` | Table Column | - | Loại hình Liver: `Vライバー` hoặc `2.5次元V`. |
| `[11]` | `フォロー` | Table Column | - | Số lượt following (Sort tăng/giảm). |
| `[12]` | `フォロワー` | Table Column | - | Số lượt follower (Sort tăng/giảm). |
| `[13]` | `ファミリアメンバー` | Table Column | - | Số thành viên trong Familia của Liver (Sort tăng/giảm). |
| `[14]` | `いいね数` | Table Column | - | Tổng số lượt like nhận được (Sort tăng/giảm). |
| `[15]` | `ポイント売上` | Table Column | - | **CR 13/10/2026:** Doanh thu Point tích lũy toàn thời gian (All-time) = Cột [16] + [17] + [18] + [19]. **Không cộng điểm Gift Gacha**. Hỗ trợ sort tăng/giảm. |
| `[16]` | `2ショット` | Table Column | - | Doanh thu quy đổi từ vé 2shot đã sử dụng trong livestream (Nhóm 1). |
| `[17]` | `ギフト` | Table Column | - | Doanh thu từ Gift thường và Gift cao cấp (Nhóm 1). |
| `[18]` | `ウィスパー` | Table Column | - | Doanh thu thu được từ tin nhắn Whisper trong live (Nhóm 1). |
| `[19]` | `エール` | Table Column | - | Doanh thu thu được từ Yell / Donate GP (Nhóm 1). |
| `[20]` | `ファミリア売上` | Table Column | - | Doanh thu Yên all-time từ gói tham gia Class và mua Backnumber. Sort tăng/giảm. |
| `[21]` | `合計売上` | Table Column | - | Tổng doanh thu All-time = `ポイント売上` [15] + `ファミリア売上` [20]. |
| `[22]` | `合計配信時間` | Table Column | - | Tổng thời lượng livestream (định dạng `hh:mm:ss`, sortable). |
| `[23]` | `通常配信時間` | Table Column | - | Thời lượng live Thường (Nhóm 2). |
| `[24]` | `2ショット時間` | Table Column | - | Thời lượng live 2Shot 1-1 (Nhóm 2). |
| `[25]` | `ファミ限時間` | Table Column | - | Thời lượng live giới hạn thành viên Familia (Nhóm 2). |
| `[26]` | `カラオケ時間` | Table Column | - | Thời lượng live Karaoke (Nhóm 2). |
| `[27]` | `BC時間` | Table Column | - | Thời lượng live Broadcast (Nhóm 2). |
| `[28]` | `OBS時間` | Table Column | - | Thời lượng live qua phần mềm OBS (Nhóm 2). |
| `[29]` | `ステータス` | Table Column | - | Trạng thái tài khoản Liver: `利用中`, `停止中`, `退会済み`. |
| `[30]` | `事務所ステータス` | Table Column | - | Trạng thái trực thuộc Agency: `申請中`, `所属済み`, `退所申請中`, `退所済み`. Trạng thái `却下` (Bị từ chối) KHÔNG hiển thị ở bảng này.<br>• **CR 11/11/2026:** Nếu Liver không live suốt 1 tuần (`一週間未配信`) và được Agency khác duyệt gia nhập $\rightarrow$ Tự động cưỡng chế rời khỏi Agency hiện tại (`強制退所`) và chuyển sang `退所済み`. |
| `[31]` | `配信権限` | Table Column | - | Quyền livestream của Liver: `あり` (Có) hoặc `なし` (Không). Mặc định khi tạo là `あり`. |
| `[32]` | `加入日時` | Table Column | - | Thời điểm Liver gia nhập Agency (`YYYY/MM/DD HH:mm`, sortable). |
| `[33]` | `詳細` | Action Button | - | Click điều hướng sang màn hình quản lý chi tiết User `AE200`. |

---

### 2. Pass 2 - Quét Các Phần Tử & Logic Không Có `[No.]`

- **`[0] Screen Access & Lifecycle`:** Breadcrumbs: `＞ 事務所一覧 ＞ 事務所詳細` (chuyển sang tab `ライバー一覧`). URL: `/admin/agencies/{agency_id}/livers`.
- **`[Notice] Không có chức năng Xóa:`** Spec ghi chú rõ ràng: `Không có chức năng xoá ở đây`. Mọi thay đổi tài khoản hoặc xóa user được thực hiện tại `AE200`.
- **`[Empty State]:`** Khi không có bản ghi Liver nào thỏa mãn $\rightarrow$ Hiển thị **`CMMSG47`** (`一致する検索結果はありません。`).

---

## II. MA TRẬN LOGIC NGHIỆP VỤ & API SCOPE

### 1. Phân định API
- **In-Scope:** `GET /agency/list/{agency_id}` (Lấy danh sách phân trang các Liver thuộc Agency kèm bộ lọc và sắp xếp).
- **Out-of-Scope:** `DELETE /user/{user_id}` (Thao tác xóa user chỉ nằm trên màn `AE200`).

### 2. Bảng Q&A Làm Rõ Yêu Cầu

| No. | Control / Logic | Vấn đề chưa rõ | Câu hỏi làm rõ | Đề xuất Option A / Option B | Giả định tạm thời khi viết TC | Trạng thái |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| `Q1` | `[7] Trạng thái Toggle cột` | Lưu trạng thái Toggle khi chuyển tab | Khi Admin bấm mở rộng nhóm cột `»` rồi chuyển sang Tab `詳細` / `売上` và quay lại, nhóm cột có giữ trạng thái mở rộng không? | **Option A:** Nhớ trạng thái mở rộng trong phiên làm việc hiện tại (SessionState).<br>**Option B:** Mặc định luôn thu gọn lại `«` mỗi lần mở lại Tab. | **Tạm giả định theo Option B** (Theo Spec: Default luôn là ẩn thu gọn). | `Pending` |
| `Q2` | `[31] 配信権限` | Thay đổi quyền live | Cột `配信権限` trên AD302 là nhãn chỉ xem (Label) hay có thể click bật/tắt trực tiếp trên bảng? | **Option A:** Là cột chỉ xem (Label / Badge), muốn thay đổi phải bấm nút Chi tiết [33] sang AE200.<br>**Option B:** Cho phép toggle trực tiếp dạng Switch. | **Tạm giả định theo Option A** (Spec định nghĩa Type là `label` $\rightarrow$ Chỉ xem). | `Pending` |
