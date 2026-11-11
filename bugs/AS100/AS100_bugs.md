# BÁO CÁO LỖI KIỂM THỬ THỦ CÔNG - MÀN HÌNH AS100 (SALES ANALYSIS DASHBOARD)

Theo quy chuẩn [06_bug_reporting_rule.md](file:///home/nga/Documents/SurrealDoll/Universal_Rules/06_bug_reporting_rule.md).

---

## 1. BẢNG TỔNG HỢP DANH SÁCH LỖI PHÁT HIỆN (FAIL SUMMARY TABLE)

| STT | Mã Bug (Tạm thời) | Mã Test Case | Phân Vùng | Tiêu Đề Lỗi | Mức Độ (Severity) | Trạng Thái | Tester | Ngày Phát Hiện |
| :---: | :---: | :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| 1 | *Trống (Chờ Jira)* | `[AS100-355]` | Table & CSV | Click header cột 終了日時 không thực hiện đảo chiều sắp xếp ASC/DESC | Minor | Open | NgaDTP | 2026/11/09 |
| 2 | *Trống (Chờ Jira)* | `[AS100-354]` | Table & CSV | Giao dịch nạp Point qua Store (Apple/Google) hiển thị "ー" thay vì tính phí Store | Major | Open | NgaDTP | 2026/11/09 |

---

## 2. DANH SÁCH BÁO CÁO LỖI CHI TIẾT (DETAILED BUG REPORTS)

### [BUG-1] [AS100] [Table Sorting] Click header cột 終了日時 không thực hiện đảo chiều sắp xếp (cả 2 lần bấm đều giữ nguyên thứ tự)

- **Mã Test Case liên quan:** `[AS100-355]` (Row 365)
- **Mức độ nghiêm trọng (Severity):** Minor
- **Môi trường (Environment):** 
  - URL: `https://admin-dev.surrealdolls.com/sales/analysis-dashboard`
  - Trình duyệt: Chromium / Google Chrome
  - Role: `Admin` (`admin@admin.com`)
- **Các bước tái hiện (Steps to Reproduce):**
  1. Đăng nhập vào trang Admin Dev bằng tài khoản Admin.
  2. Truy cập màn hình Phân tích doanh thu AS100: `/sales/analysis-dashboard`.
  3. Chọn khoảng thời gian có nhiều giao dịch (VD: chọn nút "今日" hoặc tìm kiếm ngày `2026/11/09`).
  4. Quan sát danh sách bảng giao dịch ban đầu.
  5. Click vào header cột 「終了日時」 lần 1.
  6. Click vào header cột 「終了日時」 lần 2.
- **Kết quả kỳ vọng (Expected Result):**
  - Lần 1: Bảng dữ liệu được sắp xếp theo thời gian kết thúc cũ -> mới (ASC). Hiển thị mũi tên sort tương ứng.
  - Lần 2: Bảng dữ liệu được đảo chiều sắp xếp theo thời gian kết thúc mới -> cũ (DESC). Hiển thị mũi tên sort tương ứng.
- **Kết quả thực tế (Actual Result):**
  - Cả 2 lần click vào header cột 「終了日時」, thứ tự hiển thị của các hàng trong bảng hoàn toàn không thay đổi (8 hàng có `終了日時 = "ー"` vẫn cố định ở trên và 2 hàng có giá trị thời gian kết thúc vẫn ở dưới cùng).
  - API trả về cùng một danh sách bản ghi do backend không xử lý đảo chiều cho các bản ghi có giá trị `ended_at = null`.
- **Bằng chứng đính kèm (Evidence):**
  - File ảnh chụp lỗi: [evidence_AS100_TC355_sort_end_date_no_reorder.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AS100_TC355_sort_end_date_no_reorder.png)
  - Bằng chứng trích xuất dữ liệu DOM sau 2 lần click:
    ```json
    // Dữ liệu hàng sau Click 1:
    [
      {"startDate":"2026/11/09 12:23","endDate":"ー","user":"Leo (350)"},
      {"startDate":"2026/11/09 12:23","endDate":"ー","user":"Leo (350)"},
      {"startDate":"2026/11/09 12:23","endDate":"ー","user":"Leo (350)"},
      {"startDate":"2026/11/09 12:05","endDate":"ー","user":"Dev ID 268 (268)"},
      {"startDate":"2026/11/09 11:57","endDate":"ー","user":"Dev ID 268 (268)"},
      {"startDate":"2026/11/09 11:54","endDate":"ー","user":"マイアン（テスター) 263 (263)"},
      {"startDate":"2026/11/09 11:52","endDate":"ー","user":"Leo Leo (483)"},
      {"startDate":"2026/11/09 11:51","endDate":"ー","user":"Leo Leo (483)"},
      {"startDate":"2026/11/09 11:26","endDate":"2026/11/09 12:06","user":"Dev ID 268 (268)"},
      {"startDate":"2026/11/09 11:26","endDate":"2026/11/09 12:06","user":"Dev ID 268 (268)"}
    ]

    // Dữ liệu hàng sau Click 2: Hoàn toàn trùng khớp 100%, không hề đảo chiều!
    ```

---

### [BUG-2] [AS100] [Table Store Fee] Giao dịch nạp Point qua Store (Apple/Google) hiển thị "ー" thay vì tính phí Store do thiếu bằng chứng thanh toán

- **Mã Test Case liên quan:** `[AS100-354]` (Row 364)
- **Mức độ nghiêm trọng (Severity):** Major
- **Môi trường (Environment):** 
  - URL: `https://admin-dev.surrealdolls.com/sales/analysis-dashboard`
  - Trình duyệt: Chromium / Google Chrome
  - Role: `Admin` (`admin@admin.com`)
- **Các bước tái hiện (Steps to Reproduce):**
  1. Đăng nhập vào trang Admin Dev.
  2. Truy cập màn hình AS100: `/sales/analysis-dashboard`.
  3. Tìm kiếm các giao dịch nạp point qua Google/Apple Store ngày `2026/11/09`.
  4. Cuộn bảng sang ngang đến cột 「ストア手数料（円）」.
  5. Quan sát giá trị hiển thị tại cột này đối với các giao dịch có Platform là APPLE hoặc GOOGLE.
- **Kết quả kỳ vọng (Expected Result):**
  - Theo Spec mục 16 (cột ストア手数料) và Testcase `[AS100-354]`:
    + Nếu là giao dịch qua store (GMO/Google/Apple): hiển thị phí store được tính theo công thức tại item 37, 38, 39 (dựa trên tỷ lệ phí store đã cấu hình, VD: `Số tiền x % phí store`).
    + Nếu là các loại giao dịch khác (nội bộ, quà tặng không qua store): hiển thị `"ー"`.
- **Kết quả thực tế (Actual Result):**
  - Tất cả các giao dịch nạp point qua APPLE và GOOGLE Store trên UI đều hiển thị `"ー"`.
  - API `/sales-dashboard` trả về `store_fee: null` do trường `missing_data` chứa `["MISSING_PAYMENT_RECEIPT", "MISSING_STORE_FEE_EVIDENCE"]`.
- **Bằng chứng đính kèm (Evidence):**
  - File ảnh chụp lỗi: [evidence_AS100_TC354_store_fee_hyphen.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AS100_TC354_store_fee_hyphen.png)
  - Bằng chứng API JSON Payload:
    ```json
    {
      "key": "top_ups:859fcb85-b28c-47f7-88a6-5c41340a304a",
      "occurred_at": "2026-11-09T03:23:37Z",
      "service_type": 12,
      "provider": "APPLE",
      "base_price": 8400,
      "measures": {
        "store_fee": null,
        "charged_amount": null
      },
      "missing_data": [
        "MISSING_PAYMENT_RECEIPT",
        "MISSING_STORE_FEE_EVIDENCE"
      ]
    }
    ```
