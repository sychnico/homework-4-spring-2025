import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

TEST_URLS = {
    'pixels': "https://ads.vk.com/hq/pixels",
}

@pytest.fixture(scope="session")
def chrome_options():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--start-maximized')
    return options

@pytest.fixture(scope="session")
def session_driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(TEST_URLS['pixels'])
    import time
    time.sleep(30)
    yield driver
    driver.quit() 