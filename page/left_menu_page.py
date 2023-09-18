"""
左侧菜单栏中的相关操作

@Author SunYL
@Time 2023/9/18 11:01
"""

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from base.left_menu_base import LeftMenuBase
from base.object_map import ObjectMap


class LeftMenuPage(LeftMenuBase, ObjectMap):

    def click_level_one_menu(self, driver: WebDriver, menu_name):
        """
        点击左侧菜单栏中的一级菜单
        :param driver: 浏览器驱动
        :param menu_name: 菜单名称
        :return:
        """
        menu_xpath = self.level_one_menu(menu_name)  # 获取一级菜单栏的元素定位
        return self.element_click(driver, By.XPATH, menu_xpath)

    def click_level_two_menu(self, driver: WebDriver, menu_name):
        """
        点击左侧菜单栏中的二级菜单
        :param driver: 浏览器驱动
        :param menu_name: 菜单名称
        :return:
        """
        menu_xpath = self.level_two_menu(menu_name)
        return self.element_click(driver, By.XPATH, menu_xpath)
