import unittest
from HTMLTestRunner import HTMLTestRunner
import time
# from Interface.test.test_data import DataTest
from testsuits.test1_login_case import LoginTest
from framework.commom.send_email import Report
from framework.logger import Logger
logger=Logger(__name__).getlog()

# report_dir = './test_report'

##构建测试集
test_dir = './testsuits'
suite = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")


#构建测试集
# suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
# logger.info('构建测试集')
# 定义报告生成路径
report_path = '.' + '/report/test_report/'
# 格式化时间
now_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(time.time()))
# 测试报告生成格式
HtmlFile = report_path + now_time + "result.html"


if __name__ == '__main__':

    ####################生成报告#################
    # 生成测试报告
    with open(HtmlFile, 'wb+') as f:
        HTMLTestRunner(
            stream=f, title="XX项目测试报告", description="用例执行情况").run(suite)
    logger.info('生成测试报告')

    ####################发邮件#################
    # 测试报告目录
    new_path = report_path
    # 查找最新的测试报告文件
    rp=Report()
    new_report = rp.get_new_file(new_path)
    # 发送测试报告，带附件
    rp.send_mail_attr(new_report)
