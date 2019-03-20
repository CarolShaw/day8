import os
import sys
sys.path.append(os.getcwd())
# ！！！！！！！！！！！！！！！！！！！！！！！！
# 此处一定要注意，import os sys一定要在导base模块之前
# 因为不在同级目录无法搜索到，只能先添加环境变量
# ！！！！！！！！！！！！！！！！！！！！！！！！

from base.get_driver import get_driver
from page.page_login import PageLogin


class TestLogin():

    # setup---实例化pagelogin的对象，因为pagelogin继承了base， 所以要传一个driver
    def setup(self):
        self.driver = get_driver()
        self.login = PageLogin(self.driver)


    # teardown
    def teardown(self):
        self.driver.quit()


    # 测试方法
    def test_login(self,username="itheima",pwd="123456"):
        self.login.page_Login(username,pwd)