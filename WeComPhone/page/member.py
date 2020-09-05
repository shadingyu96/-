from selenium.webdriver.common.by import By

from Shadingyu.WeComPhone.page.basepage import BasePage


class Member(BasePage):
    def del_member(self):
        self.find(By.ID, "com.tencent.wework:id/hjz").click()
        self.find(By.ID, "com.tencent.wework:id/gmz").click()
        self.find(By.ID, "com.tencent.wework:id/hjz").click()
        self.find(By.ID, "com.tencent.wework:id/b53").click()
        self.find(By.ID, "com.tencent.wework:id/e_1").click()
        self.find(By.ID, "com.tencent.wework:id/bfe").click()
        return 
