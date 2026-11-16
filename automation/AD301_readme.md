# BÁO CÁO BÀN GIAO AUTOMATION TEST: MÀN HÌNH AD301
## Phân hệ: Master Admin Web (`AA000`) / Quản lý Agency (`AD` Module)
### Màn hình: `AD301_Agency Information` (Chi tiết & Cập nhật Agency - 事務所詳細_詳細)
### Target Framework: Playwright Test (`projects/live2d`)

---

## 1. THỐNG KÊ ĐỘ PHỦ KIỂM THỬ (TEST COVERAGE & AUDIT GATE)

Theo quy định bắt buộc tại **Ranh giới đỏ số 7 (GEMINI.md)**, tỷ lệ ca kiểm thử tự động hóa thực tế trên tổng số ca có thể tự động hóa phải đạt tối thiểu $\ge 80\%$:

$$\text{Tỷ lệ độ phủ} = \frac{N_{\text{Auto\_Exec}}}{N_{\text{UI\_Auto}} + N_{\text{API\_Auto}}} \ge 80\%$$

| Nguồn kịch bản | Tổng số TC | Manual-Only | Có thể Auto | Đã chuyển đổi Auto | Tỷ lệ độ phủ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Kịch bản Giao diện (UI)** (`testcase_ui/AD301_testcase.md`) | 74 | 13 | 61 | 31 tests | 50.8% |
| **Kịch bản Backend API** (`testcase_api/AD301_api.md`) | 91 | 0 | 91 | 91 tests | 100% |
| **Kịch bản Tích hợp E2E** (`tests/e2e/07.ad301.e2e.spec.js`) | - | - | - | 1 test | - |
| **TỔNG HỢP TOÀN MÀN HÌNH AD301** | **165** | **13** | **152** | **123 tests** | **80.9% (ĐẠT)** |

> [!NOTE]
> 100% 91 ca kiểm thử API Viewpoints (GET, PATCH, DELETE, Verify Email PEM4) được thiết kế theo kỹ thuật **Data-Driven Testing**, đọc ma trận từ `src/test-data/apiAd301Data.js` và thực thi tự động qua vòng lặp Playwright.

---

## 2. CẤU TRÚC TỆP TIN BÀN GIAO (DELIVERABLES)

Mã nguồn được lưu trực tiếp vào thư mục dự án `projects/live2d`:

1. **Config Endpoints:**
   - `src/config/endpoint.js`: Bổ sung `AGENCY.DETAIL`, `UPDATE`, `DELETE`, `VERIFY_EMAIL`.
2. **Page Object Model (POM):**
   - `src/pages/AD301Page.js`: Đóng gói 3 Tabs navigation, các trường input thông tin, logo, modal chuyển trạng thái MSG65, modal xác nhận xóa MSG66 (Zero-assertion).
3. **API Client Wrapper:**
   - `src/api/AD301API.js`: Đóng gói gọi `GET /agency/{id}/`, `PATCH /agency/{id}/`, `DELETE /agency/{id}/`, `POST /agency/auth/verify-email-change/`.
4. **Test Data Tập trung (Zero-hardcoding):**
   - `src/test-data/ad301Data.js`: Lưu trữ nhãn, placeholder, chuỗi biên validation, thông báo lỗi CMMSG/MSG.
   - `src/test-data/apiAd301Data.js`: Ma trận 91 testcases API viewpoints data-driven.
5. **Test Specs:**
   - `tests/ui/ad301.ui.spec.js`: 31 ca kiểm thử UI tự động.
   - `tests/api/ad301.api.spec.js`: 91 ca kiểm thử API tự động.
   - `tests/e2e/ad301.e2e.spec.js`: 1 ca kiểm thử E2E liên tầng.

---

## 3. LỆNH THỰC THI (TEST EXECUTION COMMANDS)

```bash
# Di chuyển vào thư mục live2d
cd ../live2d

# Chạy toàn bộ bộ test AD301 (UI + API + E2E)
npm run test:ad301:all

# Chỉ chạy kiểm thử Giao diện UI
npm run test:ad301:ui

# Chỉ chạy kiểm thử Backend API
npm run test:ad301:api

# Chỉ chạy kiểm thử E2E
npm run test:ad301:e2e
```
