import dotenv from 'dotenv';
import path from 'path';

// Đảm bảo nạp đúng file env
dotenv.config({ path: path.resolve(__dirname, '../../.env.test') });
dotenv.config({ path: path.resolve(__dirname, '../../.env') });

export const env = {
  UI_BASE_URL: process.env.UI_BASE_URL || 'https://admin-dev.surrealdolls.com',
  API_BASE_URL: process.env.API_BASE_URL || 'https://api-admin-dev.surrealdolls.com',
  BASIC_AUTH_USERNAME: process.env.BASIC_AUTH_USERNAME || 'suriaru',
  BASIC_AUTH_PASSWORD: process.env.BASIC_AUTH_PASSWORD || 'suriaru',
  MASTER_ADMIN_EMAIL: process.env.MASTER_ADMIN_EMAIL || 'admin@admin.com',
  MASTER_ADMIN_PASSWORD: process.env.MASTER_ADMIN_PASSWORD || '!Ch4ng3Th1sP4ssW0rd!',
  TEST_AGENCY_ID: Number(process.env.TEST_AGENCY_ID || '1'),
  TEST_AGENCY_CODE: process.env.TEST_AGENCY_CODE || 'AG001',
  TEST_AGENCY_NAME: process.env.TEST_AGENCY_NAME || 'Tokyo Live Agency',
  DEFAULT_TIMEOUT: Number(process.env.DEFAULT_TIMEOUT || '30000'),
  ACTION_TIMEOUT: Number(process.env.ACTION_TIMEOUT || '10000'),
  NAVIGATION_TIMEOUT: Number(process.env.NAVIGATION_TIMEOUT || '15000'),
};
