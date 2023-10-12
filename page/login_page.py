"""
@Author SunYL
@Time 2023/9/13 22:13
"""
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from base.login_base import LoginBase
from base.object_map import ObjectMap
from common.ocr_identify import OcrIdentify
from common.report_add_img import add_img_path_to_report
from common.yaml_config import GetConf
from logs.log import autotest_log


class LoginPage(LoginBase, ObjectMap):

    def login_input_value(self, driver: WebDriver, input_placeholder, input_value):
        """
        获取页面用户名，设置用户名
        :param driver:
        :param input_placeholder:
        :param input_value:
        :return:
        """
        autotest_log.info("input:" + input_placeholder + " value:" + str(input_value))
        input_xpath = self.login_input(input_placeholder)
        return self.element_fill_value(driver, By.XPATH, input_xpath, input_value)

    def click_login(self, driver: WebDriver, button_name):
        """
        点击登录
        :param driver:
        :param button_name:
        :return:
        """
        autotest_log.info("click login")
        login_button = self.login_button(button_name)
        return self.element_click(driver, By.XPATH, login_button)

    def login(self, driver: WebDriver, user_info, need_captcha=False):
        """
        登录
        :param driver: 浏览器驱动
        :param user_info: 配置文件中设置的用户信息
        :param need_captcha: 是否需要打开验证码
        :return:
        """
        autotest_log.info("跳转登录页")
        self.element_to_url(driver, "/login")
        username, password = GetConf().get_username_password(user_info=user_info)
        self.login_input_value(driver, "用户名", username)
        self.login_input_value(driver, "密码", password)
        if need_captcha:
            time.sleep(3)
            autotest_log.info("需要验证码")
            self.select_need_captcha(driver)  # 点击勾选「是否需要验证码」选项
            captcha_img_xpath = self.captcha()  # 获取验证码图片定位
            captcha_screenshot_path = self.element_screenshot(driver, By.XPATH, captcha_img_xpath)  # 验证截图后存放的路径
            add_img_path_to_report(captcha_screenshot_path, "登录图像验证码")
            captcha_res = OcrIdentify().identify(captcha_screenshot_path)  # 图像验证码识别结果
            autotest_log.info("图像验证码为 " + str(captcha_res))
            input_captcha_xpath = self.input_captcha()
            self.element_fill_value(driver, By.XPATH, input_captcha_xpath, captcha_res)
            time.sleep(3)
        self.click_login(driver, "登录")
        self.assert_login_assert(driver)

    def login_assert(self, driver: WebDriver, img_name: str):
        """
        登录后判断头像是否正确
        :param driver: 浏览器驱动
        :param img_name: 头像名
        :return:
        """
        return self.find_img_in_source(driver, img_name)

    def assert_login_assert(self, driver: WebDriver):
        """
        验证是否登录成功
        :param driver: 浏览器驱动
        :return:
        """
        success_xpath = self.login_success()
        self.element_appear(driver, By.XPATH, success_xpath, 2)

    def select_need_captcha(self, driver: WebDriver):
        """
        点击勾选是否需要验证码
        :param driver:
        :return:
        """
        autotest_log.info("点击勾选是否需要验证码")
        need_captcha_xpath = self.need_captcha()
        return self.element_click(driver, By.XPATH, need_captcha_xpath)
