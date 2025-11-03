import allure
import pytest
from data import FAQ
from pages.main_page import MainPage

class TestMainPageFAQ:
    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверка появления соответствующего ответа при нажатии на вопрос на главной странице')
    @pytest.mark.parametrize('locator_of_question, locator_of_answer, text_of_answer', FAQ.faq_on_main_page)
    def test_click_on_question_expect_him_answer(self, driver, locator_of_question, locator_of_answer, text_of_answer):
        main_page = MainPage(driver)
        main_page.wait_and_find_section_FAQ()
        main_page.scroll_to_section_FAQ()
        main_page.wait_and_find_question(locator_of_question)
        main_page.click_on_question(locator_of_question)
        main_page.wait_and_find_answer_for_selected_question(locator_of_answer)
        assert main_page.get_text_of_answer(locator_of_answer) == text_of_answer
