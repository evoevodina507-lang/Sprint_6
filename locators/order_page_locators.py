from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Куки
    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-cookie")

    # Первая форма ("Для кого самокат")
    NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

    # Вторая форма ("Про аренду")
    DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")

    # Срок аренды
    RENT_TIME_FIELD = (By.XPATH, ".//div[@class='Dropdown-control']")
    RENT_TIME_OPTION = (By.XPATH, ".//div[@class='Dropdown-option']")

    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")

    ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    CONFIRM_MODAL_YES_BUTTON = (By.XPATH, ".//button[text()='Да']")
    SUCCESS_MODAL_HEADER = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]")
    SUCCESS_MODAL_STATUS_BUTTON = (By.XPATH, ".//button[text()='Посмотреть статус']")
    