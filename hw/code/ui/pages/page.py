from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
import time
import random
import string
from selenium.webdriver.common.by import By
import re

class Page(object):
    URL = 'https://ads.vk.com/'

    def __init__(self, driver):
        self.driver = driver
        self.is_open()

    def is_open(self, timeout=5):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.URL:
                return True
        raise TimeoutException

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(expected_conditions.presence_of_element_located(locator))
    
    
    
    def find_multiple(self, locator, timeout=None):
        try:
            return self.wait(timeout).until(
                expected_conditions.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            return []  
    
    def became_invisible(self, locator, timeout=None):
        try:
            self.wait(timeout).until(expected_conditions.invisibility_of_element(locator))
            return True
        except TimeoutException:
            return False

    def became_visible(self, locator, timeout=None):
        try:
            self.wait(timeout).until(expected_conditions.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 10
        return WebDriverWait(self.driver, timeout=timeout)

    def click(self, locator, timeout=None):
        el = self.wait(timeout).until(expected_conditions.element_to_be_clickable(locator))
        el.click()
        return el

    def scroll_and_click(self, locator, timeout=None):
        el = self.wait(timeout).until(expected_conditions.presence_of_element_located(locator))
        ActionChains(self.driver).move_to_element(el).click(el).perform()
        return el
    
    def hover(self, locator, timeout=None):
        el = self.wait(timeout).until(expected_conditions.presence_of_element_located(locator))
        ActionChains(self.driver).move_to_element(el).perform()

    def go_to_new_tab(self):
        handles = self.driver.window_handles
        assert len(handles) > 1
        self.driver.switch_to.window(handles[1])

    def is_redirected_to_pattern(self, url_pattern, timeout=10):
        try:
            self.wait(timeout).until(
                lambda driver: re.fullmatch(url_pattern, driver.current_url)
            )
            return True
        except TimeoutException:
            return False

   

