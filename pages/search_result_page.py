from playwright.sync_api import Page

class SearchResultPage:
    def __init__(self, page: Page):
        self.page = page

    def has_results(self):
        """搜索结果页是否有 h2 标题"""
        return self.page.locator("h2").count() > 0

    def get_result_count(self):
        """获取搜索结果数量，按链接统计"""
        return self.page.locator("ol#b_results li h2 a").count()

    result_page = SearchResultPage(page)
    print("result_count:", result_page.get_result_count())
    assert result_page.get_result_count() > 0
