from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

def test_link(src, link_str, assert_url):
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



def test_button_class(src, class_str, assert_url):
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


if __name__ == "__main__":
    url = "http://ads.vk.ru"
    test_link(url, "Новости", "news")
    test_link(url, "Кейсы", "cases")
    test_link(url, "Форум идей", "upvote")
    test_link(url, "Монетизация", "partner")
    test_link(url, "Справка", "help")
    test_link(url, "Регистрация", "auth")
    test_link(url, "Запустить рекламу", "auth")
    test_link(url, "Получить бонус", "firstbonus")
    test_link(url, "Открыть подборку", "podborka")
    test_link(url, "Смотреть все", "cases")
    test_button_class(url, "case_link__2bZoK", "cases")
    test_button_class(url, "getStarted_wrapper__gW_MK", "events")
    test_button_class(url, "news_wrapper__ieB6j", "news")
    test_link(url, "Полезные материалы", "insights")
    test_link(url, "Мероприятия", "events")
    test_link(url, "Документы", "documents")
    test_link(url, "Обучение для бизнеса", "expert")
    test_link(url, "Помощь", "help")

    url = "http://ads.vk.ru/news"
    test_button_class(url, "news-card_wrapper__n6fqN", "news/novyj")
    test_button_class(url, "vkuiPagination__page", "news?p=")

    url = "http://ads.vk.ru/insights"
    test_button_class(url, "insight-card_wrapper__YsQnM", "insights/reklama")
    test_button_class(url, "vkuiPagination__page", "?p=")

    url = "http://ads.vk.ru/events"
    test_button_class(url, "event-card_wrapper__GZkvu", "events/vybor")

    url = "http://ads.vk.ru/documents"
    test_button_class(url, "Link_wrapper__eHAEn", "documents/offer")

    url = "http://ads.vk.ru/cases"
    test_button_class(url, "case-card_wrapper__N1Mya", "cases/kak")
    test_button_class(url, "vkuiPagination__page", "?p=")