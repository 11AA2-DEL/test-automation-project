from playwright.sync_api import Page

class SearchResultPage:
    def __init__(self, page: Page):
        self.page = page

    def has_results(self):
        """检查搜索结果页是否有至少一个结果链接"""
        return self.page.locator("ol#b_results li h2 a").count() > 0

    def get_result_count(self):
        """获取搜索结果数量，按链接统计"""
        return self.page.locator("ol#b_results li h2 a").count()

