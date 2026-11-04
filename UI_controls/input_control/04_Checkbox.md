# TEST CASE: 4. CHECKBOX

- **Mô tả chức năng:** Hộp chọn cho phép chọn nhiều tùy chọn cùng lúc (hoặc đồng ý điều khoản)
- **Tổng số Test Case:** **8** (`High: 5` | `Medium: 3` | `Low: 0`)
- **Phân bổ theo loại kiểm thử:** UI / Giao diện: **2**, Functional / Chức năng: **3**, Validation & Negative: **1**, Boundary / Giá trị biên: **1**, Usability & Accessibility: **1**

---

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_CHK_001`** [High] _UI / Giao diện_ — Kiểm tra giao diện hiển thị mặc định của nhóm Checkbox
- [ ] **`TC_CHK_002`** [High] _Functional / Chức năng_ — Kiểm tra thao tác chọn (Check) và bỏ chọn (Uncheck) một Checkbox
- [ ] **`TC_CHK_003`** [High] _Functional / Chức năng_ — Kiểm tra chọn đồng thời nhiều tùy chọn (Multi-selection) trong cùng một nhóm Checkbox
- [ ] **`TC_CHK_004`** [High] _Functional / Chức năng_ — Kiểm tra chức năng 'Chọn tất cả' (Select All / Master Checkbox)
- [ ] **`TC_CHK_005`** [High] _Validation & Negative_ — Kiểm tra Checkbox bắt buộc (VD: 'Tôi đồng ý với Điều khoản và Chính sách')
- [ ] **`TC_CHK_006`** [Medium] _Boundary / Giá trị biên_ — Kiểm tra giới hạn số lượng Checkbox được phép chọn tối thiểu / tối đa
- [ ] **`TC_CHK_007`** [Medium] _UI / Giao diện_ — Kiểm tra Checkbox ở trạng thái Disabled (Checked-Disabled và Unchecked-Disabled)
- [ ] **`TC_CHK_008`** [Medium] _Usability & Accessibility_ — Kiểm tra chọn/bỏ chọn Checkbox bằng bàn phím (Phím Tab và Space)

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_CHK_001` | UI / Giao diện | **High** | **Kiểm tra giao diện hiển thị mặc định của nhóm Checkbox** | Màn hình có chứa các ô Checkbox đã tải xong. | 1. Quan sát các ô Checkbox và nhãn văn bản (Label) đi kèm.<br>2. Kiểm tra trạng thái mặc định (Checked / Unchecked) khi mới vào trang. | N/A | - Ô Checkbox hình vuông hiển thị rõ nét, căn chỉnh thẳng hàng ngang/dọc với chữ Label bên cạnh.<br>- Trạng thái mặc định (đã chọn sẵn hay bỏ trống) đúng với tài liệu yêu cầu nghiệp vụ. | `Not Run` |
| `TC_CHK_002` | Functional / Chức năng | **High** | **Kiểm tra thao tác chọn (Check) và bỏ chọn (Uncheck) một Checkbox** | Ô Checkbox đang ở trạng thái Unchecked và Enabled. | 1. Click chuột vào ô vuông Checkbox.<br>2. Click chuột lại vào ô vuông Checkbox đó lần thứ 2.<br>3. Click trực tiếp vào dòng chữ Label bên cạnh ô Checkbox. | N/A | - Bước 1: Ô Checkbox chuyển sang trạng thái Checked (hiển thị dấu tick `✓` và đổi màu nền).<br>- Bước 2: Ô Checkbox quay về trạng thái Unchecked (mất dấu tick).<br>- Bước 3: Click vào chữ Label cũng bật/tắt trạng thái Checkbox giống như click vào ô vuông (nhờ liên kết `for`/`id`). | `Not Run` |
| `TC_CHK_003` | Functional / Chức năng | **High** | **Kiểm tra chọn đồng thời nhiều tùy chọn (Multi-selection) trong cùng một nhóm Checkbox** | Nhóm Checkbox có 4 tùy chọn: A, B, C, D. | 1. Click chọn Checkbox A.<br>2. Tiếp tục click chọn Checkbox C và Checkbox D.<br>3. Nhấn Lưu / Submit. | Chọn: [A, C, D] | - Hệ thống cho phép chọn đồng thời A, C, D mà không làm mất lựa chọn trước đó.<br>- Khi Submit, dữ liệu gửi lên Server chứa đầy đủ mảng giá trị `[A, C, D]`. | `Not Run` |
| `TC_CHK_004` | Functional / Chức năng | **High** | **Kiểm tra chức năng 'Chọn tất cả' (Select All / Master Checkbox)** | Danh sách có 1 Checkbox 'Chọn tất cả' (Master) và các Checkbox con (Child items). | 1. Tick vào ô 'Chọn tất cả'.<br>2. Bỏ tick ở ô 'Chọn tất cả'.<br>3. Tick lại 'Chọn tất cả', sau đó bỏ tick 1 Checkbox con bất kỳ.<br>4. Tick lại Checkbox con vừa bỏ để tất cả Checkbox con đều được chọn. | Master Checkbox + 5 Child Checkboxes | - Bước 1: Tất cả 5 Checkbox con đồng loạt được tick chọn.<br>- Bước 2: Tất cả 5 Checkbox con đồng loạt bị bỏ chọn.<br>- Bước 3: Khi bỏ chọn 1 mục con, ô 'Chọn tất cả' tự động chuyển sang trạng thái bán phần (Indeterminate `[-]`) hoặc bỏ dấu tick.<br>- Bước 4: Khi tất cả mục con đều được chọn, ô 'Chọn tất cả' tự động chuyển sang trạng thái Checked (`[✓]`). | `Not Run` |
| `TC_CHK_005` | Validation & Negative | **High** | **Kiểm tra Checkbox bắt buộc (VD: 'Tôi đồng ý với Điều khoản và Chính sách')** | Form đăng ký có Checkbox bắt buộc đồng ý điều khoản. | 1. Điền đầy đủ các trường hợp lệ trên form nhưng KHÔNG tick vào ô 'Đồng ý điều khoản'.<br>2. Quan sát nút Submit hoặc nhấn Submit.<br>3. Tick vào ô 'Đồng ý điều khoản' và nhấn Submit. | Checkbox Điều khoản = Unchecked -> Checked | - Khi chưa tick: Nút Submit bị làm mờ (Disabled) hoặc khi bấm Submit sẽ hiển thị lỗi "Bạn phải đồng ý với điều khoản dịch vụ để tiếp tục".<br>- Khi đã tick: Cho phép Submit thành công. | `Not Run` |
| `TC_CHK_006` | Boundary / Giá trị biên | **Medium** | **Kiểm tra giới hạn số lượng Checkbox được phép chọn tối thiểu / tối đa** | Giả sử nghiệp vụ yêu cầu chọn từ 1 đến tối đa 3 mục. | 1. Không chọn mục nào (0 mục) -> Submit.<br>2. Chọn 3 mục -> Thử click chọn thêm mục thứ 4. | Chọn 0 mục / Chọn 4 mục | - Chọn 0 mục: Báo lỗi "Vui lòng chọn ít nhất 1 mục".<br>- Chọn mục thứ 4: Hệ thống disable các ô còn lại hoặc thông báo "Chỉ được chọn tối đa 3 mục". | `Not Run` |
| `TC_CHK_007` | UI / Giao diện | **Medium** | **Kiểm tra Checkbox ở trạng thái Disabled (Checked-Disabled và Unchecked-Disabled)** | Có Checkbox đang ở trạng thái Disabled. | 1. Click chuột vào ô Checkbox Disabled và chữ Label đi kèm.<br>2. Nếu có nút 'Chọn tất cả', nhấn 'Chọn tất cả' khi trong danh sách có 1 dòng bị Disabled. | N/A | - Ô Checkbox Disabled hiển thị màu xám mờ, con trỏ chuột báo `not-allowed`, click không làm thay đổi trạng thái.<br>- Khi nhấn 'Chọn tất cả', các dòng bị Disabled không bị thay đổi trạng thái trái phép. | `Not Run` |
| `TC_CHK_008` | Usability & Accessibility | **Medium** | **Kiểm tra chọn/bỏ chọn Checkbox bằng bàn phím (Phím Tab và Space)** | Màn hình chứa nhóm Checkbox. | 1. Nhấn phím Tab để di chuyển Focus đến ô Checkbox.<br>2. Nhấn phím Space (Dấu cách) trên bàn phím.<br>3. Nhấn phím Space lần nữa. | Phím Tab + Space | - Khi Focus bằng phím Tab, ô Checkbox có viền outline rõ ràng.<br>- Nhấn phím Space lần 1 sẽ chọn (Check), nhấn lần 2 sẽ bỏ chọn (Uncheck). | `Not Run` |
