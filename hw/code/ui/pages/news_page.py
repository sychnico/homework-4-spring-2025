from .page import Page
from ui.locators.news_locators import NewsLocators

class NewsPage(Page):
    URL = "https://ads.vk.com/news" # Урл страницы
    locators = NewsLocators()
    # Далее тут можно свои константы
    def click_news_card(self):
        self.click(self.locators.NEWS_CARD)
        
    def find_news_article(self):
        return self.find(self.locators.NEWS_ARTICLE)

    def click_pagination(self):
        self.click(self.locators.NEWS_PAGINATION)

    def find_page_in_url(self):
        return "?p=" in self.driver.current_url

    # И пишем атомарные функции класса, которые мы будем тестировать в другом месте, эти 
    # функции должны быть элементарными и выполнять 1 действие, например клик по кнопке, 
    # нахождение инпута или ввод текст в инпут, это будут все отдельные функции, совмещаются они в /hw/code/TestYourNamePage.py