from .page import Page
from ui.locators.companies_locators import CampaignPageLocators
from ui.constants.companies_constants import CampaignConstants as const

class CompaniesPage(Page):
    URL = const.URL
    locators = CampaignPageLocators()

    def check_visible_name(self, name):
        return self.became_visible(self.locators.ENTITY_NAME_CELL(name))

    def check_visible_title(self, title_in_page, compare_title):
        return self.became_visible(self.locators.SIDEBAR_AD_INPUT(title_in_page, compare_title))

    def get_short_description(self):
        return self.find(self.locators.SHORT_DESCRIPTION_TEXT).text

    def get_long_description(self):
        return self.find(self.locators.LONG_DESCRIPTION_TEXT).text

    def click_continue_button(self):
        self.click(self.locators.CREATE_FOOTER_CONTINUE, timeout=4)

    def click_publish_button(self):
        self.click(self.locators.CREATE_FOOTER_PUBLISH, timeout=4)


    def fill_site_name_with_valid_url(self, site_url):
        name = self.find(self.locators.SITE_NAME_INPUT, timeout=4)
        name.clear()
        name.send_keys(site_url)
 
    def click_create_button(self):
        self.click(self.locators.CREATE_BUTTON)

    def click_recognition_tabs(self):
        self.click(self.locators.RECOGNITION_TABS)

    def click_target_tabs(self):
        self.click(self.locators.TARGET_TABS)

    def click_site_cell(self, target_tabs):
        self.click(self.locators.CATEGORY_CELL(target_tabs[0]))

    def rename_entity(self, name):
        self.click(self.locators.NAME_SIGN)
        name_edit = self.find(self.locators.NAME_EDIT)
        name_edit.send_keys(name)
        self.click(self.locators.CREATE_FOOTER)

    def fill_campaign_form(self, budget):
        budget = self.find(self.locators.BUDGET_INPUT, timeout=10)
        budget.send_keys(budget)
        self.click(self.locators.STRATEGY_ACTION_SELECT, timeout=10)
        self.click(self.locators.CREATE_FOOTER_CONTINUE, timeout=10)

    def click_russia_button(self, region_buttons):
        self.click(self.locators.CREATE_FOOTER_CONTINUE, timeout=10)
        self.click(self.locators.REGION_BUTTON(region_buttons[0]))

    def click_regions_section(self, section_names):
        self.click(self.locators.SECTION(section_names[0]))

    def click_demography_section(self, section_names):
        self.scroll_and_click(self.locators.SECTION(section_names[1]))

    def click_interest_section(self, section_names):
        self.scroll_and_click(self.locators.SECTION(section_names[2]))

    def click_device_section(self, section_names):
        self.scroll_and_click(self.locators.SECTION(section_names[3]))

    
    def fill_demography(self, min_age, max_age, pegi):
        self.scroll_and_click(self.locators.AGE_SELECT_INPUT('12'))
        self.click(self.locators.DROPDOWN_OPTIONS(min_age))
        self.click(self.locators.AGE_SELECT_INPUT('75'))
        self.click(self.locators.DROPDOWN_OPTIONS(max_age))
        self.click(self.locators.PEGI_AGE_SELECT)
        self.click(self.locators.DROPDOWN_OPTIONS(pegi))

    def click_interest_subsection(self):
        self.click(self.locators.INTEREST_SUBSECTION)

 
    def fill_interests(self, interest):
        self.click(self.locators.INTEREST_SELECT)
        self.click(self.locators.DROPDOWN_OPTIONS(interest))
        self.click(self.locators.CLOSE_DROPDOWN_BUTTON)

    def click_stop_interest_opener(self):
        self.click(self.locators.STOP_INTEREST_OPENER)


    def fill_stop_interest(self, stop_interest):
        self.scroll_and_click(self.locators.STOP_INTEREST_SELECT)
        self.scroll_and_click(self.locators.DROPDOWN_OPTIONS(stop_interest))

  
    def click_mobile_checkbox(self):
        self.click(self.locators.MOBILE_CHECKBOX)

    
    def click_logo_input(self):
        self.click(self.locators.UPLOAD_AVATAR)

  
    def click_image_item(self):
        self.hover(self.locators.IMAGE_ITEM, timeout=3)
        self.click(self.locators.IMAGE_ITEM, timeout=3)

  
    def fill_ad_inputs_and_textarea(self, ad_content):
        title = self.find(self.locators.TITLE_INPUT)
        title.click()
        title.clear()
        title.send_keys(ad_content['title'])
        short = self.find(self.locators.SHORT_DESCRIPTION_INPUT)
        short.click()
        short.clear()
        short.send_keys(ad_content['short_desc'])
        long = self.find(self.locators.LONG_DESCRIPTION_INPUT)
        long.click()
        long.clear()
        long.send_keys(ad_content['long_desc'])
        button_text = self.find(self.locators.BUTTON_TEXT_INPUT)
        button_text.click()
        button_text.clear()
        button_text.send_keys(ad_content['button_text'])
        advertiser = self.find(self.locators.ADVERTISER_DESCRIPTION_INPUT)
        advertiser.click()
        advertiser.clear()
        advertiser.send_keys(ad_content['advertiser'])

    def click_media(self):
        self.click(self.locators.MEDIATEC)

  
    def click_submit_button(self):
        self.click(self.locators.SUBMIT_BUTTON)

 
    def click_publish_button(self):
        self.became_visible(self.locators.CORARI, timeout=10)
        self.find(self.locators.CORARI, timeout=10)
        self.became_visible(self.locators.CREATE_FOOTER_PUBLISH, timeout=3)
        self.hover(self.locators.CREATE_FOOTER_PUBLISH, timeout=3)
        self.click(self.locators.CREATE_FOOTER_PUBLISH,  timeout=3)

    def click_group_tabs(self, campaign_tabs):
        self.click(self.locators.ADS_PAGE_TABS(campaign_tabs[1]))

 
    def click_ad_tab(self, campaign_tabs):
        self.click(self.locators.ADS_PAGE_TABS(campaign_tabs[2]))