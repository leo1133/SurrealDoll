import { test, expect } from '../../src/fixtures/baseTest';
import { HttpStatus } from '../../src/utils/constants';

test.describe('AD100_Agency List / Search E2E Multi-Layer Verification (UI <-> API Consistency)', () => {

  test('TC_AD100_E2E_01: Verify data consistency between Backend API and UI Data Grid', async ({ agencyPage, agencyApi, page }) => {
    // 1. Gọi trực tiếp Backend API lấy dữ liệu Agency trang 1
    const apiResponse = await agencyApi.getAgencyList({
      page: 1,
      items_per_page: 10,
    });

    expect(apiResponse.status()).toBe(HttpStatus.OK);
    const apiData = await apiResponse.json();
    const apiAgencies = apiData.data?.items || [];

    // 2. Mở giao diện AD100 trên trình duyệt
    await agencyPage.goto();

    // 3. Đối chiếu số lượng dòng trên UI vs số lượng bản ghi API trả về
    const uiRowCount = await agencyPage.getRowCount();
    expect(uiRowCount).toBe(apiAgencies.length);

    // 4. Nếu có dữ liệu, đối chiếu chi tiết từng trường của bản ghi đầu tiên
    if (apiAgencies.length > 0) {
      const firstApiAgency = apiAgencies[0];
      const firstUiRow = agencyPage.tableRows.first();

      // Kiểm tra Tên Agency hiển thị trên UI khớp 100% với DB/API
      await expect(firstUiRow).toContainText(firstApiAgency.name);

      // Kiểm tra Mã 事務所ID
      await expect(firstUiRow).toContainText(firstApiAgency.agency_code);

      // Kiểm tra Số lượng Liver trực thuộc
      await expect(firstUiRow).toContainText(String(firstApiAgency.member_count));
    }
  });

  test('TC_AD100_E2E_02: Verify UI search action dynamically queries API and updates table', async ({ agencyPage, page }) => {
    await agencyPage.goto();

    const initialRowCount = await agencyPage.getRowCount();
    test.skip(initialRowCount === 0, 'Bỏ qua khi bảng không có dữ liệu mẫu');

    // Lấy tên của agency đầu tiên để search
    const firstRowText = await agencyPage.tableRows.first().innerText();
    const searchWord = firstRowText.split('\t')[2]?.trim() || 'Agency';

    // Thực hiện tìm kiếm và chờ request POST /agency/
    const [apiResponse] = await Promise.all([
      page.waitForResponse((resp) => resp.url().includes('/agency/') && resp.request().method() === 'POST'),
      (async () => {
        await agencyPage.fillSearchKeyword(searchWord);
        await agencyPage.searchButton.click();
      })(),
    ]);

    expect(apiResponse.status()).toBe(HttpStatus.OK);
    const searchResult = await apiResponse.json();

    // Đối chiếu số lượng trả về từ API và số dòng hiển thị trên UI
    const searchUiRowCount = await agencyPage.getRowCount();
    expect(searchUiRowCount).toBe(searchResult.data.items.length);
  });

});
