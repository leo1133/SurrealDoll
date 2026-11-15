# BÁO CÁO LỖI MÀN HÌNH BC200 (LIVER DETAILS - ライバー詳細)

- **Môi trường kiểm thử:** Dev-Agency (`https://admin-dev.surrealdolls.com/agencies/liver/detail/{id}`)
- **Tài khoản thực thi:** `agency01` (`ngadtp@mumesoft.vn`)
- **Ngày kiểm thử:** 2026/11/12 (Cập nhật: 2026/11/13)
- **Tổng quan kết quả:**
  - **Tổng số Test Case:** 105
  - **Pass:** 93
  - **Fail (Lỗi):** 0
  - **Pending (Chưa triển khai / Đã confirm chưa làm):** 6
  - **Blocked (Cần phối hợp Master Admin / Dữ liệu đặc biệt):** 6
  - **Bằng chứng kiểm thử màn hình ban đầu:** `evidence/BC200/evidence_BC200_TC01_initial_load.png`

---

## 1. Bảng Tổng Hợp Danh Sách Lỗi (Fail Summary Table)

| TC ID | Control / Chức năng | Các bước tái hiện (Steps) | Expected Result | Actual Result | Mức độ | File Evidence (Unique) & DOM Log | Bug ID |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| *(Không có)* | — | — | — | Không phát hiện lỗi trên các tính năng đã triển khai của màn hình BC200 | — | — | — |

---

## 2. Báo Cáo Chi Tiết

Hiện tại trên các chức năng đã triển khai của màn hình BC200:
- Toàn bộ luồng thao tác thông tin, form chỉnh sửa, tab chuyển đổi, lưu thay đổi (`保存`), hủy bỏ thay đổi kèm modal xác nhận (`キャンセル`), luồng xét duyệt gia nhập (`申請中` - ID 351, 448), luồng xét duyệt rời agency (`退所申請中` - ID 484, 456), và kiểm soát an toàn deep-link âm tính đều **HOẠT ĐỘNG HOÀN TOÀN CHÍNH XÁC (PASS)**.
- Không ghi nhận lỗi (Bug) nào còn tồn đọng trên các chức năng đã hoàn thiện.

---

## 3. Danh Sách Các Ca Pending (Đã Confirm Chưa Làm) & Blocked

### 3.1. Nhóm ca Pending (Tính năng chưa làm / Change Request mới đã confirm - 6 TCs):
1. **Các link Quick Navigation (`[BC200-67]`, `[BC200-69]`, `[BC200-70]`, `[BC200-71]` — 4 TCs):**
   - `[BC200-67]`: Quick Nav `配信アーカイブ一覧` (Đã confirm: `chưa làm`).
   - `[BC200-69]`: Quick Nav `利用者メッセージ一覧` (Đã confirm: `chưa làm`).
   - `[BC200-70]`: Quick Nav `配信コメント一覧` (Đã confirm: `chưa làm`).
   - `[BC200-71]`: Quick Nav `配信コメント・BAN管理履歴` (Đã confirm: `chưa làm`).
2. **Cưỡng chế rời agency do không live 1 tuần (`[BC200-42]` — 1 TC):**
   - `[BC200-42]`: Tính năng CR 11/11/2026 (Đã confirm: `Pending - CR 11/11`).
3. **Điều hướng từ màn khác sang BC200 (`[BC200-2]` — 1 TC):**
   - `[BC200-2]`: Điều hướng từ `BE200` / `BF100~BF500` sang BC200 (Đã confirm: `Pending`).

### 3.2. Nhóm ca Blocked (Cần phối hợp dữ liệu đặc biệt / Kịch bản đồng thời - 6 TCs):
1. **Liver trạng thái đặc biệt (`[BC200-31]`, `[BC200-38]`, `[BC200-40]` — 3 TCs):**
   - `退会済み`, `配信権限 = なし` bởi agency khác, agency cũ.
2. **Xử lý xung đột đồng thời (Race Condition) (`[BC200-80]`, `[BC200-87]` — 2 TCs):**
   - Cần 2 admin thao tác cùng một thời điểm.
3. **Từ chối liver từng rời xin lại (`[BC200-91]` — 1 TC):**
   - Cần liver từng `退所済み` nộp đơn xin lại để test nhánh từ chối (`却下`).

*(Ghi chú: Toàn bộ 4 ca phối hợp và đồng bộ với Master Admin gồm `[BC200-29]`, `[BC200-30]`, `[BC200-37]`, `[BC200-105]` đều đã được thực thi và xác nhận **PASS 100%** trên live môi trường Dev).*
