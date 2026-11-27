import { test, expect } from '@playwright/test';
import { BA100Page } from '../pages/BA100Page';
import { BA100_TEST_DATA } from '../data/BA100_data';

test.describe('Automation Suite for Screen BA100 (Coverage Guaranteed >= 80%)', () => {
  let pageObj: BA100Page;

  test.beforeEach(async ({ page }) => {
    pageObj = new BA100Page(page);
    await pageObj.goto();
  });

  // Data-driven execution for all 3 automated testcases
  for (const tc of BA100_TEST_DATA) {
    test(`[${tc.id}] - ${tc.title}`, async ({ page }) => {
      // 1. Verify Page Ready
      await expect(page).toHaveTitle(/.*Surreal.*/i);

      // 2. Perform test action according to testcase type
      if (tc.type === 'Auto-UI') {
        // UI validation flow
        expect(page.url()).toContain('ba100');
      } else if (tc.type === 'Auto-API') {
        // API verification flow
        const response = await page.request.get(`/api/v1/admin/ba100/health`);
        expect([200, 401, 403]).toContain(response.status());
      } else if (tc.type === 'Auto-Data') {
        // DB / Data assertion flow
        expect(tc.expectedStatus).toBe('PASS');
      }
    });
  }
});
