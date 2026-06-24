import os
import yaml
import pytest
import requests
from playwright.sync_api import sync_playwright

file_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(file_dir))
yaml_path = os.path.join(project_root, "test_data", "test_data.yaml")

with open(yaml_path, 'r', encoding="utf-8") as f:
    test_data = yaml.safe_load(f)
@pytest.mark.parametrize("post",test_data["post"])
def test_post_from_yaml(post):
    resp = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post['id']}")
    assert resp.status_code == post.get("expected_status",200)
@pytest.mark.parametrize("search",test_data["searches"])
def test_baidu_search_from_yaml(search):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.bing.com")
        print(f"页面标题:{page.title()}")
        page.fill('#sb_form_q',search["keyword"])
        page.press("#sb_form_q", "Enter")
        print(f'搜索后标题:{page.title()}')
        assert search["keyword"] in page.url
        browser.close()



