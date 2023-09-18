"""
@Author SunYL
@Time 2023/9/18 21:24
"""

from time import sleep

from config.driver_config import DriverConfig
from page.iframe_baidu_map_page import IframeBaiduMapPage
from page.left_menu_page import LeftMenuPage
from page.login_page import LoginPage


class TestIframeBaiduMap:

    def test_baidu_map_search_button(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, "zjl")
        sleep(1)

        LeftMenuPage().click_level_one_menu(driver, "iframe测试")
        sleep(1)

        IframeBaiduMapPage().switch_to_baidu_map_iframe(driver)
        IframeBaiduMapPage().input_search_box(driver, "北京")
        IframeBaiduMapPage().get_baidu_map_search_button(driver)
        sleep(3)
        IframeBaiduMapPage().iframe_out(driver)

        LeftMenuPage().click_level_one_menu(driver, "首页")
        sleep(1)

        driver.quit()
