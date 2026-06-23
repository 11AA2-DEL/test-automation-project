import pytest
from pages.search_page import SearchPage
from pages.search_result_page import SearchResultPage
class TestBingFlow:
    def test_search_and_check_reslt(self,page):
        #打开bing首页
        search_page = SearchPage(page)
        search_page.open()
        #搜索
        search_page.search("Pytest 教程")
        result_page = SearchResultPage(page)
        assert result_page.get_result_count() > 0
    def test_empty_search(self,page):
        search_page = SearchPage(page)
        search_page.open()
        search_page.search("")
        #空搜索后标题仍包含Bing
        assert "Bing" in page.title() or "必应" in page.title()
    def test_multi_search(self,page):
        """连续搜索多个关键词"""
        keywords = ["Python","Pytest","Selenium"]
        search_page = SearchPage(page)
        search_page.open()
        for kw in keywords:
            page.fill("#sb_form_q",kw)
            page.press("#sb_form_q","Enter")
            page.wait_for_timeout(1500)
            assert kw in page.title()




