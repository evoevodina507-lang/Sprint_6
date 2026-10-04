from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-cookie")
    
    TOP_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")

    FAQ_ITEM = lambda self, num: (By.ID, f"accordion__heading-{num}")
    FAQ_ANSWER = lambda self, num: (By.ID, f"accordion__panel-{num}")

    YANDEX_LOGO = (By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]")
    SCOOTER_LOGO = (By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]")