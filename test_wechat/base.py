from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Base:
    def setup(self):
        option = Options()
        option.debugger_address = "localhost:9222"
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass
