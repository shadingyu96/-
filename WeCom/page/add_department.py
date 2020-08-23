from time import sleep

from selenium.webdriver.common.by import By

from Shadingyu.WeCom.page.base import BasePage


class AddDepartment(BasePage):
    # 添加部门
    def add_department(self, name):
        self.find(By.CSS_SELECTOR,
                  ".qui_dialog_body [name='name']").send_keys(name)
        self.find(By.CSS_SELECTOR, ".qui_dialog_body [class='qui_btn ww_btn ww_btn_Dropdown js_toggle_party_list']").click()
        # self.find(By.CSS_SELECTOR, ".qui_dialog_body .js_parent_party_name").click()
        self.find(By.CSS_SELECTOR, ".qui_dialog_body [id='1688853079976831_anchor']").click()
        self.find(By.CSS_SELECTOR, "#__dialog__MNDialog__ .qui_btn.ww_btn.ww_btn_Blue").click()
        # list1 = self.finds(By.CSS_SELECTOR, "#1688853079976831 ul a")
        # new_department_list = []
        # for name in list1:
        #     new_department_list.append(name.text)
        sleep(2)
        return self.find(By.XPATH, "//*[@id=1688853079976831]//ul/li[last()]/a").text

