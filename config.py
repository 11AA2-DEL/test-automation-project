import os

# 日志和报告路径（跟接口配置无关）
LOG_LEVEL = "INFO"
LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")
REPORT_DIR = os.path.join(os.path.dirname(__file__), "reports")