"""
切换窗口测试

@Author SunYL
@Time 2023/9/18 17:23
"""

from time import sleep

from config.driver_config import DriverConfig
from page.login_page import LoginPage
from page.left_menu_page import LeftMenuPage
from page.external_link_page import ExternalLinkPage


class TestWindowHandle:
    def test_switch_window_handles(self):
        driver = DriverConfig().driver_config()

        LoginPage().login(driver, "zjl")
        sleep(2)

        LeftMenuPage().click_level_one_menu(driver, "外链")
        sleep(2)

        page_title = ExternalLinkPage().goto_external_page(driver)
        print("Page title: ", page_title)
        sleep(2)

        driver.quit()
