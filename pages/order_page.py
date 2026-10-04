from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class OrderPage(BasePage):

    NAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Имя']"
    )

    SURNAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Фамилия']"
    )

    ADDRESS_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Адрес: куда привезти заказ']"
    )

    METRO_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Станция метро']"
    )

    PHONE_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']"
    )

    NEXT_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Button_Button') "
        "and normalize-space()='Далее']"
    )

    DATE_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Когда привезти самокат']"
    )

    DATEPICKER = (
        By.CSS_SELECTOR,
        ".react-datepicker"
    )

    DATEPICKER_CURRENT_MONTH = (
        By.CSS_SELECTOR,
        ".react-datepicker__current-month"
    )

    DATEPICKER_NEXT_MONTH = (
        By.CSS_SELECTOR,
        ".react-datepicker__navigation--next"
    )

    RENTAL_PLACEHOLDER = (
        By.CSS_SELECTOR,
        ".Dropdown-placeholder"
    )

    RENTAL_OPTIONS = (
        By.CSS_SELECTOR,
        ".Dropdown-option"
    )

    BLACK_COLOR = (
        By.ID,
        "black"
    )

    GREY_COLOR = (
        By.ID,
        "grey"
    )

    COMMENT_INPUT = (
        By.XPATH,
        "//input[@placeholder='Комментарий для курьера']"
    )

    ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Button_Button') "
        "and normalize-space()='Заказать']"
    )

    CONFIRM_MODAL = (
        By.XPATH,
        "//div[contains(@class, 'Order_Modal')]"
    )

    CONFIRM_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Modal')]"
        "//button[normalize-space()='Да']"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//div[contains(@class, 'Order_ModalHeader')]"
    )

    def fill_first_form(
        self,
        name,
        surname,
        address,
        metro,
        phone
    ):
        self.input_text(
            self.NAME_INPUT,
            name
        )

        self.input_text(
            self.SURNAME_INPUT,
            surname
        )

        self.input_text(
            self.ADDRESS_INPUT,
            address
        )

        self.click(self.METRO_INPUT)

        metro_option = (
            By.XPATH,
            f"//button[contains(@class, 'select-search__option') "
            f"and contains(., '{metro}')]"
        )

        self.click(metro_option)

        self.input_text(
            self.PHONE_INPUT,
            phone
        )

        self.click(self.NEXT_BUTTON)

    def select_date(self, date):
        target_date = datetime.strptime(
            date,
            "%d.%m.%Y"
        )

        target_day = str(target_date.day)

        date_input = self.wait.until(
            EC.element_to_be_clickable(
                self.DATE_INPUT
            )
        )

        date_input.click()

        self.wait.until(
            EC.visibility_of_element_located(
                self.DATEPICKER
            )
        )

        for _ in range(24):
            current_month = self.driver.find_element(
                *self.DATEPICKER_CURRENT_MONTH
            ).text.strip()

            month_names = {
                1: "январ",
                2: "феврал",
                3: "март",
                4: "апрел",
                5: "май",
                6: "июн",
                7: "июл",
                8: "август",
                9: "сентябр",
                10: "октябр",
                11: "ноябр",
                12: "декабр"
            }

            target_month_name = month_names[
                target_date.month
            ]

            if (
                target_month_name in current_month.lower()
                and str(target_date.year) in current_month
            ):
                break

            next_month = self.wait.until(
                EC.element_to_be_clickable(
                    self.DATEPICKER_NEXT_MONTH
                )
            )

            next_month.click()

        day_locator = (
            By.XPATH,
            "//div[contains(@class, 'react-datepicker__day') "
            f"and normalize-space()='{target_day}' "
            "and not(contains(@class, "
            "'react-datepicker__day--outside-month'))]"
        )

        day = self.wait.until(
            EC.element_to_be_clickable(
                day_locator
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            day
        )

        day.click()

        self.wait.until(
            EC.invisibility_of_element_located(
                self.DATEPICKER
            )
        )

    def select_rental_period(self, rental_period):
        rental_placeholder = self.wait.until(
            EC.element_to_be_clickable(
                self.RENTAL_PLACEHOLDER
            )
        )

        rental_placeholder.click()

        self.wait.until(
            lambda driver: any(
                option.is_displayed()
                for option in driver.find_elements(
                    *self.RENTAL_OPTIONS
                )
            )
        )

        options = self.driver.find_elements(
            *self.RENTAL_OPTIONS
        )

        for option in options:
            if (
                option.is_displayed()
                and option.text.strip() == rental_period
            ):
                option.click()
                return

        available_options = [
            option.text.strip()
            for option in options
            if option.is_displayed()
        ]

        raise AssertionError(
            f"Не найден срок аренды '{rental_period}'. "
            f"Доступные варианты: {available_options}"
        )

    def select_scooter_color(self, color):
        if color == "black":
            color_locator = self.BLACK_COLOR
        elif color == "grey":
            color_locator = self.GREY_COLOR
        else:
            raise ValueError(
                f"Неизвестный цвет самоката: {color}"
            )

        color_checkbox = self.wait.until(
            EC.presence_of_element_located(
                color_locator
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            color_checkbox
        )

        if not color_checkbox.is_selected():
            self.driver.execute_script(
                "arguments[0].click();",
                color_checkbox
            )

        self.wait.until(
            lambda driver: color_checkbox.is_selected()
        )

    def click_order_button(self):
        buttons = self.driver.find_elements(
            *self.ORDER_BUTTON
        )

        visible_buttons = [
            button
            for button in buttons
            if button.is_displayed()
            and button.is_enabled()
        ]

        if not visible_buttons:
            raise AssertionError(
                "Не найдена доступная кнопка 'Заказать' "
                "на второй форме"
            )

        order_button = visible_buttons[-1]

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            order_button
        )

        self.wait.until(
            lambda driver: (
                order_button.is_displayed()
                and order_button.is_enabled()
            )
        )

        order_button.click()

    def fill_second_form(
        self,
        date,
        rental_period,
        color,
        comment
    ):
        self.select_date(date)

        self.select_rental_period(
            rental_period
        )

        self.select_scooter_color(
            color
        )

        self.input_text(
            self.COMMENT_INPUT,
            comment
        )

        self.click_order_button()

        self.wait.until(
            EC.visibility_of_element_located(
                self.CONFIRM_MODAL
            )
        )

    def confirm_order(self):
        confirm_button = self.wait.until(
            EC.element_to_be_clickable(
                self.CONFIRM_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            confirm_button
        )

        confirm_button.click()

    def is_success_message_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.SUCCESS_MESSAGE
            )
        ).is_displayed()