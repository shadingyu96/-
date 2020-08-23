import pytest

from Shadingyu.WeCom.page.index import Index


class TestWeCom:
    def setup(self):
        self.index = Index()

    def teardown(self):
        self.index.quit()

    @pytest.mark.parametrize("name", ["牛逼7"], ids=["通讯页添加部门"])
    def test_add_department(self, name):
        # 1.进入通讯录页 2.添加部门
        assert name in self.index.goto_login().goto_main().goto_contact().goto_add_department().add_department(name)

    @pytest.mark.parametrize("name, acctid, phone", [("圣枪游侠", 29490867, 13750034676)], ids=["主页添加成员"])
    def test_main_add_member(self, name, acctid, phone):
        # 主页点击添加成员
        assert name in self.index.goto_login().goto_main().goto_add_member().add_member(name, acctid, phone).get_member_list()

    @pytest.mark.parametrize("name, acctid, phone", [("伊泽瑞尔", 294908730, 13570259829)], ids=["通讯页添加成员"])
    def test_contact_add_member(self, name, acctid, phone):
        # 通讯录页添加成员
        assert name in self.index.goto_login().goto_main().goto_contact().goto_add_member()\
            .add_member(name, acctid, phone).get_member_list()

    def test_main_add_contact(self):
        # 主页添加通讯录
        self.index.goto_login().goto_main().goto_add_contact().add_contact()

    def test_contact_add_contact(self):
        # 通讯录页批量导入通讯录
        self.index.goto_login().goto_main().goto_contact().goto_add_contact().add_contact()

