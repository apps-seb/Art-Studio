import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 800})

        await page.goto("http://localhost:8000/index.html")
        await page.evaluate("""
            document.body.style.zoom = '0.5';
        """)
        await asyncio.sleep(2)
        await page.screenshot(path="zoom_0.5.png", full_page=True)

        await page.reload()
        await page.evaluate("""
            document.documentElement.style.transform = 'scale(0.5)';
            document.documentElement.style.transformOrigin = 'top left';
            document.documentElement.style.width = '200vw';
            document.documentElement.style.height = '200vh'; // or auto
        """)
        await asyncio.sleep(2)
        await page.screenshot(path="transform_html_0.5.png", full_page=True)

        await browser.close()

asyncio.run(main())
