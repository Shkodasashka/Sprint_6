from selenium.webdriver.common.by import By


class BasePageLocators:
    # Локатор кнопки согласия на использование куки
    ACCEPT_COOKIES_BUTTON = (By.XPATH, "//button[contains(text(),'да все привыкли')]") #кнопка согласия использования куки

    #Локаторы логотипов к шапке страницы
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]") #логотип Самокат в шапке страницы
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]") #логотип Яндекс в шапке страницы
