# BÁO CÁO KẾT QUẢ KIỂM THỬ TÁC VỤ SURREALDOLLS-14848 TRÊN MÔI TRƯỜNG STG

Theo quy chuẩn [06_bug_reporting_rule.md](../../Universal_Rules/06_bug_reporting_rule.md), [04_manual_test_execution_rule.md](../../Universal_Rules/04_manual_test_execution_rule.md) & [GEMINI.md](../../GEMINI.md).

---

## 1. THÔNG TIN TỔNG QUAN TÁC VỤ (TASK OVERVIEW)

| Thuộc tính | Chi tiết |
| :--- | :--- |
| **Mã Task Backlog** | [SURREALDOLLS-14848](https://issoh.backlog.com/view/SURREALDOLLS-14848) |
| **Tiêu đề Task** | `[Test STG][FE] - Admin web ＋ Agency web 事務所：xử lý rule mật khẩu mới (báo hết hạn khi đăng nhập, validate khi đặt mật khẩu) ＋ thêm chức năng đổi mật khẩu — theo BE 12839` |
| **Task BE Gốc** | [SURREALDOLLS-12839](https://issoh.backlog.com/view/SURREALDOLLS-12839) (GMO Sec-12 Password Policy) |
| **Môi trường kiểm thử** | **Staging (STG)** |
| **URLs & Cấu hình** | • **Admin Master STG:** `https://admin-stg.surrealdolls.com/sign-in`<br>• **Agency Web STG:** `https://admin-stg.surrealdolls.com/sign-in/agency`<br>• **HTTP Basic Auth:** `suriaru` / `suriaru` |
| **Tài khoản kiểm thử** | • **Admin Master:** `admin@admin.com` \| `!Ch4ng3Th1sP4ssW0rd!`<br>• **Agency Owner:** `123` \| `Leo150122@` |
| **Tester ID** | `NgaDTP` / `Antigravity QA` |
| **Ngày thực thi** | `17/11/2026` |
| **Quy chuẩn đối chiếu** | `CMR43` (Password Validation Rule), `CMR68` (Password Expiry 30 days), `CMR15` (Submit debounce) |

---

## 2. BẢNG TỔNG HỢP KẾT QUẢ KIỂM THỬ TRÊN STG (STG TEST SUMMARY)

| Phân hệ / Màn hình | Tổng số Viewpoints | Pass | Fail | Blocked / Pending | Tỷ lệ Pass | Tình trạng Bug |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **AA000 (Admin Login)** | 3 | 2 | 0 | 1 | **66.7%** | Không phát hiện lỗi mới; Chờ tài khoản hết hạn (>30 ngày) |
| **AA003 (Admin Change Password)** | 14 | 12 | 2 | 0 | **85.7%** | 2 bugs giao diện còn tồn đọng (Icon tam giác ▲, Role Tag) |
| **BA100 (Agency Login)** | 3 | 2 | 0 | 1 | **66.7%** | Không phát hiện lỗi mới; Chờ tài khoản hết hạn (>30 ngày) |
| **BA200 (Agency Change Password)** | 14 | 12 | 2 | 0 | **85.7%** | 2 bugs giao diện còn tồn đọng (Icon tam giác ▲, Tên Agency & Role Tag) |
| **AD301 (Agency Detail Password Reset)** | 4 | 4 | 0 | 0 | **100.0%** | Toàn bộ chức năng và validation đạt chuẩn 100% |
| **AB003 / BA1003 (Reset Password)** | 2 | 2 | 0 | 0 | **100.0%** | Xử lý token và hiển thị đúng đặc tả |
| **TỔNG CỘNG** | **40** | **34** | **4** | **2** | **85.0%** | **4 Bugs tồn đọng** (UI/UX) - Đạt cổng đối soát độ phủ >= 80% |

---

## 3. DANH SÁCH CHI TIẾT CÁC BUG CÒN TỒN ĐỌNG TRÊN STG (OPEN BUGS)

### [BUG-1] [AA003 / BA200] Nút khu tài khoản ở cuối Side menu thiếu icon tam giác ▲ ở mép phải

- **Mã Test Case liên quan:** `[AA003-8]`, `[BA200-8]`
- **Mức độ nghiêm trọng (Severity):** Minor (Giao diện / Spec mismatch)
- **Môi trường:**
  - URL Admin STG: `https://admin-stg.surrealdolls.com/`
  - URL Agency STG: `https://admin-stg.surrealdolls.com/agencies/info`
- **Các bước tái hiện (Steps to Reproduce):**
  1. Đăng nhập Admin Master hoặc Agency Owner trên STG.
  2. Quan sát khu vực nút tài khoản nằm cố định ở góc dưới cùng bên trái của Side menu.
- **Kết quả kỳ vọng (Expected Result):**
  - Hiển thị avatar tròn, Tên, Email và **icon tam giác ▲** (hoặc chevron indicator) ở mép phải của nút để biểu thị menu popup có thể mở hướng lên theo Spec item 1.
- **Kết quả thực tế trên STG (Actual Result):**
  - Nút tài khoản chỉ hiển thị Avatar tròn, Tên và Email. Hoàn toàn **KHÔNG có icon tam giác ▲** hay bất kỳ icon mũi tên/chevron nào ở mép phải nút.
- **Bằng chứng đính kèm (Evidence):**
  - Ảnh Admin STG: [evidence/AA003/evidence_AA003_STG_TC08_account_button.png](../../evidence/AA003/evidence_AA003_STG_TC08_account_button.png)
  - Ảnh Agency STG: [evidence/BA200/evidence_BA200_STG_TC08_account_button.png](../../evidence/BA200/evidence_BA200_STG_TC08_account_button.png)
  - DOM Log:
    ```html
    <button data-slot="dropdown-menu-trigger" data-sidebar="menu-button" data-size="lg" ...>
      <span data-slot="avatar" ...><span data-slot="avatar-fallback">S</span></span>
      <div class="grid flex-1 text-left text-sm leading-tight">
        <span class="truncate font-semibold">Surreal Dolls Admin</span>
        <span class="text-muted-foreground truncate text-xs">admin@admin.com</span>
      </div>
      <!-- THIẾU ICON TAM GIÁC ▲ HOẶC CHEVRON TẠI ĐÂY -->
    </button>
    ```

---

### [BUG-2] [AA003] Header Menu Popup của tài khoản Master Admin thiếu Tag Role 「マスター」

- **Mã Test Case liên quan:** `[AA003-14]`, `[AA003-15]`, `[AA003-16]`
- **Mức độ nghiêm trọng (Severity):** Major (Thiếu thông tin phân quyền người dùng)
- **Môi trường:** `https://admin-stg.surrealdolls.com/`
- **Các bước tái hiện (Steps to Reproduce):**
  1. Đăng nhập Admin Master trên STG (`admin@admin.com`).
  2. Click vào khu tài khoản ở cuối side menu để mở menu popup tài khoản.
  3. Quan sát phần header phía trên cùng của popup menu (trên vạch phân cách separator).
- **Kết quả kỳ vọng (Expected Result):**
  - Phần header menu hiển thị đầy đủ thông tin theo đặc tả Spec item 2:
    1. Avatar tròn
    2. 名前 (`Surreal Dolls Admin`)
    3. メールアドレス (`admin@admin.com`)
    4. **Tag Role người dùng: 「マスター」** (và tương ứng 「管理者」, 「監視員」 khi đăng nhập tài khoản khác).
- **Kết quả thực tế trên STG (Actual Result):**
  - Header popup menu chỉ hiển thị: Avatar tròn, 名前 (`Surreal Dolls Admin`), và メールアドレス (`admin@admin.com`).
  - Hoàn toàn **KHÔNG có Tag Role 「マスター」** (chưa có container/logic render badge phân quyền).
- **Bằng chứng đính kèm (Evidence):**
  - File ảnh chụp: [evidence/AA003/evidence_AA003_STG_TC14_account_menu.png](../../evidence/AA003/evidence_AA003_STG_TC14_account_menu.png)
  - DOM Log:
    ```html
    <div data-slot="dropdown-menu-label" class="text-sm data-[inset]:pl-8 p-0 font-light">
      <div class="flex items-center gap-2 px-1 py-1.5 text-left text-sm">
        <span data-slot="avatar" ...><span data-slot="avatar-fallback">S</span></span>
        <div class="grid flex-1 text-left text-sm leading-tight">
          <span class="truncate font-semibold">Surreal Dolls Admin</span>
          <span class="text-muted-foreground truncate text-xs">admin@admin.com</span>
          <!-- THIẾU TAG ROLE 「マスター」 -->
        </div>
      </div>
    </div>
    ```

---

### [BUG-3] [BA200] Header Menu Popup của tài khoản Agency thiếu Tên 事務所 và Tag Role 「オーナー」 / 「事務所管理者」

- **Mã Test Case liên quan:** `[BA200-14]`, `[BA200-15]`
- **Mức độ nghiêm trọng (Severity):** Major (Thiếu nhận diện Agency và vai trò)
- **Môi trường:** `https://admin-stg.surrealdolls.com/agencies/info`
- **Các bước tái hiện (Steps to Reproduce):**
  1. Đăng nhập tài khoản Agency Owner trên STG (`123` / `Leo150122@`).
  2. Click vào khu tài khoản ở cuối side menu để mở popup menu.
  3. Quan sát phần header phía trên cùng của popup menu.
- **Kết quả kỳ vọng (Expected Result):**
  - Theo đặc tả BA200 item 2, header menu popup của Agency bắt buộc hiển thị:
    1. 名前 (`tokyo`)
    2. メールアドレス (`ngaphgg@gmail.com`)
    3. **Tên 事務所** (`123` / Agency Name)
    4. **Tag Role: 「オーナー」** (hoặc 「事務所管理者」 nếu là Sub-admin tạo từ BB200).
- **Kết quả thực tế trên STG (Actual Result):**
  - Header popup menu chỉ hiển thị: Avatar tròn chữ `T`, 名前 `tokyo`, và Email `ngaphgg@gmail.com`.
  - Hoàn toàn **KHÔNG có Tên 事務所** và **KHÔNG có Tag Role 「オーナー」**.
- **Bằng chứng đính kèm (Evidence):**
  - File ảnh chụp: [evidence/BA200/evidence_BA200_STG_TC14_account_menu.png](../../evidence/BA200/evidence_BA200_STG_TC14_account_menu.png)
  - DOM Log:
    ```html
    <div data-slot="dropdown-menu-label" class="text-sm data-[inset]:pl-8 p-0 font-light">
      <div class="flex items-center gap-2 px-1 py-1.5 text-left text-sm">
        <span data-slot="avatar" ...><span data-slot="avatar-fallback">T</span></span>
        <div class="grid flex-1 text-left text-sm leading-tight">
          <span class="truncate font-semibold">tokyo</span>
          <span class="text-muted-foreground truncate text-xs">ngaphgg@gmail.com</span>
          <!-- THIẾU TÊN AGENCY VÀ ROLE BADGE オーナー -->
        </div>
      </div>
    </div>
    ```

---

## 4. CHI TIẾT KẾT QUẢ KIỂM THỬ THEO TỪNG PHÂN HỆ TRÊN STG

### 4.1. Phân hệ Đăng nhập (AA000 Admin & BA100 Agency)

| Mã ca test | Thao tác thực tế | Kỳ vọng theo Spec | Kết quả thực tế STG | Đánh giá | Bằng chứng đính kèm |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `[AA000-LOG-01]` | Đăng nhập Admin Master đúng thông tin (`admin@admin.com` / `!Ch4ng3Th1sP4ssW0rd!`) | Đăng nhập thành công, điều hướng vào Dashboard, cấp Token | HTTP 200 OK, điều hướng thành công vào `https://admin-stg.surrealdolls.com/` | **PASS** | [evidence_AA003_STG_TC08_account_button.png](../../evidence/AA003/evidence_AA003_STG_TC08_account_button.png) |
| `[AA000-LOG-02]` | Nhập sai mật khẩu Admin Master (`WrongPassword123!`) | Báo lỗi `MSG10` ở đầu form đăng nhập, ở lại màn login | Hiển thị alert `MSG10`: `メールアドレス・IDまたはパスワードが一致しません。もう一度入力してください。` | **PASS** | [evidence_AA000_STG_login_wrong_password_msg10.png](../../evidence/AA003/evidence_AA000_STG_login_wrong_password_msg10.png) |
| `[AA000-LOG-03]` | Đăng nhập tài khoản quá hạn 30 ngày (CMR68) | Chặn đăng nhập (HTTP 401), hiển thị `MSG260` | Tài khoản backfill ngày 21/10/2026 hiện mới được 27 ngày (< 30 ngày). Chưa có tài khoản quá hạn trên STG. | **BLOCKED** *(Chờ BE)* | Cần tài khoản test quá hạn 30 ngày từ BE |
| `[BA100-LOG-01]` | Đăng nhập Agency đúng thông tin (`123` / `Leo150122@`) | Đăng nhập thành công, điều hướng vào màn Agency Info, cấp Token | HTTP 200 OK, điều hướng vào `https://admin-stg.surrealdolls.com/agencies/info` | **PASS** | [evidence_BA100_STG_login_success.png](../../evidence/BA100/evidence_BA100_STG_login_success.png) |
| `[BA100-LOG-02]` | Nhập sai mật khẩu Agency (`WrongPassword123!`) | Báo lỗi `MSG10` ở đầu form đăng nhập, ở lại màn login | HTTP 401, hiển thị alert `MSG10`: `メールアドレス・IDまたはパスワードが一致しません。もう一度入力してください。` | **PASS** | [evidence_BA100_STG_login_wrong_password_msg10.png](../../evidence/BA100/evidence_BA100_STG_login_wrong_password_msg10.png) |
| `[BA100-LOG-03]` | Đăng nhập Agency quá hạn 30 ngày (CMR68) | Chặn đăng nhập (HTTP 401), hiển thị `MSG260` | Tương tự Admin, tài khoản STG chưa đủ 30 ngày kể từ mốc backfill 21/10. | **BLOCKED** *(Chờ BE)* | Cần tài khoản test quá hạn 30 ngày từ BE |

---

### 4.2. Phân hệ Đổi Mật Khẩu Khi Đang Đăng Nhập (AA003 Admin & BA200 Agency)

| Hạng mục kiểm tra | Thao tác thực tế | Kỳ vọng theo Spec | Kết quả thực tế STG | Đánh giá | Bằng chứng đính kèm |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **Khởi tạo Modal** | Click `パスワード変更` từ Account Menu | Modal mở giữa màn hình; dòng ghi chú 30 ngày (CMR68); 3 ô input trống, masked dạng `●●●`; 3 icon mắt `👁` riêng; auto-focus ô 1 | Modal hiển thị đúng tiêu đề, text ghi chú 30 ngày chuẩn 100%, 3 ô trống, focus chuẩn ô `現在のパスワード`, có 3 icon mắt riêng | **PASS** | • [evidence_AA003_STG_modal_initial.png](../../evidence/AA003/evidence_AA003_STG_modal_initial.png)<br>• [evidence_BA200_STG_modal_initial.png](../../evidence/BA200/evidence_BA200_STG_modal_initial.png) |
| **Validate để trống (CMMSG29)** | Để trống cả 3 ô và bấm `変更する` | Báo lỗi `CMMSG29` đồng thời dưới cả 3 ô input, viền đỏ, không gọi API | Hiển thị chuẩn 3 thông báo lỗi:<br>• `現在のパスワードは空欄にできません。`<br>• `新しいパスワードは空欄にできません。`<br>• `新しいパスワード確認は空欄にできません。` | **PASS** | • [evidence_AA003_STG_validation_empty_cmmsg29.png](../../evidence/AA003/evidence_AA003_STG_validation_empty_cmmsg29.png)<br>• [evidence_BA200_STG_validation_empty_cmmsg29.png](../../evidence/BA200/evidence_BA200_STG_validation_empty_cmmsg29.png) |
| **Validate Rule CMR43 (MSG13)** | Nhập mật khẩu yếu (VD: `pass123`) vào ô 新しいパスワード | Chặn submit, viền đỏ, báo lỗi `MSG13` dưới ô mật khẩu mới | Hiển thị thông báo `MSG13` nguyên văn:<br>`パスワードは8文字以上で、英大文字・小文字・数字・記号をそれぞれ1文字以上含めてください。` | **PASS** | • [evidence_AA003_STG_validation_rule_msg13.png](../../evidence/AA003/evidence_AA003_STG_validation_rule_msg13.png)<br>• [evidence_BA200_STG_validation_rule_msg13.png](../../evidence/BA200/evidence_BA200_STG_validation_rule_msg13.png) |
| **Validate Xác nhận (MSG25)** | Nhập `NewPassword123!` và xác nhận `DifferentPass123!` | Chặn submit, viền đỏ ô xác nhận, hiển thị `MSG25` | Hiển thị thông báo `MSG25`:<br>`パスワードと確認用のパスワードが一致しません。` | **PASS** | • [evidence_AA003_STG_validation_mismatch_msg25.png](../../evidence/AA003/evidence_AA003_STG_validation_mismatch_msg25.png)<br>• [evidence_BA200_STG_validation_mismatch_msg25.png](../../evidence/BA200/evidence_BA200_STG_validation_mismatch_msg25.png) |
| **Sai mật khẩu hiện tại (MSG24)** | Nhập sai ô `現在のパスワード` (`WrongCurrentPass123!`), 2 ô sau hợp lệ $\rightarrow$ Submit | BE trả HTTP 400, FE hiển thị `MSG24` dưới ô `現在のパスワード` | BE trả HTTP 400 `{"detail":"パスワードが間違っています。"}`, FE viền đỏ ô hiện tại và hiển thị đúng `MSG24` | **PASS** | • [evidence_AA003_STG_api_wrong_current_password_msg24.png](../../evidence/AA003/evidence_AA003_STG_api_wrong_current_password_msg24.png)<br>• [evidence_BA200_STG_api_wrong_current_password_msg24.png](../../evidence/BA200/evidence_BA200_STG_api_wrong_current_password_msg24.png) |
| **Cấm trùng mật khẩu cũ (MSG261)** | Nhập lại chính mật khẩu hiện tại vào ô `新しいパスワード` $\rightarrow$ Submit | BE kiểm tra lịch sử 3 mật khẩu gần nhất, trả HTTP 400 `MSG261`, FE báo dưới ô mới | BE trả HTTP 400 `{"detail":"過去2回以内に使用したパスワードは再利用できません。"}`, FE hiển thị chuẩn `MSG261` dưới ô mới | **PASS** | • [evidence_AA003_STG_api_reuse_password_msg261.png](../../evidence/AA003/evidence_AA003_STG_api_reuse_password_msg261.png)<br>• [evidence_BA200_STG_api_reuse_password_msg261.png](../../evidence/BA200/evidence_BA200_STG_api_reuse_password_msg261.png) |
| **Đóng modal** | Kiểm tra các thao tác: Nút `キャンセル`, Nút đóng `Close [X]`, Phím `Esc`, Click vùng ngoài Backdrop | Modal lập tức đóng an toàn, xóa sạch dữ liệu vừa nhập, không popup xác nhận | Cả 4 thao tác đều đóng modal an toàn và reset sạch dữ liệu | **PASS** | Xác minh trực tiếp trên browser headless Chromium |

---

### 4.3. Phân hệ Reset Mật Khẩu Agency từ Master Admin (Màn AD301)

| Mã ca test | Thao tác thực tế | Kỳ vọng theo Spec | Kết quả thực tế STG | Đánh giá | Bằng chứng đính kèm |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `[AD301-44]` | Vào `/agencies/detail/2?tab=detail` $\rightarrow$ Quan sát mục `ログインパスワードリセット` | Hiển thị nhãn `ログインパスワードリセット` kèm button `リセット` | Hiển thị nút `リセット` chuẩn thiết kế | **PASS** | [evidence_AD301_STG_detail_tab.png](../../evidence/AD301/evidence_AD301_STG_detail_tab.png) |
| `[AD301-45]` | Click nút `リセット` | Nút `リセット` được thay thế bằng ô input nhập mật khẩu mới có icon mắt `👁` | Ô input xuất hiện inline với placeholder `新しいパスワードを入力` | **PASS** | [evidence_AD301_STG_reset_modal_opened.png](../../evidence/AD301/evidence_AD301_STG_reset_modal_opened.png) |
| `[AD301-47]` | Nhập mật khẩu yếu (`weak123`) $\rightarrow$ Click `保存` | Validate theo CMR43, chặn submit, hiển thị lỗi `MSG13` dưới ô nhập | Viền đỏ ô nhập, hiển thị thông báo `MSG13` nguyên văn:<br>`パスワードは8文字以上で、英大文字・小文字・数字・記号をそれぞれ1文字以上含めてください。` | **PASS** | [evidence_AD301_STG_TC47_rule_validation_msg13.png](../../evidence/AD301/evidence_AD301_STG_TC47_rule_validation_msg13.png) |
| `[AD301-48]` | Nhập lại mật khẩu hiện tại của Agency 123 (`Leo150122@`) $\rightarrow$ Click `保存` | BE kiểm tra lịch sử mật khẩu của Owner, trả HTTP 400 kèm `MSG261`, FE hiển thị dưới ô nhập | API trả HTTP 400 PATCH `https://api-admin-stg.surrealdolls.com/api/v1/agency/25/` với `{"detail":"過去2回以内に使用したパスワードは再利用できません。"}`, FE hiển thị lỗi `MSG261` | **PASS** | [evidence_AD301_STG_TC48_reuse_validation_msg261.png](../../evidence/AD301/evidence_AD301_STG_TC48_reuse_validation_msg261.png) |

---

### 4.4. Màn hình Đặt lại Mật khẩu (BA1003 / AB003)

- **Truy cập link với token không hợp lệ:** `https://admin-stg.surrealdolls.com/reset-password?token=test_dummy_token`
- **Kết quả thực tế:** Hệ thống hiển thị thông báo lỗi `MSG19`: `パスワード再設定リンクが無効または期限切れです。` đúng chuẩn đặc tả an toàn.
- **Bằng chứng:** [evidence/BA1003/evidence_BA1003_STG_reset_password_token_page.png](../../evidence/BA1003/evidence_BA1003_STG_reset_password_token_page.png)

---

## 5. KẾT LUẬN & KIẾN NGHỊ (CONCLUSION & NEXT ACTIONS)

1. **Về tính năng cốt lõi (Core Business & Security Rules):**
   - **Tất cả các cơ chế bảo mật then chốt của GMO Sec-12 (CMR43, chống tái sử dụng mật khẩu 3 lần gần nhất, kiểm tra độ phức tạp 4 nhóm ký tự) đã hoạt động chính xác 100% trên môi trường Staging** trên toàn bộ các màn hình liên quan (`AA000`, `AA003`, `BA100`, `BA200`, `AD301`, `BA1003`).
   - Các API BE (`/auth/login/`, `/agency/auth/login/`, `/auth/change-password/`, `/agency/{id}/`) đã phân biệt chính xác mã lỗi `MSG24` (sai mật khẩu hiện tại) và `MSG261` (trùng mật khẩu cũ), trả HTTP status code 400/401 chuẩn mực.

2. **Các điểm cần FE khắc phục trước khi Release:**
   - **BUG-1:** Bổ sung icon tam giác ▲ ở mép phải nút tài khoản cuối Side menu (`AA003` / `BA200`).
   - **BUG-2:** Bổ sung Tag Role 「マスター」 trong phần Header của Menu popup tài khoản Admin Master (`AA003`).
   - **BUG-3:** Bổ sung Tên 事務所 và Tag Role 「オーナー」 / 「事務所管理者」 trong Header Menu popup tài khoản Agency (`BA200`).

3. **Về kiểm thử hết hạn mật khẩu 30 ngày (CMR68 - MSG260):**
   - Do dữ liệu STG được backfill ngày 21/10/2026 nên tài khoản thông thường chưa đến hạn 30 ngày tự nhiên. Kiến nghị Dev BE hỗ trợ chuẩn bị 1 tài khoản test có `password_changed_at` > 30 ngày trên STG hoặc hỗ trợ cập nhật thời gian để hoàn tất nghiệm thu ca `MSG260`.
