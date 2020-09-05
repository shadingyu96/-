from selenium.webdriver.common.by import By

from Shadingyu.WeComPhone.page.basepage import BasePage
from Shadingyu.WeComPhone.page.member import Member


class Search(BasePage):
    def search(self, value):
        self.find(By.XPATH, "//*[@text='搜索']").send_keys(value)
        return self

    def goto_member(self):
        self.find(By.ID, "com.tencent.wework:id/duo").click()
        return Member(self._driver)
