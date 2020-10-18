import pytest
import yaml
from common.contants import test_student_m_degree_dir
from page.main import Main


class TestStudentClassTable:

    with open(test_student_m_degree_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        setup_datas = datas["setup_datas"]
        test_search_student_username_datas = datas["test_search_student_username"]
        test_get_course_bar_teachername_datas = datas["test_get_course_bar_teachername"]
        test_get_course_details_student_num_datas = datas["test_get_course_details_student_num"]
        test_search_studentname_datas = datas["test_search_studentname"]
        test_search_studentstaffNo_datas = datas["test_search_studentstaffNo"]
        test_get_lessontime_datas = datas["test_get_lessontime"]
        test_get_lesson_student_num_datas = datas["test_get_lesson_student_num"]
        test_back_to_student_management_degree_datas = datas["test_back_to_student_management_degree"]

    def setup_class(self):
        self.main = Main().goto_login(). \
            username(self.setup_datas["username"]).password(self.setup_datas["password"]).save(). \
            goto_application(). \
            goto_classtimetable(self.setup_datas["application"])

    def teardown_class(self):
        self.main.close()

    # def setup(self):
    #     self.main = Main()


    # def teardown(self):
    #     self.main.quit()

    @pytest.mark.parametrize("data", test_search_student_username_datas)
    def test_search_student_username(self, data):
        '''
        驗證查詢學生賬號
        :return:
        '''
        result = self.main.\
            goto_student_management_degree(data["memu"]).\
            search_simple(data["keywords_stu_all"]). \
            choice_student().\
            get_current_week_courses_num()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_get_course_bar_teachername_datas)
    def test_get_course_bar_teachername(self,data):
        '''
        驗證卡片上的教師正確
        '''
        result = self.main. \
            goto_student_management_degree(data["memu"]). \
            search_simple(data["keywords_stu_all"]). \
            choice_student(). \
            get_course_bar_teachername()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_get_course_details_student_num_datas)
    def test_get_course_details_student_num(self, data):
        '''
        驗證卡片上學生總數
        :return:
        '''
        result = self.main. \
            goto_student_management_degree(data["memu"]). \
            search_simple(data["keywords_stu_all"]). \
            choice_student(). \
            get_course_details(). \
            get_course_details_student_num()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_search_studentname_datas)
    def test_search_studentname(self, data):
        '''
        驗證班級同學頁面查詢姓名正確，必須輸入英文名稱，元素定位寫死了英文名稱
        :return:
        '''
        result = self.main. \
            goto_student_management_degree(data["memu"]). \
            search_simple(data["keywords_stu_all"]). \
            choice_student(). \
            get_course_details(). \
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
            goto_student_management_degree(data["memu"]). \
            search_simple(data["keywords_stu_all"]). \
            choice_student(). \
            get_course_details(). \
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
            goto_student_management_degree(data["memu"]). \
            search_simple(data["keywords_stu_all"]). \
            choice_student(). \
            get_course_details(). \
            goto_classmate(). \
            get_lessontime()
        assert result[:10] == data["expect"]

    @pytest.mark.parametrize("data", test_get_lesson_student_num_datas)
    def test_get_lesson_student_num(self, data):
        '''
        驗證班級同學頁面顯示人數
        :return: get_lesson_student_num
        '''
        result = self.main. \
            goto_student_management_degree(data["memu"]). \
            search_simple(data["keywords_stu_all"]). \
            choice_student(). \
            get_course_details(). \
            goto_classmate(). \
            get_lesson_student_num()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_back_to_student_management_degree_datas)
    def test_back_to_student_management_degree(self, data):
        '''
        驗證班級同學頁面返回上一頁保持進入前頁面不變
        :return:
        '''
        result = self.main. \
            goto_student_management_degree(data["memu"]). \
            search_simple(data["keywords_stu_all"]). \
            choice_student(). \
            get_course_details(). \
            goto_classmate(). \
            back_to_student_management_degree().\
            get_current_week_courses_num()
        assert result == data["expect"]
