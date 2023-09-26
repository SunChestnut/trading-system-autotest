"""
切换窗口测试

@Author SunYL
@Time 2023/9/18 17:23
"""

from time import sleep

import allure

from common.report_add_img import add_img_to_report
from page.external_link_page import ExternalLinkPage
from page.left_menu_page import LeftMenuPage
from page.login_page import LoginPage


@allure.epic("点击外链功能测试")
class TestWindowHandle:

    @allure.description("测试「点击外链」功能")
    def test_switch_window_handles(self, chrome_driver):
        """
        通过 allure 设置测试步骤
        ⚠️ 测试用例代码修改后，需重新生成测试报告，再启动 allure server
        :param chrome_driver:
        :return:
        """
        with allure.step("登录"):
            LoginPage().login(chrome_driver, "zjl")
            sleep(2)
            add_img_to_report(chrome_driver, "login")

        with allure.step("点击外链"):
            LeftMenuPage().click_level_one_menu(chrome_driver, "外链")
            sleep(2)
            add_img_to_report(chrome_driver, "click-external-link")

        with allure.step("断言 title"):
            page_title = ExternalLinkPage().goto_external_page(chrome_driver)
            assert page_title == "慕课网-程序员的梦工厂"
            sleep(2)
