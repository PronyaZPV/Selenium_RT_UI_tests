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
    def footer(self):
        return self.find_element(Locators.LOCATOR_ALL_FOOTER, time=10)

    def footer_info(self):
        return self.find_element(Locators.LOCATOR_FOOTER_INFO, time=10)

    def footer_phone(self):
        return self.find_element(Locators.LOCATOR_FOOTER_PHONE, time=10)

    def footer_copyright(self):
        return self.find_element(Locators.LOCATOR_FOOTER_COPYRIGHT, time=10)

    def footer_cookies(self):
        return self.find_element(Locators.LOCATOR_FOOTER_COOKIES, time=10)

    def footer_agreement(self):
        return self.find_element(Locators.LOCATOR_FOOTER_AGREEMENT, time=10)