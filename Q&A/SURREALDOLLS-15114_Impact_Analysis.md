# BÁO CÁO PHÂN TÍCH TASK & PHẠM VI ẢNH HƯỞNG (TASK IMPACT ANALYSIS)
## Ticket Backlog: `SURREALDOLLS-15114`
### Áp dụng: Quy chuẩn Trụ cột 1 (`Universal_Rules/01_core_spec_analysis_rule.md` - Flow 2)
### Thời điểm phân tích: 2026-11-27 10:20:33

---

## 1. ĐỊNH VỊ PHẠM VI TÍNH NĂNG (FEATURE CONTEXT)

| Thuộc tính | Chi tiết Bóc tách |
| :--- | :--- |
| **Ticket ID** | `SURREALDOLLS-15114` |
| **Cụm tính năng** | N/A |
| **Tác động trực tiếp (Direct Scope)** | Các màn hình/API/DB liên quan theo phạm vi của ticket |
| **Tác động hồi quy (Regression Scope)** | Luồng nghiệp vụ cha và các màn hình liên kết chéo |

---

## 2. MA TRẬN TIÊU CHÍ NGHIỆM THU (ACCEPTANCE CRITERIA CHECKLIST)

| STT | Tiêu chí Nghiệm thu (AC) | Mức độ Ưu tiên | Kịch bản Retest / Regression | Trạng thái |
| :---: | :--- | :---: | :--- | :---: |
| 1 | Thao tác người dùng theo đúng yêu cầu mới của ticket | **High** | Chạy kiểm thử chức năng chính trên Live ENV | `Pending` |
| 2 | Bắt lỗi validation và hiển thị thông báo hợp lệ khi nhập sai | **High** | Boundary test & MSG verify | `Pending` |
| 3 | Dữ liệu lưu xuống CSDL chính xác (Rule 07, soft-delete, updated_at) | **High** | Truy vấn Read-Only CSDL | `Pending` |
| 4 | Không làm gãy/lệch luồng nghiệp vụ trên các màn hình liên quan | **Medium** | Smoke test màn hình liên kết | `Pending` |

---

## 3. ĐIỂM CHỜ XÁC NHẬN VỚI BA / PO (Q&A / OPEN POINTS)

| ID | Hạng mục cần làm rõ | Phương án đề xuất | Trạng thái |
| :---: | :--- | :--- | :---: |
| `QA-SURREALDOLLS-15114-01` | Xử lý dữ liệu cũ trước khi áp dụng logic mới | Giữ nguyên dữ liệu cũ, chỉ áp dụng logic cho bản ghi mới | `Open` |
| `QA-SURREALDOLLS-15114-02` | Quyền truy cập theo vai trò (RBAC) | Chỉ cấp quyền cho Master Admin, chặn vai trò khác nếu không có chỉ định | `Open` |

---

*Báo cáo được sinh tự động bởi `scripts/spec_analyzer.py` - Tuân thủ 100% Flow 2.*