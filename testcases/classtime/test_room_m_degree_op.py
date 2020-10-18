import os
import sys

from common.contants import  test_room_m_degree_dir

curPath = os.path.abspath(os.path.dirname(__file__))
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(base_dir)
sys.path.append('..')
from page.main import Main
import pytest
import yaml

class TestRoomClassTable:

    with open(test_room_m_degree_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        test_course_type_datas = datas["test_course_type"]
        test_simply_search_course_name_datas = datas["test_simply_search_course_name"]
        test_simply_search_course_code_datas = datas["test_simply_search_course_code"]
        test_simply_search_roomCode_datas = datas["test_simply_search_roomCode"]
        test_advanced_search_teachername_datas = datas["test_advanced_search_teachername"]
        test_advanced_search_room_datas = datas["test_advanced_search_room"]
        test_advanced_search_course_name_datas = datas["test_advanced_search_course_name"]
        test_advanced_search_course_code_datas = datas["test_advanced_search_course_code"]
        test_advanced_search_course_type_datas = datas["test_advanced_search_course_type"]
        test_advanced_search_reset_datas = datas["test_advanced_search_reset"]
        # test_get_H_S_N_course_room_datas = datas["test_get_H_S_N_course_room"]
        # test_get_H_S_N_course_zoom_datas = datas["test_get_H_S_N_course_zoom"]
        # test_get_Z_M_course_room_datas = datas["test_get_Z_M_course_room"]
        test_get_course_details_student_num_datas = datas["test_get_course_details_student_num"]
        test_search_studentname_datas = datas["test_search_studentname"]
        test_search_studentstaffNo_datas = datas["test_search_studentstaffNo"]
        test_get_lessontime_datas = datas["test_get_lessontime"]
        test_get_lesson_student_num_datas = datas["test_get_lesson_student_num"]
        test_back_to_room_management_degree_datas = datas["test_back_to_room_management_degree"]

    # def setup_class(self):
    #     self.main = Main()
    #
    # def teardown_class(self):
    #     self.main.close()

    def setup(self):
        self.main = Main()


    # def teardown(self):
    #     self.main.quit()

    @pytest.mark.parametrize("data", test_course_type_datas)
    def test_course_type(self, data):
        '''
        驗證課堂類型
        :return:
        '''
        result = self.main.\
            goto_room_management_degree(data["memu"]). \
            get_yy_mm_dd(data["year"], data["month"], data["day"]). \
            get_course_details(data["courseCode"],data["classCode"]). \
            get_course_type()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_simply_search_course_name_datas)
    def test_simply_search_course_name(self, data):
        '''
        驗證簡易查詢科目名稱
        :return:
        '''
        result = self.main.\
            goto_room_management_degree(data["memu"]). \
            get_all_facCode(). \
            get_yy_mm_dd(data["year"], data["month"], data["day"]). \
            simply_search(data["keywords_room"]). \
            simply_search_confirm(). \
            get_current_day_courses_num()
        assert result == data["expect"]


    @pytest.mark.parametrize("data", test_simply_search_roomCode_datas)
    def test_simply_search_roomCode(self, data):
        '''
        驗證簡易查詢課室
        :return:
        '''
        result = self.main. \
            goto_room_management_degree(data["memu"]). \
            get_yy_mm_dd(data["year"],data["month"],data["day"]).\
            get_all_facCode(). \
            simply_search(data["keywords_room"]). \
            simply_search_confirm(). \
            get_current_day_courses_num()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_simply_search_course_code_datas)
    def test_simply_search_course_code(self, data):
        '''
        驗證簡易查詢科目編號
        :return:
        '''
        result = self.main. \
            goto_room_management_degree(data["memu"]). \
            get_all_facCode(). \
            get_yy_mm_dd(data["year"],data["month"],data["day"]).\
            simply_search(data["keywords_room"]). \
            simply_search_confirm().\
            get_current_day_courses_num()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_advanced_search_teachername_datas)
    def test_advanced_search_teachername(self, data):
        '''
        驗證高級查詢教師名稱
        :return:
        '''
        result = self.main. \
            goto_room_management_degree(data["memu"]). \
            get_yy_mm_dd(data["year"],data["month"],data["day"]).\
            get_all_facCode(). \
            click_advanced_search(). \
            advanced_search_teachername(data["teachername"]).\
            advanced_search_confirm().\
            get_current_day_courses_num()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_advanced_search_room_datas)
    def test_advanced_search_room(self, data):
        '''
        驗證高級查詢課室
        :return:
        '''
        result = self.main. \
            goto_room_management_degree(data["memu"]). \
            get_yy_mm_dd(data["year"],data["month"],data["day"]).\
            get_all_facCode(). \
            click_advanced_search(). \
            advanced_search_room(data["room"]).\
            advanced_search_confirm().\
            get_current_day_courses_num()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_advanced_search_course_name_datas)
    def test_advanced_search_course_name(self, data):
        '''
        驗證高級查詢科目名稱
        :return:
        '''
        result = self.main. \
            goto_room_management_degree(data["memu"]). \
            get_yy_mm_dd(data["year"],data["month"],data["day"]).\
            get_all_facCode(). \
            click_advanced_search(). \
            advanced_search_course_name(data["course_name"]).\
            advanced_search_confirm().\
            get_current_day_courses_num()
        assert result == data["expect"]    \

    @pytest.mark.parametrize("data", test_advanced_search_course_code_datas)
    def test_advanced_search_course_code(self, data):
        '''
        驗證高級查詢科目編號
        :return:
        '''
        result = self.main. \
            goto_room_management_degree(data["memu"]). \
            get_yy_mm_dd(data["year"],data["month"],data["day"]).\
            get_all_facCode(). \
            click_advanced_search(). \
            advanced_search_course_code(data["course_code"]).\
            advanced_search_confirm().\
            get_current_day_courses_num()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_advanced_search_course_type_datas)
    def test_advanced_search_course_type(self, data):
        '''
        驗證高級查詢科目類型
        :return:
        '''
        result = self.main. \
            goto_room_management_degree(data["memu"]). \
            get_yy_mm_dd(data["year"],data["month"],data["day"]).\
            get_all_facCode(). \
            click_advanced_search(). \
            advanced_search_course_type(data["course_type"]).\
            advanced_search_confirm().\
            get_current_day_courses_num()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_advanced_search_reset_datas)
    def test_advanced_search_reset(self,data):
        '''
        驗證重置按鈕有效
        :return:
        '''
        result = self.main. \
            goto_room_management_degree(data["memu"]). \
            get_yy_mm_dd(data["year"],data["month"],data["day"]).\
            get_all_facCode(). \
            click_advanced_search(). \
            advanced_search_reset().\
            get_current_day_courses_num()
        assert result != data["expect"]


    # @pytest.mark.parametrize("data", test_get_H_S_N_course_room_datas)
    # def test_get_H_S_N_course_room(self, data):
    #     '''
    #     驗證線下課程、混合課程、特俗混合課程的課室顯示正常
    #     :return:
    #     '''
    #     result = self.main. \
    #         goto_room_management_degree(data["memu"]). \
    #         get_yy_mm_dd(data["year"], data["month"], data["day"]). \
    #         get_all_facCode().\
    #         simply_search(data["keywords"]). \
    #         get_course_details(data["week"],data["course_num"]).\
    #         get_H_S_N_course_room()
    #     assert result == data["expect"]

    # @pytest.mark.parametrize("data", test_get_H_S_N_course_zoom_datas)
    # def test_get_H_S_N_course_zoom(self, data):
    #     '''
    #     驗證混合課程、特俗混合課程的雲課堂顯示正常
    #     :return:
    #     '''
    #     result = self.main. \
    #         goto_room_management_degree(data["memu"]). \
    #         get_yy_mm_dd(data["year"], data["month"], data["day"]). \
    #         get_all_facCode().\
    #         simply_search(data["keywords"]). \
    #         get_course_details(data["week"],data["course_num"]).\
    #         get_H_S_N_course_zoom()
    #     assert result == data["expect"]
    #
    # @pytest.mark.parametrize("data", test_get_Z_M_course_room_datas)
    # def test_get_Z_M_course_room(self, data):
    #     '''
    #     驗證雲課堂/網課的url地址顯示正常
    #     :return:
    #     '''
    #     result = self.main. \
    #         goto_room_management_degree(data["memu"]). \
    #         get_yy_mm_dd(data["year"], data["month"], data["day"]). \
    #         get_all_facCode().\
    #         simply_search(data["keywords"]). \
    #         get_course_details(data["week"],data["course_num"]).\
    #         get_Z_M_course_room()
    #     assert result == data["expect"]


    @pytest.mark.parametrize("data", test_get_course_details_student_num_datas)
    def test_get_course_details_student_num(self, data):
        '''
        驗證卡片上學生總數
        :return:
        '''
        result = self.main. \
            goto_room_management_degree(data["memu"]). \
            get_all_facCode(). \
            get_yy_mm_dd(data["year"], data["month"], data["day"]). \
            click_advanced_search(). \
            advanced_search_course_code(data["course_code"]). \
            advanced_search_confirm(). \
            get_course_details(data["courseCode"], data["classCode"]). \
            get_course_details_student_num()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_search_studentname_datas)
    def test_search_studentname(self, data):
        '''
        驗證班級同學頁面查詢姓名正確，必須輸入英文名稱，元素定位寫死了英文名稱
        :return:
        '''
        result = self.main. \
            goto_room_management_degree(data["memu"]). \
            get_all_facCode(). \
            get_yy_mm_dd(data["year"], data["month"], data["day"]). \
            click_advanced_search(). \
            advanced_search_course_code(data["course_code"]). \
            advanced_search_confirm(). \
            get_course_details(data["courseCode"], data["classCode"]). \
            goto_classmate(). \
            search_studentname(data["stu_keywords"])
        assert result == data["expect"]


    @pytest.mark.parametrize("data", test_search_studentstaffNo_datas)
    def test_search_studentstaffNo(self, data):
        '''
        驗證班級同學頁面查詢學號正確
        :return:
        '''
        result = self.main. \
            goto_room_management_degree(data["memu"]). \
            get_all_facCode(). \
            get_yy_mm_dd(data["year"], data["month"], data["day"]). \
            click_advanced_search(). \
            advanced_search_course_code(data["course_code"]). \
            advanced_search_confirm(). \
            get_course_details(data["courseCode"], data["classCode"]). \
            goto_classmate(). \
            search_studentstaffNo(data["stu_keywords"])
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_get_lessontime_datas)
    def test_get_lessontime(self, data):
        '''
        驗證班級同學頁面顯示授課時間
        :return:
        '''
        result = self.main. \
            goto_room_management_degree(data["memu"]). \
            get_all_facCode(). \
            get_yy_mm_dd(data["year"], data["month"], data["day"]). \
            click_advanced_search(). \
            advanced_search_course_code(data["course_code"]). \
            advanced_search_confirm(). \
            get_course_details(data["courseCode"], data["classCode"]). \
            goto_classmate(). \
            get_lessontime()
        assert result[:10] == data["expect"]

    @pytest.mark.parametrize("data", test_get_lesson_student_num_datas)
    def test_get_lesson_student_num(self, data):
        '''
        驗證班級同學頁面顯示人數
        :return:
        '''
        result = self.main. \
            goto_room_management_degree(data["memu"]). \
            get_all_facCode(). \
            get_yy_mm_dd(data["year"], data["month"], data["day"]). \
            click_advanced_search(). \
            advanced_search_course_code(data["course_code"]). \
            advanced_search_confirm(). \
            get_course_details(data["courseCode"], data["classCode"]). \
            goto_classmate(). \
            get_lesson_student_num()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_back_to_room_management_degree_datas)
    def test_back_to_room_management_degree(self, data):
        '''
        驗證班級同學頁面返回上一頁保持進入前頁面不變
        :return:
        '''
        result = self.main. \
            goto_room_management_degree(data["memu"]). \
            get_all_facCode(). \
            get_yy_mm_dd(data["year"], data["month"], data["day"]). \
            click_advanced_search(). \
            advanced_search_course_code(data["course_code"]). \
            advanced_search_confirm(). \
            get_course_details(data["courseCode"], data["classCode"]). \
            goto_classmate(). \
            back_to_room_management_degree().\
            get_current_day_courses_num()
        assert result == data["expect"]

