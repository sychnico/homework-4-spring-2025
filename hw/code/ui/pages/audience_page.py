from .page import Page
from ui.locators.audience_locators import AudienceLocators

class AudiencePage(Page):
    URL = "https://ads.vk.com/hq/audience"
    locators = AudienceLocators()


    def click_create_audience_button(self):
        self.click(self.locators.CREATE_AUDIENCE_BUTTON)

    def click_add_external_audience(self):
        self.click(self.locators.ADD_EXTERNAL_AUDIENCE_BUTTON)

    def input_key_to_external_audience(self, key):
        input = self.find(self.locators.EXTERNAL_AUDIENCE_INPUT)
        input.send_keys(key)

    def click_activate_external_audience(self):
        self.click(self.locators.ACTIVATE_EXTERNAL_AUDIENCE_BUTTON)

    def is_modal_create_audience(self):
        return bool(self.driver.find_elements(*self.locators.MODAL_AUDIENCE))

    def input_name_audience(self, name):
        input = self.find(self.locators.NAME_AUDIENCE_INPUT)
        input.send_keys(name)

    def save_audience(self):
        self.click(self.locators.SAVE_AUDIENCE_BUTTON)

    def find_block_audience(self):
        return bool(self.driver.find_elements(*self.locators.AUDIENCE_BLOCK))

    def click_add_new_source(self):
        self.click(self.locators.ADD_NEW_SOURCE_BUTTON)

    def click_exclude_new_source(self):
        self.click(self.locators.EXCLUDE_NEW_SOURCE_BUTTON)

    def click_created_audience_source(self):
        self.click(self.locators.CREATED_AUDIENCE_SOURCE_BUTTON)

    def choose_created_audience(self):
        self.click(self.locators.LIST_OF_CREATED_AUDIENCE[0])

    def click_save_button(self):
        self.click(self.locators.SAVE_BUTTON)

    def click_user_list_source(self):
        self.click(self.locators.USER_LIST_SOURCE_BUTTON)

    def choose_user_list_source(self):
        self.click(self.locators.LIST_OF_USER_LIST[0])

    def click_key_words_source(self):
        self.click(self.locators.KEYWORDS_SOURCE_BUTTON)

    def input_name_keywords(self, name):
        input = self.find(self.locators.NAME_KEYWORDS_INPUT)
        input.send_keys(name)

    def input_keywords(self, keywords):
        input = self.find(self.locators.KEYWORDS_INPUT)
        input.send_keys(keywords)

    def input_minus_phrases(self, minus):
        input = self.find(self.locators.MINUS_PHRASES_INPUT)
        input.send_keys(minus)

    def input_days(self, days):
        input = self.find(self.locators.DAYS_INPUT)
        input.send_keys(days)

    def click_community_source(self):
        self.click(self.locators.COMMUNITY_SOURCE_BUTTON)

    def input_name_community(self, community):
        input = self.find(self.locators.COMMUNITY_NAME_INPUT)
        input.send_keys(community)

    def click_communities_group(self):
        self.click(self.locators.LIST_OF_GROUPES_COMMUNITIES[0])

    def click_community_in_group(self):
        self.click(self.locators.LIST_OF_COMMUNITIES[0])

    def click_button_add_communities(self):
        self.click(self.locators.ADD_COMMUNITY_BUTTON)

    def click_music_source(self):
        self.click(self.locators.MUSIC_SOURCE_BUTTON)

    def input_name_music(self, community):
        input = self.find(self.locators.MUSIC_NAME_INPUT)
        input.send_keys(community)

    def click_music(self):
        self.click(self.locators.LIST_OF_MUSIC[0])

    def click_button_add_music(self):
        self.click(self.locators.ADD_COMMUNITY_BUTTON)

    def click_apps_source(self):
        self.click(self.locators.APP_SOURCE_BUTTON)

    def input_name_app(self, community):
        input = self.find(self.locators.APP_INPUT)
        input.send_keys(community)

    def click_app(self):
        self.click(self.locators.LIST_OF_APPS[0])

    def click_button_add_app(self):
        self.click(self.locators.ADD_APP_BUTTON)


    def choose_audience_checkbox(self):
        self.click(self.locators.CHECKBOX_AUDIENCE[0])

    def click_delete_audience(self):
        self.click(self.locators.DELETE_AUDIENCE_BUTTON)

    def input_search(self, words):
        input = self.find(self.locators.AUDIENCE_SEARCH_INPUT)
        input.send_keys(words)

    def find_message(self):
        return bool(self.driver.find_elements(*self.locators.MESSAGE_TOO_FEW))

    #################

    def click_list_users(self):
        self.click(self.locators.CREATE_NEW_LIST_USERS_BUTTON)

    def click_download_list_users(self):
        self.click(self.locators.DOWNLOAD_NEW_LIST_USERS_BUTTON)

    def input_name_list_users(self, name):
        input = self.find(self.locators.NAME_LIST_USERS_INPUT)
        input.send_keys(name)

    def choose_type_of_list_users(self):
        self.click(self.locators.LIST_OF_TYPES_USER_LISTS[0])

    def download_file_user_list(self, filepath):
        download = self.find(self.locators.DOWNLOAD_FILE_LIST_USERS_BUTTON)
        download.send_keys(filepath)

    def find_error_message_about_file(self):
        return bool(self.driver.find_elements(*self.locators.ERROR_FILE))

    def click_save_user_list(self):
        self.click(self.locators.SAVE_USER_LIST)

    def find_new_list_users_block(self):
        return bool(self.driver.find_elements(*self.locators.USER_LIST_BLOCK))

    ##################

    def click_offline(self):
        self.click(self.locators.OFFLINE_BUTTON)

    def click_download_offline(self):
        self.click(self.locators.DOWNLOAD_OFFLINE_BUTTON)

    def click_create_new_offline(self):
        self.click(self.locators.DOWNLOAD_NEW_LIST_USERS_BUTTON)

    def input_name_offline(self, name):
        input = self.find(self.locators.NAME_OFFLINE_INPUT)
        input.send_keys(name)

    def choose_type_of_offline(self):
        self.click(self.locators.LIST_OF_TYPES_OFFLINE[0])

    def input_window_attribute(self, num):
        input = self.find(self.locators.WINDOW_OFFLINE_INPUT)
        input.send_keys(num)

    def download_file_offline(self, filepath):
        download = self.find(self.locators.DOWNLOAD_OFFLINE_FILE_BUTTON)
        download.send_keys(filepath)

    def click_save_offline(self):
        self.click(self.locators.SAVE_USER_LIST)

    def find_new_offline_block(self):
        return bool(self.driver.find_elements(*self.locators.OFFLINE_BLOCK))