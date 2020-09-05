from selenium.webdriver.common.by import By

from Shadingyu.WeComPhone.page.Contact import Contact
from Shadingyu.WeComPhone.page.basepage import BasePage
from Shadingyu.WeComPhone.page.search import Search


class Message(BasePage):
    def goto_contact(self):
        self.steps("../page/message.yaml")
        return Contact(self._driver)

    def goto_search(self):
        # 点击搜索图标
        self.steps("../page/goto_search.yaml")
        return Search(self._driver)
