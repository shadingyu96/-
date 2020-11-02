from Shadingyu.test_request.api_page.page_api import BasePage


class WeWorkUtils(BasePage):
    def get_token(self, corpsecret, corpid="wwe653983e4c732493"):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {"corpid": corpid, "corpsecret": corpsecret}
        }
        result = self.send_api(data)
        return result["access_token"]
