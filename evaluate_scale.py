import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 800})

        # Original
        await page.goto("http://localhost:8000/index.html")
        await asyncio.sleep(1)
        orig_height = await page.evaluate("document.body.scrollHeight")

        # Transform html
        await page.evaluate("""
            document.documentElement.style.transform = 'scale(0.5)';
            document.documentElement.style.transformOrigin = 'top left';
            document.documentElement.style.width = '200vw';
        """)
        await asyncio.sleep(1)
        transform_height = await page.evaluate("document.body.scrollHeight")

        # Meta viewport (only works on mobile emulation usually, but let's check)
        await page.reload()
        await page.evaluate("""
            document.querySelector('meta[name="viewport"]').setAttribute('content', 'width=device-width, initial-scale=0.5, maximum-scale=0.5, minimum-scale=0.5, user-scalable=no');
        """)
        await asyncio.sleep(1)

        # Zoom
        await page.reload()
        await page.evaluate("document.body.style.zoom = '0.5'")
        await asyncio.sleep(1)
        zoom_height = await page.evaluate("document.body.scrollHeight")

        print(f"Original scrollHeight: {orig_height}")
        print(f"Transform scrollHeight: {transform_height}")
        print(f"Zoom scrollHeight: {zoom_height}")

        await browser.close()

asyncio.run(main())
