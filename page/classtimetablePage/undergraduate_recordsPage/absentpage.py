from time import sleep

from selenium.webdriver.common.by import By

from page.basepage import BasePage


class Absent(BasePage):
    remark_ele = (By.XPATH,'//textarea[@class="ivu-input"]')
    save_ele = (By.XPATH, '//button[@class="we w-100 h-40 m-10 ivu-btn ivu-btn-primary"]/span')

    def absent(self, remark):
        # 填寫缺席説明
        self.finds(*self.remark_ele)[1].send_keys(remark)
        # 點擊確認
        self.finds(*self.save_ele)[1].click()
        sleep(1)
        from page.classtimetablePage.undergraduate_recordsPage.signrecorddetailpage import SignRecordDetail
        return SignRecordDetail(self._driver)
