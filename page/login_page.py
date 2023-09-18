"""
@Author SunYL
@Time 2023/9/13 22:13
"""

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from base.login_base import LoginBase
from base.object_map import ObjectMap
from common.yaml_config import GetConf


class LoginPage(LoginBase, ObjectMap):

    def login_input_value(self, driver: WebDriver, input_placeholder, input_value):
        """
        获取页面用户名，设置用户名
        :param driver:
        :param input_placeholder:
        :param input_value:
        :return:
        """
        input_xpath = self.login_input(input_placeholder)
        # return driver.find_element(By.XPATH, input_xpath).send_keys(input_value)
        return self.element_fill_value(driver, By.XPATH, input_xpath, input_value)

    def click_login(self, driver: WebDriver, button_name):
        """
        点击登录
        :param driver:
        :param button_name:
        :return:
        """
        login_button = self.login_button(button_name)
        # return driver.find_element(By.XPATH, login_button).click()
        return self.element_click(driver, By.XPATH, login_button)

    def login(self, driver: WebDriver, user_info):
        """
        登录
        :param driver: 浏览器驱动
        :param user_info: 配置文件中设置的用户信息
        :return:
        """
        self.element_to_url(driver, "/login")  # 跳转到首页
        username, password = GetConf().get_username_password(user_info=user_info)
        self.login_input_value(driver, "用户名", username)
        self.login_input_value(driver, "密码", password)
        self.click_login(driver, "登录")
