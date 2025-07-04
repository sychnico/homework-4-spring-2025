from dataclasses import field
import time
import pytest

BUY_CATEGORY = "Покупка"
PAGE_VISITED_CONDITION = "Посещена страница"
EMPTY_FIELD_ERROR = "Нужно заполнить"
INVALID_DOMAIN = "invalid"
PIXEL_PAGE = r"https://ads\.vk\.com/hq/pixels/\d+/events"
INVALID_DOMAIN_MESSAGE = "Введите корректный адрес сайта"
EMPTY_URL_MESSAGE = "Заполните это поле"
TEST_DATA = [
    {
        "url": "agiga-mail.ru"
    },
    {
        "url": "alirili-lari.la"
    },
    {
        "url": "anew-test-na.me"
    }
]

@pytest.fixture(autouse=False)
def create_pixel(pixel_page):
    pixel_page.click_create_pixel_button()
    field = pixel_page.get_domain_input_field()
    pixel_page.clear_input_field(field)
    name = "test-pixel-na.me"
    pixel_page.fill_input_field(field, name)
    pixel_page.click_submit_button()
    return name

@pytest.fixture(autouse=False)
def auto_clean_pixel(pixel_page):
    pixels_created = []
    
    yield pixels_created

    for name in pixels_created:
        pixel_page.hover_pixel()
        pixel_page.click_more()
        pixel_page.click_delete_pixel()
        pixel_page.click_delete_button()

class TestPixelPage:

    @pytest.mark.parametrize("pixel_data", TEST_DATA)
    def test_successful_pixel_creation(self, pixel_page, pixel_data, auto_clean_pixel):
        """Тест успешного создания пикселя"""
        pixel_page.click_create_pixel_button()
        field = pixel_page.get_domain_input_field()
        pixel_page.clear_input_field(field)
        name = pixel_data["url"]
        pixel_page.fill_input_field(field, name)
        pixel_page.click_submit_button()
        test_pixel = pixel_page.find_test_pixel(name)
        assert test_pixel.text == name
        auto_clean_pixel.append(name)

    @pytest.mark.parametrize("pixel_data", TEST_DATA)
    def test_pixel_change(self, pixel_page, pixel_data, create_pixel, auto_clean_pixel):
        """Тест изменения пикселя"""
        name = create_pixel
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
        auto_clean_pixel.append(name)
    
    @pytest.mark.parametrize("pixel_data", TEST_DATA)
    def test_delete_pixel(self, pixel_page, pixel_data, create_pixel):
        """Тест удаления пикселя"""
        name = create_pixel
        pixel_page.hover_pixel()
        pixel_page.click_more()
        pixel_page.click_delete_pixel()
        pixel_page.click_delete_button()
        pixels = pixel_page.find_pixels()
        for p in pixels:
            assert p.text != name
    

    def test_invalid_domain(self, pixel_page):
        """Тест невалидного домена"""
        pixel_page.click_create_pixel_button()
        field = pixel_page.get_domain_input_field()
        pixel_page.clear_input_field(field)
        pixel_page.fill_input_field(field, INVALID_DOMAIN)
        pixel_page.click_submit_button()
        error = pixel_page.get_error_message()
        assert INVALID_DOMAIN_MESSAGE in error.text

    def test_pixel_settings(self, pixel_page):
        """Тест перехода к настройкам первого пикселя"""
        pixel_page.click_link_settings()
        url = pixel_page.get_current_url()
        assert url == PIXEL_PAGE

    def test_create_tag(self, pixel_page):
        pixel_page.click_link_settings()
        pixel_page.switch_to_new_page_tag()
        pixel_page.click_create_tag_button()
        field = pixel_page.get_tag_input_field()
        name = pixel_page.generate_random_string()
        pixel_page.fill_input_field(field, name)
        pixel_page.click_tag_button()
        tag = pixel_page.get_success_tag_modal()
        assert name in tag.text

    def test_fail_create_tag(self, pixel_page):
        """Тест создания тега с пустым полем"""
        pixel_page.click_link_settings()
        pixel_page.switch_to_new_page_tag()
        pixel_page.click_create_tag_button()
        field = pixel_page.get_tag_input_field()
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
        url = pixel_page.get_current_url()
        assert url == PIXEL_PAGE

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
        error = pixel_page.get_error_message_url()
        assert EMPTY_URL_MESSAGE in error.text
