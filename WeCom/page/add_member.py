from selenium.webdriver.common.by import By
from Shadingyu.WeCom.page.base import BasePage


class AddMember(BasePage):
    # 添加成员
    def add_member(self, name, acctid, phone):
        from Shadingyu.WeCom.page.contact import Contact
        # 填写姓名
        self.find(By.CSS_SELECTOR, "#username").send_keys(name)
        # 填写账号
        self.find(By.CSS_SELECTOR, "#memberAdd_acctid").send_keys(acctid)
        # 填写手机
        self.find(By.CSS_SELECTOR, "#memberAdd_phone").send_keys(phone)
        # 保存并添加
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return Contact(self._driver)

