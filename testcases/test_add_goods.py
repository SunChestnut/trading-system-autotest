"""
@Author SunYL
@Time 2023/9/18 12:32
"""
import time

from config.driver_config import DriverConfig
from page.goods_page import GoodsPage
from page.login_page import LoginPage
from page.left_menu_page import LeftMenuPage


class TestAddGoods:

    def test_add_goods_001(self):
        driver = DriverConfig().driver_config()
        driver.implicitly_wait(2)  # 设置隐式等待 2s

        # 登录
        LoginPage().login(driver, "zjl")

        # 点击左侧一级菜单栏中的「产品」
        LeftMenuPage().click_level_one_menu(driver, "产品")

        # 点击左侧一级菜单栏「产品」下的二级菜单「新增二手商品」
        LeftMenuPage().click_level_two_menu(driver, "新增二手商品")

        GoodsPage().add_new_goods(driver, "Apple Watch",
                                  "On your wrist, a little wonder\nApple Watch, your daily companion\nStay connected, wherever you go\nA world of possibilities, all in one flow",
                                  8, ["img-04.jpg", "img-05.jpg"], 5999,
                                  "上架", "提交")

        # 退出浏览器
        driver.quit()
