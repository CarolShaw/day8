from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 实例化driver对象
    def __init__(self,driver):
        self.driver = driver

    # 定位元素--设置元素等待
    def base_find_element(self,loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 点击元素
    def base_click_ele(self,loc):
        self.base_find_element(loc).click()

    # 元素输入
    def base_input(self,loc,value):
        self.base_find_element(loc).send_keys(value)