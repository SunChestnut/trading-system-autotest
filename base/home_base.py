"""
@Author SunYL
@Time 2023/9/14 16:06
"""


class HomeBase:
    def wallet_switch(self):
        """
        返回表示首页的钱包开关的元素定位
        :return:
        """
        return "//span[contains(@class,'switch')]"

    def logo(self):
        """
        返回表示首页左上角 logo 的元素定位
        :return:
        """
        # //div[contains(@class,'logo-text')]
        return "//div[contains(text(),'二手')]"

    def welcome(self):
        """
        返回表示首页中的「欢迎您回来」语句的元素定位
        :return:
        """
        return "//span[starts-with(text(),'欢迎您回来')]"

    def show_calendar(self):
        """
        返回表示首页中的日历的元素定位
        following-sibling: 定位同级元素的下一个元素
        :return:
        """
        return "//div[text()='我的日历']/following-sibling::div"

    def home_user_avatar(self):
        """
        返回表示首页用户头像大图的元素定位（方式一）
        preceding-sibling: 定位同级元素的上一个元素
        :return:
        """
        return "//span[contains(text(),'欢迎您回来')]/parent::div/preceding-sibling::div//img"

    def home_user_avatar_2(self):
        """
        返回表示首页用户头像大图的元素定位（方式二）
        ancestor: 获取祖先元素
        :return:
        """
        return "//span[text()='我的地址']/ancestor::div[@class='first_card']/div[contains(@class,'avatar')]//img"

    def right_top_avatar(self):
        """
        返回表示首页右上角头像的元素定位
        :return:
        """
        return "//div[@class='el-row']"

    def logout_button(self):
        """
        右上角头像 -> 退出登录 tab
        :return:
        """
        return "//li[text()='退出登录']"

    def personal_profile(self):
        """
        右上角头像 -> 个人资料
        :return:
        """
        return "//li[text()='个人资料']"
