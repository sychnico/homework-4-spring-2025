from .page import Page
from ui.locators.mobile_apps_locators import MobileAppsLocators

class MobileAppsPage(Page):
    URL = "" # Урл страницы
    locators = MobileAppsLocators()
    # Далее тут можно свои константы

    # И пишем атомарные функции класса, которые мы будем тестировать в другом месте, эти 
    # функции должны быть элементарными и выполнять 1 действие, например клик по кнопке, 
    # нахождение инпута или ввод текст в инпут, это будут все отдельные функции, совмещаются они в /hw/code/TestYourNamePage.py