from selenium.webdriver.common.by import By

class InsightsLocators:
    EXAMPLE_INPUT = (
        By.XPATH,
        "//input[contains(@class, 'EXAMPLEInput__el')]"
    )
    INSIGHT_CARD = (By.XPATH, "//*[contains(@class, 'insight-card_wrapper__')]")
    INSIGHT_ARTICLE = (By.XPATH, "//*[contains(@class, 'commonArticle_article__')]")