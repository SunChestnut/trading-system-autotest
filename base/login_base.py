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

    def login_success(self):
        """
        登录成功后的提示框
        :return:
        """
        return "//p[text()='登录成功']"

    def need_captcha(self):
        """
        登录页面的是否需要验证码的单选框
        :return:
        """
        return "//span[contains(text(),'是否需要验证码')]/preceding-sibling::span/span"

    def captcha(self):
        """
        验证码图片
        :return:
        """
        return "//div[@class='kaptcha']/div[@class='el-image']"

    def input_captcha(self):
        """
        输入验证码的输入框
        :return:
        """
        return "//input[@placeholder='请输入验证码']"
