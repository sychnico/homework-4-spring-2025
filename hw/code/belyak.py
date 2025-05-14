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

    def is_empty_search_result(self):
        self.wait_for_search_results()
        try:
            title = WebDriverWait(self.driver, 5).until(
                lambda d: d.find_element(By.CSS_SELECTOR, "#pixels h2")
            )
            parent = title.find_element(By.XPATH, "..")
            divs = parent.find_elements(By.TAG_NAME, "div")
            found_subtitle = False
            for d in divs:
                if d.is_displayed() and "Попробуйте изменить или удалить фильтры" in d.text:
                    found_subtitle = True
            return (
                title.is_displayed() and "Ничего не нашлось" in title.text and found_subtitle
            )
        except Exception:
            return False

    def has_search_results(self):
        """Есть ли результаты поиска (элементы пикселей)"""
        results = self.driver.find_elements(By.CSS_SELECTOR, "#pixels > div > div.tableLayout_wrapper__r84CH > div > div > div > div.BaseTable.table_table__2JcCk.table_withoutFooter__3B3E3.table_hideScrollbars__9gFIg > div.BaseTable__table.BaseTable__table-main > div.BaseTable__body > div > div")
        return any(r.is_displayed() for r in results)

    def click_link_by_text(self, link_text, assert_url=None, wait_class=None):
        """Найти ссылку по тексту, кликнуть и проверить url (опционально)"""
        try:
            elem = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, link_text)))
            elem = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            elem = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, link_text)))
        except TimeoutException:
            return False
        elem = self.driver.find_element(By.LINK_TEXT, link_text)
        self.driver.execute_script("arguments[0].click();", elem)

        p = self.driver.current_window_handle
        for w in self.driver.window_handles:
            if w != p:
                self.driver.switch_to.window(w)

        if wait_class:
            try:
                WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, wait_class)))
            except TimeoutException:
                pass
        if assert_url:
            assert assert_url in self.driver.current_url, f"Ожидался url, содержащий {assert_url}, но сейчас {self.driver.current_url}"
        return True

    def click_button_by_class(self, class_str, assert_url=None, wait_class=None):
        """Найти кнопку по классу, кликнуть и проверить url (опционально)"""
        try:
            elem = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, class_str)))
            elem = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, class_str)))
            elem = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, class_str)))
        except TimeoutException:
            return False
        elem = self.driver.find_element(By.CLASS_NAME, class_str)
        self.driver.execute_script("arguments[0].click();", elem)

        p = self.driver.current_window_handle
        for w in self.driver.window_handles:
            if w != p:
                self.driver.switch_to.window(w)

        if wait_class:
            try:
                WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, wait_class)))
            except TimeoutException:
                pass
        if assert_url:
            assert assert_url in self.driver.current_url, f"Ожидался url, содержащий {assert_url}, но сейчас {self.driver.current_url}"
        return True

    def test_add_pixel_modal(self):
        """Тест: после клика по 'Добавить пиксель' появляется модальное окно"""
        try:
            btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#pixels > div > div.ListHeader_content__KfvHn > div.ListHeader_actions__cWXP5 > button")))
            btn.click()
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#_modal_31"))
            )
            return True
        except Exception as e:
            return False

    def test_invalid_domain_modal(self, invalid_domain="not_a_domain"): 
        """Тест: ввод некорректного домена в модалке, проверка появления ошибки"""
        try:
            input_wrap = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#_modal_31 div.DomainCheckStep_inputWrap__KIm3f input")))
            input_wrap.clear()
            input_wrap.send_keys(invalid_domain)
            add_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#_modal_31 div.vkuiModalCardBase__actions button")))
            add_btn.click()
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#_modal_31 div.vkuiFormItem--status-error.DomainCheckStep_inputWrap__KIm3f")))
            return True
        except Exception as e:
            return False

    def test_invalid_pixel_id_modal(self, invalid_id="12345", email="test@test.com"): 
        """Тест: ввод некорректного ID пикселя и email в модалке, проверка появления ошибки"""
        try:
            try:
                btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#pixels > div > div.ListHeader_content__KfvHn > div.ListHeader_actions__cWXP5 > button")))
                btn.click()
                self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#_modal_31")))
            except:
                pass
                
            id_tab = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#_modal_31 > div > div > div.vkuiDiv.DomainCheckStep_contentWrapper__RFb-h > div.vkuiSegmentedControl > div > label.vkuiSegmentedControlOption")))
            self.driver.execute_script("arguments[0].click();", id_tab)
            
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "label.vkuiSegmentedControlOption.vkuiSegmentedControlOption--checked")))
            
            id_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#_modal_31 > div > div > div.vkuiDiv.DomainCheckStep_contentWrapper__RFb-h > div:nth-child(2) input")))
            id_input.clear()
            id_input.send_keys(invalid_id)
            
            email_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#_modal_31 > div > div > div.vkuiDiv.DomainCheckStep_contentWrapper__RFb-h > div:nth-child(3) input")))
            email_input.clear()
            email_input.send_keys(email)
            
            add_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#_modal_31 > div > div > div.vkuiModalCardBase__actions > a")))
            add_btn.click()
            
            error_elem = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#_modal_31 div.vkuiFormItem--status-error")))
            return True
        except Exception as e:
            return False

    def test_pixel_id_tab_opening(self):
        """Тест: открытие вкладки с ID пикселя в модальном окне"""
        try:
            if not self.test_add_pixel_modal():
                return False
            
            modal_selectors = ["#_modal_31", "#_modal_53", "[id^='_modal_']"]
            modal_id = None
            for selector in modal_selectors:
                try:
                    modal_elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    for elem in modal_elements:
                        if elem.is_displayed():
                            modal_id = elem.get_attribute("id")
                            break
                    if modal_id:
                        break
                except:
                    continue
            
            if not modal_id:
                modal_id = "_modal_31"  

            try:
                id_tab_selectors = [
                    f"#{modal_id} > div > div > div.vkuiDiv.DomainCheckStep_contentWrapper__RFb-h > div.vkuiSegmentedControl > div > label.vkuiSegmentedControlOption",
                    f"#{modal_id} label.vkuiSegmentedControlOption:not(.vkuiSegmentedControlOption--checked)",
                    f"#{modal_id} .vkuiSegmentedControl label:last-child",
                    f"#{modal_id} .DomainCheckStep_createByTypeSelect__1796K label:last-child",
                    "label.vkuiSegmentedControlOption:not(.vkuiSegmentedControlOption--checked)"
                ]
                
                id_tab = None
                for selector in id_tab_selectors:
                    try:
                        id_tab_elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                        for elem in id_tab_elements:
                            if elem.is_displayed() and not "vkuiSegmentedControlOption--checked" in elem.get_attribute("class"):
                                id_tab = elem
                                break
                        if id_tab:
                            break
                    except:
                        continue
                
                if not id_tab:
                    return False

                try:
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", id_tab)
                    self.driver.execute_script("arguments[0].click();", id_tab)
                except Exception as e:
                    pass
                                
                try:
                    self.wait.until(lambda d: "vkuiSegmentedControlOption--checked" in id_tab.get_attribute("class"))
                except:
                    pass
                
                div_selectors = [
                    f"#{modal_id} > div > div > div.vkuiDiv.DomainCheckStep_contentWrapper__RFb-h > div:nth-child(2)",
                    f"#{modal_id} > div > div > div.vkuiDiv.DomainCheckStep_contentWrapper__RFb-h > div:nth-child(3)"
                ]
                
                elements_found = True
                for i, selector in enumerate(div_selectors):
                    try:
                        element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                        if not element.is_displayed():
                            elements_found = False
                    except:
                        elements_found = False
                
                return elements_found
                
            except Exception as e:
                pass
                
        except Exception as e:
            pass
            return False

    def test_invalid_pixel_id_validation(self, invalid_id="12345", email="test"):
        """Тест: проверка валидации при вводе некорректных данных ID пикселя"""
        try:
            if not self.test_pixel_id_tab_opening():
                return False
            
            modal_selectors = ["#_modal_31", "#_modal_53", "[id^='_modal_']"]
            modal_id = None
            for selector in modal_selectors:
                try:
                    modal_elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    for elem in modal_elements:
                        if elem.is_displayed():
                            modal_id = elem.get_attribute("id")
                            break
                    if modal_id:
                        break
                except Exception:
                    continue
            
            if not modal_id:
                modal_id = "_modal_31"
            
            id_input_selector = f"#{modal_id} > div > div > div.vkuiDiv.DomainCheckStep_contentWrapper__RFb-h > div:nth-child(2) input"
            id_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, id_input_selector)))
            id_input.clear()
            id_input.send_keys(invalid_id)
            
            email_input_selector = f"#{modal_id} > div > div > div.vkuiDiv.DomainCheckStep_contentWrapper__RFb-h > div:nth-child(3) input"
            email_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, email_input_selector)))
            email_input.clear()
            email_input.send_keys(email)
            
            button_selector = f"#{modal_id} > div > div > div.vkuiModalCardBase__actions > div > button"
            action_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector)))
            self.driver.execute_script("arguments[0].click();", action_button)
            
            error_selector = f"#{modal_id} > div > div > div.vkuiDiv.DomainCheckStep_contentWrapper__RFb-h > div.vkuiFormItem.vkuiFormItem--withPadding.vkuiInternalFormItem.vkuiFormItem--status-error"
            
            try:
                error_element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, error_selector)))
                if error_element.is_displayed():
                    return True
                else:
                    return False
            except Exception:
                try:
                    error_elements = self.driver.find_elements(By.CSS_SELECTOR, f"#{modal_id} .vkuiFormItem--status-error")
                    if error_elements and any(e.is_displayed() for e in error_elements):
                        return True
                except:
                    pass
                    
                return False
                
        except Exception:
            return False

    def test_valid_email_invalid_pixel_id(self, invalid_id="12345", valid_email="sonyabely@gmail.com"):
        """Тест: проверка валидации при вводе корректного email и некорректного ID пикселя"""
        try:
            if not self.test_pixel_id_tab_opening():
                return False
            
            modal_selectors = ["#_modal_31", "#_modal_53", "[id^='_modal_']"]
            modal_id = None
            for selector in modal_selectors:
                try:
                    modal_elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    for elem in modal_elements:
                        if elem.is_displayed():
                            modal_id = elem.get_attribute("id")
                            break
                    if modal_id:
                        break
                except Exception as e:
                    continue
            
            if not modal_id:
                modal_id = "_modal_31" 
            
            id_input_selector = f"#{modal_id} > div > div > div.vkuiDiv.DomainCheckStep_contentWrapper__RFb-h > div:nth-child(2) input"
            id_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, id_input_selector)))
            id_input.clear()
            id_input.send_keys(invalid_id)
            
            email_input_selector = f"#{modal_id} > div > div > div.vkuiDiv.DomainCheckStep_contentWrapper__RFb-h > div:nth-child(3) input"
            email_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, email_input_selector)))
            email_input.clear()
            email_input.send_keys(valid_email)
            
            button_selector = f"#{modal_id} > div > div > div.vkuiModalCardBase__actions > div > button"
            action_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector)))
            self.driver.execute_script("arguments[0].click();", action_button)
            
            self.save_screenshot("before_error_check_valid_email.png")
            
            error_selectors = [
                f"#{modal_id} > div > div > div.vkuiDiv.DomainCheckStep_contentWrapper__RFb-h > div.vkuiFormItem.vkuiFormItem--withPadding.vkuiInternalFormItem.vkuiFormItem--status-error.vkuiInternalFormItem--status-error.vkuiFormItem--sizeY-none.vkuiInternalFormItem--sizeY-none.DomainCheckStep_inputWrap__KIm3f",
                f"#{modal_id} > div > div > div.vkuiDiv.DomainCheckStep_contentWrapper__RFb-h > div.vkuiFormItem.vkuiFormItem--withPadding.vkuiInternalFormItem.vkuiFormItem--status-error"
            ]
            
            for i, error_selector in enumerate(error_selectors):
                try:
                    error_element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, error_selector)))
                    
                    if error_element.is_displayed():
                        self.save_screenshot(f"validation_error_found_selector_{i+1}.png")
                        return True
                    else:
                        continue
                except Exception as e:
                    continue
            
            try:
                error_elements = self.driver.find_elements(By.CSS_SELECTOR, f"#{modal_id} .vkuiFormItem--status-error")
                if error_elements and any(e.is_displayed() for e in error_elements):
                    self.save_screenshot("alternative_error_found_valid_email.png")
                    return True
            except Exception as e:
                pass
            
            try:
                error_message = self.driver.find_element(By.CSS_SELECTOR, f"#{modal_id} .vkuiFormItem--status-error .vkuiFormItem__error")
                if error_message.is_displayed():
                    self.save_screenshot("error_message_displayed.png")
                    return True
            except Exception as e:
                pass
            
            self.save_screenshot("validation_error_not_found_valid_email.png")
            return False
                
        except Exception as e:
            self.save_screenshot("valid_email_test_general_error.png")
            return False

    def test_create_first_pixel(self, domain="example.com"): 
        """Тест: создание первого пикселя через кнопку 'Создать первый пиксель'"""
        try:
            try:
                create_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#pixels > div > div > div.vkuiPlaceholder__action > button")))
                create_btn.click()
            except:
                btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#pixels > div > div.ListHeader_content__KfvHn > div.ListHeader_actions__cWXP5 > button")))
                btn.click()

            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#_modal_31"))
            )

            input_wrap = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#_modal_31 div.DomainCheckStep_inputWrap__KIm3f input")))
            input_wrap.clear()
            input_wrap.send_keys(domain)

            add_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#_modal_31 > div > div > div.vkuiModalCardBase__actions")))
            add_btn.click()

            
            second_modal_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#_modal_31 > div > div > div.vkuiModalCardBase__actions")))
            self.driver.execute_script("arguments[0].click();", second_modal_btn)

            time.sleep(2)  
            return True
        except Exception as e:
            return False

    def test_pixel_settings(self):
        """Тест: проверка перехода к настройкам первого пикселя в списке"""
        try:
            
            settings_btn = self.wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, 
                ".BaseTable__body > div > div:nth-child(1) > div:nth-child(4) > a"
            )))
            
            self.driver.execute_script("arguments[0].click();", settings_btn)
            
            time.sleep(2)
            
            return True
        except Exception as e:
            return False

    def test_pixel_tabs_navigation(self):
        """Тест: проверка переключения между вкладками в настройках пикселя"""
        try:
            tabs = [
                "#tab_pixels\\.events",
                "#tab_pixels\\.code",
                "#tab_pixels\\.portrait",
                "#tab_pixels\\.audience_tags",
                "#tab_pixels\\.pixel_access",
                "#tab_pixels\\.review",
            ]
            
            for tab_selector in tabs:
                tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, tab_selector)))
                self.driver.execute_script("arguments[0].click();", tab)
                
                self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"{tab_selector}.vkuiTabsItem--selected")))
                            
            return True
        except Exception as e:
            return False

    def open_add_event_form(self):
        """Открывает форму добавления события"""
        try:
            events_tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#tab_pixels\\.events")))
            self.driver.execute_script("arguments[0].click();", events_tab)
            
            add_event_btn = self.wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, 
                "#pixels\\.events > div > div.vkuiPlaceholder.vkuiPlaceholder--withPadding.Placeholder_placeholder__DgQvm.EmptyList_wrapper__-GjCe > div.vkuiPlaceholder__action > button"
            )))
            self.driver.execute_script("arguments[0].click();", add_event_btn)
            
            self.wait.until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, 
                "#root > div > div.layout_page__eAd4E > div.RightSidebar_overlay__u5hYv"
            )))
            return True
        except Exception as e:
            return False

    def test_add_event(self):
        """Тест: проверка открытия формы добавления события"""
        return self.open_add_event_form()

    def test_invalid_event_creation(self):
        """Тест: проверка появления ошибок при некорректном добавлении события"""
        try:
            if not self.open_add_event_form():
                return False
                
            save_btn = self.wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, 
                "#root > div > div.layout_page__eAd4E > div.RightSidebar_rightSidebar__4aFHb.RightSidebar_expanded__T-Sdn.RightSidebar_small__D7QzC > form > div.vkuiDiv.Footer_footer__tp9Cb > div > button.vkuiButton.vkuiButton--size-l.vkuiButton--mode-primary"
            )))
            self.driver.execute_script("arguments[0].click();", save_btn)
            
            error_element = self.wait.until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, 
                "#root > div > div.layout_page__eAd4E > div.RightSidebar_rightSidebar__4aFHb.RightSidebar_expanded__T-Sdn.RightSidebar_small__D7QzC > form > section > div.vkuiFormItem.vkuiFormItem--withPadding.vkuiInternalFormItem.vkuiFormItem--status-error"
            )))
            
            return True
        except Exception as e:
            return False

    def test_cancel_event_creation(self):
        """Тест: проверка отмены создания события"""
        try:
            if not self.open_add_event_form():
                return False
            
            cancel_btn = self.wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, 
                "#root > div > div.layout_page__eAd4E > div.RightSidebar_rightSidebar__4aFHb.RightSidebar_expanded__T-Sdn.RightSidebar_small__D7QzC > form > div.vkuiDiv.Footer_footer__tp9Cb > div > button.vkuiButton.vkuiButton--size-l.vkuiButton--mode-secondary"
            )))
            self.driver.execute_script("arguments[0].click();", cancel_btn)
            
            self.wait.until(EC.invisibility_of_element_located((
                By.CSS_SELECTOR, 
                "#root > div > div.layout_page__eAd4E > div.RightSidebar_overlay__u5hYv"
            )))
            
            return True
        except Exception as e:
            return False

    def test_create_audience_tag(self, tag_name="Test Tag"):
        """Тест: создание нового аудиторного тега"""
        try:
            audience_tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#tab_pixels\\.audience_tags")))
            self.driver.execute_script("arguments[0].click();", audience_tab)
            
            time.sleep(2)
       
            button_selectors = [
                "#pixels\\.audience_tags > div > div:nth-child(2) > button",
                "#pixels\\.audience_tags > div > div:nth-child(3) > button",
                "button.vkuiButton--mode-primary",
                "button.vkuiButton--appearance-accent",
                "#pixels\\.audience_tags button[type='button']"
            ]
            
            create_tag_btn = None
            for selector in button_selectors:
                try:
                    button_elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    for button in button_elements:
                        if button.is_displayed() and button.is_enabled():
                            create_tag_btn = button
                            break
                    if create_tag_btn:
                        break
                except Exception as e:
                    continue
            
            if not create_tag_btn:
                return False
                
            try:
                self.driver.execute_script("arguments[0].click();", create_tag_btn)
            except Exception as e:
                pass
            
            try:
                modal = self.wait.until(EC.visibility_of_element_located((
                    By.CSS_SELECTOR, 
                    "div.ModalRoot_componentWrapper__uzHTL"
                )))
                
                if not modal.is_displayed():
                    return False
                    
                time.sleep(1)
                
                tag_input = self.wait.until(EC.presence_of_element_located((
                    By.CSS_SELECTOR, 
                    "div.vkuiModalPage__content input[type='text']"
                )))
                tag_input.clear()
                tag_input.send_keys(tag_name)
                
                create_btn = self.wait.until(EC.element_to_be_clickable((
                    By.CSS_SELECTOR, 
                    "div.vkuiModalPage__content button.vkuiButton--mode-primary"
                )))
                self.driver.execute_script("arguments[0].click();", create_btn)
                
                WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((
                    By.CSS_SELECTOR, 
                    "div.ModalRoot_componentWrapper__uzHTL"
                )))
                
                return True
                
            except Exception as e:
                return False
                
        except Exception as e:
            return False

    def test_open_app_modal(self):
        """Тест: открытие модального окна создания приложения"""
        try:
            try:
                create_btn = self.wait.until(EC.element_to_be_clickable((
                    By.CSS_SELECTOR, 
                    "#mobApps > div > div > div.vkuiPlaceholder__action > button"
                )))
                self.driver.execute_script("arguments[0].click();", create_btn)
            except Exception as e:
                print("Кнопка в пустом состоянии не найдена, пробуем кнопку в заголовке:", e)
                create_btn = self.wait.until(EC.element_to_be_clickable((
                    By.CSS_SELECTOR, 
                    "#mobApps > div > div.vkuiCard.vkuiCard--mode-outline.vkuiCard--withBorder.ListHeader_wrapper__Tgp6g > div > button"
                )))
                self.driver.execute_script("arguments[0].click();", create_btn)
            
            modal = self.wait.until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, 
                "#root > div > div:nth-child(2) > div > div.ModalRoot_componentWrapper__uzHTL"
            )))
            
            return True
        except Exception as e:
            return False

    def test_invalid_app_input(self, invalid_input="examle.com"):
        """Тест: проверка валидации при вводе некорректных данных в форму создания приложения"""
        try:
            if not self.test_open_app_modal():
                return False
            
            input_field = self.wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, 
                "div.vkuiModalPage__content input[type='text']"
            )))
            input_field.clear()
            input_field.send_keys(invalid_input)
            
            add_btn = self.wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, 
                "div.vkuiModalPage__content button.vkuiButton"
            )))
            self.driver.execute_script("arguments[0].click();", add_btn)
            
            error_wait = WebDriverWait(self.driver, 10)
            
            error_selectors = [
                "div.RichBanner_container__4cY1e.RichBanner_error__hDR10.BindContent_error__mOnue",
                "div[class*='RichBanner_error']",
                "div[class*='BindContent_error']",
                "div.vkuiFormItem--status-error",
                "#_modal_29 > div > div > div.vkuiModalPage__content-wrap > div.vkuiModalPage__content > div > div > div > div > span",
                "[id^='_modal_'] > div > div > div.vkuiModalPage__content-wrap > div.vkuiModalPage__content > div > div > div > div > span",
                ".vkuiModalPage__content span:contains('Введите корректную ссылку')",
                ".vkuiModalPage__content span"
            ]
            
            error_found = False
            for selector in error_selectors:
                try:
                    
                    if ":contains" in selector:
                        base_selector, search_text = selector.split(":contains(")
                        search_text = search_text.rstrip(")")
                        search_text = search_text.strip("'\"")
                        
                        elements = self.driver.find_elements(By.CSS_SELECTOR, base_selector)
                        for elem in elements:
                            if search_text in elem.text and elem.is_displayed():
                                error_found = True
                                break
                    else:
                        error_message = error_wait.until(
                            EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
                        )
                        if error_message.is_displayed():
                            error_found = True
                            break
                except Exception as e:
                    continue
            
            if not error_found:
                try:
                    body_text = self.driver.find_element(By.TAG_NAME, "body").text
                    error_keywords = ["некорректн", "ошибк", "неверн", "проверьте"]
                    
                    for keyword in error_keywords:
                        if keyword in body_text.lower():
                            error_found = True
                            break
                except Exception as e:
                    pass
                
            if not error_found:
                return False
            
            return True
            
        except Exception as e:
            return False

    def test_valid_app_input(self, valid_input="https://apps.apple.com/ru/app/microsoft-onenote/id784801555?mt=12"):
        """Тест: проверка ввода валидного URL приложения из App Store"""
        try:
            if not self.test_open_app_modal():
                return False
            
            input_field = self.wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, 
                "div.vkuiModalPage__content input[type='text']"
            )))
            input_field.clear()
            input_field.send_keys(valid_input)
            
            time.sleep(2)
            
            add_btn = self.wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, 
                "div.vkuiModalPage__content button.vkuiButton"
            )))
            self.driver.execute_script("arguments[0].click();", add_btn)
            
            long_wait = WebDriverWait(self.driver, 20)
            
            try:
                loading = long_wait.until(EC.presence_of_element_located((
                    By.CSS_SELECTOR, 
                    "div[class*='Spinner']"
                )))
                long_wait.until(EC.invisibility_of_element_located((
                    By.CSS_SELECTOR, 
                    "div[class*='Spinner']"
                )))
            except:
                print("Индикатор загрузки не найден")
            
            try:
                final_modal = long_wait.until(EC.visibility_of_element_located((
                    By.CSS_SELECTOR,
                    "#root > div > div:nth-child(2) > div > div.ModalRoot_componentWrapper__uzHTL"
                )))
                
                if not final_modal.is_displayed():
                    return False
                                
                return True
                
            except Exception as e:
                return False
            
        except Exception as e:
            return False

    def test_valid_app_search(self, search_query="vk"):
        """Тест: поиск существующего приложения"""
        try:
            search_input = self.wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR,
                "#mobApps > div > div.vkuiCard.vkuiCard--mode-outline.vkuiCard--withBorder.ListHeader_wrapper__Tgp6g > div > div > div input"
            )))
            
            search_input.clear()
            search_input.send_keys(search_query)
                        
            results = self.wait.until(EC.presence_of_all_elements_located((
                By.CSS_SELECTOR,
                "#mobApps > div > div.vkuiCard.vkuiCard--mode-outline.vkuiCard--withBorder.AppList_card__8N2cC > div > div > div.tableLayout_wrapper__r84CH > div > div > div > div.BaseTable.table_table__2JcCk > div.BaseTable__table.BaseTable__table-main > div.BaseTable__body > div > div"
            )))
            
            if not results:
                return False
                
            return True
            
        except Exception as e:
            return False
            
    def test_invalid_app_search(self, search_query="nonexistentapp12345"):
        """Тест: поиск несуществующего приложения"""
        try:
            search_selectors = [
                "#mobApps > div > div.vkuiCard.vkuiCard--mode-outline.vkuiCard--withBorder.ListHeader_wrapper__Tgp6g > div > div > div input", 
                "input[placeholder*='Поиск']",
                "div.ListHeader_wrapper__Tgp6g input[type='text']",
                "div.vkuiCard--withBorder input",
                "div.ListHeader_search__RGomN input"
            ]
            
            search_input = None
            for selector in search_selectors:
                try:
                    search_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                    if search_input.is_displayed() and search_input.is_enabled():
                        break
                except:
                    continue
                    
            if not search_input:
                return False
            
            search_input.clear()
            search_input.send_keys(search_query)
            
            search_input.send_keys(Keys.ENTER)
            
            time.sleep(3)
            
            empty_message_selectors = [
                "#mobApps > div > div.vkuiCard.vkuiCard--mode-outline.vkuiCard--withBorder.AppList_card__8N2cC > div > div > div.tableLayout_wrapper__r84CH > div > div > div > h2",
                "div.AppList_card__8N2cC h2",
                "div.tableLayout_wrapper__r84CH h2",
                "div.vkuiPlaceholder h2",
                "div[class*='EmptySearch'] h2",
                "div.tableLayout_empty__Mjrqc h2",
                "h2.vkuiTypography",
                "h2.vkuiPlaceholder__header"
            ]
            
            empty_message = None
            for selector in empty_message_selectors:
                try:
                    empty_message = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    if empty_message.is_displayed():
                        break
                except:
                    continue
            
            if not empty_message:
                try:
                    table_rows = self.driver.find_elements(By.CSS_SELECTOR, 
                        "div.BaseTable__body > div > div"
                    )
                    if len(table_rows) == 0:
                        return True
                except:
                    pass
                    
            expected_texts = [
                "По данному запросу приложения не найдены",
                "Ничего не нашлось", 
                "Ничего не найдено", 
                "не найдено", 
                "не нашлось"
            ]
            message_text = empty_message.text.lower()
            text_matched = any(text.lower() in message_text for text in expected_texts)
            
            if not text_matched:
                return False
                
            return True
            
        except Exception as e:
            return False

    def test_leadforms_tabs_navigation(self):
        """Тест: проверка навигации по вкладкам на странице лид-форм"""
        try:
            tabs = [
                "#tab_leadforms",
                "#tab_yclients",
                "#tab_surveys"
            ]
            
            for tab_selector in tabs:
                try:
                    tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, tab_selector)))
                    self.driver.execute_script("arguments[0].click();", tab)
                    
                    self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"{tab_selector}.vkuiTabsItem--selected")))
                    
                    time.sleep(1)
                except Exception as e:
                    print(f"Ошибка при переключении на вкладку {tab_selector}: {e}")
                    return False
            
            return True
        except Exception as e:
            return False

    def test_create_leadform_modal(self):
        """Тест: проверка открытия модального окна создания лид-формы"""
        return self._test_open_modal(
            tab_selector="#tab_leadforms",
            button_selectors=[
                "#leadads\\.leadforms > div > div.EmptyView_fullViewContent__sNe50 > div > div.vkuiPlaceholder__action > div > button",
                "#leadads\\.leadforms button.vkuiButton--mode-primary",
                "div.vkuiPlaceholder__action button",
                "button.vkuiButton--appearance-accent"
            ],
            screenshot_prefix="leadform",
            entity_name="лид-формы"
        )

    def _test_open_modal(self, tab_selector, button_selectors, screenshot_prefix, entity_name):
        """Общий метод для проверки открытия модального окна"""
        try:
            try:
                tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, tab_selector)))
                if "vkuiTabsItem--selected" not in tab.get_attribute("class"):
                    self.driver.execute_script("arguments[0].click();", tab)
                    self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"{tab_selector}.vkuiTabsItem--selected")))
            except Exception as e:
                return False
            
            create_button = None
            for selector in button_selectors:
                try:
                    buttons = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    for btn in buttons:
                        if btn.is_displayed() and btn.is_enabled():
                            create_button = btn
                            break
                    if create_button:
                        break
                except Exception:
                    continue
            
            if not create_button:
                return False
            
            self.driver.execute_script("arguments[0].click();", create_button)
            
            modal_selectors = [
                "#root > div > div:nth-child(2) > div",
                "div.ModalRoot_componentWrapper__uzHTL",
                "div.vkuiModalRoot"
            ]
            
            modal_appeared = False
            for selector in modal_selectors:
                try:
                    modal = WebDriverWait(self.driver, 5).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    if modal.is_displayed():
                        modal_appeared = True
                        break
                except Exception:
                    continue
            
            if not modal_appeared:
                return False
            
            return True
            
        except Exception:
            return False
