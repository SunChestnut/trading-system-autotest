"""
@Author SunYL
@Time 2023/9/19 10:13
"""

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from base.home_base import HomeBase
from base.object_map import ObjectMap


class HomePage(HomeBase, ObjectMap):
    def open_personal_profile(self, driver: WebDriver):
        """
        点击/将鼠标悬浮到 右上角头像 -> 个人资料
        :param driver: 浏览器驱动
        :return:
        """
        avatar_xpath = self.right_top_avatar()
        self.mouse_hover_to_element(driver, By.XPATH, avatar_xpath)

        personal_profile_xpath = self.personal_profile()
        return self.element_click(driver, By.XPATH, personal_profile_xpath)

    def logout(self, driver: WebDriver):
        """
        点击/将鼠标悬浮到 右上角头像 -> 退出登录
        :param driver:
        :return:
        """
        avatar_xpath = self.right_top_avatar()
        self.mouse_hover_to_element(driver, By.XPATH, avatar_xpath)

        logout_xpath = self.logout_button()
        return self.element_click(driver, By.XPATH, logout_xpath)

    def get_user_balance(self, driver: WebDriver):
        """
        获取账户余额
        :param driver:
        :return:
        """
        balance_xpath = self.user_balance()
        return self.element_get(driver, By.XPATH, balance_xpath).text
