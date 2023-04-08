import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    driver = webdriver.Chrome(executable_path="./WebDriver/chromedriver.exe")
    yield driver
    driver.quit()
