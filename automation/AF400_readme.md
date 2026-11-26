# Automation Handover — AF400 (Gift Category Manage)

- **Page Object:** `../live2d/src/pages/AF400Page.js` (`// [Pending Live Verification]`)
- **API Client:** `../live2d/src/api/AF400API.js`
- **Test Data:** `../live2d/src/test-data/af400Data.js`, `../live2d/src/test-data/apiAf400Data.js`
- **Test Specs:**
  - UI: `../live2d/tests/ui/af400.ui.spec.js`
  - API: `../live2d/tests/api/af400.api.spec.js`
  - E2E: `../live2d/tests/e2e/af400.e2e.spec.js`
- **Lệnh chạy:**
  ```bash
  npx playwright test tests/ui/af400.ui.spec.js tests/api/af400.api.spec.js tests/e2e/af400.e2e.spec.js
  ```
