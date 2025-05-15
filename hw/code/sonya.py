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

    def test_open_empty_auditory_page(self):
        try:
            self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Аудиторий пока нет')]")
            ))
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[data-testid='create-audience']")))
            return True
        except TimeoutException:
            return False

    def test_create_audience_modal(self):
        try:
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[data-testid='create-audience']"))).click()
            self.wait.until(EC.visibility_of_element_located((
                By.XPATH, "//*[@id=\"root\"]/div/div[2]/div"
            )))
            return True

        except TimeoutException:
            return False

    def test_add_source(self):
        try:
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[data-testid='create-audience']"))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#root > div > div:nth-child(2) > div > div.ModalRoot_componentWrapper__uzHTL > form > div.ModalSidebarPage_contentWithoutHeader__cVnVe > div > div.ModalSidebarPage_content__2mBu8 > div > section.vkuiInternalGroup.vkuiGroup.vkuiGroup--mode-plain.vkuiInternalGroup--mode-plain.vkuiGroup--padding-m.CreateSegmentModal_groupContent__FpH1D > div > div > button:nth-child(1)"))).click()
            self.wait.until(EC.visibility_of_element_located((
                By.XPATH, "//*[@id=\"root\"]/div/div[2]/div[2]"
            )))
            self.wait.until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, "#root > div > div:nth-child(2) > div:nth-child(2) > div.ModalRoot_componentWrapper__uzHTL > div > div.ModalSidebarPage_contentWithoutHeader__cVnVe > div > div.ModalSidebarPage_content__2mBu8 > section > div:nth-child(2)"
            )))

            ##self.wait.until(EC.visibility_of_element_located((
            ##    By.XPATH, "//*[@id=\"root\"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/section/div/div"
            ##)))
            return True
        except TimeoutException:
            return False
    def test_user_lists(self):
        try:
            self.wait.until(EC.element_to_be_clickable(
                (By.ID, "tab_audience.users_list"))).click()
            self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Списков пользователей пока нет')]")
            ))
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[data-testid='download-list']")))
            return True
        except TimeoutException:
            return False
    def test_offline_conversion(self):
        try:
            self.wait.until(EC.element_to_be_clickable(
                (By.ID, "tab_audience.offline_conversion"))).click()
            self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Списков офлайн-конверсий пока нет')]")
            ))
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[data-testid='download-list']")))
            return True
        except TimeoutException:
            return False

    def test_modal_lists(self):
        try:
            self.wait.until(EC.element_to_be_clickable(
                (By.ID, "tab_audience.users_list"))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[data-testid='download-list']"))).click()
            self.wait.until(EC.visibility_of_element_located((
                By.XPATH, "//*[@id=\"root\"]/div/div[2]/div"
            )))
            return True
        except TimeoutException:
            return False

    def test_modal_offline(self):
        try:
            self.wait.until(EC.element_to_be_clickable(
                (By.ID, "tab_audience.offline_conversion"))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[data-testid='download-list']"))).click()
            self.wait.until(EC.visibility_of_element_located((
                By.XPATH, "//*[@id=\"root\"]/div/div[2]/div"
            )))
            return True
        except TimeoutException:
            return False
    def test_overview(self):
        try:
            self.wait.until(EC.element_to_be_clickable((
                By.XPATH, "//*[@id=\"overview\"]/section/div[1]/div[2]/div[1]/button"
            )))
            return True
        except TimeoutException:
            return False

