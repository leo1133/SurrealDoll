# BÁO CÁO LỖI KIỂM THỬ GIAO DIỆN (BUG REPORT) - MÀN HÌNH A100_WEB

- **Màn hình / Module:** `A100_WEB` (Web User Sign-In / Terms Agreement Modal `A101`)
- **Môi trường phát hiện:** Live / Production (`https://surrealdolls.com/en/sign-in?redirect=%2Fmypage`)
- **Người báo cáo:** Antigravity QA Agent / NgaDTP
- **Ngày phát hiện:** 20/11/2026

---

## DANH SÁCH LỖI PHÁT HIỆN

| Bug ID | Tên Lỗi / Tóm Tắt | Loại Lỗi | Độ Nghiêm Trọng | Trạng Thái | File Bằng Chứng |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **`BUG-A100-WEB-01`** | Nút bấm xác nhận trong modal Điều khoản bị sai chính tả tên thương hiệu: "Start Sarial Dolls" thay vì "Start Surreal Dolls" | UI / Content Typo | **Medium** | **Open** | `evidence/A100_WEB/evidence_A100_WEB_typo_sarial_dolls_modal.png` |
| **`BUG-A100-WEB-02`** | Yêu cầu prefetch liên kết `/en/help-center` tại footer bị hủy kết nối mạng (net::ERR_ABORTED) | Frontend / Network | **Low** | **Open** | Log Network: `GET https://surrealdolls.com/en/help-center -> ERR_ABORTED` |

---

## CHI TIẾT LỖI 1: `BUG-A100-WEB-01`

### 1. Tóm tắt (Summary)
Nút bấm xác nhận đăng nhập trong Modal thỏa thuận điều khoản (Terms Dialog) hiển thị sai chính tả tên thương hiệu: `"Start Sarial Dolls"` (sai chữ `Sarial` thay vì `Surreal`).

### 2. Các bước tái hiện (Steps to Reproduce)
1. Mở trình duyệt, truy cập URL: `https://surrealdolls.com/en/sign-in?redirect=%2Fmypage`
2. Tại màn hình Sign In, click vào nút **"Sign in with Google"** (hoặc bất kỳ nút đăng nhập mạng xã hội nào bên dưới).
3. Quan sát Modal thỏa thuận Điều khoản dịch vụ xuất hiện trên màn hình.
4. Kiểm tra dòng chữ trên nút bấm xác nhận màu xanh/đen chính giữa modal.

### 3. Kết quả thực tế (Actual Result)
- Nút bấm hiển thị: `"Start Sarial Dolls"`.
- Bị sai chính tả thương hiệu SurrealDoll (`Sarial` thay vì `Surreal`).

### 4. Kết quả kỳ vọng (Expected Result)
- Nút bấm phải hiển thị đúng tên thương hiệu: `"Start Surreal Dolls"`.

### 5. Bằng chứng kiểm thử (Evidence)
- Ảnh chụp màn hình: [evidence_A100_WEB_typo_sarial_dolls_modal.png](file:///home/nga/Documents/SurrealDoll/evidence/A100_WEB/evidence_A100_WEB_typo_sarial_dolls_modal.png)
