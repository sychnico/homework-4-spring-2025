from selenium.webdriver.common.by import By

class DocumentsLocators:
    EXAMPLE_INPUT = (
        By.XPATH,
        "//input[contains(@class, 'EXAMPLEInput__el')]"
    )
    DOCUMENT_CARD = (By.XPATH, "//*[contains(@class, 'Link_wrapper__')]")
    DOCUMENT_ARTICLE = (By.XPATH, "//*[contains(@class, 'commonArticle_article__')]")