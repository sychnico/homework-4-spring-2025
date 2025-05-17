from selenium.webdriver.common.by import By

class NewsLocators:
    EXAMPLE_INPUT = (
        By.XPATH,
        "//input[contains(@class, 'EXAMPLEInput__el')]"
    )
    NEWS_CARD = (By.XPATH, "//*[contains(@class, 'news-card_wrapper__')]")
    NEWS_ARTICLE = (By.XPATH, "//*[contains(@class, 'commonArticle_article__')]")
    NEWS_PAGINATION = (By.XPATH, "//*[contains(@class, 'vkuiButton--hover')]")
    