from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import os
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class TanevVKAdsPage:
    LOCATORS = {
        'root': (By.ID, "root"),
        'search_input': (By.CSS_SELECTOR, "input[placeholder*='Поиск']"),
        'empty_search_title': [
            (By.CSS_SELECTOR, "#pixels h2"),
        ],
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self, url):
        """Открыть страницу и дождаться загрузки"""
        self.driver.get(url)
        try:
            self.wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')
            self.wait.until(EC.presence_of_element_located(self.LOCATORS['root']))
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "button")))
        except TimeoutException:
            pass

    def wait_for_react_render(self):
        """Ожидание полной загрузки React-приложения"""
        try:
            self.wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, ".vkuiPanel, .vkuiRoot, .vkuiView")) > 0)
        except TimeoutException:
            pass

    def search_pixel(self, query):
        input_elem = self.wait.until(EC.presence_of_element_located(self.LOCATORS['search_input']))
        input_elem.clear()
        input_elem.send_keys(query)

    def wait_and_find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def test_open_balance_page(self):
        try:
            self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Платежей пока нет')]")
            ))
            self.wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "#budget\\.transactions > div > div.tableLayout_wrapper__r84CH > div.tableLayout_table__weM5E > div > div > div.vkuiPlaceholder__action > button"
            )))
            return True
        except TimeoutException:
            return False

    def bonus_page(self):
        try:
            # Click the second tab.
            self.wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "#budget > div > div.vkuiTabs.vkuiInternalTabs.vkuiTabs--mode-default.Tabs_tabs__OMzoL > div > div:nth-child(2)"
            ))).click()
            # Wait until the bonus button appears.
            self.wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "#budget\\.bonus > div > section > button"
            )))
            return True
        except TimeoutException:
            return False

    def bonus_inc_balance(self):
        try:
            self.wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "#budget\\.transactions > div > div.tableLayout_wrapper__r84CH > div.tableLayout_table__weM5E > div > div > div.vkuiPlaceholder__action > button"
            ))).click()
            modal = self.wait.until(EC.visibility_of_element_located((
                By.CSS_SELECTOR,
                "#_modal_18 > div > div > div.vkuiModalPage__content-wrap > div.vkuiModalPage__content > div > div > form > section"
            )))
            modal_text = modal.text
            required_texts = [
                "Пополнение баланса",
                "Cумма к оплате",
                "На баланс поступит (НДС — 20%)"
            ]
            for text in required_texts:
                if text not in modal_text:
                    raise TimeoutException(f"Missing text: {text}")
            return True
        except TimeoutException:
            return False

    def close_inc_balance(self):
        try:
            self.wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "#_modal_18 > div > div > div.vkuiModalDismissButton.vkuiTappable.vkuiInternalTappable.vkuiTappable--hasHover.vkuiTappable--hasActive.vkui-focus-visible"
            ))).click()
            self.wait.until_not(EC.visibility_of_element_located((
                By.CSS_SELECTOR,
                "#_modal_18 > div > div > div.vkuiModalPage__content-wrap > div.vkuiModalPage__content > div > div > form > section"
            )))
            return True
        except TimeoutException:
            return False
