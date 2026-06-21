
from pages.search_page import SearchPage

def test_bing_search(page):
    search_page = SearchPage(page)
    search_page.open().search("Pytest 测试框架")
    assert "Pytest" in page.title()