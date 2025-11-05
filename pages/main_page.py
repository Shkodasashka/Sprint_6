import allure
from data import url
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step('Открытие главной страницы сервиса')
    def open_mane_page(self):
        self.open_page(url.main_page)

    @allure.step('Клик на кнопку согласия использования куки в случае ее отображения на странице')
    def cookie_consent(self):
        self.click_if_button_displayed(BasePageLocators.ACCEPT_COOKIES_BUTTON)

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
    def wait_header_of_main_page(self):
        return self.wait_element(MainPageLocators.header_title)

    @allure.step('Клик на логотип яндекса')
    def click_on_logo_yandex(self):
        self.click_on_element(BasePageLocators.YANDEX_LOGO)
    
    @allure.step('Переключение с главной страницы на открывшуюся через редирект вкладку со странцией Дзена')
    def switch_to_Dzen(self):
        self.switch_to_redirect_window()
