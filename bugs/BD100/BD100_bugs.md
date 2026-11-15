# BÁO CÁO LỖI MÀN HÌNH BD100 (LIVER DETAILS - OWNED ITEMS / 所持アイテム)

- **Môi trường kiểm thử:** STG-Agency (`https://admin-stg.surrealdolls.com/agencies/liver/detail/{id}?tab=owned-items`)
- **Tài khoản thực thi:** `123` (`ngadtp@mumesoft.vn`)
- **Ngày kiểm thử:** 2026/11/13
- **Tổng quan kết quả:**
  - **Tổng số Test Case:** 117
  - **Pass:** 115
  - **Fail (Lỗi):** 0
  - **Blocked (Cần dữ liệu đặc thù):** 2
  - **Tỷ lệ Pass:** 98.3%
  - **Bằng chứng kiểm thử màn hình ban đầu:** `evidence/BD100/evidence_BD100_TC01_initial_load.png`
  - **Bằng chứng kiểm thử liver 退所済み (Dev ID 350):** `evidence/BD100/evidence_BD100_TC07_leaved_liver_owned_items.png`

---

## 1. Bảng Tổng Hợp Danh Sách Lỗi (Fail Summary Table)

| TC ID | Control / Chức năng | Các bước tái hiện (Steps) | Expected Result | Actual Result | Mức độ | File Evidence (Unique) & DOM Log | Bug ID |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| *(Không có)* | — | — | — | Không phát hiện lỗi trên các tính năng đã triển khai của màn hình BD100 | — | — | — |

---

## 2. Báo Cáo Chi Tiết Đánh Giá Môi Trường STG

Hiện tại trên các chức năng đã triển khai của màn hình BD100 (所持アイテム):
1. **Truy cập & Điều hướng:**
   - Điều hướng liên thông giữa 5 tab chính (`詳細`, `所持アイテム`, `利用履歴`, `課金情報`, `売上 [disabled]`) và Breadcrumb (`ホーム > ライバー一覧 > ライバー詳細`) hoạt động chính xác 100%.
   - Mặc định sub-tab `アバターアイテム` được kích hoạt (`active`), hiển thị đầy đủ danh sách model và danh mục trang phục/phụ kiện.
2. **Sub-tab アバターアイテム:**
   - Bộ lọc: Ô nhập `アイテム名`, các pulldown `全モデル`, `全種類`, `全レアリティ`, checkbox `所持のみ`, nút `検索` và `クリア` hoạt động mượt mà, phản hồi đúng tiêu chí lọc.
   - Accordion model (`少女モデル`, `model 2`) gập mở linh hoạt, hiển thị đúng tỷ lệ sở hữu (`16/18件`, `9/9件`).
   - Modal xem trước 3D (`アバターアイテムプレビュー`) mở chính xác khi bấm nút `プレビュー: {item_name}` (`evidence/BD100/evidence_BD100_TC81_item_preview_modal.png`), nút `閉じる` và icon `Close` đóng modal an toàn.
3. **Sub-tab 背景:**
   - Chuyển đổi qua lại giữa `アバターアイテム` và `背景` độc lập bộ lọc (`evidence/BD100/evidence_BD100_TC23_background_subtab.png`).
   - Hiển thị đầy đủ 2 nhóm accordion: `箱庭背景ガチャ一覧` và `イラスト背景ガチャ一覧`.
   - Tìm kiếm theo tên/ID background chính xác tuyệt đối (`evidence/BD100/evidence_BD100_TC100_search_by_name.png`).
   - Modal phóng to ảnh background hiển thị ảnh gốc chất lượng cao (`evidence/BD100/evidence_BD100_TC111_bg_preview_modal.png`).
   - Khi tìm kiếm không có kết quả: Hiển thị đúng thông báo chuẩn CMMSG47 `一致する検索結果はありません。` kèm gợi ý `フィルターをクリアして、もう一度お試しください` (`evidence/BD100/evidence_BD100_TC106_empty_state.png`).
4. **Bảo mật & Phân quyền:**
   - Truy cập URL liver không thuộc Agency hoặc ID ảo (`999999`): Hệ thống chặn hiển thị và đưa ra thông báo lỗi MSG254 `このライバーを閲覧する権限がありません。` (`evidence/BD100/evidence_BD100_TC05_foreign_liver_msg254.png`).
   - Liver trạng thái `申請中` (ID: 125, 111): Tab `所持アイテム` bị disabled; khi truyền trực tiếp URL parameter `?tab=owned-items`, hệ thống tự động fallback về tab `詳細` an toàn (`evidence/BD100/evidence_BD100_TC09_applicant_tabs_disabled.png`).
   - Toàn bộ giao diện ở chế độ Read-only, không hiển thị các nút cấp phát (`付与`) hay thu hồi (`解放`) của Master.

---

## 3. Danh Sách Các Ca Blocked & Đề Xuất Dữ Liệu (Test Data Seeding)

| TC ID | Tiêu đề ca kiểm thử | Lý do Blocked trên STG | Yêu cầu Test Data Seeding |
| :--- | :--- | :--- | :--- |
| `[BD100-6]` | Kiểm tra bảo mật khi truy cập URL liver đã bị 却下 | Chưa có tài khoản liver trạng thái `却下` thuộc Agency trên STG | Cần từ chối 1 đơn xin gia nhập (thao tác 却下 trên liver mẫu `125` hoặc `111`) |
| `[BD100-8]` | Kiểm tra dữ liệu liver 退所済み xin vào lại | Chưa có kịch bản liver từng rời Agency nộp đơn xin gia nhập lại | Cần 1 tài khoản đã `退所済み` gửi lại request xin vào Agency trên mobile app |

> [!NOTE]
> Ca `[BD100-7]` (Kiểm tra dữ liệu liver `退所済み`) đã được thực thi và xác nhận Pass trên live Dev (Liver ID: 350 `Leo`, status `退所済み`). Dữ liệu item và model hoàn toàn đóng băng tại thời điểm rời hội. Evidence: `evidence/BD100/evidence_BD100_TC07_leaved_liver_owned_items.png`.
