# TEST CASES: 2. COLOR PICKER

- **Mục đích:** Bộ chọn màu sắc (chọn trên bảng phổ màu, nhập mã HEX/RGB, chỉnh thanh trượt độ mờ Opacity)
- **Tổng số Test Case:** **6** (`High`: 3 | `Medium`: 2 | `Low`: 1)

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_CLR_001`** (High): Kiểm tra giao diện hiển thị của ô xem trước màu (Color Swatch) và Popup bảng chọn màu
- [ ] **`TC_CLR_002`** (High): Kiểm tra chọn màu trực tiếp trên vùng phổ màu, thanh Hue và danh sách màu gợi ý sẵn (Presets)
- [ ] **`TC_CLR_003`** (High): Kiểm tra nhập trực tiếp mã màu thủ công ở các định dạng HEX (`#RRGGBB`, `#RGB`) và RGB (`R, G, B`)
- [ ] **`TC_CLR_004`** (Medium): Kiểm tra điều chỉnh thanh trượt độ mờ (Opacity / Alpha Slider: `0% -> 100%`)
- [ ] **`TC_CLR_005`** (Medium): Kiểm tra xử lý khi nhập mã HEX sai quy chuẩn hoặc giá trị RGB vượt ngoài khoảng `0 - 255`
- [ ] **`TC_CLR_006`** (Low): Kiểm tra công cụ bút chấm hút màu (`Eyedropper`) và lưu danh sách màu vừa dùng (`Recent Colors`)

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_CLR_001` | UI / Giao diện | **High** | **Kiểm tra giao diện hiển thị của ô xem trước màu (Color Swatch) và Popup bảng chọn màu** | Màn hình cấu hình giao diện/sản phẩm có trường chọn màu sắc (Color Picker). | 1. Quan sát ô hiển thị màu hiện tại (Color Swatch) và mã màu bên cạnh.<br>2. Click vào ô màu để mở Popup bảng chọn màu.<br>3. Quan sát vùng phổ màu 2D (Saturation/Brightness), thanh trượt tông màu (Hue Slider), thanh trượt độ mờ (Opacity/Alpha), ô nhập HEX/RGB và các ô màu mẫu (Preset Swatches). | Mở Popup Color Picker | - Ô xem trước hiển thị đúng màu hiện tại.<br>- Popup mở ra đầy đủ các thành phần điều khiển, sắc nét, không bị tràn khỏi khung nhìn màn hình. | `Not Run` |
| `TC_CLR_002` | Functional / Chức năng | **High** | **Kiểm tra chọn màu trực tiếp trên vùng phổ màu, thanh Hue và danh sách màu gợi ý sẵn (Presets)** | Popup Color Picker đang mở. | 1. Kéo thanh trượt `Hue` sang vùng màu Xanh dương, sau đó di chuyển điểm tròn trên vùng phổ màu 2D.<br>2. Click chọn lần lượt các ô màu có sẵn trong danh sách `Preset Colors`. | Kéo trên phổ màu & Click Preset Swatches | - Ô xem trước màu (Preview) và giá trị mã `HEX` / `RGB` cập nhật tức thời (Real-time) theo đúng vị trí con trỏ kéo hoặc ô màu Preset vừa chọn. | `Not Run` |
| `TC_CLR_003` | Functional / Chức năng | **High** | **Kiểm tra nhập trực tiếp mã màu thủ công ở các định dạng HEX (`#RRGGBB`, `#RGB`) và RGB (`R, G, B`)** | Popup Color Picker đang mở. | 1. Nhập mã HEX đầy đủ `#FF5733` vào ô HEX.<br>2. Nhập mã HEX viết tắt 3 ký tự `#F00` (tương đương `#FF0000`).<br>3. Chuyển sang chế độ RGB và nhập `R = 37`, `G = 99`, `B = 235`. | - HEX: `#FF5733`, `#F00`<br>- RGB: `37, 99, 235` | - Bảng phổ màu, con trượt Hue và ô xem trước tự động nhảy đến đúng vị trí màu tương ứng.<br>- Chuyển đổi qua lại giữa HEX (`#2563EB`) và RGB (`37, 99, 235`) chính xác 100%. | `Not Run` |
| `TC_CLR_004` | Functional / Chức năng | **Medium** | **Kiểm tra điều chỉnh thanh trượt độ mờ (Opacity / Alpha Slider: `0% -> 100%`)** | Color Picker có hỗ trợ kênh Alpha (RGBA / HEX8). | 1. Kéo thanh trượt Opacity từ `100%` giảm xuống `50%` và về `0%`.<br>2. Nhập trực tiếp số `75%` vào ô phần trăm Opacity. | Opacity: `100%` -> `50%` -> `0%` -> `75%` | - Ô xem trước màu hiển thị lớp nền caro trắng-xám (Checkerboard) phía dưới để thể hiện rõ độ trong suốt.<br>- Mã màu tự động cập nhật đúng giá trị Alpha (VD: `rgba(255, 87, 51, 0.5)`). | `Not Run` |
| `TC_CLR_005` | Validation & Negative | **Medium** | **Kiểm tra xử lý khi nhập mã HEX sai quy chuẩn hoặc giá trị RGB vượt ngoài khoảng `0 - 255`** | Đang nhập vào ô mã màu trong Color Picker. | 1. Nhập chuỗi không hợp lệ vào ô HEX: `#GGGGGG`, `xyz123`, `#12345` rồi nhấn `Enter` hoặc click ra ngoài.<br>2. Nhập số `999` hoặc `-10` vào ô `R / G / B`. | - HEX sai: `#GGGGGG`<br>- RGB vượt ngưỡng: `999`, `-10` | - Bước 1: Hệ thống không bị crash; tự động khôi phục (Revert) về mã màu hợp lệ gần nhất trước đó hoặc hiển thị viền đỏ báo lỗi.<br>- Bước 2: Giá trị RGB tự động giới hạn trong biên `0` đến `255` (`999` -> `255`, `-10` -> `0`). | `Not Run` |
| `TC_CLR_006` | Functional / Chức năng | **Low** | **Kiểm tra công cụ bút chấm hút màu (`Eyedropper`) và lưu danh sách màu vừa dùng (`Recent Colors`)** | Color Picker có nút icon bút hút màu (Eyedropper) và hàng màu vừa sử dụng. | 1. Click icon `Eyedropper` và di chuột chấm vào một điểm màu bất kỳ trên màn hình.<br>2. Đóng và mở lại Color Picker, kiểm tra mục `Màu gần đây (Recent Colors)`. | Eyedropper & Recent Colors | - Hút chính xác mã màu tại điểm ảnh vừa click.<br>- Màu vừa chọn được thêm vào đầu danh sách `Recent Colors` để tái sử dụng nhanh. | `Not Run` |
