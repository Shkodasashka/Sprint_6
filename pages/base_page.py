import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы в браузере')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Ожидание кликабельности элемента и клик на элемент')
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Нажатие на кнопку в случае ее отображения на странице')
    def click_if_button_displayed(self, locator):
        try:
            self.click_on_element(locator)
        except Exception:
            pass

    @allure.step('Ожидание загрузки элемента')
    def wait_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидание загрузки и поиск элемента')
    def wait_and_find_element(self, locator):
        self.wait_element(locator)
        return self.driver.find_element(*locator)

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.wait_and_find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
  
    @allure.step('Клик на скрытый элемент')
    def click_on_hidden_element(self, locator):
        element = self.wait_and_find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Получить текст элемента')
    def get_text_of_element(self, locator):
        element = self.wait_and_find_element(locator)
        return self.driver.execute_script("return arguments[0].textContent", element)

    @allure.step('Ввести значение в поле ввода')
    def input_keys_in_field(self, locator, keys):
        return self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Переключение на открывшуюся через редирект вкладку')
    def switch_to_redirect_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получение текущего титула страницы')
    def get_title_page(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
        return self.driver.title
