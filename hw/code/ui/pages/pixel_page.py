from .page import Page
from ui.locators.pixel_locators import PixelLocators

class PixelPage(Page):
    URL = "https://ads.vk.com/hq/pixels" # Урл страницы
    locators = PixelLocators()
    # Далее тут можно свои константы
    def click_create_button(self):
        self.click(self.locators.BUTTON)

    def find_modal(self):
        return self.find(self.locators.MODAL)

    # И пишем атомарные функции класса, которые мы будем тестировать в другом месте, эти 
    # функции должны быть элементарными и выполнять 1 действие, например клик по кнопке, 
    # нахождение инпута или ввод текст в инпут, это будут все отдельные функции, совмещаются они в /hw/code/TestYourNamePage.py