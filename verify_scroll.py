from playwright.sync_api import sync_playwright
import time

def take_screenshots():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 800})

        # Go to the local server
        page.goto('http://localhost:3000')
        page.wait_for_load_state('networkidle')
        time.sleep(2) # let gsap initialize

        # Scroll down to the #about-studio section
        # Find the bounding box to scroll exactly to its top
        about_box = page.locator('#about-studio').bounding_box()
        page.evaluate(f"window.scrollTo(0, {about_box['y']})")
        time.sleep(1)

        # We are at the top of the #about-studio section (pinned start)
        page.screenshot(path='about_step_1.png')
        print("Captured about_step_1.png")

        # Scroll down
        page.evaluate("window.scrollBy(0, window.innerHeight)")
        time.sleep(1)
        page.screenshot(path='about_step_2.png')
        print("Captured about_step_2.png")

        # Scroll down again
        page.evaluate("window.scrollBy(0, window.innerHeight)")
        time.sleep(1)
        page.screenshot(path='about_step_3.png')
        print("Captured about_step_3.png")

        # Scroll down again
        page.evaluate("window.scrollBy(0, window.innerHeight)")
        time.sleep(1)
        page.screenshot(path='about_step_4.png')
        print("Captured about_step_4.png")

        browser.close()

if __name__ == "__main__":
    take_screenshots()
