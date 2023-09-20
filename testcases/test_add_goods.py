"""
@Author SunYL
@Time 2023/9/18 12:32
"""

from page.goods_page import GoodsPage
from page.left_menu_page import LeftMenuPage
from page.login_page import LoginPage


class TestAddGoods:

    def test_add_goods_001(self, chrome_driver):
        LoginPage().login(chrome_driver, "zjl")  # 登录

        LeftMenuPage().click_level_one_menu(chrome_driver, "产品")  # 点击左侧一级菜单栏中的「产品」
        LeftMenuPage().click_level_two_menu(chrome_driver, "新增二手商品")  # 点击左侧一级菜单栏「产品」下的二级菜单「新增二手商品」

        GoodsPage().add_new_goods(chrome_driver, "Apple Watch",
                                  "On your wrist, a little wonder\nApple Watch, your daily companion\nStay connected, wherever you go\nA world of possibilities, all in one flow",
                                  8, ["img-04.jpg", "img-05.jpg"], 5999,
                                  "上架", "提交")

    def test_add_goods_002(self, chrome_driver):
        LoginPage().login(chrome_driver, "zjl")  # 登录

        LeftMenuPage().click_level_one_menu(chrome_driver, "产品")  # 点击左侧一级菜单栏中的「产品」

        LeftMenuPage().click_level_two_menu(chrome_driver, "新增二手商品")  # 点击左侧一级菜单栏「产品」下的二级菜单「新增二手商品」

        GoodsPage().add_new_goods(chrome_driver, "《流畅的Python》",
                                  "共包括上下两册",
                                  8, ["fun-1.jpg", "fun-2.jpg"], 5999,
                                  "上架", "提交")
