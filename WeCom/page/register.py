from selenium.webdriver.common.by import By

from Shadingyu.WeCom.page.base import BasePage


class Register(BasePage):
    # 注册填写信息
    def register(self, corp_name, manager_name):
        self.find(By.CSS_SELECTOR, "#corp_name").send_keys(corp_name)
        self.find(By.CSS_SELECTOR, "#manager_name").send_keys(manager_name)
        return self.find(By.CSS_SELECTOR, "#corp_name").get_attribute("class")
