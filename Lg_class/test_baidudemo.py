import time

import allure
import pytest
import yaml
from selenium import webdriver


@allure.testcase("http://www.github.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize("test_date1", yaml.safe_load(open("data/data.yaml", encoding="utf-8")))
def test_steps_demo(test_date1):
    with allure.step("打开百度网页"):
        driver = webdriver.Chrome()
        driver.get("http://baidu.com")
        driver.maximize_window()

    with allure.step(f"输入搜素词：{test_date1}"):
        driver.find_element_by_id("kw").send_keys(test_date1)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("保存图片"):
        driver.save_screenshot("./result/b.png")
        allure.attach.file("./result/b.png", attachment_type=allure.attachment_type.PNG)

    with allure.step("关闭浏览器"):
        driver.quit()
