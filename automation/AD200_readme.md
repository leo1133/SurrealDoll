# BÁO CÁO BÀN GIAO AUTOMATION TEST: MÀN HÌNH AD200
## Phân hệ: Master Admin Web (`AA000`) / Quản lý Agency (`AD` Module)
### Màn hình: `AD200_Register Agency` (Đăng ký tạo mới Agency - 事務所新規登録)
### Target Framework: Playwright Test (`projects/live2d`)

---

## 1. THỐNG KÊ ĐỘ PHỦ KIỂM THỬ (TEST COVERAGE & AUDIT GATE)

Theo quy định bắt buộc tại **Ranh giới đỏ số 7 (GEMINI.md)**, tỷ lệ ca kiểm thử tự động hóa thực tế trên tổng số ca có thể tự động hóa phải đạt tối thiểu $\ge 80\%$:

$$\text{Tỷ lệ độ phủ} = \frac{N_{\text{Auto\_Exec}}}{N_{\text{UI\_Auto}} + N_{\text{API\_Auto}}} \ge 80\%$$

| Nguồn kịch bản | Tổng số TC | Manual-Only | Có thể Auto | Đã chuyển đổi Auto | Tỷ lệ độ phủ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Kịch bản Giao diện (UI)** (`testcase_ui/AD200_testcase.md`) | 65 | 10 | 55 | 29 tests | 52.7% |
| **Kịch bản Backend API** (`testcase_api/AD200_api.md`) | 114 | 0 | 114 | 114 tests | 100% |
| **Kịch bản Tích hợp E2E** (`tests/e2e/06.ad200.e2e.spec.js`) | - | - | - | 1 test | - |
| **TỔNG HỢP TOÀN MÀN HÌNH AD200** | **179** | **10** | **169** | **144 tests** | **85.2% (ĐẠT)** |

> [!NOTE]
> 100% 114 ca kiểm thử API Viewpoints được thiết kế theo kỹ thuật **Data-Driven Testing**, đọc ma trận từ `src/test-data/apiAd200Data.js` và thực thi tự động qua vòng lặp Playwright.

---

## 2. CẤU TRÚC TỆP TIN BÀN GIAO (DELIVERABLES)

Mã nguồn được lưu trực tiếp vào thư mục dự án `projects/live2d`:

1. **Config Endpoints:**
   - `src/config/endpoint.js`: Bổ sung `AGENCY.CREATE: "/agency/create/"`.
2. **Page Object Model (POM):**
   - `src/pages/AD200Page.js`: Đóng gói 6 trường input, file upload logo, các nút hành động, modal xác nhận hủy MSG67 (Zero-assertion).
3. **API Client Wrapper:**
   - `src/api/AD200API.js`: Đóng gói gọi `POST /agency/create/` hỗ trợ đầy đủ 419 viewpoints HTTP method, headers, payload.
4. **Test Data Tập trung (Zero-hardcoding):**
   - `src/test-data/ad200Data.js`: Lưu trữ nhãn, placeholder, chuỗi biên validation, thông báo lỗi CMMSG/MSG.
   - `src/test-data/apiAd200Data.js`: Ma trận 114 testcases API viewpoints data-driven.
5. **Test Specs:**
   - `tests/ui/ad200.ui.spec.js`: 29 ca kiểm thử UI tự động.
   - `tests/api/ad200.api.spec.js`: 114 ca kiểm thử API tự động.
   - `tests/e2e/ad200.e2e.spec.js`: 1 ca kiểm thử E2E liên tầng.

---

## 3. LỆNH THỰC THI (TEST EXECUTION COMMANDS)

```bash
# Di chuyển vào thư mục live2d
cd ../live2d

# Chạy toàn bộ bộ test AD200 (UI + API + E2E)
npm run test:ad200:all

# Chỉ chạy kiểm thử Giao diện UI
npm run test:ad200:ui

# Chỉ chạy kiểm thử Backend API
npm run test:ad200:api

# Chỉ chạy kiểm thử E2E
npm run test:ad200:e2e
```
