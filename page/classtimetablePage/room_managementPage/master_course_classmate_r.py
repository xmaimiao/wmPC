from page.basepage import BasePage


class Master_Course_Classmate_R(BasePage):
    def get_lessontime(self):
        '''
        驗證顯示了授課時間
        '''
        return self.step()

    def get_lesson_student_num(self):
        '''
        驗證顯示了課程總人數
        '''
        return self.step()

    def back_to_room_management_master(self):
        '''
        返回上一路徑
        '''
        self.step()
        return Room_Management_Master(self._driver)