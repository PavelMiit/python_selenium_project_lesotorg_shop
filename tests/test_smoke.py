from selenium import webdriver

from pages.filter_page import Filter_page
from pages.main_page import Main_page
from pages.product_page import Product_page


def test_smoke_product():
    driver = webdriver.Chrome()
    base_url = 'https://leso-torg.ru/'
    driver.get(base_url)
    driver.maximize_window()

    print("Старт теста")

    search_product = Main_page(driver)
    search_product.input_product_for_search()

    filter_page = Filter_page(driver)
    filter_page.use_filter_page()

    product_page = Product_page(driver)
    product_page.use_product_page()








