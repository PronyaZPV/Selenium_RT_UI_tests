from selenium.webdriver.common.by import By

from .base_page import BasePage


class Locators:
    LOCATOR_ALL_HEADER = (By.ID, "app-header")
    LOCATOR_HEADER_LOGO = (By.CLASS_NAME, "rt-footer-left")


class Header(BasePage):
    def header(self):
        """ Вывод хедера
            """
        return self.find_element(Locators.LOCATOR_ALL_HEADER, time=10)

    def header_logo(self):
        """ Вывод логотипа РТ в хедере
            """
        return self.find_element(Locators.LOCATOR_HEADER_LOGO, time=10)