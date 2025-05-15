import pytest
from .belyak import VKAdsPage

@pytest.fixture
def authorized_vk_ads_page(session_driver):
    return VKAdsPage(session_driver)



def test_create_pixel(authorized_vk_ads_page):
    """Тест создания  пикселя с корректным доменом"""
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/pixels")
    assert authorized_vk_ads_page.test_create_first_pixel("https://zanmsk.ru")


def test_pixel_id_tab(authorized_vk_ads_page):
    """Тест открытия вкладки ID пикселя в модальном окне"""
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/pixels")
    assert authorized_vk_ads_page.test_pixel_id_tab_opening()

def test_invalid_pixel_id(authorized_vk_ads_page):
    """Тест валидации при вводе некорректных данных ID пикселя"""
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/pixels")
    assert authorized_vk_ads_page.test_invalid_pixel_id_validation()

def test_modal(authorized_vk_ads_page):
    """Тест открытия модального окна добавления пикселя"""
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/pixels")
    assert authorized_vk_ads_page.test_add_pixel_modal()


@pytest.mark.parametrize("search_query, expect_empty", [
    ("test", True),
    ("my", False),
    ("несуществующий", True),
])
def test_pixel_search_param(authorized_vk_ads_page, search_query, expect_empty):
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/pixels")
    authorized_vk_ads_page.search_pixel(search_query)
    assert authorized_vk_ads_page.is_empty_search_result(), f"Ожидалось пустое сообщение для запроса '{search_query}'"

def test_invalid_domain(authorized_vk_ads_page):
    """Тест проверки валидации при вводе некорректного домена"""
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/pixels")
    assert authorized_vk_ads_page.test_add_pixel_modal()
    assert authorized_vk_ads_page.test_invalid_domain_modal("not_a_domain")

def test_pixel_settings(authorized_vk_ads_page):
    """Тест перехода к настройкам первого пикселя"""
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/pixels")
    assert authorized_vk_ads_page.test_pixel_settings()

def test_pixel_tabs(authorized_vk_ads_page):
    """Тест переключения между вкладками в настройках пикселя"""
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/pixels")
    assert authorized_vk_ads_page.test_pixel_settings()
    assert authorized_vk_ads_page.test_pixel_tabs_navigation()

def test_add_event_modal(authorized_vk_ads_page):
    """Тест открытия модального окна добавления события"""
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/pixels")
    assert authorized_vk_ads_page.test_pixel_settings()
    assert authorized_vk_ads_page.test_add_event()

def test_cancel_event(authorized_vk_ads_page):
    """Тест отмены создания события"""
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/pixels")
    assert authorized_vk_ads_page.test_pixel_settings()
    assert authorized_vk_ads_page.test_cancel_event_creation()


def test_invalid_event(authorized_vk_ads_page):
    """Тест проверки валидации при некорректном добавлении события"""
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/pixels")
    assert authorized_vk_ads_page.test_pixel_settings()
    assert authorized_vk_ads_page.test_invalid_event_creation()

def test_create_audience_tag(authorized_vk_ads_page):
    """Тест создания аудиторного тега"""
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/pixels")
    assert authorized_vk_ads_page.test_pixel_settings()
    assert authorized_vk_ads_page.test_create_audience_tag("My Test Tag")

def test_open_app_modal(authorized_vk_ads_page):
    """Тест открытия модального окна создания приложения"""
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/apps")
    assert authorized_vk_ads_page.test_open_app_modal()

def test_invalid_app_input(authorized_vk_ads_page):
    """Тест проверки валидации при вводе некорректных данных"""
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/apps")
    assert authorized_vk_ads_page.test_invalid_app_input("examle.com")


def test_valid_app_input(authorized_vk_ads_page):
    """Тест проверки ввода валидного URL приложения из App Store"""
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/apps")
    assert authorized_vk_ads_page.test_valid_app_input()


def test_valid_app_search(authorized_vk_ads_page):
    """Тест поиска существующего приложения"""
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/apps")
    assert authorized_vk_ads_page.test_valid_app_search()

def test_invalid_app_search(authorized_vk_ads_page):
    """Тест поиска несуществующего приложения"""
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/apps")
    assert authorized_vk_ads_page.test_invalid_app_search()

def test_leadforms_tabs(authorized_vk_ads_page):
    """Тест проверки навигации по вкладкам на странице лид-форм"""
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/leadads/leadforms")
    assert authorized_vk_ads_page.test_leadforms_tabs_navigation()

def test_create_leadform_modal(authorized_vk_ads_page):
    """Тест проверки открытия модального окна создания лид-формы"""
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/leadads/leadforms")
    assert authorized_vk_ads_page.test_create_leadform_modal()

