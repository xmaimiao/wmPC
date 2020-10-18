from time import sleep

from selenium.webdriver.common.by import By

from page.basepage import BasePage
from page.classtimetablePage.undergraduate_recordsPage.signrecorddetailpage import SignRecordDetail


class UnderGraduteRecord(BasePage):
    search_input_ele = (By.XPATH, '//*[@class="content"]/div[2]//input')
    search_click_ele = (By.XPATH, '//*[@class="ivu-icon ivu-icon-ios-search"]')
    advanced_search_ele = (By.XPATH, '//*[@class="content"]/span')
    term_ele = (By.XPATH, '//*[@class="form-items-wrapper"]//input[@class="ivu-select-input"]')
    class_ele = (By.XPATH, '//div[@class="form-items-wrapper"]/table[2]//input')
    course_ele = (By.XPATH, '//div[@class="form-items-wrapper"]/table[4]//input')
    search_comfirm_ele = (By.XPATH, '//div[@class="form-items-wrapper"]/..//span[contains(text(),"搜索")]')
    view_ele = (By.XPATH,'//tbody[@class="ivu-table-tbody"]//td[last()]//p')
    def simple_search(self,value):
        self.find_sendkeys(*self.search_input_ele,value)
        self.find_click(*self.search_click_ele)
        return self

    def advanced_search(self,term,stuclass,course):
        # 点击高级搜索
        self.find_click(*self.advanced_search_ele)
        # 点击学期
        term = (By.XPATH, f'//div[@class="form-items-wrapper"]//ul[@class="ivu-select-dropdown-list"]/li[contains(text(),"{term}")]')
        self.find_click(*self.term_ele)
        self.find_click(*term)
        # 输入学生班别
        self.find_sendkeys(*self.class_ele,stuclass)
        # 输入学生科目
        self.find_sendkeys(*self.course_ele,course)
#         点击搜索
        self.find_click(*self.search_comfirm_ele)
        return self

    def advanced_srarch_result_goto_signrecord(self,course):
        course_ele = (By.XPATH,f'//tbody[@class="ivu-table-tbody"]//td[3]//span[contains(text(),"{course}")]')
        self.wait_for_display(course_ele)
        sleep(1)
        self.find_click(*self.view_ele)
        return SignRecordDetail(self._driver)





