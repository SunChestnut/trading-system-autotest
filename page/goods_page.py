"""
新增二手商品页面相关的操作

@Author SunYL
@Time 2023/9/18 12:25
"""
import time
from datetime import datetime

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from base.goods_base import GoodsBase
from base.object_map import ObjectMap
from common.tools import get_img_path


class GoodsPage(GoodsBase, ObjectMap):

    def input_goods_title(self, driver: WebDriver, input_value):
        """
        定位商品标题元素，并填值
        :param driver: 浏览器驱动
        :param input_value: 商品标题
        :return:
        """
        goods_title_xpath = self.goods_title()  # 定位商品标题
        return self.element_fill_value(driver, By.XPATH, goods_title_xpath, input_value)  # 填值

    def input_goods_details(self, driver: WebDriver, input_value):
        """
        定位商品详情元素，并填值
        :param driver:  浏览器驱动
        :param input_value:  商品详情
        :return:
        """
        goods_details_xpath = self.goods_details()
        return self.element_fill_value(driver, By.XPATH, goods_details_xpath, input_value)

    def select_goods_number(self, driver: WebDriver, num):
        """
        通过点击 ➕号方式，设置商品数量
        :param driver: 浏览器驱动
        :param num: 商品数量，即➕号点击次数
        :return:
        """
        goods_number_add_xpath = self.goods_number(plus=True)
        for i in range(num):
            self.element_click(driver, By.XPATH, goods_number_add_xpath)
            time.sleep(0.5)  # 防止点击过快导致失败

    def upload_goods_image(self, driver: WebDriver, img_name):
        """
        定位商品图片元素，并上传图片
        :param driver: 浏览器驱动
        :param img_name: 图片名称
        :return:
        """
        img_path = get_img_path(img_name)
        goods_image_xpath = self.goods_img()
        return self.upload(driver, By.XPATH, goods_image_xpath, img_path)

    def upload_mutil_goods_images(self, driver: WebDriver, img_name_list: list):
        """
        定位商品图片元素，并上传多个图片
        :param driver:  浏览器驱动
        :param img_name_list: 图片名称集合
        :return:
        """
        goods_image_xpath = self.goods_img()
        for i in range(len(img_name_list)):
            img_path = get_img_path(img_name_list[i])
            self.upload(driver, By.XPATH, goods_image_xpath, img_path)
            print("upload image current time:" + datetime.now().strftime("%H:%M:%S"))

    def input_goods_price(self, driver: WebDriver, input_value):
        """
        定位商品单价元素，并填值
        :param driver:
        :param input_value:
        :return:
        """
        goods_price_xpath = self.goods_price()
        return self.element_fill_value(driver, By.XPATH, goods_price_xpath, input_value)

    def select_goods_status(self, driver: WebDriver, select_name):
        """
        定位商品状态元素，并为其选择商品状态
        :param driver: 浏览器驱动
        :param select_name: 商品状态：上架/下架
        :return:
        """
        goods_status_xpath = self.goods_status()
        self.element_click(driver, By.XPATH, goods_status_xpath)
        time.sleep(1)  # 为选择框的弹出留出时间
        select_name_xpath = self.goods_status_select(select_name)
        return self.element_click(driver, By.XPATH, select_name_xpath)

    def click_bottom_button(self, driver: WebDriver, button_name: str):
        """
        根据按钮名称（button_name）定位商品新增页底部的按钮，并点击
        :param driver: 浏览器驱动
        :param button_name: 按钮名称
        :return:
        """
        bottom_button_xpath = self.add_goods_bottom_button(button_name)
        return self.element_click(driver, By.XPATH, bottom_button_xpath)

    def add_new_goods(self, driver: WebDriver, goods_title: str, goods_details: str, goods_num: int,
                      goods_img_list: list, goods_price, goods_status, bottom_button_name):
        """
        新增二手商品
        :param driver:浏览器驱动
        :param goods_title: 商品标题
        :param goods_details: 商品详情
        :param goods_num: 商品数量
        :param goods_img_list: 商品图片，可传多个
        :param goods_price: 商品单价
        :param goods_status: 商品状态（上架/下架）
        :param bottom_button_name: 底部按钮名称（提交/重置）
        :return:
        """
        self.input_goods_title(driver, goods_title)
        self.input_goods_details(driver, goods_details)
        self.select_goods_number(driver, goods_num)
        self.upload_mutil_goods_images(driver, goods_img_list)
        self.input_goods_price(driver, goods_price)
        self.select_goods_status(driver, goods_status)
        self.click_bottom_button(driver, bottom_button_name)
        return True

    def add_new_goods_list(self, driver: WebDriver, goods_list: dict):
        """
        新增二手商品
        :param driver:  浏览器驱动
        :param goods_list: 商品信息
        :return:
        """
        self.input_goods_title(driver, goods_list["goods_title"])
        self.input_goods_details(driver, goods_list["goods_details"])
        self.select_goods_number(driver, goods_list["goods_num"])
        self.upload_mutil_goods_images(driver, goods_list["goods_img_list"])
        self.input_goods_price(driver, goods_list["goods_price"])
        self.select_goods_status(driver, goods_list["goods_status"])
        self.click_bottom_button(driver, goods_list["bottom_button_name"])
        return True
