from playwright.sync_api import sync_playwright
import time

def test_simple():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("1. 访问百度...")
        page.goto("https://www.baidu.com")

        print("2. 等待2秒...")
        page.wait_for_timeout(2000)

        print("3. 尝试用JS输入...")
        # 直接用 JavaScript 输入
        page.evaluate('''
                      document.querySelector('#kw').value = 'pytest';
                      document.querySelector('#su').click();
                      ''')

        print("4. 等待结果...")
        print(f"开始等待，时间：{time.strftime('%H:%M:%S')}")
        page.wait_for_timeout(10000)
        print(f"等待结束，时间：{time.strftime('%H:%M:%S')}")
        print(f"5. 页面标题: {page.title()}")
        browser.close()


if __name__ == "__main__":
    test_simple()