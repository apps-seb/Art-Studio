from playwright.sync_api import sync_playwright
import time
import os

def main():
    os.system("git checkout index.html")

    with open("index.html", "r") as f:
        content = f.read()

    new_content = content.replace("body {\n            background-color: #EAE5DF;", "body {\n            transform: scale(0.5);\n            transform-origin: top left;\n            width: 200vw;\n            height: 200vh;\n            background-color: #EAE5DF;")

    with open("index.html", "w") as f:
        f.write(new_content)

    print("Injected transform")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 720})

        page.goto("http://localhost:8000/index.html")
        time.sleep(2) # wait for preloader

        scroll_height = page.evaluate("document.documentElement.scrollHeight")
        body_rect = page.evaluate("() => { const r = document.body.getBoundingClientRect(); return {w: r.width, h: r.height, b: r.bottom} }")

        print(f"Transform Scroll Height: {scroll_height}")
        print(f"Transform Body Rect: {body_rect}")

        browser.close()

if __name__ == "__main__":
    main()
