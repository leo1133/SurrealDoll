# Automation Handover — AF300 (Gift Update / Delete)

- **Page Object:** `../live2d/src/pages/AF300Page.js` (`// [Pending Live Verification]`)
- **API Client:** `../live2d/src/api/AF300API.js`
- **Test Data:** `../live2d/src/test-data/af300Data.js`, `../live2d/src/test-data/apiAf300Data.js`
- **Test Specs:**
  - UI: `../live2d/tests/ui/af300.ui.spec.js`
  - API: `../live2d/tests/api/af300.api.spec.js`
  - E2E: `../live2d/tests/e2e/af300.e2e.spec.js`
- **Lệnh chạy:**
  ```bash
  npx playwright test tests/ui/af300.ui.spec.js tests/api/af300.api.spec.js tests/e2e/af300.e2e.spec.js
  ```
