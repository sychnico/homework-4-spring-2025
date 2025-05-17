from selenium.webdriver.common.by import By

class PixelLocators:
    EXAMPLE_INPUT = (
        By.XPATH,
        "//input[contains(@class, 'EXAMPLEInput__el')]"
    )
    BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Добавить пиксель']")
    CREATE_PIXEL_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiModalCardBase__actions')]")
    CREATE_NEW_BUTTON = By.XPATH, "//div[contains(@class, 'vkuiTappable') and .//span[contains(., 'Создать новый пиксель')]]"
    CREATE_TAG_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Создать аудиторный тег']")
    BUTTON_TAG = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Создать']")

    MODAL = (By.XPATH, "//*[contains(@class, 'ModalRoot_overlay__')]")
    MODAL_END = (By.XPATH, "//*[contains(@class, 'ModalRoot_componentWrapper__')]")


    INPUT_DOMAIN = (By.XPATH,'//input[@placeholder="Домен сайта"]')
    INPUT_TAG = (By.XPATH, '//span/input[@placeholder="Введите название тега"]')


    INVALID_DOMAIN_MESSAGE = (By.XPATH, "//span[contains(@class, 'vkuiTypography') and contains(text(), 'Введите корректный адрес сайта')]" )
    SUCCESS_TAG_MESSAGE = (By.XPATH, "//div[@class='BaseTable__row-cell-text']")

    SETTINGS_LINK = (By.XPATH,"//a[contains(@class, 'vkuiLink') and text()='Настройка']")
    AUDIENCE_TAGS_TAB = (By.XPATH,"//span[contains(@class, 'vkuiTabsItem__label') and contains(text(), 'Аудиторные теги')]")

