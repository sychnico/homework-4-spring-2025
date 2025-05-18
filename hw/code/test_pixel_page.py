from dataclasses import field


class TestPixelPage:
    def test_modal_appears(self, pixel_page):
        """Тест появления модального окна"""
        pixel_page.click_create_pixel_button()
        assert pixel_page.get_modal_element()

    def test_domain_input(self, pixel_page):
        """Тест ввода домена"""
        pixel_page.click_create_pixel_button()
        field = pixel_page.get_domain_input_field()
        pixel_page.clear_input_field(field)
        pixel_page.fill_input_field(field, "giga-mail.ru")

    def test_successful_pixel_creation(self, pixel_page):
        """Тест успешного создания пикселя"""
        pixel_page.click_create_pixel_button()
        field = pixel_page.get_domain_input_field()
        pixel_page.clear_input_field(field)
        pixel_page.fill_input_field(field, "giga-mail.ru")
        pixel_page.click_submit_button()
        pixel_page.click_create_new_option()
        assert pixel_page.get_success_modal()

    def test_change_pixel(self, pixel_page):
        pixel_page.hover_pixel()
        pixel_page.click_more()
        pixel_page.click_rename_pixel()
        field = pixel_page.get_pixel_input_field()
        name = pixel_page.generate_random_string()
        pixel_page.fill_random_string(field, name)
        pixel_page.click_change_button()
        
    def test_delete_pixel(self, pixel_page):
        """Тест удаления пикселя"""
        pixel_page.hover_pixel()
        pixel_page.click_more()
        pixel_page.click_delete_pixel()
        pixel_page.click_delete_button()

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
        pixel_page.assert_new_page(r"https://ads\.vk\.com/hq/pixels/\d+/events")

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
        pixel_page.click_link_settings()
        pixel_page.switch_to_new_page_tag()
        pixel_page.click_create_tag_button()
        field = pixel_page.get_tag_input_field()
        pixel_page.fill_input_field(field, "")
        pixel_page.click_tag_button()
        assert pixel_page.get_error_message_tag()

    def test_create_action(self, pixel_page):
        pixel_page.click_link_settings()
        pixel_page.click_create_action_button()
        field = pixel_page.get_action_input_field()
        name = pixel_page.generate_random_string()
        pixel_page.fill_input_field(field, name)
        pixel_page.select_category("Покупка")
        pixel_page.select_condition("Посещена страница")
        field2 = pixel_page.get_url_input_field()
        pixel_page.fill_input_field(field2, name)
        pixel_page.click_action_button()
        pixel_page.assert_new_page(r"https://ads\.vk\.com/hq/pixels/\d+/events")

    def test_fail_url_create_action(self, pixel_page):
        pixel_page.click_link_settings()
        pixel_page.click_create_action_button()
        field = pixel_page.get_action_input_field()
        name = pixel_page.generate_random_string()
        pixel_page.fill_input_field(field, name)
        pixel_page.select_category("Покупка")
        pixel_page.select_condition("Посещена страница")
        field2 = pixel_page.get_url_input_field()
        pixel_page.fill_input_field(field2, "")
        pixel_page.click_action_button()
        pixel_page.get_error_message_url()

