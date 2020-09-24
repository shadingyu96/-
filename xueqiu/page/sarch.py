from selenium.webdriver.common.by import By

from Shadingyu.xueqiu.page.base_page import BasePage


class Search(BasePage):
    def search(self, search):
        self._params["search"] = search
        self.steps("search", "search")
        return self

    def get_price(self):
       return self.steps("search", "price")

