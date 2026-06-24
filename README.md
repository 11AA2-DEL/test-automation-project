# 全栈自动化测试框架

## 项目简介
基于 Python + Pytest + Requests + Playwright 搭建的全栈自动化测试框架，支持接口测试和 UI 自动化，采用分层架构，集成数据驱动、日志管理、HTML 测试报告、CI/CD。

## 技术栈
- **语言**: Python 3.12+
- **测试框架**: Pytest
- **接口测试**: Requests
- **UI 自动化**: Playwright
- **数据驱动**: PyYAML
- **测试报告**: pytest-html
- **持续集成**: GitHub Actions
- **日志**: logging

## 项目结构
├── config.py                # 配置文件（日志、路径）
├── config.yaml              # 多环境配置（接口地址、超时）
├── conftest.py              # 公共 fixture（api、browser、page）
├── run_tests.py             # 一键运行脚本
├── utils/
│   ├── api_client.py        # HTTP 请求客户端（支持 Token）
│   ├── logger.py            # 日志模块（控制台 + 文件）
│   └── config_loader.py     # YAML 配置加载器
├── pages/
│   └── search_page.py       # 必应首页 Page Object
├── test_data/
│   ├── test_data.yaml       # 测试数据（参数化）
│   └── search_page.html     # 本地 UI 测试页面
├── test_cases/
│   ├── test_posts.py        # 文章接口 CRUD 测试
│   ├── test_auth.py         # Token 认证测试
│   ├── test_boundary.py     # 边界值参数化测试
│   ├── api/test_param.py    # 数据驱动接口 + UI 测试
│   └── web/test_local_search.py  # 本地 UI 搜索测试
├── reports/                 # HTML 测试报告
├── logs/                    # 测试日志
└── .github/workflows/
    └── test.yml             # CI/CD 自动测试流水线

## 快速开始
# 安装依赖
pip install pytest requests pyyaml playwright pytest-html
playwright install chromium

# 运行全部测试
pytest test_cases/ -v

# 生成测试报告
pytest test_cases/ -v --html=reports/report.html --self-contained-html

# 一键运行
python run_tests.py

## CI/CD
每次 push 代码自动触发 GitHub Actions，运行全部测试并生成报告。

## 作者
[陆明] - 测试开发实习生求职中