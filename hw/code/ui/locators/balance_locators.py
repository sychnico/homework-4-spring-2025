from selenium.webdriver.common.by import By

class BalanceLocators:
  
    INC_BALANCE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton')]")
    INC_MODAL = (By.XPATH, "//*[contains(@class, 'ModalRoot_overlay__')]")
    AMOUNT_INPUT = (By.XPATH, "//input[contains(@name, 'amount')]")
    AMOUNTWITHOUTVAT_INPUT = (By.XPATH, "//input[contains(@name, 'amountWithoutVat')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiModalDismissButton')]")
    TOP_UP_BALANCE_BUTTON = (By.XPATH, "//*[contains(@class, 'CreateInvoiceModal_button__')]")
    ERROR_PAY_NULL_VALUE  = (By.XPATH, "//*[text()='Нужно заполнить']")
    def ERROR_PAY_WRONG_VALUE(price):
        return (By.XPATH, f"//*[text()='Минимальная сумма {price},00 ₽ ']")
    BONUS_PROGRAM_TAB = (By.XPATH, "//div[contains(@tabindex, '-1') and contains(@class, 'vkuiTabsItem')]")
    ACTIVATE_PROMOCODE = (By.XPATH, "//button[contains(@class, 'CouponBanner_button__')]")
    ACTVATE = (By.XPATH, "//*[text()='Активировать']")
    PROMOCODE_INPUT = (By.XPATH, "//input[@placeholder='Введите промокод']")
    SKIP_ALERT = (By.XPATH, "//*[text()='Продолжить']")
    ERROR_NULL_PROMOCODE = (By.XPATH, "//*[text()='Укажите промокод']")
    ERROR_WRONG_PROMOCODE = (By.XPATH, "//*[text()='Неверный промокод']")
    OPLATA_TEXT_INFO  = (By.XPATH, "//button[@data-testid='pay_btn']")
    BONUS_TAB_TEXT_INFO  = (By.XPATH, "//*[text()='Персональные акции']")
    AMOUNT_TEXT_INFO = (By.XPATH, "//span[@data-testid='amount']")

