import pytest
from curl import url
from locators.base_page_locators import BasePageLocators
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='function')
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.get(url.main_page)
    try:
        WebDriverWait(firefox_driver, 10).until(EC.element_to_be_clickable(BasePageLocators.ACCEPT_COOKIES_BUTTON))
        firefox_driver.find_element(*BasePageLocators.ACCEPT_COOKIES_BUTTON).click()
    except Exception:
        pass
    yield firefox_driver
    firefox_driver.quit()
