# TÀI LIỆU BÓC TÁCH ĐẶC TẢ KỸ THUẬT & LÀM RÕ YÊU CẦU (SPEC ANALYSIS & CLARIFICATION REPORT)
## Màn hình / Cụm: `BA100` - **Quản lý Agency & Liên kết Liver**
### Phân hệ: Master Admin / Agency Web | Nguồn Spec: `BA100_online.json`
### Áp dụng: Quy chuẩn Trụ Cột 1 (`Universal_Rules/01_core_spec_analysis_rule.md`) & Master Policy (`GEMINI.md`)

---

## BẢNG THÔNG TIN TỔNG QUAN ĐẶC TẢ (SPECIFICATION METADATA)

| Thuộc tính | Chi tiết |
| :--- | :--- |
| **Mã màn hình** | `BA100` |
| **Tên cụm chức năng** | **Quản lý Agency & Liên kết Liver** |
| **Ngày phân tích** | 26/11/2026 |
| **Tổng số phần tử bóc tách** | **0** controls UI |
| **Trạng thái Spec** | Đã bóc tách tự động 2-Pass qua `scripts/spec_analyzer.py` |

---

## I. KẾT QUẢ QUÉT ĐẶC TẢ 2 BƯỚC BẮT BUỘC (2-PASS SCANNING PROTOCOL)

### 1. Pass 1 - Bóc Tách UI Controls Có `[No.]`

| No. | Tên phần tử | Loại Control | Bắt buộc | Ràng buộc kỹ thuật & Nghiệp vụ (SRS & CR) | Mã / Nội dung MSG |
| :---: | :--- | :--- | :---: | :--- | :--- |

### 2. Pass 2 - Bóc Tách Yêu Cầu Phi Giao Diện & Logic Ngầm Định (Non-UI & Implicit Business Rules)

- **[LOGIC]** Kiểm tra tính toàn vẹn phiên làm việc (Session Timeout sau 30 phút không hoạt động).
- **[LOGIC]** Đảm bảo tải dữ liệu có phân trang và lazy-load hình ảnh/avatar.
- **[LOGIC]** Tự động chuyển đổi trạng thái bản ghi trong DB khi thao tác cập nhật thành công.
- **[LOGIC]** Xử lý lỗi mạng/timeout: hiển thị Retry Toast hoặc Alert Banner thân thiện.

---

## II. MA TRẬN PHÂN QUYỀN ĐA VAI TRÒ (MULTI-ROLE RBAC MATRIX)

| Vai trò (Actor) | Quyền xem | Quyền thêm mới | Quyền chỉnh sửa | Quyền xóa / Thao tác nguy hiểm | Ghi chú & Rào chắn bảo mật |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Master Admin** | Toàn quyền | Có | Có | Có | Quản trị toàn bộ dữ liệu `BA100` |
| **Agency User** | Trong phạm vi Agency | Theo phân quyền | Theo phân quyền | Bị giới hạn | Chỉ xem/sửa bản ghi thuộc Agency mình sở hữu |
| **Liver / End-User** | Bị từ chối | Không | Không | Không | Trả về 403 Forbidden hoặc điều hướng 404 |

---

## III. DANH SÁCH CÂU HỎI LÀM RÕ & ĐIỂM CHỜ XÁC NHẬN (Q&A BACKLOG)

| ID | Hạng mục / Phần tử | Tình huống cần làm rõ | Phương án đề xuất (Proposal) | Phản hồi từ BA / PO | Trạng thái |
| :---: | :--- | :--- | :--- | :--- | :---: |
| `QA-01` | `BA100` Data Lifecycle | Khi dữ liệu cha bị vô hiệu hóa/xóa, các bản ghi con tại màn hình hiển thị như thế nào? | Soft-delete / Ẩn khỏi danh sách mặc định | Chờ BA confirm | `Open` |
| `QA-02` | Concurrent Edit | Xử lý thế nào khi 2 Admin cùng lúc cập nhật 1 bản ghi? | Áp dụng Optimistic Locking (báo lỗi version conflict) | Chờ BA confirm | `Open` |

---

*Tài liệu được sinh tự động bởi `scripts/spec_analyzer.py` - Tuân thủ 100% Rule 01.*