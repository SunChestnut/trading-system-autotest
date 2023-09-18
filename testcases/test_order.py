"""
@Author SunYL
@Time 2023/9/18 19:46
"""

from time import sleep

from config.driver_config import DriverConfig
from page.login_page import LoginPage
from page.left_menu_page import LeftMenuPage
from page.order_page import OrderPage


class TestOrder:

    def test_order_tab(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, "zjl")
        sleep(1)
        LeftMenuPage().click_level_one_menu(driver, "我的订单")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "已买到的宝贝")
        sleep(1)
        tab_names = ["全部", "待付款", "待发货", "运输中", "待确认", "待评价"]
        for t in tab_names:
            OrderPage().click_order_tab(driver, t)
            sleep(1)

        driver.quit()
