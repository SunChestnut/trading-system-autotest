"""
@Author SunYL
@Time 2023/9/18 19:46
"""

from time import sleep

import allure

from page import LoginPage
from page import LeftMenuPage
from page import OrderPage


@allure.epic("我的订单页测试")
class TestOrder:

    def test_order_tab(self, chrome_driver):
        LoginPage().login(chrome_driver, "zjl")
        sleep(1)
        LeftMenuPage().click_level_one_menu(chrome_driver, "我的订单")
        sleep(1)
        LeftMenuPage().click_level_two_menu(chrome_driver, "已买到的宝贝")
        sleep(1)
        tab_names = ["全部", "待付款", "待发货", "运输中", "待确认", "待评价"]
        for t in tab_names:
            OrderPage().click_order_tab(chrome_driver, t)
            sleep(1)
