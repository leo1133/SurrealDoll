import { APIRequestContext, APIResponse } from '@playwright/test';
import { env } from '../config/env';
import { commonData } from '../test-data/commonData';
import { Helpers } from '../utils/helpers';

/**
 * CustomApiClient tuân thủ Pillar 5 (Mục 4.2):
 * - Tự động retry khi gặp lỗi tạm thời (502, 503, 504)
 * - Tự động đính kèm Bearer token và Basic auth
 */
export class CustomApiClient {
  private request: APIRequestContext;
  private token: string | null = null;

  constructor(request: APIRequestContext, token?: string) {
    this.request = request;
    if (token) {
      this.token = token;
    }
  }

  setToken(token: string): void {
    this.token = token;
  }

  /**
   * Wrapper request với cơ chế Transient Error Handling (Tự phục hồi lỗi tạm thời)
   */
  async sendRequest(
    method: 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE',
    endpoint: string,
    options: {
      data?: any;
      params?: Record<string, any>;
      headers?: Record<string, string>;
    } = {}
  ): Promise<APIResponse> {
    const url = endpoint.startsWith('http') ? endpoint : `${env.API_BASE_URL}${endpoint}`;

    const headers: Record<string, string> = {
      ...commonData.headers.json,
      ...(this.token ? { Authorization: `Bearer ${this.token}` } : {}),
      ...(options.headers || {}),
    };

    let response: APIResponse;
    const maxRetries = 1;
    let attempt = 0;

    while (attempt <= maxRetries) {
      try {
        response = await this.request.fetch(url, {
          method,
          data: options.data,
          params: options.params,
          headers,
          timeout: commonData.timeouts.action,
        });

        // Nếu gặp lỗi mạng tạm thời 502/503/504 -> retry 01 lần với jitter backoff
        if ([502, 503, 504].includes(response.status()) && attempt < maxRetries) {
          attempt++;
          await Helpers.sleep(500 + Math.random() * 500);
          continue;
        }

        return response;
      } catch (error) {
        if (attempt < maxRetries) {
          attempt++;
          await Helpers.sleep(500);
          continue;
        }
        throw error;
      }
    }

    return response!;
  }

  async get(endpoint: string, params?: Record<string, any>, headers?: Record<string, string>): Promise<APIResponse> {
    return this.sendRequest('GET', endpoint, { params, headers });
  }

  async post(endpoint: string, data?: any, headers?: Record<string, string>): Promise<APIResponse> {
    return this.sendRequest('POST', endpoint, { data, headers });
  }

  async delete(endpoint: string, headers?: Record<string, string>): Promise<APIResponse> {
    return this.sendRequest('DELETE', endpoint, { headers });
  }
}
