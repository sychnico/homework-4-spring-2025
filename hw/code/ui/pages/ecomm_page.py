from .page import Page
from ui.locators.ecomm_locators import EcommLocators

class EcommPage(Page):
    URL = "https://ads.vk.com/hq/ecomm/catalogs" # Урл страницы
    locators = EcommLocators()
    
    def click_create_catalog(self):
        self.click(self.locators.CREATE_CATALOG_BUTTON)
        
    def click_start_education(self):
        self.click(self.locators.EDUCATION_BUTTIN)
    
    def close_modal(self):
        self.click(self.locators.CLOSE_MODAL_BUTTON)
    
    def wait_modal_disappears(self, timeout=5):
        self.became_invisible(self.locators.MODAL, timeout=timeout)
        
    def find_modal(self):
        return self.find_multiple(self.locators.MODAL, timeout=3)
    
    def find_catalog_with_noteses(self):
        return self.find(self.locators.CREATE_CATALOG_WITH_NOTESES)
    
    def find_watch_video_lesson(self):
        return self.find(self.locators.WATCH_VIDEO_LESSON)
    
    def find_watch_curse(self):
        return self.find(self.locators.WATCH_CURSE)
    
    def find_fit_tab(self):
        return self.find(self.locators.FID_TAB)
    
    def find_market_tab(self):
        return self.find(self.locators.MARKET_TAB)
    
    def find_file_tab(self):
        return self.find(self.locators.FILE_TAB) 
    
    def click_fit_tab(self):
        return self.click(self.locators.FID_TAB)
    
    def click_market_tab(self):
        return self.click(self.locators.MARKET_TAB)
    
    def click_file_tab(self):
        return self.click(self.locators.FILE_TAB)
    
    def click_create_catalog_inner(self):
        self.click(self.locators.CREATE_CATALOG_INNER_BUTTON)
        
    def get_fit_input_null_error(self):
        return self.find(self.locators.ERROR_NULL_VALUE_FIT_INPUT)
    
    def get_fit_input_wrong_error(self):
        return self.find(self.locators.ERROR_WITHOUT_HTTP_VALUE_FIT_INPUT)
    
    def get_fit_input_http_error(self):
        return self.find(self.locators.ERROR_INVALID_HTTP_VALUE_FIT_INPUT)
    
    def set_fit_input(self, value):
        field = self.find(self.locators.FID_INPUT)
        field.clear()
        field.send_keys(value)
    # Далее тут можно свои константы

    # И пишем атомарные функции класса, которые мы будем тестировать в другом месте, эти 
    # функции должны быть элементарными и выполнять 1 действие, например клик по кнопке, 
    # нахождение инпута или ввод текст в инпут, это будут все отдельные функции, совмещаются они в /hw/code/TestYourNamePage.py