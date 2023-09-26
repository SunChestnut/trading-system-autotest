"""
@Author SunYL
@Time 2023/9/18 22:26
"""

from time import sleep

import allure

from page.home_page import HomePage
from page.login_page import LoginPage


@allure.epic("首页功能测试")
class TestHomePage:

    def test_open_personal_profile_and_logout(self, chrome_driver):
        LoginPage().login(chrome_driver, "zjl")
        sleep(1)

        HomePage().open_personal_profile(chrome_driver)
        sleep(1)

        HomePage().logout(chrome_driver)
        sleep(1)
