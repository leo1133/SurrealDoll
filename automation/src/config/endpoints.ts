/**
 * Tập trung toàn bộ danh mục Route UI và API Endpoints của dự án
 * Tuyệt đối không gán cứng URL literal trong page hoặc spec
 */
export const routes = {
  login: '/sign-in',
  agencyList: '/admin/agencies',
  agencyCreate: '/admin/agencies/create',
  agencyDetail: (id: number | string) => `/admin/agencies/${id}`,
  agencyStreamers: (id: number | string) => `/admin/agencies/${id}/livers`,
  agencyRevenue: (id: number | string) => `/admin/agencies/${id}/revenue`,
};

export const apiEndpoints = {
  auth: {
    login: '/auth/login',
    refreshToken: '/auth/refresh-token',
  },
  agency: {
    list: '/agency/',
    create: '/agency/create/',
    detail: (id: number | string) => `/agency/${id}/`,
    streamerList: (id: number | string) => `/agency/list/${id}`,
    revenue: (id: number | string) => `/agency/${id}/revenue/`,
  },
};
