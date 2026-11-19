# KẾ HOẠCH PHÂN BỔ CÔNG VIỆC 8H/NGÀY - 20/11/2026
Theo quy chuẩn [08_task_estimation_rule.md](../Universal_Rules/08_task_estimation_rule.md) & [GEMINI.md](../GEMINI.md).

- **Assignee:** Mume_ガー（テスター） (`ngadtp@mumesoft.vn`)
- **Ngày thực hiện:** Thứ Sáu, 20/11/2026
- **Mục tiêu quỹ thời gian chuẩn:** **8.0 giờ / ngày** (1 Man-Day = 480 phút)
- **Nguồn dữ liệu:** Backlog Project `SURREALDOLLS` (https://issoh.backlog.com/)

---

## 1. TỔNG QUAN PHẠM VI QUÉT 3 NHÓM TRẠNG THÁI (3-TIER SCAN SUMMARY)

| Nhóm Trạng Thái | Số Lượng Ticket | Tổng Thời Gian (Giờ) | Quy Đổi Phút | Đánh Giá Tải & Ưu Tiên |
| :--- | :---: | :---: | :---: | :--- |
| **Nhóm 1: Need Verify (Dev & STG)** | 10 bugs con | **3.75 giờ** | 225 phút | **Ưu tiên 1 (Cao nhất):** Đóng vòng đời bug, unblock release 2511 |
| **Nhóm 2: In Progress (Đang thực hiện)** | 4 parent tasks | **7.50 giờ** | 450 phút | **Ưu tiên 2:** Tập trung hoàn thành 3 task có hạn hôm nay & ngày mai |
| **Nhóm 3: Open (Due hôm nay / ngày mai)** | 2 tasks khẩn | **3.75 giờ** | 225 phút | **Ưu tiên 3:** Hotfix SNS Connect & Task tồn M2061 Emote |
| **TỔNG KHỐI LƯỢNG CHỜ XỬ LÝ** | **19 tickets** | **~15.00 giờ** | 900 phút | ⚠️ **QUÁ TẢI (+7.00h so với định mức 8.0h/ngày)** |

---

## 2. KẾ HOẠCH THỰC THI CHUẨN 8.0H TRONG NGÀY MAI (20/11/2026)

> [!IMPORTANT]
> Toàn bộ thời gian ước lượng dưới đây đã được **quy đổi trực tiếp sang Đơn vị Giờ (h)** và khóa cứng quỹ thời gian làm việc chuẩn **8.0 giờ (1 Man-Day = 480 phút)**.

### 2.1. Chi tiết Danh Sách Tác Vụ Quy Đổi Ra Giờ

| STT | Mã Ticket | Tiêu đề Task / Bug | Môi Trường | Trạng Thái | Loại | Độ Khó | Est (Giờ) | Chi Tiết Phút | Lý Do Xếp Lịch & Hạn Chót |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **I** | **KHỐI VERIFY DEV & STG (ƯU TIÊN 1)** | | | | | | **3.75h** | **225 phút** | **Ưu tiên cao nhất: Nghiệm thu bug đóng tiến độ** |
| 1 | `SURREALDOLLS-14788` | **[Verify] K20241 CR アカウント解除のセキュリティ強化**<br>• `14795`: Lỗi thông báo liên kết SĐT (15p)<br>• `14797`: Hủy liên kết Line thông báo trắng (15p)<br>• `14807`: Gỡ liên kết SNS không mở login (20p)<br>• Smoke luồng xác thực lại & update evidence (40p) | **STG** (App iOS/Android) | In Progress | Verify Bug | Logic App | **1.50h** | 90 phút | **Hạn 20/11 (Ngày mai)**, Priority High, Milestone Release 2511 |
| 2 | `SURREALDOLLS-15039` | [BUG] - Không nhập được data cho trường お知らせ内容 | **STG** (Admin) | Need Verify (STG) | Bug | Validate | **0.25h** | 15 phút | Dev vừa fix, hạn 19/11 cần nghiệm thu STG |
| 3 | `SURREALDOLLS-14133` | **[Verify] BB100 + BB101 + BB200 + BB300**<br>• `14131`: Popup xác nhận CMMSG28 (9p)<br>• `14128`: Trùng tên admin Agency (12p)<br>• `14132`: Luồng email PEM4 認証待ち (25p)<br>• Update kết quả & evidence đóng ticket (14p) | **DEV** (Agency/Admin) | In Progress | Verify Bug | Chùm màn | **1.00h** | 60 phút | Hạn 19/11 tồn sang, Dev vừa fix 14131 chiều 19/11 |
| 4 | `SURREALDOLLS-13364` | **[Verify bug] AS100 - Test**<br>• `14224`: Không hiển thị agency tham gia (20p)<br>• `13998`: Lỗi overview ngày hôm qua (20p)<br>• `13433`: Lệch header CSV (10p)<br>• Update kết quả & evidence (10p) | **DEV** (Admin) | In Progress | Verify Bug | Logic Web | **1.00h** | 60 phút | Hạn 19/11 tồn sang, giải quyết dứt điểm các bug Dev đã fix |
| **II** | **KHỐI TASK KHẨN CẤP & OPEN CÓ HẠN 19/11 - 20/11 (ƯU TIÊN 2 & 3)** | | | | | | **4.25h** | **255 phút** | **Giải quyết task khẩn cấp và hotfix** |
| 5 | `SURREALDOLLS-14806` | **Test lại phần connect SNS (màn đăng nhập và màn liên kết tài khoản)** | **STG** (App iOS/Android) | Open | タスク (HOTFIX) | Logic/Auth | **2.00h** | 120 phút | **Hạn 20/11 (Ngày mai)**, Hotfix connect SNS màn login & account setting |
| 6 | `SURREALDOLLS-14787` | **[M2061][Test] - Emote: modal chọn 5 emote** | **DEV / STG** (App) | Open | タスク | UI/Logic | **1.75h** | 105 phút | Hạn 19/11 tồn sang ngày mai, thiết kế & chạy kịch bản chọn 5 emote |
| 7 | `ADMIN-DAILY` | **Tổng kết kết quả kiểm thử, Log bug phát sinh & Báo cáo cuối ngày** | Tổng hợp | — | Task | Tổng kết | **0.50h** | 30 phút | Cập nhật Backlog board, evidence và báo cáo tiến độ tuần |
| 🎯 | **TỔNG CỘNG THỰC THI** | **7 Cụm Tác Vụ Trọng Điểm (~15 tickets)** | — | — | — | — | **8.00 giờ** | **480 phút** | **ĐẠT CHUẨN 100% 1 MAN-DAY** |

---

## 3. CẢNH BÁO QUÁ TẢI & ĐỀ XUẤT XIN PM ĐIỀU CHỈNH KẾ HOẠCH (OVERLOAD ALERT)

> [!WARNING]
> **CẢNH BÁO QUÁ TẢI CÔNG VIỆC (OVERLOAD ALERT):**
> Tổng khối lượng công việc tồn đọng và mới giao trên Backlog hiện tại là **~15.00 giờ** (Vượt mức **+7.00 giờ** so với định mức 8.0h/ngày).

### 3.1. Danh sách các task đề xuất dời lịch sang tuần sau (23/11 - 26/11):
1. `SURREALDOLLS-13926`: `[Verify] Test lại luồng gacha phía app+admin trên STG (2h)`
   - **Trạng thái:** In Progress
   - **Hạn chót hiện tại:** 24/11/2026
   - **Lý do lùi:** Các subtask Dev đang In Review (13929, 13931, 13960, 13969, 13984) và Open (13976, 13927) chưa sẵn sàng để test trọn vẹn; chuyển sang ngày 23 - 24/11.
2. `SURREALDOLLS-15051`: `[Verify][K202] Login LINE - Verify trên DEV` (Due 23/11/2026, Est: 0.5h) $\rightarrow$ Xếp lịch thứ Hai 23/11.
3. `SURREALDOLLS-14912`: `[GMO Sec-39/40][OPS] - Report ClamAV tuần 23/11` (Due 23/11/2026, Est: 0.25h) $\rightarrow$ Xếp lịch thứ Hai 23/11.
4. `SURREALDOLLS-15052` & `SURREALDOLLS-15053`: `[Testcase] & [Test] AP213 + AP330 + AP405` (Due 25/11/2026) $\rightarrow$ Xếp lịch giữa tuần sau.

### 3.2. Mẫu tin nhắn soạn sẵn gửi PM / Lead:
```text
Chào anh/chị PM,

Kế hoạch làm việc ngày mai (Thứ Sáu, 20/11) của em đã được phân bổ trọn vẹn 8.00 giờ công (1 Man-Day) để tập trung giải quyết các mục tiêu khẩn cấp nhất:
1. Hoàn thành dứt điểm task Priority High [SURREALDOLLS-14788] (Verify CR K20241 gỡ liên kết SĐT/SNS - hạn 20/11).
2. Xử lý Hotfix [SURREALDOLLS-14806] (Test connect SNS login & account setting - hạn 20/11).
3. Đóng các cụm bug verify Dev [SURREALDOLLS-14133] (BB101 vừa fix xong) và [SURREALDOLLS-13364] (AS100).
4. Thực hiện task [SURREALDOLLS-14787] ([M2061] Emote modal).

Do tổng tải công việc tồn đọng trên board đang ở mức 15.0h (> 8h), em xin phép:
- Task luồng Gacha [SURREALDOLLS-13926] (hạn 24/11) do Dev vẫn đang In Review các subtask, em sẽ dời sang thực hiện vào đầu tuần sau (23 - 24/11).
- Các task verify phụ và report ClamAV có hạn 23/11 em sẽ thực hiện vào thứ Hai tuần tới.

Nhờ PM xem qua và duyệt giúp em kế hoạch phân bổ ngày mai nhé ạ. Em cảm ơn PM!
```
