from page.basepage import BasePage
from page.classtimetablePage.teacher_managementPage.master_course_classmate_t import Master_Course_Classmate


class Teacher_Management_Master(BasePage):

    def simply_search(self,keywords):
        '''
        簡易查詢課程名稱、教師名稱、賬號
        '''
        self._params["keywords"] = keywords

        return self

    def advanced_search_teacher(self,teacher):
        '''
        高級查詢教師名稱
        '''
        self._params["teacher"] = teacher
        self.step("../data/classtimetablepage/teacher_managementPage/teacher_management_degree.yaml",
                  "search_teacher")
        return self

    def advanced_search_room(self,room):
        '''
        高級查詢課室
        '''
        self._params["room"] = room
        self.step("../data/classtimetablepage/teacher_managementPage/teacher_management_degree.yaml",
                  "search_room")
        return self

    def advanced_search_course(self,room):
        '''
        高級查詢科目名稱
        '''
        self._params["room"] = room
        self.step("../data/classtimetablepage/teacher_managementPage/teacher_management_degree.yaml",
                  "search_room")
        return self

    def advanced_search_course_code(self,room):
        '''
        高級查詢科目編號
        '''
        self._params["room"] = room
        self.step("../data/classtimetablepage/teacher_managementPage/teacher_management_degree.yaml",
                  "search_room")
        return self

    def advanced_search_course_type(self,room):
        '''
        高級查詢科目類型
        '''
        self._params["room"] = room
        self.step("../data/classtimetablepage/teacher_managementPage/teacher_management_degree.yaml",
                  "search_room")
        return self

    def search_term(self):
        pass

    def search_confirm(self):
        '''
        高級查詢-確定按鈕
        '''
        self.step("../data/classtimetablepage/teacher_managementPage/teacher_management_degree.yaml",
                  "search_confirm")
        return self

    def get_current_week_courses_num(self):
        '''
        獲取當前一周科目的總數量
        '''
        return self.step()

    def get_course_type(self,num):
        '''
        獲得所有課程類型
        參數num:第1節課對應num=0，第2節課對應num=1
        '''
        self._params["num"] = num
        return self.step("../data/classtimetablepage/teacher_managementPage/teacher_management_degree.yaml",
                  "course_type")

    def get_H_S_N_course_room(self,num):
        '''
        獲得線下課程/特殊混合課程/混合課程的具體課室
        參數num:第1節課對應num=0，第2節課對應num=1
        '''
        return self.step("../data/classtimetablepage/teacher_managementPage/teacher_management_degree.yaml",
                  "course_type")

    def get_H_S_N_course_zoom(self):
        '''
        獲得線下課程/特殊混合課程/混合課程的雲課室地址
        參數num:第1節課對應num=0，第2節課對應num=1
        '''
        return self.step("../data/classtimetablepage/teacher_managementPage/teacher_management_degree.yaml",
                  "course_type")

    def get_Z_M_course_room(self):
        '''
        獲得雲課堂/網課的url地址
        參數num:第1節課對應num=0，第2節課對應num=1
        '''
        return self.step("../data/classtimetablepage/teacher_managementPage/teacher_management_degree.yaml",
                  "course_type")

    def get_course_details(self,week,num):
        '''
        1.簡易查詢課程或不通過搜索，
        2.由參數week定位周几，
        3.由參數num定位周M第N節課,num=2定位第一節課
        4.打開這節課卡片詳情
        '''
        self._params["week"] = week
        self._params["num"] = num
        self.step("../data/classtimetablepage/teacher_managementPage/teacher_management_degree.yaml",
                  "course_details")
        return self

    def goto_classmate(self):
        '''
        打開課程-同班同學頁面
        '''
        self.step()
        return Master_Course_Classmate(self._driver)