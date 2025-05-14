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
            # Нажать кнопку
            self.wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "#budget\\.transactions > div > div.tableLayout_wrapper__r84CH > div.tableLayout_table__weM5E > div > div > div.vkuiPlaceholder__action > button"
            ))).click()
            # Ждать появления модального окна и получить его текст
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

    def open_comm_page_and_start_education(self):
        try:
            # Попытка закрыть мешающую модалку, если она появилась
            try:
                from selenium.webdriver.support.wait import WebDriverWait
                WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((
                    By.CSS_SELECTOR,
                    " #_modal_36 > div > div > div.vkuiModalDismissButton.vkuiTappable.vkuiInternalTappable.vkuiTappable--hasHover.vkuiTappable--hasActive.vkui-focus-visible"  # предполагаемый селектор для мешающей модалки
                ))).click()
            except TimeoutException:
                pass
            # Нажимаем на кнопку открытия обучения
            self.wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "#catalogs > div > div > section > div > div > div.CatalogsPlaceholder_placeHolderWrapper__\+Ycn8 > div > div.vkuiButtonGroup.vkuiButtonGroup--mode-horizontal.vkuiButtonGroup--gap-m.vkuiButtonGroup--align-left > button.vkuiButton.vkuiButton--size-l.vkuiButton--mode-secondary.vkuiButton--appearance-accent.vkuiButton--align-center.vkuiButton--sizeY-regular.vkuiButton--with-icon.vkuiTappable.vkuiInternalTappable.vkuiTappable--sizeX-none.vkuiTappable--hasHover.vkuiTappable--hasActive.vkui-focus-visible"
            ))).click()
            # Ждем появления модального окна обучения
            modal = self.wait.until(EC.visibility_of_element_located((
                By.ID, "_modal_30"
            )))
            # Проверяем наличие требуемых текстов
            modal_text = modal.text
            required_texts = [
                "Создать каталог с подсказками",
                "Пошаговое обучение, ~15 минут",
                "Смотреть видеоурок от экспертов VK",
                "Видео, 7 минут",
                "Смотреть курс на обучающей платформе",
                "Полезные видео и статьи"
            ]
            for text in required_texts:
                if text not in modal_text:
                    raise TimeoutException(f"Missing text: {text}")
            # Закрываем модальное окно по крестику
            self.wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "#_modal_86 > div > div > div.vkuiModalDismissButton.vkuiTappable.vkuiInternalTappable.vkuiTappable--hasHover.vkuiTappable--hasActive.vkui-focus-visible"
            ))).click()
            # Ждем, что окно с обучением исчезло
            self.wait.until_not(EC.visibility_of_element_located((
                By.ID, "_modal_30"
            )))
            return True
        except TimeoutException:
            return False

    def create_catalog(self):
        try:
            # Click the create catalog button
            self.wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "#catalogs > div > div > section > div > div > div.CatalogsPlaceholder_placeHolderWrapper__\\+Ycn8 > div > div.vkuiButtonGroup.vkuiButtonGroup--mode-horizontal.vkuiButtonGroup--gap-m.vkuiButtonGroup--align-left > button"
            ))).click()
            # Wait for the input field in the modal to appear
            self.wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR,
                "#root > div > div:nth-child(3) > div > div.ModalRoot_componentWrapper__uzHTL > form > div.ModalSidebarPage_contentWithoutHeader__cVnVe > div > div.ModalSidebarPage_content__2mBu8 > section > div:nth-child(1) > span > input"
            )))
            # Verify three sections exist in the modal
            sections = self.driver.find_elements(
                By.CSS_SELECTOR,
                "#root > div > div:nth-child(3) > div > div.ModalRoot_componentWrapper__uzHTL > form > div.ModalSidebarPage_contentWithoutHeader__cVnVe > div > div.ModalSidebarPage_content__2mBu8 > section > div:nth-child(2) > div"
            )
            if len(sections) < 3:
                raise TimeoutException("Less than 3 sections found")
            return True
        except TimeoutException:
            return False


