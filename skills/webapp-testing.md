# webapp-testing

Test web applications by scripting browser interactions, asserting UI behavior, and running automated checks.

## What this skill does
Automates browser testing using Playwright or Selenium — navigating pages, clicking elements, filling forms, asserting content, and capturing screenshots.

## Setup
```bash
pip install playwright pytest-playwright
playwright install chromium
```

## Core Playwright patterns

### Basic page test
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("http://localhost:5004")
    assert "Sovereign" in page.title() or page.content()
    page.screenshot(path="screenshot.png")
    browser.close()
```

### Fill form and submit
```python
page.fill("#username", "aria")
page.fill("#password", "plt-sovereign")
page.click("button[type=submit]")
page.wait_for_url("**/dashboard")
assert page.is_visible(".plt-score")
```

### Check API endpoint
```python
import httpx
def check_endpoint(url, expected_keys):
    r = httpx.get(url, timeout=5)
    assert r.status_code == 200
    data = r.json()
    for key in expected_keys:
        assert key in data, f"Missing key: {key}"
    return data
```

### Screenshot regression
```python
page.goto("http://localhost:5004/dashboard")
page.screenshot(path="screenshots/dashboard_current.png", full_page=True)
# Compare with baseline using PIL
from PIL import Image, ImageChops
img1 = Image.open("screenshots/dashboard_baseline.png")
img2 = Image.open("screenshots/dashboard_current.png")
diff = ImageChops.difference(img1, img2)
if diff.getbbox():
    print("Visual regression detected!")
```

## Example commands
```
ACTION: Test the bridge reporter endpoint at localhost:5004 and verify it returns soul metrics
ACTION: Take a full-page screenshot of the kernel dashboard and save to screenshots/
```
