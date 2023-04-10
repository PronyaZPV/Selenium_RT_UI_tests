# Selenium_RT_UI_tests

**Объект тестирования UI**: https://b2c.passport.rt.ru

**Требования** с корректировками:
https://docs.google.com/document/d/15ZNFNnPgu0GtVidPXyGa2CzLnhnuIhdNJyEuei-J5LU/edit?usp=sharing

**Тест-кейсы и баг-репорты** (на разных листах):
https://docs.google.com/spreadsheets/d/1nFmKOr62rsXvQe80Ogy-BE0OgQQq7VlD2G7iXBarg1M/edit?usp=sharing

**Репозиторий с кодом**:
https://github.com/PronyaZPV/Selenium_RT_UI_tests

-----------------------------------------------------------------------------------

Тесты написаны с помощью Pytest и Selenium, для браузера Google Chrome
Использованы техники эквивалентное разбиения и анализ граничных значений, тестирование по сценариям использования.


### Локальный запуск тестов
1. Клонирйте себе репозиторий


2. Установите все необходимые модули и библиотеки. Они перечислены в файле requirements.txt
Для этого, из корневой папки проекта выполнить:
- MacOS - `python3 -m install -r requirements.txt`
- Windows - `pip install -r requirements.txt`


3. В проекте в папке `/WebDriver` уже присутвует webdriver версии 112.0.5615.49
- Для Windows - `/WebDriver/chromedriver.exe`
- Для MacOS - `/WebDriver/chromedriver`
Актуальный можете скачать по ссылке - https://chromedriver.chromium.org/downloads


4. Для запуска тестов, находясь в папке с тестами `/tests` можно использовать, например - `python -m pytest tests_rt_ui.py`



### Структура проекта

`/pages/base_page.py` - class BasePage с базовыми методами

`/pages/auth_page.py` - все необходимые локаторы и методы для тестов страницы авторизации 

`/pages/registration_page.py` - все необходимые локаторы и методы для тестов страницы регистрации 

`/pages/footer.py` - все необходимые локаторы и методы для тестов футера

`/pages/header.py` - все необходимые локаторы и методы для тестов хедера

`/pages/recovery_page.py` - все необходимые локаторы и методы для тестов страницы восстановления пароля

`/tests/tests_rt_ui.py` - файл с тестами

`/WebDriver/webdriver` - webdriver для MacOS

`/WebDriver/webdriver.exe` - webdriver для Windows

`/conftest.py` - фикстура, инициализирующая webdriver 

`/parameters.py` - данные для параметризации тестов

`/pytest.ini` - маркеры тестов + настройка отображения кириллических символов в отчете тестирования

`/requirements.txt` - список применяемых в проекте модулей с версиями
