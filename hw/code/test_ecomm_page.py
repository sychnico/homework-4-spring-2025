FIT_RIGHT_URL = "https://vk.com/swimlike"
FIT_WRONG_URL = "https://tralalelotralala"
FIT_WRONG_VALUE = "tralalelotralala"

CATALOG_WITH_NOTES_TEXT = "Создать каталог с подсказками"
WATCH_CURSE_TEXT = "Смотреть курс на обучающей платформе"
WATCH_VIDEO_LESSON_TEXT = "Смотреть видеоурок от экспертов VK"

FIT_TAB_TEXT = "Фид или сообщество"
FILE_TAB_TEXT = "Вручную"
MARKET_TAB_TEXT = "Маркетплейс"

NULL_ERROR_TEXT = "Нужно заполнить"
WRONG_ERROR_TEXT = "Необходимо указать протокол http(s)"
HTTP_ERROR_TEXT = "Не удалось выполнить запрос по HTTP"

class TestEcommPage:
    def go_to_create(self, ecomm_page):
        ecomm_page.click_create_catalog()
        ecomm_page.click_fit_tab()
        
    def test_education_modal_open(self, ecomm_page):
        ecomm_page.close_modal()
        ecomm_page.click_start_education()
        assert ecomm_page.find_catalog_with_noteses().text == CATALOG_WITH_NOTES_TEXT
        assert ecomm_page.find_watch_curse().text == WATCH_CURSE_TEXT
        assert ecomm_page.find_watch_video_lesson().text == WATCH_VIDEO_LESSON_TEXT
        

        
    def test_create_catalog_modal_open(self, ecomm_page):
        ecomm_page.click_create_catalog()
        assert FIT_TAB_TEXT in ecomm_page.find_fit_tab().text
        assert FILE_TAB_TEXT in ecomm_page.find_file_tab().text
        assert MARKET_TAB_TEXT in ecomm_page.find_market_tab().text
        
    

    def test_fit_input_null_value(self, ecomm_page):
        self.go_to_create(ecomm_page)
        ecomm_page.click_create_catalog_inner()
        assert ecomm_page.get_fit_input_null_error().text == NULL_ERROR_TEXT
        
    def test_fit_input_wrong_value(self, ecomm_page):
        self.go_to_create(ecomm_page)
        fit = ecomm_page.find_fit_input()
        ecomm_page.set_fit_input(fit, FIT_WRONG_VALUE)
        ecomm_page.click_create_catalog_inner()
        assert ecomm_page.get_fit_input_wrong_error().text == WRONG_ERROR_TEXT
        
    def test_fit_input_wrong_http_value(self, ecomm_page):
        self.go_to_create(ecomm_page)
        fit = ecomm_page.find_fit_input()
        ecomm_page.set_fit_input(fit, FIT_WRONG_URL) 
        ecomm_page.click_create_catalog_inner()
        assert ecomm_page.get_fit_input_http_error().text == HTTP_ERROR_TEXT
        
    def test_create_catalog(self, ecomm_page):
        self.go_to_create(ecomm_page)
        fit = ecomm_page.find_fit_input()
        ecomm_page.set_fit_input(fit, FIT_RIGHT_URL)
        ecomm_page.click_create_catalog_inner()
        ecomm_page.driver.get("https://ads.vk.com/hq/ecomm/catalogs")
        assert "Каталог" in ecomm_page.find_catalog_name_input().text


