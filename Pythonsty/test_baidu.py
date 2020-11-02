import multiprocessing
from time import sleep

from threading import Thread

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class TestSearch:
    def setup(self):
        self.driver = webdriver.Remote(
        command_executor="http://42.194.136.183:5001/wd/hub",
                           desired_capabilities=DesiredCapabilities.CHROME
        )

    def test_search(self):
        self.driver.get('https://www.baidu.com')

        self.driver.find_element('id', 'kw').send_keys('孙高飞')
        sleep(2)
        self.driver.find_element('id', 'su').click()
        self.driver.quit()

    def test_search1(self):
        self.driver.get('https://www.baidu.com')

        self.driver.find_element('id', 'kw').send_keys('高军')
        sleep(4)
        self.driver.find_element('id', 'su').click()
        self.driver.quit()

    # def teardown(self):
    #     self.driver.quit()

    def test_search2(self):
        self.driver.get('https://www.baidu.com')

        self.driver.find_element('id', 'kw').send_keys('左美丽')
        sleep(6)
        self.driver.find_element('id', 'su').click()
        self.driver.quit()


def run(case_name):
    pytest.main([f"test_baidu.py::TestSearch::{case_name}", "-v", "-s"])


if __name__ == '__main__':
    # t1 = Thread(target=TestSearch)
    # t2 = Thread(target=TestSearch1)
    #
    # t1.start()
    # t2.start()
    name_list = ["test_search", "test_search1", "test_search2"]
    # pytest.main(["test_selenium.py::TestSelenium::test_baidu2", "-v", "-s"])
    pool = multiprocessing.Pool(3)
    pool.map(run, name_list)
    pool.close()
    pool.join()
