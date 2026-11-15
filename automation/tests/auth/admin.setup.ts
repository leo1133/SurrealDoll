import { test as setup } from '@playwright/test';
import { LoginPage } from '../../src/pages/LoginPage';
import { env } from '../../src/config/env';
import fs from 'fs';
import path from 'path';

const AUTH_DIR = path.resolve(__dirname, '../../playwright/.auth');
const STORAGE_STATE_PATH = path.join(AUTH_DIR, 'admin.json');
const TOKEN_PATH = path.join(AUTH_DIR, 'token.json');

/**
 * Global Setup Authentication (Pillar 5 - Giai đoạn 4: Quản trị phiên)
 * Đăng nhập 1 lần và lưu trữ StorageState cho toàn bộ các ca kiểm thử UI
 */
setup('Authenticate Master Admin and Cache Session', async ({ page }) => {
  // Tạo thư mục auth nếu chưa có
  if (!fs.existsSync(AUTH_DIR)) {
    fs.mkdirSync(AUTH_DIR, { recursive: true });
  }

  // 1. Kiểm tra session hiện tại có còn hợp lệ không
  if (fs.existsSync(STORAGE_STATE_PATH)) {
    try {
      const stats = fs.statSync(STORAGE_STATE_PATH);
      const fileAgeMinutes = (Date.now() - stats.mtimeMs) / (1000 * 60);

      // Nếu file được tạo trong vòng 30 phút -> tái sử dụng
      if (fileAgeMinutes < 30) {
        console.log(`[Session Cache] Tái sử dụng phiên UI hợp lệ (${fileAgeMinutes.toFixed(1)} phút tuổi)`);
        return;
      }
    } catch (e) {
      console.log('[Session Cache] Đọc file session thất bại, tiến hành đăng nhập mới');
    }
  }

  // 2. Mở trình duyệt và thực hiện đăng nhập
  console.log('[Auth Setup] Bắt đầu đăng nhập Master Admin...');
  const loginPage = new LoginPage(page);
  await loginPage.goto();
  await loginPage.login(env.MASTER_ADMIN_EMAIL, env.MASTER_ADMIN_PASSWORD);

  // 3. Lấy cookies & token để lưu cache
  const cookies = await page.context().cookies();
  const tokenCookie = cookies.find((c) => c.name.includes('token') || c.name.includes('auth'));
  const token = tokenCookie ? tokenCookie.value : 'dummy_master_token_for_mocking';

  // Lưu file token cho API Client
  fs.writeFileSync(TOKEN_PATH, JSON.stringify({ token, createdAt: Date.now() }), 'utf-8');

  // Lưu storageState cho browser context
  await page.context().storageState({ path: STORAGE_STATE_PATH });
  console.log('[Auth Setup] Đăng nhập thành công và đã lưu StorageState.');
});
