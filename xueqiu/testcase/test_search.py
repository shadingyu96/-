from time import sleep

import pytest

from Shadingyu.xueqiu.page.base_page import BasePage
from Shadingyu.xueqiu.page.common_page import CommonPage
from Shadingyu.xueqiu.page.log import log


class TestXueQiu:
    po_file = '../page/search_page.yaml'

    def setup_class(self):
        self.app = BasePage()
        self.app.start()
        # sleep(10)

    def teardown_class(self):
        self.app.stop()

    @pytest.mark.parametrize('value', ['alibaba'])
    def test_search(self, value):
        # price = self.app.goto_main().goto_search().search("alibaba").get_price()
        demo = CommonPage(self.po_file)
        demo.search(search=value)
        price = demo.get_price()
        log.info(price)
        assert float(price) >= 200
