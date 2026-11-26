# Báo cáo Kiểm thử & Lỗi: SURREALDOLLS-14793 (BX100, BY100, BY300)

- **Ticket:** [SURREALDOLLS-14793](https://issoh.backlog.com/view/SURREALDOLLS-14793) — `BX100, BY100, BY300 [Agency] User Message, Livestream Comment, List Ban (livestream chat) - Test`
- **Môi trường kiểm thử:** **DEV** (`https://admin-dev.surrealdolls.com/sign-in/agency`)
- **Tài khoản sử dụng:** Agency `a001` (ID `224`) | Liver: `Leo Leo` (ID `483`)
- **Ngày thực thi:** 2026-11-25

---

## 1. Tóm tắt Kết quả Thực thi theo Màn hình

| Màn hình | URL | Kết quả thực thi trên DEV (`a001`) | Ghi chú phạm vi |
| :--- | :--- | :--- | :--- |
| **BX100** (`利用者メッセージ`) | `/agencies/messages` | **Pass** các luồng điều hướng, tìm kiếm `Leo`/`483`, quick-nav từ BC200, chặn scope `streamer_id=999999` (HTTP 403) | `Leo Leo` hiện có **0 hội thoại** (`該当するメッセージがありません。`), nên chưa test được luồng xem/sửa/xóa tin nhắn thực tế |
| **BY100** (`配信コメント`) | `/streams/messages` | **Pass** điều hướng, quick-nav BC200, tìm kiếm, lọc loại (`全て`/`通常`/`BC`), lọc ngày, sort (`視聴数が多い`/`コメント数が多い`), `クリア`, xem chi tiết stream `iiii`/`okkkm`/`test01`, lọc loại comment, `コメント検索`, lọc `参加者`, modal xóa (hủy `いいえ`), BAN `Nga Phg` -> **Phát hiện 3 lỗi UI/Network** | Chưa có data `2ショット`/`ファミリア限定`/`カラオケ`/`OBS`/`● LIVE`/`通報`/`退所済み` trên `a001` |
| **BY300** (`配信コメント・BAN管理`) | `/agencies/streams/ban-chat-list` | **Pass** toàn bộ luồng end-to-end (BAN `Nga Phg` từ BY100 -> hiển thị tại BY300 -> tìm kiếm/lọc/sort -> quick-nav BC200 -> mở modal `コメントBAN詳細` -> bấm `解除` chạy ngay không dialog -> `BANされた回数` giữ nguyên `1` -> quay lại BY100 nút `BAN` bật lại) | Chưa có data `停止中`/`退会済み`/`運営 BAN`/phân trang >10 dòng trên `a001` |

---

## 2. Danh sách Lỗi phát hiện (Bugs)

### [BUG] [BY100] [Datepicker] Chữ ngày đã chọn ở ô `開始日` bị tràn chạm vào dấu `〜`
- **Mức độ (Severity):** Minor (UI/CSS)
- **Môi trường:** DEV (`https://admin-dev.surrealdolls.com/streams/messages`) | Agency `a001`
- **Các bước tái hiện:**
  1. Mở màn hình `BY100` (`/streams/messages`).
  2. Chọn `開始日` = `2026年10月16日`.
  3. Quan sát khu vực nút chọn ngày `開始日 〜 終了日`.
- **Kết quả kỳ vọng:** Ngày `2026年10月16日` hiển thị gọn bên trong ô `開始日`, có khoảng cách rõ ràng với dấu `〜`.
- **Kết quả thực tế:** Chuỗi `2026年10月16日` bị tràn nhẹ sang phải, sát/chạm vào ký tự phân cách `〜`.
- **Bằng chứng:** `evidence/SURREALDOLLS-14793/evidence_BY100_date_overflow_DEV_FAIL.png`

---

### [BUG] [BY100] [Log Comment / Gift] Tên gift và giá GP hiển thị dính liền không có khoảng trắng/dấu phân cách
- **Mức độ (Severity):** Minor (UI/Formatting)
- **Môi trường:** DEV (`https://admin-dev.surrealdolls.com/streams/messages/32158`) | Agency `a001`
- **Các bước tái hiện:**
  1. Mở màn hình `BY100` (`/streams/messages`).
  2. Chọn stream có gift (ví dụ: `iiii` - `32158`, `okkkm` - `32163`, `test01` - `31853`).
  3. Quan sát dòng log hệ thống hiển thị gift.
- **Kết quả kỳ vọng:** Tên gift và số GP có khoảng trắng hoặc dấu phân cách rõ ràng (ví dụ: `123 2,500GPをあげました`).
- **Kết quả thực tế:** Tên gift và giá GP dính liền nhau: `1232,500GPをあげました`, `S_effect15,000GPをあげました`, `111100GPをあげました`.
- **Bằng chứng:** `evidence/SURREALDOLLS-14793/evidence_BY100_gift_concat_DEV_FAIL.png`

---

### [BUG] [BY100] [Avatar & Comment Filter API] Ảnh S3 cũ lỗi `ERR_BLOCKED_BY_ORB` và lỗi `HTTP 400` khi toggle nhanh bộ lọc loại comment
- **Mức độ (Severity):** Minor
- **Môi trường:** DEV (`https://admin-dev.surrealdolls.com/streams/messages/31853`) | Agency `a001`
- **Ghi nhận thực tế:**
  1. Một số ảnh avatar S3 cũ (`live2d-dev.s3...`) trả về `ERR_BLOCKED_BY_ORB` trên Console/Network và fallback về chữ cái đầu.
  2. Khi bật/tắt nhanh liên tiếp các nút lọc loại comment (`システム` / `通常` / `通報` / `ナイショ`), request `POST /api/v1/my-agency/streams/messages/comments/` trả về `HTTP 400` thoáng qua (thao tác với tốc độ bình thường trả về `HTTP 200`).

---

## 3. Bằng chứng Đính kèm (Pass Flow)
- **BY300 Modal `コメントBAN詳細` & Unban:** `evidence/SURREALDOLLS-14793/evidence_BY300_modal_detail_DEV_PASS.png`
- **BX100 Chọn Liver `Leo Leo`:** `evidence/SURREALDOLLS-14793/evidence_BX100_selected_DEV_PASS.png`
