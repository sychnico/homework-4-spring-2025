from selenium.webdriver.support import expected_conditions
from .page import Page
from ui.locators.pixel_locators import PixelLocators
import string
import random
class PixelPage(Page):
    URL = "https://ads.vk.com/hq/pixels"
    locators = PixelLocators()

    def click_create_pixel_button(self):
        """Клик по кнопке создания пикселя"""
        self.click(self.locators.BUTTON)

    def get_modal_element(self):
        """Получение элемента модального окна"""
        return self.became_visible(self.locators.MODALS, 10)

    def get_domain_input_field(self):
        """Получение поля ввода домена"""
        return self.find(self.locators.INPUT_DOMAIN)

    def clear_input_field(self, field):
        """Очистка поля ввода"""
        field.clear()

    def find_test_pixel(self, str):
        return self.find(self.locators.test_pixel_name(str))

    def check_pixel_deleted(self, str):
        return self.became_invisible(self.locators.test_pixel_name(str))

    def fill_random_string(self, field, text):
        field.send_keys(text)
        
    def fill_input_field(self, field, text):
        """Заполнение поля ввода с проверкой"""
        field.send_keys(text)
        assert field.get_attribute("value") == text

    def click_submit_button(self):
        """Клик по кнопке подтверждения"""
        self.click(self.locators.CREATE_PIXEL_BUTTON, 10)

    def click_create_new_option(self):
        """Клик по опции 'Создать новый'"""
        element = self.wait_for_element(self.locators.CREATE_NEW_BUTTON, 10)
        self.scroll_and_click(element, 10)

    def get_success_modal(self):
        """Получение модального окна успеха"""
        return self.find(self.locators.MODAL_END)

    def get_error_message(self):
        """Получение сообщения об ошибке"""
        return self.find(self.locators.INVALID_DOMAIN_MESSAGE)

    def click_link_settings(self):
        return self.click(self.locators.SETTINGS_LINK)

    def assert_new_page(self, url):
        return self.is_redirected_to_pattern(url)

    def switch_to_new_page_tag(self):
        """Переключение на вкладку аудиторных тегов"""
        element = self.wait_for_element(self.locators.AUDIENCE_TAGS_TAB, 10)
        self.click(element)

    def click_create_tag_button(self):
        """Клик по кнопке создания пикселя"""
        self.click(self.locators.CREATE_TAG_BUTTON,10)

    def click_tag_button(self):
        """Клик по кнопке подтверждения"""
        self.click(self.locators.BUTTON_TAG, 10)

    def get_tag_input_field(self):
        """Получение поля ввода домена"""
        return self.find(self.locators.INPUT_TAG, 10)

    def get_success_tag_modal(self):
        return self.find(self.locators.SUCCESS_TAG_MESSAGE, 10)

    def get_error_message_tag(self):
        """Получение сообщения об ошибке тега"""
        return self.find(self.locators.INVALID_EMPTY_TAG_MESSAGE)

    def click_create_action_button(self):
        """Клик по кнопке создания пикселя"""
        self.click(self.locators.CREATE_ACTION_BUTTON,10)

    def get_action_input_field(self):
        """Получение поля ввода события"""
        return self.find(self.locators.INPUT_NAME_ACTION, 10)

    def select_category(self, category_name):
        self.click(self.locators.CATEGORY_DROPDOWN)
        option_locator = (self.locators.CATEGORY_OPTION[0],
        self.locators.CATEGORY_OPTION[1].format(category_name))
        self.click(option_locator)

    def select_condition(self, condition_name):
        self.click(self.locators.CONDITION_DROPDOWN)
        option_locator = (
            self.locators.CONDITION_OPTION[0],
            self.locators.CONDITION_OPTION[1].format(condition_name)
        )
        self.click(option_locator)

    def get_url_input_field(self):
        """Получение поля ввода"""
        return self.find(self.locators.INPUT_URL_ACTION, 10)

    def click_action_button(self):
        """Клик по кнопке подтверждения"""
        self.click(self.locators.BUTTON_ACTION, 10)

    def get_error_message_url(self):
        """Получение сообщения об ошибке тега"""
        return self.find(self.locators.INVALID_EMPTY_URL_MESSAGE, timeout=20)

    def generate_random_string(self, length=8):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    def hover_pixel(self):
        self.hover(self.locators.FIRST_PIXEL)
        
    def click_more(self):
        """Клик по кнопке подробнее"""
        self.click(self.locators.MORE_BUTTON)

    def click_rename(self):
        """Клик по кнопке Переименовать"""
        self.click(self.locators.RENAME_BUTTON)


    def click_delete(self):
        """Клик по кнопке Удалить"""
        self.click(self.locators.DELETE_BUTTON)
        
    def click_delete_pixel(self):
        self.click(self.locators.DELETE_BUTTON)
        
    def click_rename_pixel(self):
        self.click(self.locators.RENAME_BUTTON)

    def get_pixel_input_field(self):
        return self.find(self.locators.INPUT_FIELD, 10)

    def click_change_button(self):
        """Клик по кнопке подтверждения"""
        self.click(self.locators.BUTTON_CHANGE, 10)

    def click_delete_button(self):
        """Клик по кнопке подтверждения"""
        self.click(self.locators.BUTTON_DELETE, 10)

    def get_pixel_row(self, domain=None, timeout=10):
        if domain:
            locator = (self.locators.PIXEL_ROW_BY_DOMAIN[0], self.locators.PIXEL_ROW_BY_DOMAIN[1].format(domain=domain))
        else:
            locator = self.locators.PIXEL_ROW

        return self.find(locator, timeout)

    def hover_pixel_row(self, domain=None):
        row = self.get_pixel_row(domain)
        self.hover(row)
        return row

    def wait_for_element(self, locator, timeout=10):
        """Ожидание появления элемента"""
        return self.wait(timeout).until(
            expected_conditions.presence_of_element_located(locator)
        )
