from .page import Page
from ui.locators.mobile_apps_locators import MobileAppsLocators

class MobileAppsPage(Page):
    URL = "https://ads.vk.com/hq/apps" # Урл страницы
    locators = MobileAppsLocators()
    # Далее тут можно свои константы

    def click_create_new_app_button(self):
        """Клик по кнопке создания приложения"""
        self.click(self.locators.CREATE_BUTTON)

    def get_app_input_field(self):
        """Получение поля ввода домена"""
        return self.find(self.locators.INPUT_APP, 10)

    def fill_input_app_field(self, field, text):
        """Заполнение поля ввода с проверкой"""
        field.send_keys(text)
        assert field.get_attribute("value") == text

    def click_app_button(self):
        """Клик по кнопке создания приложения"""
        self.scroll_and_click(self.locators.CREATE_APP_BUTTON, 20)

    def get_modal_element(self):
        """Получение элемента модального окна"""
        return self.find(self.locators.MODAL_APP, 30)

    def get_error_message(self):
        """Получение сообщения об ошибке"""
        return self.find(self.locators.INVALID_MESSAGE)

    def click_read_code_button(self):
        return self.click(self.locators.READ_LINK)

    def get_modal_element(self):
        """Получение элемента модального окна"""
        return self.find(self.locators.MODAL_APP, 30)

    def find_app_link(self, str):
        return self.find(self.locators.app_link(str), 5)


    # И пишем атомарные функции класса, которые мы будем тестировать в другом месте, эти
    # функции должны быть элементарными и выполнять 1 действие, например клик по кнопке, 
    # нахождение инпута или ввод текст в инпут, это будут все отдельные функции, совмещаются они в /hw/code/TestYourNamePage.py