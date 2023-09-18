"""
@Author SunYL
@Time 2023/9/18 10:23
"""

from config.driver_config import DriverConfig
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def test_implicit():
    driver = DriverConfig().driver_config()

    """
    隐式等待
    :param driver:
    :return:
    """
    driver.implicitly_wait(2)  # 2s
    driver.get("https://www.selenium.dev/selenium/web/dynamic.html")
    driver.find_element(By.ID, "adder").click()

    added = driver.find_element(By.ID, "box0")
    assert added.get_dom_attribute('class') == "redbox"
