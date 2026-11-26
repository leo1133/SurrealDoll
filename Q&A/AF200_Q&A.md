# PHÂN TÍCH SPEC & Q&A — AF200 (Gift Create)
**Nguồn Spec:** Google Sheet `AF200` (gid=`2030636358`) + `AF500` (`演出種類`) + `CMR50` + Postman `Live2d_BE/gift`

## 1. Tóm tắt Spec đã bóc tách
- **Breadcrumb & Title:** `ホーム＞ギフト管理＞ギフト登録` | `ギフト登録`
- **Fields & Rules:**
  - `演出種類` (`animation_type`, Radio từ `AF500`): `通常演出` (default) | `シャッター演出` | `継続演出`
  - `ギフト名` (`name`): Required, **Max 10 ký tự**, placeholder `ギフト名を入力してください`
  - `ギフトアイコン` (`icon`): Required, `png, JPG/JPEG, SVG, WebP`, Max **5MB**, theo **CMR50** (Upload, tabable filename mở modal preview, `変更`, `削除`, `閉じる`)
  - `ギフトコンテンツ` (`image`): Required (khi `通常演出`), `png, lottie, gif`, Max **5MB**, format error `CMMSG43`, size error `CMMSG45`, theo **CMR50**. **Disable khi chọn `シャッター演出` / `継続演出`**
  - `ステータス` (`status`): Required Radio `公開` (default) / `非公開`
  - `並び順` (`sort_order`): Required, chỉ nhập số, nhỏ đứng trước, trùng ưu tiên `id`
  - `ギフト値段` (`price`): Required, số nguyên, tự format dấu phẩy 3 số (`10,000`). Khi chọn `シャッター演出` → chỉ chọn `5,000`/`10,000`; `継続演出` → chỉ chọn `1000pt`/`3000pt`/`5,000pt`/`10,000pt`
  - `ギフトカテゴリ` (`category_id`): **Optional** (`未設定` → tab `一般/General` trên `I600`). **Không cho chọn khi `シャッター演出` / `継続演出`**
  - Inline `+` Popover: `カテゴリを追加します` (max 20 ký tự, Required, nút `追加する`)
  - Actions: `キャンセル` (`CMR07`), `登録` (`CMMSG12` → `AF100`)
- **APIs:** `POST /gift/`, `POST /gift/category/`, `GET /gift/category/`.

## 2. Bảng Q&A Clarification

| No. | Control / Logic | Vấn đề chưa rõ trong Spec | Câu hỏi làm rõ | Phương án đề xuất | Giả định tạm thời | Trạng thái |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| `Q1` | `[12] ギフト値段` | Giá tối thiểu (`price = 0` hay `>= 1`) khi chọn `通常演出`. | Quà thường có được phép nhập giá `= 0` không? | **Option A:** Chặn `0`, yêu cầu `>= 1`.<br>**Option B:** Cho phép `0` (quà miễn phí). | Tạm giả định **Option A** (`>= 1`). | `Pending` |
| `Q2` | `[16]-[19] Popover +` | Khi đang tạo gift mà thêm category mới qua `+`, có tự động chọn category vừa tạo vào pulldown không? | Sau khi ấn `追加する`, category mới có được auto-select không? | **Option A:** Auto-select category vừa tạo.<br>**Option B:** Chỉ thêm vào list, giữ nguyên lựa chọn cũ. | Tạm giả định **Option A**. | `Pending` |
