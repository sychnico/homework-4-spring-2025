
class TestAppsPage:

    def test_add_new_app(self, mobile_apps_page):
        mobile_apps_page.click_create_new_app_button()
        field = mobile_apps_page.get_app_input_field()
        mobile_apps_page.fill_input_app_field(field, "https://apps.apple.com/ru/app/microsoft-bing-for-safari/id1560727432?mt=12")
        mobile_apps_page.click_app_button()
        mobile_apps_page.get_modal_element()

    def test_invalid_add_new_app(self, mobile_apps_page):
        mobile_apps_page.click_create_new_app_button()
        field = mobile_apps_page.get_app_input_field()
        mobile_apps_page.fill_input_app_field(field, "invalid.ru")
        mobile_apps_page.click_app_button()
        assert mobile_apps_page.get_error_message()

    def test_read_code(self, mobile_apps_page):
        mobile_apps_page.click_read_code_button()
        assert mobile_apps_page.get_modal_code()