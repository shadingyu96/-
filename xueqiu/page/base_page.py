import logging

import yaml
from appium.webdriver import WebElement

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from appium import webdriver


class BasePage(object):
    _driver: WebDriver = None
    _current_element: WebElement = None
    _black_list = []
    _error_count = 0
    _error_max = 10
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def __init__(self, po_file=None, driver: WebDriver = None):
        if po_file is not None:
            self._po_file = po_file
        # self._driver = driver

    # def start(self):
    #     if self._driver is None:
    #         caps = dict()
    #         caps["platformName"] = "android"
    #         caps["platformVersion"] = "6.0"
    #         caps["deviceName"] = "emulator-5554"
    #         caps["appPackage"] = self._package
    #         caps["appActivity"] = self._activity
    #         caps["noReset"] = True
    #         self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    #         self._driver.implicitly_wait(20)
    #     else:
    #         self._driver.start_activity(self._package, self._activity)
    @classmethod
    def start(cls):
        caps = {
            'platformName': 'android',
            'deviceName': 'ceshiren.com',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            'noReset': True
        }
        cls._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        cls._driver.implicitly_wait(20)
        return cls

    def stop(self):
        BasePage._driver.quit()

    def exception_handle(fun):
        def magic(*args, **kwargs):
            instance: BasePage = args[0]


    def find(self, by, locator=None):
        try:
            if isinstance(by, tuple):
                self._current_element = BasePage._driver.find_element(*by)
                self._error_count = 0
                return self._current_element
            else:
                self._current_element = BasePage._driver.find_element(*by)
                self._error_count = 0
                return self._current_element

        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            for black in self._black_list:
                elements = BasePage._driver.find_elements(*black)
                if len(elements) >= 1:
                    elements[0].click()
                    return self.find(by, locator)
            raise e

    def click(self):
        try:
            self._current_element.click()
            return self
        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            for black in self._black_list:
                elements = BasePage._driver.find_elements(*black)
                if len(elements) >= 1:
                    elements[0].click()
                    return self.click()
            raise e

    def send(self, value):
        try:
            self._current_element.send_keys(value)
            return self
        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            for black in self._black_list:
                elements = BasePage._driver.find_elements(*black)
                if len(elements) >= 1:
                    elements[0].click()
                    return self.send(value)
            raise e

    def get_text(self):
        try:
            value = self._current_element.text
            return value
        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            for black in self._black_list:
                elements = BasePage._driver.find_elements(*black)
                if len(elements) >= 1:
                    elements[0].click()
                    return self.get_text()
            raise e

    def steps(self, method, **kwargs):
        with open(self._po_file, encoding='UTF-8') as f:
            steps: list[dict] = yaml.safe_load(f)
            for step in steps[method]:
                if isinstance(step, dict):
                    for key in step.keys():
                        if key in ['id', 'aid', 'xpath', 'name']:
                            locator = (key, step[key])
                            self.find(locator)
                        elif key == "text":
                            locator = (By.XPATH, f"//*[contains(@text, '{step[key]}')]")
                            self.find(locator)
                        elif key == 'click':
                            self.click()
                        elif key == 'send':
                            content: str = step[key]
                            for k, v in kwargs.items():
                                content = content.replace(f"{k}", v)
                                self.send(content)
                        elif key == 'get_text':
                            return self.get_text()

                        # todo: 更多关键词
                        else:
                            logging.error(f"dont know {step}")
