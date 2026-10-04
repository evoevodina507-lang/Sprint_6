from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
from data import Urls


class TestRedirects:

    def test_yandex_logo_redirect(self, driver):
        driver.get(Urls.MAIN_PAGE_URL)
        
        main_page = MainPage(driver)
        main_page.accept_cookies()
        
        main_page.click_yandex_logo()
        main_page.switch_to_next_window()

        # Ждем загрузки страницы Дзена вместо about:blank
        WebDriverWait(driver, 10).until(
            lambda d: "dzen.ru" in d.current_url or "yandex" in d.current_url
        )

        assert "dzen.ru" in driver.current_url or "yandex" in driver.current_url