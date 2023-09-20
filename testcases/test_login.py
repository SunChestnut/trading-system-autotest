"""
@Time: 2023/9/11 19:27
@Author: syl
"""

from time import sleep

import pytest

from config.driver_config import DriverConfig
from page.login_page import LoginPage


class TestLogin:
    @pytest.fixture(scope="class")
    def chrome_driver(self):
        driver = DriverConfig().driver_config()
        yield driver
        driver.quit()

    def test_login(self, chrome_driver):
        # driver = DriverConfig().driver_config()  # DriverConfig 用于启动浏览器
        LoginPage().login(chrome_driver, "zjl")
        sleep(1)
        # chrome_driver.quit()
