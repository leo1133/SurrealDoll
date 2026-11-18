# UNIVERSAL TESTING RULES (KHUNG QUY CHUẨN KIỂM THỬ ĐA DỰ ÁN BẰNG AI)

Thư mục này chứa trọn vẹn bộ **8 Quy chuẩn Kiểm thử Phần mềm (8 Trụ Cột)** được thiết kế độc lập dự án (Project-Agnostic), phân định rành mạch giữa **Kiểm thử Đặc tả**, **Kiểm thử Giao diện (UI)**, **Kiểm thử Backend API**, **Kiểm thử Thủ công (Manual)**, **Kiểm thử Tự động (Automation)**, **Quản lý Báo cáo Lỗi & Bằng chứng**, **Kiểm thử Cơ sở Dữ liệu (Database)**, và **Ước lượng Tác vụ Kiểm thử (Task Estimation)**, dùng chung cho mọi dự án (Web, SaaS, E-Commerce, ERP, Mobile Web):

---

## I. QUY CHUẨN CẤU TRÚC THƯ MỤC LƯU TRỮ ĐẦU RA (OUTPUT DIRECTORY & NAMING STANDARD)

Để triệt tiêu hoàn toàn tình trạng file bị lưu lộn xộn ở thư mục gốc, mọi sản phẩm do AI hoặc Tester sinh ra **BẮT BUỘC** phải được tự động lưu vào các thư mục chuyên biệt:

```
[Thư mục Dự án]/
├── 📁 Universal_Rules/ -> Quy chuẩn 8 trụ cột kiểm thử phần mềm (Specs, UI, API, Manual, Auto, Bug, Database, Estimate)
├── 📁 Q&A/            -> [Tên màn hình]_Q&A.md        (Rule 01: Câu hỏi làm rõ spec & giả định)
├── 📁 testcase_ui/    -> [Tên màn hình]_testcase.md   (Rule 02 & 04: Kịch bản & Kết quả UI manual)
├── 📁 testcase_api/   -> [Tên màn hình]_api.md        (Rule 03: Kịch bản kiểm thử backend API)
├── 📁 automation/     -> [Tên màn hình]_readme.md     (Rule 05: Kịch bản Playwright POM & runner)
├── 📁 bugs/           -> [Mã_màn]/[Mã_màn]_bugs.md    (Rule 06: Báo cáo danh sách lỗi & chi tiết bug)
├── 📁 evidence/       -> [Mã_màn]/evidence_{{MÃ}}_{{TC_ID}}_{{Mô_tả}}.png (Rule 06: Ảnh chụp bằng chứng lỗi)
├── 📁 estimates/      -> [Mã_hoặc_Ticket]_estimate.md (Rule 08: Báo cáo ước lượng kiểm thử theo loại task)
├── 📁 test_specs/     -> Snapshot JSON trích xuất từ Google Sheets 17 cột ([MÃ]_online.json)
└── 📁 test_files/     -> Dữ liệu mẫu kiểm thử tải file (5MB, 10MB, đúng/sai định dạng)
```

| Thư mục Lưu Trữ | Định Dạng File Bắt Buộc | Quy Định Trong Rule | Ví Dụ Màn Hình `AE800` / `AS100` |
| :--- | :--- | :--- | :--- |
| **`Q&A/`** | `[Tên màn hình]_Q&A.md` | Rule 01 | `Q&A/AE800_Q&A.md` |
| **`testcase_ui/`** | `[Tên màn hình]_testcase.md` | Rule 02, 04 | `testcase_ui/AE800_testcase.md` |
| **`testcase_api/`** | `[Tên màn hình]_api.md` | Rule 03 | `testcase_api/AE800_api.md` |
| **`automation/`** | `[Tên màn hình]_readme.md` | Rule 05 | `automation/AE800_readme.md` |
| **`bugs/`** | `[Mã_màn]/[Mã_màn]_bugs.md` | Rule 06 | `bugs/AS100/AS100_bugs.md` |
| **`evidence/`** | `[Mã_màn]/evidence_{{MÃ}}_{{TC_ID}}_{{Mô_tả}}.png` | Rule 06 | `evidence/AS100/evidence_AS100_TC354_store_fee_hyphen.png` |
| **`estimates/`** | `[Mã_hoặc_Ticket]_estimate.md` | Rule 08 | `estimates/SURREALDOLLS-14230_estimate.md` |

> [!WARNING]
> **Quy định nghiêm ngặt:** Tuyệt đối không lưu file kết quả hoặc ảnh chụp màn hình tự do ở thư mục gốc của dự án. AI khi nhận lệnh xuất file bắt buộc phải tự động kiểm tra/tạo thư mục tương ứng và lưu đúng đường dẫn quy chuẩn ở trên.

---

## II. DANH MỤC CÁC FILE QUY CHUẨN 8 TRỤ CỘT (`Universal_Rules/`)

| File Quy Chuẩn | Phạm Vi & Vai Trò | Thư Mục Đầu Ra Tương Ứng |
| :--- | :--- | :--- |
| [01_core_spec_analysis_rule.md](Universal_Rules/01_core_spec_analysis_rule.md) | **Trụ cột 1:** Phân tích Spec 2-Pass, đối chiếu Figma 1:1 & Lập Q&A (Option A/B) | Lưu vào `Q&A/[Tên màn hình]_Q&A.md` |
| [02_manual_ui_test_case_rule.md](Universal_Rules/02_manual_ui_test_case_rule.md) | **Trụ cột 2 (Manual Design):** Thiết kế Test Case Giao diện (Đối chiếu bộ ba sheet `CommonSpec`, `Common MSG`, `MSG`; Checklist Common Controls & CMR bắt buộc; Header 1 TC/cột; 8 viewpoints KPI; Nạp thông điệp nguyên văn) | Lưu vào `testcase_ui/[Tên màn hình]_testcase.md` |
| [03_api_test_case_rule.md](Universal_Rules/03_api_test_case_rule.md) | **Trụ cột 3 (API Design):** Thiết kế Test Case Backend API (419 viewpoints, toàn vẹn DB, A1-A14) | Lưu vào `testcase_api/[Tên màn hình]_api.md` |
| [04_manual_test_execution_rule.md](Universal_Rules/04_manual_test_execution_rule.md) | **Trụ cột 4 (Manual Execution):** Thực Thi Kiểm Thử Thủ Công (Role matrix, Round 1/2 trên Sheet, Đối soát CSDL, Retest & Sign-off) | Cập nhật vào `testcase_ui/` & Google Sheets |
| [05_automation_test_rule.md](Universal_Rules/05_automation_test_rule.md) | **Trụ cột 5 (Automation):** Kiểm Thử Tự Động Hóa (Sinh code Playwright POM, Triple-Layer E2E, Resilient Locators, Smart Waiting) | Lưu vào `automation/[Tên màn hình]_readme.md` |
| [06_bug_reporting_rule.md](Universal_Rules/06_bug_reporting_rule.md) | **Trụ cột 6 (Bug & Evidence):** Quản Lý Báo Cáo Lỗi & Bằng Chứng (Atomic Screenshot, Bug Template, Fail Table, DB Query Log) | Lưu vào `bugs/[Mã_màn]/[Mã_màn]_bugs.md` & `evidence/[Mã_màn]/` |
| [07_database_testing_rule.md](Universal_Rules/07_database_testing_rule.md) | **Trụ cột 7 (Database Testing):** Kiểm Thử Cơ Sở Dữ Liệu & Đối Soát Tính Toàn Vẹn Dữ Liệu (Xác thực 3 chiều UI ↔ API ↔ DB, Read-Only Safety, Data Seeding & Teardown, Audit Trail, Zero-Hardcoding) | `logs/db/` hoặc đính kèm vào `testcase_ui/` & `bugs/` |
| [08_task_estimation_rule.md](Universal_Rules/08_task_estimation_rule.md) | **Trụ cột 8 (Estimation):** Ước Lượng Tác Vụ Kiểm Thử Thực Tế (Định mức Bug UI/Val/Logic, New Feature Task Design & Exec, Verify Bug Subtasks) | `estimates/[Mã_hoặc_Ticket]_estimate.md` hoặc báo cáo trực tiếp |

---

## III. DỮ LIỆU CACHE TEST CASES GOOGLE SHEETS (`test_specs/`)

Thư mục `test_specs/` lưu snapshot JSON tải từ Google Sheets Master (theo [TEST_CONFIG.md](TEST_CONFIG.md)):
- `[MÃ_MÀN]_online.json`: Bản snapshot online mới nhất (gồm 5 dòng header metadata tổng quan và toàn bộ các hàng test case 17 cột từ A đến Q).
- `[MÃ_MÀN].json`: Bản snapshot trích xuất phần nội dung test case.

---

## IV. GIAO THỨC TỰ ĐỘNG NHẬN DIỆN FILE & CÚ PHÁP RA LỆNH (TASK ROUTER & AUTO-DISCOVERY)

Theo quy chuẩn điều hành tại [GEMINI.md](GEMINI.md), Agent được tích hợp **Giao thức Tự động Nhận diện File (Auto-Discovery Protocol)** và **Cơ chế Phân giải Ngữ cảnh (Context Resolution)**. Người dùng **KHÔNG CẦN** gõ câu lệnh dài dòng, không cần chỉ định đường dẫn file đầu vào hay @ mention từng rule một cách thủ công.

Chỉ cần ra lệnh bằng các **cú pháp ngắn gọn**, Agent sẽ tự động trích xuất mã màn hình, tự nạp đúng Rule chuẩn và tự động quét các file đầu vào theo thứ tự ưu tiên:

| Giai Đoạn & Tác Vụ | Cú Pháp Ra Lệnh Ngắn Gọn | Rule Tự Nạp | Nguồn Đầu Vào Tự Động Quét (Theo thứ tự) | Thư Mục Đầu Ra Chuẩn |
| :--- | :--- | :--- | :--- | :--- |
| **1. Phân tích Spec & Lập Q&A** | • `phân tích spec [MÃ]`<br>• `làm rõ spec [MÃ]`<br>• `tạo Q&A [MÃ]` | [Rule 01](Universal_Rules/01_core_spec_analysis_rule.md) | 1. `test_specs/[MÃ]_online.json` hoặc `test_specs/[MÃ].json`<br>2. [TEST_CONFIG.md](TEST_CONFIG.md) (Google Sheet SRS: Tab màn hình, CommonSpec, Common MSG, MSG)<br>3. Figma / Mockup link có trong spec | `Q&A/[Mã_màn]_Q&A.md` |
| **2. Thiết kế Testcase UI** | • `gen testcase [MÃ]`<br>• `viết testcase UI [MÃ]`<br>• `tạo kịch bản UI [MÃ]` | [Rule 02](Universal_Rules/02_manual_ui_test_case_rule.md) | 1. `test_specs/[MÃ]_online.json` hoặc `test_specs/[MÃ].json`<br>2. `Q&A/[MÃ]_Q&A.md` (nếu đã có làm rõ nghiệp vụ)<br>3. `UI_controls/` (tự quét spec để nạp các control tương ứng)<br>4. [TEST_CONFIG.md](TEST_CONFIG.md) | `testcase_ui/[Mã_màn]_testcase.md`<br>*(Bắt buộc có cột `Automation Feasibility` theo tỷ lệ ~80% Auto / ~20% Manual)* |
| **3. Thiết kế Testcase API** | • `gen testcase API [MÃ]`<br>• `viết testcase API [MÃ]`<br>• `tạo kịch bản API [MÃ]` | [Rule 03](Universal_Rules/03_api_test_case_rule.md) | 1. `test_specs/[MÃ]_online.json` hoặc `test_specs/[MÃ].json`<br>2. `API_controls/API_Viewpoint.md` (419 viewpoints backend logic)<br>3. [TEST_CONFIG.md](TEST_CONFIG.md) (Postman Collection link & Swagger)<br>4. `Q&A/[MÃ]_Q&A.md` (nếu có logic/ràng buộc đã chốt) | `testcase_api/[Mã_màn]_api.md` |
| **4. Thực thi Manual Test** | • `run test [MÃ]`<br>• `test manual [MÃ]`<br>• `retest round 2 [MÃ]` | [Rule 04](Universal_Rules/04_manual_test_execution_rule.md)<br>& [Rule 07](Universal_Rules/07_database_testing_rule.md) | 1. `testcase_ui/[MÃ]_testcase.md`<br>2. [TEST_CONFIG.md](TEST_CONFIG.md) (URL môi trường, Basic Auth, Tài khoản Admin/Agency, DB Tunnel)<br>3. `test_files/` (Tự lấy file upload hợp lệ / không hợp lệ: png, jpg, pdf...) | Sheet Master & `testcase_ui/` |
| **5. Sinh Mã Automation** | • `gen script auto [MÃ]`<br>• `viết code auto [MÃ]`<br>• `tạo test playwright [MÃ]` | [Rule 05](Universal_Rules/05_automation_test_rule.md)<br>& [Rule 07](Universal_Rules/07_database_testing_rule.md) | 1. **Cả 2 kịch bản**: `testcase_ui/[MÃ]_testcase.md` **VÀ** `testcase_api/[MÃ]_api.md`<br>2. `test_specs/[MÃ]_online.json` hoặc `test_specs/[MÃ].json`<br>3. [TEST_CONFIG.md](TEST_CONFIG.md) (Target project: `../live2d`, URLs, Credentials, DB Tunnel)<br>4. `test_files/` (Fixture data upload) | Project Automation `../live2d` (`src/pages/`, `src/api/`, `src/db/`, `tests/`) & `automation/[Mã_màn]_readme.md` |
| **6. Báo cáo & Rà soát Bug** | • `log bug [MÃ]`<br>• `báo cáo lỗi [MÃ]`<br>• `tổng hợp bug [MÃ]`<br>• `check list bug [MÃ]`<br>• `danh sách bug [MÃ]` | [Rule 06](Universal_Rules/06_bug_reporting_rule.md)<br>& [Rule 08](Universal_Rules/08_task_estimation_rule.md) | 1. `bugs/[MÃ]/[MÃ]_bugs.md` (khi check list bug)<br>2. `testcase_ui/[MÃ]_testcase.md` (hoặc log chạy test thực tế: TC Fail, Step, Expected)<br>3. `evidence/[Mã_màn]/` (ảnh chụp fail per-step & log HTTP/console)<br>4. `test_specs/[MÃ].json` (đối chiếu mã lỗi MSG / CMMSG chính xác) | `bugs/[Mã_màn]/[Mã_màn]_bugs.md` & `evidence/[Mã_màn]/`<br>*(Lệnh `check list bug` bắt buộc lên Est cho từng bug để kiểm soát thời gian)* |
| **7. Xác thực & Retest Bug (Verify Bug)** | • `verify bug [MÃ/TICKET]`<br>• `kiểm tra lại bug [MÃ/TICKET]`<br>• `retest bug [TICKET]`<br>• `xác nhận bug [TICKET]` | [Rule 06](Universal_Rules/06_bug_reporting_rule.md)<br>& [Rule 04](Universal_Rules/04_manual_test_execution_rule.md)<br>& [Rule 08](Universal_Rules/08_task_estimation_rule.md)<br>& [Rule 07](Universal_Rules/07_database_testing_rule.md) | 1. Ticket Backlog / Issue details<br>2. `bugs/[MÃ]/[MÃ]_bugs.md`<br>3. `testcase_ui/[MÃ]_testcase.md`<br>4. [TEST_CONFIG.md](TEST_CONFIG.md) (Môi trường DEV/STG, SSM DB Tunnel)<br>5. `evidence/[Mã_màn]/` | Cập nhật Backlog Ticket + Sheet Test Case Khối Round 2 (Cột M:Q) + `bugs/[Mã_màn_hoặc_Ticket]/[Mã_màn_hoặc_Ticket]_bugs.md` & `evidence/[Mã_màn]/`<br>*(Bắt buộc: Mở đúng DEV/STG, chụp ảnh evidence Pass/Fail, cập nhật 3 chiều và log Actual Delta)* |
| **8. Kiểm tra CSDL & Đối soát** | • `check db`<br>• `đối soát db`<br>• `query db [MÃ]` | [Rule 07](Universal_Rules/07_database_testing_rule.md) | 1. [TEST_CONFIG.md](TEST_CONFIG.md) (Thông tin kết nối CSDL & SSM Tunnel)<br>2. Spec ERD / Data Dictionary / Mapping spec<br>3. `testcase_ui/[MÃ]_testcase.md` & `testcase_api/[MÃ]_api.md` | `logs/db/` hoặc đính kèm kết quả đối soát vào `testcase_ui/` / `bugs/` |
| **9. Ước lượng & Kế hoạch 8h** | • `estimate [MÃ/TICKET]`<br>• `ước lượng [MÃ/TICKET]`<br>• `check task`<br>• `kiểm tra task`<br>• `kế hoạch hôm nay` | [Rule 08](Universal_Rules/08_task_estimation_rule.md) | 1. Backlog Board / Ticket qua [TEST_CONFIG.md](TEST_CONFIG.md)<br>2. Danh sách subtasks / bugs<br>3. `test_specs/[MÃ].json` (nếu là task màn hình mới) | `estimates/[Mã_hoặc_Ticket]_estimate.md` hoặc báo cáo trực tiếp<br>*(Lệnh `check task` lọc Need Verify Dev/STG, In Progress, Open due hôm nay/mai -> Lên Est đủ 8h/ngày, ưu tiên Verify. Nếu quá 8h, thông báo xin PM lùi plan)* |

### Cơ chế Suy luận Ngữ cảnh (Context Fallback)
Khi câu lệnh của người dùng chỉ ghi ngắn gọn không kèm mã màn hình (ví dụ: `gen testcase`, `run test`, `log bug`):
1. **Lịch sử trao đổi gần nhất:** Agent tự động kiểm tra xem các lượt trao đổi trước đang làm việc với màn hình nào $\rightarrow$ Tự động dùng ngay mã màn hình đó.
2. **File workspace vừa thay đổi:** Agent tự động kiểm tra xem trong workspace vừa có thay đổi/tạo mới file liên quan đến màn hình nào $\rightarrow$ Tự động dùng mã màn hình đó.
3. **Hỏi tối giản 1 câu duy nhất:** Chỉ khi hoàn toàn không có bất kỳ thông tin nào trong ngữ cảnh, Agent mới dừng lại hỏi: *"Bạn muốn thực hiện cho mã màn hình nào (ví dụ: BA100, BC100...)?"*. Sau khi nhận câu trả lời, toàn bộ quy trình đọc file và thực thi được kích hoạt tự động mà không hỏi thêm.
