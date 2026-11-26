# PHÂN TÍCH SPEC & Q&A — AF100 (Gift List)
**Nguồn Spec:** Google Sheet `AF100` (gid=`217442794`) + `AF500` (`演出種類`) + Postman `Live2d_BE/gift`

## 1. Tóm tắt Spec đã bóc tách
- **Sidebar & Breadcrumb:** `商品管理 > ギフト管理 > ギフト一覧` | `ホーム＞ギフト管理`
- **Search `[1]`:** Placeholder `ギフト名・ギフトID・ギフト値段` (`CMR02`) — Partial match `gift name`, Exact match `gift price` & `gift ID`.
- **Filters:** Category (`全てカテゴリー` + list), Status (`全てステータス`, `公開`, `非公開`), Animation Type (`全て演出種類`, `通常演出`, `シャッター演出`, `継続演出` từ `AF500`).
- **Table Columns:** `ID`, `ギフト名` (icon + name), `ステータス` (`公開`/`非公開`), `カテゴリ`, `値段` (sort asc/desc), `演出種類`, Actions (Edit → `AF300`, Delete `CMMSG28`), `作成者`, `作成日` (`yyyy/mm/dd hh:mm`), `変更日` (`yyyy/mm/dd hh:mm`).
- **Paging:** `CMR01` (`items_per_page: 10`).
- **APIs:** `GET /gift/`, `DELETE /gift/{gift_id}/`, `GET /gift/category/`.

## 2. Bảng Q&A Clarification

| No. | Control / Logic | Vấn đề chưa rõ trong Spec | Câu hỏi làm rõ | Phương án đề xuất | Giả định tạm thời | Trạng thái |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| `Q1` | `[1] Search box` | Tìm kiếm theo `値段` khi giá có dấu phẩy (`10,000` vs `10000`). | Người dùng nhập `10,000` có dấu phẩy có tìm thấy quà giá `10000` không? | **Option A:** Chuẩn hóa bỏ dấu phẩy trước khi search.<br>**Option B:** Chỉ khớp số nguyên không dấu phẩy `10000`. | Tạm giả định **Option A**. | `Pending` |
| `Q2` | `[AF100-Status]` | Pulldown Status ghi chú "(Chưa có trên WF)". | Pulldown Status `公開`/`非公開` đã được triển khai trên FE chưa? | **Option A:** Đã triển khai đầy đủ.<br>**Option B:** Chưa có trên UI. | Tạm giả định **Option A**. | `Pending` |
