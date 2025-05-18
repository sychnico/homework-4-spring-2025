import pytest
from selenium import webdriver
from ui.pages.audience_page import AudiencePage
from ui.pages.balance_page import BalancePage
from ui.pages.cases_page import CasesPage
from ui.pages.companies_page import CompaniesPage
from ui.pages.documents_page import DocumentsPage
from ui.pages.ecomm_page import EcommPage
from ui.pages.events_page import EventsPage
from ui.pages.insights_page import InsightsPage
from ui.pages.leadforms_page import LeadformsPage
from ui.pages.main_page import MainPage
from ui.pages.mobile_apps_page import MobileAppsPage
from ui.pages.news_page import NewsPage
from ui.pages.overview_page import OverwiewPage
from ui.pages.pixel_page import PixelPage

@pytest.fixture(scope='session')
def driver(config):
    url = config['url']
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    import time
    time.sleep(30)
    yield driver
    driver.quit()

@pytest.fixture
def audience_page(driver):
    driver.get(AudiencePage.URL)
    # wait(driver)
    return AudiencePage(driver=driver)

@pytest.fixture
def balance_page(driver):
    driver.get(BalancePage.URL)
    # wait(driver)
    return BalancePage(driver=driver)

@pytest.fixture
def cases_page(driver):
    driver.get(CasesPage.URL)
    return CasesPage(driver=driver)

@pytest.fixture
def companies_page(driver):
    driver.get(CompaniesPage.URL)
    return CompaniesPage(driver=driver)

@pytest.fixture
def documents_page(driver):
    driver.get(DocumentsPage.URL)
    return DocumentsPage(driver=driver)

@pytest.fixture
def insights_page(driver):
    driver.get(InsightsPage.URL)
    return InsightsPage(driver=driver)

@pytest.fixture
def ecomm_page(driver):
    return EcommPage(driver=driver)

@pytest.fixture
def events_page(driver):
    driver.get(EventsPage.URL)
    return EventsPage(driver=driver)

@pytest.fixture
def leadforms_page(driver):
    driver.get(LeadformsPage.URL)
    return LeadformsPage(driver=driver)

@pytest.fixture
def main_page(driver):
    driver.get(MainPage.URL)
    return MainPage(driver=driver)

@pytest.fixture
def mobile_apps_page(driver):
    driver.get(MobileAppsPage.URL)
    return MobileAppsPage(driver=driver)

@pytest.fixture
def news_page(driver):
    driver.get(NewsPage.URL)
    return NewsPage(driver=driver)

@pytest.fixture
def overview_page(driver):
    driver.get(OverwiewPage.URL)
    return OverwiewPage(driver=driver)

@pytest.fixture
def pixel_page(driver):
    driver.get(PixelPage.URL)
    return PixelPage(driver=driver)