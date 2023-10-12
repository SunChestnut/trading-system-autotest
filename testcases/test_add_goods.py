"""
@Author SunYL
@Time 2023/9/18 12:32
"""
import allure
import pytest

from page import *

"""
通过 pytest 中的 parameterize 来向测试用例中传入多个参数
"""

goods_list = [
    {
        "goods_title": "好糟糕纸巾",
        "goods_details": "用了就能糟糕一整天的纸巾",
        "goods_num": 3,
        "goods_img_list": ["fun-2.jpg", "img-02.jpg"],
        "goods_price": 100,
        "goods_status": "上架",
        "bottom_button_name": "提交"
    },
    {
        "goods_title": "桃子极美炫光深紫巴洛克耳钉",
        "goods_details": "小众简约耳钉 14k 注金耳针",
        "goods_num": 30,
        "goods_img_list": ["img-05.jpg", "img-04.jpg"],
        "goods_price": 188,
        "goods_status": "上架",
        "bottom_button_name": "提交"
    }
]

flaw_goods_list = [
    {  # empty goods title
        "goods_title": "",
        "goods_details": "小众简约耳钉 14k 注金耳针",
        "goods_num": 2,
        "goods_img_list": ["img-05.jpg", "img-04.jpg"],
        "goods_price": 200,
        "goods_status": "上架",
        "bottom_button_name": "提交"
    }
]


@allure.epic("新增二手商品测试")
class TestAddGoods:

    @pytest.mark.parametrize("goods", goods_list)
    def test_add_goods_001(self, chrome_driver, goods):
        LoginPage().login(chrome_driver, "zjl")  # 登录

        LeftMenuPage().click_level_one_menu(chrome_driver, "产品")  # 点击左侧一级菜单栏中的「产品」
        LeftMenuPage().click_level_two_menu(chrome_driver, "新增二手商品")  # 点击左侧一级菜单栏「产品」下的二级菜单「新增二手商品」

        GoodsPage().add_new_goods_list(chrome_driver, goods)


def test_add_goods_002(self, chrome_driver):
    LoginPage().login(chrome_driver, "zjl")  # 登录

    LeftMenuPage().click_level_one_menu(chrome_driver, "产品")  # 点击左侧一级菜单栏中的「产品」
    LeftMenuPage().click_level_two_menu(chrome_driver, "新增二手商品")  # 点击左侧一级菜单栏「产品」下的二级菜单「新增二手商品」

    GoodsPage().add_new_goods(chrome_driver, "《流畅的Python》",
                              "共包括上下两册",
                              8, ["fun-1.jpg", "fun-2.jpg"], 5999,
                              "上架", "提交")


@pytest.mark.parametrize("flaw_goods", flaw_goods_list)
def test_add_goods_fail(self, chrome_driver, flaw_goods):
    LoginPage().login(chrome_driver, "zjl")

    LeftMenuPage().click_level_one_menu(chrome_driver, "产品")
    LeftMenuPage().click_level_two_menu(chrome_driver, "新增二手商品")

    GoodsPage().add_new_goods_list(chrome_driver, flaw_goods)
