from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from pages.base_page import BasePage


class MainPage(BasePage):

    URL = "https://qa-scooter.praktikum-services.ru/"

    ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Button_Button') and text()='Заказать']"
    )

    FAQ_QUESTIONS = (
        By.XPATH,
        "//div[contains(@class, 'accordion__heading')]"
    )

    FAQ_ANSWERS = (
        By.XPATH,
        "//div[contains(@class, 'accordion__panel')]"
    )

    SCOOTER_LOGO = (
        By.XPATH,
        "//a[contains(@class, 'Header_LogoScooter')]"
    )

    YANDEX_LOGO = (
        By.XPATH,
        "//a[contains(@class, 'Header_LogoYandex')]"
    )

    COOKIE_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'да все привыкли')]"
    )

    def open(self):
        self.driver.get(self.URL)

    def accept_cookies(self):
        try:
            cookie_button = self.wait.until(
                EC.element_to_be_clickable(
                    self.COOKIE_BUTTON
                )
            )

            cookie_button.click()

        except Exception:
            pass

    def click_order_button(self, position):
        buttons = self.driver.find_elements(
            *self.ORDER_BUTTON
        )

        if position == "top":
            button = buttons[0]
        else:
            button = buttons[-1]

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            button
        )

        self.wait.until(
            lambda driver: button.is_displayed()
            and button.is_enabled()
        )

        button.click()

    def click_faq_question(self, index):
        questions = self.driver.find_elements(
            *self.FAQ_QUESTIONS
        )

        question = questions[index]

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            question
        )

        self.wait.until(
            lambda driver: question.is_displayed()
        )

        question.click()

    def get_faq_answer(self, index):
        answers = self.driver.find_elements(
            *self.FAQ_ANSWERS
        )

        answer = answers[index]

        self.wait.until(
            lambda driver: answer.is_displayed()
            and answer.text.strip() != ""
        )

        return answer.text.strip()

    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)

    def switch_to_next_window(self):
        current_window = self.driver.current_window_handle

        self.wait.until(
            lambda driver: len(driver.window_handles) > 1
        )

        for window in self.driver.window_handles:
            if window != current_window:
                self.driver.switch_to.window(window)
                return

        raise AssertionError(
            "Новое окно не найдено"
        )