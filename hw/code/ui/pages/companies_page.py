from .page import Page
from ui.locators.companies_locators import CampaignPageLocators
from ui.constants.companies_constants import CampaignConstants as const

class CompaniesPage(Page):
    URL = const.URL
    locators = CampaignPageLocators()


    def name_sign_became_visible(self):
        return self.became_visible(self.locators.NAME_SIGN, timeout=3)

    def has_tabs_title_content(self):
        return self.became_visible(self.locators.TARGET_TABS, timeout=3) and self.became_visible(self.locators.RECOGNITION_TABS, timeout=3)

    def has_target_tabs_content_name_sign(self):
        return self.became_visible(self.locators.TARGET_TABS_SIGN, timeout=3)

    def has_target_tabs_content_cells(self, target_tabs):
        for t in target_tabs:
            if not self.became_visible(self.locators.CATEGORY_CELL(t), timeout=3):
                return False
        return True

    def has_recognition_tabs_content_name_sign(self):
        return self.became_visible(self.locators.RECOGNITION_TABS_SIGN)

    def has_recognition_tabs_content_cells(self, recognition_tabs):
        for r in recognition_tabs:
            if not self.became_visible(self.locators.CATEGORY_CELL(r)):
                return False
        return True

    def site_name_input_became_visible(self):
        return self.became_visible(self.locators.SITE_NAME_INPUT)

    def create_footer_became_visible(self):
        return self.became_visible(self.locators.CREATE_FOOTER)

    def has_create_footer_continue_button_content(self):
        return self.became_visible(self.locators.CREATE_FOOTER_CONTINUE)

    def has_create_footer_publish_button_content(self):
        return self.became_visible(self.locators.CREATE_FOOTER_PUBLISH)

    def click_continue_button(self):
        self.click(self.locators.CREATE_FOOTER_CONTINUE, timeout=4)

    def click_publish_button(self):
        self.click(self.locators.CREATE_FOOTER_PUBLISH, timeout=4)

    def has_error_site_name_content(self):
        for k in self.SITE_NAME_INPUT_ERROR_DICT:
            name = self.find(self.locators.SITE_NAME_INPUT, timeout=4)
            name.clear()
            name.send_keys(k)
            self.click_continue_button()
            if not self.became_visible(self.locators.ERROR_SITE_NAME(self.SITE_NAME_INPUT_ERROR_DICT[k])):
                return False
        return True

    def fill_site_name_with_valid_url(self, site_url):
        name = self.find(self.locators.SITE_NAME_INPUT, timeout=4)
        name.clear()
        name.send_keys(site_url)

    def banner_became_visible(self):
        return self.became_visible(self.locators.BANNER, timeout=4)

    def target_select_became_visible(self):
        return self.became_visible(self.locators.TARGET_ACTION_SELECT)

    def switch_became_visible(self):
        return self.became_visible(self.locators.SWITCH)

    def strategy_action_select_became_visible(self):
        return self.became_visible(self.locators.STRATEGY_ACTION_SELECT)

    def budget_inputs_became_visible(self):
        return self.became_visible(self.locators.BUDGET_INPUT) and self.became_visible(
            self.locators.BUDGET_PERIOD_SELECT)

    def data_inputs_became_visible(self):
        return self.became_visible(self.locators.START_DATE) and self.became_visible(self.locators.END_DATE)

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

    def fill_campaign_form(self):
        budget = self.find(self.locators.BUDGET_INPUT, timeout=10)
        budget.send_keys(150)
        self.click(self.locators.STRATEGY_ACTION_SELECT, timeout=10)
        self.click(self.locators.CREATE_FOOTER_CONTINUE, timeout=10)

    def has_sections_title_content(self, section_names):
        for s in section_names:
            if not self.became_visible(self.locators.SECTION(s)):
                return False
        return True

    def has_section_region_region_buttons_content(self, region_buttons):
        for r in region_buttons:
            if not self.became_visible(self.locators.REGION_BUTTON(r)):
                return False
        return True

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

    def has_gender_radio_content(self):
        for g in self.GENDER_NAME_LIST:
            if not self.became_visible(self.locators.GENDER_RADIO(g)):
                return False
        return True

    def has_age_select_content(self):
        return self.became_visible(self.locators.AGE_SELECT_CHECK('12')) and self.became_visible(
            self.locators.AGE_SELECT_CHECK('75'))

    def has_pegi_select_content(self):
        return self.became_visible(self.locators.PEGI_AGE_SELECT)

    def fill_demography(self, min_age, max_age, pegi):
        self.scroll_and_click(self.locators.AGE_SELECT_INPUT('12'))
        self.click(self.locators.DROPDOWN_OPTIONS(min_age))
        self.click(self.locators.AGE_SELECT_INPUT('75'))
        self.click(self.locators.DROPDOWN_OPTIONS(max_age))
        self.click(self.locators.PEGI_AGE_SELECT)
        self.click(self.locators.DROPDOWN_OPTIONS(pegi))

    def interest_subsection_became_visible(self):
        return self.became_visible(self.locators.INTEREST_SUBSECTION)

    def click_interest_subsection(self):
        self.click(self.locators.INTEREST_SUBSECTION)

    def has_interest_subsection_content(self):
        return self.became_visible(self.locators.INTEREST_SELECT) and self.became_visible(
            self.locators.STOP_INTEREST_OPENER)

    def fill_interests(self, interest):
        self.click(self.locators.INTEREST_SELECT)
        self.click(self.locators.DROPDOWN_OPTIONS(interest))
        self.click(self.locators.CLOSE_DROPDOWN_BUTTON)

    def click_stop_interest_opener(self):
        self.click(self.locators.STOP_INTEREST_OPENER)

    def has_stop_interest_content(self):
        return self.became_visible(self.locators.STOP_INTEREST_SELECT)

    def fill_stop_interest(self, stop_interest):
        self.scroll_and_click(self.locators.STOP_INTEREST_SELECT)
        self.scroll_and_click(self.locators.DROPDOWN_OPTIONS(stop_interest))

    def has_device_section_content(self):
        return self.became_visible(self.locators.DESKTOP_CHECKBOX) and self.became_visible(
            self.locators.MOBILE_CHECKBOX)

    def click_mobile_checkbox(self):
        self.click(self.locators.MOBILE_CHECKBOX)

    def logo_input_became_visible(self):
        return self.became_visible(self.locators.UPLOAD_AVATAR)

    def has_ads_inputs_content(self):
        return self.became_visible(self.locators.TITLE_LABEL) and self.became_visible(self.locators.BUTTON_TEXT)

    def has_ads_textarea_content(self):
        return self.became_visible(self.locators.SHORT_DESCRIPTION) and self.became_visible(
            self.locators.LONG_DESCRIPTION) and self.became_visible(self.locators.ADVERTISER_DESCRIPTION)

    def mediatec_became_visible(self):
        return self.became_visible(self.locators.MEDIATEC)

    def click_logo_input(self):
        self.click(self.locators.UPLOAD_AVATAR)

    def has_media_sidebar_content(self):
        return self.became_visible(self.locators.IMAGE_ITEM)

    def click_image_item(self):
        self.hover(self.locators.IMAGE_ITEM, timeout=3)
        self.click(self.locators.IMAGE_ITEM, timeout=3)

    def preview_image_became_visible(self):
        return self.became_visible(self.locators.PREVIEW_IMAGE)

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

    def has_mediatec_sidebar_image_content(self):
        return self.became_visible(self.locators.IMAGE_ITEM)

    def submit_button_became_visible(self):
        return self.became_visible(self.locators.SUBMIT_BUTTON)

    def click_submit_button(self):
        self.click(self.locators.SUBMIT_BUTTON)

    def media_content_list_became_visible(self):
        return self.became_visible(self.locators.MEDIA_CONTENT_LIST)

    def click_publish_button(self):
        self.became_visible(self.locators.CORARI, timeout=10)
        self.find(self.locators.CORARI, timeout=10)
        self.became_visible(self.locators.CREATE_FOOTER_PUBLISH, timeout=3)
        self.hover(self.locators.CREATE_FOOTER_PUBLISH, timeout=3)
        self.click(self.locators.CREATE_FOOTER_PUBLISH,  timeout=3)

    def buttons_changed(self):
        return self.became_invisible(self.locators.CREATE_FOOTER_CONTINUE) and self.became_visible(
            self.locators.CREATE_FOOTER_PUBLISH)

    def has_bug_modal_content(self):
        return self.became_visible(self.locators.MODAL_CANCEL_BUTTON) and self.became_visible(
            self.locators.MODAL_SEND_BUTTON)

    def click_send_bug_modal(self):
        self.click(self.locators.MODAL_SEND_BUTTON)

    def has_campaign_page_tabs_content(self, campaign_tabs):
        for t in campaign_tabs:
            if not self.became_visible(self.locators.ADS_PAGE_TABS(t)):
                return False
        return True

    def action_select_became_visible(self):
        return self.became_visible(self.locators.ACTION_SELECT)

    def checkbox_all_became_visible(self):
        return self.became_visible(self.locators.CHECKBOX_ALL)

    def check_campaign_title(self, campaign_name):
        return self.became_visible(self.locators.ENTITY_NAME_CELL(campaign_name))

    def check_campaign_budget(self):
        return self.became_visible(self.locators.BUDGET_CELL('150'))

    def check_campaign_action(self, action):
        return self.became_visible(self.locators.ACTION_CELL(action))

    def hover_campaign_title(self, campaign_name):
        return self.hover(self.locators.ENTITY_NAME_CELL(campaign_name))

    def edit_became_visible(self):
        return self.became_visible(self.locators.EDIT_CELL_TAPABLE)

    def click_edit(self):
        self.click(self.locators.EDIT_CELL_TAPABLE)

    def sidebar_buttons_became_visible(self):
        return self.became_visible(self.locators.SUBMIT_BUTTON) and self.became_visible(self.locators.CANCEL_BUTTON)

    def check_title_input_value_campaign(self, campaign_name):
        return self.became_visible(self.locators.ENTITY_NAME_TITLE(campaign_name))

    def check_site_name_value_campaign(self, url_text):
        return self.became_visible(self.locators.SIDEBAR_SITE_NAME_INPUT(url_text))

    def check_action_select_value_campaign(self, action):
        return self.became_visible(self.locators.SIDEBAR_ACTION_SELECT(action))

    def check_strategy_select_value_campaign(self, strategy):
        return self.became_visible(self.locators.SIDEBAR_STRATEGY_SELECT(strategy))

    def check_budget_input_value_campaign(self):
        return self.became_visible(self.locators.SIDEBAR_BUDGET_INPUT('150 ₽'))

    def check_budget_period_input_value_campaign(self):
        return self.became_visible(self.locators.SIDEBAR_BUDGET_SELECT('за день'))

    def click_cancel_button(self):
        return self.click(self.locators.CANCEL_BUTTON)

    def click_confirm_cancel_button(self):
        return self.click(self.locators.CONFIRM_CANCEL_BUTTON)

    def delete_entity(self):
        self.click(self.locators.CHECKBOX_ALL)
        self.click(self.locators.ACTION_SELECT)
        self.click(self.locators.DROPDOWN_OPTIONS('Удалить'))

    def click_group_tabs(self, campaign_tabs):
        self.click(self.locators.ADS_PAGE_TABS(campaign_tabs[1]))

    def check_group_title(self, group_name):
        return self.became_visible(self.locators.ENTITY_NAME_CELL(group_name))

    def check_title_input_value_group(self, group_name):
        return self.became_visible(self.locators.ENTITY_NAME_TITLE(group_name))

    def hover_group_title(self, group_name):
        return self.hover(self.locators.ENTITY_NAME_CELL(group_name))

    def check_selected_region(self, selected_region):
        return self.became_visible(self.locators.SELECTED_REGION(selected_region))

    def check_ages(self, min_age, max_age):
        return self.became_visible(self.locators.AGE_SELECT_CHECK(min_age)) and self.became_visible(
            self.locators.AGE_SELECT_CHECK(max_age))

    def check_pegi(self):
        return self.became_visible(self.locators.PEGI_16_AGE_SELECT)

    def check_interest(self, interest):
        return self.became_visible(self.locators.INTEREST_CHIP(interest))

    def check_stop_interest(self, stop_interest):
        return self.became_visible(self.locators.STOP_INTEREST_CHIP(stop_interest))

    def check_devices(self):
        return self.became_visible(
            self.locators.CHECKBOX_NAME_IS_CHECKED_OR_NOT('Десктопные', 'on')) and self.became_visible(
            self.locators.CHECKBOX_NAME_IS_CHECKED_OR_NOT('Мобильные', 'off'))

    def click_ad_tab(self, campaign_tabs):
        self.click(self.locators.ADS_PAGE_TABS(campaign_tabs[2]))

    def check_ad_title(self, ad_name):
        return self.became_visible(self.locators.ENTITY_NAME_CELL(ad_name))

    def hover_ad_title(self, ad_name):
        return self.hover(self.locators.ENTITY_NAME_CELL(ad_name))

    def check_ad_name(self, ad_content):
        return self.became_visible(self.locators.SIDEBAR_AD_INPUT('Заголовок', ad_content['title']))

    def check_ad_short_description(self, ad_content):
        return self.find(self.locators.SHORT_DESCRIPTION_TEXT).text == ad_content['short_desc']

    def check_ad_long_description(self, ad_content):
        return self.find(self.locators.LONG_DESCRIPTION_TEXT).text == ad_content['long_desc']

    def check_ad_button_text(self, ad_content):
        return self.became_visible(self.locators.SIDEBAR_AD_INPUT('Текст рядом с кнопкой', ad_content['button_text']))

    def check_ad_advertiser(self, ad_content):
        return self.find(self.locators.ADVERTISER_DESCRIPTION_TEXT).text == ad_content['advertiser']