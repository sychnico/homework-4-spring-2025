VALID_AUDIENCE_NAME_ADD = "Test Audience"
VALID_AUDIENCE_NAME_EXCLUDE = ""
INVALID_KEY = "test_key_123"
VALID_KEYWORDS = "keyword1, keyword2"
VALID_USER_LIST_NAME = "Test User List"
VALID_OFFLINE_NAME = "Test Offline"
VALID_KEYWORD_NAME = "Keywords"
INVALID_FILE_USERLIST = "hw/code/test_files/test_wrong_user_list.csv"
VALID_FILE_USERLIST = "hw/code/test_files/test_user_list.csv"
VALID_FILE_OFFLINE = "hw/code/test_files/test_offline_list.csv"
INVALID_FILE_OFFLINE = "hw/code/test_files/test_wrong_offline_list.csv"
ERROR_INVALID_KEY = "Ключ не найден"
ERROR_FILE = "Не удалось загрузить файл"

class TestAudiencePage:

    def test_add_external_audience_error(self, audience_page):
        audience_page.click_add_external_audience()
        audience_page.input_key_to_external_audience(INVALID_KEY)
        audience_page.click_activate_external_audience()
        assert audience_page.find(
            audience_page.locators.ERROR_MESSAGE).text == ERROR_INVALID_KEY

    def test_add_user_list_error(self, audience_page):
        audience_page.click_list_users()
        audience_page.click_download_list_users()
        audience_page.input_name_list_users(VALID_USER_LIST_NAME)
        audience_page.choose_type_of_list_users()
        audience_page.download_file_user_list(INVALID_FILE_USERLIST)
        audience_page.click_save_user_list()
        assert audience_page.find(
            audience_page.locators.ERROR_FILE_MODAL).text == ERROR_FILE
        assert not audience_page.became_visible(
            audience_page.locators.USERLIST_BLOCK_BY_NAME(VALID_USER_LIST_NAME))

    def test_add_user_list(self, audience_page):
        audience_page.click_list_users()
        audience_page.click_download_list_users()
        audience_page.input_name_list_users(VALID_USER_LIST_NAME)
        audience_page.choose_type_of_list_users()
        audience_page.download_file_user_list(VALID_FILE_USERLIST)
        audience_page.click_save_user_list()
        assert audience_page.became_visible(
            audience_page.locators.USERLIST_BLOCK_BY_NAME(VALID_USER_LIST_NAME))

    def test_add_offline_error(self, audience_page):
        audience_page.click_offline()
        audience_page.click_download_offline()
        audience_page.click_create_new_offline()
        audience_page.input_name_offline(VALID_OFFLINE_NAME)
        audience_page.choose_type_of_offline()
        audience_page.download_file_offline(INVALID_FILE_OFFLINE)
        audience_page.click_save_offline()
        assert audience_page.find(
            audience_page.locators.ERROR_FILE_MODAL).text == ERROR_FILE
        assert not audience_page.became_visible(
            audience_page.locators.OFFLINE_BLOCK_BY_NAME(VALID_OFFLINE_NAME))

    def test_add_offline(self, audience_page):
        audience_page.click_offline()
        audience_page.click_download_offline()
        audience_page.click_create_new_offline()
        audience_page.input_name_offline(VALID_OFFLINE_NAME)
        audience_page.choose_type_of_offline()
        audience_page.download_file_offline(VALID_FILE_OFFLINE)
        audience_page.click_save_offline()
        assert audience_page.became_visible(
            audience_page.locators.OFFLINE_BLOCK_BY_NAME(VALID_USER_LIST_NAME))

    def test_create_keywords_audience(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.input_name_audience(VALID_AUDIENCE_NAME_ADD)
        audience_page.click_add_new_source()
        audience_page.click_key_words_source()
        audience_page.input_name_keywords(VALID_KEYWORD_NAME)
        audience_page.input_keywords(VALID_KEYWORDS)
        audience_page.save_source()
        assert audience_page.became_visible(
            audience_page.locators.SOURCE_BLOCK_BY_NAME(VALID_USER_LIST_NAME))
        audience_page.save_audience()
        assert audience_page.became_visible(
            audience_page.locators.AUDIENCE_BLOCK_BY_NAME(VALID_USER_LIST_NAME))

    def test_exclude_keywords_source(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.input_name_audience(VALID_AUDIENCE_NAME_ADD)
        audience_page.click_exclude_new_source()
        audience_page.click_key_words_source()
        audience_page.input_name_keywords(VALID_KEYWORD_NAME)
        audience_page.input_keywords(VALID_KEYWORDS)
        audience_page.save_source()
        assert audience_page.became_visible(
            audience_page.locators.SOURCE_BLOCK_BY_NAME(VALID_USER_LIST_NAME))
        audience_page.save_audience()
        assert audience_page.became_visible(
            audience_page.locators.AUDIENCE_BLOCK_BY_NAME(VALID_USER_LIST_NAME))

