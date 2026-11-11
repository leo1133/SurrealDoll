# BÁO CÁO ĐỐI SOÁT & TEST CASE KIỂM THỬ GIAO DIỆN & TÍNH TOÁN AS100
## Màn hình: AS100 - Sale Analysis Dashboard (Bảng Điều Khiển Phân Tích Doanh Thu Tổng Hợp)
### Kỳ kiểm tra: `2026/11/09 〜 2026/11/09`
### Google Sheet Target: [Bảng Tính Kiểm Thử Sheet15 (gid=1737064147)](https://docs.google.com/spreadsheets/d/1nAJU06so8kY5QwVfScC9hEbxY6nVznexwi9C6X8vK6k/edit?gid=1737064147#gid=1737064147)

---

## I. TỔNG QUAN SO SÁNH: DỮ LIỆU THỰC TẾ TRÊN DEV-ADMIN VS SPEC TÍNH TOÁN

| Chỉ số (KPI Measure) | Dev-Admin AS100 (Giao diện UI) | Dev-Admin Backend API (`known_subtotal`) | Tính toán Sheet15 (Theo Spec & Công thức) | Trạng thái đối soát | Nguyên nhân hiển thị trên Dev-Admin |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **売上合計 (Total Sales)** | `ー 円` | `6,315 円` | `6,515 円` | **Lệch 200¥** (giữa API subtotal & Spec) | UI hiện `ー` do `missing_count: 2`. Subtotal thiếu 200¥ từ TX20 & TX21 bị lỗi stream. |
| **カラオケ配信以外売上 (Non-Karaoke Sales)** | `ー 円` | `5,600 円` | `5,800 円` | **Lệch 200¥** (giữa API subtotal & Spec) | Subtotal gồm: 100¥ (TX01) + 2,500¥ (TX03) + 3,000¥ (TX04) = 5,600¥. Thiếu 200¥ từ TX20 & TX21. |
| **カラオケ配信売上 (Karaoke Sales)** | `ー 円` | `0 円` | `0 円` | **Khớp (0¥)** | Ngày 2026/11/09 không có luồng nào bật Karaoke. UI hiện `ー` do missing_count=2. |
| **ファミリア売上 (Familia Sales)** | **`715 円`** | **`715 円`** | **`715 円`** | **KHỚP CHÍNH XÁC (100%)** | `missing_count: 0`. Giao dịch mua Class của Leo -> Nga Nga (TX08: 715¥). |
| **ライバー報酬支払 (Liver Reward Payout)** | `ー 円` | `1,200 円` | `1,200 円` | **KHỚP VỚI API SUBTOTAL** | Thưởng Phg từ 2-shot TX04 (3,000P * 40% = 1,200¥). UI hiện `ー` do missing_count=5. |
| **事務所報酬支払 (Agency Reward Payout)** | `ー 円` | `0 円` | `0 円` | **Khớp (0¥)** | Ngày 2026/11/09 chưa có bản ghi chi trả Agency AD303. UI hiện `ー` do missing_count=1. |
| **ストア手数料支払 (Store Fee Payout)** | `ー 円` | `0 円` | `0 円` | **Lỗi dữ liệu Dev** | UI hiện `ー` do thiếu Payment Receipt (`MISSING_PAYMENT_RECEIPT`, missing_count=15). |
| **カラオケ手数料 (Karaoke Fee)** | **`0 円`** | **`0 円`** | **`0 円`** | **KHỚP CHÍNH XÁC (100%)** | DT Karaoke = 0 nên phí bản quyền = 0. Admin UI hiển thị đúng số `0 円`. |
| **粗利益 (Gross Profit)** | `ー 円` | `1,800 円` | `5,315 円` | **Lệch tính toán** | API Dev chỉ lấy subtotal TX04 (3,000 - 1,200 = 1,800¥). Lý thuyết: 6,515 - 1,200 = 5,315¥. |
| **課金額合計 (Total Charged Amount)** | `ー 円` | `0 円` | `119,850 円` | **Lỗi dữ liệu Dev** | 11 giao dịch nạp Top-up chưa có payment receipt từ store nên Dev API bỏ qua. |
| **消費P合計 (Total Consumed Points)** | **`5,800 P`** | **`5,800 P`** | **`5,800 P`** | **KHỚP CHÍNH XÁC (100%)** | 100P (TX01) + 2,500P (TX03) + 3,000P (TX04) + 100P (TX20) + 100P (TX21) = 5,800 P! |
| **消費GP合計 (Total Consumed GP)** | **`100 GP`** | **`100 GP`** | **`100 GP`** | **KHỚP CHÍNH XÁC (100%)** | Giao dịch TX02 gửi Whisper bằng 100 GP! |
| **前受金総合計 (Total Prepaid Balance)** | **`119,850 円`** | **`119,850 円`** | **`119,850 円`** | **KHỚP CHÍNH XÁC (100%)** | Tổng tiền nạp chưa tiêu của tất cả user trong hệ thống. |
| **未消費P合計 (Total Unconsumed Points)** | **`119,850 P`** | **`119,850 P`** | **`119,850 P`** | **KHỚP CHÍNH XÁC (100%)** | Tổng số Point chưa tiêu của tất cả user trong hệ thống. |
| **未消費GP合計 (Total Unconsumed GP)** | **`2,400 GP`** | **`2,400 GP`** | **`2,400 GP`** | **KHỚP CHÍNH XÁC (100%)** | Tổng số GP chưa tiêu của tất cả user trong hệ thống. |

---

## II. DANH SÁCH 21 GIAO DỊCH THỰC TẾ TRÊN DEV-ADMIN (ĐÃ ĐIỀN VÀO RANGE 23:43 VÀ ĐÁNH DẤU MÀU XANH)

Toàn bộ 21 giao dịch thực tế đã tạo trong ngày `2026/11/09` được điền vào **Rows 23 đến 43** trên `Sheet15`, được đánh dấu tiền tố `[ĐÃ TẠO TRÊN DEV]` và bôi nền màu xanh nhạt `#E6F4EA`:

1. **Row 23 (TX_ACT_01):** Whisper 100 P - Nga Nga (456) gửi cho Phg (351) trong Stream 33078. Consumed: 100 P, DT Non-Karaoke: `=(P23/F23)*E23` (100¥).
2. **Row 24 (TX_ACT_02):** Whisper 100 GP - Nga Nga (456) gửi bằng GP cho Phg (351). Consumed: 100 GP, DT: `0¥` (GP không tạo doanh thu quy đổi).
3. **Row 25 (TX_ACT_03):** Gift 2,500 P - Nga Nga (456) gửi tặng Phg (351) trong Stream 33078. Consumed: 2,500 P, DT Non-Karaoke: `=(P25/F25)*E25` (2,500¥).
4. **Row 26 (TX_ACT_04):** 2-Shot 3,000 P - Nga Nga (456) chụp 2shot với Phg (351). Rank Rookie 3 (40%). Consumed: 3,000 P, DT Non-Karaoke: `3,000¥`, GOLD: `=(Q26*0.4)` (1,200 G), Thưởng: `=T26` (1,200¥).
5. **Rows 27-29 (TX_ACT_05 ~ 07):** 3 giao dịch đăng ký gói Hội viên Gold Plan (Monthly Pass) qua Apple Store bởi user Nga Nga (456).
6. **Row 30 (TX_ACT_08):** Mua Class tham gia Familia - Leo (350) mua Class của streamer Nga Nga (456) qua Google Play. DT Familia: `715¥`, Thưởng: `0¥` (do Nga Nga thuộc Agency01).
7. **Rows 31-41 (TX_ACT_09 ~ 19):** 11 giao dịch nạp Point Top-up qua Google & Apple bởi các user (Dev ID 268, Leo, マイアン, Leo Leo).
8. **Rows 42-43 (TX_ACT_20 ~ 21):** 2 giao dịch Whisper 100 P và Gift 100 P trong Stream 33044 của streamer HaiLT661 (493). Lỗi Dev: `MISSING_STREAM_STATE` khiến doanh thu hiển thị `"ー"`.

---

## III. CÁC CASE BỔ SUNG THEO SPEC CHƯA TẠO TRÊN DEV (RANGE 45:54 - ĐÁNH DẤU MÀU VÀNG)

Dòng 44 là đường phân cách (Divider Row) bôi nền vàng đậm.
Các dòng **45 đến 54** chứa 10 test case theo spec AS100 chưa có giao dịch tương ứng trên môi trường Dev (được đánh dấu `[CHƯA TẠO TRÊN DEV - THEO SPEC]` và bôi nền màu vàng nhạt `#FFF9C4`):

1. **Row 45 (TX_SPEC_01):** Gửi Gift 840 P trong stream BẬT KARAOKE (ON) -> Ghi nhận DT Karaoke `=(P45/F45)*E45` (1,200¥), Thưởng `=(R45*0.6)` (504¥).
2. **Row 46 (TX_SPEC_02):** Gửi Whisper 840 P trong stream BẬT KARAOKE (ON) -> Ghi nhận DT Karaoke `1,200¥`, Thưởng `504¥`.
3. **Row 47 (TX_SPEC_03):** Quay Gift Gacha 840 P trong stream Karaoke -> DT Karaoke `1,200¥`, GOLD & Thưởng: `"ー"`.
4. **Row 48 (TX_SPEC_04):** Tiêu vé 2-Shot 840 P trong luồng Karaoke -> DT Karaoke `1,200¥`, Thưởng `504¥`.
5. **Row 49 (TX_SPEC_05):** Mở rương kho báu 1,000 P trong stream thường -> DT Non-Karaoke `1,100¥`, GOLD: `"ー"`.
6. **Row 50 (TX_SPEC_06):** Mua vé quay Gacha giới hạn 1,000 P ngoài stream -> DT Non-Karaoke `1,100¥`.
7. **Row 51 (TX_SPEC_07):** Mua vé thẩm mỹ làm đẹp Doll 840 P ngoài stream -> DT Non-Karaoke `1,200¥`.
8. **Row 52 (TX_SPEC_08):** Mua Backnumber Familia lưu trữ streamer Agency01 (2,860¥) -> DT Familia `2,860¥`, Phí Store `=(S52*0.1)` (286¥).
9. **Row 53 (TX_SPEC_09):** User xóa tài khoản quá 30 ngày -> Tự động tất toán 1,000 P chưa tiêu thành DT Non-Karaoke `1,000¥`.
10. **Row 54 (TX_SPEC_10):** Admin tạo bản ghi chi trả thưởng quản lý 5,000¥ cho Agency01 tại AD303 -> Ghi nhận Thưởng Agency `=5000`.
