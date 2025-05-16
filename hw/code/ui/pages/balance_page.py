from .page import Page
from ui.locators.balance_locators import BalanceLocators

class BalancePage(Page):
    URL = "https://ads.vk.com/hq/budget/transactions" # Урл страницы
    locators = BalanceLocators()
    # Далее тут можно свои константы
    def click_inc_button(self):
        self.click(self.locators.INC_BALANCE)
        
    def find_inc_modal(self):
        return self.find(self.locators.INC_MODAL)
        
    # И пишем атомарные функции класса, которые мы будем тестировать в другом месте, эти 
    # функции должны быть элементарными и выполнять 1 действие, например клик по кнопке, 
    # нахождение инпута или ввод текст в инпут, это будут все отдельные функции, совмещаются они в /hw/code/TestYourNamePage.py