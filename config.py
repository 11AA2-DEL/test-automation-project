"""项目配置文件：日志级别、路径管理"""
import os
from datetime import datetime
# 日志和报告路径（跟接口配置无关）
LOG_LEVEL = "INFO"
LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")
REPORT_DIR = os.path.join(os.path.dirname(__file__), "reports")


# 报告名称加时间戳
REPORT_NAME = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"