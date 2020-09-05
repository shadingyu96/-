from appium import webdriver

from Shadingyu.WeComPhone.page.basepage import BasePage
from Shadingyu.WeComPhone.page.message import Message


class App(BasePage):
    # 指定app的报名和activity名
    _package = "com.tencent.wework"
    _activity = "com.tencent.wework.launch.WwMainActivity"

    def start(self):
        # 如果driver为空则初始化
        if self._driver is None:
            caps = {}
            caps['platformName'] = 'Android'
            caps['platformVersion'] = '6.0'
            caps['deviceName'] = 'emulator-5554'
            caps['appPackage'] = self._package
            caps['appActivity'] = self._activity
            caps['noReset'] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(3)
        # 如果driver不为空，则直接启动activity
        else:
            print(self._driver)
            self._driver.start_activity(self._package, self._activity)

        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def message(self):
        return Message(self._driver)
