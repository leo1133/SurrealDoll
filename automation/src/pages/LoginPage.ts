import { Page, Locator } from '@playwright/test';
import { BasePage } from './BasePage';
import { routes } from '../config/endpoints';
import { env } from '../config/env';
import { commonData } from '../test-data/commonData';

/**
 * Page Object Model cho trang Đăng nhập Master Admin
 */
export class LoginPage extends BasePage {
  readonly emailInput: Locator;
  readonly passwordInput: Locator;
  readonly loginButton: Locator;
  readonly errorMessage: Locator;

  constructor(page: Page) {
    super(page);
    // Ưu tiên locator accessible & role theo Mục 2.1
    this.emailInput = page.getByPlaceholder(/メールアドレス|Email/i).or(page.locator('input[type="email"], input[name="email"]'));
    this.passwordInput = page.getByPlaceholder(/パスワード|Password/i).or(page.locator('input[type="password"], input[name="password"]'));
    this.loginButton = page.getByRole('button', { name: /ログイン|Sign in/i });
    this.errorMessage = page.locator('.error-message, [role="alert"], .text-destructive');
  }

  /**
   * Điều hướng vào trang đăng nhập
   */
  async goto(): Promise<void> {
    await this.page.goto(routes.login, { timeout: commonData.timeouts.pageLoad });
  }

  /**
   * Thực hiện đăng nhập với thông tin tài khoản
   */
  async login(email?: string, password?: string): Promise<void> {
    const userEmail = email || env.MASTER_ADMIN_EMAIL;
    const userPass = password || env.MASTER_ADMIN_PASSWORD;

    await this.emailInput.fill(userEmail);
    await this.passwordInput.fill(userPass);

    await Promise.all([
      this.page.waitForNavigation({ timeout: commonData.timeouts.pageLoad }).catch(() => {}),
      this.loginButton.click(),
    ]);

    await this.waitForLoadingDetached();
  }
}
