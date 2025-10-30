import pytest
from curl import url
from locators.base_page_locators import ManePageLocators
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='function')
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.get(url.main_page)
    if WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ManePageLocators.ACCEPT_COOKIES_BUTTON)):
        driver.find_element(*ManePageLocators.ACCEPT_COOKIES_BUTTON).click()
    yield firefox_driver
    firefox_driver.quit()
