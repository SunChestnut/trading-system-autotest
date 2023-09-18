"""
@Author SunYL
@Time 2023/9/18 21:17
"""

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from base.iframe_baidu_map_base import IframeBaiduMapBase
from base.object_map import ObjectMap


class IframeBaiduMapPage(IframeBaiduMapBase, ObjectMap):

    def switch_to_baidu_map_iframe(self, driver: WebDriver):
        """
        切换到百度地图的 iframe
        :param driver: 浏览器驱动
        :return:
        """
        iframe_xpath = self.baidu_map_iframe()
        return self.switch_into_iframe(driver, By.XPATH, iframe_xpath)

    def iframe_out(self, driver: WebDriver):
        """
        从百度地图 iframe 切回到原网站
        :param driver:
        :return:
        """
        return self.switch_from_iframe_to_content(driver)

    def input_search_box(self, driver: WebDriver, input_value):
        search_box_xpath = self.search_box()
        return self.element_fill_value(driver, By.XPATH, search_box_xpath, input_value)

    def get_baidu_map_search_button(self, driver: WebDriver):
        """
        获取百度地图搜索按钮
        :param driver: 浏览器驱动
        :return:
        """
        button_xpath = self.search_button()
        # return self.element_get(driver, By.XPATH, button_xpath)
        return self.element_click(driver,By.XPATH,button_xpath)