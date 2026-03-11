const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('http://localhost:3000/#servicios');
  await page.waitForTimeout(5000);
  await page.screenshot({ path: 'images_fixed_servicios.png', fullPage: true });
  await browser.close();
})();
