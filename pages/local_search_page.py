from playwright.sync_api import Page
import os


class LocalSearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_box = page.locator("#search_box")
        self.search_btn = page.locator("#search_btn")
        self.results = page.locator("#results")

    def open(self):
        path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "test_data", "search_page.html"
        )
        self.page.goto(f"file://{path}")
        return self

    def search(self, keyword: str):
        self.search_box.fill(keyword)
        self.search_btn.click()
        self.page.wait_for_timeout(500)

    def has_results(self):
        return self.results.is_visible()

    def get_result_count(self):
        return self.results.locator(".result-item").count()