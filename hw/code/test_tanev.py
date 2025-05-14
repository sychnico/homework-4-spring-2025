import pytest
from .tanev import TanevVKAdsPage

@pytest.fixture
def authorized_vk_ads_page(session_driver):
    return TanevVKAdsPage(session_driver)




def test_open_balance_page(authorized_vk_ads_page): 
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/budget/transactions")
    assert authorized_vk_ads_page.test_open_balance_page()

def test_bonus_page(authorized_vk_ads_page):
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/budget/transactions")
    assert authorized_vk_ads_page.bonus_page()


def test_inc_balance(authorized_vk_ads_page):
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/budget/transactions")
    assert authorized_vk_ads_page.bonus_inc_balance()

def test_close_inc_balance(authorized_vk_ads_page):
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/budget/transactions")
    # Открываем формочку перед тем как её закрыть
    assert authorized_vk_ads_page.bonus_inc_balance()
    # Закрываем формочку и проверяем, что она исчезла
    assert authorized_vk_ads_page.close_inc_balance()

def test_open_comm_page_and_start_education(authorized_vk_ads_page): 
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/ecomm/catalogs")
    assert authorized_vk_ads_page.open_comm_page_and_start_education()

def test_create_catalog(authorized_vk_ads_page): 
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/ecomm/catalogs")
    assert authorized_vk_ads_page.create_catalog()