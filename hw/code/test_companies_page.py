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
        flag_camp_name = campaign_page.check_visible_name(campaign_data['name'])
        assert flag_camp_name, f"Компания с именем {campaign_data['name']} не найдена"
        campaign_page.click_group_tabs(const.Tabs.CAMPAIGN)
        flag_group_name = campaign_page.check_visible_name(campaign_data['group'])
        assert flag_group_name, f"Группа с именем {campaign_data['group']} не найдена"
        campaign_page.click_ad_tab(const.Tabs.CAMPAIGN)
        flag_ad_name = campaign_page.check_visible_name(campaign_data['ad'])
        assert flag_ad_name, f"Объявление с именем {campaign_data['ad']} не найдено"
        flag_title = campaign_page.check_visible_title(const.TITLE, campaign_data['title'])
        assert flag_title, "Заголовок объявления не соответствует ожидаемому"
        short_description = campaign_page.get_short_description()
        assert short_description == campaign_data['short_desc'], "Блок с коротким описанием не соответствует ожидаемому"
        long_description = campaign_page.get_long_description()
        assert long_description == campaign_data['long_desc'], "Блок с длинным описанием не соответствует ожидаемому"




