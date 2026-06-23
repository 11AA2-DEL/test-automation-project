from playwright.sync_api import Page
class SearchResultPage():
    def __init__(self,page):
        self.page = page
        self.result = self.page.locator("#sb_result")
    def has_results(self):
        return self.result.is_visible()
    def get_result_count(self):
        return self.result.locator("li.b_algo").conut()