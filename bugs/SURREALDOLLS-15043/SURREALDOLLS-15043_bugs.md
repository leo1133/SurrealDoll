# BÁO CÁO XÁC MINH LỖI TICKET SURREALDOLLS-15043
## [BUG] - [AJ100 / AJ200] - BGM: Bấm 新規登録 / mở /bgm/create bị chuyển về ダッシュボード, không tạo được BGM
### Áp dụng: Master Agent Policy (GEMINI.md) & Trụ cột 6 (06_bug_reporting_rule.md)

---

## 1. THÔNG TIN TỔNG QUAN

- **Ticket ID:** [SURREALDOLLS-15043](https://issoh.backlog.com/view/SURREALDOLLS-15043)
- **Màn hình / Phân hệ:** `AJ100` (BGM一覧) / `AJ200` (BGM登録) - Quản lý BGM (Web Admin)
- **Môi trường định tuyến:** **DEV** (URL: `https://admin-dev.surrealdolls.com`)
- **Tài khoản kiểm thử:** Admin `admin@admin.com` (HTTP Basic Auth: `suriaru` / `suriaru`)
- **Trạng thái Backlog tiếp nhận:** `Need Verify (Dev)`
- **Thời lượng ước tính (Est):** 0.15h (9 phút)
- **Thời lượng thực tế (Actual):** 0.15h (9 phút)
- **Tester:** `NgaDTP` / `Antigravity QA`
- **Ngày kiểm tra:** 20/11/2026
- **Kết luận:** <span style="color:green; font-weight:bold;">VERIFIED PASS (ĐÃ SỬA XONG TRÊN DEV)</span>

---

## 2. KẾT QUẢ ĐỐI SOÁT CHI TIẾT

| STT | Vị trí / Thao tác | Tiêu chí | Kết quả cũ (Old Actual Result) | Kết quả kỳ vọng (Expected Result) | Kết quả thực tế live DEV (New Actual Result) | Đánh giá |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| 1 | **Sidebar Menu BGM管理** | Hiển thị menu con | Chỉ có mục `BGM一覧`, không có mục `BGM登録` | Có cả 2 menu con: `BGM一覧` (`/bgm`) và `BGM登録` (`/bgm/create`) | Đã hiển thị đầy đủ 2 menu con: `BGM一覧` và `BGM登録` trỏ link chuẩn `/bgm/create` | <span style="color:green; font-weight:bold;">PASS</span> |
| 2 | **Màn BGM一覧 (`/bgm`)** | Nút `新規登録` trên Header bảng | Bấm `新規登録` bị điều hướng về Dashboard `/` với thông báo 「機能はまだ開発中」 | Điều hướng thành công đến màn BGM登録 (`/bgm/create` - AJ200) | Nút `新規登録` (thẻ `<a>` trỏ `/bgm/create`) click chuyển hướng mượt mà sang `/bgm/create` | <span style="color:green; font-weight:bold;">PASS</span> |
| 3 | **Truy cập trực tiếp `/bgm/create`** | Route `/bgm/create` (AJ200) | Bị redirect về Dashboard (`/`) kèm message 「機能はまだ開発中」 | Hiển thị trọn vẹn màn hình BGM登録 (AJ200), không bị redirect | Mở thẳng form BGM登録 (`https://admin-dev.surrealdolls.com/bgm/create`), Document Title: `Surreal Dolls - BGM登録`, H1: `BGM登録` | <span style="color:green; font-weight:bold;">PASS</span> |
| 4 | **Form BGM登録 (AJ200)** | Các trường nhập liệu & Controls | Không thể mở màn hình | Hiển thị đầy đủ form tạo mới BGM gồm: Tiêu đề, Upload file âm thanh, Trạng thái, Thứ tự sắp xếp, nút Hủy, nút Đăng ký | Đầy đủ: Input Tiêu đề, Upload MP3/WAV (max 10MB), Radio Status (公開/非公開), Input 並び順, nút キャンセル, 登録 | <span style="color:green; font-weight:bold;">PASS</span> |
| 5 | **Validation Form BGM登録** | Bấm `登録` khi để trống các trường bắt buộc | Không kiểm tra được | Kích hoạt validation hiển thị thông báo lỗi tương ứng cho các trường bắt buộc | Hiển thị đúng 3 thông báo lỗi validation:<br>• `BGMタイトルは空欄にできません。`<br>• `BGM音源は空欄にできません。`<br>• `並び順は空欄にできません。` | <span style="color:green; font-weight:bold;">PASS</span> |
| 6 | **Nút Cancel (`キャンセル`)** | Click `キャンセル` trên màn `/bgm/create` | Không kiểm tra được | Quay trở lại màn hình danh sách BGM一覧 (`/bgm`) | Điều hướng chuẩn xác quay về `https://admin-dev.surrealdolls.com/bgm` | <span style="color:green; font-weight:bold;">PASS</span> |

---

## 3. BẰNG CHỨNG KIỂM THỬ (EVIDENCE)

Toàn bộ ảnh chụp thực tế đã được inject khung viền nổi bật (Bounding Box viền xanh lá `#16a34a` 3px) và badge nhận diện trực quan trong vòng 3 giây:

1. **Nút `新規登録` & Menu Sidebar `BGM登録` trên màn BGM一覧 (`/bgm`):**
   - Link file: [evidence_SURREALDOLLS-15043_DEV_PASS_bgm_list_register_button.png](file:///home/nga/Documents/SurrealDoll/evidence/SURREALDOLLS-15043/evidence_SURREALDOLLS-15043_DEV_PASS_bgm_list_register_button.png)
   - Chi tiết: Nút `新規登録` trỏ link `/bgm/create`, Sidebar hiển thị đủ mục `BGM一覧` và `BGM登録`.

2. **Màn hình Form BGM登録 (`/bgm/create` - AJ200):**
   - Link file: [evidence_SURREALDOLLS-15043_DEV_PASS_bgm_create_screen.png](file:///home/nga/Documents/SurrealDoll/evidence/SURREALDOLLS-15043/evidence_SURREALDOLLS-15043_DEV_PASS_bgm_create_screen.png)
   - Chi tiết: Truy cập trực tiếp URL `https://admin-dev.surrealdolls.com/bgm/create` thành công, `document.title = "Surreal Dolls - BGM登録"`, giao diện form AJ200 hiển thị đầy đủ, không bị chuyển hướng về Dashboard.

3. **Validation & Chi tiết Form BGM登録:**
   - Link file: [evidence_SURREALDOLLS-15043_DEV_PASS_bgm_create_validation.png](file:///home/nga/Documents/SurrealDoll/evidence/SURREALDOLLS-15043/evidence_SURREALDOLLS-15043_DEV_PASS_bgm_create_validation.png)
   - Chi tiết: Bấm `登録` kích hoạt đầy đủ 3 validation message cho BGMタイトル, BGM音源, 並び順.

---

## 4. ĐỀ XUẤT ĐỒNG BỘ BACKLOG

> [!CAUTION]
> **Tuân thủ Ranh giới đỏ (Master Agent Policy):** Tester/Agent không tự ý thao tác chuyển trạng thái ticket trên Backlog. Dưới đây là đề xuất chuẩn bị sẵn để Tester / Người dùng chủ động cập nhật:

- **Trạng thái đề xuất:** Chuyển sang **`WaitBuid(STG)-PM`** (hoặc `Resolved` nếu quy trình kiểm tra trực tiếp trên STG sau khi deploy).
- **Thời lượng thực tế (Actual Time):** `0.15h` (9 phút)
- **Mẫu comment đề xuất copy lên Backlog:**
```markdown
Đã tiến hành xác minh lại lỗi trên môi trường **DEV** (URL: `https://admin-dev.surrealdolls.com`):
- **Kết quả:** Bug đã được khắc phục hoàn toàn trên môi trường DEV:
  + Sidebar `BGM管理`: Đã bổ sung mục `BGM登録` (`/bgm/create`) bên cạnh `BGM一覧` (`/bgm`).
  + Màn BGM一覧 (`/bgm`): Nút `新規登録` điều hướng chuẩn xác sang `/bgm/create` (AJ200).
  + Màn BGM登録 (`/bgm/create`): Không còn bị redirect về Dashboard (`/`), form đăng ký BGM hiển thị trọn vẹn (Title: `Surreal Dolls - BGM登録`, đầy đủ controls và validation hoạt động chính xác).
  + Nút `キャンセル`: Điều hướng quay trở về màn `BGM一覧` an toàn.
- **Bằng chứng xác thực:** Đã kiểm tra thực tế và lưu 3 ảnh bằng chứng màn hình:
  + `evidence_SURREALDOLLS-15043_DEV_PASS_bgm_list_register_button.png`
  + `evidence_SURREALDOLLS-15043_DEV_PASS_bgm_create_screen.png`
  + `evidence_SURREALDOLLS-15043_DEV_PASS_bgm_create_validation.png`
- **Trạng thái đề xuất:** Chuyển sang **WaitBuid(STG)-PM** (chờ build STG để kiểm tra vòng 2).
- **Actual Time:** 0.15h
```
