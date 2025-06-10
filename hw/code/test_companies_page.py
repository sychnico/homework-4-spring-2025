import pytest
from ui.constants.companies_constants import CampaignConstants

class TestCampaignPage():
    @pytest.mark.parametrize("campaign_data", [
        {
            "name": "Компания Гигачадов",
            "group": "Группа Гигачадов",
            "ad": "Объявление Гигачадов",
            "budget": 150,
            "site_url": "https://education.vk.company/",
            "ad_content": {
                "title": "Abobus",
                "short_desc": "Лучший трекер задач",
                "long_desc": "Гигачадов даст 6000$ если ты его используешь",
                "button_text": "Кликните",
                "advertiser": "BMSTU, Гигачадов"
            }
        },
        {
            "name": "Кампания ВКонтакте",
            "group": "Группа ВКонтакте",
            "ad": "Объявление ВКонтакте",
            "site_url": "https://vk.com/",
            "budget": 150,
            "ad_content": {
                "title": "Реклама ВКонтакте",
                "short_desc": "Лучшая платформа для рекламы",
                "long_desc": "Создавайте рекламу вместе с ВКонтакте",
                "button_text": "СОЗДАТЬ",
                "advertiser": "Команда ВКонтакте"
            }
        },
        {
            "name": "VK Campaign",
            "group": "VK Group",
            "ad": "VK Ad",
            "site_url": "https://ads.vk.com/",
            "budget": 150,
            "ad_content": {
                "title": "VK Ads",
                "short_desc": "Best Ads Platform",
                "long_desc": "Create your ads with VK",
                "button_text": "CREATE",
                "advertiser": "VK Team"
            }
        }
    ])
    def test_campaign_group_ad_created(self, campaign_page, campaign_data):
        const = CampaignConstants()
        campaign_page.click_create_button()
        campaign_page.click_recognition_tabs()
        campaign_page.click_target_tabs()
        campaign_page.click_site_cell(const.Tabs.TARGET)
        campaign_page.fill_site_name_with_valid_url(campaign_data["site_url"])
        campaign_page.click_target_tabs()
        campaign_page.rename_entity(campaign_data["name"])
        campaign_page.fill_campaign_form(campaign_data["budget"])
        campaign_page.click_continue_button()
        campaign_page.rename_entity(campaign_data["group"])
        campaign_page.click_russia_button(const.Sections.REGIONS)
        campaign_page.click_interest_section(const.Sections.NAMES)
        campaign_page.click_interest_subsection()
        campaign_page.fill_interests(const.Targeting.INTEREST)
        campaign_page.click_stop_interest_opener()
        campaign_page.fill_stop_interest(const.Targeting.STOP_INTEREST)
        campaign_page.click_interest_section(const.Sections.NAMES)
        campaign_page.click_device_section(const.Sections.NAMES)
        campaign_page.click_mobile_checkbox()
        campaign_page.click_continue_button()
        campaign_page.rename_entity(campaign_data["ad"])
        campaign_page.click_logo_input()
        campaign_page.click_image_item()
        campaign_page.fill_ad_inputs_and_textarea(campaign_data["ad_content"])
        campaign_page.click_media()
        campaign_page.click_image_item()
        campaign_page.click_submit_button()
        campaign_page.click_publish_button()
        campaign_page.driver.get("https://ads.vk.com/hq/dashboard/ad_plans")
        assert campaign_page.became_visible(campaign_page.locators.ENTITY_NAME_CELL(campaign_data['name'])), f"Кампания с именем {campaign_data['name']} не найдена"
        campaign_page.click_group_tabs(const.Tabs.CAMPAIGN)
        assert campaign_page.became_visible(campaign_page.locators.ENTITY_NAME_CELL(campaign_data['group'])), f"Группа с именем {campaign_data['group']} не найдена"
        campaign_page.click_ad_tab(const.Tabs.CAMPAIGN)
        assert campaign_page.became_visible(campaign_page.locators.ENTITY_NAME_CELL(campaign_data['ad'])), f"Объявление с именем {campaign_data['ad']} не найдено"
        assert campaign_page.became_visible(campaign_page.locators.SIDEBAR_AD_INPUT('Заголовок', campaign_data['title'])), "Заголовок объявления не соответствует ожидаемому"
        assert campaign_page.find(campaign_page.locators.SHORT_DESCRIPTION_TEXT).text == campaign_data['short_desc'], "Блок с коротким описанием не соответствует ожидаемому"
        assert campaign_page.find(campaign_page.locators.LONG_DESCRIPTION_TEXT).text == campaign_data['long_desc'], "Блок с длинным описанием не соответствует ожидаемому"
        
        