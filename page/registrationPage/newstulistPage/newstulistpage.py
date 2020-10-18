from time import sleep

from selenium.webdriver.common.by import By
from page.basepage import BasePage
from page.registrationPage.newstulistPage.newstulistdetailspage import NewStuListDetails


class NewStuLsit(BasePage):
    term_ele = (By.XPATH,'//div[@class="table-top-bar bottom-line"]/*/*[2]/*[2]')
    total_ele = (By.XPATH,'//div[@class="table-top-bar bottom-line"]/*/*[2]/*[2]/*[2]/*[2]/*[1]')
    input_ele = (By.XPATH,'//*[@class="ivu-input ivu-input-default"]')
    search_ele = (By.XPATH,'//*[@class="pair-label-any"][3]/*[2]/*[2]')
    eventdetail_title_ele = (By.XPATH, '//*[contains(text(),"新生報道詳情")]')
    export_ele = (By.XPATH,'//*[@class="title-bar"]/div//span')
    exported_text = (By.XPATH, '//*[@class="ivu-message-notice-content"]//span')
    detail_no_ele = (By.XPATH,'//*[@class="ivu-table-tbody"]/tr[1]/td[last()]//p')

    def simple_search(self,staffNO):
        # 點擊入學學期，出現下拉框
        sleep(2)
        self.find_click(*self.term_ele)
        # 點擊“全部”選項
        self.find_click(*self.total_ele)
        # 在搜索框輸入學號，點擊查詢
        self.find(*self.input_ele).clear()
        self.find_sendkeys(*self.input_ele,staffNO)
        self.find_click(*self.search_ele)
        return self

    def search_result_guide(self,stffNo):
        ele = (By.XPATH,f'//*[contains(text(),"{stffNo}")]/../../following-sibling::td[6]/*/*/*')
        result = self.wait_for_display(ele).text
        return result

    def search_result_groupinsurance(self,stffNo):
        ele = (By.XPATH, f'//*[contains(text(),"{stffNo}")]/../../following-sibling::td[8]/*/*/*')
        result = self.wait_for_display(ele).text
        return result


    def search_result_progress(self,stffNo):
        ele = (By.XPATH,f'//*[contains(text(),"{stffNo}")]/../../following-sibling::td[9]/*/*/*')
        result = self.wait_for_display(ele).text
        return result

    def search_result_progress_status(self,stffNo):
        ele = (By.XPATH,f'//*[contains(text(),"{stffNo}")]/../../following-sibling::td[10]/*/*/*')
        result = self.wait_for_display(ele).text
        return result

    def goto_details(self,stffNo):
        ele = (By.XPATH, f'//*[contains(text(),"{stffNo}")]/../../following-sibling::td[last()]/*/*/*/*')
        # 打開詳情頁，不斷點擊“詳情”直到跳轉頁面的title出現，停止點擊
        def detail_button_condition(x):
            element_len = len(self.finds(*self.eventdetail_title_ele))
            if element_len <= 0:
                self.find(*ele).click()
            return element_len > 0
        self.wait_for_condition(detail_button_condition)
        return NewStuListDetails(self._driver)

    def goto_detail_nosearch(self):
        result = self.find(*self.detail_no_ele).text
        return result


    def export(self):
        if len(self.finds(*self.export_ele)):
            self.find_click(*self.export_ele)
            sleep(2)
            text = self.find(*self.exported_text).text
            return text
        return False
