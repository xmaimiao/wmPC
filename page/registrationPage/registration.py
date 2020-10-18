from selenium.webdriver.common.by import By

from page.basepage import BasePage
from page.registrationPage.progressPage.progresspage import Progress
from page.registrationPage.newstulistPage.newstulistpage import NewStuLsit


class Registration(BasePage):
    newstulist_ele = (By.XPATH,'//*[@class="we-sider-menu app-sider-menu"]/*[1]')
    progress_ele = (By.XPATH,'//*[@class="we-sider-menu app-sider-menu"]/*[2]')
    insurance_ele = (By.XPATH, '//*[@class="we-sider-menu app-sider-menu"]/*[3]')
    def goto_newstulist(self):

        if len(self.finds(*self.newstulist_ele)):
            self.find_click(*self.newstulist_ele)
            return NewStuLsit(self._driver)
        return False

    def goto_progress(self):
        if self.find_click(*self.progress_ele):
            return Progress(self._driver)
        return False

    # def goto_groupinsurance(self):
    #     if self.find_click(*self.progress_ele):
    #         return GroupInsurance(self._driver)
    #     return False


    # def goto_postadminsettings(self):
    #     return PostAdminSettings(self.driver)
    #
    # def goto_underadminsettings(self):
    #     return UnderAdminSettings(self.driver)
    #
    # def goto_registrationplan(self):
    #     return RegistrationPlan(self.driver)
    #
    # def goto_insurancestatement(self):
    #     return InsuranceStatement(self.driver)