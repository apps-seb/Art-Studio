const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 1440, height: 1080 }
  });
  await page.goto('http://localhost:3000/#contacto');
  await page.waitForTimeout(5000);
  await page.screenshot({ path: 'footer_premium.png', fullPage: true });
  await browser.close();
})();
