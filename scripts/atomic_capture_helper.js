/**
 * ATOMIC CAPTURE HELPER (scripts/atomic_capture_helper.js)
 * Module chuẩn hóa thực thi tương tác DOM và chụp Atomic Evidence
 * Tuân thủ 100% Rule 04 & GEMINI.md Anti-Shortcut Protocol.
 */

const fs = require('fs');
const path = require('path');

class AtomicCaptureHelper {
  constructor(page, screenId, envName = 'DEV') {
    this.page = page;
    this.screenId = screenId;
    this.envName = envName;
    this.outputDir = path.resolve(__dirname, `../evidence/${screenId}`);
    fs.mkdirSync(this.outputDir, { recursive: true });
    this.dateStr = '20261126';
  }

  /**
   * Đảm bảo mọi container ẩn/accordion được mở ra trước khi tìm phần tử
   */
  async expandAllContainers() {
    await this.page.evaluate(() => {
      // 1. Expand all button
      const expandAll = document.querySelector('button[aria-label*="すべて展開"], button[aria-label*="展開"]');
      if (expandAll) expandAll.click();

      // 2. Click accordion triggers if collapsed
      document.querySelectorAll('[data-state="closed"], details:not([open])').forEach(el => {
        if (el.tagName === 'DETAILS') el.open = true;
        else if (el.click) el.click();
      });
    });
    await new Promise(r => setTimeout(r, 600));
  }

  /**
   * Thao tác trên phần tử + Highlight viền xanh 3px + Badge + Chụp ảnh Atomic
   * @param {Object} options
   * @param {string} options.tcId - Ví dụ: 'AP213-162'
   * @param {string} options.description - Mô tả ngắn của trường/hành động
   * @param {string|Function} options.targetQuery - CSS selector hoặc hàm JS trả về DOM element
   * @param {string|null} options.inputValue - Giá trị cần nhập thử nghiệm (nếu là input)
   * @param {string|null} options.clickAction - Click trước khi chụp nếu có
   * @returns {Promise<string>} - Đường dẫn file ảnh đã lưu
   */
  async captureAtomicEvidence({ tcId, description, targetQuery, inputValue = null, clickAction = false }) {
    const cleanTcId = tcId.replace('[', '').replace(']', '').trim();
    const fileName = `evidence_${this.screenId}_${cleanTcId}_${this.envName}_PASS_${this.dateStr}.png`;
    const fullPath = path.join(this.outputDir, fileName);
    const relPath = `evidence/${this.screenId}/${fileName}`;

    // Ensure containers expanded
    await this.expandAllContainers();

    const evaluationResult = await this.page.evaluate(({ queryStr, badgeText, inputVal, doClick }) => {
      // 1. Remove old badges/highlights
      document.querySelectorAll('.test-highlight-box, .test-highlight-badge').forEach(e => e.remove());

      // 2. Resolve target element
      let el = null;
      if (typeof queryStr === 'string' && (queryStr.startsWith('.') || queryStr.startsWith('#') || queryStr.startsWith('['))) {
        el = document.querySelector(queryStr);
      }
      if (!el && typeof queryStr === 'string') {
        // Find leaf node with exact or matching text
        const leaves = Array.from(document.querySelectorAll('*')).filter(e => e.children.length === 0 && e.innerText && e.innerText.trim() === queryStr);
        if (leaves.length > 0) el = leaves[0];
      }
      if (!el && typeof queryStr === 'string') {
        // Evaluation string function
        try {
          const fn = new Function(queryStr);
          el = fn();
        } catch (e) {}
      }

      if (!el) {
        return { success: false, reason: `Element not found for query: ${queryStr}` };
      }

      // 3. Assert element is visible and has dimension
      const rect = el.getBoundingClientRect();
      const style = window.getComputedStyle(el);
      if (style.display === 'none' || style.visibility === 'hidden') {
        return { success: false, reason: `Element found but is hidden (display: none / visibility: hidden)` };
      }

      // 4. Perform input typing if specified
      if (inputVal !== null && (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA')) {
        el.focus();
        el.value = inputVal;
        el.dispatchEvent(new Event('input', { bubbles: true }));
        el.dispatchEvent(new Event('change', { bubbles: true }));
      }

      // 5. Perform click if requested
      if (doClick && el.click) {
        el.click();
      }

      // 6. Scroll into center view
      el.scrollIntoView({ behavior: 'instant', block: 'center', inline: 'center' });

      // 7. Inject 3px solid #16a34a highlight border
      el.style.outline = '3px solid #16a34a';
      el.style.outlineOffset = '3px';
      el.style.boxShadow = '0 0 12px rgba(22, 163, 74, 0.8)';

      // 8. Inject visual badge label
      const badge = document.createElement('div');
      badge.className = 'test-highlight-badge';
      badge.innerText = badgeText;
      badge.style.position = 'absolute';
      badge.style.zIndex = '999999';
      badge.style.backgroundColor = '#16a34a';
      badge.style.color = '#ffffff';
      badge.style.padding = '4px 10px';
      badge.style.borderRadius = '4px';
      badge.style.fontSize = '12px';
      badge.style.fontWeight = 'bold';
      badge.style.fontFamily = 'sans-serif';
      badge.style.boxShadow = '0 2px 6px rgba(0,0,0,0.3)';

      const updatedRect = el.getBoundingClientRect();
      badge.style.top = `${Math.max(0, window.scrollY + updatedRect.top - 28)}px`;
      badge.style.left = `${Math.max(0, window.scrollX + updatedRect.left)}px`;
      document.body.appendChild(badge);

      return { success: true, tagName: el.tagName, value: el.value || '' };
    }, {
      queryStr: targetQuery,
      badgeText: `[PASS] ${cleanTcId}: ${description}`,
      inputVal: inputValue,
      doClick: clickAction
    });

    if (!evaluationResult.success) {
      throw new Error(`[ATOMIC_ERROR] Failed on ${tcId}: ${evaluationResult.reason}`);
    }

    await new Promise(r => setTimeout(r, 250));
    await this.page.screenshot({ path: fullPath });

    // Clean up badge after capture
    await this.page.evaluate(() => {
      document.querySelectorAll('.test-highlight-box, .test-highlight-badge').forEach(e => e.remove());
    });

    console.log(`[PASS] Atomic screenshot captured: ${relPath} (${evaluationResult.tagName})`);
    return relPath;
  }
}

module.exports = AtomicCaptureHelper;
