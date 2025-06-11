from dataclasses import field
import time
import pytest

BUY_CATEGORY = "Покупка"
PAGE_VISITED_CONDITION = "Посещена страница"
EMPTY_FIELD_ERROR = "Нужно заполнить"

class TestPixelPage:

    def test_modal_appears(self, pixel_page):
        """Тест появления модального окна"""
        pixel_page.click_create_pixel_button()
        assert pixel_page.get_modal_element()
    
    @pytest.mark.parametrize("pixel_data", [
        {
            "url": "giga-mail.ru"
        },
        {
            "url": "lirili-lari.la"
        },
        {
            "url": "new-test-na.me"
        }
    ])
    def test_successful_pixel_creation(self, pixel_page, pixel_data):
        """Тест успешного создания пикселя"""
        pixel_page.click_create_pixel_button()
        field = pixel_page.get_domain_input_field()
        pixel_page.clear_input_field(field)
        name = pixel_data["url"]
        pixel_page.fill_input_field(field, name)
        pixel_page.click_submit_button()
        test_pixel = pixel_page.find_test_pixel(name)
        assert test_pixel.text == name

    @pytest.mark.parametrize("pixel_data", [
        {
            "url": "giga-mail.ru"
        },
        {
            "url": "lirili-lari.la"
        },
        {
            "url": "new-test-na.me"
        }
    ])
    def test_pixel_change(self, pixel_page, pixel_data):
        """Тест изменения пикселя"""
        pixel_page.hover_pixel()
        pixel_page.click_more()
        pixel_page.click_rename_pixel()
        field = pixel_page.get_pixel_input_field()
        pixel_page.clear_input_field(field)
        name = pixel_data["url"]
        pixel_page.fill_input_field(field, name)
        pixel_page.click_change_button()
        test_pixel = pixel_page.find_test_pixel(name)
        assert test_pixel.text == name
    
    @pytest.mark.parametrize("pixel_data", [
        {
            "url": "giga-mail.ru"
        },
        {
            "url": "lirili-lari.la"
        },
        {
            "url": "new-test-na.me"
        }
    ])
    def test_delete_pixel(self, pixel_page, pixel_data):
        """Тест удаления пикселя"""
        name = pixel_data["url"]
        pixel_page.hover_pixel()
        pixel_page.click_more()
        pixel_page.click_delete_pixel()
        pixel_page.click_delete_button()
        assert pixel_page.check_pixel_deleted(name)
    

    def test_invalid_domain(self, pixel_page):
        """Тест невалидного домена"""
        pixel_page.click_create_pixel_button()
        field = pixel_page.get_domain_input_field()
        pixel_page.clear_input_field(field)
        pixel_page.fill_input_field(field, "invalid")
        pixel_page.click_submit_button()
        assert pixel_page.get_error_message()

    def test_pixel_settings(self, pixel_page):
        """Тест перехода к настройкам первого пикселя"""
        pixel_page.click_link_settings()
        assert pixel_page.assert_new_page(r"https://ads\.vk\.com/hq/pixels/\d+/events")

    def test_create_tag(self, pixel_page):
        pixel_page.click_link_settings()
        pixel_page.switch_to_new_page_tag()
        pixel_page.click_create_tag_button()
        field = pixel_page.get_tag_input_field()
        name = pixel_page.generate_random_string()
        pixel_page.fill_input_field(field, name)
        pixel_page.click_tag_button()
        assert pixel_page.get_success_tag_modal()

    def test_fail_create_tag(self, pixel_page):
        """Тест создания тега с пустым полем"""
        pixel_page.click_link_settings()
        pixel_page.fill_input_field(field, "")
        pixel_page.click_tag_button()
        error = pixel_page.get_error_message_tag()
        assert EMPTY_FIELD_ERROR in error.text

    def test_create_action(self, pixel_page):
        pixel_page.click_link_settings()
        pixel_page.click_create_action_button()
        field = pixel_page.get_action_input_field()
        name = pixel_page.generate_random_string()
        pixel_page.fill_input_field(field, name)
        pixel_page.select_category(BUY_CATEGORY)
        pixel_page.select_condition(PAGE_VISITED_CONDITION)
        field2 = pixel_page.get_url_input_field()
        pixel_page.fill_input_field(field2, name)
        pixel_page.click_action_button()
        assert pixel_page.assert_new_page(r"https://ads\.vk\.com/hq/pixels/\d+/events")

    def test_fail_url_create_action(self, pixel_page):
        pixel_page.click_link_settings()
        pixel_page.click_create_action_button()
        field = pixel_page.get_action_input_field()
        name = pixel_page.generate_random_string()
        pixel_page.fill_input_field(field, name)
        pixel_page.select_category(BUY_CATEGORY)
        pixel_page.select_condition(PAGE_VISITED_CONDITION)
        field2 = pixel_page.get_url_input_field()
        pixel_page.fill_input_field(field2, "")
        pixel_page.click_action_button()
        assert pixel_page.get_error_message_url()

