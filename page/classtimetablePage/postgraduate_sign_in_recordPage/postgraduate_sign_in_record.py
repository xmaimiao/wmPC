from time import sleep

from common.contants import postgraduate_sign_in_record_dir
from page.basepage import BasePage


class Postgraduate_Sign_In_Record(BasePage):

    def search_simple(self,keywords):
        '''
        簡易查詢科目編號
        '''
        self._params["keywords"] = keywords
        self.step(postgraduate_sign_in_record_dir,"search_simple")
        return self

    def serach_simple_records(self):
        '''
        簡易查詢，當前頁面的記錄總數
        '''
        sleep(4)
        return self.step(postgraduate_sign_in_record_dir,"serach_simple_records").text
