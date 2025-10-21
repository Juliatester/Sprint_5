import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from faker import Faker

faker = Faker()

@pytest.mark.usefixtures("driver")
class TestRegistration:

    def test_register_valid_user(self, driver):

        driver.get("https://qa-desk.stand.praktikum-services.ru")

        driver.find_element(*Locators.login_button).click()
        driver.find_element(*Locators.no_account_button).click()

        email = faker.email()
        password = faker.password()

        driver.find_element(*Locators.email_field).send_keys(email)
        driver.find_element(*Locators.password_input).send_keys(password)
        driver.find_element(*Locators.repeat_password_field).send_keys(password)
        driver.find_element(*Locators.create_account_button).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.user_text)
        )

        user_avatar = driver.find_element(*Locators.user_avatar)
        assert user_avatar.is_displayed(), "Аватар пользователя не отображается"

        user_text = driver.find_element(*Locators.user_text)
        assert user_text.text == "User.", "Имя пользователя не соответствует ожидаемому"

    def test_register_invalid_email(self, driver):

        driver.get("https://qa-desk.stand.praktikum-services.ru")

        driver.find_element(*Locators.login_button).click()
        driver.find_element(*Locators.no_account_button).click()


        email = faker.text(15)
        password = faker.password()

        driver.find_element(*Locators.email_field).send_keys(email)
        driver.find_element(*Locators.password_input).send_keys(password)
        driver.find_element(*Locators.repeat_password_field).send_keys(password)
        driver.find_element(*Locators.create_account_button).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.error_text)
        )
        email_container = driver.find_element(*Locators.email_container)
        password_container = driver.find_element(*Locators.password_error_container)
        confirm_password_container = driver.find_element(*Locators.confirm_password_container)

    def test_register_existing_user(self, driver):

        driver.get("https://qa-desk.stand.praktikum-services.ru")

        driver.find_element(*Locators.login_button).click()
        driver.find_element(*Locators.no_account_button).click()
        driver.find_element(*Locators.email_field).send_keys("juliamur@mail.com")
        driver.find_element(*Locators.password_input).send_keys("password123")
        driver.find_element(*Locators.repeat_password_field).send_keys("password123")
        driver.find_element(*Locators.create_account_button).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.error_text)
        )

        email_container = driver.find_element(*Locators.email_container)
        password_container = driver.find_element(*Locators.password_error_container)
        confirm_password_container = driver.find_element(*Locators.confirm_password_container)

        assert email_container.value_of_css_property("border-color") == 'rgb(255, 105, 114)', 'цвет ошибки поля'
        assert password_container.value_of_css_property("border-color") == 'rgb(255, 105, 114)', 'цвет ошибки поля'
        assert confirm_password_container.value_of_css_property("border-color") == 'rgb(255, 105, 114)', 'цвет ошибки поля'

class TestRegistrationIncorrectEmail:
    def test_register_invalid_email(self, driver):

        driver.get("https://qa-desk.stand.praktikum-services.ru")

        driver.find_element(*Locators.login_button).click()
        driver.find_element(*Locators.no_account_button).click()


        email = faker.text(15)
        password = faker.password()

        driver.find_element(*Locators.email_field).send_keys(email)
        driver.find_element(*Locators.password_input).send_keys(password)
        driver.find_element(*Locators.repeat_password_field).send_keys(password)
        driver.find_element(*Locators.create_account_button).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.error_text)
        )
        email_container = driver.find_element(*Locators.email_container)
        password_container = driver.find_element(*Locators.password_error_container)
        confirm_password_container = driver.find_element(*Locators.confirm_password_container)

        assert email_container.value_of_css_property("border-color") == 'rgb(255, 105, 114)', 'цвет ошибки поля'
        assert password_container.value_of_css_property("border-color") == 'rgb(255, 105, 114)', 'цвет ошибки поля'
        assert confirm_password_container.value_of_css_property("border-color") == 'rgb(255, 105, 114)', 'цвет ошибки поля'