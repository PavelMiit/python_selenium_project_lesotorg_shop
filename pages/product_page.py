import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Product_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    # локаторы записываем в переменные
    name_product_on_product_page = "//h1[@id='pagetitle']"
    price_product_on_product_page = "(//span[@class='price_value'])[1]"
    add_to_cart_button = "//div[@id='bx_1213802087_98336_basket_actions']"
    cart_button = "(//a[@class='basket-link basket  with_price big  basket-count'])[1]"


    #Getters
    # находим элементы по локатору
    def get_name_product_on_product_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product_on_product_page)))

    def get_price_product_on_product_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_on_product_page)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))


    #Actions
    # что-то вводим или нажимаем кнопки
    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Добавили товар в корзину")
        # time.sleep(3)

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Нажали на кнопку Корзина")
        # time.sleep(3)


    #Methods
    # вызываем к выполнению
    def use_product_page(self):
        self.get_current_url() #получаем URL
        self.assert_word(self.get_name_product_on_product_page(), "Лопатка кулинарная рыбная 93-AK2C-11") #сравниваем название продукта на странице product page
        self.assert_price(self.get_price_product_on_product_page(), "120") #сравниваем цену продукта на странице product page
        self.click_add_to_cart_button() #добавлям товар в корзину
        self.click_cart_button() #нажимаем на кнопку корзина












