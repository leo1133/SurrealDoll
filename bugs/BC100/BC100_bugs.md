# BÁO CÁO KẾT QUẢ & LỖI MÀN HÌNH BC100 (LIVER LIST - ライバー一覧)

- **Môi trường kiểm thử:** Dev-Agency (`https://admin-dev.surrealdolls.com/agencies/liver`)
- **Tài khoản thực thi:** `agency01` (`ngadtp@mumesoft.vn`)
- **Ngày kiểm thử:** 2026/11/12 (Round 1 - sau khi cập nhật testcase theo Rule 02 & UI_controls)
- **Tổng quan kết quả:**
  - **Tổng số Test Case:** 124
  - **Pass:** 110
  - **Fail:** 0
  - **Blocked (Thiếu dữ liệu test trên Dev):** 14
  - **Bằng chứng màn hình ban đầu:** `evidence/BC100/evidence_BC100_TC01_initial_load.png`

---

## 1. Bảng Tổng Hợp Danh Sách Lỗi (Fail Summary Table)

| TC ID | Control / Chức năng | Các bước tái hiện (Steps) | Expected Result | Actual Result | Mức độ | File Evidence (Unique) & DOM Log | Bug ID |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| *(Không có)* | — | — | — | Không phát hiện lỗi trên 108 ca đã thực thi. | — | — | — |

---

## 2. Danh Sách Ca Bị Chặn Do Thiếu Dữ Liệu (Test Data Blocker)

Theo quy chuẩn tại [04_manual_test_execution_rule.md](../../Universal_Rules/04_manual_test_execution_rule.md) mục 3.2, 17 ca kiểm thử dưới đây tạm dừng (`Blocked`, để trống cột Result trên Google Sheet và ghi chú lý do tại cột Note) do dữ liệu `agency01` hiện tại chỉ có **4 bản ghi** (3 `所属済み`, 1 `退所済み`):

1. **Dữ liệu trạng thái Liver (`[BC100-5]`, `[BC100-6]` - ĐÃ PASS):**
   - Đã kiểm thử Pass ca `[BC100-3]` với liver applicant ID `448`: Sau khi từ chối gia nhập (`却下`), liver bị ẩn hoàn toàn khỏi danh sách BC100.
   - Đã kiểm thử Pass ca `[BC100-5]` và `[BC100-6]` với Liver ID `456` (`Nga Nga`): Liver `退所済み` nộp lại đơn chuyển trạng thái sang `申請中`, cập nhật `加入日時` 17:38, không sinh duplicate row (Single Record Rule). Sau đó Agency duyệt `承認`, chuyển thành `所属済み`.
   - Cần tạo/seed thêm cho `agency01`:
     - Kịch bản CR 11/11/2026 (`強制退所`): liver `所属済み`/`退所申請中` không live 1 tuần xin sang agency khác và được duyệt (`[BC100-102]`).
2. **Dữ liệu phân trang (`[BC100-109]` ~ `[BC100-117]`, `[BC100-120]` ~ `[BC100-123]`):**
   - Hiện `agency01` có 4 liver (1 trang).
   - Cần seed tối thiểu **11 bản ghi** để test chuyển trang (`[BC100-109]`~`[BC100-114]`, `[BC100-120]`~`[BC100-123]`) và **> 70 bản ghi (> 7 trang)** để test rút gọn dấu `...` và nhảy trang (`[BC100-115]`~`[BC100-117]`).
