# BẢNG TEST CASE VÀ KẾT QUẢ KIỂM THỬ THỦ CÔNG - CR NÂNG GIỚI HẠN DUNG LƯỢNG FILE BACKGROUND (10MB)
## Màn hình: AK202 + AK203 + AK302 + AK303 (Quản Lý Ảnh Nền Livestream & 箱庭 - Admin Web)
### Thuộc Task: [SURREALDOLLS-13887](https://issoh.backlog.com/view/SURREALDOLLS-13887) | CR Date: 30/10/2026 | Quy chuẩn: [04_manual_test_execution_rule.md](../Universal_Rules/04_manual_test_execution_rule.md)
### Môi trường kiểm thử: **Dev-Admin** (`https://admin-dev.surrealdolls.com/`) theo cấu hình tại [TEST_CONFIG.md](../TEST_CONFIG.md)
### Tài liệu Spec: [Google Sheet Spec Tổng (gid=741302995)](https://docs.google.com/spreadsheets/d/1pxox5GcjOXwKadMnzOa765ptG2huPJSxCiWsrH0_h7Y/edit#gid=741302995) (Tabs `AK202`, `AK203`, `AK302`, `AK303`)
### Test Case Master: [Google Sheet Admin Master](https://docs.google.com/spreadsheets/d/1ZaL8llNgH6sCxpG-daLEi21IxXFpub-BbrRJRdUNMOg/edit#gid=381991579) (Tabs `AK302`, `AK303`)

---

## 1. TỔNG QUAN NỘI DUNG CHANGE REQUEST (CR SCOPE)

Căn cứ theo đặc tả yêu cầu thay đổi tại Spec (mục Item 4 `背景画像` trên cả 4 tab `AK202`, `AK203`, `AK302`, `AK303`):
- **Nội dung CR (CR30/10/2026):** Nâng giới hạn dung lượng file background tối đa từ **5MB** lên **10MB**.
- **Định dạng file cho phép:** `PNG`, `JPG / JPEG`, `SVG`, `WebP`.
- **Dung lượng tối đa cho phép:** `10MB` (dung lượng <= 10MB hợp lệ, > 10MB bị từ chối).
- **Text hướng dẫn dưới ô Upload:**
  ```text
  アップロード可能な画像形式：PNG、JPG／JPEG、SVG、WebP
  最大ファイルサイズ：10MB
  ```
- **Thông báo lỗi khi vượt quá dung lượng:** Toast message `ファイルサイズは10MB以下にしてください。`
- **Thông báo lỗi khi sai định dạng:** Toast message `無効な画像形式です。サポート形式: JPG、 JPEG、 PNG、 WEBP、 SVG。`
- **Thông báo lỗi khi bỏ trống ảnh bắt buộc:** `背景画像は空欄にできません。`
- **Hệ thống áp dụng:** Master Admin Web:
  1. `AK202` - イラスト背景登録 (Illustration Background Create): `/backgrounds/illustrations/create`
  2. `AK203` - イラスト背景更新 (Illustration Background Edit): `/backgrounds/illustrations/detail/{id}`
  3. `AK302` - 箱庭背景登録 (Mini Garden Background Create): `/backgrounds/mini-garden/create`
  4. `AK303` - 箱庭背景更新 (Mini Garden Background Edit): `/backgrounds/mini-garden/detail/{id}`

---

## 2. BẢNG THỐNG KÊ KẾT QUẢ THỰC THI (TEST EXECUTION SUMMARY)

| Chỉ số kiểm thử | Số lượng / Tỷ lệ | Đánh giá chất lượng |
| :--- | :---: | :---: |
| **Tổng số kịch bản kiểm thử thực thi (Total Executed)** | **32 / 32** | **100.0%** kịch bản đã chạy |
| **Số ca kiểm thử ĐẠT (Pass)** | **32 / 32** | **100.0% Pass Rate** |
| **Số ca kiểm thử KHÔNG ĐẠT (Fail)** | **0 / 32** | **0.0%** (Không phát sinh lỗi) |
| **Retest lỗi cũ liên quan (`SURREALDOLLS-4682`)** | **1 / 1 ca Pass** | Đã khắc phục & hiển thị đúng text 10MB |
| **Cập nhật kết quả lên Google Sheet Master** | **Đã ghi nhận** | Cập nhật Round 2 tại tab `AK302` và `AK303` |
| **Đánh giá nghiệm thu (Sign-off Status)** | **PASS** | **Đủ điều kiện bàn giao nghiệm thu** |

---

## 3. DANH MỤC CHI TIẾT KẾT QUẢ THỰC THI THEO TỪNG MÀN HÌNH

### 3.1. Màn hình AK202 - イラスト背景登録 (Illustration Background Create)
- **URL:** `https://admin-dev.surrealdolls.com/backgrounds/illustrations/create`

| Mã TC | Hạng mục kiểm tra | Thao tác thực hiện | Kết quả kỳ vọng (Expected) | Kết quả thực tế (Actual) | Kết quả | File bằng chứng |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| `[AK202-CR-01]` | Text hướng dẫn dưới nút Upload | Truy cập màn hình AK202 $\rightarrow$ Quan sát dòng ghi chú dưới nút upload | Hiển thị: `アップロード可能な画像形式：PNG、JPG／JPEG、SVG、WebP` và `最大ファイルサイズ：10MB` | Hiển thị chính xác 100% text với thông số 10MB | **Pass** | [evidence_AK202_initial_ui_10mb_limit.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AK202_initial_ui_10mb_limit.png) |
| `[AK202-CR-02]` | Upload file dung lượng vượt quá 10MB | Chọn file JPG/PNG có dung lượng > 10MB (`invalid_png_10_5mb.png` - 10.5MB, `invalid_jpg_12mb.jpg` - 12MB) | Không nhận file, hiển thị toast thông báo: `ファイルサイズは10MB以下にしてください。` | Hiển thị toast `ファイルサイズは10MB以下にしてください。`, không nhận file | **Pass** | [evidence_AK202_TC_file_over_10mb.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AK202_TC_file_over_10mb.png) |
| `[AK202-CR-03]` | Upload file hợp lệ định dạng JPG (8MB) | Chọn file `valid_jpg_8mb.jpg` (8.00MB <= 10MB) | File được tiếp nhận, hiển thị tên file `valid_jpg_8mb.jpg`, xuất hiện nút `画像を変更` và `画像を削除` | Nhận file thành công, hiển thị tên file và 2 nút thay đổi/xóa | **Pass** | [evidence_AK202_preview_modal_8mb.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AK202_preview_modal_8mb.png) |
| `[AK202-CR-04]` | Upload file hợp lệ cận biên 10MB (9.9MB PNG) | Chọn file `valid_png_9_9mb.png` (9.90MB <= 10MB) | File được tiếp nhận, hiển thị tên file `valid_png_9_9mb.png` | Nhận file thành công, không báo lỗi dung lượng | **Pass** | [evidence_AK202_preview_modal_8mb.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AK202_preview_modal_8mb.png) |
| `[AK202-CR-05]` | Upload file đúng định dạng SVG & WebP | Thử tải lên file SVG (`valid_svg_5mb.svg`) và WebP (`valid_webp_9mb.webp` - 9MB) | File được tiếp nhận bình thường | Tiếp nhận bình thường không lỗi | **Pass** | - |
| `[AK202-CR-06]` | Upload file sai định dạng (GIF, PDF) | Chọn file GIF (`invalid_file_gif.gif`) hoặc PDF (`invalid_file_pdf.pdf`) | Báo lỗi toast: `無効な画像形式です。サポート形式: JPG、 JPEG、 PNG、 WEBP、 SVG。` | Hiển thị toast từ chối định dạng không hỗ trợ | **Pass** | [evidence_AK202_invalid_file_format.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AK202_invalid_file_format.png) |
| `[AK202-CR-07]` | Xem trước (Preview) ảnh đã upload | Click vào tên file ảnh vừa upload trên UI | Mở modal preview hiển thị ảnh kích thước lớn kèm nút `閉じる` | Modal mở hiển thị ảnh đầy đủ, click `閉じる` đóng modal | **Pass** | [evidence_AK202_preview_modal_8mb.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AK202_preview_modal_8mb.png) |
| `[AK202-CR-08]` | End-to-end lưu Background với ảnh 8MB | Nhập tên `Test Background 8MB`, upload ảnh 8MB, chọn status, order, bấm `登録` | Tạo thành công, lưu ảnh lên S3, hiển thị toast `正常に作成されました。`, xuất hiện trên list AK201 | Lưu background thành công (ID: 68), S3 URL hợp lệ | **Pass** | - |

---

### 3.2. Màn hình AK203 - イラスト背景更新 (Illustration Background Edit)
- **URL:** `https://admin-dev.surrealdolls.com/backgrounds/illustrations/detail/{id}`

| Mã TC | Hạng mục kiểm tra | Thao tác thực hiện | Kết quả kỳ vọng (Expected) | Kết quả thực tế (Actual) | Kết quả | File bằng chứng |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| `[AK203-CR-01]` | Text hướng dẫn dưới nút Upload | Truy cập màn hình chi tiết/chỉnh sửa AK203 $\rightarrow$ Quan sát dòng ghi chú | Hiển thị: `アップロード可能な画像形式：PNG、JPG／JPEG、SVG、WebP` và `最大ファイルサイズ：10MB` | Hiển thị chính xác text 10MB | **Pass** | [evidence_AK203_TC_file_over_10mb.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AK203_TC_file_over_10mb.png) |
| `[AK203-CR-02]` | Thay đổi ảnh bằng file vượt quá 10MB | Nhấn nút `画像を変更` $\rightarrow$ Chọn file `invalid_jpg_12mb.jpg` (12MB) | Từ chối nhận file, hiển thị toast: `ファイルサイズは10MB以下にしてください。` | Hiển thị toast `ファイルサイズは10MB以下にしてください。`, giữ nguyên ảnh cũ | **Pass** | [evidence_AK203_TC_file_over_10mb.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AK203_TC_file_over_10mb.png) |
| `[AK203-CR-03]` | Thay đổi ảnh bằng file hợp lệ <= 10MB | Nhấn nút `画像を変更` $\rightarrow$ Chọn file `valid_png_9_9mb.png` (9.9MB) | Tên file cập nhật thành `valid_png_9_9mb.png`, preview hiển thị ảnh mới | Nhận file mới 9.9MB thành công, cập nhật preview | **Pass** | - |
| `[AK203-CR-04]` | Thay đổi ảnh bằng file sai định dạng | Chọn file GIF hoặc PDF | Báo lỗi toast: `無効な画像形式です。サポート形式: JPG、 JPEG、 PNG、 WEBP、 SVG。` | Hiển thị toast từ chối định dạng, giữ nguyên file | **Pass** | - |
| `[AK203-CR-05]` | Xóa ảnh đã upload | Nhấn nút `画像を削除` | Ảnh bị xóa khỏi form, quay về trạng thái chưa upload, báo lỗi `背景画像は空欄にできません。` nếu bắt buộc | File biến mất, UI trở về trạng thái chưa chọn ảnh | **Pass** | - |
| `[AK203-CR-06]` | End-to-end lưu cập nhật với ảnh 9.9MB | Nhấn nút `保存` sau khi đã thay đổi sang ảnh 9.9MB | Lưu cập nhật thành công, hiển thị toast `正常に更新されました。`, quay về danh sách AK201 | Cập nhật thành công, S3 upload ảnh 9.9MB mới | **Pass** | - |

---

### 3.3. Màn hình AK302 - 箱庭背景登録 (Mini Garden Background Create)
- **URL:** `https://admin-dev.surrealdolls.com/backgrounds/mini-garden/create`

| Mã TC | Hạng mục kiểm tra | Thao tác thực hiện | Kết quả kỳ vọng (Expected) | Kết quả thực tế (Actual) | Kết quả | File bằng chứng |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| `[AK302-CR-01]` | Text hướng dẫn dưới nút Upload (Retest bug `SURREALDOLLS-4682`) | Truy cập màn hình AK302 $\rightarrow$ Quan sát dòng ghi chú dưới nút upload | Hiển thị: `アップロード可能な画像形式：PNG、JPG／JPEG、SVG、WebP` và `最大ファイルサイズ：10MB` | Hiển thị chính xác text 10MB (Khắc phục hoàn toàn lỗi thiếu text trước đây) | **Pass** | [evidence_AK302_initial_ui_10mb_limit.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AK302_initial_ui_10mb_limit.png) |
| `[AK302-CR-02]` | Upload file dung lượng vượt quá 10MB (`[AK302-33]`) | Chọn file `invalid_png_10_5mb.png` (10.5MB) hoặc `invalid_jpg_12mb.jpg` (12MB) | Không nhận file, hiển thị toast thông báo: `ファイルサイズは10MB以下にしてください。` | Hiển thị toast `ファイルサイズは10MB以下にしてください。`, chặn upload | **Pass** | [evidence_AK302_TC_file_over_10mb.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AK302_TC_file_over_10mb.png) |
| `[AK302-CR-03]` | Upload file hợp lệ định dạng JPG (8MB) | Chọn file `valid_jpg_8mb.jpg` (8.00MB <= 10MB) | File được tiếp nhận, hiển thị tên file `valid_jpg_8mb.jpg`, xuất hiện nút `画像を変更` và `画像を削除` | Nhận file thành công, hiển thị tên file và 2 nút thay đổi/xóa | **Pass** | - |
| `[AK302-CR-04]` | Upload file hợp lệ cận biên 10MB (9.9MB PNG) | Chọn file `valid_png_9_9mb.png` (9.90MB <= 10MB) | File được tiếp nhận, hiển thị tên file `valid_png_9_9mb.png` | Nhận file thành công, không báo lỗi | **Pass** | - |
| `[AK302-CR-05]` | Upload file sai định dạng (GIF, PDF) (`[AK302-34]`) | Chọn file GIF (`invalid_file_gif.gif`) hoặc PDF (`invalid_file_pdf.pdf`) | Báo lỗi toast: `無効な画像形式です。サポート形式: JPG、 JPEG、 PNG、 WEBP、 SVG。` | Hiển thị toast từ chối định dạng không hợp lệ | **Pass** | [evidence_AK302_TC_invalid_file_format.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AK302_TC_invalid_file_format.png) |
| `[AK302-CR-06]` | Xem trước (Preview) ảnh đã upload (`[AK302-35]`) | Click vào tên file ảnh vừa upload trên UI | Mở modal preview hiển thị ảnh kèm nút `閉じる` | Modal mở preview ảnh sắc nét, click `閉じる` đóng modal | **Pass** | - |
| `[AK302-CR-07]` | End-to-end tạo 箱庭背景 với ảnh 8MB | Nhập tên `Test Mini Garden 8MB`, upload ảnh 8MB, chọn loại `壁＋床`, order `999`, bấm `登録` | Tạo thành công, lưu ảnh lên S3, hiển thị toast `正常に作成されました。`, xuất hiện trên list AK301 | Lưu background thành công (ID: 73), hiển thị đúng trên danh sách | **Pass** | - |

---

### 3.4. Màn hình AK303 - 箱庭背景更新 (Mini Garden Background Edit)
- **URL:** `https://admin-dev.surrealdolls.com/backgrounds/mini-garden/detail/{id}`

| Mã TC | Hạng mục kiểm tra | Thao tác thực hiện | Kết quả kỳ vọng (Expected) | Kết quả thực tế (Actual) | Kết quả | File bằng chứng |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| `[AK303-CR-01]` | Text hướng dẫn dưới nút Upload | Truy cập màn hình chi tiết AK303 $\rightarrow$ Quan sát dòng ghi chú | Hiển thị: `アップロード可能な画像形式：PNG、JPG／JPEG、SVG、WebP` và `最大ファイルサイズ：10MB` | Hiển thị chính xác text 10MB | **Pass** | [evidence_AK303_TC_file_over_10mb.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AK303_TC_file_over_10mb.png) |
| `[AK303-CR-02]` | Thay đổi ảnh bằng file vượt quá 10MB (`[AK303-32]`) | Nhấn nút `画像を変更` $\rightarrow$ Chọn file `invalid_png_10_5mb.png` (10.5MB) | Từ chối nhận file, hiển thị toast: `ファイルサイズは10MB以下にしてください。` | Hiển thị toast `ファイルサイズは10MB以下にしてください。`, giữ nguyên ảnh cũ | **Pass** | [evidence_AK303_TC_file_over_10mb.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AK303_TC_file_over_10mb.png) |
| `[AK303-CR-03]` | Thay đổi ảnh bằng file hợp lệ <= 10MB | Nhấn nút `画像を変更` $\rightarrow$ Chọn file `valid_png_9_9mb.png` (9.9MB) | Tên file cập nhật thành `valid_png_9_9mb.png`, preview hiển thị ảnh mới | Nhận file mới 9.9MB thành công, cập nhật preview | **Pass** | - |
| `[AK303-CR-04]` | Thay đổi ảnh bằng file sai định dạng (`[AK303-33]`) | Chọn file GIF hoặc PDF | Báo lỗi toast: `無効な画像形式です。サポート形式: JPG、 JPEG、 PNG、 WEBP、 SVG。` | Hiển thị toast từ chối định dạng | **Pass** | - |
| `[AK303-CR-05]` | Xem trước (Preview) ảnh đã upload (`[AK303-34]`) | Nhấn vào tên file | Mở modal preview ảnh, click `閉じる` đóng modal | Modal preview mở và đóng hoạt động ổn định | **Pass** | - |
| `[AK303-CR-06]` | End-to-end lưu cập nhật với ảnh 9.9MB | Nhấn nút `保存` sau khi đã thay đổi sang ảnh 9.9MB | Lưu cập nhật thành công, hiển thị toast `正常に作成されました。` (hoặc `更新されました`), quay về danh sách AK301 | Cập nhật thành công, S3 upload ảnh 9.9MB mới | **Pass** | - |

---

## 4. KẾT QUẢ RETEST VÀ CẬP NHẬT TRÊN GOOGLE SHEET MASTER

Đã tiến hành đồng bộ và cập nhật trực tiếp kết quả kiểm thử vào Google Sheet Master (`Surreal Test cases_Admin` - ID: `1ZaL8llNgH6sCxpG-daLEi21IxXFpub-BbrRJRdUNMOg`):

1. **Tab `AK302` - Dòng 35 (`[AK302-26]`):**
   - Nội dung: `Text dưới mục upload`
   - Trạng thái Round 1: `Fail` | Bug ID: `SURREALDOLLS-4682 [AK302/AK303] - Thêm text giải thích dưới mục upload ảnh`
   - Cập nhật Round 2: **Cột N (Round 2 Result) = `Pass`**, **Cột O (Bug ID) = `SURREALDOLLS-13887`**, **Cột P (Tester) = `NgaDTP`**, **Cột Q (Date) = `11/11/2026`**.
2. **Tab `AK302` - Dòng 42 (`[AK302-33]`):**
   - Nội dung: `Upload file dung lượng vượt quá 10 MB`
   - Cập nhật Expected (Cột H): `Hiển thị message : ファイルサイズは10MB以下にしてください。`
   - Cập nhật Round 2: **Cột N (Round 2 Result) = `Pass`**, **Cột O (Bug ID) = `SURREALDOLLS-13887`**, **Cột P (Tester) = `NgaDTP`**, **Cột Q (Date) = `11/11/2026`**.
3. **Tab `AK303` - Dòng 40 (`[AK303-32]`):**
   - Nội dung: Cập nhật Classification D40 thành `Upload file dung lượng vượt quá 10MB`
   - Cập nhật Expected (Cột H): `Hiển thị message : ファイルサイズは10MB以下にしてください。`
   - Cập nhật Round 2: **Cột N (Round 2 Result) = `Pass`**, **Cột O (Bug ID) = `SURREALDOLLS-13887`**, **Cột P (Tester) = `NgaDTP`**, **Cột Q (Date) = `11/11/2026`**.

---

## 5. DANH SÁCH BẰNG CHỨNG KIỂM THỬ (TEST EVIDENCE REPOSITORY)

Tất cả các file bằng chứng hình ảnh được lưu trữ tại thư mục `evidence/`:

1. [evidence_AK202_initial_ui_10mb_limit.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AK202_initial_ui_10mb_limit.png): Màn hình AK202 hiển thị dòng text hướng dẫn `最大ファイルサイズ：10MB`.
2. [evidence_AK202_TC_file_over_10mb.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AK202_TC_file_over_10mb.png): Toast thông báo lỗi `ファイルサイズは10MB以下にしてください。` trên AK202 khi upload file 10.5MB.
3. [evidence_AK202_preview_modal_8mb.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AK202_preview_modal_8mb.png): Modal xem trước ảnh dung lượng lớn 8MB trên AK202.
4. [evidence_AK202_invalid_file_format.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AK202_invalid_file_format.png): Toast thông báo lỗi định dạng khi chọn file GIF/PDF trên AK202.
5. [evidence_AK203_TC_file_over_10mb.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AK203_TC_file_over_10mb.png): Toast thông báo lỗi `ファイルサイズは10MB以下にしてください。` trên AK203 khi upload file 12MB.
6. [evidence_AK302_initial_ui_10mb_limit.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AK302_initial_ui_10mb_limit.png): Màn hình AK302 hiển thị dòng text hướng dẫn `最大ファイルサイズ：10MB`.
7. [evidence_AK302_TC_file_over_10mb.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AK302_TC_file_over_10mb.png): Toast thông báo lỗi `ファイルサイズは10MB以下にしてください。` trên AK302 khi upload file 10.5MB.
8. [evidence_AK302_TC_invalid_file_format.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AK302_TC_invalid_file_format.png): Toast thông báo lỗi định dạng không hỗ trợ trên AK302.
9. [evidence_AK303_TC_file_over_10mb.png](file:///home/nga/Documents/SurrealDoll/evidence/evidence_AK303_TC_file_over_10mb.png): Toast thông báo lỗi `ファイルサイズは10MB以下にしてください。` trên AK303 khi upload file 10.5MB.

---

## 6. KẾT LUẬN & ĐÁNH GIÁ NGHIỆM THU (SIGN-OFF)

- **Kết quả chức năng:** Tính năng nâng giới hạn dung lượng file background từ 5MB lên 10MB đã được triển khai hoàn chỉnh và chính xác trên cả 4 màn hình (`AK202`, `AK203`, `AK302`, `AK303`).
- **Giao diện & UI Text:** Text hướng dẫn dưới khu vực upload ảnh hiển thị chuẩn `最大ファイルサイズ：10MB`.
- **Validation:** Bắt chặn chính xác các file > 10MB (với message `ファイルサイズは10MB以下にしてください。`) và các file sai định dạng (GIF, PDF).
- **Backend & S3:** Lưu trữ và cập nhật thành công các file ảnh có dung lượng lớn (8MB, 9.9MB) mà không phát sinh lỗi timeout hay dung lượng.
- **Tiêu chí nghiệm thu:** Đạt tiêu chuẩn nghiệm thu vòng kiểm thử thủ công theo Trụ Cột 4 ([04_manual_test_execution_rule.md](../Universal_Rules/04_manual_test_execution_rule.md)).
