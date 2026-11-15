# MASTER AGENT POLICY (GEMINI.md)

Quy chuẩn điều hành & kỷ luật hành vi bắt buộc cho Agent trên toàn dự án:

---

## 1. Task Router (Điều phối quy chuẩn)
Khi nhận tác vụ, tự động nạp và tuân thủ rule tương ứng trong `Universal_Rules/`:

| Tác vụ | Rule tham chiếu | Thư mục đầu ra chuẩn |
| :--- | :--- | :--- |
| **Phân tích Spec & Q&A** | [01_core_spec_analysis_rule.md](Universal_Rules/01_core_spec_analysis_rule.md) | `Q&A/[Mã_màn]_Q&A.md` |
| **Testcase Giao diện** | [02_manual_ui_test_case_rule.md](Universal_Rules/02_manual_ui_test_case_rule.md) | `testcase_ui/[Mã_màn]_testcase.md` |
| **Testcase Backend API** | [03_api_test_case_rule.md](Universal_Rules/03_api_test_case_rule.md) | `testcase_api/[Mã_màn]_api.md` |
| **Thực thi Manual Test** | [04_manual_test_execution_rule.md](Universal_Rules/04_manual_test_execution_rule.md) | Sheet 17 cột & `testcase_ui/` |
| **Automation Test** | [05_automation_test_rule.md](Universal_Rules/05_automation_test_rule.md) | `automation/[Mã_màn]_readme.md` |
| **Báo cáo Bug & Evidence**| [06_bug_reporting_rule.md](Universal_Rules/06_bug_reporting_rule.md) | `bugs/[Mã_màn]/` & `evidence/[Mã_màn]/` |

---

## 2. Ranh giới đỏ (Core Guardrails)

> [!CAUTION]
> **NGHIÊM CẤM VI PHẠM TRÊN MỌI MÀN HÌNH VÀ TÁC VỤ:**
>
> 1. **Phân định Round 1 vs Round 2:** Khi test Round 2 / Retest, **CẤM TUYỆT ĐỐI** lấy kết quả Round 1 (Cột H:L) báo `Pass` cho Round 2 hoặc copy đè kết quả. Bắt buộc test lại trên môi trường live và chỉ ghi nhận vào khối **Round 2 (Cột M:Q)**.
> 2. **No Execution, No Pass:** Cấm suy đoán từ code FE/BE, file build JS hoặc dùng mocking để báo `Pass` cho test thủ công. Chỉ kết luận `Pass`/`Fail` khi thao tác thực tế trên browser/API live.
> 3. **Chủ động Thiết lập Tiền đề & Dữ liệu (Proactive Preconditions & Data Seeding):** Khi gặp ca kiểm thử thiếu dữ liệu mẫu hoặc yêu cầu điều kiện tiên quyết (kể cả liên màn hình hoặc phối hợp liên vai trò RBAC/Cross-role), Tester/Agent **BẮT BUỘC chủ động tự tạo/cấu hình** qua giao diện người dùng (UI) hoặc API có sẵn trong cấu hình kiểm thử. **NGHIÊM CẤM** dừng lại báo `Blocked`/`Pending` thụ động khi luồng hệ thống hoặc tài khoản được cấp cho phép tự thiết lập. CHỈ ĐƯỢC PHÉP báo `Blocked` khi điều kiện đó bắt buộc can thiệp trực tiếp Database hoặc tài khoản đặc thù chưa được cấp quyền. Tuyệt đối không tự ý đánh `Pass` khi chưa thực thi kiểm tra thực tế.
> 4. **No Evidence, No Report:** Mọi ca `Fail` và Bug Report bắt buộc phải có ảnh chụp độc lập (Atomic Screenshot) hoặc HTTP log thực tế tại thời điểm lỗi. Không bằng chứng $\rightarrow$ Không công nhận kết quả.
> 5. **Bảo tồn Công thức Bảng tính (Zero-Hardcoding & Formula Integrity):** Tuyệt đối **CẤM GHI ĐÈ GIÁ TRỊ TĨNH** (số đếm Pass/Fail, phần trăm, text) vào các ô công thức thống kê trên Dashboard (dòng 1-7) và Sheet tổng hợp kết quả (Master / Result). Kết quả kiểm thử **CHỈ ĐƯỢC GHI NHẬN** vào từng dòng testcase thực tế (Cột Result: H hoặc M từ dòng 8 trở đi); toàn bộ chỉ số tổng hợp bắt buộc phải được tính toán tự động 100% bằng công thức.

---

## 3. Quy chuẩn Thư mục & File

- **Clean Workspace:** Tuyệt đối không sinh file nháp, kết quả hay ảnh screenshot tự do ở thư mục gốc repo.
- **Subfolder bắt buộc theo từng màn hình:**
  - **Báo cáo lỗi:** `bugs/[Mã_màn_hình]/[Mã_màn_hình]_bugs.md` (hoặc `bug/`)
  - **Ảnh bằng chứng:** `evidence/[Mã_màn_hình]/evidence_{{MÃ}}_{{TC_ID}}_{{Timestamp/Mô_tả}}.png`

---

## 4. Cấu hình & Định danh Dự án

- **Environment & Spec:** Đọc và đối chiếu từ [TEST_CONFIG.md](TEST_CONFIG.md) ở thư mục gốc.
- **Tester ID:** Theo cấu hình tại `TEST_CONFIG.md` (mặc định) hoặc do User chỉ định.
