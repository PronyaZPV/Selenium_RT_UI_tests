from selenium.webdriver.common.by import By

from .base_page import BasePage


class Locators:
    LOCATOR_ALL_FOOTER = (By.ID, "app-footer")
    LOCATOR_FOOTER_INFO = (By.CLASS_NAME, "rt-footer-left")
    LOCATOR_FOOTER_PHONE = (By.XPATH, "//*[@id='app-footer']/div[2]/a")
    LOCATOR_FOOTER_COPYRIGHT = (By.CSS_SELECTOR, "div[class *='copyright']")
    LOCATOR_FOOTER_COOKIES = (By.CSS_SELECTOR, "span[class *='cookies']")
    LOCATOR_FOOTER_AGREEMENT = (By.ID, "rt-footer-agreement-link")


class Footer(BasePage):
    """ Класс, содержащий все необходимые методы для проверки футера
        """
    def footer(self):
        """ Вывод футера
            """
        return self.find_element(Locators.LOCATOR_ALL_FOOTER, time=10)

    def footer_info(self):
        """ Вывод блока информации в футере
            """
        return self.find_element(Locators.LOCATOR_FOOTER_INFO, time=10)

    def footer_phone(self):
        """ Вывод номера телефона поддержки, указанного в футере
            """
        return self.find_element(Locators.LOCATOR_FOOTER_PHONE, time=10)

    def footer_copyright(self):
        """ Вывод информации об ©авторском праве
            """
        return self.find_element(Locators.LOCATOR_FOOTER_COPYRIGHT, time=10)

    def footer_cookies(self):
        """ Вывод гиперссылки на Cookies
            """
        return self.find_element(Locators.LOCATOR_FOOTER_COOKIES, time=10)

    def footer_agreement(self):
        """ Вывод гиперссылки на пользовательское соглашение в футере
            """
        return self.find_element(Locators.LOCATOR_FOOTER_AGREEMENT, time=10)
