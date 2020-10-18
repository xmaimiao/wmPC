from common.contants import exam_plan_dir
from page.basepage import BasePage
from page.examPage.exam_planPage.add_exists_plan import Add_Exists_Plan


class Exam_Plan(BasePage):
    def add_exists_plan(self):
        '''
        添加已排计划
        '''
        self.step(exam_plan_dir,"add_exists_plan")
        return Add_Exists_Plan(self._driver)