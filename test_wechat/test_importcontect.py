import shelve
from time import sleep

from Shadingyu.test_wechat.base import Base

"""
1、要先获取到企业微信的cookie
    -采用复用已有浏览器的方式（只能使用chrome，window先把chrome快捷方式地址配置到path环境变量，关闭所有chrome浏览器页面，命令行执行chrome --remote-debugging-port=9222）
    -在打开的chrome浏览器中登录企业微信后台管理账号
    -在setup方法中，设置调试器地址 (debugger_address)，设置的端口号与命令行执行的一致，引用option时要注意引用chrome的，代码语句如下：
        option = Options()
        option.debugger_address = "localhost:9222"
    -在实例化driver对象时，注意此处是chrome的，然后参数方法要使用options=，代码语句如下：
        self.driver = webdriver.Chrome(options=option)
2、在test_cookie方法中，要先去获取cookie，使用driver.get_cookies方法，并在控制台输出以便使用，代码语句如下：
    cookies = self.driver.get_cookies()
    print(cookies)
3、然后执行test_cookie方法，获取到cookies，在控制台复制并赋值给自定义变量cookies
4、此时已获取到cookies，则实例化driver时，不再需要复用浏览器cookie，即把实例化中参数删去；并且不需要重复获取和输出cookies，即注释掉2、中的代码
5、使用for循环和driver.add_cookie方法将cookie添加，用以完成登录验证(添加cookie如果遇到浮点型的参数，运行会报错，这种情况，可以去做处理，在for循环中添加if判断，通过对应key值判断，pop删除这个值)
6、然后就可以进行登陆后的操作验证等
"""


class TestContact(Base):

    def test_add_contact(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu")
        # cookies = self.driver.get_cookies()
        # print(cookies)
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688852957646903'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688852957646903'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '1169990266'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '3048640512'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325015158632'},
            {'domain': '.qq.com', 'expiry': 1597930780, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1634045579.1597766254'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'NKduK8gBwGJuIvPjEG4pY6ykViE-ggEkClabUOtPc4Pmv1wBRlmpw-XgrTm1j94H'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a9835041'},
            {'domain': '.qq.com', 'expiry': 1609045614, 'httpOnly': False, 'name': 'ied_qq', 'path': '/',
             'secure': False, 'value': 'o0294908720'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '41657893042370346'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1597871044, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '22ijft9'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1600436416, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh-cn'},
            {'domain': '.qq.com', 'expiry': 1660916380, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.642293014.1597766254'},
            {'domain': '.qq.com', 'expiry': 1885204123, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': False, 'value': 'bbab833ded91952e'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1629302252, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 1597844428, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 1598103827, 'httpOnly': False, 'name': 'same_pc', 'path': '/',
             'secure': False, 'value': '%7B%7D'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'DS9_nW_rRmLkpS6BxduiqkHtXnvYnfdf9qqqGVyzuHfwWKZEqc7Dl2tMcx7XfaGGlyMhQFo6LECgMJkMTP7UqHXdV2OR9Z0Km9-ICMZzuxbNSPP2XEiV73Q2DZh5gA5uUGoUWnbMYb6n4yIgUcZ2sLqXxQTSF_-LnmS1ubjnsiDg4ME_m8tnihonk32fydl2ZZbCfwj2GDPfL8kH04nF5-5Gti7lpiVCI32H3C1ZKvb-lDGYi1rBX7WlM8Rz0X-zgCBDebb19BqVVbtwQ685SA'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1629375608, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
             'value': '1597766325,1597839510'},
            {'domain': '.qq.com', 'expiry': 1901607217, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '1_294908720'},
            {'domain': '.qq.com', 'expiry': 1600432181, 'httpOnly': False, 'name': 'eas_sid', 'path': '/',
             'secure': False, 'value': '21c5L6l8E81946f1I8G162Q7e1'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '5133910d29ad5c9feb3890e26f7be221f0d876369a45d01eddcc955207d56f42'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
             'secure': False, 'value': '294908720'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147483649, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'nRKowJToMp'}]
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu")
        self.driver.find_element_by_css_selector("#menu_contacts span").click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[3]/div[1]/div[2]/a/div[1]').click()
        self.driver.find_element_by_xpath('//*[@id="js_contacts44"]/div/div[2]/div/div[2]/div[3]/div[1]/div[2]/div/ul/li[1]/a').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="js_upload_file_input"]').send_keys(r"D:\Hogwarts1\Shadingyu\test_wechat\data.xls")
        my_fileName = self.driver.find_element_by_id("upload_file_name").text
        assert my_fileName == "data.xls"

    def test_add_contact2(self):

        # shelve 小型的数据库， 对象持久化保存方法
        db = shelve.open("mydb/logincookies")
        # db["cookie"] = cookies
        cookies = db["cookie"]
        db.close()

        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu")

        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu")
        self.driver.find_element_by_css_selector("#menu_contacts span").click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[3]/div[1]/div[2]/a/div[1]').click()
        self.driver.find_element_by_xpath('//*[@id="js_contacts44"]/div/div[2]/div/div[2]/div[3]/div[1]/div[2]/div/ul/li[1]/a').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="js_upload_file_input"]').send_keys(r"D:\Hogwarts1\Shadingyu\test_wechat\data.xls")
        my_fileName = self.driver.find_element_by_id("upload_file_name").text
        assert my_fileName == "data.xls"
