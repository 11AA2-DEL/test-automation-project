import yaml
import os
import pytest
from pages.search_page import SearchPage
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
#加载YAML数据
yaml_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "test_data","test_data.yaml"

    )
with open(yaml_path,"r",encoding="utf-8") as f:
    test_data = yaml.safe_load(f)
@pytest.mark.parametrize("search_data", test_data["ui_searches"])
def test_search_from_yaml(page, search_data):
    search_page = SearchPage(page)
    search_page.open().search(search_data["keyword"])
    assert search_data["keyword"] in page.title()






