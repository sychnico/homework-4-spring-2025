from .page import Page
from ui.locators.events_locators import EventsLocators

class EventsPage(Page):
    URL = "https://ads.vk.com/events" # Урл страницы
    locators = EventsLocators()
    # Далее тут можно свои константы
    def click_event_card(self):
        self.click(self.locators.EVENT_CARD)
        
    def find_event_article(self):
        return self.find(self.locators.EVENT_ARTICLE)

    # И пишем атомарные функции класса, которые мы будем тестировать в другом месте, эти 
    # функции должны быть элементарными и выполнять 1 действие, например клик по кнопке, 
    # нахождение инпута или ввод текст в инпут, это будут все отдельные функции, совмещаются они в /hw/code/TestYourNamePage.py