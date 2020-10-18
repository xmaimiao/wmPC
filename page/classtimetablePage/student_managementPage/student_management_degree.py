import re
from time import sleep

from common.contants import student_management_degree_dir
from page.basepage import BasePage
from page.classtimetablePage.student_managementPage.degree_course_classmate_s import Degree_Course_Classmate_S


class Student_Management_Degree(BasePage):

    def search_simple(self,keywords_stu_all):
        '''
        查詢學生賬號、學號、姓名，僅輸入關鍵詞
        '''
        self._params["keywords_stu_all"] = keywords_stu_all
        self.step(student_management_degree_dir,"search_simple")
        return self

    def get_choice_value(self):
        '''
        獲取到下拉框的值
        '''
        # self.set_implicitly_wait(20)
        # result = self.step(student_management_degree_dir,"get_choice_value")
        # self.set_implicitly_wait(3)
        sleep(2)
        return self.step(student_management_degree_dir,"get_choice_value").text

    def get_choice_value_not_exist(self):
        '''
        獲取到下拉框的值
        '''
        sleep(2)
        # result = self.step(student_management_degree_dir,"get_choice_value_not_exist")
        return self.step(student_management_degree_dir,"get_choice_value_not_exist").text


    def choice_student(self):
        '''
        1.查詢下拉框，選擇人員
        2.點擊查詢按鈕
        '''
        self.set_implicitly_wait(20)
        self.step(student_management_degree_dir,"choice_student")
        self.set_implicitly_wait(3)
        return self

    def get_current_week_courses_num(self):
        '''
        獲取當前一周科目的總數量
        '''
        sleep(3)
        return self.step(student_management_degree_dir, "get_current_week_courses_num")

    def get_course_bar_teachername(self):
        '''
        獲取課程條上的教師名稱
        '''
        result= self.step(student_management_degree_dir,"get_course_bar_teachername")
        return re.search("[ \t\n]+([^\x00-\xff]+)\s+", result).group(1)

    def get_course_details(self):
        '''
        通過課程條上的教師打開卡片詳情
        '''
        self.step(student_management_degree_dir,"get_course_details")
        return self


    def get_course_details_student_num(self):
        '''
        獲取卡片上的學生總數
        '''
        result = self.step(student_management_degree_dir, "get_course_details_student_num")
        return int(re.search("(\d+)", result).group(1))

    def goto_classmate(self):
        '''
        打開課程-同班同學頁面
        '''
        self.step(student_management_degree_dir, "goto_classmate")
        return Degree_Course_Classmate_S(self._driver)

