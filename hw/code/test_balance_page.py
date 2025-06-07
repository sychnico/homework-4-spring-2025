import pytest
from ui.constants.companies_constants import CampaignConstants

WRONG_PAY_VALUE = ["0", "10,5", "100", "apsdkjsaoi"]
RIGHT_PAY_VALUE = ["1000", "1000,05", "10000", "100000"]
WRONG_PROMOCODE = "tralalelo tralala"
MIN_ERROR_OPLATA = 'Минимальная сумма 600,00 ₽'
NULL_ERROR_OPLATA = 'Нужно заполнить'
PROMO_INFO_OPLATA = 'Персональные акции'
NULL_ERROR_PROMO = 'Укажите промокод'
WRONG_ERROR_PROMO = 'Неверный промокод'

class TestBalancePage:
    def go_to_pay(self, balance_page):
        balance_page.click_inc_button()
        return balance_page.find_inc_modal()
    
    def test_open_pay_modal(self, balance_page):
        up_top_modal = self.go_to_pay(balance_page=balance_page)
        assert len(up_top_modal) == 1
        
    def test_null_pay_error(self, balance_page):
        self.go_to_pay(balance_page=balance_page)
        balance_page.click_pay_balance()
        error = balance_page.find_pay_null_error()
        assert error.text == NULL_ERROR_OPLATA

    @pytest.mark.parametrize("amount,expected_error", [
        ("0", MIN_ERROR_OPLATA),
        ("10,5", MIN_ERROR_OPLATA),
        ("100", MIN_ERROR_OPLATA),
        ("apsdkjsaoi", MIN_ERROR_OPLATA)
    ])
    def test_wrong_pay_error(self, balance_page, amount, expected_error):
        self.go_to_pay(balance_page=balance_page)
        balance_page.set_amound_input(amount)
        balance_page.click_pay_balance()
        error = balance_page.find_pay_wrong_error()
        assert error.text == expected_error

    @pytest.mark.parametrize("amount", RIGHT_PAY_VALUE)
    def test_successful_pay(self, balance_page, amount):
        self.go_to_pay(balance_page=balance_page)
        balance_page.set_amound_input(amount)
        balance_page.click_pay_balance()
        amount_info = balance_page.find_amount_text_info()
        assert amount_info.text == f'{amount} ₽'
 
    def test_open_bonus_program(self, balance_page):
        balance_page.open_bonus_tab()
        bonus_info = balance_page.find_text_bonus_info()
        assert bonus_info.text == PROMO_INFO_OPLATA
        
    def go_to_promo(self, balance_page):
        balance_page.open_bonus_tab()
        balance_page.click_activate_promocode()
        return balance_page.find_inc_modal()
        
    def test_open_promo_modal(self, balance_page):
        modal = self.go_to_promo(balance_page=balance_page)
        assert len(modal) == 1
    
    def test_null_promocode_error(self, balance_page):
        self.go_to_promo(balance_page=balance_page)
        balance_page.click_activate()
        balance_page.skip_alert()
        error = balance_page.find_null_promocode_error()
        assert error.text == NULL_ERROR_PROMO
        
    def test_wrong_promocode_error(self, balance_page):
        self.go_to_promo(balance_page=balance_page)
        balance_page.set_promocode_input(WRONG_PROMOCODE)
        balance_page.click_activate()
        balance_page.skip_alert()
        error = balance_page.find_wrong_promocode_error()
        assert error.text == WRONG_ERROR_PROMO
        
        
        
        