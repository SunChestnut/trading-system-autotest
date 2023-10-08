"""
@Time: 2023/9/11 19:27
@Author: syl
"""

from time import sleep

import allure

from page.login_page import LoginPage


@allure.epic("登录测试")
class TestLogin:
    def test_login(self, chrome_driver):
        LoginPage().login(chrome_driver, "zjl")
        sleep(1)

    def test_login_avatar(self, chrome_driver):
        """
        登录后对首页截图，并判断截图中的头像是否正确
        :param chrome_driver:
        :return:
        """
        LoginPage().login(chrome_driver, "zjl")
        sleep(3)
        # 若返回的信心值 > 0.9，表明头像正确
        assert LoginPage().login_assert(chrome_driver, "avatar-screenshot.png") > 0.9
