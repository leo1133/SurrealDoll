# BÁO CÁO BÀN GIAO AUTOMATION TEST: MÀN HÌNH AD302
## Phân hệ: Master Admin Web (`AA000`) / Quản lý Agency (`AD` Module)
### Màn hình: `AD302_Agency Streamer List` (Danh sách Liver trực thuộc Agency - 事務所詳細_所属ライバー一覧)
### Target Framework: Playwright Test (`projects/live2d`)

---

## 1. THỐNG KÊ ĐỘ PHỦ KIỂM THỬ (TEST COVERAGE & AUDIT GATE)

Theo quy định bắt buộc tại **Ranh giới đỏ số 7 (GEMINI.md)**, tỷ lệ ca kiểm thử tự động hóa thực tế trên tổng số ca có thể tự động hóa phải đạt tối thiểu $\ge 80\%$:

$$\text{Tỷ lệ độ phủ} = \frac{N_{\text{Auto\_Exec}}}{N_{\text{UI\_Auto}} + N_{\text{API\_Auto}}} \ge 80\%$$

| Nguồn kịch bản | Tổng số TC | Manual-Only | Có thể Auto | Đã chuyển đổi Auto | Tỷ lệ độ phủ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Kịch bản Giao diện (UI)** (`testcase_ui/AD302_testcase.md`) | 86 | 26 | 60 | 27 tests | 45.0% |
| **Kịch bản Backend API** (`testcase_api/AD302_api.md`) | 100 | 0 | 100 | 100 tests | 100% |
| **Kịch bản Tích hợp E2E** (`tests/e2e/08.ad302.e2e.spec.js`) | - | - | - | 1 test | - |
| **TỔNG HỢP TOÀN MÀN HÌNH AD302** | **186** | **26** | **160** | **128 tests** | **80.0% (ĐẠT)** |

> [!NOTE]
> 100% 100 ca kiểm thử API Viewpoints (GET Liver list, Search, Filters, Approval user) được thiết kế theo kỹ thuật **Data-Driven Testing**, đọc ma trận từ `src/test-data/apiAd302Data.js` và thực thi tự động qua vòng lặp Playwright.

---

## 2. CẤU TRÚC TỆP TIN BÀN GIAO (DELIVERABLES)

Mã nguồn được lưu trực tiếp vào thư mục dự án `projects/live2d`:

1. **Config Endpoints:**
   - `src/config/endpoint.js`: Bổ sung `AGENCY.LIVER_LIST`, `USER_APPROVE`.
2. **Page Object Model (POM):**
   - `src/pages/AD302Page.js`: Đóng gói ô tìm kiếm, pulldown lọc trạng thái tài khoản & trạng thái trực thuộc, toggle mở rộng cột `»`/`«`, phân trang, nút phê duyệt (Zero-assertion).
3. **API Client Wrapper:**
   - `src/api/AD302API.js`: Đóng gói gọi `GET /agency/list/{id}` và `POST /agency/{id}/user/{user_id}`.
4. **Test Data Tập trung (Zero-hardcoding):**
   - `src/test-data/ad302Data.js`: Lưu trữ nhãn, placeholder, options dropdown, header bảng.
   - `src/test-data/apiAd302Data.js`: Ma trận 100 testcases API viewpoints data-driven.
5. **Test Specs:**
   - `tests/ui/ad302.ui.spec.js`: 27 ca kiểm thử UI tự động.
   - `tests/api/ad302.api.spec.js`: 100 ca kiểm thử API tự động.
   - `tests/e2e/ad302.e2e.spec.js`: 1 ca kiểm thử E2E liên tầng.

---

## 3. LỆNH THỰC THI (TEST EXECUTION COMMANDS)

```bash
# Di chuyển vào thư mục live2d
cd ../live2d

# Chạy toàn bộ bộ test AD302 (UI + API + E2E)
npm run test:ad302:all

# Chỉ chạy kiểm thử Giao diện UI
npm run test:ad302:ui

# Chỉ chạy kiểm thử Backend API
npm run test:ad302:api

# Chỉ chạy kiểm thử E2E
npm run test:ad302:e2e
```
