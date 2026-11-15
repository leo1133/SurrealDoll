/**
 * Hằng số hệ thống dùng chung theo chuẩn Pillar 5 (Zero-Hardcode)
 */

export enum HttpStatus {
  OK = 200,
  CREATED = 201,
  NO_CONTENT = 204,
  BAD_REQUEST = 400,
  UNAUTHORIZED = 401,
  FORBIDDEN = 403,
  NOT_FOUND = 404,
  METHOD_NOT_ALLOWED = 405,
  CONFLICT = 409,
  UNPROCESSABLE_ENTITY = 422,
  INTERNAL_SERVER_ERROR = 500,
}

export enum HttpMethod {
  GET = 'GET',
  POST = 'POST',
  PUT = 'PUT',
  PATCH = 'PATCH',
  DELETE = 'DELETE',
}

export enum AgencyStatus {
  ALL = 'ALL',
  ACTIVE = 1,    // 利用中
  INACTIVE = 2,  // 停止中
}

export enum SortDirection {
  ASC = 'ASC',
  DESC = 'DESC',
}

export const ContentType = {
  JSON: 'application/json',
  FORM_DATA: 'multipart/form-data',
  PDF: 'application/pdf',
};
