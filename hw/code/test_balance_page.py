WRONG_PAY_VALUE = 100
RIGHT_PAY_VALUE = 1000
WRONG_PROMOCODE = "tralalelo tralala"


class TestBalancePage:
    def go_to_pay(self, balance_page):
        balance_page.click_inc_button()
        return balance_page.find_inc_modal()
    
    def test_open_pay_modal(self, balance_page):
        up_top_modal = self.go_to_pay(balance_page=balance_page)
        assert len(up_top_modal) == 1
    
    def test_close_pay_modal(self, balance_page):
        self.go_to_pay(balance_page=balance_page)
        balance_page.close_modal()
        balance_page.wait_modal_disappears()
        
    def test_null_pay_error(self, balance_page):
        self.go_to_pay(balance_page=balance_page)
        balance_page.click_pay_balance()
        error = balance_page.find_pay_null_error()
        assert error
    
    def test_wrong_pay_error(self, balance_page):
        self.go_to_pay(balance_page=balance_page)
        balance_page.set_amound_input(WRONG_PAY_VALUE)
        balance_page.click_pay_balance()
        error = balance_page.find_pay_wrong_error()
        assert error
        
    def test_successful_pay(self, balance_page):
        self.go_to_pay(balance_page=balance_page)
        balance_page.set_amound_input(RIGHT_PAY_VALUE)
        balance_page.click_pay_balance()
        balance_page.find_text_pay_info()

        
    def test_open_bonus_program(self, balance_page):
        balance_page.open_bonus_tab()
        balance_page.find_text_bonus_info()
        assert balance_page
        
    def go_to_promo(self, balance_page):
        balance_page.open_bonus_tab()
        balance_page.click_activate_promocode()
        return balance_page.find_inc_modal()
        
    def test_open_promo_modal(self, balance_page):
        modal = self.go_to_promo(balance_page=balance_page)
        assert len(modal) == 1
        
    def test_close_promo_modal(self, balance_page):
        self.go_to_promo(balance_page=balance_page)
        balance_page.close_modal()
        balance_page.wait_modal_disappears()
    
    def test_null_promocode_error(self, balance_page):
        self.go_to_promo(balance_page=balance_page)
        balance_page.click_activate()
        balance_page.skip_alert()
        error = balance_page.find_null_promocode_error()
        assert error
        
    def test_wrong_promocode_error(self, balance_page):
        self.go_to_promo(balance_page=balance_page)
        balance_page.set_promocode_input(WRONG_PROMOCODE)
        balance_page.click_activate()
        balance_page.skip_alert()
        error = balance_page.find_wrong_promocode_error()
        assert error
        
        
        
        