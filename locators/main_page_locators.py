from selenium.webdriver.common.by import By


class MainPageLocators:
    # Локаторы вопросов на главной странице
    question_button_1 = [By.XPATH, "//div[@id='accordion__heading-0']"]
    question_button_2 = [By.XPATH, "//div[@id='accordion__heading-1']"]
    question_button_3 = [By.XPATH, "//div[@id='accordion__heading-2']"]
    question_button_4 = [By.XPATH, "//div[@id='accordion__heading-3']"]
    question_button_5 = [By.XPATH, "//div[@id='accordion__heading-4']"]
    question_button_6 = [By.XPATH, "//div[@id='accordion__heading-5']"]
    question_button_7 = [By.XPATH, "//div[@id='accordion__heading-6']"]
    question_button_8 = [By.XPATH, "//div[@id='accordion__heading-7']"]
    # Локаторы ответов на главной странице
    answer_for_question_1 = [By.XPATH, "//div[@id='accordion__panel-0']"]
    answer_for_question_2 = [By.XPATH, "//div[@id='accordion__panel-1']"]
    answer_for_question_3 = [By.XPATH, "//div[@id='accordion__panel-2']"]
    answer_for_question_4 = [By.XPATH, "//div[@id='accordion__panel-3']"]
    answer_for_question_5 = [By.XPATH, "//div[@id='accordion__panel-4']"]
    answer_for_question_6 = [By.XPATH, "//div[@id='accordion__panel-5']"]
    answer_for_question_7 = [By.XPATH, "//div[@id='accordion__panel-6']"]
    answer_for_question_8 = [By.XPATH, "//div[@id='accordion__panel-7']"]
    # Локатор секции с вопросами и ответами на главной странице
    header_FAQ = [By.XPATH, "//div[contains(text(),'Вопросы о важном')]"]
    # Локаторы кнопок заказать на главной странице
    header_button_order = [By.XPATH, "//div[contains(@class,'Header_Nav')]/button[contains(@class,'Button_Button')]"] #кнопка в шапке главной страницы для перехода на страницу оформления заказа
    page_button_order = [By.XPATH, "//div[contains(@class,'Home_FinishButton')]/button[contains(@class,'Button_Button')]"] #кнопка в центральной части главной страницы для перехода на страницу оформления заказа
    # Локатор заголовка на главной странице
    header_title = [By.XPATH, "//div[contains(@class,'Home_Header')]"] #заголовок центральной страницы
