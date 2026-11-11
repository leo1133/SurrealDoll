# BÁO CÁO LỖI KIỂM THỬ THỦ CÔNG - MÀN HÌNH AA003 (PASSWORD CHANGE MODAL - ADMIN WEB)

Theo quy chuẩn [06_bug_reporting_rule.md](Universal_Rules/06_bug_reporting_rule.md).
Môi trường kiểm thử: **Dev-Admin** (`https://admin-dev.surrealdolls.com/`) theo cấu hình tại [TEST_CONFIG.md](TEST_CONFIG.md).

---

## 1. DANH SÁCH BÁO CÁO LỖI CHI TIẾT (DETAILED BUG REPORTS)

### [BUG-1] [AA003] [Side Menu Account Area] Nút khu tài khoản ở cuối side menu thiếu icon tam giác ▲ ở mép phải

- **Mã Test Case liên quan:** `[AA003-8]`
- **Mức độ nghiêm trọng (Severity):** Minor
- **Môi trường (Environment):** 
  - URL: `https://admin-dev.surrealdolls.com/`
  - Trình duyệt: Chromium / Chrome
  - Role: `Master Admin (admin@admin.com)`
- **Các bước tái hiện (Steps to Reproduce):**
  1. Đăng nhập tài khoản Admin (`admin@admin.com` | `!Ch4ng3Th1sP4ssW0rd!`).
  2. Quan sát khu vực tài khoản nằm ở góc dưới cùng bên trái của thanh Side menu.
- **Kết quả kỳ vọng (Expected Result):**
  - Hiển thị ô tròn chứa chữ cái đầu của 名前 (`S`).
  - Hiển thị 名前 (`Surreal Dolls Admin`) và メールアドレス (`admin@admin.com`) của tài khoản đang đăng nhập.
  - Hiển thị icon tam giác ▲ (hoặc chevron indicator) ở mép phải của nút để biểu thị menu popup có thể mở lên theo Spec item 1 (`icon ▲`).
- **Kết quả thực tế (Actual Result):**
  - Khu vực tài khoản chỉ hiển thị Avatar tròn chứa ký tự đầu, Tên và Email.
  - Hoàn toàn KHÔNG có icon tam giác ▲ hay bất kỳ icon mũi tên/chevron nào ở mép phải nút.
- **Bằng chứng đính kèm (Evidence):**
  - File ảnh chụp lỗi: `evidence/evidence_AA003_TC08_missing_triangle_icon.png`
  - Bằng chứng DOM HTML:
    ```html
    <button data-slot="dropdown-menu-trigger" data-sidebar="menu-button" data-size="lg" ...>
      <span data-slot="avatar" ...><span data-slot="avatar-fallback">S</span></span>
      <div class="grid flex-1 text-left text-sm leading-tight">
        <span class="truncate font-semibold">Surreal Dolls Admin</span>
        <span class="text-muted-foreground truncate text-xs">admin@admin.com</span>
      </div>
      <!-- Missing triangle ▲ / chevron icon here -->
    </button>
    ```

---

### [BUG-2] [AA003] [Account Menu Header] Header của Menu tài khoản không hiển thị Tag Role 「マスター」 (và các Role khác)

- **Mã Test Case liên quan:** `[AA003-14]`, `[AA003-15]`, `[AA003-16]`
- **Mức độ nghiêm trọng (Severity):** Major
- **Môi trường (Environment):** 
  - URL: `https://admin-dev.surrealdolls.com/`
  - Trình duyệt: Chromium / Chrome
  - Role: `Master Admin (admin@admin.com)`
- **Các bước tái hiện (Steps to Reproduce):**
  1. Đăng nhập tài khoản Admin Master (`admin@admin.com` | `!Ch4ng3Th1sP4ssW0rd!`).
  2. Click vào khu tài khoản ở cuối side menu để mở menu popup tài khoản.
  3. Quan sát phần header phía trên cùng của popup menu (trên đường phân cách separator).
- **Kết quả kỳ vọng (Expected Result):**
  - Phần header menu hiển thị đầy đủ thông tin theo đặc tả Spec item 2:
    1. 名前 (Tên người dùng: `Surreal Dolls Admin`)
    2. メールアドレス (Email: `admin@admin.com`)
    3. Tag Role người dùng: 「マスター」 (hoặc 「管理者」, 「監視員」 tương ứng với tài khoản đăng nhập).
- **Kết quả thực tế (Actual Result):**
  - Header popup menu chỉ hiển thị: Avatar tròn, 名前 (`Surreal Dolls Admin`), và メールアドレス (`admin@admin.com`).
  - Hoàn toàn KHÔNG có Tag Role 「マスター」 (cùng thiếu container/logic render role badge như ở Agency Web).
- **Bằng chứng đính kèm (Evidence):**
  - File ảnh chụp lỗi: `evidence/evidence_AA003_TC14_missing_role_tag.png`
  - Bằng chứng DOM HTML:
    ```html
    <div data-slot="dropdown-menu-label" class="text-sm data-[inset]:pl-8 p-0 font-light">
      <div class="flex items-center gap-2 px-1 py-1.5 text-left text-sm">
        <span data-slot="avatar" class="..."><span data-slot="avatar-fallback">S</span></span>
        <div class="grid flex-1 text-left text-sm leading-tight">
          <span class="truncate font-semibold">Surreal Dolls Admin</span>
          <span class="text-muted-foreground truncate text-xs">admin@admin.com</span>
          <!-- Missing role badge 'マスター' -->
        </div>
      </div>
    </div>
    ```

---

## 2. BẢNG TỔNG HỢP DANH SÁCH LỖI (FAIL SUMMARY TABLE)

| TC ID | Control / Chức năng | Các bước tái hiện (Steps) | Expected Result | Actual Result | Mức độ | File Evidence (Unique) & DOM Log | Bug ID |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `[AA003-8]` | Nút tài khoản side menu | 1. Đăng nhập Admin<br>2. Quan sát nút tài khoản cuối side menu | Hiển thị avatar tròn, Tên, Email và icon tam giác ▲ ở mép phải | Không có icon tam giác ▲ ở mép phải | Minor | `evidence/evidence_AA003_TC08_missing_triangle_icon.png`<br>`DOM: button[data-sidebar="menu-button"] lacks triangle/chevron SVG` | *(Để trống)* |
| `[AA003-14]` | Header Menu tài khoản | 1. Click mở menu tài khoản ở cuối side menu<br>2. Quan sát phần header menu | Hiển thị đầy đủ: Tên, Email, Tag role 「マスター」 | Chỉ hiển thị Tên và Email; thiếu Tag role 「マスター」 | Major | `evidence/evidence_AA003_TC14_missing_role_tag.png`<br>`DOM: div[data-slot="dropdown-menu-label"] lacks role tag` | *(Để trống)* |
| `[AA003-15]` | Tag Role 管理者 | 1. Mở menu tài khoản với role 管理者<br>2. Quan sát vị trí role tag | Hiển thị tag role 「管理者」 đúng style thiết kế | Component menu header hoàn toàn không có logic/container render role tag | Major | `evidence/evidence_AA003_TC14_missing_role_tag.png`<br>`DOM: No role badge element rendered` | *(Để trống)* |
| `[AA003-16]` | Tag Role 監視員 | 1. Mở menu tài khoản với role 監視員<br>2. Quan sát vị trí role tag | Hiển thị tag role 「監視員」 đúng style thiết kế | Component menu header hoàn toàn không có logic/container render role tag | Major | `evidence/evidence_AA003_TC14_missing_role_tag.png`<br>`DOM: No role badge element rendered` | *(Để trống)* |

> [!NOTE]
> **Về ca kiểm thử `[AA003-6]` (Click Backdrop đóng modal):**
> Sau khi retest đối chiếu với thao tác thực tế (sử dụng sự kiện chuột chuẩn của người dùng), Modal パスワード変更 đóng lại an toàn và lập tức khi click ra vùng nền tối Backdrop bên ngoài. Ca này đã được cập nhật sang trạng thái **PASS**.
