"""
@Time: 2023/9/11 19:25
@Author: syl
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager


class DriverConfig:
    def driver_config(self) -> webdriver:
        """
        浏览器驱动
        :return:
        """
        options = webdriver.ChromeOptions()
        options.add_argument("window-size=1920,1080")  # 设置窗口大小，设置为 1920*1080
        options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 去除 “chrome 正在受到自动测试软件的控制” 的提醒
        options.add_argument("--ignore-certificate-errors")  # 忽略网站的证书认证错误，解决 Selenium 无法访问 https 的问题
        options.add_argument("--allow-insecure-localhost")  # 忽略 localhost 上的 TLS/SSL 错误
        options.add_argument("--incognito")  # 设置为无痕模式
        # options.add_argument("--headless")  # 设置为无头模式，即不显示打开浏览器窗口，整个流程都在后台执行
        options.add_argument("--disable-gpu")  # 禁用 GPU 的页面加速，解决卡顿
        options.add_argument("--no-sandbox")  # 禁用沙箱，解决卡顿
        options.add_argument("--disable-dev-shm-usage")  # 解决卡顿

        driver = webdriver.Chrome(
            service=ChromeService(
                ChromeDriverManager(cache_manager=DriverCacheManager(root_dir=".", valid_range=365)).install()),
            options=options)  # 设置 webdriver_manager 所管理的浏览器驱动缓存有效期为 365 天

        # 删除所有cookies
        driver.delete_all_cookies()

        return driver
