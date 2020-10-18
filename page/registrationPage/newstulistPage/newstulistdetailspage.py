from time import sleep
from selenium.webdriver.common.by import By
from page.basepage import BasePage
from page.registrationPage.newstulistPage.eventdetailpage import EventDetail


class NewStuListDetails(BasePage):
    title_ele = (By.XPATH,'//*[contains(text(),"新生報道詳情")]')
    first_ele = (By.XPATH,'//*[@class="ivu-table-tbody"]/*[1]/*[2]/*/*')
    last_ele = (By.XPATH,'//*[@class="ivu-table-tbody"]/*[last()]/*[2]/*/*')
    editadress_ele = (By.XPATH,'//*[@class="ivu-table-tbody"]/*[1]/*[2]/following-sibling::td[3]/*/*/*/*')
    first_ele_stutas = (By.XPATH,'//*[@class="ivu-table-tbody"]/*[1]/*[2]/following-sibling::td[4]/*/*/*')
    operate_button = (By.XPATH,'//*[@class="ivu-table-tbody"]/*[1]/*[2]/following-sibling::td[last()]/*/*/*')
    goback_ele = (By.LINK_TEXT,"Go back")
    adress_input_ele = (By.XPATH,'//*[@class="ivu-input ivu-input-default"]')
    button_comfire = (By.XPATH,'//*[@class="ivu-modal-wrap"]//button[1]')
    toast_ele = (By.XPATH,'//*[@class="ivu-message-notice-content"]//span')

    def first_event(self):
        self.wait_for_display(self.title_ele)
        firstevent = self.find(*self.first_ele).text
        return firstevent

    def last_event(self):
        self.wait_for_display(self.title_ele)
        lastevent = self.find(*self.last_ele).text
        return lastevent

    def edit_dress(self,adress):
        # 點擊第一個事件的辦理地點-更改按鈕
        self.wait_for_display(self.title_ele)
        # 該事件狀態未完成，則可更改地點
        if len(self.finds(*self.editadress_ele)):
            if self.find(*self.first_ele_stutas).text == "未完成":
                # 點擊更改按鈕
                self.find_click(*self.editadress_ele)
                # 等待彈出框出現，清空input框，輸入内容
                self.wait_for_display(self.adress_input_ele)
                self.find(*self.adress_input_ele).clear()
                self.find_sendkeys(*self.adress_input_ele,adress)
                self.find_click(*self.button_comfire)
                sleep(2)
                # 獲取“更改成功”的toast
                result = self.find(*self.toast_ele).get_attribute('textContent')
                return result
            else:
                print("該事項已完成，無法更改")
                return
        return False

    def goto_event_detail(self):
        self.wait_for_display(self.title_ele)
        if len(self.finds(*self.operate_button)):
            self.find_click(*self.operate_button)
            return EventDetail(self._driver)
        return False

