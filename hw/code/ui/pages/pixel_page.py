from selenium.webdriver.support import expected_conditions
from .page import Page
from ui.locators.pixel_locators import PixelLocators

class PixelPage(Page):
    URL = "https://ads.vk.com/hq/pixels"
    locators = PixelLocators()

    def click_create_pixel_button(self):
        """Клик по кнопке создания пикселя"""
        self.click(self.locators.BUTTON)

    def get_modal_element(self):
        """Получение элемента модального окна"""
        return self.find(self.locators.MODAL)

    def get_domain_input_field(self):
        """Получение поля ввода домена"""
        return self.find(self.locators.INPUT_DOMAIN)

    def clear_input_field(self, field):
        """Очистка поля ввода"""
        field.clear()

    def fill_input_field(self, field, text):
        """Заполнение поля ввода с проверкой"""
        field.send_keys(text)
        assert field.get_attribute("value") == text

    def click_submit_button(self):
        """Клик по кнопке подтверждения"""
        self.click(self.locators.CREATE_PIXEL_BUTTON, 10)

    def click_create_new_option(self):
        """Клик по опции 'Создать новый'"""
        self.scroll_and_click(self.locators.CREATE_NEW_BUTTON, 10)

    def get_success_modal(self):
        """Получение модального окна успеха"""
        return self.find(self.locators.MODAL_END)

    def get_error_message(self):
        """Получение сообщения об ошибке"""
        return self.find(self.locators.INVALID_DOMAIN_MESSAGE)

    def click_link_settings(self):
        return self.click(self.locators.SETTINGS_LINK)

    def assert_new_page(self, url):
        assert self.is_redirected_to_pattern(url)

    def switch_to_new_page_tag(self):
        self.click(self.locators.AUDIENCE_TAGS_TAB)

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
