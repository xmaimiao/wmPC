from selenium.webdriver.common.by import By

from page.basepage import BasePage
from page.classtimetablePage.undergraduate_recordsPage.absentpage import Absent
from page.classtimetablePage.undergraduate_recordsPage.suppsignIn import SuppSignIn


class SignRecordDetail(BasePage):
    search_input_ele = (By.XPATH, '//*[@class="content"]/div[3]//input')
    search_click_ele = (By.XPATH, '//*[@class="ivu-icon ivu-icon-ios-search"]')
    firstsign_in_ele = (By.XPATH, '//tbody[@class="ivu-table-tbody"]/tr[1]/td[6]//p[1]')
    firstsign_in_day_ele = (By.XPATH, '//tbody[@class="ivu-table-tbody"]/tr[1]/td[6]//p[2]')
    firstsign_in_time_ele = (By.XPATH, '//tbody[@class="ivu-table-tbody"]/tr[1]/td[6]//p[3]')
    secondsign_in_ele = (By.XPATH, '//tbody[@class="ivu-table-tbody"]/tr[1]/td[7]//p[1]')
    secondsign_in_day_ele = (By.XPATH, '//tbody[@class="ivu-table-tbody"]/tr[1]/td[7]//p[2]')
    secondsign_in_time_ele = (By.XPATH, '//tbody[@class="ivu-table-tbody"]/tr[1]/td[7]//p[3]')
    signstatus_in_ele = (By.XPATH, '//tbody[@class="ivu-table-tbody"]/tr[1]/td[8]//p[1]')
    item_name1_ele = (By.XPATH, '//tbody[@class="ivu-table-tbody"]/tr[1]/td[9]//p[1]')
    item_value1_ele = (By.XPATH, '//tbody[@class="ivu-table-tbody"]/tr[1]/td[9]//p[2]')
    item_name2_ele = (By.XPATH, '//tbody[@class="ivu-table-tbody"]/tr[1]/td[9]//p[3]')
    item_value2_ele = (By.XPATH, '//tbody[@class="ivu-table-tbody"]/tr[1]/td[9]//p[4]')
    supp_signin_ele = (By.XPATH, '//tbody[@class="ivu-table-tbody"]/tr[1]/td[last()]//p[1]')
    absent_ele = (By.XPATH, '//tbody[@class="ivu-table-tbody"]/tr[1]/td[last()]//p[2]')


    def simple_search(self,stafNo):
        '''
        通過查詢學號找到該學生最新得簽到數據
        :param value:
        :return:
        '''
        self.find_sendkeys(*self.search_input_ele, stafNo)
        self.find_click(*self.search_click_ele)
        return self

    def simple_search_result_firstrecords_firstsign(self,staffNo):
        '''
        1.簡易查詢，2.定位第一條記錄為最新簽到，3.定位首簽——>未簽？補簽？已簽？
        :return:
        '''
        firstsign_staffNo_ele = (By.XPATH,
                                 '//tbody[@class="ivu-table-tbody"]/tr[1]/td[4]//span[contains(text(),'
                                 f'"{staffNo}")]')
        self.wait_for_display(firstsign_staffNo_ele)
        result = self.find(*self.firstsign_in_ele).text
        return result

    def simple_search_result_firstrecords_firstsign_day(self,staffNo):
        '''
        1.簡易查詢，2.定位第一條記錄為最新簽到，3.定位首簽日期——>判斷非當天簽到 or 當天簽到
        :return:
        '''
        firstsign_staffNo_ele = (By.XPATH,
                                 '//tbody[@class="ivu-table-tbody"]/tr[1]/td[4]//span[contains(text(),'
                                 f'"{staffNo}")]')
        self.wait_for_display(firstsign_staffNo_ele)
        result = self.find(*self.firstsign_in_day_ele).text
        return result

    def simple_search_result_firstrecords_firstsign_time(self,staffNo):
        '''
        1.簡易查詢，2.定位第一條記錄為最新簽到，3.定位首簽時間
        :return:
        '''
        firstsign_staffNo_ele = (By.XPATH,
                                 '//tbody[@class="ivu-table-tbody"]/tr[1]/td[4]//span[contains(text(),'
                                 f'"{staffNo}")]')
        self.wait_for_display(firstsign_staffNo_ele)
        result = self.find(*self.firstsign_in_time_ele).text
        return result

    def simple_search_result_firstrecords_secondsign(self,staffNo):
        '''
        1.簡易查詢，2.定位第一條記錄為最新簽到，3.定位次簽——>未簽？補簽？已簽？
        :return:
        '''
        firstsign_staffNo_ele = (By.XPATH,
                                 '//tbody[@class="ivu-table-tbody"]/tr[1]/td[4]//span[contains(text(),'
                                 f'"{staffNo}")]')
        self.wait_for_display(firstsign_staffNo_ele)
        result = self.find(*self.secondsign_in_ele).text
        return result

    def simple_search_result_firstrecords_secondsign_day(self,staffNo):
        '''
        1.簡易查詢，2.定位第一條記錄為最新簽到，3.定位首簽日期——>判斷非當天簽到 or 當天簽到
        :return:
        '''
        firstsign_staffNo_ele = (By.XPATH,
                                 '//tbody[@class="ivu-table-tbody"]/tr[1]/td[4]//span[contains(text(),'
                                 f'"{staffNo}")]')
        self.wait_for_display(firstsign_staffNo_ele)
        result = self.find(*self.secondsign_in_day_ele).text
        return result

    def simple_search_result_firstrecords_secondsign_time(self,staffNo):
        '''
        1.簡易查詢，2.定位第一條記錄為最新簽到，3.定位次簽時間
        :return:
        '''
        firstsign_staffNo_ele = (By.XPATH,
                                 '//tbody[@class="ivu-table-tbody"]/tr[1]/td[4]//span[contains(text(),'
                                 f'"{staffNo}")]')
        self.wait_for_display(firstsign_staffNo_ele)
        result = self.find(*self.secondsign_in_time_ele).text
        return result

    def simple_search_result_firstrecords_signstatus(self,staffNo):
        '''
        1.簡易查詢，2.定位第一條記錄為最新簽到，3.定位簽到情況
        :return:
        '''
        firstsign_staffNo_ele = (By.XPATH,
                                 '//tbody[@class="ivu-table-tbody"]/tr[1]/td[4]//span[contains(text(),'
                                 f'"{staffNo}")]')
        self.wait_for_display(firstsign_staffNo_ele)
        result = self.find(*self.signstatus_in_ele).text
        return result

    def simple_search_result_firstrecords_remark_item_name1(self,staffNo):
        '''
        1.簡易查詢，2.定位第一條記錄為最新簽到，3.定位備注item——>
        判斷一次性首次簽：首簽/次簽，非一次性：首簽、次簽分開
        此為定位第一個item
        :return:
        '''
        firstsign_staffNo_ele = (By.XPATH,
                                 '//tbody[@class="ivu-table-tbody"]/tr[1]/td[4]//span[contains(text(),'
                                 f'"{staffNo}")]')
        self.wait_for_display(firstsign_staffNo_ele)
        result = self.find(*self.item_name1_ele).text
        return result

    def simple_search_result_firstrecords_remark_item_value1(self,staffNo):
        '''
        1.簡易查詢，2.定位第一條記錄為最新簽到，3.定位備注文案——>
        判斷一次性首次簽：首簽/次簽説明合一快，非一次性：首簽、次簽説明分開
        此為定位第一個説明
        :return:
        '''
        firstsign_staffNo_ele = (By.XPATH,
                                 '//tbody[@class="ivu-table-tbody"]/tr[1]/td[4]//span[contains(text(),'
                                 f'"{staffNo}")]')
        self.wait_for_display(firstsign_staffNo_ele)
        result = self.find(*self.item_value2_ele).text
        return result

    def simple_search_result_firstrecords_remark_item_name2(self,staffNo):
        '''
        1.簡易查詢，2.定位第一條記錄為最新簽到，3.定位備注item——>
        判斷一次性首次簽：首簽/次簽，非一次性：首簽、次簽分開
        此為定位第二個item
        :return:
        '''
        firstsign_staffNo_ele = (By.XPATH,
                                 '//tbody[@class="ivu-table-tbody"]/tr[1]/td[4]//span[contains(text(),'
                                 f'"{staffNo}")]')
        self.wait_for_display(firstsign_staffNo_ele)
        result = self.find(*self.item_name2_ele).text
        return result

    def simple_search_result_firstrecords_remark_item_value2(self,staffNo):
        '''
        1.簡易查詢，2.定位第一條記錄為最新簽到，3.定位備注item——>
        判斷一次性首次簽：首簽/次簽，非一次性：首簽、次簽分開
        此為定位第二個説明
        :return:
        '''
        firstsign_staffNo_ele = (By.XPATH,
                                 '//tbody[@class="ivu-table-tbody"]/tr[1]/td[4]//span[contains(text(),'
                                 f'"{staffNo}")]')
        self.wait_for_display(firstsign_staffNo_ele)
        result = self.find(*self.item_value2_ele).text
        return result

    def simple_search_result_firstrecords_goto_supp_signin(self,staffNo):
        '''
        1.簡易查詢，2.定位第一條記錄為最新簽到，3.定位“補簽”按鈕
        :return:
        '''
        firstsign_staffNo_ele = (By.XPATH,
                                 '//tbody[@class="ivu-table-tbody"]/tr[1]/td[4]//span[contains(text(),'
                                 f'"{staffNo}")]')
        self.wait_for_display(firstsign_staffNo_ele)
        result = self.find_click(*self.supp_signin_ele)
        return SuppSignIn(self._driver)

    def simple_search_result_firstrecords_goto_absent(self,staffNo):
        '''
        1.簡易查詢，2.定位第一條記錄為最新簽到，3.定位“缺席”按鈕
        :return:
        '''
        firstsign_staffNo_ele = (By.XPATH,
                                 '//tbody[@class="ivu-table-tbody"]/tr[1]/td[4]//span[contains(text(),'
                                 f'"{staffNo}")]')
        self.wait_for_display(firstsign_staffNo_ele)
        result = self.find_click(*self.absent_ele)
        return Absent(self._driver)
