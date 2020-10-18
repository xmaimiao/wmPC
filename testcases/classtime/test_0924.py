import os
import sys


# curPath = os.path.abspath(os.path.dirname(__file__))
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_dir)
# sys.path.append('..')
print(sys.path)
from common.contants import test_0924_dir
from page.main import Main
import pytest
import yaml


class Test0924:
    with open(test_0924_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        setup_datas = datas["setup_datas"]
        test_get_program_datas = datas["test_get_program"]
        test_get_Z_M_course_teachername_datas = datas["test_get_Z_M_course_teachername"]
        test_doctor_in_records_datas = datas["test_doctor_in_records"]
        test_search_student_username_is_exist_datas = datas["test_search_student_username_is_exist"]
        test_search_student_username_not_exist_datas = datas["test_search_student_username_not_exist"]

    def setup_class(self):
        '''
        非調試端口用
        '''
        self.main = Main().goto_login(). \
            username(self.setup_datas["username"]).password(self.setup_datas["password"]).save(). \
            goto_application(). \
            goto_classtimetable(self.setup_datas["application"])

    def teardown_class(self):
        '''
        非調試端口啓用
        '''
        self.main.close()

    # def setup(self):
    #     '''
    #     開啓調試端口啓用
    #     '''
    #     self.main = Main()

    @pytest.mark.skip
    @pytest.mark.parametrize("data", test_get_program_datas)
    def test_get_program(self, data):
        '''
        bug26623 驗證班級同學頁面課程字段顯示正確
        '''
        result = self.main. \
            goto_teacher_management_degree(data["memu"]). \
            get_yy_mm_dd(data["year"], data["month"], data["day"]). \
            get_course_details(data["week"], data["course_num"]). \
            goto_classmate(). \
            get_program()
        assert result == data["expect"]

    @pytest.mark.skip
    @pytest.mark.parametrize("data", test_get_Z_M_course_teachername_datas)
    def test_get_Z_M_teachername(self, data):
        '''
        bug26651 驗證教師課表顯示多個老師
        '''
        result = self.main. \
            goto_teacher_management_degree(data["memu"]). \
            get_yy_mm_dd(data["year"], data["month"], data["day"]). \
            get_all_facCode(). \
            click_advanced_search(). \
            advanced_search_course_type(data["course_type"]). \
            advanced_search_confirm(). \
            get_course_details(data["week"], data["course_num"]). \
            get_Z_M_course_teachername()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_doctor_in_records_datas)
    def test_doctor_in_records(self, data):
        '''
        bug26651 驗證教師課表顯示多個老師
        '''
        result = self.main. \
            goto_postgraduate_sign_in_record(data["memu"]). \
            search_simple(data["keywords"]). \
            serach_simple_records()
        print(sys.path)
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_search_student_username_is_exist_datas)
    def test_search_student_username_is_exist(self, data):
        '''
        bug26592驗證查詢學生賬號，本科生存在
        :return:
        '''
        result = self.main. \
            goto_student_management_degree(data["memu"]). \
            search_simple(data["keywords_stu_all"]). \
            get_choice_value(data["expect"])
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_search_student_username_not_exist_datas)
    def test_search_student_username_not_exist(self, data):
        '''
        bug26592驗證查詢學生賬號,研究生不存在
        :return:
        '''
        result = self.main. \
            goto_student_management_degree(data["memu"]). \
            search_simple(data["keywords_stu_all"]). \
            get_choice_value_not_exist()
        assert result == data["expect"]
