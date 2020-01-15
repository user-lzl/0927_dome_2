import unittest
import HTMLTestRunnerPlugins
import time
import os

# 初始化当前路径
current_dir = os.path.dirname(os.path.realpath(__file__))
# 添加测试用例路径
case_dir = os.path.join(current_dir,"script")
# 添加测试报告存放路径
report_dir = os.path.join(current_dir,"report")
# 将测试用例添加到测试套件中
discover = unittest.defaultTestLoader.discover(case_dir,pattern="test*.py")

# 命名测试报告名称
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_file_name = report_dir + '\\' + now + "report.html"
with open(report_file_name,"wb") as fp:
    runner = HTMLTestRunnerPlugins.HTMLTestRunner(title="自动化测试报告",
                                                  description="自动化测试报告描述",
                                                  stream=fp)
    runner.run(discover)