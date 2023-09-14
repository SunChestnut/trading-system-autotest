"""
@Author SunYL
@Time 2023/9/14 16:06
"""


class HomeBase:
    def wallet_switch(self):
        """
        首页的钱包开关
        :return:
        """
        return "//span[contains(@class,'switch')]"

    def logo(self):
        """
        首页左上角 logo
        :return:
        """
        # //div[contains(@class,'logo-text')]
        return "//div[contains(text(),'二手')]"

    def welcome(self):
        """
        首页中的「欢迎您回来」语句
        :return:
        """
        return "//span[starts-with(text(),'欢迎您回来')]"
