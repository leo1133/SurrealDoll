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
| [01_core_spec_analysis_rule.md](01_core_spec_analysis_rule.md) | **Trụ cột 1:** Phân tích Spec 2-Pass, đối chiếu Figma 1:1 & Lập Q&A (Option A/B) | Lưu vào `Q&A/[Tên màn hình]_Q&A.md` |
| [02_manual_ui_test_case_rule.md](02_manual_ui_test_case_rule.md) | **Trụ cột 2 (Manual Design):** Thiết kế Test Case Giao diện (Đối chiếu bộ ba sheet `CommonSpec`, `Common MSG`, `MSG`; Checklist Common Controls & CMR bắt buộc; Header 1 TC/cột; 8 viewpoints KPI; Nạp thông điệp nguyên văn; **Cột Automation Feasibility định danh ~80% Auto / ~20% Manual**) | Lưu vào `testcase_ui/[Tên màn hình]_testcase.md` |
| [03_api_test_case_rule.md](03_api_test_case_rule.md) | **Trụ cột 3 (API Design):** Thiết kế Test Case Backend API (419 viewpoints, toàn vẹn DB, A1-A14) | Lưu vào `testcase_api/[Tên màn hình]_api.md` |
| [04_manual_test_execution_rule.md](04_manual_test_execution_rule.md) | **Trụ cột 4 (Manual Execution):** Thực Thi Kiểm Thử Thủ Công (Role matrix, Round 1/2 trên Sheet, Retest & Sign-off) | Cập nhật vào `testcase_ui/` & Google Sheets |
| [05_automation_test_rule.md](05_automation_test_rule.md) | **Trụ cột 5 (Automation):** Kiểm Thử Tự Động Hóa (Sinh code Playwright POM, Resilient Locators, Smart Waiting; **Chống sinh mã minh họa & Cam kết độ phủ $\ge 80\%$ bằng Data-Driven Loop**) | Lưu vào `automation/[Tên màn hình]_readme.md` & target repo |
| [06_bug_reporting_rule.md](06_bug_reporting_rule.md) | **Trụ cột 6 (Bug & Evidence):** Quản Lý Báo Cáo Lỗi & Bằng Chứng (Atomic Screenshot, Bug Template, Fail Table) | Lưu vào `bugs/[Tên màn hình]/[Tên màn hình]_bugs.md` & `evidence/` |

---

## III. CÚ PHÁP RA LỆNH TỐI GIẢN (AUTO-DISCOVERY COMMANDS)

Nhờ **Giao thức tự động nhận diện file (Auto-Discovery Protocol)** quy định tại [GEMINI.md](../GEMINI.md), bạn chỉ cần ra lệnh ngắn gọn; Agent sẽ tự động nạp Rule, tìm Spec và xuất đúng thư mục:

1. **Phân tích Spec & Lập Q&A:**
   > `phân tích spec [MÃ_MÀN]` *(Ví dụ: `phân tích spec BA100`)*
2. **Thiết kế Testcase UI Thủ công:**
   > `gen testcase [MÃ_MÀN]` *(Ví dụ: `gen testcase BA100`)*
3. **Thiết kế Testcase Backend API:**
   > `gen testcase API [MÃ_MÀN]` *(Ví dụ: `gen testcase API BA100`)*
4. **Thực thi Kiểm thử Thủ công (Manual Test):**
   > `run test [MÃ_MÀN]` hoặc `retest round 2 [MÃ_MÀN]`
5. **Sinh Mã Automation Playwright:**
   > `gen script auto [MÃ_MÀN]` *(Ví dụ: `gen script auto BA100` - Tự động nạp đồng thời cả `testcase_ui` và `testcase_api` để sinh trọn bộ POM UI, API Client và E2E vào project `live2d`)*
6. **Báo cáo Lỗi & Bằng chứng (Log Bug):**
   > `log bug [MÃ_MÀN]` *(Ví dụ: `log bug BA100`)*

*(Lưu ý: Nếu bạn chỉ gõ lệnh không kèm mã màn như `gen testcase`, AI sẽ tự động lấy mã màn từ ngữ cảnh trao đổi gần nhất).*
