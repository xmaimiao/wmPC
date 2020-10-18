from common.contants import classtimetable_dir
from page.basepage import BasePage
from page.classtimetablePage.postgraduate_sign_in_recordPage.postgraduate_sign_in_record import \
    Postgraduate_Sign_In_Record
from page.classtimetablePage.room_managementPage.room_management_degree import Room_Management_Degree
from page.classtimetablePage.student_managementPage.student_management_degree import Student_Management_Degree
from page.classtimetablePage.teacher_managementPage.teacher_management_degree import Teacher_Management_Degree
from page.classtimetablePage.teacher_managementPage.teacher_management_master import Teacher_Management_Master
from page.classtimetablePage.undergraduate_recordsPage.Undergraduate_record import UnderGraduteRecord



class ClassTimeTable(BasePage):

    def goto_undergradute_record(self,memu):
        '''
        打開對應的菜單
        '''
        # memu_ele = (By.XPATH, f'//div[@class="we-sider-menu app-sider-menu"]//span[contains(text(),"{memu}")]')
        # self.wait_for_display(memu_ele)
        # self.find_click(*memu_ele)
        self._params["memu"] = memu
        self.set_implicitly_wait(3)
        self.step(classtimetable_dir,"goto_undergradute_record")
        return UnderGraduteRecord(self._driver)

    def goto_teacher_management_degree(self,memu):
        '''
        打開教師課表（管理端-本科生）
        '''
        self._params["memu"] = memu
        self.set_implicitly_wait(5)
        self.step(classtimetable_dir, "goto_teacher_management_degree")
        return Teacher_Management_Degree(self._driver)

    def goto_teacher_management_master(self,memu):
        '''
        打開教師課表（管理端-研究生）
        '''
        self._params["memu"] = memu
        self.set_implicitly_wait(3)
        self.step(classtimetable_dir, "goto_teacher_management_master")
        return Teacher_Management_Master(self._driver)

    def goto_room_management_degree(self,memu):
        '''
        打開課室課表（管理端-本科生）
        '''
        self._params["memu"] = memu
        self.set_implicitly_wait(3)
        self.step(classtimetable_dir, "goto_room_management_degree")
        return Room_Management_Degree(self._driver)

    def goto_room_management_master(self,memu):
        '''
        打開課室課表（管理端-研究生）
        '''
        self._params["memu"] = memu
        self.set_implicitly_wait(3)
        self.step(classtimetable_dir, "goto_room_management_master")
        return Room_Management_Master(self._driver)

    def goto_student_management_degree(self,memu):
        '''
        打開學生課表（管理端-本科生）
        '''
        self._params["memu"] = memu
        self.set_implicitly_wait(3)
        self.step(classtimetable_dir, "goto_student_management_degree")
        return Student_Management_Degree(self._driver)

    def goto_student_management_master(self,memu):
        '''
        打開學生課表（管理端-研究生）
        '''
        self._params["memu"] = memu
        self.set_implicitly_wait(3)
        self.step(classtimetable_dir, "goto_student_management_master")
        return Student_Management_Master(self._driver)

    def goto_postgraduate_sign_in_record(self,memu):
        '''
        測試入口，打開研究生簽到記錄
        '''
        self._params["memu"] = memu
        self.set_implicitly_wait(3)
        self.step(classtimetable_dir, "goto_postgraduate_sign_in_record")
        return Postgraduate_Sign_In_Record(self._driver)