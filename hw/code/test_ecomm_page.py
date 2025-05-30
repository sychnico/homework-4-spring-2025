FIT_RIGHT_URL = "https://vk.com/swimlike"
FIT_WRONG_URL = "https://tralalelotralala"
FIT_WRONG_VALUE = "tralalelotralala"

class TestEcommPage:
    
    def test_education_modal_open(self, ecomm_page):
        ecomm_page.close_modal()
        ecomm_page.click_start_education()
        assert ecomm_page.find_catalog_with_noteses()
        assert ecomm_page.find_watch_curse()
        assert ecomm_page.find_watch_video_lesson()
        
    def test_education_modal_close(self, ecomm_page):
        ecomm_page.click_start_education()
        ecomm_page.close_modal()
        ecomm_page.wait_modal_disappears()
        
    def test_create_catalog_modal_open(self, ecomm_page):
        ecomm_page.click_create_catalog()
        assert ecomm_page.find_modal()
        assert ecomm_page.find_fit_tab()
        assert ecomm_page.find_file_tab()
        assert ecomm_page.find_market_tab()
        
    def test_create_catalog_modal_tabing(self, ecomm_page):
        ecomm_page.click_create_catalog()
        assert ecomm_page.click_fit_tab()
        assert ecomm_page.click_file_tab()
        assert ecomm_page.click_market_tab()
        
    def test_fit_input_null_value(self, ecomm_page):
        ecomm_page.click_create_catalog()
        ecomm_page.click_fit_tab()
        ecomm_page.click_create_catalog_inner()
        assert ecomm_page.get_fit_input_null_error()
        
    def test_fit_input_wrong_value(self, ecomm_page):
        ecomm_page.click_create_catalog()
        ecomm_page.click_fit_tab()
        ecomm_page.set_fit_input(FIT_WRONG_VALUE)
        ecomm_page.click_create_catalog_inner()
        assert ecomm_page.get_fit_input_wrong_error()
        
    def test_fit_input_wrong_http_value(self, ecomm_page):
        ecomm_page.click_create_catalog()
        ecomm_page.click_fit_tab()
        ecomm_page.set_fit_input(FIT_WRONG_URL) 
        ecomm_page.click_create_catalog_inner()
        assert ecomm_page.get_fit_input_http_error()
        
    def test_fit_input_correct_value(self, ecomm_page):
        ecomm_page.click_create_catalog()
        ecomm_page.click_fit_tab()
        ecomm_page.set_fit_input(FIT_RIGHT_URL)
        ecomm_page.click_create_catalog_inner()
        ecomm_page.wait_modal_disappears()
    
    
        
    