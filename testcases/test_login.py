"""
@Time: 2023/9/11 19:27
@Author: syl
"""

from time import sleep

import allure
import pytest

from common.report_add_img import add_img_to_report
from page.login_page import LoginPage


@allure.epic("登录测试")
class TestLogin:

    @pytest.mark.login
    @allure.feature("登录")
    @allure.description("登录成功")
    def test_login(self, chrome_driver):
        """登录成功"""
        LoginPage().login(chrome_driver, "zjl")
        sleep(1)

    @pytest.mark.login
    @allure.feature("登录失败")
    @allure.description("登录失败测试")
    def test_login_fail(self, chrome_driver):
        """使用错误的账号登录"""
        with allure.step("登录"):
            LoginPage().login(chrome_driver, "notExistUser")
            sleep(3)
            add_img_to_report(chrome_driver, "登录")

    @pytest.mark.login
    @allure.feature("验证码登录")
    @allure.description("登录时使用验证码校验")
    def test_login_with_captcha(self, chrome_driver):
        """登录时候增加验证码校验"""
        with allure.step("登录"):
            LoginPage().login(chrome_driver, "zjl", True)
            sleep(3)
            add_img_to_report(chrome_driver, "登录")

    @pytest.mark.login
    @allure.feature("API 登录")
    @allure.description("调用 API 登录")
    def test_login_with_api(self, chrome_driver):
        with allure.step("周杰伦登录"):
            LoginPage().api_login(chrome_driver, "zjl")
            sleep(5)

        with allure.step("syl 登录"):
            LoginPage().api_login(chrome_driver, "syl")
            sleep(5)
