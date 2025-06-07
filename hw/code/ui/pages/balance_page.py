from .page import Page
from ui.locators.balance_locators import BalanceLocators

class BalancePage(Page):
    URL = "https://ads.vk.com/hq/budget/transactions" # Урл страницы
    locators = BalanceLocators()
    
    def find_amount_text_info(self):
        return self.find(self.locators.AMOUNT_TEXT_INFO, timeout=5)

    def click_inc_button(self):
        self.click(self.locators.INC_BALANCE_BUTTON)
           
    def find_inc_modal(self):
        return self.find_multiple(self.locators.INC_MODAL, 2)
    
    def click_pay_balance(self):
        self.click(self.locators.TOP_UP_BALANCE_BUTTON)
        
    def find_pay_null_error(self):
        return self.find(self.locators.ERROR_PAY_NULL_VALUE)
    
    def find_pay_wrong_error(self):
        return self.find(self.locators.ERROR_PAY_WRONG_VALUE)
    
    def set_amound_input(self, price):
        amound_input = self.find(self.locators.AMOUNT_INPUT)
        amound_input.send_keys(price)
    
    def close_modal(self):
        self.click(self.locators.MODAL_CLOSE_BUTTON, 2)
    
    def is_modal_present(self):
        return bool(self.driver.find_elements(*self.locators.INC_MODAL))
    
    def open_bonus_tab(self):
        self.click(self.locators.BONUS_PROGRAM_TAB)
        
    def click_activate_promocode(self):
        self.click(self.locators.ACTIVATE_PROMOCODE)
    
    def click_activate(self):
        self.click(self.locators.ACTVATE)
    
    def skip_alert(self):
        self.click(self.locators.SKIP_ALERT)
        
    def find_null_promocode_error(self):
        return self.find(self.locators.ERROR_NULL_PROMOCODE)
    
    def set_promocode_input(self, price):
        promocode_input = self.find(self.locators.PROMOCODE_INPUT)
        promocode_input.send_keys(price)
        
        
    def wait_modal_disappears(self, timeout=5):
        self.became_invisible(self.locators.INC_MODAL, timeout=timeout)
        
    def find_wrong_promocode_error(self):
        return self.find(self.locators.ERROR_WRONG_PROMOCODE)
    
    def find_text_pay_info(self, timeout=5):
        return self.became_visible(self.locators.OPLATA_TEXT_INFO, timeout=timeout)
    
    def find_text_bonus_info(self):
        return self.find(self.locators.BONUS_TAB_TEXT_INFO, timeout=15)
        
  