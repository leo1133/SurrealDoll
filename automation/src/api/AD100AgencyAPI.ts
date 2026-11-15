import { APIResponse } from '@playwright/test';
import { CustomApiClient } from './CustomApiClient';
import { apiEndpoints } from '../config/endpoints';

export interface AgencyListPayload {
  q?: string;
  status?: number;
  page?: number;
  items_per_page?: number;
  sort_query?: string | Record<string, any>;
}

/**
 * API Client đóng gói các thao tác gọi API liên quan đến AD100
 * Tuân thủ Rule 05: Trả về raw response, không chứa expect() bên trong
 */
export class AD100AgencyAPI {
  private client: CustomApiClient;

  constructor(client: CustomApiClient) {
    this.client = client;
  }

  /**
   * Gọi API POST /agency/ lấy danh sách Agency kèm bộ lọc và phân trang
   */
  async getAgencyList(payload: AgencyListPayload = {}, customHeaders?: Record<string, string>): Promise<APIResponse> {
    return this.client.post(apiEndpoints.agency.list, payload, customHeaders);
  }

  /**
   * Gọi API với HTTP method không hợp lệ (để test mã lỗi 405)
   */
  async getAgencyListWithMethod(method: 'GET' | 'DELETE' | 'PUT', customHeaders?: Record<string, string>): Promise<APIResponse> {
    return this.client.sendRequest(method, apiEndpoints.agency.list, { headers: customHeaders });
  }
}
