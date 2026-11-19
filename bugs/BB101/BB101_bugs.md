# BÁO CÁO KẾT QUẢ KIỂM THỬ VÀ XÁC MINH LỖI MÀN HÌNH BB101
## Module: BB101 - 事務所詳細 / 情報 (Agency Detail / Info)
### Ticket tham chiếu: [SURREALDOLLS-14130](https://issoh.backlog.com/view/SURREALDOLLS-14130), [SURREALDOLLS-14132](https://issoh.backlog.com/view/SURREALDOLLS-14132), [SURREALDOLLS-14885](https://issoh.backlog.com/view/SURREALDOLLS-14885)
### Áp dụng: Quy chuẩn Trụ cột 6 (06_bug_reporting_rule.md) & MASTER AGENT POLICY (GEMINI.md)

---

## 1. THÔNG TIN TỔNG QUAN TÁC VỤ (TASK OVERVIEW)

| Thuộc tính | Chi tiết |
| :--- | :--- |
| **Phân hệ & Màn hình** | Phân hệ Agency Web (`/sign-in/agency`) - Màn hình BB101 (`/agencies/info`) |
| **Môi trường kiểm thử** | **DEV** (`https://admin-dev.surrealdolls.com`) & **STG** (`https://admin-stg.surrealdolls.com`) |
| **Tài khoản kiểm thử** | DEV: `agency01` \| `Phgnga1998@`<br>STG: `123` \| `Leo150122@`, Basic Auth: `suriaru` / `suriaru` |
| **Tester ID** | `ngadtp` / `Antigravity QA` |
| **Thời gian thực thi** | Round 1 (DEV): `18/11/2026` \| Round 2 (STG): `19/11/2026` |
| **Kết luận kiểm thử** | <span style="color:green; font-weight:bold;">VERIFIED PASS 100% (CLOSED / 完了 - FIXED)</span> |

---

## 2. BẢNG TỔNG HỢP KẾT QUẢ XÁC MINH LỖI (RE-TEST SUMMARY)

| Mã Ticket | Môi trường | Mục tiêu kiểm thử | Dữ liệu đầu vào (Input) | Kết quả kỳ vọng (Expected) | Kết quả thực tế (Actual) | Trạng thái | Bằng chứng (Evidence) |
| :---: | :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| **SURREALDOLLS-14130** | DEV | Validation trùng email trên contact_email | `admin@admin.com` (email đã tồn tại) | Chặn lưu, báo lỗi MSG14: `「このメールアドレスは既に登録されています。」` | API trả về HTTP 422, UI báo lỗi inline: `「このメールアドレスは登録済みです。」` | <span style="color:green; font-weight:bold;">PASS</span> | [evidence_BB101_SURREALDOLLS-14130_DEV_PASS_duplicate_email.png](file:///home/nga/Documents/SurrealDoll/evidence/BB101/evidence_BB101_SURREALDOLLS-14130_DEV_PASS_duplicate_email.png) |
| **SURREALDOLLS-14132** | DEV | Luồng đổi email mới & block trạng thái 認証待ち | `newagency_...@testdomain.com` | Giữ nguyên contact_email cũ, hiển thị block `認証待ち：{new_email}` | Giữ nguyên contact_email = `ngadtp@mumesoft.vn`, hiển thị đúng `認証待ち：{new_email}` và trang FE verify token hoạt động | <span style="color:green; font-weight:bold;">PASS</span> | [evidence_BB101_SURREALDOLLS-14132_DEV_PARTIAL_pending_verification.png](file:///home/nga/Documents/SurrealDoll/evidence/BB101/evidence_BB101_SURREALDOLLS-14132_DEV_PARTIAL_pending_verification.png)<br>[evidence_BB101_SURREALDOLLS-14132_DEV_PASS_verify_email_change_page.png](file:///home/nga/Documents/SurrealDoll/evidence/BB101/evidence_BB101_SURREALDOLLS-14132_DEV_PASS_verify_email_change_page.png) |
| **SURREALDOLLS-14885** | DEV | BE lưu pending_email và hủy pending khi revert | Lưu email mới -> sau đó lưu lại `ngadtp@mumesoft.vn` | BE lưu `pending_email` khi đổi mới; hủy pending khi revert về email cũ | API GET trả về `pending_email` khi đổi mới; reset về `pending_email: null` khi revert về email cũ | <span style="color:green; font-weight:bold;">PASS</span> | [evidence_BB101_SURREALDOLLS-14885_DEV_PASS_cancel_pending_by_reverting_email.png](file:///home/nga/Documents/SurrealDoll/evidence/BB101/evidence_BB101_SURREALDOLLS-14885_DEV_PASS_cancel_pending_by_reverting_email.png) |
| **SURREALDOLLS-14885** | **STG** | Xác thực toàn diện 5 ca trên STG theo yêu cầu PM/Lead | 1. Đổi email mới<br>2. Sửa SĐT giữ pending<br>3. Validate trùng MSG14<br>4. Revert hủy pending<br>5. Trang FE verify token | Toàn bộ 5 ca hoạt động chuẩn xác theo đặc tả | API trả về 200/422 chuẩn, pending_email được quản lý chính xác, UI hiển thị / gỡ bỏ block `認証待ち` mượt mà | <span style="color:green; font-weight:bold;">PASS</span> | [evidence_01_new_pending](file:///home/nga/Documents/SurrealDoll/evidence/BB101/evidence_BB101_SURREALDOLLS-14885_STG_PASS_01_new_pending_email_created.png)<br>[evidence_02_keep_pending](file:///home/nga/Documents/SurrealDoll/evidence/BB101/evidence_BB101_SURREALDOLLS-14885_STG_PASS_02_keep_pending_when_editing_info.png)<br>[evidence_03_dup_email](file:///home/nga/Documents/SurrealDoll/evidence/BB101/evidence_BB101_SURREALDOLLS-14885_STG_PASS_03_duplicate_email_validation.png)<br>[evidence_04_cancel_pending](file:///home/nga/Documents/SurrealDoll/evidence/BB101/evidence_BB101_SURREALDOLLS-14885_STG_PASS_04_cancel_pending_by_reverting_email.png)<br>[evidence_05_fe_page](file:///home/nga/Documents/SurrealDoll/evidence/BB101/evidence_BB101_SURREALDOLLS-14885_STG_PASS_05_verify_email_change_page.png) |

---

## 3. ĐỒNG BỘ BÁO CÁO CỤC BỘ & BACKLOG

- **Backlog Ticket [SURREALDOLLS-14885](https://issoh.backlog.com/view/SURREALDOLLS-14885):**
  - Trạng thái: **`Closed` (完了)**
  - Resolution: **`Fixed`**
  - Actual Hours: **3.50h** (Delta $\Delta \text{Actual} = +0.25\text{h}$)
- **File báo cáo chi tiết:**
  - `bugs/SURREALDOLLS-14130/SURREALDOLLS-14130_bugs.md`
  - `bugs/SURREALDOLLS-14132/SURREALDOLLS-14132_bugs.md`
  - `bugs/SURREALDOLLS-14885/SURREALDOLLS-14885_bugs.md`
