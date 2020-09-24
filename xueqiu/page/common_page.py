from Shadingyu.xueqiu.page.base_page import BasePage
from Shadingyu.xueqiu.page.log import log


class CommonPage(BasePage):
    def __getattr__(self, item):
        # log.debug(f"__getattr__{item}")
        self._method_name = item
        # 当方法找不到时，调用一个通用方法进行处理
        return self._po_method

    # 定义通用方法
    def _po_method(self, **kwargs):
        # log.debug(f"_po_method {kwargs}")
        # self.steps(self._method_name, **kwargs)
        return self.steps(self._method_name, **kwargs)
