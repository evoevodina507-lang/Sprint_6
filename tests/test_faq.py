import pytest

from pages.main_page import MainPage


class TestFAQ:

    @pytest.mark.parametrize(
        "question_index",
        [0, 1, 2, 3, 4, 5, 6, 7]
    )
    def test_faq_question_opens_answer(
        self,
        driver,
        question_index
    ):
        main_page = MainPage(driver)

        main_page.open()
        main_page.click_faq_question(question_index)

        answer = main_page.get_faq_answer(question_index)

        assert answer != ""