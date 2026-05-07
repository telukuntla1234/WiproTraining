import pytest

from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage


def test_open_amazon(driver):
    assert "amazon" in driver.current_url, 'URL for amazon is not correct'
    print("\nOpened amazon homepage. Tile & URL verified. ")

@pytest.mark.parametrize("searchproduct", [
    ("wireless mouse"), ("shoes")

])
def test_search_product(driver,searchproduct):
    homepage = HomePage(driver)

    homepage.type_search_input_type(searchproduct)
    print(f"Searching product - {searchproduct}")
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded()  ,'Search results page did not load.'
    print(f"\nSearch results page loaded successfully - {searchproduct}")

@pytest.mark.parametrize("searchproduct", [
    ("wireless mouse"), ("shoes")

])
def test_find_elements(driver, searchproduct):
    homepage = HomePage(driver)

    homepage.type_search_input_type(searchproduct)
    print(f"Searching product - {searchproduct}")
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded(), 'Search results page did not load.'
    print(f"\nSearch results page loaded successfully - {searchproduct}")

    productlistingpage = ProductListingPage(driver)

    productlistingpage.find_product_tile()
    value = productlistingpage.all_products()

    assert value,"No products found on amazon search results!"

@pytest.mark.parametrize( ("searchproduct", "brandname"), [
    ("wireless mouse", 'Logitech'), ("shoes", 'Nike')

])

def test_brand_filter(driver, searchproduct, brandname):
    homepage = HomePage(driver)

    homepage.type_search_input_type(searchproduct)
    print(f"Searching product - {searchproduct}")
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded(), 'Search results page did not load.'
    print(f"\nSearch results page loaded successfully - {searchproduct}")

    productlistingpage = ProductListingPage(driver)

    productlistingpage.select_brand_filter(brandname)

    assert productlistingpage.check_product_titles_for_brand_filter(brandname), 'Brand Filter did not apply properly'

