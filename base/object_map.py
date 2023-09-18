"""
存放将 Selenium 二次封装的类

@Author SunYL
@Time 2023/9/15 14:10
"""
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException, NoSuchElementException, \
    StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

from common.yaml_config import GetConf


class ObjectMap:
    # root path
    parent_url = GetConf().get_url()

    def element_get(self, driver: WebDriver, locate_type, locator_expression, timeout=10, must_be_visible=False):
        """
        获取元素
        :param driver: 浏览器驱动
        :param locate_type: 元素定位器类型，比如 xpath
        :param locator_expression: 定位表达式
        :param timeout: 超时时间
        :param must_be_visible: 元素是否可见
        :return:
        """
        start_ms = time.time() * 1000  # 开始时间，获取秒级别的时间戳，转换为毫秒级别的
        stop_ms = start_ms + (timeout * 1000)  # 设置结束时间
        for x in range(int(timeout * 10)):
            try:
                element = driver.find_element(by=locate_type, value=locator_expression)  # 查找元素
                if not must_be_visible:  # 若元素不是必须可见，则直接返回元素
                    return element
                else:
                    if element.is_displayed():  # 判断元素是否可见，可见，则直接返回元素，否则，抛出异常
                        return element
                    else:
                        raise Exception()
            except Exception:
                now_ms = time.time() * 1000
                if now_ms > stop_ms:
                    break
                pass
            time.sleep(0.1)
        return ElementNotVisibleException("元素定位失败，定位方式：" + locate_type + " 定位表达式：" + locator_expression)

    def wait_for_ready_state_complete(self, driver: WebDriver, timeout=30):
        """
        等待页面完全加载完成
        :param driver: 浏览器驱动
        :param timeout: 超时时间
        :return:
        """
        start_ms = time.time() * 1000
        stop_ms = start_ms + (timeout * 1000)
        # 循环判断页面是否加载完成 -> 加载完成 -> 结束；未加载完成 -> 判断是否超时：超时->跳出循环，未超时->继续循环
        for x in range(int(timeout * 10)):
            try:
                ready_state = driver.execute_script(
                    "return document.readyState")  # 获取页面的状态。可能会因 driver 有问题而失败，因此抛出 WebDriverException
            except WebDriverException:
                time.sleep(0.03)
                return True
            if ready_state == 'complete':
                time.sleep(0.01)
                return True
            else:
                if time.time() * 1000 >= stop_ms:
                    break
                time.sleep(0.1)  # 防止程序跑太快，页面跟不上
        raise Exception("打开网页时，页面元素在 %s秒 后仍未完全加载成功" % timeout)

    def element_disappear(self, driver: WebDriver, locate_type, locator_expression, timeout=30):
        """
        等待页面元素消失
        :param driver: 浏览器驱动
        :param locate_type:  元素定位器类型，比如 xpath
        :param locator_expression: 定位表达式
        :param timeout: 超时时间
        :return:
        """
        if locate_type:  # 判断是否传入了定位方式，是->继续执行，否->直接返回
            start_ms = time.time() * 1000
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locator_expression)
                    if element.is_displayed:  # 元素可见
                        if time.time() * 1000 >= stop_ms:  # 超时，结束循环
                            break
                        time.sleep(0.1)
                except Exception:
                    return True
            raise Exception("元素未消失，定位方式：" + locate_type + " 定位表达式：" + locator_expression)
        else:  # 保持 if-else 的完整性
            pass

    def element_appear(self, driver: WebDriver, locate_type, locator_expression, timeout=30):
        """
        等待页面元素出现
        :param driver: 浏览器驱动
        :param locate_type:  元素定位器类型，比如 xpath
        :param locator_expression: 定位表达式
        :param timeout: 超时时间
        :return:
        """
        if locate_type:
            start_ms = time.time() * 1000
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
                except Exception:
                    if time.time() * 1000 >= stop_ms:
                        break
                    time.sleep(0.1)
            raise ElementNotVisibleException("元素未出现，定位方式：" + locate_type + " 定位表达式：" + locator_expression)
        else:
            pass

    def element_to_url(self, driver: WebDriver, url, locate_type_disappear=None, locate_expression_disappear=None,
                       locate_type_appear=None, locate_expression_appear=None):
        """
        跳转到指定的网址
        :param driver: 浏览器驱动
        :param url:    目标地址
        :param locate_type_disappear: 「等待页面元素消失」的元素定位
        :param locate_expression_disappear: 「等待页面元素消失」的定位表达式
        :param locate_type_appear: 「等待页面元素出现」的元素定位
        :param locate_expression_appear: 「等待页面元素出现」的定位表达式
        :return:
        """
        try:
            driver.get(self.parent_url + url)
            self.wait_for_ready_state_complete(driver)  # 等待页面元素都加载完成
            self.element_disappear(driver, locate_type_disappear, locate_expression_disappear)  # 跳转地址后等待元素消失
            self.element_appear(driver, locate_type_appear, locate_expression_appear)  # 跳转地址后等待元素出现
            return True
        except Exception as e:
            print("跳转地址出现异常，异常原因：%s" % e)
            return False

    def element_is_display(self, driver: WebDriver, locate_type, locator_expression):
        """
        判断元素是否显示
        :param driver: 浏览器驱动
        :param locate_type: 元素定位器类型，比如 xpath
        :param locator_expression: 定位表达式
        :return:
        """
        try:
            driver.find_element(by=locate_type, value=locator_expression)
            return True
        except NoSuchElementException:
            return False

    def element_fill_value(self, driver: WebDriver, locate_type, locator_expression, fill_value, timeout=30):
        """
        输入框内填入元素的值
        :param driver: 浏览器驱动
        :param locate_type: 元素定位器类型，比如 xpath
        :param locator_expression: 元素定位表达式
        :param fill_value: 填入的值
        :param timeout: 超时时间
        :return:
        """

        element = self.element_appear(driver, locate_type, locator_expression, timeout)  # 1⃣ 元素出现
        try:
            element.clear()  # 2⃣ 清除元素
        except StaleElementReferenceException:  # 当页面元素未刷新出来时抛出
            self.wait_for_ready_state_complete(driver)  # 等待页面元素加载完成
            element = self.element_appear(driver, locate_type, locator_expression, timeout)
            try:
                element.clear()
            except Exception:
                pass
        except Exception:
            pass

        fill_value_type = type(fill_value)
        if fill_value_type is int or fill_value_type is float:  # 将填入的值转成字符串（为何要转成字符串❓）
            fill_value = str(fill_value)
        try:
            self.append_return(fill_value, element, driver)
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver)  # 等待页面元素加载完成
            time.sleep(0.06)
            self.element_appear(driver, locate_type, locator_expression)  # 等待页面元素出现
            element.clear()
            self.append_return(fill_value, element, driver)
        except Exception:
            raise Exception("元素填值失败")
        return True

    def append_return(self, fill_value, element, driver: WebDriver):
        if not fill_value.endswith("\n"):  # 填入的值不以 \n 结尾，表明填入值后无需 return
            element.send_keys(fill_value)
        else:  # 若需要 return，需要去掉字符串中的 \n，再通过 Keys.RETURN 设置 return
            fill_value = fill_value[:-1]
            element.send_keys(fill_value)
            element.send_keys(Keys.RETURN)
        self.wait_for_ready_state_complete(driver)  # 等待页面元素加载完成

    def element_click(self, driver: WebDriver, locate_type, locator_expression, locate_type_disappear=None,
                      locate_expression_disappear=None,
                      locate_type_appear=None, locate_expression_appear=None, timeout=30):
        """
        元素点击
        :param driver: 浏览器驱动
        :param locate_type: 元素定位器类型，比如 xpath
        :param locator_expression: 元素定位表达式
        :param locate_type_disappear: 「等待页面元素消失」的元素定位
        :param locate_expression_disappear: 「等待页面元素消失」的定位表达式
        :param locate_type_appear: 「等待页面元素出现」的元素定位
        :param locate_expression_appear: 「等待页面元素出现」的定位表达式
        :param timeout 超时时间
        :return:
        """
        element = self.element_appear(driver, locate_type, locator_expression, timeout)  # 等待页面元素出现
        try:
            element.click()  # 点击元素
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver)  # 等待页面加载完成
            time.sleep(0.6)
            element = self.element_appear(driver, locate_type, locator_expression, timeout)  # 等待页面元素出现
            element.click()
        except Exception as e:
            print("页面出现异常，元素不可点击", e)
            return False

        try:
            self.element_appear(driver, locate_type_appear, locate_expression_appear)  # 等待页面元素出现
            self.element_disappear(driver, locate_type_disappear, locate_expression_disappear)  # 等待页面元素消失
        except Exception as e:
            print("等待元素消失或出现失败", e)
            return False
        return True

    def upload(self, driver: WebDriver, locate_type, locator_expression, file_path):
        """
        文件上传
        :param driver:浏览器驱动
        :param locate_type: 元素定位器类型，比如 xpath
        :param locator_expression: 元素定位表达式
        :param file_path: 文件路径
        :return:
        """
        element = self.element_get(driver, locate_type, locator_expression)
        return element.send_keys(file_path)

    def switch_window_to_latest_handle(self, driver: WebDriver):
        """
        切换窗口。每个窗口对于 selenium 来说都相当于一个句柄（handle）
        :param driver:
        :return:
        """
        window_handles = driver.window_handles  # 获取当前所有的句柄
        driver.switch_to.window(window_handles[-1])
