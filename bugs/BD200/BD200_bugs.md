# BÁO CÁO LỖI MÀN HÌNH BD200 (LIVER DETAILS - USAGE HISTORY / 利用履歴)

- **Môi trường kiểm thử:** STG-Agency (`https://admin-stg.surrealdolls.com/agencies/liver/detail/{id}?tab=usage-history`)
- **Tài khoản thực thi:** `123` (`ngadtp@mumesoft.vn`)
- **Ngày kiểm thử:** 2026/11/13
- **Tổng quan kết quả:**
  - **Tổng số Test Case:** 89
  - **Pass:** 87
  - **Fail (Lỗi):** 0
  - **Blocked (Cần dữ liệu đặc thù):** 2
  - **Tỷ lệ Pass:** 97.8%
  - **Bằng chứng kiểm thử màn hình ban đầu:** `evidence/BD200/evidence_BD200_TC01_initial_load.png`
  - **Bằng chứng kiểm thử liver 退所済み (Dev ID 350):** `evidence/BD200/evidence_BD200_TC08_leaved_liver_usage_history.png`

---

## 1. Bảng Tổng Hợp Danh Sách Lỗi (Fail Summary Table)

| TC ID | Control / Chức năng | Các bước tái hiện (Steps) | Expected Result | Actual Result | Mức độ | File Evidence (Unique) & DOM Log | Bug ID |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| *(Không có)* | — | — | — | Không phát hiện lỗi trên các tính năng đã triển khai của màn hình BD200 | — | — | — |

---

## 2. Báo Cáo Chi Tiết Đánh Giá Môi Trường STG

Hiện tại trên các chức năng đã triển khai của màn hình BD200 (利用履歴):
1. **Khối Card Số Dư & Chuyển Đổi:**
   - Card [3] `現在残高` (Point: 788 P, Gift Point: 9,797 GP, Coin: 90 C) mặc định được kích hoạt khi mở màn hình.
   - Bấm vào Card [4] `所持チケット` (`evidence/BD200/evidence_BD200_TC29_ticket_history_selected.png`): Giao diện lập tức chuyển đổi động sang bảng số liệu vé:
     - Bảng `累計収支` chuyển sang thống kê 4 loại vé: `2ショットチケット`, `期間限定ガチャチケット`, `ノーマルガチャチケット`, `エステチケット`.
     - Bảng log giao dịch xuất hiện thêm cột `チケット種類`, cột tăng giảm hiển thị đúng đơn vị `枚` (ví dụ: `-10 枚`, `+1 枚`).
2. **Bộ Lọc Thời Gian (Date Filter):**
   - Các nút chọn nhanh `今日`, `昨日`, `今週`, `今月`, `先月` tự động tính toán và điền chính xác khoảng ngày.
   - Nút `検索` lọc chuẩn xác dữ liệu (`evidence/BD200/evidence_BD200_TC45_date_filter_today.png` - lọc hôm nay ra đúng 4 giao dịch ngày 2026/11/13).
   - Nút `クリア` reset toàn bộ ngày bắt đầu và kết thúc về trạng thái mặc định rỗng.
3. **Phân Trang & Định Dạng Số Liệu:**
   - Định dạng hiển thị chuẩn quy cách CMR23: `全 91 件中 1〜10 件を表示`, hiển thị đầy đủ các nút chuyển trang `1, 2, 3, 4, 5, 6 ... 10, 次, 最後のページへ`.
   - Chuyển trang mượt mà, duy trì tính toàn vẹn của dữ liệu và bộ lọc.
   - Giao dịch cộng (`+`) hiển thị màu xanh/dương, giao dịch trừ (`-`) hiển thị màu đỏ/xám kèm đúng ký hiệu tiền tệ hoặc vé.
4. **Bảo Mật:**
   - Chặn truy cập trái phép liver ngoài agency với MSG254 (`evidence/BD200/evidence_BD200_TC06_foreign_liver_msg254.png`).
   - Khóa truy cập tab `利用履歴` đối với liver `申請中` (ID: 125, 111).

---

## 3. Danh Sách Các Ca Blocked & Đề Xuất Dữ Liệu (Test Data Seeding)

| TC ID | Tiêu đề ca kiểm thử | Lý do Blocked trên STG | Yêu cầu Test Data Seeding |
| :--- | :--- | :--- | :--- |
| `[BD200-7]` | Kiểm tra bảo mật khi truy cập URL liver đã bị 却下 | Chưa có tài khoản liver trạng thái `却下` thuộc Agency trên STG | Cần từ chối 1 đơn xin gia nhập (thao tác 却下 trên liver mẫu `125` hoặc `111`) |
| `[BD200-9]` | Kiểm tra dữ liệu liver 退所済み xin vào lại | Chưa có kịch bản liver từng rời Agency nộp đơn xin gia nhập lại | Cần 1 tài khoản đã `退所済み` gửi lại request xin vào Agency trên mobile app |

> [!NOTE]
> Ca `[BD200-8]` (Kiểm tra dữ liệu liver `退所済み`) đã được thực thi và xác nhận Pass trên live Dev (Liver ID: 350 `Leo`, status `退所済み`). Số dư tiền tệ/vé chốt về 0 và toàn bộ log giao dịch đóng băng tại thời điểm rời hội. Evidence: `evidence/BD200/evidence_BD200_TC08_leaved_liver_usage_history.png`.
