from time import sleep

from selenium.webdriver.common.by import By

from Shadingyu.WeCom.page.add_contact import AddContact
from Shadingyu.WeCom.page.add_department import AddDepartment
from Shadingyu.WeCom.page.add_member import AddMember
from Shadingyu.WeCom.page.base import BasePage


class Contact(BasePage):
    def goto_add_member(self):
        sleep(2)
        self.find(By.CSS_SELECTOR,".ww_operationBar .qui_btn.ww_btn.js_add_member").click()
        return AddMember(self._driver)

    def goto_add_department(self):
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        self.find(By.CSS_SELECTOR, ".js_create_party").click()
        return AddDepartment(self._driver)

    def goto_add_contact(self):
        self.find(By.CSS_SELECTOR, "#js_contacts261 > div > div.member_colRight > div > "
                                   "div.js_party_info > div.js_has_member > div:nth-child(1) "
                                   "> div.ww_btnWithMenu.js_btnWithMenu.js_import_other_wrap.ww_btnWithMenu_Open "
                                   "> a > div.ww_btn_PartDropdown_left").click()
        return AddContact(self._driver)

    def get_member_list(self):
        name_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        list1 = []
        for name in name_list:
            list1.append(name.text)
        return list1