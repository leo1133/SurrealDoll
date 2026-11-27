# BÁO CÁO LỖI KIỂM THỬ (BUG REPORT) - MÀN HÌNH G702 (POINT PURCHASE WEB & MENU)

- **Màn hình / Module:** `G702` (Point Purchase Web & Menu Điều khoản `A201` - `A208`)
- **Môi trường:** Live / Production (`https://surrealdolls.com`)
- **Người báo cáo:** Antigravity QA Agent / NgaDTP
- **Ngày phát hiện:** 20/11/2026

---

## TỔNG HỢP DANH SÁCH LỖI

| Mã Bug | Tên Lỗi / Tóm Tắt | Phân Loại | Mức Độ | Trạng Thái | Màn Hình / Vị Trí |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **`BUG-G702-01`** | Thiếu tiêu đề màn hình "Point Purchase" dưới Logo SurrealDoll | UI / Content | **Medium** | **Open** | Trang `G702` |
| **`BUG-G702-02`** | Lộ chuỗi placeholder `[本サービス名]` / `[Service Name]` trong Điều 1 Terms of Service | Content Leak | **Medium** | **Open** | Trang `A205` (`/terms-of-service`) |
| **`BUG-G702-03`** | Lệch ngày ban hành văn bản tại Quy chế Hộp kho báu (Web ghi 15/08/2025, Spec là 14/08/2025) | Spec Discrepancy | **Low** | **Open** | Trang `A207` (`/treasure-box-terms-of-use`) |
| **`BUG-G702-04`** | Hiển thị từ khóa kỹ thuật nội bộ "Sub-screen" trên menu người dùng cuối (`...Payment Services Act Sub-screen`) | UI / Content Leak | **Medium** | **Open** | Trang `G702` (Dòng menu số 9) |
| **`BUG-G702-05`** | Cần xác minh sự tồn tại của nút "Log Out" và bộ chọn ngôn ngữ ở chân trang (Footer) | Missing Feature | **Low** | **Open** | Chân trang `G702` |
