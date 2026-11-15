import { test as base, expect } from '@playwright/test';
import { AD100AgencyListPage } from '../pages/AD100AgencyListPage';
import { LoginPage } from '../pages/LoginPage';
import { CustomApiClient } from '../api/CustomApiClient';
import { AD100AgencyAPI } from '../api/AD100AgencyAPI';
import { env } from '../config/env';
import fs from 'fs';
import path from 'path';

// Định nghĩa kiểu cho các fixture mở rộng
type CustomFixtures = {
  agencyPage: AD100AgencyListPage;
  loginPage: LoginPage;
  customApiClient: CustomApiClient;
  agencyApi: AD100AgencyAPI;
};

export const test = base.extend<CustomFixtures>({
  // Fixture Page Object AD100
  agencyPage: async ({ page }, use) => {
    const agencyPage = new AD100AgencyListPage(page);
    await agencyPage.enableResourceAborting(); // Kích hoạt Rule 05: Resource Aborting
    await use(agencyPage);
  },

  // Fixture Page Object Login
  loginPage: async ({ page }, use) => {
    const loginPage = new LoginPage(page);
    await use(loginPage);
  },

  // Fixture Custom API Client với Token tự động
  customApiClient: async ({ request }, use) => {
    const tokenPath = path.resolve(__dirname, '../../playwright/.auth/token.json');
    let token = '';

    if (fs.existsSync(tokenPath)) {
      try {
        const tokenData = JSON.parse(fs.readFileSync(tokenPath, 'utf-8'));
        token = tokenData.token || '';
      } catch (e) {}
    }

    const client = new CustomApiClient(request, token);
    await use(client);
  },

  // Fixture AD100 API Wrapper
  agencyApi: async ({ customApiClient }, use) => {
    const api = new AD100AgencyAPI(customApiClient);
    await use(api);
  },
});

export { expect };
