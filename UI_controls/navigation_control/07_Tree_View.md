# TEST CASE: 7. TREE VIEW

- **Mô tả chức năng:** Menu dạng cấu trúc cây cha - con đa cấp (Quản lý thư mục, phòng ban, danh mục)
- **Tổng số Test Case:** **8** (`High: 5` | `Medium: 3` | `Low: 0`)
- **Phân bổ theo loại kiểm thử:** UI / Giao diện: **1**, Functional / Chức năng: **4**, Boundary / Giá trị biên: **1**, Validation & Negative: **1**, Usability & Accessibility: **1**

---

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_TRV_001`** [High] _UI / Giao diện_ — Kiểm tra giao diện hiển thị cấu trúc phân cấp Cha - Con của Tree View
- [ ] **`TC_TRV_002`** [High] _Functional / Chức năng_ — Kiểm tra thao tác Mở rộng (Expand) và Thu gọn (Collapse) các nhánh trên Tree View
- [ ] **`TC_TRV_003`** [High] _Functional / Chức năng_ — Kiểm tra click chọn một nút (Node Selection) trên Tree View để xem dữ liệu tương ứng
- [ ] **`TC_TRV_004`** [High] _Functional / Chức năng_ — Kiểm tra Tree View kết hợp Checkbox chọn đa cấp (Parent - Child Checkbox Propagation)
- [ ] **`TC_TRV_005`** [Medium] _Functional / Chức năng_ — Kiểm tra tìm kiếm / lọc nút trên Tree View (Tree Search & Auto-expand)
- [ ] **`TC_TRV_006`** [Medium] _Boundary / Giá trị biên_ — Kiểm tra hiển thị khi cây có độ sâu lớn (> 8 cấp) hoặc tên nút quá dài
- [ ] **`TC_TRV_007`** [High] _Validation & Negative_ — Kiểm tra chặn lỗi vòng lặp (Circular Reference) khi di chuyển / kéo thả nhánh Cha vào chính nhánh Con của nó
- [ ] **`TC_TRV_008`** [Medium] _Usability & Accessibility_ — Kiểm tra điều hướng trên Tree View bằng bàn phím (Mũi tên Up, Down, Left, Right, Enter)

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_TRV_001` | UI / Giao diện | **High** | **Kiểm tra giao diện hiển thị cấu trúc phân cấp Cha - Con của Tree View** | Màn hình chứa cây thư mục / sơ đồ phòng ban (Tree View) đã tải xong. | 1. Quan sát các nút gốc (Root nodes), nút nhánh (Parent nodes) và nút lá (Leaf nodes).<br>2. Kiểm tra khoảng cách thụt lề (Indentation) giữa các cấp và icon mũi tên mở rộng (`▸` / `▾`). | Cây thư mục 3-4 cấp | - Mỗi cấp con được thụt lề sang phải một khoảng đồng đều so với cấp cha, giúp nhìn rõ quan hệ Cha - Con.<br>- Các nút có chứa cấp con hiển thị icon mũi tên `▸` (hoặc dấu `+`); nút lá cuối cùng (không có con) không hiển thị mũi tên mở rộng. | `Not Run` |
| `TC_TRV_002` | Functional / Chức năng | **High** | **Kiểm tra thao tác Mở rộng (Expand) và Thu gọn (Collapse) các nhánh trên Tree View** | Nhánh Cha 'Khối Công nghệ' có các nhánh Con 'Phòng Phát triển' và 'Phòng QA'. | 1. Click vào mũi tên `▸` cạnh 'Khối Công nghệ' (Expand).<br>2. Click tiếp mũi tên `▸` cạnh 'Phòng QA' để mở các nhóm con.<br>3. Click lại vào mũi tên `▾` cạnh 'Khối Công nghệ' (Collapse). | Expand -> Collapse nhánh cây | - Bước 1-2: Mũi tên xoay thành `▾`, hiển thị đầy đủ các nút con bên dưới.<br>- Bước 3: Khi thu gọn nhánh Cha cao nhất ('Khối Công nghệ'), toàn bộ các nhánh Con và Cháu trực thuộc đều được ẩn gọn lại. | `Not Run` |
| `TC_TRV_003` | Functional / Chức năng | **High** | **Kiểm tra click chọn một nút (Node Selection) trên Tree View để xem dữ liệu tương ứng** | Tree View dùng để lọc dữ liệu theo Phòng ban hoặc Thư mục. | 1. Click vào tên nút 'Phòng QA' trên cây.<br>2. Click chuyển sang tên nút 'Phòng Phát triển'. | Chọn Node trên cây | - Nút đang được chọn đổi màu nền highlight (Selected state).<br>- Bảng dữ liệu chi tiết bên phải cập nhật ngay danh sách nhân sự/tài liệu thuộc đúng phòng ban/thư mục vừa chọn. | `Not Run` |
| `TC_TRV_004` | Functional / Chức năng | **High** | **Kiểm tra Tree View kết hợp Checkbox chọn đa cấp (Parent - Child Checkbox Propagation)** | Tree View có hỗ trợ Checkbox ở đầu mỗi nút (VD: Cây phân quyền chức năng). | 1. Tick chọn Checkbox tại nút Cha.<br>2. Bỏ tick 1 nút Con bên trong nhánh đó.<br>3. Bỏ tick toàn bộ các nút Con bên trong nhánh đó. | Checkbox trên Tree View | - Bước 1: Khi tick nút Cha, tất cả các nút Con và Cháu trực thuộc tự động được tick chọn.<br>- Bước 2: Khi chỉ có một số nút Con được chọn, nút Cha tự động chuyển sang trạng thái bán phần (`Indeterminate [-]` ).<br>- Bước 3: Khi không còn nút Con nào được chọn, nút Cha tự động bỏ tick (`Unchecked`). | `Not Run` |
| `TC_TRV_005` | Functional / Chức năng | **Medium** | **Kiểm tra tìm kiếm / lọc nút trên Tree View (Tree Search & Auto-expand)** | Tree View có ô tìm kiếm nhanh các nút trên cây. | 1. Nhập tên của một nút Con đang nằm ẩn ở cấp thứ 3 vào ô tìm kiếm.<br>2. Xóa từ khóa tìm kiếm. | Từ khóa khớp với Node cấp 3 | - Hệ thống lọc và tự động mở rộng (Auto-expand) các nhánh Cha liên quan để lộ ra nút Con khớp từ khóa (kèm tô đậm từ khóa).<br>- Khi xóa từ khóa, cây quay về trạng thái hiển thị đầy đủ. | `Not Run` |
| `TC_TRV_006` | Boundary / Giá trị biên | **Medium** | **Kiểm tra hiển thị khi cây có độ sâu lớn (> 8 cấp) hoặc tên nút quá dài** | Cây có nhánh sâu 8-10 cấp và tên thư mục dài. | 1. Mở rộng liên tiếp từ cấp 1 đến cấp 10.<br>2. Quan sát khung chứa Tree View. | Deep Nesting (10 cấp) | - Khung Tree View xuất hiện thanh cuộn ngang/dọc mượt mà hoặc hiển thị Tooltip đầy đủ khi Hover, không làm chữ bị cắt mất hoàn toàn hay tràn đè sang khung nội dung bên phải. | `Not Run` |
| `TC_TRV_007` | Validation & Negative | **High** | **Kiểm tra chặn lỗi vòng lặp (Circular Reference) khi di chuyển / kéo thả nhánh Cha vào chính nhánh Con của nó** | Tree View cho phép Kéo thả (Drag & Drop) hoặc đổi 'Danh mục cha' của một nút. | 1. Thử kéo nhánh Cha 'Thư mục A' thả vào bên trong 'Thư mục A1' (vốn là con của A). | Di chuyển Node Cha vào trong Node Con của chính nó | - Hệ thống chặn thao tác và báo lỗi "Không thể di chuyển thư mục cha vào bên trong thư mục con của chính nó". | `Not Run` |
| `TC_TRV_008` | Usability & Accessibility | **Medium** | **Kiểm tra điều hướng trên Tree View bằng bàn phím (Mũi tên Up, Down, Left, Right, Enter)** | Đang Focus tại một nút trên Tree View. | 1. Nhấn phím mũi tên `Down` / `Up` để đi lên/xuống.<br>2. Nhấn mũi tên `Right` để mở rộng nhánh (Expand), mũi tên `Left` để đóng nhánh (Collapse).<br>3. Nhấn `Enter` hoặc `Space` để chọn nút. | Keyboard Navigation | - Các phím mũi tên điều khiển đóng/mở và di chuyển giữa các nút đúng quy chuẩn `role="tree"` và `role="treeitem"`. | `Not Run` |
