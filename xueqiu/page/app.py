from appium import webdriver

from Shadingyu.xueqiu.page.base_page import BasePage
from Shadingyu.xueqiu.page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        if self._driver is None:
            caps = dict()
            caps["platformName"] = "android"
            caps["platformVersion"] = "6.0"
            caps["deviceName"] = "emulator-5554"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["noReset"] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(10)

        else:
            self._driver.start_activity(self._package, self._activity)

    def stop(self):
        self._driver.quit()

    def restart(self):
        pass

    def goto_main(self):
        return Main(self._driver)
