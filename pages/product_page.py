
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Product_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    # локаторы записываем в переменныеее
    name_product_on_product_page = "//h1[@id='pagetitle']"
    price_product = "(//span[@class='price_value'])[1]"





    #Getters
    # находим элементы по локатору
    def get_name_product_on_product_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product_on_product_page))) #спарсили название товара со страницы продукты

    def get_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product)))




    #Actions
    # что-то вводим или нажимаем кнопки
    # def input_filter_price_min(self, price_min):
    #     self.get_filter_price_min().send_keys(price_min)
    #     print("Ввели минимальную стоимость товара: "+ price_min)



    #Methods
    # вызываем к выполнению
    def use_product_page(self):
        self.get_current_url()
        self.assert_word(self.get_name_product_on_product_page(), "Лопатка кулинарная рыбная 93-AK2C-11")
        self.assert_price(self.get_price_product(), "120")












