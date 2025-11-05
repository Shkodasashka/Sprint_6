import allure
from data import TITLE_DATA
from pages.order_page import OrderPage
from pages.main_page import MainPage
from pages.dzen_page import DzenPage
from locators.main_page_locators import MainPageLocators


class TestLogoClick:
    @allure.title('Проверка открытия главной страницы сервиса после нажатия на логотип Самоката')
    @allure.description('Проверка открытия главной страницы сервиса после нажатия на логотоип Самоката в шапке сайта')
    def test_open_mane_page_after_logo_scooter_click(self, driver):
        main_page = MainPage(driver)
        main_page.open_mane_page()
        main_page.cookie_consent()
        main_page.click_on_button_order(MainPageLocators.header_button_order)
        order_page = OrderPage(driver)
        order_page.click_on_logo_scooter()
        assert main_page.wait_header_of_main_page()

    @allure.title('Проверка открытия страницы Дзена после клика на логотип Яндекса')
    @allure.description('Проверка открытия страницы Дзена после нажатия на логотоип Яндекса в шапке сайта')
    def test_open_dzen_page_after_logo_yandex_click(self, driver):
        main_page = MainPage(driver)
        main_page.open_mane_page()
        main_page.cookie_consent()
        main_page.click_on_logo_yandex()
        main_page.switch_to_Dzen()
        dzen_page = DzenPage(driver)
        assert dzen_page.get_title_page_Dzen() == TITLE_DATA.dzen_title_information
