"""
@Author SunYL
@Time 2023/9/18 19:54
"""

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from base.account_base import AccountBase
from base.object_map import ObjectMap
from common.tools import get_img_path


class AccountPage(AccountBase, ObjectMap):

    def upload_avatar(self, driver: WebDriver, img_name):
        """
        上传个人头像
        :param driver: 浏览器驱动
        :param img_name: 图片名称
        :return:
        """
        img_path = get_img_path(img_name)
        profile_xpath = self.basic_info_avatar_input()
        self.upload(driver, By.XPATH, profile_xpath, img_path)

    def click_save(self, driver: WebDriver):
        """
        保存个人信息
        :param driver: 浏览器驱动
        :return:
        """
        save_button_xpath = self.basic_info_save_button()
        return self.element_click(driver, By.XPATH, save_button_xpath)
