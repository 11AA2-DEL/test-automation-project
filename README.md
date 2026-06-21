#测试开发实习生项目 - 自动化测试框架
##项目简介
基于python+Pytest + Requests +Playwright的全栈自动化测试框架，支持接口测试和UI测试，集成日志、HTML报告、CI/CD。
##技术栈
- Python 3.12+
- Pytest (测试框架)
- Request(接口测试)
- Playwright(UI 自动化)
- PyYAML(数据驱动)
- Pytest-html(测试报告)
- GitHub Actions(持续集成)
## 项目结构
├── config.py                # 配置文件
├── conftest.py              # 公共 fixture
├── utils/
│   ├── api_client.py        # 封装请求客户端
│   └── logger.py            # 日志模块
├── test_data/
│   └── test_data.yaml       # 测试数据
├── test_cases/
│   ├── api/
│   │   └── test_param.py    # 数据驱动测试
│   └── test_posts.py        # 接口测试用例
├── reports/                 # 测试报告
└── .github/workflows/       # CI/CD 配置

## 快速开始
# 安装依赖
pip install pytest requests pyyaml playwright pytest-html
playwright install chromium

# 运行测试
pytest test_cases/ -v

# 生成报告
pytest test_cases/ -v --html=reports/report.html --self-contained-html

## 作者
陆明 - 测试开发实习生求职中