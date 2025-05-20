from .page import Page
from ui.locators.companies_locators import CampaignPageLocators

class CompaniesPage(Page):
    URL = 'https://ads.vk.com/hq/dashboard/ad_plans'
    locators = CampaignPageLocators()

    TARGET_TABS_CONTENT_LIST = ['Сайт', 'Каталог товаров', 'Мобильное приложение', 'Сообщество и профиль',
                                'Группа и профиль ОК', 'Дзен', 'Лид-формы и опросы', 'VK Mini Apps и игры', 'Музыка',
                                'Видео и трансляции']

    RECOGNITION_TABS_CONTENT_LIST = ['Баннерная реклама', 'Видеореклама', 'Реклама в Дзене', 'HTML5 баннер',
                                     'Премиальное размещение']

    SECTION_NAME_LIST = ['Регионы показа', 'Демография', 'Интересы и поведение', 'Устройства', 'Аудитории',
                         'Параметры URL', 'Места размещения']

    REGION_BUTTON_NAME_LIST = ['Россия', 'Москва', 'Санкт-Петербург']

    CAMPAIGN_PAGE_TABS_LIST = ['Кампании', 'Группы', 'Объявления']

    url = 'https://education.vk.company/'
    URL_TEXT = 'education.vk.company'
    MIN_AGE = '16'
    PEGI = '16+'
    MAX_AGE = '68'
    CAMPAIGN_NAME = "Makarov Campaign"
    GROUP_NAME = "Makarov Group"
    AD_NAME = "Makarov Ad"
    AD_TITLE = 'Abob'
    AD_SHORT_DESC = 'Best Task Tracker'
    AD_LONG_DESC = 'Mr. Beast will give u 6000$ if u use it'
    AD_BUTTON_TEXT = 'SHISHKA'
    AD_ADVERTISER = 'BMSTU, Mr. Makarov'
    SELECTED_REGION = 'Россия'
    INTEREST = 'Автобарахолка'
    STOP_INTEREST = 'Авто премиум класс'
    CAMPAIGN_ACTION = 'Показы рекламы'
    CAMPAIGN_STRATEGY = 'Минимальная цена'

    def name_sign_became_visible(self):
        return self.became_visible(self.locators.NAME_SIGN, timeout=3)

    def has_tabs_title_content(self):
        return self.became_visible(self.locators.TARGET_TABS, timeout=3) and self.became_visible(self.locators.RECOGNITION_TABS, timeout=3)

    def has_target_tabs_content_name_sign(self):
        return self.became_visible(self.locators.TARGET_TABS_SIGN, timeout=3)

    def has_target_tabs_content_cells(self):
        for t in self.TARGET_TABS_CONTENT_LIST:
            if not self.became_visible(self.locators.CATEGORY_CELL(t), timeout=3):
                return False
        return True

    def has_recognition_tabs_content_name_sign(self):
        return self.became_visible(self.locators.RECOGNITION_TABS_SIGN)

    def has_recognition_tabs_content_cells(self):
        for r in self.RECOGNITION_TABS_CONTENT_LIST:
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

    def fill_site_name_with_valid_url(self):
        name = self.find(self.locators.SITE_NAME_INPUT, timeout=4)
        name.clear()
        name.send_keys(self.url)

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

    def click_site_cell(self):
        self.click(self.locators.CATEGORY_CELL(self.TARGET_TABS_CONTENT_LIST[0]))

    def rename_entity(self, name):
        self.click(self.locators.NAME_SIGN)
        name_edit = self.find(self.locators.NAME_EDIT)
        name_edit.send_keys(name)
        self.click(self.locators.CREATE_FOOTER)

    def fill_campaign_form(self):
        budget = self.find(self.locators.BUDGET_INPUT, timeout=10)
        budget.send_keys(150)
        # self.click(self.locators.TARGET_ACTION_SELECT, timeout=10)
        # self.became_visible(self.locators.POKAZ, timeout=10)
        # self.click(self.locators.POKAZ, timeout=10)
        self.click(self.locators.STRATEGY_ACTION_SELECT, timeout=10)
        self.click(self.locators.CREATE_FOOTER_CONTINUE, timeout=10)

    def has_sections_title_content(self):
        for s in self.SECTION_NAME_LIST:
            if not self.became_visible(self.locators.SECTION(s)):
                return False
        return True

    def has_section_region_region_buttons_content(self):
        for r in self.REGION_BUTTON_NAME_LIST:
            if not self.became_visible(self.locators.REGION_BUTTON(r)):
                return False
        return True

    def click_russia_button(self):
        self.click(self.locators.REGION_BUTTON(self.REGION_BUTTON_NAME_LIST[0]))

    def click_regions_section(self):
        self.click(self.locators.SECTION(self.SECTION_NAME_LIST[0]))

    def click_demography_section(self):
        self.scroll_and_click(self.locators.SECTION(self.SECTION_NAME_LIST[1]))

    def click_interest_section(self):
        self.scroll_and_click(self.locators.SECTION(self.SECTION_NAME_LIST[2]))

    def click_device_section(self):
        self.scroll_and_click(self.locators.SECTION(self.SECTION_NAME_LIST[3]))

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

    def fill_demography(self):
        self.scroll_and_click(self.locators.AGE_SELECT_INPUT('12'))
        self.scroll_and_click(self.locators.DROPDOWN_OPTIONS(self.MIN_AGE))
        self.scroll_and_click(self.locators.AGE_SELECT_INPUT('75'))
        self.scroll_and_click(self.locators.DROPDOWN_OPTIONS(self.MAX_AGE))
        self.scroll_and_click(self.locators.PEGI_AGE_SELECT)
        self.scroll_and_click(self.locators.DROPDOWN_OPTIONS(self.PEGI))

    def interest_subsection_became_visible(self):
        return self.became_visible(self.locators.INTEREST_SUBSECTION)

    def click_interest_subsection(self):
        self.click(self.locators.INTEREST_SUBSECTION)

    def has_interest_subsection_content(self):
        return self.became_visible(self.locators.INTEREST_SELECT) and self.became_visible(
            self.locators.STOP_INTEREST_OPENER)

    def fill_interests(self):
        self.click(self.locators.INTEREST_SELECT)
        self.click(self.locators.DROPDOWN_OPTIONS(self.INTEREST))
        self.click(self.locators.CLOSE_DROPDOWN_BUTTON)

    def click_stop_interest_opener(self):
        self.click(self.locators.STOP_INTEREST_OPENER)

    def has_stop_interest_content(self):
        return self.became_visible(self.locators.STOP_INTEREST_SELECT)

    def fill_stop_interest(self):
        self.scroll_and_click(self.locators.STOP_INTEREST_SELECT)
        self.scroll_and_click(self.locators.DROPDOWN_OPTIONS(self.STOP_INTEREST))

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
        self.click(self.locators.IMAGE_ITEM)

    def preview_image_became_visible(self):
        return self.became_visible(self.locators.PREVIEW_IMAGE)

    def fill_ad_inputs_and_textarea(self):
        title = self.find(self.locators.TITLE_INPUT)
        title.click()
        title.clear()
        title.send_keys(self.AD_TITLE)
        short = self.find(self.locators.SHORT_DESCRIPTION_INPUT)
        short.click()
        short.clear()
        short.send_keys(self.AD_SHORT_DESC)
        long = self.find(self.locators.LONG_DESCRIPTION_INPUT)
        long.click()
        long.clear()
        long.send_keys(self.AD_LONG_DESC)
        button_text = self.find(self.locators.BUTTON_TEXT_INPUT)
        button_text.click()
        button_text.clear()
        button_text.send_keys(self.AD_BUTTON_TEXT)
        advertiser = self.find(self.locators.ADVERTISER_DESCRIPTION_INPUT)
        advertiser.click()
        advertiser.clear()
        advertiser.send_keys(self.AD_ADVERTISER)

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
        self.click(self.locators.CREATE_FOOTER_PUBLISH)

    def buttons_changed(self):
        return self.became_invisible(self.locators.CREATE_FOOTER_CONTINUE) and self.became_visible(
            self.locators.CREATE_FOOTER_PUBLISH)

    def has_bug_modal_content(self):
        return self.became_visible(self.locators.MODAL_CANCEL_BUTTON) and self.became_visible(
            self.locators.MODAL_SEND_BUTTON)

    def click_send_bug_modal(self):
        self.click(self.locators.MODAL_SEND_BUTTON)

    def has_campaign_page_tabs_content(self):
        for t in self.CAMPAIGN_PAGE_TABS_LIST:
            if not self.became_visible(self.locators.ADS_PAGE_TABS(t)):
                return False
        return True

    def action_select_became_visible(self):
        return self.became_visible(self.locators.ACTION_SELECT)

    def checkbox_all_became_visible(self):
        return self.became_visible(self.locators.CHECKBOX_ALL)

    def check_campaign_title(self):
        return self.became_visible(self.locators.ENTITY_NAME_CELL(self.CAMPAIGN_NAME))

    def check_campaign_budget(self):
        return self.became_visible(self.locators.BUDGET_CELL('150'))

    def check_campaign_action(self):
        return self.became_visible(self.locators.ACTION_CELL(self.CAMPAIGN_ACTION))

    def hover_campaign_title(self):
        return self.hover(self.locators.ENTITY_NAME_CELL(self.CAMPAIGN_NAME))

    def edit_became_visible(self):
        return self.became_visible(self.locators.EDIT_CELL_TAPABLE)

    def click_edit(self):
        self.click(self.locators.EDIT_CELL_TAPABLE)

    def sidebar_buttons_became_visible(self):
        return self.became_visible(self.locators.SUBMIT_BUTTON) and self.became_visible(self.locators.CANCEL_BUTTON)

    def check_title_input_value_campaign(self):
        return self.became_visible(self.locators.ENTITY_NAME_TITLE(self.CAMPAIGN_NAME))

    def check_site_name_value_campaign(self):
        return self.became_visible(self.locators.SIDEBAR_SITE_NAME_INPUT(self.URL_TEXT))

    def check_action_select_value_campaign(self):
        return self.became_visible(self.locators.SIDEBAR_ACTION_SELECT(self.CAMPAIGN_ACTION))

    def check_strategy_select_value_campaign(self):
        return self.became_visible(self.locators.SIDEBAR_STRATEGY_SELECT(self.CAMPAIGN_STRATEGY))

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

    def click_group_tabs(self):
        self.click(self.locators.ADS_PAGE_TABS(self.CAMPAIGN_PAGE_TABS_LIST[1]))

    def check_group_title(self):
        return self.became_visible(self.locators.ENTITY_NAME_CELL(self.GROUP_NAME))

    def check_title_input_value_group(self):
        return self.became_visible(self.locators.ENTITY_NAME_TITLE(self.GROUP_NAME))

    def hover_group_title(self):
        return self.hover(self.locators.ENTITY_NAME_CELL(self.GROUP_NAME))

    def check_selected_region(self):
        return self.became_visible(self.locators.SELECTED_REGION(self.SELECTED_REGION))

    def check_ages(self):
        return self.became_visible(self.locators.AGE_SELECT_CHECK(self.MIN_AGE)) and self.became_visible(
            self.locators.AGE_SELECT_CHECK(self.MAX_AGE))

    def check_pegi(self):
        return self.became_visible(self.locators.PEGI_16_AGE_SELECT)

    def check_interest(self):
        return self.became_visible(self.locators.INTEREST_CHIP(self.INTEREST))

    def check_stop_interest(self):
        return self.became_visible(self.locators.STOP_INTEREST_CHIP(self.STOP_INTEREST))

    def check_devices(self):
        return self.became_visible(
            self.locators.CHECKBOX_NAME_IS_CHECKED_OR_NOT('Десктопные', 'on')) and self.became_visible(
            self.locators.CHECKBOX_NAME_IS_CHECKED_OR_NOT('Мобильные', 'off'))

    def click_ad_tab(self):
        self.click(self.locators.ADS_PAGE_TABS(self.CAMPAIGN_PAGE_TABS_LIST[2]))

    def check_ad_title(self):
        return self.became_visible(self.locators.ENTITY_NAME_CELL(self.AD_NAME))

    def hover_ad_title(self):
        return self.hover(self.locators.ENTITY_NAME_CELL(self.AD_NAME))

    def check_ad_name(self):
        return self.became_visible(self.locators.SIDEBAR_AD_INPUT('Заголовок', self.AD_TITLE))

    def check_ad_short_description(self):
        return self.find(self.locators.SHORT_DESCRIPTION_TEXT).text == self.AD_SHORT_DESC

    def check_ad_long_description(self):
        return self.find(self.locators.LONG_DESCRIPTION_TEXT).text == self.AD_LONG_DESC

    def check_ad_button_text(self):
        return self.became_visible(self.locators.SIDEBAR_AD_INPUT('Текст рядом с кнопкой', self.AD_BUTTON_TEXT))

    def check_ad_advertiser(self):
        return self.find(self.locators.ADVERTISER_DESCRIPTION_TEXT).text == self.AD_ADVERTISER