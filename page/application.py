from common.contants import application_dir
from page.basepage import BasePage
from page.classtimetablePage.classtimetable import ClassTimeTable
from page.examPage.exampage import ExamPage
from page.registrationPage.registration import Registration


class Application(BasePage):

    def goto_registration(self,application_name):
        '''
        進入入學應用
        '''
        # self._params["application_name"] = application_name
        # self.step("../data/application.yaml","goto_registration")
        # self.wait_for_display((By.LINK_TEXT,application_name))
        # self.find_click(By.LINK_TEXT,application_name)
        return Registration(self._driver)

    def goto_classtimetable(self, application):
        '''
        進入課表應用
        '''
        self._params["application"] = application
        self.step(application_dir, "goto_classtimetable")
        return ClassTimeTable(self._driver)

    def goto_exam(self, application):
        '''
        進入考试應用
        '''
        self._params["application"] = application
        self.step(application_dir, "goto_exam")
        return ExamPage(self._driver)


