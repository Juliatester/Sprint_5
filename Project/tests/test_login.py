import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import config

@pytest.mark.usefixtures("driver")
class TestLogin:

    def test_successful_login(self, driver):
        driver.get(config.link)
        driver.find_element(*Locators.login_button).click()
        driver.find_element(*Locators.email_field).send_keys(config.login_user["email"])
        driver.find_element(*Locators.password_input).send_keys(config.login_user["password"])
        driver.find_element(*Locators.main_login_button).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.user_text)
        )
        user_avatar = driver.find_element(*Locators.user_avatar)
        assert user_avatar.is_displayed(), "Аватар пользователя не отображается"
        user_text = driver.find_element(*Locators.user_text)
        assert user_text.text == "User.", "Имя пользователя не соответствует ожидаемому"