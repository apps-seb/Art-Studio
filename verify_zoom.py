import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 800})
        await page.goto("http://localhost:8000/index.html")

        # Test 1: zoom
        await page.evaluate("document.body.style.zoom = '0.5'")
        await asyncio.sleep(2)
        await page.screenshot(path="zoom_05.png", full_page=False)

        # Test 2: transform
        await page.reload()
        await page.evaluate("""
            document.body.style.transform = 'scale(0.5)';
            document.body.style.transformOrigin = 'top left';
            document.body.style.width = '200vw';
        """)
        await asyncio.sleep(2)
        await page.screenshot(path="transform_05.png", full_page=False)

        await browser.close()

asyncio.run(main())
