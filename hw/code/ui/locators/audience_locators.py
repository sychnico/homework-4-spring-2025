from selenium.webdriver.common.by import By

class AudienceLocators:

    def USERLIST_BLOCK_BY_NAME(self, name):
        return (By.XPATH, f'//div[@id="audience.users_list"]//div[contains(@class, "EditableName_nameValue__") and text()="{name}"]')

    def AUDIENCE_BLOCK_BY_NAME(self, name):
        return (By.XPATH, f'//div[@id="audience"]//span[contains(@class, "NameCell_name") and text()="{name}"]')

    def OFFLINE_BLOCK_BY_NAME(self, name):
        return (By.XPATH, f'//div[@id="audience.offline_conversion"]//div[contains(@class, "EditableName_nameValue__") and text()="{name}"]')

    def SOURCE_BLOCK_BY_NAME(self, name):
        return (By.XPATH, f'//div[contains(@class, "SourceType_button")][.//*[contains(., "{name}")]]')

    AUDIENCE_ITEM_MENU = (By.CSS_SELECTOR, "[data-testid='audience-item-menu']")
    CREATE_AUDIENCE_BUTTON = (By.CSS_SELECTOR, "[data-testid='create-audience']")
    DELETE_AUDIENCE_BUTTON = (By.XPATH, "//label[@data-testid='dropdown-item']")
    DELETE_CONFIRM_BUTTON = (By.XPATH, "//button[.//span[text()='Удалить']]")

    MORE_ACTIONS = (By.CSS_SELECTOR, "[data-testid='other-buttons']")
    ADD_EXTERNAL_AUDIENCE_BUTTON = (By.CSS_SELECTOR, "[data-testid='Активировать внешнюю аудиторию-others']")
    EXTERNAL_AUDIENCE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Введите ключ']")
    ACTIVATE_EXTERNAL_AUDIENCE_BUTTON  = (By.XPATH, "//button[.//span[contains(text(), 'Активировать')]]")
    ERROR_MESSAGE = (By.XPATH, "//span[@role='alert']")

    LIST_USERS_SECTION = (By.ID, "tab_audience.users_list")
    DOWNLOAD_NEW_LIST_USERS_BUTTON = (By.XPATH, '//span[text()="Загрузить список"]')
    NAME_LIST_USERS_INPUT = (By.CSS_SELECTOR, "input[placeholder='Введите название списка']")
    LIST_OF_TYPES_USER_LISTS = (By.XPATH, '//div[contains(@class, "vkuiCustomSelect")]//input[@role="combobox"]')
    TYPE_USER_LIST = (By.XPATH, '//div[contains(@class, "vkuiCustomSelect")]//*[text()="ID ВКонтакте"]')
    DOWNLOAD_FILE_LIST_USERS_BUTTON = (By.XPATH, "//input[@type= 'file']")
    ERROR_FILE_MODAL = (By.XPATH, "//div[@role = 'dialog']//span")
    SAVE_USER_LIST = (By.CSS_SELECTOR, "[data-testid='submit']")
    USER_LIST_BLOCK = (By.CSS_SELECTOR, "div.BaseTable__row[role='row']")

    OFFLINE_SECTION = (By.ID, "tab_audience.offline_conversion")
    DOWNLOAD_OFFLINE_BUTTON = (By.XPATH, '//span[text()="Загрузить список"]')
    CREATE_NEW_OFFLINE =(By.XPATH, '//span[text()="Создать новый"]')
    NAME_OFFLINE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Введите название списка']")
    LIST_OF_TYPES_OFFLINE = (By.XPATH, '//div[contains(@class, "vkuiCustomSelect")]//input[@role="combobox"]')
    TYPE_OFFLINE = (By.XPATH, '//div[contains(@class, "vkuiCustomSelect")]//*[text()="Телефонные номера"]')
    DOWNLOAD_OFFLINE_FILE_BUTTON = (By.XPATH, "//input[@type= 'file']")
    SAVE_OFFLINE = (By.CSS_SELECTOR, "[data-testid='submit']")
    OFFLINE_BLOCK = (By.CSS_SELECTOR, "div.BaseTable__row[role='row']")

    NAME_AUDIENCE_INPUT = (By.XPATH, '//input[@type="text"]')
    SAVE_AUDIENCE_BUTTON = (By.XPATH, '//div[contains(@class, "ModalSidebarPage_container")]//button[.//span[text()="Сохранить"]]')
    AUDIENCE_BLOCK = (By.CSS_SELECTOR, "div.BaseTable__row[role='row']")

    ADD_NEW_SOURCE_BUTTON = (By.XPATH, '//button[contains(.,"Добавить источник")]')
    EXCLUDE_NEW_SOURCE_BUTTON = (By.XPATH, '//button[contains(.,"Исключить источник")]')

    CREATED_AUDIENCE_SOURCE_BUTTON = (By.XPATH, "//button[contains(text(), 'Уже созданная аудитория')]")
    LIST_OF_CREATED_AUDIENCE = (By.XPATH, "//div[contains(@class, 'vkuiCustomSelect')]")
    SAVE_BUTTON = (By.XPATH, '//div[contains(@class, "ModalSidebarPage_container")]//button[.//span[text()="Сохранить"]]')

    USER_LIST_SOURCE_BUTTON = (By.XPATH, "//*[contains(text(), 'Список пользователей')]")
    LIST_OF_USER_LIST = (By.XPATH, "//div[contains(@class, 'UserListItem_item__')]")

    KEYWORDS_SOURCE_BUTTON = (By.XPATH, "//*[contains(text(), 'Вводили ключевые фразы')]")
    NAME_KEYWORDS_INPUT = (By.XPATH, "//input[@value= 'Ключевые фразы']")
    KEYWORDS_INPUT = (By.XPATH, '//*[contains(text(), "Ключевые фразы")]/ancestor::div[contains(@class, "vkuiFormItem")]//textarea')

    CHECKBOX_AUDIENCE = (By.XPATH, "//input[contains(@type, 'checkbox')]")
    DELETE_AUDIENCE_BUTTON = (By.XPATH, "//button[contains(text(), 'Удалить')]")
    AUDIENCE_SEARCH_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Поиск')]")


