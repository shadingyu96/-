
from Shadingyu.xueqiu.page.app import App


class TestXueQiu:
    def setup_class(self):
        self.app = App()
        self.app.start()

    def teardown_class(self):
        self.app.stop()

    def test_search(self):
        price = self.app.goto_main().goto_search().search("alibaba").get_price()
        assert price >= 200
