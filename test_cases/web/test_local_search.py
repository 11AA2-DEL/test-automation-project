import pytest
from pages.local_search_page import LocalSearchPage


class TestLocalSearch:
    def test_search_has_results(self, page):
        search_page = LocalSearchPage(page)
        search_page.open()
        search_page.search("测试")
        assert search_page.has_results()

    def test_search_result_count(self, page):
        search_page = LocalSearchPage(page)
        search_page.open()
        search_page.search("测试")
        assert search_page.get_result_count() == 3

    def test_title_contains_keyword(self, page):
        search_page = LocalSearchPage(page)
        search_page.open()
        search_page.search("Pytest")
        assert "Pytest" in page.title()