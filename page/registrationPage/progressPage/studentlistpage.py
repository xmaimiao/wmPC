from selenium.webdriver.common.by import By

from page.basepage import BasePage
from page.registrationPage.progressPage.detailpage import Detail


class StudentList(BasePage):
    input_ele = (By.XPATH, '//*[@class="table-top-bar bottom-line"]/div[2]/div[2]/div/div[1]/input')
    search_ele = (By.XPATH, '//*[@class="table-top-bar bottom-line"]/div[2]/div[2]/div/div[2]')
    close_ele = (By.XPATH, '//*[@class="button-close"]')

    def simple_search(self,staffNo):
        # 在搜索框輸入學號，點擊查詢
        self.find(*self.input_ele).clear()
        self.find_sendkeys(*self.input_ele, staffNo)
        self.find_click(*self.search_ele)
        return self

    def event_stutas(self,staffNo):
        stutas_ele = (By.XPATH, f'//*[contains(text(),"{staffNo}")]/../../following-sibling::td[last()-1]/*/*/*/div')
        self.wait_for_display(stutas_ele)
        stutas = self.find(*stutas_ele).text
        return stutas

    def goto_detail(self,staffNo):
        stutas_ele = (By.XPATH, f'//*[contains(text(),"{staffNo}")]/../../following-sibling::td[last()]/*/*/*/span')
        def detail_button_condition(x):
            element_len = len(self.finds(*self.close_ele))
            if element_len <= 0:
                self.find(*stutas_ele).click()
            return element_len > 0
        self.wait_for_condition(detail_button_condition)
        return Detail(self._driver)
