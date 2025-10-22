import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from locators import Locators

# Инициализация генератора фейковых данных
@pytest.fixture
def faker():
    return Faker()

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://qa-desk.stand.praktikum-services.ru")
    yield driver
    driver.quit()


