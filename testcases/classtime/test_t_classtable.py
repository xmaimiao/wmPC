import sys
sys.path.append('..')
import pytest
import yaml

from page.main import Main

class TestTeacherClassTable:

    with open("../../data/cases/signin/teacherclass.yaml", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    @pytest.fixture(scope='function')
    @pytest.mark.parametrize("data", data)
    def t_classtable(self,data):
        '''
        把setup的內容包裝成函數調用，原因：要傳參data
        :param data:
        :return:
        '''
        # 处理data参数
        memu = data['memu']
        term = data['term']

        # t_classtable = Main().goto_classtimetable(). \
        #     goto_teacher_classtable(memu)
        t_classtable = Main().goto_teacher_classtable(memu)
        return t_classtable

    @pytest.mark.parametrize("data", data)
    def test_course_type(self, data,t_classtable):
        '''
        驗證課堂類型
        :return:
        '''
        course_num = data['course_num']
        type_num = data['type_num']
        week = data['week']
        result = t_classtable. \
            course_details(week,course_num).\
            course_type(type_num)
        return result

    @pytest.mark.parametrize("data", data)
    def test_course_room(self, data,t_classtable):
        '''
        驗證課堂類型——》不同的課堂出現的課室字段
        :return:
        '''
        course_num = data['course_num']
        type_num = data['type_num']
        week = data['week']
        # result = t_classtable. \
        #     course_details(week, course_num). \
        #     course_room(type_num)
        result = t_classtable. \
            course_room(type_num)
        return result


    @pytest.mark.parametrize("data", data)
    def test_classtype_all(self,data,t_classtable):
        expect_type = data["expect_type"]
        expect_room = data["expect_room"]
        assert self.test_course_type(data,t_classtable) == expect_type
        assert self.test_course_room(data, t_classtable)[:-1] == expect_room



