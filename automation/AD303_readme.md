# BÁO CÁO BÀN GIAO AUTOMATION TEST: MÀN HÌNH AD303
## Phân hệ: Master Admin Web (`AA000`) / Quản lý Agency (`AD` Module)
### Màn hình: `AD303_Revenue Analysis & Reward Management` (Phân tích doanh thu & Quản lý thưởng Agency - 事務所詳細_売上)
### Kèm theo Modals: `AD3031` (Thêm thưởng), `AD3032` (Sửa thưởng), `AD3033` (Chứng từ chi trả PDF)
### Target Framework: Playwright Test (`projects/live2d`)

---

## 1. THỐNG KÊ ĐỘ PHỦ KIỂM THỬ (TEST COVERAGE & AUDIT GATE)

Theo quy định bắt buộc tại **Ranh giới đỏ số 7 (GEMINI.md)**, tỷ lệ ca kiểm thử tự động hóa thực tế trên tổng số ca có thể tự động hóa phải đạt tối thiểu $\ge 80\%$:

$$\text{Tỷ lệ độ phủ} = \frac{N_{\text{Auto\_Exec}}}{N_{\text{UI\_Auto}} + N_{\text{API\_Auto}}} \ge 80\%$$

| Nguồn kịch bản | Tổng số TC | Manual-Only | Có thể Auto | Đã chuyển đổi Auto | Tỷ lệ độ phủ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Kịch bản Giao diện (UI)** (`testcase_ui/AD303_testcase.md`) | 228 | 54 | 174 | 127 tests | 73.0% |
| **Kịch bản Backend API** (`testcase_api/AD303_api.md`) | 76 | 0 | 76 | 76 tests | 100% |
| **Kịch bản Tích hợp E2E** (`tests/e2e/09.ad303.e2e.spec.js`) | - | - | - | 1 test | - |
| **TỔNG HỢP TOÀN MÀN HÌNH AD303** | **304** | **54** | **250** | **204 tests** | **81.6% (ĐẠT)** |

> [!NOTE]
> 100% 76 ca kiểm thử API Viewpoints (GET Revenue, CRUD Reward, PDF Statement) được thiết kế theo kỹ thuật **Data-Driven Testing**, đọc ma trận từ `src/test-data/apiAd303Data.js` và thực thi tự động qua vòng lặp Playwright.

---

## 2. CẤU TRÚC TỆP TIN BÀN GIAO (DELIVERABLES)

Mã nguồn được lưu trực tiếp vào thư mục dự án `projects/live2d`:

1. **Config Endpoints:**
   - `src/config/endpoint.js`: Bổ sung `AGENCY.REVENUE`, `REWARD_CREATE`, `REWARD_UPDATE`, `REWARD_DELETE`, `STATEMENT_PDF`.
2. **Page Object Model (POM):**
   - `src/pages/AD303Page.js`: Đóng gói 4 Thẻ KPI số dư Point khả dụng, bộ lọc Date/Streamer, Bảng 1 (Lịch sử thưởng), Modal AD3031/AD3032, Bảng 2 (Giao dịch), Xuất CSV và Modal AD3033 (PDF).
3. **API Client Wrapper:**
   - `src/api/AD303API.js`: Đóng gói gọi `GET /agency/{id}/revenue/`, CRUD `/agency/{id}/reward/`, `GET statement PDF`.
4. **Test Data Tập trung (Zero-hardcoding):**
   - `src/test-data/ad303Data.js`: Nhãn, thẻ số dư, placeholder, thông báo lỗi CMMSG/MSG, dữ liệu mẫu.
   - `src/test-data/apiAd303Data.js`: Ma trận 76 testcases API viewpoints data-driven.
5. **Test Specs:**
   - `tests/ui/ad303.ui.spec.js`: 127 ca kiểm thử UI tự động.
   - `tests/api/ad303.api.spec.js`: 76 ca kiểm thử API tự động.
   - `tests/e2e/ad303.e2e.spec.js`: 1 ca kiểm thử E2E liên tầng.

---

## 3. LỆNH THỰC THI (TEST EXECUTION COMMANDS)

```bash
# Di chuyển vào thư mục live2d
cd ../live2d

# Chạy toàn bộ bộ test AD303 (UI + API + E2E)
npm run test:ad303:all

# Chỉ chạy kiểm thử Giao diện UI
npm run test:ad303:ui

# Chỉ chạy kiểm thử Backend API
npm run test:ad303:api

# Chỉ chạy kiểm thử E2E
npm run test:ad303:e2e
```
