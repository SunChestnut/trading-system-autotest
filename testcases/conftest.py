"""
@Author SunYL
@Time 2023/9/20 15:35
"""
import pytest

from common.report_add_img import add_img_to_report
from config.driver_config import DriverConfig

driver = None


@pytest.fixture()
def chrome_driver():
    global driver
    driver = DriverConfig().driver_config()
    yield driver
    driver.quit()


# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     """
#     pytest_runtest_makereport(item,call) 是 pytest 内置的钩子函数，使用时函数名不能变更
#     🔗 https://docs.pytest.org/en/7.4.x/reference/reference.html#pytest.hookspec.pytest_runtest_makereport
#     :param item:
#     :param call:
#     :return:
#     """
#     # 获取钩子方法的调用结果
#     out = yield
#     # 从钩子方法的调用结果中获取测试报告
#     report = out.get_result()
#     report.description = str(item.function.__doc__)
#
#     # 共三个阶段，分别为 setup、call、teardown
#     if report.when == "call":
#         if report.failed:
#             add_img_to_report(driver, "失败截图", False)
