from time import sleep

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = input('what browser you want to use ?').lower()

match (browser):
    case 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    case 'edge':
        driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))

    case _:
        print('Enter VALID browser!!')

driver.get("https://www.google.com")

pagetitle = driver.title

if pagetitle == 'Google':
    print('Google homepage loaded - pass')
else:
    print('Google homepage not loaded - fail')

sleep(3)

driver.quit()