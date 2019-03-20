
from base.base01 import Base

import page


class PageLogin(Base):

    # 封装输入用户名
    def page_input_username(self,username):
        self.base_input(page.login_username,username)

    # 封装输入密码
    def page_input_pwd(self,pwd):
        self.base_input(page.login_pwd,pwd)

    # 封装点击登录
    def page_click_login(self):
        self.base_click_ele(page.login_btn)

    # 组装业务方法
    def page_Login(self,username,pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login()
