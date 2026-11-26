# PHÂN TÍCH SPEC & Q&A — AF300 (Gift Update / Delete)
**Nguồn Spec:** Google Sheet `AF300` (gid=`213255523`) + `AF500` (`演出種類`) + `CMR50` + Postman `Live2d_BE/gift`

## 1. Tóm tắt Spec đã bóc tách
- **Breadcrumb & Title:** `ホーム＞ギフト管理＞ギフト更新` | `ギフト更新`
- **Fields & Rules:** Kế thừa toàn bộ ràng buộc từ `AF200` + `AF500` (`name` max 10, `icon` 5MB `CMR50`, `image` 5MB `CMR50`, `animation_type` Radio, `status` Radio, `sort_order`, `price`, `category_id` Optional `"未設定"`, Inline `+` Popover max 20, `キャンセル` `CMR07`).
- **Delete (`[21] 削除`):** Mở popup `CMMSG28`. Khi xóa thành công: **trên màn hình livestream (`I600`) không hiển thị gift đã xóa, nhưng các màn lịch sử mua gift vẫn hiện gift đã xóa**.
- **Save (`[22] 保存`):** Gọi `PATCH /gift/{gift_id}/`, thông báo `CMMSG13`, quay về `AF100`.
- **APIs:** `GET /gift/{gift_id}/`, `PATCH /gift/{gift_id}/`, `DELETE /gift/{gift_id}/`, `GET /gift/category/`, `POST /gift/category/`.

## 2. Bảng Q&A Clarification

| No. | Control / Logic | Vấn đề chưa rõ trong Spec | Câu hỏi làm rõ | Phương án đề xuất | Giả định tạm thời | Trạng thái |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| `Q1` | `[AF500] 演出種類` | Khi sửa gift (`AF300`), có cho phép đổi `animation_type` từ `通常演出` sang `シャッター演出` / `継続演出` không? | Trường `演出種類` ở màn Edit `AF300` là editable hay readonly? | **Option A:** Editable, đổi type sẽ reset/disable `category_id` & `image`.<br>**Option B:** Readonly không cho đổi type sau khi tạo. | Tạm giả định **Option A** (Editable). | `Pending` |
| `Q2` | `[21] 削除` | Xóa gift đang nằm trong Wishlist (`M1011`/`M20507`) của Streamer. | Hệ thống có tự động gỡ khỏi Wishlist hay chặn xóa? | **Option A:** Soft-delete và tự ẩn khỏi Wishlist.<br>**Option B:** Báo lỗi ràng buộc không cho xóa. | Tạm giả định **Option A**. | `Pending` |
