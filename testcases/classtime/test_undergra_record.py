import pytest
import yaml

from page.main import Main

class TestUnderGra_Record:

    with open("../../data/cases/signin/undergra_data.yaml", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    @pytest.fixture(scope='function')
    @pytest.mark.parametrize("data", data)
    def sign_in_derail(self,data):
        '''
        把setup的內容包裝成函數調用，原因：要傳參data
        :param data:
        :return:
        '''
        # 处理data参数
        memu = data['memu']
        term = data['term']
        stuclass = data['stuclass']
        course = data['course']
        staffNo = data['staffNo']

        sign_in_derail = Main().goto_classtimetable(). \
            goto_undergradute_record(memu). \
            advanced_search(term, stuclass,course). \
            advanced_srarch_result_goto_signrecord(course). \
            simple_search(staffNo)
        return sign_in_derail

    # def setup(self):
    #
    #     # self.main = Main()
    #     # 瀏覽器復用“簽到詳情”頁面，臨時調用
    #     self.sign_in_derail = Main().goto_classtimetable().\
    #         goto_undergradute_record(memu).\
    #         advanced_search(term,stuclass,course).\
    #         advanced_srarch_result_goto_signrecord(course).\
    #         simple_search(staffNo)

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_firstsign_supp(self,data,sign_in_derail):
        staffNo = data['staffNo']
        # 驗證首簽為：補簽
        result = sign_in_derail. \
            simple_search_result_firstrecords_firstsign(staffNo)
        assert result == "補簽"

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_firstsign_nosign(self,data,sign_in_derail):
        # 驗證首簽為：未簽
        staffNo = data['staffNo']
        result = sign_in_derail.\
            simple_search_result_firstrecords_firstsign(staffNo)
        assert result == "未簽"

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_firstsign_present(self,data,sign_in_derail):
        # 驗證首簽為：已簽
        staffNo = data['staffNo']
        result = sign_in_derail.\
            simple_search_result_firstrecords_firstsign(staffNo)
        assert result == "已簽"

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_firstsign_absent(self,data,sign_in_derail):
        # 驗證首簽為：—
        staffNo = data['staffNo']
        result = sign_in_derail.\
            simple_search_result_firstrecords_firstsign(staffNo)
        assert result == "—"


    @pytest.mark.parametrize("data", data)
    def test_firstrecords_firstsign_day_isNone(self,data,sign_in_derail):
        # 驗證首簽日期爲空
        staffNo = data['staffNo']
        result = sign_in_derail.\
            simple_search_result_firstrecords_firstsign_day(staffNo)
        assert result == ""

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_firstsign_day(self,data,sign_in_derail):
        # 驗證首簽日期不爲空
        staffNo = data['staffNo']
        result = sign_in_derail.\
            simple_search_result_firstrecords_firstsign_day(staffNo)
        assert result != ""

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_firstsign_time(self,data,sign_in_derail):
        # 驗證首簽時間不爲空
        staffNo = data['staffNo']
        result = sign_in_derail.\
            simple_search_result_firstrecords_firstsign_time(staffNo)
        assert result != ""

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_secondsign_supp(self,data,sign_in_derail):
        # 驗證次簽為：補簽
        staffNo = data['staffNo']
        result = sign_in_derail.\
            simple_search_result_firstrecords_secondsign(staffNo)
        assert result == "補簽"

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_secondsign_nosign(self,data,sign_in_derail):
        # 驗證次簽為：未簽
        staffNo = data['staffNo']
        result = sign_in_derail.\
            simple_search_result_firstrecords_secondsign(staffNo)
        assert result == "未簽"

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_secondsign_present(self,data,sign_in_derail):
        # 驗證次簽為：已簽
        staffNo = data['staffNo']
        result = sign_in_derail.\
            simple_search_result_firstrecords_secondsign(staffNo)
        assert result == "已簽"

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_secondsign_absent(self,data,sign_in_derail):
        # 驗證次簽為：—
        staffNo = data['staffNo']
        result = sign_in_derail.\
            simple_search_result_firstrecords_secondsign(staffNo)
        assert result == "—"

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_secondsign_day_isNone(self,data,sign_in_derail):
        # 驗證次簽日期爲空
        staffNo = data['staffNo']
        result = sign_in_derail.\
            simple_search_result_firstrecords_firstsign_day(staffNo)
        assert result == ""

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_secondsign_day(self,data,sign_in_derail):
        # 驗證次簽日期不爲空
        staffNo = data['staffNo']
        result = sign_in_derail.\
            simple_search_result_firstrecords_firstsign_day(staffNo)
        assert result != ""

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_secondsign_time(self,data,sign_in_derail):
        # 驗證次簽時間不爲空
        staffNo = data['staffNo']
        result = sign_in_derail.\
            simple_search_result_firstrecords_firstsign_time(staffNo)
        assert result != ""

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_status_present(self,data,sign_in_derail):
        # 驗證第一條簽到狀態為：出席
        staffNo = data['staffNo']
        result = sign_in_derail. \
            simple_search_result_firstrecords_signstatus(staffNo)
        assert result == "出席"

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_status_late(self,data,sign_in_derail):
        # 驗證第一條簽到狀態為：遲到
        staffNo = data['staffNo']
        result = sign_in_derail. \
            simple_search_result_firstrecords_signstatus(staffNo)
        assert result == "遲到"

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_status_excused(self,data,sign_in_derail):
        # 驗證第一條簽到狀態為：早退
        staffNo = data['staffNo']
        result = sign_in_derail. \
            simple_search_result_firstrecords_signstatus(staffNo)
        assert result == "早退"

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_status_adsent(self,data,sign_in_derail):
        # 驗證第一條簽到狀態為：缺席
        staffNo = data['staffNo']
        result = sign_in_derail. \
            simple_search_result_firstrecords_signstatus(staffNo)
        assert result == "缺席"

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_status_absenteeism(self,data,sign_in_derail):
        # 驗證第一條簽到狀態為：曠課
        staffNo = data['staffNo']
        result = sign_in_derail. \
            simple_search_result_firstrecords_signstatus(staffNo)
        assert result == "曠課"

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_remark_item_name1_firstsign(self,data,sign_in_derail):
        # 驗證第一條簽到備註僅有首簽
        staffNo = data['staffNo']
        result = sign_in_derail. \
            simple_search_result_firstrecords_remark_item_name1(staffNo)
        assert result == "首簽:"

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_remark_item_name1_secondsign(self,data,sign_in_derail):
        # 驗證第一條簽到備註僅有次簽
        staffNo = data['staffNo']
        result = sign_in_derail. \
            simple_search_result_firstrecords_remark_item_name1(staffNo)
        assert result == "次簽:"

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_remark_item_name1_first_and_secondsign(self,data,sign_in_derail):
        # 驗證第一條簽到備註為：首簽/次簽
        staffNo = data['staffNo']
        result = sign_in_derail. \
            simple_search_result_firstrecords_remark_item_name1(staffNo)
        assert result == "首簽/次簽:"

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_remark_item_name2(self,data,sign_in_derail):
        # 驗證第一條簽到備註必有次簽
        staffNo = data['staffNo']
        result = sign_in_derail. \
            simple_search_result_firstrecords_remark_item_name2(staffNo)
        assert result == "次簽:"

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_goto_supp(self,data,sign_in_derail):
        # 驗證第一條簽到去補簽
        staffNo = data['staffNo']
        remark = data['remark']
        result = sign_in_derail. \
            simple_search_result_firstrecords_goto_supp_signin(staffNo).\
            default_suppsignin(remark).\
            simple_search_result_firstrecords_signstatus(staffNo)
        assert result == "出席"

    @pytest.mark.parametrize("data", data)
    def test_firstrecords_goto_absent(self,data,sign_in_derail):
        # 驗證第一條簽到缺席
        staffNo = data['staffNo']
        remark = data['remark']
        result = sign_in_derail. \
            simple_search_result_firstrecords_goto_absent(staffNo). \
            absent(remark). \
            simple_search_result_firstrecords_signstatus(staffNo)
        assert result == "缺席"




