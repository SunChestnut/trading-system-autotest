"""
page 层：
* 元素对应的操作

@Time: 2023/9/12 15:08
@Author: syl
"""

from .account_page import AccountPage
from .external_link_page import ExternalLinkPage
from .goods_page import GoodsPage
from .home_page import HomePage
from .iframe_baidu_map_page import IframeBaiduMapPage
from .left_menu_page import LeftMenuPage
from .login_page import LoginPage
from .order_page import OrderPage

__all__ = ['AccountPage', 'ExternalLinkPage', 'GoodsPage', 'HomePage', 'IframeBaiduMapPage',
           'LeftMenuPage', 'LoginPage', 'OrderPage']
