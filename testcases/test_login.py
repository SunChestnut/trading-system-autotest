"""
@Time: 2023/9/11 19:27
@Author: syl
"""

from time import sleep

from config.driver_config import DriverConfig

from page.login_page import LoginPage


class TestLogin:

    def test_login(self):
        driver = DriverConfig().driver_config()  # DriverConfig 用于启动浏览器
        LoginPage().login(driver, "zjl")
        sleep(5)

        driver.quit()


if __name__ == '__main__':
    TestLogin().test_login()

# driver.get("http://192.168.56.20")
# sleep(3)

# 设置用户名密码
# driver.find_element(By.XPATH, "//input[@placeholder='用户名']").send_keys("周杰伦")
# driver.find_element(By.XPATH, "//input[@placeholder='密码']").send_keys("1234abcd!")
# driver.find_element(By.XPATH, "//span[text()='登录']/parent::button").click()

# LoginPage().login_input_value(driver, "用户名", "周杰伦")
# LoginPage().login_input_value(driver, "密码", "1234abcd!")
# LoginPage().click_login(driver, "登录")
