# MASTER AGENT POLICY (GEMINI.md)

Quy chuẩn điều hành, kỷ luật hành vi & giao thức tự động nhận diện tác vụ bắt buộc cho Agent trên toàn dự án:

---

## 1. Task Router & Giao thức tự động nhận diện File (Auto-Discovery Protocol)

Khi nhận các câu lệnh ngắn gọn từ người dùng (như `gen testcase`, `gen testcase API`, `gen script auto`, `log bug`, `phân tích spec`, `run test`), Agent **BẮT BUỘC tự động nhận diện mã màn hình**, tự động nạp **Rule chuẩn** và **quét đúng các file đầu vào theo thứ tự ưu tiên** mà không cần hỏi lại người dùng:

| Tác vụ & Cú pháp gợi ý | Rule tham chiếu | Nguồn file đầu vào tự động (Tự đọc theo thứ tự ưu tiên) | Thư mục đầu ra chuẩn |
| :--- | :--- | :--- | :--- |
| **Phân tích Spec & Q&A**<br>• `phân tích spec [MÃ]`<br>• `làm rõ spec [MÃ]`<br>• `tạo Q&A [MÃ]` | [01_core_spec_analysis_rule.md](Universal_Rules/01_core_spec_analysis_rule.md) | 1. `test_specs/[MÃ]_online.json` hoặc `test_specs/[MÃ].json`<br>2. [TEST_CONFIG.md](TEST_CONFIG.md) (Google Sheet Spec: tab màn hình, CommonSpec, Common MSG, MSG)<br>3. Figma / Mockup link có trong spec | `Q&A/[Mã_màn]_Q&A.md` |
| **Testcase Giao diện**<br>• `gen testcase [MÃ]`<br>• `viết testcase UI [MÃ]`<br>• `tạo kịch bản UI [MÃ]` | [02_manual_ui_test_case_rule.md](Universal_Rules/02_manual_ui_test_case_rule.md) | 1. `test_specs/[MÃ]_online.json` hoặc `test_specs/[MÃ].json`<br>2. `Q&A/[MÃ]_Q&A.md` (nếu đã có làm rõ nghiệp vụ)<br>3. `UI_controls/` (tự quét spec để nạp các control tương ứng: input, button, table, dropdown...)<br>4. [TEST_CONFIG.md](TEST_CONFIG.md) | `testcase_ui/[Mã_màn]_testcase.md`<br>*(Bắt buộc có cột `Automation Feasibility` phân loại 4 nhóm chuẩn theo tỷ lệ ~80% Auto / ~20% Manual)* |
| **Testcase Backend API**<br>• `gen testcase API [MÃ]`<br>• `viết testcase API [MÃ]`<br>• `tạo kịch bản API [MÃ]` | [03_api_test_case_rule.md](Universal_Rules/03_api_test_case_rule.md) | 1. `test_specs/[MÃ]_online.json` hoặc `test_specs/[MÃ].json`<br>2. `API_controls/API_Viewpoint.md` (419 viewpoints backend logic)<br>3. [TEST_CONFIG.md](TEST_CONFIG.md) (Postman Collection link & Swagger)<br>4. `Q&A/[MÃ]_Q&A.md` (nếu có logic/ràng buộc đã chốt) | `testcase_api/[Mã_màn]_api.md` |
| **Thực thi Manual Test**<br>• `run test [MÃ]`<br>• `test manual [MÃ]`<br>• `retest round 2 [MÃ]` | [04_manual_test_execution_rule.md](Universal_Rules/04_manual_test_execution_rule.md)<br>& [07_database_testing_rule.md](Universal_Rules/07_database_testing_rule.md) | 1. `testcase_ui/[MÃ]_testcase.md`<br>2. [TEST_CONFIG.md](TEST_CONFIG.md) (URL, Basic Auth, Tài khoản Admin/Agency, DB Tunnel)<br>3. `test_files/` (Tự lấy file upload hợp lệ/không hợp lệ: png, jpg, pdf...) | Sheet 17 cột & `testcase_ui/` |
| **Automation Test**<br>• `gen script auto [MÃ]`<br>• `viết code auto [MÃ]`<br>• `tạo test playwright [MÃ]` | [05_automation_test_rule.md](Universal_Rules/05_automation_test_rule.md)<br>& [07_database_testing_rule.md](Universal_Rules/07_database_testing_rule.md) | 1. **Cả 2 kịch bản**: `testcase_ui/[MÃ]_testcase.md` **VÀ** `testcase_api/[MÃ]_api.md`<br>2. `test_specs/[MÃ]_online.json` hoặc `test_specs/[MÃ].json`<br>3. [TEST_CONFIG.md](TEST_CONFIG.md) (Target: `../live2d`, URLs, Credentials, DB Tunnel)<br>4. `test_files/` (Fixture data upload) | Project Automation `../live2d` (`src/pages/`, `src/api/`, `src/db/`, `tests/`) & `automation/[Mã_màn]_readme.md` |
| **Kiểm tra CSDL & Đối soát**<br>• `check db`<br>• `đối soát db`<br>• `query db [MÃ]` | [07_database_testing_rule.md](Universal_Rules/07_database_testing_rule.md) | 1. [TEST_CONFIG.md](TEST_CONFIG.md) (Thông tin kết nối CSDL & SSM Tunnel)<br>2. Spec ERD / Data Dictionary<br>3. Kịch bản testcase cần đối soát dữ liệu | Báo cáo đối soát trong bảng testcase hoặc `evidence/` |
| **Báo cáo Bug & Evidence**<br>• `log bug [MÃ]`<br>• `báo cáo lỗi [MÃ]`<br>• `tổng hợp bug [MÃ]` | [06_bug_reporting_rule.md](Universal_Rules/06_bug_reporting_rule.md) | 1. `testcase_ui/[MÃ]_testcase.md` (hoặc log chạy test thực tế: TC Fail, Step, Expected)<br>2. `evidence/[Mã_màn]/` (ảnh chụp fail per-step & log HTTP/console/DB)<br>3. `test_specs/[MÃ].json` (đối chiếu mã lỗi MSG / CMMSG chính xác) | `bugs/[Mã_màn]/[Mã_màn]_bugs.md` & `evidence/[Mã_màn]/` |

---

## 2. Cơ chế Xác định Mã Màn hình & Ngữ cảnh (Screen ID & Context Resolution)

Khi nhận câu lệnh từ người dùng:
1. **Trực tiếp qua câu lệnh:** Nếu câu lệnh chứa mã màn (ví dụ: `gen testcase BA100`, `log bug BC200`), trích xuất ngay `MÃ = BA100`.
2. **Suy luận từ ngữ cảnh hội thoại (Context Fallback):** Nếu câu lệnh chỉ ghi `gen testcase` hoặc `log bug` không kèm mã, Agent **tự động kiểm tra lịch sử trao đổi gần nhất**:
   - Nếu trong các lượt trao đổi trước đang làm việc với một mã màn hình cụ thể $\rightarrow$ Tự động dùng ngay mã màn hình đó.
   - Nếu trong workspace vừa có thay đổi/tạo mới file liên quan đến một mã màn hình $\rightarrow$ Tự động dùng mã màn hình đó.
3. **Hỏi tối giản khi không có bất kỳ ngữ cảnh nào:** Chỉ khi hoàn toàn không có thông tin mã màn hình trong lịch sử, Agent mới dừng lại hỏi đúng **1 câu duy nhất**: *"Bạn muốn thực hiện cho mã màn hình nào (ví dụ: BA100, BC100...)?*". Sau khi người dùng trả lời mã màn, lập tức tự động kích hoạt toàn bộ quy trình đọc file mà không hỏi thêm.

---

## 3. Ranh giới đỏ (Core Guardrails)

> [!CAUTION]
> **NGHIÊM CẤM VI PHẠM TRÊN MỌI MÀN HÌNH VÀ TÁC VỤ:**
>
> 1. **Phân định Round 1 vs Round 2:** Khi test Round 2 / Retest, **CẤM TUYỆT ĐỐI** lấy kết quả Round 1 (Cột H:L) báo `Pass` cho Round 2 hoặc copy đè kết quả. Bắt buộc test lại trên môi trường live và chỉ ghi nhận vào khối **Round 2 (Cột M:Q)**.
> 2. **No Execution, No Pass:** Cấm suy đoán từ code FE/BE, file build JS hoặc dùng mocking để báo `Pass` cho test thủ công. Chỉ kết luận `Pass`/`Fail` khi thao tác thực tế trên browser/API live.
> 3. **Chủ động Thiết lập Tiền đề & Dữ liệu (Proactive Preconditions & Data Seeding):** Khi gặp ca kiểm thử thiếu dữ liệu mẫu hoặc yêu cầu điều kiện tiên quyết (kể cả liên màn hình hoặc phối hợp liên vai trò RBAC/Cross-role), Tester/Agent **BẮT BUỘC chủ động tự tạo/cấu hình** qua giao diện người dùng (UI) hoặc API có sẵn trong cấu hình kiểm thử. **NGHIÊM CẤM** dừng lại báo `Blocked`/`Pending` thụ động khi luồng hệ thống hoặc tài khoản được cấp cho phép tự thiết lập. CHỈ ĐƯỢC PHÉP báo `Blocked` khi điều kiện đó bắt buộc can thiệp trực tiếp Database hoặc tài khoản đặc thù chưa được cấp quyền. Tuyệt đối không tự ý đánh `Pass` khi chưa thực thi kiểm tra thực tế.
> 4. **No Evidence, No Report:** Mọi ca `Fail` và Bug Report bắt buộc phải có ảnh chụp độc lập (Atomic Screenshot) hoặc HTTP log thực tế tại thời điểm lỗi. Không bằng chứng $\rightarrow$ Không công nhận kết quả.
> 5. **Bảo tồn Công thức Bảng tính (Zero-Hardcoding & Formula Integrity):** Tuyệt đối **CẤM GHI ĐÈ GIÁ TRỊ TĨNH** (số đếm Pass/Fail, phần trăm, text) vào các ô công thức thống kê trên Dashboard (dòng 1-7) và Sheet tổng hợp kết quả (Master / Result). Kết quả kiểm thử **CHỈ ĐƯỢC GHI NHẬN** vào từng dòng testcase thực tế (Cột Result: H hoặc M từ dòng 8 trở đi); toàn bộ chỉ số tổng hợp bắt buộc phải được tính toán tự động 100% bằng công thức.
> 6. **Phân loại Automation Feasibility Bắt buộc (Mandatory Automation Tagging):** Khi thiết kế testcase giao diện, Agent **BẮT BUỘC** phải điền đầy đủ 100% cột `Automation Feasibility` trên từng dòng testcase theo 4 giá trị chuẩn: `Auto-UI`, `Auto-API`, `Auto-Data`, `Manual-Only` (kèm lý do trong ngoặc đơn: Visual, Complex DB, 3rd-party, UX) tuân thủ tỷ lệ vàng ~70-80% Auto và ~20-30% Manual. Nghiêm cấm để trống hoặc gán cứng 100% testcase là Auto hay 100% Manual.
> 7. **Chống Sinh Mã Minh Họa & Cam Kết Độ Phủ Automation >= 80% (Anti-Scaffolding & Minimum 80% Coverage Enforcement):** Khi thực hiện tác vụ sinh mã automation cho bất kỳ màn hình hoặc module nào trên toàn bộ dự án, Agent **TUYỆT ĐỐI CẤM** sinh mã kiểu "khung sườn / làm mẫu" (chỉ viết vài ca tượng trưng cho mỗi nhóm rồi bỏ sót hàng chục đến hàng trăm ca kiểm thử khác).
>    - **Nguyên tắc chuyển đổi toàn vẹn:** Mọi testcase được phân loại `Auto-UI`, `Auto-API`, `Auto-Data` từ cả hai nguồn kịch bản UI và API bắt buộc phải có mã kiểm thử thực thi tương ứng. Với các nhóm kiểm thử có số lượng lớn (input validation, boundary, status code, 419 API viewpoints), bắt buộc ứng dụng kỹ thuật Data-Driven Testing (đóng gói ma trận ca kiểm thử vào mảng dữ liệu tập trung tại `test-data/` và dùng vòng lặp Playwright `for...of` hoặc `test.describe.each` để phủ 100% các ca kiểm thử).
>    - **Cổng đối soát định lượng bắt buộc:** Tổng số ca kiểm thử Playwright thực tế chạy được bắt buộc phải đạt tối thiểu **70% - 80%** trên tổng số ca kiểm thử của màn hình ($\frac{N_{\text{Auto}}}{N_{\text{UI}} + N_{\text{API}} - N_{\text{Manual-Only}}} \ge 80\%$). Nếu tỷ lệ đạt $< 70\%$, nhiệm vụ bị coi là **Không Đạt (Rejected)** và Agent bắt buộc phải tiếp tục bổ sung cho đến khi đủ độ phủ mới được nghiệm thu bàn giao.
> 8. **An toàn CSDL & Nguyên tắc Read-Only Tuyệt Đối (Database Safety & Zero Data Corruption):** Khi thực thi kiểm thử hoặc đối soát dữ liệu trên mọi môi trường dùng chung (Dev, Staging), Agent **TUYỆT ĐỐI CHỈ SỬ DỤNG TÀI KHOẢN READ-ONLY**. Nghiêm cấm mọi hành vi thực thi câu lệnh làm biến đổi hoặc phá hủy dữ liệu (như `UPDATE`, `DELETE`, `DROP`, `TRUNCATE`). Mọi kết nối CSDL phải tuân thủ nghiêm ngặt chuẩn bảo mật mã hóa SSL và giới hạn thời gian chờ truy vấn theo [07_database_testing_rule.md](Universal_Rules/07_database_testing_rule.md).
> 9. **Triệt Tiêu Hardcode Selector & Chuẩn Hóa 100% Dữ Liệu Động (Zero-Hardcoded Selectors & Dynamic Data Standardization):**
>    - **Tuyệt đối cấm Raw Selectors & Magic Index:** Nghiêm cấm viết raw selector strings (CSS, XPath, id, class) hoặc magic column index (`nth(4)`, `last()`) trực tiếp trong Page Object hay Test Specs. Toàn bộ selector tĩnh phải được quy hoạch thành biến tập trung trong object `selectors` tại `src/test-data/`; toàn bộ vị trí cột phải được ánh xạ qua object `columns`.
>    - **Bắt buộc tham số hóa Locator Động (Parameterized Locators):** Mọi phần tử mang tính động (theo ID bản ghi, theo tên menu/submenu, theo tiêu đề cột, theo trạng thái) bắt buộc phải đóng gói thành các hàm/phương thức nhận tham số (`getSidebarMenu(name)`, `getTableCell(row, colName)`, `getTableRowById(id)`). Nghiêm cấm gán cứng một nhãn cố định vào thuộc tính trong constructor.
>    - **Chuẩn hóa Dữ liệu Động (Dynamic Data Governance):** Toàn bộ dữ liệu kiểm thử mang tính động (Unique IDs, ngày tháng, query URL params, form/API payloads, assertions) bắt buộc phải sử dụng helpers/factories sinh động (UUID, dynamic date helpers, query builder, schema matchers), tuyệt đối không gán cứng literal values (`"Tokyo"`, `"page=-1"`, `"2026-11-16"`).

---

## 4. Quy chuẩn Thư mục & File

- **Clean Workspace:** Tuyệt đối không sinh file nháp, kết quả hay ảnh screenshot tự do ở thư mục gốc repo.
- **Subfolder bắt buộc theo từng màn hình:**
  - **Báo cáo lỗi:** `bugs/[Mã_màn_hình]/[Mã_màn_hình]_bugs.md`
  - **Ảnh bằng chứng:** `evidence/[Mã_màn_hình]/evidence_{{MÃ}}_{{TC_ID}}_{{Timestamp/Mô_tả}}.png`
  - **Kịch bản UI:** `testcase_ui/[Mã_màn_hình]_testcase.md`
  - **Kịch bản API:** `testcase_api/[Mã_màn_hình]_api.md`
  - **Automation:** Mã nguồn lưu trực tiếp vào project target `../live2d` theo chuẩn định danh đồng bộ 100% theo Mã màn hình (Spec ID): `tests/ui/[mã_màn].ui.spec.js`, `tests/api/[mã_màn].api.spec.js`, `tests/e2e/[mã_màn].e2e.spec.js`, `src/pages/[MÃ_MÀN]Page.js` (riêng login page chỉ để mỗi mã màn `[MÃ_MÀN]Page.js`, nếu để cả tên màn thì theo format `[ID]_[Admin/Agency]_[Tên_màn]Page.js`), `src/api/[MÃ_MÀN]API.js`, `src/test-data/[mã_màn]Data.js`. Tuyệt đối không thêm tiền tố số thứ tự (`01.`, `05.`); Báo cáo bàn giao tại `automation/[Mã_màn_hình]_readme.md`
  - **Q&A Spec:** `Q&A/[Mã_màn_hình]_Q&A.md`
  - **Kiểm tra CSDL & Đối soát:** File log truy vấn CSDL lưu tại `logs/db/` hoặc đính kèm trực tiếp vào mục Evidence của `testcase_ui/` / `bugs/`

---

## 5. Cấu hình & Định danh Dự án

- **Environment & Spec:** Đọc và đối chiếu từ [TEST_CONFIG.md](TEST_CONFIG.md) ở thư mục gốc.
- **Tester ID:** Theo cấu hình tại `TEST_CONFIG.md` (mặc định) hoặc do User chỉ định.
