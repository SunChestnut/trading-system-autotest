"""
@Author SunYL
@Time 2023/9/18 21:14
"""


class IframeBaiduMapBase:

    def baidu_map_iframe(self):
        """
        定位 iframe
        :return:
        """
        return "//iframe[@src='https://map.baidu.com/']"

    def search_box(self):
        return "//div[@id='searchbox']//input[@placeholder='搜地点、查公交、找路线']"

    def search_button(self):
        """
        Iframe 内嵌的百度地图中的搜索按钮
        :return:
        """
        return "//button[@id='search-button']"
