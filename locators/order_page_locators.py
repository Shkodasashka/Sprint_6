from selenium.webdriver.common.by import By
from data import ORDER_DATA

class OrderPageLocators:
    #Локаторы полей для заполнения данных заказа в первой форме
    NAME_ORDER = (By.XPATH, "//input[@placeholder='* Имя']")  #поле ввода имени 
    SURNAME_ORDER = (By.XPATH, "//input[@placeholder='* Фамилия']")  #поле ввода фамилии
    ADRESS_ORDER = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")  #поле ввода адреса заказа
    STATION_LIST_ORDER = (By.XPATH, "//input[@placeholder='*  Станция метро']")  #поле выбора станции метро
    SELECT_STATION_FROM_SEARCH = (By.XPATH, "li[@class='select-search__row']")  #выбор станции в выпадающем списке после ввода в полне ее названия
    TELEPHONE_ORDER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")  #поле ввода телефона для звонка курьера
    FURTHER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")  #кнопка перехода на следующую страницу заказа
    
    #Локаторы полей для заполнения данных заказа во второй форме
    DATE_ORDER = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")  #поле ввода даты аренды
    TIME_ORDER = (By.XPATH, "//div[@class='Dropdown-placeholder']")  #поле ввода срока аренды
    SELEСT_TIME_ORDER = (By.XPATH, "//div[contains(text(),'сутки']")  #выбор суток аренды
    COLOUR_ORDER = (By.XPATH, "//input[@id='black']") #выбор цвета самоката "черный жемчуг"
    COMMENT_ORDER = (By.XPATH, "//input[@placeholder='Комментарий для курьера']") #поле ввода коментария для курьера
    FINAL_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']") #итоговая кнопка для оформления заказа
    
    #Локаторы подтверждения заказа
    CONFIRMATION_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Да')]") #итоговая кнопка для оформления заказа
    CONFIRMATION_SUCCESS_ORDER = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']") #окно подтверждения успешного выполнения заказа
