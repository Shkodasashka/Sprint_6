import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step('Ожидание появления и поиск заголовка первой формы для заполнения заказа')
    def wait_and_find_header_first_form_order(self):
        self.wait_and_find_element(OrderPageLocators.HEADER_FIRST_FORM_ORDER)

    @allure.step('Клик на поле для ввода имени')
    def click_on_field_name_order(self):
        self.click_on_element(OrderPageLocators.NAME_ORDER)

    @allure.step('Ввод имени в поле')
    def input_name_order(self, test_data_user):
        self.input_keys_in_field(OrderPageLocators.NAME_ORDER, test_data_user[0])

    @allure.step('Клик на поле для ввода фамилии')
    def click_on_field_surname_order(self):
        self.click_on_element(OrderPageLocators.SURNAME_ORDER)

    @allure.step('Ввод фамилии в поле')
    def input_surname_order(self, test_data_user):
        self.input_keys_in_field(OrderPageLocators.SURNAME_ORDER, test_data_user[1])

    @allure.step('Клик на поле для ввода адреса')
    def click_on_field_adress_order(self):
        self.click_on_element(OrderPageLocators.ADRESS_ORDER)

    @allure.step('Ввод адреса в поле')
    def input_adress_order(self, test_data_user):
        self.input_keys_in_field(OrderPageLocators.ADRESS_ORDER, test_data_user[2])

    @allure.step('Клик на поле ввода станции метро')
    def click_on_field_station_list_order(self):
        self.click_on_element(OrderPageLocators.STATION_LIST_ORDER)

    @allure.step('Ввод станции в поле')
    def input_station_list_order(self, test_data_user):
        self.input_keys_in_field(OrderPageLocators.STATION_LIST_ORDER, test_data_user[3])

    @allure.step('Выбор станции в отфильтрованном списке')
    def click_on_select_station_from_search(self):
        self.click_on_element(OrderPageLocators.SELECT_STATION_FROM_SEARCH)

    @allure.step('Клик на поле ввода телефона')
    def click_on_field_telephone_order(self):
        self.click_on_element(OrderPageLocators.TELEPHONE_ORDER)

    @allure.step('Ввод номера телефона в поле')
    def input_telephone_order(self, test_data_user):
        self.input_keys_in_field(OrderPageLocators.TELEPHONE_ORDER, test_data_user[4])

    @allure.step('Клик на кнопку перехода ко второй форме')
    def click_on_button_crossing_next_form(self):
        self.click_on_element(OrderPageLocators.FURTHER_BUTTON)

    @allure.step('Ожидание появления и поиск заголовка второй формы для заполнения заказа')
    def wait_and_find_header_second_form_order(self):
        self.wait_and_find_element(OrderPageLocators.HEADER_SECOND_FORM_ORDER)

    @allure.step('Клик на поле ввода даты')
    def click_on_field_date_order(self):
        self.click_on_element(OrderPageLocators.DATE_ORDER)

    @allure.step('Ввод даты в поле')
    def input_date_order(self, test_data_user):
        self.input_keys_in_field(OrderPageLocators.DATE_ORDER, test_data_user[5])

    @allure.step('Клик на выбранную дату в появившемся окне календаря')
    def click_on_date_on_calendar(self):
        self.click_on_element(OrderPageLocators.DATE_ON_CALENDAR)

    @allure.step('Клик на поле выбора срока аренды')
    def click_on_field_time_order(self):
        self.click_on_element(OrderPageLocators.TIME_ORDER)

    @allure.step('Клик выбор одних суток аренды из выпадающего списка')
    def click_on_field_select_time_order(self):
        self.click_on_element(OrderPageLocators.SELEСT_TIME_ORDER)

    @allure.step('Клик на чекбокс цвета "Черная жемчужина" для самоката')
    def click_on_colour_order(self):
        self.click_on_element(OrderPageLocators.COLOUR_ORDER)

    @allure.step('Клик на поле ввода комментария к заказу')
    def click_on_field_comment_order(self):
        self.click_on_element(OrderPageLocators.COMMENT_ORDER)

    @allure.step('Ввод комментария в поле')
    def input_comment_order(self, test_data_user):
        self.input_keys_in_field(OrderPageLocators.COMMENT_ORDER, test_data_user[6])

    @allure.step('Клик на кнопку формирования заказа')
    def click_on_final_order_button(self):
        self.click_on_element(OrderPageLocators.FINAL_ORDER_BUTTON)

    @allure.step('Ожидание появления окна подтверждения заказа')
    def wait_and_find_header_confirmation_order(self):
        self.wait_and_find_element(OrderPageLocators.HEADER_CONFIRMATION_ORDER)

    @allure.step('Клик на кнопку подтверждения заказа')
    def click_on_confirmation_order_button(self):
        self.click_on_element(OrderPageLocators.CONFIRMATION_ORDER_BUTTON)

    @allure.step('Ожидание появления окна успешно сформированного заказа')
    def wait_and_find_header_success_order(self):
        self.wait_and_find_element(OrderPageLocators.CONFIRMATION_SUCCESS_ORDER)

    @allure.step('Клик на кнопку просмотра статуса заказа')
    def click_on_status_order_button(self):
        self.click_on_element(OrderPageLocators.STATUS_ORDER_BUTTON)
