"""
定位左侧菜单栏中的【产品->新增二手商品】页面中的相关元素

@Author SunYL
@Time 2023/9/18 11:11
"""


class GoodsBase:
    def goods_title(self):
        """
        商品标题
        :return:
        """
        return "//form[@class='el-form']//textarea[@placeholder='请输入商品标题']"

    def goods_details(self):
        """
        商品详情
        :return:
        """
        return "//form[@class='el-form']//textarea[@placeholder='请输入商品详情']"

    def goods_number(self, plus: bool):
        """
        设置商品数量，共两种方式，plus==True 时通过 +/- 号设置，否则直接在输入框内填入数值
        :param plus: True -> 通过 +/- 号设置商品数量；False -> 通过输入框设置商品数量
        :return:
        """
        if plus:
            return "//label[@for='product_stock']/following-sibling::div//i[@class='el-icon-plus']/parent::span"
        else:
            return "//label[@for='product_stock']/following-sibling::div//input[@placeholder='商品数量'] "

    def goods_img(self):
        """
        商品图片
        :return:
        """
        return "//input[@type='file']"

    def goods_price(self):
        """
        商品单价
        :return:
        """
        return "//form[@class='el-form']//input[@placeholder='请输入商品单价']"

    def goods_status(self):
        """
        商品状态
        :return:
        """
        return "//form[@class='el-form']//input[@placeholder='请选择商品状态']"

    def goods_status_select(self, select_name):
        """
        选择商品状态
        :param select_name: 上架/下架
        :return:
        """
        return "//span[text()='" + select_name + "']/parent::li"

    def add_goods_bottom_button(self, button_name: str):
        """
        新增二手商品页面底部的按钮
        :param button_name: 提交/重置
        :return:
        """
        return "//span[text()='" + button_name + "']/parent::button "
