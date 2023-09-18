"""
订单页面相关操作
@Author SunYL
@Time 2023/9/18 19:34
"""

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from base.object_map import ObjectMap
from base.order_base import OrderBase


class OrderPage(OrderBase, ObjectMap):

    def click_order_tab(self, driver: WebDriver, tab_name):
        """
        点击订单 tab 栏按钮
        :param driver:  浏览器驱动
        :param tab_name: tab 栏按钮（全部/待付款/待发货/运输中/待确认/待评价）
        :return:
        """
        tab_name_xpath = self.order_tab(tab_name)
        return self.element_click(driver, By.XPATH, tab_name_xpath)
