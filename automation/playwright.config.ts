import { defineConfig, devices } from '@playwright/test';
import dotenv from 'dotenv';
import path from 'path';

// Load environment variables
dotenv.config({ path: path.resolve(__dirname, '.env.test') });
dotenv.config({ path: path.resolve(__dirname, '.env') });

const STORAGE_STATE_PATH = path.resolve(__dirname, 'playwright/.auth/admin.json');

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 1, // Rule 05: Monitored Retry 01 lần
  workers: process.env.CI ? 2 : undefined,
  reporter: [
    ['list'],
    ['html', { outputFolder: 'playwright-report', open: 'never' }]
  ],
  timeout: parseInt(process.env.DEFAULT_TIMEOUT || '30000', 10),
  expect: {
    timeout: 5000,
  },
  use: {
    baseURL: process.env.UI_BASE_URL || 'https://admin-dev.surrealdolls.com',
    trace: 'on-first-retry', // Rule 05: Bật trace khi retry để triage flaky test
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
    actionTimeout: parseInt(process.env.ACTION_TIMEOUT || '10000', 10),
    navigationTimeout: parseInt(process.env.NAVIGATION_TIMEOUT || '15000', 10),
    httpCredentials: process.env.BASIC_AUTH_USERNAME ? {
      username: process.env.BASIC_AUTH_USERNAME,
      password: process.env.BASIC_AUTH_PASSWORD || '',
    } : undefined,
  },

  projects: [
    // 1. Global Setup Authentication (Rule 05: Session Caching)
    {
      name: 'setup',
      testMatch: /.*\.setup\.ts/,
    },

    // 2. UI Functional Tests (Chrome Desktop)
    {
      name: 'chromium',
      use: {
        ...devices['Desktop Chrome'],
        storageState: STORAGE_STATE_PATH,
      },
      dependencies: ['setup'],
      testMatch: /.*\.ui\.spec\.ts|.*\.e2e\.spec\.ts/,
    },

    // 3. API Functional Tests (Headless Request Context)
    {
      name: 'api',
      testMatch: /.*\.api\.spec\.ts/,
    },
  ],
});
