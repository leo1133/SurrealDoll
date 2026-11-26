# Automation Handover — AF100 (Gift List)

- **Page Object:** `../live2d/src/pages/AF100Page.js` (`// [Pending Live Verification]`)
- **API Client:** `../live2d/src/api/AF100API.js`
- **Test Data:** `../live2d/src/test-data/af100Data.js`, `../live2d/src/test-data/apiAf100Data.js`
- **Test Specs:**
  - UI: `../live2d/tests/ui/af100.ui.spec.js`
  - API: `../live2d/tests/api/af100.api.spec.js`
  - E2E: `../live2d/tests/e2e/af100.e2e.spec.js`
- **Lệnh chạy:**
  ```bash
  npx playwright test tests/ui/af100.ui.spec.js tests/api/af100.api.spec.js tests/e2e/af100.e2e.spec.js
  ```
