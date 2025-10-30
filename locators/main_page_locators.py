from selenium.webdriver.common.by import By


class ManePageLocators:
    # Локаторы на главной странице
    question_buttons = {
        1: [By.XPATH, "//div[@id='accordion__heading-48']"],
        2: [By.XPATH, "//div[@id='accordion__heading-49']"],
        3: [By.XPATH, "//div[@id='accordion__heading-50']"],
        4: [By.XPATH, "//div[@id='accordion__heading-51']"],
        5: [By.XPATH, "//div[@id='accordion__heading-52']"],
        6: [By.XPATH, "//div[@id='accordion__heading-53']"],
        7: [By.XPATH, "//div[@id='accordion__heading-54']"],
        8: [By.XPATH, "//div[@id='accordion__heading-55']"]
    }
    answers_area = {
        1: [By.XPATH, "//div[@id='accordion__panel-48']"],
        2: [By.XPATH, "//div[@id='accordion__panel-49']"],
        3: [By.XPATH, "//div[@id='accordion__panel-50']"],
        4: [By.XPATH, "//div[@id='accordion__panel-51']"],
        5: [By.XPATH, "//div[@id='accordion__panel-52']"],
        6: [By.XPATH, "//div[@id='accordion__panel-53']"],
        7: [By.XPATH, "//div[@id='accordion__panel-54']"],
        8: [By.XPATH, "//div[@id='accordion__panel-55']"]
    }
