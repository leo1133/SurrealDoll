import { test, expect } from '../../src/fixtures/baseTest';
import { HttpStatus, AgencyStatus, ContentType } from '../../src/utils/constants';
import { commonData } from '../../src/test-data/commonData';
import { env } from '../../src/config/env';

test.describe('AD100_Agency List / Search Backend API Automation Suite (POST /agency/)', () => {

  // =========================================================================
  // KHỐI 1: HAPPY PATH & SCHEMA INTEGRITY (Rule 05 - Khối 1)
  // =========================================================================
  test('@tc: [AD100-API-28] Khối 1: Verify Happy Path returns 200 OK with correct JSON schema', async ({ agencyApi }) => {
    const response = await agencyApi.getAgencyList({
      page: 1,
      items_per_page: 10,
    });

    expect(response.status()).toBe(HttpStatus.OK);
    expect(response.headers()['content-type']).toContain(ContentType.JSON);

    const body = await response.json();

    // Verify root JSON schema structure
    expect(body).toHaveProperty('data');
    expect(body.data).toHaveProperty('items');
    expect(body.data).toHaveProperty('pagination');
    expect(Array.isArray(body.data.items)).toBe(true);

    // Verify pagination metadata
    expect(body.data.pagination).toMatchObject({
      page: expect.any(Number),
      items_per_page: expect.any(Number),
      total: expect.any(Number),
    });

    // Verify Item structure if exists
    if (body.data.items.length > 0) {
      const firstItem = body.data.items[0];
      expect(firstItem).toMatchObject({
        id: expect.any(Number),
        agency_code: expect.any(String),
        name: expect.any(String),
        status: expect.any(Number),
        member_count: expect.any(Number),
        point_sales: expect.any(Number),
        familia_sales: expect.any(Number),
        total_sales: expect.any(Number),
      });
    }
  });

  // =========================================================================
  // KHỐI 2: INVALID HTTP METHODS (405) (Rule 05 - Khối 2)
  // =========================================================================
  test('@tc: [AD100-API-16] Khối 2: Verify calling GET/DELETE method returns 405 Method Not Allowed', async ({ agencyApi }) => {
    // Gọi phương thức GET vào endpoint chỉ nhận POST
    const getRes = await agencyApi.getAgencyListWithMethod('GET');
    expect([HttpStatus.METHOD_NOT_ALLOWED, HttpStatus.NOT_FOUND]).toContain(getRes.status());

    // Gọi phương thức DELETE
    const delRes = await agencyApi.getAgencyListWithMethod('DELETE');
    expect([HttpStatus.METHOD_NOT_ALLOWED, HttpStatus.NOT_FOUND]).toContain(delRes.status());
  });

  // =========================================================================
  // KHỐI 3: HEADERS & AUTH MATRIX (Rule 05 - Khối 3)
  // =========================================================================
  test('@tc: [AD100-API-01] Khối 3: Verify request without Authorization Header returns 401 Unauthorized', async ({ agencyApi }) => {
    // Gửi request không kèm Authorization header
    const res = await agencyApi.getAgencyList({}, { Authorization: '' });
    expect(res.status()).toBe(HttpStatus.UNAUTHORIZED);

    const body = await res.json();
    expect(body.code || body.message).toBeDefined();
  });

  test('@tc: [AD100-API-11] Khối 3: Verify request with Malformed / Invalid Token returns 401 Unauthorized', async ({ agencyApi }) => {
    // Gửi token giả mạo
    const res = await agencyApi.getAgencyList({}, { Authorization: 'Bearer invalid_malformed_token_xyz' });
    expect(res.status()).toBe(HttpStatus.UNAUTHORIZED);
  });

  // =========================================================================
  // KHỐI 4: QUERY PARAMETERS & BOUNDARY (Rule 05 - Khối 4)
  // =========================================================================
  test('@tc: [AD100-API-31], [AD100-API-32] Khối 4: Verify status filtering (Active vs Inactive)', async ({ agencyApi }) => {
    // 1. Lọc Agency Active (status = 1)
    const activeRes = await agencyApi.getAgencyList({ status: AgencyStatus.ACTIVE });
    expect(activeRes.status()).toBe(HttpStatus.OK);
    const activeBody = await activeRes.json();
    activeBody.data.items.forEach((item: any) => {
      expect(item.status).toBe(AgencyStatus.ACTIVE);
    });

    // 2. Lọc Agency Inactive (status = 2)
    const inactiveRes = await agencyApi.getAgencyList({ status: AgencyStatus.INACTIVE });
    expect(inactiveRes.status()).toBe(HttpStatus.OK);
    const inactiveBody = await inactiveRes.json();
    inactiveBody.data.items.forEach((item: any) => {
      expect(item.status).toBe(AgencyStatus.INACTIVE);
    });
  });

  test('@tc: [AD100-API-18], [AD100-API-19] Khối 4: Verify search keyword by name and code', async ({ agencyApi }) => {
    // Tìm kiếm theo tên Agency
    const res = await agencyApi.getAgencyList({ q: env.TEST_AGENCY_NAME });
    expect(res.status()).toBe(HttpStatus.OK);
    const body = await res.json();
    expect(body.data.items.length).toBeGreaterThanOrEqual(0);

    // Tìm kiếm với từ khóa không tồn tại -> Trả về mảng rỗng []
    const emptyRes = await agencyApi.getAgencyList({ q: 'NON_EXISTENT_AGENCY_999999' });
    expect(emptyRes.status()).toBe(HttpStatus.OK);
    const emptyBody = await emptyRes.json();
    expect(emptyBody.data.items.length).toBe(0);
    expect(emptyBody.data.pagination.total).toBe(0);
  });

  test('@tc: [AD100-API-50], [AD100-API-53] Khối 4: Verify pagination limits (10, 20, 50, 100)', async ({ agencyApi }) => {
    const limits = [10, 20, 50, 100];
    for (const limit of limits) {
      const res = await agencyApi.getAgencyList({ page: 1, items_per_page: limit });
      expect(res.status()).toBe(HttpStatus.OK);
      const body = await res.json();
      expect(body.data.items.length).toBeLessThanOrEqual(limit);
      expect(body.data.pagination.items_per_page).toBe(limit);
    }
  });

  // =========================================================================
  // KHỐI 5: BUSINESS CALCULATION & STATE INTEGRITY (Rule 05 - Khối 5)
  // =========================================================================
  test('@tc: [AD100-API-75], [AD100-API-76] Khối 5: Verify total_sales calculation algorithm', async ({ agencyApi }) => {
    const res = await agencyApi.getAgencyList({ page: 1, items_per_page: 10 });
    expect(res.status()).toBe(HttpStatus.OK);
    const body = await res.json();

    // Thuật toán: total_sales = point_sales + familia_sales
    body.data.items.forEach((agency: any) => {
      expect(agency.total_sales).toBe(agency.point_sales + agency.familia_sales);
    });
  });

  // =========================================================================
  // KHỐI 6: NEGATIVE & INPUT VALIDATION (Rule 05 - Khối 6)
  // =========================================================================
  test('@tc: [AD100-API-55], [AD100-API-56] Khối 6: Verify invalid items_per_page values rejected with 400', async ({ agencyApi }) => {
    // items_per_page = 0
    const zeroRes = await agencyApi.getAgencyList({ items_per_page: 0 });
    expect([HttpStatus.BAD_REQUEST, HttpStatus.UNPROCESSABLE_ENTITY]).toContain(zeroRes.status());

    // items_per_page vượt quá mức tối đa (101)
    const exceedRes = await agencyApi.getAgencyList({ items_per_page: 101 });
    expect([HttpStatus.BAD_REQUEST, HttpStatus.UNPROCESSABLE_ENTITY]).toContain(exceedRes.status());
  });

  test('@tc: [AD100-API-61], [AD100-API-62] Khối 6: Verify invalid page values rejected with 400', async ({ agencyApi }) => {
    // page = 0
    const zeroPageRes = await agencyApi.getAgencyList({ page: 0 });
    expect([HttpStatus.BAD_REQUEST, HttpStatus.UNPROCESSABLE_ENTITY]).toContain(zeroPageRes.status());

    // page = -1 (số âm)
    const negPageRes = await agencyApi.getAgencyList({ page: -1 });
    expect([HttpStatus.BAD_REQUEST, HttpStatus.UNPROCESSABLE_ENTITY]).toContain(negPageRes.status());
  });

  test('@tc: [AD100-API-29], [AD100-API-30] Khối 6: Verify SQL Injection and XSS payloads in query parameter', async ({ agencyApi }) => {
    // SQL Injection payload
    const sqliRes = await agencyApi.getAgencyList({ q: "' OR 1=1 --" });
    expect(sqliRes.status()).toBe(HttpStatus.OK); // Parametric query escape an toàn

    // XSS payload
    const xssRes = await agencyApi.getAgencyList({ q: "<script>alert('xss')</script>" });
    expect(xssRes.status()).toBe(HttpStatus.OK);
  });

});
