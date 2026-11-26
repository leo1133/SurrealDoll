# Automation Handover — AF200 (Gift Create)

- **Page Object:** `../live2d/src/pages/AF200Page.js` (`// [Pending Live Verification]`)
- **API Client:** `../live2d/src/api/AF200API.js`
- **Test Data:** `../live2d/src/test-data/af200Data.js`, `../live2d/src/test-data/apiAf200Data.js`
- **Test Specs:**
  - UI: `../live2d/tests/ui/af200.ui.spec.js`
  - API: `../live2d/tests/api/af200.api.spec.js`
  - E2E: `../live2d/tests/e2e/af200.e2e.spec.js`
- **Lệnh chạy:**
  ```bash
  npx playwright test tests/ui/af200.ui.spec.js tests/api/af200.api.spec.js tests/e2e/af200.e2e.spec.js
  ```
