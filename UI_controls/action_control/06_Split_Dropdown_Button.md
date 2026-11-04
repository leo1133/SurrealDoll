# TEST CASE: 6. SPLIT / DROPDOWN BUTTON

- **Mô tả chức năng:** Nút bấm kết hợp mũi tên thả xuống các tùy chọn phụ (Lưu -> Lưu nháp / Lưu và gửi)
- **Tổng số Test Case:** **8** (`High: 5` | `Medium: 3` | `Low: 0`)
- **Phân bổ theo loại kiểm thử:** UI / Giao diện: **2**, Functional / Chức năng: **4**, Boundary / Giá trị biên: **1**, Usability & Accessibility: **1**

---

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_SPL_001`** [High] _UI / Giao diện_ — Kiểm tra giao diện cấu trúc 2 phần của Split Button (Nút chính + Nút mũi tên thả xuống)
- [ ] **`TC_SPL_002`** [High] _Functional / Chức năng_ — Kiểm tra click vào phần Nút chính (bên trái) của Split Button
- [ ] **`TC_SPL_003`** [High] _Functional / Chức năng_ — Kiểm tra click vào phần Nút mũi tên (▾ bên phải) để mở/đóng danh sách tùy chọn phụ
- [ ] **`TC_SPL_004`** [High] _Functional / Chức năng_ — Kiểm tra chọn và thực thi từng tùy chọn phụ trong menu của Split Button
- [ ] **`TC_SPL_005`** [Medium] _Functional / Chức năng_ — Kiểm tra đóng menu tùy chọn phụ khi click ra ngoài (Click Outside) hoặc nhấn phím Esc
- [ ] **`TC_SPL_006`** [Medium] _UI / Giao diện_ — Kiểm tra vị trí hiển thị tự động của menu con khi Split Button nằm sát mép hoặc đáy màn hình
- [ ] **`TC_SPL_007`** [High] _Boundary / Giá trị biên_ — Kiểm tra khóa đồng bộ cả 2 phần của Split Button khi đang trong trạng thái Loading hoặc Disabled
- [ ] **`TC_SPL_008`** [Medium] _Usability & Accessibility_ — Kiểm tra điều khiển Split Button và menu tùy chọn phụ bằng bàn phím

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_SPL_001` | UI / Giao diện | **High** | **Kiểm tra giao diện cấu trúc 2 phần của Split Button (Nút chính + Nút mũi tên thả xuống)** | Màn hình có nút Split Button (VD: 'Lưu \| ▾' gồm Lưu nháp, Lưu và gửi, Lưu và thêm mới). | 1. Quan sát cấu trúc nút Split Button.<br>2. Di chuột (Hover) lần lượt vào phần chữ bên trái và phần mũi tên `▾` bên phải. | N/A | - Nút được chia thành 2 vùng bấm rõ ràng ngăn cách bởi đường kẻ dọc (Divider): Bên trái là nhãn hành động mặc định (VD: 'Lưu'), bên phải là biểu tượng mũi tên `▾`.<br>- Khi Hover vào nửa bên nào thì nửa bên đó phản hồi hiệu ứng sáng riêng biệt để người dùng biết là 2 vùng chức năng độc lập. | `Not Run` |
| `TC_SPL_002` | Functional / Chức năng | **High** | **Kiểm tra click vào phần Nút chính (bên trái) của Split Button** | Dữ liệu trên form hợp lệ, menu thả xuống đang đóng. | 1. Click chuột trái vào phần chữ hành động chính (bên trái, VD: 'Lưu'). | Click nửa trái ('Lưu') | - Hệ thống thực thi **ngay lập tức** hành động mặc định ('Lưu') mà KHÔNG mở menu danh sách tùy chọn phụ. | `Not Run` |
| `TC_SPL_003` | Functional / Chức năng | **High** | **Kiểm tra click vào phần Nút mũi tên (▾ bên phải) để mở/đóng danh sách tùy chọn phụ** | Split Button đang ở trạng thái Enabled. | 1. Click chuột vào phần mũi tên `▾` (bên phải).<br>2. Quan sát danh sách menu xổ xuống.<br>3. Click lại vào mũi tên `▾` lần thứ 2. | Click nửa phải (`▾`) | - Bước 1-2: Chỉ mở danh sách các tùy chọn phụ (VD: 'Lưu nháp', 'Lưu và gửi duyệt', 'Lưu và tạo mới'), tuyệt đối **không** tự động kích hoạt hành động 'Lưu' chính.<br>- Bước 3: Menu tùy chọn phụ đóng lại gọn gàng. | `Not Run` |
| `TC_SPL_004` | Functional / Chức năng | **High** | **Kiểm tra chọn và thực thi từng tùy chọn phụ trong menu của Split Button** | Menu tùy chọn phụ của Split Button đang mở. | 1. Click chọn tùy chọn 'Lưu nháp' (Save as Draft) -> Kiểm tra kết quả.<br>2. Mở lại menu và click chọn 'Lưu và tạo mới' (Save & Create New) -> Kiểm tra kết quả. | - Chọn 'Lưu nháp'<br>- Chọn 'Lưu và tạo mới' | - Ngay khi click chọn 1 mục: Menu tự động đóng lại.<br>- Thực thi đúng logic nghiệp vụ của mục đó (VD: 'Lưu nháp' lưu bản ghi ở trạng thái Nháp; 'Lưu và tạo mới' lưu xong sẽ làm mới trắng form để nhập tiếp bản ghi mới). | `Not Run` |
| `TC_SPL_005` | Functional / Chức năng | **Medium** | **Kiểm tra đóng menu tùy chọn phụ khi click ra ngoài (Click Outside) hoặc nhấn phím Esc** | Menu tùy chọn phụ của Split Button đang mở. | 1. Click chuột vào vùng trống bất kỳ bên ngoài Split Button.<br>2. Mở lại menu và nhấn phím `Esc` trên bàn phím. | Click outside / Phím Esc | - Cả hai trường hợp menu đều đóng lại ngay lập tức và không kích hoạt bất kỳ hành động lưu nào. | `Not Run` |
| `TC_SPL_006` | UI / Giao diện | **Medium** | **Kiểm tra vị trí hiển thị tự động của menu con khi Split Button nằm sát mép hoặc đáy màn hình** | Nút Split Button đặt ở thanh công cụ dưới cùng màn hình (Footer) hoặc sát lề phải. | 1. Cuộn trang sao cho nút Split Button nằm sát mép dưới cùng của cửa sổ trình duyệt.<br>2. Click vào mũi tên `▾` để mở menu. | Nút ở sát đáy màn hình | - Menu tùy chọn tự động bật ngược lên phía trên nút (Drop-up) và căn lề phải hợp lý để hiển thị đầy đủ 100% các mục, không bị cắt khuất hoặc tràn ra ngoài màn hình. | `Not Run` |
| `TC_SPL_007` | Boundary / Giá trị biên | **High** | **Kiểm tra khóa đồng bộ cả 2 phần của Split Button khi đang trong trạng thái Loading hoặc Disabled** | Người dùng vừa bấm 'Lưu' (hoặc chọn 'Lưu và gửi') và hệ thống đang xử lý API. | 1. Trong lúc nút chính đang quay Loading (Saving...), thử click vào mũi tên `▾` bên phải để chọn thêm 'Lưu nháp'. | Click `▾` khi đang Loading | - Khi một hành động đang được xử lý (Loading) hoặc khi nút bị Disabled: **Cả hai phần** (Nút chính bên trái và Mũi tên `▾` bên phải) đều phải bị khóa đồng thời, ngăn người dùng mở menu bấm chồng lệnh khác gây xung đột dữ liệu. | `Not Run` |
| `TC_SPL_008` | Usability & Accessibility | **Medium** | **Kiểm tra điều khiển Split Button và menu tùy chọn phụ bằng bàn phím** | Split Button đang ở trạng thái Enabled. | 1. Nhấn `Tab` vào phần nút chính -> Nhấn `Enter` để kiểm tra.<br>2. Nhấn `Tab` sang phần nút mũi tên `▾` -> Nhấn `Enter` / `Space` / `Down Arrow` để mở menu.<br>3. Dùng phím mũi tên `Up`/`Down` di chuyển giữa các mục phụ và nhấn `Enter` để chọn. | Keyboard Navigation | - Hỗ trợ đầy đủ thao tác bàn phím cho cả nút chính và menu thả xuống theo chuẩn WAI-ARIA (`aria-expanded`, `aria-haspopup="true"`). | `Not Run` |
