"""
@Author SunYL
@Time 2023/9/18 19:56
"""

from time import sleep

from config.driver_config import DriverConfig
from page.account_page import AccountPage
from page.left_menu_page import LeftMenuPage
from page.login_page import LoginPage


class TestAccount:

    def test_update_account(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, "zjl")
        sleep(1)

        LeftMenuPage().click_level_one_menu(driver, "账户设置")
        LeftMenuPage().click_level_two_menu(driver, "个人资料")
        sleep(1)

        # 测试个人头像上传
        AccountPage().upload_avatar(driver, "avatar-01.jpeg")
        sleep(3)

        AccountPage().click_save(driver)
        sleep(2)

        driver.quit()
