from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import os
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class VKAdsPage:
    LOCATORS = {
        'root': (By.ID, "root"),
        'search_input': (By.CSS_SELECTOR, "input[placeholder*='Поиск']"),
        'empty_search_title': [
            (By.CSS_SELECTOR, "#pixels h2"),
        ],
    }

    def init(self, driver):
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

    def get_empty_search_message(self):
        """Получить сообщение о пустом результате поиска"""
        try:
            title = WebDriverWait(self.driver, 5).until(
                lambda d: d.find_element(By.CSS_SELECTOR, "#pixels h2")
            )
            parent = title.find_element(By.XPATH, "..")
            divs = parent.find_elements(By.TAG_NAME, "div")
            subtitle_text = None
            for d in divs:
                if d.is_displayed() and "Попробуйте изменить или удалить фильтры" in d.text:
                    subtitle_text = d.text
            return {
                'title': title.text if title else None,
                'subtitle': subtitle_text
            }
        except Exception:
            return None

    def wait_for_search_results(self):
        """Ожидание обновления результатов поиска"""
        try:
            results = self.driver.find_elements(By.CSS_SELECTOR, "#pixels > div > div.tableLayout_wrapper__r84CH > div > div > div > div.BaseTable.table_table__2JcCk.table_withoutFooter__3B3E3.table_hideScrollbars__9gFIg > div.BaseTable__table.BaseTable__table-main > div.BaseTable__body > div > div")
            if len(results) > 0:
                return True

            for locator in self.LOCATORS['empty_search_title']:
                try:
                    if self.driver.find_element(*locator).is_displayed():
                        return True
                except:
                    continue
            return False
        except:
            return False