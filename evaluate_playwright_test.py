from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 720})

    page.set_content("""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      body {
        margin: 0;
        transform: scale(0.5);
        transform-origin: top left;
        width: 200%;
        height: 200%;
      }
      .vh { height: 100vh; background: red; }
      .preloader { position: fixed; top: 0; left: 0; width: 100%; height: 100vh; background: blue; opacity: 0.5; }
    </style>
    </head>
    <body>
      <div class="vh"></div>
      <div class="preloader"></div>
    </body>
    </html>
    """)
    rect = page.evaluate("document.querySelector('.preloader').getBoundingClientRect()")
    print("Transform Preloader:", rect)

    page.set_content("""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      body {
        margin: 0;
        zoom: 0.5;
      }
      .vh { height: 100vh; background: red; }
      .preloader { position: fixed; top: 0; left: 0; width: 100%; height: 100vh; background: blue; opacity: 0.5; }
    </style>
    </head>
    <body>
      <div class="vh"></div>
      <div class="preloader"></div>
    </body>
    </html>
    """)
    rect = page.evaluate("document.querySelector('.preloader').getBoundingClientRect()")
    print("Zoom Preloader:", rect)

    browser.close()
