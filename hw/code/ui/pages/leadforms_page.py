from .page import Page
from ui.locators.leadforms_locators import LeadFormsLocators

class LeadformsPage(Page):
    URL = "https://ads.vk.com/hq/leadads/leadforms" # Урл страницы
    locators = LeadFormsLocators()

    def click_create_leadform_button(self):
        self.click(self.locators.CREATE_LEADFORM_BUTTON)

    def click_create_questions_button(self):
        self.click(self.locators.CREATE_QUESTIONS_BUTTON)

    def click_surveys(self):
        self.click(self.locators.SURVEYS_TAB)

    def click_yclients(self):
        self.click(self.locators.YCLIENTS_TAB)

    def click_close_questions_button(self):
        self.click(self.locators.ClOSE_QUESTIONS_BUTTON)

    def click_close_leadform_button(self):
        self.click(self.locators.CANCEL_LEADFORM_BUTTON)

    def is_displayed_leadform(self):
        self.find(self.locators.MODAL_FORM_LEAD, timeout= 30)

    def hover_panel(self):
        self.hover(self.locators.HOVER_BUTTON)

    def upload_image(self, filepath: str):
        self.click(self.locators.LOAD_IMAGE_BUTTON)
        load_image_input = self.find(self.locators.LOAD_IMAGE_INPUT)
        load_image_input.send_keys(filepath)
        self.click(self.locators.SAVE_IMAGE_BUTTON, 15)

    def click_last_image_name_from_media_library(self):
        self.click(self.locators.LOAD_IMAGE_BUTTON)
        self.hover(self.locators.UPLOADED_IMAGE_ITEM)
        self.click(self.locators.UPLOADED_IMAGE_NAME, timeout=30)

    def clear_input_field(self, field):
        field.clear()
        self.wait().until(lambda _: field.get_attribute("value") == "",)
    def get_name_input_field(self):
        return self.find(self.locators.FORM_NAME_INPUT, 60)

    def get_company_input_field(self):
        return self.find(self.locators.COMPANY_NAME_INPUT, 10)

    def get_header_input_field(self):
        return self.find(self.locators.FORM_HEADER_INPUT, 10)

    def get_description_input_field(self):
        return self.find(self.locators.DESCRIPTION_INPUT, 10)

    def fill_input_field(self, field, text):
        self.wait().until(lambda _: field.is_displayed() and field.is_enabled())
        field.send_keys(text)
        self.wait().until(lambda _: field.get_attribute("value") == text)

    def get_input_name(self):
        return self.find(self.locators.NAME_INPUT)

    def get_adress(self):
        return self.find(self.locators.ADRESS_INPUT)

    def continue_click(self):
        self.scroll_and_click(self.locators.CONTINUE_BUTTON, timeout=10)

    def save_form_click(self):
        self.click(self.locators.SAVE_IMAGE_BUTTON, timeout=20)

    def save_questions_click(self):
        self.click(self.locators.SUBMIT_BUTTON, timeout=20)


    def get_company_input(self):
        return self.find(self.locators.COMPANY_INPUT)

    def get_name_title_input(self):
        return self.find(self.locators.NAME_TITLE_INPUT)

    def get_title_input(self):
        return self.find(self.locators.TITLE_INPUT)

    def get_description_que_input(self):
        return self.find(self.locators.DESCRIPTION_QUE_INPUT)

    def get_question_input(self):
        return self.find(self.locators.QUESTION_INPUT)

    def get_answer_1_input(self):
        return self.find(self.locators.ANSWER_1_INPUT)

    def get_answer_2_input(self):
        return self.find(self.locators.ANSWER_2_INPUT)

    def find_locator(self):
        return self.find((self.locators.ACTIVE_STATUS_CELL), timeout=20)

    def click_archive_link(self):
        self.click(self.locators.ARCHIVE_LINK)

    def click_archive_button(self):
        self.click(self.locators.ARCHIVE_BUTTON)
