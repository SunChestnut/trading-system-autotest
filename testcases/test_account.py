"""
@Author SunYL
@Time 2023/9/18 19:56
"""

from time import sleep

from page.account_page import AccountPage
from page.left_menu_page import LeftMenuPage
from page.login_page import LoginPage


class TestAccount:

    def test_update_account(self, chrome_driver):
        LoginPage().login(chrome_driver, "zjl")
        sleep(1)

        LeftMenuPage().click_level_one_menu(chrome_driver, "账户设置")
        LeftMenuPage().click_level_two_menu(chrome_driver, "个人资料")
        sleep(2)

        # 测试个人头像上传
        AccountPage().upload_avatar(chrome_driver, "fun-1.jpg")
        sleep(3)

        AccountPage().click_save(chrome_driver)
        sleep(2)
