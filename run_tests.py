"""一键运行所有测试报告"""
import os
import subprocess
from datetime import datetime
os.makedirs("reports", exist_ok=True)
# 生成带时间戳的报告名
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_path = f"reports/report_{timestamp}.html"

#运行测试
cmd =f"pytest test_cases/ -v --html={report_path} --self-contained-html"
result = subprocess.run(cmd, shell=True)
print(f"\n报告已生成:{report_path}")

