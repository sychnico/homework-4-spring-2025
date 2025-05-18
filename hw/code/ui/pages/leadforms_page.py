from .page import Page
from ui.locators.leadforms_locators import LeadFormsLocators

class LeadformsPage(Page):
    URL = "https://ads.vk.com/hq/leadads/leadforms" # Урл страницы
    locators = LeadFormsLocators()

    def click_create_leadform_button(self):
        self.click(self.locators.CREATE_LEADFORM_BUTTON)

    def click_close_leadform_button(self):
        self.click(self.locators.CANCEL_LEADFORM_BUTTON)

    def is_displayed_leadform(self):
        self.find(self.locators.MODAL_FORM_LEAD)

    def upload_image(self, filepath: str):
        self.click(self.locators.LOAD_IMAGE_BUTTON)
        load_image_input = self.find(self.locators.LOAD_IMAGE_INPUT)
        load_image_input.send_keys(filepath)

    def get_last_image_name_from_media_library(self) -> str:
        self.hover(self.locators.UPLOADED_IMAGE_ITEM)
        return self.find(self.locators.UPLOADED_IMAGE_NAME).text

    def click_last_image_name_from_media_library(self):
        self.click(self.locators.LOAD_IMAGE_BUTTON)
        self.hover(self.locators.UPLOADED_IMAGE_ITEM)
        self.click(self.locators.UPLOADED_IMAGE_NAME)

    def delete_all_from_media_library(self):
        self.scroll_and_click(self.locators.EDIT_IMAGES_BUTTON, 10)
        self.click(self.locators.SELECT_ALL_IMAGES_BUTTON, 10)
        self.click(self.locators.DELETE_IMAGES_BUTTON, 10)
        self.click(self.locators.CONFIRM_DELETE_BUTTON, 10)

    def get_name_input_field(self):
        return self.find(self.locators.FORM_NAME_INPUT, 10)

    def get_company_input_field(self):
        return self.find(self.locators.COMPANY_NAME_INPUT, 10)

    def get_header_input_field(self):
        return self.find(self.locators.FORM_HEADER_INPUT, 10)

    def get_description_input_field(self):
        return self.find(self.locators.DESCRIPTION_INPUT, 10)

    def fill_input_field(self, field, text):
        field.send_keys(text)
        assert field.get_attribute("value") == text

    def get_input_name(self):
        return self.find(self.locators.NAME_INPUT)


    def continue_click(self):
        self.click(self.locators.CONTINUE_BUTTON)

    # И пишем атомарные функции класса, которые мы будем тестировать в другом месте, эти
    # функции должны быть элементарными и выполнять 1 действие, например клик по кнопке, 
    # нахождение инпута или ввод текст в инпут, это будут все отдельные функции, совмещаются они в /hw/code/TestYourNamePage.py