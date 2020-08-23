from selenium.webdriver.common.by import By
from Shadingyu.WeCom.page.add_contact import AddContact
from Shadingyu.WeCom.page.base import BasePage
from Shadingyu.WeCom.page.contact import Contact


class Main(BasePage):
    # 进入通讯录页面
    def goto_contact(self):
        self.find(By.CSS_SELECTOR, "#menu_contacts").click()
        return Contact(self._driver)

    # 进入添加成员页面
    def goto_add_member(self):
        from Shadingyu.WeCom.page.add_member import AddMember
        self.find(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMember(self._driver)

    # 进入添加通讯录页面
    def goto_add_contact(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        return AddContact(self._driver)
