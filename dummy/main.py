import pytest
from playwright.sync_api import Playwright, Browser, Page

@pytest.fixture(scope='module')
def playwright() -> Playwright:
    from playwright.sync_api import Playwright
    with Playwright() as playwright:
        yield playwright

@pytest.fixture(scope='module')
def browser(playwright: Playwright) -> Browser:
    from playwright.sync_api import BrowserType
    browser = playwright.chromium.launch()
    yield browser
    browser.close()

@pytest.fixture(scope='module')
def page(browser: Browser) -> Page:
    page = browser.new_page()
    yield page
    page.close()

def test_playwright_search(page: Page):
    page.goto('https://www.google.com')
    page.fill('input[name="q"]', 'Playwright')
    page.press('input[name="q"]', 'Enter')
    assert page.title() == 'Playwright - Google Search'

# You can add more test functions here

if __name__ == '__main__':
    pytest.main(['-v', '--html=report.html'])
