import pytest
from sys import platform
from selenium import webdriver

MAC_WEBDRIVER = "./WebDriver/chromedriver"
WIN_WEBDRIVER = "./WebDriver/chromedriver.exe"


@pytest.fixture
def browser():
    driver = webdriver.Chrome(executable_path=(MAC_WEBDRIVER if platform == "darwin" else WIN_WEBDRIVER))

    yield driver
    driver.quit()
