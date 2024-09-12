import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def driver():
    service = Service('geckodriver')
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()