import os
import time
FILEPATH = os.path.join(os.path.dirname(__file__), 'images/leds.jpg')

class TestLeadformsPage:

    def test_click_create_leadforms_page(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.is_displayed_leadform()

    def test_click_close_leadforms_page(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_close_leadform_button()

    def test_upload_image(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.upload_image(FILEPATH)



    def test_create_leadforms_page(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image_name_from_media_library()

        field = leadforms_page.get_name_input_field()
        leadforms_page.clear_input_field(field)
        leadforms_page.fill_input_field(field, "test")
        field = leadforms_page.get_company_input_field()
        leadforms_page.fill_input_field(field, "test2")
        field = leadforms_page.get_header_input_field()
        leadforms_page.fill_input_field(field, "test3")
        field = leadforms_page.get_description_input_field()
        leadforms_page.fill_input_field(field, "test4")
        leadforms_page.continue_click()




