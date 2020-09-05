from Shadingyu.xueqiu.page.base_page import BasePage
from Shadingyu.xueqiu.page.sarch import Search


class Main(BasePage):
    def goto_search(self):
        self.steps("main", "search")
        return Search(self._driver)