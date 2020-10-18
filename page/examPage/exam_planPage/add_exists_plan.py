from time import sleep

import win32con
import win32gui
from selenium.common.exceptions import NoSuchElementException

from common.contants import add_exists_plan_dir
from page.basepage import BasePage


class Add_Exists_Plan(BasePage):
    def plan_name(self,plan_name):
        '''
        输入计划名称
        '''
        self._params["plan_name"] = plan_name
        self.step(add_exists_plan_dir,"plan_name")
        return self

    def term(self):
        '''
        选择学期
        '''
        self.step(add_exists_plan_dir,"term")
        return self

    def upload_exists_plan_import(self,excel_path):
        '''
        上传附件
        '''
        self._params["excel_path"] = excel_path
        self.step(add_exists_plan_dir,"upload_exists_plan_import")
        sleep(2)
        # 找元素
        # 一级窗口"#32770","打开"
        dialog = win32gui.FindWindow("#32770", "打开")
        # 向下传递
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        # 编辑按钮
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
        # 打开按钮
        button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 二级

        # 输入文件的绝对路径，点击“打开”按钮
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, excel_path)  # 发送文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
        return self

    def check_upload_result(self):
        '''
        检查上传结果,判断“請通過校驗後提交”是否存在页面中，存在返回Ture，不存在返回False
        '''
        return self.step(add_exists_plan_dir,"check_upload_result")

    def download_result(self):
        '''
        下載錯誤文件
        '''
        try:
            self.step(add_exists_plan_dir,"download_result").click()
            return self
        except NoSuchElementException as e:
            return self


