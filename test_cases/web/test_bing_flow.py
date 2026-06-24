import pytest
from playwright.sync_api import Page
from pages.search_page import SearchPage
from pages.search_result_page import SearchResultPage
import os
import yaml
class TestBingFlow:
    def test_search_and_check_result(self, page: Page):
        """验证搜索结果数量正常"""
        search_page = SearchPage(page)
        search_page.open()
        search_page.search("Pytest 教程")

        result_page = SearchResultPage(page)
        assert result_page.has_results()

        count = result_page.get_result_count()
        print(f"搜索结果数量: {count}")
        assert count > 0, f"预期至少 1 条结果，实际 {count} 条"
yaml_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "test_data",
    "test_data.yaml"
)
print(yaml_path)
with open(yaml_path, "r", encoding="utf-8") as f:
    test_data = yaml.safe_load(f)

@pytest.mark.parametrize("search_info", test_data["search_verification"])
def test_search_verification(page,search_info):
    search_page = SearchPage(page)
    search_page.open()
    search_page.search(search_info["keyword"])

    result_page = SearchResultPage(page)
    count= result_page.get_result_count()
    print(f"'关键词'{search_info['keyword']}'搜索结果:{count}条")
    assert count >=search_info['min_results'],(
        f"关键词'{search_info['keyword']}'预期至少{search_info['min_result']}条,实际{count}条"
    )






