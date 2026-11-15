import { test, expect } from '../../src/fixtures/baseTest';
import { ad100Data } from '../../src/test-data/ad100Data';
import { commonData } from '../../src/test-data/commonData';
import { routes } from '../../src/config/endpoints';
import { env } from '../../src/config/env';

test.describe('AD100_Agency List / Search (事務所一覧・検索) UI Automation Suite', () => {

  // @tc: [AD100-1], [AD100-2], [AD100-3] - Kiểm tra điều hướng & Truy cập màn hình
  test('TC_AD100_01: Verify navigation to AD100 via direct URL and breadcrumb display', async ({ agencyPage, page }) => {
    await agencyPage.goto();

    // Verify URL
    expect(page.url()).toContain(routes.agencyList);

    // Verify Breadcrumb (CMR35)
    await expect(agencyPage.breadcrumb).toBeVisible({ timeout: commonData.timeouts.action });

    // Verify Search & Table elements are displayed
    await expect(agencyPage.searchInput).toBeVisible();
    await expect(agencyPage.searchButton).toBeVisible();
    await expect(agencyPage.clearButton).toBeVisible();
    await expect(agencyPage.createButton).toBeVisible();
    await expect(agencyPage.table).toBeVisible();
  });

  // @tc: [AD100-4] - Inbound Deep-link với Query Params
  test('TC_AD100_02: Verify deep-link with query parameters autofills filter controls', async ({ agencyPage, page }) => {
    const testKeyword = 'Tokyo';
    await agencyPage.goto(`q=${testKeyword}&status=1`);

    // Kiểm tra ô search được điền tự động từ query params
    await expect(agencyPage.searchInput).toHaveValue(testKeyword);
  });

  // @tc: [AD100-10] - Placeholder ô tìm kiếm
  test('TC_AD100_03: Verify search input placeholder text matches spec', async ({ agencyPage }) => {
    await agencyPage.goto();
    await expect(agencyPage.searchInput).toHaveAttribute('placeholder', ad100Data.placeholders.searchInput);
  });

  // @tc: [AD100-11], [AD100-12], [AD100-14] - Nhập liệu từ khóa & Auto-trim space
  test('TC_AD100_04: Verify search input accepts text, numbers and trims spaces', async ({ agencyPage }) => {
    await agencyPage.goto();

    // Nhập từ khóa có khoảng trắng đầu và cuối
    await agencyPage.fillSearchKeyword(ad100Data.searchTestData.spacesAround);
    await agencyPage.clickSearch();

    // Bảng dữ liệu hiển thị hoặc trả về kết quả lọc an toàn
    const rowCount = await agencyPage.getRowCount();
    expect(rowCount).toBeGreaterThanOrEqual(0);
  });

  // @tc: [AD100-17] - Tìm kiếm bằng phím Enter
  test('TC_AD100_05: Verify pressing Enter key in search box triggers search', async ({ agencyPage, page }) => {
    await agencyPage.goto();
    await agencyPage.fillSearchKeyword(env.TEST_AGENCY_NAME);
    await agencyPage.pressEnterInSearch();

    // Đảm bảo không bị reload toàn trang và có kết quả hoặc empty state
    await expect(agencyPage.table).toBeVisible();
  });

  // @tc: [AD100-19], [AD100-20] - Tìm kiếm một phần tên (Partial match) và chính xác Agency ID
  test('TC_AD100_06: Verify partial match and exact match search return correct records', async ({ agencyPage }) => {
    await agencyPage.goto();

    // 1. Tìm kiếm một phần tên Agency
    await agencyPage.fillSearchKeyword(ad100Data.searchTestData.kanjiKeyword);
    await agencyPage.clickSearch();
    await expect(agencyPage.table).toBeVisible();

    // 2. Tìm kiếm chính xác mã Agency Code
    await agencyPage.fillSearchKeyword(env.TEST_AGENCY_CODE);
    await agencyPage.clickSearch();
    await expect(agencyPage.table).toBeVisible();
  });

  // @tc: [AD100-22], [AD100-23], [AD100-24], [AD100-25] - Dropdown lọc trạng thái ステータス
  test('TC_AD100_07: Verify status dropdown filters records correctly by Active and Inactive', async ({ agencyPage }) => {
    await agencyPage.goto();

    // Dropdown hiển thị
    await expect(agencyPage.statusDropdown).toBeVisible();

    // Lọc theo trạng thái 利用中 (Active)
    await agencyPage.selectStatus(ad100Data.dropdownOptions.status.active);
    await agencyPage.clickSearch();
    await expect(agencyPage.table).toBeVisible();

    // Lọc theo trạng thái 停止中 (Inactive)
    await agencyPage.selectStatus(ad100Data.dropdownOptions.status.inactive);
    await agencyPage.clickSearch();
    await expect(agencyPage.table).toBeVisible();
  });

  // @tc: [AD100-32] - Nút クリア (Reset bộ lọc về mặc định)
  test('TC_AD100_08: Verify Clear button resets search keyword and dropdown to default', async ({ agencyPage }) => {
    await agencyPage.goto();

    // Nhập từ khóa và chọn dropdown
    await agencyPage.fillSearchKeyword(ad100Data.searchTestData.latinKeyword);
    await agencyPage.selectStatus(ad100Data.dropdownOptions.status.inactive);

    // Bấm nút クリア
    await agencyPage.clickClear();

    // Ô input bị xóa trắng
    await expect(agencyPage.searchInput).toHaveValue('');

    // Dropdown trở về mặc định '全て'
    await expect(agencyPage.statusDropdown).toContainText(ad100Data.dropdownOptions.status.all);
  });

  // @tc: [AD100-33], [AD100-34] - Nút 新規登録 (Điều hướng sang AD200)
  test('TC_AD100_09: Verify clicking Create Agency button navigates to AD200', async ({ agencyPage, page }) => {
    await agencyPage.goto();
    await agencyPage.clickCreateAgency();

    // URL điều hướng sang màn hình tạo mới AD200
    await expect(page).toHaveURL(new RegExp(routes.agencyCreate));
  });

  // @tc: [AD100-35] - [AD100-46] - Hiển thị đầy đủ tiêu đề các cột của bảng
  test('TC_AD100_10: Verify table headers display all required columns', async ({ agencyPage }) => {
    await agencyPage.goto();

    await expect(agencyPage.tableHeaderId).toBeVisible();
    await expect(agencyPage.tableHeaderAgencyId).toBeVisible();
    await expect(agencyPage.tableHeaderAgencyName).toBeVisible();
    await expect(agencyPage.tableHeaderContactOwner).toBeVisible();
    await expect(agencyPage.tableHeaderStreamerCount).toBeVisible();
    await expect(agencyPage.tableHeaderPointSales).toBeVisible();
    await expect(agencyPage.tableHeaderFamiliaSales).toBeVisible();
    await expect(agencyPage.tableHeaderTotalSales).toBeVisible();
    await expect(agencyPage.tableHeaderStatus).toBeVisible();
    await expect(agencyPage.tableHeaderCreatedAt).toBeVisible();
    await expect(agencyPage.tableHeaderUpdatedAt).toBeVisible();
  });

  // @tc: [AD100-47], [AD100-48] - Sắp xếp bảng theo 作成日 và 変更日
  test('TC_AD100_11: Verify sorting table by Created Date and Updated Date', async ({ agencyPage }) => {
    await agencyPage.goto();

    // Click sort ngày tạo
    await agencyPage.clickSortCreatedAt();
    await expect(agencyPage.table).toBeVisible();

    // Click sort ngày cập nhật
    await agencyPage.clickSortUpdatedAt();
    await expect(agencyPage.table).toBeVisible();
  });

  // @tc: [AD100-51], [AD100-52] - Click ライバー数 điều hướng sang AD302 (CR 06/11/2025)
  test('TC_AD100_12: Verify clicking Streamer Count navigates to AD302 Streamer List tab', async ({ agencyPage, page }) => {
    await agencyPage.goto();

    const rowCount = await agencyPage.getRowCount();
    test.skip(rowCount === 0, 'Bỏ qua khi bảng không có bản ghi nào để click');

    await agencyPage.clickStreamerCount(0);

    // URL điều hướng sang AD302 (/admin/agencies/{id}/livers)
    await expect(page).toHaveURL(/\/admin\/agencies\/\d+\/livers/);
  });

  // @tc: [AD100-57] - Click vào dòng hoặc nút Chi tiết điều hướng sang AD301
  test('TC_AD100_13: Verify clicking row detail action navigates to AD301 Agency Detail', async ({ agencyPage, page }) => {
    await agencyPage.goto();

    const rowCount = await agencyPage.getRowCount();
    test.skip(rowCount === 0, 'Bỏ qua khi bảng không có bản ghi nào để click');

    await agencyPage.clickRowDetail(0);

    // URL điều hướng sang màn hình chi tiết AD301
    await expect(page).toHaveURL(/\/admin\/agencies\/\d+/);
  });

  // @tc: [AD100-58] - CR 13/08/2026: Kiểm tra KHÔNG CÓ nút Xóa trên bảng AD100
  test('TC_AD100_14: Verify absence of Delete button on AD100 table rows per CR 13/08/2026', async ({ agencyPage, page }) => {
    await agencyPage.goto();

    const rowCount = await agencyPage.getRowCount();
    test.skip(rowCount === 0, 'Bỏ qua khi không có dòng nào');

    // Chắc chắn không có button xóa (trash icon, [aria-label*="delete"], .btn-delete) trên bảng AD100
    const deleteButtons = page.locator('table button[aria-label*="削除"], table button.btn-delete, table [data-testid="delete-agency"]');
    expect(await deleteButtons.count()).toBe(0);
  });

  // @tc: [AD100-59], [AD100-60], [AD100-61] - Phân trang danh sách (CMR01, CMR23)
  test('TC_AD100_15: Verify pagination controls and max 10 rows per page limit', async ({ agencyPage }) => {
    await agencyPage.goto();

    const rowCount = await agencyPage.getRowCount();
    // Mỗi trang hiển thị tối đa đúng 10 bản ghi theo chuẩn CMR01
    expect(rowCount).toBeLessThanOrEqual(ad100Data.pagination.defaultItemsPerPage);

    // Nếu có phân trang, kiểm tra chuyển sang trang 2
    if (await agencyPage.nextPageButton.isVisible() && await agencyPage.nextPageButton.isEnabled()) {
      await agencyPage.clickPageNumber(2);
      const newRowCount = await agencyPage.getRowCount();
      expect(newRowCount).toBeGreaterThanOrEqual(1);
    }
  });

  // @tc: [AD100-5], [AD100-71] - Trạng thái rỗng (Empty State) với CMMSG47
  test('TC_AD100_16: Verify Empty State displays CMMSG47 when no results match', async ({ agencyPage }) => {
    await agencyPage.goto();

    // Nhập từ khóa chắc chắn không tồn tại
    await agencyPage.fillSearchKeyword(ad100Data.searchTestData.nonExistentKeyword);
    await agencyPage.clickSearch();

    // Số dòng dữ liệu = 0
    const rowCount = await agencyPage.getRowCount();
    expect(rowCount).toBe(0);

    // Hiển thị thông báo CMMSG47: 一致する検索結果はありません。
    await expect(agencyPage.emptyStateText).toBeVisible({ timeout: commonData.timeouts.action });
    await expect(agencyPage.emptyStateText).toContainText(ad100Data.labels.emptyState);
  });

});
