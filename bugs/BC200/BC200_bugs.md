# BÁO CÁO LỖI MÀN HÌNH BC200 (LIVER DETAILS - ライバー詳細)

- **Môi trường kiểm thử:** STG-Agency (`https://admin-stg.surrealdolls.com/agencies/liver/detail/{id}`) & Dev-Agency (`https://admin-dev.surrealdolls.com/agencies/liver/detail/{id}`)
- **Tài khoản thực thi:** `123` / `Leo150122@` (STG) | `agency01` (Dev) | Tester: `ngadtp@mumesoft.vn`
- **Ngày kiểm thử Round 1 (Dev):** 2026/11/12 (Cập nhật: 2026/11/13)
- **Ngày kiểm thử Round 2 (STG):** 2026/11/16
- **Tổng quan kết quả Round 2 (STG):**
  - **Tổng số Test Case:** 105
  - **Pass:** 93 (88.6%)
  - **Fail (Lỗi):** 0
  - **Pending (Chưa triển khai / Đã confirm chưa làm):** 6
  - **Blocked (Cần dữ liệu đặc thù / Kịch bản đồng thời):** 6
  - **Bằng chứng kiểm thử màn hình STG:**
    - Khởi tạo màn hình chi tiết: [evidence_BC200_STG_TC01_initial_load.png](../../evidence/BC200/evidence_BC200_STG_TC01_initial_load.png)
    - Kiểm soát an toàn truy cập ngoài Agency (MSG254): [evidence_BC200_STG_TC03_permission_denied_msg254.png](../../evidence/BC200/evidence_BC200_STG_TC03_permission_denied_msg254.png)
    - Banner và phân quyền xét duyệt gia nhập (申請中): [evidence_BC200_STG_TC06_TC77_applicant_review_banner.png](../../evidence/BC200/evidence_BC200_STG_TC06_TC77_applicant_review_banner.png)
    - Banner và phân quyền xét duyệt rời agency (退所申請中): [evidence_BC200_STG_TC78_leave_applicant_banner.png](../../evidence/BC200/evidence_BC200_STG_TC78_leave_applicant_banner.png)
    - Modal xác nhận duyệt gia nhập (24.1): [evidence_BC200_STG_TC81_approve_join_modal.png](../../evidence/BC200/evidence_BC200_STG_TC81_approve_join_modal.png)
    - Modal xác nhận duyệt rời agency (24.2): [evidence_BC200_STG_TC84_approve_leave_modal.png](../../evidence/BC200/evidence_BC200_STG_TC84_approve_leave_modal.png)
    - Modal xác nhận từ chối gia nhập (25.1): [evidence_BC200_STG_TC88_reject_join_modal.png](../../evidence/BC200/evidence_BC200_STG_TC88_reject_join_modal.png)
    - Modal xác nhận từ chối rời agency (25.2): [evidence_BC200_STG_TC92_reject_leave_modal.png](../../evidence/BC200/evidence_BC200_STG_TC92_reject_leave_modal.png)
    - Modal xác nhận hủy bỏ thay đổi (本当に進みますか？): [evidence_BC200_STG_TC96_cancel_confirm_modal.png](../../evidence/BC200/evidence_BC200_STG_TC96_cancel_confirm_modal.png)
    - Lưu trạng thái thành công và Toast CMMSG13: [evidence_BC200_STG_TC27_TC99_status_stopped_saved_cmmsg13.png](../../evidence/BC200/evidence_BC200_STG_TC27_TC99_status_stopped_saved_cmmsg13.png)

---

## 1. Bảng Tổng Hợp Danh Sách Lỗi (Fail Summary Table)

| TC ID | Control / Chức năng | Các bước tái hiện (Steps) | Expected Result | Actual Result | Mức độ | File Evidence (Unique) & DOM Log | Bug ID |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| *(Không có)* | — | — | — | Không phát hiện lỗi trên các tính năng đã triển khai của màn hình BC200 trên môi trường STG | — | — | — |

---

## 2. Báo Cáo Chi Tiết

Hiện tại trên các chức năng đã triển khai của màn hình BC200:
- Toàn bộ luồng thao tác thông tin, form chỉnh sửa, tab chuyển đổi sang BD100/BD200/BD300, lưu thay đổi (`保存`), hủy bỏ thay đổi kèm modal xác nhận (`キャンセル`), luồng xét duyệt gia nhập (`申請中` - ID 125, 111), luồng xét duyệt rời agency (`退所申請中` - ID 123), và kiểm soát an toàn URL âm tính/ngoài agency đều **HOẠT ĐỘNG HOÀN TOÀN CHÍNH XÁC (PASS)**.
- Không ghi nhận lỗi (Bug) nào còn tồn đọng trên các chức năng đã hoàn thiện.

---

## 3. Danh Sách Các Ca Pending (Đã Confirm Chưa Làm) & Blocked

### 3.1. Nhóm ca Pending (Tính năng chưa làm / Change Request mới đã confirm - 6 TCs):
1. **Các link Quick Navigation (`[BC200-67]`, `[BC200-69]`, `[BC200-70]`, `[BC200-71]` — 4 TCs):**
   - `[BC200-67]`: Quick Nav `配信アーカイブ一覧` (`href="#"`, màn BF300 chưa triển khai).
   - `[BC200-69]`: Quick Nav `利用者メッセージ一覧` (`href="#"`, màn BX100 chưa triển khai).
   - `[BC200-70]`: Quick Nav `配信コメント一覧` (`href="#"`, màn BY100 chưa triển khai).
   - `[BC200-71]`: Quick Nav `配信コメント・BAN管理履歴` (`href="#"`, màn BY300 chưa triển khai).
2. **Cưỡng chế rời agency do không live 1 tuần (`[BC200-42]` — 1 TC):**
   - `[BC200-42]`: Tính năng Change Request 11/11/2026 (Pending - CR 11/11).
3. **Điều hướng từ màn khác sang BC200 (`[BC200-2]` — 1 TC):**
   - `[BC200-2]`: Điều hướng từ `BE200` / `BF100~BF500` sang BC200 (Pending).

### 3.2. Nhóm ca Blocked (Cần phối hợp dữ liệu đặc biệt / Kịch bản đồng thời - 6 TCs):
1. **Liver trạng thái đặc biệt (`[BC200-31]`, `[BC200-38]`, `[BC200-40]` — 3 TCs):**
   - `退会済み`, `配信権限 = なし` bởi agency khác, agency cũ.
2. **Xử lý xung đột đồng thời (Race Condition) (`[BC200-80]`, `[BC200-87]` — 2 TCs):**
   - Cần 2 admin thao tác cùng một thời điểm.
3. **Từ chối liver từng rời xin lại (`[BC200-91]` — 1 TC):**
   - Cần liver từng `退所済み` nộp đơn xin lại để test nhánh từ chối (`却下`).
