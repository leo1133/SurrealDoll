/**
 * Dữ liệu tĩnh đặc thù cho màn hình AD100 (Agency List & Search)
 * Áp dụng: Tiêu chí kiểm duyệt 3, 4, 6 (Không viết string trực tiếp trong expect)
 */

export const ad100Data = {
  labels: {
    breadcrumbs: '＞ 事務所管理',
    screenTitle: '事務所一覧',
    sidebarMenu: '事務所管理',
    sidebarSubmenu: '事務所一覧',
    statusDropdown: 'ステータス',
    btnSearch: '検索',
    btnClear: 'クリア',
    btnCreate: '新規登録',
    emptyState: '一致する検索結果はありません。',
  },

  placeholders: {
    searchInput: '事務所名・事務所ID',
  },

  dropdownOptions: {
    status: {
      all: '全て',
      active: '利用中',
      inactive: '停止中',
    },
  },

  tableHeaders: {
    id: 'ID',
    agencyId: '事務所ID',
    agencyName: '事務所名',
    contactOwner: '連絡先 オーナー名',
    streamerCount: 'ライバー数',
    pointSales: 'ポイント売上',
    familiaSales: 'ファミリア売上',
    totalSales: '売上合計',
    status: 'ステータス',
    createdAt: '作成日',
    updatedAt: '変更日',
    actions: '操作',
  },

  pagination: {
    defaultItemsPerPage: 10,
    allowedLimits: [10, 20, 50, 100],
    nextBtn: '次>>',
    prevBtn: '<<前',
    firstBtn: '<<',
    lastBtn: '>>',
  },

  searchTestData: {
    nonExistentKeyword: 'NON_EXISTENT_AGENCY_XYZ_99999',
    specialCharacters: '!@#$%^&*()',
    spacesAround: '  Agency  ',
    kanjiKeyword: '事務所',
    latinKeyword: 'Agency',
  },
};
