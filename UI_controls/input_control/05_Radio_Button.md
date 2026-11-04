# TEST CASE: 5. RADIO BUTTON

- **Mô tả chức năng:** Nút chọn dạng tròn, chỉ cho phép chọn duy nhất 1 tùy chọn trong một nhóm
- **Tổng số Test Case:** **7** (`High: 4` | `Medium: 3` | `Low: 0`)
- **Phân bổ theo loại kiểm thử:** UI / Giao diện: **1**, Functional / Chức năng: **4**, Validation & Negative: **1**, Usability & Accessibility: **1**

---

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_RAD_001`** [High] _UI / Giao diện_ — Kiểm tra giao diện hiển thị mặc định của nhóm Radio Button
- [ ] **`TC_RAD_002`** [High] _Functional / Chức năng_ — Kiểm tra tính loại trừ (Mutual Exclusivity) - Chỉ chọn được duy nhất 1 tùy chọn trong nhóm
- [ ] **`TC_RAD_003`** [Medium] _Functional / Chức năng_ — Kiểm tra click lại vào Radio Button đang được chọn và click vào chữ Label
- [ ] **`TC_RAD_004`** [High] _Functional / Chức năng_ — Kiểm tra tính độc lập giữa nhiều nhóm Radio Button khác nhau trên cùng 1 màn hình
- [ ] **`TC_RAD_005`** [High] _Validation & Negative_ — Kiểm tra không chọn bất kỳ Radio Button nào đối với nhóm bắt buộc (Required)
- [ ] **`TC_RAD_006`** [Medium] _Functional / Chức năng_ — Kiểm tra hiển thị các trường phụ thuộc (Conditional Fields) khi đổi lựa chọn Radio Button
- [ ] **`TC_RAD_007`** [Medium] _Usability & Accessibility_ — Kiểm tra điều hướng bằng bàn phím (Tab + Phím mũi tên Up/Down/Left/Right) và trạng thái Disabled

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_RAD_001` | UI / Giao diện | **High** | **Kiểm tra giao diện hiển thị mặc định của nhóm Radio Button** | Màn hình chứa nhóm Radio Button (VD: Giới tính: Nam / Nữ / Khác). | 1. Quan sát hình dạng, căn lề, khoảng cách giữa các Radio Button và Label.<br>2. Kiểm tra giá trị được chọn mặc định (Default selected) nếu có. | N/A | - Các nút Radio Button có dạng hình tròn đồng nhất, căn thẳng hàng với Label.<br>- Giá trị mặc định (nếu được quy định trong tài liệu) được chấm tròn sẵn chính xác. | `Not Run` |
| `TC_RAD_002` | Functional / Chức năng | **High** | **Kiểm tra tính loại trừ (Mutual Exclusivity) - Chỉ chọn được duy nhất 1 tùy chọn trong nhóm** | Nhóm Radio Button có 3 tùy chọn: Option 1, Option 2, Option 3. | 1. Click chọn 'Option 1'.<br>2. Click chuyển sang chọn 'Option 2'.<br>3. Click chuyển sang chọn 'Option 3'. | Option 1 -> Option 2 -> Option 3 | - Bước 1: 'Option 1' được chọn (có chấm tròn ở giữa).<br>- Bước 2: 'Option 2' được chọn và 'Option 1' tự động bị bỏ chọn.<br>- Bước 3: 'Option 3' được chọn và 'Option 2' tự động bị bỏ chọn.<br>- Tại mọi thời điểm chỉ có duy nhất 1 Radio Button được active trong cùng một nhóm. | `Not Run` |
| `TC_RAD_003` | Functional / Chức năng | **Medium** | **Kiểm tra click lại vào Radio Button đang được chọn và click vào chữ Label** | Radio Button 'Option 1' đang ở trạng thái chưa chọn. | 1. Click vào chữ Label của 'Option 1'.<br>2. Click thêm một lần nữa vào chính 'Option 1' đang được chọn. | N/A | - Bước 1: Click vào chữ Label sẽ chọn 'Option 1' (vùng bấm bao gồm cả nút tròn và chữ).<br>- Bước 2: Click lại vào Radio Button đang chọn sẽ KHÔNG làm bỏ chọn nút đó (vẫn giữ trạng thái Selected). | `Not Run` |
| `TC_RAD_004` | Functional / Chức năng | **High** | **Kiểm tra tính độc lập giữa nhiều nhóm Radio Button khác nhau trên cùng 1 màn hình** | Form có Nhóm 1 (Giới tính: Nam/Nữ) và Nhóm 2 (Hình thức thanh toán: Tiền mặt/Chuyển khoản). | 1. Chọn 'Nam' ở Nhóm 1.<br>2. Chọn 'Chuyển khoản' ở Nhóm 2.<br>3. Đổi Nhóm 1 sang 'Nữ'. | Nhóm 1: Nữ, Nhóm 2: Chuyển khoản | - Việc chọn hoặc thay đổi giá trị ở Nhóm 2 hoàn toàn độc lập, không làm mất hay ảnh hưởng đến lựa chọn của Nhóm 1 (do mỗi nhóm có thuộc tính `name` riêng biệt). | `Not Run` |
| `TC_RAD_005` | Validation & Negative | **High** | **Kiểm tra không chọn bất kỳ Radio Button nào đối với nhóm bắt buộc (Required)** | Nhóm Radio Button là trường bắt buộc nhưng chưa có giá trị chọn mặc định. | 1. Để trống không chọn tùy chọn nào trong nhóm Radio Button.<br>2. Nhấn nút Submit / Tiếp tục. | Giá trị chọn: null | - Hệ thống chặn Submit và hiển thị thông báo lỗi yêu cầu người dùng phải chọn 1 phương án. | `Not Run` |
| `TC_RAD_006` | Functional / Chức năng | **Medium** | **Kiểm tra hiển thị các trường phụ thuộc (Conditional Fields) khi đổi lựa chọn Radio Button** | Chọn Radio A mở thêm ô nhập A1; Chọn Radio B ẩn ô A1 và mở ô B1. | 1. Chọn Radio A -> Nhập dữ liệu vào ô A1.<br>2. Chuyển sang chọn Radio B -> Quan sát giao diện và nhấn Submit. | Chuyển từ Radio A sang Radio B | - Khi chuyển sang Radio B, ô A1 bị ẩn đi (hoặc disable) và dữ liệu cũ của A1 không gây lỗi validation hay gửi rác lên Server. | `Not Run` |
| `TC_RAD_007` | Usability & Accessibility | **Medium** | **Kiểm tra điều hướng bằng bàn phím (Tab + Phím mũi tên Up/Down/Left/Right) và trạng thái Disabled** | Nhóm Radio Button có các nút Enabled và 1 nút Disabled. | 1. Nhấn Tab để di chuyển vào nhóm Radio Button.<br>2. Nhấn các phím mũi tên Lên/Xuống/Trái/Phải để đổi lựa chọn.<br>3. Thử click hoặc di chuyển vào nút Radio đang bị Disabled. | Keyboard Navigation | - Phím mũi tên cho phép chuyển đổi mượt mà giữa các Radio Button đang Enabled trong nhóm.<br>- Nút Radio bị Disabled hiển thị mờ, không thể chọn bằng chuột hay bàn phím. | `Not Run` |
