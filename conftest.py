import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.page_load_strategy = "eager"

    driver = webdriver.Firefox(options=options)
    driver.maximize_window()

    yield driver

    driver.quit()