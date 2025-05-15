from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

def link_test(src, link_str, assert_url):
  options = Options()
  options.page_load_strategy = 'normal'
  driver = webdriver.Chrome(options=options)
  driver.get(src)

  try:
    elem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, link_str)))
    elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, link_str)))
    elem = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, link_str)))
    print("element is ready!")
  except TimeoutException:
    print("Loading took too much time!")
  elem = driver.find_element(By.LINK_TEXT, link_str)
  driver.execute_script("arguments[0].click();", elem)
  #elem.click()
  print("title: ", driver.title)

  p = driver.current_window_handle
  for w in driver.window_handles:
    if w != p:
        driver.switch_to.window(w)

  try:
    new_elem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "pages_gridRow__ymQy5")))
    print("Page is ready!")
  except TimeoutException:
    print("Loading took too much time!")

  print("new title: ", driver.title)
  assert assert_url in driver.current_url

  driver.close()



def button_class_test(src, class_str, assert_url):
  options = Options()
  options.page_load_strategy = 'normal'
  driver = webdriver.Chrome(options=options)
  driver.get(src)

  try:
    elem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, class_str)))
    elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, class_str)))
    elem = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, class_str)))
    print("element is ready!")
  except TimeoutException:
    print("Loading took too much time!")
  elem = driver.find_element(By.CLASS_NAME, class_str)
  driver.execute_script("arguments[0].click();", elem)
  #elem.click()
  print("title: ", driver.title)

  p = driver.current_window_handle
  for w in driver.window_handles:
    if w != p:
        driver.switch_to.window(w)

  try:
    new_elem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "pages_gridRow__ymQy5")))
    print("Page is ready!")
  except TimeoutException:
    print("Loading took too much time!")

  print("new title: ", driver.title)
  assert assert_url in driver.current_url

  driver.close()


def test_main_page():
    url = "http://ads.vk.ru"
    link_test(url, "Новости", "news")
    link_test(url, "Кейсы", "cases")
    #link_test(url, "Форум идей", "upvote") #не появляется при маленьком размере окна
    link_test(url, "Монетизация", "partner")
    #link_test(url, "Справка", "help") #то же самое
    link_test(url, "Регистрация", "auth")
    link_test(url, "Запустить рекламу", "auth")
    link_test(url, "Получить бонус", "firstbonus")
    link_test(url, "Открыть подборку", "podborka")
    link_test(url, "Смотреть все", "cases")
    button_class_test(url, "case_link__2bZoK", "cases")
    button_class_test(url, "getStarted_wrapper__gW_MK", "events")
    button_class_test(url, "news_wrapper__ieB6j", "news")
    link_test(url, "Полезные материалы", "insights")
    link_test(url, "Мероприятия", "events")
    link_test(url, "Документы", "documents")
    link_test(url, "Обучение для бизнеса", "expert")
    link_test(url, "Помощь", "help")

def test_events():
    url = "http://ads.vk.ru/events"
    button_class_test(url, "event-card_wrapper__GZkvu", "events/")

def test_documents():
    url = "http://ads.vk.ru/documents"
    button_class_test(url, "Link_wrapper__eHAEn", "documents/")

def test_cases():
    url = "http://ads.vk.ru/cases"
    button_class_test(url, "case-card_wrapper__N1Mya", "cases/")
    button_class_test(url, "vkuiPagination__page", "?p=")