import pytest

class TestAppsPage:

    @pytest.mark.parametrize("app_data", [
        {
            "url": "https://apps.apple.com/ru/app/microsoft-bing-for-safari/id1560727432?mt=12",
            "name": "Microsoft Bing for Safari"
        }
    ])
    def test_add_new_app(self, mobile_apps_page, app_data):
        mobile_apps_page.click_create_new_app_button()
        field = mobile_apps_page.get_app_input_field()
        mobile_apps_page.fill_input_app_field(field, app_data["url"])
        mobile_apps_page.click_app_button()
        mobile_apps_page.get_modal_element()
        app_link = mobile_apps_page.find_app_link(app_data["name"])
        assert app_link.text == app_data["name"]

    @pytest.mark.parametrize("invalid_app_data", [
        {
            "url": "invalid.ru"
        }
    ])
    def test_invalid_add_new_app(self, mobile_apps_page, invalid_app_data):
        mobile_apps_page.click_create_new_app_button()
        field = mobile_apps_page.get_app_input_field()
        mobile_apps_page.fill_input_app_field(field, invalid_app_data["url"])
        mobile_apps_page.click_app_button()
        error = mobile_apps_page.get_error_message()
        assert error.text == "Введите корректную ссылку на приложение"

