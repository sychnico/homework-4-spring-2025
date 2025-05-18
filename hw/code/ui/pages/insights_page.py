from .page import Page
from ui.locators.insights_locators import InsightsLocators

class InsightsPage(Page):
    URL = "https://ads.vk.com/insights" # Урл страницы
    locators = InsightsLocators()
    # Далее тут можно свои константы
    def click_insight_card(self):
        self.click(self.locators.INSIGHT_CARD)
        
    def find_insight_article(self):
        return self.find(self.locators.INSIGHT_ARTICLE)
    # И пишем атомарные функции класса, которые мы будем тестировать в другом месте, эти 
    # функции должны быть элементарными и выполнять 1 действие, например клик по кнопке, 
    # нахождение инпута или ввод текст в инпут, это будут все отдельные функции, совмещаются они в /hw/code/TestYourNamePage.py