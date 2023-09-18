"""
账号相关操作

@Author SunYL
@Time 2023/9/18 19:51
"""


class AccountBase:

    def basic_info_avatar_input(self):
        """
        基本资料——个人头像
        :return:
        """
        return "//div[@class='avatar-uploader']//input[@type='file']"

    def basic_info_save_button(self):
        """
        基本资料——保存按钮
        :return:
        """
        return "//span[text()='保存']/parent::button"
