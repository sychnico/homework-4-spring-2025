import pytest
from .sonya import VKAdsPage

@pytest.fixture
def authorized_vk_ads_page(session_driver):
    return VKAdsPage(session_driver)

def test_open_empty_auditory_page(authorized_vk_ads_page):
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/audience")
    assert authorized_vk_ads_page.test_open_empty_auditory_page()
def test_create_audience_modal(authorized_vk_ads_page):
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/audience")
    assert authorized_vk_ads_page.test_create_audience_modal()
def test_add_source(authorized_vk_ads_page):
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/audience")
    assert authorized_vk_ads_page.test_add_source()
def test_user_lists(authorized_vk_ads_page):
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/audience")
    assert authorized_vk_ads_page.test_user_lists()
def test_offline_conversion(authorized_vk_ads_page):
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/audience")
    assert authorized_vk_ads_page.test_offline_conversion()
def test_modal_lists(authorized_vk_ads_page):
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/audience")
    assert authorized_vk_ads_page.test_modal_lists()
def test_modal_offline(authorized_vk_ads_page):
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/audience")
    assert authorized_vk_ads_page.test_modal_offline()
def test_overview(authorized_vk_ads_page):
    authorized_vk_ads_page.open_page("https://ads.vk.com/hq/overview")
    assert authorized_vk_ads_page.test_overview()
