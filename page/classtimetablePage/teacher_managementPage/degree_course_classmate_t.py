import re
from time import sleep

from common.contants import degree_course_classmate_t_dir
from page.basepage import BasePage


class Degree_Course_Classmate(BasePage):
    def get_lessontime(self):
        '''
        驗證顯示了授課時間
        '''
        return self.step(degree_course_classmate_t_dir , "get_lessontime")

    def get_lesson_student_num(self):
        '''
        驗證顯示了課程總人數
        '''
        result = self.step(degree_course_classmate_t_dir, "get_lesson_student_num")
        return int(re.search("(\d+)",result).group(1))

    def search_studentname(self,stu_keywords):
        '''
        查詢學生姓名
        '''
        self._params["stu_keywords"] = stu_keywords
        return self.step(degree_course_classmate_t_dir,"search_studentname")

    def search_studentstaffNo(self,stu_keywords):
        '''
        查詢學生學號
        '''
        self._params["stu_keywords"] = stu_keywords
        return self.step(degree_course_classmate_t_dir,"search_studentstaffNo")

    def get_program(self):
        '''
        獲得學生的課程
        '''
        sleep(2)
        return self.step(degree_course_classmate_t_dir, "get_program")

    def back_to_teacher_management_degree(self):
        self.step(degree_course_classmate_t_dir, "back_to_room_management_degree")
        from page.classtimetablePage.teacher_managementPage.teacher_management_degree import Teacher_Management_Degree
        return Teacher_Management_Degree(self._driver)