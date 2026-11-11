# UNIVERSAL TESTING RULES (KHUNG QUY CHUẨN KIỂM THỬ ĐA DỰ ÁN BẰNG AI)

Thư mục này chứa trọn vẹn bộ **6 Quy chuẩn Kiểm thử Phần mềm** được thiết kế độc lập dự án (Project-Agnostic), phân định rành mạch giữa **Kiểm thử Thủ công (Manual)** và **Kiểm thử Tự động (Automation)**, dùng chung cho mọi dự án (Web, SaaS, E-Commerce, ERP, Mobile Web):

---

## I. QUY CHUẨN CẤU TRÚC THƯ MỤC LƯU TRỮ ĐẦU RA (OUTPUT DIRECTORY & NAMING STANDARD)

Để triệt tiêu hoàn toàn tình trạng file bị lưu lộn xộn ở thư mục gốc, mọi sản phẩm do AI hoặc Tester sinh ra **BẮT BUỘC** phải được tự động lưu vào các thư mục chuyên biệt:

```
[Thư mục Dự án]/
├── 📁 Q&A/           -> [Tên màn hình]_Q&A.md        (Rule 01: Toàn bộ câu hỏi làm rõ spec & giả định)
├── 📁 testcase_ui/   -> [Tên màn hình]_testcase.md   (Rule 02 & 04: Kịch bản & Kết quả kiểm thử giao diện thủ công)
├── 📁 testcase_api/  -> [Tên màn hình]_api.md        (Rule 03: Kịch bản kiểm thử backend API)
├── 📁 automation/    -> [Tên màn hình]_readme.md     (Rule 05: Theo dõi kịch bản manual -> auto & script)
├── 📁 bugs/          -> [Tên màn hình]/[Tên màn hình]_bugs.md       (Rule 06: Báo cáo danh sách lỗi & chi tiết bug theo thư mục màn hình)
└── 📁 evidence/      -> [Tên màn hình]/evidence_{{MÃ_MÀN}}_{{TC_ID}}_{{Mô_tả/Timestamp}}.png (Rule 06: Ảnh chụp bằng chứng theo thư mục màn hình)
```

| Thư mục Lưu Trữ | Định Dạng File Bắt Buộc | Quy Định Trong Rule | Ví Dụ Màn Hình `AE800` |
| :--- | :--- | :--- | :--- |
| **`Q&A/`** | `[Tên màn hình]_Q&A.md` | Rule 01 | `Q&A/AE800_Q&A.md` |
| **`testcase_ui/`** | `[Tên màn hình]_testcase.md` | Rule 02, 04 | `testcase_ui/AE800_testcase.md` |
| **`testcase_api/`** | `[Tên màn hình]_api.md` | Rule 03 | `testcase_api/AE800_api.md` |
| **`automation/`** | `[Tên màn hình]_readme.md` | Rule 05 | `automation/AE800_readme.md` |
| **`bugs/`** | `[Tên màn hình]/[Tên màn hình]_bugs.md` | Rule 06 | `bugs/AE800/AE800_bugs.md` |
| **`evidence/`** | `[Tên màn hình]/evidence_{{MÃ}}_{{TC_ID}}_{{Mô_tả}}.png` | Rule 06 | `evidence/AE800/evidence_AE800_TC05_dup_name.png` |

> [!WARNING]
> **Quy định nghiêm ngặt:** Tuyệt đối không lưu file kết quả hoặc ảnh chụp màn hình tự do ở thư mục gốc của dự án. AI khi nhận lệnh xuất file bắt buộc phải tự động kiểm tra/tạo thư mục tương ứng và lưu đúng đường dẫn quy chuẩn ở trên.

---

## II. DANH MỤC CÁC FILE QUY CHUẨN 6 TRỤ CỘT

| File Quy Chuẩn | Phạm Vi & Vai Trò | Thư Mục Đầu Ra Tương Ứng |
| :--- | :--- | :--- |
| [01_core_spec_analysis_rule.md](file:///home/nga/Documents/SurrealDoll/Universal_Rules/01_core_spec_analysis_rule.md) | **Trụ cột 1:** Phân tích Spec 2-Pass, đối chiếu Figma 1:1 & Lập Q&A (Option A/B) | Lưu vào `Q&A/[Tên màn hình]_Q&A.md` |
| [02_manual_ui_test_case_rule.md](file:///home/nga/Documents/SurrealDoll/Universal_Rules/02_manual_ui_test_case_rule.md) | **Trụ cột 2 (Manual Design):** Thiết kế Test Case Giao diện (Đối chiếu bộ ba sheet `CommonSpec`, `Common MSG`, `MSG`; Checklist Common Controls & CMR bắt buộc; Header 1 TC/cột; 8 viewpoints KPI; Nạp thông điệp nguyên văn) | Lưu vào `testcase_ui/[Tên màn hình]_testcase.md` |
| [03_api_test_case_rule.md](file:///home/nga/Documents/SurrealDoll/Universal_Rules/03_api_test_case_rule.md) | **Trụ cột 3 (API Design):** Thiết kế Test Case Backend API (419 viewpoints, toàn vẹn DB, A1-A14) | Lưu vào `testcase_api/[Tên màn hình]_api.md` |
| [04_manual_test_execution_rule.md](file:///home/nga/Documents/SurrealDoll/Universal_Rules/04_manual_test_execution_rule.md) | **Trụ cột 4 (Manual Execution):** Thực Thi Kiểm Thử Thủ Công (Role matrix, Round 1/2 trên Sheet, Retest & Sign-off) | Cập nhật vào `testcase_ui/` & Google Sheets |
| [05_automation_test_rule.md](file:///home/nga/Documents/SurrealDoll/Universal_Rules/05_automation_test_rule.md) | **Trụ cột 5 (Automation):** Kiểm Thử Tự Động Hóa (Sinh code Playwright POM, Resilient Locators, Smart Waiting) | Lưu vào `automation/[Tên màn hình]_readme.md` |
| [06_bug_reporting_rule.md](file:///home/nga/Documents/SurrealDoll/Universal_Rules/06_bug_reporting_rule.md) | **Trụ cột 6 (Bug & Evidence):** Quản Lý Báo Cáo Lỗi & Bằng Chứng (Atomic Screenshot, Bug Template, Fail Table) | Lưu vào `bugs/[Tên màn hình]_bugs.md` & `evidence/` |

---

## III. CÚ PHÁP RA LỆNH MẪU CHO AI THEO TỪNG GIAI ĐOẠN:

1. **Phân tích Spec & Lập Q&A:**
   > *"Áp dụng rule @01_core_spec_analysis_rule.md để bóc tách Spec màn hình AE800 và lưu kết quả vào thư mục Q&A/."*
2. **Thiết kế Testcase UI Thủ công:**
   > *"Dựa trên Q&A đã chốt, áp dụng rule @02_manual_ui_test_case_rule.md để viết bộ testcase UI màn hình AE800 và lưu vào testcase_ui/."*
3. **Thiết kế Testcase API:**
   > *"Áp dụng rule @03_api_test_case_rule.md để thiết kế bộ testcase API và lưu vào testcase_api/."*
4. **Thực thi Kiểm thử Thủ công & Ghi nhận Kết quả:**
   > *"Áp dụng rule @04_manual_test_execution_rule.md để thực thi kiểm thử thủ công trên môi trường Staging, đánh dấu Pass/Fail/Impact vào cột Round 1 và chuẩn bị quy trình Retest Round 2."*
5. **Sinh Mã Automation & Chạy Tự Động:**
   > *"Áp dụng rule @05_automation_test_rule.md để sinh mã Playwright TypeScript theo chuẩn Page Object Model và lưu file theo dõi vào automation/."*
6. **Báo cáo Lỗi & Thu thập Bằng chứng:**
   > *"Áp dụng rule @06_bug_reporting_rule.md để thu thập ảnh bằng chứng độc lập vào evidence/ và xuất báo cáo lỗi chi tiết vào bugs/."*
