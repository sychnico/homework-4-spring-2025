from selenium.webdriver.common.by import By

class BalanceLocators:
    EXAMPLE_INPUT = (
        By.XPATH,
        "//input[contains(@class, 'EXAMPLEInput__el')]"
    )
    INC_BALANCE = (By.XPATH, "//*[contains(@class, 'vkuiButton')]")
    INC_MODAL = (By.XPATH, "//*[contains(@class, 'ModalRoot_overlay__')]")
    AMOUNT_INPUT = (By.XPATH, "//input[constains(@name, 'amount')]")
    AMOUNTWITHOUTVAT_INPUT = (By.XPATH, "//input[constains(@name, 'amountWithoutVat')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, '//div[@role="button" and @aria-label="Закрыть"]')
    TOP_UP_BALANCE = (By.XPATH, "//*[contains(@class, 'CreateInvoiceModal_button__')]")
    
    