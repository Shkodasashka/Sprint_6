import allure
from pages.base_page import BasePage
from locators.dzen_page_locators import DzenPageLocators


class DzenPage(BasePage):
    @allure.step('Получение титула страницы Дзена')
    def get_title_page_Dzen(self):
        return self.get_title_page(DzenPageLocators.DZEN_LOGO)
