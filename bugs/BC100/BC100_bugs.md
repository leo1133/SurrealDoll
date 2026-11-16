# BÁO CÁO KẾT QUẢ & LỖI MÀN HÌNH BC100 (LIVER LIST - ライバー一覧)

- **Môi trường kiểm thử:** STG-Agency (`https://admin-stg.surrealdolls.com/agencies/liver`) & Dev-Agency (`https://admin-dev.surrealdolls.com/agencies/liver`)
- **Tài khoản thực thi:** `123` / `Leo150122@` (STG) | `agency01` (Dev) | Tester: `ngadtp@mumesoft.vn`
- **Ngày kiểm thử Round 1 (Dev):** 2026/11/12 (Cập nhật: 2026/11/13)
- **Ngày kiểm thử Round 2 (STG):** 2026/11/16
- **Tổng quan kết quả Round 2 (STG):**
  - **Tổng số Test Case:** 124
  - **Pass:** 123 (99.2%)
  - **Fail:** 0
  - **Pending (Change Request 11/11):** 1 (`[BC100-102]`)
  - **Bằng chứng kiểm thử màn hình STG:**
    - Khởi tạo màn hình: [evidence_BC100_STG_initial_load.png](../../evidence/BC100/evidence_BC100_STG_initial_load.png)
    - Empty State tìm kiếm không có kết quả: [evidence_BC100_STG_TC56_empty_state.png](../../evidence/BC100/evidence_BC100_STG_TC56_empty_state.png)
    - Lọc trạng thái 申請中 (2 bản ghi): [evidence_BC100_STG_TC58_filter_applicant_status.png](../../evidence/BC100/evidence_BC100_STG_TC58_filter_applicant_status.png)
    - Lọc trạng thái 退所申請中 (1 bản ghi): [evidence_BC100_STG_TC38_filter_pending_leave.png](../../evidence/BC100/evidence_BC100_STG_TC38_filter_pending_leave.png)
    - Mở rộng chi tiết doanh thu và thời lượng: [evidence_BC100_STG_TC65_TC67_expanded_breakdown_columns.png](../../evidence/BC100/evidence_BC100_STG_TC65_TC67_expanded_breakdown_columns.png)

---

## 1. Bảng Tổng Hợp Danh Sách Lỗi (Fail Summary Table)

| TC ID | Control / Chức năng | Các bước tái hiện (Steps) | Expected Result | Actual Result | Mức độ | File Evidence (Unique) & DOM Log | Bug ID |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| *(Không có)* | — | — | — | Không phát hiện lỗi trên 123 ca đã thực thi kiểm thử trên môi trường STG. | — | — | — |

---

## 2. Danh Sách Ca Pending / Yêu Cầu Dữ Liệu Đặc Biệt

Theo quy chuẩn tại [04_manual_test_execution_rule.md](../../Universal_Rules/04_manual_test_execution_rule.md) mục 3.2, 01 ca kiểm thử dưới đây giữ trạng thái `Pending`:

1. **`[BC100-102]` - Cưỡng chế rời agency (強制退所 - Change Request 11/11/2026):**
   - **Mô tả:** Liver đang `所属済み` hoặc `退所申請中` không live suốt 1 tuần, gửi `参加申請` sang agency khác và được agency đó bấm `承認`.
   - **Kỳ vọng:** Liver tự động chuyển sang trạng thái `退所済み` ở agency hiện tại mà không cần agency hiện tại duyệt.
   - **Trạng thái:** `Pending - CR 11/11` (Cần data liver không live 1 tuần xin sang agency khác để kích hoạt luồng).
