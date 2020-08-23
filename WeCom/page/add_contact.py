from selenium.webdriver.common.by import By

from Shadingyu.WeCom.page.base import BasePage


class AddContact(BasePage):
    # 添加通讯录
    def add_contact(self, xls):
        self.find(By.CSS_SELECTOR, ".qui_btn ww_btn ww_fileInputWrap").send_keys(xls)
        return self.find(By.CSS_SELECTOR, "#upload_file_name").text
