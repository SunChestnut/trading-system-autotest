"""
侧边栏

@Author SunYL
@Time 2023/9/14 17:42
"""


class LeftMenuBase:

    def level_one_menu(self, menu_name: str):
        """
        一级菜单栏
        :param menu_name:
        :return:
        """
        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']/ancestor::li"

    def level_two_menu(self, menu_name):
        """
        二级菜单栏
        :param menu_name:
        :return:
        """
        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']/parent::li"
