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
