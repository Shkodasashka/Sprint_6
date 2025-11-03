from selenium.webdriver.common.by import By


class DzenPageLocators:
    # Локатор кнопки согласия на использование куки
    DZEN_LOGO = (By.XPATH, "//title[contains(text(), 'Дзен')]") #логотип дзена
