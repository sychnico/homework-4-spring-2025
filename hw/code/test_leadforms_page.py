import os
import time
from time import sleep

FILEPATH = os.path.join(os.path.dirname(__file__), 'images/leds.jpg')

class TestLeadformsPage:

    def test_click_create_leadforms_page(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.is_displayed_leadform()

    def test_click_close_leadforms_page(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_close_leadform_button()

    def test_tab_page(self, leadforms_page):
        leadforms_page.click_surveys()
        leadforms_page.click_yclients()

    def test_upload_image(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.upload_image(FILEPATH)

    def test_create_leadforms_page(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        field = leadforms_page.get_name_input_field()
        leadforms_page.clear_input_field(field)
        leadforms_page.fill_input_field(field, "test")
        field = leadforms_page.get_company_input_field()
        leadforms_page.fill_input_field(field, "test2")
        field = leadforms_page.get_header_input_field()
        leadforms_page.fill_input_field(field, "test3")
        field = leadforms_page.get_description_input_field()
        leadforms_page.fill_input_field(field, "test4")
        leadforms_page.click_last_image_name_from_media_library()
        leadforms_page.continue_click()
        leadforms_page.continue_click()
        leadforms_page.continue_click()
        leadforms_page.find_locator_site()
        field = leadforms_page.get_input_name()
        leadforms_page.fill_input_field(field, "Ivan Ivanov Ivanovich")
        field = leadforms_page.get_adress()
        leadforms_page.fill_input_field(field, "Moscow moscowich")
        leadforms_page.save_form_click()

    def test_archive_leadforms_page(self, leadforms_page):
        leadforms_page.click_lead()
        leadforms_page.hover_panel()
        leadforms_page.click_archive_link()
        leadforms_page.click_archive_button()

    def test_click_create_questions_page(self, leadforms_page):
        leadforms_page.click_surveys()
        leadforms_page.click_create_questions_button()
        leadforms_page.is_displayed_leadform()

    def test_click_close_questions_page(self, leadforms_page):
        leadforms_page.click_surveys()
        leadforms_page.click_create_questions_button()
        leadforms_page.click_close_questions_button()

    def test_create_questions_page(self, leadforms_page):
        leadforms_page.click_surveys()
        leadforms_page.click_create_questions_button()
        field = leadforms_page.get_company_input()
        leadforms_page.fill_input_field(field, "test")
        field = leadforms_page.get_name_title_input()
        leadforms_page.fill_input_field(field, "test2")
        field = leadforms_page.get_title_input()
        leadforms_page.fill_input_field(field, "test3")
        field = leadforms_page.get_description_que_input()
        leadforms_page.fill_input_field(field, "test4")
        leadforms_page.click_last_image_name_from_media_library()
        leadforms_page.continue_click()
        field = leadforms_page.get_question_input()
        leadforms_page.fill_input_field(field, "test?")
        field = leadforms_page.get_answer_1_input()
        leadforms_page.fill_input_field(field, "yes")
        field = leadforms_page.get_answer_2_input()
        leadforms_page.fill_input_field(field, "no")
        leadforms_page.continue_click()
        leadforms_page.save_questions_click()
        leadforms_page.find_locator()

    def test_archive_questions_page(self, leadforms_page):
        leadforms_page.click_surveys()
        leadforms_page.hover_panel()
        leadforms_page.click_archive_link()
        leadforms_page.click_archive_button()
