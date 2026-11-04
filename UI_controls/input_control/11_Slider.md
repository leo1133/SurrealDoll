# TEST CASE: 11. SLIDER

- **Mô tả chức năng:** Thanh trượt để chọn giá trị định lượng (ví dụ: mức âm lượng, khoảng giá tiền)
- **Tổng số Test Case:** **7** (`High: 4` | `Medium: 3` | `Low: 0`)
- **Phân bổ theo loại kiểm thử:** UI / Giao diện: **1**, Functional / Chức năng: **4**, Boundary / Giá trị biên: **1**, Usability & Accessibility: **1**

---

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_SLD_001`** [High] _UI / Giao diện_ — Kiểm tra giao diện hiển thị mặc định của thanh trượt Slider
- [ ] **`TC_SLD_002`** [High] _Functional / Chức năng_ — Kiểm tra kéo thả nút trượt (Drag Thumb) và click trực tiếp lên thanh Track
- [ ] **`TC_SLD_003`** [Medium] _Functional / Chức năng_ — Kiểm tra bước nhảy định lượng (Step Increment) của thanh Slider
- [ ] **`TC_SLD_004`** [High] _Boundary / Giá trị biên_ — Kiểm tra kéo kịch về giá trị biên tối thiểu (Min) và tối đa (Max), kéo tràn ra ngoài khung
- [ ] **`TC_SLD_005`** [High] _Functional / Chức năng_ — Kiểm tra Range Slider 2 đầu kéo (Chọn khoảng giá từ Min đến Max)
- [ ] **`TC_SLD_006`** [Medium] _Functional / Chức năng_ — Kiểm tra đồng bộ 2 chiều giữa thanh Slider và ô Textbox nhập số đi kèm
- [ ] **`TC_SLD_007`** [Medium] _Usability & Accessibility_ — Kiểm tra điều khiển Slider bằng bàn phím (Mũi tên, Home, End) và trạng thái Disabled

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_SLD_001` | UI / Giao diện | **High** | **Kiểm tra giao diện hiển thị mặc định của thanh trượt Slider** | Màn hình chứa thanh trượt Slider (VD: Khoảng giá / Âm lượng) đã tải xong. | 1. Quan sát thanh ngang (Track), phần thanh đã chọn (Filled track), nút kéo (Thumb/Handle) và nhãn giá trị Min/Max. | N/A | - Hiển thị đúng vị trí giá trị mặc định.<br>- Hiển thị rõ mốc giá trị tối thiểu (Min), tối đa (Max) và số đo hiện tại (qua Label hoặc Tooltip trên đầu nút kéo). | `Not Run` |
| `TC_SLD_002` | Functional / Chức năng | **High** | **Kiểm tra kéo thả nút trượt (Drag Thumb) và click trực tiếp lên thanh Track** | Thanh Slider có `Min = 0`, `Max = 100`, `Step = 1`. | 1. Nhấn giữ chuột vào nút Thumb và kéo sang phải / sang trái.<br>2. Click trực tiếp vào vị trí 50% hoặc 80% trên thanh Track. | Kéo tới 35, Click tại 80 | - Khi kéo: Nút Thumb di chuyển mượt theo con trỏ chuột, màu thanh Track và con số hiển thị cập nhật liên tục theo thời gian thực.<br>- Khi click lên Track: Nút Thumb nhảy ngay đến đúng vị trí vừa click và cập nhật giá trị chính xác. | `Not Run` |
| `TC_SLD_003` | Functional / Chức năng | **Medium** | **Kiểm tra bước nhảy định lượng (Step Increment) của thanh Slider** | Thanh Slider được cấu hình `Min = 0`, `Max = 1.000.000`, `Step = 50.000`. | 1. Kéo nhẹ nút trượt qua từng nấc từ trái sang phải.<br>2. Quan sát các giá trị hiển thị. | Step = 50.000 | - Giá trị của Slider chỉ tăng/giảm theo đúng bội số của bước nhảy `50.000` (`0 -> 50.000 -> 100.000 -> 150.000...`), không xuất hiện các số lẻ nằm giữa bước nhảy. | `Not Run` |
| `TC_SLD_004` | Boundary / Giá trị biên | **High** | **Kiểm tra kéo kịch về giá trị biên tối thiểu (Min) và tối đa (Max), kéo tràn ra ngoài khung** | Slider có `Min = 0`, `Max = 100`. | 1. Kéo nút trượt kịch về đầu bên trái.<br>2. Kéo nút trượt kịch về đầu bên phải.<br>3. Nhấn giữ nút trượt, kéo chuột văng ra ngoài vùng cửa sổ trình duyệt rồi nhả chuột (Mouseup outside). | Min = 0, Max = 100 | - Đầu trái dừng đúng ở `0` (không bị âm).<br>- Đầu phải dừng đúng ở `100` (không vượt quá 100).<br>- Khi nhả chuột bên ngoài khung, sự kiện Drag kết thúc an toàn (không bị dính chuột khi di chuyển lại vào trang). | `Not Run` |
| `TC_SLD_005` | Functional / Chức năng | **High** | **Kiểm tra Range Slider 2 đầu kéo (Chọn khoảng giá từ Min đến Max)** | Thanh trượt có 2 nút kéo: Đầu trái (Min Price) và Đầu phải (Max Price). | 1. Kéo đầu trái đến mức `200.000đ` và đầu phải đến mức `800.000đ`.<br>2. Thử kéo đầu trái vượt qua đầu phải (VD: kéo đầu trái lên `900.000đ` khi đầu phải đang ở `800.000đ`). | Đầu trái = 200k, Đầu phải = 800k | - Bước 1: Phần thanh nằm giữa 2 nút được tô màu nổi bật, lọc dữ liệu đúng trong khoảng `[200.000đ - 800.000đ]`.<br>- Bước 2: Đầu trái bị chặn lại tại mốc `800.000đ` (không được vượt quá đầu phải) hoặc tự động hoán đổi hai đầu hợp lý, không bao giờ để xảy ra `Min > Max`. | `Not Run` |
| `TC_SLD_006` | Functional / Chức năng | **Medium** | **Kiểm tra đồng bộ 2 chiều giữa thanh Slider và ô Textbox nhập số đi kèm** | Slider có ô Textbox hiển thị/nhập số bên cạnh (`Min = 0`, `Max = 100`). | 1. Kéo thanh Slider đến vị trí `65` -> Quan sát ô Textbox.<br>2. Gõ số `30` vào ô Textbox -> Quan sát vị trí nút kéo trên thanh Slider.<br>3. Gõ số `999` (vượt Max) hoặc `-10` (nhỏ hơn Min) vào ô Textbox. | Nhập 65, 30, 999, -10 | - Bước 1 & 2: Slider và Textbox đồng bộ 2 chiều ngay lập tức.<br>- Bước 3: Khi nhập số ngoài biên vào Textbox, hệ thống tự động đưa về biên gần nhất (`100` hoặc `0`) hoặc hiển thị cảnh báo lỗi. | `Not Run` |
| `TC_SLD_007` | Usability & Accessibility | **Medium** | **Kiểm tra điều khiển Slider bằng bàn phím (Mũi tên, Home, End) và trạng thái Disabled** | Slider đang ở trạng thái Enabled / Disabled. | 1. Nhấn `Tab` để Focus vào nút kéo của Slider.<br>2. Nhấn phím mũi tên `Right`/`Up` và `Left`/`Down`, phím `Home` và `End`.<br>3. Kiểm tra khi Slider ở trạng thái Disabled. | Keyboard Navigation | - Mũi tên `Right`/`Up` tăng 1 step; `Left`/`Down` giảm 1 step; `Home` nhảy về Min; `End` nhảy lên Max.<br>- Khi Disabled: Thanh trượt đổi màu xám mờ, không thể kéo hay dùng bàn phím thay đổi giá trị. | `Not Run` |
