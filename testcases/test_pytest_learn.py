"""
Pytest 学习部分

@Author SunYL
@Time 2023/9/19 14:58
"""
from time import sleep

import pytest

from config.driver_config import DriverConfig


class TestPytestLearn:

    @pytest.fixture(scope="class")
    def scope_class(self):
        """
        fixture scope 为 class 级别，在执行当前类时只执行一次
        :return:
        """
        print("class 级别的 fixture，只在执行 class 时执行一次")

    @pytest.fixture(scope="function")
    def driver(self):
        """
        fixture scope 为 function 级别，在当前类中的每个函数执行前都会执行一次
        :return:
        """
        print("🥝init driver 🥝")
        return DriverConfig().driver_config()

    @pytest.mark.bing
    def test_open_bing(self, driver, scope_class):
        driver.get("https://cn.bing.com/")
        sleep(2)
        driver.quit()

    @pytest.mark.baidu
    def test_open_baidu(self, driver, scope_class):
        driver.get("https://baidu.com/")
        sleep(2)
        driver.quit()

    # @pytest.mark.google
    # def test_open_google(self, driver, scope_class):
    #     driver.get("https://www.google.com/")
    #     sleep(2)
    #     driver.quit()
