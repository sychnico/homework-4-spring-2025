from .page import Page
from ui.locators.cases_locators import CasesLocators

class CasesPage(Page):
    URL = "https://ads.vk.com/cases" # Урл страницы
    locators = CasesLocators()
    # Далее тут можно свои константы

    def click_case_card(self):
        self.click(self.locators.CASE_CARD)
        
    def find_case_article(self):
        return self.find(self.locators.CASE_ARTICLE)

    # И пишем атомарные функции класса, которые мы будем тестировать в другом месте, эти 
    # функции должны быть элементарными и выполнять 1 действие, например клик по кнопке, 
    # нахождение инпута или ввод текст в инпут, это будут все отдельные функции, совмещаются они в /hw/code/TestYourNamePage.py