from playwright.sync_api import sync_playwright
import time
import os

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 720})

        page.goto("http://localhost:8000/index.html")
        time.sleep(2) # wait for preloader

        scroll_height = page.evaluate("document.documentElement.scrollHeight")
        body_rect = page.evaluate("() => { const r = document.body.getBoundingClientRect(); return {w: r.width, h: r.height, b: r.bottom} }")

        print(f"Final Scroll Height: {scroll_height}")
        print(f"Final Body Rect: {body_rect}")

        preloader_rect = page.evaluate("document.getElementById('preloader').getBoundingClientRect()")
        print(f"Final Preloader Rect: {preloader_rect}")

        browser.close()

if __name__ == "__main__":
    main()
