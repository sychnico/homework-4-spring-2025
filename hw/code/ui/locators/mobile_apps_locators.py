from selenium.webdriver.common.by import By

class MobileAppsLocators:
    CREATE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Добавить приложение']")
    INPUT_APP = (By.XPATH,'//input[@placeholder="Введите ссылку на приложение"]')
    CREATE_APP_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Добавить']")
    MODAL_APP = (By.XPATH, "//div[contains(@class, 'vkuiModalPage') and contains(@class, 'ModalManagerPage_medium__')]")
    MODAL_CODE = (By.XPATH, "//*[contains(@class, 'ModalRoot_componentWrapper__')]")

    INVALID_MESSAGE = (By.XPATH, "//span[contains(@class, 'vkuiTypography') and contains(text(), 'Введите корректную ссылку на приложение')]" )

    READ_LINK = (By.XPATH,"//a[contains(@class, 'vkuiLink') and text()='Посмотреть код']")

