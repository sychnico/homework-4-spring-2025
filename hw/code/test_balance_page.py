
class TestBalancePage:

    def test_click_inc_button(self, balance_page):
        balance_page.click_inc_button()
        assert balance_page.find_inc_modal()
        
    def test_click_inc_button2(self, balance_page):
        balance_page.click_inc_button()
        assert balance_page.find_inc_modal()