from .page import Page
from ui.locators.audience_locators import AudienceLocators
from selenium.webdriver.support.ui import Select
import os
from os import path
from selenium.webdriver.common.action_chains import ActionChains

class AudiencePage(Page):
    URL = "https://ads.vk.com/hq/audience"
    locators = AudienceLocators()

    def has_this_element(self, locator):
        return self.became_visible(locator, timeout=3)

    def delete_audience(self, name):
        list = self.find(self.locators.AUDIENCE_BLOCK_BY_NAME(name))
        ActionChains(self.driver).move_to_element(list).perform()
        menu = self.find(self.locators.AUDIENCE_ITEM_MENU)
        ActionChains(self.driver).move_to_element(menu).click(menu).perform()
        delete = self.find(self.locators.DELETE_BUTTON)
        delete.click()
        confirm = self.find(self.locators.DELETE_CONFIRM_BUTTON)
        confirm.click()

    def delete_user_list(self, name):
        list = self.find(self.locators.USERLIST_BLOCK_BY_NAME(name))
        ActionChains(self.driver).move_to_element(list).perform()
        menu = self.find(self.locators.AUDIENCE_ITEM_MENU)
        ActionChains(self.driver).move_to_element(menu).click(menu).perform()
        delete = self.find(self.locators.DELETE_BUTTON)
        delete.click()
        confirm = self.find(self.locators.DELETE_CONFIRM_BUTTON)
        confirm.click()

    def find_offline(self, name):
        return self.locators.OFFLINE_BLOCK_BY_NAME(name)
    def find_audience(self, name):
        return self.locators.AUDIENCE_BLOCK_BY_NAME(name)
    def find_userlist(self, name):
        return self.locators.USERLIST_BLOCK_BY_NAME(name)

    def click_create_audience_button(self):
        self.click(self.locators.CREATE_AUDIENCE_BUTTON, 10)

    def click_add_external_audience(self):
        self.click(self.locators.MORE_ACTIONS, 5)
        self.click(self.locators.ADD_EXTERNAL_AUDIENCE_BUTTON, 5)

    def input_key_to_external_audience(self, key):
        input = self.find(self.locators.EXTERNAL_AUDIENCE_INPUT, 5)
        input.send_keys(key)

    def click_activate_external_audience(self):
        self.scroll_and_click(self.locators.ACTIVATE_EXTERNAL_AUDIENCE_BUTTON, 10)

    def is_error(self):
        return bool(self.find(self.locators.ERROR_MESSAGE, 10))

    def save_source(self):
        self.click(self.locators.SAVE_BUTTON, 5)

    def find_block_audience(self):
        return bool(self.find(self.locators.AUDIENCE_BLOCK, 5))

    def input_name_audience(self, name):
        input = self.find(self.locators.NAME_AUDIENCE_INPUT, 5)
        self.driver.execute_script("arguments[0].value = '';", input)
        input.send_keys(name)


    def save_audience(self):
        self.click(self.locators.SAVE_AUDIENCE_BUTTON, 5)

    def click_add_new_source(self):
        self.click(self.locators.ADD_NEW_SOURCE_BUTTON, 10)

    def click_exclude_new_source(self):
        self.click(self.locators.EXCLUDE_NEW_SOURCE_BUTTON, 5)

    def click_key_words_source(self):
        self.click(self.locators.KEYWORDS_SOURCE_BUTTON, 5)

    def input_name_keywords(self, name):
        input = self.find(self.locators.NAME_KEYWORDS_INPUT, 5)
        self.driver.execute_script("arguments[0].value = '';", input)
        input.send_keys(name)

    def input_keywords(self, keywords):
        input = self.find(self.locators.KEYWORDS_INPUT, 5)
        input.send_keys(keywords)

    def click_list_users(self):
        self.click(self.locators.LIST_USERS_SECTION, 5)

    def click_download_list_users(self):
        self.click(self.locators.DOWNLOAD_NEW_LIST_USERS_BUTTON, 10)

    def input_name_list_users(self, name):
        input = self.find(self.locators.NAME_LIST_USERS_INPUT, 5)
        self.driver.execute_script("arguments[0].value = '';", input)
        input.send_keys(name)

    def choose_type_of_list_users(self):
        self.click(self.locators.LIST_OF_TYPES_USER_LISTS, 5)
        self.click(self.locators.TYPE_USER_LIST, 5)

    def download_file_user_list(self, filepath):
        filepathCorrect = os.path.abspath(path.join(path.curdir, filepath))
        download = self.find(self.locators.DOWNLOAD_FILE_LIST_USERS_BUTTON, 5)
        download.send_keys(filepathCorrect)

    def find_error_message_about_file(self):
        return bool(self.find(self.locators.ERROR_FILE, 5))

    def click_save_user_list(self):
        self.click(self.locators.SAVE_USER_LIST, 5)

    def find_new_list_users_block(self):
        return bool(self.find(self.locators.USER_LIST_BLOCK, 5))

    def click_offline(self):
        self.click(self.locators.OFFLINE_SECTION, 5)

    def click_download_offline(self):
        self.click(self.locators.DOWNLOAD_OFFLINE_BUTTON, 5)

    def click_create_new_offline(self):
        self.click(self.locators.CREATE_NEW_OFFLINE, 5)

    def input_name_offline(self, name):
        input = self.find(self.locators.NAME_OFFLINE_INPUT, 5)
        self.driver.execute_script("arguments[0].value = '';", input)
        input.send_keys(name)

    def choose_type_of_offline(self):
        self.click(self.locators.LIST_OF_TYPES_OFFLINE, 5)
        self.click(self.locators.TYPE_OFFLINE, 5)

    def download_file_offline(self, filepath):
        filepathCorrect = os.path.abspath(path.join(path.curdir, filepath))
        download = self.find(self.locators.DOWNLOAD_OFFLINE_FILE_BUTTON, 5)
        download.send_keys(filepathCorrect)

    def click_save_offline(self):
        self.click(self.locators.SAVE_OFFLINE, 5)

    def find_new_offline_block(self):
        return bool(self.find(self.locators.OFFLINE_BLOCK, 5))