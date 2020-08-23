from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        self._driver = ""
        if driver is None:
            # self._driver = webdriver.Chrome()
            option = Options()
            option.debugger_address = "localhost:9222"
            self._driver = webdriver.Chrome(options=option)
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.maximize_window()
            self._driver.get(self._base_url)

    def quit(self):
        self._driver.quit()

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)
