/**
 * Dữ liệu tĩnh dùng chung toàn dự án (Single Source of Truth)
 */

export const commonData = {
  timeouts: {
    pageLoad: 15000,
    modal: 5000,
    action: 10000,
    suite: 60000,
    debounceWait: 500,
  },

  errorMessages: {
    unexpectedServer: 'CMMSG1: 予期しないサーバーエラーが発生しました。',
    unauthorized: 'CMMSG4: 認証されていないアクセスです。再度ログインしてください。',
    permissionDenied: 'CMMSG5: この操作を行う権限がありません。',
    networkError: 'CMMSG8: ネットワークエラー。接続を確認してください。',
    sessionExpired: 'CMMSG10: ログインの有効期限が切れました。再度ログインしてください。',
    noSearchResult: 'CMMSG47: 一致する検索結果はありません。',
  },

  headers: {
    json: {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
    },
    wildcard: {
      'Accept': '*/*',
    },
  },
};
