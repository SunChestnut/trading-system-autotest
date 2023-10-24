"""
@Author SunYL
@Time 2023/9/18 22:26
"""

from time import sleep

import allure

from common.mysql_operate import MySqlOperate
from page import HomePage
from page import LoginPage


@allure.epic("首页功能测试")
class TestHomePage:

    def test_open_personal_profile_and_logout(self, chrome_driver):
        LoginPage().login(chrome_driver, "zjl")
        sleep(1)

        HomePage().open_personal_profile(chrome_driver)
        sleep(1)

        HomePage().logout(chrome_driver)
        sleep(1)

    def test_login_avatar(self, chrome_driver):
        """登录后对首页截图，并判断截图中的头像是否正确"""
        LoginPage().login(chrome_driver, "zjl")
        sleep(3)
        # 若返回的信心值 > 0.9，表明头像正确
        assert LoginPage().login_assert(chrome_driver, "avatar-screenshot.png") > 0.9

    def test_user_balance(self, chrome_driver):
        with allure.step("login"):
            LoginPage().login(chrome_driver, "zjl")
            sleep(3)
        with allure.step("get balance from home page"):
            user_balance = HomePage().get_user_balance(chrome_driver)

        with allure.step("get balance from database"):
            sql_query = MySqlOperate().query(
                "select balance from wallet where user_id = (select id from user WHERE user = '周杰伦');")

        with allure.step("determine equal"):
            assert user_balance == str(sql_query[0][0])
