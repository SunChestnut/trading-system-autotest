"""
@Author SunYL
@Time 2023/9/13 11:55
"""


class LoginBase:

    def login_input(self, input_placeholder) -> str:
        """
        获取登录的用户名/密码的 HTML 标签
        :param input_placeholder:
        :return:
        """
        return "//input[@placeholder='" + input_placeholder + "']"

    def login_button(self, button_name):
        """
        登录按钮
        :param button_name:
        :return:
        """
        return "//span[text()='" + button_name + "']"
