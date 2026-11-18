# 📋 BỘ CHECKLIST KIỂM THỬ TOÀN DIỆN ỨNG DỤNG DI ĐỘNG (MOBILE APP CHECKLIST) - SURREALDOLL

> **Hệ điều hành áp dụng:** iOS & Android  
> **Người lập:** Antigravity QA Agent  
> **Phiên bản tài liệu:** v1.0  
> **Trạng thái:** Sẵn sàng thực thi kiểm thử  
> ⚠️ **LƯU Ý ĐẶC THÙ:** Tính năng **Setup avatar & Background** hiện có phụ thuộc (Dependency) vào việc Admin upload model lên hệ thống. Đang đặt cờ `[PENDING ADMIN MODEL]` chờ cấu hình thực tế.

---

## 📌 MỤC LỤC TỔNG QUAN

1. [Phần 1: Xác thực & Đăng nhập (Authentication)](#phần-1-xác-thực--đăng-nhập-authentication)
2. [Phần 2: Thiết lập Avatar & Background (Profile & Virtual Model)](#phần-2-thiết-lập-avatar--background-profile--virtual-model)
3. [Phần 3: Kiểm tra Phòng Thử Nghiệm (Test Livestream)](#phần-3-kiểm-tra-phòng-thử-nghiệm-test-livestream)
4. [Phần 4: Phát & Xem Livestream Thường (Normal Livestream)](#phần-4-phát--xem-livestream-thường-normal-livestream)
5. [Phần 5: Phát & Xem Livestream 2Shot & Gia Hạn 2Shot](#phần-5-phát--xem-livestream-2shot--gia-hạn-2shot)
6. [Phần 6: Phát & Xem Livestream Familia (Familia-Exclusive Live)](#phần-6-phát--xem-livestream-familia-familia-exclusive-live)
7. [Phần 7: Phát & Xem Livestream OBS (External RTMP / PC Studio)](#phần-7-phát--xem-livestream-obs-external-rtmp--pc-studio)
8. [Phần 8: Phát & Xem Livestream Broadcast (Chế độ Quảng bá Sự kiện)](#phần-8-phát--xem-livestream-broadcast-chế-độ-quảng-bá-sự-kiện)
9. [Phần 9: Chế độ Hình Trong Hình (PIP - Picture-in-Picture)](#phần-9-chế-độ-hình-trong-hình-pip---picture-in-picture)
10. [Phần 10: Tương tác Trong Phòng Livestream (Chat, Quà, Whisper, Share)](#phần-10-tương-tác-trong-phòng-livestream-chat-quà-whisper-share)
11. [Phần 11: Thông Báo & Push Notification (Admin Push & In-app/Room Notice)](#phần-11-thông-báo--push-notification-admin-push--in-approom-notice)
12. [Phần 12: Quản Lý Familia, Tạo Class & Đăng Bài Post](#phần-12-quản-lý-familia-tạo-class--đăng-bài-post)
13. [Phần 13: Trò Chuyện Ngoài Phòng Live (Chat 1-1 & Chat Group)](#phần-13-trò-chuyện-ngoài-phòng-live-chat-1-1--chat-group)

---

## PHẦN 1: XÁC THỰC & ĐĂNG NHẬP (AUTHENTICATION)

### 1.1. Đăng nhập bằng Google (Google Sign-In) - `[Android & iOS]`
- [ ] **[AUTH-GG-01]** Mở form đăng nhập, click nút "Đăng nhập bằng Google" -> Mở bottom sheet chọn tài khoản Google (Android) hoặc webview Google Auth (iOS).
- [ ] **[AUTH-GG-02]** Đăng nhập lần đầu với tài khoản Google mới -> Điều hướng thành công đến luồng Onboarding/Tạo hồ sơ người dùng.
- [ ] **[AUTH-GG-03]** Đăng nhập lại với tài khoản Google đã có tài khoản -> Điều hướng thẳng vào màn hình chính (Home) với đúng dữ liệu người dùng.
- [ ] **[AUTH-GG-04]** Người dùng hủy (Cancel/Back) giữa chừng khi đang ở hộp thoại Google -> Đóng hộp thoại, quay lại màn Login, app hoạt động bình thường không crash/treo.
- [ ] **[AUTH-GG-05]** Chuyển đổi giữa các tài khoản Google khác nhau trên thiết bị -> Đăng nhập đúng thông tin tài khoản được chọn.

### 1.2. Đăng nhập bằng LINE (LINE Login) - `[Android & iOS]`
- [ ] **[AUTH-LINE-01]** Máy ĐÃ CÀI app LINE: Click nút "Đăng nhập bằng LINE" -> Mở app LINE, hiển thị màn hình cấp quyền xác thực (Consent Screen).
- [ ] **[AUTH-LINE-02]** Cấp quyền thành công trên LINE -> Tự động chuyển hướng quay lại app SurrealDoll và đăng nhập thành công.
- [ ] **[AUTH-LINE-03]** Từ chối cấp quyền trên app LINE -> Quay lại app SurrealDoll, hiển thị thông báo lỗi thân thiện, không văng app.
- [ ] **[AUTH-LINE-04]** Máy CHƯA CÀI app LINE: Click nút "Đăng nhập bằng LINE" -> Mở trình duyệt Web Auth để người dùng đăng nhập bằng Email/Password của LINE.
- [ ] **[AUTH-LINE-05]** Hủy/Đóng Web Auth giữa chừng -> Trở lại màn hình đăng nhập bình thường.

### 1.3. Đăng nhập bằng Apple ID (Sign in with Apple) - `[Chỉ iOS]`
- [ ] **[AUTH-APPLE-01]** Nút "Sign in with Apple" CHỈ hiển thị trên phiên bản iOS, kiểm tra đảm bảo KHÔNG hiển thị trên Android.
- [ ] **[AUTH-APPLE-02]** Click "Sign in with Apple" -> Kích hoạt Native Sheet của Apple với Face ID / Touch ID / Mật mã thiết bị.
- [ ] **[AUTH-APPLE-03]** Kiểm tra tùy chọn "Share My Email" (Chia sẻ email thật) -> Hệ thống nhận diện đúng email Apple ID.
- [ ] **[AUTH-APPLE-04]** Kiểm tra tùy chọn "Hide My Email" (Chuyển tiếp relay email của Apple) -> Đăng nhập thành công, hệ thống lưu relay email ẩn danh mà không bị lỗi xác thực.
- [ ] **[AUTH-APPLE-05]** Hủy đăng nhập (Bấm dấu X hoặc hủy Face ID) -> Đóng sheet xác thực, giữ nguyên trạng thái ứng dụng.

### 1.4. Quản lý Phiên Đăng nhập & Đăng xuất
- [ ] **[AUTH-SESS-01]** Đóng app hoàn toàn (Kill app) rồi mở lại -> Giữ nguyên phiên đăng nhập (Auto-login), không bắt đăng nhập lại.
- [ ] **[AUTH-SESS-02]** Thực hiện Đăng xuất (Logout) -> Xóa toàn bộ token trong secure storage, đưa người dùng về màn hình Chào mừng/Đăng nhập.
- [ ] **[AUTH-SESS-03]** Xóa tài khoản (Account Deletion) -> Hiển thị cảnh báo xác nhận, chuyển trạng thái tài khoản sang chờ xóa và đăng xuất hoàn toàn.

---

## PHẦN 2: THIẾT LẬP AVATAR & BACKGROUND (PROFILE & VIRTUAL MODEL)

> ⏳ **Trạng thái:** `PENDING ADMIN MODEL` (Chờ Admin upload model mẫu lên hệ thống quản trị để kiểm tra kết nối Live2D/3D thực tế).

### 2.1. Cấu hình & Lựa chọn Avatar Live2D / 3D Model
- [ ] **[AVATAR-01]** Truy cập màn hình Setup Avatar từ Profile/Settings -> Tải danh mục model mà tài khoản sở hữu hoặc model mặc định.
- [ ] **[AVATAR-02]** Xem trước (Preview) Model: Hiển thị model mượt mà ở khung hình trung tâm, texture hiển thị sắc nét, không bị vỡ hình hay lệch trục tọa độ.
- [ ] **[AVATAR-03]** Thao tác cử chỉ trên Model: Thử nghiệm xoay góc nhìn, phóng to (Zoom in), thu nhỏ (Zoom out), điều chỉnh vị trí đứng của avatar.
- [ ] **[AVATAR-04]** Kiểm tra Facial Tracking (khi cấp quyền Camera): Mắt chớp theo cử động người dùng, miệng mấp máy theo giọng nói từ mic.
- [ ] **[AVATAR-05]** Bấm "Lưu/Áp dụng Model" -> Cập nhật thành công vào thông tin nhân vật của streamer.

### 2.2. Cấu hình Background (Hình nền phòng)
- [ ] **[BG-01]** Truy cập thư viện Background có sẵn của hệ thống -> Chọn từng background mẫu và xem preview thời gian thực sau lưng model.
- [ ] **[BG-02]** Tải lên Background tùy chỉnh từ thư viện ảnh máy (Camera Roll / Gallery) -> Hỗ trợ định dạng chuẩn (JPG, PNG), tự động căn chỉnh tỷ lệ khung hình.
- [ ] **[BG-03]** Kiểm tra các trường hợp chọn ảnh quá nặng (> 10MB) hoặc định dạng không hỗ trợ -> Hiển thị cảnh báo hợp lệ.
- [ ] **[BG-04]** Lưu cấu hình Background -> Background được áp dụng đồng bộ cho mọi phiên livestream tiếp theo.

---

## PHẦN 3: KIỂM TRA PHÒNG THỬ NGHIỆM (TEST LIVESTREAM)

- [ ] **[TESTLIVE-01]** Streamer chọn chế độ "Test Livestream" (Phòng phát thử trước khi phát chính thức).
- [ ] **[TESTLIVE-02]** Kiểm tra quyền Camera & Microphone: Yêu cầu cấp quyền hợp lệ khi lần đầu truy cập; xử lý đúng nếu bị từ chối quyền.
- [ ] **[TESTLIVE-03]** Bật/Tắt Micro trong phòng test: Kiểm tra thanh đo âm lượng (Audio meter) phản hồi theo tiếng nói.
- [ ] **[TESTLIVE-04]** Kiểm tra Tracking & Biểu cảm: Chuyển đổi biểu cảm (vui, buồn, ngạc nhiên...), kiểm tra độ nhạy cử động đầu và ánh mắt.
- [ ] **[TESTLIVE-05]** Thử đổi nhanh Avatar hoặc Background ngay trong phòng test -> Render tức thì không bị giật lag.
- [ ] **[TESTLIVE-06]** Kiểm tra tính riêng tư của phòng test: **TUYỆT ĐỐI KHÔNG** hiển thị phòng test trên màn hình Home của bất kỳ Viewer nào.
- [ ] **[TESTLIVE-07]** Bấm nút "Bắt đầu phát sóng chính thức" (Go Live) từ phòng test -> Chuyển trạng thái mượt mà sang phòng live thật mà không bị ngắt kết nối.

---

## PHẦN 4: PHÁT & XEM LIVESTREAM THƯỜNG (NORMAL LIVESTREAM)

### 4.1. Dành cho Streamer (Người phát sóng)
- [ ] **[LIVE-STR-01]** Tạo phiên live: Nhập tiêu đề live, chọn danh mục/tag, chụp hoặc upload ảnh bìa (Thumbnail).
- [ ] **[LIVE-STR-02]** Bắt đầu phát (Start Live): Kết nối WebRTC/RTMP thành công, luồng hình ảnh và âm thanh phát ổn định.
- [ ] **[LIVE-STR-03]** Giao diện Streamer: Hiển thị thời lượng live (hh:mm:ss), số lượng viewer đang xem, số tim nhận được, thanh điều khiển công cụ.
- [ ] **[LIVE-STR-04]** Thao tác điều khiển trong lúc live: Bật/tắt mic, chuyển đổi camera, thay đổi biểu cảm avatar, tắt tiếng nhanh (Mute).
- [ ] **[LIVE-STR-05]** Kết thúc live (End Stream): Bấm nút tắt -> Popup xác nhận kết thúc -> Hiển thị màn hình Thống kê tổng kết (Thời lượng live, Lượt xem, Quà tặng nhận được, Điểm doanh thu).

### 4.2. Dành cho Viewer (Người xem)
- [ ] **[LIVE-VIE-01]** Màn hình danh sách (Home): Phòng livestream hiển thị đầy đủ Thumbnail, Avatar streamer, Tiêu đề, Tag và Badge trạng thái "LIVE".
- [ ] **[LIVE-VIE-02]** Bấm vào phòng live: Vào phòng nhanh chóng (< 2 giây), âm thanh và hình ảnh đồng bộ hoàn hảo (Lipsync).
- [ ] **[LIVE-VIE-03]** Thao tác Thả tim: Tap liên tục vào màn hình -> Hiển thị hiệu ứng tim bay lên mượt mà, bộ đếm tim tăng tương ứng.
- [ ] **[LIVE-VIE-04]** Xem danh sách người xem đang có trong phòng: Hiển thị đúng avatar và tên các viewer.
- [ ] **[LIVE-VIE-05]** Thoát phòng live (Bấm nút X hoặc vuốt xuống): Dừng luồng phát video, đóng kết nối âm thanh và socket ngay lập tức.
- [ ] **[LIVE-VIE-06]** Xử lý khi Streamer kết thúc live: Viewer nhận thông báo "Streamer đã kết thúc phiên phát sóng" và tự động điều hướng ra ngoài hoặc hiển thị màn tóm tắt.

---

## PHẦN 5: PHÁT & XEM LIVESTREAM 2SHOT & GIA HẠN 2SHOT

### 5.1. Khởi tạo & Chấp nhận Yêu cầu 2Shot
- [ ] **[2SHOT-01]** Streamer kích hoạt trạng thái "Mở nhận 2Shot" trong phòng livestream.
- [ ] **[2SHOT-02]** Viewer có đủ Vé 2Shot hoặc đủ Point: Bấm nút "Yêu cầu 2Shot" -> Trừ vé/point tạm giữ và gửi request đến streamer.
- [ ] **[2SHOT-03]** Viewer KHÔNG ĐỦ vé/point: Bấm yêu cầu -> Hiển thị thông báo số dư không đủ và gợi ý nạp point/mua vé.
- [ ] **[2SHOT-04]** Streamer nhận popup thông báo yêu cầu 2Shot (Tên viewer, thời gian countdown phản hồi ví dụ 15s).
- [ ] **[2SHOT-05]** Streamer bấm "Từ chối" hoặc để hết giờ: Yêu cầu bị hủy, hệ thống hoàn vé/point lại cho viewer kèm thông báo lý do.
- [ ] **[2SHOT-06]** Streamer bấm "Đồng ý": Bắt đầu chuyển đổi luồng phát sang chế độ 2Shot 1-1 riêng tư.

### 5.2. Trải nghiệm Trong Phiên 2Shot
- [ ] **[2SHOT-07]** Màn hình Streamer & Viewer 2Shot: Hiển thị giao diện 1-1, đồng hồ đếm ngược thời gian còn lại (ví dụ 60s/120s), hai bên nghe/nói tương tác trực tiếp.
- [ ] **[2SHOT-08]** Màn hình các Viewer KHÁC trong phòng: Hiển thị màn hình chờ/che riêng tư (Waiting Screen / Audio mute theo spec), không nghe lén hoặc can thiệp phiên 2Shot.

### 5.3. Gia Hạn 2Shot (Extend 2Shot)
- [ ] **[2SHOT-09]** Thông báo gia hạn: Khi thời gian 2Shot còn lại khoảng 15s - 30s, popup hỏi "Bạn có muốn gia hạn thêm thời gian không?" hiển thị cho Viewer.
- [ ] **[2SHOT-10]** Viewer chọn "Gia hạn" khi đủ vé/điểm: Trừ vé/điểm gia hạn, đồng hồ thời gian lập tức cộng thêm số phút/giây tương ứng, cuộc trò chuyện không bị gián đoạn.
- [ ] **[2SHOT-11]** Viewer chọn "Không gia hạn" hoặc không đủ điểm: Đồng hồ đếm về 00:00 -> Kết thúc phiên 2Shot.
- [ ] **[2SHOT-12]** Hết phiên 2Shot: Tự động đưa Streamer và phòng quay lại chế độ Livestream Thường, các viewer khác tiếp tục xem live bình thường.

---

## PHẦN 6: PHÁT & XEM LIVESTREAM FAMILIA (FAMILIA-EXCLUSIVE LIVE)

- [ ] **[LIVE-FAM-01]** Streamer có Familia: Chọn chế độ phát "Chỉ dành cho Familia" (Familia Limited Live) trước khi phát.
- [ ] **[LIVE-FAM-02]** Hiển thị trên danh sách Live: Phòng có huy hiệu / Icon khóa "Familia" đặc thù để phân biệt với live thường.
- [ ] **[LIVE-FAM-03]** Viewer ĐÃ GIA NHẬP Familia của Streamer: Bấm vào phòng -> Vào xem mượt mà, đầy đủ tính năng tương tác.
- [ ] **[LIVE-FAM-04]** Viewer CHƯA GIA NHẬP Familia: Bấm vào phòng -> Bị chặn truy cập, hiển thị thông báo "Phòng live chỉ dành cho thành viên Familia".
- [ ] **[LIVE-FAM-05]** Điều hướng tham gia: Modal chặn hiển thị nút "Tham gia Familia" -> Click nút điều hướng chuẩn xác sang trang đăng ký Class của Familia đó.
- [ ] **[LIVE-FAM-06]** Bảo mật luồng phát: Viewer chưa tham gia hoàn toàn không thể nghe lén audio ngầm hoặc nhận video frame.

---

## PHẦN 7: PHÁT & XEM LIVESTREAM OBS (EXTERNAL RTMP / PC STUDIO)

- [ ] **[LIVE-OBS-01]** Streamer chọn chế độ phát "OBS Live" trên App.
- [ ] **[LIVE-OBS-02]** Cấp thông tin kết nối: Hệ thống tạo và hiển thị chính xác **RTMP Server URL** và **Stream Key** duy nhất cho phiên live.
- [ ] **[LIVE-OBS-03]** Tính năng Copy: Bấm nút Copy URL và Copy Stream Key -> Dữ liệu lưu vào Clipboard kèm toast message thông báo thành công.
- [ ] **[LIVE-OBS-04]** Bắt đầu đẩy luồng từ OBS Studio trên PC -> App nhận tín hiệu trong vòng vài giây và chuyển trạng thái sang "Đang phát sóng".
- [ ] **[LIVE-OBS-05]** Viewer trên App: Xem được luồng video phát từ OBS với độ trễ thấp, âm thanh và hình ảnh từ phần mềm PC hiển thị đầy đủ.
- [ ] **[LIVE-OBS-06]** Tương tác trong phòng live OBS: Chat, tặng quà, thả tim hoạt động bình thường như live thường.
- [ ] **[LIVE-OBS-07]** Tắt luồng từ OBS: App phát hiện mất tín hiệu luồng -> Hiển thị trạng thái chờ hoặc tự động kết thúc phiên live sau thời gian timeout quy định.

---

## PHẦN 8: PHÁT & XEM LIVESTREAM BROADCAST (CHẾ ĐỘ QUẢNG BÁ SỰ KIỆN)

- [ ] **[LIVE-BC-01]** Streamer/Admin khởi chạy phiên Live dạng Broadcast (Quy mô phát quảng bá hàng loạt người xem).
- [ ] **[LIVE-BC-02]** Tải luồng CDN: Đảm bảo luồng phát ổn định khi lượng viewer đồng thời (Concurrent Viewers) tăng cao.
- [ ] **[LIVE-BC-03]** Tối ưu hóa Chat/Gift: Khi có hàng nghìn người cùng xem, khung chat tự động kích hoạt cơ chế throttle/debounce để không bị tràn RAM hoặc giật lag thiết bị.
- [ ] **[LIVE-BC-04]** Chuyển đổi qua lại giữa mạng Wi-Fi và 4G/5G trong lúc xem Broadcast: Luồng phát tự động reconnect mượt mà, không bị crash app.

---

## PHẦN 9: CHẾ ĐỘ HÌNH TRONG HÌNH (PIP - PICTURE-IN-PICTURE)

### 9.1. PIP Dành Cho Viewer (Người xem)
- [ ] **[PIP-VIE-01]** Cấp quyền hệ thống: Lần đầu dùng PIP, app yêu cầu cấp quyền "Display over other apps" (Android) hoặc bật Picture in Picture (iOS).
- [ ] **[PIP-VIE-02]** Kích hoạt PIP: Khi đang xem live, viewer vuốt Home / bấm nút Home / chuyển sang app khác -> Cửa sổ video thu nhỏ (Floating Mini-Player) xuất hiện trên màn hình thiết bị.
- [ ] **[PIP-VIE-03]** Di chuyển cửa sổ PIP: Kéo thả mini-player đến các góc màn hình dễ dàng, không bị che khuất bất thường.
- [ ] **[PIP-VIE-04]** Tiếp tục phát âm thanh: Video và tiếng của phiên live vẫn tiếp tục phát mượt mà trong chế độ PIP.
- [ ] **[PIP-VIE-05]** Thao tác trên thanh mini-player: Nút Tạm dừng/Phát tiếp (Play/Pause), Nút đóng PIP (X), Nút phóng to toàn màn hình.
- [ ] **[PIP-VIE-06]** Bấm vào cửa sổ PIP: Tự động mở lại app SurrealDoll và điều hướng thẳng vào phòng live toàn màn hình.

### 9.2. PIP Dành Cho Streamer & Xử Lý Gián Đoạn (Interruptions)
- [ ] **[PIP-STR-01]** Streamer chuyển app hoặc bật đa nhiệm: App hiển thị thông báo tạm dừng video hoặc duy trì audio/floating badge theo cấu hình cho phép.
- [ ] **[PIP-STR-02]** Xử lý cuộc gọi đến (Incoming Phone Call): Khi có cuộc gọi thoại/video đến máy streamer hoặc viewer, luồng âm thanh tạm dừng hợp lý, sau khi kết thúc cuộc gọi âm thanh tự động phục hồi.
- [ ] **[PIP-STR-03]** Khóa màn hình (Lock Screen): Kiểm tra cơ chế chạy nền (Background mode), không gây rò rỉ bộ nhớ hoặc đơ ứng dụng.

---

## PHẦN 10: TƯƠNG TÁC TRONG PHÒNG LIVESTREAM (CHAT, QUÀ, WHISPER, SHARE)

### 10.1. Chat Trực Tiếp Trong Phòng Live
- [ ] **[CHAT-LIVE-01]** Viewer nhập tin nhắn text -> Bấm gửi -> Tin nhắn xuất hiện tức thì trong khung chat của streamer và toàn bộ viewer trong phòng.
- [ ] **[CHAT-LIVE-02]** Hỗ trợ icon, sticker, emoji chuẩn hệ thống.
- [ ] **[CHAT-LIVE-03]** Hiển thị huy hiệu (Badge): Huy hiệu Fan cứng, huy hiệu thành viên Familia, huy hiệu Rank hiển thị chuẩn xác trước tên user.
- [ ] **[CHAT-LIVE-04]** Cơ chế cuộn tin nhắn: Tự động cuộn theo tin mới nhất; khi người dùng chủ động cuộn lên xem lịch sử thì dừng auto-scroll.
- [ ] **[CHAT-LIVE-05]** Bộ lọc từ cấm (Word Blacklist): Không cho phép gửi hoặc tự động ẩn dấu `***` đối với các từ thô tục, vi phạm tiêu chuẩn cộng đồng.

### 10.2. Gửi Quà Thường (Normal Gifts)
- [ ] **[GIFT-NOR-01]** Bấm biểu tượng Hộp quà -> Mở Gift Panel phân chia rõ ràng danh mục quà tặng.
- [ ] **[GIFT-NOR-02]** Hiển thị đúng số dư Point / Gift Point / Gold hiện tại của người dùng ngay trên panel quà.
- [ ] **[GIFT-NOR-03]** Chọn Quà Thường và bấm gửi -> Hệ thống trừ điểm ví tức thì, hiển thị icon quà và animation nhỏ trong khung chat.
- [ ] **[GIFT-NOR-04]** Streamer nhận được điểm tích lũy quà tặng tương ứng theo tỷ lệ quy định.

### 10.3. Gửi Quà Cao Cấp (High-Tier / Premium Gifts)
- [ ] **[GIFT-PRE-01]** Chọn Quà Cao Cấp (Giá trị lớn) -> Kiểm tra số dư ví: Nếu không đủ, chặn gửi và gợi ý nạp.
- [ ] **[GIFT-PRE-02]** Gửi Quà Cao Cấp thành công -> Kích hoạt **Hiệu ứng Animation Toàn Màn Hình (Full-Screen Effect)** lộng lẫy (xe hơi, vương miện, rồng lửa...).
- [ ] **[GIFT-PRE-03]** Hiệu ứng âm thanh (Sound Effect) riêng biệt của món quà cao cấp phát kèm animation.
- [ ] **[GIFT-PRE-04]** Banner/Marquee thông báo nổi trên đầu phòng live vinh danh người gửi quà cao cấp.
- [ ] **[GIFT-PRE-05]** Điểm cống hiến và Bảng xếp hạng (Top Spender / Yell Rank) cập nhật tăng ngay lập tức.

### 10.4. Gửi Tin Nhắn Thì Thầm (Whisper) Trong Phòng Live
- [ ] **[WHISPER-01]** Viewer chọn tính năng Gửi Whisper cho Streamer trong phòng live.
- [ ] **[WHISPER-02]** Soạn nội dung whisper (và trừ point nếu spec có quy định phí whisper).
- [ ] **[WHISPER-03]** **Tính riêng tư bảo mật:** CHỈ Streamer và Viewer gửi tin mới nhìn thấy nội dung Whisper; các Viewer khác hoàn toàn KHÔNG THẤY trong khung chat chung.
- [ ] **[WHISPER-04]** Streamer nhận được thông báo/tab riêng để đọc và phản hồi whisper của fan.

### 10.5. Chia Sẻ Livestream & Chia Sẻ App (Share Live & App)
- [ ] **[SHARE-01]** Bấm nút Share trong phòng live -> Mở Native Share Sheet hệ điều hành (Facebook, X/Twitter, LINE, Sao chép link).
- [ ] **[SHARE-02]** Sao chép liên kết (Copy Link): Link chứa mã phòng live được lưu vào clipboard.
- [ ] **[SHARE-03]** Deep Link kiểm thử: Gửi link cho người khác qua tin nhắn -> Người nhận click link -> Tự động mở app SurrealDoll và điều hướng thẳng vào phòng live đó.
- [ ] **[SHARE-04]** Chia sẻ App: Nút share app từ trang Profile/Settings mở đúng link tải app trên App Store / Google Play.

---

## PHẦN 11: THÔNG BÁO & PUSH NOTIFICATION (ADMIN PUSH & IN-APP/ROOM NOTICE)

### 11.1. Xem Thông Báo Từ Admin Tại Màn Hình Chính (Home Notification)
- [ ] **[NOTI-HOME-01]** Admin tạo và gửi thông báo hệ thống mới từ trang Admin Portal.
- [ ] **[NOTI-HOME-02]** Icon Quả chuông trên màn Home hiển thị chấm đỏ / Badge số lượng thông báo chưa đọc.
- [ ] **[NOTI-HOME-03]** Mở danh sách thông báo: Hiển thị đầy đủ Tiêu đề, Nội dung rút gọn, Thời gian gửi, Thumbnail/Banner (nếu có).
- [ ] **[NOTI-HOME-04]** Bấm vào 1 thông báo: Chuyển sang màn hình Chi tiết thông báo, đánh dấu trạng thái "Đã đọc", badge số chưa đọc giảm tương ứng.

### 11.2. Xem Thông Báo Trong Phòng Livestream (In-Room Notification)
- [ ] **[NOTI-ROOM-01]** Admin gửi thông báo khẩn cấp hoặc thông báo bảo trì toàn hệ thống khi phòng live đang diễn ra.
- [ ] **[NOTI-ROOM-02]** Trong phòng live xuất hiện Banner chạy chữ (Marquee Banner) hoặc Dialog nổi thông báo từ admin mà không làm gián đoạn luồng live.
- [ ] **[NOTI-ROOM-03]** Người dùng có thể đóng banner hoặc xem chi tiết mà không bị văng khỏi phòng phát.

### 11.3. Đẩy Thông Báo Sự Kiện Bất Kỳ (Push Event Notification)
- [ ] **[PUSH-EV-01]** Admin kích hoạt lệnh Push Notification cho một Sự kiện (Event/Campaign) bất kỳ.
- [ ] **[PUSH-EV-02]** **Trường hợp App đang MỞ (Foreground):** Hiển thị In-app Banner thông báo ở mép trên màn hình, không chặn thao tác hiện tại.
- [ ] **[PUSH-EV-03]** **Trường hợp App chạy NGẦM (Background):** Xuất hiện Push Notification trên thanh trạng thái thiết bị (kèm icon app, âm thanh, rung).
- [ ] **[PUSH-EV-04]** **Trường hợp App đã ĐÓNG HOÀN TOÀN (Killed State):** Nhận push notification chuẩn xác qua FCM (Android) và APNs (iOS).
- [ ] **[PUSH-EV-05]** **Deep Link Sự Kiện:** Người dùng click vào Push Notification -> Khởi động app và điều hướng thẳng đến trang Chi tiết Sự kiện tương ứng.

---

## PHẦN 12: QUẢN LÝ FAMILIA, TẠO CLASS & ĐĂNG BÀI POST

### 12.1. Tạo Familia (Create Familia)
- [ ] **[FAM-01]** Streamer đủ điều kiện truy cập tính năng "Tạo Familia" từ Profile.
- [ ] **[FAM-02]** Nhập Tên Familia, Mô tả giới thiệu, Tải lên Avatar/Cover của Familia.
- [ ] **[FAM-03]** Kiểm tra validation: Bỏ trống tên, tên trùng lặp, vượt quá số ký tự cho phép -> Báo lỗi hợp lệ.
- [ ] **[FAM-04]** Tạo thành công: Familia hiển thị trên trang cá nhân của Streamer và mở khóa các tính năng quản trị Familia.

### 12.2. Tạo Class Trong Familia (Create Subscription Tiers)
- [ ] **[FAM-CLASS-01]** Chủ Familia tạo Class mới: Nhập Tên Class (ví dụ: Đồng, Bạc, Vàng), Mức phí đăng ký theo tháng (Yen / Point / Gold), Mô tả quyền lợi.
- [ ] **[FAM-CLASS-02]** Thiết lập các đặc quyền của Class: Huy hiệu riêng, quyền truy cập phòng live familia, quyền đọc post độc quyền.
- [ ] **[FAM-CLASS-03]** Chỉnh sửa hoặc ẩn/tắt Class đã tạo -> Cập nhật trạng thái thành công cho các thành viên xem bảng giá.

### 12.3. Tạo Bài Viết Trong Familia (Create Post)
- [ ] **[FAM-POST-01]** Soạn bài viết mới: Nhập nội dung văn bản (hỗ trợ ký tự xuống dòng, link, emoji).
- [ ] **[FAM-POST-02]** Đính kèm đa phương tiện: Chọn và đính kèm 1 hoặc nhiều hình ảnh từ máy.
- [ ] **[FAM-POST-03]** Phân quyền hiển thị (Visibility): Chọn đối tượng được xem bài viết (Tất cả thành viên Familia HOẶC Chỉ các Class cao cấp chỉ định).
- [ ] **[FAM-POST-04]** Đăng bài: Bài viết hiển thị ngay lập tức trên Feed của Familia theo thứ tự thời gian mới nhất.
- [ ] **[FAM-POST-05]** Kiểm tra hiển thị phía Member: Member thuộc đúng Class mới đọc được bài viết độc quyền; member chưa đủ cấp độ sẽ thấy trạng thái bài bị khóa.

---

## PHẦN 13: TRÒ CHUYỆN NGOÀI PHÒNG LIVE (CHAT 1-1 & CHAT GROUP)

### 13.1. Trò Chuyện Trực Tiếp 1-1 (Direct Chat)
- [ ] **[CHAT-1-1-01]** Mở cuộc trò chuyện 1-1 từ trang cá nhân của người dùng khác.
- [ ] **[CHAT-1-1-02]** Gửi/nhận tin nhắn văn bản thời gian thực (Realtime WebSocket): Bên nhận thấy tin nhắn mới không cần tải lại trang.
- [ ] **[CHAT-1-1-03]** Gửi hình ảnh đính kèm: Tải ảnh lên thành công, hiển thị thumbnail và cho phép bấm xem ảnh phóng to.
- [ ] **[CHAT-1-1-04]** Trạng thái tin nhắn: Hiển thị đúng trạng thái Đã gửi -> Đã nhận -> Đã đọc (Read Receipt).
- [ ] **[CHAT-1-1-05]** Nhận thông báo tin nhắn: Khi đang ở ngoài màn hình chat hoặc thoát app, có tin nhắn đến -> Bắn push notification chuẩn xác.
- [ ] **[CHAT-1-1-06]** Chặn & Báo cáo: Chặn người dùng khác -> Hai bên không thể tiếp tục gửi tin nhắn cho nhau.

### 13.2. Trò Chuyện Nhóm (Chat Group)
- [ ] **[CHAT-GRP-01]** Tạo nhóm chat mới: Đặt tên nhóm, chọn ảnh đại diện nhóm, chọn danh sách bạn bè/thành viên để thêm vào nhóm.
- [ ] **[CHAT-GRP-02]** Nhắn tin nhóm thời gian thực: Tin nhắn gửi đi được đồng bộ tức thì đến tất cả thành viên trong nhóm kèm tên/avatar người gửi.
- [ ] **[CHAT-GRP-03]** Quản trị nhóm (Admin Group): Admin có quyền đổi tên nhóm, thêm thành viên mới, xóa thành viên vi phạm khỏi nhóm.
- [ ] **[CHAT-GRP-04]** Tự rời nhóm: Thành viên bấm "Rời nhóm" -> Xóa nhóm khỏi danh sách chat của người đó, nhóm thông báo "User X đã rời nhóm".
- [ ] **[CHAT-GRP-05]** Tắt thông báo nhóm (Mute Group): Bật chế độ im lặng -> Tin nhắn mới vẫn lưu trong nhóm nhưng không phát âm thanh push phiền hà.

---

## 🎯 TIÊU CHÍ NGHIỆM THU (ACCEPTANCE CRITERIA)
- 100% các mục checklist được kiểm thử trên cả **Android** và **iOS** (trừ mục Apple ID chỉ kiểm tra trên iOS).
- Các tình huống ngắt quãng (mất mạng, rớt mạng, đa nhiệm, cuộc gọi thoại đến, chuyển đổi Wi-Fi sang 4G) được xử lý ổn định, không gây crash ứng dụng.
- Dữ liệu tiền tệ (Point, Gift Point, Vé 2Shot, Gold) được trừ và cộng chính xác, đồng bộ giữa Mobile App và CSDL backend.
