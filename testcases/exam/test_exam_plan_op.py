import os
import sys

from common.contants import test_exam_plan_dir

curPath = os.path.abspath(os.path.dirname(__file__))
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(base_dir)
sys.path.append('..')
from page.main import Main
import pytest
import yaml


class Test_Exam_Plan:
    with open(test_exam_plan_dir, encoding="utf-8") as f:

        datas = yaml.safe_load(f)
        setup_datas = datas["setup_datas"]
        test_check_upload_exists_plan_datas = datas["test_check_upload_exists_plan"]

    def setup_class(self):
        '''
        非調試端口用
        '''
        self.main = Main().goto_login(). \
            username(self.setup_datas["username"]).password(self.setup_datas["password"]).save(). \
            goto_application(). \
            goto_exam(self.setup_datas["application"])

    def teardown_class(self):
        '''
        非調試端口啓用
        '''
        # self.main.close()
        pass

    # def setup(self):
    #     '''
    #     開啓調試端口啓用
    #     '''
    #     self.main = Main()

    @pytest.mark.parametrize("data", test_check_upload_exists_plan_datas)
    def test_check_upload_exists_plan(self, data):
        '''
        验证上传已排计划
        '''

        result = self.main.goto_exam_plan().\
            add_exists_plan().\
            plan_name(data["plan_name"]).term().\
            upload_exists_plan_import(data["excel_path"]).\
            download_result().\
            check_upload_result()
        assert result == data["expect"]

