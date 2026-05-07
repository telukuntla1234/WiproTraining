import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
driver.get("https://www.google.com")
#implicit
driver.implicitly_wait(5)
search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("Selenium")

search_btn = driver.find_element(By.NAME,"btnK")
search_btn.click()

#explicit wait:
wait = WebDriverWait(driver,10)

search_box = wait.until(EC.visibility_of_element_located((By.NAME,"q")))
search_box.send_keys("Explicit wait!!")

google_btn = wait.until(EC.element_to_be_clickable((By.NAME,"btnK")))
google_btn.click()


wait = WebDriverWait(driver,timeout=10,poll_frequency=0.3,
                     ignored_exceptions=[NoSuchElementException])

search_box = wait.until(EC.visibility_of_element_located((By.NAME,"q")))
search_box.send_keys("Fluent wait !")

imfl_btn = wait.until(EC.element_to_be_clickable((By.NAME,"btnK")))
imfl_btn.click()


driver.quit()