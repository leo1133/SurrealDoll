# BÁO CÁO LỖI KIỂM THỬ THỦ CÔNG - MÀN HÌNH BA200 (PASSWORD CHANGE MODAL)

Theo quy chuẩn [06_bug_reporting_rule.md](Universal_Rules/06_bug_reporting_rule.md).

---

## 1. DANH SÁCH BÁO CÁO LỖI CHI TIẾT (DETAILED BUG REPORTS)

### [BUG-1] [BA200] [Modal Backdrop] Modal パスワード変更 không đóng khi người dùng click vào vùng nền tối mờ (Backdrop) bên ngoài

- **Mã Test Case liên quan:** `[BA200-6]`
- **Mức độ nghiêm trọng (Severity):** Minor
- **Môi trường (Environment):** 
  - URL: `https://admin-dev.surrealdolls.com/agencies/info`
  - Trình duyệt: Chromium / Chrome
  - Role: `Agency Owner (agency01)`
- **Các bước tái hiện (Steps to Reproduce):**
  1. Đăng nhập tài khoản Agency (`agency01` / `Phgnga1998@`).
  2. Bấm vào khu tài khoản ở cuối side menu, chọn 「パスワード変更」 để mở modal.
  3. Nhập dữ liệu dở dang hoặc để trống các ô input trong modal.
  4. Click chuột vào vùng nền tối mờ (Backdrop overlay: `div[data-slot="dialog-overlay"]`) nằm bên ngoài modal dialog.
  5. Quan sát phản hồi của giao diện.
- **Kết quả kỳ vọng (Expected Result):**
  - Modal パスワード変更 lập tức đóng lại an toàn.
  - Toàn bộ dữ liệu vừa nhập vào modal bị xóa sạch khi đóng.
- **Kết quả thực tế (Actual Result):**
  - Modal không đóng khi click vào vùng nền tối mờ (Backdrop overlay).
  - Người dùng chỉ có thể đóng modal bằng cách bấm nút "キャンセル", nút đóng [X] ở góc trên bên phải, hoặc nhấn phím `Esc` trên bàn phím.
- **Bằng chứng đính kèm (Evidence):**
  - File ảnh chụp lỗi: [evidence/BA200/evidence_BA200_TC06_backdrop_click_not_closing.png](../../evidence/BA200/evidence_BA200_TC06_backdrop_click_not_closing.png)
  - Bằng chứng DOM HTML & Event Log:
    ```html
    <!-- Backdrop overlay element outside dialog -->
    <div data-slot="dialog-overlay" class="data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 fixed inset-0 z-50 bg-black/[0.42]"></div>
    
    <!-- Dialog container still open after backdrop click -->
    <div role="dialog" class="...">
      <h2 class="...">パスワード変更</h2>
      ...
    </div>
    ```
    ```javascript
    // Technical evidence log:
    const overlay = document.querySelector('[data-slot="dialog-overlay"]');
    overlay.click();
    console.log(document.querySelector('[role="dialog"]') !== null); // true (modal still open)
    ```

---

### [BUG-2] [BA200] [Side Menu Account Area] Nút khu tài khoản ở cuối side menu thiếu icon tam giác ▲ ở mép phải

- **Mã Test Case liên quan:** `[BA200-8]`
- **Mức độ nghiêm trọng (Severity):** Minor
- **Môi trường (Environment):** 
  - URL: `https://admin-dev.surrealdolls.com/agencies/info`
  - Trình duyệt: Chromium / Chrome
  - Role: `Agency Owner (agency01)`
- **Các bước tái hiện (Steps to Reproduce):**
  1. Đăng nhập tài khoản Agency (`agency01` / `Phgnga1998@`).
  2. Quan sát khu vực tài khoản nằm ở góc dưới cùng bên trái của thanh Side menu.
- **Kết quả kỳ vọng (Expected Result):**
  - Hiển thị ô tròn chứa chữ cái đầu của 名前.
  - Hiển thị 名前 và メールアドレス của tài khoản đang đăng nhập.
  - Hiển thị icon tam giác ▲ (hoặc chevron indicator) ở mép phải của nút để biểu thị menu có thể mở lên.
- **Kết quả thực tế (Actual Result):**
  - Khu vực tài khoản chỉ hiển thị Avatar tròn chứa ký tự đầu, Tên và Email.
  - Hoàn toàn KHÔNG có icon tam giác ▲ hay bất kỳ icon mũi tên/chevron nào ở mép phải nút.
- **Bằng chứng đính kèm (Evidence):**
  - File ảnh chụp lỗi: [evidence/BA200/evidence_BA200_TC08_missing_triangle_icon.png](../../evidence/BA200/evidence_BA200_TC08_missing_triangle_icon.png)
  - Bằng chứng DOM HTML:
    ```html
    <button data-slot="dropdown-menu-trigger" data-sidebar="menu-button" data-size="lg" ...>
      <span data-slot="avatar" ...><span data-slot="avatar-fallback">1</span></span>
      <div class="grid flex-1 text-left text-sm leading-tight">
        <span class="truncate font-semibold">123</span>
        <span class="text-muted-foreground truncate text-xs">ngadtp@mumesoft.vn</span>
      </div>
      <!-- Missing triangle ▲ / chevron icon here -->
    </button>
    ```

---

### [BUG-3] [BA200] [Account Menu Header] Header của Menu tài khoản không hiển thị Tên 事務所 và Tag Role 「オーナー」

- **Mã Test Case liên quan:** `[BA200-14]`
- **Mức độ nghiêm trọng (Severity):** Major
- **Môi trường (Environment):** 
  - URL: `https://admin-dev.surrealdolls.com/agencies/info`
  - Trình duyệt: Chromium / Chrome
  - Role: `Agency Owner (agency01)`
- **Các bước tái hiện (Steps to Reproduce):**
  1. Đăng nhập tài khoản Agency Owner (`agency01` / `Phgnga1998@`).
  2. Click vào khu tài khoản ở cuối side menu để mở menu popup tài khoản.
  3. Quan sát phần header phía trên cùng của popup menu (trên đường phân cách separator).
- **Kết quả kỳ vọng (Expected Result):**
  - Phần header menu hiển thị đầy đủ 4 thông tin theo đặc tả Design & Spec:
    1. 名前 (Tên người dùng)
    2. メールアドレス (Email)
    3. Tên 事務所 (Agency Name, ví dụ: `testadm02`)
    4. Tag Role người dùng: 「オーナー」
- **Kết quả thực tế (Actual Result):**
  - Header popup menu chỉ hiển thị: Avatar tròn, 名前 (`123`), và メールアドレス (`ngadtp@mumesoft.vn`).
  - Hoàn toàn KHÔNG hiển thị Tên 事務所 và KHÔNG có Tag Role 「オーナー」.
- **Bằng chứng đính kèm (Evidence):**
  - File ảnh chụp lỗi: [evidence/BA200/evidence_BA200_TC14_missing_agency_name_and_role_tag.png](../../evidence/BA200/evidence_BA200_TC14_missing_agency_name_and_role_tag.png)
  - Bằng chứng DOM HTML:
    ```html
    <div data-slot="dropdown-menu-label" class="text-sm data-[inset]:pl-8 p-0 font-light">
      <div class="flex items-center gap-2 px-1 py-1.5 text-left text-sm">
        <span data-slot="avatar" class="..."><span data-slot="avatar-fallback">1</span></span>
        <div class="grid flex-1 text-left text-sm leading-tight">
          <span class="truncate font-semibold">123</span>
          <span class="text-muted-foreground truncate text-xs">ngadtp@mumesoft.vn</span>
          <!-- Missing agency_name and role badge 'オーナー' -->
        </div>
      </div>
    </div>
    ```

---

### [BUG-4] [BA200] [Account Menu Header] Menu tài khoản không hiển thị Tag Role 「事務所管理者」 đối với tài khoản Sub-Admin

- **Mã Test Case liên quan:** `[BA200-15]`
- **Mức độ nghiêm trọng (Severity):** Major
- **Môi trường (Environment):** 
  - URL: `https://admin-dev.surrealdolls.com/agencies/info`
  - Trình duyệt: Chromium / Chrome
  - Role: `Agency Sub-Admin (事務所管理者)`
- **Các bước tái hiện (Steps to Reproduce):**
  1. Mở menu tài khoản tại góc dưới thanh Side menu.
  2. Quan sát cấu trúc DOM và thành phần hiển thị của component dropdown menu header.
- **Kết quả kỳ vọng (Expected Result):**
  - Hiển thị badge / tag role 「事務所管理者」 đúng màu sắc thiết kế theo Spec (CMR43 / Figma).
- **Kết quả thực tế (Actual Result):**
  - Component Dropdown menu header trên Frontend hoàn toàn không có container hay logic render badge / tag role cho người dùng.
- **Bằng chứng đính kèm (Evidence):**
  - File ảnh chụp lỗi: [evidence/BA200/evidence_BA200_TC15_missing_subadmin_role_tag.png](../../evidence/BA200/evidence_BA200_TC15_missing_subadmin_role_tag.png)
  - Bằng chứng DOM HTML: Cùng cấu trúc dropdown menu label thiếu role container như BUG-3.

---

## 2. BẢNG TỔNG HỢP DANH SÁCH LỖI (FAIL SUMMARY TABLE)

| TC ID | Control / Chức năng | Các bước tái hiện (Steps) | Expected Result | Actual Result | Mức độ | File Evidence (Unique) & DOM Log | Bug ID |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `[BA200-6]` | Modal Backdrop | 1. Mở modal パスワード変更<br>2. Click chuột vào vùng nền tối mờ (Backdrop) bên ngoài modal | Modal lập tức đóng lại an toàn, xóa sạch dữ liệu vừa nhập | Modal không đóng khi click backdrop, chỉ đóng khi click Cancel, [X] hoặc phím Esc | Minor | `evidence/evidence_BA200_TC06_backdrop_click_not_closing.png`<br>`DOM: div[data-slot="dialog-overlay"] onPointerDownOutside prevented` | *(Để trống)* |
| `[BA200-8]` | Nút tài khoản side menu | 1. Đăng nhập Agency<br>2. Quan sát nút tài khoản cuối side menu | Hiển thị avatar tròn, Tên, Email và icon tam giác ▲ ở mép phải | Không có icon tam giác ▲ ở mép phải | Minor | `evidence/evidence_BA200_TC08_missing_triangle_icon.png`<br>`DOM: button[data-sidebar="menu-button"] lacks triangle/chevron SVG` | *(Để trống)* |
| `[BA200-14]` | Header Menu tài khoản | 1. Click mở menu tài khoản ở cuối side menu<br>2. Quan sát phần header menu | Hiển thị đầy đủ: Tên, Email, Tên 事務所, Tag role 「オーナー」 | Chỉ hiển thị Tên và Email; thiếu Tên 事務所 và Tag role 「オーナー」 | Major | `evidence/evidence_BA200_TC14_missing_agency_name_and_role_tag.png`<br>`DOM: div[data-slot="dropdown-menu-label"] lacks agency_name & role tag` | *(Để trống)* |
| `[BA200-15]` | Tag Role 事務所管理者 | 1. Mở menu tài khoản<br>2. Quan sát vị trí role tag | Hiển thị tag role 「事務所管理者」 đúng style thiết kế | Component menu header hoàn toàn không có logic/container render role tag | Major | `evidence/evidence_BA200_TC15_missing_subadmin_role_tag.png`<br>`DOM: No role badge element rendered` | *(Để trống)* |

---

## 3. KẾT QUẢ KIỂM THỬ LẠI ROUND 2 (ROUND 2 RETEST RESULTS - 11/11/2026)

Theo quy chuẩn [04_manual_test_execution_rule.md](Universal_Rules/04_manual_test_execution_rule.md) Section 5:

| TC ID | Trạng thái R1 | Kết quả Retest R2 | Mô tả chi tiết kết quả Retest | File Evidence mới (Round 2) | Trạng thái Bug |
| :---: | :---: | :---: | :--- | :--- | :---: |
| `[BA200-6]` | **Fail** | **PASS** | Modal đóng bình thường, an toàn và xóa sạch nội dung khi click chuột vào vùng nền tối (Backdrop) bên ngoài modal dialog. | *(Đã xác minh video & live)* | **Closed** |
| `[BA200-8]` | **Fail** | **FAIL** | Dev chưa sửa: Nút tài khoản ở đáy side menu vẫn chỉ có Avatar, Tên và Email; **hoàn toàn thiếu icon tam giác ▲** ở mép phải. | `evidence/evidence_BA200_TC08_R2_missing_triangle_icon.png` | **Reopen** |
| `[BA200-14]` | **Fail** | **FAIL** | Dev chưa sửa: Header menu popup chỉ hiển thị Avatar, Tên và Email; **vẫn thiếu Tên 事務所 và thiếu Tag role 「オーナー」**. | `evidence/evidence_BA200_TC14_R2_missing_agency_name_and_role_tag.png` | **Reopen** |
| `[BA200-15]` | **Fail** | **FAIL** | Dev chưa sửa: Component menu header hoàn toàn chưa có container/logic render Tag role cho Sub-admin (`事務所管理者`). | `evidence/evidence_BA200_TC14_R2_missing_agency_name_and_role_tag.png` | **Reopen** |

