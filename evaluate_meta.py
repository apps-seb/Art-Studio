import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 800})

        await page.goto("http://localhost:8000/index.html")
        await page.evaluate("""
            const meta = document.querySelector('meta[name="viewport"]');
            meta.setAttribute('content', 'width=device-width, initial-scale=0.5, maximum-scale=0.5, minimum-scale=0.5, user-scalable=no');
        """)
        await asyncio.sleep(2)
        await page.screenshot(path="meta_viewport_0.5.png", full_page=True)

        await browser.close()

asyncio.run(main())
