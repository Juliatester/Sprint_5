# Sprint_5

Этот проект содержит UI-автотесты для веб-приложения "Doska" с использованием Selenium WebDriver и pytest.

Структура проекта:

Project/
├── tests/
│   ├── test_create_announcement.py
│   ├── test_create_user.py
│   ├── test_login.py
│   ├── test_logout.py
├── .gitignore
├── conftest.py
└── locators.py

Технологии:
Python - язык программирования
Selenium WebDriver - автоматизация браузера
pytest - фреймворк для тестирования
ChromeDriver - управление браузером Chrome

Описание тестовых сценариев:

1. Создание объявления неавторизованным пользователем (test_annoucement_unauthorized_user)/авторизованным пользователем (test_annoucement_authorized_user)
2. Регистрация с некорректным email(test_register_invalid_email)/Регистрация с корректным email(test_register_valid_user), регистрация существующего пользователя (test_register_existing_user)
3. Логин пользователя (test_successful_login)
4. Разлогин пользователя (test_successful_logout)


Запуск тестов:
pytest -v