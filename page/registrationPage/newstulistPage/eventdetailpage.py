from time import sleep

from selenium.webdriver.common.by import By

from page.basepage import BasePage


class EventDetail(BasePage):
    stutas_text = (By.XPATH,'//label[contains(text(),"狀態")]/following-sibling::span')
    repeat_ele = (By.XPATH,'//*[@class="btn-active w-150 h-46 ivu-btn ivu-btn-default"]')
    repeat_input_ele = (By.XPATH,'//textarea[@class="ivu-input"]')
    repeat_confirm = (By.XPATH,'//div[@class="ivu-modal-wrap"]//span[contains(text(),"確認")]')
    history_num = (By.XPATH,'//*[@class="we ivu-table-wrapper"]//tr[@class="ivu-table-row"]')
    close_ele = (By.XPATH,'//*[@class="button-close"]')
    def repeat(self,value):
        if self.find(*self.stutas_text).text == "完成":
            beforenum = self.finds(*self.history_num)
            print(beforenum)
            self.find_click(*self.repeat_ele)
            self.find_sendkeys(*self.repeat_input_ele,value)
            self.find_click(*self.repeat_confirm)
            sleep(10)
            afternum = self.finds(*self.history_num)
            print(afternum)

            self.find_click(*self.close_ele)
            return int(len(afternum)) - int(len(beforenum))
        else:
            print("該事項狀態已完成，無法重置")
            self.find_click(*self.close_ele)
            return

    def operation_history(self):
        number = len(self.finds(*self.history_num))
        self.find_click(*self.close_ele)
        return number
