class TestPixelPage:

    def test_click_create_pixel(self, pixel_page):
        pixel_page.click_create_button()
        assert pixel_page.find_modal()


