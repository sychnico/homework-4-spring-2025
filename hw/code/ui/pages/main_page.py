from .page import Page
from ui.locators.main_locators import MainLocators

class MainPage(Page):
    URL = "https://ads.vk.com/" # Урл страницы
    locators = MainLocators()
    # Далее тут можно свои константы
    
    def click_news_button(self):
        self.click(self.locators.NEWS_BUTTON)
        
    def find_news_card(self):
        return self.find(self.locators.NEWS_CARD)

    def click_cases_button(self):
        self.click(self.locators.CASES_BUTTON)
        
    def find_case_card(self):
        return self.find(self.locators.CASE_CARD)

    def click_events_button(self):
        self.scroll_and_click(self.locators.EVENTS_BUTTON)
        
    def find_event_card(self):
        return self.find(self.locators.EVENT_CARD)

    def click_insights_button(self):
        self.scroll_and_click(self.locators.INSIGHTS_BUTTON)
        
    def find_insight_card(self):
        return self.find(self.locators.INSIGHT_CARD)

    def click_partner_button(self):
        self.scroll_and_click(self.locators.PARTNER_BUTTON)

    def check_partner_redirect(self):
        self.go_to_new_tab()
        return self.is_redirected_to_pattern("https://ads.vk.com/partner")

    def click_signup_button(self):
        self.scroll_and_click(self.locators.SIGNUP_BUTTON)

    def check_signup_redirect(self):
        self.go_to_new_tab()
        return self.is_redirected_to_pattern("https://id.vk.com/auth")

    def click_expert_button(self):
        self.scroll_and_click(self.locators.EXPERT_BUTTON)

    def check_expert_redirect(self):
        self.go_to_new_tab()
        return self.is_redirected_to_pattern("https://expert.vk.com/")

    def click_help_button(self):
        self.scroll_and_click(self.locators.HELP_BUTTON)

    def check_help_redirect(self):
        self.go_to_new_tab()
        return self.is_redirected_to_pattern("https://ads.vk.com/help")

    def click_documents_button(self):
        self.scroll_and_click(self.locators.DOCUMENTS_BUTTON)

    def check_documents_redirect(self):
        self.go_to_new_tab()
        return self.is_redirected_to_pattern("https://ads.vk.com/documents")

    # И пишем атомарные функции класса, которые мы будем тестировать в другом месте, эти 
    # функции должны быть элементарными и выполнять 1 действие, например клик по кнопке, 
    # нахождение инпута или ввод текст в инпут, это будут все отдельные функции, совмещаются они в /hw/code/TestYourNamePage.py