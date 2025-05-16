from selenium.webdriver.common.by import By

class BalanceLocators:
    EXAMPLE_INPUT = (
        By.XPATH,
        "//input[contains(@class, 'EXAMPLEInput__el')]"
    )
    INC_BALANCE = (By.XPATH, "//*[contains(@class, 'vkuiButton')]")
    INC_MODAL = (By.XPATH, "//*[contains(@class, 'ModalRoot_overlay__')]")