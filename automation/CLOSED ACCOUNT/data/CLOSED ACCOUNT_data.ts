export const CLOSED ACCOUNT_TEST_DATA = [
  {
    id: '[CLOSED ACCOUNT-1]',
    title: '[0] Kiểm tra truy cập màn hình',
    type: 'Auto-UI',
    inputData: { valid: true },
    expectedStatus: 'PASS'
  },
  {
    id: '[CLOSED ACCOUNT-2]',
    title: '[0] Kiểm tra truy cập màn hình',
    type: 'Auto-UI',
    inputData: { valid: true },
    expectedStatus: 'PASS'
  },
  {
    id: '[CLOSED ACCOUNT-3]',
    title: '[Common] Business Rules',
    type: 'Auto-UI',
    inputData: { valid: true },
    expectedStatus: 'PASS'
  },
  {
    id: '[CLOSED ACCOUNT-API-01]',
    title: '[API] /closed account - Gửi request không kèm Authorization header',
    type: 'Auto-API',
    inputData: { valid: true },
    expectedStatus: 'PASS'
  },
  {
    id: '[CLOSED ACCOUNT-API-02]',
    title: '[API] /closed account - Gửi request với Bearer token hết hạn',
    type: 'Auto-API',
    inputData: { valid: true },
    expectedStatus: 'PASS'
  },
  {
    id: '[CLOSED ACCOUNT-API-03]',
    title: '[API] /closed account - Tài khoản thường gọi API quản trị Admin',
    type: 'Auto-API',
    inputData: { valid: true },
    expectedStatus: 'PASS'
  },
  {
    id: '[CLOSED ACCOUNT-API-04]',
    title: '[API] /closed account - Gửi payload body rỗng thiếu trường bắt buộc',
    type: 'Auto-API',
    inputData: { valid: true },
    expectedStatus: 'PASS'
  },
  {
    id: '[CLOSED ACCOUNT-API-05]',
    title: '[API] /closed account - Gửi trường tên vượt quá ký tự tối đa',
    type: 'Auto-API',
    inputData: { valid: true },
    expectedStatus: 'PASS'
  },
  {
    id: '[CLOSED ACCOUNT-API-06]',
    title: '[API] /closed account - Gửi tham số tìm kiếm chứa chuỗi SQL Injection',
    type: 'Auto-API',
    inputData: { valid: true },
    expectedStatus: 'PASS'
  },
  {
    id: '[CLOSED ACCOUNT-API-07]',
    title: '[API] /closed account - Tạo mới hoặc tra cứu dữ liệu hợp lệ',
    type: 'Auto-API',
    inputData: { valid: true },
    expectedStatus: 'PASS'
  },
  {
    id: '[CLOSED ACCOUNT-API-08]',
    title: '[API] /closed account - Đối soát cập nhật dữ liệu vào CSDL (Rule 07)',
    type: 'Auto-API',
    inputData: { valid: true },
    expectedStatus: 'PASS'
  },
  {
    id: '[CLOSED ACCOUNT-API-09]',
    title: '[API] /closed account - Xóa bản ghi (Soft Delete Rule 07)',
    type: 'Auto-API',
    inputData: { valid: true },
    expectedStatus: 'PASS'
  },
];
