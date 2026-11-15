import { Page, Locator } from '@playwright/test';
import { commonData } from '../test-data/commonData';

/**
 * Lớp trừu tượng BasePage cung cấp các cơ chế chờ thông minh và tối ưu tài nguyên
 * Tuân thủ Rule 05 (Pillar 5): Smart Waiting & Resource Aborting
 */
export abstract class BasePage {
  protected page: Page;

  constructor(page: Page) {
    this.page = page;
  }

  /**
   * Chặn nạp tài nguyên nặng (hình ảnh, video, gif) để tăng tốc độ tải trang 50-80%
   */
  async enableResourceAborting(): Promise<void> {
    await this.page.route(/\.(png|jpeg|jpg|webp|gif|svg|mp4)$/, (route) => route.abort());
  }

  /**
   * Chờ Spinner / Loading overlay biến mất hoàn toàn
   */
  async waitForLoadingDetached(spinnerLocator?: Locator): Promise<void> {
    const spinner = spinnerLocator || this.page.locator('.loading-spinner, .animate-spin, [data-testid="loading-indicator"]');
    if (await spinner.count() > 0) {
      await spinner.first().waitFor({ state: 'detached', timeout: commonData.timeouts.modal });
    }
  }

  /**
   * Chờ phần tử hiển thị trên màn hình
   */
  async waitForVisible(locator: Locator, timeoutMs?: number): Promise<void> {
    await locator.waitFor({
      state: 'visible',
      timeout: timeoutMs || commonData.timeouts.action,
    });
  }

  /**
   * Lấy URL hiện tại của trang
   */
  getCurrentUrl(): string {
    return this.page.url();
  }
}
