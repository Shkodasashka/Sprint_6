from locators.main_page_locators import MainPageLocators


class FAQ:
    text_answer_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    text_answer_2 = 'Пока что у нас так: один заказ — один самокат. ' \
                    'Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    text_answer_3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. ' \
                    'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. ' \
                    'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    text_answer_4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'     
    text_answer_5 = 'Пока что нет! Но если что-то срочное — ' \
                    'всегда можно позвонить в поддержку по красивому номеру 1010.'            
    text_answer_6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток ' \
                    '— даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    text_answer_7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. ' \
                    'Все же свои.'
    text_answer_8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
    
    faq_on_main_page = [[MainPageLocators.question_button_1, MainPageLocators.answer_for_question_1, text_answer_1],
                        [MainPageLocators.question_button_2, MainPageLocators.answer_for_question_2, text_answer_2],
                        [MainPageLocators.question_button_3, MainPageLocators.answer_for_question_3, text_answer_3],
                        [MainPageLocators.question_button_4, MainPageLocators.answer_for_question_4, text_answer_4],
                        [MainPageLocators.question_button_5, MainPageLocators.answer_for_question_5, text_answer_5],
                        [MainPageLocators.question_button_6, MainPageLocators.answer_for_question_6, text_answer_6],
                        [MainPageLocators.question_button_7, MainPageLocators.answer_for_question_7, text_answer_7],
                        [MainPageLocators.question_button_8, MainPageLocators.answer_for_question_8, text_answer_8]]

class ORDER_DATA:
    test_data_user_1=['Линкин', 'Парк', 'Москва', 'Сокольники', '89833545375', '20.11.2025', 'Зарядите пожалуйста']
    test_data_user_2=['Радио', 'Рекорд', 'Балтийск', 'Красносельская','89327456318', '12.11.2025', 'Морская дискотека']
