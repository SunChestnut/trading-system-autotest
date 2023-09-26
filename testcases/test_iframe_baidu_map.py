"""
@Author SunYL
@Time 2023/9/18 21:24
"""

from time import sleep

import allure

from page.iframe_baidu_map_page import IframeBaiduMapPage
from page.left_menu_page import LeftMenuPage
from page.login_page import LoginPage


@allure.epic("iframe 测试")
class TestIframeBaiduMap:

    def test_baidu_map_search_button(self, chrome_driver):
        LoginPage().login(chrome_driver, "zjl")
        sleep(1)

        LeftMenuPage().click_level_one_menu(chrome_driver, "iframe测试")
        sleep(1)

        IframeBaiduMapPage().switch_to_baidu_map_iframe(chrome_driver)
        IframeBaiduMapPage().input_search_box(chrome_driver, "北京")
        IframeBaiduMapPage().get_baidu_map_search_button(chrome_driver)
        sleep(3)
        IframeBaiduMapPage().iframe_out(chrome_driver)

        LeftMenuPage().click_level_one_menu(chrome_driver, "首页")
        sleep(1)
