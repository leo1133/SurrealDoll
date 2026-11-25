# PHÂN TÍCH SPEC & Q&A — AF500 (GIFT Animation Type)
**Nguồn Spec:** Google Sheet `AF500` (gid=`1458098150`)

## 1. Tóm tắt Spec đã bóc tách
- `AF500` **không phải màn hình độc lập**, mà là tính năng mở rộng (`演出種類` / `animation_type`) tích hợp trực tiếp trên:
  1. **Màn Tạo / Sửa Gift (`AF200` / `AF300`):**
     - Radio `演出種類` (`animation_type`):
       - `通常演出` (default): Giá nhập tự do | Category được chọn | `ギフトコンテンツ` (`image`) được upload.
       - `シャッター演出`: Giá chỉ chọn `5,000` / `10,000` | Category **KHÔNG cho chọn** (disabled) | `ギフトコンテンツ` **disable** (dùng hiệu ứng cố định).
       - `継続演出`: Giá chỉ chọn `1000pt`, `3000pt`, `5,000pt`, `10,000pt` | Category **KHÔNG cho chọn** (disabled) | `ギフトコンテンツ` **disable** (dùng hiệu ứng cố định).
  2. **Màn List Gift (`AF100`):**
     - Thêm pulldown filter `演出種類`: `全て演出種類`, `通常演出`, `シャッター演出`, `継続演出`.
     - Thêm cột `演出種類` hiển thị giá trị tương ứng.
- **APIs:** `POST /gift/`, `GET /gift/` (và `PATCH /gift/{gift_id}/` khi sửa).

## 2. Bảng Q&A Clarification

| No. | Control / Logic | Vấn đề chưa rõ trong Spec | Câu hỏi làm rõ | Phương án đề xuất | Giả định tạm thời | Trạng thái |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| `Q1` | `[1]-[2] Chuyển đổi Radio` | Khi đã nhập giá `250` + chọn Category + upload `image` ở `通常演出`, rồi chuyển sang `シャッター演出` và quay lại `通常演出`. | Dữ liệu cũ có bị clear khi chuyển radio không? | **Option A:** Clear giá trị `category_id` & `image` khi chuyển sang Shutter/Continuous.<br>**Option B:** Chỉ disable UI, bỏ qua giá trị khi submit. | Tạm giả định **Option A**. | `Pending` |
