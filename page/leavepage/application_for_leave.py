from page.basepage import BasePage


class Application_For_Leaver(BasePage):

    def send_mobile_no(self):
        '''
        填写电话号码
        '''
        self.step()
        return self

    def choice_leave_type(self):
        '''
        选择假期类型
        '''
        self.step()
        return self

    def choice_over_a_day(self):
        '''
        选择超过一天模式,并输入开始-结束日期
        '''
        self.step()
        return self

    def choice_date(self):
        '''
        默认仅一天模式，输入日期
        '''
        self.step()
        return self

    def remarks(self):
        '''
        输入备注
        '''
        self.step()
        return self

    def upload_attachment(self):
        '''
        上传附件
        '''
        pass

    def cleck_save(self):
        self.step()
        return