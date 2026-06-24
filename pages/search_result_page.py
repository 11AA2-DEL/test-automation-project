from playwright.sync_api import Page

class SearchResultPage:
    def __init__(self, page: Page):
        self.page = page

    def has_results(self):
        """只要有至少一个链接，就认为有结果"""
        return self.page.locator("a h3").count() > 0

    def get_result_count(self):
        """统计搜索结果数量"""
        return self.page.locator("a h3").count()