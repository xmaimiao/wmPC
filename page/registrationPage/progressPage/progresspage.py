from selenium.webdriver.common.by import By
from page.basepage import BasePage
from page.registrationPage.progressPage.studentlistpage import StudentList


class Progress(BasePage):
    term_ele = (By.XPATH, '//div[@class="table-top-bar bottom-line"]/*/*[1]/*[2]')
    total_ele = (By.XPATH,'//div[@class="table-top-bar bottom-line"]/div/div[1]//ul[2]/li[1]')
    studentlist_ele = (By.XPATH,'//div[@class="ivu-table-body"]//tbody/tr[1]/td[last()]/*/*/*/span[2]')

    def simple_search(self):
        # 點擊入學學期，出現下拉框
        self.find_click(*self.term_ele)
        # 點擊“全部”選項
        self.find_click(*self.total_ele)
        return self

    def goto_firstevent_stulist(self):
        self.find_click(*self.studentlist_ele)
        return StudentList(self._driver)

