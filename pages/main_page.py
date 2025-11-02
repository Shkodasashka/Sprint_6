import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    @allure.step('Ожидание появления и поиск на странице раздела с вопросами о важном')
    def wait_and_find_section_FAQ(self):
        self.wait_and_find_element(MainPageLocators.header_FAQ)
   
    @allure.step('Скролл страницы до раздела с вопросами')
    def scroll_to_section_FAQ(self):
        self.scroll_to_element(MainPageLocators.header_FAQ)

    @allure.step('Клик по вопросу')
    def click_on_question(self, locator_of_question):
        self.click_on_element(locator_of_question)

    @allure.step('Ожидание появления и поиск ответа, соответствующего вопросу')
    def wait_and_find_answer_for_selected_question(self, locator_of_answer):
        self.wait_and_find_element(locator_of_answer)

    @allure.step('Получить текст ответа')
    def get_text_of_answer(self, locator):
        self.get_text_of_element(locator)

    @allure.step('Клик по кнопке заказать в шапке страницы')
    def click_on_header_button_order(self):
        self.click_on_element(MainPageLocators.header_button_order)

    @allure.step('Клик по кнопке заказать в центральной части страницы')
    def click_on_page_button_order(self):
        self.click_on_element(MainPageLocators.page_button_order)
