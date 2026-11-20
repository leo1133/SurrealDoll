# BÁO CÁO XÁC MINH LỖI TICKET SURREALDOLLS-13433
## [BUG] - [AS100] - Dòng Header và cấu trúc cột của file CSV xuất ra không khớp với bảng Table AS100
### Áp dụng: Master Agent Policy (GEMINI.md) & Trụ cột 6 (06_bug_reporting_rule.md)

---

## 1. THÔNG TIN TỔNG QUAN

- **Ticket ID:** [SURREALDOLLS-13433](https://issoh.backlog.com/view/SURREALDOLLS-13433)
- **Màn hình / Phân hệ:** `AS100` - 売上管理 / 売上分析ダッシュボード (Sales Analysis Dashboard)
- **Môi trường định tuyến:** **STG** (URL: `https://admin-stg.surrealdolls.com/sales/analysis-dashboard`)
- **Tài khoản kiểm thử:** Admin: `admin@admin.com` | `!Ch4ng3Th1sP4ssW0rd!` (HTTP Basic Auth: `suriaru` / `suriaru`)
- **Trạng thái Backlog tiếp nhận:** `Need Verify (STG)`
- **Thời lượng ước tính (Est):** 0.25h (15 phút)
- **Thời lượng thực tế (Actual):** 0.25h (15 phút) (Tổng Actual trên Backlog: 0.75h)
- **Tester:** `NgaDTP` / `Antigravity QA`
- **Ngày kiểm tra:** 19/11/2026
- **Kết luận:** <span style="color:green; font-weight:bold;">VERIFIED PASS (ĐÃ SỬA XONG / RESOLVED)</span>

---

## 2. KẾT QUẢ ĐỐI SOÁT CHI TIẾT (STG RE-TEST RESULT)

| Tiêu chí kiểm tra | Đặc tả kỳ vọng (Expected) | Thực tế cũ (Old Actual) | Thực tế xác minh STG (New Actual) | Đánh giá |
| :--- | :--- | :--- | :--- | :---: |
| **Số lượng cột Header CSV** | Đúng **21 cột** tiếng Nhật theo Spec và UI Table AS100 | Chỉ có 18 cột raw database keys | Đầy đủ chính xác **21 cột** tiếng Nhật | <span style="color:green; font-weight:bold;">PASS</span> |
| **Tên cột và thứ tự các cột** | Khớp 100% với danh sách và thứ tự 21 cột của Table AS100: <br>1. `開始日時`<br>2. `終了日時`<br>3. `利用者`<br>4. `消費前の前受金 （円）`<br>5. `消費前の所持P （P）`<br>6. `ライバー`<br>7. `報酬率（ランク）`<br>8. `事務所`<br>9. `カテゴリー`<br>10. `配信状態`<br>11. `サービス`<br>12. `元ソース`<br>13. `支払方法`<br>14. `振込日`<br>15. `GP/P`<br>16. `カラオケ配信以外売上 （円）`<br>17. `カラオケ配信売上 （円）`<br>18. `ファミリア売上 （円）`<br>19. `GOLD （G）`<br>20. `報酬支払 （円）`<br>21. `ストア手数料 （円）` | 18 cột tiếng Anh raw API: `key, report_at, service_type, currency_type, payer_name, streamer_name, non_karaoke_revenue, karaoke_revenue, familia_revenue, charged_amount, consumed_point, consumed_gift_point, streamer_reward, agency_reward, store_fee, karaoke_fee, gross_profit, missing_data` | Khớp chính xác 100% cả 21 cột tiếng Nhật theo đúng thứ tự từ cột 1 đến cột 21 của bảng Table AS100 trên UI. | <span style="color:green; font-weight:bold;">PASS</span> |
| **11 cột trước đây bị thiếu** | Có mặt đầy đủ 11 cột: `終了日時, 消費前の前受金, 消費前の所持P, 報酬率, 事務所, カテゴリー, 配信状態, 元ソース, 支払方法, 振込日, GOLD` | Thiếu hoàn toàn 11 cột này | Đã bổ sung 100% đầy đủ cả 11 cột vào file CSV xuất ra | <span style="color:green; font-weight:bold;">PASS</span> |
| **Quy tắc đặt tên file CSV** | `{startdate}-{enddate}.csv` (Ví dụ: `20261101-20261130.csv`) | Đúng quy tắc | File tải về tên: `20261101-20261130.csv` | <span style="color:green; font-weight:bold;">PASS</span> |
| **Tính toàn vẹn dữ liệu từng dòng** | Dữ liệu từng dòng khớp 1-1 giữa CSV và Table AS100 | Không tương ứng cấu trúc 1-1 | Dữ liệu dòng 1 CSV: `2026/11/19 16:45:39, ー, miao maio test9 (97), 20057, 14040, ー, ー, ー, ー, ー, ポイント購入, ー, Google, ー, ー, ー, ー, ー, ー, ー, 12` khớp chính xác với dòng 1 trên Table AS100 | <span style="color:green; font-weight:bold;">PASS</span> |

---

## 3. BẢNG ĐỐI CHIẾU 21 CỘT (CSV HEADERS VS UI TABLE HEADERS)

| STT | Tên cột trên UI Table AS100 | Tên cột trong Header CSV (`20261101-20261130.csv`) | Trạng thái đối soát |
| :---: | :--- | :--- | :---: |
| 1 | `開始日時` | `開始日時` | ✅ MATCH |
| 2 | `終了日時` | `終了日時` | ✅ MATCH |
| 3 | `利用者` | `利用者` | ✅ MATCH |
| 4 | `消費前の前受金 （円）` | `消費前の前受金 （円）` | ✅ MATCH |
| 5 | `消費前の所持P （P）` | `消費前の所持P （P）` | ✅ MATCH |
| 6 | `ライバー` | `ライバー` | ✅ MATCH |
| 7 | `報酬率（ランク）` | `報酬率（ランク）` | ✅ MATCH |
| 8 | `事務所` | `事務所` | ✅ MATCH |
| 9 | `カテゴリー` | `カテゴリー` | ✅ MATCH |
| 10 | `配信状態` | `配信状態` | ✅ MATCH |
| 11 | `サービス` | `サービス` | ✅ MATCH |
| 12 | `元ソース` | `元ソース` | ✅ MATCH |
| 13 | `支払方法` | `支払方法` | ✅ MATCH |
| 14 | `振込日` | `振込日` | ✅ MATCH |
| 15 | `GP/P` | `GP/P` | ✅ MATCH |
| 16 | `カラオケ配信以外売上 （円）` | `カラオケ配信以外売上 （円）` | ✅ MATCH |
| 17 | `カラオケ配信売上 （円）` | `カラオケ配信売上 （円）` | ✅ MATCH |
| 18 | `ファミリア売上 （円）` | `ファミリア売上 （円）` | ✅ MATCH |
| 19 | `GOLD （G）` | `GOLD （G）` | ✅ MATCH |
| 20 | `報酬支払 （円）` | `報酬支払 （円）` | ✅ MATCH |
| 21 | `ストア手数料 （円）` | `ストア手数料 （円）` | ✅ MATCH |

---

## 4. BẰNG CHỨNG XÁC THỰC TRỰC QUAN (VISUAL EVIDENCE & TECHNICAL ARTIFACTS)

- **Ảnh bằng chứng toàn cảnh có viền nổi bật (Overview with Bounding Box & QA Badge):**
  - File: [evidence_AS100_SURREALDOLLS-13433_STG_PASS_csv_export_overview.png](file:///home/nga/Documents/SurrealDoll/evidence/AS100/evidence_AS100_SURREALDOLLS-13433_STG_PASS_csv_export_overview.png)
  - Khung viền xanh lá `#16a34a` (3px) bao quanh nút `CSV出力` và dòng Table Header kèm badge `🔍 RE-TEST PASS: CSV出力 HEADER & 21 COLUMNS MATCH (SURREALDOLLS-13433)`.
- **Ảnh bằng chứng cận cảnh (Zoomed Header & CSV Button Screenshot):**
  - File: [evidence_AS100_SURREALDOLLS-13433_STG_PASS_csv_export_zoom.png](file:///home/nga/Documents/SurrealDoll/evidence/AS100/evidence_AS100_SURREALDOLLS-13433_STG_PASS_csv_export_zoom.png)
- **File CSV xuất thực tế từ STG:**
  - File: [evidence_AS100_SURREALDOLLS-13433_STG_PASS_20261101-20261130.csv](file:///home/nga/Documents/SurrealDoll/evidence/AS100/evidence_AS100_SURREALDOLLS-13433_STG_PASS_20261101-20261130.csv)
  - Kích thước: 11,629 bytes | 86 dòng dữ liệu.
- **Trích xuất dòng 1 Header từ file CSV:**
  ```csv
  開始日時,終了日時,利用者,消費前の前受金 （円）,消費前の所持P （P）,ライバー,報酬率（ランク）,事務所,カテゴリー,配信状態,サービス,元ソース,支払方法,振込日,GP/P,カラオケ配信以外売上 （円）,カラオケ配信売上 （円）,ファミリア売上 （円）,GOLD （G）,報酬支払 （円）,ストア手数料 （円）
  ```

---

## 5. ĐỒNG BỘ KẾT QUẢ 3 CHIỀU

1. **Backlog Ticket [SURREALDOLLS-13433](https://issoh.backlog.com/view/SURREALDOLLS-13433#comment-857199910):**
   - Đã chuyển trạng thái sang: **`Resolved`**.
   - Đã đính kèm ảnh bằng chứng `evidence_AS100_SURREALDOLLS-13433_STG_PASS_csv_export_overview.png`.
   - Đã log thêm **+0.25h** vào Actual Hours (Tổng: 0.75h).
   - Đã để lại comment báo cáo chi tiết cho Backend Team.
2. **Kịch bản kiểm thử giao diện thủ công (`testcase_ui/AS100_testcase_manual_ui.md`):**
   - Đã cập nhật kết quả Retest Pass cho ca `[AS100-319]` và `[AS100-320]`.
3. **Báo cáo lỗi màn hình AS100 (`bugs/AS100/AS100_bugs.md`):**
   - Đã bổ sung mục ghi nhận kết quả xác minh Round 2 STG cho ticket `SURREALDOLLS-13433`.
