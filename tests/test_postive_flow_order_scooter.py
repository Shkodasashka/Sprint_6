import allure
import pytest
from data import ORDER_DATA, TITLE_DATA
from pages.order_page import OrderPage
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.dzen_page import DzenPage
from locators.main_page_locators import MainPageLocators


class TestPositiveFlowOrderScooter:
    @allure.title('Проверка заказа самоката')
    @allure.description('Проверка всего флоу позитивного сценария с двумя наборами данных и двумя точками перехода на форму заказа')
    @pytest.mark.parametrize('button, test_data', [[MainPageLocators.header_button_order,ORDER_DATA.test_data_user_1],
                                                   [MainPageLocators.page_button_order, ORDER_DATA.test_data_user_2]])
    def test_postive_flow_order_scooter(self, driver, button, test_data):
        main_page = MainPage(driver)
        main_page.open_mane_page()
        main_page.cookie_consent()
        main_page.click_on_button_order(button)
        order_page = OrderPage(driver)
        order_page.input_data_in_first_form(test_data)
        order_page.input_data_in_second_form(test_data)
        order_page.wait_and_find_header_confirmation_order()
        order_page.click_on_confirmation_order_button()
        order_page.wait_and_find_header_success_order()
        order_page.click_on_status_order_button()
        base_page = BasePage(driver)
        base_page.click_on_logo_scooter()
        main_page.wait_and_find_header_of_main_page()
        base_page.click_on_logo_yandex()
        base_page.switch_to_redirect_window()
        dzen_page = DzenPage(driver)
        assert dzen_page.get_title_page_Dzen() == TITLE_DATA.dzen_title_information
