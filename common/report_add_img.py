"""
在 allure 生成的测试报告中增加测试过程/结果图片

@Author SunYL
@Time 2023/9/26 15:22
"""
from time import sleep

import allure
from selenium.webdriver.chrome.webdriver import WebDriver


def add_img_to_report(driver: WebDriver, step_name, need_sleep=True):
    """
    在测试过程中截图并将其插入 allure 测试报告中
    :param driver: 浏览器驱动
    :param step_name: 测试步骤名称
    :param need_sleep: 是否需要休眠
    :return:
    """
    if need_sleep:
        sleep(2)

    allure.attach(driver.get_screenshot_as_png(), step_name + ".png", allure.attachment_type.PNG)


def add_img_path_to_report(img_path, step_name):
    """
    将图片以附件的形式插入 allure 测试报告中
    :param img_path:
    :param step_name:
    :return:
    """
    allure.attach.file(img_path, step_name, allure.attachment_type.PNG)
