import pytest
from utils.api_client import ApiClient
from playwright.sync_api import sync_playwright
@pytest.fixture(scope="session")
def api():
    return ApiClient()
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        yield b
        b.close()
@pytest.fixture(scope="session")
def page(browser):
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    yield page
    page.close()