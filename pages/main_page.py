import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
   
    @allure.step('Скролл страницы до раздела с вопросами')
    def scroll_to_section_FAQ(self):
        self.scroll_to_element(MainPageLocators.header_FAQ)

    @allure.step('Клик по вопросу')
    def click_on_hidden_question(self, locator_of_question):
        self.click_on_hidden_element(locator_of_question)

    @allure.step('Получить текст ответа')
    def get_text_of_answer(self, locator):
        return self.get_text_of_element(locator)

    @allure.step('Клик по кнопке заказать')
    def click_on_button_order(self, button_locator):
        self.click_on_element(button_locator)

    @allure.step('Ожидание появления и поиск заголовка главной страницы')
    def wait_and_find_header_of_main_page(self):
        self.wait_and_find_element(MainPageLocators.header_title)
