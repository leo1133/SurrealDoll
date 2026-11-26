# 📋 BỘ CHECKLIST KIỂM THỬ TOÀN DIỆN HỆ THỐNG MASTER ADMIN (ADMIN CHECKLIST) - SURREALDOLL

> **Phân hệ áp dụng:** Master Admin Web (`AA000`)  
> **Người lập:** Antigravity QA Agent / NgaDTP  
> **Phiên bản tài liệu:** v1.0  
> **Trạng thái:** Đã đồng bộ lên Google Sheets  
> **Link Google Sheets:** [Checklist_admin (gid=1138378553)](https://docs.google.com/spreadsheets/d/1nAJU06so8kY5QwVfScC9hEbxY6nVznexwi9C6X8vK6k/edit?gid=1138378553#gid=1138378553)

---

## 📌 MỤC LỤC TỔNG QUAN

1. [Phần 1: Xác thực & Tài khoản Quản trị (`AA`, `AB`)](#phần-1-xác-thực--tài-khoản-quản-trị)
2. [Phần 2: Quản lý Quản trị viên hệ thống & RBAC (`AC`)](#phần-2-quản-lý-quản-trị-viên-hệ-thống--rbac)
3. [Phần 3: Quản lý Agency (`AD`)](#phần-3-quản-lý-agency)
4. [Phần 4: Quản lý Người dùng / Liver & Viewer (`AE`)](#phần-4-quản-lý-người-dùng--liver--viewer)
5. [Phần 5: Quản lý Quà tặng & Vật phẩm ảo (`AF`)](#phần-5-quản-lý-quà-tặng--vật-phẩm-ảo)
6. [Phần 6: Giám sát & Quản lý Livestream Thời gian thực (`AG`)](#phần-6-giám-sát--quản-lý-livestream-thời-gian-thực)
7. [Phần 7: Quản lý Thông báo & Nội dung Truyền thông (`AH`)](#phần-7-quản-lý-thông-báo--nội-dung-truyền-thông)
8. [Phần 8: Quản lý Báo cáo Vi phạm & Khiếu nại (`AI`)](#phần-8-quản-lý-báo-cáo-vi-phạm--khiếu-nại)
9. [Phần 9: Quản lý Âm thanh & Nhạc nền Livestream (`AJ`)](#phần-9-quản-lý-âm-thanh--nhạc-nền-livestream)
10. [Phần 10: Quản lý Hình nền Livestream & Mini Garden (`AK`)](#phần-10-quản-lý-hình-nền-livestream--mini-garden)
11. [Phần 11: Quản lý Karaoke & Bản quyền Âm nhạc (`AL`)](#phần-11-quản-lý-karaoke--bản-quyền-âm-nhạc)
12. [Phần 12: Quản lý Bài đăng Mạng xã hội (`AM`)](#phần-12-quản-lý-bài-đăng-mạng-xã-hội)
13. [Phần 13: Quản lý Model Avatar 2D/3D & Phụ kiện (`AP`)](#phần-13-quản-lý-model-avatar-2d3d--phụ-kiện)
14. [Phần 14: Quản lý Vòng quay Gacha & Tỷ lệ May rủi (`AQ`)](#phần-14-quản-lý-vòng-quay-gacha--tỷ-lệ-may-rủi)
15. [Phần 15: Quản lý Doanh thu, Đổi thưởng & Tài chính (`AS`)](#phần-15-quản-lý-doanh-thu-đổi-thưởng--tài-chính)
16. [Phần 16: Giám sát Tin nhắn & Lọc Bình luận (`AX`, `AY`)](#phần-16-giám-sát-tin-nhắn--lọc-bình-luận)
17. [Phần 17: Quản trị Vòng đời Tài khoản (`K2022`)](#phần-17-quản-trị-vòng-đời-tài-khoản)

---


## Xác thực & Tài khoản Quản trị

### 1. **[ADM-AUTH-01]** - Đăng nhập Master Admin thành công (`AA000`)
- **Điều kiện tiên quyết:** Đã có tài khoản Master Admin hợp lệ trong hệ thống
- **Các bước thực hiện:** 1. Truy cập trang đăng nhập Admin (/sign-in)<br>2. Nhập email và mật khẩu chính xác<br>3. Bấm nút [ログイン / Đăng nhập]
- **Kết quả mong đợi:** Đăng nhập thành công, lưu session token vào Cookie HttpOnly/Secure, điều hướng vào màn hình Dashboard chính.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AA000`

### 2. **[ADM-AUTH-02]** - Đăng nhập thất bại khi sai thông tin (`AA000`)
- **Điều kiện tiên quyết:** Tại trang đăng nhập Admin
- **Các bước thực hiện:** 1. Nhập sai email hoặc mật khẩu<br>2. Bấm [ログイン]
- **Kết quả mong đợi:** Hiển thị thông báo lỗi MSG chính xác, không tạo phiên đăng nhập, giữ nguyên dữ liệu email đã nhập.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AA000`

### 3. **[ADM-AUTH-03]** - Bảo mật Token & Cookie HttpOnly/Secure (`AA001`)
- **Điều kiện tiên quyết:** Đã đăng nhập thành công
- **Các bước thực hiện:** 1. Mở DevTools > Application > Cookies<br>2. Kiểm tra cờ HttpOnly, Secure và SameSite của access token cookie
- **Kết quả mong đợi:** Cookie được gắn đầy đủ HttpOnly=true, Secure=true, SameSite=Strict/Lax chống tấn công XSS/CSRF.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AA001`

### 4. **[ADM-AUTH-04]** - Đổi mật khẩu trong phiên làm việc (`AA003`)
- **Điều kiện tiên quyết:** Admin đang đăng nhập vào hệ thống
- **Các bước thực hiện:** 1. Click avatar admin ở góc dưới sidebar<br>2. Chọn [パスワード変更]<br>3. Nhập mật khẩu cũ, mật khẩu mới hợp lệ, xác nhận lại<br>4. Bấm [保存]
- **Kết quả mong đợi:** Hệ thống cập nhật mật khẩu mới thành công, hiển thị thông báo thành công và ghi nhận audit log.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AA003`

### 5. **[ADM-AUTH-05]** - Yêu cầu cấp lại mật khẩu qua Email (`AB000`)
- **Điều kiện tiên quyết:** Tại màn hình đăng nhập
- **Các bước thực hiện:** 1. Bấm liên kết [パスワードをお忘れの方]<br>2. Nhập địa chỉ email quản trị viên đã đăng ký<br>3. Bấm gửi yêu cầu
- **Kết quả mong đợi:** Điều hướng sang màn hình hoàn tất AB000-2, hệ thống gửi email kèm link reset token có thời hạn 30 phút.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AB000`

### 6. **[ADM-AUTH-06]** - Đặt lại mật khẩu mới qua link reset (`AB000`)
- **Điều kiện tiên quyết:** Nhận được email khôi phục mật khẩu
- **Các bước thực hiện:** 1. Click link trong email để mở màn hình đặt lại mật khẩu<br>2. Nhập mật khẩu mới thỏa mãn độ mạnh<br>3. Bấm xác nhận
- **Kết quả mong đợi:** Cập nhật mật khẩu mới thành công, vô hiệu hóa link cũ, chuyển hướng về trang đăng nhập AA000.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AB000`

### 7. **[ADM-AUTH-07]** - Đăng xuất khỏi hệ thống (`AA002`)
- **Điều kiện tiên quyết:** Admin đang trong phiên đăng nhập
- **Các bước thực hiện:** 1. Click avatar/tên admin tại sidebar<br>2. Bấm [ログアウト / Đăng xuất]
- **Kết quả mong đợi:** Hủy token cookie, xóa cache phiên làm việc, điều hướng an toàn về trang đăng nhập.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AA002`


## Quản lý Quản trị viên & RBAC

### 8. **[ADM-AC-01]** - Tìm kiếm & Lọc danh sách Quản trị viên (`AC100`)
- **Điều kiện tiên quyết:** Tài khoản Master Admin đăng nhập thành công
- **Các bước thực hiện:** 1. Truy cập menu [管理者管理 > 管理者一覧]<br>2. Nhập từ khóa tìm kiếm (tên, email), chọn trạng thái<br>3. Bấm [検索]
- **Kết quả mong đợi:** Bảng danh sách hiển thị đúng các bản ghi khớp với điều kiện lọc, đầy đủ các cột thông tin.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AC100`

### 9. **[ADM-AC-02]** - Phân trang danh sách Quản trị viên (`AC100`)
- **Điều kiện tiên quyết:** Danh sách có nhiều hơn số bản ghi trên 1 trang
- **Các bước thực hiện:** 1. Thao tác chuyển trang (Next, Prev, số trang cụ thể)<br>2. Đổi số lượng hiển thị (10, 20, 50)
- **Kết quả mong đợi:** Danh sách tải đúng số lượng bản ghi tương ứng, thứ tự sắp xếp được bảo toàn.
- **Độ ưu tiên:** `Medium` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AC100`

### 10. **[ADM-AC-03]** - Đăng ký tạo mới Quản trị viên (`AC200`)
- **Điều kiện tiên quyết:** Tại màn hình AC100
- **Các bước thực hiện:** 1. Bấm nút [新規登録]<br>2. Nhập đầy đủ thông tin: họ tên, email, vai trò (Admin/Operator)<br>3. Bấm [登録]
- **Kết quả mong đợi:** Tạo tài khoản quản trị mới thành công, gửi email kích hoạt/mật khẩu tạm, thêm bản ghi vào AC100.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AC200`

### 11. **[ADM-AC-04]** - Cập nhật thông tin Quản trị viên (`AC300`)
- **Điều kiện tiên quyết:** Tại danh sách AC100
- **Các bước thực hiện:** 1. Click nút chỉnh sửa bản ghi quản trị viên<br>2. Thay đổi quyền hạn hoặc chuyển trạng thái sang Vô hiệu hóa (Inactive)<br>3. Bấm [保存]
- **Kết quả mong đợi:** Cập nhật thành công thông tin vào DB; tài khoản bị Inactive không thể đăng nhập vào hệ thống.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AC300`

### 12. **[ADM-AC-05]** - Chặn xóa tài khoản Super Admin tối cao (`AC300`)
- **Điều kiện tiên quyết:** Tại danh sách AC100
- **Các bước thực hiện:** 1. Tìm bản ghi có vai trò Super Admin<br>2. Quan sát nút hành động hoặc cố ý gửi request xóa
- **Kết quả mong đợi:** Hệ thống ẩn/disable nút xóa hoặc hiển thị lỗi: "スーパー管理者を削除することはできません。".
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AC300`

### 13. **[ADM-AC-06]** - Cấu hình ma trận phân quyền RBAC (`AC400`)
- **Điều kiện tiên quyết:** Quyền Master Admin
- **Các bước thực hiện:** 1. Truy cập màn hình cấu hình quyền hạn AC400<br>2. Bật/tắt các quyền truy cập module cho nhóm vai trò Operator<br>3. Lưu cấu hình
- **Kết quả mong đợi:** Phân quyền được áp dụng tức thì, tài khoản thuộc vai trò đó chỉ xem/thao tác đúng module được cấp.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AC400`


## Quản lý Agency

### 14. **[ADM-AD-01]** - Tìm kiếm & Lọc danh sách Agency (`AD100`)
- **Điều kiện tiên quyết:** Đăng nhập quyền Master Admin
- **Các bước thực hiện:** 1. Truy cập [事務所管理 > 事務所一覧]<br>2. Nhập từ khóa tên Agency, lọc theo trạng thái Đang hoạt động / Ngưng hoạt động<br>3. Bấm [検索]
- **Kết quả mong đợi:** Hiển thị danh sách Agency tương ứng kèm mã, tên người đại diện, số lượng Streamer trực thuộc.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AD100`

### 15. **[ADM-AD-02]** - Xuất danh sách Agency ra file CSV (`AD100`)
- **Điều kiện tiên quyết:** Tại màn hình AD100 có dữ liệu
- **Các bước thực hiện:** 1. Thiết lập bộ lọc<br>2. Bấm nút [CSV出力]
- **Kết quả mong đợi:** Tải xuống file CSV đúng định dạng UTF-8 with BOM, dữ liệu khớp 100% với danh sách đang hiển thị.
- **Độ ưu tiên:** `Medium` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AD100`

### 16. **[ADM-AD-03]** - Đăng ký tạo mới Agency (`AD200`)
- **Điều kiện tiên quyết:** Tại AD100, bấm [新規登録]
- **Các bước thực hiện:** 1. Nhập mã Agency, tên pháp lý, tên đại diện, email liên hệ, số điện thoại<br>2. Thiết lập tỷ lệ hoa hồng chia sẻ (% revenue share)<br>3. Bấm [登録]
- **Kết quả mong đợi:** Tạo Agency thành công, sinh tài khoản đăng nhập Agency Portal mặc định và hiển thị trên AD100.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AD200`

### 17. **[ADM-AD-04]** - Chi tiết & Chỉnh sửa thông tin Agency (`AD301`)
- **Điều kiện tiên quyết:** Tại AD100, click dòng Agency
- **Các bước thực hiện:** 1. Điều hướng vào AD301<br>2. Chỉnh sửa thông tin liên hệ, tài khoản ngân hàng thụ hưởng<br>3. Bấm [保存]
- **Kết quả mong đợi:** Dữ liệu được cập nhật thành công vào cơ sở dữ liệu, hiển thị thông báo lưu thành công.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AD301`

### 18. **[ADM-AD-05]** - Chuyển trạng thái Agency Ngưng hoạt động (`AD301`)
- **Điều kiện tiên quyết:** Tại AD301 của Agency đang Active
- **Các bước thực hiện:** 1. Đổi trạng thái sang [停止 / Inactive]<br>2. Bấm xác nhận lưu
- **Kết quả mong đợi:** Toàn bộ tài khoản quản trị của Agency đó bị chặn đăng nhập; App mobile chặn người dùng nộp đơn vào Agency này.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AD301`

### 19. **[ADM-AD-06]** - Xem danh sách Streamer trực thuộc Agency (`AD302`)
- **Điều kiện tiên quyết:** Tại AD100, click vào số lượng Liver cột [ライバー数]
- **Các bước thực hiện:** 1. Điều hướng sang màn hình AD302<br>2. Quan sát danh sách các Streamer đang thuộc quyền quản lý của Agency
- **Kết quả mong đợi:** Hiển thị danh sách streamer của đúng Agency đó kèm User ID, Nickname, ngày ký hợp đồng, trạng thái.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AD302`

### 20. **[ADM-AD-07]** - Phân tích doanh thu & Đối soát Agency (`AD303`)
- **Điều kiện tiên quyết:** Tại AD301, chuyển sang tab Doanh thu AD303
- **Các bước thực hiện:** 1. Chọn kỳ đối soát (Tháng/Năm)<br>2. Xem bảng tổng hợp doanh thu quà tặng, hoa hồng Agency, số tiền thanh toán
- **Kết quả mong đợi:** Số liệu doanh thu tổng hợp chính xác theo công thức chia sẻ, hỗ trợ xuất CSV đối soát kế toán.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AD303`


## Quản lý Người dùng

### 21. **[ADM-AE-01]** - Danh sách & Tìm kiếm Người dùng (`AE100`)
- **Điều kiện tiên quyết:** Đăng nhập quyền Admin
- **Các bước thực hiện:** 1. Truy cập [利用者管理 > 利用者一覧]<br>2. Tìm kiếm theo User ID, Tên người dùng, loại tài khoản (Viewer/Liver), trạng thái
- **Kết quả mong đợi:** Hiển thị danh sách người dùng đầy đủ thông tin: ID, Avatar, Nickname, Cấp bậc, Ngày đăng ký, Trạng thái.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AE100`

### 22. **[ADM-AE-02]** - Xem chi tiết Hồ sơ người dùng (`AE200`)
- **Điều kiện tiên quyết:** Tại AE100, click vào một User
- **Các bước thực hiện:** 1. Điều hướng vào màn hình AE200<br>2. Quan sát thông tin cá nhân, tiểu sử, số follower, số kim cương/coin
- **Kết quả mong đợi:** Hiển thị toàn diện hồ sơ người dùng, phân loại rõ Liver tự do hay thuộc Agency.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AE200`

### 23. **[ADM-AE-03]** - Khóa / Mở khóa tài khoản Người dùng (`AE200`)
- **Điều kiện tiên quyết:** Tại màn hình chi tiết AE200
- **Các bước thực hiện:** 1. Chọn hành động [アカウント停止 / Khóa tài khoản]<br>2. Nhập lý do kỷ luật và thời hạn<br>3. Bấm xác nhận
- **Kết quả mong đợi:** Tài khoản bị khóa ngay lập tức, ngắt phiên làm việc trên App; người dùng không thể đăng nhập.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AE200`

### 24. **[ADM-AE-04]** - Kiểm tra Vật phẩm & Tài sản sở hữu (`AE300`)
- **Điều kiện tiên quyết:** Tại AE200, chọn tab [所持アイテム]
- **Các bước thực hiện:** 1. Quan sát danh sách vật phẩm quà tặng, vé gacha, trang phục avatar trong kho của người dùng
- **Kết quả mong đợi:** Hiển thị chính xác số lượng từng loại vật phẩm, hạn sử dụng (nếu có).
- **Độ ưu tiên:** `Medium` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AE300`

### 25. **[ADM-AE-05]** - Tra cứu Lịch sử hoạt động (`AE400`)
- **Điều kiện tiên quyết:** Tại AE200, chọn tab [利用履歴]
- **Các bước thực hiện:** 1. Tra cứu lịch sử phiên live đã phát, các phòng live đã xem, lịch sử tặng quà
- **Kết quả mong đợi:** Bảng dữ liệu hiển thị rõ thời gian, hành động, ID đối tượng tương tác.
- **Độ ưu tiên:** `Medium` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AE400`

### 26. **[ADM-AE-06]** - Tra cứu Lịch sử Nạp tiền & Giao dịch (`AE500`)
- **Điều kiện tiên quyết:** Tại AE200, chọn tab [課金情報]
- **Các bước thực hiện:** 1. Xem lịch sử nạp coin qua In-App Purchase (Apple/Google) hoặc Web Checkout<br>2. Kiểm tra mã giao dịch, số tiền JPY, số coin nhận
- **Kết quả mong đợi:** Hiển thị đầy đủ lịch sử giao dịch nạp tiền kèm trạng thái Thành công / Thất bại / Hoàn tiền.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AE500`

### 27. **[ADM-AE-07]** - Quản lý Thông tin Thanh toán (`AE600`)
- **Điều kiện tiên quyết:** Tại AE200, chọn tab [決済情報]
- **Các bước thực hiện:** 1. Kiểm tra phương thức thanh toán thẻ tín dụng đã lưu trữ (được mã hóa/tokenized qua cổng thanh toán)
- **Kết quả mong đợi:** Hiển thị an toàn 4 số cuối thẻ, loại thẻ, không để lộ thông tin nhạy cảm.
- **Độ ưu tiên:** `Medium` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AE600`

### 28. **[ADM-AE-08]** - Kiểm duyệt Xác thực Danh tính eKYC & OCR (`AE700`)
- **Điều kiện tiên quyết:** Liver gửi yêu cầu xác thực eKYC
- **Các bước thực hiện:** 1. Truy cập tab [認証 / eKYC] tại AE700<br>2. Đối chiếu ảnh chụp giấy tờ (CCCD/Bằng lái) và kết quả OCR<br>3. Bấm [承認 / Phê duyệt] hoặc [却下 / Từ chối]
- **Kết quả mong đợi:** Cập nhật trạng thái xác thực của Liver sang Đã xác minh; cho phép Liver đủ điều kiện đổi thưởng.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AE700`

### 29. **[ADM-AE-09]** - Phân tích Doanh thu cá nhân từng Liver (`AE800`)
- **Điều kiện tiên quyết:** Tại AE200, chọn tab [売上 / AE800]
- **Các bước thực hiện:** 1. Chọn khoảng thời gian (Ngày/Tuần/Tháng)<br>2. Xem biểu đồ doanh thu chi tiết từ quà tặng, vé xem live, Monthly Pass
- **Kết quả mong đợi:** Hiển thị đầy đủ chỉ số doanh thu, tỷ lệ chia sẻ, số tiền thực nhận và hỗ trợ xuất CSV.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AE800`


## Quản lý Quà tặng & Vật phẩm

### 30. **[ADM-AF-01]** - Danh sách & Bộ lọc Quà tặng (`AF100`)
- **Điều kiện tiên quyết:** Đăng nhập quyền Admin
- **Các bước thực hiện:** 1. Truy cập [商品管理 > ギフト管理 > ギフト一覧]<br>2. Tìm kiếm theo tên quà, lọc theo danh mục, trạng thái hiển thị
- **Kết quả mong đợi:** Hiển thị danh sách quà tặng kèm hình ảnh thumbnail, giá coin/point, danh mục, trạng thái hoạt động.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AF100`

### 31. **[ADM-AF-02]** - Tạo mới Quà tặng kèm hiệu ứng động (`AF200`)
- **Điều kiện tiên quyết:** Tại AF100, bấm [新規登録]
- **Các bước thực hiện:** 1. Nhập tên quà tặng, chọn danh mục, đơn giá<br>2. Tải lên file ảnh icon và file animation (SVGA/Lottie)<br>3. Tải lên âm thanh hiệu ứng (nếu có)<br>4. Bấm [登録]
- **Kết quả mong đợi:** Tạo quà tặng thành công, file animation được lưu trữ trên S3/CDN và hiển thị trong phòng live của App.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AF200`

### 32. **[ADM-AF-03]** - Chỉnh sửa Quà tặng & Tắt/Bật hiển thị (`AF300`)
- **Điều kiện tiên quyết:** Tại AF100, chọn chỉnh sửa một món quà
- **Các bước thực hiện:** 1. Cập nhật đơn giá hoặc đổi trạng thái hiển thị sang Ẩn<br>2. Bấm [保存]
- **Kết quả mong đợi:** Dữ liệu quà tặng được cập nhật ngay lập tức; quà bị ẩn sẽ không hiển thị trên khay quà của Viewer.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AF300`

### 33. **[ADM-AF-04]** - Xóa Quà tặng (`AF300`)
- **Điều kiện tiên quyết:** Tại AF300 của món quà chưa phát sinh giao dịch
- **Các bước thực hiện:** 1. Bấm nút [削除]<br>2. Xác nhận popup cảnh báo xóa
- **Kết quả mong đợi:** Quà tặng được xóa an toàn (Soft delete) khỏi hệ thống, không làm lỗi dữ liệu lịch sử quà tặng cũ.
- **Độ ưu tiên:** `Medium` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AF300`

### 34. **[ADM-AF-05]** - Quản lý Danh mục phân loại Quà tặng (`AF400`)
- **Điều kiện tiên quyết:** Truy cập [ギフトカテゴリー管理]
- **Các bước thực hiện:** 1. Thêm mới danh mục quà (Ví dụ: Sự kiện Valentine, Quà cao cấp)<br>2. Sắp xếp thứ tự ưu tiên hiển thị trên tab quà của App<br>3. Lưu
- **Kết quả mong đợi:** Cập nhật thành công danh mục quà tặng, thứ tự hiển thị trên App thay đổi tương ứng.
- **Độ ưu tiên:** `Medium` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AF400`

### 35. **[ADM-AF-06]** - Cấu hình Quà tặng Cao cấp toàn màn hình (`AF500`)
- **Điều kiện tiên quyết:** Tại màn hình cấu hình quà cao cấp AF500
- **Các bước thực hiện:** 1. Cài đặt các hiệu ứng toàn màn hình (Full-screen Overlay Banner, chạy chữ chúc mừng toàn phòng)<br>2. Bấm [保存]
- **Kết quả mong đợi:** Khi viewer tặng món quà này, toàn bộ người xem trong phòng live đều thấy hiệu ứng đặc biệt.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AF500`


## Giám sát & Quản lý Livestream

### 36. **[ADM-AG-01]** - Giám sát danh sách phòng Live đang phát sóng (`AG100`)
- **Điều kiện tiên quyết:** Hệ thống đang có các phiên livestream trực tiếp
- **Các bước thực hiện:** 1. Truy cập [配信管理 > 配信一覧]<br>2. Quan sát danh sách các phòng đang LIVE: Streamer ID, Tiêu đề, Thể loại (Thường, 2Shot, OBS, Karaoke), Số lượng Viewer
- **Kết quả mong đợi:** Danh sách cập nhật trạng thái thời gian thực, hiển thị đầy đủ thông số phòng phát sóng.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AG100`

### 37. **[ADM-AG-02]** - Xem trực tiếp luồng Live từ Admin (`AG200`)
- **Điều kiện tiên quyết:** Tại AG100, click vào một phòng live đang hoạt động
- **Các bước thực hiện:** 1. Điều hướng sang AG200<br>2. Xem video phát sóng và nghe âm thanh thời gian thực của Streamer
- **Kết quả mong đợi:** Video tải mượt mà không có độ trễ lớn; Admin quan sát rõ hình ảnh Live2D và âm thanh micro.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AG200`

### 38. **[ADM-AG-03]** - Quản lý Danh sách Cấm phát sóng (Stream Ban) (`AG300`)
- **Điều kiện tiên quyết:** Tại menu [配信管理 > BAN一覧]
- **Các bước thực hiện:** 1. Tra cứu danh sách các Streamer đang bị cấm mở phòng live<br>2. Thực hiện gỡ lệnh cấm (Unban) hoặc kéo dài thời hạn
- **Kết quả mong đợi:** Cập nhật trạng thái cấm phát sóng thành công, đồng bộ ngay lập tức sang ứng dụng di động.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AG300`

### 39. **[ADM-AG-04]** - Cưỡng chế Dừng Livestream khẩn cấp (`AG400`)
- **Điều kiện tiên quyết:** Tại phòng live đang phát hiện vi phạm thuần phong mỹ tục hoặc bản quyền (AG200/AG400)
- **Các bước thực hiện:** 1. Bấm nút [強制終了 / Dừng khẩn cấp]<br>2. Nhập lý do cưỡng chế<br>3. Bấm xác nhận
- **Kết quả mong đợi:** Phòng livestream lập tức bị ngắt kết nối; Streamer và Viewer nhận thông báo MSG61: "配信は管理者より強制終了されました".
- **Độ ưu tiên:** `Critical` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AG400`

### 40. **[ADM-AG-05]** - Danh sách & Xem lại kho lưu trữ Live Archive (`AG500`)
- **Điều kiện tiên quyết:** Truy cập [配信管理 > 配信アーカイブ]
- **Các bước thực hiện:** 1. Tra cứu lịch sử các phiên live đã kết thúc<br>2. Click xem lại bản ghi video lưu trữ (Archive Player)
- **Kết quả mong đợi:** Trình phát phát lại toàn bộ nội dung livestream đã ghi nhận kèm các chỉ số thống kê tổng kết.
- **Độ ưu tiên:** `Medium` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AG500`


## Quản lý Thông báo & Nội dung

### 41. **[ADM-AH-01]** - Danh sách & Bộ lọc Thông báo (`AH100`)
- **Điều kiện tiên quyết:** Đăng nhập quyền Admin
- **Các bước thực hiện:** 1. Truy cập [お知らせ管理 > お知らせ一覧]<br>2. Lọc theo danh mục (Bảo trì, Sự kiện, Cập nhật), trạng thái (Đã phát, Chờ phát)
- **Kết quả mong đợi:** Danh sách hiển thị đúng tiêu đề thông báo, ngày phát hành, phạm vi đối tượng nhận.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AH100`

### 42. **[ADM-AH-02]** - Tạo mới Thông báo & Hẹn giờ phát hành (`AH200`)
- **Điều kiện tiên quyết:** Tại AH100, bấm [新規登録]
- **Các bước thực hiện:** 1. Nhập tiêu đề, nội dung thông báo (Rich Text/HTML)<br>2. Tải lên ảnh banner đính kèm<br>3. Cài đặt thời gian hẹn giờ phát hành<br>4. Chọn đối tượng (Toàn bộ, Chỉ Viewer, Chỉ Liver)<br>5. Bấm [登録]
- **Kết quả mong đợi:** Tạo thông báo thành công; hệ thống tự động xuất bản khi đến giờ hẹn và gửi thông báo tới App.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AH200`

### 43. **[ADM-AH-03]** - Chỉnh sửa nội dung Thông báo (`AH300`)
- **Điều kiện tiên quyết:** Tại AH100, chọn chỉnh sửa thông báo
- **Các bước thực hiện:** 1. Thay đổi nội dung text hoặc đổi ảnh banner<br>2. Bấm [保存]
- **Kết quả mong đợi:** Thông báo được cập nhật nội dung mới; người dùng trên App nhìn thấy dữ liệu mới khi mở thông báo.
- **Độ ưu tiên:** `Medium` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AH300`

### 44. **[ADM-AH-04]** - Xem trước Giao diện Thông báo trên App/Web (`AH301`)
- **Điều kiện tiên quyết:** Tại màn hình tạo/sửa thông báo
- **Các bước thực hiện:** 1. Bấm nút [プレビュー / Xem trước]
- **Kết quả mong đợi:** Mở modal AH301 mô phỏng chính xác khung hình hiển thị của màn hình điện thoại (Mobile Preview).
- **Độ ưu tiên:** `Medium` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AH301`

### 45. **[ADM-AH-05]** - Gửi Tin nhắn Hệ thống / Push Notification (`AH400`)
- **Điều kiện tiên quyết:** Truy cập [お知らせ管理 > メッセージ管理 / AH400]
- **Các bước thực hiện:** 1. Soạn tin nhắn thông báo đẩy (Push Title, Message Body, Deep-link URL)<br>2. Chọn phân khúc người dùng mục tiêu<br>3. Bấm gửi
- **Kết quả mong đợi:** Tin nhắn được đẩy tức thì qua Firebase Cloud Messaging (FCM/APNs) đến thiết bị của người dùng.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AH400`


## Quản lý Báo cáo Vi phạm

### 46. **[ADM-AI-01]** - Danh sách Báo cáo Vi phạm từ Người dùng (`AI100`)
- **Điều kiện tiên quyết:** Đăng nhập quyền Admin
- **Các bước thực hiện:** 1. Truy cập [通報管理 > 通報一覧]<br>2. Lọc theo trạng thái (Chờ xử lý, Đang xử lý, Đã hoàn tất), loại vi phạm (Livestream, Chat, Bài đăng)
- **Kết quả mong đợi:** Bảng danh sách hiển thị đầy đủ: ID tố cáo, Người báo cáo, Người bị báo cáo, Lý do, Thời gian gửi.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AI100`

### 47. **[ADM-AI-02]** - Xem chi tiết bằng chứng & Trích xuất vi phạm (`AI200`)
- **Điều kiện tiên quyết:** Tại AI100, click vào một ca báo cáo
- **Các bước thực hiện:** 1. Điều hướng sang AI200<br>2. Xem chi tiết nội dung tố cáo, ảnh chụp màn hình bằng chứng, trích xuất đoạn chat/video thời điểm đó
- **Kết quả mong đợi:** Admin nắm rõ đầy đủ ngữ cảnh vi phạm để đưa ra phán quyết chính xác.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AI200`

### 48. **[ADM-AI-03]** - Xử lý chế tài vi phạm & Đóng ca tố cáo (`AI200`)
- **Điều kiện tiên quyết:** Tại AI200 sau khi xem xét bằng chứng
- **Các bước thực hiện:** 1. Chọn quyết định xử lý: Bác bỏ / Cảnh cáo / Cấm phát live / Khóa tài khoản<br>2. Nhập ghi chú phản hồi nội bộ<br>3. Bấm [完了]
- **Kết quả mong đợi:** Hệ thống áp dụng hình thức kỷ luật ngay lập tức; ca tố cáo chuyển sang trạng thái Đã xử lý (Resolved).
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AI200`


## Quản lý Âm thanh & BGM

### 49. **[ADM-AJ-01]** - Danh sách Nhạc nền BGM phòng Live (`AJ100`)
- **Điều kiện tiên quyết:** Đăng nhập quyền Admin
- **Các bước thực hiện:** 1. Truy cập [配信管理 > BGM管理 > BGM一覧]<br>2. Tra cứu theo tên bài, tác giả, thể loại nhạc
- **Kết quả mong đợi:** Hiển thị danh sách các bản nhạc nền kèm nút nghe thử (Audio Player) trực tiếp trên Web Admin.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AJ100`

### 50. **[ADM-AJ-02]** - Tải lên & Tạo mới bản nhạc nền BGM (`AJ200`)
- **Điều kiện tiên quyết:** Tại AJ100, bấm [新規登録]
- **Các bước thực hiện:** 1. Nhập tên bản nhạc, tác giả, thể loại (Vui vẻ, Chill, Sôi động)<br>2. Tải lên file âm thanh chuẩn<br>3. Bấm [登録]
- **Kết quả mong đợi:** Upload nhạc nền thành công lên hệ thống lưu trữ; bản nhạc lập tức xuất hiện trong danh sách BGM của Streamer.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AJ200`

### 51. **[ADM-AJ-03]** - Chỉnh sửa thông tin & Xóa BGM (`AJ300`)
- **Điều kiện tiên quyết:** Tại AJ100, chọn chỉnh sửa một bản BGM
- **Các bước thực hiện:** 1. Đổi tên bài hát hoặc cập nhật thể loại<br>2. Bấm lưu hoặc bấm xóa bản ghi
- **Kết quả mong đợi:** Dữ liệu được cập nhật hoặc xóa an toàn, không gây crash ứng dụng nếu streamer đang mở danh sách BGM.
- **Độ ưu tiên:** `Medium` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AJ300`

### 52. **[ADM-AJ-04]** - Bộ chuyển đổi định dạng âm thanh MP3/WAV (`AJ400`)
- **Điều kiện tiên quyết:** Tại màn hình công cụ AJ400
- **Các bước thực hiện:** 1. Tải lên file âm thanh gốc WAV chất lượng cao<br>2. Chọn định dạng đầu ra MP3/AAC tối ưu bitrate streaming<br>3. Thực hiện chuyển đổi
- **Kết quả mong đợi:** File âm thanh sau khi convert đảm bảo chất lượng sắc nét và dung lượng tối ưu hóa đường truyền.
- **Độ ưu tiên:** `Low` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AJ400`


## Quản lý Background & Mini Garden

### 53. **[ADM-AK-01]** - Danh sách Hình nền minh họa phòng Live (`AK201`)
- **Điều kiện tiên quyết:** Đăng nhập quyền Admin
- **Các bước thực hiện:** 1. Truy cập [背景管理 > イラスト背景一覧]<br>2. Xem danh sách background kèm ảnh thumbnail preview
- **Kết quả mong đợi:** Bảng danh sách hiển thị đầy đủ tên hình nền, chủ đề (Phòng ngủ, Sân khấu, Quán cafe...), trạng thái hoạt động.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AK201`

### 54. **[ADM-AK-02]** - Tạo mới & Tải lên file ảnh Background Live (`AK202`)
- **Điều kiện tiên quyết:** Tại AK201, bấm [新規登録]
- **Các bước thực hiện:** 1. Nhập tên background, chọn chủ đề<br>2. Tải lên file ảnh tỷ lệ 9:16 độ phân giải cao<br>3. Bấm [登録]
- **Kết quả mong đợi:** Background được tải lên thành công, sẵn sàng cho Streamer chọn làm hình nền phòng livestream.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AK202`

### 55. **[ADM-AK-03]** - Chỉnh sửa & Xóa Background Live (`AK203`)
- **Điều kiện tiên quyết:** Tại AK203
- **Các bước thực hiện:** 1. Cập nhật thông tin hoặc đổi trạng thái sang Ẩn<br>2. Bấm lưu
- **Kết quả mong đợi:** Cập nhật thành công; background bị ẩn sẽ không hiển thị trên màn hình Setup Background của App.
- **Độ ưu tiên:** `Medium` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AK203`

### 56. **[ADM-AK-04]** - Quản lý Background cho Mini Garden (`AK301-AK303`)
- **Điều kiện tiên quyết:** Truy cập [背景管理 > ミニガーデン背景一覧 / AK301]
- **Các bước thực hiện:** 1. Quản lý danh sách, tạo mới (AK302) và chỉnh sửa (AK303) các mẫu hình nền khu vườn ảo Mini Garden của người dùng
- **Kết quả mong đợi:** Người dùng có thể trang trí không gian riêng của mình bằng các mẫu background đã được Admin duyệt.
- **Độ ưu tiên:** `Medium` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AK301-AK303`


## Quản lý Karaoke & Bản quyền

### 57. **[ADM-AL-01]** - Danh sách Bài hát Karaoke (`AL100`)
- **Điều kiện tiên quyết:** Đăng nhập quyền Admin
- **Các bước thực hiện:** 1. Truy cập [カラオケ管理 > カラオケ一覧]<br>2. Tìm kiếm theo tên bài hát, ca sĩ, nhạc sĩ, mã số bản quyền
- **Kết quả mong đợi:** Hiển thị danh sách ca khúc karaoke kèm mã JASRAC/NEXTONE, thời lượng, trạng thái kích hoạt.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AL100`

### 58. **[ADM-AL-02]** - Upload dữ liệu Karaoke hàng loạt (`AL101`)
- **Điều kiện tiên quyết:** Tại AL101
- **Các bước thực hiện:** 1. Tải lên file nén hoặc file danh sách CSV chứa beat nhạc và file phụ đề lyric (.lrc)<br>2. Bấm Import
- **Kết quả mong đợi:** Hệ thống tự động phân giải dữ liệu, đồng bộ lyric chạy chữ theo nhịp beat và thêm vào kho Karaoke.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AL101`

### 59. **[ADM-AL-03]** - Tạo mới & Chỉnh sửa Bài hát Karaoke (`AL200-AL300`)
- **Điều kiện tiên quyết:** Tại AL200 / AL300
- **Các bước thực hiện:** 1. Nhập thông tin chi tiết bài hát, mã bản quyền<br>2. Tải lên file beat và chỉnh sửa thời gian hiển thị từng câu lyric<br>3. Bấm [保存]
- **Kết quả mong đợi:** Dữ liệu ca khúc được lưu hoàn chỉnh, hiển thị chữ chạy mượt mà khi Streamer phát karaoke trên App.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AL200-AL300`

### 60. **[ADM-AL-04]** - Tiếp nhận & Xử lý Yêu cầu bài hát (`AL400`)
- **Điều kiện tiên quyết:** Truy cập [カラオケリクエスト一覧 / AL400]
- **Các bước thực hiện:** 1. Xem danh sách các bài hát do người dùng đề xuất<br>2. Cập nhật trạng thái: Tiếp nhận / Đang sản xuất / Đã phát hành / Từ chối
- **Kết quả mong đợi:** Thông báo tiến độ bài hát được gửi phản hồi về cho người dùng đã gửi yêu cầu.
- **Độ ưu tiên:** `Medium` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AL400`

### 61. **[ADM-AL-05]** - Bảng xếp hạng Karaoke theo Thời kỳ & Theo Tháng (`AL501-AL502`)
- **Điều kiện tiên quyết:** Truy cập [カラオケランキング / AL501, AL502]
- **Các bước thực hiện:** 1. Xem thống kê các ca khúc có lượt hát nhiều nhất theo niên đại (Era) và theo tháng (Month)
- **Kết quả mong đợi:** Dữ liệu bảng xếp hạng được tổng hợp tự động, làm cơ sở hiển thị mục thịnh hành trên App.
- **Độ ưu tiên:** `Medium` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AL501-AL502`

### 62. **[ADM-AL-06]** - Xuất Báo cáo Bản quyền gửi JASRAC / NEXTONE (`AL600`)
- **Điều kiện tiên quyết:** Truy cập [JASRAC・NEXTONE利用楽曲の報告 / AL600]
- **Các bước thực hiện:** 1. Chọn kỳ báo cáo (Tháng/Quý)<br>2. Kiểm tra tổng hợp số lượt phát, thời lượng sử dụng của từng mã bài hát<br>3. Bấm [レポート出力]
- **Kết quả mong đợi:** Xuất báo cáo định dạng chuẩn CSV/Excel theo quy chuẩn của hiệp hội bản quyền JASRAC và NEXTONE Nhật Bản.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AL600`

### 63. **[ADM-AL-07]** - Đối soát ca khúc người dùng hát qua ACRCloud (`AL700`)
- **Điều kiện tiên quyết:** Truy cập [ユーザー利用曲目報告 / AL700]
- **Các bước thực hiện:** 1. Xem nhật ký nhận diện âm thanh tự động ACRCloud ghi nhận các ca khúc được phát trong phòng live<br>2. Thống kê nội dung trả phí
- **Kết quả mong đợi:** Báo cáo minh bạch, chính xác từng ca khúc thực tế được sử dụng, đảm bảo tuân thủ bản quyền.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AL700`


## Quản lý Bài đăng Mạng xã hội

### 64. **[ADM-AM-01]** - Danh sách & Kiểm duyệt Bài đăng Feed (`AM100-AM101`)
- **Điều kiện tiên quyết:** Đăng nhập quyền Admin
- **Các bước thực hiện:** 1. Truy cập [投稿管理 > 投稿一覧]<br>2. Tra cứu danh sách bài đăng cộng đồng trên App; lọc theo từ khóa, người đăng (AM101)
- **Kết quả mong đợi:** Hiển thị danh sách bài đăng kèm ảnh, video, lượt like, comment, thời gian đăng.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AM100-AM101`

### 65. **[ADM-AM-02]** - Xem chi tiết & Xóa bài đăng vi phạm (`AM200`)
- **Điều kiện tiên quyết:** Tại AM100, click vào một bài đăng
- **Các bước thực hiện:** 1. Mở màn hình AM200<br>2. Xem chi tiết toàn bộ nội dung và bình luận<br>3. Bấm nút [削除] nếu phát hiện vi phạm tiêu chuẩn cộng đồng
- **Kết quả mong đợi:** Bài đăng bị xóa lập tức khỏi hệ thống, không còn hiển thị trên Feed của người dùng App.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AM200`


## Quản lý Model Avatar 2D/3D

### 66. **[ADM-AP-01]** - Danh sách Model & Cấu hình độ phân giải (`AP000`)
- **Điều kiện tiên quyết:** Đăng nhập quyền Admin
- **Các bước thực hiện:** 1. Truy cập [モデル管理 > モデル一覧 / AP000]<br>2. Xem danh mục model nhân vật Live2D/3D và cấu hình tỷ lệ khung hình, độ phân giải render
- **Kết quả mong đợi:** Model hiển thị sắc nét, đảm bảo tương thích hiệu năng trên cả thiết bị cấu hình trung bình.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AP000`

### 67. **[ADM-AP-02]** - Quản lý Cấu trúc Model: Đầu, Thân & Phụ kiện (`AP100-AP400`)
- **Điều kiện tiên quyết:** Tại màn hình chi tiết AP100
- **Các bước thực hiện:** 1. Quản lý các bộ phận tóc, mắt, biểu cảm khuôn mặt (AP200)<br>2. Quản lý trang phục cơ thể (AP300)<br>3. Quản lý phụ kiện đi kèm (AP400: nón, kính, tai nghe...)
- **Kết quả mong đợi:** Hệ thống quản lý đầy đủ các layer bộ phận của avatar, phục vụ cơ chế tùy biến nhân vật trên App.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AP100-AP400`

### 67.1. **[ADM-AP-03]** - Cài Đặt Tham Số Tracking Model (CR: `AP213` + `AP330` + `AP405`)
- **Điều kiện tiên quyết:** Tại màn hình chi tiết từng bộ phận AP200 / AP300 / AP400, chọn tab [トラッキング設定]
- **Các bước thực hiện:**
  1. **AP213 (Face Tracking):** Cấu hình độ nhạy Eye Blink, Eye Tracking, khẩu hình miệng theo âm thanh (Mouth Audio Threshold), góc quay đầu tối đa (Head Angle X/Y/Z).
  2. **AP330 (Body Tracking):** Cấu hình biên độ nghiêng thân Body Angle Z, nhịp thở (Breathing cycle/depth), bật chống xuyên thấu trang phục (Clothing collision).
  3. **AP405 (Accessory Tracking):** Chọn layer mục tiêu gắn phụ kiện (Follow Target: Head/Body/Arm), cài đặt độ trễ vật lý (Physics Delay), đàn hồi (Elasticity) và trọng lực (Gravity).
  4. Thao tác lưu `[保存]` (kiểm tra Toast `CMMSG13: 保存しました。`), khôi phục mặc định `[デフォルトに戻す]`, và hủy bỏ thay đổi dở dang `[キャンセル]`.
- **Kết quả mong đợi:** Toàn bộ tham số được lưu chính xác vào DB Master JSONB; đồng bộ sang API User Mobile `/user-model-setting/model/{id}/parameters/`.
- **Độ ưu tiên:** `Critical` | **Trạng thái:** `Chờ thực thi R1` | **Ghi chú/Màn hình:** `AP213, AP330, AP405`
- **Kịch bản chi tiết:**
  - 📋 **UI Testcase (70 TCs):** [AP213_AP330_AP405_testcase.md](AP213_AP330_AP405_testcase.md)
  - 🔌 **API Testcase (25 TCs):** [../testcase_api/AP213_AP330_AP405_api.md](../testcase_api/AP213_AP330_AP405_api.md)
  - 🎯 **Task Backlog:** [SURREALDOLLS-15052](https://issoh.backlog.com/view/SURREALDOLLS-15052) (Testcase) & [SURREALDOLLS-15053](https://issoh.backlog.com/view/SURREALDOLLS-15053) (Test)


## Quản lý Gacha & Tỷ lệ May rủi

### 68. **[ADM-AQ-01]** - Quản lý Bể quay Gacha Avatar, Garden & BG (`AQ100, AQ400, AQ500`)
- **Điều kiện tiên quyết:** Đăng nhập quyền Admin
- **Các bước thực hiện:** 1. Truy cập [ガチャ管理]<br>2. Quản lý các sự kiện quay Gacha cho Avatar (AQ100), Mini Garden (AQ400), Background (AQ500)
- **Kết quả mong đợi:** Hiển thị danh sách các Banner gacha, thời gian bắt đầu và kết thúc sự kiện.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AQ100, AQ400, AQ500`

### 69. **[ADM-AQ-02]** - Cấu hình Danh mục rơi & Tỷ lệ trúng thưởng (`AQ200-AQ300`)
- **Điều kiện tiên quyết:** Tại AQ200 / AQ300
- **Các bước thực hiện:** 1. Thiết lập danh sách vật phẩm trúng thưởng<br>2. Cài đặt tỷ lệ phần trăm trúng thưởng theo cấp độ hiếm (SSR, SR, R)<br>3. Đảm bảo tổng tỷ lệ đạt chính xác 100.00%<br>4. Bấm [保存]
- **Kết quả mong đợi:** Lưu cấu hình thành công; tỷ lệ hiển thị công khai trên màn hình Tỷ lệ Gacha (A209) của App đúng quy định pháp luật.
- **Độ ưu tiên:** `Critical` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AQ200-AQ300`


## Quản lý Doanh thu & Tài chính

### 70. **[ADM-AS-01]** - Dashboard Báo cáo Doanh thu toàn nền tảng (`AS100`)
- **Điều kiện tiên quyết:** Đăng nhập quyền Admin
- **Các bước thực hiện:** 1. Truy cập [売上管理 > 売上分析ダッシュボード / AS100]<br>2. Quan sát biểu đồ tổng doanh thu, doanh thu theo kênh (IAP iOS/Android, Thẻ, Monthly Pass)<br>3. Lọc theo khoảng thời gian và xuất file CSV
- **Kết quả mong đợi:** Biểu đồ trực quan, số liệu khớp chính xác với lịch sử giao dịch nạp tiền, hỗ trợ xuất báo cáo tài chính.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AS100`

### 71. **[ADM-AS-02]** - Tiếp nhận & Duyệt Yêu cầu Đổi thưởng (Payout) (`AS200`)
- **Điều kiện tiên quyết:** Liver gửi lệnh rút tiền về tài khoản ngân hàng
- **Các bước thực hiện:** 1. Truy cập [売上管理 > 換金リクエスト / AS200]<br>2. Kiểm tra thông tin Liver, số point đổi, số tiền JPY thực nhận sau thuế thu nhập và phí dịch vụ<br>3. Bấm [承認 / Duyệt] để thực hiện lệnh chuyển khoản qua Aozora Bank
- **Kết quả mong đợi:** Hệ thống trừ điểm tích lũy của Liver, gửi yêu cầu thanh toán tự động qua API OpenID Connect của ngân hàng.
- **Độ ưu tiên:** `Critical` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AS200`

### 72. **[ADM-AS-03]** - Quản lý Tỷ giá Quy đổi Point sang JPY (`AS300`)
- **Điều kiện tiên quyết:** Truy cập [売上管理 > 交換レート / AS300]
- **Các bước thực hiện:** 1. Thiết lập tỷ lệ quy đổi từ Point kiếm được của Liver sang đồng Yên Nhật (JPY)<br>2. Cài đặt các gói nạp Coin quy đổi từ tiền mặt<br>3. Bấm lưu
- **Kết quả mong đợi:** Cập nhật thành công bảng tỷ giá tài chính; mọi giao dịch quy đổi tiền từ thời điểm đó áp dụng tỷ giá mới.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AS300`


## Giám sát Tin nhắn & Lọc Chat

### 73. **[ADM-MSG-01]** - Tra cứu Tin nhắn Direct Message 1-1 & Group (`AX100-AX300`)
- **Điều kiện tiên quyết:** Đăng nhập quyền Admin
- **Các bước thực hiện:** 1. Truy cập [メッセージ管理 > 検索 / AX100]<br>2. Tra cứu tin nhắn giữa 2 người dùng (AX200) hoặc trong nhóm chat khi có khiếu nại lừa đảo
- **Kết quả mong đợi:** Hiển thị chính xác dòng thời gian tin nhắn, tài khoản gửi/nhận, file hình ảnh đính kèm phục vụ điều tra.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AX100-AX300`

### 74. **[ADM-MSG-02]** - Quản lý Bình luận Live & BAN LIST Từ khóa cấm (`AY100-AY300`)
- **Điều kiện tiên quyết:** Truy cập [配信メッセージ管理 > BAN LIST / AY100, AY300]
- **Các bước thực hiện:** 1. Thêm các từ ngữ thô tục, nhạy cảm, số điện thoại vào danh sách đen (Blacklist)<br>2. Cài đặt chế độ tự động che dấu bằng dấu *** hoặc chặn gửi tin
- **Kết quả mong đợi:** Hệ thống tự động lọc bình luận độc hại trong phòng livestream, giữ môi trường tương tác an toàn, văn minh.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `AY100-AY300`


## Quản trị Vòng đời Tài khoản

### 75. **[ADM-DEL-01]** - Tiếp nhận & Xử lý Yêu cầu Xóa tài khoản (`K2022`)
- **Điều kiện tiên quyết:** Người dùng nộp đơn xóa tài khoản từ App
- **Các bước thực hiện:** 1. Truy cập màn hình quản trị xóa tài khoản K2022<br>2. Kiểm tra tài khoản trong thời gian chờ hủy (Grace Period 30 ngày)<br>3. Thực thi xác nhận xóa vĩnh viễn khi hết hạn chờ
- **Kết quả mong đợi:** Toàn bộ thông tin định danh cá nhân được ẩn/mã hóa (Anonymized) theo đúng chính sách quyền riêng tư dữ liệu GDPR.
- **Độ ưu tiên:** `High` | **Trạng thái:** `Untested` | **Ghi chú/Màn hình:** `K2022`

