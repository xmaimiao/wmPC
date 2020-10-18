import re
from time import sleep

from common.contants import room_management_degree_dir
from page.basepage import BasePage
from page.classtimetablePage.room_managementPage.degree_course_classmate_r import Degree_Course_Classmate_R


class Room_Management_Degree(BasePage):

    def get_all_facCode(self):
        '''
        獲取所有教學單位課程
        '''
        self.step(room_management_degree_dir,"get_all_facCode")
        return self


    def simply_search(self,keywords_room):
        '''
        簡易查詢課程課室、科目名稱（中英）、科目編碼
        '''
        self._params["keywords_room"] = keywords_room
        self.step(room_management_degree_dir, "simply_search")
        return self

    def simply_search_confirm(self):
        '''
        簡易查詢點擊確認
        '''
        sleep(3)
        self.step(room_management_degree_dir, "simply_search_confirm")
        return self

    def get_yy_mm_dd(self,year,month,day):
        '''
        定位具體年月日,僅適用中文版
        '''
        self._params["year"] = year
        self._params["month"] = month
        self._params["day"] = day
        self.step(room_management_degree_dir, "get_yy_mm_dd")
        return self

    def click_advanced_search(self):
        '''
        打開高級查詢
        '''
        self.step(room_management_degree_dir, "click_advanced_search")
        return self

    def advanced_search_teachername(self,teachername):
        '''
        高級查詢教師名稱
        '''
        self._params["teachername"] = teachername
        self.step(room_management_degree_dir,"advanced_search_teachername")
        return self

    def advanced_search_username(self,tusername):
        '''
        高級查詢教師賬號
        '''
        self._params["tusername"] = tusername
        self.step(room_management_degree_dir,"advanced_search_username")
        return self

    def advanced_search_room(self,room):
        '''
        高級查詢課室
        '''
        self._params["room"] = room
        self.step(room_management_degree_dir,"advanced_search_room")
        return self

    def advanced_search_course_name(self,course_name):
        '''
        高級查詢科目名稱
        '''
        self._params["course_name"] = course_name
        self.step(room_management_degree_dir,"advanced_search_course_name")
        return self


    def advanced_search_course_code(self,course_code):
        '''
        高級查詢科目編號
        '''
        self._params["course_code"] = course_code
        self.step(room_management_degree_dir,"advanced_search_course_code")
        return self

    def advanced_search_course_type(self,course_type):
        '''
        高級查詢科目類型
        '''
        self._params["course_type"] = course_type
        self.step(room_management_degree_dir,"advanced_search_course_type")
        return self

    def search_term(self):
        pass

    def advanced_search_confirm(self):
        '''
        高級查詢-確定按鈕
        '''
        # sleep(2)
        sleep(4)
        self.step(room_management_degree_dir,"advanced_search_confirm")
        return self

    def advanced_search_reset(self):
        '''
        高級查詢-重置按鈕
        '''
        sleep(2)
        self.step(room_management_degree_dir,"advanced_search_reset")
        return self

    def get_current_day_courses_num(self):
        '''
        獲取當前日期科目的總數量
        '''
        sleep(3)
        return self.step(room_management_degree_dir,"get_current_day_courses_num")

    def get_course_details(self,courseCode,classCode):
        '''
        通過科目編號 和 班別 定位某節課，
        打開某節課卡片詳情
        '''
        self._params["courseCode"] = courseCode
        self._params["classCode"] = classCode
        sleep(2)
        self.step(room_management_degree_dir,"get_course_details")
        return self

    def get_course_type(self):
        '''
        通過科目編號 和 班別 定位某節課，獲得課程類型
        '''
        self.set_implicitly_wait(5)
        return self.step(room_management_degree_dir,"get_course_type")


    # def get_H_S_N_course_room(self):
    #     '''
    #     獲得線下課程/特殊混合課程/混合課程的具體課室
    #     參數num:第1節課對應num=0，第2節課對應num=1
    #     '''
    #     return self.step(room_management_degree_dir,"get_H_S_N_course_room")
    #
    # def get_H_S_N_course_zoom(self):
    #     '''
    #     獲得特殊混合課程/混合課程的雲課室地址
    #     參數num:第1節課對應num=0，第2節課對應num=1
    #     '''
    #     return self.step(room_management_degree_dir,"get_H_S_N_course_zoom")

    # def get_Z_M_course_room(self):
    #     '''
    #     獲得雲課堂/網課的url地址
    #     參數num:第1節課對應num=0，第2節課對應num=1
    #     '''
    #     return self.step(room_management_degree_dir,"get_Z_M_course_room")

    def get_course_details_student_num(self):
        '''
        獲取卡片上的學生總數
        '''
        result = self.step(room_management_degree_dir,"get_course_details_student_num")
        return int(re.search("(\d+)",result).group(1))

    def goto_classmate(self):
        '''
        打開課程-同班同學頁面
        '''
        self.step(room_management_degree_dir,"goto_classmate")
        return Degree_Course_Classmate_R(self._driver)



