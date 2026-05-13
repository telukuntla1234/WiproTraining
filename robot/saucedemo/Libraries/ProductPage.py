from selenium.webdriver.common.by import By

class ProductPage:

    def __init__(self):
        pass

    def get_product_price_by_name(self, driver, product_name):

        products = driver.find_elements(By.CLASS_NAME, "inventory_item")

        for product in products:

            name = product.find_element(By.CLASS_NAME, "inventory_item_name").text

            if name == product_name:
                price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
                return float(price.replace("$", ""))

        return 0.0