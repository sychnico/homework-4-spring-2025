from selenium.webdriver.common.by import By

class AudienceLocators:
    CREATE_AUDIENCE_BUTTON = (By.XPATH, "//*[contains(@class, 'CreateButton_button__')]")
    ADD_EXTERNAL_AUDIENCE_BUTTON = (By.XPATH, "//*[contains(text(), 'Внешний источник')]")
    EXTERNAL_AUDIENCE_INPUT = (By.XPATH, "//input[contains(@name, 'externalAudience')]")
    ACTIVATE_EXTERNAL_AUDIENCE_BUTTON = (By.XPATH, "//button[contains(text(), 'Активировать')]")
    MODAL_AUDIENCE = (By.XPATH, "//*[contains(@class, 'ModalRoot_overlay__')]")
    NAME_AUDIENCE_INPUT = (By.XPATH, "//input[contains(@name, 'name')]")
    SAVE_AUDIENCE_BUTTON = (By.XPATH, "//button[contains(text(), 'Сохранить')]")
    AUDIENCE_BLOCK = (By.XPATH, "//div[contains(@class, 'AudienceItem_item__')]")

    ADD_NEW_SOURCE_BUTTON = (By.XPATH, "//button[contains(text(), 'Добавить источник')]")
    EXCLUDE_NEW_SOURCE_BUTTON = (By.XPATH, "//button[contains(text(), 'Исключить')]")
    CREATED_AUDIENCE_SOURCE_BUTTON = (By.XPATH, "//*[contains(text(), 'Аудитория')]")
    LIST_OF_CREATED_AUDIENCE = (By.XPATH, "//div[contains(@class, 'SourceSelector_item__')]")
    SAVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Сохранить изменения')]")

    USER_LIST_SOURCE_BUTTON = (By.XPATH, "//*[contains(text(), 'Список пользователей')]")
    LIST_OF_USER_LIST = (By.XPATH, "//div[contains(@class, 'UserListItem_item__')]")

    KEYWORDS_SOURCE_BUTTON = (By.XPATH, "//*[contains(text(), 'Ключевые фразы')]")
    NAME_KEYWORDS_INPUT = (By.XPATH, "//input[contains(@name, 'keywordsName')]")
    KEYWORDS_INPUT = (By.XPATH, "//textarea[contains(@name, 'keywords')]")
    MINUS_PHRASES_INPUT = (By.XPATH, "//textarea[contains(@name, 'minusPhrases')]")
    DAYS_INPUT = (By.XPATH, "//input[contains(@name, 'days')]")

    COMMUNITY_SOURCE_BUTTON = (By.XPATH, "//*[contains(text(), 'Сообщества')]")
    COMMUNITY_NAME_INPUT = (By.XPATH, "//input[contains(@name, 'communityName')]")
    LIST_OF_GROUPES_COMMUNITIES = (By.XPATH, "//div[contains(@class, 'CommunityGroup_group__')]")
    LIST_OF_COMMUNITIES = (By.XPATH, "//div[contains(@class, 'CommunityItem_item__')]")
    ADD_COMMUNITY_BUTTON = (By.XPATH, "//button[contains(text(), 'Добавить')]")

    MUSIC_SOURCE_BUTTON = (By.XPATH, "//*[contains(text(), 'Музыка')]")
    MUSIC_NAME_INPUT = (By.XPATH, "//input[contains(@name, 'musicName')]")
    LIST_OF_MUSIC = (By.XPATH, "//div[contains(@class, 'MusicItem_item__')]")

    APP_SOURCE_BUTTON = (By.XPATH, "//*[contains(text(), 'Приложения')]")
    APP_INPUT = (By.XPATH, "//input[contains(@name, 'appName')]")
    LIST_OF_APPS = (By.XPATH, "//div[contains(@class, 'AppItem_item__')]")
    ADD_APP_BUTTON = (By.XPATH, "//button[contains(text(), 'Добавить приложение')]")

    CHECKBOX_AUDIENCE = (By.XPATH, "//input[contains(@type, 'checkbox')]")
    DELETE_AUDIENCE_BUTTON = (By.XPATH, "//button[contains(text(), 'Удалить')]")
    AUDIENCE_SEARCH_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Поиск')]")

    CREATE_NEW_LIST_USERS_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать список')]")
    DOWNLOAD_NEW_LIST_USERS_BUTTON = (By.XPATH, "//button[contains(text(), 'Загрузить')]")
    NAME_LIST_USERS_INPUT = (By.XPATH, "//input[contains(@name, 'listName')]")
    LIST_OF_TYPES_USER_LISTS = (By.XPATH, "//div[contains(@class, 'UserListType_item__')]")
    DOWNLOAD_FILE_LIST_USERS_BUTTON = (By.XPATH, "//input[contains(@type, 'file')]")
    ERROR_FILE = (By.XPATH, "//*[contains(text(), 'Ошибка')]")
    SAVE_USER_LIST = (By.XPATH, "//button[contains(text(), 'Сохранить список')]")
    USER_LIST_BLOCK = (By.XPATH, "//div[contains(@class, 'UserListBlock_block__')]")

    OFFLINE_BUTTON = (By.XPATH, "//button[contains(text(), 'Оффлайн')]")
    DOWNLOAD_OFFLINE_BUTTON = (By.XPATH, "//button[contains(text(), 'Загрузить оффлайн')]")
    NAME_OFFLINE_INPUT = (By.XPATH, "//input[contains(@name, 'offlineName')]")
    LIST_OF_TYPES_OFFLINE = (By.XPATH, "//div[contains(@class, 'OfflineType_item__')]")
    WINDOW_OFFLINE_INPUT = (By.XPATH, "//input[contains(@name, 'window')]")
    DOWNLOAD_OFFLINE_FILE_BUTTON = (By.XPATH, "//input[contains(@type, 'file')]")
    SAVE_OFFLINE = (By.XPATH, "//button[contains(text(), 'Сохранить')]")
    OFFLINE_BLOCK = (By.XPATH, "//div[contains(@class, 'OfflineBlock_block__')]")
