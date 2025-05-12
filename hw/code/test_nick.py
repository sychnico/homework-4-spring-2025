import pytest
from .sychnico_ht4 import test_link, test_button_class

BASE_URL = "http://ads.vk.ru"

@pytest.mark.parametrize("link, expected", [
    ("Новости", "news"),
    ("Кейсы", "cases"),
    ("Форум идей", "upvote"),
    ("Монетизация", "partner"),
    ("Справка", "help"),
    ("Регистрация", "auth"),
    ("Запустить рекламу", "auth"),
    ("Получить бонус", "firstbonus"),
    ("Открыть подборку", "podborka"),
    ("Смотреть все", "cases"),
    ("Полезные материалы", "insights"),
    ("Мероприятия", "events"),
    ("Документы", "documents"),
    ("Обучение для бизнеса", "expert"),
    ("Помощь", "help")
])
def test_links(link, expected):
    test_link(BASE_URL, link, expected)


@pytest.mark.parametrize("class_str, expected", [
    ("case_link__2bZoK", "cases"),
    ("getStarted_wrapper__gW_MK", "events"),
    ("news_wrapper__ieB6j", "news")
])
def test_buttons(class_str, expected):
    test_button_class(BASE_URL, class_str, expected)


@pytest.mark.parametrize("url, class_str, expected", [
    ("http://ads.vk.ru/news", "news-card_wrapper__n6fqN", "news/novyj"),
    ("http://ads.vk.ru/news", "vkuiPagination__page", "news?p="),
    ("http://ads.vk.ru/insights", "insight-card_wrapper__YsQnM", "insights/reklama"),
    ("http://ads.vk.ru/insights", "vkuiPagination__page", "?p="),
    ("http://ads.vk.ru/events", "event-card_wrapper__GZkvu", "events/vybor"),
    ("http://ads.vk.ru/documents", "Link_wrapper__eHAEn", "documents/offer"),
    ("http://ads.vk.ru/cases", "case-card_wrapper__N1Mya", "cases/kak"),
    ("http://ads.vk.ru/cases", "vkuiPagination__page", "?p=")
])
def test_other(url, class_str, expected):
    test_button_class(url, class_str, expected)