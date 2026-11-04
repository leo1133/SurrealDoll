# TEST CASE: 9. DATE / TIME PICKER

- **Mô tả chức năng:** Bộ chọn ngày tháng, giờ hoặc khoảng thời gian (Date Range)
- **Tổng số Test Case:** **8** (`High: 7` | `Medium: 1` | `Low: 0`)
- **Phân bổ theo loại kiểm thử:** UI / Giao diện: **1**, Functional / Chức năng: **3**, Validation & Negative: **2**, Boundary / Giá trị biên: **2**

---

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_DTP_001`** [High] _UI / Giao diện_ — Kiểm tra giao diện ô Date/Time Picker và Popup Lịch khi mở
- [ ] **`TC_DTP_002`** [High] _Functional / Chức năng_ — Kiểm tra chọn ngày, chuyển đổi Tháng / Năm trên Popup Lịch và nút 'Hôm nay' / 'Xóa'
- [ ] **`TC_DTP_003`** [High] _Functional / Chức năng_ — Kiểm tra chọn Giờ / Phút trên Time Picker (Định dạng 24h hoặc 12h AM/PM)
- [ ] **`TC_DTP_004`** [High] _Functional / Chức năng_ — Kiểm tra chọn khoảng thời gian hợp lệ (Date Range: Từ ngày <= Đến ngày)
- [ ] **`TC_DTP_005`** [High] _Validation & Negative_ — Kiểm tra lỗi khi chọn 'Từ ngày' lớn hơn 'Đến ngày' (Start Date > End Date)
- [ ] **`TC_DTP_006`** [High] _Boundary / Giá trị biên_ — Kiểm tra ngày tháng năm nhuận (Leap Year 29/02) và số ngày cuối tháng (30 vs 31 ngày)
- [ ] **`TC_DTP_007`** [High] _Boundary / Giá trị biên_ — Kiểm tra giới hạn Min Date / Max Date theo nghiệp vụ (VD: Ngày sinh, Ngày đặt lịch hẹn)
- [ ] **`TC_DTP_008`** [Medium] _Validation & Negative_ — Kiểm tra nhập chữ cái, ký tự đặc biệt hoặc sai định dạng vào ô Date Picker

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_DTP_001` | UI / Giao diện | **High** | **Kiểm tra giao diện ô Date/Time Picker và Popup Lịch khi mở** | Màn hình chứa Date Picker / Time Picker đã tải xong. | 1. Quan sát ô nhập ngày/giờ và icon Lịch/Đồng hồ.<br>2. Click vào ô hoặc icon để mở Popup Lịch. | N/A | - Ô input hiển thị rõ định dạng gợi ý (VD: `DD/MM/YYYY` hoặc `DD/MM/YYYY HH:mm`).<br>- Popup lịch hiển thị đúng Tháng/Năm hiện tại, làm nổi bật (highlight) ngày hôm nay (Today), các thứ trong tuần (T2 -> CN) sắp xếp chính xác. | `Not Run` |
| `TC_DTP_002` | Functional / Chức năng | **High** | **Kiểm tra chọn ngày, chuyển đổi Tháng / Năm trên Popup Lịch và nút 'Hôm nay' / 'Xóa'** | Popup Date Picker đang mở. | 1. Click nút mũi tên `<` (Tháng trước), `>` (Tháng sau) và chọn nhanh Năm.<br>2. Click chọn một ngày bất kỳ trên lịch (VD: ngày 15).<br>3. Mở lại lịch, nhấn nút 'Hôm nay' (Today) và nút 'Xóa' (Clear). | Chọn ngày: 15/10/2026 | - Khi chọn ngày: Popup lịch đóng lại, ô input hiển thị đúng chuỗi `15/10/2026` theo định dạng quy định.<br>- Nút 'Hôm nay' chọn nhanh đúng ngày hệ thống hiện tại.<br>- Nút 'Xóa' làm trống giá trị trong ô input. | `Not Run` |
| `TC_DTP_003` | Functional / Chức năng | **High** | **Kiểm tra chọn Giờ / Phút trên Time Picker (Định dạng 24h hoặc 12h AM/PM)** | Trường nhập có bộ chọn giờ (Time Picker). | 1. Mở Time Picker.<br>2. Chọn Giờ = `00`, Phút = `00` (Đầu ngày) và Giờ = `23`, Phút = `59` (Cuối ngày).<br>3. Nếu là định dạng 12h: Kiểm tra chuyển đổi giữa `AM` và `PM`. | - `00:00`<br>- `23:59`<br>- `12:30 PM` | - Hiển thị và lưu chính xác giờ/phút đã chọn, không bị lệch múi giờ (Timezone UTC vs Local Time) khi lưu lên Server và hiển thị lại. | `Not Run` |
| `TC_DTP_004` | Functional / Chức năng | **High** | **Kiểm tra chọn khoảng thời gian hợp lệ (Date Range: Từ ngày <= Đến ngày)** | Màn hình có bộ chọn khoảng thời gian 'Từ ngày' (Start Date) - 'Đến ngày' (End Date). | 1. Chọn 'Từ ngày' = `01/10/2026` và 'Đến ngày' = `10/10/2026`.<br>2. Chọn 'Từ ngày' = `10/10/2026` và 'Đến ngày' = `10/10/2026` (Cùng 1 ngày). | - Range 1: `01/10/2026` - `10/10/2026`<br>- Range 2: `10/10/2026` - `10/10/2026` | - Cả hai trường hợp đều hợp lệ.<br>- Trên lịch hiển thị vùng màu nối giữa ngày bắt đầu và ngày kết thúc.<br>- Khi chọn cùng 1 ngày, hệ thống vẫn lấy đủ dữ liệu trong ngày đó (từ `00:00:00` đến `23:59:59`). | `Not Run` |
| `TC_DTP_005` | Validation & Negative | **High** | **Kiểm tra lỗi khi chọn 'Từ ngày' lớn hơn 'Đến ngày' (Start Date > End Date)** | Bộ chọn Date Range. | 1. Chọn 'Từ ngày' = `20/10/2026`.<br>2. Thử chọn hoặc nhập 'Đến ngày' = `10/10/2026` (nhỏ hơn Từ ngày).<br>3. Nếu có thêm Giờ: Chọn cùng ngày `10/10/2026` nhưng 'Giờ bắt đầu' = `15:00` và 'Giờ kết thúc' = `14:00`. | Từ ngày: `20/10/2026` > Đến ngày: `10/10/2026` | - Trên Popup lịch: Các ngày nhỏ hơn `20/10/2026` ở ô 'Đến ngày' bị làm mờ (Disabled) không cho chọn.<br>- Nếu cho phép nhập tay: Hiển thị thông báo lỗi "Ngày/Giờ kết thúc phải lớn hơn hoặc bằng Ngày/Giờ bắt đầu". | `Not Run` |
| `TC_DTP_006` | Boundary / Giá trị biên | **High** | **Kiểm tra ngày tháng năm nhuận (Leap Year 29/02) và số ngày cuối tháng (30 vs 31 ngày)** | Ô Date Picker cho phép gõ trực tiếp từ bàn phím hoặc chọn trên lịch. | 1. Nhập ngày `29/02/2024` hoặc `29/02/2028` (Năm nhuận).<br>2. Nhập ngày `29/02/2025` hoặc `29/02/2026` (Năm không nhuận).<br>3. Nhập các ngày không tồn tại: `30/02/2026`, `31/04/2026`, `31/06/2026`, `31/09/2026`, `31/11/2026`. | - Hợp lệ: `29/02/2024`<br>- Không hợp lệ: `29/02/2026`, `31/04/2026` | - Ngày `29/02/2024`: Hệ thống chấp nhận hợp lệ.<br>- Ngày `29/02/2026` và các ngày `31` của tháng 4, 6, 9, 11: Hệ thống báo lỗi "Ngày tháng không hợp lệ" (tuyệt đối không tự động nhảy sang ngày 01 hoặc 02 của tháng tiếp theo mà không báo cho người dùng). | `Not Run` |
| `TC_DTP_007` | Boundary / Giá trị biên | **High** | **Kiểm tra giới hạn Min Date / Max Date theo nghiệp vụ (VD: Ngày sinh, Ngày đặt lịch hẹn)** | - TH1: Trường 'Ngày sinh' (không được lớn hơn ngày hiện tại).<br>- TH2: Trường 'Ngày đặt lịch hẹn' (không được chọn ngày trong quá khứ). | 1. Ở trường 'Ngày sinh', thử chọn ngày ngày mai hoặc năm 1800.<br>2. Ở trường 'Ngày đặt lịch', thử chọn ngày hôm qua. | - Ngày tương lai cho Ngày sinh<br>- Ngày quá khứ cho Ngày hẹn | - Các ngày nằm ngoài phạm vi `[Min Date, Max Date]` bị disable trên lịch.<br>- Nếu nhập bằng bàn phím sẽ báo lỗi vượt quá giới hạn cho phép. | `Not Run` |
| `TC_DTP_008` | Validation & Negative | **Medium** | **Kiểm tra nhập chữ cái, ký tự đặc biệt hoặc sai định dạng vào ô Date Picker** | Ô Date Picker cho phép gõ văn bản. | 1. Nhập chuỗi chữ "abcdef", "99/99/9999" hoặc định dạng ngược "2026-30-12" vào ô ngày tháng.<br>2. Blur ra ngoài hoặc nhấn Submit. | "abcdef", "99/99/9999" | - Chặn nhập chữ cái (Input Mask) hoặc hiển thị thông báo lỗi "Định dạng ngày không hợp lệ (DD/MM/YYYY)". | `Not Run` |
