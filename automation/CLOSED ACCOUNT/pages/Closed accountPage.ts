import { Page, Locator, expect } from '@playwright/test';

export class CLOSED ACCOUNTPage {
  readonly page: Page;
  readonly heading: Locator;
  readonly submitButton: Locator;
  readonly toastMessage: Locator;

  constructor(page: Page) {
    this.page = page;
    this.heading = page.locator('h1, h2, [data-testid="page-title"]');
    this.submitButton = page.locator('button[type="submit"], button:has-text("保存"), button:has-text("検索")');
    this.toastMessage = page.locator('.ant-message, [role="alert"], .toast');
  }

  async goto() {
    await this.page.goto('/closed account');
    await this.page.waitForLoadState('networkidle');
  }

  async fillField(selector: string, value: string) {
    const el = this.page.locator(selector);
    await el.waitFor({ state: 'visible' });
    await el.fill(value);
  }

  async clickSubmit() {
    await this.submitButton.first().click();
  }

  async expectSuccessToast(msg?: string) {
    await expect(this.toastMessage.first()).toBeVisible();
    if (msg) {
      await expect(this.toastMessage.first()).toContainText(msg);
    }
  }
}
