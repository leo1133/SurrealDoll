# TEST CASE: 3. SCOPED & FILTERED EXPORT (XUẤT THEO BỘ LỌC, TÌM KIẾM & DÒNG ĐÃ CHỌN)

- **Mục đích:** Kiểm tra tính nhất quán giữa dữ liệu đang lọc/tìm kiếm/chọn trên bảng UI và dữ liệu trong file xuất ra
- **Tổng số kịch bản:** **6 Test Cases** (`High: 4`, `Medium: 1`, `Low: 1`)

---

## I. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_SCP_001`** ([High] - *Functional / Chức năng*): Kiểm tra xuất dữ liệu khớp chính xác với kết quả sau khi áp dụng Bộ lọc (Filter) và Tìm kiếm (Search)
- [ ] **`TC_SCP_002`** ([High] - *Functional / Chức năng*): Kiểm tra xuất dữ liệu giữ nguyên đúng thứ tự Sắp xếp (Sort Order) hiện tại trên bảng
- [ ] **`TC_SCP_003`** ([High] - *Functional / Chức năng*): Kiểm tra xuất chỉ riêng các dòng đã tích chọn Checkbox (Export Selected Rows)
- [ ] **`TC_SCP_004`** ([Medium] - *Functional / Chức năng*): Kiểm tra tùy chọn phạm vi xuất: 'Chỉ xuất trang hiện tại (Current Page)' vs 'Xuất tất cả các trang (All Pages)'
- [ ] **`TC_SCP_005`** ([High] - *Boundary / Giá trị biên*): Kiểm tra hành vi nút Export khi danh sách dữ liệu đang trống (0 bản ghi / Empty State)
- [ ] **`TC_SCP_006`** ([Low] - *Boundary / Giá trị biên*): Kiểm tra xuất dữ liệu khi bảng chỉ có duy nhất 1 bản ghi

---

## II. Bảng Chi Tiết Kịch Bản Kiểm Thử

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_SCP_001` | Functional / Chức năng | **High** | **Kiểm tra xuất dữ liệu khớp chính xác với kết quả sau khi áp dụng Bộ lọc (Filter) và Tìm kiếm (Search)** | Tổng dữ liệu trong hệ thống có 1,000 bản ghi. Khi lọc theo `Trạng thái = Hoàn thành` và từ khóa `'Hà Nội'` thì trên màn hình còn lại **18 bản ghi**. | 1. Áp dụng bộ lọc `Trạng thái = Hoàn thành` + từ khóa `'Hà Nội'` (màn hình hiển thị 18 kết quả).<br>2. Click nút `[Xuất Excel / Export]`.<br>3. Mở file Excel kiểm tra số lượng và nội dung bản ghi. | Tổng 1000 dòng -> Lọc còn 18 dòng -> Bấm Export | - File Excel xuất ra chỉ chứa đúng **18 bản ghi** thỏa mãn điều kiện đang lọc trên màn hình (tuyệt đối không xuất nhầm toàn bộ 1,000 bản ghi chưa lọc). | `Not Run` |
| `TC_SCP_002` | Functional / Chức năng | **High** | **Kiểm tra xuất dữ liệu giữ nguyên đúng thứ tự Sắp xếp (Sort Order) hiện tại trên bảng** | Người dùng đã bấm sắp xếp cột `Tổng tiền` theo thứ tự Giảm dần (`DESC` - từ cao nhất xuống thấp nhất). | 1. Sắp xếp bảng theo `Tổng tiền giảm dần`.<br>2. Click `[Xuất Excel]` và mở file kiểm tra thứ tự các dòng. | Sort Tổng tiền Giảm dần -> Bấm Export | - Thứ tự các dòng trong file Excel được giữ nguyên từ cao xuống thấp giống hệt với thứ tự người dùng đang xem trên màn hình. | `Not Run` |
| `TC_SCP_003` | Functional / Chức năng | **High** | **Kiểm tra xuất chỉ riêng các dòng đã tích chọn Checkbox (Export Selected Rows)** | Bảng dữ liệu có cột Checkbox ở đầu mỗi dòng. Người dùng tích chọn 4 dòng bất kỳ. | 1. Tích chọn Checkbox ở dòng thứ 1, 3, 7 và 10.<br>2. Click nút `[Xuất các mục đã chọn (4)]` (hoặc bấm `[Export]` khi đang có dòng được chọn).<br>3. Mở file kiểm tra. | Tích chọn 4 dòng -> Click Export Selected | - File xuất ra chỉ chứa đúng **4 bản ghi** mà người dùng đã tích chọn. | `Not Run` |
| `TC_SCP_004` | Functional / Chức năng | **Medium** | **Kiểm tra tùy chọn phạm vi xuất: 'Chỉ xuất trang hiện tại (Current Page)' vs 'Xuất tất cả các trang (All Pages)'** | Kết quả lọc có tổng cộng 150 bản ghi, đang chia thành 8 trang (20 dòng/trang), người dùng đang đứng ở Trang 2. | 1. Chọn xuất với tùy chọn `'Trang hiện tại (Current Page)'`.<br>2. Chọn xuất với tùy chọn `'Tất cả bản ghi (All 150 records)'`.  | 150 bản ghi (8 trang) -> Xuất Trang 2 vs Xuất Tất cả | - Bước 1: File xuất ra chứa đúng 20 bản ghi của Trang 2 (từ bản ghi 21 đến 40).<br>- Bước 2: File xuất ra chứa đầy đủ toàn bộ 150 bản ghi của cả 8 trang. | `Not Run` |
| `TC_SCP_005` | Boundary / Giá trị biên | **High** | **Kiểm tra hành vi nút Export khi danh sách dữ liệu đang trống (0 bản ghi / Empty State)** | Lọc dữ liệu với từ khóa không có kết quả nào (`0 bản ghi hiển thị trên bảng`). | 1. Quan sát trạng thái nút `[Xuất dữ liệu / Export]` khi bảng có 0 bản ghi.<br>2. (Nếu nút vẫn cho bấm): Click vào nút `[Export]`.  | Bảng dữ liệu có 0 bản ghi | - Cách 1 (Khuyến nghị): Nút `[Export]` tự động chuyển sang trạng thái làm mờ (`Disabled`) khi không có dữ liệu.<br>- Cách 2: Nếu cho bấm thì hiển thị Toast cảnh báo `'Không có dữ liệu nào để xuất'`, không gọi API tải về file rỗng vô nghĩa. | `Not Run` |
| `TC_SCP_006` | Boundary / Giá trị biên | **Low** | **Kiểm tra xuất dữ liệu khi bảng chỉ có duy nhất 1 bản ghi** | Bộ lọc trả về đúng 1 bản ghi duy nhất. | 1. Click `[Xuất dữ liệu]` và mở file. | Bảng có đúng 1 bản ghi | - File xuất thành công gồm 1 dòng Header và 1 dòng dữ liệu chính xác. | `Not Run` |
