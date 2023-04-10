from sys import platform
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    """ Класс, содержащий базовые методы для проверки сайта РТ
        """
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://b2c.passport.rt.ru/"

    def go_to_site(self):
        """ Открытие страницы авторизации
            """
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        """ Метод для поиска единичных элементов на странице
            """
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Not find {locator}')

    def find_elements(self, locator, time=10):
        """ Метод для поиска группы элементов на странице
            """
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Not find {locator}')

    def submit(self):
        """ Функция, запускающая валидацию в полях ввода, кликая в свободном месте страницы
            """
        return self.find_element((By.TAG_NAME, "body")).click()

    def clear_all(self):
        """ Метод для очистки всех полей ввода
            """
        input_fields = self.find_elements((By.CSS_SELECTOR, "input[class*='rt-input__input']"))
        for field in input_fields:
            field.send_keys((Keys.COMMAND if platform == "darwin" else Keys.CONTROL) + "a")
            field.send_keys(Keys.DELETE)

    def agreement_contract_page(self):
        """ Вывод заголовка оферты пользовательского соглашения
            """
        return self.find_element((By.CSS_SELECTOR, "h1[class='offer-title']"), time=5)
