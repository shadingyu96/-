from Shadingyu.test_request.api_page.address_page import AddressPage


class TestRequest:
    def setup_class(self):
        self.department_page = AddressPage()

    def test_create_department(self):
        message = self.department_page.create_department("超级部门", 1)
        assert message["errmsg"] == "created"

    def test_update_department(self):
        assert r.json()["errmsg"] == "updated"

    def test_get_department(self):
        assert r.json()["department"][0]["id"] == ID

    def test_delete_department(self):
        assert r.json()["department"][0]["id"] == ID
