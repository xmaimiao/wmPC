from common.contants import classtimetable_dir, exampage_dir
from page.basepage import BasePage
from page.index import Index
from page.loginpage import Login
from page.registrationPage.registration import Registration


class Main(BasePage):
    '''
    首頁面po
    '''
    # _base_url = "http://wmstaff-entry.doocom.net/home"
    # _base_url = "https://oa.must.edu.mo/home/"
    _base_url = "https://oa-wmtest.must.edu.mo:10443/home/"

    def goto_login(self):
        '''
        進去登錄頁面
        :return:
        '''
        return Login(self._driver)

    def goto_index(self):
        '''
        打開首頁
        :return:
        '''
        return Index(self._driver)


    def goto_registration(self):
        '''
        復用瀏覽器，直接在入學應用裏測試
        :return:
        '''
        return Registration(self._driver)

    def goto_teacher_management_degree(self,memu):
        '''
        測試入口，打開教師課表（管理端-本科生）
        '''
        self._params["memu"] = memu
        self.set_implicitly_wait(5)
        self.step(classtimetable_dir, "goto_teacher_management_degree")
        from page.classtimetablePage.teacher_managementPage.teacher_management_degree import Teacher_Management_Degree
        return Teacher_Management_Degree(self._driver)

    def goto_student_management_degree(self,memu):
        '''
        測試入口，打開學生課表（管理端-本科生）
        '''
        self._params["memu"] = memu
        self.set_implicitly_wait(5)
        self.step(classtimetable_dir, "goto_student_management_degree")
        from page.classtimetablePage.student_managementPage.student_management_degree import Student_Management_Degree
        return Student_Management_Degree(self._driver)

    def goto_room_management_degree(self,memu):
        '''
        測試入口，打開課室課表（管理端-本科生）
        '''
        self._params["memu"] = memu
        self.set_implicitly_wait(5)
        self.step(classtimetable_dir, "goto_room_management_degree")
        from page.classtimetablePage.room_managementPage.room_management_degree import Room_Management_Degree
        return Room_Management_Degree(self._driver)

    def goto_postgraduate_sign_in_record(self,memu):
        '''
        測試入口，打開研究生簽到記錄
        '''
        self._params["memu"] = memu
        self.set_implicitly_wait(5)
        self.step(classtimetable_dir, "goto_postgraduate_sign_in_record")
        from page.classtimetablePage.postgraduate_sign_in_recordPage.postgraduate_sign_in_record import \
            Postgraduate_Sign_In_Record
        return Postgraduate_Sign_In_Record(self._driver)

    def goto_exam_plan(self):
        '''
        測試入口，打開考試
        '''
        self.set_implicitly_wait(5)
        self.step(exampage_dir,"goto_exam_plan")
        from page.examPage.exam_planPage.exam_plan import Exam_Plan
        return Exam_Plan(self._driver)
