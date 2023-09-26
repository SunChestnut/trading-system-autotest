"""
@Author SunYL
@Time 2023/9/18 19:56
"""
import allure

from common.report_add_img import add_img_to_report
from page.account_page import AccountPage
from page.left_menu_page import LeftMenuPage
from page.login_page import LoginPage


@allure.epic("用户账户测试")
class TestAccount:

    # @allure.description("Description Level")
    # @allure.epic("Epic Level")
    # @allure.feature("Feature Level")
    # @allure.story("Story Level")
    # @allure.tag("用户账户标签")
    def test_update_account(self, chrome_driver):
        LoginPage().login(chrome_driver, "zjl")
        # sleep(1)
        add_img_to_report(chrome_driver, "login")

        LeftMenuPage().click_level_one_menu(chrome_driver, "账户设置")
        LeftMenuPage().click_level_two_menu(chrome_driver, "个人资料")
        # sleep(2)
        add_img_to_report(chrome_driver, "person-profile")

        # 测试个人头像上传
        AccountPage().upload_avatar(chrome_driver, "fun-1.jpg")
        # sleep(3)

        AccountPage().click_save(chrome_driver)
        # sleep(2)
