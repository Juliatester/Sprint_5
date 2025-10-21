import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

@pytest.mark.usefixtures("driver")
class TestAnnoucement:

    def test_annoucement_unauthorized_user(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru")
        driver.find_element(*Locators.create_add_button).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.auth_required_text)
        )
        auth_required_text_element = driver.find_element(*Locators.auth_required_text).text
        assert auth_required_text_element == "Чтобы разместить объявление, авторизуйтесь", "Текст заголовка модального окна не соответствует ожидаемому"    

    def test_annoucement_authorized_user(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru")

        driver.find_element(*Locators.login_button).click()
        driver.find_element(*Locators.email_field).send_keys("juliamur@mail.com")
        driver.find_element(*Locators.password_input).send_keys("password123")
        driver.find_element(*Locators.main_login_button).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.user_text)
        )

        driver.find_element(*Locators.create_add_button).click()

        driver.find_element(*Locators.add_name_field).send_keys("Продам душу")
        driver.find_element(*Locators.category_dropdown).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.category_option)
        )
        driver.find_element(*Locators.category_option).click()
        driver.find_element(*Locators.condition_selector).click()
        driver.find_element(*Locators.city_dropdown).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.city_option)
        )
        driver.find_element(*Locators.city_option).click()
        driver.find_element(*Locators.add_description_field).send_keys("Душу дъяволу продам за часик сна")
        driver.find_element(*Locators.add_price_field).send_keys("1000")

        driver.find_element(*Locators.publish_button).click()
        driver.find_element(*Locators.user_profile_button).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.my_ads_section)
        )

        driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(*Locators.my_ads_section))

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.add_item)
        )
        add_item = driver.find_element(*Locators.add_item)
        assert add_item.is_displayed(), "Созданное объявление не отображается в блоке 'Мои объявления'"
