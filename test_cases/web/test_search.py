import pytest
from pages.search_page import SearchPage
from pages.search_result_page import SearchResultPage
class TestBingSearch:
    def test_search_pytest(self,page):
        search_page = SearchPage(page)
        search_page.open().search("Pytest")
        assert "Pytest" in page.title()
    def test_search_python(self,page):
        search_page = SearchPage(page)
        search_page.open().search("Python 测试开发")
        assert "Python" in page.title()
    def test_search_empty(self,page):
        search_page = SearchPage(page)
        search_page.open().search("")
        assert "必应" in page.title() or "Bing" in page.title()
    def test_search_has_result(self,page):
        search_page = SearchPage(page)
        search_page.open().search("Pytest")
        
        result_page = SearchResultPage(page)
        assert result_page.has_results()
        assert result_page.get_result_count()>0








"""def test_bing_search(page):
    search_page = SearchPage(page)
    search_page.open().search("Pytest 测试框架")
    assert "Pytest" in page.title()"""