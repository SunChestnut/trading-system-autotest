"""
@Author SunYL
@Time 2023/9/20 15:35
"""
import pytest

from config.driver_config import DriverConfig


@pytest.fixture()
def chrome_driver():
    driver = DriverConfig().driver_config()
    yield driver
    driver.quit()
