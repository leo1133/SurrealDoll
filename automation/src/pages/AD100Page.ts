import { Page, Locator } from '@playwright/test';
import { BasePage } from './BasePage';
import { routes, apiEndpoints } from '../config/endpoints';
import { ad100Data } from '../test-data/ad100Data';
import { commonData } from '../test-data/commonData';

/**
 * Page Object Model cho màn hình AD100_Agency List / Search (事務所一覧・検索)
 * Tuân thủ Rule 05: Chỉ chứa khai báo phần tử (Locators) & Thao tác hành động (Actions).
 * Tuyệt đối không chứa câu lệnh expect() kiểm tra kết quả bên trong class này.
 */
export class AD100Page extends BasePage {
  // Navigation & Header
  readonly breadcrumb: Locator;
  readonly sidebarMenu: Locator;
  readonly sidebarSubmenu: Locator;

  // Search Controls
  readonly searchInput: Locator;
  readonly statusDropdown: Locator;
  readonly searchButton: Locator;
  readonly clearButton: Locator;
  readonly createButton: Locator;

  // Table Headers
  readonly table: Locator;
  readonly tableHeaderId: Locator;
  readonly tableHeaderAgencyId: Locator;
  readonly tableHeaderAgencyName: Locator;
  readonly tableHeaderContactOwner: Locator;
  readonly tableHeaderStreamerCount: Locator;
  readonly tableHeaderPointSales: Locator;
  readonly tableHeaderFamiliaSales: Locator;
  readonly tableHeaderTotalSales: Locator;
  readonly tableHeaderStatus: Locator;
  readonly tableHeaderCreatedAt: Locator;
  readonly tableHeaderUpdatedAt: Locator;

  // Table Data & Rows
  readonly tableRows: Locator;
  readonly emptyStateText: Locator;
  readonly loadingSpinner: Locator;

  // Pagination Controls
  readonly paginationContainer: Locator;
  readonly prevPageButton: Locator;
  readonly nextPageButton: Locator;
  readonly firstPageButton: Locator;
  readonly lastPageButton: Locator;

  constructor(page: Page) {
    super(page);

    // 1. Navigation & Breadcrumb (Tham chiếu qua ad100Data.selectors)
    this.breadcrumb = page.locator(ad100Data.selectors.breadcrumb).or(page.getByText(ad100Data.labels.breadcrumbs));
    this.sidebarMenu = page.getByRole('button', { name: ad100Data.labels.sidebarMenu });
    this.sidebarSubmenu = page.getByRole('link', { name: ad100Data.labels.sidebarSubmenu });

    // 2. Search & Action Controls
    this.searchInput = page.getByPlaceholder(ad100Data.placeholders.searchInput).or(page.locator(ad100Data.selectors.searchInput));
    this.statusDropdown = page.getByRole('combobox', { name: ad100Data.labels.statusDropdown }).or(page.locator(ad100Data.selectors.statusDropdown));
    this.searchButton = page.getByRole('button', { name: ad100Data.labels.btnSearch, exact: true });
    this.clearButton = page.getByRole('button', { name: ad100Data.labels.btnClear, exact: true });
    this.createButton = page.getByRole('button', { name: ad100Data.labels.btnCreate, exact: true });

    // 3. Table Headers
    this.table = page.getByRole('table').or(page.locator(ad100Data.selectors.dataTable));
    this.tableHeaderId = this.table.locator(ad100Data.selectors.tableHeaders).filter({ hasText: ad100Data.tableHeaders.id });
    this.tableHeaderAgencyId = this.table.locator(ad100Data.selectors.tableHeaders).filter({ hasText: ad100Data.tableHeaders.agencyId });
    this.tableHeaderAgencyName = this.table.locator(ad100Data.selectors.tableHeaders).filter({ hasText: ad100Data.tableHeaders.agencyName });
    this.tableHeaderContactOwner = this.table.locator(ad100Data.selectors.tableHeaders).filter({ hasText: ad100Data.tableHeaders.contactOwner });
    this.tableHeaderStreamerCount = this.table.locator(ad100Data.selectors.tableHeaders).filter({ hasText: ad100Data.tableHeaders.streamerCount });
    this.tableHeaderPointSales = this.table.locator(ad100Data.selectors.tableHeaders).filter({ hasText: ad100Data.tableHeaders.pointSales });
    this.tableHeaderFamiliaSales = this.table.locator(ad100Data.selectors.tableHeaders).filter({ hasText: ad100Data.tableHeaders.familiaSales });
    this.tableHeaderTotalSales = this.table.locator(ad100Data.selectors.tableHeaders).filter({ hasText: ad100Data.tableHeaders.totalSales });
    this.tableHeaderStatus = this.table.locator(ad100Data.selectors.tableHeaders).filter({ hasText: ad100Data.tableHeaders.status });
    this.tableHeaderCreatedAt = this.table.locator(ad100Data.selectors.tableHeaders).filter({ hasText: ad100Data.tableHeaders.createdAt });
    this.tableHeaderUpdatedAt = this.table.locator(ad100Data.selectors.tableHeaders).filter({ hasText: ad100Data.tableHeaders.updatedAt });

    // 4. Data Rows & States
    this.tableRows = this.table.locator(ad100Data.selectors.tableRows);
    this.emptyStateText = page.getByText(ad100Data.labels.emptyState).or(page.locator(ad100Data.selectors.emptyState));
    this.loadingSpinner = page.locator(ad100Data.selectors.loadingSpinner);

    // 5. Pagination Controls
    this.paginationContainer = page.locator(ad100Data.selectors.paginationContainer);
    this.prevPageButton = page.getByRole('button', { name: ad100Data.pagination.prevBtn }).or(page.locator(ad100Data.selectors.prevPageButton));
    this.nextPageButton = page.getByRole('button', { name: ad100Data.pagination.nextBtn }).or(page.locator(ad100Data.selectors.nextPageButton));
    this.firstPageButton = page.getByRole('button', { name: ad100Data.pagination.firstBtn }).or(page.locator(ad100Data.selectors.firstPageButton));
    this.lastPageButton = page.getByRole('button', { name: ad100Data.pagination.lastBtn }).or(page.locator(ad100Data.selectors.lastPageButton));
  }

  // Parameterized Locators
  getTableCell(rowIndex: number = 0, columnName: keyof typeof ad100Data.selectors.columns = 'id'): Locator {
    const colIndex = ad100Data.selectors.columns[columnName];
    return this.tableRows.nth(rowIndex).locator(ad100Data.selectors.tableCells).nth(colIndex);
  }

  getSidebarMenu(menuName: string = ad100Data.labels.sidebarMenu): Locator {
    return this.page.getByRole('button', { name: menuName });
  }

  getSidebarSubmenu(submenuName: string = ad100Data.labels.sidebarSubmenu): Locator {
    return this.page.getByRole('link', { name: submenuName });
  }

  /**
   * Điều hướng vào màn hình AD100
   */
  async goto(queryParams?: string): Promise<void> {
    const url = queryParams ? `${routes.agencyList}?${queryParams}` : routes.agencyList;
    await this.page.goto(url, { timeout: commonData.timeouts.pageLoad });
    await this.waitForLoadingDetached(this.loadingSpinner);
  }

  /**
   * Nhập từ khóa tìm kiếm
   */
  async fillSearchKeyword(keyword: string): Promise<void> {
    await this.searchInput.fill(keyword);
  }

  /**
   * Chọn trạng thái từ dropdown
   */
  async selectStatus(statusText: string): Promise<void> {
    await this.statusDropdown.click();
    await this.page.getByRole('option', { name: statusText }).click();
  }

  /**
   * Thực hiện tìm kiếm kèm theo chờ hoàn tất request mạng (Smart Waiting)
   */
  async clickSearch(): Promise<void> {
    await Promise.all([
      this.page.waitForResponse((resp) => resp.url().includes(apiEndpoints.agency.list) && resp.status() === 200).catch(() => {}),
      this.searchButton.click(),
    ]);
    await this.waitForLoadingDetached(this.loadingSpinner);
  }

  /**
   * Nhấn Enter trên ô tìm kiếm
   */
  async pressEnterInSearch(): Promise<void> {
    await Promise.all([
      this.page.waitForResponse((resp) => resp.url().includes(apiEndpoints.agency.list) && resp.status() === 200).catch(() => {}),
      this.searchInput.press('Enter'),
    ]);
    await this.waitForLoadingDetached(this.loadingSpinner);
  }

  /**
   * Click nút クリア (Reset bộ lọc)
   */
  async clickClear(): Promise<void> {
    await Promise.all([
      this.page.waitForResponse((resp) => resp.url().includes(apiEndpoints.agency.list) && resp.status() === 200).catch(() => {}),
      this.clearButton.click(),
    ]);
    await this.waitForLoadingDetached(this.loadingSpinner);
  }

  /**
   * Click nút 新規登録 (Điều hướng sang AD200)
   */
  async clickCreateAgency(): Promise<void> {
    await Promise.all([
      this.page.waitForNavigation({ timeout: commonData.timeouts.pageLoad }).catch(() => {}),
      this.createButton.click(),
    ]);
  }

  /**
   * Sort cột 作成日 (Ngày tạo)
   */
  async clickSortCreatedAt(): Promise<void> {
    await Promise.all([
      this.page.waitForResponse((resp) => resp.url().includes(apiEndpoints.agency.list)).catch(() => {}),
      this.tableHeaderCreatedAt.click(),
    ]);
    await this.waitForLoadingDetached(this.loadingSpinner);
  }

  /**
   * Sort cột 変更日 (Ngày cập nhật)
   */
  async clickSortUpdatedAt(): Promise<void> {
    await Promise.all([
      this.page.waitForResponse((resp) => resp.url().includes(apiEndpoints.agency.list)).catch(() => {}),
      this.tableHeaderUpdatedAt.click(),
    ]);
    await this.waitForLoadingDetached(this.loadingSpinner);
  }

  /**
   * Lấy số lượng bản ghi hiển thị trên bảng
   */
  async getRowCount(): Promise<number> {
    return await this.tableRows.count();
  }

  /**
   * Click vào cột ライバー数 (CR 06/11/2025: Điều hướng sang AD302)
   */
  async clickStreamerCount(rowIndex: number = 0): Promise<void> {
    const streamerCountCell = this.getTableCell(rowIndex, 'streamerCount');
    await Promise.all([
      this.page.waitForNavigation({ timeout: commonData.timeouts.pageLoad }).catch(() => {}),
      streamerCountCell.click(),
    ]);
  }

  /**
   * Click vào dòng Agency hoặc nút Chi tiết (Điều hướng sang AD301)
   */
  async clickRowDetail(rowIndex: number = 0): Promise<void> {
    const actionCell = this.getTableCell(rowIndex, 'actions');
    await Promise.all([
      this.page.waitForNavigation({ timeout: commonData.timeouts.pageLoad }).catch(() => {}),
      actionCell.click(),
    ]);
  }

  /**
   * Click chuyển sang số trang cụ thể
   */
  async clickPageNumber(pageNumber: number): Promise<void> {
    const pageBtn = this.paginationContainer.getByRole('button', { name: String(pageNumber), exact: true });
    await Promise.all([
      this.page.waitForResponse((resp) => resp.url().includes(apiEndpoints.agency.list)).catch(() => {}),
      pageBtn.click(),
    ]);
    await this.waitForLoadingDetached(this.loadingSpinner);
  }
}

export { AD100Page as AD100AgencyListPage };
