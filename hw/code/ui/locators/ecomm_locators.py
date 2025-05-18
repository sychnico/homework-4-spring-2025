from selenium.webdriver.common.by import By

class EcommLocators:
    CREATE_CATALOG_BUTTON = (By.XPATH, "//button[@data-testid='create-catalog']")
    EDUCATION_BUTTIN = (By.XPATH, "//button[@data-testid='ecomm-onboarding-start']")
    MODAL = (By.XPATH, "//*[contains(@class, 'ModalRoot_overlay__')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiModalDismissButton')]")
    CREATE_CATALOG_WITH_NOTESES = (By.XPATH, "//*[text()='Создать каталог с подсказками']")
    WATCH_VIDEO_LESSON = (By.XPATH, "//*[text()='Смотреть видеоурок от экспертов VK']")
    WATCH_CURSE = (By.XPATH, "//*[text()='Смотреть курс на обучающей платформе']")
    CLOSE_CREATE_CATALOG = (By.XPATH, "//button[contains(@class, 'vkuiIconButton') and @aria-label='Close']")
    CATALOG_NAME_INPUT = (By.XPATH, "//input[@data-testid='catalogName-input']")
    FID_TAB = (By.XPATH, "//div[@data-entityid='url']")
    MARKET_TAB = (By.XPATH, "//div[@data-entityid='marketplace']")
    FILE_TAB = (By.XPATH, "//div[@data-entityid='file']")
    FID_INPUT = (By.XPATH, "//input[@data-testid='catalogUrl-input']")
    CREATE_CATALOG_INNER_BUTTON = (By.XPATH, "//button[@type='submit']")
    CANCEL_BUTTON = (By.XPATH, "//button[@data-entityid='cancel']")
    ERROR_NULL_VALUE_FIT_INPUT = (By.XPATH, "//*[text()='Нужно заполнить']")
    ERROR_WITHOUT_HTTP_VALUE_FIT_INPUT = (By.XPATH, "//*[text()='Необходимо указать протокол http(s)']")
    ERROR_INVALID_HTTP_VALUE_FIT_INPUT = (By.XPATH, "//*[text()='Неверный статус HTTP-запроса']")

    