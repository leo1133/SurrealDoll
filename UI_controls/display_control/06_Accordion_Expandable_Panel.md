# TEST CASE: 6. ACCORDION / EXPANDABLE PANEL

- **Mô tả chức năng:** Khối nội dung có thể mở rộng ra hoặc thu gọn lại (thường dùng ở trang FAQ / Chi tiết)
- **Tổng số Test Case:** **6** (`High: 3` | `Medium: 3` | `Low: 0`)
- **Phân bổ theo loại kiểm thử:** UI / Giao diện: **1**, Functional / Chức năng: **3**, Boundary / Giá trị biên: **1**, Usability & Accessibility: **1**

---

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_ACC_001`** [High] _UI / Giao diện_ — Kiểm tra giao diện hiển thị mặc định của khối Accordion / Expandable Panel
- [ ] **`TC_ACC_002`** [High] _Functional / Chức năng_ — Kiểm tra thao tác Mở rộng (Expand) và Thu gọn (Collapse) nội dung Accordion
- [ ] **`TC_ACC_003`** [High] _Functional / Chức năng_ — Kiểm tra quy tắc đóng/mở đồng thời nhiều khối Accordion (Single-expand vs Multi-expand)
- [ ] **`TC_ACC_004`** [Medium] _Functional / Chức năng_ — Kiểm tra tương tác với các phần tử bên trong Accordion và giữ nguyên trạng thái khi đóng/mở lại
- [ ] **`TC_ACC_005`** [Medium] _Boundary / Giá trị biên_ — Kiểm tra hiển thị khi nội dung bên trong Accordion rất dài hoặc chứa ảnh / bảng lớn
- [ ] **`TC_ACC_006`** [Medium] _Usability & Accessibility_ — Kiểm tra điều khiển đóng/mở Accordion bằng bàn phím (Tab + Enter / Space) và trạng thái Disabled

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_ACC_001` | UI / Giao diện | **High** | **Kiểm tra giao diện hiển thị mặc định của khối Accordion / Expandable Panel** | Màn hình chứa danh sách Accordion (VD: Trang Câu hỏi thường gặp FAQ / Thông số kỹ thuật). | 1. Quan sát các thanh tiêu đề (Accordion Header), icon đóng/mở (`▾` / `+`) và trạng thái mặc định của các khối khi mới vào trang. | Danh sách 5 khối Accordion | - Các thanh tiêu đề hiển thị rõ ràng, con trỏ chuột là `pointer`.<br>- Trạng thái mặc định (tất cả đều đóng hoặc mở sẵn mục đầu tiên) đúng theo thiết kế.<br>- Icon của mục đang mở (`▴` hoặc `-`) và mục đang đóng (`▾` hoặc `+`) thể hiện đúng trạng thái. | `Not Run` |
| `TC_ACC_002` | Functional / Chức năng | **High** | **Kiểm tra thao tác Mở rộng (Expand) và Thu gọn (Collapse) nội dung Accordion** | Khối Accordion 1 đang ở trạng thái Thu gọn (Collapsed). | 1. Click vào bất kỳ vị trí nào trên thanh tiêu đề (Header) của Accordion 1.<br>2. Quan sát nội dung mở ra và vị trí của các khối Accordion 2, 3 bên dưới.<br>3. Click lại vào thanh tiêu đề của Accordion 1 một lần nữa. | Click Header lần 1 (Expand) -> Click lần 2 (Collapse) | - Bước 1-2: Khối nội dung của Accordion 1 mở rộng ra mượt mà, icon mũi tên xoay ngược lại, đẩy các khối Accordion 2, 3 xuống dưới một cách tự nhiên (không đè lấp lên nhau).<br>- Bước 3: Khối nội dung thu gọn lại hoàn toàn như ban đầu. | `Not Run` |
| `TC_ACC_003` | Functional / Chức năng | **High** | **Kiểm tra quy tắc đóng/mở đồng thời nhiều khối Accordion (Single-expand vs Multi-expand)** | Danh sách có nhiều khối Accordion: Khối 1 đang được mở. | 1. Click mở tiếp Khối 2.<br>2. Quan sát trạng thái của Khối 1. | Khối 1 đang mở -> Click mở Khối 2 | - Hệ thống hoạt động đúng theo thiết kế quy định:<br>  + Nếu là **Single-expand Accordion**: Khi mở Khối 2, Khối 1 tự động thu gọn lại.<br>  + Nếu là **Multi-expand Panel**: Cho phép cả Khối 1 và Khối 2 cùng mở song song. | `Not Run` |
| `TC_ACC_004` | Functional / Chức năng | **Medium** | **Kiểm tra tương tác với các phần tử bên trong Accordion và giữ nguyên trạng thái khi đóng/mở lại** | Bên trong nội dung Accordion có chứa các ô nhập liệu, Checkbox hoặc đường Link. | 1. Mở Accordion -> Nhập dữ liệu hoặc tích chọn Checkbox bên trong.<br>2. Thu gọn Accordion đó lại rồi mở ra lần nữa. | Nhập liệu trong Accordion -> Collapse -> Expand | - Các nút bấm, đường link, ô input bên trong Accordion hoạt động bình thường.<br>- Khi thu gọn rồi mở lại, dữ liệu vừa nhập bên trong vẫn được giữ nguyên (không bị unmount làm mất state). | `Not Run` |
| `TC_ACC_005` | Boundary / Giá trị biên | **Medium** | **Kiểm tra hiển thị khi nội dung bên trong Accordion rất dài hoặc chứa ảnh / bảng lớn** | Khối Accordion có phần câu trả lời dài 1000 từ kèm hình ảnh minh họa. | 1. Click mở khối Accordion có nội dung dài trên cả Desktop và Mobile. | Nội dung dài 1000 từ + Hình ảnh | - Chiều cao khung nội dung tự động giãn nở hết toàn bộ văn bản và hình ảnh, không bị lỗi cắt cụt phần đuôi văn bản do giới hạn `max-height` cứng trong CSS animation. | `Not Run` |
| `TC_ACC_006` | Usability & Accessibility | **Medium** | **Kiểm tra điều khiển đóng/mở Accordion bằng bàn phím (Tab + Enter / Space) và trạng thái Disabled** | Danh sách Accordion có các mục Enabled và 1 mục Disabled. | 1. Dùng phím `Tab` di chuyển Focus đến tiêu đề Accordion rồi nhấn `Enter` hoặc `Space`.<br>2. Thử click hoặc nhấn phím vào mục Accordion đang bị Disabled. | Keyboard Navigation & Disabled Accordion | - Nhấn `Enter` hoặc `Space` đóng/mở được khối Accordion đang Focus, thuộc tính `aria-expanded="true/false"` cập nhật đúng.<br>- Khối bị Disabled hiển thị mờ và không thể mở ra. | `Not Run` |
