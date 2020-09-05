import logging

import yaml
from appium.webdriver import WebElement

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage(object):
    _current_element: WebElement = None
    _black_list = []
    _error_count = 0
    _error_max = 10
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, by, locator=None):
        try:
            if isinstance(by, tuple):
                self._current_element = self._driver.find_element(*by)
                self._error_count = 0
                return self
            else:
                self._current_element = self._driver.find_element(*by)
                self._error_count = 0
                return self

        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
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
                elements = self._driver.find_elements(*black)
                if len(elements) >= 1:
                    elements[0].click()
                    return self._current_element.click()
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
                elements = self._driver.find_elements(*black)
                if len(elements) >= 1:
                    elements[0].click()
                    return self._current_element.send_keys(value)
            raise e

    def text(self):
        try:
            value = self._current_element.text
            return value
        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) >= 1:
                    elements[0].click()
                    return self._current_element.text
            raise e

    def steps(self, path, method):
        with open(f"../page/{path}.yaml", encoding='UTF-8') as f:
            steps: list[dict] = yaml.safe_load(f)
            for step in steps[method]:
                if isinstance(step, dict):
                    for key in step.keys():
                        if key == "id":
                            locator = (By.ID, step[key])
                            self.find(locator)
                        elif key == "xpath":
                            locator = (By.XPATH, step[key])
                            self.find(locator)
                        elif key == 'click':
                            self.click()
                        elif key == 'send':
                            content: str = step[key]
                            for parm in self._params:
                                content = content.replace("{%s}" % parm, self._params[parm])
                                self.send(content)
                        elif key == 'text':
                            return self.text()

                        # todo: 更多关键词
                        else:
                            logging.error(f"dont know {step}")
