import time
from pydoc import locate
from re import search


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))

driver.get("https://www.google.com")

# #ID
# driver.find_element(By.ID, "APjFqb").send_keys("selenium")
# time.sleep(3)
# driver.quit()

# #Name
# search_input = driver.find_element(By.NAME, "q").send_keys("locators")
# time.sleep(5)

# #Name
# google_search_button = driver.find_element(By.NAME, "btnK")
# google_search_button.click()
# time.sleep(30)

# #Classname
#
# imfl_button = driver.find_element(By.CLASS_NAME, "RNmpXc")
# imfl_button.click()
# time.sleep(3)
#

# #tagname
# href_elements = driver.find_elements(By.TAG_NAME, "a")
# for elmt in href_elements:
#     print(f'{elmt.text} - {elmt.get_attribute("href")}')

# #linktext
# images_link = driver.find_element(By.LINK_TEXT, "Images")
# images_link.click()
# time.sleep(10)

#Partial link text

# images_link = driver.find_element(By.PARTIAL_LINK_TEXT, "ma")
# images_link.click()
# time.sleep(10)

# #CSSsel
# search_input = driver.find_element(By.CSS_SELECTOR, "div > textarea")
# search_input.send_keys('selenium')
# time.sleep(5)

# #Xpath
#
# setting_text = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]')
# print(setting_text.text)
# time.sleep(3)
#

# driver.get("https://the-internet.herokuapp.com/tables")
#
# time.sleep(5)

'''#AND & OR expressions

and_example = driver.find_element(By.XPATH, "//td[text() = 'Tim' and @class= 'first-name']")
print(f"AND Example -> Found with both conditions : {and_example.text}")

or_example = driver.find_element(By.XPATH, "//td[text() = 'Tim' or text() = 'Frank']")
print(f"OR Example -> Found with OR condition : {or_example.text}")

rows= driver.find_elements(By.XPATH, "//table[@id = 'table1']/tbody/tr/td")
print(f"Child Exmaple -> Found {len(rows)} columns in the first table.")

email_cell = driver.find_element(By.XPATH, "//table[@id='table1']//td[text()='jdoe@hotmail.com']")
parent_row = driver.find_element(By.XPATH, "//table[@id = 'table1']//td[text()='jdoe@hotmail.com']/parent::tr")
print(f"Parent example -> email '{email_cell.text}' belongs to row with first name: "
      f"{parent_row.find_element(By.XPATH, './td[2]').text}")
'''
# #Ancestor - get the table element that is an ancestor of a cell
# ancestor_table = driver.find_element(By.XPATH, "//td[text() = 'jsmith@gmail.com']/ancestor::table")
# print(f"Ancestor Example -> Table ID : {ancestor_table.get_attribute('id')}")
#
# #Descendant - find all descendants (cells) under table body
# descendants = driver.find_elements(By.XPATH, "//table[@id = 'table1']/descendant::td")
# print(f"Descendant Example -> Found {len(descendants)} descendant cells.")


#RELATIVE LOCATOR

driver.get("https://www.saucedemo.com/")
time.sleep(3)

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login = driver.find_element(By.ID, "login-button")

#above
ele_above_password = driver.find_element(
    locate_with(By.TAG_NAME,"input").above(password))
print(f"Above eg -- text above password : {ele_above_password.get_attribute('placeholder')}")
ele_above_password.send_keys('standard_user')
time.sleep(3)

#below
ele_below_username = driver.find_element(
    locate_with(By.TAG_NAME,"input").below(username)
)
print(f"Below eg -- placeholder below username : {ele_below_username.get_attribute('placeholder')}")
ele_below_username.send_keys('secret_sauce')
time.sleep(3)
login.click()
time.sleep(2)

#right
twitter_ico = driver.find_element(By.LINK_TEXT, "Twitter")
facebbok_ico = driver.find_element(locate_with(By.TAG_NAME, "a").to_right_of(twitter_ico))
print(f"The right side of twitter icon is : {facebbok_ico.get_attribute('href')}")

#to left of
left_ico = driver.find_element(locate_with(By.TAG_NAME, "a").to_left_of(facebbok_ico))

#near
near_ico = driver.find_element(locate_with(By.TAG_NAME, "a").near(facebbok_ico))

print(f"Near element : {near_ico.get_attribute('href')}")
time.sleep(5)

driver.quit()














