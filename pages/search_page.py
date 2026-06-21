from playwright.sync_api import Page
class SearchPage:
    def __init__(self,page:Page):
        self.page = page
        self.search_box = page.locator("#sb_form_q")

    def open(self):
        self.page.goto( "https://www.bing.com",
        timeout=10000,
        wait_until="networkidle")
        return self
    def search(self,keyword:str):
        self.search_box.fill(keyword)
        self.page.press("#sb_form_q","Enter")
        self.page.wait_for_timeout(2000)