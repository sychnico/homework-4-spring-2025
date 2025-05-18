from .page import Page
from ui.locators.documents_locators import DocumentsLocators

class DocumentsPage(Page):
    URL = "https://ads.vk.com/documents" # Урл страницы
    locators = DocumentsLocators()
    # Далее тут можно свои константы
    def click_document_card(self):
        self.click(self.locators.DOCUMENT_CARD)
        
    def find_document_article(self):
        return self.find(self.locators.DOCUMENT_ARTICLE)
    # И пишем атомарные функции класса, которые мы будем тестировать в другом месте, эти 
    # функции должны быть элементарными и выполнять 1 действие, например клик по кнопке, 
    # нахождение инпута или ввод текст в инпут, это будут все отдельные функции, совмещаются они в /hw/code/TestYourNamePage.py