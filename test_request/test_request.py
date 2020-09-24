import requests


class TestRequest:
    def test_get_token(self):
        corpid = "wwf55a566b6d1c6bd3"
        corpsecret = "lsgkRCZorU9MLTU7h-f7s0S7fOA4-fXIJutzJChxxIk"
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
        # print(r.json()['access_token'])
        return r.json()['access_token']

    def test_create_department(self):
        token = self.test_get_token()
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={token}"
        body = {
            "name": "超级部门1",
            "parentid": 1
        }
        r = requests.post(url, json=body)
        print(r.text)
        assert r.json()["errmsg"] == "created"

    def test_update_department(self):
        token = self.test_get_token()
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={token}"
        body = {
            "name": "超级部门111",
            "parentid": 1,
            "id": 11
        }
        r = requests.post(url, json=body)
        print(r.text)
        assert r.json()["errmsg"] == "updated"

    def test_get_department(self):
        token = self.test_get_token()
        ID = 11
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={token}&id={ID}"
        r = requests.get(url)
        print(r.json())
        assert r.json()["department"][0]["id"] == ID

    def test_delete_department(self):
        token = self.test_get_token()
        ID = 11
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={token}&id={ID}"
        r = requests.get(url)
        print(r.json())
        assert r.json()["department"][0]["id"] == ID
