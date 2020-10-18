from page.basepage import BasePage
from page.leavepage.application_for_leave import Application_For_Leaver


class LeavePage(BasePage):

    def goto_application_for_leaver(self):
        '''
        打開申請休假頁面
        '''
        self.step()
        return Application_For_Leaver(self._driver)