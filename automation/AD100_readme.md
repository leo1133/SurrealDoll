# TÀI LIỆU HƯỚNG DẪN & THEO DÕI KIỂM THỬ TỰ ĐỘNG HÓA (AUTOMATION HANDOVER & TRACEABILITY REPORT)
## Màn hình: AD100_Agency List / Search (事務所一覧・検索)
### Phân hệ: Master Admin Web Portal (`AA000`) / Quản lý Agency (`AD` Module)
### Target Repository: `../live2d` (`/Users/ngaphuong/projects/live2d`)
### Áp dụng: Quy chuẩn Trụ cột 5 (`Universal_Rules/05_automation_test_rule.md`) & Framework Playwright (JavaScript ES Module)

---

## 1. THÔNG TIN TỔNG QUAN HỆ THỐNG KIỂM THỬ TỰ ĐỘNG (AUTOMATION METADATA)

| Thuộc tính | Chi tiết |
| :--- | :--- |
| **Mã màn hình** | `AD100` |
| **Tên màn hình** | `AD100 Agency Manage - Agency List & Search` (事務所一覧・検索) |
| **Target Project Path** | `/Users/ngaphuong/projects/live2d` (đường dẫn tương đối: `../live2d`) |
| **Framework kiểm thử** | [Playwright Test](https://playwright.dev/) v1.63+ (Ngôn ngữ: JavaScript ES Module `"type": "module"`) |
| **Kiến trúc mã nguồn** | Page Object Model (POM) + Resilient Locators + Custom Resilient API Client |
| **Cơ chế xác thực** | Session Caching qua `storageState` (`tests/auth/admin.setup.js`) & `api_token_dev.json` |
| **Môi trường cấu hình** | `Dev-Admin` / `STG-Admin` (Tham số hóa 100% qua `../live2d/.env.dev` & `TEST_CONFIG.md`) |
| **Nguồn Test Case Manual** | [AD100_testcase.md](file:///Users/ngaphuong/projects/SurrealDoll/testcase_ui/AD100_testcase.md) (78 TCs Manual UI) |
| **Nguồn Test Case API** | [AD100_api.md](file:///Users/ngaphuong/projects/SurrealDoll/testcase_api/AD100_api.md) (178 TCs Backend API) |

---

## 2. BẢNG TRUY XUẤT NGUỒN GỐC (TRACEABILITY MATRIX: MANUAL $\rightarrow$ AUTOMATION)

### 2.1. Danh mục Kịch bản Đã Tự Động Hóa (Automated Test Cases):

| Target Test Spec (in `../live2d`) | Manual TC ID | Tên Kịch Bản Kiểm Thử Tự Động (Spec Name) | Loại Kiểm Thử | Trạng Thái |
| :--- | :---: | :--- | :---: | :---: |
| `tests/ui/04.agency.ui.spec.js` | `[AD100-1]`, `[AD100-2]`, `[AD100-3]` | `TC1 - Xác minh điều hướng thành công vào màn hình Quản lý Agency (AD100)` | UI / Navigation | **Automated** |
| `tests/ui/04.agency.ui.spec.js` | `[AD100-8]`, `[AD100-9]` | `TC2 - Kiểm tra hiển thị thanh Breadcrumb và click breadcrumb` | UI / Breadcrumb | **Automated** |
| `tests/ui/04.agency.ui.spec.js` | `[AD100-4]` | `TC3 - Kiểm tra truy cập màn hình qua Inbound Deep-link với query params` | UI / Deep-link | **Automated** |
| `tests/ui/04.agency.ui.spec.js` | `[AD100-10]` | `TC4 - Kiểm tra placeholder ô tìm kiếm hiển thị đúng spec` | UI / Label | **Automated** |
| `tests/ui/04.agency.ui.spec.js` | `[AD100-11]`, `[AD100-12]`, `[AD100-14]` | `TC5 - Kiểm tra nhập liệu từ khóa có khoảng trắng đầu cuối (Auto-trim space)` | UI / Input | **Automated** |
| `tests/ui/04.agency.ui.spec.js` | `[AD100-17]` | `TC6 - Kiểm tra kích hoạt tìm kiếm bằng phím Enter` | UI / Action | **Automated** |
| `tests/ui/04.agency.ui.spec.js` | `[AD100-19]`, `[AD100-20]` | `TC7 - Kiểm tra tìm kiếm khớp 1 phần tên và khớp chính xác mã Agency ID` | UI / Search | **Automated** |
| `tests/ui/04.agency.ui.spec.js` | `[AD100-22]`, `[AD100-24]`, `[AD100-25]` | `TC8 - Kiểm tra lọc trạng thái theo Active (利用中) và Inactive (停止中)` | UI / Dropdown | **Automated** |
| `tests/ui/04.agency.ui.spec.js` | `[AD100-32]` | `TC9 - Kiểm tra nút クリア reset từ khóa và dropdown về mặc định` | UI / Reset | **Automated** |
| `tests/ui/04.agency.ui.spec.js` | `[AD100-33]`, `[AD100-34]` | `TC10 - Kiểm tra nút 新規登録 điều hướng sang màn hình AD200` | UI / Navigation | **Automated** |
| `tests/ui/04.agency.ui.spec.js` | `[AD100-35]` $\rightarrow$ `[AD100-46]` | `TC11 - Kiểm tra hiển thị đầy đủ các tiêu đề cột của bảng` | UI / Header | **Automated** |
| `tests/ui/04.agency.ui.spec.js` | `[AD100-47]`, `[AD100-48]` | `TC12 - Kiểm tra tính năng sắp xếp theo 作成日 và 変更日` | UI / Sort | **Automated** |
| `tests/ui/04.agency.ui.spec.js` | `[AD100-58]` | `TC13 - Xác minh KHÔNG CÓ nút Xóa trên bảng AD100 theo CR 13/08/2026` | UI / Security | **Automated** |
| `tests/ui/04.agency.ui.spec.js` | `[AD100-51]`, `[AD100-52]` | `TC14 - Click ライバー数 điều hướng sang màn hình AD302 (CR 06/11/2025)` | UI / Deep-link | **Automated** |
| `tests/ui/04.agency.ui.spec.js` | `[AD100-57]` | `TC15 - Click nút Chi tiết điều hướng sang màn hình AD301` | UI / Action | **Automated** |
| `tests/ui/04.agency.ui.spec.js` | `[AD100-59]`, `[AD100-60]` | `TC16 - Kiểm tra giới hạn 10 bản ghi/trang theo chuẩn CMR01` | UI / Pagination | **Automated** |
| `tests/ui/04.agency.ui.spec.js` | `[AD100-5]`, `[AD100-71]` | `TC17 - Kiểm tra hiển thị Empty State chuẩn CMMSG47 khi không có kết quả` | UI / Feedback | **Automated** |
| `tests/api/04.agency.api.spec.js` | `[AD100-API-28]` | `Khối 1: Lấy danh sách Agency thành công (200 OK) và kiểm tra Schema JSON` | API / Schema | **Automated** |
| `tests/api/04.agency.api.spec.js` | `[AD100-API-16]` | `Khối 2: Gọi phương thức GET/DELETE vào endpoint chỉ nhận POST trả về 405` | API / Method | **Automated** |
| `tests/api/04.agency.api.spec.js` | `[AD100-API-01]`, `[AD100-API-11]` | `Khối 3: Request không kèm token hoặc token giả mạo trả về 401 Unauthorized` | API / Security | **Automated** |
| `tests/api/04.agency.api.spec.js` | `[AD100-API-31]`, `[AD100-API-32]` | `Khối 4: Lọc danh sách Agency theo trạng thái (status = 1 vs status = 2)` | API / Filter | **Automated** |
| `tests/api/04.agency.api.spec.js` | `[AD100-API-18]`, `[AD100-API-19]` | `Khối 4: Tìm kiếm từ khóa theo tên Agency và từ khóa không tồn tại` | API / Filter | **Automated** |
| `tests/api/04.agency.api.spec.js` | `[AD100-API-50]`, `[AD100-API-53]` | `Khối 4: Phân trang danh sách với các hạn mức (10, 20, 50)` | API / Limit | **Automated** |
| `tests/api/04.agency.api.spec.js` | `[AD100-API-75]`, `[AD100-API-76]` | `Khối 5: Kiểm tra thuật toán tổng doanh thu (total_sales = point + familia)` | API / Logic | **Automated** |
| `tests/api/04.agency.api.spec.js` | `[AD100-API-55]`, `[AD100-API-56]` | `Khối 6: Từ chối giá trị items_per_page không hợp lệ (0 hoặc vượt max 100)` | API / Validation | **Automated** |
| `tests/api/04.agency.api.spec.js` | `[AD100-API-29]`, `[AD100-API-30]` | `Khối 6: Escape an toàn payload SQL Injection và XSS trong ô tìm kiếm` | API / Security | **Automated** |
| `tests/e2e/04.agency.e2e.spec.js` | `[AD100-E2E-01]` | `TC_E2E_01: Kiểm tra tính đồng bộ dữ liệu giữa Backend API POST /agency/ và UI` | E2E / Multi-tier | **Automated** |
| `tests/e2e/04.agency.e2e.spec.js` | `[AD100-E2E-02]` | `TC_E2E_02: Thao tác tìm kiếm trên UI kích hoạt API tương ứng và cập nhật bảng` | E2E / Multi-tier | **Automated** |

---

### 2.2. Danh mục Chỉ Kiểm Thử Thủ Công (Manual Only):

| Manual TC ID | Tên Ca Kiểm Thử | Lý Do Không Tự Động Hóa (Rationale) |
| :---: | :--- | :--- |
| `[AD100-72]` | Xử lý khi ngắt kết nối mạng Internet vật lý | Yêu cầu ngắt card mạng vật lý của máy client, gây gián đoạn runner kiểm thử CI/CD. Đã có mock test lỗi ở tầng API. |
| `[AD100-75]` | Kiểm tra hiển thị giao diện Responsive trên màn hình vật lý nhỏ | Kiểm tra thẩm mỹ mắt người (Visual UX) trên các kích thước màn hình dị biệt; nên dùng Visual Regression Test riêng nếu cần. |
| `[AD100-76]` | Hover hiệu ứng đổi màu dòng bảng | Hiệu ứng CSS hover vi mô không ảnh hưởng đến luồng nghiệp vụ chức năng. |
| `[AD100-77]` | Kiểm tra text dài tên Agency cắt gọn '…' và hiển thị tooltip | Kiểm tra hiển thị font chữ và tooltip native của trình duyệt. |

---

## 3. CẤU TRÚC MÃ NGUỒN TẠI TARGET REPOSITORY (`../live2d`)

```
/Users/ngaphuong/projects/live2d/
├── package.json                     # Đã cập nhật các npm scripts cho Agency
├── playwright.config.js             # Cấu hình đa project (setup, Admin UI Tests, API Tests)
├── .env.dev                         # Biến môi trường Dev (URLs, Credentials, Basic Auth)
├── src/
│   ├── config/
│   │   └── endpoint.js              # Đã bổ sung ENDPOINTS.AGENCY (GET_LIST, CREATE, DETAIL...)
│   ├── test-data/
│   │   ├── index.js                 # Export tập trung các bộ dữ liệu
│   │   ├── agencyData.js            # Dữ liệu UI (Labels, Placeholders, Options, Headers)
│   │   └── apiAgencyData.js         # Dữ liệu API (Default params, Schema, Error messages)
│   ├── pages/
│   │   └── AgencyPage.js            # POM cho màn hình AD100 (Locators & Actions only)
│   └── api/
│       └── AgencyAPI.js             # API Service Wrapper cho POST /agency/
└── tests/
    ├── ui/
    │   └── 04.agency.ui.spec.js     # 17 Kịch bản UI Test AD100 (Serial execution)
    ├── api/
    │   └── 04.agency.api.spec.js    # 10 Kịch bản API Test tổ chức theo 6 Khối Chuẩn Mực
    └── e2e/
        └── 04.agency.e2e.spec.js    # 2 Kịch bản E2E kiểm tra tính toàn vẹn 3 chiều (UI <-> API)
```

---

## 4. HƯỚNG DẪN THỰC THI KIỂM THỬ (QUICK RUN GUIDE)

Thực hiện tại thư mục dự án target `../live2d`:

```bash
cd /Users/ngaphuong/projects/live2d

# 1. Chạy toàn bộ kịch bản Giao diện UI AD100:
npm run test:agency:ui

# 2. Chạy toàn bộ kịch bản Backend API (POST /agency/):
npm run test:agency:api

# 3. Chạy kịch bản E2E đối chiếu 3 chiều (UI <-> API):
npm run test:agency:e2e

# 4. Chạy toàn bộ test suites AD100:
npm run test:agency:all

# 5. Chạy ở chế độ giao diện đồ họa Playwright UI Mode:
npm run test:ui:dev

# 6. Mở báo cáo kết quả kiểm thử HTML Report:
npm run report
```

---

## 5. BẢNG RÀ SOÁT 7 TIÊU CHÍ KIỂM DUYỆT CỦA AI (PRE-FLIGHT GATEKEEPER)

| STT | Tiêu chí kiểm duyệt | Hiện trạng kiểm tra trong toàn bộ mã nguồn `../live2d` | Đánh giá |
| :---: | :--- | :--- | :---: |
| **1** | **URL & Account** | Tuyệt đối không xuất hiện literal `'https://...'` hay password gán cứng trong `pages/` hoặc `tests/`. Toàn bộ nạp qua `process.env.*` và `ENDPOINTS.*`. | **ĐẠT (PASS)** |
| **2** | **Target IDs** | Sử dụng tham số động từ API hoặc `agencyData.searchTestData`. | **ĐẠT (PASS)** |
| **3** | **Magic Values & Enum** | Sử dụng Enum `HTTP_STATUS_CODE.OK`, `HTTP_STATUS_CODE.BAD_REQUEST`, `METHODS.POST`. | **ĐẠT (PASS)** |
| **4** | **Thông báo lỗi & Nhãn UI** | Toàn bộ chuỗi hiển thị được ánh xạ từ `agencyData.labels.*`, `agencyData.tableHeaders.*`. | **ĐẠT (PASS)** |
| **5** | **Thời gian & Ngày tháng** | Sử dụng helper động từ `helpers.js`, không điền chuỗi ngày cố định. | **ĐẠT (PASS)** |
| **6** | **Timeouts** | Thời gian chờ được tham chiếu chuẩn hóa qua config và timeout 15000ms. | **ĐẠT (PASS)** |
| **7** | **Asset Upload Path** | Không có upload file trên màn AD100. | **ĐẠT (PASS)** |
