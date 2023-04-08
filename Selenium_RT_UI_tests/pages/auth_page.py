from sys import platform
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from .base_page import BasePage


TABS_MENU_ELEMENTS = [
        'Телефон',
        'Почта',
        'Логин',
        'Лицевой счёт',
    ]


class Locators:
    LOCATOR_LOGIN_FIELD = (By.ID, "username")
    LOCATOR_PASS_FIELD = (By.ID, "password")
    LOCATOR_ENTER_BUTTON = (By.CSS_SELECTOR, "button[name='login']")
    LOCATOR_LEFT_BODY = (By.ID, "page-left")
    LOCATOR_RIGHT_BODY = (By.ID, "page-right")
    LOCATOR_BODY_LOGO = (By.CLASS_NAME, "rt-logo.main-header__logo")
    LOCATOR_FORM_TITLE = (By.CLASS_NAME, "card-container__title")
    LOCATOR_AUTH_FORM = (By.CLASS_NAME, "login-form")
    LOCATOR_TABS_MENU = (By.CSS_SELECTOR, "div[class *='tabs-input-container__tabs']")
    LOCATOR_REMEMBER_ME = (By.CLASS_NAME, "rt-checkbox")
    LOCATOR_FORM_ERROR_MESSAGE = (By.CSS_SELECTOR, "span[id='form-error-message']")
    LOCATOR_FORGOT_PASSWORD_MUTED = (By.XPATH, "//a[@id='forgot_password' and contains(@class, 'muted')]")
    LOCATOR_FORGOT_PASSWORD_ACTIVE = (By.XPATH, "//a[@id='forgot_password' and  not(contains(@class, 'muted'))]")
    LOCATOR_FORM_AGREEMENT = (By.LINK_TEXT, "пользовательского соглашения")
    LOCATOR_SOCIAL_PROVIDERS = (By.CLASS_NAME, "social-providers")
    LOCATOR_SOCIAL_VK = (By.ID, "oidc_vk")
    LOCATOR_SOCIAL_OK = (By.ID, "oidc_ok")
    LOCATOR_SOCIAL_MAIL = (By.ID, "oidc_mail")
    LOCATOR_SOCIAL_GOOGLE = (By.ID, "oidc_google")
    LOCATOR_SOCIAL_YA = (By.ID, "oidc_ya")
    LOCATOR_FORM_REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")
    LOCATOR_INPUT_LOGIN_TEXT = (By.CSS_SELECTOR, "input[name='username']")

    LOCATORS_TABS_MENU_ELEMENTS = {
        'Телефон': {
            'LOCATOR_TAB_MENU': (By.ID, "t-btn-tab-phone"),
            'LOCATOR_INPUT_FIELD': (By.XPATH, "//span[contains(text(), 'Мобильный телефон')]")
        },
        'Почта': {
            'LOCATOR_TAB_MENU': (By.ID, "t-btn-tab-mail"),
            'LOCATOR_INPUT_FIELD': (By.XPATH, "//span[contains(text(), 'Электронная почта')]")
        },
        'Логин': {
            'LOCATOR_TAB_MENU': (By.ID, "t-btn-tab-login"),
            'LOCATOR_INPUT_FIELD': (By.XPATH, "//span[contains(text(), 'Логин')]")
        },
        'Лицевой счёт': {
            'LOCATOR_TAB_MENU': (By.ID, "t-btn-tab-ls"),
            'LOCATOR_INPUT_FIELD': (By.XPATH, "//span[contains(text(), 'Лицевой счёт')]")
        },
    }


class AuthPage(BasePage):
    LIST_TABS_MENU_ELEMENTS = '\n'.join(Locators.LOCATORS_TABS_MENU_ELEMENTS.keys())

    def enter_login(self, login):
        """ Ввод в поле логина независимо от способа авторизации
            """
        login_field = self.find_element(Locators.LOCATOR_LOGIN_FIELD)
        login_field.send_keys(login)
        return login_field

    def enter_pass(self, password):
        pass_field = self.find_element(Locators.LOCATOR_PASS_FIELD)
        pass_field.send_keys((Keys.COMMAND if platform == "darwin" else Keys.CONTROL) + "a")
        pass_field.send_keys(Keys.DELETE)
        pass_field.send_keys(password)
        return pass_field

    def enter_button(self):
        return self.find_element(Locators.LOCATOR_ENTER_BUTTON, time=2)

    def click_on_enter_button(self):
        return self.find_element(Locators.LOCATOR_ENTER_BUTTON, time=2).click()

    def left_body(self):
        return self.find_element(Locators.LOCATOR_LEFT_BODY, time=10)

    def right_body(self):
        return self.find_element(Locators.LOCATOR_RIGHT_BODY, time=10)

    def body_logo(self):
        """ Вывод логотипа РТ в теле страницы
            """
        return self.find_element(Locators.LOCATOR_BODY_LOGO, time=10)

    def form_title(self):
        """ Вывод заголовка отображаемой формы ввода данных
            """
        return self.find_element(Locators.LOCATOR_FORM_TITLE, time=10)

    def auth_form(self):
        return self.find_element(Locators.LOCATOR_AUTH_FORM, time=10)

    def tabs_menu(self):
        """ Вывод меню с выбором типа авторизации
                """
        return self.find_element(Locators.LOCATOR_TABS_MENU, time=10)

    def login_field(self):
        """ Вывод поля для ввода логина, независимо от выбранного способа ввода
            """
        return self.find_element(Locators.LOCATOR_LOGIN_FIELD, time=10)

    def pass_field(self):
        return self.find_element(Locators.LOCATOR_PASS_FIELD, time=10)

    def checkbox_remember_me(self):
        return self.find_element(Locators.LOCATOR_REMEMBER_ME, time=10)

    def click_on_tab_menu_phone(self):
        """ Выбор авторизации через телефон
            """
        return self.find_element(Locators.LOCATORS_TABS_MENU_ELEMENTS['Телефон']['LOCATOR_TAB_MENU'],
                                 time=2).click()

    def click_on_tab_menu_email(self):
        """ Выбор авторизации через электронную почту
                """
        return self.find_element(Locators.LOCATORS_TABS_MENU_ELEMENTS['Почта']['LOCATOR_TAB_MENU'],
                                 time=2).click()

    def click_on_tab_menu_login(self):
        """ Выбор авторизации через логин
                """
        return self.find_element(Locators.LOCATORS_TABS_MENU_ELEMENTS['Логин']['LOCATOR_TAB_MENU'],
                                 time=2).click()

    def click_on_tab_menu_ls(self):
        """ Выбор авторизации через личный счет
                """
        return self.find_element(Locators.LOCATORS_TABS_MENU_ELEMENTS['Лицевой счёт']['LOCATOR_TAB_MENU'],
                                 time=2).click()

    def phone_field(self):
        return self.find_element(Locators.LOCATORS_TABS_MENU_ELEMENTS['Телефон']['LOCATOR_INPUT_FIELD'], time=10)

    def email_field(self):
        return self.find_element(Locators.LOCATORS_TABS_MENU_ELEMENTS['Почта']['LOCATOR_INPUT_FIELD'], time=2)

    def login_field_in_tab(self):
        """ Вывод поля ввода логина при регистрации через логин
            """
        return self.find_element(Locators.LOCATORS_TABS_MENU_ELEMENTS['Логин']['LOCATOR_INPUT_FIELD'], time=2)

    def input_ls_field(self):
        """ Вывод поля ввода личного счета при регистрации через личный счет
            """
        return self.find_element(Locators.LOCATORS_TABS_MENU_ELEMENTS['Лицевой счёт']['LOCATOR_INPUT_FIELD'], time=2)

    def form_error_message(self):
        """ Вывод ошибки при вводе неверного логина или пароля"""
        return self.find_element(Locators.LOCATOR_FORM_ERROR_MESSAGE, time=10)

    def forgot_password_muted(self):
        """ Вывод ссылки 'Забыли пароль' в обычном неподсвеченном состоянии
            """
        return self.find_element(Locators.LOCATOR_FORGOT_PASSWORD_MUTED, time=10)

    def forgot_password_active(self):
        """ Вывод ссылки 'Забыли пароль' в подсвеченном состоянии
            """
        return self.find_element(Locators.LOCATOR_FORGOT_PASSWORD_ACTIVE, time=10)

    def agreement_contract(self):
        """ Вывод ссылки на пользовательское соглашение из формы авторизации
            """
        return self.find_element(Locators.LOCATOR_FORM_AGREEMENT, time=10)

    def social_providers(self):
        """ Вывод блока ссылок на соц.сети
            """
        return self.find_element(Locators.LOCATOR_SOCIAL_PROVIDERS, time=2)


    def social_vk(self):
        """ Вывод ссылки на ВКонтакте
            """
        return self.find_element(Locators.LOCATOR_SOCIAL_VK, time=10)


    def social_ya(self):
        """ Вывод ссылки на Яндекс
            """
        return self.find_element(Locators.LOCATOR_SOCIAL_YA, time=10)

    def social_ok(self):
        """ Вывод ссылки на Одноклассники
                    """
        return self.find_element(Locators.LOCATOR_SOCIAL_OK, time=10)

    def social_mail(self):
        """ Вывод ссылки на Mail.ru
                    """
        return self.find_element(Locators.LOCATOR_SOCIAL_MAIL, time=10)

    def social_google(self):
        """ Вывод ссылки на Google
                    """
        return self.find_element(Locators.LOCATOR_SOCIAL_GOOGLE, time=10)

    def register_link(self):
        """ Вывод ссылки на форму регистрации из формы авторизации
            """
        return self.find_element(Locators.LOCATOR_FORM_REGISTER_LINK, time=10)

    def input_login_mask(self):
        """ Вывод ссылки на форму регистрации из формы авторизации
            """
        return self.find_element(Locators.LOCATOR_INPUT_LOGIN_TEXT, time=2).get_attribute("value")



