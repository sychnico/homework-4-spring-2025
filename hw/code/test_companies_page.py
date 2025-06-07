import pytest
from ui.constants.companies_constants import CampaignConstants

class TestCampaignPage():
    @pytest.mark.parametrize("campaign_data", [
        {
            "name": "Компания Гигачадов",
            "group": "Группа Гигачадов",
            "ad": "Объявление Гигачадов",
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
        campaign_page.fill_campaign_form()
        campaign_page.click_continue_button()
        campaign_page.rename_entity(campaign_data["group"])
        campaign_page.click_russia_button(const.Sections.REGIONS)
        campaign_page.click_interest_section(const.Sections.NAMES)
        campaign_page.click_interest_subsection()
        campaign_page.fill_interests(const.Targeting.INTEREST)
        campaign_page.click_stop_interest_opener()
        assert campaign_page.has_stop_interest_content(), "Блок исключения интересов не отображается"
        campaign_page.fill_stop_interest(const.Targeting.STOP_INTEREST)
        campaign_page.click_interest_section(const.Sections.NAMES)
        campaign_page.click_device_section(const.Sections.NAMES)
        campaign_page.click_mobile_checkbox()
        campaign_page.click_continue_button()
        assert campaign_page.has_ads_inputs_content(), "Поля для ввода объявления не отображаются"
        campaign_page.rename_entity(campaign_data["ad"])
        campaign_page.click_logo_input()
        campaign_page.click_image_item()
        campaign_page.fill_ad_inputs_and_textarea(campaign_data["ad_content"])
        campaign_page.click_media()
        campaign_page.click_image_item()
        assert campaign_page.submit_button_became_visible(), "Кнопка отправки не появилась"
        campaign_page.click_submit_button()
        campaign_page.click_publish_button()
        campaign_page.driver.get("https://ads.vk.com/hq/dashboard/ad_plans")
        assert campaign_page.check_campaign_title(campaign_data["name"]), f"Кампания с именем {campaign_data['name']} не найдена"
        assert campaign_page.check_campaign_budget(), "Бюджет кампании не соответствует ожидаемому"
        assert campaign_page.check_campaign_action("Показы рекламы"), "Целевое действие не соответствует ожидаемому"
        campaign_page.click_group_tabs(const.Tabs.CAMPAIGN)
        assert campaign_page.check_group_title(campaign_data["group"]), f"Группа с именем {campaign_data['group']} не найдена"
        campaign_page.click_ad_tab(const.Tabs.CAMPAIGN)
        assert campaign_page.check_ad_title(campaign_data["ad"]), f"Объявление с именем {campaign_data['ad']} не найдено"
        assert campaign_page.check_ad_name(campaign_data["ad_content"]), "Заголовок объявления не соответствует ожидаемому"
        assert campaign_page.check_ad_short_description(campaign_data["ad_content"]), "Короткое описание не соответствует ожидаемому"
        assert campaign_page.check_ad_long_description(campaign_data["ad_content"]), "Длинное описание не соответствует ожидаемому"
        
        