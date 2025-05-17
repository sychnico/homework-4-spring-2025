from selenium.webdriver.common.by import By

class CasesLocators:
    EXAMPLE_INPUT = (
        By.XPATH,
        "//input[contains(@class, 'EXAMPLEInput__el')]"
    )
    CASE_CARD = (By.XPATH, "//*[contains(@class, 'case-card_wrapper__')]")
    CASE_ARTICLE = (By.XPATH, "//*[contains(@class, 'commonArticle_article__')]")