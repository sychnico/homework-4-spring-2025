from selenium.webdriver.common.by import By

class PixelLocators:
    EXAMPLE_INPUT = (
        By.XPATH,
        "//input[contains(@class, 'EXAMPLEInput__el')]"
    )
    BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Добавить пиксель']")
    MODAL = (By.XPATH, "//*[contains(@class, 'ModalRoot_overlay__')]")
