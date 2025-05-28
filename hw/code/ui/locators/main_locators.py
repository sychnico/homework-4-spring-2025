from selenium.webdriver.common.by import By

class MainLocators:
    EXAMPLE_INPUT = (
        By.XPATH,
        "//input[contains(@class, 'EXAMPLEInput__el')]"
    )
    NEWS_BUTTON = (By.LINK_TEXT, "Новости")
    NEWS_CARD = (By.XPATH, "//*[contains(@class, 'news-card_wrapper__')]")
    CASES_BUTTON = (By.LINK_TEXT, "Кейсы")
    CASE_CARD = (By.XPATH, "//*[contains(@class, 'case-card_wrapper__')]")
    EVENTS_BUTTON = (By.LINK_TEXT, "Мероприятия")
    EVENT_CARD = (By.XPATH, "//*[contains(@class, 'event-card_wrapper__')]")
    INSIGHTS_BUTTON = (By.LINK_TEXT, "Полезные материалы")
    INSIGHT_CARD = (By.XPATH, "//*[contains(@class, 'insight-card_wrapper__')]")
    PARTNER_BUTTON = (By.LINK_TEXT, "Монетизация")
    SIGNUP_BUTTON = (By.LINK_TEXT, "Регистрация")
    EXPERT_BUTTON = (By.LINK_TEXT, "Обучение для бизнеса")
    HELP_BUTTON = (By.LINK_TEXT, "Помощь")
    DOCUMENTS_BUTTON = (By.LINK_TEXT, "Документы")