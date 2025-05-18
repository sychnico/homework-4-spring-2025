from selenium.webdriver.common.by import By

class EventsLocators:
    EXAMPLE_INPUT = (
        By.XPATH,
        "//input[contains(@class, 'EXAMPLEInput__el')]"
    )
    EVENT_CARD = (By.XPATH, "//*[contains(@class, 'event-card_wrapper__')]")
    EVENT_ARTICLE = (By.XPATH, "//*[contains(@class, 'commonArticle_article__')]")