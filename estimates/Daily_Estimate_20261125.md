# KẾ HOẠCH PHÂN BỔ CÔNG VIỆC 8H/NGÀY - 25/11/2026
Theo quy chuẩn [08_task_estimation_rule.md](../Universal_Rules/08_task_estimation_rule.md) & [GEMINI.md](../GEMINI.md).

- **Assignee:** Mume_ガー（テスター） (`ngadtp@mumesoft.vn`)
- **Ngày thực hiện:** Thứ Tư, 25/11/2026
- **Mục tiêu quỹ thời gian chuẩn:** **8.0 giờ / ngày** (1 Man-Day = 480 phút)
- **Milestone trọng điểm:** **2511 (T4) - Release**
- **Nguồn dữ liệu:** Backlog Project `SURREALDOLLS` (https://issoh.backlog.com/)

---

## 1. TỔNG QUAN PHẠM VI QUÉT 3 NHÓM TRẠNG THÁI (3-TIER SCAN SUMMARY)

| Nhóm Trạng Thái | Số Lượng Ticket | Tổng Thời Gian (Giờ) | Quy Đổi Phút | Đánh Giá Tải & Ưu Tiên |
| :--- | :---: | :---: | :---: | :--- |
| **Nhóm 1: Need Verify (Dev & STG)** | 8 bugs / subtasks | **5.25 giờ** | 315 phút | **Ưu tiên 1 (Cao nhất):** Đóng vòng đời bug, nghiệm thu release 2511 |
| **Nhóm 2: In Progress (Đang chạy)** | 4 parent tasks | **4.50 giờ** | 270 phút | **Ưu tiên 2:** Hoàn tất các task chùm BB, AS100, K20241 |
| **Nhóm 3: Open (Due hôm nay 25/11 & mai 26/11)** | 4 tasks khẩn | **6.50 giờ** | 390 phút | **Ưu tiên 3:** CR AP213/AP330/AP405 (Due hôm nay), Hotfix SNS, Livestream |
| **TỔNG KHỐI LƯỢNG CHỜ XỬ LÝ** | **16 tickets** | **~13.25 giờ** | 795 phút | ⚠️ **QUÁ TẢI (+5.25h so với định mức 8.0h/ngày)** |

---

## 2. KẾ HOẠCH THỰC THI CHUẨN 8.0H TRONG NGÀY (25/11/2026)

> [!IMPORTANT]
> Toàn bộ thời gian ước lượng dưới đây đã được **quy đổi trực tiếp sang Đơn vị Giờ (h)** và khóa cứng quỹ thời gian làm việc chuẩn **8.0 giờ (1 Man-Day = 480 phút)** theo [08_task_estimation_rule.md](../Universal_Rules/08_task_estimation_rule.md).

### 2.1. Chi tiết Danh Sách Tác Vụ Quy Đổi Ra Giờ

| STT | Mã Ticket | Tiêu đề Task / Bug | Môi Trường | Trạng Thái | Loại | Độ Khó | Est (Giờ) | Chi Tiết Phút | Lý Do Xếp Lịch & Hạn Chót |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **I** | **KHỐI VERIFY DEV & STG (ƯU TIÊN 1)** | | | | | | **3.75h** | **225 phút** | **Ưu tiên cao nhất: Nghiệm thu đóng release 2511** |
| 1 | `SURREALDOLLS-14788` | **[Verify] K20241 CR アカウント解除のセキュリティ強化**<br>• `14795`: Lỗi thông báo liên kết SĐT (15p)<br>• `14797`: Hủy liên kết Line thông báo trắng (15p)<br>• `14807`: Gỡ liên kết SNS không mở login (20p)<br>• Smoke luồng xác thực lại & update evidence (40p) | **STG** (App iOS/Android) | In Progress | Verify Bug | Logic App | **1.50h** | 90 phút | **Milestone Release 2511**, Priority High, đóng dứt điểm CR bảo mật |
| 2 | `SURREALDOLLS-15039` | [BUG] - Không nhập được data cho trường お知らせ内容 | **STG** (Admin) | Need Verify (STG) | Bug | Validate | **0.25h** | 15 phút | Nghiệm thu rich text field trên STG Admin |
| 3 | `SURREALDOLLS-15051` | [Verify][K202] Login LINE - アカウント設定 dòng Line hiển thị "line.com" thay vì thông tin tài khoản LINE | **DEV** (App/Web) | Open | Verify Bug | Logic | **0.50h** | 30 phút | Milestone 2511, xác thực hiển thị account info LINE |
| 4 | `SURREALDOLLS-14133` | **[Verify] BB100 + BB101 + BB200 + BB300**<br>• `14131`: Popup xác nhận CMMSG28 (9p)<br>• `14128`: Trùng tên admin Agency (12p)<br>• Cập nhật ticket & evidence đóng task (9p) | **DEV** (Agency/Admin) | In Progress | Verify Bug | Chùm màn | **0.50h** | 30 phút | Đóng hoàn toàn chùm BB Agency sau khi fix các subtask cuối |
| 5 | `SURREALDOLLS-13364` | **[Verify bug] AS100 - Test**<br>• `14224`: Không hiển thị agency tham gia (20p)<br>• `13998`: Lỗi overview ngày hôm qua (20p)<br>• Update kết quả & evidence (20p) | **DEV** (Admin) | In Progress | Verify Bug | Logic Web | **1.00h** | 60 phút | Đóng cụm bug màn hình thống kê AS100 |
| **II** | **KHỐI TASK HÔM NAY 25/11 & KHẨN CẤP (ƯU TIÊN 2 & 3)** | | | | | | **4.25h** | **255 phút** | **Trọng tâm CR Tracking Model & Hotfix** |
| 6 | `SURREALDOLLS-15052` | **[Testcase] AP213 + AP330 + AP405 - CR - Thêm tính năng tracking setting** | Web Admin / App | Open | Task | Design | **0.75h** | 45 phút | **Hạn 25/11 (Hôm nay)**, nghiệm thu & sync bộ 70 UI + 25 API testcase |
| 7 | `SURREALDOLLS-15053` | **[Test] AP213 + AP330 + AP405 - CR - Thêm tính năng tracking setting (Phase 1)** | **DEV/STG** (Admin) | Open | Task | Logic/API | **2.50h** | 150 phút | **Hạn 25/11 (Hôm nay)**, thực thi R1 các ca Critical/High: slider, min-max, DB JSONB & API parameters |
| 8 | `SURREALDOLLS-14806` | **Test lại phần connect SNS (màn đăng nhập và màn liên kết tài khoản)** | **STG** (App iOS/Android) | Open | タスク (HOTFIX) | Logic/Auth | **0.50h** | 30 phút | Hotfix sanity test luồng connect SNS |
| 9 | `ADMIN-DAILY` | **Tổng kết kết quả kiểm thử, Log bug phát sinh & Báo cáo cuối ngày** | Tổng hợp | — | Task | Tổng kết | **0.50h** | 30 phút | Cập nhật Backlog board, evidence và đối soát Actual Hours 8h |
| 🎯 | **TỔNG CỘNG THỰC THI** | **9 Cụm Tác Vụ Trọng Điểm (~14 tickets)** | — | — | — | — | **8.00 giờ** | **480 phút** | **ĐẠT CHUẨN 100% 1 MAN-DAY** |

---

## 3. CẢNH BÁO QUÁ TẢI & ĐỀ XUẤT XIN PM ĐIỀU CHỈNH KẾ HOẠCH (OVERLOAD ALERT)

> [!WARNING]
> **CẢNH BÁO QUÁ TẢI CÔNG VIỆC (OVERLOAD ALERT):**
> Tổng khối lượng công việc tồn đọng và mới giao trên Backlog hiện tại là **~13.25 giờ** (Vượt mức **+5.25 giờ** so với định mức 8.0h/ngày).

### 3.1. Danh sách các task đề xuất dời lịch sang ngày mai (26/11):
1. `SURREALDOLLS-13926`: `[Verify] Test lại luồng gacha phía app+admin trên STG (2h)`
   - **Trạng thái:** In Progress | **Est:** 1.50h
   - **Lý do lùi:** Dồn tải hoàn tất CR AP Tracking và các cụm Verify K20241, BB101, AS100 trong ngày Release 2511; chuyển sang 26/11.
2. `SURREALDOLLS-14787`: `[M2061][Test] - Emote: modal chọn 5 emote`
   - **Trạng thái:** Open | **Est:** 1.50h
   - **Lý do lùi:** Tính năng Emote chuyển thực thi vào 26/11 sau khi giải quyết xong Release 2511.
3. `SURREALDOLLS-15053` (Phase 2): `Thực thi các ca kiểm thử Medium / Boundary phụ của AP213/AP330/AP405`
   - **Est:** 1.00h $\rightarrow$ Chuyển sang sáng 26/11 để hoàn tất 100% test matrix.
4. `SURREALDOLLS-14804` & `SURREALDOLLS-14805`: `Triển khai chống quay/chụp màn hình (録画・スクショ防止)`
   - **Due Date:** 26/11/2026 $\rightarrow$ Giữ đúng tiến độ vào ngày mai.

### 3.2. Mẫu tin nhắn soạn sẵn gửi PM / Lead:
```text
Chào anh/chị PM,

Kế hoạch làm việc hôm nay (Thứ Tư, 25/11 - Ngày Release Milestone 2511) của em đã được phân bổ trọn vẹn 8.00 giờ công (1 Man-Day) để tập trung giải quyết các mục tiêu trọng điểm:
1. Nghiệm thu đóng dứt điểm cụm bug Verify STG [SURREALDOLLS-14788] (CR K20241 bảo mật hủy liên kết SĐT/SNS) và [SURREALDOLLS-15039].
2. Nghiệm thu đóng dứt điểm cụm bug Verify DEV [SURREALDOLLS-14133] (BB101) và [SURREALDOLLS-13364] (AS100).
3. Bàn giao kịch bản [SURREALDOLLS-15052] và thực thi Round 1 trọng tâm [SURREALDOLLS-15053] (CR Cài đặt tham số tracking model AP213 + AP330 + AP405 có hạn hôm nay 25/11).
4. Sanity test Hotfix [SURREALDOLLS-14806] (Connect SNS).

Do tổng tải công việc tồn đọng hiện đang ở mức 13.25h (> 8h), em xin phép:
- Dời task Verify Gacha [SURREALDOLLS-13926] và Task [SURREALDOLLS-14787] (Emote modal) sang ngày mai (26/11) để ưu tiên thông luồng release 2511 và CR Tracking Model hôm nay.
- Hoàn thiện phase 2 của task [SURREALDOLLS-15053] vào sáng mai 26/11.

Nhờ PM xem qua và duyệt giúp em kế hoạch phân bổ ngày hôm nay nhé ạ. Em cảm ơn PM!
```
