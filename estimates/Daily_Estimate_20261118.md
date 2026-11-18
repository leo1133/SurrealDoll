# KẾ HOẠCH PHÂN BỔ CÔNG VIỆC 8H/NGÀY - 18/11/2026
Theo quy chuẩn [08_task_estimation_rule.md](../Universal_Rules/08_task_estimation_rule.md) & [GEMINI.md](../GEMINI.md).

- **Assignee:** Mume_ガー（テスター） (`ngadtp@mumesoft.vn`)
- **Ngày thực hiện:** Thứ Tư, 18/11/2026
- **Mục tiêu quỹ thời gian chuẩn:** **8.0 giờ / ngày** (1 Man-Day = 480 phút)
- **Nguồn dữ liệu:** Backlog Project `SURREALDOLLS` (https://issoh.backlog.com/)

---

## 1. TỔNG QUAN PHẠM VI QUÉT 3 NHÓM TRẠNG THÁI (3-TIER SCAN SUMMARY)

| Nhóm Trạng Thái | Số Lượng Ticket | Tổng Thời Gian (Giờ) | Quy Đổi Phút | Đánh Giá Tải & Ưu Tiên |
| :--- | :---: | :---: | :---: | :--- |
| **Nhóm 1: Need Verify (Dev & STG)** | 16 bugs | **4.33 giờ** | 260 phút | **Ưu tiên 1 (Cao nhất):** Đóng vòng đời bug, unblock release 1811 |
| **Nhóm 2: In Progress (Đang thực hiện)** | 4 tasks | **3.67 giờ** | 220 phút | **Ưu tiên 2:** Hoàn tất các chùm testcase đang dang dở có hạn hôm nay |
| **Nhóm 3: Open (Due hôm nay / ngày mai)** | 1 task | **2.00 giờ** | 120 phút | **Ưu tiên 3:** Task mới `M2061` bắt đầu từ 19/11 (Ngày mai) |
| **TỔNG KHỐI LƯỢNG TỒN ĐỌNG** | **21 tickets** | **~10.00 giờ** | 600 phút | ⚠️ **QUÁ TẢI (+2.00h so với định mức 8.0h/ngày)** |

---

## 2. KẾ HOẠCH THỰC THI CHUẨN 8.0H TRONG NGÀY HÔM NAY (18/11/2026)

> [!IMPORTANT]
> Toàn bộ thời gian ước lượng dưới đây đã được **quy đổi trực tiếp sang Đơn vị Giờ (h)** và khóa cứng quỹ thời gian làm việc chuẩn **8.0 giờ (1 Man-Day)**.

### 2.1. Chi tiết Danh Sách Tác Vụ Quy Đổi Ra Giờ

| STT | Mã Ticket | Tiêu đề Task / Bug | Trạng Thái | Loại | Độ Khó | Est (Giờ) | Chi Tiết Phút | Lý Do Xếp Lịch & Hạn Chót |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **I** | **KHỐI VERIFY DEV & STG (ƯU TIÊN 1)** | | | | | **4.33 giờ** | **260 phút** | **Ưu tiên cao nhất: Đóng vòng đời bug release 1811** |
| 1 | `SURREALDOLLS-14129` | [BUG] - [BB101] - Không hiển thị Toast thông báo CMMSG14 khi xác nhận xóa logo trong Modal | Need Verify (Dev) | Bug | Validate | **0.15h** | 9 phút | Hạn 18/11, check toast CMMSG14 |
| 2 | `SURREALDOLLS-14127` | [BUG] - [BB300] - Không điều hướng về màn hình danh sách BB100 sau khi xóa quản trị viên thành công | Need Verify (Dev) | Bug | Logic | **0.37h** | 22 phút | Hạn 18/11, check redirect router |
| 3 | `SURREALDOLLS-14125` | [BUG] - [BB300] - Sai lệch nội dung thông báo lỗi định dạng email khi chỉnh sửa quản trị viên | Need Verify (Dev) | Bug | Validate | **0.15h** | 9 phút | Hạn 18/11, check regex email |
| 4 | `SURREALDOLLS-14123` | [BUG] - [BB200] - Sai lệch nội dung thông báo lỗi định dạng email | Need Verify (Dev) | Bug | Validate | **0.15h** | 9 phút | Hạn 18/11, check regex email |
| 5 | `SURREALDOLLS-13450` | [CR] - Update hiển thị thời gian chạy batch lần gần nhất | Need Verify (STG) | CR | UI/Logic | **0.28h** | 17 phút | STG Tồn đọng, check format datetime batch |
| 6 | `SURREALDOLLS-14374` | [BUG] [BA1001] Thông báo lỗi sai định dạng email hiển thị không đúng theo tài liệu đặc tả | Need Verify (STG) | Bug | Validate | **0.15h** | 9 phút | STG Tồn đọng, check MSG BA1001 |
| 7 | `SURREALDOLLS-14376` | [BUG] - Tạo mới agency/admin agency cho phép nhập email có đuôi +@gmail.com nhưng khi reset mật khẩu thì báo lỗi mail | Need Verify (STG) | Bug | Logic | **0.37h** | 22 phút | STG Tồn đọng, check sub-addressing email |
| 8 | `SURREALDOLLS-14164` | [BUG] - [AH300 お知らせ詳細] - Nội dung có cùng 1 ảnh 2 lần: mở lại thì ảnh vỡ (URL presigned lồng nhau) | Need Verify (STG) | Bug | Logic | **0.37h** | 22 phút | STG Tồn đọng, check presigned S3 url |
| 9 | `SURREALDOLLS-14152` | [BUG] - [アバターガチャ ガチャ設定] - Sửa item ボディ / アクセ: variant có 重複数「ー」 bị bỏ khỏi payload | Need Verify (STG) | Bug | Logic | **0.37h** | 22 phút | STG Tồn đọng, check payload JSON DB |
| 10 | `SURREALDOLLS-14153` | [BUG] - [AP221 共通アクセから選択] - 共通アクセ có 色変更 (drawable) bị báo lỗi tham số | Need Verify (STG) | Bug | Logic | **0.37h** | 22 phút | STG Tồn đọng, check tham số màu model |
| 11 | `SURREALDOLLS-14165` | [BUG] - [AP400 アクセ設定 / 頭・体変更] - Unity không trả anchor thì loading không tắt, khoá chức năng | Need Verify (STG) | Bug | Logic | **0.37h** | 22 phút | STG Tồn đọng, check error handling Unity |
| 12 | `SURREALDOLLS-14172` | [BUG] - [AP300 モデル詳細(ボディ) 共通アクセから選択] - Rò rỉ tham số giữa màn Head và Body | Need Verify (STG) | Bug | Logic | **0.37h** | 22 phút | STG Tồn đọng, check state cache |
| 13 | `SURREALDOLLS-14147` | [BUG] - [BE200 投稿詳細] - 「さらに回答を見る」 lỗi API rồi bấm lại thì bỏ qua 1 trang reply | Need Verify (STG) | Bug | Logic | **0.37h** | 22 phút | STG Tồn đọng, check offset pagination |
| 14 | `SURREALDOLLS-14150` | [BUG] - [事務所 配信詳細] - Stream 2ショット: 「ユーザー一覧：N人」 tính sai | Need Verify (STG) | Bug | Logic | **0.37h** | 22 phút | STG Tồn đọng, check logic đếm viewer |
| 15 | `SURREALDOLLS-14151` | [BUG] - [事務所 配信一覧] - Nhấn Enter / Space trên nút âm thanh preview mở nhầm tab chi tiết | Need Verify (STG) | Bug | UI/Event | **0.20h** | 12 phút | STG Tồn đọng, check event bubbling |
| 16 | `SURREALDOLLS-13954` | [BUG] - [事務所 通報詳細] - Link trong 通報詳細 của portal 事務所 trỏ nhầm sang system-admin | Need Verify (STG) | Bug | UI | **0.12h** | 7 phút | STG Tồn đọng, check href domain agency |
| **II** | **KHỐI IN PROGRESS CÓ DUE HÔM NAY 18/11 (ƯU TIÊN 2)** | | | | | **3.67 giờ** | **220 phút** | **Hoàn thành dứt điểm WIP trong ngày** |
| 17 | `SURREALDOLLS-14133` | [verify] BB100 + BB101 + BB200 + BB300 (1h) 2/11 | In Progress | Verify Bug | Chùm màn | **0.50h** | 30 phút | Cập nhật tiến độ sau khi verify 4 bug BB |
| 18 | `SURREALDOLLS-14357` | [Verify] BA100 + BA200 + BA1001 + BA1002 + BA1003 - Test (0.5) 0/3 | In Progress | Verify Bug | Chùm màn | **0.50h** | 30 phút | Cập nhật sau khi verify bug 14374, 14376 |
| 19 | `SURREALDOLLS-14788` | [Verify] - [K20241] CR アカウント解除のセキュリティ強化 - Gỡ liên kết SĐT/SNS phải xác thực lại - Test STG iOS/Android 2/8 | In Progress | Verify Bug | Logic App | **1.50h** | 90 phút | Hạn hôm nay 18/11, verify luồng xác thực |
| 20 | `SURREALDOLLS-13364` | [Verify bug] AS100 - Test 20/27 | In Progress | Verify Bug | Logic Web | **1.17h** | 70 phút | Hạn hôm nay 18/11, chốt các case AS100 |
| 🎯 | **TỔNG CỘNG THỰC THI** | **20 Tác Vụ Trọng Điểm** | — | — | — | **8.00 giờ** | **480 phút** | **ĐẠT CHUẨN 100% 1 MAN-DAY** |

---

## 3. CẢNH BÁO QUÁ TẢI & ĐỀ XUẤT XIN PM ĐIỀU CHỈNH KẾ HOẠCH (OVERLOAD ALERT)

> [!WARNING]
> **CẢNH BÁO QUÁ TẢI CÔNG VIỆC TRONG NGÀY (OVERLOAD ALERT):**
> Tổng khối lượng công việc đang chờ thực hiện trên Backlog là **~10.00 giờ** (Vượt mức **+2.00 giờ** so với định mức 8.0h/ngày).

### 3.1. Danh sách các task đề xuất dời lịch:
1. `SURREALDOLLS-14787`: `[M2061][Test] - Emote: modal chọn 5 emote`
   - **Trạng thái:** Open
   - **Ước tính:** **2.00 giờ**
   - **Hạn chót hiện tại:** 19/11/2026 (Ngày mai)
   - **Đề xuất:** Xếp lịch thực hiện chính vào ngày mai **19/11/2026** sau khi giải phóng toàn bộ 16 bug Verify tồn đọng hôm nay.
2. `SURREALDOLLS-13926`: `[Verify] Test lại luồng gacha phía app+admin trên STG (2h) 1/8`
   - **Trạng thái:** In Progress
   - **Ước tính:** **2.00 giờ**
   - **Hạn chót hiện tại:** 25/11/2026
   - **Đề xuất:** Giữ nguyên lịch tiếp tục làm vào các ngày 20 - 24/11 (chưa gấp trong ngày 18/11).

### 3.2. Mẫu tin nhắn soạn sẵn gửi PM / Lead:
```text
Chào anh/chị PM,

Hôm nay (18/11), phía QA em cần tập trung dồn toàn lực xử lý dứt điểm 16 bug đang ở trạng thái Need Verify trên Dev & STG (phục vụ đóng vòng đời kịp mốc Release 1811) cùng 4 task In Progress có hạn chót trong ngày hôm nay (BB cluster, BA cluster, K20241, AS100). 

Tổng khối lượng thực thi thực tế đã đạt đủ 8.00 giờ công (1 Man-Day). Do đó:
- Task mới [SURREALDOLLS-14787] ([M2061][Test] - Emote: modal chọn 5 emote - Est 2.0h) em sẽ bắt đầu triển khai vào sáng mai (19/11) theo đúng kế hoạch.
- Task gacha [SURREALDOLLS-13926] (hạn 25/11 - Est 2.0h) em xin phép tiếp tục chạy vào các ngày kế tiếp sau đợt verify release 1811 này.

Nhờ PM xem qua và xác nhận giúp em kế hoạch phân bổ công việc hôm nay nhé ạ. Em cảm ơn PM!
```
