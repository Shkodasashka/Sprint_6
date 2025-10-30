from selenium.webdriver.common.by import By


class ManePageLocators:
    # Локаторы на главной странице
    ACCEPT_COOKIES_BUTTON = (By.XPATH, "//button[contains(text(),'да все привыкли')]") #кнопка согласия использования куки