# BÁO CÁO XÁC MINH LỖI TICKET SURREALDOLLS-15049
## [BUG] - [ADMIN] - Tab title (document.title) sai / thiếu prefix ở một số màn Admin
### Áp dụng: Master Agent Policy (GEMINI.md) & Trụ cột 6 (06_bug_reporting_rule.md)

---

## 1. THÔNG TIN TỔNG QUAN

- **Ticket ID:** [SURREALDOLLS-15049](https://issoh.backlog.com/view/SURREALDOLLS-15049)
- **Màn hình / Phân hệ:** Web Admin (Chùm màn hình Messages, Forgot Password, Gachas)
- **Môi trường định tuyến:** **DEV** (URL: `https://admin-dev.surrealdolls.com`)
- **Tài khoản kiểm thử:** Admin `admin@admin.com` & Agency (HTTP Basic Auth: `suriaru` / `suriaru`)
- **Trạng thái Backlog tiếp nhận:** `Need Verify (Dev)`
- **Thời lượng ước tính (Est):** 0.15h (9 phút)
- **Thời lượng thực tế (Actual):** 0.15h (9 phút)
- **Tester:** `NgaDTP` / `Antigravity QA`
- **Ngày kiểm tra:** 20/11/2026
- **Kết luận:** <span style="color:green; font-weight:bold;">VERIFIED PASS (ĐÃ SỬA XONG TRÊN DEV)</span>

---

## 2. KẾT QUẢ ĐỐI SOÁT CHI TIẾT

| STT | Màn hình / URL | Tiêu chí | Kết quả cũ (Old Actual) | Kết quả kỳ vọng (Expected) | Kết quả thực tế live DEV (New Actual) | Đánh giá |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| 1 | `/messages` (Hệ thống tin nhắn) | Tab title (`document.title`) | `Surreal Dolls - 利用者メッセージ` (Sai tên màn hình) | `Surreal Dolls - システムメッセージ` | `Surreal Dolls - システムメッセージ` | <span style="color:green; font-weight:bold;">PASS</span> |
| 2 | `/messages/ALL_USER` (Chi tiết tin nhắn hệ thống) | Tab title (`document.title`) | `利用者メッセージ - 会話詳細` (Sai tên màn, thiếu prefix) | `Surreal Dolls - システムメッセージ - 会話詳細` | `Surreal Dolls - システムメッセージ - 会話詳細` | <span style="color:green; font-weight:bold;">PASS</span> |
| 3 | `/forgot-password/agency` (Quên mật khẩu Agency) | Tab title (`document.title`) | `パスワードを忘れた方` (Thiếu prefix) | `Surreal Dolls - パスワードを忘れた方` | `Surreal Dolls - パスワードを忘れた方` | <span style="color:green; font-weight:bold;">PASS</span> |
| 4 | `/gachas/detail/{id}/normal` (Chi tiết Gacha Normal) | Tab title (`document.title`) | `アバター一覧` (Sai tên màn, thiếu prefix) | `Surreal Dolls - ノーマルアバターガチャ` | `Surreal Dolls - ノーマルアバターガチャ` | <span style="color:green; font-weight:bold;">PASS</span> |

### Kiểm tra hồi quy bổ sung (Regression Check):
- `/gachas/detail/{id}/limited`: `Surreal Dolls - 期間限定アバターガチャ` $\rightarrow$ <span style="color:green; font-weight:bold;">PASS</span>
- `/forgot-password` (Admin Forgot Password): `Surreal Dolls - パスワードを忘れた方` $\rightarrow$ <span style="color:green; font-weight:bold;">PASS</span>
- `/users/messages` (Tin nhắn người dùng): `Surreal Dolls - 利用者メッセージ` $\rightarrow$ <span style="color:green; font-weight:bold;">PASS</span>
- `/streams/messages` (Bình luận livestream): `Surreal Dolls - 配信コメント` $\rightarrow$ <span style="color:green; font-weight:bold;">PASS</span>

---

## 3. BẰNG CHỨNG KIỂM THỬ (EVIDENCE)

Toàn bộ ảnh chụp thực tế đã được inject khung viền nổi bật (Bounding Box viền xanh lá `#16a34a` 3px) và badge nhận diện trực quan:

1. **Màn `/messages`:**
   - Link file: [evidence_SURREALDOLLS-15049_DEV_PASS_messages.png](file:///home/nga/Documents/SurrealDoll/evidence/SURREALDOLLS-15049/evidence_SURREALDOLLS-15049_DEV_PASS_messages.png)
   - Giá trị `document.title`: `Surreal Dolls - システムメッセージ`

2. **Màn `/messages/ALL_USER`:**
   - Link file: [evidence_SURREALDOLLS-15049_DEV_PASS_messages_detail.png](file:///home/nga/Documents/SurrealDoll/evidence/SURREALDOLLS-15049/evidence_SURREALDOLLS-15049_DEV_PASS_messages_detail.png)
   - Giá trị `document.title`: `Surreal Dolls - システムメッセージ - 会話詳細`

3. **Màn `/forgot-password/agency`:**
   - Link file: [evidence_SURREALDOLLS-15049_DEV_PASS_forgot_password_agency.png](file:///home/nga/Documents/SurrealDoll/evidence/SURREALDOLLS-15049/evidence_SURREALDOLLS-15049_DEV_PASS_forgot_password_agency.png)
   - Giá trị `document.title`: `Surreal Dolls - パスワードを忘れた方`

4. **Màn `/gachas/detail/51/normal`:**
   - Link file: [evidence_SURREALDOLLS-15049_DEV_PASS_gacha_normal.png](file:///home/nga/Documents/SurrealDoll/evidence/SURREALDOLLS-15049/evidence_SURREALDOLLS-15049_DEV_PASS_gacha_normal.png)
   - Giá trị `document.title`: `Surreal Dolls - ノーマルアバターガチャ`

5. **Màn `/gachas/detail/51/limited` (Regression):**
   - Link file: [evidence_SURREALDOLLS-15049_DEV_PASS_gacha_limited.png](file:///home/nga/Documents/SurrealDoll/evidence/SURREALDOLLS-15049/evidence_SURREALDOLLS-15049_DEV_PASS_gacha_limited.png)
   - Giá trị `document.title`: `Surreal Dolls - 期間限定アバターガチャ`

---

## 4. ĐỀ XUẤT ĐỒNG BỘ BACKLOG

> [!CAUTION]
> Tuân thủ Ranh giới đỏ: Tester/Agent không tự ý chuyển trạng thái trên Backlog. Dưới đây là đề xuất để Tester/Người dùng chủ động cập nhật:

- **Trạng thái đề xuất:** Chuyển sang **`WaitBuid(STG)-PM`** (Chờ merge PR release/20261118 và build STG để kiểm tra vòng 2).
- **Thời lượng thực tế (Actual Time):** `0.15h` (9 phút)
- **Mẫu comment đề xuất copy lên Backlog:**
```markdown
Đã tiến hành xác minh lại lỗi trên môi trường **DEV** (URL: `https://admin-dev.surrealdolls.com`):
- **Kết quả:** Bug đã được khắc phục hoàn toàn theo đúng đặc tả trên môi trường DEV:
  + `/messages` → `Surreal Dolls - システムメッセージ` (PASS)
  + `/messages/ALL_USER` → `Surreal Dolls - システムメッセージ - 会話詳細` (PASS)
  + `/forgot-password/agency` → `Surreal Dolls - パスワードを忘れた方` (PASS)
  + `/gachas/detail/{id}/normal` → `Surreal Dolls - ノーマルアバターガチャ` (PASS)
  + Regression: `/gachas/detail/{id}/limited`, `/forgot-password`, `/users/messages`, `/streams/messages` đều hiển thị đúng prefix và tiêu đề.
- **Bằng chứng xác thực:** Đã kiểm tra và lưu 5 ảnh bằng chứng màn hình kèm giá trị document.title.
- **Trạng thái:** Chuyển sang **WaitBuid(STG)-PM** chờ build STG.
- **Actual Time:** 0.15h
```
