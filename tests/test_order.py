import pytest
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:

    @pytest.mark.parametrize(
        "order_button, user_data",
        [
            (
                "top",
                {
                    "name": "Иван",
                    "surname": "Иванов",
                    "address": "Москва, улица Ленина, 1",
                    "metro": "Черкизовская",
                    "phone": "89991234567",
                    "date": "30.10.2026",
                    "rental_period": "сутки",
                    "color": "black",
                    "comment": "Позвонить за час"
                }
            ),
            (
                "bottom",
                {
                    "name": "Анна",
                    "surname": "Петрова",
                    "address": "Москва, улица Пушкина, 10",
                    "metro": "Сокольники",
                    "phone": "89997654321",
                    "date": "31.10.2026",
                    "rental_period": "двое суток",
                    "color": "grey",
                    "comment": "Оставить у двери"
                }
            )
        ]
    )
    def test_order_success(
        self,
        driver,
        order_button,
        user_data
    ):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()

        main_page.click_order_button(
            order_button
        )

        order_page.fill_first_form(
            user_data["name"],
            user_data["surname"],
            user_data["address"],
            user_data["metro"],
            user_data["phone"]
        )

        order_page.fill_second_form(
            user_data["date"],
            user_data["rental_period"],
            user_data["color"],
            user_data["comment"]
        )

        order_page.confirm_order()

        assert order_page.is_success_message_displayed()

    def test_scooter_logo_returns_to_main_page(self, driver):
        main_page = MainPage(driver)

        main_page.open()
        main_page.click_scooter_logo()

        assert driver.current_url == MainPage.URL

    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)

        main_page.open()

        original_window = driver.current_window_handle

        main_page.click_yandex_logo()

        main_page.switch_to_next_window()

        WebDriverWait(driver, 15).until(
            lambda d: "dzen.ru" in d.current_url
        )

        assert driver.current_window_handle != original_window
        assert "dzen.ru" in driver.current_url