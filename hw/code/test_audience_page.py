VALID_AUDIENCE_NAME = "Test Audience"
VALID_KEY = "test_key_123"
VALID_KEYWORDS = "keyword1, keyword2"
VALID_MINUS_PHRASES = "minus1, minus2"
VALID_DAYS = "30"
VALID_COMMUNITY_NAME = "Test Community"
VALID_MUSIC_NAME = "Test Music"
VALID_APP_NAME = "Test App"
VALID_USER_LIST_NAME = "Test User List"
VALID_OFFLINE_NAME = "Test Offline"
VALID_WINDOW = "15"
TEST_FILE_PATH = "/path/to/test/file.txt"

WRONG_AUDIENCE_NAME = ""
WRONG_KEY = "invalid_key"
WRONG_DAYS = "999"
WRONG_FILE_PATH = "/path/to/invalid/file.txt"


class TestAudiencePage:
    def test_open_audience_page(self, audience_page):
        assert audience_page.driver.current_url == audience_page.URL

    def test_create_audience_modal(self, audience_page):
        audience_page.click_create_audience_button()
        assert audience_page.is_modal_create_audience()

    def test_create_external_audience(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_add_external_audience()
        audience_page.input_key_to_external_audience(VALID_KEY)
        audience_page.click_activate_external_audience()
        assert audience_page.find_block_audience()

    def test_create_keywords_audience(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_key_words_source()
        audience_page.input_name_keywords(VALID_AUDIENCE_NAME)
        audience_page.input_keywords(VALID_KEYWORDS)
        audience_page.input_minus_phrases(VALID_MINUS_PHRASES)
        audience_page.input_days(VALID_DAYS)
        audience_page.save_audience()
        assert audience_page.find_block_audience()

    def test_create_community_audience(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_community_source()
        audience_page.input_name_community(VALID_COMMUNITY_NAME)
        audience_page.click_communities_group()
        audience_page.click_community_in_group()
        audience_page.click_button_add_communities()
        audience_page.save_audience()
        assert audience_page.find_block_audience()

    def test_create_music_audience(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_music_source()
        audience_page.input_name_music(VALID_MUSIC_NAME)
        audience_page.click_music()
        audience_page.click_button_add_music()
        audience_page.save_audience()
        assert audience_page.find_block_audience()

    def test_create_app_audience(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_apps_source()
        audience_page.input_name_app(VALID_APP_NAME)
        audience_page.click_app()
        audience_page.click_button_add_app()
        audience_page.save_audience()
        assert audience_page.find_block_audience()

    def test_delete_audience(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_key_words_source()
        audience_page.input_name_keywords(VALID_AUDIENCE_NAME)
        audience_page.save_audience()

        audience_page.choose_audience_checkbox()
        audience_page.click_delete_audience()
        assert not audience_page.find_block_audience()

    def test_search_audience(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_key_words_source()
        audience_page.input_name_keywords(VALID_AUDIENCE_NAME)
        audience_page.save_audience()

        audience_page.input_search(VALID_AUDIENCE_NAME)
        assert audience_page.find_block_audience()

    def test_create_user_list(self, audience_page):
        audience_page.click_list_users()
        audience_page.click_download_list_users()
        audience_page.input_name_list_users(VALID_USER_LIST_NAME)
        audience_page.choose_type_of_list_users()
        audience_page.download_file_user_list(TEST_FILE_PATH)
        audience_page.click_save_user_list()
        assert audience_page.find_new_list_users_block()

    def test_create_offline_audience(self, audience_page):
        audience_page.click_offline()
        audience_page.click_download_offline()
        audience_page.click_create_new_offline()
        audience_page.input_name_offline(VALID_OFFLINE_NAME)
        audience_page.choose_type_of_offline()
        audience_page.input_window_attribute(VALID_WINDOW)
        audience_page.download_file_offline(TEST_FILE_PATH)
        audience_page.click_save_offline()
        assert audience_page.find_new_offline_block()

    def test_invalid_file_upload(self, audience_page):
        audience_page.click_list_users()
        audience_page.click_download_list_users()
        audience_page.download_file_user_list(WRONG_FILE_PATH)
        assert audience_page.find_error_message_about_file()

    def test_empty_audience_name(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_key_words_source()
        audience_page.input_name_keywords(WRONG_AUDIENCE_NAME)
        audience_page.save_audience()
        assert audience_page.find_message()

    def test_add_source_to_audience(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_key_words_source()
        audience_page.input_name_keywords(VALID_AUDIENCE_NAME)
        audience_page.save_audience()

        audience_page.click_add_new_source()
        audience_page.click_user_list_source()
        audience_page.choose_user_list_source()
        audience_page.click_save_button()
        assert audience_page.find_block_audience()

    def test_exclude_source_from_audience(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_key_words_source()
        audience_page.input_name_keywords(VALID_AUDIENCE_NAME)
        audience_page.save_audience()

        audience_page.click_exclude_new_source()
        audience_page.click_user_list_source()
        audience_page.choose_user_list_source()
        audience_page.click_save_button()
        assert audience_page.find_block_audience()