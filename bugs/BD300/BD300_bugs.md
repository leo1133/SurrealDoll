# BÁO CÁO LỖI MÀN HÌNH BD300 (LIVER DETAILS - BILLING LOG / 課金情報)

- **Môi trường kiểm thử:** STG-Agency (`https://admin-stg.surrealdolls.com/agencies/liver/detail/{id}?tab=billing-information`)
- **Tài khoản thực thi:** `123` (`ngadtp@mumesoft.vn`)
- **Ngày kiểm thử:** 2026/11/13
- **Tổng quan kết quả:**
  - **Tổng số Test Case:** 144
  - **Pass:** 139
  - **Fail (Lỗi):** 0
  - **Blocked (Cần dữ liệu đặc thù):** 5
  - **Tỷ lệ Pass:** 96.5%
  - **Bằng chứng kiểm thử màn hình ban đầu:** `evidence/BD300/evidence_BD300_TC01_initial_load.png`
  - **Bằng chứng kiểm thử liver 退所済み (Dev ID 350):** `evidence/BD300/evidence_BD300_TC09_leaved_liver_billing.png`

---

## 1. Bảng Tổng Hợp Danh Sách Lỗi (Fail Summary Table)

| TC ID | Control / Chức năng | Các bước tái hiện (Steps) | Expected Result | Actual Result | Mức độ | File Evidence (Unique) & DOM Log | Bug ID |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| *(Không có)* | — | — | — | Không phát hiện lỗi trên các tính năng đã triển khai của màn hình BD300 | — | — | — |

---

## 2. Báo Cáo Chi Tiết Đánh Giá Môi Trường STG

Hiện tại trên các chức năng đã triển khai của màn hình BD300 (課金情報):
1. **Khối Dashboard 4 Cards:**
   - Hiển thị đầy đủ và chuẩn xác 4 chỉ số tài chính: `今月の課金額` (¥98,755), `平均（月）` (¥118,002), `最高（月）` (¥137,250), `過去12ヶ月合計` (¥236,005). Các số tiền đều có định dạng phân cách hàng nghìn và ký hiệu tiền tệ yên Nhật (`¥`).
2. **Sub-tab すべて:**
   - Mặc định active khi mở màn hình BD300.
   - Bảng log hiển thị đầy đủ 7 cột thông tin: `発生日時`, `カテゴリ`, `内容`, `イベント`, `参加期間`, `プラットフォーム`, `金額（円）`.
   - Phân trang đúng quy chuẩn CMR23 với 6 dòng / trang (`全 16 件中 1〜6 件を表示`).
3. **Sub-tab サブスク（クラス）:**
   - Gom nhóm trực quan theo từng Familia (`evidence/BD300/evidence_BD300_TC103_subscription_familia_group.png`): Hiển thị Avatar, tên streamer (`Yến Nguyễn のファミリア`), User ID (`102`), badge trạng thái (`脱退済み`), và dòng ghi chú ngày thoát (`脱退日 2026/11/06（この日で退会済み）`).
   - Bảng lịch sử đăng ký subscription hiển thị chi tiết tên class (`class D 5,000円/月`), loại event (`自動更新`), kỳ hạn (`2026/11/06 21:56 ~ 2026/11/06 22:56`), nền tảng (`iOS`) và số tiền (`¥7,150`).
4. **Sub-tab 単発課金:**
   - Chuyển tab hiển thị chuyên biệt cho các giao dịch đơn lẻ (`evidence/BD300/evidence_BD300_TC121_onetime_billing_table.png`): Bao gồm các lượt mua point, gói nạp tiền.
   - Cột `種別` hiển thị rõ ràng (`ポイント`), số point nhận được (`8,400P`, `84P`).
5. **Bộ Lọc Thời Gian & Xử Lý Empty State:**
   - Hỗ trợ 2 chế độ lọc song song: Pulldown `対象月` (tháng cụ thể hoặc `全期間`) và datepicker `期間指定` (`開始日 〜 終了日`).
   - Khi lọc khoảng thời gian không có giao dịch: Giao diện giữ nguyên header bảng và hiển thị chuẩn thông báo CMMSG47 `一致する検索結果はありません。`, số lượng hiển thị `全 0 件` (`evidence/BD300/evidence_BD300_TC139_empty_state.png`).
6. **Bảo Mật:**
   - Chặn xem trực tiếp URL liver ngoài agency (`evidence/BD300/evidence_BD300_TC06_foreign_liver_msg254.png`).
   - Khóa tab đối với liver `申請中` (ID: 125, 111).

---

## 3. Danh Sách Các Ca Blocked & Đề Xuất Dữ Liệu (Test Data Seeding)

| TC ID | Tiêu đề ca kiểm thử | Lý do Blocked trên STG | Yêu cầu Test Data Seeding |
| :--- | :--- | :--- | :--- |
| `[BD300-7]` | Kiểm tra bảo mật khi truy cập URL liver đã bị 却下 | Chưa có tài khoản liver trạng thái `却下` thuộc Agency trên STG | Cần từ chối 1 đơn xin gia nhập (thao tác 却下 trên liver mẫu `125` hoặc `111`) |
| `[BD300-10]` | Kiểm tra dữ liệu liver 退所済み xin vào lại | Chưa có kịch bản liver từng rời Agency nộp đơn xin gia nhập lại | Cần 1 tài khoản đã `退所済み` gửi lại request xin vào Agency trên mobile app |
| `[BD300-108]` | Kiểm tra hiển thị khi liver đang tham gia subscription (参加中) | Hiện tại liver `102` đang ở trạng thái `脱退済み`, chưa có bản ghi nào `参加中` | Cần tài khoản liver đang có subscription hoạt động bình thường |
| `[BD300-111]` | Kiểm tra format ngày 次回更新日 khi 参加中 | Chưa có subscription trạng thái `参加中` để hiển thị ngày gia hạn kế tiếp | Cần subscription đang `参加中` để kiểm tra label 次回更新日 yyyy/mm/dd |
| `[BD300-112]` | Kiểm tra tính toán ngày 次回更新日 | Chưa có subscription trạng thái `参加中` | Cần subscription active để kiểm tra chu kỳ tính ngày gia hạn tự động |

> [!NOTE]
> Ca `[BD300-9]` (Kiểm tra dữ liệu liver `退所済み`) đã được thực thi và xác nhận Pass trên live Dev (Liver ID: 350 `Leo`, status `退所済み`). 4 card thống kê doanh thu và toàn bộ lịch sử thanh toán đóng băng tại thời điểm rời hội. Evidence: `evidence/BD300/evidence_BD300_TC09_leaved_liver_billing.png`.
