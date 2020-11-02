from Shadingyu.test_request.api_page.page_api import BasePage
from Shadingyu.test_request.api_page.wework_utills import WeWorkUtils


class AddressPage(BasePage):
    def __init__(self):
        util = WeWorkUtils()
        _corpsecret = "lsgkRCZorU9MLTU7h-f7s0S7fOA4-fXIJutzJChxxIk"
        self.token = util.get_token(_corpsecret)

    def create_department(self, name, parentid):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/create",
            "params": {"access_token": self.token},
            "json": {"name": name, "parentid": parentid}
        }
        # r = requests.post(url, json=body)
        return self.send_api(data)

    def update_department(self):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/update",
            "params": {"access_token": self.token},
            "json": {
                "name": "超级部门111",
                "parentid": 1,
                "id": 11}
        }
        # r = requests.post(url, json=body)
        # print(r.text)
        # assert r.json()["errmsg"] == "updated"
        return self.send_api(data)

    def get_department(self):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/list",
            "params": {"ID": 11, "access_token": self.token}
        }

        # ID = 11
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}&id={ID}"
        # r = requests.get(url)
        # print(r.json())
        # assert r.json()["department"][0]["id"] == ID
        return self.send_api(data)

    def delete_department(self):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/delete",
            "params": {"ID": 11, "access_token": self.token}
        }
        # ID = 11
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={ID}"
        # r = requests.get(url)
        # print(r.json())
        # assert r.json()["department"][0]["id"] == ID
        return self.send_api(data)
