from selenium.webdriver.common.by import By

from Shadingyu.WeCom.page.base import BasePage
from Shadingyu.WeCom.page.main import Main
from Shadingyu.WeCom.page.register import Register


class Login(BasePage):
    # 进入注册页面
    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return Register(self._driver)

    # 扫描二维码，进入主页面
    def goto_main(self):
        return Main(self._driver)

