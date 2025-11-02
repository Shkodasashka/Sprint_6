import pytest
import allure
from curl import url
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание загрузки и поиск элемента')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.wait_and_find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Ожидание кликабельности элемента и клик на элемент')
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Получить текст элемента')
    def get_text_of_element(self, element):
        return self.driver.find_element(*element).text
