import pytest
from data.data import TestData
from pages.main_page import MainPage

class TestMainPage:

    @pytest.mark.parametrize('num', list(range(8))) 
    def test_questions_and_answers(self, num, driver):
        page = MainPage(driver)
        page.go_to_url(TestData.BASE_URL)
        actual_answer = page.check_question_and_answer(num)
        assert actual_answer == TestData.answers_data[num]
