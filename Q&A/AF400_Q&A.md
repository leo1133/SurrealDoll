# PHÂN TÍCH SPEC & Q&A — AF400 (Gift Category)
**Nguồn Spec:** Google Sheet `AF400` (gid=`993447379`) + Postman `Live2d_BE/gift/category`

## 1. Tóm tắt Spec đã bóc tách
- **Sidebar & Breadcrumb:** `商品管理 > ギフト管理 > ギフトカテゴリ管理` | `ホーム＞ギフトカテゴリ管理` | Title: `カテゴリ一覧`
- **Danh sách:** **Infinite Scroll** (không dùng phân trang số), mặc định sort theo `sort_order`. Tạo sau mặc định `sort_order` ở sau cùng.
- **Kéo thả Sort Order (`[6]`):** Icon 6 dots cho phép kéo thả đổi thứ tự (`PUT /gift/category/sort-order/{category_id}`).
- **Tạo mới (`[2]-[5]`):** Nút `新規登録` mở modal `カテゴリを追加します`, input `name` Required **max 20 ký tự**, nút `追加`.
- **Sửa (`[7], [10]-[12]`):** Click/tab vào tên category (`tabable text`) mở modal `カテゴリを編集します`, input `name` Required **max 20 ký tự**, nút `保存` (lưu xuống dưới cùng).
- **Xóa (`[9]`):** Xóa category → **các gift trực thuộc category đã bị xóa sẽ trở thành gift không có category (`未設定`)**.
- **APIs:** `GET /gift/category/`, `POST /gift/category/`, `PUT /gift/category/{category_id}`, `DELETE /gift/category/{category_id}`, `PUT /gift/category/sort-order/{category_id}`.

## 2. Bảng Q&A Clarification

| No. | Control / Logic | Vấn đề chưa rõ trong Spec | Câu hỏi làm rõ | Phương án đề xuất | Giả định tạm thời | Trạng thái |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| `Q1` | `[4][11] Category Name` | Có cho phép tạo/sửa 2 danh mục trùng tên nhau không? | Tên danh mục có bắt buộc Unique không? | **Option A:** Không cho trùng (báo `CMMSG57`).<br>**Option B:** Cho phép trùng tên. | Tạm giả định **Option A**. | `Pending` |
| `Q2` | `[9] Xóa category` | Click nút Xóa có mở popup xác nhận `CMMSG28` trước khi chuyển gift về `未設定` không? | Có modal xác nhận trước khi xóa danh mục không? | **Option A:** Có popup xác nhận `CMMSG28`.<br>**Option B:** Xóa trực tiếp ngay. | Tạm giả định **Option A**. | `Pending` |
