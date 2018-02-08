# coding:utf-8
import unittest
import time
import HTMLTestRunnerCN

# 定义测试用例的目录为当前目录
test_dir = 'C:\\Users\\admin\\PycharmProjects\\UITest\\EUV\\BS'
report_dir = 'C:\\Users\\admin\\PycharmProjects\\UITest\\EUV\\BS\\report'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')


now = time.strftime("%Y-%m-%d %H_%M_%S")
filePath = report_dir + '/' + now + 'result.html'
fp = open(filePath, 'wb')
runner = HTMLTestRunnerCN.HTMLTestRunner(
    stream=fp,
    title=u"易优维自动化测试报告",
    description=u"用例执行情况：",
    tester=u"许臻"
)
runner.run(discover)
fp.close()