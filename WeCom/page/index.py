from selenium.webdriver.common.by import By

from Shadingyu.WeCom.page.base import BasePage
from Shadingyu.WeCom.page.login import Login
from Shadingyu.WeCom.page.register import Register


class Index(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    # 进入注册页面
    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self._driver)

    # 进入登录页面
    def goto_login(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login(self._driver)
