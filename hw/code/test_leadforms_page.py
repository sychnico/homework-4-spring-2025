import os
import time
from time import sleep
import pytest

FILEPATH = os.path.join(os.path.dirname(__file__), 'images/leds.jpg')
CREATE_SURVEY = "Создать опрос"
GOTO_YCLIENTS = "Перейти в YCLIENTS"
LOAD_LOGO = "Загрузить логотип"
ACTIVE = "Активен"

class TestLeadformsPage:

    def test_click_create_leadforms_page(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        assert leadforms_page.is_displayed_leadform()

    def test_tab_surveys(self, leadforms_page):
        leadforms_page.click_surveys()
        elem = leadforms_page.find_create_questions_button()
        assert elem.text == CREATE_SURVEY

    def test_tab_yclients(self, leadforms_page):
        leadforms_page.click_yclients()
        elem = leadforms_page.find_yclients_button()
        assert elem.text == GOTO_YCLIENTS

    def test_upload_image(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.upload_image(FILEPATH)
        assert leadforms_page.check_elem_deleted(LOAD_LOGO)

    @pytest.mark.parametrize("leadform_data", [
        {
            "name": "test",
            "company": "test2",
            "title": "test3",
            "description": "test4",
            "owner": "Ivan Ivanov Ivanovich",
            "adress": "Moscow moscowich"
        }
    ])
    def test_create_leadforms_page(self, leadforms_page, leadform_data):
        """Проверка создания лидформы"""
        leadforms_page.click_create_leadform_button()
        field = leadforms_page.get_name_input_field()
        leadforms_page.clear_input_field(field)
        leadforms_page.fill_input_field(field, leadform_data["name"])
        field = leadforms_page.get_company_input_field()
        leadforms_page.fill_input_field(field, leadform_data["company"])
        field = leadforms_page.get_header_input_field()
        leadforms_page.fill_input_field(field, leadform_data["title"])
        field = leadforms_page.get_description_input_field()
        leadforms_page.fill_input_field(field, leadform_data["description"])
        leadforms_page.click_last_image_name_from_media_library()
        leadforms_page.continue_click()
        leadforms_page.continue_click()
        leadforms_page.continue_click()
        field = leadforms_page.get_input_name()
        leadforms_page.fill_input_field(field, leadform_data["owner"])
        field = leadforms_page.get_adress()
        leadforms_page.fill_input_field(field, leadform_data["adress"])
        leadforms_page.save_form_click()
        test_leadform = leadforms_page.find_test_leadform(leadform_data["name"])
        assert test_leadform.text == leadform_data["name"]

        """Проверка архивирования лидформы"""
        leadforms_page.click_lead()
        leadforms_page.hover_panel()
        leadforms_page.click_archive_link()
        leadforms_page.click_archive_button()
        assert leadforms_page.check_elem_deleted(leadform_data["name"])
      
    def test_click_create_questions_page(self, leadforms_page):
        leadforms_page.click_surveys()
        leadforms_page.click_create_questions_button()
        assert leadforms_page.is_displayed_leadform()


    @pytest.mark.parametrize("questions_data", [
        {
            "name": "test",
            "company": "test2",
            "title": "test3",
            "description": "test4",
            "question": "test?",
            "answer1": "yes",
            "answer2": "no"
        }
    ])
    def test_create_questions_page(self, leadforms_page, questions_data):
        """Проверка создания опроса"""
        leadforms_page.click_surveys()
        leadforms_page.click_create_questions_button()
        field = leadforms_page.get_company_input()
        leadforms_page.fill_input_field(field, questions_data["name"])
        field = leadforms_page.get_name_title_input()
        leadforms_page.fill_input_field(field, questions_data["company"])
        field = leadforms_page.get_title_input()
        leadforms_page.fill_input_field(field, questions_data["title"])
        field = leadforms_page.get_description_que_input()
        leadforms_page.fill_input_field(field, questions_data["description"])
        leadforms_page.click_last_image_name_from_media_library()
        leadforms_page.continue_click()
        field = leadforms_page.get_question_input()
        leadforms_page.fill_input_field(field, questions_data["question"])
        field = leadforms_page.get_answer_1_input()
        leadforms_page.fill_input_field(field, questions_data["answer1"])
        field = leadforms_page.get_answer_2_input()
        leadforms_page.fill_input_field(field, questions_data["answer2"])
        leadforms_page.continue_click()
        leadforms_page.save_questions_click()
        test_question = leadforms_page.find_test_leadform(questions_data["name"])
        assert test_question.text == questions_data["name"]
        elem = leadforms_page.find_locator()
        assert elem.text == ACTIVE

        """Проверка архивирования опроса"""
        leadforms_page.click_surveys()
        leadforms_page.hover_panel()
        leadforms_page.click_archive_link()
        leadforms_page.click_archive_button()
        elem = leadforms_page.find_test_leadform(questions_data["name"])
        assert elem.text == questions_data["name"]
        