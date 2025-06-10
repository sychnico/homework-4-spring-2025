from selenium.webdriver.common.by import By

class PixelLocators:
    EXAMPLE_INPUT = (
        By.XPATH,
        "//input[contains(@class, 'EXAMPLEInput__el')]"
    )
    BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Добавить пиксель']")
    CREATE_PIXEL_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiModalCardBase__actions')]")
    CREATE_NEW_BUTTON = By.XPATH, "//div[contains(@class, 'vkuiTappable') and .//span[contains(., 'Создать новый пиксель')]]"
    FIRST_PIXEL = (By.XPATH, "//div[contains(@class, 'PixelsList__row')]")
    CREATE_TAG_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Создать аудиторный тег']")
    BUTTON_TAG = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Создать']")

    CREATE_ACTION_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Добавить событие']")
    BUTTON_ACTION = (By.XPATH, "//button[@data-testid='submit' and contains(@class, 'vkuiButton')]//span[contains(@class, 'vkuiButton__content') and text()='Добавить событие']/..")
    MODALS = (By.XPATH, "//*[contains(@class, 'ModalRoot_overlay__')]")
    MODAL_END = (By.XPATH, "//*[contains(@class, 'ModalRoot_componentWrapper__')]")
    MORE_BUTTON = (By.XPATH, "//button[@aria-label='More']")
    RENAME_BUTTON = (By.XPATH, "//span[text()='Переименовать']")
    DELETE_BUTTON = (By.XPATH, "//span[text()='Удалить пиксель']")
    BUTTON_CHANGE = (By.XPATH, "//button[@data-testid='submit' and contains(@class, 'vkuiButton')]//span[contains(@class, 'vkuiButton__content') and text()='Изменить']/..")
    BUTTON_DELETE = (By.XPATH, "//span[text()='Удалить']")
    PIXEL_ROW_BY_DOMAIN = (By.XPATH, "//div[contains(@class, 'BaseTable__row') and .//a[contains(@href, '{domain}')]")

    INPUT_DOMAIN = (By.XPATH,'//input[@placeholder="Домен сайта"]')
    INPUT_TAG = (By.XPATH, '//input[@placeholder="Введите название тега"]')
    INPUT_NAME_ACTION = (By.XPATH, '//input[@placeholder="Введите название"]')
    INPUT_URL_ACTION = (By.XPATH, '//input[@placeholder="Введите значение"]')
    INPUT_FIELD = (By.XPATH, "//input[contains(@class, 'vkuiInput__el')]")

    INVALID_DOMAIN_MESSAGE = (By.XPATH, "//span[contains(@class, 'vkuiTypography') and contains(text(), 'Введите корректный адрес сайта')]" )
    INVALID_EMPTY_TAG_MESSAGE = (By.XPATH, "//span[contains(@class, 'vkuiTypography') and contains(text(), 'Нужно заполнить')]" )
    INVALID_EMPTY_URL_MESSAGE = (By.XPATH, "//span[contains(@class, 'vkuiFormItem__bottom') and contains(@class, 'vkuiFootnote')]//div[contains(text(), 'Заполните это поле')]")
    SUCCESS_TAG_MESSAGE = (By.XPATH, "//div[@class='BaseTable__row-cell-text']")

    SETTINGS_LINK = (By.XPATH,"//a[contains(@class, 'vkuiLink') and text()='Настройка']")
    AUDIENCE_TAGS_TAB = (By.XPATH,"//span[contains(@class, 'vkuiTabsItem__label') and contains(text(), 'Аудиторные теги')]")

    CATEGORY_DROPDOWN = (By.CSS_SELECTOR, ".vkuiCustomSelectInput__el")
    CATEGORY_OPTION = (By.XPATH, "//div[@role='option' and contains(., '{}')]")
    CONDITION_DROPDOWN = (By.CSS_SELECTOR, ".vkuiCustomSelectInput__el[placeholder='Выберите условие']")
    CONDITION_OPTION = (By.XPATH, "//div[@role='option' and contains(., '{}')]")

    TEST_PIXEL_NAME = (By.XPATH, "//span[text()='giga-mail.ru']")
    def test_pixel_name(self, str):
        return (By.XPATH, "//span[contains(text()='" + str +"')]")