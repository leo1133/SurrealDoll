# TEST CASE: 3. BREADCRUMBS

- **Mô tả chức năng:** Vết điều hướng hiển thị vị trí phân cấp hiện tại (Trang chủ > Sản phẩm > Điện thoại > iPhone)
- **Tổng số Test Case:** **7** (`High: 3` | `Medium: 3` | `Low: 1`)
- **Phân bổ theo loại kiểm thử:** UI / Giao diện: **1**, Functional / Chức năng: **3**, Boundary / Giá trị biên: **1**, Security / Bảo mật: **1**, Usability & Accessibility: **1**

---

## 1. Checklist Kiểm Thử Nhanh (Quick QA Checklist)

- [ ] **`TC_BRC_001`** [High] _UI / Giao diện_ — Kiểm tra giao diện hiển thị mặc định của thanh đường dẫn phân cấp Breadcrumbs
- [ ] **`TC_BRC_002`** [High] _Functional / Chức năng_ — Kiểm tra điều hướng khi click vào các cấp cha trên Breadcrumbs
- [ ] **`TC_BRC_003`** [High] _Functional / Chức năng_ — Kiểm tra phần tử cuối cùng trên Breadcrumbs (Trang hiện tại) không phải là link bấm lại
- [ ] **`TC_BRC_004`** [Medium] _Functional / Chức năng_ — Kiểm tra tính chính xác của Breadcrumbs khi truy cập bằng Deep Link hoặc sau khi cập nhật tên
- [ ] **`TC_BRC_005`** [Medium] _Boundary / Giá trị biên_ — Kiểm tra hiển thị Breadcrumbs khi tên trang quá dài (> 150 ký tự) hoặc phân cấp quá sâu
- [ ] **`TC_BRC_006`** [Medium] _Security / Bảo mật_ — Kiểm tra chống lỗi XSS trên Breadcrumbs khi tên danh mục/sản phẩm chứa thẻ HTML
- [ ] **`TC_BRC_007`** [Low] _Usability & Accessibility_ — Kiểm tra chuẩn trợ năng (WAI-ARIA) và điều hướng bàn phím trên Breadcrumbs

---

## 2. Bảng Chi Tiết Test Cases

| Mã TC | Phân loại | Độ ưu tiên | Tên kịch bản (Title) | Điều kiện tiên quyết | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả mong đợi (Expected Result) | Trạng thái |
| :--- | :--- | :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| `TC_BRC_001` | UI / Giao diện | **High** | **Kiểm tra giao diện hiển thị mặc định của thanh đường dẫn phân cấp Breadcrumbs** | Đang ở trang danh mục con hoặc trang chi tiết (VD: Trang chủ > Sản phẩm > Điện thoại > iPhone 16). | 1. Quan sát vị trí, font chữ, màu sắc và ký tự phân cách (`>` hoặc `/`) giữa các cấp trên Breadcrumbs. | Trang chủ > Sản phẩm > Điện thoại > iPhone 16 | - Breadcrumbs đặt ở phía trên tiêu đề trang, hiển thị đúng thứ tự phân cấp từ gốc (Trang chủ) đến trang hiện tại.<br>- Các cấp cha có màu sắc của liên kết (Link), cấp cuối cùng (trang hiện tại) có màu chữ trầm/đậm hơn để phân biệt. | `Not Run` |
| `TC_BRC_002` | Functional / Chức năng | **High** | **Kiểm tra điều hướng khi click vào các cấp cha trên Breadcrumbs** | Breadcrumbs đang hiển thị: `Trang chủ > Sản phẩm > Điện thoại > iPhone 16`. | 1. Click vào chữ 'Điện thoại' trên Breadcrumbs.<br>2. Quay lại trang chi tiết rồi click vào chữ 'Sản phẩm' và 'Trang chủ'. | Click các cấp cha trên Breadcrumbs | - Click 'Điện thoại': Điều hướng về đúng danh sách danh mục Điện thoại.<br>- Click 'Sản phẩm': Điều hướng về trang tổng hợp Sản phẩm.<br>- Click 'Trang chủ': Điều hướng về Trang chủ. | `Not Run` |
| `TC_BRC_003` | Functional / Chức năng | **High** | **Kiểm tra phần tử cuối cùng trên Breadcrumbs (Trang hiện tại) không phải là link bấm lại** | Breadcrumbs đang hiển thị: `Trang chủ > Sản phẩm > Điện thoại > iPhone 16`. | 1. Di chuột vào mục cuối cùng ('iPhone 16') trên Breadcrumbs và thử click. | Mục cuối: 'iPhone 16' | - Mục cuối cùng hiển thị tên của trang hiện tại, ở trạng thái không thể click (Plain text, `cursor: default`), không gây tải lại trang một cách dư thừa. | `Not Run` |
| `TC_BRC_004` | Functional / Chức năng | **Medium** | **Kiểm tra tính chính xác của Breadcrumbs khi truy cập bằng Deep Link hoặc sau khi cập nhật tên** | Người dùng mở trực tiếp link sản phẩm từ bên ngoài hoặc vừa sửa tên sản phẩm/danh mục. | 1. Dán trực tiếp URL trang chi tiết vào tab trình duyệt mới.<br>2. Chỉnh sửa tên sản phẩm/bài viết và lưu lại, sau đó quan sát Breadcrumbs. | Deep Link & Cập nhật tên | - Breadcrumbs luôn hiển thị đầy đủ và chính xác các cấp cha theo cấu trúc dữ liệu (không bị mất cấp giữa khi vào bằng link trực tiếp).<br>- Khi đổi tên bản ghi, nhãn trên Breadcrumbs cập nhật theo tên mới ngay lập tức. | `Not Run` |
| `TC_BRC_005` | Boundary / Giá trị biên | **Medium** | **Kiểm tra hiển thị Breadcrumbs khi tên trang quá dài (> 150 ký tự) hoặc phân cấp quá sâu** | Bài viết / Sản phẩm có tiêu đề rất dài hoặc nằm ở cấp thư mục thứ 6. | 1. Quan sát thanh Breadcrumbs trên màn hình Desktop và Mobile. | Tiêu đề dài 150 ký tự / 6 cấp danh mục | - Tên quá dài được cắt gọn bằng dấu `...` (`text-overflow: ellipsis`) kèm Tooltip khi Hover.<br>- Khi có quá nhiều cấp hoặc trên màn hình Mobile hẹp: Tự động thu gọn các cấp giữa thành `Trang chủ > ... > Điện thoại > iPhone 16` hoặc cho phép cuộn ngang gọn gàng, không làm vỡ giao diện. | `Not Run` |
| `TC_BRC_006` | Security / Bảo mật | **Medium** | **Kiểm tra chống lỗi XSS trên Breadcrumbs khi tên danh mục/sản phẩm chứa thẻ HTML** | Tên sản phẩm hoặc danh mục có chứa chuỗi `<script>alert(1)</script>` hoặc `<b>Tên</b>`. | 1. Mở trang chi tiết của sản phẩm đó và quan sát thanh Breadcrumbs. | Tên chứa `<script>alert(1)</script>` | - Chuỗi tên trên Breadcrumbs được escape hoàn toàn dưới dạng văn bản thuần, không thực thi script và không làm hỏng thẻ HTML của Breadcrumbs. | `Not Run` |
| `TC_BRC_007` | Usability & Accessibility | **Low** | **Kiểm tra chuẩn trợ năng (WAI-ARIA) và điều hướng bàn phím trên Breadcrumbs** | Màn hình có Breadcrumbs. | 1. Dùng phím `Tab` di chuyển qua các link trên Breadcrumbs.<br>2. Kiểm tra thuộc tính HTML của vùng Breadcrumbs. | `aria-label="Breadcrumb"`, `aria-current="page"` | - Chỉ các cấp cha mới nhận Focus khi nhấn `Tab`.<br>- Có thẻ `<nav aria-label="Breadcrumb">` và mục cuối cùng có `aria-current="page"`. | `Not Run` |
