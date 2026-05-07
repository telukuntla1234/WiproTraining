
import pytest
import pytest_check as check
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait





@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https:/www.google.com')
    yield driver
    driver.quit()

def test_ghpload(driver):
    pagetitle = driver.title
    assert pagetitle == 'Google' , 'Google home page loaded'

def test_imagespageload(driver):
    driver.find_element(By.LINK_TEXT, 'Images').click()
    pagetitle = driver.title
    assert  pagetitle == 'Google Images', 'Images Page Not loaded'

def test_businessLink(driver):
    driver.find_element(By.LINK_TEXT, 'Business').click()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.title_contains('Business'))
    # assert 'Business' in driver.title, 'Business page not loaded - Title check'
    # assert 'business' in driver.current_url, 'Business page not loaded - URL check'

    check.is_true('Business',driver.title, 'Business page not loaded - Title check')
    check.is_in('business', driver.current_url, 'Business page not loaded - URL check')
