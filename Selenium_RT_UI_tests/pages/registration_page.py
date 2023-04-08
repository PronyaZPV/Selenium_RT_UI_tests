from selenium.webdriver.common.by import By

from .base_page import BasePage
from ..pages.auth_page import AuthPage


class Locators:
    LOCATOR_FORM_TITLE = (By.CLASS_NAME, "card-container__title")
    LOCATOR_REGISTRATION_FORM = (By.CLASS_NAME, "register-form")
    LOCATOR_FIRSTNAME_FIELD = (By.NAME, "firstName")
    LOCATOR_LASTNAME_FIELD = (By.NAME, "lastName")
    LOCATOR_REGION_FIELD = (By.CSS_SELECTOR, "div[class*='register-form__dropdown']")
    LOCATOR_LOGIN_FIELD = (By.ID, "address")
    LOCATOR_PASSWORD_FIELD = (By.ID, "password")
    LOCATOR_PASSWORD_CONFIRM_FIELD = (By.ID, "password-confirm")
    LOCATOR_ENTER_BUTTON = (By.CSS_SELECTOR, "button[name='register']")
    LOCATOR_FORM_AGREEMENT = (By.LINK_TEXT, "пользовательского соглашения")
    LOCATOR_VALIDATION_ERROR = (By.CSS_SELECTOR, "span[class *='meta--error']")


class RegistrationPage(BasePage):
    @staticmethod
    def go_to_registration_page(browser):
        """ Открытие формы регистрации
            """
        auth_page = AuthPage(browser)
        auth_page.go_to_site()
        auth_page.register_link().click()
        return auth_page

    def form_title(self):
        """ Вывод заголовка отображаемой формы ввода данных
            """
        return self.find_element(Locators.LOCATOR_FORM_TITLE, time=10)

    def registration_form(self):
        return self.find_element(Locators.LOCATOR_REGISTRATION_FORM, time=10)

    def firstname_field(self):
        return self.find_element(Locators.LOCATOR_FIRSTNAME_FIELD, time=10)

    def enter_firstname(self, firstname):
        self.firstname_field().send_keys(firstname)
        return self.firstname_field()

    def lastname_field(self):
        return self.find_element(Locators.LOCATOR_LASTNAME_FIELD, time=10)

    def enter_lastname(self, lastname):
        self.lastname_field().send_keys(lastname)
        return self.firstname_field()

    def region_dropdown(self):
        return self.find_element(Locators.LOCATOR_REGION_FIELD, time=10)

    def login_field(self):
        return self.find_element(Locators.LOCATOR_LOGIN_FIELD, time=10)

    def password_field(self):
        return self.find_element(Locators.LOCATOR_PASSWORD_FIELD, time=10)

    def password_confirm_field(self):
        return self.find_element(Locators.LOCATOR_PASSWORD_CONFIRM_FIELD, time=10)

    def enter_password(self, password):
        self.password_field().send_keys(password)
        return self.password_field()

    def enter_button(self):
        return self.find_element(Locators.LOCATOR_ENTER_BUTTON, time=10)

    def form_agreement(self):
        """ Вывод ссылки на пользовательское соглашение из формы регистрации
            """
        return self.find_element(Locators.LOCATOR_FORM_AGREEMENT, time=10)

    def count_of_errors(self):
        """ Подсчет количества отображаемых ошибок валидации
            """
        errors_set = self.find_elements(Locators.LOCATOR_VALIDATION_ERROR, time=2)
        return len(errors_set)

    def validation_error(self):
        """ Вывод любой валидационной ошибки в форме регистрации
            """
        return self.find_element(Locators.LOCATOR_VALIDATION_ERROR, time=2)


