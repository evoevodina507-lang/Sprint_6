import pytest
import allure
from pages.main_page import MainPage
from data import Urls, FAQData

class TestFAQ:
    @allure.feature("Главная страница")
    @allure.story("Раздел 'Вопросы о важном'")
    @pytest.mark.parametrize("index, expected_answer", FAQData.FAQ_ANSWERS.items())
    def test_faq_accordion(self, driver, index, expected_answer):
        main_page = MainPage(driver)
        main_page.open_url(Urls.MAIN_PAGE_URL)
        main_page.accept_cookies()

        main_page.click_faq_question(index)
        actual_answer = main_page.get_faq_answer_text(index)

        assert actual_answer == expected_answer, (
            f"Ожидаемый текст: '{expected_answer}', но получен: '{actual_answer}'"
        )