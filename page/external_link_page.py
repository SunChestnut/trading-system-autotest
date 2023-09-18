"""
跳转到外链页面

@Author SunYL
@Time 2023/9/18 17:18
"""

from selenium.webdriver.chrome.webdriver import WebDriver

from base.object_map import ObjectMap


class ExternalLinkPage(ObjectMap):
    def goto_external_page(self, driver: WebDriver):
        """
        切换窗口为最新打开的页面
        :param driver: 浏览器驱动
        :return: 当前页面的标题
        """
        self.switch_window_to_latest_handle(driver)
        return driver.title
