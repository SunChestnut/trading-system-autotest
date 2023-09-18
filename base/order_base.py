"""
订单相关的基础操作

@Author SunYL
@Time 2023/9/18 17:40
"""


class OrderBase:
    def order_tab(self, tab_name):
        """
        「我的订单」->「已买到的宝贝」页面中的 tab 按钮
        :param tab_name: 全部/待付款/待发货/运输中/待确认/待评价
        :return:
        """
        # this work too? "//div[@class='top_label']//div[text()='待付款']"
        return "//div[@role='tab' and text() = '" + tab_name + "']"
