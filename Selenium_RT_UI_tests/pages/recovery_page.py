from selenium.webdriver.common.by import By

from .base_page import BasePage


class Locators:
    LOCATOR_FORM_TITLE = (By.CLASS_NAME, "card-container__title")


class RecoveryPage(BasePage):
    def form_title(self):
        return self.find_element(Locators.LOCATOR_FORM_TITLE, time=10)
