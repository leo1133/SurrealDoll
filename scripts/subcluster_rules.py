# Auto-extracted subcluster classification rules for SurrealDoll

def get_subclusters(grp, mod_title, items):
    def match_ids(prefixes):
        return lambda it: any(it['id'].upper().startswith(p.upper()) for p in prefixes)

    def match_exact(ids):
        s = {x.upper() for x in ids}
        return lambda it: it['id'].upper() in s

    def match_kw(kws):
        return lambda it: any(k.lower() in it['name_en'].lower() or k.lower() in it['id'].lower() for k in kws)

    rules = []

    if grp == 'Admin':
        if mod_title.startswith('1.'):
            rules = [
                ('1.1 Xác thực & Quên/Đổi mật khẩu Admin',
                 'Đăng nhập CMS Admin (`AA000`), đổi mật khẩu khi đang đăng nhập (`AA003`), luồng yêu cầu quên mật khẩu qua email & đặt lại mật khẩu mới (`AB000`).',
                 'Kiểm tra rule mật khẩu (độ dài, ký tự đặc biệt), token reset hết hạn, khóa tài khoản khi sai nhiều lần, session timeout.',
                 'Tương đồng luồng Auth với Agency (`BA100`, `BA200`, `BA1001-BA1003`).',
                 match_exact(['AA000', 'AA003', 'AB000'])),
                ('1.2 Quản lý Tài khoản & Phân quyền System Admin',
                 'Danh sách/tìm kiếm System Admin (`AC100`), tạo mới (`AC200`), cập nhật/xóa (`AC300`), và cấu hình ma trận phân quyền RBAC (`AC400`).',
                 'Kiểm tra phân quyền thực tế trên sidebar/API theo role được gán ở `AC400`, validate email trùng, không cho tự xóa/hạ quyền chính mình.',
                 'Áp dụng phân quyền cho toàn bộ module `AD`–`AY` trong Admin CMS.',
                 lambda it: True),
            ]
        elif mod_title.startswith('2.'):
            rules = [
                ('2.1 Quản lý Hồ sơ Agency & Danh sách Streamer trực thuộc',
                 'Tìm kiếm/lọc danh sách Agency (`AD100`), đăng ký Agency mới (`AD200`), xem/sửa/xóa chi tiết Agency (`AD301`) và xem danh sách Streamer/Liver thuộc Agency (`AD302`).',
                 'Validate thông tin thuế/ngân hàng/email liên hệ Agency; khi xóa/khóa Agency kiểm tra trạng thái đăng nhập cổng Agency (`BA100`) và liên kết của Liver (`K203`).',
                 'Liên kết trực tiếp với Agency Portal (`BB100-BB300`, `BC100`) và App (`K203` Join/Exit Agency).',
                 lambda it: True),
            ]
        elif mod_title.startswith('3.'):
            rules = [
                ('3.1 Hồ sơ Người dùng, Xác thực eKYC & Xóa tài khoản',
                 'Danh sách/tìm kiếm người dùng (`AE100`), chi tiết hồ sơ (`AE200`), kiểm duyệt eKYC & OCR giấy tờ tùy thân (`AE700`), xóa tài khoản từ Admin (`K2022`).',
                 'Kiểm tra trạng thái duyệt/từ chối eKYC đồng bộ về App (`K205`) và mở khóa tính năng rút tiền (`K906`); kiểm tra logic đóng tài khoản khi còn số dư GOLD/Point.',
                 'Liên kết với Agency (`BC100`, `BC200`) và App (`K000`, `K205`, `K2022`).',
                 match_exact(['AE100', 'AE200', 'AE700', 'K2022'])),
                ('3.2 Tài sản, Lịch sử sử dụng, Hóa đơn & Doanh thu Người dùng',
                 'Xem vật phẩm sở hữu (`AE300`), lịch sử sử dụng (`AE400`), lịch sử nạp/gói tháng Billing Log (`AE500`), thông tin thanh toán (`AE600`) và chi tiết doanh thu cá nhân (`AE800`).',
                 'Đối chiếu số liệu tổng hợp với DB (`users`, `orders`, `payments`, `gifts`), kiểm tra phân trang, lọc theo khoảng ngày và export/tính toán hoa hồng.',
                 'Liên kết với Agency (`BD100-BD500`), Admin Sales (`AS100`) và App (`G600`, `K601`).',
                 lambda it: True),
            ]
        elif mod_title.startswith('4.'):
            rules = [
                ('4.1 Danh mục, CRUD Quà tặng & Quà cao cấp',
                 'Quản lý danh sách quà (`AF100`), tạo/sửa/xóa quà tặng (`AF200`, `AF300`), quản lý danh mục quà (`AF400`) và cấu hình quà cao cấp/hiệu ứng đặc biệt (`AF500`).',
                 'Kiểm tra upload asset (animation/icon), giá coin, thứ tự hiển thị, trạng thái ON/OFF đồng bộ realtime lên danh sách quà trong phòng Live (`I600`).',
                 'Hiển thị trực tiếp trên App Livestream (`I600`, `I601`) và Wishlist (`M1011`, `M20507`).',
                 lambda it: True),
            ]
        elif mod_title.startswith('5.'):
            rules = [
                ('5.1 Giám sát Phòng Live đang phát, Xem trực tiếp & Archive',
                 'Danh sách phòng đang live (`AG100`), xem luồng livestream trực tiếp (`AG200`), quản lý danh sách bị Ban (`AG300`), danh sách bị Force Stop (`AG400`), và xem lại các phiên đã kết thúc (`AG500`).',
                 'Kiểm tra thao tác Force Stop từ Admin có ngắt phòng live trên App (`M200`/`I100`) ngay lập tức không; kiểm tra log lý do Ban/Force Stop và phát lại video Archive.',
                 'Liên kết 3 chiều với Agency (`BF100-BF500`) và App (`I100`, `M200`, `D701`, `K9051`).',
                 lambda it: True),
            ]
        elif mod_title.startswith('6.'):
            rules = [
                ('6.1 Quản lý Thông báo Hệ thống & Tin nhắn từ Admin',
                 'Danh sách thông báo (`AH100`), tạo/sửa thông báo (`AH200`, `AH300`), xem trước nội dung (`AH301`) và gửi tin nhắn hệ thống từ Admin (`AH400`).',
                 'Kiểm tra hẹn giờ đăng (publish schedule), đối tượng nhận (All/User/Streamer), render HTML/Webview trên App (`E201`, `E202`, `I804`) và tin nhắn hệ thống (`F103`).',
                 'Hiển thị tại App (`E201`, `E202`, `I804`, `I8041`, `F103`).',
                 lambda it: True),
            ]
        elif mod_title.startswith('7.'):
            rules = [
                ('7.1 Xử lý Báo cáo Vi phạm (Report Management)',
                 'Danh sách báo cáo vi phạm (`AI100`) và chi tiết xử lý báo cáo (`AI200`) đối với user, bài đăng, tin nhắn hoặc livestream.',
                 'Kiểm tra lọc theo loại vi phạm/trạng thái xử lý, xem bằng chứng đính kèm, cập nhật trạng thái xử lý và đồng bộ với Agency (`BG100`, `BG200`).',
                 'Nhận dữ liệu từ App (`D2021-D2023`) và đồng bộ với Agency (`BG100`, `BG200`).',
                 lambda it: True),
            ]
        elif mod_title.startswith('8.'):
            rules = [
                ('8.1 Quản lý Kho BGM & Chuyển đổi định dạng Audio',
                 'Danh sách nhạc nền BGM (`AJ100`), thêm mới (`AJ200`), chỉnh sửa (`AJ300`) và luồng convert MP3 sang WAV (`AJ400`).',
                 'Kiểm tra upload file âm thanh, dung lượng/định dạng hợp lệ, quá trình convert MP3->WAV không lỗi, trạng thái hiển thị trong phòng live (`M20514`).',
                 'Cung cấp kho nhạc nền cho Streamer trên App (`M20514`).',
                 lambda it: True),
            ]
        elif mod_title.startswith('9.'):
            rules = [
                ('9.1 Quản lý Hình nền Minh họa (Background Illustrations)',
                 'Danh sách (`AK201`), tạo mới (`AK202`), chỉnh sửa (`AK203`) hình nền dùng trong livestream.',
                 'Kiểm tra upload ảnh/tỷ lệ khung hình, trạng thái kích hoạt và đồng bộ sang App (`M00131`, `M20504`).',
                 'Liên kết với App Streamer Background (`M00131`, `M20504`) và BG Gacha (`AQ500`).',
                 match_exact(['AK201', 'AK202', 'AK203'])),
                ('9.2 Quản lý Hình nền Mini Garden',
                 'Danh sách (`AK301`), tạo mới (`AK302`), chỉnh sửa (`AK303`) hình nền Mini Garden.',
                 'Kiểm tra cấu hình asset Mini Garden, trạng thái hiển thị và liên kết với Mini Garden Gacha (`AQ400`).',
                 'Liên kết với Admin Gacha (`AQ400`) và App Shop/Gacha.',
                 lambda it: True),
            ]
        elif mod_title.startswith('10.'):
            rules = [
                ('10.1 Quản lý Kho bài hát Karaoke & Yêu cầu thêm bài',
                 'Danh sách bài hát (`AL100`), upload hàng loạt/file (`AL101`), tạo mới (`AL200`), chỉnh sửa (`AL300`) và danh sách yêu cầu thêm bài hát mới từ user (`AL400`).',
                 'Kiểm tra đồng bộ file lyric/audio/beat, trạng thái duyệt request ở `AL400` phản hồi về `M4071`/`M4072`.',
                 'Cung cấp dữ liệu cho Karaoke trên App (`I501-I509`, `M401-M409`, `K010-K0142`).',
                 match_exact(['AL100', 'AL101', 'AL200', 'AL300', 'AL400'])),
                ('10.2 Báo cáo Bản quyền Âm nhạc (JASRAC / NEXTONE) & Nội dung trả phí',
                 'Báo cáo bài hát sử dụng cho JASRAC/NEXTONE (`AL600`), danh sách & chi tiết báo cáo bài hát user đã dùng (`AL700`), danh sách nội dung trả phí (`AL700`).',
                 'Đối chiếu dữ liệu nhận diện ACRCloud/nhập tay từ App (`K209-New`), kiểm tra xuất file CSV/báo cáo chuẩn định dạng JASRAC/NEXTONE và tính toán kỳ báo cáo.',
                 'Nhận dữ liệu trực tiếp từ App (`K209-New` ACRCloud Report of Used Songs).',
                 lambda it: True),
            ]
        elif mod_title.startswith('11.'):
            rules = [
                ('11.1 Quản lý & Kiểm duyệt Bài đăng Familia (Post Management)',
                 'Danh sách toàn bộ bài đăng (`AM100`), bài đăng theo từng user (`AM101`) và chi tiết bài đăng (`AM200`) để kiểm duyệt/ẩn/xóa nội dung vi phạm.',
                 'Kiểm tra tìm kiếm theo user/từ khóa, xem media đính kèm (ảnh/video/audio) và thao tác ẩn/xóa bài đăng đồng bộ về Agency (`BE100-BE200`) và App (`L402-L406`).',
                 'Liên kết với Agency (`BE100`, `BE200`) và App Familia (`L202-L203`, `L402-L406`).',
                 lambda it: True),
            ]
        elif mod_title.startswith('12.'):
            rules = [
                ('12.1 Quản lý 3D Model, Bộ phận (Head/Body/Accessory) & Độ phân giải',
                 'Danh sách 3D Model (`AP000`), cấu hình độ phân giải (`AP000`), chi tiết Model (`AP100`), chi tiết Head (`AP200`), Body (`AP300`) và Phụ kiện Accessory (`AP400`).',
                 'Kiểm tra upload asset 3D/texture, cấu hình thông số độ phân giải đồng bộ với thiết lập trên App (`M100`, `M0011-M00121`) và Gacha Avatar (`AQ100-AQ300`).',
                 'Liên kết với App Model Setup (`M0011-M00121`, `M100`) và Admin Gacha (`AQ100`).',
                 lambda it: True),
            ]
        elif mod_title.startswith('13.'):
            rules = [
                ('13.1 Quản lý Gacha (Avatar, Mini Garden & Background Gacha)',
                 'Danh sách Avatar Gacha (`AQ100`), chi tiết (`AQ200`), thiết lập tỷ lệ & pool item (`AQ300`), quản lý Mini Garden Gacha (`AQ400`) và Background Gacha (`AQ500`).',
                 'Kiểm tra tổng tỷ lệ rơi (%) phải bằng 100%, cấu hình thời gian mở/đóng banner, giá quay bằng Coin/Ticket, hiển thị bảng tỷ lệ trên Webview (`A209`) và Shop (`G200-G201`).',
                 'Liên kết trực tiếp với App Shop Gacha (`G200-G203`, `I700-I701`) và Webview tỷ lệ (`A209`).',
                 lambda it: True),
            ]
        elif mod_title.startswith('14.'):
            rules = [
                ('14.1 Phân tích Doanh thu, Tỷ giá & Duyệt Yêu cầu Rút tiền (Payout)',
                 'Dashboard phân tích doanh thu User (`AS100`), doanh thu theo Agency (`AS500`), cấu hình tỷ giá quy đổi (`AS300`) và xử lý yêu cầu rút tiền (`AS200`).',
                 'Kiểm tra công thức tính doanh thu gộp/thuần (trừ phí Store Apple/Google, tỷ giá `AS300`, hoa hồng Agency), duyệt/từ chối Payout ở `AS200` cập nhật trạng thái về App (`K9064-K9066`).',
                 'Liên kết với Admin User Revenue (`AE800`), Agency (`BD500`) và App (`K601`, `K906-K9066`).',
                 lambda it: True),
            ]
        elif mod_title.startswith('15.'):
            rules = [
                ('15.1 Giám sát Tin nhắn Người dùng (User Messages Monitoring)',
                 'Tìm kiếm hội thoại (`AX100`), xem chi tiết nội dung tin nhắn (`AX200`) và thông tin hội thoại/thành viên (`AX300`).',
                 'Kiểm tra tìm kiếm theo user/khoảng thời gian/từ khóa, hiển thị đúng loại tin nhắn (text, stamp, 2shot invite) và phân quyền xem dữ liệu nhạy cảm.',
                 'Liên kết với Agency (`BX100`) và App Direct Messages (`F100-F500`).',
                 lambda it: True),
            ]
        elif mod_title.startswith('16.'):
            rules = [
                ('16.1 Giám sát Bình luận & Danh sách Cấm Chat Livestream',
                 'Tìm kiếm bình luận livestream (`AY100`), xem chi tiết log chat của phiên live (`AY200`) và quản lý danh sách user bị Ban chat (`AY300`).',
                 'Kiểm tra thao tác Ban/Unban chat từ Admin có hiệu lực ngay với phiên live và đồng bộ với Agency (`BY100`, `BY300`).',
                 'Liên kết với Agency (`BY100`, `BY300`) và App Livestream (`I100`, `I1013`).',
                 lambda it: True),
            ]

    elif grp == 'Agency':
        if mod_title.startswith('1.'):
            rules = [
                ('1.1 Đăng nhập & Đổi/Quên mật khẩu Cổng Agency',
                 'Đăng nhập cổng Agency (`BA100`), đổi mật khẩu khi đang đăng nhập (`BA200`), gửi yêu cầu quên mật khẩu (`BA1001`), màn hình hoàn tất gửi mail (`BA1002`) và đặt lại mật khẩu qua link token (`BA1003`).',
                 'Kiểm tra Basic Auth + rule mật khẩu, khóa tài khoản Agency khi bị Admin disable (`AD301`), token hết hạn/đã sử dụng ở `BA1003`.',
                 'Tài khoản Agency được tạo/quản lý từ Admin (`AD200`, `AD301`) và nhân viên ở `BB200`.',
                 lambda it: True),
            ]
        elif mod_title.startswith('2.'):
            rules = [
                ('2.1 Thông tin Agency & Quản lý Quản trị viên trực thuộc',
                 'Xem chi tiết thông tin Agency (`BB101`), danh sách quản trị viên Agency (`BB100`), tạo mới (`BB200`) và xem/sửa chi tiết quản trị viên (`BB300`).',
                 'Kiểm tra phân quyền Owner vs Staff Agency, validate email/tên đăng nhập trùng, cập nhật thông tin ở `BB101` đồng bộ với Admin (`AD301`).',
                 'Liên kết với Admin Agency (`AD301`) và Auth Agency (`BA100`).',
                 lambda it: True),
            ]
        elif mod_title.startswith('3.'):
            rules = [
                ('3.1 Quản lý Danh sách & Hồ sơ Streamer / Liver trực thuộc',
                 'Danh sách Liver thuộc Agency (`BC100`) và chi tiết hồ sơ Liver (`BC200`), bao gồm duyệt/quản lý Liver tham gia hoặc rời Agency.',
                 'Kiểm tra chỉ hiển thị Liver thuộc Agency hiện tại (Data Isolation), xử lý yêu cầu gia nhập/rời Agency từ App (`K203`).',
                 'Liên kết với Admin (`AD302`, `AE100-AE200`) và App (`K203`).',
                 match_exact(['BC100', 'BC200'])),
                ('3.2 Tài sản, Lịch sử, Billing & Doanh thu của Liver',
                 'Xem vật phẩm sở hữu (`BD100`), lịch sử sử dụng (`BD200`), lịch sử gói tháng (`BD300`), thông tin thanh toán (`BD400`) và phân tích doanh thu Liver (`BD500`).',
                 'Kiểm tra dữ liệu chỉ giới hạn trong phạm vi Liver của Agency; đối chiếu số liệu doanh thu/hoa hồng với Admin (`AE800`, `AS500`).',
                 'Liên kết với Admin (`AE300-AE600`, `AE800`, `AS500`) và App (`K601`).',
                 lambda it: True),
            ]
        elif mod_title.startswith('4.'):
            rules = [
                ('4.1 Quản lý Bài đăng của Streamer (Streamer Posts)',
                 'Danh sách bài đăng (`BE100`) và chi tiết bài đăng (`BE200`) của các Liver thuộc Agency.',
                 'Kiểm tra lọc theo Liver, xem nội dung/media bài đăng, đảm bảo không xem được bài của Liver thuộc Agency khác.',
                 'Liên kết với Admin (`AM100-AM200`) và App (`L402`, `L405`).',
                 lambda it: True),
            ]
        elif mod_title.startswith('5.'):
            rules = [
                ('5.1 Giám sát Livestream, Archive, Ban & Force Stop của Agency',
                 'Danh sách phòng live của Liver (`BF100`), xem chi tiết phòng live (`BF200`), xem lại Archive (`BF300`), danh sách Ban (`BF400`) và danh sách Force Stop (`BF500`).',
                 'Kiểm tra quyền Force Stop/Ban của Agency đối với Liver trực thuộc và đồng bộ trạng thái với Admin (`AG100-AG500`).',
                 'Liên kết với Admin (`AG100-AG500`) và App (`M200`, `I100`).',
                 lambda it: True),
            ]
        elif mod_title.startswith('6.'):
            rules = [
                ('6.1 Quản lý Báo cáo Vi phạm liên quan đến Liver của Agency',
                 'Danh sách báo cáo (`BG100`) và chi tiết báo cáo (`BG200`) liên quan đến các Liver trực thuộc Agency.',
                 'Kiểm tra phân tách dữ liệu theo Agency, cập nhật trạng thái xử lý và đối chiếu với Admin (`AI100`, `AI200`).',
                 'Liên kết với Admin (`AI100`, `AI200`) và App (`D2021-D2023`).',
                 lambda it: True),
            ]
        elif mod_title.startswith('7.'):
            rules = [
                ('7.1 Giám sát Tin nhắn & Bình luận Chat của Liver',
                 'Xem tin nhắn của Liver (`BX100`), bình luận livestream (`BY100`) và danh sách cấm chat livestream (`BY300`).',
                 'Kiểm tra dữ liệu lọc đúng Liver thuộc Agency, thao tác Ban/Unban chat tại `BY300` đồng bộ với `AY300` và phòng live.',
                 'Liên kết với Admin (`AX100-AX300`, `AY100-AY300`) và App (`F100`, `I100`).',
                 lambda it: True),
            ]

    elif grp == 'App':
        if mod_title.startswith('1.'):
            rules = [
                ('1.1 Khởi động, Đăng nhập (SNS / SĐT OTP) & Điều khoản',
                 'Màn hình Splash (`A000`), chọn phương thức đăng nhập (`A100`), popup đồng ý điều khoản (`A101`), nhập SĐT (`A1031`), nhập mã OTP (`A1032`) cho cả App & Web.',
                 'Kiểm tra gửi/hết hạn/nhập sai OTP, bắt buộc đồng ý điều khoản ở `A101` trước khi vào app, đồng bộ luồng App và Web.',
                 'Liên kết với `K202` (Account Settings), `K2025` (Phone Linkage).',
                 match_exact(['A000', 'A100', 'A101', 'A1031', 'A1032'])),
                ('1.2 Khởi tạo Hồ sơ, Quà tân thủ & Single-Device Session',
                 'Thiết lập hồ sơ ban đầu (`A105`), nhận thưởng đăng nhập tân thủ (`A300`), và logic CR 1 UID chỉ được đăng nhập trên 1 thiết bị tại một thời điểm (`-`).',
                 'Kiểm tra khi đăng nhập thiết bị B thì thiết bị A bị force logout (đặc biệt khi đang xem/phát livestream); kiểm tra nhận Login Bonus 1 lần duy nhất.',
                 'Liên kết với `K800` (Edit Profile) và `M200`/`I100` (xử lý ngắt kết nối khi đá session).',
                 lambda it: True),
            ]
        elif mod_title.startswith('2.'):
            rules = [
                ('2.1 Trung tâm Trợ giúp & Gửi yêu cầu Hỗ trợ (Help & Inquiry)',
                 'Trang chủ Help (`A201`), tìm kiếm, danh mục, chi tiết bài viết (`A201`), gửi & hoàn tất yêu cầu hỗ trợ Inquiry (`A202`).',
                 'Kiểm tra tìm kiếm từ khóa tiếng Nhật, mở Webview mượt trên iOS/Android, submit form Inquiry gửi mail/ticket thành công.',
                 'Mở từ màn hình Login (`A100`) hoặc My Page Settings (`K100`).',
                 match_exact(['A201', 'A202'])),
                ('2.2 Điều khoản Pháp lý, Chính sách & Tỷ lệ Gacha (Webview)',
                 'Chính sách bảo mật (`A204`), Điều khoản sử dụng (`A205`), Quy định tiền tệ trong app (`A206`), Điều khoản Hộp kho báu (`A207`), Luật giao dịch thương mại (`A208`) và Chi tiết tỷ lệ Gacha (`A209`).',
                 'Kiểm tra hiển thị đúng nội dung pháp lý mới nhất, link điều hướng không 404, bảng tỷ lệ `A209` khớp với cấu hình trên Admin (`AQ100-AQ500`).',
                 'Liên kết với `A101`, `G201` (Gacha Detail), `I1021` (Treasure Box).',
                 lambda it: True),
            ]
        elif mod_title.startswith('3.'):
            rules = [
                ('3.1 Trang chủ, Gợi ý Nội dung & Quảng cáo (Recommend & Ads)',
                 'Các màn hình gợi ý bài đăng (`B001`), phòng live standby (`B002`), phòng live đang phát (`B003`), danh sách khởi tạo (`B100`), gợi ý (`B101`), theo danh mục (`B102`) và màn hình quảng cáo (`B300`).',
                 'Kiểm tra phân trang/infinite scroll, lọc theo category, chuyển trạng thái real-time khi phòng live bắt đầu/kết thúc, hiển thị popup/banner quảng cáo đúng tần suất.',
                 'Điều hướng trực tiếp vào phòng live (`I099`, `I100`) hoặc bài đăng Familia (`L203`).',
                 match_exact(['B001', 'B002', 'B003', 'B100', 'B101', 'B102', 'B300'])),
                ('3.2 Bảng xếp hạng & Nhiệm vụ (Ranking & Missions)',
                 'Bảng xếp hạng Ranker (`B103`), Gifter (`B104`), Dolls (`B104`) và danh sách Nhiệm vụ GĐ1+2, GĐ3 (`B200`).',
                 'Kiểm tra tính toán điểm xếp hạng theo kỳ (ngày/tuần/tháng), tiến độ hoàn thành nhiệm vụ và nhận thưởng tự động.',
                 'Liên kết với `K901` (Dolls Ranking), `K902` (Gifter Ranking).',
                 lambda it: True),
            ]
        elif mod_title.startswith('4.'):
            rules = [
                ('4.1 Tìm kiếm Tổng hợp (Search Top)',
                 'Màn hình tìm kiếm người dùng, livestream, bài đăng hoặc từ khóa (`C100`).',
                 'Kiểm tra tìm kiếm ký tự đặc biệt/tiếng Nhật, lịch sử tìm kiếm, phân loại kết quả theo tab và chặn hiển thị user đã Block (`K207`).',
                 'Liên kết với `D100` (Profile), `I100` (Livestream), `K207` (Block).',
                 lambda it: True),
            ]
        elif mod_title.startswith('5.'):
            rules = [
                ('5.1 Hồ sơ Người khác, Ghi chú, Nhạc yêu thích & Báo cáo/Block',
                 'Xem hồ sơ (`D100`), menu chức năng mở rộng (`D202`), luồng báo cáo đối tượng/lý do/chi tiết (`D2021-D2023`), ghi chú cá nhân về user (`D203`), lịch sử hát & bài hát/ca sĩ yêu thích (`D301`, `D3021`, `D3022`), cài đặt thông báo (`D500`) và danh sách Soldier (`D600`).',
                 'Kiểm tra logic Block/Unblock, Report gửi lên Admin (`AI100`)/Agency (`BG100`), bật/tắt thông báo theo từng user đồng bộ với `K2044`.',
                 'Liên kết với Admin (`AI100`), Agency (`BG100`), My Page (`K2044`, `K207`).',
                 match_exact(['D100', 'D202', 'D2021', 'D2022', 'D2023', 'D203', 'D301', 'D3021', 'D3022', 'D500', 'D600'])),
                ('5.2 Video Lưu trữ (Archive) của Người khác',
                 'Danh sách Archive (`D701`), chi tiết phát video (`D702`), chọn ngôn ngữ phụ đề (`D703`), tốc độ phát (`D704`) và bình luận Archive (`D705`).',
                 'Kiểm tra quyền xem Archive (public vs follower/familia), đồng bộ phụ đề đa ngôn ngữ, đổi tốc độ phát mượt mà và gửi/xem bình luận.',
                 'Dữ liệu Archive được cấu hình quyền hiển thị từ chủ sở hữu tại `K9051-K9054`.',
                 lambda it: True),
            ]
        elif mod_title.startswith('6.'):
            rules = [
                ('6.1 Thông báo Hệ thống, Hoạt động & Push Notification',
                 'Danh sách thông báo (`E201`), chi tiết thông báo (`E202`), bản Webview trong live (`I8042`), danh sách hoạt động (`E203`) và thanh Push Noti UI (`E203`).',
                 'Kiểm tra trạng thái đã đọc/chưa đọc (badge count), deep link khi bấm vào thông báo đẩy, nội dung thông báo đồng bộ từ Admin (`AH100-AH301`).',
                 'Nhận dữ liệu từ Admin (`AH100-AH301`) và cấu hình tại `K204`.',
                 lambda it: True),
            ]
        elif mod_title.startswith('7.'):
            rules = [
                ('7.1 Hòm thư, Chat 1-1 & Yêu cầu 2-Shot qua Tin nhắn',
                 'Danh sách hội thoại (`F100`), tạo chat 1-1 (`F200`), chat 1-1 (`F101`), gửi lời mời 2-shot (`F1011`), cài đặt chat & block (`F1012`, `F10121`), tin nhắn hệ thống (`F103`), tin nhắn của tôi (`F104`), xem trước chưa đọc (`F400`) và gửi Stamp (`F500`).',
                 'Kiểm tra quyền nhắn tin (`K400` Message Access & tham gia Familia), logic chặn nhận tin từ user bị Block, nhận/từ chối lời mời 2-shot và hiển thị Stamp.',
                 'Liên kết với `K400`, `K207`, Admin (`AX100-AX300`), Agency (`BX100`).',
                 match_exact(['F100', 'F101', 'F1011', 'F1012', 'F10121', 'F103', 'F104', 'F200', 'F400', 'F500'])),
                ('7.2 Nhóm Chat (Group Message & Quản lý thành viên)',
                 'Tạo nhóm chat (`F300`), màn hình chat nhóm (`F102`), cài đặt nhóm của chủ phòng (`F1021`), thêm thành viên (`F1022`), xem thành viên (`F1023`), rời nhóm (`F1024`, `F1025`).',
                 'Kiểm tra quyền Owner vs Member (thêm/xóa thành viên, giải tán nhóm khi Owner rời), cập nhật tin nhắn realtime cho tất cả thành viên.',
                 'Liên kết với Admin (`AX100-AX300`).',
                 lambda it: True),
            ]
        elif mod_title.startswith('8.'):
            rules = [
                ('8.1 Cửa hàng Tổng hợp, Vé (Ticket) & Lịch sử Point/Coin',
                 'Trang chủ Shop (`G100`), đổi vé (`G401`), lịch sử vé (`G402`), lịch sử Point/Coin trên App & Web (`G600`), nạp Point trên App (`G701`) và Web (`G702`).',
                 'Kiểm tra thanh toán IAP (Apple/Google) và Web Payment, cộng số dư ngay sau khi thanh toán, trừ tiền đúng thứ tự Coin trả phí / miễn phí, ghi nhận log `G600`.',
                 'Đối chiếu với Admin Billing (`AE500`, `AE600`) và Revenue (`AS100`).',
                 match_exact(['G100', 'G401', 'G402', 'G600', 'G701', 'G702'])),
                ('8.2 Gói Hội viên Hàng tháng (Monthly Plans)',
                 'Danh sách gói tháng (`G501`), Monthly Pass và chi tiết các hạng Silver, Gold, Royal, Platinum (`G5021`).',
                 'Kiểm tra quyền lợi từng hạng, tự động gia hạn (auto-renew), nâng/hạ hạng và hủy gói; đồng bộ trạng thái gói lên Admin (`AE500`) và Agency (`BD300`).',
                 'Liên kết với Admin (`AE500`) và Agency (`BD300`).',
                 match_exact(['G501', 'G5021'])),
                ('8.3 Gacha tại Shop & Trong Livestream, Đổi Mảnh (Fragment)',
                 'Danh sách & chi tiết Gacha tại Shop (`G200`, `G201`), đổi mảnh Fragment (`G301`, `G302`), và Gacha trong lúc đang livestream (`G200-G203` Streamer View).',
                 'Kiểm tra trừ Coin/Ticket khi quay x1/x10, cộng vật phẩm/mảnh vào kho đồ, xử lý hiệu ứng chờ kết quả (`G203`) và hiển thị kết quả (`G202`).',
                 'Cấu hình pool & tỷ lệ từ Admin (`AQ100-AQ500`, `A209`).',
                 lambda it: True),
            ]
        elif mod_title.startswith('9.'):
            rules = [
                ('9.1 Vào phòng Live, Chế độ phòng & Khóa Familia/Soldier',
                 'Phòng chờ Standby (`I099`), phòng Live thường (`I100`), khóa Familia (`I202`), màn hình Familia (`I203`), và điều kiện cấp độ Soldier (`I104` Level 1/2).',
                 'Kiểm tra điều kiện vào phòng (phòng khóa Familia chỉ thành viên mới vào được, đạt Soldier Level mới xem/tương tác), chuyển trạng thái Standby -> Live -> End mượt mà.',
                 'Tương ứng với luồng phát của Streamer (`M100_final`, `M200`, `M500`).',
                 match_exact(['I099', 'I100', 'I202', 'I203', 'I104'])),
                ('9.2 Chế độ 2-Shot (Đăng ký, Phòng riêng, Khóa, Gia hạn & Kết nối lại)',
                 'Xác nhận/đăng ký 2-shot (`I301`), phòng 2-shot (`I303`), 2-shot Lock (`I302`), chuyển sang 2-shot Lock (`I305`), gia hạn 2-shot (`I304`), kết nối lại khi rớt mạng (`I3031`), xác nhận kết thúc (`I303`) và chế độ Broadcast (`I306`).',
                 'Kiểm tra trừ Coin/Ticket khi được Streamer duyệt, đếm ngược thời gian 2-shot, gia hạn thêm giờ không bị ngắt âm thanh/hình ảnh, reconnect lại đúng phiên `I3031`.',
                 'Phối hợp 2 chiều với Streamer (`M300`, `M3001`, `M3002`, `M302`).',
                 match_exact(['I301', 'I302', 'I303', 'I3031', 'I304', 'I305', 'I306'])),
                ('9.3 Tương tác Khán giả (Chat, Whisper, Profile, Danh sách Listener)',
                 'Danh sách khán giả (`I103`), tùy chọn bình luận (`I1013`), tùy chọn màn hình (`I1014`), chat thầm Whisper (`I402`), modal xem profile Viewer (`I1011`) và profile Streamer (`I1012`).',
                 'Kiểm tra gửi chat thường & Whisper chat realtime, ẩn UI khi chọn Screen Option, xử lý user bị Ban chat từ Admin/Agency/Streamer.',
                 'Liên kết với Admin (`AY100-AY300`), Agency (`BY100`, `BY300`) và Streamer (`M201`, `M203`).',
                 match_exact(['I103', 'I1011', 'I1012', 'I1013', 'I1014', 'I402'])),
                ('9.4 Quà tặng, Gift Gacha & Hiệu ứng Quà cao cấp',
                 'Danh sách quà tặng (`I600`), chế độ hiệu ứng quà cao cấp (`I601`), Gift Gacha (`I700`) và xác nhận Gift Gacha (`I701`).',
                 'Kiểm tra gửi quà trừ đúng số dư, hiển thị animation/combo quà trên màn hình cả Viewer và Streamer, không lag/crash khi nhận nhiều quà cùng lúc.',
                 'Cấu hình quà từ Admin (`AF100-AF500`) và thống kê tại `K9091A`, `K909`.',
                 match_exact(['I600', 'I601', 'I700', 'I701'])),
                ('9.5 Hộp Kho báu (Treasure Box)',
                 'Chi tiết hộp kho báu (`I1021`), lịch sử gửi (`I1022`), tùy chỉnh hộp (`I1023`), danh sách hộp đang mở (`I1024`), hoạt ảnh mở hộp (`I1024`), kết quả (`I1025`) và danh sách người trúng (`I1026`).',
                 'Kiểm tra điều kiện mở hộp (đếm ngược/comment), giới hạn số người trúng, cộng thưởng Coin/Point chính xác cho người trúng và đồng bộ lịch sử (`K9093`).',
                 'Liên kết với Điều khoản `A207` và My Page `K9093`.',
                 match_exact(['I1021', 'I1022', 'I1023', 'I1024', 'I1025', 'I1026'])),
                ('9.6 Karaoke Khán giả (Tìm kiếm, Yêu cầu bài hát & Chấm điểm)',
                 'Chế độ Karaoke (`I501`), cài đặt Karaoke (`I502`), tìm bài theo từ khóa/phổ biến/thập niên/chi tiết (`I5031-I5034`), tìm ca sĩ & bài của ca sĩ (`I5041-I5042`), danh sách yêu thích (`I5051-I5052`), lịch sử hát (`I507`), chấm điểm (`I508`) và gửi yêu cầu bài hát cho Streamer (`I509`).',
                 'Kiểm tra đồng bộ lời bài hát (lyric timing) giữa Streamer và Viewer, gửi Song Request (`I509`) sang hàng đợi của Streamer (`M403`).',
                 'Liên kết với Admin Karaoke (`AL100-AL400`) và Streamer Karaoke (`M401-M409`).',
                 match_exact(['I501', 'I502', 'I5031', 'I5032', 'I5033', 'I5034', 'I5041', 'I5042', 'I5051', 'I5052', 'I507', 'I508', 'I509'])),
                ('9.7 Cài đặt trong Phòng Live & Picture-in-Picture (PiP)',
                 'Menu cài đặt tổng hợp (`I800`), âm lượng mic (`I802`), âm lượng đối phương (`I803`), thông báo (`I804`, `I8041`), đồ họa (`I805`), và chế độ PiP ngoài/trong app (`CMR 63 - I1001`).',
                 'Kiểm tra giữ âm thanh/hình ảnh mượt khi thu nhỏ PiP trong và ngoài app, chỉnh âm lượng/đồ họa có tác dụng tức thì không làm văng phòng.',
                 'Liên kết với Streamer Settings (`M205*`) và `CMR63`.',
                 lambda it: True),
            ]
        elif mod_title.startswith('10.'):
            rules = [
                ('10.1 Thiết lập Model 3D, Trang phục & Hình nền Ban đầu (Initial Setup)',
                 'Chọn model (`M0011`), chỉnh đầu (`M00111`), ngoại hình (`M00112`, `M00113`), biểu cảm (`M00114`), trang phục (`M0012`, `M00121`) và hình nền lần đầu (`M00131`).',
                 'Kiểm tra lưu preset model/trang phục không bị mất khi thoát app, render avatar 3D đúng tỷ lệ, không xung đột phụ kiện.',
                 'Dùng dữ liệu Model từ Admin (`AP000-AP400`) và Background (`AK201-AK203`).',
                 match_exact(['M0011', 'M00111', 'M00112', 'M00113', 'M00114', 'M0012', 'M00121', 'M00131'])),
                ('10.2 Chuẩn bị trước khi Phát sóng (Prepare to Stream)',
                 'Màn hình Prepare TOP (`M100_final`), chọn độ phân giải (`M100`), chọn chủ đề Topic (`M1012`), chọn/thêm quà Wishlist (`M1011`), kiểm tra mời 2-shot (`M102`).',
                 'Kiểm tra cấu hình độ phân giải tương thích thiết bị, lưu Topic & Wishlist hiển thị đúng ngay khi bấm Go Live.',
                 'Độ phân giải cấu hình tại Admin (`AP000`).',
                 match_exact(['M100_final', 'M100', 'M1011', 'M1012', 'M102'])),
                ('10.3 Điều hành Phòng Live & Các Chế độ Phát (Normal/Test/Familia/Broadcast/PiP)',
                 'Phát thường (`M200`), phát thử nghiệm (`M199`), chế độ Familia (`M500`), xác nhận & chuyển sang Broadcast (`M2071`, `M2073`), tùy chọn màn hình (`M2001`), đổi tiêu đề (`CMR64`), danh sách khán giả (`M203`), PiP cho streamer (`PIP streamer`, `CMR 63 - I1001`).',
                 'Kiểm tra chuyển đổi qua lại giữa Normal <-> Familia <-> Broadcast không rớt stream; chế độ Test (`M199`) không gửi thông báo push tới follower.',
                 'Tương tác 2 chiều với Viewer (`I100`, `I202`, `I203`, `I306`) và Admin (`AG100-AG400`).',
                 match_exact(['M200', 'M199', 'M500', 'M2071', 'M2073', 'M2001', 'CMR64', 'M203', 'PIP streamer', 'CMR 63 - I1001'])),
                ('10.4 Quản lý 2-Shot phía Streamer (Approve, Reconnect, Extend)',
                 'Danh sách yêu cầu 2-shot (`M302`), phòng 2-shot (`M300`), xử lý 2-shot dang dở/quay lại (`M3001`) và xử lý gia hạn 2-shot (`M3002`).',
                 'Kiểm tra duyệt/từ chối yêu cầu trong `M302`, tự động chuyển phòng sang 2-shot, xử lý khi 1 trong 2 bên rớt mạng và đồng ý gia hạn.',
                 'Phối hợp 2 chiều với Viewer (`I301-I305`).',
                 match_exact(['M300', 'M3001', 'M3002', 'M302'])),
                ('10.5 Công cụ Tương tác & Cài đặt Âm thanh/Hình ảnh trong Live',
                 'Menu cài đặt (`M205`), trả lời & lịch sử Whisper (`M201`, `M203`), đổi trang phục/ngoại hình/nền (`M20501`, `M20502`, `M20504`), bảng thông báo (`M20506`), cập nhật Wishlist (`M20507`), đổi Topic (`M2055`), chia sẻ (`M206`), Emote & Biểu cảm (`M2061`, `M2062`), thông báo (`M20515`), đồ họa (`M20516`), âm thanh/mic/echo/voice changer/BGM/voice monitor (`M20510-M20514`, `M20518`, CR Voice Monitor) và thống kê follow (`CMR60`).',
                 'Kiểm tra đổi trang phục/nền/voice changer/BGM realtime hiển thị & phát đúng sang phía Viewer; kiểm tra Voice Monitor không bị vọng âm.',
                 'Dùng BGM từ `AJ100`, Background từ `AK201`, Gift từ `AF100`.',
                 match_exact(['M205', 'M201', 'M203', 'M20501', 'M20502', 'M20504', 'M20506', 'M20507', 'M2055', 'M206', 'M2061', 'M2062', 'M20510', 'M20511', 'M20512', 'M20513', 'M20514', 'M20515', 'M20516', 'M20518', 'CMR60', '-'])),
                ('10.6 Karaoke Streamer & Đề xuất Bài hát mới',
                 'Chế độ Karaoke (`M401`), cài đặt (`M402`), danh sách yêu cầu hát (`M403`), tìm bài & ca sĩ (`M4041-M4044`, `M4051-M4052`), yêu thích (`M4061-M4062`), đề xuất bài mới chưa có (`M4071`, `M4072`), lịch sử hát (`M408`) và chấm điểm (`M409`).',
                 'Kiểm tra nhận bài từ Viewer (`I509`), phát beat & sync lyric, gửi đề xuất bài mới (`M4071`) lên Admin (`AL400`).',
                 'Liên kết với Admin (`AL100-AL400`) và Viewer (`I501-I509`).',
                 match_exact(['M401', 'M402', 'M403', 'M4041', 'M4042', 'M4043', 'M4044', 'M4051', 'M4052', 'M4061', 'M4062', 'M4071', 'M4072', 'M408', 'M409'])),
                ('10.7 Phát sóng qua OBS (OBS Normal / Familia / 2-Shot / Viewer)',
                 'Hỗ trợ phát và xem livestream qua OBS ở các chế độ Normal, Familia, 2-shot và Viewer All Mode (`OBS`).',
                 'Kiểm tra stream key/RTMP kết nối ổn định, đồng bộ avatar/audio từ OBS sang App Viewer ở mọi chế độ.',
                 'Tương thích với các phòng Viewer (`I100`, `I202`, `I303`).',
                 lambda it: True),
            ]
        elif mod_title.startswith('11.'):
            rules = [
                ('11.1 Hồ sơ Cá nhân (My Page Core, Edit, Rank & Danh hiệu)',
                 'Trang cá nhân (`K000`), xem ảnh toàn màn hình (`K001`), chỉnh sửa hồ sơ & ngày sinh (`K800`), cắt ảnh đại diện & ảnh bìa (`K801`, `K802`), xem Rank (`K908`) và danh sách Danh hiệu (`K500`).',
                 'Kiểm tra upload/crop ảnh, validate độ dài bio/nickname, tính điểm lên hạng Rank (`K908`) và gắn danh hiệu (`K500`).',
                 'Hiển thị công khai sang `D100` (Other User Profile).',
                 match_exact(['K000', 'K001', 'K800', 'K801', 'K802', 'K908', 'K500'])),
                ('11.2 Cài đặt Tài khoản, SĐT, Liên kết SNS, eKYC & Block',
                 'Menu cài đặt (`K100`), cài đặt tài khoản & Facebook (`K202`), liên kết/đổi SĐT & chọn mã quốc gia/OTP (`K2025`), gỡ liên kết SNS (`K20241`, `K20242`), đăng xuất (`K2021`), xóa tài khoản (`K2022`), xác thực danh tính eKYC (`K205`), danh sách bạn SNS/danh bạ (`K206`), danh sách chặn & logic Block (`K207`).',
                 'Kiểm tra không cho gỡ SNS cuối cùng (`K20242`), điều kiện xóa tài khoản (không còn gói tháng/số dư/payout pending), logic Block ẩn toàn bộ tương tác 2 chiều.',
                 'Liên kết với Admin (`AE700`, `K2022`) và Login (`A100`).',
                 match_exact(['K100', 'K202', 'K2021', 'K2022', 'K20241', 'K20242', 'K2025', 'K205', 'K206', 'K207'])),
                ('11.3 Liên kết Agency (Tham gia / Rời khỏi Agency)',
                 'Đăng ký tham gia Agency hoặc xác nhận rời khỏi Agency (`K203`).',
                 'Kiểm tra nhập mã Agency hợp lệ, trạng thái chờ duyệt/đã duyệt/từ chối và ràng buộc khi đang còn doanh thu/yêu cầu rút tiền.',
                 'Liên kết trực tiếp với Agency (`BC100`, `BC200`) và Admin (`AD302`).',
                 match_exact(['K203'])),
                ('11.4 Cài đặt Thông báo Đẩy (Push Notification Settings)',
                 'Cài đặt thông báo chung (`K204`), cài đặt theo người đang follow (`K2041`), bật/tắt hàng loạt (`K2042`, `K2043`) và cài đặt riêng từng user (`K2044`).',
                 'Kiểm tra toggle từng mục & bật/tắt hàng loạt đồng bộ tức thì với `D500` và backend push notification.',
                 'Liên kết với `D500` và `E203`.',
                 match_exact(['K204', 'K2041', 'K2042', 'K2043', 'K2044'])),
                ('11.5 Kết nối Xã hội, Familia, Soldier & Quyền Nhắn tin',
                 'Danh sách Dolls yêu thích (`K3011`), Soldier Level (`K3012`), Familia đã tham gia (`K302`), thành viên Familia (`K701`), Follower/Following (`K702`), quyền nhắn tin (`K400`), nhà tài trợ (`K208` List of Sponsors) và giới thiệu app (`K208`).',
                 'Kiểm tra đồng bộ số lượng follower/following, quyền nhắn tin `K400` áp dụng đúng vào `F101`/`F200`.',
                 'Liên kết với `D600`, `F200`, `L100-L500`.',
                 match_exact(['K3011', 'K3012', 'K302', 'K701', 'K702', 'K400', 'K208'])),
                ('11.6 Quản lý GOLD, Đổi Point & Lịch Thưởng (Reward Calendar)',
                 'Số dư & thông tin GOLD (`K601`), đổi GOLD sang Point (`K6012`), lịch sử đổi (`K6013`) và Lịch nhận thưởng (`K602`).',
                 'Kiểm tra tỷ giá đổi GOLD -> Point, trừ GOLD và cộng Point nguyên tử (atomic), xử lý logic đóng tài khoản khi còn GOLD.',
                 'Liên kết với Admin (`AE800`, `AS300`) và Shop (`G600`).',
                 match_exact(['K601', 'K6012', 'K6013', 'K602'])),
                ('11.7 Tài khoản Nhận tiền & Yêu cầu Rút tiền (Payout)',
                 'Liên kết tài khoản ngân hàng (`K906`), xem trước (`K9061`), xác thực OTP (`K9062`), xác nhận (`K9063`), lịch sử tất cả (`K9064`), yêu cầu rút tiền tức thì (`K9065`) và lịch sử chi trả thành công (`K9066`).',
                 'Kiểm tra bắt buộc hoàn tất eKYC (`K205`) trước khi rút tiền, validate thông tin ngân hàng, hạn mức rút tối thiểu/tối đa, trạng thái yêu cầu đồng bộ với Admin (`AS200`).',
                 'Liên kết chặt với Admin (`AS200`, `AE700`).',
                 match_exact(['K906', 'K9061', 'K9062', 'K9063', 'K9064', 'K9065', 'K9066'])),
                ('11.8 Thống kê LIVE, Bảng Xếp hạng & Nhật ký Tương tác',
                 'Tổng quan phân tích LIVE (`K9071`), chọn lịch (`K9072`), danh sách phiên (`K9073`), chi tiết phiên (`K9074`), danh sách người xem (`K9075`); xếp hạng Dolls/Gifter (`K901`, `K902`); nhật ký người gửi quà/Gift Gacha/2-shot/Kho báu/Follower/Familia/Whisper (`K909`, `K9091A`, `K9092-K9096`), Likes (`K903`) và Keeps (`K904`).',
                 'Kiểm tra độ chính xác số liệu thống kê (viewer, thời lượng, quà, GOLD nhận được) khớp với phiên live thực tế và dữ liệu DB.',
                 'Liên kết với `B103-B104`, `AE800`, `BD500`.',
                 match_exact(['K9071', 'K9072', 'K9073', 'K9074', 'K9075', 'K901', 'K902', 'K903', 'K904', 'K909', 'K9091A', 'K9092', 'K9093', 'K9094', 'K9095', 'K9096'])),
                ('11.9 Quản lý Video Lưu trữ Cá nhân (My Archive)',
                 'Danh sách Archive của tôi (`K9051` - không cho download video có gắn karaoke), chi tiết (`K9052`), cài đặt công khai (`K9053`) và tùy chọn Archive (`K9054`).',
                 'Kiểm tra rule cấm tải xuống video có chứa nhạc Karaoke, cài đặt quyền riêng tư (Public/Familia/Private) phản ánh đúng sang `D701`.',
                 'Liên kết với `D701-D705`, Admin (`AG500`), Agency (`BF300`).',
                 match_exact(['K9051', 'K9052', 'K9053', 'K9054'])),
                ('11.10 Karaoke Cá nhân & Báo cáo Bài hát đã sử dụng (ACRCloud)',
                 'Kho Karaoke trên My Page (`K010`), lịch sử hát (`K011`), tìm bài & ca sĩ (`K0121-K0124`, `K0131-K0132`), danh sách yêu thích (`K0141-K0142`), và luồng báo cáo bài hát sử dụng ACRCloud (`K209-New` Xem/Tạo/Sửa).',
                 'Kiểm tra nhận diện/báo cáo bài hát bản quyền (`K209-New`) đồng bộ chính xác lên Admin (`AL600`, `AL700`).',
                 'Liên kết với Admin (`AL600`, `AL700`) và Karaoke Live (`M401`, `I501`).',
                 lambda it: True),
            ]
        elif mod_title.startswith('12.'):
            rules = [
                ('12.1 Trang chủ Familia, Khám phá & Tìm kiếm',
                 'Trang chủ Familia (`L100`), bài mới từ Familia đã tham gia (`L1001`), Familia mới nổi bật (`L1002`), bài mới nổi bật (`L1003`), bảng xếp hạng bài đăng ngày (`L1004`), tìm kiếm theo Familia/Bài đăng/Tag (`L1021-L1023`).',
                 'Kiểm tra phân loại feed đúng Familia đã join vs gợi ý, tìm kiếm chính xác theo tag và thứ hạng daily ranking.',
                 'Điều hướng tới `L200-L203` (Other Familia) hoặc `L300` (My Familia).',
                 match_exact(['L100', 'L1001', 'L1002', 'L1003', 'L1004', 'L1021', 'L1022', 'L1023'])),
                ('12.2 Quản lý Giới thiệu & Mục tiêu Yell của My Familia',
                 'Xem/sửa trang giới thiệu (`L300`, `L301`, `L302`), upload portfolio (`L303`), danh sách mục tiêu (`L3041`), tạo/sửa mục tiêu (`L3042`, `L3043`) và danh sách người ủng hộ Yell (`L3044`).',
                 'Kiểm tra upload media portfolio, tiến độ thanh mục tiêu Yell cập nhật realtime khi có user donate ở `L201`.',
                 'Liên kết với `L200`, `L201` (Other Familia Donate).',
                 match_exact(['L300', 'L301', 'L302', 'L303', 'L3041', 'L3042', 'L3043', 'L3044'])),
                ('12.3 Quản lý Bài đăng, Tag & Bình luận của My Familia',
                 'Gợi ý tag (`L401`), danh sách bài đăng (`L402`), tạo bài & thêm nội dung/upload file (`L403`, `L4041`, `L4042`), chi tiết bài (`L405`), chỉnh sửa/xóa bài & nội dung (`L406`, `L4061`) và bình luận bài đăng (`L407`).',
                 'Kiểm tra phân quyền xem bài theo Class/Backnumber, upload đa phương tiện (ảnh/video/audio), xóa/sửa bài đồng bộ sang Admin (`AM100`) và Agency (`BE100`).',
                 'Liên kết với Admin (`AM100-AM200`) và Agency (`BE100-BE200`).',
                 match_exact(['L401', 'L402', 'L403', 'L4041', 'L4042', 'L405', 'L406', 'L4061', 'L407'])),
                ('12.4 Quản lý Hạng thành viên (Class), Stamp & Backnumber của tôi',
                 'Danh sách hạng (`L501`), tạo/sửa hạng (`L502`, `L503`), thêm Stamp độc quyền (`L504`) và danh sách Backnumber của tôi (`L600`).',
                 'Kiểm tra cấu hình giá/quyền lợi từng Class, upload Stamp sử dụng được trong chat (`F500`), bật/tắt bán Backnumber.',
                 'Liên kết với `F500` (Stamp) và `L205-L210` (Other Familia Subscribe/Backnumber).',
                 match_exact(['L501', 'L502', 'L503', 'L504', 'L600'])),
                ('12.5 Xem Familia Người khác, Donate Yell & Trình phát Bài đăng',
                 'Trang giới thiệu (`L200`), ủng hộ Yell (`L201`), danh sách & chi tiết bài đăng (`L202`, `L203`), xem chi tiết bài riêng lẻ (`L2041`), tùy chọn phát (`L2042`), tốc độ phát (`L2043`) và cài đặt phụ đề (`L2044`).',
                 'Kiểm tra trừ Coin/Point khi Donate Yell (`L201`), khóa nội dung trả phí nếu chưa tham gia Class/mua Backnumber, đổi tốc độ và phụ đề video.',
                 'Liên kết với `L300`, `L3044`, `L402`.',
                 match_exact(['L200', 'L201', 'L202', 'L203', 'L2041', 'L2042', 'L2043', 'L2044'])),
                ('12.6 Tham gia Class & Mua Backnumber Familia Người khác',
                 'Danh sách Class (`L205`), đăng ký tham gia Class (`L206`), đổi Class (`L207`), hủy đăng ký (`L208`), danh sách Backnumber (`L209`), mua Backnumber (`L210`) và logic bật/tắt bán Backnumber (`-`).',
                 'Kiểm tra thanh toán khi join Class/mua Backnumber, nâng/hạ hạng (`L207`), hủy gia hạn (`L208`) vẫn giữ quyền đến hết chu kỳ, và ẩn nút mua khi Backnumber sale OFF.',
                 'Liên kết với `L501-L503`, `L600` và Billing (`G600`).',
                 lambda it: True),
            ]

    # Apply rules sequentially (each item goes to first matching subcluster)
    assigned = [False] * len(items)
    result = []
    for title, spec, verify, cross, pred in rules:
        sub_items = []
        for idx, it in enumerate(items):
            if not assigned[idx] and pred(it):
                sub_items.append(it)
                assigned[idx] = True
        if sub_items:
            result.append((title, spec, verify, cross, sub_items))
    return result

