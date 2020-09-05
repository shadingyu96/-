from Shadingyu.WeComPhone.page.basepage import BasePage
from Shadingyu.WeComPhone.page.search import Search


class Contact(BasePage):
    def goto_message(self):
        from Shadingyu.WeComPhone.page.message import Message
        return Message(self._driver)

    def goto_search(self, value):
        return Search(self._driver)
