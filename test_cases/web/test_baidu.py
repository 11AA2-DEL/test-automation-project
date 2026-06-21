"""import pytest
from playwright.sync_api import sync_playwright
from pages.baidu_page import BaiduPage
@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()
def test_baidu_search(page):
    baidu = BaiduPage(page)
    baidu.open().search("测试开发")
    assert "测试开发" in page.title()"""